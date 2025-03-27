from typing import List
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential


class IndexedTextConsumerAzure:

    def upload_documents_to_index(
        self,
        azure_endpoint: str,
        azure_index_name: str,
        azure_api_key: str,
        documents: List[str],
    ) -> None:
        """
        Upload documents to an Azure AI Search index using an API key.

        :param endpoint: The endpoint URL of your Azure AI Search service
        :param index_name: Name of the index you want to upload documents to
        :param api_key: The API key for authentication
        :param documents: List of documents to upload
        """
        try:
            credential = AzureKeyCredential(azure_api_key)

            search_client = SearchClient(
                azure_endpoint, azure_index_name, credential
            )

            try:
                documents_list = [
                    {"id": str(idx), "chunk": chunk}
                    for idx, chunk in enumerate(documents, 1)
                ]

                result = search_client.upload_documents(documents_list)
                print(f"Uploaded {len(documents)} documents")

                for res in result:
                    if res.succeeded:
                        print(f"Document {res.key} uploaded successfully")
                    else:
                        print(f"Document {res.key} failed : {res.error_message}")

            except Exception as e:
                print(f"Upload failed: {e}")

        except Exception as e:
            print(f"An error occurred: {e}")
