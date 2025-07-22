import streamlit as st
import pandas as pd

# Set up the Streamlit app
st.set_page_config(page_title="RAG Recommender", page_icon="🔍")
st.title("🔍 RAG Model & Similarity Metric Recommender")

st.markdown("""
This tool helps you choose the best **model** and **similarity metric** for your RAG (Retrieval-Augmented Generation) application based on your use case.
""")

# User inputs
use_case = st.selectbox("📌 Select Use Case", [
    "Question Answering",
    "Chatbot",
    "Summarization",
    "Document Search",
    "Tag/Topic Matching"
])

vector_store = st.selectbox("📦 Choose Vector Store", [
    "FAISS",
    "Pinecone",
    "Weaviate",
    "Qdrant",
    "Elasticsearch"
])

similarity_metric = st.selectbox("📏 Select Similarity Metric", [
    "Cosine",
    "Euclidean",
    "Dot Product",
    "Manhattan",
    "Jaccard"
])

# Model recommendation logic
def recommend_model(use_case, vector_store):
    if use_case == "Question Answering":
        return "GPT-4" if vector_store != "Elasticsearch" else "LLaMA 3"
    elif use_case == "Chatbot":
        return "GPT-4 Turbo"
    elif use_case == "Summarization":
        return "Claude 3"
    elif use_case == "Document Search":
        return "Mistral 7B"
    else:
        return "Any open-source model + lightweight embedding (e.g., MiniLM)"

# Metric explanation
def explain_metric(metric):
    explanations = {
        "Cosine": "✅ Best for semantic embeddings like BERT, SBERT, OpenAI. Measures angle between vectors, scale-invariant.",
        "Euclidean": "📐 Measures straight-line distance. Use when vector magnitude matters (less common in NLP).",
        "Dot Product": "⚡ Fast inner product for large-scale retrieval. Often used in FAISS. Normalize vectors first.",
        "Manhattan": "↔️ Adds absolute differences between dimensions. Rare in NLP; better for sparse vectors.",
        "Jaccard": "🔢 Compares binary/categorical data — useful for tags, keywords, or topic sets."
    }
    return explanations.get(metric, "ℹ️ No explanation available.")

# Show recommendation
if st.button("🔎 Show Recommendation"):
    model = recommend_model(use_case, vector_store)
    explanation = explain_metric(similarity_metric)

    st.subheader("✅ Recommended Setup:")
    st.markdown(f"**Model:** `{model}`")
    st.markdown(f"**Vector Store:** `{vector_store}`")
    st.markdown(f"**Similarity Metric:** `{similarity_metric}`")
    st.info(explanation)

# Optional: Metric usage explanation (expander)
with st.expander("📘 What Do These Metrics Mean?"):
    st.markdown("""
**🔹 Cosine Similarity**  
Measures angle between vectors (direction), ignoring length.  
Best for: semantic similarity using BERT/SBERT/OpenAI embeddings.

**🔹 Euclidean Distance**  
Measures straight-line distance between points.  
Use when magnitude matters (e.g., dense image vectors).

**🔹 Dot Product**  
Calculates inner product. Works best on normalized vectors.  
Fast and used in FAISS or Pinecone for large-scale RAG.

**🔹 Manhattan Distance**  
Adds absolute differences between vector dimensions.  
Rare in NLP, better for sparse and tabular embeddings.

**🔹 Jaccard Similarity**  
Measures overlap of binary sets.  
Great for tag/keyword/topic matching.
""")

# Optional: Table comparing metrics
st.subheader("📊 Metric Comparison Table")

data = {
    "Metric": ["Cosine", "Euclidean", "Dot Product", "Manhattan", "Jaccard"],
    "Best For": [
        "Semantic NLP embeddings (BERT, SBERT)",
        "Dense vectors, image/text mix",
        "Large-scale vector search (FAISS)",
        "Sparse/high-dimensional data",
        "Set/tag/category comparison"
    ],
    "Typical Use Cases": [
        "QA, Chatbots, Semantic Search",
        "Document Search, Embedding Distance",
        "FAISS, Pinecone RAG Retrieval",
        "Rare in NLP; tabular/sparse",
        "Topic Matching, Tag Search"
    ]
}

df = pd.DataFrame(data)
st.table(df)
