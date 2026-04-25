# Soc Ops Design System & Development Guide

## Project Overview

**Soc Ops** is a minimalist social bingo game built with FastAPI, Jinja2, and HTMX. The design emphasizes warmth, ease of connection, and refined minimalism. All styling is CSS-only (no frameworks) for clean, performant code.

---

## 🎨 Design System

### Philosophy
The design embodies **Scandinavian Calm** meets **Desert Sand Minimal**—warm, accessible, spacious, and intentional. Every color, font choice, and space serves the goal of making real human connection feel natural and effortless.

### Color Palette

```css
/* Primary Sand Tones (Warm Neutrals) */
--sand-50:    #faf8f4    /* Lightest background */
--sand-100:   #f5f1eb    /* Subtle backgrounds */
--sand-200:   #ebe5dd    /* Borders, dividers */
--sand-300:   #d9cfc3    /* Secondary borders */
--sand-400:   #c2b5a3    /* Text accents */
--sand-500:   #a89277    /* Muted text */
--sand-600:   #8b755d    /* Secondary text */
--cream:      #fdfbf7    /* Card backgrounds */
--off-white:  #f9f7f3    /* Subtle variations */

/* Accent - Warm Clay/Terracotta */
--accent-warm:       #c9825c    /* Primary buttons, titles */
--accent-warm-light: #d99368    /* Hover state */
--accent-warm-dark:  #a86a47    /* Active state */

/* Semantic Colors */
--success:           #8b9d7e    /* Marked squares, confirmations */
--success-light:     #a4b396    /* Hover for success states */
--success-bg:        #f0f4ed    /* Success background */

/* Text Hierarchy */
--text-primary:      #3a3530    /* Headings, important text */
--text-secondary:    #6b6460    /* Body copy */
--text-tertiary:     #8b8580    /* Hints, secondary info */
--border:            #dcd5cc    /* Borders, dividers */
--subtle-bg:         #f5f1eb    /* Backgrounds */
```

### Typography

**Fonts:**
- **Body text:** `Georgia`, `Garamond`, serif (1.6 line-height)
- **Headings/UI:** `system-ui`, `-apple-system`, sans-serif (letter-spacing: -0.3px)

**Scale:**
```
xs:  0.75rem    (12px)
sm:  0.875rem   (14px)
base: 1rem      (16px)
lg:  1.125rem   (18px)
3xl: 1.875rem   (30px)
4xl: 2.25rem    (36px)
5xl: 3rem       (48px)
```

**Weight Guidance:**
- UI buttons/labels: 500 (medium)
- Headings: 600-700
- Body copy: 400 (normal)
- Disabled/hints: 400

---

## 🏗️ Component Patterns

### Buttons

```html
<!-- Primary Action -->
<button class="btn-primary">Start Game</button>

<!-- Secondary Action -->
<button class="btn-secondary">← Back</button>
```

**Primary Button Behavior:**
- Default: Clay terracotta background with soft shadow
- Hover: Slightly lighter shade
- Active: Darker shade with reduced shadow
- All with 180ms smooth transition

### Cards

```html
<!-- Card Container -->
<div class="card">
  <h2>Title</h2>
  <p>Content</p>
</div>

<!-- Card with Interior Content -->
<div class="card card-content">
  <!-- Nested content with padding -->
</div>
```

**Style:** 
- Cream background with subtle border
- Soft shadow (2px blur, very light)
- 1.5rem padding
- Rounded corners (0.75rem)

### Bingo Board

```html
<div class="grid grid-cols-5 gap-1 aspect-square">
  <!-- Each square is a button with .bingo-square class -->
</div>
```

**Square States:**
- **Default:** Cream background, sand border
- **Hover:** Subtle sand-50 background shift
- **Marked:** Success-bg with success border and checkmark
- **Winning:** Clay accent background with inset border, darker text
- **Free Space:** Disabled button (no hover)

### Modals

```html
<div class="modal-overlay">
  <div class="modal-content">
    <div class="modal-emoji">🎉</div>
    <h2 class="modal-title">BINGO!</h2>
    <p class="modal-text">Message</p>
    <button class="btn-primary">Action</button>
  </div>
</div>
```

**Overlay:** Semi-transparent dark backdrop with 2px blur
**Content:** Scale-in animation (0.4s cubic-bezier)
**Emoji:** Float animation (0.6s ease-in-out)

---

## 📐 Spacing & Layout

### Padding Scale
```
0.25rem (p-1)
0.75rem (p-3)
1rem    (p-4)
1.25rem (p-5)
1.5rem  (p-6)
2rem    (p-8)
```

### Common Layouts

**Full-Height Container (Start Screen):**
```html
<div class="flex flex-col items-center justify-center min-h-full p-6 bg-white">
  <div class="text-center max-w-sm">
    <!-- Content -->
  </div>
</div>
```

**Game Screen with Header & Board:**
```html
<div class="flex flex-col min-h-full bg-white">
  <header><!-- --></header>
  <div class="flex-1 flex items-center justify-center p-6">
    <!-- Board -->
  </div>
</div>
```

### Responsive Breakpoints
Mobile-first approach. CSS includes `@media (max-width: 640px)` adjustments for type sizing and board spacing.

---

## ✨ Animations & Transitions

- **Default transition:** 150ms cubic-bezier(0.4, 0, 0.2, 1)
- **Modal entrance:** 400ms scale-in animation
- **Float effect:** 600ms ease-in-out vertical movement
- **All transitions smooth:** Prefer cubic-bezier for natural feel

**Avoid jarring animations.** Scandinavian design favors calm, purposeful motion.

---

## 🎯 When Adding New Features

### New Components
1. Define colors as CSS variables (reuse palette)
2. Use existing spacing utilities
3. Test on mobile first
4. Ensure sufficient contrast (WCAG compliance)
5. Add soft shadows (not harsh)
6. Use rounded corners (0.5rem minimum)

### New Colors
- Don't introduce new hues
- Use existing palette or desaturate new colors to match tone
- Maintain warm, earthy feel

### Typography
- Serif for body/flavor text
- Sans for UI/headings
- Max line-length ~50-60 characters for readability

### States & Feedback
- Use success color (#8b9d7e) for positive feedback
- Use accent-warm for primary actions
- Provide hover/active states for all interactive elements
- Include disabled states (muted colors, no cursor)

---

## 🚀 Development Best Practices

### HTML Structure
- Use semantic class names (`.btn-primary`, `.bingo-square`, `.modal-overlay`)
- Avoid inline styles
- Leverage CSS variables for theming
- Include ARIA labels for accessibility

### CSS Organization
```
1. CSS Variables (color system)
2. Global resets & body styles
3. Typography & hierarchy
4. Layout utilities
5. Component styles
6. State patterns (hover, active, disabled)
7. Animations & transitions
8. Responsive utilities
```

### Jinja2 Templates
- Use class composition for reusable styles
- Keep markup clean and semantic
- Conditionally apply classes (e.g., `.marked`, `.winning`)
- Use HTMX attributes for interactivity (not inline JavaScript)

### Testing CSS Changes
```bash
# After CSS edits, verify:
uv run pytest                    # Functionality intact
# Then manually check:
# - Desktop view
# - Mobile view (landscape & portrait)
# - Dark mode (if testing cross-browser)
# - Touch interactions on actual device
```

---

## 📋 Common Tasks

### Adding a New Button Style
```css
.btn-tertiary {
  padding: 0.875rem 1.25rem;
  background-color: transparent;
  border: 2px solid var(--accent-warm);
  color: var(--text-accent);
  font-weight: 500;
  border-radius: 0.5rem;
}

.btn-tertiary:hover {
  background-color: var(--sand-50);
}
```

### Adding a New Card Variant
```css
.card-alert {
  background-color: #f0f4ed;
  border-left: 4px solid var(--success);
  padding: 1rem;
}
```

### Adjusting Spacing
- Use existing scale (0.25, 0.5, 0.75, 1, 1.25, 1.5, 2 rem)
- Maintain breathing room
- Match surrounding elements
- Test on mobile (avoid too-large gaps on small screens)

---

## 🔍 Design Principles to Remember

1. **Warmth over coldness** — Use warm neutrals, avoid harsh grays/blacks
2. **Spaciousness** — Generous padding/margins; never feels cramped
3. **Intentionality** — Every visual choice serves the social mission
4. **Minimalism** — Remove decorative elements; use negative space
5. **Accessibility** — Sufficient contrast, readable sizes, clear states
6. **Performance** — CSS-only, no heavy frameworks or animations
7. **Human-first** — Design for real social connection, not tech spectacle

---

## 📚 File Reference

- **CSS:** `/app/static/css/app.css` (~650 lines, well-organized)
- **Start Screen:** `/app/templates/components/start_screen.html`
- **Game Screen:** `/app/templates/components/game_screen.html`
- **Board:** `/app/templates/components/bingo_board.html`
- **Modal:** `/app/templates/components/bingo_modal.html`

---

## ✅ Checklist for Design Reviews

- [ ] Colors match palette (using CSS variables)
- [ ] Typography hierarchy is clear
- [ ] Spacing is generous and consistent
- [ ] Interactive elements have hover/active states
- [ ] Mobile layout is tested and responsive
- [ ] Animations are smooth (150-400ms range)
- [ ] No orphaned inline styles
- [ ] ARIA labels on interactive elements
- [ ] Sufficient color contrast for accessibility
- [ ] Warm, inviting feel maintained
