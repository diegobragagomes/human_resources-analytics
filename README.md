# Projeto de Human Resources Analytics

## Descrição Inicial ##

O projeto possui como principal interesse, <b>o maior entendimento dos atributos que podem levar ao churn</b>.

O objetivo é destrinchar as características de funcionários e as relações deles com a empresa, para buscar quantificar a possibilidade de um possível churn no decorrer do tempo.

O projeto conta com três principais etapas:
<li> Arquitetura dos dados </li>
<li> Entendimento e Processamento dos Dados </li>
<li> Predição dos Dados via Algoritmos de Machine Learning</li><br>

Principais Ferramentas:
<li><b>Airflow</b></li>
<li> <b>Minio</b></li>
<li><b>SQL</b></li>
<li><b>Python</b></li><br>

## Arquitetura de Dados

Nessa etapa, o objetivo foi desenhar a arquitetura, isto é, o caminho pelo qual os dados partiriam desde o computador até a visualizaçaõ de dados e predição deles. Abaixo, pode-se observar o desenho dessa arquitetura:

<img src = "./images/HR_project.drawio (1).png" alt = "Arquitetura de Dados">

<li> Tudo se inicia com o download dos dados do case <a href="https://www.kaggle.com/datasets/yingwurenjian/chicago-divvy-bicycle-sharing-data">Chicago Divvy</a> no Kaggle. </li><br>

<li>Após isso, os dados são inseridos em um bucket, chamado de Raw, no <b>S3</b> dentro da AWS. Esses dados chegarão brutos, em .csv, e serão processados pelo <b>EMR</b> (Elastic Map Reduce) e serão salvos em .parquet em outro bucket no <b>S3</b>, chamado de Curated.</li><br>

<li>A partir desse dado em .parquet, haverá um acionamento de um crawler no <b>Glue</b>, responsável por entender a estrutura e o tipo dos dados, para catalogar como esses dados estão dispostos no arquivo e qual é o formato de cada uma das colunas. </li><br>

<li>Seguindo o caminho dos dados até a visualização, faz-se necessária a utilização do <b>Redshift Spectrum</b>, que permite a leitura de arquivos no <b>S3</b> pelo <b>Redshift</b> ao se criarem schemas e tabelas externas, com o auxílio do catálogo prévio do <b>Glue</b>. A partir desse processo, os dados que foram catalogados no <b>Glue</b> e estão presentes no <b>S3</b>, podem ser lidos e disponibilizados no <b>RedShift</b>.</li><br>

<li>Por último, a ferramenta de visualização escolhida foi o <b>Metabase</b>, pelo fato de ser open source e trabalhar com o <b>SQL</b>, que é uma ferramenta que também buscava desenvolver e expor. Para que o <b>Metabase</b> pudesse funcionar, foi utilizado o <b>Docker</b> e a partir da imagem metabase/metabase rodando na porta 3000 do localhost, houve a possibilidade de utilização dele. A conexão no <b>Metabase</b> é feita de maneira bastante simples, conectando ao database do <b>Redshift</b> e fazendo queries a partir dele.</li><br>

Essa é uma arquitetura simples, mas cumpre o objetivo de se trabalhar quase inteiramente na nuvem, passando pelos processos de storage, processamento e disponibilização como um DW, pelo <b>Redshift</b>, até a conexão com a ferramenta de visualização, esta que poderia estar sendo utilizada num EC2, como um app no Elastic BeanStalk, numa app no Heruko, ou simplesmente na própria nuvem do <b>Metabase</b>, como seria o caso de uma versão online paga para o <b>Power BI</b>, <b>Tableau</b> e demais.

- Quais são os fatores que influenciam para um colaborador deixar a
empresa?

- Como reter pessoas?

- Como antecipar e saber se um determinado colaborador vai sair da
empresa?

E por fim disponibilizar recursos para que a empresa consiga realizar a predição para verificar se um colaborador vai ou não deixar a empresa com base em atributos como comportamento e carga de trabalho, nível de satisfação com a empresa e resultados de performance.

Para resolver esse problema foi construído uma solução completa para armazenamento, gestão e automatização de fluxos de dados utilizando tecnologias como **Apache Airflow, Docker e Minio**, além de explorar uma suíte poderosa de tecnologias para trabalhar com Análise de Dados e Machine Learning que são: **Pandas, Scikit-learn, Pycaret, Streamlit**.

A escolha do **Apache Airflow** foi devido a necessidade do projeto de lidar com fontes de dados diferentes, com formatos diferentes, no qual uma orquestração, uma automatização, dos processos de extração e pequenas transformações nos arquivos se mostrava interessante.

Em relação ao **Docker e Minio**, ambos serviram como ferramentas para a configuração ideal para auxiliar o manejo dos arquivos e sua orquestração. Um dando possibilidade do **Minio*** e **Airflow** funcionarem de forma adequada, graças ao seu poder de compartimentalização, enquanto o outro foi responsável pela criação de um Data Lake, onde os arquivos ficaram dispostos e foram acionados nos momentos necessários.

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

## Conclusão

Através desse projeto foi possível praticar e implementar conceitos importantes da Ciência e Engenharia de Dados e propor uma solução para um problema latente e recorrente de qualquer empresa que é a retenção de talentos através da Análise de Dados de Recursos Humanos.

Como um processo de melhoria contínua pode ser desenvolvido uma automação para executar não só o pipeline de coleta e transformação de dados como automatizar os passo da etapa de Machine Learning e Deploy.
