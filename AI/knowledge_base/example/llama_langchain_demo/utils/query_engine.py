from llama_index.core.query_engine import RetrieverQueryEngine

def create_engine(index, llm):
    return index.as_query_engine(llm=llm)