以下是一个完整的教学项目结构，基于 **LangChain + LlamaIndex** 实现私有文档问答系统，适合用于教学或开发原型系统。

---

# 🧱 教学项目结构：LangChain + LlamaIndex 文档问答系统

```
llama_langchain_demo/
├── main.py                        # 主运行入口
├── requirements.txt              # 依赖列表
├── config.py                     # 配置项（API Key等）
├── data/
│   └── example.txt               # 示例文档（可自行添加）
├── utils/
│   └── llm_init.py               # LLM 初始化模块
│   └── index_builder.py          # 构建索引模块
│   └── query_engine.py           # 查询引擎封装
└── README.md                     # 教学说明文档
```

---

## 📄 示例文档内容（`data/example.txt`）

```text
LangChain 是一个用于构建基于大语言模型（LLM）的应用的开发框架。LlamaIndex 是一个用于将结构化和非结构化数据连接到语言模型的工具。
```

---

## 🧪 示例运行流程（`main.py`）

```python
# main.py
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
```

---

## 🧰 模块详解

### 🔧 `utils/llm_init.py`

```python
from langchain.chat_models import ChatOpenAI
import os

def init_llm():
    return ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo",
        openai_api_key=os.environ["OPENAI_API_KEY"]
    )
```

### 🔧 `utils/index_builder.py`

```python
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

def build_index(doc_dir: str):
    documents = SimpleDirectoryReader(doc_dir).load_data()
    return VectorStoreIndex.from_documents(documents)
```

### 🔧 `utils/query_engine.py`

```python
from llama_index.core.query_engine import RetrieverQueryEngine

def create_engine(index, llm):
    return index.as_query_engine(llm=llm)
```

---

## 📦 requirements.txt

```txt
openai
langchain
llama-index
```

安装方式：

```bash
pip install -r requirements.txt
```

---

## 📘 README.md 示例内容

````markdown
# LangChain + LlamaIndex 教学项目

## 🧠 项目目标
构建一个私有文档问答系统，支持用户通过自然语言提问，自动从本地文档中检索答案。

## 📁 文件结构
- `data/`：放置需要检索的文本文件
- `utils/`：封装 LLM 初始化、索引构建、查询引擎等模块
- `main.py`：交互式问答入口

## 🚀 运行方式
1. 设置环境变量：
```bash
export OPENAI_API_KEY=你的key
````

2. 安装依赖：

```bash
pip install -r requirements.txt
```

3. 启动问答系统：

```bash
python main.py
```

## 🧪 示例问题

* LangChain 是什么？
* LlamaIndex 的作用？


---
## 📦 可选增强模块（拓展练习）

| 模块         | 说明                                  |
|--------------|---------------------------------------|
| PDFLoader     | 支持加载 PDF 文档                     |
| 多轮对话记忆  | 加入 LangChain 的 Memory 模块          |
| Web 接口      | 使用 Flask/FastAPI 提供 API 服务        |
| 向量存储持久化 | 支持 FAISS / Weaviate 等保存索引       |
| Agent 模式    | 加入搜索工具、函数调用等复杂场景       |

---



