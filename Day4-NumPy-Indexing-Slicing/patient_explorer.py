import numpy as np

patient_count = 20
header = ["||PATIENT ID|", "|AGE|", "|BLOOD PERSSURE|", "|SUGAR LEVEL|", "|HEART RATE|", "|BMI||"]

high_bp = 140
high_sugar = 140
senior_age = 60

def create_patient_dataset():
    patient_id = np.arange(1, patient_count + 1)

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

def main():
    patients_datas = create_patient_dataset()
    print(patients_datas)

main()
