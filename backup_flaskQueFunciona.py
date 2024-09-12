from flask import Flask, render_template, request, redirect, url_for, send_file, jsonify
from conectar_banco import ConectarBanco #novo
import psycopg2
from psycopg2 import sql
from motorista import (
    criar_motorista,
    buscar_motorista_por_nome,
    buscar_foto_motorista,
    editar_motorista,
    excluir_motorista,
    buscar_dados_motorista
)

from io import BytesIO
from Linha import (pesquisar_linha_metropolitana,
 pesquisar_linha_Interestadual,
 criar_linha,
 excluir_linha, 
 alterar_linha
 
 )

import Trajeto

from Paineis_Gerais import busca_Painel_metropolitano, busca_Linhas_Atuais

app = Flask(__name__)
########################################MOTORISTA###############################################
################################################################################################
@app.route('/upload')
def motorista():
    return render_template('upload.html') #http://127.0.0.1:5000/upload

@app.route('/motorista', methods=['POST'])
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
        
        return redirect(url_for('motorista'))  # Atualizado para 'motorista'
    return 'Falha no upload', 500

@app.route('/search', methods=['GET'])
def search_motorista():
    nome = request.args.get('name')
    if not nome:
        return 'Nome não fornecido', 400
    
    motorista = buscar_motorista_por_nome(nome)
    if motorista:
        return render_template('result.html', motorista=motorista)
    else:
        return 'Motorista não encontrado', 404

@app.route('/foto/<int:motorista_id>')
def foto(motorista_id):
    foto = buscar_foto_motorista(motorista_id)
    if foto:
        return send_file(BytesIO(foto[0]), mimetype='image/jpeg')
    else:
        return 'Foto não encontrada', 404
    
@app.route('/edit/<int:motorista_id>', methods=['GET', 'POST'])
def edit_motorista(motorista_id):
    if request.method == 'POST':
        nome = request.form['name']
        telefone = request.form['phone']
        linha_id = request.form['linha_id']
        empresa_id = request.form['empresa_id']

        # Verifica se uma nova foto foi enviada
        if 'foto' in request.files and request.files['foto'].filename != '':
            foto = request.files['foto'].read()
        else:
            foto = None

        editar_motorista(motorista_id, nome, telefone, linha_id, empresa_id, foto)
        return redirect(url_for('search_motorista', name=nome))
    else:
        motorista = buscar_dados_motorista(motorista_id)
        if motorista:
            return render_template('edit.html', motorista=motorista, motorista_id=motorista_id)
        else:
            return 'Motorista não encontrado', 404

@app.route('/delete/<int:motorista_id>', methods=['POST'])
def delete_motorista(motorista_id):
    excluir_motorista(motorista_id)
    return redirect(url_for('motorista'))  # Atualizado para 'motorista'

###TELA USUÁRIO ####
@app.route('/tela1_usuario')
def index(): #Pode ter lugares que vão chamar essa função index
    return render_template('tela1_usuario.html') #http://127.0.0.1:5000/tela1_usuario


#############################ESSE AQUI NÃO ESTÁ SENDO USADO NO MOMENTO POIS TEM PARADAS ####################################
@app.route('/usuario_buscaLinha', methods=['GET', 'POST']) #http://127.0.0.1:5000/usuario_buscaLinha METROPOLITANA
def usuario_busca_linha():
    linha = None
    mensagem = None
   
    if request.method == 'POST':
        nome_linha = request.form.get('linha_numero')
       
        # Verifica se o campo da linha não está vazio
        if nome_linha:
            linha = pesquisar_linha_metropolitana(nome_linha)
            if not linha or not any(linha):  # Se não encontrar resultados ou a lista estiver vazia
                mensagem = "Nenhuma linha encontrada para o número fornecido."
        else:
            mensagem = "Por favor, insira um número de linha válido."
 
    return render_template('tela1_usuario.html', linha=linha, mensagem=mensagem)
########################################################################################################

###################################ESSE ESTÁ SENDO USADO NO TELA1, POIS NÃO TEM PARADAS##################
# Rota para processar a pesquisa de linhas interestaduais
@app.route('/usuario_buscaLinhaInterestadual', methods=['POST'])
def usuario_buscaLinhaInterestadual():
    nome_linha = request.form['linha_numero']
    resultado = pesquisar_linha_Interestadual(nome_linha)

    if resultado:
        return render_template('tela1_usuario.html', linha=resultado)
    else:
        mensagem = "Nenhuma linha encontrada com o número fornecido."
        return render_template('tela1_usuario.html', mensagem=mensagem)

#############################################################################
@app.route('/excluir_linha', methods=['POST'])
def excluir_linha_route():
    data = request.get_json()
    nome = data.get('nome')

    if nome:
        resultado = excluir_linha(nome)
        if resultado:
            return jsonify({"message": "Linha excluída com sucesso!"}), 200
        else:
            return jsonify({"message": "Nenhuma linha encontrada com esse nome."}), 404
    else:
        return jsonify({"message": "Nome não fornecido."}), 400

@app.route('/excluir_linha_page')
def excluir_linha_page():
    return render_template('excluir_linha.html')


@app.route('/alterar_linha', methods=['POST'])
def alterar_linha_route():
    data = request.get_json()
    
    nome = data.get('nome')
    modelo = data.get('modelo')
    origem_id = data.get('origem_id')
    destino_id = data.get('destino_id')
    parada_1 = data.get('parada_1')
    parada_2 = data.get('parada_2')
    parada_3 = data.get('parada_3')
    parada_4 = data.get('parada_4')
    parada_5 = data.get('parada_5')
    horario_1 = data.get('horario_1')
    horario_2 = data.get('horario_2')
    horario_3 = data.get('horario_3')
    horario_4 = data.get('horario_4')
    horario_5 = data.get('horario_5')

    if nome:
        try:
            alterar_linha(
                nome=nome,
                modelo=modelo,
                origem_id=origem_id,
                destino_id=destino_id,
                parada_1=parada_1,
                parada_2=parada_2,
                parada_3=parada_3,
                parada_4=parada_4,
                parada_5=parada_5,
                horario_1=horario_1,
                horario_2=horario_2,
                horario_3=horario_3,
                horario_4=horario_4,
                horario_5=horario_5
            )
            return jsonify({"message": "Linha atualizada com sucesso!"}), 200
        except Exception as e:
            return jsonify({"message": f"Erro ao atualizar linha: {e}"}), 500
    else:
        return jsonify({"message": "Nome não fornecido."}), 400


@app.route('/alterar_linha_page')
def alterar_linha_page():
    return render_template('alterar_linha.html')


    
###############Kethlen aqui
@app.route('/tela_Loga_Admin') #adicionei essa rota aqui para o botao area do administrador ser ligado a tela de login do adm 
def login_admin():
    return render_template('tela_Loga_Admin.html')  # Renderiza a tela de login do administrador


#Faz o login do adm
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
            return redirect(url_for('tela3_inicio_adm')) #aqui o adm entra na tela de pesquisa de linha dele
            #return redirect(url_for('bem_vindo_adm ')) #bem_vindo_adm tava assim antes
        else:
            return "Credenciais inválidas"
    
    return render_template('tela_Loga_Admin.html') #chama a página para o flask 
'''
#Não apagar 
@app.route('/tela3_inicio_adm')
def tela3_inicio_adm ():
    return render_template('tela3_inicio_adm.html')
'''

@app.route('/tela3_inicio_adm')
def tela3_inicio_adm():
    #Chama a função que busca as linhas atuais
    resultados = busca_Linhas_Atuais()
    
    # Passa os resultados para o template
    return render_template('tela3_inicio_adm.html', resultados=resultados)

#### CRIAR LINHA BIANCA ## 
@app.route('/criar_linha', methods=['GET', 'POST'])
def criar_linha_view():
    if request.method == 'POST':
        nome = request.form['nome']
        modelo = request.form['modelo']
        empresa_id = request.form['empresa_id']
        garagem_id = request.form['garagem_id']
        origem_id = request.form['origem_id']
        destino_id = request.form['destino_id']
        parada_1 = request.form['parada_1']
        parada_2 = request.form['parada_2']
        parada_3 = request.form['parada_3']
        parada_4 = request.form['parada_4']
        parada_5 = request.form['parada_5']
        horario_1 = request.form['horario_1']
        horario_2 = request.form['horario_2']
        horario_3 = request.form['horario_3']
        horario_4 = request.form['horario_4']
        horario_5 = request.form['horario_5']
        
        try:
            criar_linha(nome, modelo, empresa_id, garagem_id, origem_id, destino_id, 
                        parada_1, parada_2, parada_3, parada_4, parada_5, horario_1, horario_2, horario_3, horario_4, horario_5)
            mensagem = 'Linha criada com sucesso!'
        except Exception as e:
            mensagem = f'Erro ao criar linha: {e}'
        
        return render_template('tela4_linha.html', mensagem=mensagem)

    return render_template('tela4_linha.html')

########################################## PAINEIS ######################################################### 
############################################################################################################

@app.route('/painel_metropolitano')
def painel_metropolitano():
    resultados = busca_Painel_metropolitano()
    return render_template('painel_metropolitano.html', resultados=resultados)



############################################################################################################
#######################################TESTANDO O NOVO CRUD DE TRAJETO######################################
@app.route('/tela_trajeto')
def tela_trajeto():
    return render_template('tela_trajeto.html')

@app.route('/criar', methods=['POST'])
def criar():
    linha_id = request.form.get('linha_id')
    origem_id = request.form.get('origem_id')
    destino_id = request.form.get('destino_id')
    Trajeto.criar_trajeto(linha_id, origem_id, destino_id)
    return redirect(url_for('tela_trajeto'))

@app.route('/pesquisar', methods=['POST'])
def pesquisar():
    linha_id = request.form.get('linha_id')
    resultados = Trajeto.pesquisar_trajeto(linha_id)
    return render_template('tela_trajeto.html', resultados=resultados)

@app.route('/excluir/<linha_id>')
def excluir(linha_id):
    Trajeto.excluir_trajeto(linha_id)
    return redirect(url_for('tela_trajeto'))

@app.route('/atualizar', methods=['POST'])
def atualizar():
    linha_id = request.form.get('linha_id')
    origem_id = request.form.get('origem_id')
    destino_id = request.form.get('destino_id')
    Trajeto.atualizar_trajeto(linha_id, origem_id, destino_id)
    return redirect(url_for('tela_trajeto'))




###########################################################################################################
##########################################################################################################



if __name__ == '__main__':
    app.run(debug=True)
