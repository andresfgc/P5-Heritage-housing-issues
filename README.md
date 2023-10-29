# Heritage Housing Issues

This is a machine learning project focused on housing price prediction in Ames, Iowa.

![Dashboard](/media/Dashoard-heritage-housing-issues.JPG)

## Table of Contents

- [Heritage Housing Issues](#heritage-housing-issues)
  - [Table of Contents](#table-of-contents)
  - [Dataset Content](#dataset-content)
  - [Terms and Jargons](#terms-and-jargons)
  - [Business Requirements](#business-requirements)
    - [Epics \& User Stories](#epics--user-stories)
  - [Hypothesis and how to validate?](#hypothesis-and-how-to-validate)
  - [The rationale to map the business requirements to the Data Visualisations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualisations-and-ml-tasks)
  - [ML Business Case](#ml-business-case)
  - [Dashboard Design](#dashboard-design)
    - [Page 1: Quick project summary](#page-1-quick-project-summary)
    - [Page 2: Sales price correlation Study](#page-2-sales-price-correlation-study)
    - [Page 3: House sales price predictor](#page-3-house-sales-price-predictor)
    - [Page 4: Project hypothesis](#page-4-project-hypothesis)
    - [Page 5: ML: Predict sales price](#page-5-ml-predict-sales-price)
  - [Fixed Bugs](#fixed-bugs)
  - [Unfixed Bugs](#unfixed-bugs)
  - [Deployment](#deployment)
    - [Heroku](#heroku)
  - [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace. 
- The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|

## Terms and Jargons

- Variables: Refers to the different attributes of a house, such as Second floor square feet, Total square feet of basement area,lot size in square feet or original construction date.
- Target Variable: The target variable in this study is the 'SalePrice'. It is the value at which the properties were sold.

## Business Requirements

The client, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, has requested us to  help in maximising the sales price for the inherited properties.

Although our client has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa and has provided us with the following requests:

- 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
- 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.

Epics and user stories were created for the correct management of customer requirements.

### Epics & User Stories

- Information gathering and data collection.
  - US1: As a data practitioner, I want to be able to collect the public dataset for house prices in Ames, Iowa. So that I can use it for further analysis.

- Data visualization, cleaning, and preparation.
  - US2: As a data practitioner, I want to use data cleaning techniques to prepare data for better Correlation-interpretation of the variables and training.

- Model training, optimization and validation.
  - US3: As a data professional, I want to use feature engineering techniques to improve the training process of the algorithms and obtain the highest possible R2.

- Dashboard planning, designing, and development.
  - US4: As a data practitioner, I want to create a dashboard with pages to show the client the correlation study, the predicted price of her inherited homes and the trained algorithm for future predictions.

- Dashboard deployment and release.
  - US5: As a data professional, I want to be able to deploy the app on Heroku so the customer can access it.

## Hypothesis and how to validate?

- Hypothesis 1: Size has a significant influence in sales price.
  - the analysis of variables related to square metres suggests that size is a relevant factor for the proper valuation of the property.

- Hypothesis 2: Newer properties have higher prices.
  - The historical analysis between sales price and date of construction gives an indication that new homes tend to have higher prices than older ones..

- Hypothesis 3: The quality of the kitchen affects property value.
  - We observed a high correlation between kitchen quality and sales price. It may suggest that homes with excellent kitchen quality ratings may command a higher price.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

- **Business Requirement 1:** Data visualization and Correlation Sudy
  - We will inspect the data related to the SalePrice variable.
  - We will conduct a correlation study to understand better how variables are correlated to Sales Price.
  - We will plot the main variables against the SalePrice variable to visualize insights.

- **Business Requirement 2:** Regression Analysis
  - As we want to predict the sales prices for the inherited house, we will use a regression analysis to achieve it.
  - We will use the ExtraTreesRegressor with its respective adjusment to achieve at least R of 0.75.
  - Once the ML pipeline is trained adn evaluated, it can be used to predict prices for the inherited houses and any other house in Ames, Iowa.

## ML Business Case

- **Predict Sales price**
  - We want a ML model to predict the sales price for the inherited houses from our client.
  - We also want a ML model to predict the sales prices for houses in Ames, Iowa.
  - The model achieves the agreed R2 score of at least 0.75 on the train as well as on the test set.
  - The Dashboard will provide the client the relevant information to understand the correlation between variables and sales price and analyse future house in Ames, Iowa

## Dashboard Design

### Page 1: Quick project summary

- Quick project summary
- Project Terms & Jargon
- Describe Project Dataset
- State Business Requirements
![Quick Project Summary](/media/quick-project-summry.JPG)

### Page 2: Sales price correlation Study

- This pages was created to answer business requirement 1.
- It contains a data visualization of the correlated variables against the sales price.
- With the button function "Inspect House Price Dataset" it lets the client to have a look at the row dataset.
- It also shows insights related to the top 10 correlated variables.
- For better analysis the client has two oder buttons where she can see the correlations represented in scatter plots and a heatmap.
![Sales Price Correlation Study](/media/sales-price-correlation-study-1.JPG)
![Inspect House Prices Dataset](/media/sales-price-correlation-study-2.JPG)
![Most correlated variables and scatter plots](/media/sales-price-correlation-study-3.JPG)
![Heatmap](/media/sales-price-correlation-study-4.JPG)

### Page 3: House sales price predictor

- This pages was created to answer business requirement 2.
- It shows the attributes for the 4 houses and their respective predicted sales prices.
- It also displays a message showing the sum of all predicted sales prices of the four inherited houses.
- The button "Predict Sales Price" let the user send the given information to the ML pipeline in order to get a new prediction.
![House Sales Price Predictor](/media/house-sales-price-predictor.JPG)

### Page 4: Project hypothesis

- During the correlation study it was possible to investigate the following hypothesis:
- Hypothesis 1: Size has a significant influence in sales price.
  - The analysis of variables related to square metres suggests that size is a relevant factor for the proper valuation of the property.
- Hypothesis 2: Newer properties have higher prices.
  - The historical analysis between sales price and date of construction gives an indication that new homes tend to have higher prices than older ones.
- Hypothesis 3: The quality of the kitchen affects property value.
  - We observed a high correlation between kitchen quality and sales price. It may suggest that homes with excellent kitchen quality ratings may command a higher price.
- ![Project Hypothesis](/media/project-hypothesis.JPG)

### Page 5: ML: Predict sales price

- Considerations and conclusions after the pipeline is trained
- Present ML pipeline steps
- Feature importance
- Pipeline performance
![ML: Predict Sales Price](/media/ml-predict-sales-price-1.JPG)
![Features and their importance](/media/ml-predict-sales-price-2.JPG)
![Pipeline Performance](/media/ml-predict-sales-price-3.JPG)
![Regression Evaluation plots](/media/ml-predict-sales-price-4.JPG)

## Fixed Bugs

- Line too long (95 > 79 characters) pycodestyle(E501)
![Line too Long](/media/fix_bug_1.JPG)
  - Solution
![Line too long solution](/media/fix_bug_solution_1.JPG)

## Unfixed Bugs

- Pylint(import-error): It says that the page is unable to import:
  - src.data_management
  - src.machine_learning.evaluate_regression
- It is only a visual error from pylint, the page is actually able to import data from src
![pylint(import-error)](/media/ml-predict-sales-price-1.JPG)

- Warnings: pandas.In64Index and Passing a set as an index are deprecated.
![warning-1](/media/unfixed_bugs_2.JPG)
![warning-2](/media/unfixed_bugs_3.JPG)

## Deployment

### Heroku

- The App live link is: [heritage-housing-issues-afgc](https://heritage-housing-issues-afgc-4e55c09890ec.herokuapp.com/)
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
   ![Heroku - login and create App](/media/heroku-steps-1.JPG)
2. At the Deploy tab, select GitHub as the deployment method
   ![Deploy tab - Select GitHub](/media/heroku-steps-2.JPG)
3. Select the repository name and click Search. Once it is found, click Connect
   ![Connect Repository](/media/heroku-steps-3.JPG)
4. To deploy from GitHub it was necessary to use install the Heroku CLI
   ![Download Heroku CLI](/media/heroku-steps-4.JPG)
5. Login to the terminal with $ heroku login -i. E-mail and API Token instead of password.
   ![Login CLI terminal](/media/heroku-steps-5.JPG)
6. Since the repository already exits in heroku it is necessary to get it first $ git:remote -a heritage-housing-issues-afgc
   ![git:remote](/media/heroku-steps-6.JPG)
7. Then write the following comman to change the heroku version of your app $ heroku stack:set heroku-20
   ![change version app](/media/heroku-steps-7.JPG)
8. finally the repository can be deployed by the GitHub connection inside the Heroku deploy section at the botton of the page
   ![Deploy on Heroku](/media/heroku-steps-8.JPG)

## Main Data Analysis and Machine Learning Libraries

- Numpy - Used to generate arrays for the correlation to generate heatmaps.
- Pandas - Used to convert CSV data into data frames to support data manipulation and analysis.
- pandas_profiling - Used to  generate reports on the input DataFrame such as statistical values and variable types.
- seaborn - Used to generate charts for the correlation histograms, heatmap and feature importance.
- matplotlib - Used to generate plots to visualize data and present findings.
- Feature-engine - Use to apply data engineering techniques for categorical and numerical transformations.
- Scikit-Learn - Used to train and evaluate ML model performance.
- Streamlit - Used to create the dashboard.
- Jupyter: Used to create the notebooks for DataCollection, DataCleaning, FeatureEngineering, Correlation Study and Modeling and Evaluation.

## Credits

- Code Institute for the repository template and [Churnometer project](https://github.com/Code-Institute-Solutions/churnometer).
- Dataset obtained from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data)
- Code Institute Chapter [Data Analysis & Machine Laarning Toolkit](https://learn.codeinstitute.net/courses/course-v1:code_institute+CI_DA_ML+2021_Q4/courseware/d186ae95191f48e9a2151559c7e6f85d/771e4d181ce0413c87572c1baa903190/)
- I want to thank [Amare](https://github.com/Amareteklay/heritage-housing-issues) and [Iman](https://github.com/Imangnp/heritage-housing-issues) for allowing me to learn about their work. Thanks to them I was able to improve my project.

## Acknowledgements

- I would specially like to thank my mentor Mo Shami, for his good advice and guidance.
