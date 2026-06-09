![[media/iris_logo.png]]

## Présentation

Outil permettant la création et l'exploitation d'API à partir de script Python.
Chaque script qui contient un endpoint sera convertis en API utilisable dans Iris.

## Description globale

Au démarrage, l'application provisionne un répertoire **fabric**. 
Ce répertoire permettra de stocker l'ensemble des scripts qui pourront être utilisés comme une API.
Iris va lire l'ensemble des scripts présents dans le répertoire fabric et créer des entrées d'API à partir des fonctions contenant le décorateur **entrypoint**.

![[media/Iris_1.png]]

### Définition des API

Sur l'administration, nous pourrons ainsi retrouver l'ensemble de nos APIs disponibles.

![[media/Iris_2.png]]

Il sera alors possible d'éditer les informations du script comme la description ou la documentation spécifique qui sera affichée sur le frontend.
On pourra également définir des variables d'environnements interne qui pourront être utilisées dans les scripts.
Les API pourront être définis soit en public (accessible sans restrictions), soit en private (nécessitant une authentification par token).
Pour finir, chaque script pourront être désactivé (en le passant Offline) pour bloquer son accès.

### Définition des access token

![[media/Iris_3.png]]

Comme dit au dessus, les API private doivent obligatoirement être authentifié avec un token.
Dans l'administration, il sera possible de créer de nouveaux tokens et de leur définir des accès (soit un accès à l'ensemble des API, soit un accès restreint à certaines briques).
Comme pour les API Script, il sera possible de définir des variables d'environnements interne au niveau du token qui sera exposé au script.

### Système de logs interne

Pour simplifier l'administration et la gestion des scripts, l'ensemble des logs sont disponibles dans la même interface.

#### System logs

Permet de voir les logs qui concernent le fonctionnement de l'application comme le scan des scripts, le système de protection...

![[media/Iris_4.png]]

#### Web logs

Concerne les logs liés au appel des différentes routes de l'application

![[media/Iris_10.png]]

#### API Logs

Concerne les logs d'appels des différentes API, avec la possibilité de voir les requêtes, les statuts et les éventuels retours de code.

![[media/Iris_5.png]]

#### Socket Logs

Concerne les logs direct du moteur web (Flask)

![[media/Iris_6.png]]

### Système de protection

Pour réduire la surface d'attaque, un système de protection est mis en place. Il analyse les différentes requêtes et ajoute des flags lorsqu'une erreur est identifiée. Lorsque l'utilisateur dépasse X flags, il est bannis pendant un temps donnés.

![[media/Iris_7.png]]

### Frontend utilisateur

Pour faciliter l'accessibilité des utilisateurs, l'application va mettre en place une page d'accueil permettant de voir les API disponibles (les privates accessibles uniquement lorsqu'on est connecté).


![[media/Iris_8.png]]

En cliquant sur l'une d'elle, il sera possible de voir l'url d'accès, les paramètres nécessaires et éventuellement la documentation fournies.


![[media/Iris_9.png]]
