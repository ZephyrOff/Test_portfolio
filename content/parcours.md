## Vinci Construction
##### Depuis Décembre 2021
### Ingénieur de production
#### Contexte
Travail au sein de l'équipe d'exploitation pour la résolution des incidents, l'application des changes et l'évolutions/automatisations des environnements existants.
#### Missions
##### Exploitation & support (RUN)
- Résolutions d'incidents (Web, Applicatif propriétaire, Serveur...)
- Exécution de change applicatif (Installation, Configuration, Patching...)
##### Automatisation & outils internes
- Développement d’outils Python/Bash/PowerShell pour automatiser les opérations
    - Création d'un reporting pour les mises à jour Windows (WSUS) (Powershell)
    - Parseur de log pour la sécurisation des mots de passe de compte de services et injection dans un keepass (Python)
    - Synchronisation automatique de code depuis git et notification par mail en cas de problème (Bash)
    - Création de backup de base de données multi-bases Mariadb en local et sur AWS (Bash)
- Développement de plusieurs applications internes :
    - Création d'une application interne pour la gestion des certificats (création de CSR, conversion de certificat, contrôle de l'intégrité, lecture des métadonnées...) et stockage dans un Keepass (Python)
    - Création d'une application pour faciliter la gestion de la supervision et des snapshots de VM (Python)
    - Création d'une web app pour le monitoring et le déploiement de mise à jour d'application propriétaire interne. (Python)
    - Création d'une web app pour le suivi et la gestion des applications tenues par les chefs de projets

##### Infrastructure & amélioration continue
- Hébergement des sites web publics de Vinci Construction:
    - Maintien de l'environnement actuelle
    - Création/Configuration d'un nouvel environnement d'hébergement
    - Migration de sites de production
    - Gestion de base de données
    - Automatisation des processus de mise à jour en préproduction.
    - Travail avec les éditeurs pour la mise en place de nouveaux sites et le patching des environnements actuels.
    - Mise en place de procédure pour uniformer et normer les environnements.
- Evolution et optimisation d'infrastructure existante:
    - Refonte du process de déploiement des sites web
    - Optimisation de la configuration des bases de données SQL
    - Renforcement de la sécurité et optimisation des performances sur Apache
- Installation/Configuration de serveur RDS (Remote Desktop Services) pour l'accès à des applications métiers

##### DevOps & industrialisation
- Création de playbook et rôles Ansible pour des applications métiers propriétaires
- Mise en place d'un environnement de déploiement Ansible avec Azure Pipelines sur des connecteurs locaux.

##### Knowledge Management
- Mise en place d'une solution de knowledge management pour la centralisation et la normalisation des documentations techniques et fonctionnelles de l'ensemble des équipes
    - Installation de la solution (Wiki.js)
    - Création de l'ensemble de l'arborescence et des procédures (basés sur la méthode P.A.R.A)
    - Création de pipeline Azure pour la migration des documentations, le déploiement de template et l'export de documentation au format PDF
    - Création d'une WebApp pour le déplacement simplifié des documentations, la configuration et le chargement de template et l'export des documentations au format Word ou PDF

#### Environnement technique
- Windows Server (2012 à 2019)
- RedHat (6-9)
- CentOs (6-7)
- Vcenter
- Scripting: Python, PowerShell, Bash
- Outil d'administration (AD,DNS,LDAP,SMTP...) 
- PKI
- Supervision: Check_mk
- Automatisation: Ansible, Terraform 

## Synapsys IT
##### De Septembre 2021 à Novembre 2021
### Ingénieur Système
#### Contexte

Mise en place d'une solution automatisée pour la gestion de ticket ITSM sur une base de mail.

#### Missions
- Création et configuration d'une Azure LogicApp
- Création et configuration d'une Azure App Function
- Mise en place d'un Azure Key Vault
- Développement de script python pour le parsing mail et l'interfaçage avec une API ITSM

#### Résultats
Création de ticket ITSM automatisée à partir d'une base de mail

#### Environnement technique
- Azure Cloud
- Python 

## Total Global Information Technology Services
##### De Septembre 2017 à Septembre 2020
### Ingénieur systèmes
#### Contexte

Au sein du service responsable de l’hébergement des données sensibles du groupe, en charge de maintenir les solutions déjà existantes et d'en proposer/installer des nouvelles.

600 serveurs virtuels et 200 serveurs physiques

#### Missions
- Automatisation via PowerShell/Python - Exemples de réalisations :
    Ajout d'utilisateur en masse dans les annuaires AD et LDAP avec vérification des informations utilisateurs grâce au PKI
    Déploiement de mise à jour en masse et à distance
    Solution d'exécution de commande en masse et à distance
- Présentation et mise en place d’un cloud privé (OwnCloud)
    Proposition d'une solution d'échange de fichiers sécurisés
    Installation et configuration de la solution
    Test de la solution en environnement restreint
- Elaboration et gestion de projet sur un projet de mise en place de procédure de hardening sur Windows Server
    Elaboration d'un référentiel de durcissement des systèmes Windows Server 2016
    Créations des GPO associés
    Déploiements et tests sur un environnement de test
- Migration d’un Data Center vers un nouveau site avec mise en place des procédures associées
    Inventaire du Data Center et marquage des serveurs devant être migrés
    Préparation de l'environnement réseau sur le nouveau site
    Contrôle de l'état des sauvegardes
    Mise en place des procédures de migration
    Synchronisation avec l'ensemble des équipes intervenants sur le projet
    Remontage du Data Center sur le nouveau site
    Vérification de la configuration et de l'état de fonctionnement des serveurs sur le nouveau site
- Analyse et élaboration de projets d’évolutions d’infrastructures (Virtualisation, Firewall, Stockage...)
    Refonte d'une partie du réseau d'intégration
    Mise en place de nouveau firewall
    Création d'un environnement de partage de documents internes
    Maintien en condition opérationnelle sur la solution Nutanix
- Création d’un environnement virtualisé HyperV 2016
    Installation des serveurs
    Configuration du réseau virtuel
    Configuration des clusters et des stockages associés
- Migration d’une infrastructure virtuelle d’un cluster 2012 vers 2016
- Mise en place d’une PKI Windows (RootCA + Subordinate CA)
    Installation des serveurs et des outils
    Création des certificats racines
    Configuration de la RootCA Offline et des Subordinate CA
    Déploiement des certificats
- Configuration et exploitation des ressources de stockage NetApp
- Maintien en condition opérationnelle des outils de supervision (Centreon)
    Vérification des alertes
    Contrôle de l'état des pollers
    Mise à jour de la solution

#### Environnement technique
- Windows (10, Server 2012/2016)
- Linux (Red Hat 6/7)
- Virtualisation: HyperV, ESXi, Nutanix
- Infrastructure: Firewall, PKI, Supervision 
- Scripting: Python, PowerShell 

## Total Global Information Technology Services
##### De Juin 2017 à Juillet 2017
### Intégrateur solution OpenDCIM
#### Contexte

En charge de l’intégration et de la migration du nouvel outil de CMDB pour la gestion du DataCenter

#### Missions
- Exportation des données de l’outil racktables
- Exploitation de données
- Développement d’un outil d’import
- Migration de racktables vers l’outil openDCIM
- Inventaire du matériel physique et virtuel
- Réalisation de documentation technique pour la solution OpenDCIM
- Rackage de serveur de stockage en salle machine

#### Environnement technique
-  Windows (10, Server 2012/2016)
- Linux (Red Hat 6)
- Virtualisation: HyperV Scripting: Python 

