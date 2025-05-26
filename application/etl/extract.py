import requests
import os
from dotenv import load_dotenv
import pandas as pd
# from datetime import datetime
from log import setup_logger
from extract_functions.s3_date_object import fetch_date_object


def extract_energy_data() -> pd.DataFrame:
    """
    extract data from the API and use
    pandas json_normalize to create and
    return a Dataframe out of it
    """

    try:
        logger = setup_logger()
        load_dotenv()
        api_key = os.environ.get("API_KEY")

    except FileNotFoundError:
        logger.error("file to .env was not found, check if it exists")
        raise
    except Exception as e:
        logger.error(f"unexpected error: {e}", exc_info=True)
        raise

    
    ###### assign variable ######
    req_exc = requests.exceptions
    #############################

    all_json_data = []
    try:
        date = fetch_date_object()
        while date <= '2025-05':
            
            print(date)
            endpoint = (
                "https://api.eia.gov/v2/electricity/retail-sales/data/"
                "?frequency=monthly"
                "&sort[0][column]=period&sort[0][direction]=asc"
                "&data[0]=customers"
                "&data[1]=price"
                "&data[2]=revenue"
                "&data[3]=sales"
                f"&start={date}&end=2025-01" # needs to change end date to dynamic value to current date
                "&length=5000"
                f"&api_key={api_key}"
            )
            data = requests.get(endpoint)
            json_data = data.json()
            all_json_data.append()
    except (
        req_exc.Timeout,
        req_exc.ConnectionError,
        req_exc.HTTPError,
        req_exc.RequestException,
    ) as e:
        logger.error(f"Exception occurred: {e}", exc_info=True)
        raise
    except Exception as e:
        logger.error(f"unexpected error: {e}", exc_info=True)

    try:
        raw_df = pd.json_normalize(json_data["response"]["data"])
        print(raw_df["period"].dtype)

    except KeyError as ke:
        logger.error(f"Exception occurred: {ke}", exc_info=True)
        raise
    except Exception as e:
        logger.error(f"unexpected error: {e}", exc_info=True)
        raise
    print(raw_df.tail(10))
    return raw_df


if __name__ == "__main__":

    extract_energy_data()
