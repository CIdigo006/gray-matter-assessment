# gray-matter-assessment
Take home assessment for Gray Matter Analytics


# NYC Taxi Data Processing

This script is designed to process NYC Taxi data using Azure Machine Learning (AML) SDK Open Datasets and Dask for parallelized computation. It extracts, transforms, and loads the data into both CSV and Parquet formats. The script focuses on aggregating and summarizing taxi trip data based on payment type, year, and month.

## Prerequisites

Make sure you have the necessary dependencies installed. You can install them using the following:

'pip install azureml-opendatasets dask pandas pyarrow'

## Usage

1. Open the script `data_processing.py` in your preferred Python environment.

2. Set the desired date range for data extraction by modifying the `start_date` and `end_date` parameters in the `process_data` function.

   nyc_tlc = extract("2018-12-27", "2018-12-31")

3. Run the script. The data will be processed, and the results will be saved in both CSV and Parquet formats.

4. Check the specified file paths for the processed data:

   - CSV file: `nyc_tlc_processed.csv`
   - Parquet file: `nyc_tlc_processed.parquet`

## Script Structure

### 1. Extract

The `extract` function initializes the NYC Taxi dataset using AML SDK Open Datasets and converts it into a Dask DataFrame with specified partitions.

### 2. Transform

The `transform` function processes and aggregates the data. It creates new columns for the month and year, drops unnecessary columns, and calculates mean values for various trip attributes.

### 3. Load

The `load` function saves the processed data to both CSV and Parquet formats.

### 4. Process Data

The `process_data` function orchestrates the entire data processing pipeline. It sets the date range for data extraction, calls the extract, transform, and load functions, and saves the results.

## Note

Ensure that you have the required permissions and correct file paths for saving the processed data. Adjust the script parameters based on your analysis requirements.
