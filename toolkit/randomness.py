
import numpy as np

def entropy(values):
    values=list(values)
    unique=set(values)
    probs=[values.count(v)/len(values) for v in unique]
    return -sum(p*np.log2(p) for p in probs)
