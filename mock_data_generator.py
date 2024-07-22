import pandas as pd
import random
from faker import Faker

fake = Faker()

# Definitions
days = ["2024-07-07", "2024-07-08", "2024-07-09", "2024-07-10", "2024-07-11"]
diseases = [("D123", "Diabetes"), ("H234", "High Blood Pressure"), ("C345", "Cancer"), ("M678", "Malaria"),
            ("R901", "Rheumatoid Arthritis"), ("A456", "Asthma"), ("H789", "Heart Disease"), ("L012", "Lung Cancer"),
            ("D567", "Dementia"), ("B234", "Bronchitis"), ("P678", "Parkinson's Disease"), ("S901", "Stroke"),
            ("E234", "Epilepsy"), ("I456", "Irritable Bowel Syndrome"), ("T789", "Thyroid Disorder"),
            ]
genders = ["Male", "Female"]

# For each day
for i, day in enumerate(days):
    # Create a list to hold data
    data = []
    # Create 100 records for each day
    for j in range(1, 201):
        patient_id = f'P{i*200 + j}'
        age = random.randint(30, 70)
        gender = random.choice(genders)
        diagnosis_code, diagnosis_description = random.choice(diseases)
        diagnosis_date = day
        # Append the row to the data list
        data.append([patient_id, age, gender, diagnosis_code, diagnosis_description, diagnosis_date])
    
    # Create a DataFrame and write it to CSV
    df = pd.DataFrame(data, columns=["patient_id", "age", "gender", "diagnosis_code", "diagnosis_description", "diagnosis_date"])
    df.to_csv(f'health_data_{day.replace("-", "")}.csv', index=False)