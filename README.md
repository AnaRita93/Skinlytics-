# Skinlytics project 

This repository is dedicated to all applications related with https://skinlytics.net/, a website I created dedicated to skincare products
review using analytics and data science. 



## Motivation 

I thought it would be fun to explore the data side of skin care and at the same time provide a visual interactive tool for anyone to use for their own analysis.With this project I also want to use my data skills to gather broader perspective on a product, considering its ingredients list, the sentiment and the topics around that product in the internet. 


## Goals 
In this project, the goal is create a set of dashboards with Dash and streamline them into the skinlytics website. 

#### 1. Ingredient Profile Dashboard
  - Gather a cleaned list of ingredients classified by their role in the formula
  - Create a score system based on the number of ingredients per role 
  - Create a spider chart visualization that showcases the ingredient list strog role-based points per product
  - Create a dashboard that allows you to recreate this visualizations based on filters and selections
  
#### 2. Product Comparison dashboard
  - Prepare a table with all the products with a category and their respective relevant comparison metrics
  - Create a dashboard that enables to interactively filter and subselect this table 
  
#### 3. Product recommender system and similarity matrix dashboard 
  - Create a product recommender system dashboard where the user can change the filtering/recommendation conditions
  - Visualize respective similarity matrix
  - Add filters and dimensions to the dashboard
  
#### 4. Sentiment and topic analysis dashboard 
- Data collection: webscrape review data on listed products 
   * from skincare retailers (Stylevana, Amazon,Look Fantastic, Sephora,other sites)
   * In specified review languages: english, german, other languages 
- Text data cleaning and pre-processing 
- Per each product classify sentiment and identify main topic

## Project workflow 

This repo is organized by the project workflow folders:

#### 1. Data Collection & Storage:
  * this folder contains SQL database files, the scripts that create the tables and store the data on a SQL database. 

#### 2. Data pre-processing:
  * this folder contains all the big pre-processing data parts of the project, which includes:
      - the ingredient list cleansing
      - the webscrapping and cleaning up of the data for sentiment analysis 

#### 3. Data modelation:
*   this folder is dedicated to all data modeling scripts, which includes:
      - Sentiment analysis script
      - Product recommender script  
  
#### 4.Data Analytics
  * this folder contains the scripts and notebooks related with data visualization and dashboards, which includes:
      - Script for Ingredient Profile visualization per product 
      - Script for Product comparison & recommendation dashboard
      - Script for Sentiment analysis dashboard
