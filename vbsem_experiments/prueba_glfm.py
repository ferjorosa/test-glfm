import numpy as np

y = np.array([2.45, -0.06, 0.0], np.float)
# transformation function for categorical data
# input argument y: [N*R]
# output: x [N*1]
#assert (len(y.shape) > 1), 'there is only one category, this dimension does not make sense'
x = np.zeros(y.shape[0])
for i in xrange(y.shape[0]):
    val = max(y[i,:])
    x[i] = np.where(y[i,:] == val)[0][0] + 1
# [a,x] = max(y,[],2);