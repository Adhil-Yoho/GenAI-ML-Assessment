import pandas as pd


def get_high_salary_employees_list(df: pd.DataFrame, threshold: float = 70000) -> list:
    names = [
        f"{row.first_name} {row.last_name}"
        for row in df.itertuples()
        if row.salary > threshold
    ]
    return names


def clean_department_names(department_list) -> list:
    return list(map(lambda name: str(name).strip().title(), department_list))


def filter_active_employees(df: pd.DataFrame) -> pd.DataFrame:
    active_statuses = list(filter(lambda status: status == "Active", df["status"]))
    return df[df["status"].isin(active_statuses)]


def sort_departments_by_salary(department_summary: pd.DataFrame):
    return department_summary.sort_values(by="avg_salary", key=lambda col: col, ascending=False)
