# LlamaIndex Practice

## description
`llamaindex_practice` 是一個使用 Python 開發的項目，使用LlamaIndex 的網頁資料打造了一個 retrieval augmented generation (RAG) 應用。此項目將數據存儲到 Pinecone（一種向量數據庫），街上
 ChatGPT API 來打造具備聊天功能。使用戶能夠通過聊天查詢存儲在向量數據庫中的資訊，返回llamaindex相關的文件內容

## features**
### 1. `download.py`
從指定的網址（如 LlamaIndex 文檔頁面）下載所有的 `.html` 文件爬取網頁上的超連結，檢查每個連結是否指向 `.html` 文件，若是，則下載這些文件並將它們保存在本地指定的目錄中。
主要用於初步收集網頁資料，為後續數據處理或分析工作準備原始資料。

### 2. `ingestion.py`
已下載的 HTML 文檔進行處理和索引，並將它們輸入到 Pinecone 向量數據庫中。使用 LlamaIndex 的工具讀取並解析文檔，然後將文檔內容轉換為向量並存儲在 Pinecone 數據庫中。

### 3. `main.py`
此模塊基於 Streamlit 框架，建立一個用戶界面，允許用戶通過chatgpt與 LlamaIndex 文檔進行交互。用戶可以通過界面提問，
系統則根據已索引的數據庫提供回答。核心功能是提供一個直觀的視覺界面，讓用戶能夠方便地查詢文檔資料庫並獲取所需資訊

## teckstack
- **Streamlit**: 前端畫面。
- **Pinecone**: 用於儲存和indexing向量化的文本。
- **ChatGPT API**: 用於處理自然語言生成和理解。

## 安裝與設置
1. **clone**
   ```bash
   git clone https://github.com/yourgithub/llamaindex_practice.git
   cd llamaindex_practice
   pip install pipenv
2. **environment variable**
```bash
   PINECONE_API_KEY=your_pinecone_api_key
   PINECONE_ENVIRONMENT=your_pinecone_environment
3.
```bash
   pipenv run streamlit run main.py

