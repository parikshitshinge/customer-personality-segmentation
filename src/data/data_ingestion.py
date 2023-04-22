import os 
from pathlib import Path
import sys
from src.exception import CustomException
from src.logger import logging 
from src.data.data_transformation import DataTransformation, DataTransformationConfig

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    # Configure connection from data source
    source_data_path: str = os.path.join('data/source', 'marketing_campaign.csv')
    
    # Define destination path to load source data
    raw_data_path: str = os.path.join('data/raw', 'marketing_campaign.csv')
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method")
        try:
            # Read data from source database
            raw_data = pd.read_csv("./data/source/marketing_campaign.csv", sep="\t")
            logging.info("Read the marketing_campaign.csv dataset as dataframe") 
            
            # Prepare the staging file path 
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            
            # Ingest data into our raw folder as it is from source
            raw_data.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            
            logging.info("Ingestion of the data is completed")
            return(
                self.ingestion_config.raw_data_path
            )
                       
        except Exception as e:
            raise CustomException(e, sys)
            
if __name__ == "__main__":
    obj = DataIngestion()
    raw_data = obj.initiate_data_ingestion()
    
    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(raw_data)