Project Goal:

This project focuses on predicting laptop prices using machine learning techniques. I performed exploratory data analysis and visualizations in a Jupyter Notebook, followed by building a regression model using RandomForestRegressor from sklearn. ensemble. Hyperparameter tuning was done via GridSearchCV to optimize model performance.

Problem Statement:

Determining a fair price for a laptop can be challenging for both buyers and sellers due to the wide variety of brands, configurations, and rapidly changing market dynamics. Manually assessing these factors to estimate a price is often subjective and time-consuming. This project aims to solve this by providing an objective approach to laptop price estimation.


Solution:

To address this problem, I implemented a machine learning-based solution with the following components:

Data Collection & Preparation: A dataset (Laptop_price.csv) containing information about various laptops, including features like 'Brand', 'Processor_Speed', 'RAM_Size', 'Storage_Capacity', 'Screen_Size', 'Weight', and their corresponding 'Price', was utilized.

Exploratory Data Analysis (EDA): The dataset was thoroughly analyzed to understand its structure, identify relationships between features and price, and prepare it for modeling. This involved:

. Data cleaning (handling missing values and duplicates, though none were found in this dataset).

. Statistical summaries and correlation analysis to identify important features.

. Visualizations (bar charts, pie charts) to better understand data distributions and trends (e.g., average price by brand).

Feature Selection: Key features deemed most influential for price prediction ('Processor_Speed', 'RAM_Size', 'Storage_Capacity') were selected as inputs for the model.

Model Development & Tuning:

. RandomForestRegressor from the scikit-learn library was chosen as the predictive model due to its robustness and ability to handle non-linear relationships.

. The dataset was split into training and testing sets to evaluate model performance on unseen data.

. GridSearchCV was employed for hyperparameter tuning, systematically searching for the optimal settings for max_depth, max_features, 
  and n_estimators to enhance the model's accuracy.

Evaluation: The tuned model's performance was assessed using the Mean Absolute Error (MAE) metric, which measures the average difference between predicted prices and actual prices on the test set.

Model Deployment (via Streamlit App):

. The trained and tuned GridSearchCV model (containing the best RandomForestRegressor) was serialized and saved using joblib (as 
  rf_model.pkl).

. a user-friendly web application was developed using Streamlit, allowing users to input laptop specifications and receive real-time 
  price predictions from the loaded model.

Tools: Python, Jupyter, Pandas, Matplotlib, Scikit-learn, Streamlit, Joblib, Numpy.
