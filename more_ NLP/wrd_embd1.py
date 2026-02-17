
"""
- Cosine, Cityblock (Manhattan), and Euclidean are three commonly used distance or
similarity metrics in machine learning and data science.
- Euclidean (L2 norm): measures the straight line distance between two points.
- Cityblock (Manhattan/L1 norm): measures distance as the sum of absolute differences
across dimensions, similar to traveling along a grid.
- Cosine Similarity: measures the cosine of the angle between two vectors, focusing on
orientation rather than magnitude.
"""



import spacy
from scipy.spatial.distance import cosine, cityblock, euclidean

# load model
nlp = spacy.load('en_core_web_sm')

# define vectors
summer_vec = nlp("summer").vector
winter_vec = nlp("winter").vector

mustard_vec = nlp("mustard").vector
hotdog_vec = nlp("hotdog").vector

# compare cosine similarity
print(f"The cosine distance between the word embeddings for 'summer' and 'winter' is {cosine(summer_vec, winter_vec)}\n")
print(f"The cosine distance between 'mustard' and 'hotdog' is {cosine(mustard_vec, hotdog_vec)}.\n")

# cityblock
print(f"city block: {cityblock(summer_vec, winter_vec)}")

# euclidean
print(f"euclidean: {euclidean(mustard_vec, hotdog_vec)}")

