import streamlit as st


def page_summary_body():

    st.write("### Quick Project Summary\n")

    st.write(
        f"This project is an ML app specifically developed for the "
        f"visualization and prediction of house prices in Ames, Iowa.\n\n"
        f"The app offers users the following functionalities:\n"
        f"* **Correlation Analysis:** The application "
        f"allows users to identify "
        f"the correlation between house attributes and the sale price.\n"
        f"* **Sale Price Prediction:** The application provides a predictive "
        f"model that enables users to obtain accurate estimates for "
        f"the sale price.\n"
    )

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Terms & Jargons**\n"
        f" * **Variables**: Refers to the different attributes of a house, "
        f"such as Second floor square feet, Total square feet of "
        f"basement area,"
        f"lot size in square feet or original construction date.\n"
        f" * **Target Variable**: The target variable in this study is the "
        f"'SalePrice'. It is the value at which the properties were sold.\n\n"

        f"**Project Dataset**\n"
        f"* The dataset is a group of properties that have been sold in Ames, "
        f"Iowa. It contains 24 distinct features for each property, "
        f"which have the potential to impact the price.\n"
        f"The dataset was obtained from "
        f"[Kaggle]"
        f"(https://www.kaggle.com/datasets/codeinstitute/housing-prices-data)."
        f"\n"
    )

    # Link to README file, users can have access to full project documentation
    st.write(
        f"For additional information, please visit and **read** the"
        f" **[Project's README file]"
        f"(https://github.com/andresfgc/heritage-housing-issues)**. "
    )

    # copied from README file - "Business Requirements" section
    st.success(
        f"The project has 2 business requirements:\n\n "
        f"1 - The client is interested in discovering how house attributes "
        f"correlate with sale prices. Therefore, the client "
        f"expects data visualizations of the correlated variables against "
        f"the sale price.\n\n"
        f"2 - The client is interested in predicting the house sale prices "
        f"from her 4 inherited houses, and any other house in Ames, Iowa."
    )
