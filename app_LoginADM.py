from flask import Flask, render_template, request, redirect, url_for
import psycopg2
from psycopg2 import sql
from conectar_banco import ConectarBanco

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form['usuario']
        senha = request.form['senha']
        
        # Conectar ao banco de dados
        conn = ConectarBanco()
        cur = conn.cursor()
        
        # Verificar as credenciais
        query = sql.SQL("SELECT * FROM Administrador WHERE Nome = %s AND Senha = %s")
        cur.execute(query, (nome, senha))
        admin = cur.fetchone()
        
        cur.close()
        conn.close()
        
        if admin:
            return redirect(url_for('tela3_inicio_adm'))
            #return redirect(url_for('bem_vindo_adm ')) #bem_vindo_adm tava assim antes
        else:
            return "Credenciais inválidas"
    
    return render_template('tela_Loga_Admin.html') #chama a página para o flask 


@app.route('/tela3_inicio_adm')
def tela3_inicio_adm ():
    return render_template('tela3_inicio_adm.html')  #está indo para essa tela temporáriamente até criar a tela bem vindo 
'''
@app.route('/bem_vindo_adm')
def bem_vindo_adm():
    return "Bem-vindo à área do administrador!"
'''


if __name__ == '__main__':
    app.run(debug=True)
