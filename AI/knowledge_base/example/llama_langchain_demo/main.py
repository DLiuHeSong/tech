from utils.llm_init import init_llm
from utils.index_builder import build_index
from utils.query_engine import create_engine

if __name__ == "__main__":
    llm = init_llm()
    index = build_index("data/")
    query_engine = create_engine(index, llm)

    while True:
        query = input("请输入你的问题（输入 exit 退出）：")
        if query.strip().lower() == "exit":
            break
        response = query_engine.query(query)
        print("🤖 答案：", response)