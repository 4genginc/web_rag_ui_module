# components/__init__.py
"""
UI Components for the AI Personal Assistant Web Interface

This package contains modular Gradio components for each system:
- personal_rag_tab: Personal RAG System interface
- web_search_tab: Web Search Agent interface  
- hybrid_rag_tab: Hybrid RAG System interface
- comparison_tab: Side-by-side system comparison
"""

from .personal_rag_tab import create_personal_rag_tab
from .web_search_tab import create_web_search_tab
from .hybrid_rag_tab import create_hybrid_rag_tab
from .comparison_tab import create_comparison_tab

__all__ = [
    'create_personal_rag_tab',
    'create_web_search_tab', 
    'create_hybrid_rag_tab',
    'create_comparison_tab'
]

# services/__init__.py
"""
Service Layer for the AI Personal Assistant Suite

This package contains service wrappers for each AI system:
- ai_assistant: Main service coordinator
- personal_rag_service: Personal RAG System wrapper
- web_search_service: Web Search Agent wrapper
- hybrid_rag_service: Hybrid RAG System wrapper
"""

from .ai_assistant import AIAssistantService
from .personal_rag_service import PersonalRAGService
from .web_search_service import WebSearchService
from .hybrid_rag_service import HybridRAGService

__all__ = [
    'AIAssistantService',
    'PersonalRAGService',
    'WebSearchService', 
    'HybridRAGService'
]