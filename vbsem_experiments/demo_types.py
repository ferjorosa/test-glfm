import numpy as np

data = dict()
data['X'] = np.array([[1.0, 1, -0.3, 1, 1],[6.3, 2, 3.8, 23, np.nan],[11, 3, 4.1, 4, 2]]) # (N,D)
data['C'] = 'poGNc'

print(data['X'].dtype)

res = np.isnan(data['X'])