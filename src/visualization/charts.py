import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path


class VisualizationManager:
    def __init__(self, output_dir):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def bar_chart_avg_salary(self, department_summary: pd.DataFrame) -> None:
        plt.figure(figsize=(9, 5))
        plt.bar(department_summary["department"], department_summary["avg_salary"], color="steelblue")
        plt.title("Average Salary by Department")
        plt.xlabel("Department")
        plt.ylabel("Average Salary")
        plt.xticks(rotation=30)
        plt.grid(axis="y", linestyle="--", alpha=0.5)
        plt.tight_layout()
        plt.savefig(self.output_dir / "01_avg_salary_by_department.png")
        plt.close()

    def line_chart_join_trend(self, df: pd.DataFrame) -> None:
        joins_per_month = (
            df.groupby(df["joining_date"].dt.to_period("M")).size().sort_index()
        )
        cumulative = joins_per_month.cumsum()

        plt.figure(figsize=(9, 5))
        plt.plot(cumulative.index.astype(str), cumulative.values, marker="o", color="green")
        plt.title("Cumulative Employee Joins Over Time")
        plt.xlabel("Month")
        plt.ylabel("Cumulative Employees Joined")
        plt.xticks(rotation=45)
        plt.grid(True, linestyle="--", alpha=0.5)
        plt.tight_layout()
        plt.savefig(self.output_dir / "02_cumulative_join_trend.png")
        plt.close()

    def histogram_salary_distribution(self, df: pd.DataFrame) -> None:
        plt.figure(figsize=(9, 5))
        plt.hist(df["salary"], bins=20, color="orange", edgecolor="black")
        plt.title("Salary Distribution")
        plt.xlabel("Salary")
        plt.ylabel("Frequency")
        plt.grid(axis="y", linestyle="--", alpha=0.5)
        plt.tight_layout()
        plt.savefig(self.output_dir / "03_salary_distribution.png")
        plt.close()

    def scatter_experience_vs_salary(self, df: pd.DataFrame) -> None:
        plt.figure(figsize=(9, 5))
        plt.scatter(df["experience"], df["salary"], alpha=0.6, color="purple")
        plt.title("Years of Experience vs Salary")
        plt.xlabel("Experience (Years)")
        plt.ylabel("Salary")
        plt.grid(True, linestyle="--", alpha=0.5)
        plt.tight_layout()
        plt.savefig(self.output_dir / "04_experience_vs_salary.png")
        plt.close()

    def pie_chart_department_headcount(self, department_summary: pd.DataFrame) -> None:
        plt.figure(figsize=(7, 7))
        plt.pie(
            department_summary["employee_count"],
            labels=department_summary["department"],
            autopct="%1.1f%%",
            startangle=90,
        )
        plt.title("Department Headcount Share")
        plt.tight_layout()
        plt.savefig(self.output_dir / "05_department_headcount_share.png")
        plt.close()

    def generate_all_charts(self, df: pd.DataFrame, department_summary: pd.DataFrame) -> None:
        self.bar_chart_avg_salary(department_summary)
        self.line_chart_join_trend(df)
        self.histogram_salary_distribution(df)
        self.scatter_experience_vs_salary(df)
        self.pie_chart_department_headcount(department_summary)
        print("All 5 charts are saved")
