from duckduckgo_search import DDGS
from openai import OpenAI
from typing import Tuple
import logging

logger = logging.getLogger(__name__)

class WebSearchService:
    """Service wrapper for Web Search functionality"""
    
    def __init__(self, api_key: str):
        """Initialize Web Search Service"""
        try:
            self.client = OpenAI(api_key=api_key)
            logger.info("Web Search Service initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize Web Search Service: {e}")
            raise
    
    def search_web(self, query: str) -> str:
        """Perform web search using DuckDuckGo"""
        try:
            results = []
            with DDGS() as ddgs:
                for r in ddgs.text(query, region='wt-wt', safesearch='Moderate', max_results=3):
                    results.append(f"**{r['title']}**\n{r['href']}\n{r['body']}\n")
            return "\n---\n".join(results) if results else "No results found."
        except Exception as e:
            logger.error(f"Web search failed: {e}")
            return f"Search error: {str(e)}"
    
    def query(self, query: str) -> Tuple[str, str]:
        """Query with web search and AI analysis"""
        try:
            # Get web search results
            web_results = self.search_web(query)
            
            if "Search error" in web_results or "No results found" in web_results:
                return web_results, "❌ Web search failed"
            
            # Process with AI
            prompt = f"""You are a research assistant. Based on the web search results below, provide a comprehensive answer to the user's question. Always cite your sources with URLs when available.

Web Search Results:
{web_results}

Question: {query}

Answer:"""
            
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500,
                temperature=0.1
            )
            
            answer = response.choices[0].message.content
            sources = "🌐 Web Search (DuckDuckGo)"
            
            return answer, sources
            
        except Exception as e:
            logger.error(f"Web search query failed: {e}")
            return f"Error processing web search: {str(e)}", "❌ Error"
    
    def is_available(self) -> bool:
        """Check if the service is available"""
        return hasattr(self, 'client') and self.client is not None