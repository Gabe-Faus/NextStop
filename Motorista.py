import psycopg2
from psycopg2 import sql
from conectar_banco import ConectarBanco
from io import BytesIO


def criar_motorista(nome, telefone, foto, linha_id, empresa_id):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            query = sql.SQL("""
                INSERT INTO Motorista (Nome, Telefone, Foto, Linha_id, Empresa_id)
                VALUES (%s, %s, %s, %s, %s)
            """)
            cur.execute(query, (nome, telefone, psycopg2.Binary(foto), linha_id, empresa_id))
            conn.commit()
            print("Motorista criado com sucesso!")
    except Exception as e:
        print(f"Erro ao criar motorista: {e}")
    finally:
        conn.close()



def buscar_motorista_por_nome(nome):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            query = sql.SQL("""
                SELECT Motorista_id, Nome, Telefone FROM Motorista WHERE Nome = %s
            """)
            cur.execute(query, (nome,))
            return cur.fetchone()
    except Exception as e:
        print(f"Erro ao pesquisar motorista: {e}")
        return None
    finally:
        conn.close()

def buscar_foto_motorista(motorista_id):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            query = sql.SQL("""
                SELECT Foto FROM Motorista WHERE Motorista_id = %s
            """)
            cur.execute(query, (motorista_id,))
            return cur.fetchone()
    except Exception as e:
        print(f"Erro ao recuperar foto: {e}")
        return None
    finally:
        conn.close()

################################TESTE TESTE TESTE ################################################
def editar_motorista(motorista_id, nome, telefone, linha_id, empresa_id, foto=None):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            if foto:
                query = sql.SQL("""
                    UPDATE Motorista
                    SET Nome = %s, Telefone = %s, Linha_id = %s, Empresa_id = %s, Foto = %s
                    WHERE Motorista_id = %s
                """)
                cur.execute(query, (nome, telefone, linha_id, empresa_id, foto, motorista_id))
            else:
                query = sql.SQL("""
                    UPDATE Motorista
                    SET Nome = %s, Telefone = %s, Linha_id = %s, Empresa_id = %s
                    WHERE Motorista_id = %s
                """)
                cur.execute(query, (nome, telefone, linha_id, empresa_id, motorista_id))
            
            conn.commit()
    except Exception as e:
        print(f"Erro ao editar motorista: {e}")
    finally:
        conn.close()

###################################################################################################

def excluir_motorista(motorista_id):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            query = sql.SQL("DELETE FROM Motorista WHERE Motorista_id = %s")
            cur.execute(query, (motorista_id,))
            conn.commit()
    except Exception as e:
        print(f"Erro ao excluir motorista: {e}")
    finally:
        conn.close()

def buscar_dados_motorista(motorista_id):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            query = sql.SQL("""
                SELECT Nome, Telefone, Linha_id, Empresa_id FROM Motorista WHERE Motorista_id = %s
            """)
            cur.execute(query, (motorista_id,))
            return cur.fetchone()
    except Exception as e:
        print(f"Erro ao buscar dados do motorista: {e}")
        return None
    finally:
        conn.close()
