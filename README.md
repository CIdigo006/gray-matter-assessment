# gray-matter-assessment
Take home assessment for Gray Matter Analytics


# NYC Taxi & Limousine Commission (TLC) Yellow Dataset Processing

This script demonstrates how to process the NYC TLC Yellow dataset using Azure Machine Learning (AML) Open Datasets and Dask. The goal is to clean, transform, and aggregate the data, and then save it to both CSV and Parquet formats.

## Setup

Make sure to install the required libraries:

```bash
pip install azureml.opendatasets dask pandas
```
or can run and install the requirements.txt file to install all the needed libraries

## Code Explanation

1. **Import Libraries:**

2. **Define Date Range:**

3. **Load NYC TLC Data into Dask DataFrame:**

4. **Create Month and Year Columns:**

5. **Drop Unnecessary Columns:**

6. **Convert Data Type:**`

7. **Group and Aggregate Data:**

8. **Sort Data:**

9. **Save to CSV:**

10. **Save to Parquet:**

## Output

- Processed CSV file: `nyc_tlc_processed.csv`
- Processed Parquet file: `nyc_tlc_processed.parquet`

Feel free to customize the file paths and parameters based on your specific requirements.
