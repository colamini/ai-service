
# AI Service

基于 FastAPI + LangChain + FAISS 的简易问答服务，前端使用 Vue 2 实现。

---

## 📁 项目结构

```
ai-service/
├── backend/          # Python 后端服务 (FastAPI + LangChain)
│   ├── main.py
│   ├── documents/    # 示例文档（txt格式）
│   ├── vectorstore/  # 向量数据存储目录
│   ├── Makefile      # 一键运行指令集合
│   └── .env          # 存放 OPENAI_API_KEY 等私密变量
├── frontend/         # 前端项目（Vue2）
│   └── ...
```

---

## 🚀 快速开始（Backend）

### 1. 安装 Poetry（首次）
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### 2. 进入 backend 并安装依赖
```bash
cd backend
poetry install
```

### 3. 设置环境变量

创建 `.env` 文件，填入你的 OpenAI Key，目前的 API Key 用的是我的代理，可以跑通

```
OPENAI_API_KEY=sk-xxxx
```

### 4. 初始化向量库（首次）
```bash
make init-db
```

### 5. 启动服务
```bash
make run
```

接口运行在：`http://127.0.0.1:8000`

---

## 🔍 API 接口说明

### `GET /init`

加载 `documents/` 下所有 `.txt` 文件并写入 FAISS 向量库。

---

### `POST /ask`

问答接口，从向量数据库检索相关文段并调用 LLM 生成回答。

#### 请求格式：
```json
{
  "question": "What is in the sample doc?"
}
```

#### 响应格式：
```json
{
  "answer": "This document is a sample...",
  "source_documents": [...]
}
```

---

## 🖥️ 启动前端服务（Vue2）

### 1. 安装依赖
```bash
cd frontend
npm install
```

### 2. 运行开发环境
```bash
npm run dev
```

确保后端接口运行在 `http://localhost:8000`，前端代码中默认访问该地址。

---

## 📦 一键命令速查

在 `backend` 目录下：

| 命令           | 说明                      |
|----------------|---------------------------|
| `make start`   | 安装依赖 + 启动服务       |
| `make run`     | 启动 FastAPI 服务          |
| `make shell`   | 进入 Poetry 虚拟环境       |
| `make init-db` | 初始化文档向量库           |
| `make ask`     | 测试问答接口（POST /ask） |

---

## 🧠 使用技术栈

- Python 3.10
- [FastAPI](https://fastapi.tiangolo.com/)
- [LangChain](https://www.langchain.com/)
- [Chroma]()
- Vue 2 + Vite
- OpenAI API

---

## 📄 License

MIT
