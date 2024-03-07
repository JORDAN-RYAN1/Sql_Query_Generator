
# SQL Query Generator: Streamlit SQL Query Generator

SQLGenius is a web application built with Streamlit, designed to assist users in generating SQL queries effortlessly. Simply input your query in English, and let SQLGenius translate it into a valid SQL query snippet. The tool provides not only the generated SQL query but also the expected output and an explanation for better understanding.

## Features:

- English to SQL translation
- Streamlined interface with Streamlit
- Insightful explanations for generated queries
- Quick access to expected query output

## Prerequisites:

Before running the application, make sure you have the following installed:

- Python 3.x
- Pip (Python package installer)

## Installation:

1. Clone the repository to your local machine
2. Install the required Python packages

## Configuration:

1. Obtain a Google API key from the [Google Cloud Console]([https://console.cloud.google.com/](https://aistudio.google.com/app/apikey)).
2. Insert your API key in the `config.py` file:

    ```python
    # config.py

    GOOGLE_API_KEY = "INSERT_YOUR_API_KEY_HERE"
    ```

## How to Run:

1. Open a terminal and navigate to the project directory.

2. Run the Streamlit app:

    ```bash
    streamlit run Sql_Quer_Generator.py
    ```

3. Open your web browser and go to [http://localhost:8501](http://localhost:8501) to access the application.

## Usage:

1. Enter your SQL query in English in the provided text area.

2. Click the "Generate SQL Query" button.

3. Explore the generated SQL query, expected output, and query explanation.
