import streamlit as st

# ================= CONFIG =================
st.set_page_config(
    page_title="Mukul Mehta | ML Portfolio",
    page_icon="💻",
    layout="wide"
)

# ================= SIDEBAR =================
st.sidebar.image("assets/profile.jpg", width=200)
st.sidebar.title("Mukul Mehta")

st.sidebar.markdown("""
📍 **Haldwani, India**  
📧 **mehtamukul689@gmail.com**  
📞 **6397233573**
""")

st.sidebar.markdown(
    """
🔗 [LinkedIn](https://linkedin.com/in/mukul-mehta-574123283)  
🐙 [GitHub](https://github.com/)
"""
)

with open("resume.pdf", "rb") as f:
    st.sidebar.download_button(
        "📄 Download Resume",
        f,
        file_name="Mukul_Mehta_Resume.pdf"
    )

# ================= MAIN =================
st.title("👋 Hello, I'm Mukul Mehta")
st.subheader("Machine Learning | Deep Learning | Model Deployment")

st.markdown("""
I am a **BCA student** with strong hands-on experience in **Machine Learning, Deep Learning, 
and production-ready model deployment** using **FastAPI, Docker, and AWS**.

I focus on building **real-world ML systems**, not just notebooks.
""")

st.markdown("---")

# ================= SKILLS =================
st.header("🛠 Technical Skills")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
**Programming**
- Python
- SQL

**ML & DL**
- Scikit-learn
- XGBoost
- CNN
- NLP
""")

with col2:
    st.markdown("""
**Web & Deployment**
- FastAPI
- Streamlit
- Docker
- AWS (EC2)

**Databases & Tools**
- MySQL
- MongoDB
- Git & GitHub
""")

st.markdown("---")

# ================= PROJECTS =================
st.header("📂 Projects")

# ---- Project 1 ----
st.subheader("🎬 Hybrid Movie Recommendation System")
st.markdown("""
**Tech:** Python, Scikit-learn, NLP, FastAPI, Docker, AWS  

- Hybrid recommendation using collaborative filtering + TF-IDF content similarity  
- Cascade re-ranking approach for better relevance and cold-start handling  
- FastAPI backend for real-time inference  
- Dockerized and deployed on AWS  

🔗 **Links:**  
- GitHub: https://github.com/  
- Live Demo: https://example.com
""")

# ---- Project 2 ----
st.subheader("📊 Telecom Customer Churn Prediction System")
st.markdown("""
**Tech:** Python, XGBoost, SMOTE, SHAP, Streamlit  

- Built churn classifier with full preprocessing pipeline  
- Solved class imbalance using SMOTE  
- Added SHAP explainability for business insights  
- Interactive Streamlit dashboard  

🔗 **Links:**  
- GitHub: https://github.com/  
- Live Demo: https://example.com
""")

# ---- Project 3 ----
st.subheader("🤟 Sign Language to Speech & Text Converter")
st.markdown("""
**Tech:** CNN, OpenCV, Streamlit, FastAPI, Docker, AWS  

- CNN-based ASL alphabet recognition system  
- Data augmentation & batch normalization for generalization  
- Streamlit UI with FastAPI inference backend  
- Dockerized deployment on AWS  
- Converted predictions to text and speech  

🔗 **Links:**  
- GitHub: https://github.com/  
- Live Demo: https://example.com
""")

st.markdown("---")

# ================= CERTIFICATIONS =================
st.header("📜 Certifications")

st.markdown("""
- **Supervised Machine Learning: Regression & Classification** — Coursera  
  🔗 https://www.coursera.org/verify  

- **CS50’s Introduction to Programming with Python** — Harvard University  
  🔗 https://cs50.harvard.edu/certificates/
""")

st.markdown("---")

# ================= STRENGTHS =================
st.header("🚀 What I Bring")

st.markdown("""
- End-to-end ML pipeline development  
- Model deployment using APIs & containers  
- Strong ML fundamentals with production mindset  
- Clear understanding of real-world constraints  
""")

# ================= FOOTER =================
st.markdown("---")
st.markdown(
    "© 2025 **Mukul Mehta** | Built with ❤️ using Streamlit"
)
