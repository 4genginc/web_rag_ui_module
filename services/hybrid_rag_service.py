import sys
from pathlib import Path
from typing import Tuple
import logging

logger = logging.getLogger(__name__)

class HybridRAGService:
    """Service wrapper for Hybrid RAG System"""
    
    def __init__(self, documents_folder: str = "../personal-rag-system/me", min_context_length: int = 300):
        """Initialize Hybrid RAG Service"""
        try:
            # Add the hybrid-rag-system directory to Python path
            current_dir = Path(__file__).parent.parent
            hybrid_system_dir = current_dir / "hybrid-rag-system"
            sys.path.insert(0, str(hybrid_system_dir))
            
            # Import the existing HybridRAGSystem
            from hybrid_rag import HybridRAGSystem
            
            # Initialize with documents folder and threshold (use relative path from web-ui)
            self.hybrid_system = HybridRAGSystem(
                documents_folder="../personal-rag-system/me",
                min_context_length=min_context_length
            )
            
            logger.info("Hybrid RAG Service initialized successfully")
            
        except ImportError as e:
            logger.error(f"Failed to import HybridRAGSystem: {e}")
            logger.error(f"Make sure you're running from the project root directory")
            raise
        except Exception as e:
            logger.error(f"Failed to initialize Hybrid RAG Service: {e}")
            raise
    
    def query(self, query: str) -> Tuple[str, str]:
        """Query the hybrid RAG system"""
        try:
            answer, metadata = self.hybrid_system.hybrid_query(query)
            
            # Format sources based on what was used
            sources_used = metadata.get("sources_used", [])
            local_length = metadata.get("local_context_length", 0)
            web_length = metadata.get("web_context_length", 0)
            
            if "local" in sources_used and "web" in sources_used:
                sources = f"🔄 Hybrid: Personal docs ({local_length} chars) + Web search"
            elif "local" in sources_used:
                sources = f"🏠 Personal documents only ({local_length} chars)"
            elif "web" in sources_used:
                sources = f"🌐 Web search only"
            else:
                sources = "❓ Unknown sources"
            
            return answer, sources
            
        except Exception as e:
            logger.error(f"Hybrid RAG query failed: {e}")
            return f"Error with Hybrid RAG: {str(e)}", "❌ Error"
    
    def is_available(self) -> bool:
        """Check if the service is available"""
        return hasattr(self, 'hybrid_system') and self.hybrid_system is not None