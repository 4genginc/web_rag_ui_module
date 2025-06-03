import gradio as gr
import logging
from pathlib import Path

# Import our modular components
from components.personal_rag_tab import create_personal_rag_tab
from components.web_search_tab import create_web_search_tab
from components.hybrid_rag_tab import create_hybrid_rag_tab
from components.comparison_tab import create_comparison_tab
from services.ai_assistant import AIAssistantService

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_main_interface():
    """Create the main Gradio interface with all tabs"""
    
    # Initialize the AI assistant service
    try:
        assistant_service = AIAssistantService()
        logger.info("AI Assistant Service initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize AI Assistant Service: {e}")
        assistant_service = None
    
    # Create the main interface
    with gr.Blocks(
        title="AI Personal Assistant Suite",
        theme=gr.themes.Soft(),
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
    ) as demo:
        
        # Header
        gr.Markdown("""
        # 🤖 AI Personal Assistant Suite
        
        Interactive web interface for three complementary AI systems:
        - **Personal RAG**: Query your personal documents
        - **Web Search Agent**: Real-time web research  
        - **Hybrid RAG**: Intelligently combines both sources
        
        ---
        """)
        
        # Create tabs
        with gr.Tabs():
            # Personal RAG Tab
            create_personal_rag_tab(assistant_service)
            
            # Web Search Tab
            create_web_search_tab(assistant_service)
            
            # Hybrid RAG Tab
            create_hybrid_rag_tab(assistant_service)
            
            # Comparison Tab
            create_comparison_tab(assistant_service)
        
        # System Status
        with gr.Accordion("🔧 System Status", open=False):
            if assistant_service:
                status_lines = assistant_service.get_system_status()
            else:
                status_lines = ["❌ AI Assistant Service: Not initialized"]
            
            gr.Markdown("\n".join(status_lines))
        
        # Footer
        gr.Markdown("""
        ---
        **AI Personal Assistant Suite** - Powered by OpenAI, ChromaDB, and DuckDuckGo  
        💡 Tip: Try the comparison tab to see how different systems handle the same question!
        """)
    
    return demo

def main():
    """Launch the Gradio web interface"""
    print("🚀 Starting AI Personal Assistant Web UI...")
    print("📍 Make sure you have:")
    print("   ✅ OpenAI API key in .env file")
    print("   ✅ Personal documents in personal-rag-system/me/")
    print("   ✅ All dependencies installed")
    print()
    
    try:
        demo = create_main_interface()
        demo.launch(
            server_name="0.0.0.0",  # Allow external connections
            server_port=7860,       # Default Gradio port
            share=False,            # Set to True for public sharing
            show_error=True,        # Show detailed errors
            quiet=False             # Show startup info
        )
    except Exception as e:
        print(f"❌ Failed to launch web UI: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Check that all dependencies are installed: pip install gradio")
        print("2. Ensure .env file exists with OPENAI_API_KEY")
        print("3. Verify personal documents are in personal-rag-system/me/")

if __name__ == "__main__":
    main()