import gradio as gr
from typing import Tuple

def create_hybrid_rag_tab(assistant_service):
    """Create the Hybrid RAG tab interface"""
    
    def safe_hybrid_query(query: str) -> Tuple[str, str]:
        """Safely execute hybrid RAG query"""
        if not assistant_service:
            return "AI Assistant not initialized", "❌ System Error"
        
        if not query.strip():
            return "Please enter a question", "❌ Empty Query"
        
        return assistant_service.query_hybrid_rag(query)
    
    with gr.TabItem("🔄 Hybrid RAG System"):
        gr.Markdown("Intelligent system that automatically combines personal documents and web search.")
        
        with gr.Row():
            with gr.Column():
                hybrid_input = gr.Textbox(
                    label="Ask any question - the system will choose the best source(s)",
                    placeholder="e.g., How do my skills compare to current AI industry trends?",
                    lines=2
                )
                hybrid_btn = gr.Button("Ask Hybrid System", variant="primary")
            
            with gr.Column():
                hybrid_output = gr.Textbox(
                    label="Answer",
                    lines=8,
                    interactive=False
                )
                hybrid_sources = gr.Textbox(
                    label="Sources Used",
                    lines=1,
                    interactive=False,
                    elem_classes=["source-info"]
                )
        
        # Example questions
        gr.Examples(
            examples=[
                "Tell me about my background",
                "Who is the CEO of OpenAI and what is their background?",
                "What are the latest AI trends and how do they relate to my skills?",
                "My food preferences and popular restaurants in San Francisco"
            ],
            inputs=hybrid_input
        )
        
        # Event handler
        hybrid_btn.click(
            fn=safe_hybrid_query,
            inputs=hybrid_input,
            outputs=[hybrid_output, hybrid_sources]
        )