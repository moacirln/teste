import streamlit as st
import sqlite3
import sys
import os
import pandas as pd

def connect_BD():
    executable_path = sys.executable
    base_path = os.path.dirname(executable_path)
    db_path = os.path.join(base_path, 'banco_dados.db')
    banco = sqlite3.connect(db_path)
    return banco

def criar_teste():
    banco = connect_BD()
    sql = '''CREATE TABLE reg (usuario VARCHAR (100), tipo VARCHAR (50), Data_Hora TIMESTAMP, comentario VARCHAR (300))'''
    cursor = banco.cursor()
    cursor.execute(sql)
    banco.commit()
    banco.close()

def return_teste():
    banco = connect_BD()
    sql = '''SELECT * FROM reg'''
    df = pd.read_sql_query(sql, banco)
    banco.close()
    return df

df = return_teste()

def main():
    #Configuração página inicial
    st.set_page_config(page_title='Dashboard', layout= 'wide', initial_sidebar_state='collapsed')

    st.dataframe(df)



if __name__ == '__main__':
    main()
