from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clientes.db'
db = SQLAlchemy(app)

class Cliente(db.Model):
    __tablename__ = 'cliente'

    id = db.Column(db.Integer, primary_key=True)
    nomeCliente = db.Column(db.String(100), nullable=False)
    cpfCnpj = db.Column(db.String(20), nullable=False, unique=True)
    login = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    dataNascimento = db.Column(db.Date, nullable=False)
    estadoCivil = db.Column(db.String(20), nullable=False)
    nrDocumento = db.Column(db.String(20), nullable=False)
    dataEmissaoDoc = db.Column(db.Date, nullable=False)
    naturalidade = db.Column(db.String(100), nullable=False)
    idNacionalidade = db.Column(db.Integer, nullable=False)
    logradouro = db.Column(db.String(100), nullable=False)
    nrEndereco = db.Column(db.String(20), nullable=False)
    dddTel = db.Column(db.String(5))
    telefone = db.Column(db.String(15))
    dddCel = db.Column(db.String(5))
    celular = db.Column(db.String(15))
    bairro = db.Column(db.String(50), nullable=False)
    complemento = db.Column(db.String(100))
    cidade = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.String(50), nullable=False)
    cep = db.Column(db.String(15), nullable=False)
    nacao = db.Column(db.String(50), nullable=False)
    profissao = db.Column(db.String(50), nullable=False)
    estadoEmissor = db.Column(db.String(50), nullable=False)
    dataCadastro = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'Cliente {self.nomeCliente}'


@app.route('/')
def index():
    return render_template('cadastro_cliente.html')

@app.route('/clientes', methods=['POST'])
def cadastrar_cliente():
    data = request.json
    data_nascimento = datetime.strptime(data['dataNascimento'], "%d/%m/%Y")
    data['dataNascimento'] = data_nascimento
    data_emissao_doc = datetime.strptime(data['dataEmissaoDoc'], "%d/%m/%Y")
    data['dataEmissaoDoc'] = data_emissao_doc
    data_cadastro = datetime.strptime(data['dataCadastro'], "%d/%m/%Y")
    data['dataCadastro'] = data_cadastro
    novo_cliente = Cliente(**data)
    db.session.add(novo_cliente)
    db.session.commit()
    return jsonify({'message': 'Cliente cadastrado com sucesso!'}), 201

@app.route('/clientes', methods=['GET'])
def listar_clientes():
    clientes = Cliente.query.all()
    return jsonify(clientes), 200

if __name__ == '__main__':
    app.run(debug=True)
