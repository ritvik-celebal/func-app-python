import azure.functions as func
import logging
import os
from azure.identity import ManagedIdentityCredential
from azure.storage.queue import QueueClient

app = func.FunctionApp(http_auth_level=func.AuthLevel.ADMIN)

@app.route(route="pythonfunction")
def pythonfunction(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Function triggered.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
            name = req_body.get('name')
        except (ValueError, AttributeError):
            name = None

    if not name:
        return func.HttpResponse(
            "Please pass a 'name' in the query string or in the request body.",
            status_code=400
        )

    try:
        # Get queue name and storage account from environment
        storage_account_name = os.getenv("STORAGE_ACCOUNT_NAME")  # e.g., mystorageaccount
        queue_name = os.getenv("QUEUE_NAME")                      # e.g., myqueue

        if not storage_account_name or not queue_name:
            raise ValueError("STORAGE_ACCOUNT_NAME or QUEUE_NAME is not set.")

        account_url = f"https://{storage_account_name}.queue.core.windows.net"

        # Authenticate using Managed Identity
        credential = ManagedIdentityCredential()
        queue_client = QueueClient(account_url=account_url, queue_name=queue_name, credential=credential)

        # Send the message
        queue_client.send_message(name)
        logging.info(f"Message '{name}' sent to queue '{queue_name}'.")

        return func.HttpResponse(f"Message '{name}' sent successfully.", status_code=200)

    except Exception as e:
        logging.error(f"Error sending message: {str(e)}")
        return func.HttpResponse(f"Internal server error: {str(e)}", status_code=500)