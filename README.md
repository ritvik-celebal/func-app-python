# Azure Storage Queue Trigger Function

This repository contains an Azure Function that is triggered by messages in an Azure Storage Queue. The function processes the messages and stores the data in Azure Table Storage.

## Prerequisites

- Python 3.8 or later
- Azure Functions Core Tools
- Azure Storage Account
- Azure Table Storage
- Azure CLI

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/AzureServerLess.git
    cd AzureServerLess/AzureStorageQueueTriggerFunction
    ```

2. **Create a virtual environment and activate it**:
    ```bash
    python -m venv .venv
    .venv\Scripts\activate  # On Windows
    # source .venv/bin/activate  # On macOS/Linux
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root of the project and add the following environment variables:
    ```env
    TABLE_STORAGE_ENDPOINT=<your_table_storage_endpoint>
    TABLE_NAME=<your_table_name>
    ```

5. **Run the function locally**:
    ```bash
    func start
    ```

## Deployment

1. **Log in to Azure**:
    ```bash
    az login
    ```

2. **Create a resource group**:
    ```bash
    az group create --name <resource-group-name> --location <location>
    ```

3. **Create a storage account**:
    ```bash
    az storage account create --name <storage-account-name> --location <location> --resource-group <resource-group-name> --sku Standard_LRS
    ```

4. **Deploy the function app**:
    ```bash
    func azure functionapp publish <function-app-name>
    ```

## Testing

Unit tests are located in the `tests` directory. To run the tests, use the following command:
```bash
python -m unittest discover -s tests