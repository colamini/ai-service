
import os
import faiss
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()

# 加载和向量化文档
def build_vector_store():
    loader = TextLoader("./docs/sample.txt")  # 简单示例文档
    docs = loader.load()
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local("./faiss_index")
    return vectorstore

def load_vector_store():
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local("./faiss_index", embeddings)

# RAG问答接口
def get_qa_chain():
    vectorstore = load_vector_store()
    retriever = vectorstore.as_retriever()
    llm = ChatOpenAI(temperature=0)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain
