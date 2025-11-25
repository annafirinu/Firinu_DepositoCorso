import numpy as np

arr = np.array([1, 2, 3, 4])
scalar = 10

# Broadcasting aggiunge lo scalare a ogni elemento dell'array
result = arr + scalar
print(result) # Output: [11 12 13 14]