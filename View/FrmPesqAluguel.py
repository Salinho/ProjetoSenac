# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmPesqAluguel.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Controller.AluguelCTR import AluguelCTR



class Ui_FrmPesqAluguel(object):
    def DevolverVeiculo(self):
        linha = self.tableWidget.currentItem().row()
        codigoAlug = self.tableWidget.item(linha, 0).text()
        dataDevol = self.edtDevolucao.text()
        valorMulta = self.edtMulta.text()
        kmSaida = self.edtSaida.text()

        aluguelCTR = AluguelCTR
        aluguelCTR.DevolverVeiculo(codigoAlug, dataDevol, valorMulta, kmSaida)

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText('Veiculo devolvido')
        msg.setWindowTitle('Devovler Veículo')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

        self.edtDevolucao.setText('')
        self.edtMulta.setText('')
        self.edtSaida.setText('')

    def PesquisarAluguel(self, valor, tipo):
        if (valor == ''):
            self.PesquisarTodosAluguel()
        else:
            aluguel = AluguelCTR
            query = aluguel.PesquisarAluguel(valor, tipo)

            while (self.tableWidget.rowCount() > 0):
                self.tableWidget.removeRow(0)
            
            row = 0
            while query.next():
                self.tableWidget.insertRow(row)
                codigoAlug = QtWidgets.QTableWidgetItem(str(query.value(0)))
                nomecliente = QtWidgets.QTableWidgetItem(str(query.value(10)))
                dataAlug = QtWidgets.QTableWidgetItem(str(query.value(1)))
                dataPrazo = QtWidgets.QTableWidgetItem(str(query.value(2)))
                dataDevolucao = QtWidgets.QTableWidgetItem(str(query.value(3)))
                valorAluguel = QtWidgets.QTableWidgetItem(str(query.value(4)))
                valorMulta = QtWidgets.QTableWidgetItem(str(query.value(5)))
                kmEntrada = QtWidgets.QTableWidgetItem(str(query.value(6)))
                kmSaida = QtWidgets.QTableWidgetItem(str(query.value(7)))

                self.tableWidget.setItem(row, 0, codigoAlug)
                self.tableWidget.setItem(row, 1, nomecliente)
                self.tableWidget.setItem(row, 2, dataAlug)
                self.tableWidget.setItem(row, 3, dataPrazo)
                self.tableWidget.setItem(row, 4, dataDevolucao)
                self.tableWidget.setItem(row, 5, valorAluguel)
                self.tableWidget.setItem(row, 6, valorMulta)
                self.tableWidget.setItem(row, 7, kmEntrada)
                self.tableWidget.setItem(row, 8, kmSaida)

                row = row + 1
        self.edtPesquisa.setText('')
    def PesquisarTodosAluguel(self):
        aluguel = AluguelCTR
        query = aluguel.PesquisarTodosAluguel()

        while (self.tableWidget.rowCount() > 0):
            self.tableWidget.removeRow(0)

        row = 0
        while query.next():
            self.tableWidget.insertRow(row)
            codigoAlug = QtWidgets.QTableWidgetItem(str(query.value(0)))
            nomecliente = QtWidgets.QTableWidgetItem(str(query.value(10)))
            dataAlug = QtWidgets.QTableWidgetItem(str(query.value(1)))
            dataPrazo = QtWidgets.QTableWidgetItem(str(query.value(2)))
            dataDevolucao = QtWidgets.QTableWidgetItem(str(query.value(3)))
            valorAluguel = QtWidgets.QTableWidgetItem(str(query.value(4)))
            valorMulta = QtWidgets.QTableWidgetItem(str(query.value(5)))
            kmEntrada = QtWidgets.QTableWidgetItem(str(query.value(6)))
            kmSaida = QtWidgets.QTableWidgetItem(str(query.value(7)))

            self.tableWidget.setItem(row, 0, codigoAlug)
            self.tableWidget.setItem(row, 1, nomecliente)
            self.tableWidget.setItem(row, 2, dataAlug)
            self.tableWidget.setItem(row, 3, dataPrazo)
            self.tableWidget.setItem(row, 4, dataDevolucao)
            self.tableWidget.setItem(row, 5, valorAluguel)
            self.tableWidget.setItem(row, 6, valorMulta)
            self.tableWidget.setItem(row, 7, kmEntrada)
            self.tableWidget.setItem(row, 8, kmSaida)    

            row = row + 1
    def setupUi(self, FrmPesqAluguel):
        FrmPesqAluguel.setObjectName("FrmPesqAluguel")
        FrmPesqAluguel.resize(519, 365)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../TesteProjeto/Imagens/btnListAluguel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrmPesqAluguel.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(FrmPesqAluguel)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 501, 71))
        self.groupBox.setObjectName("groupBox")
        self.cbPesquisa = QtWidgets.QComboBox(self.groupBox)
        self.cbPesquisa.setGeometry(QtCore.QRect(10, 40, 161, 22))
        self.cbPesquisa.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cbPesquisa.setObjectName("cbPesquisa")
        self.cbPesquisa.addItem("")
        self.cbPesquisa.addItem("")
        self.cbPesquisa.addItem("")
        self.cbPesquisa.addItem("")
        self.edtPesquisa = QtWidgets.QLineEdit(self.groupBox)
        self.edtPesquisa.setGeometry(QtCore.QRect(180, 40, 221, 20))
        self.edtPesquisa.setObjectName("edtPesquisa")

        #botão pesquisa
        self.btnPesquisa = QtWidgets.QPushButton(self.groupBox)
        self.btnPesquisa.setGeometry(QtCore.QRect(404, 10, 91, 51))
        self.btnPesquisa.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../../TesteProjeto/Imagens/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisa.setIcon(icon1)
        self.btnPesquisa.setIconSize(QtCore.QSize(30, 30))
        self.btnPesquisa.setObjectName("btnPesquisa")
        #pesquisar click
        self.btnPesquisa.clicked.connect(lambda: self.PesquisarAluguel(self.edtPesquisa.text(), self.cbPesquisa.currentText()))
        self.tableWidget = QtWidgets.QTableWidget(FrmPesqAluguel)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 501, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        #modo de seleção
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)


        self.groupBox_2 = QtWidgets.QGroupBox(FrmPesqAluguel)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 280, 501, 80))
        self.groupBox_2.setObjectName("groupBox_2")

        #botão deovlver
        self.btnDevolver = QtWidgets.QPushButton(self.groupBox_2)
        self.btnDevolver.setGeometry(QtCore.QRect(394, 10, 101, 61))
        self.btnDevolver.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../../TesteProjeto/Imagens/return.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDevolver.setIcon(icon2)
        self.btnDevolver.setIconSize(QtCore.QSize(30, 30))
        self.btnDevolver.setObjectName("btnDevolver")
        #click
        self.btnDevolver.clicked.connect(lambda: self.DevolverVeiculo())


        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label.setObjectName("label")
        self.edtDevolucao = QtWidgets.QLineEdit(self.groupBox_2)
        self.edtDevolucao.setGeometry(QtCore.QRect(10, 40, 113, 20))
        self.edtDevolucao.setObjectName("edtDevolucao")
        self.edtMulta = QtWidgets.QLineEdit(self.groupBox_2)
        self.edtMulta.setGeometry(QtCore.QRect(130, 40, 113, 20))
        self.edtMulta.setObjectName("edtMulta")
        self.edtSaida = QtWidgets.QLineEdit(self.groupBox_2)
        self.edtSaida.setGeometry(QtCore.QRect(250, 40, 113, 20))
        self.edtSaida.setObjectName("edtSaida")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(130, 20, 46, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(250, 20, 46, 13))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(FrmPesqAluguel)
        QtCore.QMetaObject.connectSlotsByName(FrmPesqAluguel)
        
        self.PesquisarTodosAluguel

    def retranslateUi(self, FrmPesqAluguel):
        _translate = QtCore.QCoreApplication.translate
        FrmPesqAluguel.setWindowTitle(_translate("FrmPesqAluguel", "Lista de Aluguéis", None))
        self.groupBox.setTitle(_translate("FrmPesqAluguel", "Selecione o Tipo de Pesquisa", None))
        self.cbPesquisa.setItemText(0, _translate("FrmPesqAluguel", "Código Aluguel", None))
        self.cbPesquisa.setItemText(1, _translate("FrmPesqAluguel", "Código Cliente", None))
        self.cbPesquisa.setItemText(2, _translate("FrmPesqAluguel", "Código Veículo", None))
        self.cbPesquisa.setItemText(3, _translate("FrmPesqAluguel", "Nome Cliente", None))
        self.btnPesquisa.setText(_translate("FrmPesqAluguel", "Pesquisar", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("FrmPesqAluguel", "Código Aluguel", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("FrmPesqAluguel", "Nome Cliente", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("FrmPesqAluguel", "Data Aluguel", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("FrmPesqAluguel", "Data Prazo", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("FrmPesqAluguel", "Data Devolução", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("FrmPesqAluguel", "Valor Aluguel", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("FrmPesqAluguel", "Valor Multa", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("FrmPesqAluguel", "Km Entrada", None))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("FrmPesqAluguel", "Km Saída", None))
        self.groupBox_2.setTitle(_translate("FrmPesqAluguel", "Devolver Veículo", None))
        self.btnDevolver.setText(_translate("FrmPesqAluguel", "Devolver", None))
        self.label.setText(_translate("FrmPesqAluguel", "Data Devolução", None))
        self.label_2.setText(_translate("FrmPesqAluguel", "Multa", None))
        self.label_3.setText(_translate("FrmPesqAluguel", "Km Saída", None))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmPesqAluguel = QtWidgets.QDialog()
    ui = Ui_FrmPesqAluguel()
    ui.setupUi(FrmPesqAluguel)
    FrmPesqAluguel.show()
    sys.exit(app.exec_())
