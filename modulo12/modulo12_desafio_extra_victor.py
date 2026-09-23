'''




'''

from flask import Flask, jsonify, request
import pytest

# ---------------------------------------------------------
# APLICAÇÃO FLASK
# ---------------------------------------------------------
app = Flask(__name__)

@app.route('/somar', methods=['POST'])
def somar():
    dados = request.get_json()
    if not dados or 'a' not in dados or 'b' not in dados:
        return jsonify({'erro': 'Entrada inválida'}), 400
    return jsonify({'resultado': dados['a'] + dados['b']}), 200

@app.route('/dividir', methods=['POST'])
def dividir():
    dados = request.get_json()
    if not dados or 'a' not in dados or 'b' not in dados:
        return jsonify({'erro': 'Entrada inválida'}), 400
    if dados['b'] == 0:
        return jsonify({'erro': 'Divisão por zero não é permitida.'}), 400
    return jsonify({'resultado': dados['a'] / dados['b']}), 200


# ---------------------------------------------------------
# TESTES AUTOMATIZADOS (PYTEST)
# ---------------------------------------------------------
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_rota_somar(client):
    response = client.post('/somar', json={'a': 5, 'b': 5})
    assert response.status_code == 200
    assert response.get_json() == {'resultado': 10}

def test_rota_dividir_sucesso(client):
    response = client.post('/dividir', json={'a': 10, 'b': 2})
    assert response.status_code == 200
    assert response.get_json() == {'resultado': 5.0}

def test_rota_dividir_por_zero(client):
    response = client.post('/dividir', json={'a': 10, 'b': 0})
    assert response.status_code == 400
    assert response.get_json() == {'erro': 'Divisão por zero não é permitida.'}


# ---------------------------------------------------------
# EXECUÇÃO
# ---------------------------------------------------------
if __name__ == '__main__':
    # Roda a API normalmente se executar: python app_com_testes.py
    app.run(debug=True)