import numpy as np


class NeuralNetwork():

    def __init__(self):
        # Seed the random number generator
        np.random.seed(1)

        # Set synaptic weights to a 3x1 matrix,
        # with values from -1 to 1 and mean 0
        self.synaptic_weights = 2 * np.random.random((10, 15, 1)) - 1

    def sigmoid(self, x):
        """
        Takes in weighted sum of the inputs and normalizes
        them through between 0 and 1 through a sigmoid function
        """
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        """
        The derivative of the sigmoid function used to
        calculate necessary weight adjustments
        """
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iterations):
        """
        We train the model through trial and error, adjusting the
        synaptic weights each time to get a better result
        """
        for j in range(10):
            for iteration in range(training_iterations):
             # Pass training set through the neural network
                output = self.think(training_inputs, j)

            # Calculate the error rate
                error = training_outputs[j].T - output

            # Multiply error by input and gradient of the sigmoid function
            # Less confident weights are adjusted more through the nature of
            # the function
                adjustments = np.dot(
                    training_inputs.T, error * self.sigmoid_derivative(output))

            # Adjust synaptic weights
                self.synaptic_weights[j] += adjustments

    def think(self, inputs, number):
        """
        Pass inputs through the neural network to get output
        """

        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights[number]))
        return output


if __name__ == "__main__":

    # Initialize the single neuron neural network
    neural_network = NeuralNetwork()

    #print("Random starting synaptic weights: ")
   # print(neural_network.synaptic_weights)

    # The training set, with 4 examples consisting of 3
    # input values and 1 output value
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

    # Train the neural network
    neural_network.train(training_inputs, training_outputs, 20000)

    print(neural_network.synaptic_weights)

    print("Output data: ")
    for j in range(10):
        print(j, " : %.4f" % neural_network.think(
            np.array([1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1]), j))
