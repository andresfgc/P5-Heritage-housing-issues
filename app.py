import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_correlation_study import page_correlation_study_body
from app_pages.page_price_predictor import page_predict_price_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_ml_predict_price import page_ml_predict_price_body

# Create an instance of the app
app = MultiPage(app_name="Heritage Housing Sale Price")

# Add app pages using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Sales Price Correlation Study",
             page_correlation_study_body)
app.add_page("House Sales Price Predictor", page_predict_price_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)
app.add_page("ML: Predict Sales Price", page_ml_predict_price_body)

app.run()  # Run the app
