# Projeto de Human Resources Analytics

## Descrição Inicial ##

Neste projeto se procurou cobrir todas as etapas de um projeto real de Data Science, desde o entendimento do problema, ideação da solução, análise, etapas de machine learning e um deploy. Logo, com essa proposta, pude resolver o problema de como utilizar dados para responder a questões importantes, no que tange a área de **Recursos Humanos (Human Resources)**, para permitir que uma empresa tenha conhecimento sobre:

- Quais são os fatores que influenciam para um colaborador deixar a
empresa?

- Como reter pessoas?

- Como antecipar e saber se um determinado colaborador vai sair da
empresa?

E por fim disponibilizar recursos para que a empresa consiga realizar a predição para verificar se um colaborador vai ou não deixar a empresa com base em atributos como comportamento e carga de trabalho, nível de satisfação com a empresa e resultados de performance.

Para resolver esse problema foi construído uma solução completa para armazenamento, gestão e automatização de fluxos de dados utilizando tecnologias como **Apache Airflow, Docker e Minio**, além de explorar uma suíte poderosa de tecnologias para trabalhar com Análise de Dados e Machine Learning que são: **Pandas, Scikit-learn, Pycaret, Streamlit**.

A escolha do **Apache Airflow** foi devido a necessidade do projeto de lidar com fontes de dados diferentes, com formatos diferentes, no qual uma orquestração, uma automatização, dos processos de extração e pequenas transformações nos arquivos se mostrava interessante.

Em relação ao **Docker e Minio**, ambos serviram como ferramentas para a configuração ideal para auxiliar o manejo dos arquivos e sua orquestração. Um dando possibilidade do **Minio*** e **Airflow** funcionarem de forma adequada, graças ao seu poder de compartimentalização, enquanto o outro foi responsável pela criação de um Data Lake, onde os arquivos ficarem dispostos e foram acionados nos momentos necessários.

Para as etapas de análise e Machine Learning, utilizou-se extensamente as possibilidades das bibliotecas **Pandas e Scikit-learn**, passando pelo entendimento dos dados, através dos dataframes, transformações nesses dados e por fim a separação e tratamento deles para que os algoritmos de machine learning fossem utilizados. Houve, ainda, o uso do **PyCaret**, ferramenta interessante no que tange o AutoML (processos de machine learning mais automatizados), no qual pude comparar diversos algoritmos de machine learning de maneira bastante ágil e prática. Finalizando o projeto com a implementação do **Streamlit**, criando um mini app para que se pudesse interagir com novos dados e ver o modelo escolhido de machine learning funcionando.

## Etapas do Projeto ##

A príncipio, os dados se encontravam em arquivos em formato xlsx, json e dados no Sistemas de Gerenciamento de Banco de Dados MySQL.

Foram criadas Dags para serem empregadas pelo **Airflow**, nas quais elas liam os arquivos no **Minio**, depois faziam suas transformações e retornavam os novos arquivos ao **Minio**. Por fim, com um arquivo transformado e único, esse foi aproveitado na etapa de Análise Exploratória.

Na etapa de Análise Exploratória de Dados foram descobertos os vários insights importantes abaixo:

- A empresa tem uma rotatividade de 24%

- Podemos assumir que os empregados que mais deixam a empresa estão menos satisfeitos.

- Existe um valor considerável de empregados insatisfeitos.

- A maioria dos empregados que saíram tinha salário baixo ou médio.

- Os departamentos de vendas, técnico e suporte são top 3 departamentos com maior índice de turnover.

- Todos os empregados que estavam inseridos sem muitos projetos deixaram a empresa.

- Colaboradores com baixa performance tendem a deixar a empresa.

- Colaboradores insatisfeitos com a empresa têm uma maior tendência para evadir.

Através da análise foi possível desenvolver 3 grupos distintos para agrupar colaboradores que deixaram a empresa por comportamentos similares que são:

- **Grupo 1 (Empregados insatisfeitos e trabalhadores)**: A satisfação foi inferior a 20 e as avaliações foram superiores a 75.
Que corresponde ao grupo de funcionários que deixaram a empresa e eram bons trabalhadores, mas se sentiam péssimos no trabalho.

- **Grupo 2 (Empregados ruins e insatisfeitos)**: Satisfação entre 35 à 50 e as suas avaliações abaixo de ~ 58.
Corresponde aos empregados que foram mal avaliados e se sentiram mal no trabalho.

- **Grupo 3 (Empregados satisfeitos e trabalhadores)**:
Representa os empregados ideais, que gostam do seu trabalho e são bem avaliados por seu desempenho. Este grupo pode indicar os empregados que deixaram a empresa porque encontraram outra oportunidade de trabalho.

Para a estimativa com o objetivo de predizer se um empregado vai deixar a empresa foi implementado um modelo utilizando o algoritmo **Light Gradient Boosting Machine** que atingiu uma performance de **AUC em 0.99**. Escolhi o AUC, por se portar, em geral, mais robusto do que a Acurácia.

Através desse projeto foi possível praticar e implementar conceitos importantes da Ciência e Engenharia de Dados e propor uma solução para um problema latente e recorrente de qualquer empresa que é a retenção de talentos através da Análise de Dados de Recursos Humanos.

Como um processo de melhoria contínua pode ser desenvolvido uma automação para executar não só o pipeline de coleta e transformação de dados como automatizar os passo da etapa de Machine Learning e Deploy.
