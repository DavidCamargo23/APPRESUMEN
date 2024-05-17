from resumen import Resumentexto
from flask import  Flask, jsonify,render_template, request    
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
gpt_resumen = Resumentexto(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resumir_traducir', methods=['POST'])
def resumir_traducir():
    data = request.get_json()
    print(data)  
    texto = data['texto']
    idioma = data['idioma']
    resumen_traduccion = gpt_resumen.resumen(texto, idioma)
    print(resumen_traduccion) 
    return jsonify({'resultado': resumen_traduccion})


if __name__ == "__main__":
    app.run()