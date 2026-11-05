import numpy as np

patient_count = 20
header = ["PATIENT ID", "AGE", "BLOOD PERSSURE", "SUGAR LEVEL", "HEART RATE", "BMI"]

high_bp = 140
high_sugar = 140
senior_age = 60

def create_patient_dataset():
    patient_id = np.arange(1, patient_count + 1)                  # Get same datas for every run

    age = np.random.randint(20, 81, patient_count)
    bp  = np.random.randint(100, 181, patient_count)              # Blood Pressure
    sl  = np.random.randint(70, 251, patient_count)               # Sugar Level
    hr  = np.random.randint(60, 111, patient_count)               # Heart Rate
    bmi = np.round(np.random.uniform(18, 40, patient_count), 1)   # BMI

    return np.column_stack((patient_id,
                            age,
                            bp,
                            sl,
                            hr,
                            bmi))

def display_datas(patients_datas):

    if len(patients_datas) == 0:
        print("No records found..!")
        return 
        
    print("-" * 90)
    print("" .join(f"{head:<15}" for head in header))
    print("-" * 90)

    for datas in patients_datas:
        print("" .join(f"{value:<15}" for value in datas)) 

def main():
    patients_datas = create_patient_dataset()
    display_datas(patients_datas)

main()
