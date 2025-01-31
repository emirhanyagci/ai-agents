from phi.model.google import Gemini
from phi.model.ollama import Ollama
from phi.agent import Agent
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.pgvector import PgVector, SearchType
from phi.embedder.ollama import OllamaEmbedder
from phi.embedder.google import GeminiEmbedder

embedder = OllamaEmbedder(dimensions=1536)

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
knowledge_base = PDFUrlKnowledgeBase(
    # Read PDF from this URL
    urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    # Store embeddings in the `ai.recipes` table
    vector_db=PgVector(
        table_name="recipes",
        db_url=db_url,
        embedder=GeminiEmbedder(),
        search_type=SearchType.hybrid,
    ),
)

# knowledge_base.load(upsert=True)
agent = Agent(
    model=Ollama(id="llama3.1"),
    knowledge=knowledge_base,
    description="You are the expert recipe master",
    instructions=[
        "Search requested recipe in your knowladge if you not find answer without knowladge"
    ],
    # Enable RAG by adding references from AgentKnowledge to the user prompt.
    add_context=True,
    # Set as False because Agents default to `search_knowledge=True`
    search_knowledge=False,
    markdown=True,
    show_tool_calls=True,
    read_chat_history=True,
    # debug_mode=True,
)
agent.print_response("How do I make 1 serve chicken and galangal in coconut milk soup")
agent.print_response("What is my previous question")
