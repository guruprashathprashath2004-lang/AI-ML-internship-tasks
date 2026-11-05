import numpy as np

patient_count = 20
header = ["PATIENT ID", "AGE", "BLOOD PRESSURE", "SUGAR LEVEL", "HEART RATE", "BMI"]

high_bp = 140
high_sugar = 140
senior_age = 60

def main():
    patients_datas = create_patient_dataset()
    display_datas(patients_datas)
    first_and_last_patients(patients_datas)
    display_blood_pressure_values(patients_datas)
    display_only_age_and_bmi(patients_datas)
    retrieve_1_to_15_patients(patients_datas)
    high_blood_pressure_patients(patients_datas)
    senior_citizens(patients_datas)
    high_bp_and_high_sugar_level(patients_datas)


def create_patient_dataset():
    np.random.seed(42)

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

    print("|==== PATIENTS DATASET ====|".center(90))

    if len(patients_datas) == 0:
        print("No records found..!")
        return 
        
    print("-" * 90)
    print("" .join(f"{head:<15}" for head in header))
    print("-" * 90)

    for datas in patients_datas:
        print("" .join(f"{value:<15}" for value in datas)) 


def first_and_last_patients(patients_datas):

    print()
    print("|==== FIRST AND LAST PATIENTS ====|".center(90))

    print("-" * 90)
    print("" .join(f"{head:<15}" for head in header))
    print("-" * 90)

    for data in patients_datas[[0, -1], :]:
        print("" .join(f"{value:<15}" for value in data))


def display_blood_pressure_values(patients_datset):

    print()
    print("|==== ALL BLOOD PRESSURE VALUES ====|" )

    print("-" * 20)
    print(header[2].center(20))
    print("-" * 20)

    for data in patients_datset[:, [2]]:
        print("" .join(f"{value:<20}" for value in data))


def display_only_age_and_bmi(patients_datas):

    print()
    print("|==== ALL PATIENT'S AGE AND BMI ====|".center(40))

    print("-" * 40)
    print("" .join(f"{head:<20}" for head in [header[1], header[5]]))
    print("-" * 40)

    for data in patients_datas[:, [1, 5]]:
        print("" .join(f"{value:<20}" for value in data))


def retrieve_1_to_15_patients(patients_datas):

    print()
    print("|==== RETRIEVED PATIENTS (5 - 15) ====|".center(90))

    print("-" * 90)
    print("" .join(f"{head:<15}" for head in header))
    print("-" * 90)

    for data in patients_datas[4: 15]:
        print("" .join(f"{value:<15}" for value in data))


def high_blood_pressure_patients(patients_datas):

    print()
    print("|==== HIGH BLOOD PRESSURE PATIENTS ====|".center(90))

    print("-" * 90)
    print("" .join(f"{head:<15}" for head in header))
    print("-" * 90)

    high_bp_patients = patients_datas[patients_datas[:, 2] > high_bp]
    for data in high_bp_patients:
        print("" .join(f"{value:<15}" for value in data))


def senior_citizens(patients_datas):

    print()
    print("|==== SENIOR CITIZENS ====|".center(90))
    
    print("-" * 90)
    print("" .join(f"{head:<15}" for head in header))
    print("-" * 90)

    senior_citizen = patients_datas[patients_datas[:, 1] > senior_age]
    for data in senior_citizen:
        print("" .join(f"{value:<15}" for value in data))


def high_bp_and_high_sugar_level(patients_datas):

    print()
    print("|==== PATIENTS WITH BOTH HIGH BP AND HIGH SUGAR LEVELS ====|".center(90))
        
    print("-" * 90)
    print("" .join(f"{head:<15}" for head in header))
    print("-" * 90)
   
    both = patients_datas[
        (patients_datas[:, 2] > high_bp) & 
        (patients_datas[:, 3] > high_sugar)
        ]

    for data in both:
        print("" .join(f"{value:<15}" for value in data))


main()
