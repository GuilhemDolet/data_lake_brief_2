from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient
from azure.storage.blob import BlobServiceClient


# Fonction pour récupérer la valeur du secret, stocké dans keyvault

def get_secret_from_keyvault_with_sp(secret_name, key_vault_url, client_id, client_secret, tenant_id):
    """Récupère un secret depuis Key Vault en utilisant un Service Principal explicite.
    
    Arguments :
    - secret_name : nom du secret à récupérer.
    - key_vault_url : URL du Key Vault.
    - client_id : ID du Service Principal.
    - client_secret : Secret du Service Principal.
    - tenant_id : ID du tenant Azure.
    
    Retourne :
    - La valeur du secret.
    """
    credential = ClientSecretCredential(client_id=client_id, client_secret=client_secret, tenant_id=tenant_id) # classe qui permet de s'authentifier auprès d'un service principal d'azure -
    client = SecretClient(vault_url=key_vault_url, credential=credential) # interagir avec un Azure Key Vault pour effectuer des opérations
    secret = client.get_secret(secret_name) # fonction récupératrice de la valeur associée au secret_name, via le client créé au dessus.

    return secret.value

def connect_to_data_lake(client_id, client_secret, tenant_id, storage_account_name):
    """Cette fonction va permettre la connexion au datalake, en utilisant le mot de passe
    récupérer sur keyvault, afin de se connecter au service principale disposant des droits
    d'écriture sur le datalake.

    Args:
        client_id (_type_, optional): _description_. Defaults to client_id_dl.
        client_secret (_type_, optional): _description_. Defaults to mdp.
        tenant_id (_type_, optional): _description_. Defaults to tenant_id.
    """
    credential = ClientSecretCredential(tenant_id=tenant_id, client_id=client_id, client_secret=client_secret)
    
    blob_service_client = BlobServiceClient(account_url=f"https://{storage_account_name}.blob.core.windows.net", credential=credential)

    print("Connexion au DataLake réussi")

    return blob_service_client