import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score



# this function predicts tumors type based on the features of the dataset
def tumor_classifier(
        radius_mean,
        perimeter_mean,
        area_mean,
        smoothness_mean,
        compactness_mean,
        concavity_mean,
        symmetry_mean
    ):
    # the data set is available at the url below.
    URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0231EN-SkillsNetwork/datasets/cancer.csv"

    # Load the data into a dataframe from the URL
    df = pd.read_csv(URL)

    # Clean the data
    df["diagnosis"].fillna(df["diagnosis"].mode()[0], inplace=True)
    df["radius_mean"].fillna(df["radius_mean"].mean(), inplace=True)
    df["perimeter_mean"].fillna(df["perimeter_mean"].mean(), inplace=True)
    df["area_mean"].fillna(df["area_mean"].mean(), inplace=True)
    df["smoothness_mean"].fillna(df["smoothness_mean"].mean(), inplace=True)
    df["compactness_mean"].fillna(df["compactness_mean"].mean(), inplace=True)
    df["concavity_mean"].fillna(df["concavity_mean"].mean(), inplace=True)
    df["symmetry_mean"].fillna(df["symmetry_mean"].mean(), inplace=True)

    # data visualization using seaborn
    sns.pairplot(df, hue="diagnosis")
    plt.savefig("cancer_pairplot.png")

    # define features(X) and target(Y) and split the data into training(80%) and testing(20%)
    X = df[["radius_mean", "perimeter_mean", "area_mean", "smoothness_mean", "compactness_mean", "concavity_mean", "symmetry_mean"]]
    Y = df["diagnosis"]
    X=X.values
    Y=Y.values
    # Split the data into training(80%) and testing(20%)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    # Create a logistic regression model
    MODEL = LogisticRegression()

    # Fit the model to the training data (X_train, Y_train)
    MODEL.fit(X_train, Y_train)

    # Make predictions using the testing data
    Y_pred = MODEL.predict(X_test)

    # Calculate the accuracy of the model
    accuracy = accuracy_score(Y_test, Y_pred)
    print(f'\nOutput Section :\nModel Accuracy : {accuracy * 100:.2f}%')

    # predict the output
    predicted_value = MODEL.predict([[radius_mean,perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, symmetry_mean]])

    print(f'predicted Tumor Type : {predicted_value[0]}\n')





# this is the main function
if __name__ == "__main__":
    print("\n###### Welcome to the Tumor Classification Predictor #####")
    print("\nExample input :\nradius_mean = 13.45, perimeter_mean = 86.6, area_mean = 555.1, smoothness_mean = 0.1022,\ncompactness_mean = 0.08165, concavity_mean = 0.03974, symmetry_mean = 0.1638\n")

    # calling the function
    while True:
        print("Choose an option : ")
        print("1. Predict Tumor Type")
        print("2. Exit")
        option=int(input("Enter your choice : "))
        if option == 1:
            print("\nInput Section :")
            radius_mean = float(input("Enter the radius_mean : "))
            perimeter_mean = float(input("Enter the perimeter_mean : "))
            area_mean = float(input("Enter the area_mean : "))
            smoothness_mean = float(input("Enter the smoothness_mean : "))
            compactness_mean = float(input("Enter the compactness_mean : "))
            concavity_mean = float(input("Enter the concavity_mean : "))
            symmetry_mean = float(input("Enter the symmetry_mean : "))
            tumor_classifier(radius_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, symmetry_mean)
        elif option == 2:
            print("\nThanks for using the Tumor Classification Predictor. Have a nice day!")
            break
        else:
            print("\nPlease enter a valid option.")



