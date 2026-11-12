import numpy as np

TOPICS = ["Python", "AI", "Machine Learning", "Sports", "Travel"]

DOCUMENTS = {
    "Python Basics": {
        "text": "Learn Python variables, loops and functions",
        "vector": [5, 1, 0, 0, 0],
    },
    "Python for Data": {
        "text": "Using Python with NumPy and pandas for data analysis",
        "vector": [5, 1, 3, 0, 0],
    },
    "What is AI": {
        "text": "Artificial intelligence builds machines that think and learn",
        "vector": [1, 5, 2, 0, 0],
    },
    "AI in Daily Life": {
        "text": "Chatbots and voice assistants use AI every day",
        "vector": [1, 5, 1, 0, 0],
    },
    "ML Basics": {
        "text": "Machine learning trains models from data",
        "vector": [2, 3, 5, 0, 0],
    },
    "Neural Networks": {
        "text": "Deep learning uses neural networks with many layers",
        "vector": [1, 4, 5, 0, 0],
    },
    "Cricket World Cup": {
        "text": "Cricket teams compete in the world cup",
        "vector": [0, 0, 0, 5, 1],
    },
    "Football Training": {
        "text": "Football players train fitness and tactics",
        "vector": [0, 0, 0, 5, 0],
    },
    "Sri Lanka Travel": {
        "text": "Visit Kandy, Ella and Sigiriya beaches and hills",
        "vector": [0, 0, 0, 1, 5],
    },
    "Backpacking Tips": {
        "text": "Budget tips for backpacking and cheap hotels",
        "vector": [0, 0, 0, 0, 5],
    },
}


def cosine_similarity(vector1, vector2):
    a = np.array(vector1, dtype=float)
    b = np.array(vector2, dtype=float)

    length_a = np.linalg.norm(a)
    length_b = np.linalg.norm(b)

    if length_a == 0 or length_b == 0:
        return 0.0

    return float(np.dot(a, b) / (length_a * length_b))


def display_document():
    print()
    print("|==== DOCUMENTS ====|\n".center(96))
    print("-" * 96)
    print(f"{'No':<5}{'Title':<20}{'Vector':<20}{'Text'}")
    print("-" * 96)

    for number, (name, detail) in enumerate(DOCUMENTS.items(), start=1):
        print(f"{number:<4}{name:<20}{str(detail['vector']):<20}{detail['text']}")


def get_query_vector():

    print(f"\nEnter {len(TOPICS)} scores for {TOPICS} separated by spaces")
    print("Example: 3 1 0 0 0")

    while True:
        text = input("Enter Query vector: ").strip()

        try:
            query = [float(value) for value in text.split()]         
        except ValueError as error: 
            print("ERROR:", error)
            print("Invalid input..! Please enter numbers only.")
            continue

        if len(query) != len(TOPICS):
            print(f"Please enter exactly {len(TOPICS)} numbers.")
        elif any(value < 0 for value in query):
            print("Please enter positive numbers.")
        elif all(value == 0 for value in query):
            print("Query cannot be all zeros.")
        else:
            return query


def compare_with_every_vector(query):

    results = []

    for name, detail in DOCUMENTS.items():
        score = cosine_similarity(query, detail["vector"])
        results.append((score, name))

    results.sort(key=lambda item: (-item[0], item[1]))
    return results

def display_compared_result(results):
    print("\n|==== RANKING (MOST SIMILAR -> LEAST SIMILAR) ====|\n")
    print(f"{'Rank':<6}{'Document':<22}{'Result':<12}")
    print("-" * 40)

    for rank, (score, name) in enumerate(results, start=1):
        print(f"{rank:<6}{name:<22}{score:<12.4f}")


def display_top_3(results):
    print("\n|==== TOP 3 RESULTS ====|\n")

    for rank, (score, name) in enumerate(results[:3], start=1):
        print(f"{rank}. {name}  (similarity: {score:.4f})")
        print(f"   {DOCUMENTS[name]['text']}")


def display_similarity_matrix():
    names = list(DOCUMENTS.keys())
    vectors = [DOCUMENTS[name]["vector"] for name in names]
    size = len(names)

    matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            matrix[i][j] = cosine_similarity(vectors[i], vectors[j])

    print("\n|==== SIMILARITY MATRIX ====|\n")
    for number, name in enumerate(names, start=1):
        print(f"D{number:<3}= {name}")

    print()
    print(" " * 6 + "".join(f"{'D' + str(n):<7}" for n in range(1, size + 1)))
    print("-" * (6 + 7 * size))

    for i in range(size):
        row = "".join(f"{value:<7.2f}" for value in matrix[i])
        print(f"{'D' + str(i + 1):<6}{row}")

def main():
    display_document()
    query = get_query_vector()
    results = compare_with_every_vector(query)
    display_compared_result(results)
    display_top_3(results)
    display_similarity_matrix()

main()

