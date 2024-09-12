# conectar_banco.py
#Função para conectar ao banco de dados verifque se seu banco de dados tem o user, host, porta e password igual para funcionar em seu computador
import psycopg2

def ConectarBanco():
    """
    Estabelece uma conexão com o banco de dados PostgreSQL.
    """
    try:
        conexao = psycopg2.connect(dbname="Sistema onibus",
                                   host="localhost",
                                   user="postgres",
                                   password="#Gabriel19",
                                   port="5432")
        print("Conexão estabelecida com sucesso.")
        return conexao
    except psycopg2.OperationalError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Testando a conexão
if __name__ == "__main__":
    ConectarBanco()
