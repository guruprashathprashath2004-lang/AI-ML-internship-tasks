import numpy as np

HEADER = ["Python", "AI", "Machine Learning", "Sports", "Travel"] 

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

def main():
    print(f"Total documents: {len(DOCUMENTS)}")

main()