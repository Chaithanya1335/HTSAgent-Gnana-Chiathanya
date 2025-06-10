from langchain.tools import tool
from src.Pipeline.Rag_Pipeline import Ragpipeline

# Load once and reuse
rag_instance = Ragpipeline().pipeline()

@tool
def rag_query_tool(query: str) -> str:
    """
    Answers questions using RAG with the HTS General Notes context.

    Example query: 
    "According to General Rule of Interpretation 2(a), under what condition can an incomplete or unfinished article be classified as a complete or finished article?"
    """
    try:
        return rag_instance.invoke(query)
    except Exception as e:
        return f"RAG Error: {e}"
