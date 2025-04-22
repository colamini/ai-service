import os
from langchain_community.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA, LLMChain
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv

from prompts import qa_prompt

# 加载环境变量
load_dotenv()

# 配置OpenAI参数
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_BASE"] = os.getenv("OPENAI_API_BASE")

PERSIST_DIR = "./chroma_index"

def build_vector_store():
    loader = TextLoader("./docs/sample.txt")
    docs = loader.load()
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    # 配置自定义API终端的Embeddings
    embeddings = OpenAIEmbeddings(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_api_base=os.getenv("OPENAI_API_BASE")
    )
    
    vectorstore = Chroma.from_documents(
        chunks, 
        embeddings, 
        persist_directory=PERSIST_DIR
    )
    vectorstore.persist()
    return vectorstore

def load_vector_store():
    embeddings = OpenAIEmbeddings(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_api_base=os.getenv("OPENAI_API_BASE")
    )
    return Chroma(
        persist_directory=PERSIST_DIR, 
        embedding_function=embeddings
    )


def get_qa_chain():
    vectorstore = load_vector_store()
    retriever = vectorstore.as_retriever()

    # 配置自定义API终端的Chat模型
    llm = ChatOpenAI(
        temperature=0,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_api_base=os.getenv("OPENAI_API_BASE")
    )



    # # 创建 LLMChain，结合 ChatOpenAI 和 prompt_template
    # qa_chain = LLMChain(
    #     llm=llm,
    #     prompt=prompt
    # )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": qa_prompt}
    )

    return qa_chain
