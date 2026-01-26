import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# define vectors (these are arbitrary scores)
scores_zavier = np.array([88, 92])
scores_niko = np.array([94, 87])

# plot the vectors
try:
    plt.arrow(0, 0, scores_zavier[0], scores_zavier[1], width=1, color="blue")
    plt.arrow(0, 0, scores_niko[0], scores_niko[1], width=1, color="red")
except:
    pass

plt.axis([0, 100, 0, 100])
plt.show()