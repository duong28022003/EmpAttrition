import pandas as pd
import numpy as np
from torch.utils.data import Dataset, DataLoader
import joblib
import sys
from pathlib import Path
from config.ModelConfig  import DataConfig
import torch

sys.path.append(str(Path(__file__).parent))

class CustomDataset(Dataset):
    def __init__(self, data: pd.DataFrame):
        super().__init__()
        self.data = torch.tensor(data.values, dtype=torch.float32)
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
        return self.data[index]

class Processor:
    def __init__(self):
        self.base_path = Path(__file__).parent 
        self.encoder = joblib.load(self.base_path / 'Encoder.joblib')
        self.scaler = joblib.load(self.base_path / 'Scaler.joblib')
        self.ENCODED_COLUMNS = DataConfig.ENCODED_COLUMNS
        self.SCALED_COLUMNS = DataConfig.SCALED_COLUMNS
        self.LOG_TRANSFORMED_COLUMNS = DataConfig.LOG_TRANSFORMED_COLUMNS
        
    def transform(self, json_data):
        data = pd.DataFrame(json_data)
        
        # Encode categorical columns
        for col in self.ENCODED_COLUMNS:
            data[col] = self.encoder[col].transform(data[col])
        
        # Transform numerical columns
        for col in self.SCALED_COLUMNS:
            data[[col]] = self.scaler[col].transform(data[[col]])
            
        for col in self.LOG_TRANSFORMED_COLUMNS:
            data[col] = np.log1p(data[col])
        
        return data
    
    def make_dataLoader(self, data: pd.DataFrame, BATCH_SIZE: int = 16):
        predict_data = CustomDataset(data)
        return DataLoader(predict_data, batch_size=BATCH_SIZE, shuffle=False)        