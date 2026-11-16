import numpy as np
import os
from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"
EMBEDDINGS_FILE = "document_embeddings.npy"
TOP_N = 5
CATEGORY_LIST = ["Python", "NumPy", "Pandas", "Machine Learning", "AI"]

DATASET = [
    ["Python", "Python is a high-level language known for readable code."],
    ["Python", "Indentation decides which lines belong to a block in Python."],
    ["Python", "Lists store many items in a single ordered collection."],
    ["Python", "Dictionaries keep data as key and value pairs."],
    ["Python", "Functions let us reuse the same code many times."],
    ["Python", "Loops repeat a set of instructions again and again."],
    ["Python", "The pip tool installs extra libraries for Python."],
    ["Python", "Try and except blocks handle errors without crashing the program."],
    ["Python", "Classes help us design programs around objects."],
    ["Python", "Virtual environments keep project libraries separate."],

    ["NumPy", "NumPy is used for fast numerical computing with arrays."],
    ["NumPy", "The ndarray is the main data structure in NumPy."],
    ["NumPy", "Broadcasting lets arrays of different shapes work together."],
    ["NumPy", "NumPy can do linear algebra such as matrix multiplication."],
    ["NumPy", "Vectorized operations are much quicker than Python loops."],
    ["NumPy", "The reshape function changes the shape of an array."],
    ["NumPy", "NumPy has tools to generate random numbers."],
    ["NumPy", "Functions like mean and std calculate statistics on arrays."],
    ["NumPy", "Boolean indexing selects array values that match a condition."],
    ["NumPy", "Many data science libraries are built on top of NumPy."],

    ["Pandas", "Pandas is a library for analysing and cleaning tabular data."],
    ["Pandas", "A DataFrame is a table with labelled rows and columns."],
    ["Pandas", "A Series is a single labelled column of data."],
    ["Pandas", "The read_csv function loads a CSV file into a table."],
    ["Pandas", "The groupby method summarises data by groups."],
    ["Pandas", "Missing values can be filled or dropped in Pandas."],
    ["Pandas", "The loc property picks rows and columns by their labels."],
    ["Pandas", "Two tables can be joined together using merge."],
    ["Pandas", "The describe method shows quick summary statistics."],
    ["Pandas", "Rows can be filtered by writing a condition on a column."],

    ["Machine Learning", "Machine learning lets computers learn patterns from data."],
    ["Machine Learning", "Supervised learning trains a model using labelled examples."],
    ["Machine Learning", "Unsupervised learning finds hidden groups in unlabelled data."],
    ["Machine Learning", "Overfitting means a model memorises training data and fails on new data."],
    ["Machine Learning", "A train test split checks how well a model works on unseen data."],
    ["Machine Learning", "Linear regression predicts a number from input features."],
    ["Machine Learning", "Classification models put items into categories such as spam or not spam."],
    ["Machine Learning", "Decision trees make predictions by asking a series of questions."],
    ["Machine Learning", "Cross validation tests a model on several parts of the data."],
    ["Machine Learning", "Feature engineering creates better inputs for a model."],

    ["AI", "Artificial intelligence builds systems that do tasks needing human intelligence."],
    ["AI", "Neural networks are layers of connected nodes inspired by the brain."],
    ["AI", "Deep learning uses many layers to learn complex patterns."],
    ["AI", "Large language models learn from huge amounts of text."],
    ["AI", "Embeddings turn text into numbers that capture its meaning."],
    ["AI", "Retrieval augmented generation gives a language model relevant documents."],
    ["AI", "Vector databases store embeddings and find similar items fast."],
    ["AI", "Natural language processing helps computers understand human language."],
    ["AI", "Computer vision allows machines to understand images and video."],
    ["AI", "Reinforcement learning teaches an agent using rewards."],
]

texts = []
categories = []
for item in DATASET:
    texts.append(item[1])
    categories.append(item[0])


def display_dataset():
    
    print("|==== ALL DATAS ====|\n".center(85))

    print("-" * 90)
    print(f"{'No':<5}{'Category':<20}{'text'}")
    print("-" * 90)

    for i in range(len(texts)):
        print(f"{(i + 1):<5}{categories[i]:<20}{texts[i]}")


def model_load():

    print("Loading model (Please wait for first time load..!) ")
    model = SentenceTransformer(MODEL_NAME)
    print(f"Model '{MODEL_NAME}' Loaded.")
    return model


def get_embedding(model):
    
    if os.path.exists(EMBEDDINGS_FILE):
        embeddings = np.load(EMBEDDINGS_FILE)
        if embeddings.shape[0] == len(texts):
            print(f"Load saved embeddings : {embeddings.shape}")
            return embeddings

    print("Generating embeddings...")
    embeddings = model.encode(texts, normalize_embeddings=True)
    np.save(EMBEDDINGS_FILE, embeddings)
    print(f"Load saved embeddings : {embeddings.shape}")
    return embeddings


def search(model, embeddings, query):

    query_embeddings = model.encode(query, normalize_embeddings=True)
    scores = embeddings @ query_embeddings
    order = np.argsort(-scores)

    print(f"\n|==== TOP {TOP_N} RESULTS ====|\n")
    for rank in range(TOP_N):
        index = order[rank]
        print(f"{rank + 1}. [{categories[index]}] {texts[index]}")
        print(f"   Similarity: {scores[index]:.4f}")


def main():
    display_dataset()
    model = model_load()
    embeddings = get_embedding(model)
    search(model, embeddings, "What is NumPy used for?")

main()