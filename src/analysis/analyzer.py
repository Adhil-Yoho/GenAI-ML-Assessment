import numpy as np
import pandas as pd


class DataAnalyzer:
    def __init__(self, employee_df: pd.DataFrame, department_df: pd.DataFrame = None):
        self.employee_df = employee_df
        self.department_df = department_df

    def get_salary_array(self) -> np.ndarray:
        salary_array = self.employee_df["salary"].to_numpy()
        print("First 10 salaries:", salary_array[:10])
        return salary_array

    def basic_stats(self, column: str = "salary") -> dict:
        array = self.employee_df[column].to_numpy()
        stats = {
            "mean": np.mean(array),
            "sum": np.sum(array),
            "std": np.std(array),
        }
        print(f"Stats for {column}:", stats)
        return stats

    def apply_bonus_broadcast(self, bonus_percent: float = 5.0) -> np.ndarray:
        salary_array = self.employee_df["salary"].to_numpy()
        factor = 1 + (bonus_percent / 100)
        new_salaries = salary_array * factor
        return new_salaries

    def reshape_example(self) -> np.ndarray:
        salary_array = self.employee_df["salary"].to_numpy()
        reshaped = salary_array.reshape(-1, 1)
        print("Reshaped salary array shape:", reshaped.shape)
        return reshaped

    def composite_performance_score(self, weight_vector=None) -> np.ndarray:
        if weight_vector is None:
            weight_vector = np.array([0.6, 0.4])

        feature_matrix = self.employee_df[["performance_score", "experience"]].to_numpy()
        composite_score = np.dot(feature_matrix, weight_vector)
        self.employee_df["composite_score"] = composite_score
        return composite_score

    def department_summary(self) -> pd.DataFrame:
        summary = self.employee_df.groupby("department").agg(
            employee_count=("employee_id", "count"),
            avg_salary=("salary", "mean"),
            max_salary=("salary", "max"),
        )
        return summary.reset_index()

    def merge_with_departments(self) -> pd.DataFrame:
        if self.department_df is None:
            raise ValueError("Department data was not provided")

        merged_df = pd.merge(
            self.employee_df,
            self.department_df,
            on="department_id",
            how="left",
        )
        return merged_df

    def high_salary_employees(self, threshold: float = 70000) -> pd.DataFrame:
        return self.employee_df[self.employee_df["salary"] > threshold]
