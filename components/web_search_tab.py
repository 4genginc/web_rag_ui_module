import gradio as gr
from typing import Tuple

def create_web_search_tab(assistant_service):
    """Create the Web Search tab interface"""
    
    def safe_web_query(query: str) -> Tuple[str, str]:
        """Safely execute web search query"""
        if not assistant_service:
            return "AI Assistant not initialized", "❌ System Error"
        
        if not query.strip():
            return "Please enter a question", "❌ Empty Query"
        
        return assistant_service.query_web_search(query)
    
    with gr.TabItem("🌐 Web Search Agent"):
        gr.Markdown("Real-time web search with AI-powered analysis.")
        
        with gr.Row():
            with gr.Column():
                web_input = gr.Textbox(
                    label="Search for current information, news, or research topics",
                    placeholder="e.g., Latest developments in AI in 2025",
                    lines=2
                )
                web_btn = gr.Button("Search the Web", variant="primary")
            
            with gr.Column():
                web_output = gr.Textbox(
                    label="Answer",
                    lines=8,
                    interactive=False
                )
                web_sources = gr.Textbox(
                    label="Sources",
                    lines=1,
                    interactive=False,
                    elem_classes=["source-info"]
                )
        
        # Example questions
        gr.Examples(
            examples=[
                "Latest developments in AI in 2025",
                "Current trends in renewable energy",
                "Who is the CEO of OpenAI?",
                "Recent breakthroughs in quantum computing"
            ],
            inputs=web_input
        )
        
        # Event handler
        web_btn.click(
            fn=safe_web_query,
            inputs=web_input,
            outputs=[web_output, web_sources]
        )