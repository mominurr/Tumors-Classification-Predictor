# Tumor Classification Predictor

## Project Overview

This project focuses on building a predictive model for classifying tumors into different types based on their characteristics. It aims to develop a robust machine learning model that can accurately classify tumors into categories such as "Malignant" and "Benign."

## Functions and Features

### tumor_classifier

The "tumor_classifier" function is a comprehensive utility for performing tumor classification. It takes multiple input parameters representing tumor characteristics and provides two key outputs: model accuracy and predicted tumor type.

### Function Workflow

The function performs the following steps in its workflow:

1. **Data Loading and Cleaning:**

   - Load the tumor classification dataset using the Pandas library.
   - Perform data cleaning to handle missing values, duplicates, or any other data quality issues.

2. **Data Visualization:**

   - Utilize Matplotlib and Seaborn to create data visualizations, including scatter plots and histograms. These visualizations help users understand the distribution of tumor characteristics.

3. **Model Training:**

   - Train a machine learning classifier on the cleaned dataset. The classifier's goal is to predict the tumor type (e.g., "Malignant" or "Benign") based on tumor characteristics.

4. **Making Predictions:**

   - Use the trained classifier to make predictions on new data. The input parameters for prediction are characteristics of the tumor.

5. **Model Evaluation:**

   - Evaluate the performance of the trained model using accuracy and other relevant metrics.

## Video Presentation

To see a demonstration of our Tumor Classification Predictor project in action, please watch the following video:

[Demo Video](https://youtu.be/DRGinTnXzN4)

In this video, we provide a step-by-step walkthrough of how to use our project's features, objectives, and results. Feel free to watch the video to get a better understanding of our project.

## Dataset

### Dataset Overview

This project utilizes a dataset containing information about tumor characteristics. The dataset includes the following features:

- **radius_mean:** Mean of the radius of the tumor.
- **perimeter_mean:** Mean of the perimeter of the tumor.
- **area_mean:** Mean of the area of the tumor.
- **smoothness_mean:** Mean of the smoothness of the tumor.
- **compactness_mean:** Mean of the compactness of the tumor.
- **concavity_mean:** Mean of the concavity of the tumor.
- **symmetry_mean:** Mean of the symmetry of the tumor.

### Target Variable

The target variable in this dataset is:

- **diagnosis:** This variable indicates whether the tumor is "Malignant" or not, possibly denoting "Benign."

This dataset serves as the foundation for building a predictive model to classify tumors into categories based on their characteristics.


## Dependencies

This project requires the following Python libraries:

- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn (for visualization)

You can install these dependencies using pip:

      pip install numpy pandas scikit-learn matplotlib seaborn

## Usage

To use this project, follow these steps:

1. Ensure you have Python installed on your machine.
2. Clone the project repository to your local machine:

     ```bash
     git clone https://github.com/mominurr/Tumors-Classification-Predictor.git
     cd Iris-Flower-Classification-Predictor
     python flower_classifications_predictor.py

##Author:
[Mominur Rahman](https://github.com/mominurr)
