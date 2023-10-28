import streamlit as st


def page_project_hypothesis_body():

    st.write("### Project Hypotheses and Validation")

    # conclusions taken from "03 - Correlation_Study" notebook
    st.success(
        f"* the analysis of variables related to square metres suggests "
        f"that size is a relevant factor for the proper "
        f"valuation of the property.\n\n"

        f"* The historical analysis between sales price and date of "
        f"construction gives an indication that new homes tend to have "
        f"higher prices than older ones..\n\n"

        f"* We observed a high correlation between overall quality "
        f"(OverallQual) and sales price. It may suggest that homes with "
        f"high quality ratings may command a higher price."
    )
