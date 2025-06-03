import sys
from pathlib import Path
from typing import Tuple
import logging

logger = logging.getLogger(__name__)

class PersonalRAGService:
    """Service wrapper for Personal RAG System"""
    
    def __init__(self, documents_folder: str = "../personal-rag-system/me"):
        """Initialize Personal RAG Service"""
        try:
            # Add the personal-rag-system directory to Python path
            current_dir = Path(__file__).parent.parent
            rag_system_dir = current_dir / "personal-rag-system"
            sys.path.insert(0, str(rag_system_dir))
            
            # Import the existing PersonalRAGSystem
            from rag_multi_docs import PersonalRAGSystem
            
            # Initialize with documents folder (use relative path from web-ui)
            self.rag_system = PersonalRAGSystem("../personal-rag-system/me")
            self.rag_system.load_personal_documents()
            
            logger.info("Personal RAG Service initialized successfully")
            
        except ImportError as e:
            logger.error(f"Failed to import PersonalRAGSystem: {e}")
            logger.error(f"Make sure you're running from the project root directory")
            raise
        except Exception as e:
            logger.error(f"Failed to initialize Personal RAG Service: {e}")
            raise
    
    def query(self, query: str) -> Tuple[str, str]:
        """Query the personal RAG system"""
        try:
            result = self.rag_system.query_personal_info(query)
            
            # Extract answer and sources
            answer = result.get("answer", "No answer generated")
            sources = result.get("sources", [])
            files = result.get("files", [])
            
            # Format sources
            if sources and files:
                source_info = f"📚 Personal Documents: {', '.join(sources)} from {', '.join(set(files))}"
            elif sources:
                source_info = f"📚 Personal Documents: {', '.join(sources)}"
            else:
                source_info = "📚 Personal Documents"
            
            return answer, source_info
            
        except Exception as e:
            logger.error(f"Personal RAG query failed: {e}")
            return f"Error with Personal RAG: {str(e)}", "❌ Error"
    
    def is_available(self) -> bool:
        """Check if the service is available"""
        return hasattr(self, 'rag_system') and self.rag_system is not None