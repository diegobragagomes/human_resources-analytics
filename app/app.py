import pandas as pd
import streamlit as st
from minio import Minio
import joblib
import matplotlib.pyplot as plt
from pycaret.classification import *

client = Minio( "localhost:9000",
                access_key= "minioadmin",
                secret_key= "minioadmin",
                secure= False)

client.fget_object("curated", "model.pkl", "model.pkl")
client.fget_object("curated", "dataset.csv", "dataset.csv")
client.fget_object("curated", "cluster.joblib", "cluster.joblib")

var_model = "model"
var_model_cluster = "cluster.joblib"
var_dataset = "dataset.csv"

#Recarregando o modelo treinado

model = load_model(var_model)
model_cluster = joblib.load(var_model_cluster)

#Recarregando o conjunto de dados

dataset = pd.read_csv(var_dataset)

print(dataset.head())

#Título

st.title("Human Resource Analytics")

#Subtítulo

st.markdown("App utilizado para exibir a solução de Machine Learning para o problema de turnover")

#Imprime o conjunto de dados 

st.dataframe(dataset.head())

#Grupos de empregados

kmeans_colors = ['green' if c == 0 else 'red' if c == 1 else 'blue' for c in model_cluster.labels_]

st.sidebar.subheader("Defina os atributos do empregado para predição de turnover")

#Atributos 

satisfaction = st.sidebar.number_input("satisfaction", value = dataset['satisfaction'].mean())
evaluation = st.sidebar.number_input("evaluation", value=dataset["evaluation"].mean())
projectCount = st.sidebar.number_input("projectCount", value=dataset["projectCount"].mean())
yearsAtCompany = st.sidebar.number_input("yearsAtCompany", value=dataset["yearsAtCompany"].mean())

#Colocando botão na tela

btn_predict = st.sidebar.button("Realizar Classificação")

#Verifica se o botão foi acionado

if btn_predict:
    data_teste = pd.DataFrame()
    data_teste['satisfaction'] = [satisfaction]
    data_teste['evaluation'] = [evaluation]
    data_teste['projectCount'] = [projectCount]
    data_teste['yearsAtCompany'] = [yearsAtCompany]

    print(data_teste)

    result = predict_model(model, data = data_teste)

    st.write(result)

    #plotagem

    #fig = plt.figure(figsize = (10,6))
    #plt.scatter(x = "satisfaction",
                #y = "evaluation",
                #data_= dataset[dataset.turnover == 1],
                #alpha = 0.25)

    #plt.xlabel("Satisfaction")
    #plt.ylabel("Evaluation")


    #plt.scatter(x = model_cluster_centers_[:0],
                #y=  model_cluster_centers_[:1],
                #color = 'black',
                #marker = 'X', s = 100)

    #plt.scatter(x = [satisfaction],
                #y=  [evaluation],
                #color = 'yellow',
                #marker = 'X', s = 300)

    #plt.title("Grupos de Empregados - Satisfação vs Avaliação")
    #plt.show()
    #st.pyplot(fig)




