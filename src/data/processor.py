
from abc import ABC, abstractmethod
import pandas as pd


class BaseDataProcessor(ABC):
    def __init__(self, df: pd.DataFrame):
        self.df = df

    @abstractmethod
    def process(self) -> pd.DataFrame:
        """Every child class has to fill this in itself"""
        pass


class EmployeeDataProcessor(BaseDataProcessor):
    def __init__(self, df: pd.DataFrame, bonus_factor: float = 1.10):
        super().__init__(df)
        self.bonus_factor = bonus_factor

    def process(self) -> pd.DataFrame:
        self.df["salary_after_bonus"] = self.df["salary"] * self.bonus_factor
        print("Employee data processed with bonus factor applied")
        return self.df
 