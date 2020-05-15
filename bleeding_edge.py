import numpy as np





class NeuralNetwork():

    def __init__(self):
        # Сид генератора чисел для одинаковой работы программы
        np.random.seed(1)

        # Задаём случайные веса(10 цифр по 15 клеточек)
        self.synaptic_weights = 2 * np.random.random((10, 15, 1)) - 1

    def sigmoid(self, x):
        """
		Сигмоида
        """
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        """
		Производная сигмоиды
        """
        return x * (1 - x)


    def trainpro(self, training_inputs, training_outputs,j):

        """
		Обучение методом обратного распространения
		Один цикл нужен для прогресс бара
        """

        output = self.think(training_inputs, j)

        error = training_outputs[j].T - output

        adjustments = np.dot(
            training_inputs.T, error * self.sigmoid_derivative(output))

        self.synaptic_weights[j] += adjustments

    def train(self, training_inputs, training_outputs, training_iterations):
        """
		Обучение методом обратного распространения
        """
        for j in range(10):
            for iteration in range(training_iterations):
                output = self.think(training_inputs, j)

   
                error = training_outputs[j].T - output


                adjustments = np.dot(
                    training_inputs.T, error * self.sigmoid_derivative(output))


                self.synaptic_weights[j] += adjustments
               

    def think(self, inputs, number):
        """
        Функция которая пропускает данные через нейросеть и выдаёт вердикт
        """

        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights[number]))
        return output


if __name__ == "__main__":

    # Инициализация нейросети
    neural_network = NeuralNetwork()

    # Тренировочные данные, состоящие из 10 цифр
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
    # Выходные данные на каждую цифру
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

    # Вызов функции тренировки
    neural_network.train(training_inputs, training_outputs, 20000)

    print(neural_network.synaptic_weights)

    print("Output data: ")
    for j in range(10):
        print(j, " : %.4f" % neural_network.think(
            np.array([1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1]), j))
