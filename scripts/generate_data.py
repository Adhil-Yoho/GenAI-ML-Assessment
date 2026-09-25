import os
import random
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

script_dir = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(script_dir)
data_dir = os.path.join(root, "data", "raw")

os.makedirs(data_dir, exist_ok=True)

random.seed(42)
np.random.seed(42)

departments_data = [
    {
        "department_id": "DEP001",
        "department": "Engineering",
        "budget": 2500000,
        "division_head": "Sarah Connor",
        "target_headcount": 120
    },
    {
        "department_id": "DEP002",
        "department": "Data Science",
        "budget": 1800000,
        "division_head": "Alex Mercer",
        "target_headcount": 80
    },
    {
        "department_id": "DEP003",
        "department": "Product Management",
        "budget": 1200000,
        "division_head": "Elena Fisher",
        "target_headcount": 50
    },
    {
        "department_id": "DEP004",
        "department": "Marketing",
        "budget": 950000,
        "division_head": "Arthur Pendelton",
        "target_headcount": 60
    },
    {
        "department_id": "DEP005",
        "department": "Human Resources",
        "budget": 600000,
        "division_head": "Samantha Carter",
        "target_headcount": 40
    },
    {
        "department_id": "DEP006",
        "department": "Sales",
        "budget": 2100000,
        "division_head": "Gordon Freeman",
        "target_headcount": 150
    },
]

dept_output_path = os.path.join(data_dir, "departments.csv")
df_departments = pd.DataFrame(departments_data)
df_departments.to_csv(dept_output_path, index=False)
print(f"Successfully generated: {dept_output_path} (6 departments)")


first_names = [
    "James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda", 
    "William", "Elizabeth", "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica",
    "Thomas", "Sarah", "Charles", "Karen", "Christopher", "Nancy", "Daniel", "Lisa",
    "Matthew", "Betty", "Anthony", "Margaret", "Donald", "Sandra", "Mark", "Ashley"
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
    "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson", "White"
]

cities = ["New York", "San Francisco", "Austin", "Seattle", "Chicago", "Boston", "Atlanta"]
designations = ["Junior", "Mid-Level", "Senior", "Lead", "Manager", "Director"]
genders = ["Male", "Female", "Non-Binary"]
statuses = ["Active", "Active", "Active", "Active", "On Leave", "Terminated"]

records = []
start_date = datetime(2018, 1, 1)
end_date = datetime(2025, 12, 31)

def random_date(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

for i in range(1, 521):
    dept_info = random.choice(departments_data)
    
    age = random.randint(22, 63)
    experience = max(0, age - random.randint(21, 25))
    
    base_salary = dept_info["budget"] / dept_info["target_headcount"] * 0.8
    salary = round(base_salary + (experience * 2500) + random.randint(-5000, 10000), 2)
    
    performance_score = round(random.uniform(1.5, 5.0), 1)
    
    join_dt = random_date(start_date, end_date)
    if random.random() < 0.3:
        joining_date_str = join_dt.strftime("%d-%m-%Y")
    elif random.random() < 0.2:
        joining_date_str = join_dt.strftime("%Y/%m/%d")
    else:
        joining_date_str = join_dt.strftime("%Y-%m-%d")

    record = {
        "employee_id": f"EMP{i:04d}",
        "first_name": random.choice(first_names),
        "last_name": random.choice(last_names),
        "age": age if random.random() > 0.05 else np.nan,  # 5% missing age
        "gender": random.choice(genders),
        "department_id": dept_info["department_id"],
        "department": dept_info["department"],
        "designation": random.choice(designations),
        "salary": salary if random.random() > 0.08 else np.nan,  # 8% missing salaries
        "joining_date": joining_date_str,
        "experience": experience,
        "performance_score": performance_score if random.random() > 0.03 else np.nan, # 3% missing scores
        "city": random.choice(cities),
        "status": random.choice(statuses)
    }
    records.append(record)

df_employees = pd.DataFrame(records)

duplicate_rows = df_employees.sample(n=15, random_state=42)
df_employees = pd.concat([df_employees, duplicate_rows], ignore_index=True)

emp_output_path = os.path.join(data_dir, "employees.csv")
df_employees.to_csv(emp_output_path, index=False)
print(f"Successfully generated: {emp_output_path} ({len(df_employees)} records with missing values and duplicates)")
