import spacy
from scipy.spatial.distance import cosine

# load model
nlp = spacy.load('en_core_web_sm')

# define vectors
summer_vec = nlp("summer").vector
winter_vec = nlp("winter").vector

mustard_vec = nlp("mustard").vector
hotdog_vec = nlp("mayo").vector

# compare similarity
print(f"The cosine distance between the word embeddings for 'summer' and 'winter' is {cosine(summer_vec, winter_vec)}\n")
print(f"The cosine distance between 'mustard' and 'hotdog' is {cosine(mustard_vec, hotdog_vec)}.\n")

