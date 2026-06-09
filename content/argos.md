## Présentation

Outil permettant la mise à jour automatisée des packages Linux (RHEL) sur l'ensemble d'un parc de serveurs.
Avant chaque opération, un downtime de la supervision et un snapshot du serveur seront effectués.
Pour les serveurs de préproduction et production, une approbation en amont sera nécessaire pour valider le déclenchement des mises à jour planifiées.
Après chaque opération, un contrôle de l'état sera effectué pour garantir le bon rétablissement du service, et pourra réaliser un rollback en cas de problème identifié.
L'objectif est de laisser l'outil en charge des tâches de mise à jour de nos systèmes et de le laisser nous alerter en cas de problème.
L'administrateur aura juste à définir les plages de mises à jour pour ces serveurs.

## Description globale

L'application se décompose en 5 gros composants. 3 composants indépendants (ArgosCore, ArgosServer et BeeKeeper) et 2 composants interconnectés au reste (Bee et Mitra).

### ArgosCore

Ce composant va se charger de la synchronisation des données, de la vérification des planifications et du déclenchement des threads de mise à jour (Bee).
Au démarrage, ArgosCore va initialiser ces paramètres et initialiser les connexions avec les composants externes (Vcenter, Check_MK, Suma). C'est grâce à ces connexions que les Bee vont effectuer des actions pendant leur procédure de mise à jour.
Le système va également contrôler que chaque serveur a des mises à jour planifiées, sinon il enverra une notification par mail avec la liste des projets concernés.

![[media/Argos_1.png]]


### ArgosServer

Il va se charger de faire le lien entre l'application et le client d'administration (qui sera utilisé par les administrateurs pour approuver les mises à jour et contrôler le comportement de l'application). C'est l'unique lien entre l'application et l'administrateur.


![[media/Argos_2.png]]

### BeeKeeper

Ce composant est un des plus importants. C'est lui qui va contrôler que les différents services sont opérationnels et que les différents thread de mise à jour (Bee) ne sont pas en échec ou dans un état anormal.
Si un service est défectueux, il le redémarre automatiquement.
Si un Bee est en échec ou dans un état anormal, il se chargera de l'arrêter.
Il a également un système de redémarrage automatique lorsque lui-même tombe en échec.

![[media/Argos_3.png]]
### Bee

Chaque Bee correspond à un processus qui est dédié à la mise à jour d'un serveur spécifique et qui se charge de l'ensemble des étapes de mise à jour (pre-process, process et post-process).
En pre-process, il va faire un snapshot de la VM, downtime l'host sur la supervision et sauvegarder l'état des services de la VM sur la supervision.
En process, il va lister l'ensemble des packages à mettre à jour, exclure les packages critiques (comme PHP ou Mysql) et lancer la procédure de mise à jour.
En post-process, il commence par faire un reboot de la VM si nécessaire. Ensuite, il va réaliser différents contrôles pour s'assurer que la mise à jour n'a pas détériosé le fonctionnement de l'application sur le serveur.
Si un disfonctionnement est détecté, il va extraire les logs nécessaire et restaurer le snapshot de la VM.
Si l'application est toujours fonctionnel, il va simplement supprimer le snapshot et enlever le downtime sur la supervision.

### Mitra

Mitra est un système interne à Argos qui permet de faire des tests fonctionnels sur des serveurs.
Le système va réaliser des tests programmés de façon séquentiel et nous retourner la liste des erreurs éventuelles.
Le système se base sur un fichier de définition, qui va décrire les serveurs à prendre en compte et les tests à effectuer.
Dans les tests, on retrouve par exemple:
**test_http**: va permettre de réaliser des tests sur des sites web pour vérifier leur fonctionnement.
**test_connection**: va permettre de tester l'accès à des ports spécifiques
**service_status**: va permettre de vérifier l'état d'un service sur un serveur
**mountpoint**: va permettre de contrôler qu'un point de montage est fonctionnel
**remote_command**: va permettre de lancer des commandes et de contrôler leur retour. (Attention, le système va contrôler également que la commande lancée n'est pas dangereuse pour le serveur cible.)
**remote_script**: va permettre de lancer des scripts et de contrôler leur retour. (Attention, le système va contrôler que le script n'est pas dangereux pour le serveur cible)
**conditional**: va permettre de définir des conditions à remplir pour lancer les tests.


## Processus de mise à jour

Argos va respecter un process bien précis avec de multiples contrôles pour garantir le bon fonctionnement de nos applications. L'action se déroule en 3 phases: pre-process, process et post-process

#### pre-process

Au cours de cette phase, plusieurs étapes vont être réalisées pour préparer le serveur:
- Le système va commencer par faire un test d'état du serveur. Si celui-ci ne respecte pas les exigences demandées ou si une application ne fonctionne pas, il considère que le système est non conforme pour une mise à jour.
- Il va récupérer l'état de la supervision à l'instant T et mettre en downtime les services pour éviter de recevoir des alertes dues à la mise à jour.
- Il va réaliser un snapshot de la VM pour assurer un rollback rapide.

#### process

Durant cette phase, il va simplement lancer les mises à jour sur le serveur.

#### post-process

La phase de post-process est la plus importante. C'est elle qui va garantir que le service est rétabli:
- Le système va contrôler si un redémarrage est nécessaire (en effet, certains packages comme le kernel nécessitent un redémarrage du serveur)
- Test applicatif: Le système va réaliser les mêmes tests que ceux réalisés durant la phase de pre-process pour garantir qu'aucun service n'a été altéré ou compromis durant la mise à jour. En cas d'erreur, le système va dumper les logs souhaités et initier le rollback pour rétablir le service.
- Contrôle de la supervision: Il va récupérer l'état de la supervision et le comparer à l'état sauvegardé durant la phase de pre-process. Si un service a changé, le système va dumper les logs souhaités et initier le rollback pour rétablir le service.
- Si l'ensemble du système est conforme, l'application va supprimer le snapshot et le downtime sur la supervision.

## Système de contrôle inter-serveur

Dans le cas d'un parc informatique avec une nomenclature stricte, le système va réussir à détecter les différentes applications du parc et les différents environnements de chaque application pour y appliquer des dépendances entre eux.

Grâce à cela, le système va pouvoir s'assurer que l'ensemble des environnements sont mis à jour dans l'ordre et qu'il n'y a pas eu de problème lors de la mise à jour des autres environnements.

Par exemple, si nous avons une application qui va 3 environnements Test, PreProd, Prod.
Si le système va commencer les mises à jour sur la Test, si tout se passe bien, il considère qu'il peut passer à la suite. Sinon il bloque les mises à jour des autres environnements. Donc si une erreur a été détectée durant la mise à jour de la PreProd par exemple, il va bloquer la mise à jour de la Prod jusqu'à ce qu'un admin valide la résolution du problème.

Maintenant, prenons un second cas, imaginons qu'un admin se trompe lors de ces planifications et veut déclencher la PreProd avant la Test. Le système va également bloquer parce qu'il ne voit pas de mise à jour sur l'environnement de Test. 