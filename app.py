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
📍 **Meerut, India**  
📧 **mehtamukul689@gmail.com**  
📞 **+91 6397233573**
""")

st.sidebar.markdown(
    """
🔗 [LinkedIn](https://linkedin.com/in/mukul-mehta-574123283)  
🐙 [GitHub](https://github.com/Mukul9112003)  
🌐 [Live Portfolio](https://mukulportfolio.streamlit.app/)
"""
)

# ===== Resume Download =====
try:
    with open("resume.pdf", "rb") as f:
        st.sidebar.download_button(
            "📄 Download Resume",
            f,
            file_name="Mukul_Mehta_Resume.pdf"
        )
except Exception:
    st.sidebar.warning("⚠️ Upload resume.pdf to enable download.")

# ===== Navigation =====
page = st.sidebar.radio(
    "📌 Navigation",
    [
        "🏠 Home",
        "💼 Salary Intelligence Platform",
        "🎬 Hybrid Recommender",
        "📊 Churn Prediction",
        "📜 Certifications"
    ]
)

# ================= HOME =================
if page == "🏠 Home":
    st.title("👋 Hello, I'm Mukul Mehta")
    st.subheader("BCA Student | Machine Learning & MLOps Enthusiast")

    st.markdown("""
I am a **BCA undergraduate** focused on building **end-to-end production-ready ML systems**
using **FastAPI, Docker, MLflow, and AWS**.

I specialize in transforming machine learning models into **scalable real-world applications**.
""")

    st.markdown("---")

    st.header("🛠 Technical Skills")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
**Programming & Databases**
- Python  
- SQL  
- MySQL  

**Machine Learning**
- Scikit-learn  
- Random Forest  
- XGBoost  
- NLP  
- Feature Engineering  
""")

    with col2:
        st.markdown("""
**MLOps & Deployment**
- FastAPI  
- Streamlit  
- Docker  
- MLflow  
- AWS EC2  
- CI/CD (GitHub Actions)  

**Tools**
- Git & GitHub  
- Power BI  
- DVC  
""")

    st.markdown("---")

    st.header("🚀 What I Bring")

    st.markdown("""
✅ End-to-end ML pipeline development  
✅ Production deployment with Docker & FastAPI  
✅ Experiment tracking with MLflow  
✅ Strong focus on real-world ML systems  
""")

# ================= SALARY PROJECT =================
elif page == "💼 Salary Intelligence Platform":
    st.title("💼 Salary Intelligence Platform (End-to-End Data & ML System)")

    st.markdown("### 📌 Project Overview")
    st.markdown("""
Built a production-ready end-to-end machine learning system to predict salaries
and generate business intelligence insights from structured data.
""")

    st.markdown("### ⚙️ Tech Stack")
    st.markdown("""
FastAPI • Docker • AWS EC2 • MLflow • MySQL • Power BI • GitHub Actions
""")

    st.markdown("### 🔄 End-to-End Pipeline")
    st.markdown("""
1. Data ingestion and storage using MySQL  
2. EDA and feature engineering  
3. Model training with MLflow experiment tracking  
4. REST API development using FastAPI  
5. Docker containerization  
6. CI/CD automation with GitHub Actions  
7. Deployment on AWS EC2  
8. Business dashboard creation in Power BI  
""")

    st.markdown("### 🚀 Key Achievements")
    st.markdown("""
- Built scalable ML pipeline for salary prediction  
- Implemented MLflow for experiment tracking and model versioning  
- Automated deployment using Docker and CI/CD  
- Delivered business insights through Power BI dashboards  
""")

    st.markdown("🔗 **GitHub:** https://github.com/Mukul9112003/project1_Salary_Intelligence_Platform")

# ================= RECOMMENDER =================
elif page == "🎬 Hybrid Recommender":
    st.title("🎬 Hybrid Movie Recommendation System")

    st.markdown("### 📌 Project Overview")
    st.markdown("""
Designed a two-stage hybrid recommendation system combining collaborative
filtering and content-based filtering to improve recommendation relevance.
""")

    st.markdown("### ⚙️ Tech Stack")
    st.markdown("""
Python • TF-IDF • SVM • FastAPI • Docker • Streamlit
""")

    st.markdown("### 🔄 System Architecture")
    st.markdown("""
1. Candidate generation using collaborative filtering  
2. Content-based refinement using TF-IDF similarity  
3. SVM-based meta-ranking  
4. Evaluation using ranking metrics  
5. Real-time inference via FastAPI  
6. Dockerized deployment with Streamlit UI  
""")

    st.markdown("### 📊 Evaluation Metrics")
    st.markdown("""
- Precision@K  
- Recall@K  
- NDCG@K  
""")

    st.markdown("🔗 **GitHub:** https://github.com/Mukul9112003/Project2_Hybrid_Movie_Recommendation_System")

# ================= CHURN =================
elif page == "📊 Churn Prediction":
    st.title("📊 Telecom Customer Churn Prediction System")

    st.markdown("### 📌 Project Overview")
    st.markdown("""
Developed an end-to-end telecom churn prediction system focused on identifying
high-risk customers using imbalanced learning and explainable AI.
""")

    st.markdown("### ⚙️ Tech Stack")
    st.markdown("""
Python • Random Forest • XGBoost • SMOTE • SHAP • MLflow • Docker • Streamlit
""")

    st.markdown("### 🔄 Pipeline")
    st.markdown("""
1. Data preprocessing and cleaning  
2. SMOTE class balancing  
3. Model training  
4. MLflow experiment tracking  
5. SHAP explainability  
6. Docker containerization  
7. Streamlit deployment  
""")

    st.markdown("🔗 **GitHub:** https://github.com/Mukul9112003/project3_Telecom_Customer_Churn_Prediction_System")

# ================= CERTIFICATIONS =================
elif page == "📜 Certifications":
    st.title("📜 Certifications")

    st.markdown("""
🎓 **Supervised Machine Learning: Regression & Classification — Coursera**  
🔗 https://www.coursera.org/verify  

🎓 **CS50’s Introduction to Programming with Python — Harvard University**  
🔗 https://cs50.harvard.edu/certificates/
""")

# ================= FOOTER =================
st.markdown("---")
st.markdown("© 2026 **Mukul Mehta** | Built with ❤️ using Streamlit")