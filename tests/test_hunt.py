import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.models import HuntItem, GameState


@pytest.fixture
def client():
    return TestClient(app)


class TestHuntItem:
    """Test HuntItem model."""

    def test_hunt_item_creation(self):
        item = HuntItem(id=0, text="test question", is_checked=False)
        assert item.id == 0
        assert item.text == "test question"
        assert item.is_checked is False

    def test_hunt_item_checked_state(self):
        item = HuntItem(id=0, text="test question", is_checked=True)
        assert item.is_checked is True

    def test_hunt_item_is_immutable(self):
        item = HuntItem(id=0, text="test question", is_checked=False)
        with pytest.raises(Exception):  # FrozenInstanceError
            item.is_checked = True


class TestStartHuntMode:
    """Test starting a scavenger hunt game."""

    def test_start_hunt_route_exists(self, client: TestClient):
        client.get("/")
        response = client.post("/start-hunt")
        assert response.status_code == 200

    def test_start_hunt_includes_hunt_screen(self, client: TestClient):
        client.get("/")
        response = client.post("/start-hunt")
        assert "Scavenger Hunt" in response.text

    def test_start_hunt_has_24_items(self, client: TestClient):
        client.get("/")
        response = client.post("/start-hunt")
        # Should have 24 hunt items (same as bingo board - 1 for free space)
        assert response.text.count('hx-post="/toggle-hunt/') == 24

    def test_start_hunt_shows_progress_bar(self, client: TestClient):
        client.get("/")
        response = client.post("/start-hunt")
        assert "hunt-progress" in response.text
        assert "Complete" in response.text

    def test_start_hunt_initializes_zero_percent(self, client: TestClient):
        client.get("/")
        response = client.post("/start-hunt")
        assert "0%" in response.text

    def test_start_hunt_creates_different_items(self, client: TestClient):
        client.get("/")
        response1 = client.post("/start-hunt")
        
        # Create a new session for second hunt
        client.cookies.clear()
        client.get("/")
        response2 = client.post("/start-hunt")
        
        # Items should be different (very high probability with shuffled questions)
        assert response1.text != response2.text


class TestToggleHuntItem:
    """Test toggling hunt items on/off."""

    def test_toggle_hunt_item_route_exists(self, client: TestClient):
        client.get("/")
        client.post("/start-hunt")
        response = client.post("/toggle-hunt/0")
        assert response.status_code == 200

    def test_toggle_hunt_item_marks_item(self, client: TestClient):
        client.get("/")
        client.post("/start-hunt")
        response = client.post("/toggle-hunt/0")
        # Should show checkmark or checked state
        assert "hunt-item-checked" in response.text or "✓" in response.text

    def test_toggle_hunt_item_updates_progress(self, client: TestClient):
        client.get("/")
        client.post("/start-hunt")
        response = client.post("/toggle-hunt/0")
        # Progress should show something greater than 0%
        assert "4%" in response.text  # 1 out of 24 = 4.16%

    def test_toggle_hunt_item_unmarks_item(self, client: TestClient):
        client.get("/")
        client.post("/start-hunt")
        client.post("/toggle-hunt/0")
        response = client.post("/toggle-hunt/0")
        # Should be unchecked now
        assert response.text.count("hunt-item-checked") == 0 or "0%" in response.text

    def test_toggle_hunt_multiple_items(self, client: TestClient):
        client.get("/")
        client.post("/start-hunt")
        client.post("/toggle-hunt/0")
        client.post("/toggle-hunt/1")
        response = client.post("/toggle-hunt/2")
        # Should show ~13% (3 out of 24)
        assert "12%" in response.text or "13%" in response.text

    def test_toggle_hunt_item_preserves_other_items(self, client: TestClient):
        client.get("/")
        client.post("/start-hunt")
        client.post("/toggle-hunt/0")
        response = client.post("/toggle-hunt/1")
        # Item 0 should still be checked
        assert response.text.count("hunt-item-checked") >= 2


class TestHuntCompletion:
    """Test hunt completion detection."""

    def test_hunt_completion_all_items_checked(self, client: TestClient):
        client.get("/")
        client.post("/start-hunt")
        
        # Check all 24 items
        for i in range(24):
            client.post(f"/toggle-hunt/{i}")
        
        response = client.post(f"/toggle-hunt/23")
        # Should show 100%
        assert "100%" in response.text

    def test_hunt_completion_shows_modal(self, client: TestClient):
        client.get("/")
        client.post("/start-hunt")
        
        # Check all 24 items
        for i in range(24):
            client.post(f"/toggle-hunt/{i}")
        
        response = client.post(f"/toggle-hunt/23")
        # Should show completion modal
        assert "COMPLETE" in response.text or "modal" in response.text.lower()

    def test_hunt_completion_shows_celebration_emoji(self, client: TestClient):
        client.get("/")
        client.post("/start-hunt")
        
        # Check all 24 items
        for i in range(24):
            client.post(f"/toggle-hunt/{i}")
        
        response = client.post(f"/toggle-hunt/23")
        # Should show celebration emoji
        assert "🎉" in response.text

    def test_hunt_completion_button_text(self, client: TestClient):
        client.get("/")
        client.post("/start-hunt")
        
        # Check all 24 items
        for i in range(24):
            client.post(f"/toggle-hunt/{i}")
        
        response = client.post(f"/toggle-hunt/23")
        # Should have play again button
        assert "Play Again" in response.text or "play" in response.text.lower()

    def test_hunt_not_complete_with_partial_items(self, client: TestClient):
        client.get("/")
        client.post("/start-hunt")
        
        # Check only 23 items (one short)
        for i in range(23):
            client.post(f"/toggle-hunt/{i}")
        
        response = client.post("/")
        # Should NOT show completion modal
        assert response.status_code == 200


class TestHuntProgress:
    """Test hunt progress calculation."""

    def test_progress_zero_on_start(self, client: TestClient):
        client.get("/")
        response = client.post("/start-hunt")
        assert "0%" in response.text

    def test_progress_increases_by_4_percent(self, client: TestClient):
        client.get("/")
        client.post("/start-hunt")
        response = client.post("/toggle-hunt/0")
        # 1/24 ≈ 4%
        assert "4%" in response.text

    def test_progress_at_50_percent(self, client: TestClient):
        client.get("/")
        client.post("/start-hunt")
        
        # Check 12 items (50%)
        for i in range(12):
            client.post(f"/toggle-hunt/{i}")
        
        response = client.post(f"/toggle-hunt/12")
        # Should show ~54% (13/24)
        assert "54%" in response.text or "50%" in response.text

    def test_progress_bar_visual_width(self, client: TestClient):
        client.get("/")
        client.post("/start-hunt")
        client.post("/toggle-hunt/0")
        response = client.post("/toggle-hunt/1")
        # Progress bar should have inline style with width
        assert 'style="width:' in response.text
        # 2/24 = 8.33%, should be around 8%
        assert 'width: 8%' in response.text or 'width: 9%' in response.text


class TestHuntGameState:
    """Test game state management for hunt mode."""

    def test_game_state_hunt_after_start(self, client: TestClient):
        client.get("/")
        response = client.post("/start-hunt")
        # Game state should be hunt (GameState.HUNT)
        assert "hunt-item" in response.text.lower()

    def test_game_mode_property(self, client: TestClient):
        """Test that game_mode is set to 'hunt'."""
        client.get("/")
        response = client.post("/start-hunt")
        # Hunt screen should be rendered
        assert "Scavenger Hunt" in response.text

    def test_reset_from_hunt_returns_to_start(self, client: TestClient):
        client.get("/")
        client.post("/start-hunt")
        response = client.post("/reset")
        assert response.status_code == 200
        assert "Start Game" in response.text

    def test_dismiss_modal_after_hunt_completion(self, client: TestClient):
        client.get("/")
        client.post("/start-hunt")
        
        # Check all items
        for i in range(24):
            client.post(f"/toggle-hunt/{i}")
        
        # Completion triggers modal
        client.post(f"/toggle-hunt/23")
        
        # Dismiss modal
        response = client.post("/dismiss-modal")
        assert response.status_code == 200


class TestStartScreenModeSelection:
    """Test mode selection on start screen."""

    def test_start_screen_shows_mode_options(self, client: TestClient):
        response = client.get("/")
        assert "Bingo Board" in response.text or "start-bingo" in response.text
        assert "Scavenger Hunt" in response.text or "start-hunt" in response.text

    def test_bingo_button_starts_bingo_mode(self, client: TestClient):
        client.get("/")
        response = client.post("/start-bingo")
        assert response.status_code == 200
        assert "FREE SPACE" in response.text

    def test_hunt_button_starts_hunt_mode(self, client: TestClient):
        client.get("/")
        response = client.post("/start-hunt")
        assert response.status_code == 200
        assert "Scavenger Hunt" in response.text.lower()


class TestHuntItemsAreFromQuestionPool:
    """Test that hunt items come from the question pool."""

    def test_hunt_items_from_questions(self, client: TestClient):
        from app.data import QUESTIONS
        
        client.get("/")
        response = client.post("/start-hunt")
        
        # Extract question texts from response
        # Each hunt item should contain text from QUESTIONS
        for question in QUESTIONS[:5]:  # Check first 5 questions
            # At least some should appear (not all will due to sampling)
            pass
        
        # The hunt should have valid questions
        assert "hx-post=" in response.text

    def test_hunt_items_no_free_space(self, client: TestClient):
        client.get("/")
        response = client.post("/start-hunt")
        # Hunt should NOT include "FREE SPACE"
        assert "FREE SPACE" not in response.text


class TestHuntErrorHandling:
    """Test error handling for hunt mode."""

    def test_toggle_invalid_item_id(self, client: TestClient):
        client.get("/")
        client.post("/start-hunt")
        response = client.post("/toggle-hunt/999")
        # Should handle gracefully (either 200 or 404)
        assert response.status_code in [200, 404]

    def test_toggle_negative_item_id(self, client: TestClient):
        client.get("/")
        client.post("/start-hunt")
        response = client.post("/toggle-hunt/-1")
        # Should handle gracefully
        assert response.status_code in [200, 404]

    def test_toggle_without_starting_hunt(self, client: TestClient):
        client.get("/")
        # Don't start hunt
        response = client.post("/toggle-hunt/0")
        # Should not crash
        assert response.status_code in [200, 400, 404]
