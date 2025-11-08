# Study Buddy AI

A systematic AI tutor built using Google Agent Development Kit (ADK) that helps students master their exam subjects through structured learning and assessment.

## 🎯 How It Works

The Study Buddy AI follows a proven educational methodology:

1. **Get to Know Student**: Collects grade level, subject, and learning goals
2. **Research Subject**: Analyzes curriculum and identifies key concepts  
3. **Create Study Plan**: Divides subject into logical, sequential sections
4. **Iterative Learning Loop**: For each section:
   - 📖 **Teach** concepts with explanations and examples
   - 🧪 **Quiz** to test understanding
   - 📊 **Assess** performance and identify gaps
   - 🔄 **Re-teach** weak areas before moving forward

## ✨ Features

- 🤖 **AI-Powered Tutoring**: Uses Google ADK with advanced language models
- 📚 **Subject Research**: Automatic curriculum analysis and content structuring
- 🎯 **Personalized Learning**: Adapts to student's grade level and pace
- 📋 **Structured Study Plans**: Breaks complex subjects into manageable sections
- 🧪 **Interactive Quizzing**: Tests understanding before progressing
- 💡 **Mastery-Based**: Won't move forward until concepts are understood
- 🎓 **Grade-Appropriate**: Content complexity matches student level

## Setup

### Prerequisites

- Python 3.9+
- UV package manager

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd study-buddy-ai
```

2. Create and activate virtual environment:
```bash
uv venv
source .venv/bin/activate  # On macOS/Linux
```

3. Install dependencies:
```bash
uv add google-adk python-dotenv
uv add --dev pytest black isort flake8 mypy
uv sync
```

## 🚀 Usage

### Running the Main Tutor Agent

```bash
uv run python agent.py
```

### Using Individual Agents

```bash
# Import and use specific agents in Python
from agents.studyplan_agent import studyplan_agent
from agent import root_agent
```

## 📁 Project Structure

```
study-buddy-ai/
├── agent.py                          # Main root tutor agent
├── agents/                           # Specialized agent modules  
│   └── studyplan_agent.py           # Subject research & study planning
├── tools/                           # Reusable tool functions
│   ├── __init__.py                  # Package initialization
│   └── studyplan_agent_tools.py     # Study plan creation tools
├── pyproject.toml                   # UV project configuration
├── .gitignore                       # Git ignore patterns
├── .venv/                          # Virtual environment (auto-created)
└── README.md                       # This documentation
```

### 🔧 Agent Architecture

- **Root Agent** (`agent.py`): Main tutor that orchestrates the learning process
- **StudyPlan Agent** (`agents/studyplan_agent.py`): Researches subjects and creates structured learning plans
- **Tools** (`tools/`): Shared functionality used by multiple agents

### 🛠 Key Tools

- `quick_subject_research`: Analyzes curriculum and identifies key concepts
- `divide_into_study_sections`: Creates logical, sequential learning modules
- Additional tools for teaching, quizzing, and assessment (in main agent)

## 🛠 Development

### Installing Development Dependencies

Development tools are automatically included when you run:
```bash
uv sync
```

### Code Quality Tools

```bash
# Format code
uv run black .
uv run isort .

# Type checking  
uv run mypy agent.py

# Linting
uv run flake8 .

# Run tests
uv run pytest
```

### Adding New Tools

1. Create tool functions in `tools/` directory
2. Add imports to `tools/__init__.py` 
3. Import and use in your agents

### Creating New Agents

1. Create agent file in `agents/` directory
2. Import required tools from `tools/`
3. Define agent with Google ADK Agent class

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root for configuration:

```bash
# Google ADK Configuration (if needed)
GOOGLE_APPLICATION_CREDENTIALS=path/to/your/service-account.json
GOOGLE_CLOUD_PROJECT=your-project-id

# Development settings
DEBUG=True
LOG_LEVEL=INFO
```

### Agent Configuration

Agents are configured in their respective files:
- Model selection (e.g., `gemini-2.0-flash-exp`)
- System instructions and behavior
- Tool assignments

## 🎓 Educational Methodology

The Study Buddy AI implements proven educational principles:

- **Mastery Learning**: Students must demonstrate understanding before advancing
- **Scaffolded Learning**: Complex topics broken into manageable chunks  
- **Formative Assessment**: Continuous feedback through quizzes and checks
- **Personalized Pacing**: Adapts to individual student needs and timeline
- **Metacognitive Support**: Helps students understand how they learn best

## 📚 Supported Subjects

The system can tutor students in any subject by:
- Researching curriculum standards for the grade level
- Identifying key concepts and learning objectives
- Creating appropriate explanations and examples
- Generating relevant quiz questions

Common subjects include:
- **Mathematics**: Algebra, Geometry, Calculus, Statistics
- **Sciences**: Biology, Chemistry, Physics, Earth Science  
- **Languages**: English, Literature, Foreign Languages
- **Social Studies**: History, Geography, Government, Economics
- **And many more**: The system adapts to any academic subject

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## License

This project is for educational purposes.