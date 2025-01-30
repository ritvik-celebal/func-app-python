import azure.functions as func
import logging
from azure.data.tables import TableServiceClient, TableEntity
from azure.identity import DefaultAzureCredential
import datetime
import json
import os

def main(msg: func.QueueMessage) -> None:
    logging.info("Queue trigger function started.")
    message = msg.get_body().decode('utf-8')
    logging.info(f"Queue trigger function processed message: {message}")
    
    try:
        # Parse the message
        data = json.loads(message)
        row_key = data.get("row_key", str(datetime.datetime.utcnow().timestamp()))
        partition_key = data.get("partition_key", "default_partition")
        additional_data = data.get("data", {})

        # Create TableServiceClient
        table_service_client = TableServiceClient(
            endpoint=os.getenv("TABLE_STORAGE_ENDPOINT"),
            credential=DefaultAzureCredential()
        )

        # Get table client
        table_name = os.getenv("TABLE_NAME", "defaultTable")
        table_client = table_service_client.get_table_client(table_name)

        # Create entity
        entity = TableEntity()
        entity["PartitionKey"] = partition_key
        entity["RowKey"] = row_key
        entity.update(additional_data)

        # Insert or update entity in table storage
        table_client.upsert_entity(entity)
        logging.info(f"Entity with PartitionKey: {partition_key} and RowKey: {row_key} upserted successfully.")

    except json.JSONDecodeError as e:
        logging.error(f"JSON decode error: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
