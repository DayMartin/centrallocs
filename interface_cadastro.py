from PyQt5 import QtCore, QtGui, QtWidgets, uic
import mysql.connector
from mysql.connector import Error
import PyQt5.QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtPrintSupport import *
import datetime
from PyQt5.QtWidgets import QMessageBox

import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem
from mysql.connector import errorcode

from sqlalchemy import create_engine
import pymysql

import sys
import requests

ip_publico = requests.get('https://api.ipify.org/').text
print(f'IP Publico: {ip_publico}')

qtCreatorFile = "aba_cadastro.ui" #Esse é o arquivo .ui gerado pelo QtDesigner
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


def connectar():
        global banco 
        banco = mysql.connector.connect(
           host= '35.237.99.182',
           user='dinahdoria',
           passwd='teste123',
            database='centralloc')

#ABA DE COTAÇÃO 
def funcao_principal():
    connectar()
    cursor = banco.cursor()

    linha = formulario.lineEdit.text() 
    linha11 = formulario.lineEdit_11.text()
    linha12 = formulario.lineEdit_12.text()
    linha15 = formulario.lineEdit_15.text()
    linha16 = formulario.lineEdit_16.text()
    linha17 = formulario.lineEdit_17.text()
    linha18 = formulario.lineEdit_18.text()
    linha19 = formulario.lineEdit_19.text()
    linha20 = formulario.lineEdit_20.text()
    linha21 = formulario.lineEdit_21.text()
    linha23 = formulario.lineEdit_23.text()
    linha22 = formulario.lineEdit_22.text()
    linha14 = formulario.lineEdit_14.text()

    nome_solicitante = "" 
    categoria_solicitada = ""
    tipo_retirada = ""

    #SOLICITANTE

    if formulario.checkBox.isChecked():
        print("SOLICITANTE: MONIQUE PONTES")
        nome_solicitante = "Monique Pontes"

    elif formulario.checkBox_2.isChecked():
        print("SOLICITANTE: MARCOS ROBERTO")
        nome_solicitante = "Marcos Roberto"

    elif formulario.checkBox_3.isChecked():
        print("SOLICITANTE: JULIANA VASCONCELOS")
        nome_solicitante = "Juliana Vasconcelos"


    # CATEGORIA SOLICITADA

    if formulario.checkBox_4.isChecked():
        print("CATEGORIA SOLICITADA: A")
        categoria_solicitada = "A"
    elif formulario.checkBox_5.isChecked():
        print("CATEGORIA SOLICITADA: B")
        categoria_solicitada = "B"
    elif formulario.checkBox_6.isChecked():
        print("CATEGORIA SOLICITADA: C")
        categoria_solicitada = "C"
    elif formulario.checkBox_7.isChecked():
        print("CATEGORIA SOLICITADA: D")
        categoria_solicitada = "D"
    elif formulario.checkBox_8.isChecked():
        print("CATEGORIA SOLICITADA: E")
        categoria_solicitada = "E"
    elif formulario.checkBox_9.isChecked():
        print("CATEGORIA SOLICITADA: F")
        categoria_solicitada = "F"
    elif formulario.checkBox_10.isChecked():
        print("CATEGORIA SOLICITADA: FX")
        categoria_solicitada = "FX"
    elif formulario.checkBox_11.isChecked():
        print("CATEGORIA SOLICITADA: G")
        categoria_solicitada = "G"
    elif formulario.checkBox_12.isChecked():
        print("CATEGORIA SOLICITADA: L")
        categoria_solicitada = "L"
    elif formulario.checkBox_13.isChecked():
        print("CATEGORIA SOLICITADA: QX")
        categoria_solicitada = "QX"
    elif formulario.checkBox_14.isChecked():
        print("CATEGORIA SOLICITADA: SS")
        categoria_solicitada = "SS" 

    #TIPO DE ENTREGA
  
    if formulario.checkBox_15.isChecked():
        print("RETIRADA: LOJA")
        tipo_retirada = "LOJA"
    elif formulario.checkBox_16.isChecked():
        print("RETIRADA: ENTREGA E RETIRADA")
        tipo_retirada = "ENTREGA E RETIRADA" 


    #CADASTRO NA TABELA ACOMPANHAMENTO
    connectar()
    cursor = banco.cursor()
    comandoSQL = """
        INSERT INTO reserva_acompanhamento (
        nmr_solicitacao_dynamics,
        nome_solicitante,
        categoria_solicitada,
        nome_condutor,
        cpf_condutor,
        nome_locadora,
        data_ret,
        data_dev,
        qnt_diarias_iniciais,
        mod_vei,
        nome_cnss,
        assistencia_id_juvo,
        chassi_veiculo_condutor,
        nmr_resv_juvo,
        tipo_retirada,
        status_reserva
        ) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""   
    dados = (str(linha),nome_solicitante,categoria_solicitada,str(linha21),str(linha23),str(linha22),str(linha18),str(linha19),str(linha20),str(linha11),str(linha17),str(linha15),str(linha16),str(linha12),tipo_retirada,str(linha14))
    cursor.execute(comandoSQL,dados)
    banco.commit()
    
    #LIMPANDO OS DADOS APÓS CADASTRAR ELEMENTOS NA TABELA
    formulario.lineEdit.setText("")
    formulario.lineEdit_11.setText("")
    formulario.lineEdit_12.setText("")
    formulario.lineEdit_15.setText("")
    formulario.lineEdit_16.setText("")
    formulario.lineEdit_17.setText("")
    formulario.lineEdit_18.setText("")
    formulario.lineEdit_19.setText("")
    formulario.lineEdit_20.setText("")
    formulario.lineEdit_21.setText("")
    formulario.lineEdit_23.setText("")
    formulario.lineEdit_22.setText("")

    cursor.close()
    banco.close()



#ABA DE ACOMPANHAMENTO 
def chama_aba_acompanhamento():
    connectar()
    acompanhamento_reserva.show()
    cursor = banco.cursor()
    comando_SQL_2 = "SELECT * FROM reserva_acompanhamento;" 
    cursor.execute(comando_SQL_2)
    dados_lidos = cursor.fetchall()
    print(dados_lidos)

    acompanhamento_reserva.tableWidget.setRowCount(len(dados_lidos))
    acompanhamento_reserva.tableWidget.setColumnCount(18)

    for i in range(0,len(dados_lidos)):
        for j in range(0,18):
            acompanhamento_reserva.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    cursor.close()
    banco.close()

#PESQUISAR POR CPF
def pesquisa_id(): 
        connectar()
        dbname = acompanhamento_reserva.lineEdit.text()
        cursor = banco.cursor()
        comando_SQL_2 = "SELECT * FROM reserva_acompanhamento WHERE cpf_condutor = {} ".format(dbname)
        cursor.execute(comando_SQL_2)
        dados_lidos = cursor.fetchall()
        print(dados_lidos)

        acompanhamento_reserva.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(dados_lidos):
            print(row_number)
            acompanhamento_reserva.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                acompanhamento_reserva.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        banco.close()
        cursor.close()

#class atualizar():  
    #global mostrar_dados
    #global pesquisa_id_aba_atualizar
    #global Preencher_campos_auto
    #global Pega_selecao_do_banco
    #global atualizar_reserva
    #global pega_id_tabela
    #global ID_SQL
    #global closeEvent

    #Mostrar todas as reservas
def mostrar_dados():
        connectar()
        aba_atualiza.show()
        cursor = banco.cursor()
        comando_SQL_2 = "SELECT * FROM reserva_acompanhamento;" 
        cursor.execute(comando_SQL_2)
        dados_lidos = cursor.fetchall()
        print(dados_lidos)

        aba_atualiza.tableWidget.setRowCount(len(dados_lidos))
        aba_atualiza.tableWidget.setColumnCount(18)

        for i in range(0,len(dados_lidos)):
            for j in range(0,18):
                aba_atualiza.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

        cursor.close()
        banco.close()

    #Pesquisar por CPF do condutor
def pesquisa_id_aba_atualizar(): 
        connectar()
        dbname = aba_atualiza.lineEdit.text()
        cursor = banco.cursor()
        comando_SQL_2 = "SELECT * FROM reserva_acompanhamento WHERE cpf_condutor = {} ".format(dbname)
        cursor.execute(comando_SQL_2)
        dados_lidos = cursor.fetchall()
        print(dados_lidos)

        aba_atualiza.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(dados_lidos):
            print(row_number)
            aba_atualiza.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                aba_atualiza.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        cursor.close()
        banco.close()

    #Seleciona  a linha clicada perante a tabela 
def Pega_selecao_do_banco():
        connectar()
        cursor = banco.cursor()
        return aba_atualiza.tableWidget.currentRow()
        cursor.close()
        banco.close()

    #Preencher os campos para edição automaticamente após clicar na linha
def Preencher_campos_auto():
        connectar()
        cursor = banco.cursor()
        global id_linha_selecionada
        id_linha_selecionada = Pega_selecao_do_banco()
        print(id_linha_selecionada)
        
        N_Solicitacao = aba_atualiza.tableWidget.item(id_linha_selecionada,1).text()
        Solicitante =  aba_atualiza.tableWidget.item(id_linha_selecionada,2).text()
        Assistencia =  aba_atualiza.tableWidget.item(id_linha_selecionada,3).text()
        CPF_Condutor = aba_atualiza.tableWidget.item(id_linha_selecionada,4).text()
        Nome_Condutor = aba_atualiza.tableWidget.item(id_linha_selecionada,5).text()
        Chassi = aba_atualiza.tableWidget.item(id_linha_selecionada,6).text()
        Locadora = aba_atualiza.tableWidget.item(id_linha_selecionada,7).text()
        N_Reserva = aba_atualiza.tableWidget.item(id_linha_selecionada,8).text()
        Categoria = aba_atualiza.tableWidget.item(id_linha_selecionada,9).text()
        Data_Retirada = aba_atualiza.tableWidget.item(id_linha_selecionada,10).text()
        Data_Devolucao= aba_atualiza.tableWidget.item(id_linha_selecionada,11).text()
        Qnt_diarias_iniciais = aba_atualiza.tableWidget.item(id_linha_selecionada,12).text()
        Modelo_Veiculo = aba_atualiza.tableWidget.item(id_linha_selecionada,13).text()
        Concessionaria = aba_atualiza.tableWidget.item(id_linha_selecionada,14).text()
        status_reserva = aba_atualiza.tableWidget.item(id_linha_selecionada,15).text()
        Qtd_diarias_totais = aba_atualiza.tableWidget.item(id_linha_selecionada,16).text()
        tipo_retirada = aba_atualiza.tableWidget.item(id_linha_selecionada,17).text()

        aba_atualiza.lineEdit_4.setText(N_Solicitacao)
        aba_atualiza.lineEdit_5.setText(Solicitante)
        aba_atualiza.lineEdit_6.setText(Assistencia)
        aba_atualiza.lineEdit_7.setText(CPF_Condutor)
        aba_atualiza.lineEdit_8.setText(Nome_Condutor)
        aba_atualiza.lineEdit_9.setText(Chassi)
        aba_atualiza.lineEdit_10.setText(Locadora)
        aba_atualiza.lineEdit_11.setText(N_Reserva)
        aba_atualiza.lineEdit_12.setText(Categoria)
        aba_atualiza.lineEdit_13.setText(Data_Retirada)
        aba_atualiza.lineEdit_14.setText(Data_Devolucao)
        aba_atualiza.lineEdit_15.setText(Qnt_diarias_iniciais)
        aba_atualiza.lineEdit_16.setText(Modelo_Veiculo)
        aba_atualiza.lineEdit_17.setText(Concessionaria)
        aba_atualiza.lineEdit_18.setText(status_reserva)
        aba_atualiza.lineEdit_19.setText(Qtd_diarias_totais)
        aba_atualiza.lineEdit_20.setText(tipo_retirada)
        banco.close()

    #Pega o id da linha
def pega_id_tabela(): 
        connectar()
        cursor = banco.cursor()
        valor = aba_atualiza.tableWidget.item(Pega_selecao_do_banco(), 0)
        return valor.text() if not valor is None else valor 
        cursor = banco.cursor()
        banco.close()

    #BOTÃO ATUALIZAR
def atualizar_reserva():
        connectar()
        cursor = banco.cursor()

        #try:
            
        #    print("Connection established")
        #except mysql.connector.Error as err:
        #    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        #        print("Something is wrong with the user name or password")
        #    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        #        print("Database does not exist")
        #    else:
        #         print(err)  
    

        N_Solicitacao = aba_atualiza.lineEdit_4.text()
        Solicitante = aba_atualiza.lineEdit_5.text()
        Assistencia = aba_atualiza.lineEdit_6.text()
        CPF_Condutor = aba_atualiza.lineEdit_7.text()
        Nome_Condutor = aba_atualiza.lineEdit_8.text()
        Chassi = aba_atualiza.lineEdit_9.text()
        Locadora = aba_atualiza.lineEdit_10.text()
        N_Reserva = aba_atualiza.lineEdit_11.text()
        Categoria = aba_atualiza.lineEdit_12.text()
        Data_Retirada = aba_atualiza.lineEdit_13.text()
        Data_Devolucao= aba_atualiza.lineEdit_14.text()
        Qnt_diarias_iniciais = aba_atualiza.lineEdit_15.text()
        Modelo_Veiculo = aba_atualiza.lineEdit_16.text()
        Concessionaria = aba_atualiza.lineEdit_17.text()
        status_reserva = aba_atualiza.lineEdit_18.text()
        Qtd_diarias_totais = aba_atualiza.lineEdit_19.text() 
        Tipo_retirada = aba_atualiza.lineEdit_20.text()


        cursor.execute("SELECT id_reserva_sql FROM reserva_acompanhamento")
        dados_lidos = cursor.fetchall()
        valor_id = dados_lidos[id_linha_selecionada][0]

        comandoSQL_6 = ("UPDATE reserva_acompanhamento SET nmr_solicitacao_dynamics = '{}', nome_solicitante = '{}', assistencia_id_juvo = '{}', CPF_Condutor = '{}', nome_condutor = '{}', chassi_veiculo_condutor = '{}', nome_locadora = '{}', nmr_resv_juvo = '{}', categoria_solicitada = '{}', data_ret = '{}', data_dev = '{}', qnt_diarias_iniciais = '{}', mod_vei = '{}', nome_cnss = '{}', tipo_retirada = '{}',   Qtd_dias_totais = '{}', status_reserva = '{}'  WHERE id_reserva_sql = {}".format(N_Solicitacao,Solicitante,Assistencia,CPF_Condutor,Nome_Condutor,Chassi,Locadora,N_Reserva,Categoria,Data_Retirada,Data_Devolucao,Qnt_diarias_iniciais,Modelo_Veiculo,Concessionaria,status_reserva,Qtd_diarias_totais,Tipo_retirada,str(valor_id)))
        cursor.execute(comandoSQL_6)
        banco.commit()
        print("Updated",cursor.rowcount,"row(s) of data.")
        QMessageBox.warning(QMessageBox(), "Muito Bom", "Atualizado com sucesso")
        cursor.close()
        banco.close()

def closeEvent():
    connectar()
    cursor = banco.cursor()
    aba_atualiza.lineEdit.setText("")
    aba_atualiza.lineEdit_4.setText("")
    aba_atualiza.lineEdit_5.setText("")
    aba_atualiza.lineEdit_6.setText("")
    aba_atualiza.lineEdit_7.setText("")
    aba_atualiza.lineEdit_8.setText("")
    aba_atualiza.lineEdit_9.setText("")
    aba_atualiza.lineEdit_10.setText("")
    aba_atualiza.lineEdit_11.setText("")
    aba_atualiza.lineEdit_12.setText("")
    aba_atualiza.lineEdit_13.setText("")
    aba_atualiza.lineEdit_14.setText("")
    aba_atualiza.lineEdit_15.setText("")
    aba_atualiza.lineEdit_16.setText("")
    aba_atualiza.lineEdit_17.setText("")
    aba_atualiza.lineEdit_18.setText("")
    aba_atualiza.lineEdit_19.setText("")
    aba_atualiza.lineEdit_20.setText("")
    aba_atualiza.close()
    cursor.close() 
    banco.close()

def mostrar_todas_reservas():
    acompanhamento_reserva.lineEdit.setText("")
    chama_aba_acompanhamento()

def botaocancelar():
    acompanhamento_reserva.close()

import sys 

app = QtWidgets.QApplication([])
Form = QtWidgets.QWidget()
formulario=uic.loadUi("aba_cadastro.ui")
acompanhamento_reserva=uic.loadUi("aba_acompanhamento_reserva.ui")
aba_atualiza=uic.loadUi("aba_atualizar.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(chama_aba_acompanhamento)
aba_atualiza.pushButton.clicked.connect(pesquisa_id_aba_atualizar)
aba_atualiza.pushButton_2.clicked.connect(atualizar_reserva)
aba_atualiza.pushButton_3.clicked.connect(closeEvent)
acompanhamento_reserva.pushButton_6.clicked.connect(mostrar_todas_reservas)
acompanhamento_reserva.pushButton.clicked.connect(pesquisa_id)
acompanhamento_reserva.pushButton_7.clicked.connect(mostrar_dados)
acompanhamento_reserva.pushButton_3.clicked.connect(botaocancelar)
aba_atualiza.tableWidget.itemSelectionChanged.connect(Preencher_campos_auto)

formulario.show()
app.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


