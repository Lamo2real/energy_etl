import logging
from datetime import datetime

def setup_logger() -> logging:
    """setup logging and monitoring system for AWS CloudWatch Logs"""

    date = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    logging.basicConfig(
        filename=f"etl-pipeline-{date}.log",
        filemode='a',
        format='[%(levelname)s] - [%(module)s]: %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M'
    )

    list = [
        'botocore.credentials',
        'botocore.auth',
        'urllib3.connectionpool',
        'snowflake.connector', 
        'snowflake.connector.network',
        'snowflake.connector.connection'
    ]

    for noisy_logger in list:
        logger = logging.getLogger(noisy_logger)
        logger.setLevel(logging.WARNING)
        logger.propagate = False
    
    return logging.getLogger('etl-pipeline')