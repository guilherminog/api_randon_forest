from flask import Flask, request
import joblib

app = Flask(__name__)

# carega modelo 
model = joblib.load('Modelo_Floresta_Aleatorio_v100.pkl')

@app.route('/app_preditivo/<m2>;<quartos>;<banheiro>;<garagem>;<andar>;<animais>;<moveis>;<condominio>;<taxas>', methods=['GET'])
def predict_(m2,quartos,banheiro,garagem,andar,animais,moveis,condominio,taxas):
    
    #recebe inputs
    lista = [float(m2),float(quartos),float(banheiro),float(garagem),float(andar),float(animais),float(moveis),float(condominio),float(taxas)]
    try:
        previsao = model.predict([lista])
        return {'Valor_Aluguel' : str(previsao)}
    except:
        return {'Aviso': 'Deu erro na função!'}
    
   
if __name__ == '__main__':
    app.run(debug=True)



