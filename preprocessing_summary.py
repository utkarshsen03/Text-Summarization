import re
import nltk

# Download the punkt tokenizer for sentence splitting
nltk.download('punkt')

# Original text with reference brackets removed
summary_text = "In 1986, BMW established a head office in Canada.[144] BMW sold 28,149 vehicles in Canada in 2008.[145] BMW Japan Corp, a wholly owned subsidiary, imports and distributes BMW vehicles in Japan.[146] BMW Philippines, an owned subsidiary of San Miguel Corporation, is the official importer and distributor of BMW in the Philippines.[147] BMW sold 920 vehicles in the Philippines in 2019.[148] BMW Korea imports BMW vehicles in South Korea with more than fifty service centers to fully cater to South Korean customers.The design of the bike was inspired by the company's BMW R1200 GS model.[50] The current model lines of BMW cars are: The current model lines of the X Series SUVs and crossovers are: The current model line of the Z Series two-door roadsters is the Z4 (model code G29). In Uruguay, Spanish-born businessman José Arijón founded Convex (later Camur), which assembled BMW cars from 1965 to 1992.Many BMW's are still produced in this layout, which is designated the R Series. Also, BMW Korea has its own driving center in Incheon.[149] BMW has received criticism for attempting to lock vehicle hardware features behind subscription fees."

# Remove references in brackets
clean_text = re.sub(r'\[\d+\]', '', summary_text)

# Tokenize the text into sentences using NLTK
sentences = nltk.sent_tokenize(clean_text)

# Join every two consecutive sentences into one
joined_sentences = []
for i in range(0, len(sentences) - 1, 2):  # Iterates over every two sentences
    joined_sentences.append(f"{sentences[i]} {sentences[i + 1]}")

# If there is an odd number of sentences, append the last sentence as is
if len(sentences) % 2 != 0:
    joined_sentences.append(sentences[-1])

# Create bullet points for each joined sentence
bullet_points = '\n'.join([f"- {sentence}" for sentence in joined_sentences])

print(bullet_points)
