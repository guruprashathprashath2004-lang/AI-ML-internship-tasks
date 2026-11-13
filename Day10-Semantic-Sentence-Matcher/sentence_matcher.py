import numpy as np
from sentence_transformers import SentenceTransformer
import os

MODEL_NAME = "all-MiniLM-L6-v2"
EMBEDDINGS_FILE = "sentence_embedding.npy"
TOP_N = 5

# Topic -> 6 sentences (5 topics x 6 = 30 sentences)
DATASET = {
    "Programming": [
        "Python is a popular language for writing programs.",
        "JavaScript makes web pages interactive.",
        "Developers use Git to track changes in their code.",
        "Debugging means finding and fixing errors in software.",
        "A function is a reusable block of code.",
        "Databases store and organize information for applications.",
    ],
    "AI": [
        "Machine learning is a branch of artificial intelligence.",
        "Neural networks learn patterns from large amounts of data.",
        "Chatbots can answer questions using language models.",
        "Computer vision helps machines understand images.",
        "Training a model means teaching it from examples.",
        "Embeddings turn text into numbers that capture meaning.",
    ],
    "Education": [
        "Students learn new skills at university.",
        "Online courses let people study from home.",
        "Teachers explain difficult lessons using examples.",
        "Regular practice improves exam results.",
        "Libraries provide books and quiet places to read.",
        "Scholarships help students pay for their studies.",
    ],
    "Business": [
        "Startups need funding to grow their company.",
        "Good marketing increases product sales.",
        "Customers expect fast and friendly service.",
        "A budget helps a company control its spending.",
        "Entrepreneurs take risks to build new businesses.",
        "Investors look for profitable opportunities.",
    ],
    "Travel": [
        "I want to travel to Japan next spring.",
        "Sigiriya is a famous tourist attraction in Sri Lanka.",
        "Booking flights early can save money.",
        "Hikers enjoy the mountains and waterfalls in Ella.",
        "Hotels offer rooms for visitors staying overnight.",
        "A passport is required for international trips.",
    ],
}

sentences = []
topics = []
for topic, topic_sentences in DATASET.items():
    for sentence in topic_sentences:
        sentences.append(sentence)
        topics.append(topic)


def display_dataset():
    print("-" * 80)
    print(f"{'No':<4}{'Topic':<15}{'Sentence'}")
    print("-" * 80)

    for number, (topic, sentence) in enumerate(zip(topics, sentences), start=1):
        print(f"{number:<4}{topic:<15}{sentence}")


def model_load():

    print(f"Loading embedding model '{MODEL_NAME}' (For the 1st time the model will be download, so please wait..!)...")
    model = SentenceTransformer(MODEL_NAME)
    print(f"{MODEL_NAME} Model loaded")

    return model


def sentence_embeddings(model):
    
    print("Creating embeddings for all sentences")
    embeddings = model.encode(sentences, normalize_embeddings= True)

    np.save(EMBEDDINGS_FILE, embeddings)
    print(f"Embeddings shape : {embeddings.shape}")
    print(f"Saved to : {EMBEDDINGS_FILE}")

    return embeddings


def get_embeddings(model):
    if os.path.exists(EMBEDDINGS_FILE):
        embeddings = np.load(EMBEDDINGS_FILE)

        if embeddings.shape[0] == len(sentences):
            print(f"Loaded saved embeddings from {EMBEDDINGS_FILE} {embeddings.shape}")
            return embeddings    

        print("Saved embeddings do not match the sentences. Regenerating...")

    return sentence_embeddings(model)


def search(model, embeddings, query):
    query_embedding = model.encode(query, normalize_embeddings=True)
    print(f"\nQuery embedding shape : {query_embedding.shape}")
    print(f"First 5 values        : {np.round(query_embedding[:5], 4)}")

    scores = embeddings @ query_embedding      
    order = np.argsort(-scores)                
    return scores, order


def display_top_results(scores, order):
    print(f"\n|==== TOP {TOP_N} MATCHES ====|\n")

    for rank, index in enumerate(order[:TOP_N], start=1):
        print(f"{rank}. [{topics[index]}] {sentences[index]}")
        print(f"   Similarity: {scores[index]:.4f}")

def get_query():
    while True:
        query = input("\nEnter your query: ").strip()
        if query:
            return query
        print("Query cannot be empty.")


def search_sentences(model, embeddings):
    query = get_query()
    scores, order = search(model, embeddings, query)
    display_top_results(scores, order)


def show_menu():
    print("\n===== SEMANTIC SENTENCE MATCHER =====")
    print("1. View All Sentences")
    print("2. Search by Meaning")
    print("3. Exit")
    print("=====================================")


def main():
    model = model_load()
    embeddings = get_embeddings(model)

    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            display_dataset()
        elif choice == "2":
            search_sentences(model, embeddings)
        elif choice == "3":
            print("Thank you! Bye.")
            break
        else:
            print("Invalid choice. Please enter 1-3.")


main()