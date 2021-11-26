# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmPesqCliente.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmPesqCliente(object):
    def setupUi(self, frmPesqCliente):
        frmPesqCliente.setObjectName("frmPesqCliente")
        frmPesqCliente.resize(651, 504)
        self.gridCliente = QtWidgets.QTableWidget(frmPesqCliente)
        self.gridCliente.setGeometry(QtCore.QRect(20, 150, 621, 291))
        self.gridCliente.setObjectName("gridCliente")
        self.gridCliente.setColumnCount(6)
        self.gridCliente.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.gridCliente.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridCliente.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridCliente.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridCliente.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridCliente.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridCliente.setHorizontalHeaderItem(5, item)
        self.edtPesquisa = QtWidgets.QLineEdit(frmPesqCliente)
        self.edtPesquisa.setGeometry(QtCore.QRect(190, 60, 451, 20))
        self.edtPesquisa.setObjectName("edtPesquisa")
        self.cbPesquisa = QtWidgets.QComboBox(frmPesqCliente)
        self.cbPesquisa.setGeometry(QtCore.QRect(20, 60, 161, 22))
        self.cbPesquisa.setObjectName("cbPesquisa")
        self.cbPesquisa.addItem("")
        self.cbPesquisa.addItem("")
        self.cbPesquisa.addItem("")
        self.label = QtWidgets.QLabel(frmPesqCliente)
        self.label.setGeometry(QtCore.QRect(20, 30, 271, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnPesquisar = QtWidgets.QPushButton(frmPesqCliente)
        self.btnPesquisar.setGeometry(QtCore.QRect(530, 92, 111, 51))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../TesteProjeto/Imagens/Lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisar.setIcon(icon)
        self.btnPesquisar.setIconSize(QtCore.QSize(30, 30))
        self.btnPesquisar.setObjectName("btnPesquisar")
        self.lblTotal = QtWidgets.QLabel(frmPesqCliente)
        self.lblTotal.setGeometry(QtCore.QRect(20, 450, 111, 16))
        self.lblTotal.setObjectName("lblTotal")
        self.btnExcluir = QtWidgets.QPushButton(frmPesqCliente)
        self.btnExcluir.setGeometry(QtCore.QRect(554, 450, 91, 51))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../../TesteProjeto/Imagens/delete-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExcluir.setIcon(icon1)
        self.btnExcluir.setIconSize(QtCore.QSize(30, 30))
        self.btnExcluir.setObjectName("btnExcluir")
        self.btnAlterar = QtWidgets.QPushButton(frmPesqCliente)
        self.btnAlterar.setGeometry(QtCore.QRect(450, 450, 101, 51))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../../TesteProjeto/Imagens/editar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAlterar.setIcon(icon2)
        self.btnAlterar.setIconSize(QtCore.QSize(35, 35))
        self.btnAlterar.setObjectName("btnAlterar")

        self.retranslateUi(frmPesqCliente)
        QtCore.QMetaObject.connectSlotsByName(frmPesqCliente)

    def retranslateUi(self, frmPesqCliente):
        _translate = QtCore.QCoreApplication.translate
        frmPesqCliente.setWindowTitle(_translate("frmPesqCliente", "Lista de Cliente"))
        item = self.gridCliente.horizontalHeaderItem(0)
        item.setText(_translate("frmPesqCliente", "Código"))
        item = self.gridCliente.horizontalHeaderItem(1)
        item.setText(_translate("frmPesqCliente", "Nome"))
        item = self.gridCliente.horizontalHeaderItem(2)
        item.setText(_translate("frmPesqCliente", "CPF"))
        item = self.gridCliente.horizontalHeaderItem(3)
        item.setText(_translate("frmPesqCliente", "Endereço"))
        item = self.gridCliente.horizontalHeaderItem(4)
        item.setText(_translate("frmPesqCliente", "Email"))
        item = self.gridCliente.horizontalHeaderItem(5)
        item.setText(_translate("frmPesqCliente", "Telefone"))
        self.cbPesquisa.setItemText(0, _translate("frmPesqCliente", "Código"))
        self.cbPesquisa.setItemText(1, _translate("frmPesqCliente", "Nome"))
        self.cbPesquisa.setItemText(2, _translate("frmPesqCliente", "CPF"))
        self.label.setText(_translate("frmPesqCliente", "Selecione o Tipo de Pesquisa:"))
        self.btnPesquisar.setText(_translate("frmPesqCliente", "Pesquisar"))
        self.lblTotal.setText(_translate("frmPesqCliente", "TextLabel"))
        self.btnExcluir.setText(_translate("frmPesqCliente", "Excluir"))
        self.btnAlterar.setText(_translate("frmPesqCliente", "Alterar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmPesqCliente = QtWidgets.QDialog()
    ui = Ui_frmPesqCliente()
    ui.setupUi(frmPesqCliente)
    frmPesqCliente.show()
    sys.exit(app.exec_())
