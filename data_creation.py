import numpy as np

# TODO: Modify the training data later to see how it impacts the program

# Array of arrays, each subarray having both terms to be added
train_data = np.array([[1.0, 1.0]])

# Array of arrays, each subarray having the expected output for the
# corresponding index in the train_data array
train_targets = np.array([[2.0]])

for i in range(3, 10000, 2):
    train_data = np.append(train_data, [[i, i]], axis=0)
    train_targets = np.append(train_targets, [[i + i]])

test_data = np.array([[2.0, 2.0]])
test_target = np.array([[4.0]])

for i in range(4, 8000, 4):
    test_data = np.append(test_data, [[i, i]], axis=0)
    test_target = np.append(test_target, [[i + i]])
