import streamlit as st
import numpy as np
from src.data_management import load_house_prices_data  # pylint: disable=E401

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


def page_correlation_study_body():

    # load data
    df = load_house_prices_data()

    # hard copied from correlation study notebook
    vars_to_study = ['1stFlrSF',
                     'GarageArea',
                     'GarageYrBlt',
                     'GrLivArea',
                     'KitchenQual',
                     'MasVnrArea',
                     'OverallQual',
                     'TotalBsmtSF',
                     'YearBuilt',
                     'YearRemodAdd']

    st.write("### House Sales Price Study")

    st.info(
        f"#### Business Requirement 1\n"
        f"The client is interested in discovering how house attributes "
        f"correlate with sales prices. Therefore, the client "
        f"expects data visualizations of the correlated variables against "
        f"the sales price.\n\n"
    )

    # inspect data
    if st.checkbox("Inspect House Prices Dataset"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 10 rows.")

        st.write(df.head(10))

    st.write("---")

    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to better "
        f"understand how the variables are correlated to `SalePrice`.\n\n"
        f"The most correlated variables are: **{vars_to_study}**"
    )

    # Text based on "Sale Price Correlation Study" notebook
    st.info(
        f" Based on the analysis of the correlation coefficients and "
        f"examination of the corresponding plots, it is indicated that:\n\n "
        f"* **1stFlrSF**, **GarageArea**, **GarageYrBlt**, **TotalBsmtSF** "
        f"are showing a moderate correlation with the sales price.\n"
        f"* **OverallQual**, **GrLivArea** are showing a high correlation "
        f"with the sales price.\n"
        f"* **KitchenQual** is showing a consiredable higher sales price for "
        f"properties with kitchens in excellent condition.\n"
        f"* **MasVnrArea** is showing a low-moderate correlation with "
        f"the sales price.\n"
        f"* From 1980 onwards, an acceleration in price increases can "
        f"be observed in **YearBuilt** and **YearRemodAdd**.\n\n"
        f"**Correlation-Interpretation:**\n\n"
        f"* from 0,1 to 0,25 low correlation.\n"
        f"* from 0,26 to 4,9 low-moderate correlation.\n"
        f"* from 0,5 to 0,6 moderate correlation.\n"
        f"* from 0,7 to 0,9 high correlation.\n"

    )

    st.write(
        f"* Scatter plots showing correlation between each variable and the "
        f"'SalePrice':"
    )

    # Copied from "Sale Price Correlation Study" notebook
    df_eda = df.filter(vars_to_study + ['SalePrice'])

    # Individual plots per variable
    if st.checkbox("Sale Price Correlation Per Variable"):
        sale_price_per_variable(df_eda, vars_to_study)

    st.write(
        f"* Heatmap showing the correlation between the relevant variables: "
    )

    # Heatmap plot
    if st.checkbox("Show Heatmap Correlation"):
        plot_heatmap(df_eda, vars_to_study)


# Iteration with SalePrice
def sale_price_per_variable(df_eda, vars_to_study):
    target_var = 'SalePrice'
    for col in vars_to_study:
        plot_numerical(df_eda, col, target_var)
        st.write("\n\n")


# code copied and modified from "02 - Churned Customer Study" notebook
def plot_numerical(df_eda, col, target_var):

    fig = plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df_eda, x=col, y='SalePrice')
    plt.title(f"{col} vs SalePrice", fontsize=20, y=1.05)
    plt.xlabel(col)
    plt.ylabel('SalePrice')
    st.pyplot(fig)


# Code taken and modified from repository: heritage-housing-issues - Imangnp
def plot_heatmap(df_eda, vars_to_study):

    heatmap_vars = df_eda.copy()

    # Calculate the correlation matrix
    correlation_matrix = heatmap_vars.corr()

    # Plot the heat map
    fig = plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True)
    plt.title("Correlation Matrix", fontsize=20)
    st.pyplot(fig)
