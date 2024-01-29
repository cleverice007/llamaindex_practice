from dotenv import load_dotenv
from llama_index.chat_engine.types import ChatMode
from llama_index.indices.postprocessor import SentenceEmbeddingOptimizer
from node_postprocessors.duplicate_postprocessing import DuplicateRemoverNodePostprocessor

load_dotenv()
import os

from llama_index.callbacks import LlamaDebugHandler, CallbackManager
import streamlit as st
import pinecone
from llama_index import VectorStoreIndex, ServiceContext
from llama_index.vector_stores import PineconeVectorStore

print("***Streamlit LlamaIndex Documentation Helper***")

llama_debug = LlamaDebugHandler(print_trace_on_end=True)
callback_manager = CallbackManager(handlers=[llama_debug])
service_context = ServiceContext.from_defaults(callback_manager=callback_manager)

@st.cache_resource(show_spinner=False)
def get_index() -> VectorStoreIndex:
    pinecone.init(
        api_key=os.environ["PINECONE_API_KEY"],
        environment=os.environ["PINECONE_ENVIRONMENT"],
    )
    pinecone_index = pinecone.Index(index_name="llamaindex-practice")
    vector_store = PineconeVectorStore(pinecone_index=pinecone_index)

    return VectorStoreIndex.from_vector_store(
        vector_store=vector_store, service_context=service_context
    )

# 初始化並獲取索引
index = get_index()

# 在session state中初始化chat_engine
if 'chat_engine' not in st.session_state:
    # 使用index.as_chat_engine創建chat_engine
    st.session_state.chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

st.set_page_config(
    page_title="Chat with LlamaIndex docs, powered by LlamaIndex",
    page_icon="🦙",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)

st.title("Chat with LlamaIndex docs 💬🦙")

if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Ask me a question about LlamaIndex's open source python library?",
        }
    ]

# 用戶輸入提示
if prompt := st.chat_input("Your question"):
    st.session_state.messages.append({"role": "user", "content": prompt})

# 顯示消息歷史
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 如果最後一條消息不是來自助手，則生成新的回應
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # 使用chat_engine獲取回應
            response = st.session_state.chat_engine.chat(prompt)
            st.write(response.response)
            # 將回應添加到消息歷史中
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message)
