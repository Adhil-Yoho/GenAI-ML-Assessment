from src.data.loader import DataLoader
from src.data.cleaner import DataCleaner
from src.data.processor import EmployeeDataProcessor
from src.analysis.analyzer import DataAnalyzer
from src.api.client import APIClient
from src.visualization.charts import VisualizationManager
from src.reports.generator import ReportGenerator
from src.config import settings
from src.utils.exceptions import InvalidDatasetError


def run_pipeline():
    print("STEP 1: Loading data")
    loader = DataLoader()

    try:
        employee_df = loader.load_employees()
        department_df = loader.load_departments()
        loader.validate_employee_schema(employee_df)
        loader.validate_department_schema(department_df)
    except InvalidDatasetError as error:
        print(f"Dataset validation failed: {error}")
        return

    loader.inspect_data(employee_df)

    print("\nSTEP 2: Cleaning data")
    cleaner = DataCleaner(employee_df)
    cleaned_df = cleaner.clean_all()
    cleaner.save_cleaned_data(settings.PROCESSED_DATA_DIR / "cleaned_employees.csv")

    print("\nSTEP 3: Processing data (inheritance example)")
    processor = EmployeeDataProcessor(cleaned_df, bonus_factor=1.10)
    processed_df = processor.process()

    print("\nSTEP 4: Running analysis")
    analyzer = DataAnalyzer(processed_df, department_df)
    analyzer.get_salary_array()
    analyzer.basic_stats("salary")
    analyzer.composite_performance_score()
    department_summary = analyzer.department_summary()

    print("\nSTEP 5: Calling external API")
    api_client = APIClient(settings.API_URL, settings.API_TIMEOUT)
    api_data = api_client.get_data()
    api_client.save_cache(api_data, settings.REPORTS_DIR.parent / "api_cache.json")

    print("\nSTEP 6: Generating charts")
    viz = VisualizationManager(settings.CHARTS_DIR)
    viz.generate_all_charts(processed_df, department_summary)

    print("\nSTEP 7: Generating report")
    reporter = ReportGenerator(settings.REPORTS_DIR)
    findings = reporter.build_findings(processed_df, department_summary)
    reporter.write_markdown_report(findings, department_summary)
    reporter.write_json_summary(findings, department_summary)
    reporter.write_text_summary(findings)

    print("\nPipeline finished successfully.")


if __name__ == "__main__":
    run_pipeline()
