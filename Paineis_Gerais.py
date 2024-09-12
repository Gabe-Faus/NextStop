#Função Painel Geral

from psycopg2 import sql
import psycopg2
from conectar_banco import ConectarBanco


def busca_Painel_metropolitano():
    conn = ConectarBanco()

    try:
        with conn.cursor() as cur:
            lista = []
            query_read = sql.SQL("""
                SELECT * FROM Painel_Geral_Metropolitano;
            """)

            # Executando a consulta
            cur.execute(query_read)
            resultados = cur.fetchall()
            lista.append(resultados)
                
            # Retornando os resultados
            if lista:
                return(lista) 
            else:
                return []
    
    except Exception as e:
        print(f"Erro ao mostrar Painel Geral Metropolitano: {e}")
    
    finally:
        conn.close()


def busca_Painel_interestadual():
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            query_read = sql.SQL("""
                SELECT * FROM Painel_Geral_Interestadual;
            """)

            # Executando a consulta
            cur.execute(query_read)
            resultados = cur.fetchall()
                
            # Retornando os resultados
            if resultados:
                print(resultados) 
            else:
                return []
    
    except Exception as e:
        print(f"Erro ao mostrar Painel Geral Interestadual: {e}")
    
    finally:
        conn.close()


def busca_Linhas_Atuais():
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            lista = []
            query_read = sql.SQL("""
                SELECT * FROM Linhasatuais();
            """)

            # Executando a consulta
            cur.execute(query_read)
            resultados = cur.fetchall()
            lista.append(resultados)
                
            # Retornando os resultados
            if lista:
                return(lista) 
            else:
                return []
    
    except Exception as e:
        print(f"Erro ao mostrar Painel Geral Metropolitano: {e}")
    
    finally:
        conn.close()


busca_Linhas_Atuais();