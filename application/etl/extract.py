

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

    except FileNotFoundError:
        logger.error('file to .env was not found, check if it exists')
        raise
    except Exception as e:
        print(e)
        raise

    endpoint = (
        f'https://api.eia.gov/v2/electricity/retail-sales/data/'
        f'?frequency=monthly'
        f'&sort[0][column]=period&sort[0][direction]=asc'
        f'&data[0]=customers'
        f'&data[1]=price'
        f'&data[2]=revenue'
        f'&data[3]=sales'
        f'&start=2001-01&end=2001-12'
        f'&length=5000'
        f'&api_key={api_key}'
    )

    ###### assign variable ######
    req_exc = requests.exceptions
    #############################
    try:
        data = requests.get(endpoint)

    except (
        req_exc.Timeout, req_exc.ConnectionError,
        req_exc.HTTPError, req_exc.RequestException, Exception
    ) as e:
        logger.error(f'Exception occurred: {e}', exc_info=True)
        raise

    try:
        json_data = data.json()
        raw_df = pd.json_normalize(json_data['response']['data'])

    except KeyError as ke:
        logger.error(ke, exc_info=True)
        raise
    except Exception as e:
        logger.error(f'unexpected error: {e}', exc_info=True)
        raise

    # print(raw_df.head(10))
    return raw_df


if __name__ == '__main__':
    extract_energy_data()
