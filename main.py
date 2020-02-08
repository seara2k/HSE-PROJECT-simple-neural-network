import sys
from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5 import QtWidgets
# from PySide2 import QtCore, QtGui
from ui import Ui_Form
from bleeding_edge import NeuralNetwork
import numpy as np
# Create application

app = QtWidgets.QApplication(sys.argv)


# Form and ui
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()


# logic
def bc1():

    if ui.pushButton1.isChecked():
        input = ui.labelresult.text()
        output = "1" + input[1:15]
        ui.labelresult.setText(output)
    else:
        input = ui.labelresult.text()
        output = "0" + input[1:15]
        ui.labelresult.setText(output)
ui.pushButton1.toggled.connect(bc1)


def bc2():

    if ui.pushButton1_2.isChecked():
        input = ui.labelresult.text()
        output = input[0] + "1" + input[2:15]
        ui.labelresult.setText(output)
    else:
        input = ui.labelresult.text()
        output = input[0] + "0" + input[2:15]
        ui.labelresult.setText(output)
ui.pushButton1_2.toggled.connect(bc2)


def bc3():

    if ui.pushButton1_3.isChecked():
        input = ui.labelresult.text()
        output = input[0:2] + "1" + input[3:15]
        ui.labelresult.setText(output)
    else:
        input = ui.labelresult.text()
        output = input[0:2] + "0" + input[3:15]
        ui.labelresult.setText(output)
ui.pushButton1_3.toggled.connect(bc3)


def bc4():

    if ui.pushButton1_4.isChecked():
        input = ui.labelresult.text()
        output = input[0:3] + "1" + input[4:15]
        ui.labelresult.setText(output)
    else:
        input = ui.labelresult.text()
        output = input[0:3] + "0" + input[4:15]
        ui.labelresult.setText(output)
ui.pushButton1_4.toggled.connect(bc4)


def bc5():

    if ui.pushButton1_5.isChecked():
        input = ui.labelresult.text()
        output = input[0:4] + "1" + input[5:15]
        ui.labelresult.setText(output)
    else:
        input = ui.labelresult.text()
        output = input[0:4] + "0" + input[5:15]
        ui.labelresult.setText(output)
ui.pushButton1_5.toggled.connect(bc5)


def bc6():

    if ui.pushButton1_6.isChecked():
        input = ui.labelresult.text()
        output = input[0:5] + "1" + input[6:15]
        ui.labelresult.setText(output)
    else:
        input = ui.labelresult.text()
        output = input[0:5] + "0" + input[6:15]
        ui.labelresult.setText(output)
ui.pushButton1_6.toggled.connect(bc6)


def bc7():

    if ui.pushButton1_7.isChecked():
        input = ui.labelresult.text()
        output = input[0:6] + "1" + input[7:15]
        ui.labelresult.setText(output)
    else:
        input = ui.labelresult.text()
        output = input[0:6] + "0" + input[7:15]
        ui.labelresult.setText(output)
ui.pushButton1_7.toggled.connect(bc7)


def bc8():

    if ui.pushButton1_8.isChecked():
        input = ui.labelresult.text()
        output = input[0:7] + "1" + input[8:15]
        ui.labelresult.setText(output)
    else:
        input = ui.labelresult.text()
        output = input[0:7] + "0" + input[8:15]
        ui.labelresult.setText(output)
ui.pushButton1_8.toggled.connect(bc8)


def bc9():

    if ui.pushButton1_9.isChecked():
        input = ui.labelresult.text()
        output = input[0:8] + "1" + input[9:15]
        ui.labelresult.setText(output)
    else:
        input = ui.labelresult.text()
        output = input[0:8] + "0" + input[9:15]
        ui.labelresult.setText(output)
ui.pushButton1_9.toggled.connect(bc9)


def bc10():

    if ui.pushButton1_10.isChecked():
        input = ui.labelresult.text()
        output = input[0:9] + "1" + input[10:15]
        ui.labelresult.setText(output)
    else:
        input = ui.labelresult.text()
        output = input[0:9] + "0" + input[10:15]
        ui.labelresult.setText(output)
ui.pushButton1_10.toggled.connect(bc10)


def bc11():

    if ui.pushButton1_11.isChecked():
        input = ui.labelresult.text()
        output = input[0:10] + "1" + input[11:15]
        ui.labelresult.setText(output)
    else:
        input = ui.labelresult.text()
        output = input[0:10] + "0" + input[11:15]
        ui.labelresult.setText(output)
ui.pushButton1_11.toggled.connect(bc11)


def bc12():

    if ui.pushButton1_12.isChecked():
        input = ui.labelresult.text()
        output = input[0:11] + "1" + input[12:15]
        ui.labelresult.setText(output)
    else:
        input = ui.labelresult.text()
        output = input[0:11] + "0" + input[12:15]
        ui.labelresult.setText(output)
ui.pushButton1_12.toggled.connect(bc12)


def bc13():

    if ui.pushButton1_13.isChecked():
        input = ui.labelresult.text()
        output = input[0:12] + "1" + input[13:15]
        ui.labelresult.setText(output)
    else:
        input = ui.labelresult.text()
        output = input[0:12] + "0" + input[13:15]
        ui.labelresult.setText(output)
ui.pushButton1_13.toggled.connect(bc13)


def bc14():

    if ui.pushButton1_14.isChecked():
        input = ui.labelresult.text()
        output = input[0:13] + "1" + input[14:15]
        ui.labelresult.setText(output)
    else:
        input = ui.labelresult.text()
        output = input[0:13] + "0" + input[14:15]
        ui.labelresult.setText(output)
ui.pushButton1_14.toggled.connect(bc14)


def bc15():

    if ui.pushButton1_15.isChecked():
        input = ui.labelresult.text()
        output = input[0:14] + "1"
        ui.labelresult.setText(output)
    else:
        input = ui.labelresult.text()
        output = input[0:14] + "0"
        ui.labelresult.setText(output)
ui.pushButton1_15.toggled.connect(bc15)


def pognali():
	neural_network = NeuralNetwork()

	
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


	neural_network.train(training_inputs, training_outputs, 20000)
	neuro_input=ui.labelresult.text()
	neuro_input_mass=list(neuro_input)
	prediction=np.random.random((10))
	for i in range(10):
		prediction[i] = neural_network.think(np.array(neuro_input_mass),i)
		print(i, " : %.4f" % prediction[i])
	neuro_output_max=max(prediction)
	print(neuro_output_max)
	for j in range (10):
		if (prediction[j]==neuro_output_max):
			final=j
	ui.label.setText(str(final))


ui.GO.clicked.connect(pognali)
sys.exit(app.exec_())
