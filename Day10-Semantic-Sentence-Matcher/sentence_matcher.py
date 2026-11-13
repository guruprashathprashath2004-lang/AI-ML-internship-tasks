import numpy as np

MODEL_NAME = "all-MiniLM-L6-v2"
EMBEDDINGD_FILE = "sentence_embedding.npy"
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


def main():
    print(f"Total Sentences : {len(sentences)}")
    print(sentences[0], "->", topics[0])


main()