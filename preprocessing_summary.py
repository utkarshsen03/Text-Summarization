import re
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')


summary_text = "Machine learning (ML) is a discipline of artificial intelligence (AI) that provides machines with the ability to automatically learn from data and past experiences while identifying patterns to make predictions with minimal human intervention. Machine learning methods enable computers to operate autonomously without explicit programming. ML applications are fed with new data, and they can independently learn, grow, develop, and adapt. Machine learning derives insightful information from large volumes of data by leveraging algorithms to identify patterns and learn in an iterative process. ML algorithms use computation methods to learn directly from data instead of relying on any predetermined equation that may serve as a model. The performance of ML algorithms adaptively improves with an increase in the number of available samples during the ‘learning’ processes. For example, deep learning is a sub-domain of machine learning that trains computers to imitate natural human traits like learning from examples. It offers better performance parameters than conventional ML algorithms. While machine learning is not a new concept – dating back to World War II when the Enigma Machine was used – the ability to apply complex mathematical calculations automatically to growing volumes and varieties of available data is a relatively recent development. Today, with the rise of big data, IoT, and ubiquitous computing, machine learning has become essential for solving problems across numerous areas, such as"

clean_text = re.sub(r'\[\d+\]', '', summary_text)
sentences = nltk.sent_tokenize(clean_text)
# Join two sentences into one
joined_sentences = []
for i in range(0, len(sentences) - 1, 2):  # Iterates over every two sentences
    joined_sentences.append(f"{sentences[i]} {sentences[i + 1]}")

# Odd number of sentences
if len(sentences) % 2 != 0:
    joined_sentences.append(sentences[-1])

# Create bullet points 
bullet_points = '\n'.join([f"- {sentence}" for sentence in joined_sentences])

print(bullet_points)