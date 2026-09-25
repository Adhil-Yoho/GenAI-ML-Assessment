import pandas as pd


class DataCleaner:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def show_missing_values(self) -> pd.Series:
        missing = self.df.isna().sum()
        print("\n--- Missing Values Before Cleaning ---")
        print(missing)
        return missing

    def drop_duplicate_rows(self) -> pd.DataFrame:
        before = self.df.shape[0]
        self.df = self.df.drop_duplicates(subset="employee_id")
        after = self.df.shape[0]
        print(f"Removed {before - after} duplicate rows.")
        return self.df

    def fix_salary_column(self) -> pd.DataFrame:
        self.df["salary"] = pd.to_numeric(self.df["salary"], errors="coerce")
        median_salary = self.df["salary"].median()
        self.df["salary"] = self.df["salary"].fillna(median_salary)
        return self.df

    def fix_date_column(self) -> pd.DataFrame:
        self.df["joining_date"] = pd.to_datetime(
            self.df["joining_date"], format="mixed",dayfirst=True, errors="coerce"
        )
        return self.df

    def fix_numeric_columns(self, columns: list, default_value: float = 0) -> pd.DataFrame:
        for col in columns:
            self.df[col] = pd.to_numeric(self.df[col], errors="coerce")
            self.df[col] = self.df[col].fillna(default_value)
        return self.df

    def clean_all(self) -> pd.DataFrame:
        self.show_missing_values()
        self.drop_duplicate_rows()
        self.fix_salary_column()
        self.fix_date_column()
        self.fix_numeric_columns(["age", "experience", "performance_score"])
        print("\n--- Missing Values After Cleaning ---")
        print(self.df.isna().sum())
        return self.df

    def save_cleaned_data(self, output_path) -> None:
        self.df.to_csv(output_path, index=False)
        print(f"Cleaned data saved to {output_path}")

