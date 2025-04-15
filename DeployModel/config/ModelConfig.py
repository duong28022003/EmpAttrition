import sys 

from pathlib import Path

sys.path.append(str(Path(__file__).parent))

class DataConfig:
    N_CLASSES = 2
    ID2LABEL = {0:'No', 1: 'Yes'}
    LABEL2ID = {'Yes': 1, 'No': 0}
    ENCODED_COLUMNS = ['BusinessTravel', 'JobRole', 'MaritalStatus', 'OverTime']
    
    SCALED_COLUMNS = ['EnvironmentSatisfaction', 'JobInvolvement', 'JobLevel', 'JobSatisfaction',
                      'RelationshipSatisfaction', 'WorkLifeBalance', 'StockOptionLevel',
                        'HourlyRate', 'DailyRate', 'MonthlyRate', 'Age', 'NumCompaniesWorked',
                        'TrainingTimesLastYear', 'YearsInCurrentRole', 'YearsWithCurrManager']
    
    LOG_TRANSFORMED_COLUMNS = ['DistanceFromHome', 'MonthlyIncome', 'PercentSalaryHike', 
                             'YearsAtCompany', 'TotalWorkingYears', 'YearsSinceLastPromotion']
    
class ModelConfig:
    INPUT_DIM = 25
    OUTPUT_DIM = 2
    ROOT_DIR = Path(__file__).parent.parent
    MODEL_NAME = 'NN Predictor'
    MODEL_WEIGHT = ROOT_DIR  / 'weights' / 'attrition.pt'
    DEVICE = 'cpu'