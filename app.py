import streamlit as st
st.set_page_config(
    page_title="Mukul Mehta | Machine Learning Portfolio",
    layout="wide"
)
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
""")

st.sidebar.info("Resume available below https://drive.google.com/drive/folders/1ewAghfICcgmfLWwadzk7U7MvKag5D7TZ?usp=sharing")

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
Solved 50+ problems on LeetCode
""")
elif page == "Experience":
    st.title("Experience")
elif page == "Salary Intelligence Platform":
    st.title("Salary Intelligence Platform")
    st.write("""
    This project is an end-to-end machine learning system designed to predict salaries
    based on job-related features such as job title, location, company, and required skills.

    The focus of this project is not just model building, but designing a complete
    production-ready ML pipeline with deployment, experiment tracking, and cloud integration.
    """)
    st.subheader("Problem Statement")
    st.write("""
    Salary information is often inconsistent and difficult to analyze across platforms.
    This system aims to provide structured predictions and insights by leveraging machine learning,
    enabling better understanding of compensation trends for different job roles.
    """)
    st.subheader("Machine Learning Pipeline")
    st.write("""
    The project follows a modular and scalable architecture where each stage of the pipeline
    is handled independently.
    1. Data ingestion from MongoDB.
    2. Data validation to ensure schema consistency and data quality.
    3. Data transformation and feature engineering.
    4. Model training using XGBoost.
    5. Model evaluation and selection of the best-performing model.
    6. Experiment tracking using MLflow.
    7. Model storage and versioning using AWS S3.
    8. API development using FastAPI.
    9. Containerization using Docker.
    10. CI/CD pipeline using GitHub Actions.
    11. Deployment on AWS EC2 using Docker containers.
    """)
    st.subheader("System Architecture")
    st.write("""
    The system is designed as an end-to-end MLOps pipeline integrating data, model lifecycle,
    and deployment in a production environment.
    """)
    st.image("assets/salary_architecture.png")
    st.subheader("Model Performance")
    st.write("""
    The model performance is evaluated using appropriate metrics and tracked across experiments
    to ensure reproducibility and improvement over time.
    """)
    st.image("assets/salary_model_performance.png")
    st.subheader("MLflow Experiment Tracking")
    st.write("""
    MLflow is used to track experiments, including parameters, metrics, and model versions,
    enabling systematic comparison and model selection.
    """)
    st.image("assets/mlflow_salary.png")
    st.subheader("Cloud Integration")
    st.image("assets/salary_ci.png")
    st.image("assets/salary_ci.png")
    st.write("""
    - AWS S3 is used for storing trained models.
    - AWS ECR is used to store Docker images.
    - AWS EC2 is used for hosting the FastAPI application.
    """)
    st.image("assets/salary_s3_bucket.png")
    st.image("assets/salary_fastapi_1.png")
    st.image("assets/salary_fastapi_2.png")
    st.image("assets/salary_ec2.png")
    st.image("assets/salary_ecr.png")
    st.subheader("Technologies Used")
    st.write("""
    Python  
    Pandas  
    Scikit-learn  
    XGBoost  
    MLflow  
    FastAPI  
    Docker  
    MongoDB  
    AWS S3  
    AWS EC2  
    AWS ECR  
    GitHub Actions  
    """)
    st.link_button("Watch Full Demo", "https://drive.google.com/file/d/1GaczRkUPAstKR3wBWCJUwjJqzqHB4RHR/view?usp=sharing")
    st.write("Quick preview:")
    st.write("GitHub Repository:")
    st.write("https://github.com/Mukul9112003/Project2_Salary_Intelligence_Platform")
elif page == "Hybrid Movie Recommendation System":

    st.title("Hybrid Movie Recommendation System")

    st.write("""
This project is a Hybrid Movie Recommendation System that combines Collaborative Filtering 
and Content-Based Filtering to provide personalized movie suggestions.
The system first identifies similar users and movies using collaborative filtering, 
and then refines the recommendations using content-based techniques based on movie metadata.
""")

    st.subheader("Problem Statement")

    st.write("""
Traditional recommendation systems struggle with cold-start and sparse data problems. 
This project aims to improve recommendation accuracy by combining multiple techniques 
into a hybrid approach.
""")

    st.subheader("Approach")

    st.write("""
• Collaborative Filtering is used to generate initial movie recommendations based on user behavior.

• Content-Based Filtering (TF-IDF) is applied to analyze movie features such as genres, keywords, and descriptions.

• The final recommendations are generated by combining both approaches.
""")

    st.subheader("Pipeline")

    st.write("""
1. User-item interaction data is used for collaborative filtering.
2. Movie metadata is processed using TF-IDF vectorization.
3. Similarity scores are computed.
4. Results from both methods are combined to produce final recommendations.
""")

    st.subheader("Technologies Used")

    st.write("""
• Python  
• Pandas, NumPy  
• Scikit-learn  
• Streamlit  
""")
    

    st.write("""
The application is deployed using Streamlit, providing an interactive interface 
for users to get movie recommendations.
""")

    st.subheader("GitHub Repository")

    st.write("https://github.com/Mukul9112003/Project2_Hybrid_Movie_Recommendation_System")
elif page == "Telecom Churn Prediction":
    st.title(" Customer Churn Prediction System")
    st.markdown("End-to-End Machine Learning Project with MLOps (MLflow + Docker + AWS)")
    st.header(" Overview")
    st.write("""
    This project predicts whether a telecom customer is likely to churn or not.  
    The goal is to help businesses reduce customer loss by identifying high-risk users in advance.
    The project is built using an end-to-end MLOps pipeline, including:
    - Data ingestion and validation
    - Feature engineering
    - Model training and evaluation
    - Experiment tracking using MLflow
    - Deployment using Streamlit and Docker
    - Cloud deployment on AWS EC2
    """)
    st.header(" Key Features")
    st.markdown("""
    - ✔ End-to-end ML pipeline
    - ✔ Multiple model training & comparison
    - ✔ MLflow experiment tracking
    - ✔ Docker containerization
    - ✔ Streamlit interactive UI
    - ✔ AWS deployment (EC2)
    """)
    st.header(" System Architecture")
    st.image("assets/churn_architecture.png", use_column_width=True)
    st.write("""
    Pipeline Flow:
    1. Data is collected from telecom dataset
    2. Data preprocessing & feature engineering applied
    3. Multiple ML models are trained
    4. MLflow tracks experiments (metrics, parameters, artifacts)
    5. Best model is selected and registered
    6. Model is deployed using FastAPI + Streamlit
    7. Docker container is created and deployed on AWS EC2
    """)
    st.header("MLflow Experiment Tracking")
    st.image("assets/mlflow_ui.png", use_column_width=True)
    st.write("""
    MLflow is used to track:
    - Model parameters
    - Performance metrics (Accuracy, AUC)
    - Different experiments
    - Best model selection

    This helps in reproducibility and comparison of models.
    """)
    st.header(" Tech Stack")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        **Languages & Libraries**
        - Python
        - Pandas, NumPy
        - Scikit-learn
        - XGBoost
        """)

    with col2:
        st.markdown("""
        **Tools & Deployment**
        - MLflow
        - Streamlit
        - Docker
        - AWS EC2
        """)
    st.image("assets/churn_s3_bucket.png")
    st.image("assets/churn_fastapi_1.png")
    st.image("assets/churn_fastapi_2.png")
    st.image("assets/churn_ec2.png")
    st.image("assets/churn_ecr.png")
    st.subheader("Deployment")
    st.header(" Project Links")
    st.link_button("Watch Full Demo", "https://drive.google.com/file/d/1yFc5TUNCdXmk6RX3oQ0br4kHKk2K87Qb/view?usp=sharing")
    st.write("GitHub Repository:")
    st.write("https://github.com/Mukul9112003/Project3_Telecom_Customer_Churn_Prediction_System-")
    st.write("---")
    st.write("Built by Mukul Mehta")
# ================= CERTIFICATIONS =================
elif page == "Certifications":

    st.title("Certifications")

    st.write("""
Supervised Machine Learning: Regression and Classification  
Coursera
""")
    st.info("Certifications available https://drive.google.com/drive/folders/1ewAghfICcgmfLWwadzk7U7MvKag5D7TZ?usp=sharing")
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

st.write("---")
st.write("© Mukul Mehta")