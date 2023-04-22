import os
import sys
from datetime import datetime
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

from dataclasses import dataclass
import numpy as np
import pandas as pd 
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler
from sklearn.compose import ColumnTransformer

@dataclass
class DataTransformationConfig:
    preprocessed_data_file = os.path.join('./data/processed' , 'processed_data.csv')
    vectorizer_obj_file = os.path.join('models', 'vectorizer.pkl')
    
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_preprocessed_data(self, raw_data_path):
        """
        This function is responsible for preprocessing data
        """
        try:
           # Read file
            data = pd.read_csv(raw_data_path)
            logging.info('Read raw data completed')
                        
            logging.info('Data transformation started')
            data.drop('Z_CostContact', inplace=True, axis=1)
            data.drop('Z_Revenue', inplace=True, axis=1)
            logging.info("Dropped 'Z_CostContact' & 'Z_Revenue'")
            
            data['Dt_Customer'] = pd.to_datetime(data['Dt_Customer'], format="%d-%m-%Y") 
            logging.info("Converted 'Dt_Customer' to date")
            
            income_median = data['Income'].median()
            data['Income'] = data['Income'].fillna(income_median)
            logging.info("Imputed 'Income' with median")
            
            data['Marital_Status'] = data['Marital_Status'].replace(['Absurd', 'Alone', 'YOLO'], 'Single')
            data['Marital_Status'] = data['Marital_Status'].replace('Widow', 'Divorced')
            logging.info("Cleaned 'Marital_Status'")
            
            data['Education'] = data['Education'].replace('2n Cycle', 'Basic')            
            logging.info("Cleaned 'Education'")
            
            # Removing outliers
            numerical_features = []
            for col in data.columns:
                if ((data[col].dtype != 'object') & (data[col].nunique()>2)):
                    numerical_features.append(col)

            #numerical_features.remove(['ID', 'Dt_Customer'])
            dict = {}
            for col in data[numerical_features]:
                percentile25 = data[col].quantile(0.25)
                percentile75 = data[col].quantile(0.75)
                IQR = percentile75 - percentile25
                upper_limit = percentile75 + IQR*5
                lower_limit = percentile25 - IQR*5
                dict["upper_lim_"+col] = upper_limit 
                dict["lower_lim_"+col] = lower_limit
                
            for feature in data[numerical_features]:
                data.drop(data[ (data[feature] < dict["lower_lim_"+feature]) | (data[feature] > dict["upper_lim_"+feature]) ].index, inplace=True)
                
            logging.info("Outliers are removed")
            
            # Some feature engineering
            data['Cust_Age'] = 2023 - data['Year_Birth']
            data['Cust_Tensure'] = (datetime.now() - data['Dt_Customer']).dt.days
            logging.info("Added 'Cust_Age' and 'Cust_Tenure' features")
            
            data.drop(['Dt_Customer', 'Year_Birth'], inplace=True, axis=1)
            logging.info("Dropped 'Dt_Customer' & 'Year_Birth'")
            
            logging.info("Preprocessing is completed")
            

            save_object(
                file_path = self.data_transformation_config.preprocessed_data_file,
                obj = data
            )
                        
            logging.info("Preprocessed data is saved")
            
            return (
                data
            )
            
        except Exception as e:
            raise CustomException(e, sys)
    
            
    def get_vectorizer_object(self):
        '''
        This function is responsible to return column vectorizer object
        '''
        try:
            categorical_features = ['Education', 'Marital_Status']
            numerical_features = ['Income', 'Kidhome', 'Teenhome', 'Recency', 'MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds', 'NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'AcceptedCmp1', 'AcceptedCmp2', 'Complain', 'Response', 'Cust_Age', 'Cust_Tensure']
            
            cat_pipeline = Pipeline(
                steps = [
                    ("ohe", OneHotEncoder())
                ]
                )
            
            num_pipeline = Pipeline(
                steps = [
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("normalizer", MinMaxScaler())
                ]
                )
            
            logging.info("Categorical columns: {0}".format(categorical_features))
            logging.info("Numerical columns: {0}".format(numerical_features))
            
            vectorizer = ColumnTransformer([
                                              ("cat_piplines", cat_pipeline, categorical_features),
                                              ("num_piplines", num_pipeline, numerical_features)
                                              ])
            
            return vectorizer
        
        except Exception as e:
            raise CustomException(e, sys)
    
    def initiate_data_transformation(self, raw_data_path):
        try:
            logging.info('Obtaining preprocessed data')
            
            preprocessed_data = self.get_preprocessed_data(raw_data_path) 
 
            logging.info('Obtained processed data')
            
            logging.info('Obtaining vectorizer object')

            vectorizer_obj = self.get_vectorizer_object()

            logging.info("Applying vectorizer object on processed data")
            
            categorical_features = ['Education', 'Marital_Status']
            numerical_features = ['Income', 'Kidhome', 'Teenhome', 'Recency', 'MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds', 'NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'AcceptedCmp1', 'AcceptedCmp2', 'Complain', 'Response', 'Cust_Age', 'Cust_Tensure']
            
            preprocessed_data_vectorized = vectorizer_obj.fit_transform(preprocessed_data)
                      
            
            logging.info("Vectorization is completed")
            
            save_object(
                file_path = self.data_transformation_config.vectorizer_obj_file,
                obj = vectorizer_obj
            )
            
            logging.info("Saved vectorizer object")
                        
            return (
                preprocessed_data_vectorized,
                self.data_transformation_config.vectorizer_obj_file
            )
                        
        except Exception as e:
            raise CustomException(e, sys)
        