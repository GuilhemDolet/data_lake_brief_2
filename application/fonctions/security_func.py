from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

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

