import streamlit as st
import random

# ------------------------------------------
# Recommendation rules
# ------------------------------------------
def recommend(use_case):
    uc = use_case.lower()
    vector_store = "FAISS"
    metric = "Cosine"
    embedding_model = "SBERT"

    if "chat" in uc or "chatbot" in uc or "real-time" in uc:
        vector_store = "Pinecone"
        embedding_model = "OpenAI (text-embedding-3-small)"

    if "multilingual" in uc:
        embedding_model = "LaBSE or Gemini"

    if "pdf" in uc or "offline" in uc or "low resource" in uc:
        vector_store = "FAISS"
        embedding_model = "MiniLM or SBERT"

    if "enterprise" in uc or "internal" in uc or "on-prem" in uc or "secure" in uc:
        vector_store = "Milvus or FAISS"
        embedding_model = "SambaNova"

    if "tag" in uc or "category" in uc or "classification" in uc:
        metric = "Jaccard"
        embedding_model = "MiniLM"

    if "long document" in uc or "summarize" in uc:
        metric = "Dot Product"
        embedding_model = "BGE or Claude"

    if "accuracy" in uc:
        vector_store = "Qdrant"
        metric = "Dot Product"

    return vector_store, metric, embedding_model

# ------------------------------------------
# Dynamic explanation
# ------------------------------------------
def explain_config(vector_store, metric, model):
    explanations = []

    if vector_store.lower() == "faiss":
        explanations.append("🔹 **Vector Store: FAISS** — Lightweight, open-source, and works well **offline**. Ideal for rural or low-resource environments.")
    elif "pinecone" in vector_store.lower():
        explanations.append("🔹 **Vector Store: Pinecone** — Scalable and fast. Great for **real-time chatbots**.")
    elif "milvus" in vector_store.lower():
        explanations.append("🔹 **Vector Store: Milvus** — Designed for **enterprise/private deployments** with secure vector search.")
    elif "qdrant" in vector_store.lower():
        explanations.append("🔹 **Vector Store: Qdrant** — Modern, fast, and optimized for **high accuracy** use cases.")

    if metric.lower() == "cosine":
        explanations.append("🔹 **Similarity Metric: Cosine** — Ideal for measuring **semantic similarity**, especially with sentence-level embeddings.")
    elif metric.lower() == "dot product":
        explanations.append("🔹 **Similarity Metric: Dot Product** — Efficient for **normalized embeddings** and ranking similarity quickly.")
    elif metric.lower() == "jaccard":
        explanations.append("🔹 **Similarity Metric: Jaccard** — Best for comparing **sets** like tags or keyword overlap.")

    model_lower = model.lower()
    if "minilm" in model_lower:
        explanations.append("🔹 **Embedding Model: MiniLM** — Small, fast model suitable for **offline or low-compute devices**.")
    if "labse" in model_lower:
        explanations.append("🔹 **Embedding Model: LaBSE** — Excellent for **multilingual search**, covering 100+ languages.")
    if "sambanova" in model_lower:
        explanations.append("🔹 **Embedding Model: SambaNova** — Ideal for **enterprise**, on-prem, or regulated environments.")
    if "sbert" in model_lower:
        explanations.append("🔹 **Embedding Model: SBERT** — Well-suited for **semantic search** and lightweight deployment.")

    return "\n\n".join(explanations)

# ------------------------------------------
# Streamlit UI
# ------------------------------------------
st.set_page_config(page_title="📊 RAG Recommender", page_icon="🧠")
st.title("📊 RAG Application Recommender")

st.markdown("""
Enter your **RAG application use case**. We'll:
- ✅ Recommend the best vector store, similarity metric, and embedding model
- 🧠 Explain **why** they are ideal for your use case
""")

use_case = st.text_area("📝 Describe your RAG use case:")

# On Click
if st.button("🔍 Recommend"):
    if not use_case.strip():
        st.warning("❗ Please enter a use case.")
    else:
        # Recommend
        vs, sim, model = recommend(use_case)
        st.subheader("📌 Recommended RAG Configuration")
        st.markdown(f"- **Vector Store**: `{vs}`")
        st.markdown(f"- **Similarity Metric**: `{sim}`")
        st.markdown(f"- **Embedding Model**: `{model}`")

        # Explain
        st.subheader("📘 Why This Setup Works")
        explanation = explain_config(vs, sim, model)
        st.markdown(explanation)
