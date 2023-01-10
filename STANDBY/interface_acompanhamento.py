from PyQt5 import uic, QtWidgets

def funcao_secundaria():
    print("teste")

app = QtWidgets.QApplication([])
formulario=uic.loadUi("acompanhamento.ui")
formulario.pushButton.clicked.connect(funcao_secundaria)
formulario.show()
app.exec()
