from sqlalchemy import create_engine
import pymysql

import mysql.connector
from mysql.connector import Error

def connectar():
        global banco 
        banco = mysql.connector.connect(
           host= '35.237.99.182',
           user='dinahdoria',
           passwd='teste123',
           database='centralloc')


connectar()
cursor = banco.cursor()
criar_tabelas = """ 
    CREATE TABLE reserva_acompanhamento (
    id_reserva_sql INT(12) NOT NULL AUTO_INCREMENT,
    nmr_solicitacao_dynamics INT(12),
    nome_solicitante VARCHAR(30),
    assistencia_id_juvo INT(100),
    cpf_condutor VARCHAR(16),
    nome_condutor VARCHAR(80),
    chassi_veiculo_condutor VARCHAR(30),
    nome_locadora VARCHAR(60),
    nmr_resv_juvo VARCHAR(60),
    categoria_solicitada VARCHAR(5),
    data_ret VARCHAR(10),
    data_dev VARCHAR(10),
    qnt_diarias_iniciais INT(4),
    mod_vei VARCHAR(30),
    nome_cnss VARCHAR(30),
    tipo_retirada VARCHAR(40),
    Qtd_dias_totais INT(12),
    status_reserva VARCHAR(30),
    PRIMARY KEY(id_reserva_sql)
)"""
cursor.execute(criar_tabelas)
banco.commit()

# AO EXECUTAR É CRIADO NO BANCO DE DADOS DA GOOGLE CLOUD UMA TABELA COM TODOS AS COLUNAS PARA QUE O PROGRAMA SEJA EXECUTADO APARTIR DISTO