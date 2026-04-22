import streamlit as st

# ================= CONFIG =================
st.set_page_config(
    page_title="Mukul Mehta | Machine Learning Portfolio",
    layout="wide"
)

# ================= SIDEBAR =================
st.sidebar.image("assets/profile.jpg", width=200)
st.sidebar.title("Mukul Mehta")

st.sidebar.markdown("""
Almora, India  
Email: mehtamukul689@gmail.com  
Phone: +91 6397233573
""")

st.sidebar.markdown("""
LinkedIn: https://linkedin.com/in/mukul-mehta-574123283  
GitHub: https://github.com/Mukul9112003  
Portfolio: https://mukulportfolio.streamlit.app/
""")

# Resume download
try:
    with open("Resume.pdf", "rb") as f:
        st.sidebar.download_button(
            label="Download Resume",
            data=f,
            file_name="Mukul_Mehta_Resume.pdf"
        )
except:
    st.sidebar.info("Upload Resume.pdf to enable download.")

# Navigation
page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Skills",
        "Experience",
        "Salary Intelligence Platform",
        "Hybrid Movie Recommendation System",
        "Telecom Churn Prediction",
        "Certifications",
        "Contact"
    ]
)

# ================= HOME =================
if page == "Home":

    st.title("Mukul Mehta")

    st.write("""
I am currently pursuing a Bachelor of Computer Applications and I am interested
in machine learning engineering and MLOps.

Most of my projects focus on building complete machine learning systems instead
of only training models. I enjoy working across the entire workflow including
data preprocessing, feature engineering, model training, experiment tracking,
API development, and deployment.

This portfolio contains several projects where I implemented end-to-end machine
learning pipelines using tools such as Python, Scikit-learn, FastAPI, Docker,
MLflow, and AWS.
""")

    st.write("---")

    st.subheader("Main Areas of Interest")

    st.write("""
Machine Learning Systems  
MLOps and Model Deployment  
Recommendation Systems  
Data Engineering for ML  
Building APIs for Machine Learning Models
""")

# ================= SKILLS =================
elif page == "Skills":

    st.title("Technical Skills")

    st.subheader("Programming")

    st.write("""
Python  
SQL
""")

    st.subheader("Data Analysis and Visualization")

    st.write("""
Pandas  
NumPy  
Matplotlib  
Seaborn  
Excel  
Power BI
""")

    st.subheader("Machine Learning")

    st.write("""
Scikit-learn  
Random Forest  
XGBoost  
Feature Engineering  
Model Evaluation  
TF-IDF  
Collaborative Filtering  
SMOTE  
SHAP
""")

    st.subheader("Backend Development")

    st.write("""
FastAPI  
Streamlit  
Pydantic  
REST APIs  
Requests
""")

    st.subheader("Databases")

    st.write("""
MySQL  
MongoDB  
PyMySQL  
PyMongo
""")

    st.subheader("MLOps and DevOps")

    st.write("""
Docker  
MLflow  
CI/CD pipelines  
GitHub Actions  
DVC
""")

    st.subheader("Cloud and Infrastructure")

    st.write("""
AWS EC2  
AWS S3  
Linux
""")

    st.subheader("Software Tools")

    st.write("""
Git  
GitHub  
YAML  
Logging
""")

    st.subheader("Computer Science")

    st.write("""
Data Structures and Algorithms  
Solved 100+ problems on LeetCode
""")

# ================= EXPERIENCE =================
elif page == "Experience":

    st.title("Experience")


# ================= SALARY PROJECT =================
elif page == "Salary Intelligence Platform":

    st.title("Salary Intelligence Platform")

    st.write("""
    This project is an end-to-end machine learning system designed to analyze salary datasets
    and predict salary ranges based on factors such as experience, job role, and industry.

    The goal of the project was to build a production-style machine learning pipeline rather
    than simply training a model inside a notebook.
    """)

    st.subheader("Problem Statement")

    st.write("""
    Salary data is often scattered across different platforms and is difficult to analyze
    in a structured way. This system processes salary datasets and provides both predictions
    and analytics to help understand compensation trends.
    """)

    st.subheader("Machine Learning Pipeline")

    st.write("""
    The project follows a modular architecture where each stage of the workflow is separated
    into independent components.

    1. Data ingestion and storage using a MySQL database.
    2. Data validation to ensure dataset consistency.
    3. Data preprocessing and feature engineering using Pandas and Scikit-learn.
    4. Model training using ensemble algorithms such as Random Forest and XGBoost.
    5. Experiment tracking using MLflow.
    6. API development using FastAPI.
    7. Containerization using Docker.
    8. Deployment on AWS EC2.
    9. Business analytics dashboards using Power BI.
    """)

    st.subheader("System Architecture")

    st.write("Architecture diagram will be added here.")

    st.image("assets/salary_architecture.png")

    st.subheader("Model Performance")

    st.write("Performance comparison charts will be added here.")

    st.image("assets/salary_model_performance.png")

    st.subheader("MLflow Experiment Tracking")

    st.write("Screenshots of experiment runs will be added here.")

    st.image("assets/mlflow_salary.png")

    st.subheader("Power BI Dashboard")

    st.write("Screenshots of dashboards showing salary insights will be added here.")

    st.image("assets/salary_dashboard.png")

    st.subheader("Technologies Used")

    st.write("""
    Python  
    Pandas  
    Scikit-learn  
    Random Forest  
    XGBoost  
    MLflow  
    FastAPI  
    Docker  
    MySQL  
    Power BI  
    AWS EC2  
    GitHub Actions
    """)

    st.write("GitHub Repository:")
    st.write("github.com/Mukul9112003/project1_Salary_Intelligence_Platform")

# ================= RECOMMENDER =================
elif page == "Hybrid Movie Recommendation System":

    st.title("Hybrid Movie Recommendation System")

    st.write("""
This project implements a hybrid recommendation system that combines collaborative
filtering and content-based filtering to generate personalized movie recommendations.
""")

    st.subheader("Problem Statement")

    st.write("""
Traditional recommendation systems often rely on a single technique, which can lead
to poor recommendations when data is sparse. The goal of this project was to combine
multiple approaches to improve recommendation quality.
""")

    st.subheader("Recommendation Architecture")

    st.write("""
The recommendation system follows a two-stage approach.

Stage 1: Candidate generation using collaborative filtering.

Stage 2: Content-based filtering using TF-IDF to analyze movie metadata.

Stage 3: Ranking models such as Logistic Regression and Support Vector Machine
determine the final recommendation order.
""")

    st.subheader("Recommendation Pipeline")

    st.write("""
1. Generate candidate movies based on user similarity.
2. Transform movie descriptions using TF-IDF vectorization.
3. Calculate similarity between movies.
4. Apply ranking models to select the best recommendations.
5. Track experiments using MLflow.
""")

    st.subheader("System Architecture")

    st.write("Architecture diagram will be added here.")

    st.image("assets/recommender_architecture.png")

    st.subheader("Evaluation Metrics")

    st.write("""
Precision@K  
Recall@K  
NDCG@K
""")

    st.write("Evaluation graphs will be added here.")

    st.image("assets/recommendation_metrics.png")

    st.subheader("MLflow Experiment Tracking")

    st.write("Screenshots of model comparison experiments will be added here.")

    st.image("assets/mlflow_recommendation.png")

    st.subheader("Deployment")

    st.write("""
The recommendation system is exposed through a FastAPI service that returns
real-time movie recommendations. A Streamlit interface allows users to interact
with the system.

The application is containerized using Docker.
""")

    st.write("GitHub Repository:")
    st.write("github.com/Mukul9112003/Project2_Hybrid_Movie_Recommendation_System")

# ================= CHURN =================
elif page == "Telecom Churn Prediction":

    st.title("Telecom Customer Churn Prediction System")

    st.write("""
This project predicts which telecom customers are likely to leave a service provider.
Customer churn prediction helps companies identify high-risk customers and take
preventive action.
""")

    st.subheader("Dataset Challenge")

    st.write("""
The dataset used in this project is highly imbalanced. The number of customers who churn
is much smaller than the number of customers who stay.

This imbalance can cause machine learning models to ignore the minority class.
""")

    st.subheader("Machine Learning Pipeline")

    st.write("""
1. Data preprocessing and cleaning using Pandas.
2. Handling class imbalance using the SMOTE technique.
3. Training classification models including Random Forest and XGBoost.
4. Tracking experiments using MLflow.
5. Model explainability using SHAP.
""")

    st.subheader("System Architecture")

    st.write("Architecture diagram will be added here.")

    st.image("assets/churn_architecture.png")
    st.subheader("MLflow Experiment Tracking")

    st.write("Screenshots of model comparison experiments will be added here.")

    st.image("assets/mlflow_churn.png")

    st.subheader("Model Performance")

    st.write("Performance comparison graphs will be added here.")

    st.image("assets/churn_model_performance.png")

    st.subheader("Model Explainability")

    st.write("SHAP visualizations will be added here.")

    st.image("assets/shap_visualization.png")

    st.subheader("Deployment")

    st.write("""
A Streamlit application was built so users can input customer information and
receive churn predictions in real time.

The system was containerized using Docker.
""")

    st.write("GitHub Repository:")
    st.write("github.com/Mukul9112003/project3_Telecom_Customer_Churn_Prediction_System")

# ================= CERTIFICATIONS =================
elif page == "Certifications":

    st.title("Certifications")

    st.write("""
Supervised Machine Learning: Regression and Classification  
Coursera
""")

    st.write("""
CS50's Introduction to Programming with Python  
Harvard University
""")

# ================= CONTACT =================
elif page == "Contact":

    st.title("Contact")

    st.write("""
If you would like to discuss projects, collaboration, or opportunities,
you can reach me through the following:

Email: mehtamukul689@gmail.com  
Phone: +91 6397233573  

LinkedIn:
https://linkedin.com/in/mukul-mehta-574123283

GitHub:
https://github.com/Mukul9112003
""")

# ================= FOOTER =================
st.write("---")
st.write("© Mukul Mehta")