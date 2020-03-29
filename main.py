import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from ui import Ui_Form
from bleeding_edge import NeuralNetwork
import numpy as np


def button_function(button_name):
    if (len(button_name) == 11):
        button_number = button_name[len(button_name) - 1]
    else:
        button_number = button_name[
            len(button_name) - 2] + button_name[len(button_name) - 1]
    if getattr(ui, button_name).isChecked():
        input = ui.labelresult.text()
        output = input[0:int(button_number) - 1] + "1" + \
            input[int(button_number):15]
        ui.labelresult.setText(output)
    else:
        input = ui.labelresult.text()
        output = input[0:int(button_number) - 1] + "0" + \
            input[int(button_number):15]
        ui.labelresult.setText(output)


def clear():
    for i in range(15):
        button_name = 'pushButton' + str(i + 1)
        if getattr(ui, button_name).isChecked():
            getattr(ui, button_name).click()
    ui.console.clear()
    ui.label.setText("")
    ui.console.append("Cleared")
    QtTest.QTest.qWait(1500)
    ui.console.clear()


def teach(k):
    if (k[0] == '0'):

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
        ui.progressBar.setRange(0, 19999)
        ui.console.append("Teaching...")
        number = 0
        for j in range(10):
            for iteration in range(20000):

                number += 0.1
                ui.progressBar.setValue(number)
                neural_network.trainpro(training_inputs, training_outputs, j)

        ui.console.append("Weights found")
        k[0] = '1'
    else:
        ui.console.append("Already teached")


def go(k, neural_network):
    neuro_input = ui.labelresult.text()
    neuro_input_mass = list(neuro_input)
    prediction = np.random.random((10))
    ui.console.append('Chances')
    for i in range(10):
        prediction[i] = neural_network.think(np.array(neuro_input_mass), i)
        outputstr = str(i) + " : %0.2f" % (prediction[i]*100) +'%'
        ui.console.append(outputstr)
    neuro_output_max = max(prediction)
    for j in range(10):
        if (prediction[j] == neuro_output_max):
            final = j
    ui.label.setText(str(final))
    if (k[0] == '1'):    
        outputstr = 'Number is ' + str(final)
    else:
        outputstr = 'Not teached number is ' + str(final)
    ui.console.append(outputstr)


app = QtWidgets.QApplication(sys.argv)


Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()


k = list('0')
global neural_network
neural_network = NeuralNetwork()

ui.pushButton1.toggled.connect(lambda: button_function('pushButton1'))
ui.pushButton2.toggled.connect(lambda: button_function('pushButton2'))
ui.pushButton3.toggled.connect(lambda: button_function('pushButton3'))
ui.pushButton4.toggled.connect(lambda: button_function('pushButton4'))
ui.pushButton5.toggled.connect(lambda: button_function('pushButton5'))
ui.pushButton6.toggled.connect(lambda: button_function('pushButton6'))
ui.pushButton7.toggled.connect(lambda: button_function('pushButton7'))
ui.pushButton8.toggled.connect(lambda: button_function('pushButton8'))
ui.pushButton9.toggled.connect(lambda: button_function('pushButton9'))
ui.pushButton10.toggled.connect(lambda: button_function('pushButton10'))
ui.pushButton11.toggled.connect(lambda: button_function('pushButton11'))
ui.pushButton12.toggled.connect(lambda: button_function('pushButton12'))
ui.pushButton13.toggled.connect(lambda: button_function('pushButton13'))
ui.pushButton14.toggled.connect(lambda: button_function('pushButton14'))
ui.pushButton15.toggled.connect(lambda: button_function('pushButton15'))

ui.clearButton.clicked.connect(clear)
ui.teachButton.clicked.connect(lambda: teach(k))
ui.goButton.clicked.connect(lambda: go(k, neural_network))
ui.exitButton.clicked.connect(quit)


sys.exit(app.exec_())
