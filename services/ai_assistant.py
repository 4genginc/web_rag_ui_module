import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import logging
from typing import Tuple, List

# Import service wrappers
from .personal_rag_service import PersonalRAGService
from .web_search_service import WebSearchService
from .hybrid_rag_service import HybridRAGService

logger = logging.getLogger(__name__)

class AIAssistantService:
    """Main service coordinator for all AI systems"""
    
    def __init__(self):
        """Initialize all AI services"""
        # Load environment
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        
        # Initialize services
        self.personal_rag = None
        self.web_search = None
        self.hybrid_rag = None
        
        self._initialize_services()
    
    def _initialize_services(self):
        """Initialize individual services with error handling"""
        
        # Personal RAG Service
        try:
            self.personal_rag = PersonalRAGService()
            logger.info("Personal RAG Service initialized")
        except Exception as e:
            logger.warning(f"Personal RAG Service failed: {e}")
        
        # Web Search Service
        try:
            self.web_search = WebSearchService(self.api_key)
            logger.info("Web Search Service initialized")
        except Exception as e:
            logger.warning(f"Web Search Service failed: {e}")
        
        # Hybrid RAG Service
        try:
            self.hybrid_rag = HybridRAGService()
            logger.info("Hybrid RAG Service initialized")
        except Exception as e:
            logger.warning(f"Hybrid RAG Service failed: {e}")
    
    def query_personal_rag(self, query: str) -> Tuple[str, str]:
        """Query personal RAG system"""
        if not self.personal_rag:
            return "Personal RAG Service not available", "❌ Service unavailable"
        
        return self.personal_rag.query(query)
    
    def query_web_search(self, query: str) -> Tuple[str, str]:
        """Query web search system"""
        if not self.web_search:
            return "Web Search Service not available", "❌ Service unavailable"
        
        return self.web_search.query(query)
    
    def query_hybrid_rag(self, query: str) -> Tuple[str, str]:
        """Query hybrid RAG system"""
        if not self.hybrid_rag:
            return "Hybrid RAG Service not available", "❌ Service unavailable"
        
        return self.hybrid_rag.query(query)
    
    def compare_all_systems(self, query: str) -> Tuple[str, str, str, str, str, str]:
        """Compare responses from all three systems"""
        
        # Query all systems
        personal_answer, personal_sources = self.query_personal_rag(query)
        web_answer, web_sources = self.query_web_search(query)
        hybrid_answer, hybrid_sources = self.query_hybrid_rag(query)
        
        return personal_answer, personal_sources, web_answer, web_sources, hybrid_answer, hybrid_sources
    
    def get_system_status(self) -> List[str]:
        """Get status of all systems"""
        status = []
        
        if self.personal_rag:
            status.append("✅ Personal RAG System: Ready")
        else:
            status.append("❌ Personal RAG System: Not available")
        
        if self.web_search:
            status.append("✅ Web Search Agent: Ready")
        else:
            status.append("❌ Web Search Agent: Not available")
        
        if self.hybrid_rag:
            status.append("✅ Hybrid RAG System: Ready")
        else:
            status.append("❌ Hybrid RAG System: Not available")
        
        return status
    
    def is_available(self) -> bool:
        """Check if at least one system is available"""
        return any([self.personal_rag, self.web_search, self.hybrid_rag])