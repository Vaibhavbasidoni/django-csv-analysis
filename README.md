# Django CSV Analysis

This project is a Django application that allows users to upload CSV files, analyze the data, and visualize the results using matplotlib and seaborn.

## Features

- Upload CSV files
- Display the first few rows of the data
- Display summary statistics
- Display missing values
- Generate and display histograms for numerical columns

## Setup Instructions

### Prerequisites

- Python 3.x
- Django
- pandas
- matplotlib
- seaborn

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Vaibhavbasidoni/django-csv-analysis.git
    cd django-csv-analysis
    ```

2. **Create a virtual environment** (optional but recommended):
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

5. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

6. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

1. Navigate to the upload page.
2. Upload a CSV file.
3. View the analysis results, including data head, summary statistics, missing values, and histograms for numerical columns.

## Project Structure

- `data_processor/`: Contains the Django application code.
- `data_processor/forms.py`: Defines the form for file upload.
- `data_processor/views.py`: Handles the file upload, data processing, and visualization.
- `data_processor/templates/data_processor/`: Contains the HTML templates.


