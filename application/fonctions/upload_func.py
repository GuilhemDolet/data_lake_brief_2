from azure.storage.blob import BlobServiceClient

def upload_local_data_to_cloud(blob_service_client, container_name, local_file_path, blob_name):
    """Fonction qui peut charger un fichier local vers un container blob du datalake

    Args:
        container_name (_type_): _description_
        local_file_path (_type_): _description_
        blob_name (_type_): _description_
    """
    container_client = blob_service_client.get_container_client(container_name)
    with open(local_file_path, 'rb') as local_data:
        container_client.upload_blob(blob_name, local_data, overwrite=True)

    print(f"Fichier correctement uploader dans le container {container_name}")