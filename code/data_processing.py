from azureml.opendatasets import NycTlcYellow
import dask.dataframe as dd
from datetime import datetime
from dateutil import parser


def extract(start_date, end_date):
    start_date = parser.parse(start_date)
    end_date = parser.parse(end_date)
    nyc_tlc = dd.from_pandas(NycTlcYellow(start_date=start_date, end_date=end_date).to_pandas_dataframe(), npartitions=12)
    return nyc_tlc

def transform(nyc_tlc_df):
    nyc_tlc_df
    nyc_tlc_df["puMonth"] = nyc_tlc_df['tpepPickupDateTime'].apply(lambda x: x.month, meta=('month', 'int'))
    nyc_tlc_df["puYear"] = nyc_tlc_df['tpepPickupDateTime'].apply(lambda x: x.year, meta=('year', 'int'))
    nyc_tlc_df = nyc_tlc_df.drop(["vendorID", "tpepDropoffDateTime", "tpepPickupDateTime", "tripDistance", 
                               "puLocationId", "doLocationId", "startLon", "startLat", "endLon", "endLat", 
                               "rateCodeId", "storeAndFwdFlag"], axis = 1)
    nyc_tlc_df["improvementSurcharge"] = nyc_tlc_df["improvementSurcharge"].astype('float')

    nyc_tlc_grouped = nyc_tlc_df.groupby(['paymentType', 'puYear', 'puMonth']).agg({'passengerCount': 'mean', "fareAmount": "mean", 
                                                                               "extra": "mean", "mtaTax": "mean", 
                                                                               "improvementSurcharge": "mean", 
                                                                               "tipAmount": "mean", "tollsAmount": "mean", 
                                                                               "totalAmount": "mean"})
    nyc_tlc_sorted = nyc_tlc_grouped.sort_values(['paymentType', 'puYear', 'puMonth'], ascending=[True, True, True])
    return nyc_tlc_sorted

def load(nyc_tlc_sorted):
    csv_file_path = "nyc_tlc_processed.csv"
    # Enter path to where the csv should be saved to
    nyc_tlc_sorted.to_csv(csv_file_path, index = True, single_file = True)

    parquet_file_path = 'nyc_tlc_processed.parquet'
    # Enter path to where the parquet file should be saved to
    nyc_tlc_sorted.to_parquet(parquet_file_path, engine='pyarrow')
    return


def process_data():
    nyc_tlc = extract("2018-10-01", "2018-12-31")
    # Put in the period to analyze in the line above to have the script run for the period wanted
    nyc_tlc_sorted = transform(nyc_tlc)
    load(nyc_tlc_sorted)

process_data()
# breakpoint()