import streamlit as st


def page_project_hypothesis_body():

    st.write("### Project Hypotheses and Validation")

    # conclusions taken from "03 - Correlation_Study" notebook
    st.success(
        f"**Hypothesis 1**: Size has a significant influence in sales price.\n"
        f"* the analysis of variables related to square metres suggests "
        f"that size is a relevant factor for the proper "
        f"valuation of the property.\n\n"

        f"**Hypothesis 2**: Newer properties have higher prices.\n"
        f"* The historical analysis between sales price and date of "
        f"construction gives an indication that new homes tend to have "
        f"higher prices than older ones.\n\n"

        f"**Hypothesis 3**: The quality of the kitchen "
        f"affects property value.\n"
        f"* We observed a high correlation between kitchen quality "
        f"and sales price. It may suggest that homes with "
        f"excellent kitchen quality ratings may command a higher price."
    )
