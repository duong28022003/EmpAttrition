from pydantic import BaseModel

class Employee(BaseModel):
    Age: int
    BusinessTravel: str
    DailyRate: float
    DistanceFromHome: float
    EnvironmentSatisfaction: int
    HourlyRate: float
    JobInvolvement: int
    JobLevel: int
    JobRole: str	
    JobSatisfaction: int
    MaritalStatus: str
    MonthlyIncome: float
    MonthlyRate: float
    NumCompaniesWorked: int
    OverTime: str
    PercentSalaryHike: float
    RelationshipSatisfaction: int
    StockOptionLevel: int
    TotalWorkingYears: int
    TrainingTimesLastYear: int
    WorkLifeBalance: int
    YearsAtCompany: int
    YearsInCurrentRole: int
    YearsSinceLastPromotion: int
    YearsWithCurrManager:int