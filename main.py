from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''<h1> Sistema de coleta e visualização de dados epidemiológicos - Primeira entrega </h1>
    <h2> Nayara Lorrane Santos Silveira - RA: 1460481821067</h2> 
    <h2> Professor: FABRICIO GALENDE MARQUES DE CARVALHO</2>'''


if __name__ == "__main__":
    app.run()