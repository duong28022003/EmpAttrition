import sys
from pathlib import Path
import torch.nn as nn 
import torch
import torch.nn.functional as F 
from config.ModelConfig import ModelConfig, DataConfig
from .AttritionModel import AttritionModel

sys.path.append(str(Path(__file__).parent.parent))

from processor.process import Processor
from utils.logger import Logger

LOGGER = Logger(__file__, log_file='predictor.log')
LOGGER.log.info('Start Model Serving')
LOGGER.log_model(ModelConfig.MODEL_NAME)

class AttritionPredictor:
    def __init__(self, model_name: str = ModelConfig.MODEL_NAME, model_weight: str = ModelConfig.MODEL_WEIGHT, device: str = 'cpu'):
        self.model_name = model_name
        self.model_weight = model_weight
        self.device = device 
        self.load_model_config()
        self.load_model()
    
    def load_model_config(self):
        INPUT_DIM = ModelConfig.INPUT_DIM
        OUTPUT_DIM = ModelConfig.OUTPUT_DIM
        self.model = AttritionModel(INPUT_DIM, OUTPUT_DIM)
    
    def load_model(self):
        try:
            state_dict = torch.load(self.model_weight, map_location=self.device)
            self.model.load_state_dict(state_dict)
            self.model = self.model.to(self.device)
        except Exception as e:
            raise RuntimeError(f"Failed to load model from {self.model_weight}: {e}")
        
    def model_inference(self, data):
        processor = Processor()
        data = processor.transform(data)
        loader = processor.make_dataLoader(data)
        
        respones = []
        
        self.model.eval()
        with torch.no_grad():
            for features in loader:
                result = dict()
                features = features.to(self.device)
                probs = self.model(features)
                predictions = probs.argmax(dim=1).tolist()
                
                # Extract the probs & labels
                for i in range(len(predictions)):
                    
                    result['Probs'] = probs[i].tolist()
                    label = DataConfig.ID2LABEL.get(predictions[i])
                    result['Prediction'] = label
                    respones.append(result)
                    
                    LOGGER.log_response(probs[i].tolist(), label)
                    
        torch.cuda.empty_cache()
        return respones
        