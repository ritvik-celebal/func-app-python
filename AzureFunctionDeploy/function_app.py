import azure.functions as func
import logging
import os
from azure.identity import ManagedIdentityCredential
from azure.storage.queue import QueueClient

app = func.FunctionApp(http_auth_level=func.AuthLevel.ADMIN)

@app.route(route="pythonfunction")
def pythonfunction(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function started.')

    # Read "name" from query or body
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
        # Get queue URL from environment
        queue_url = os.getenv("QUEUE_URL")
        if not queue_url:
            raise ValueError("QUEUE_URL not set in environment variables.")

        # Authenticate with Managed Identity
        credential = ManagedIdentityCredential()
        queue_client = QueueClient(queue_url=queue_url, credential=credential)

        # Send message to queue
        queue_client.send_message(name)
        logging.info(f"Message '{name}' enqueued successfully.")

        return func.HttpResponse(f"Message '{name}' enqueued successfully.", status_code=200)

    except Exception as e:
        logging.error(f"Failed to enqueue message: {str(e)}")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)