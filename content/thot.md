## Présentation

Thot est une application web qui permet de créer de façon dynamique des tableaux de données.

## Description globale

A partir d'une matrice, l'application va récupérer des données dans une BDD et les afficher sous forme de tableau.
Grâce à cela, il est possible de créer des dashboard dynamiques qui vont changer de comportement en fonction des données récupérées.

![[media/Thot_1.png]]

L'ensemble de l'application est customisable à partir de fichier yaml.
>- Un fichier settings.yaml permet de configurer l'ensemble de l'application.
>- Un fichier de matrice par dashboard permet de définir la structure de l'affichage.
	Des options permettant de créer des boutons de filtre est également disponible pour rajouter des options de customisation à l'utilisateur


L'ensemble des dashboard sont volatiles. Ils sont générés à la volée lorsque l'utilisateur accède à la page et n'est sauvegardé nulle part.

Par défaut, le système supporte le multilingue avec traduction automatique grâce à une ressource locale.

## Authentification/Sécurité

La configuration propose 2 possibilités:
>- Dashboard accessible sans connexion
>- Authentification obligatoire pour accéder au dashboard

Lorsque l'authentification est nécessaire, l'application propose plusieurs méthodes d'authentification. 
Soit en login/password, dans ce cas, il faudra créer des comptes depuis le back-office. 
Soit par SSO, dans ce cas, il faudra réaliser la configuration SSO depuis le fichier yaml.

Pour garantir la sécurité de l'application, plusieurs mécanismes sont mis en place. 
L'ensemble des contrôles d'accès sont réalisés côté serveur, déjà en contrôlant la provenance du client, puis en stockant l'ensemble de ces permissions dans une mémoire volatile qui sera révoquée lors du redémarrage de l'application.
A l'image d'un Fail2Ban, l'application va également contrôler en continu l'activité des clients sur le site pour analyser les potentielles actions suspectes. En fonction des paramètres définis, si un client réalise des requêtes non autorisées, il sera alors banni pendant un temps donné.
En cas d'erreur, un administrateur pourra tout de même débannir celui-ci sans attendre la fin du temps défini.

## Back-office

Comme évoqué dans la partie précédente, le back-office permet aux administrateurs de créer de nouveaux utilisateurs locaux. Il pourra également les ajouter dans des groupes pour simplifier la gestion des accès et des permissions.
C'est également sur cette interface qu'on pourra retrouver la liste des clients qui ont été bannis pour activité suspecte.

Il sera également possible de retrouver l'ensemble des tables de la base de données pour permettre une visualisation des données et la possibilité de les modifier sans passer par un IDE externe.

Si on souhaite des options supplémentaires, le back-office prend en charge la création de plug-in. Chacun peut facilement créer de nouvelles vues en quelques minutes pour les intégrer dans le back-office.