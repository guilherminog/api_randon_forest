# Criação de um modelo de Machine Learning RandonForest + API Flask

### Modelo de floresta randômica criado em cima do dataset de imóveis.

#### Na etapa do modelo foram feitas as etapas dê:
-> ETL

-> Exploração de dados:
    
Onde colunas e linhas foram renomeadas. Utilizando dois métodos, '.rename()' e '.replace()'.

Após são feitas análises de campos vazios. Foi utlizado o método '.isnull().sum().sort_values(ascending=False)'

Pesquisa por campos unicos, onde o método usado para buscar campos únicos foi '.nunique()', após busco informações com método '.info()', que traz informaçãoes sobre os índices, nomes da colunas, se existem dados nulos e tipo dados de cada coluna.

Após, utilizei o método '.dtypes.value_caounts()' para obter informação sobre a quantificação e tipos das colunas.

-> Exploração analítica dos dados, Tratamento e Limpeza dos dados:

Nesta etapa começo a criar filtros para colunas numéricas e categóricas.
Método utilizado: 
                'df.columns[df.dtypes == object]' para dados categóricos
                'df.columns[df.dtypes != object]' para dados numéricos

O próximo passo foi analisar qual seria o melhor objeto a ser a analisado, em relação ao grupo de dados que continha maior frequência. 
Método utilizado:
                'df['column'].value_counts( normalize=True ) * 100'

Foi Criado um laço para as colunas categóricas, onde busco um padrão nos dados ou erros de tabulação.

Método utilizado:
                for coluna in coluna_categoricas:
                    analise = df[coluna].value_counts(normalize=True) * 100
                    print(coluna, '\n', analise, '\n')

Após o passo anterior, faço ajustes nos dados, usando método '.loc' e '.iloc'. Os registros que na base de dados. Utilizei em conjuto o método '.apply()' para com para retornar 0 se algum registro fosse '-' (Hifén).    
Método:
        '.apply(lambda Registro : 0 if Registro == '-' else Registro)'

No próximo passo, crio gráficos para ter melhor viazualização dos dados e em consequência analisar como os dados estão se comportando, e como estão os outliers.

Após criar o gráficos fiz analise dos outliers utlizando métodos do pandas, e faitas as análises nos dados, foram feitos filtros nos dados para tirar outliers.


-> Features:

-> Ajustes na colunas:
    
Primeiro ajusto as colunas categoricas utlizando método '.map()', que mapeia os valores de
series de acordo com a entrada.

Após filtro uso método de exclusão de colunas '.drop()' para retirar a coluna cidade, para ter apenas os dados numéricos.

Após filtrar dados, crio uma correlação para analisar o que pode ser usado para o modelo. Nesta etapa utilizo dois métodos, correlção do pandas '.corr()' e correção utilizando 'yellowbrick.features', que utiliza o base do 'algoritmo - Pearson' (Correlação de Pearson - Estatística).

"Person é um método estatísta que busca calcular a intensidade de associação linear de uma variável independente em a ralção a outra variável dependente. O coeficiente retorna valor entre -1 a 1, onde o valor mais baixo negativo indica uma correlação inversamente proporcional, o valor mais alto positivo indica correlação direta." 
    
                                                            
-> Início da separação do dados de teste e treino:

Foi utilizada a biblioteca scikit-learn, onde crio um método para geral o Score de cada coluna e ver qual relação de cada coluna com o modelo. 

Segundo o Score quanto mais próximo de 1 mais proximo de uma correlação direta tem essa coluna para ser utlizada no modelo. (Parafraseando comentário dobre Pearson)

-> Construção do modelo:

Modelo foi construindo com lib sklearn.ensemble.RandomForestRegressor <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html>.

Com esse método podemos criar um medelo de Floresta Aleatória, que cria um série de arvores de decisão de classificação em varios subconjuntos de dados amostrais e utiliza a média para melhorar a precisão da previsão preditivae controlar o ajuste excessivo.

O paramêtro utlizado nesse caso foi 'RandomForestRegressor( max_depth=5 )', onde essa função chama o método Random Foreste Regressor e o parâmetro 'max_depth=5' diz ao método o limíte da profundidade máxima da árvore. Caso não tivesse definido nenhum parâmentro, o modelo criaria 'nós' até que todas as folhas fosse puras.

-> Avaliação do modelo:

Neste ponto crio um método para avaliar e metrificar o modelo utilizando o 'sklearn.metrics' <https://scikit-learn.org/stable/modules/model_evaluation.html>.

Utilizo método estatístico RMSE ou Raiz Quadrática Média dos Erros 'sklearn.metrics.mean_squared_error' e 'sklearn.metrics.r2_score' que é uma função de pontuação de regressão.

Após estas métricas, utilizo a lib 'yellowbrick.regressor.PredictionError' para criar um gráfico que cria uma vizualização da melhor ajuste e a predição de erro no gráfico.


Última etapa - Exportação de dados:

-> Exporto dados:

Exporto dados utlizando a função 'joblib.dump()'.

-> Carrego e testo os dados exportados:

Carrego os dados utlizando a função 'joblib.load()'.

-> Teste do modelo:

Método utilizado - 'Funcao_Modelo_Carregado.predict( x_teste.head(1).values )'.





          
            






