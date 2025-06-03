import gradio as gr
from typing import Tuple

def create_personal_rag_tab(assistant_service):
    """Create the Personal RAG tab interface"""
    
    def safe_personal_query(query: str) -> Tuple[str, str]:
        """Safely execute personal RAG query"""
        if not assistant_service:
            return "AI Assistant not initialized", "❌ System Error"
        
        if not query.strip():
            return "Please enter a question", "❌ Empty Query"
        
        return assistant_service.query_personal_rag(query)
    
    with gr.TabItem("🏠 Personal RAG System"):
        gr.Markdown("Query your personal documents using advanced RAG technology.")
        
        with gr.Row():
            with gr.Column():
                personal_input = gr.Textbox(
                    label="Ask about your background, experience, or personal information",
                    placeholder="e.g., Tell me about my background and where I'm from",
                    lines=2
                )
                personal_btn = gr.Button("Query Personal Documents", variant="primary")
            
            with gr.Column():
                personal_output = gr.Textbox(
                    label="Answer",
                    lines=8,
                    interactive=False
                )
                personal_sources = gr.Textbox(
                    label="Sources",
                    lines=1,
                    interactive=False,
                    elem_classes=["source-info"]
                )
        
        # Example questions
        gr.Examples(
            examples=[
                "Tell me about my background and where I'm from",
                "What are my main technical skills?",
                "What are my food preferences?",
                "What is my education background?"
            ],
            inputs=personal_input
        )
        
        # Event handler
        personal_btn.click(
            fn=safe_personal_query,
            inputs=personal_input,
            outputs=[personal_output, personal_sources]
        )