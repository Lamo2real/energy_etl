
import boto3
from datetime import datetime
from botocore.exceptions import ClientError
from log import setup_logger #i am running this from extract.py so it will be in the etl directory

def fetch_date_object():
    """
    fetch the date from S3 object stored as .txt
    """
    try:
        logger = setup_logger()
    except FileNotFoundError as fnfe:
        print(f'no file was found: {fnfe}', exc_info=True)
        raise

    try:
        client = boto3.client('s3')
        file = client.get_object(Bucket='bucket-name', Key='file-name')
        if file:
            date_object = file['Body'].read().decode('utf-8')
        else:
            date_object = datetime.strptime('2001-01', '%Y-%m').strftime('%Y-%m')
            logger.info('this is the start of the project and no txt file is pre-existing in S3')

        return date_object


    except ClientError as ce:
        logger.error(f'could not connect or other issues with s3 client: {ce}', exc_info=True)
        raise
    except ValueError as ve:
        logger.error(f'invalid value: {ve}', exc_info=True)
        raise
    except Exception as e:
        logger.error(f'unexpected error: {e}', exc_info=True)
        raise


def push_date_object():
    pass


def current_date():
    pass