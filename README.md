# 📊 RAG Application Recommender

This is a simple and intelligent **Streamlit web app** that recommends optimal components for building **Retrieval-Augmented Generation (RAG)** pipelines based on your use case.

Just describe your RAG scenario (e.g., chatbot, PDF reader, enterprise search), and it suggests the **best vector store**, **similarity metric**, and **embedding model**, along with explanations for each choice.

---

## 🚀 Introduction

**RAG (Retrieval-Augmented Generation)** is a powerful approach for combining external knowledge sources with LLMs. However, selecting the right configuration (vector database, similarity metric, and embedding model) depends heavily on your specific use case.

This tool simplifies that process using basic NLP rules to provide:
- ✅ Suitable vector database (e.g., FAISS, Pinecone, Milvus)
- ✅ Ideal similarity metric (Cosine, Jaccard, Dot Product)
- ✅ Optimal embedding model (MiniLM, SBERT, LaBSE, OpenAI)

---

## 🛠 Installation

1. **Clone the repository**:
   ```bash
git clone https://github.com/meghaharikant/Rag_recommender.git
cd Rag_recommender
