<!-- ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png) -->

## Heritage Housing Issues

This is a machine learning project focused on housing price prediction in Ames, Iowa.

[Dashboard](/media/Dashoard-heritage-housing-issues.JPG)

## Table of Contents

[Dataset Content](#dataset-content)
[Tearms and Jargons](#terms-and-jargons)
[Business Requirements](#business-requirements)
[Hypothesis and how to validate](#hypothesis-and-how-to-validate)
[Rationale to map the business requirements to the data visualizations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualisations-and-ml-tasks)
[ML Business Case](#ml-business-case)
[Dashboard Design](#dashboard-design)
[Unfixed Bugs](#unfixed-bugs)
[Deployment](#deployment)
[Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)

## Dataset Content

* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace. 
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

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

* Variables: Refers to the different attributes of a house, such as Second floor square feet, Total square feet of basement area,lot size in square feet or original construction date.
* Target Variable: The target variable in this study is the 'SalePrice'. It is the value at which the properties were sold.

## Business Requirements

The client, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, has requested us to  help in maximising the sales price for the inherited properties.

Although our client has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa and has provided us with the following requests:

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
* 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.

Epics and user stories were created for the correct management of customer requirements.

### Epics & User Stories

* Information gathering and data collection.
  * US1: As a data practitioner, I want to be able to collect the public dataset for house prices in Ames, Iowa. So that I can use it for further analysis.

* Data visualization, cleaning, and preparation.
  * US2: As a data practitioner, I want to use data cleaning techniques to prepare data for better Correlation-interpretation of the variables and training.

* Model training, optimization and validation.
  * US3: As a data professional, I want to use feature engineering techniques to improve the training process of the algorithms and obtain the highest possible R2.

* Dashboard planning, designing, and development.
  * US4: As a data practitioner, I want to create a dashboard with pages to show the client the correlation study, the predicted price of her inherited homes and the trained algorithm for future predictions.

* Dashboard deployment and release.
  * US5: As a data professional, I want to be able to deploy the app on Heroku so the customer can access it.

## Hypothesis and how to validate?

* Hypothesis 1: Size has a significant influence in sales price.
  * the analysis of variables related to square metres suggests that size is a relevant factor for the proper valuation of the property.

* Hypothesis 2: Newer properties have higher prices.
  * The historical analysis between sales price and date of construction gives an indication that new homes tend to have higher prices than older ones..

* Hypothesis 3: The quality of the kitchen affects property value.
  * We observed a high correlation between kitchen quality and sales price. It may suggest that homes with excellent kitchen quality ratings may command a higher price.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

* **Business Requirement 1:** Data visualization and Correlation Sudy
  * We will inspect the data related to the SalePrice variable.
  * We will conduct a correlation study to understand better how variables are correlated to Sales Price.
  * We will plot the main variables against the SalePrice variable to visualize insights.

* **Business Requirement 2:** Regression Analysis
  * As we want to predict the sales prices for the inherited house, we will use a regression analysis to achieve it.
  * We will use the ExtraTreesRegressor with its respective adjusment to achieve at least R of 0.75.
  * Once the model is trained adn evaluated, it can be used to predict prices for the inherited houses and any other house in Ames, Iowa.

## ML Business Case

* In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course.

## Dashboard Design

* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items that your dashboard library supports.
* Eventually, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but eventually you needed to use another plot type)

## Unfixed Bugs

* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not valid reason to leave bugs unfixed.

## Deployment

### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

* Here you should list the libraries you used in the project and provide example(s) of how you used these libraries.

## Credits

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open Source site
- The images used for the gallery page were taken from this other open-source site

## Acknowledgements (optional)
* In case you would like to thank the people that provided support through this project.

