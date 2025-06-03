# Web UI - AI Personal Assistant Suite

A modular Gradio-based web interface that provides unified access to all three AI systems: Personal RAG, Web Search Agent, and Hybrid RAG.

## 📁 Structure

```
web_rag_ui/
├── app.py                      # Main application launcher
├── components/                 # UI components (Gradio tabs)
│   ├── __init__.py
│   ├── personal_rag_tab.py     # Personal RAG interface
│   ├── web_search_tab.py       # Web search interface
│   ├── hybrid_rag_tab.py       # Hybrid RAG interface
│   └── comparison_tab.py       # System comparison interface
├── services/                   # Business logic layer
│   ├── __init__.py
│   ├── ai_assistant.py         # Main service coordinator
│   ├── personal_rag_service.py # Personal RAG wrapper
│   ├── web_search_service.py   # Web search wrapper
│   └── hybrid_rag_service.py   # Hybrid RAG wrapper
└── README.md                   # This file
```

## 🎯 Design Principles

### Modular Architecture
- **Separation of Concerns**: UI components separated from business logic
- **Reusable Services**: Service layer can be used by CLI, API, or other interfaces
- **Single Responsibility**: Each file has one clear purpose
- **Easy Testing**: Components and services can be tested independently

### File Size Management
- **Small Files**: Each file is 30-80 lines (vs 300+ monolithic file)
- **Focused Components**: Each tab component handles one system
- **Lightweight Services**: Service wrappers are thin and focused

## 🚀 Usage

### Quick Start

```bash
# From project root
cd web-ui
python app.py
```

Then open your browser to `http://localhost:7860`

### Development Setup

```bash
# Install dependencies (if not already installed)
pip install gradio

# Run in development mode
python app.py
```

## 🏗 Architecture

### Service Layer Pattern

The web UI uses a clean service layer pattern:

```
UI Layer (Gradio Components)
     ↓
Service Layer (Business Logic)
     ↓
System Layer (Original AI Systems)
```

### Component Structure

Each UI component follows the same pattern:

```python
def create_[system]_tab(assistant_service):
    """Create the [System] tab interface"""
    
    def safe_query(query: str) -> Tuple[str, str]:
        # Input validation and error handling
        
    with gr.TabItem("[System Name]"):
        # UI layout
        # Example questions
        # Event handlers
```

### Service Structure

Each service wrapper provides a consistent interface:

```python
class [System]Service:
    def __init__(self, ...):
        # Initialize the underlying system
        
    def query(self, query: str) -> Tuple[str, str]:
        # Execute query and return (answer, sources)
        
    def is_available(self) -> bool:
        # Check if service is ready
```

## 🎮 Features

### Four Main Tabs

1. **🏠 Personal RAG System**
   - Query personal documents
   - Local document retrieval
   - Personal context responses

2. **🌐 Web Search Agent**
   - Real-time web search
   - AI-powered analysis
   - Current information retrieval

3. **🔄 Hybrid RAG System**
   - Intelligent source selection
   - Combines local + web when needed
   - Adaptive information retrieval

4. **⚖️ Compare All Systems**
   - Side-by-side comparison
   - See different approaches to same question
   - Source attribution for each system

### Additional Features

- **Example Questions**: Pre-built examples for each system
- **Source Attribution**: Clear indication of information sources
- **System Status**: Real-time monitoring of system availability
- **Error Handling**: Graceful fallbacks and helpful error messages
- **Responsive Design**: Works on desktop and mobile

## 🔧 Configuration

### System Status Display

The interface automatically detects which systems are available:

- ✅ System Ready
- ❌ System Not Available

### Error Handling

Each component includes comprehensive error handling:

- API key validation
- System availability checks
- Input validation
- Graceful error messages

## 🎨 Customization

### Adding New Systems

1. Create service wrapper in `services/`
2. Create UI component in `components/`
3. Add to main interface in `app.py`
4. Update `AIAssistantService` coordinator

### Modifying Existing Components

Each component is self-contained and can be modified independently:

- Update UI layout in component files
- Modify business logic in service files
- Adjust styling in `app.py` CSS

### Custom Styling

CSS customization is centralized in `app.py`:

```python
css="""
.gradio-container {
    max-width: 1200px !important;
}
.source-info {
    font-size: 0.9em;
    color: #666;
    font-style: italic;
}
"""
```

## 🚨 Troubleshooting

### Common Issues

**Import Errors**
- Ensure all parent systems are properly set up
- Check Python path configuration
- Verify dependencies are installed

**System Not Available**
- Check system status in the accordion
- Verify underlying systems work independently
- Check API keys and configuration

**UI Not Loading**
- Ensure Gradio is installed: `pip install gradio`
- Check for port conflicts (default: 7860)
- Verify all import statements work

### Development Tips

- **Test Components Individually**: Each component can be imported and tested
- **Service Layer Testing**: Services can be tested without UI
- **Debug Mode**: Run with `show_error=True` for detailed error messages

## 📈 Performance

### Optimization Strategies

- **Lazy Loading**: Services are only initialized when needed
- **Error Isolation**: One system failure doesn't affect others
- **Efficient Imports**: Only import what's needed when needed

### Resource Usage

- **Memory**: Each service maintains its own state
- **Network**: Only active systems make API calls
- **CPU**: Gradio interface is lightweight

## 🔄 Integration

### CLI Integration

Services can be imported and used in command-line scripts:

```python
from services import PersonalRAGService

service = PersonalRAGService()
answer, sources = service.query("Tell me about my background")
```

### API Integration

Services can be wrapped in FastAPI or Flask for REST API:

```python
from fastapi import FastAPI
from services import AIAssistantService

app = FastAPI()
assistant = AIAssistantService()

@app.post("/query")
def query_assistant(query: str, system: str):
    if system == "personal":
        return assistant.query_personal_rag(query)
    # ... other systems
```

## 📞 Support

For web UI specific issues:

1. **Check System Status**: Use the status accordion in the interface
2. **Verify Dependencies**: Ensure `gradio` is installed
3. **Test Individual Systems**: Verify each system works independently
4. **Check Console Output**: Look for error messages in terminal
5. **Port Issues**: Try a different port if 7860 is occupied

---

*Modular web interface for seamless AI system interaction*# web_rag_ui_module
