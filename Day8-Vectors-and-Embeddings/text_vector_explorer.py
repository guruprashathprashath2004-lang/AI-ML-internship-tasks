import numpy as np

HEADER = ["Word", "Category", "Vector", "Dimention"]
CATEGORIES = {
    "Animals": {"cat": [2, 3], "dog": [3, 4], "lion": [4, 5], "tiger": [3, 5]},
    "Vehicles": {"car": [9, 1], "bus": [8, 2], "bike": [9, 2], "train": [8, 1]},
    "Technology": {"laptop": [1, 8], "phone": [2, 9], "robot": [3, 8], "computer": [1, 9]},
    "Food": {"pizza": [6, 8], "burger": [7, 9], "rice": [6, 9], "apple": [7, 7]},
    "Sports": {"cricket": [6, 5], "football": [7, 4], "tennis": [5, 6], "hockey": [6, 3]},
}

COLORS = {
    "Animals" : "green",
    "Vehicles" : "red",
    "Technologies" : "blue",
    "Food" : "Orange",
    "Sports" : "purple"
}

 # Simple Lookup
data = {}                                  # word -> vector
word_category = {}                         # word -> category
for category,words in CATEGORIES.items():
    for word, vector in  words.items():
        data[word] = vector
        word_category[word] = category


def calculate_distence(vector1, vector2):
    return float(np.linalg.norm(np.array(vector1) - np.array(vector2)))

def display_all_vectors():
    print()
    print("-" * (15 * len(HEADER)))
    print("" .join(f"{head:<15}" for head in HEADER))
    print("-" * (15 * len(HEADER)))

    for word,vector in data.items():
        print("" .join(f"{word:<15}{word_category[word]:<15}{str(vector):<15}{len(vector):<15}"))

def main():
    display_all_vectors()

main()