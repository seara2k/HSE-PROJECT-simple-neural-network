def button_function(button_name):
    if (len(button_name) == 11):
        button_number = button_name[len(button_name) - 1]
    else:
        button_number = button_name[len(button_name) - 2] + button_name[len(button_name) - 1]
    if getattr(ui, button_name).isChecked():
        input = ui.labelresult.text()
        output = input[0:button_number - 1] + "1" + input[button_number:15]
        ui.labelresult.setText(output)
    else:
        input = ui.labelresult.text()
        output = input[0:button_number - 1] + "0" + input[button_number:15]
        ui.labelresult.setText(output)


if __name__ == "__main__":
	pass
