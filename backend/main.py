from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from rag_service import get_qa_chain, build_vector_store
import os
import asyncio
import time  # 需要导入 time 模块
import json

app = FastAPI()

# CORS配置，允许Vue的请求访问
origins = ["http://localhost:8080"]  # Vue 默认端口
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 初始化QA链和向量存储
qa_chain = get_qa_chain()

# POST请求的查询模型
class Query(BaseModel):
    question: str

@app.post("/ask")
def ask_question(query: Query):
    # 从qa_chain生成答案
    result = qa_chain.run(query.question)
    return {"answer": result}

@app.get("/init")
def initialize():
    # 构建向量存储索引
    build_vector_store()
    return {"status": "Index built"}

# 处理WebSocket连接
active_connections = {}

@app.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str):
    await websocket.accept()
    active_connections[room_id] = websocket
    try:
        while True:
            # 接受信息
            data = await websocket.receive_text()
            print(f"接收到来自房间 {room_id} 的消息: {data}")

             # 解析接收到的消息
            parsed_data = json.loads(data)
            question = parsed_data.get("content", "")  # 获取 'content' 字段
            
            # 使用 qa_chain 处理接收到的消息（即用户提问）
            answer = qa_chain.run(question)


            # 构建消息对象（模拟回答）
            response = {
                "_id": f"msg-{int(time.time())}",
                "content": f"收到了你的问题：{answer}",
                "senderId": "bot",
                "timestamp": int(time.time() * 1000),
                "roomId": room_id
            }

            # 返回标准 JSON 格式
            await websocket.send_text(json.dumps(response))
    except WebSocketDisconnect:
        # 断开连接时从active_connections移除该房间
        active_connections.pop(room_id, None)
        print(f"房间 {room_id} 的连接已断开")
