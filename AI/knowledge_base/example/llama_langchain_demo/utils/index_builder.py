from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

def build_index(doc_dir: str):
    documents = SimpleDirectoryReader(doc_dir).load_data()
    return VectorStoreIndex.from_documents(documents)