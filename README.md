Customer Perosnality Segmentation
==============================
Description:

Customer Personality Analysis is a detailed analysis of a company’s ideal customers. It helps a business to better understand its customers and makes it easier for them to modify products according to the specific needs, behaviors and concerns of different types of customers.

Customer personality analysis helps a business to modify its product based on its target customers from different types of customer segments. For example, instead of spending money to market a new product to every customer in the company’s database, a company can analyze which customer segment is most likely to buy the product and then market the product only on that particular segment.

Attributes:

People

ID: Customer's unique identifier
Year_Birth: Customer's birth year
Education: Customer's education level
Marital_Status: Customer's marital status
Income: Customer's yearly household income
Kidhome: Number of children in customer's household
Teenhome: Number of teenagers in customer's household
Dt_Customer: Date of customer's enrollment with the company
Recency: Number of days since customer's last purchase
Complain: 1 if the customer complained in the last 2 years, 0 otherwise

Products

MntWines: Amount spent on wine in last 2 years
MntFruits: Amount spent on fruits in last 2 years
MntMeatProducts: Amount spent on meat in last 2 years
MntFishProducts: Amount spent on fish in last 2 years
MntSweetProducts: Amount spent on sweets in last 2 years
MntGoldProds: Amount spent on gold in last 2 years

Promotion

NumDealsPurchases: Number of purchases made with a discount
AcceptedCmp1: 1 if customer accepted the offer in the 1st campaign, 0 otherwise
AcceptedCmp2: 1 if customer accepted the offer in the 2nd campaign, 0 otherwise
AcceptedCmp3: 1 if customer accepted the offer in the 3rd campaign, 0 otherwise
AcceptedCmp4: 1 if customer accepted the offer in the 4th campaign, 0 otherwise
AcceptedCmp5: 1 if customer accepted the offer in the 5th campaign, 0 otherwise
Response: 1 if customer accepted the offer in the last campaign, 0 otherwise

Place

NumWebPurchases: Number of purchases made through the company’s website
NumCatalogPurchases: Number of purchases made using a catalogue
NumStorePurchases: Number of purchases made directly in stores
NumWebVisitsMonth: Number of visits to company’s website in the last month

Target

Need to perform clustering to summarize customer segments.

Kaggle link: https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis
==============================
Project Organization


    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    |
    ├── data
    │   ├── source         <- The source data sets in case the source files are downloaded from source systems.
    │   ├── raw            <- The original, immutable data dump.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── external       <- Data from third party sources.
    |
    ├── logs               <- Logs generated when program is running
    │
    ├── models             <- Trained and serialized models, model predictions, model summaries, or vectorizers
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    |
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        ├── app.py         <- Initiator for flask app
        ├── exception.py   <- Custom exception handler
        ├── logger.py      <- Custom logger
        ├── utils.py       <- Set of custom utilities functions
        │
        ├── data           <- Scripts to extract data and transform data
        │   ├── data_ingestion.py
        │   └── data_transformation.py
        │
        ├── pipelines      <- Scripts to train models and then use trained models to make
        │   │                 predictions
        │   ├── train_pipeline.py
        │   └── predict_pipeline.py
        │
        └── templates      <- Web pages to host to take real time inputs and provide predictions
            ├── index.html
            └── home.html


--------
