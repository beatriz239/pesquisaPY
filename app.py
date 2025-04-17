from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resposta', methods=['POST'])
def resposta():
    nome = request.form['nome']
    return f'<h1>Olá, {nome}! Bem-vindo ao mundo do Python + Web! 🐍🌐</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
