from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.storage.blob import BlobServiceClient
import os
from dotenv import load_dotenv
from fonctions.security_func import get_secret_from_keyvault_with_sp

# variables d'environnement 
load_dotenv()

secret_name = os.getenv("KEYVAULT_SECRET_NAME")
key_vault_url = os.getenv("KEYVAULT_URL")
client_id = os.getenv("SP_CLIENT_ID")
client_secret = os.getenv("SP_KEYVAULT_VALUE")
tenant_id= os.getenv("TENANT_ID")

# 1ere étape : je récupère la valeur de mon secret, dans keyvault, en me connectant au service principal secondaire
# cela me permet 
mdp = get_secret_from_keyvault_with_sp(secret_name, key_vault_url, client_id, client_secret, tenant_id )

print(mdp)