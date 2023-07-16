# Retail-Forecast

- Situation: a big retail company with two stores and 10 products by stored needed to predict sales for the next 8 days at store-product level.

- Task: a 3-year historic SQL database was provided and needed to be cleaned, analyzed, preprocessed and used for making the forecast prediction for this window.

- Action: the process was wrapped on several functions using Python Pandas and Sklearn with the goal to build the final datamart for prediction through different processes such as data wrangling, data quality, EDA, variable creating (assessing the Intermittent demand), feature transformation (using OneHot and Target Encoding), variable preselection (using Mutual Information) and later training (using TimeSeriesSplit for cross validation and Random Search), evaluating (on a Validation dataset) and finally executing the HistGradientBoost Regression model to predict the 8 days window prediction.

- Results: after testing the correct functioning of the model we relied on MAE (5.45), it was decided to carry on with execution which showed the model successfully predicted the sales for the 8-days window thanks to the recursive forecast function.
