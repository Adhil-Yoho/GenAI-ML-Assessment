from pathlib import Path

import pandas as pd

from src.utils.exceptions import InvalidDatasetError


class DataLoader:

    def __init__(self, raw_data_dir=None):

        if raw_data_dir is None:
            project_root = Path(__file__).resolve().parents[2]
            raw_data_dir = project_root / "data" / "raw"

        self.raw_data_dir = Path(raw_data_dir)

        self.employee_file = (
            self.raw_data_dir / "employees.csv"
        )

        self.department_file = (
            self.raw_data_dir / "departments.csv"
        )

    def load_employees(self) -> pd.DataFrame:
    
            if not self.employee_file.exists():
                raise FileNotFoundError(
                    f"Employee file not found: {self.employee_file}"
                )
    
            df = pd.read_csv(self.employee_file)
    
            return df
    
    def load_departments(self) -> pd.DataFrame:
    
            if not self.department_file.exists():
                raise FileNotFoundError(
                    f"Department file not found: {self.department_file}"
                )
    
            df = pd.read_csv(self.department_file)
    
            return df
    
    def validate_employee_schema(
            self, df: pd.DataFrame
        ) -> None:
    
            required_columns = {
                "employee_id",
                "first_name",
                "last_name",
                "age",
                "gender",
                "department_id",
                "department",
                "designation",
                "salary",
                "joining_date",
                "experience",
                "performance_score",
                "city",
                "status",
            }
    
            missing_columns = required_columns - set(df.columns)
    
            if missing_columns:
                raise InvalidDatasetError(
                    f"Employee dataset is missing columns: "
                    f"{sorted(missing_columns)}"
                )
    
            print("Employee dataset schema is valid")
    
    def validate_department_schema(
            self, df: pd.DataFrame
        ) -> None:
    
            required_columns = {
                "department_id",
                "department",
                "budget",
                "division_head",
                "target_headcount",
            }
    
            missing_columns = required_columns - set(df.columns)
    
            if missing_columns:
                raise InvalidDatasetError(
                    f"Department dataset is missing columns: "
                    f"{sorted(missing_columns)}"
                )
    
            print("Department dataset schema is valid")


    def inspect_data(self, df: pd.DataFrame) -> None:
    
            print("\n--- Dataset Shape ---")
            print(df.shape)
    
            print("\n--- First 5 Rows ---")
            print(df.head())
    
            print("\n--- Last 5 Rows ---")
            print(df.tail())
    
            print("\n--- Dataset Information ---")
            df.info()
    
            print("\n--- Statistical Summary ---")
            print(df.describe(include="all"))
    
            print("\n--- Missing Values ---")
            print(df.isna().sum())


