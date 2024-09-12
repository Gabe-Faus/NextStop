# Trajeto.py

from psycopg2 import sql
import psycopg2
from conectar_banco import ConectarBanco


#Função para aceitar valores NUll
def tratar_input(valor):
    return None if valor.upper() == 'NULL' else valor

#Função para criar Trajeto
def criar_trajeto(linha_id, origem_id, destino_id):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            query_create = sql.SQL("""
                INSERT INTO Trajeto (linha_id, origem_id, destino_id)
                VALUES (%s, %s, %s);
            """)
            cur.execute(query_create, (linha_id, origem_id, destino_id))

            # Confirma todas as inserções
            conn.commit()

            return("Trajeto criado com sucesso!") #

    except Exception as e:
        print(f"Erro ao criar Trajeto: {e}")
    finally:
        conn.close()

#Função para pesquisar Trajeto
def pesquisar_trajeto(linha_id):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:

            query_read = sql.SQL("""
                SELECT * FROM Trajeto
                WHERE linha_id = %s;
            """)

            # Executando a consulta
            cur.execute(query_read, (linha_id,))
            resultados = cur.fetchall()
                
            # Exibindo os resultados
            if resultados:
                return(resultados)     #
    
    except Exception as e:
        print(f"Erro ao pesquisar Trajeto: {e}")
    
    finally:
        conn.close()

#Função exclui Trajeto
def excluir_trajeto(linha_id):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            query_delete = sql.SQL("""
                DELETE FROM Trajeto
                WHERE linha_id = %s
            """)
            cur.execute(query_delete, (linha_id,))
            conn.commit()
            if cur.rowcount > 0:
                print(f"Trajeto de nome '{nome}' excluída com sucesso!")
            else:
                print(f"Nenhum Trajeto de nome '{nome}' foi encontrada.")
    except Exception as e:
        print(f"Erro ao excluir Trajeto: {e}")
    finally:
        conn.close()

#Função atualiza Trajeto
def atualizar_trajeto(linha_id, origem_id, destino_id):
    conn = ConectarBanco() 
    try:
        with conn.cursor() as cur:
            query_update = """
                UPDATE Trajeto
                SET origem_id = %s, destino_id = %s
                WHERE linha_id = %s;
            """
            cur.execute(query_update, (linha_id, origem_id, destino_id))

            # Confirma todas as atualizações
            conn.commit()

            return("Trajeto atualizado com sucesso!") # print("Trajeto atualizado com sucesso!")

    except Exception as e:
        print(f"Erro ao atualizar o Trajeto: {e}")
    finally:
        conn.close()