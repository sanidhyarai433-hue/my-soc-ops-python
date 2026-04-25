🌐 [Português (BR)](README.pt_BR.md) | [Español](README.es.md)

<div align="center">

# 🎲 Soc Ops

### The Social Bingo Game That Brings People Together

**Break the ice, find your people, and win—all while making genuine connections at mixers and events.**

[🚀 Quick Start](#quick-start) • [✨ Features](#features) • [📚 Learn](#learn-by-doing) • [🛠️ Tech Stack](#tech-stack)

</div>

---

## What is Soc Ops?

Soc Ops is a **real-time bingo game** designed for in-person mixers, conferences, and team events. Players circulate through the room finding **real people who match printed bingo questions**, then mark them on a digital board. First to get 5 in a row wins—and everyone wins by meeting new connections.

**Key Insight:** Traditional icebreakers are awkward. Soc Ops gives people a *mission* and *mutual benefit*, turning networking from uncomfortable to natural.

---

## ✨ Key Features

- **🎯 Interactive Bingo Board** — Dynamic 5×5 grid with center free space, refreshes for each game
- **👥 Real-Time Sessions** — Cookie-based session management; start playing immediately
- **💯 Question Pool** — Curated questions designed to spark genuine human connection
- **✅ Win Detection** — Automatically detects row, column, and diagonal wins with celebration modal
- **📱 Responsive Design** — Works seamlessly on mobile and desktop devices
- **🔄 HTMX Integration** — Instant feedback without page reloads; smooth interactive experience

---

## 🚀 Quick Start

### Prerequisites
- **Python 3.13+** 
- **UV** (Python package manager)

### Setup (2 minutes)
```bash
# Clone and navigate
git clone https://github.com/sanidhyarai433-hue/my-soc-ops-python
cd my-soc-ops-python

# Sync dependencies
uv sync

# Run the dev server
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Open **http://localhost:8000** in your browser. Start playing! 🎮

### Development Checklist
```bash
uv run ruff check .                           # Lint (strict type hints)
uv run pytest                                 # Test (25 tests, always green)
uv run uvicorn app.main:app --reload          # Dev server (hot reload)
```

---

## 🏗️ Project Structure

```
soc-ops/
├── app/
│   ├── main.py                 # FastAPI routes & entry point
│   ├── game_service.py         # Session management
│   ├── game_logic.py           # Bingo grid generation & win detection
│   ├── models.py               # Pydantic data models
│   ├── data.py                 # Question pool
│   ├── templates/              # Jinja2 templates
│   │   ├── base.html
│   │   ├── home.html
│   │   └── components/
│   └── static/                 # CSS & HTMX JS
├── tests/                      # 25 comprehensive tests
├── workshop/                   # Multi-part learning guides
└── pyproject.toml              # Dependencies & config
```

---

## 📚 Learn By Doing

This project includes a **structured workshop** with 5 learning modules, each with hands-on coding:

| Module | Focus | Learn |
|--------|-------|-------|
| **00** | [Overview & Setup](workshop/00-overview.md) | Project architecture & environment setup |
| **01** | [Context Engineering](workshop/01-setup.md) | Building effective AI prompts & instructions |
| **02** | [Design-First Frontend](workshop/02-design.md) | Iterative frontend with AI assistance |
| **03** | [Custom Quiz Master](workshop/03-quiz-master.md) | Adding multi-agent AI capabilities |
| **04** | [Multi-Agent Dev](workshop/04-multi-agent.md) | Advanced agent orchestration patterns |
| **05** | [Complete Solution](workshop/05-complete.md) | Full production-ready implementation |

👉 **Start here:** [Workshop Guide](workshop/GUIDE.md)  
📖 **Online docs:** [Full Lab Guide](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=00-overview)

---

## 🛠️ Tech Stack

| Layer | Technology | Why |
|-------|-----------|-----|
| **Backend** | FastAPI | Fast, modern async Python web framework |
| **Frontend** | Jinja2 + HTMX | Template-driven, interactive without JS complexity |
| **Styling** | CSS3 | Clean, performant, no framework overhead |
| **Testing** | pytest | Comprehensive test coverage (25 tests) |
| **Linting** | Ruff | Enforces type hints, modern Python, zero unsused imports |
| **Dev** | UV + Uvicorn | Lightning-fast Python package management & serving |

---

## 🎮 How to Play

1. **Enter a mixer event** — Get a physical printout of the bingo board questions
2. **Start the game** — Open Soc Ops on your phone and hit "Start Game"
3. **Find people** — Walk around and find real people matching each question:
   - _"Has been to 3+ countries"_ → Find someone, mark the square ✓
   - _"Works in a creative field"_ → Found one! Mark it ✓
4. **Get 5 in a row** — Horizontal, vertical, or diagonal wins 🎉
5. **Celebrate** — Winner announced with fanfare; everyone else keeps playing

---

## 🧪 Quality Assurance

✅ **25 automated tests** covering:
- API endpoints (responses, status codes, content)
- Game logic (bingo detection, square marking, board generation)
- Session management

Run tests anytime:
```bash
uv run pytest -v
```

Linting enforces:
- ✓ Type hints on all functions
- ✓ No unused imports or variables  
- ✓ Modern Python syntax
- ✓ PEP 8 naming conventions

---

## 📖 What You'll Build

By completing the workshop modules, you'll have hands-on experience with:
- ✅ FastAPI backend development
- ✅ Jinja2 templating for dynamic HTML
- ✅ HTMX for interactive UIs without frontend frameworks
- ✅ AI-assisted development workflow
- ✅ Multi-agent systems and orchestration
- ✅ Test-driven development
- ✅ Professional Python code practices

---

## 🤝 Contributing

We welcome contributions! Check out [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Code of Conduct
Please review our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

### Security
For security concerns, see [SECURITY.md](SECURITY.md).

---

## 📄 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

---

## 🙌 Support

- **Questions?** Check [SUPPORT.md](SUPPORT.md)
- **Found a bug?** Open a GitHub issue
- **Have an idea?** We'd love to hear it!

---

<div align="center">

**Made with ❤️ to make networking memorable**

[⭐ Star us on GitHub](https://github.com/sanidhyarai433-hue/my-soc-ops-python) • [📢 Share the project](#)

</div>
