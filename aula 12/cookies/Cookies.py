# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programacao Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Andre Moreno
# 1 semestre 2018

'''
Para verificar o examplo, digitar na URL 127.0.0.1/set e 127.0.0.1/get
'''

from flask import Flask, make_response, request, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route("/set")
def setcookie():
    resp = make_response('Setting cookie!')
    resp.set_cookie('framework', 'flask')
    return  render_template('set.html')
    #return resp

@app.route("/get")
def getcookie():
    framework = request.cookies.get('framework')
    return 'The framework is ' + framework

if __name__ == '__main__':
    app.run(debug=True)