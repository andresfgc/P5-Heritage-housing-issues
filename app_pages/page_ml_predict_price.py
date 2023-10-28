import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_house_prices_data, load_pkl_file
from src.machine_learning.evaluate_regression import (
    regression_performance, regression_evaluation, regression_evaluation_plots
)


# Code taken and modified from walktrough Project 02 - Churnometer
def page_ml_predict_price_body():

    # load pipeline files
    version = 'v2'
    best_regressor_pipeline = load_pkl_file(
        "outputs/ml_pipeline/predict_price/" +
        f"{version}/pipeline_clf.pkl"
    )
    sale_price_importance = plt.imread(
        "outputs/ml_pipeline/predict_price/" +
        f"{version}/features_importance.png"
    )
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_price/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_price/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_price/{version}/y_train.csv")
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_price/{version}/y_test.csv")

    st.write("### ML: Predict Sale Price")
    # display pipeline training summary conclusions
    st.info(
        f"* this ML pipeline was designed to at least achieve a R2 Score "
        f"of 0.75 on both the train and test set "
        f"when predicting the price of a property.\n"
        f"**ExtraTreesRegressor** demonstrated consistent performance."
        f" It achieved an **R2 score** of **1.0** on the train set and "
        f"**0.796** on the test set. \n"
        f"* Considering this results, the objective was to improve "
        f"the pipeline by using only the best variables for "
        f"its optimal development.."
    )
    st.write("---")

    # show pipelines
    st.write("* **ML pipeline to predict house sales price**")
    st.write(best_regressor_pipeline)
    st.write("---")

    # show best features
    st.write("* **The features the model was trained and their importance:**")
    st.write(X_train.columns.to_list())
    st.image(sale_price_importance)
    st.write("---")

    # code taken and modified from Scikit-Lean Unit 4
    st.write("### Pipeline Performance")
    regression_performance(X_train=X_train, y_train=y_train,
                           X_test=X_test, y_test=y_test,
                           pipeline=best_regressor_pipeline)
    st.write("---")

    # Plot predicted versus actual sale price for train and test sets
    st.write("**Regression Evaluation plots:**")
    st.write(
        f"* comparison between prediction and actual values "
        f"of the train & test set:\n\n"
        f"(It may take some time while charging)"
    )
    regression_evaluation_plots(X_train=X_train, y_train=y_train,
                                X_test=X_test, y_test=y_test,
                                pipeline=best_regressor_pipeline,
                                alpha_scatter=0.5)

    st.write(
        f"* The red line is the corresponding the expected value to "
        f"predict while the blue value is the actual value.\n"
        f"* The closer the blue point is to the red line, the higher the "
        f"effectiveness of the model and the further away from the red line, "
        f"the lower the effectiveness of the model.."
    )
