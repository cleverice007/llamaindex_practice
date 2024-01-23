from dotenv import load_dotenv
from llama_index.chat_engine.types import ChatMode
from llama_index.indices.postprocessor import SentenceEmbeddingOptimizer

from node_postprocessors.duplicate_postprocessing import (
    DuplicateRemoverNodePostprocessor,
)

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
    pinecone_index = pinecone.Index(index_name="llamaindex-documentation-helper")
    vector_store = PineconeVectorStore(pinecone_index=pinecone_index)

    return VectorStoreIndex.from_vector_store(
        vector_store=vector_store, service_context=service_context
    )
