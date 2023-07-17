# Rent Portugal Data Collection Project

This repository contains a data collection project that focuses on gathering rental data from a popular house rental website in Portugal. The objective of this project is to apply best practices in MLOps, utilizing technologies such as XGBoost, Prefect, Evidently AI, mlflow, and FastAPI.

## Problem
Finding suitable rental properties in Portugal can be a time-consuming and challenging task. The rental market is vast and dynamic, making it difficult for individuals and businesses to estimate fair rental prices for different types of properties in various regions. Additionally, manually collecting and analyzing rental data from numerous sources can be tedious and error-prone.

To address these challenges, the Rent Portugal Data Collection Project aims to automate the data collection process from a specific house rental website. By leveraging web scraping techniques and machine learning algorithms, the project seeks to provide accurate and up-to-date rental price estimations, empowering users to make informed decisions about rental properties.

## Project Overview
The Rent Portugal Data Collection Project automates the process of collecting rental data from a popular house rental website in Portugal. By scraping the website, relevant information such as property details, location, and rental prices are collected and stored for further analysis. The project utilizes technologies such as XGBoost, Prefect, Evidently AI, mlflow, and FastAPI to apply best practices in MLOps and ensure efficient data collection, modeling, monitoring, and real-time predictions.

## Technologies Used
The project utilizes the following technologies:

1. XGBoost: XGBoost is a powerful machine learning library known for its high-performance gradient boosting algorithms. It can be used for building predictive models based on the collected rental data.
2. Prefect: Prefect is an open-source workflow management system that allows for the creation and scheduling of data collection tasks. It provides a powerful infrastructure for orchestrating the data collection process, ensuring reliability and scalability.
3. Evidently AI: Evidently AI is a Python library that enables model monitoring and validation. It allows for the analysis and visualization of model performance, ensuring the quality and reliability of the collected data and subsequent models.
4. mlflow: mlflow is an open-source platform for managing the machine learning lifecycle. It provides tools for tracking experiments, packaging code, and managing model deployments. In this project, mlflow is used to evaluate and compare different machine learning models' performance.
5. FastAPI: FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints. It can be used to develop a RESTful API to expose the collected data and provide real-time predictions.


## Project Structure
The project follows a modular structure to separate different stages and functionalities. The main components of the project are:


Usage
To use this project, follow these steps: