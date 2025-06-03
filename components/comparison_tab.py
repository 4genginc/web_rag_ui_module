import gradio as gr
from typing import Tuple

def create_comparison_tab(assistant_service):
    """Create the System Comparison tab interface"""
    
    def safe_compare_query(query: str) -> Tuple[str, str, str, str, str, str]:
        """Safely execute comparison across all systems"""
        if not assistant_service:
            error_msg = "AI Assistant not initialized"
            return error_msg, "❌ Error", error_msg, "❌ Error", error_msg, "❌ Error"
        
        if not query.strip():
            empty_msg = "Please enter a question"
            return empty_msg, "❌ Empty", empty_msg, "❌ Empty", empty_msg, "❌ Empty"
        
        return assistant_service.compare_all_systems(query)
    
    with gr.TabItem("⚖️ Compare All Systems"):
        gr.Markdown("Compare responses from all three systems side-by-side.")
        
        compare_input = gr.Textbox(
            label="Enter your question to see how each system responds",
            placeholder="e.g., What are the latest developments in AI?",
            lines=2
        )
        compare_btn = gr.Button("Compare All Systems", variant="primary")
        
        with gr.Row():
            with gr.Column():
                gr.Markdown("### 🏠 Personal RAG")
                compare_personal = gr.Textbox(
                    label="Answer", 
                    lines=6, 
                    interactive=False
                )
                compare_personal_sources = gr.Textbox(
                    label="Sources", 
                    lines=1, 
                    interactive=False, 
                    elem_classes=["source-info"]
                )
            
            with gr.Column():
                gr.Markdown("### 🌐 Web Search")
                compare_web = gr.Textbox(
                    label="Answer", 
                    lines=6, 
                    interactive=False
                )
                compare_web_sources = gr.Textbox(
                    label="Sources", 
                    lines=1, 
                    interactive=False, 
                    elem_classes=["source-info"]
                )
            
            with gr.Column():
                gr.Markdown("### 🔄 Hybrid RAG")
                compare_hybrid = gr.Textbox(
                    label="Answer", 
                    lines=6, 
                    interactive=False
                )
                compare_hybrid_sources = gr.Textbox(
                    label="Sources", 
                    lines=1, 
                    interactive=False, 
                    elem_classes=["source-info"]
                )
        
        # Example questions for comparison
        gr.Examples(
            examples=[
                "Tell me about my background",
                "Latest developments in AI",
                "Who is the CEO of OpenAI?",
                "My skills and current job market trends"
            ],
            inputs=compare_input
        )
        
        # Event handler
        compare_btn.click(
            fn=safe_compare_query,
            inputs=compare_input,
            outputs=[
                compare_personal, compare_personal_sources,
                compare_web, compare_web_sources,
                compare_hybrid, compare_hybrid_sources
            ]
        )