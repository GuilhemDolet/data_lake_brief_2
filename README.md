# DataLake semaine 2
Deuxième semaine sur la notion de data lake (AZURE)

## Notions : 
- C’est quoi **Storage Access Keys** (clés de compte de stockage): 
	C’est comme un mot de passe généré automatiquement qui protège l’accès au compte de stockage.
- C’est quoi **Azure Key Vault** :
	système de gestion et de protection des clés (mot de passe). Point fort, on peut permuter et régénérer régulièrement les clés.
- C’est quoi un **SAS**: 
	mécanisme d’autorisation basé sur des jetons. L’intérêt est de fournir l’accès à des ressources spécifiques, sans donner l’accès global à tout le compte de stockage 
    SAP : Signature d'Accès Partagé = SAS : Shared Access Signature (delegation key)
- C'est quoi **Microsoft Endtra ID**:
     c’est un outil qui permet de gérer qui peut accéder à quoi, où service de gestion des identités et des accès.
     Il vérifie l’identité des personnes ou des applications qui essaient de se connecter à des ressources.
     Single Signe On : SSO
- C'est quoi **IAM (Identity and Access Management) et Role-Based Access Control (RBAC)**:
    Le RBAC est une méthode du IAM. Il découpe en rôle, un ou des ensemble de permissions. Puis les attribut à des utilisateurs ou à des groupes. Microsoft Entra ID est la solution d’IAM de Microsoft, conçue pour gérer les identités et les accès dans l’écosystème Microsof