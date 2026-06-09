## Présentation

Construction d'un cluster Hashicorp Vault pour le stockage de secret et l'accès depuis des solutions d'automatisations comme Ansible.

## Description globale

L'objectif était de mettre en place une solution de secret management pour permettre à nos solutions d'automatisations (Ansible, Terraform...) de récupérer les secrets nécessaires pour le bon déroulement de leur processus.
Pour cela, nous avons mis en place un cluster Hashicorp Vault avec un stockage Raft sur 5 noeuds.
