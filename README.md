<p align="center">
  <img width="100" src="https://github.com/nursena8/BankCustomerProject/assets/115145369/31f9aae3-a1e5-4ad6-88a3-0e88241096e2" height="100">
  <img width="100" src="https://github.com/nursena8/BankCustomerProject/assets/115145369/eb84b568-80b2-4ca6-ac76-01980fdd3646" height="100">
  <img width="100" src="https://github.com/nursena8/BankCustomerProject/assets/115145369/652ce86c-b288-4550-980c-b1d758222c18" height="100">
  <img width="100" src="https://github.com/nursena8/BankCustomerProject/assets/115145369/537473f2-af80-4daa-8a9a-535a8a77ed06" height="100">
  <img width="100" src="https://github.com/nursena8/BankCustomerProject/assets/115145369/2e2fb617-49c9-466a-9b60-600c2025eaa0" height="100">
  <img width="100" src="https://github.com/nursena8/BankCustomerProject/assets/115145369/5882fb8f-e39d-4645-81c7-7d7f4b6605de" height="100">
</p>

# Bank Customer Churn Prediction Project

- This project is developed to predict the likelihood of churn for bank customers. The project has gone through various stages, including analyzing customer behaviors, making predictions with various models, and evaluating the performance of the model.

- The insights obtained from the project contribute to providing valuable feedback to the bank, enabling it to improve and retain customers. By understanding various customer behaviors, the bank can make informed decisions to enhance its services and address any areas that may lead to customer churn.

## Technologies Used:

1. **Python:**
   - The project is developed in Python, a language well-suited for data science projects due to its extensive library support and rapid prototyping capabilities.

2. **Pandas:**
   - Pandas, used for data manipulation and analysis, played a crucial role in processing and preprocessing the dataset.

3. **NumPy:**
   - NumPy, essential for numerical computations and data manipulation, facilitated various matrix operations and numerical tasks.

4. **Scikit-Learn:**
   - Scikit-Learn was employed for developing, training, and evaluating machine learning models, including the Gradient Boosting Classifier.

5. **Matplotlib and Seaborn:**
   - Matplotlib and Seaborn were used for data visualization, aiding in understanding and presenting the data during the exploratory data analysis (EDA) phase.

6. **Streamlit:**
   - [Streamlit](https://streamlit.io/) was utilized to create a live web application. It provides a user-friendly interface for efficient and rapid development.[Streamlit Website](https://bankcustomerproject-nevtbnfnsyxpwfuyksfxyq.streamlit.app/)

7. **Joblib:**
   - Joblib was chosen for saving and loading models, a crucial aspect for using the model in a live environment and managing deployment processes.

8. **Evident AI:**
   - [Evidently AI](https://www.evidentlyai.com) was employed to monitor and evaluate the model's performance continuously. This ensures ongoing assessment of the model's effectiveness in a live setting.
   - 
## Project Objectives

The main objectives of the project are as follows:
- Analyze and visualize customer behaviors.
- Develop various models to predict the likelihood of customer churn.
- Use different methods to select the best model and optimize it.
- Monitor and evaluate the model's performance using Evident AI.
## Overview

The main objectives of this project are as follows:

- **Analyze and Visualize Customer Behaviors:**
  - Utilized exploratory data analysis (EDA) techniques to gain insights into customer behaviors.
  - Visualized key metrics using Matplotlib and other data visualization tools.

- **Develop Predictive Models:**
  - Built various machine learning models to predict the likelihood of customer churn.
  - Explored classification and clustering models to capture different aspects of customer behavior.

- **Model Optimization:**
  - Employed different methods to select the best-performing model.
  - Utilized hyperparameter tuning and grid search to optimize model performance.

- **Monitoring with Evident AI:**
  - Incorporated Evident AI for model monitoring and evaluation.
  - Evaluated the model's performance over time and made necessary adjustments.

## Project Components

1. **Streamlit App (app.py):**
   - Deployed a Streamlit web application for live predictions.
   - Streamlit documentation: [Streamlit Documentation](https://docs.streamlit.io/)

2. **Monitoring with Evident AI:**
   - Monitored and evaluated model performance using Evident AI.
   - Evident AI documentation: [Evident AI Documentation](http://evidentlyai.com/))

3. **Classification and Clustering Models:**
   - Developed classification models to predict churn.
   - Explored clustering models to understand customer segmentation.

4. **Data Cleaning and Preprocessing:**
   - Cleaned and preprocessed the dataset to handle outliers and improve model accuracy.

## File Structure

- `app.py`: Streamlit web application for live predictions.
- `monitoring.ipynb`: Jupyter notebook for model monitoring using Evident AI.
- `project.ipynb`: Jupyter notebook for classification models.
- `project.ipynb`: Jupyter notebook for clustering models.
- `gbm_production_model.joblib`: save and use machine learning model.
- `gbm_model_prediction.py`:Predict model on your local.

## How to Download and Run

1. Clone the project repository to your computer:
- `git clone https://github.com/nursena8/BankCustomerProject.git`
2.Install depndecies
- `pip install -r requirements.txt`
3. Run the streamlit app
- `streamlit run app.py`
## Required HTML Files

The following HTML files are required for the project to function properly:

1. `assets/class_report.html`: This html created by evidently ai show us classification reports.
2. `assets/report.html`: This html created by evidently using Jpyter notebook shows us dataframe summary.
3. `assets/data_quality_report.html`:this html created by evidently using Jupyter notebook shows us dataset correlatio n.


## Streamlit Application
[MY streamlit Website :)](https://bankcustomerproject-nevtbnfnsyxpwfuyksfxyq.streamlit.app/)

<img width="828"   src="https://github.com/nursena8/BankCustomerProject/assets/115145369/11fdd03e-ea76-4feb-95e4-0d4e58534315">

To start the Streamlit application, follow these steps:

1. Install the Streamlit application:
     - `!pip install streamlit`
3. Run your streamlit project:
     - streamlit run app.py
3. Go your port you  that you defineded
     - http://localhost:8501
## Our project owerview

<img width="1190"  src="https://github.com/nursena8/BankCustomerProject/assets/115145369/c1fdf473-46a7-4410-93a4-64b67cff8f8a">

## Evidentlu ai 
1.Install evidentlu
 !pip install evidently
2. Import evidently
3. Monitor model performance metrics and useful data dashboards

## Future Work

1. **Continuous Improvement:**
   - Plan for continuous model improvement based on ongoing monitoring and feedback.

2. **Additional Features:**
   - Explore the incorporation of new features for enhanced predictive power.

3. **Advanced Models:**
   - Investigate the implementation of advanced machine learning models for further accuracy.

4. **Feedback Mechanism:**
   - Establish a feedback mechanism for customers to provide insights into their preferences.

## License
This project has MIT License

## Owner
Nursena Baykir

Would you like to Ask me anything?

- [Mail](nursenabaykir@gmail.com)
















