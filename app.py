from flask import Flask

# __name__ de forma manual = "__main__"
app = Flask(__name__)

#colocar o endpoint dentro da rota
@app.route("/")
#criar o que vai ser executado a partir dela
def helloworld():
    return "Hello World"

@app.route("/about")
def about():
    return "Página sobre, doideira"

#pra executar, fazer funcionar
if __name__ == "__main__":
    app.run(debug=True)

#esse modo tem que ser apenas local, se for no servidor a gente não faz isso

#[04/Jun/2025 12:48:05] "GET /about HTTP/1.1" 200
#get - metodo que vem do navegador
#http = protocolo
#200 = resposta positiva