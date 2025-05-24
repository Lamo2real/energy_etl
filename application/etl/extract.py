


import requests
import os
from dotenv import load_dotenv
import pandas as pd
from log import setup_logger
logger = setup_logger()

def extract_energy_data() -> pd.DataFrame:
    """
    extract data from the API and use
    pandas json_normalize to create and
    return a Dataframe out of it
    """

    try:    
        load_dotenv()
        api_key = os.environ.get('API_KEY')

    except FileNotFoundError as fnfe:
        logger.error('file to .env was not found, check if it exists')
        raise
    except Exception as e:
        print(e)
        raise

    endpoint = (
        f"https://api.eia.gov/v2/electricity/retail-sales/data/"
        f"?frequency=monthly"
        f"&sort[0][column]=period&sort[0][direction]=asc"
        f"&data[0]=customers"
        f"&data[1]=price"
        f"&data[2]=revenue"
        f"&data[3]=sales"
        f"&start=2001-01&end=2001-12"
        f"&length=5000"
        f"&api_key={api_key}"
    )

    ###### assign variable ######
    req_exc = requests.exceptions
    #############################
    try:
        data = requests.get(endpoint)

    except req_exc.Timeout:
        logger.error('request timeout')
        raise
    except req_exc.ConnectionError:
        logger.error('connection to API FAILED')
        raise
    except req_exc.HTTPError as http_error:
        logger.error(f"HTTP error ocurred: {http_error}")
        raise
    except req_exc.RequestException as re:
        logger.error(f"An error ocurred while making the request: {re}")
        raise

    json_data = data.json()
    raw_df = pd.json_normalize(json_data['response']['data'])
    # print(raw_df.head(10))
    return raw_df
    


if __name__ == '__main__':
    extract_energy_data()