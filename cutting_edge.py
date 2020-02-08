import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

training_inputs = np.array([[1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
                            [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
                            [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
                            [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                            [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
                            [1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                            [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                            [1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
                            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                            [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1]])

training_outputs = np.array([[[1, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
                             [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0]],
                             [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0]],
                             [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0]],
                             [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0]],
                             [[0, 0, 0, 0, 0, 1, 0, 0, 0, 0]],
                             [[0, 0, 0, 0, 0, 0, 1, 0, 0, 0]],
                             [[0, 0, 0, 0, 0, 0, 0, 1, 0, 0]],
                             [[0, 0, 0, 0, 0, 0, 0, 0, 1, 0]],
                             [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]])

np.random.seed(1)

synaptic_weights = 2 * np.random.random((10, 15, 1)) - 1


for j in range(10):
    for i in range(20000):
        input_layer = training_inputs
        outputs = sigmoid(np.dot(input_layer, synaptic_weights[j]))

        err = training_outputs[j].T - outputs
        adjustments = np.dot(input_layer.T, err * (outputs * (1 - outputs)))

        synaptic_weights[j] += adjustments

print(synaptic_weights)
output = np.random.random((10))
# while input!=5:
# new_inputs

new_inputs = np.array([1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1])
for j in range(10):
    output[j] = sigmoid(np.dot(new_inputs, synaptic_weights[j]))
print("Новая ситуация: ")
for j in range(10):
    print(j, " : %.4f" % output[j])
