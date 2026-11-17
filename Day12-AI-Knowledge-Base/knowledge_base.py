import numpy as np

MODEL_NAME = "all-MiniLM-L6-v2"
EMBEDDINGS_FILE = "kb_embeddings.npy"
TOP_N = 5
CHUNK_SIZE = 2         
THRESHOLD = 0.35  

# [category, document name, full text]   (100 documents)
DATASET = [
    # ---------- Python (17) ----------
    ["Python", "Python Introduction", "Python is a high-level language known for readable code. It is widely used in web development, data science and automation."],
    ["Python", "Python Variables", "A variable stores a value such as a number or some text. Python does not need the type to be declared."],
    ["Python", "Python Lists", "Lists store many items in one ordered collection. Items can be added, removed or changed later."],
    ["Python", "Python Dictionaries", "Dictionaries keep data as key and value pairs. They give fast lookups using the key."],
    ["Python", "Python Functions", "Functions let us reuse the same code many times. They can take inputs and return results."],
    ["Python", "Python Loops", "Loops repeat instructions again and again. The for loop goes through items and the while loop runs until a condition fails."],
    ["Python", "Python Conditions", "The if, elif and else statements choose which code runs. The choice depends on whether a condition is true."],
    ["Python", "Python Errors", "Try and except blocks handle errors without crashing the program. They keep the program running when the input is wrong."],
    ["Python", "Python Classes", "Classes help us design programs around objects. An object bundles data and behaviour together."],
    ["Python", "Python Modules", "A module is a file of Python code that can be imported. Importing lets us reuse code written elsewhere."],
    ["Python", "Python Pip", "The pip tool installs extra libraries for Python. Libraries are downloaded from the PyPI website."],
    ["Python", "Python Virtual Environments", "Virtual environments keep project libraries separate. Each project can then use its own versions."],
    ["Python", "Python Strings", "Strings hold text and can be sliced or joined. Methods like lower and split change or break the text."],
    ["Python", "Python File Handling", "The open function reads and writes files. The with statement closes the file automatically."],
    ["Python", "Python Comprehensions", "List comprehensions build a new list in one line. They are a short way to write a loop."],
    ["Python", "Python Scope", "Variables made inside a function are local to it. Global variables can be used anywhere in the program."],
    ["Python", "Python Debugging", "Debugging means finding and fixing mistakes in code. Reading the error message is the first step."],

    # ---------- AI/ML (17) ----------
    ["AI/ML", "AI Introduction", "Artificial intelligence builds systems that do tasks needing human intelligence. Examples are chatbots, translation and image recognition."],
    ["AI/ML", "Machine Learning Basics", "Machine learning lets computers learn patterns from data. The program is not given fixed rules for every case."],
    ["AI/ML", "Supervised Learning", "Supervised learning trains a model using labelled examples. The model learns to predict the label for new data."],
    ["AI/ML", "Unsupervised Learning", "Unsupervised learning finds hidden groups in unlabelled data. Clustering is a common example."],
    ["AI/ML", "Overfitting", "Overfitting means a model memorises the training data. It then performs badly on new data."],
    ["AI/ML", "Train Test Split", "A train test split keeps some data aside for testing. It shows how well a model works on unseen data."],
    ["AI/ML", "Linear Regression", "Linear regression predicts a number from input features. It fits a straight line through the data."],
    ["AI/ML", "Classification", "Classification models put items into categories. A spam filter that sorts emails is one example."],
    ["AI/ML", "Decision Trees", "Decision trees make predictions by asking a series of questions. Each answer leads to another branch until a result is reached."],
    ["AI/ML", "Cross Validation", "Cross validation tests a model on several parts of the data. It gives a more reliable score than a single test."],
    ["AI/ML", "Feature Engineering", "Feature engineering creates better inputs for a model. Good features often improve accuracy more than a new algorithm."],
    ["AI/ML", "Neural Networks", "Neural networks are layers of connected nodes inspired by the brain. They learn by adjusting the weights between nodes."],
    ["AI/ML", "Deep Learning", "Deep learning uses many layers to learn complex patterns. It needs a lot of data and computing power."],
    ["AI/ML", "Large Language Models", "Large language models learn from huge amounts of text. They can answer questions and write text."],
    ["AI/ML", "Embeddings", "Embeddings turn text into numbers that capture its meaning. Similar meanings get vectors that are close together."],
    ["AI/ML", "Retrieval Augmented Generation", "Retrieval augmented generation gives a language model relevant documents. The model answers using that retrieved information."],
    ["AI/ML", "Vector Databases", "Vector databases store embeddings and find similar items fast. They are used in search and recommendation systems."],

    # ---------- NumPy (16) ----------
    ["NumPy", "NumPy Introduction", "NumPy is used for fast numerical computing with arrays. Many data science libraries are built on top of it."],
    ["NumPy", "NumPy Arrays", "The ndarray is the main data structure in NumPy. All its elements share the same data type."],
    ["NumPy", "NumPy Shape", "The shape of an array tells the size of each dimension. For a table it is the number of rows and columns."],
    ["NumPy", "NumPy Indexing", "Indexing picks a single value from an array. Negative indexes count from the end."],
    ["NumPy", "NumPy Slicing", "Slicing takes a range of rows or columns using a colon. The stop position is not included."],
    ["NumPy", "NumPy Boolean Indexing", "Boolean indexing selects array values that match a condition. A True and False mask decides which values stay."],
    ["NumPy", "NumPy Broadcasting", "Broadcasting lets arrays of different shapes work together. A single number can be added to every element."],
    ["NumPy", "NumPy Reshape", "The reshape function changes the shape of an array. The total number of elements must stay the same."],
    ["NumPy", "NumPy Statistics", "Functions like mean, median and std calculate statistics on arrays. The axis argument works along rows or columns."],
    ["NumPy", "NumPy Random", "NumPy has tools to generate random numbers. Setting a seed gives the same numbers every run."],
    ["NumPy", "NumPy Linear Algebra", "NumPy can do linear algebra such as matrix multiplication. The dot function multiplies vectors and matrices."],
    ["NumPy", "NumPy Vectorization", "Vectorized operations are much quicker than Python loops. They apply an operation to the whole array at once."],
    ["NumPy", "NumPy Missing Values", "Missing values are stored as nan in NumPy. Functions like nanmean ignore them."],
    ["NumPy", "NumPy Saving Data", "The save function stores an array in a file. The load function reads it back later."],
    ["NumPy", "NumPy Sorting", "The sort function arranges array values in order. The argsort function gives the positions of the sorted values."],
    ["NumPy", "NumPy Transpose", "Transpose swaps the rows and columns of an array. It is written as the T attribute."],

    # ---------- Pandas (16) ----------
    ["Pandas", "Pandas Introduction", "Pandas is a library for analysing and cleaning tabular data. It is built on top of NumPy."],
    ["Pandas", "Pandas DataFrame", "A DataFrame is a table with labelled rows and columns. It is the main object in Pandas."],
    ["Pandas", "Pandas Series", "A Series is a single labelled column of data. A DataFrame is made of many Series."],
    ["Pandas", "Pandas Read CSV", "The read_csv function loads a CSV file into a table. It is the usual first step of an analysis."],
    ["Pandas", "Pandas Groupby", "The groupby method summarises data by groups. For example it can find the average salary of each department."],
    ["Pandas", "Pandas Missing Values", "Missing values can be filled with fillna or removed with dropna. Cleaning them avoids wrong results."],
    ["Pandas", "Pandas Loc and Iloc", "The loc property picks rows and columns by their labels. The iloc property picks them by position."],
    ["Pandas", "Pandas Merge", "Two tables can be joined together using merge. It works like a join in a database."],
    ["Pandas", "Pandas Describe", "The describe method shows quick summary statistics. It gives the count, mean, minimum and maximum."],
    ["Pandas", "Pandas Filtering", "Rows can be filtered by writing a condition on a column. Only the rows that match are kept."],
    ["Pandas", "Pandas Sorting", "The sort_values method orders rows by a column. It can sort from small to large or the reverse."],
    ["Pandas", "Pandas Duplicates", "Duplicate rows can be found with duplicated. The drop_duplicates method removes them."],
    ["Pandas", "Pandas Apply", "The apply method runs a function on every row or column. It is useful for custom calculations."],
    ["Pandas", "Pandas Pivot Table", "A pivot table reorganises data into a summary grid. It shows totals for each pair of categories."],
    ["Pandas", "Pandas Rename", "The rename method changes column names. Clear names make the table easier to read."],
    ["Pandas", "Pandas Save Data", "The to_csv method writes a table to a CSV file. The cleaned data can then be shared."],

    # ---------- Company Policies (17) ----------
    ["Company Policy", "Leave Policy", "Every employee gets 14 days of paid annual leave. Leave must be requested at least three days in advance."],
    ["Company Policy", "Sick Leave Policy", "Employees get 7 days of paid sick leave each year. A medical certificate is needed for more than two days."],
    ["Company Policy", "Working Hours Policy", "Office hours are from 9 AM to 5 PM, Monday to Friday. A one hour lunch break is included."],
    ["Company Policy", "Remote Work Policy", "Employees may work from home two days a week. The manager must approve the days in advance."],
    ["Company Policy", "Dress Code Policy", "Staff should wear smart casual clothes at the office. Formal wear is needed when meeting clients."],
    ["Company Policy", "Salary Payment Policy", "Salaries are paid on the last working day of each month. Payment goes directly into the employee bank account."],
    ["Company Policy", "Overtime Policy", "Overtime must be approved by the manager before it is worked. Approved overtime is paid at one and a half times the normal rate."],
    ["Company Policy", "Code of Conduct", "Employees must behave respectfully and honestly at work. Breaking the code can lead to disciplinary action."],
    ["Company Policy", "Data Security Policy", "Company data must never be shared with outsiders. Confidential files should be stored only on approved systems."],
    ["Company Policy", "Password Policy", "Passwords must have at least 10 characters with numbers and symbols. They must be changed every 90 days."],
    ["Company Policy", "Internet Usage Policy", "Company internet is meant for work purposes. Streaming and social media are not allowed during working hours."],
    ["Company Policy", "Expense Claim Policy", "Work travel and meal costs can be claimed back with receipts. Claims must be submitted within 30 days."],
    ["Company Policy", "Holiday Policy", "The company observes all public holidays in Sri Lanka. The office stays closed on those days."],
    ["Company Policy", "Resignation Policy", "An employee who resigns must give 30 days written notice. All company equipment must be returned on the last day."],
    ["Company Policy", "Harassment Policy", "The company does not tolerate harassment of any kind. Complaints can be reported to the HR department in confidence."],
    ["Company Policy", "Performance Review Policy", "Performance is reviewed every six months. The review looks at goals, teamwork and quality of work."],
    ["Company Policy", "Equipment Policy", "Laptops and tools are given for work use only. Employees must take care of them and report any damage."],

    # ---------- Training Information (17) ----------
    ["Training", "Training Attendance Policy", "Interns must attend every training session. Missing a session without notice may reduce the final evaluation marks."],
    ["Training", "Training Schedule", "Training sessions start at 9 AM and finish at 4 PM. Sessions run from Monday to Friday."],
    ["Training", "Training Certificate", "A certificate is given after the internship is completed. It requires good attendance and all tasks submitted."],
    ["Training", "Training Assignments", "A practical task is given at the end of each day. Interns must finish it and submit it before the next session."],
    ["Training", "Training Mentor Support", "Each intern has a mentor who answers technical questions. Mentors are available during training hours."],
    ["Training", "Training Internship Duration", "The internship lasts for three months. The first month is training and the rest is project work."],
    ["Training", "Training GitHub Submission", "All tasks must be uploaded to a GitHub repository. Work should be committed in small steps with clear messages."],
    ["Training", "Training Daily Report", "Interns submit a daily report on the portal. It includes the work description, GitHub link and hours spent."],
    ["Training", "Training Assessment", "Interns are assessed on tasks, reports and attendance. Marks are shared with the mentor each week."],
    ["Training", "Training Missed Session", "If an intern misses a session, the mentor must be informed. The intern should study the recording and complete the missed task."],
    ["Training", "Training Laptop Requirements", "Interns should bring a laptop with at least 8 GB of memory. Python and Git must be installed before the first day."],
    ["Training", "Training Venue", "Training is held at the main office training room on the second floor. Remote sessions are announced by email."],
    ["Training", "Training Feedback", "Interns can give feedback after every week of training. The feedback helps improve the next sessions."],
    ["Training", "Training Project Evaluation", "The final project is presented to a panel of engineers. It is judged on correctness, code quality and explanation."],
    ["Training", "Training Language Support", "Sessions are taught in English with Tamil and Sinhala explanations when needed. Notes are shared in English."],
    ["Training", "Training Breaks", "There is a 15 minute tea break in the morning and afternoon. Lunch is one hour from 12 PM."],
    ["Training", "Training Completion", "The internship is complete when all tasks and the final project are submitted. HR then issues the completion letter."],
]

chunks = []
categories = []
doc_names = []


def main():
    print("Total documents:", len(DATASET))


main()