from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.storage.blob import BlobServiceClient
import os
from dotenv import load_dotenv
from fonctions.security_func import get_secret_from_keyvault_with_sp, connect_to_data_lake
from fonctions.upload_func import upload_local_data_to_cloud

# variables d'environnement 
load_dotenv()

secret_name = os.getenv("KEYVAULT_SECRET_NAME")
key_vault_url = os.getenv("KEYVAULT_URL")
client_id = os.getenv("SP_CLIENT_ID")
client_secret = os.getenv("SP_KEYVAULT_VALUE")
tenant_id= os.getenv("TENANT_ID")
client_id_dl = os.getenv("SP_DL_CLIENT_ID")
storage_account_name = os.getenv("STORAGE_ACCOUNT_NAME")

local_file_path = "./external_data/data.csv"
blob_name = "mon_deuxieme_fichier_sur_mon_data_lake"

# 1ere étape : je récupère la valeur de mon secret, dans keyvault, en me connectant au service principal secondaire
mdp = get_secret_from_keyvault_with_sp(secret_name, key_vault_url, client_id, client_secret, tenant_id )

#2ème étape : je me connecte au deuxième service principal, grace au mdp que je viens de récupérer. J'obtiendrais donc les droits d'écrire sur le Datalake
blob_service_client = connect_to_data_lake(client_id_dl, mdp, tenant_id, storage_account_name)

containers = blob_service_client.list_containers()
for container in containers:
    print(f"Container trouvé : {container['name']}")

target_container = input("Quel container voulez-vous choisir: ")

upload_local_data_to_cloud(blob_service_client, target_container, local_file_path, blob_name)