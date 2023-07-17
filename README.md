# Sistema de Predição de Preços Aluguel Portugal
## Resumo

O projeto consiste no desenvolvimento de um sistema automatizado capaz de coletar dados de valores de aluguéis de casas e apartamentos de um determinado site. Esses dados serão utilizados para criar um modelo de predição de preços, permitindo estimar o valor de aluguel para diferentes tipos de imóveis em uma determinada região. 

## Objetivos:

1. Coletar dados de valores de aluguéis de casas e apartamentos de um site específico.(imovirtual.com)
2. Pré-processar e limpar os dados coletados, garantindo sua qualidade e consistência.
3. Desenvolver um modelo de predição de preços com base nos dados coletados, utilizando técnicas de aprendizado de máquina.

## Problem and Data

## Metodologia:

1. Identificar e selecionar um site confiável e relevante para a coleta de dados de aluguéis.
2. Desenvolver um script de web scraping para extrair os dados de aluguéis do site selecionado.
3. Realizar o pré-processamento e a limpeza dos dados coletados, tratando valores ausentes, removendo duplicatas e realizando transformações necessárias.
4. Dividir os dados em conjuntos de treinamento e teste para a construção e validação do modelo de predição.
5. Implementar um modelo de aprendizado de máquina adequado, como regressão linear, regressão logística ou algoritmos de árvore de decisão.
6. Utilizar o mlflow para avaliar o desempenho do modelo utilizando métricas como: erro quadrático médio (MSE)
7. Documentar o processo de desenvolvimento do projeto, fornecendo instruções detalhadas para replicação e uso futuro.


Start Mlflow Service
```bash
mlflow server --backend-store-uri=sqlite:///mlflow.db --default-artifact-root=s3://final-project-mlops/airflow/
```