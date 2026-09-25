import json
from pathlib import Path
import pandas as pd


class ReportGenerator:
    def __init__(self, output_dir):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def build_findings(self, df: pd.DataFrame, department_summary: pd.DataFrame) -> list:
        top_department = department_summary.sort_values("avg_salary", ascending=False).iloc[0]
        lowest_department = department_summary.sort_values("avg_salary", ascending=True).iloc[0]
        avg_experience = df["experience"].mean()
        active_count = df[df["status"] == "Active"].shape[0]

        findings = [
            f"The highest paying department is {top_department['department']} "
            f"with an average salary of {round(top_department['avg_salary'], 2)}.",
            f"The lowest paying department is {lowest_department['department']} "
            f"with an average salary of {round(lowest_department['avg_salary'], 2)}.",
            f"The average years of experience across employees is {round(avg_experience, 1)}.",
            f"{active_count} out of {df.shape[0]} employees currently have an 'Active' status.",
            f"There are {department_summary.shape[0]} departments in the dataset.",
        ]
        return findings

    def write_markdown_report(self, findings: list, department_summary: pd.DataFrame) -> None:
        path = self.output_dir / "analysis_report.md"

        lines = []
        lines.append("# Employee Data Analysis Report\n")
        lines.append("## Executive Summary")
        lines.append("This report summarizes the analysis of the employee dataset.\n")

        lines.append("## Dataset Overview")
        lines.append(department_summary.to_string(index=False))
        lines.append("")

        lines.append("## Key Findings")
        for i, finding in enumerate(findings, start=1):
            lines.append(f"{i}. {finding}")
        lines.append("")

        lines.append("## Visualizations")
        lines.append("![Average Salary by Department](../charts/01_avg_salary_by_department.png)")
        lines.append("![Join Trend](../charts/02_cumulative_join_trend.png)")
        lines.append("![Salary Distribution](../charts/03_salary_distribution.png)")
        lines.append("![Experience vs Salary](../charts/04_experience_vs_salary.png)")
        lines.append("![Department Headcount](../charts/05_department_headcount_share.png)\n")

        lines.append("## Actionable Recommendations")
        lines.append("- Review the pay gap between the highest and lowest paying departments.")
        lines.append("- Investigate the source of missing/inconsistent data to prevent it going forward.")

        with open(path, "w") as f:
            f.write("\n".join(lines))

        print(f"Markdown report saved to {path}")

    def write_json_summary(self, findings: list, department_summary: pd.DataFrame) -> None:
        path = self.output_dir.parent / "analysis_summary.json"

        summary = {
            "findings": findings,
            "department_summary": department_summary.to_dict(orient="records"),
        }

        with open(path, "w") as f:
            json.dump(summary, f, indent=4)

        print(f"JSON summary saved to {path}")

    def write_text_summary(self, findings: list) -> None:
        path = self.output_dir.parent / "analysis_summary.txt"

        with open(path, "w") as f:
            f.write("EXECUTIVE BRIEFING\n")
            f.write("===================\n\n")
            for finding in findings:
                f.write(f"- {finding}\n")

        print(f"Text summary saved to {path}")
