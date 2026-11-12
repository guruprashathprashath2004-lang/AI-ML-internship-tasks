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
    print("|==== DOCUMENTS ====|\n".center(90))
    print("-" * 96)
    print(f"{'No':<5}{'Title':<20}{'Vector':<20}{'Text'}")
    print("-" * 96)

    for number, (name, detail) in enumerate(DOCUMENTS.items(), start=1):
        print(f"{number:<4}{name:<20}{str(detail['vector']):<20}{detail['text']}")

def main():
    display_document()

main()