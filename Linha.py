#Linha.py

from psycopg2 import sql
import psycopg2
from conectar_banco import ConectarBanco


#Função para aceitar valores NUll
def tratar_input(valor):
    return None if valor.upper() == 'NULL' else valor

#Função Criar Linha
def criar_linha(nome, modelo, empresa_id, garagem_id, origem_id, destino_id, 
                parada_1, parada_2, parada_3, parada_4, parada_5, horario_1, horario_2, horario_3, horario_4, horario_5):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
             # Inserir na tabela Linha
            query_linha = sql.SQL("""
                INSERT INTO Linha (nome, modelo, empresa_id, garagem_id)
                VALUES (%s, %s, %s, %s);
            """)
            cur.execute(query_linha, (nome, modelo, empresa_id, garagem_id))

            # Inserir na tabela Trajeto
            query_trajeto = sql.SQL("""
                INSERT INTO Trajeto (linha_id, origem_id, destino_id)
                VALUES (%s, %s, %s);
            """)
            cur.execute(query_trajeto, (nome, origem_id, destino_id))

            # Inserir na tabela Trajeto_Parada
            query_paradas = sql.SQL("""
                INSERT INTO Trajeto_Parada (linha_id, parada_1, parada_2, parada_3, parada_4, parada_5)
                VALUES (%s, %s, %s, %s, %s, %s);
            """)
            cur.execute(query_paradas, (nome, parada_1, parada_2, parada_3, parada_4, parada_5))

            # Inserir na tabela Horario_Linha
            query_horarios = sql.SQL("""
                INSERT INTO Horario_Linha (linha_id, horario_1, horario_2, horario_3, horario_4, horario_5)
                VALUES (%s, %s, %s, %s, %s, %s);
            """)
            cur.execute(query_horarios, (nome, horario_1, horario_2, horario_3, horario_4, horario_5))

            # Confirma todas as inserções
            conn.commit()

            print("Linha criada com sucesso!")

    except Exception as e:
        print(f"Erro ao criar linha: {e}")
    finally:
        conn.close()

#Função Excluir Linha 
def excluir_linha(nome):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            query = sql.SQL("""
                DELETE FROM Linha
                WHERE Nome = %s
            """)
            cur.execute(query, (nome,))
            conn.commit()
            if cur.rowcount > 0:
                return True
            else:
                return False
    except Exception as e:
        print(f"Erro ao excluir Linha: {e}")
    finally:
        conn.close()


def pesquisar_linha_metropolitana(nome):
    conn = ConectarBanco()
    lista = []
    try:
        with conn.cursor() as cur:
            # Loop para pesquisar nos 5 horários
            for i in range(5):
                horario = f'horario_{i+1}'
                # Construção correta da query SQL
                query = sql.SQL(f"""
                    SELECT Horario_Linha.Linha_id, modelo, Duracao, Dia_semana, origem_id, destino_id, Parada_1, Parada_2, Parada_3, Parada_4, Parada_5
                    FROM HORARIO_LINHA
                    INNER JOIN Horario ON {horario} = horario_id
                    INNER JOIN Linha ON Horario_Linha.linha_id = Linha.nome
                    INNER JOIN Trajeto ON Trajeto.linha_id = Linha.nome
                    INNER JOIN Trajeto_Parada ON Trajeto.Linha_id = Trajeto_Parada.Linha_id
                    WHERE Horario_Linha.linha_id = %s;
                """)


                # Executando a consulta
                cur.execute(query, (nome,))
                resultados = cur.fetchall()
                lista.append(resultados)
                
            # Exibindo os resultados
            if lista:
                return(lista)
                
    
    except Exception as e:
        print(f"Erro ao pesquisar linha: {e}")
    
    finally:
        conn.close()

'''
#Função Pesquizar Linha Interestadual
#FUNÇÃO COM JOIN
def pesquisar_linha_Interestadual(nome):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            # Loop para pesquisar nos 5 horários
            for i in range(5):
                horario = f'horario_{i+1}'
                # Construção correta da query SQL
                query = sql.SQL(f"""
                    SELECT Horario_Linha.Linha_id, modelo, Duracao, Dia_semana, origem_id, destino_id 
                    FROM HORARIO_LINHA 
                    INNER JOIN Horario ON {horario} = horario_id
                    INNER JOIN Linha ON Horario_Linha.linha_id = Linha.nome 
                    INNER JOIN Trajeto ON Trajeto.linha_id = Linha.nome
                    WHERE Horario_Linha.linha_id = %s;
                """)

                # Executando a consulta
                cur.execute(query, (nome,))
                resultados = cur.fetchall()
                print(resultados)
                
                # Exibindo os resultados
                if resultados:
                    print (resultados)
                
                
    
    except Exception as e:
        print(f"Erro ao pesquisar linha: {e}")
    
    finally:
        conn.close()
'''

##############################testando novo #####################
def pesquisar_linha_Interestadual(nome):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            lista = []
            # Loop para pesquisar nos 5 horários
            for i in range(5):
                horario = f'horario_{i+1}'
                # Construção correta da query SQL
                query = sql.SQL(f"""
                    SELECT Horario_Linha.Linha_id, modelo, Duracao, Dia_semana, origem_id, destino_id 
                    FROM HORARIO_LINHA 
                    INNER JOIN Horario ON {horario} = horario_id
                    INNER JOIN Linha ON Horario_Linha.linha_id = Linha.nome 
                    INNER JOIN Trajeto ON Trajeto.linha_id = Linha.nome
                    WHERE Horario_Linha.linha_id = %s;
                """)

                # Executando a consulta
                cur.execute(query, (nome,))
                resultados = cur.fetchall()
                lista.append(resultados)
            
                
            # Exibindo os resultados
            if lista != [[], [], [], [], []]:
                return(lista)
            else:
                lista_1 = []
                # Loop para pesquisar nos 5 horários
                for i in range(5):
                    horario = f'horario_{i+1}'
                    # Construção correta da query SQL
                    query = sql.SQL(f"""
                        SELECT Horario_Linha.Linha_id, modelo, Duracao, Dia_semana
                    FROM HORARIO_LINHA
                    INNER JOIN Horario ON horario_1 = horario_id
                    INNER JOIN Linha ON Horario_Linha.linha_id = Linha.nome
                    WHERE Horario_Linha.linha_id = %s;
                    """)

                    # Executando a consulta
                    cur.execute(query, (nome,))
                    resultados = cur.fetchall()
                    lista_1.append(resultados)

                if lista_1 != [[], [], [], [], []]:
                    return(lista_1)
                else:
                    lista_1 = [[["Linha Não existe"]], [["Linha Não existe"]], [["Linha Não existe"]], [["Linha Não existe"]], [["Linha Não existe"]]]
                    return(lista_1)
                
                
                
    
    except Exception as e:
        return(f"Erro ao pesquisar linha: {e}")
    
    finally:
        conn.close()

###################################################

#Função Atualizar Linha
def alterar_linha(nome, modelo=None, origem_id=None, destino_id=None, 
                  parada_1=None, parada_2=None, parada_3=None, parada_4=None, parada_5=None, 
                  horario_1=None, horario_2=None, horario_3=None, horario_4=None, horario_5=None):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            # Atualizar a tabela Linha
            campos_atualizacao_linha = []
            valores_linha = []

            if modelo is not None:
                campos_atualizacao_linha.append("Modelo = %s")
                valores_linha.append(modelo)

            if campos_atualizacao_linha:
                query_linha = sql.SQL("""
                    UPDATE Linha
                    SET {}
                    WHERE nome = %s
                """).format(sql.SQL(', ').join(sql.SQL(campo) for campo in campos_atualizacao_linha))

                valores_linha.append(nome)
                cur.execute(query_linha, tuple(valores_linha))
                conn.commit()
                print("Linha atualizada com sucesso!")

            # Atualizar a tabela Trajeto
            campos_atualizacao_trajeto = []
            valores_trajeto = []

            if origem_id is not None:
                campos_atualizacao_trajeto.append("Origem_id = %s")
                valores_trajeto.append(origem_id)
            if destino_id is not None:
                campos_atualizacao_trajeto.append("Destino_id = %s")
                valores_trajeto.append(destino_id)

            if campos_atualizacao_trajeto:
                query_trajeto = sql.SQL("""
                    UPDATE Trajeto
                    SET {}
                    WHERE linha_id = %s
                """).format(sql.SQL(', ').join(sql.SQL(campo) for campo in campos_atualizacao_trajeto))

                valores_trajeto.append(nome)
                cur.execute(query_trajeto, tuple(valores_trajeto))
                conn.commit()
                print("Trajeto atualizado com sucesso!")

            # Atualizar a tabela Trajeto_Parada
            campos_atualizacao_paradas = []
            valores_paradas = []

            if parada_1 is not None:
                campos_atualizacao_paradas.append("Parada_1 = %s")
                valores_paradas.append(parada_1)
            if parada_2 is not None:
                campos_atualizacao_paradas.append("Parada_2 = %s")
                valores_paradas.append(parada_2)
            if parada_3 is not None:
                campos_atualizacao_paradas.append("Parada_3 = %s")
                valores_paradas.append(parada_3)
            if parada_4 is not None:
                campos_atualizacao_paradas.append("Parada_4 = %s")
                valores_paradas.append(parada_4)
            if parada_5 is not None:
                campos_atualizacao_paradas.append("Parada_5 = %s")
                valores_paradas.append(parada_5)

            if campos_atualizacao_paradas:
                query_paradas = sql.SQL("""
                    UPDATE Trajeto_Parada
                    SET {}
                    WHERE linha_id = %s
                """).format(sql.SQL(', ').join(sql.SQL(campo) for campo in campos_atualizacao_paradas))

                valores_paradas.append(nome)
                cur.execute(query_paradas, tuple(valores_paradas))
                conn.commit()
                print("Paradas do trajeto atualizadas com sucesso!")

            # Atualizar a tabela Horario_Linha
            campos_atualizacao_horarios = []
            valores_horarios = []

            if horario_1 is not None:
                campos_atualizacao_horarios.append("Horario_1 = %s")
                valores_horarios.append(horario_1)
            if horario_2 is not None:
                campos_atualizacao_horarios.append("Horario_2 = %s")
                valores_horarios.append(horario_2)
            if horario_3 is not None:
                campos_atualizacao_horarios.append("Horario_3 = %s")
                valores_horarios.append(horario_3)
            if horario_4 is not None:
                campos_atualizacao_horarios.append("Horario_4 = %s")
                valores_horarios.append(horario_4)
            if horario_5 is not None:
                campos_atualizacao_horarios.append("Horario_5 = %s")
                valores_horarios.append(horario_5)

            if campos_atualizacao_horarios:
                query_horarios = sql.SQL("""
                    UPDATE Horario_Linha
                    SET {}
                    WHERE linha_id = %s
                """).format(sql.SQL(', ').join(sql.SQL(campo) for campo in campos_atualizacao_horarios))

                valores_horarios.append(nome)
                cur.execute(query_horarios, tuple(valores_horarios))
                conn.commit()
                print("Horários atualizados com sucesso!")
    
    except Exception as e:
        print(f"Erro ao atualizar linha: {e}")
    finally:
        conn.close()

