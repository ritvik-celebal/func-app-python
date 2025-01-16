import azure.functions as func
import logging
import datetime

def main(msg: func.QueueMessage) -> None:
    message = msg.get_body().decode('utf-8')
    print(f"Queue trigger function processed message: {message}")
