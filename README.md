# Skinlytics-
This repository is dedicated to the all data projects related with Skinlytics main project

## Project Description: 
Dash plotly web dashboard with interactive visualizations on Ingredient List Score profile, Similarity Matrix and Recommender system engine based on ingredient list
This notebook collection is a small prototype for part I of the project and intends to outline most of the steps, commands and packages necessary for this part of the project in a smaller part of the data (SPF Product category, total 50 products).

Live version of the dashboard can be accessed here: http://anaritasantos.pythonanywhere.com/

## Workflow Part 1 - Ingredient Profile Analysis & Product Recommendation

#### 1.Dash DataTable:
Create an interactive table of the targeted product list, with Brand, Product Name, Full ingredient list, price, quantity, price/ml. As the project moves forward more columns would be added here (ex: review sentiment, main product benefits based on the ingredient list, ect.);
#### 2.Ingredient List Processing & Visualization:
Access the data, clean the ingredient list, classify the ingredients by role/function  and generate a spider radar visualization of ingredient profile per one product;

#### 3.Recommender:
Calculate the similarity matrix based for products based on common active ingredients and generate a recommended list. This engine will become more sofisticated as the project progresses, including more revire generated variables and options to adjust the engine parameters ;

#### 4.Dash App:
Create a Product Analysis Dashboard on Dash using the previous elements (spider radar chart,recommender and dash table);

## Workflow Part 2 - Product Review Analysis
1. Collect and transform the data from different sources on reviews about the products listed

2. Create first iteration of the sentiment and topic modeling of these reviews 

3. Create Data Exploration visualizations on the reviews and integrate them into the web dashboard 


## Sources:
Listing of sources I used to help me with domain knowledge, data cleaning and code for visualizations and the recommender system.

#### Ingredient List Research & Classification
https://incidecoder.com/
https://cosmetics.specialchem.com/
https://www.hautschutzengel.de/

#### Product Recommender System
https://www.kaggle.com/code/eward96/skincare-recommendation-engine

#### Dash web application programming
Dash Tutorial videos on Youtube (CharmingData channel: https://www.youtube.com/@CharmingData)
Dash bootstrap Cheatsheet: https://dashcheatsheet.pythonanywhere.com/

#### Other Resources:
Dash Documentation, Medium Articles, Chat-GTP
