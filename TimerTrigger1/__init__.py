import datetime
import logging

def main(mytimer) -> None:
    utc_time = datetime.datetime.utcnow().isoformat()
    logging.info(f"Timer triggered at {utc_time}")