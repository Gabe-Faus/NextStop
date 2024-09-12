#FlaskMotorista
from flask import Flask, render_template, request, redirect, url_for, send_file
import psycopg2
from psycopg2 import sql
from conectar_banco import ConectarBanco
from io import BytesIO

app = Flask(__name__)
# Função Criar Motorista
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

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'Nenhum arquivo selecionado', 400
    
    file = request.files['file']
    
    if file.filename == '':
        return 'Nenhum arquivo selecionado', 400
    
    if file:
        image_data = file.read()
        nome = request.form['name']
        telefone = request.form['phone']
        linha_id = request.form['linha_id']
        empresa_id = request.form['empresa_id']
        
        criar_motorista(nome, telefone, image_data, linha_id, empresa_id)
        
        return redirect(url_for('index'))
    return 'Falha no upload', 500

@app.route('/search', methods=['GET'])
def search_motorista():
    nome = request.args.get('name')
    if not nome:
        return 'Nome não fornecido', 400
    
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            query = sql.SQL("""
                SELECT Motorista_id, Nome, Telefone FROM Motorista WHERE Nome = %s
            """)
            cur.execute(query, (nome,))
            motorista = cur.fetchone()
            if motorista:
                return render_template('result.html', motorista=motorista)
            else:
                return 'Motorista não encontrado', 404
    except Exception as e:
        print(f"Erro ao pesquisar motorista: {e}")
        return 'Erro na pesquisa', 500
    finally:
        conn.close()

@app.route('/foto/<int:motorista_id>')
def foto(motorista_id):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            query = sql.SQL("""
                SELECT Foto FROM Motorista WHERE Motorista_id = %s
            """)
            cur.execute(query, (motorista_id,))
            foto = cur.fetchone()
            if foto:
                return send_file(BytesIO(foto[0]), mimetype='image/jpeg')
            else:
                return 'Foto não encontrada', 404
    except Exception as e:
        print(f"Erro ao recuperar foto: {e}")
        return 'Erro na recuperação da foto', 500
    finally:
        conn.close()

###Novo Editar e excluir 
@app.route('/edit/<int:motorista_id>', methods=['GET', 'POST'])
def edit_motorista(motorista_id):
    conn = ConectarBanco()
    try:
        if request.method == 'POST':
            nome = request.form['name']
            telefone = request.form['phone']
            linha_id = request.form['linha_id']
            empresa_id = request.form['empresa_id']
            
            with conn.cursor() as cur:
                query = sql.SQL("""
                    UPDATE Motorista
                    SET Nome = %s, Telefone = %s, Linha_id = %s, Empresa_id = %s
                    WHERE Motorista_id = %s
                """)
                cur.execute(query, (nome, telefone, linha_id, empresa_id, motorista_id))
                conn.commit()
                return redirect(url_for('search_motorista', name=nome))
        
        else:
            with conn.cursor() as cur:
                query = sql.SQL("""
                    SELECT Nome, Telefone, Linha_id, Empresa_id FROM Motorista WHERE Motorista_id = %s
                """)
                cur.execute(query, (motorista_id,))
                motorista = cur.fetchone()
                if motorista:
                    return render_template('edit.html', motorista=motorista, motorista_id=motorista_id)
                else:
                    return 'Motorista não encontrado', 404
    except Exception as e:
        print(f"Erro ao editar motorista: {e}")
        return 'Erro na edição', 500
    finally:
        conn.close()

@app.route('/delete/<int:motorista_id>', methods=['POST'])
def delete_motorista(motorista_id):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            query = sql.SQL("DELETE FROM Motorista WHERE Motorista_id = %s")
            cur.execute(query, (motorista_id,))
            conn.commit()
            return redirect(url_for('index'))
    except Exception as e:
        print(f"Erro ao excluir motorista: {e}")
        return 'Erro na exclusão', 500
    finally:
        conn.close()


#####
if __name__ == '__main__':
    app.run(debug=True)