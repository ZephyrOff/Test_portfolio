
# 🔧 Présentation 2

`Threader` est une classe dérivée de `threading.Thread` qui permet de :

- Lancer une fonction dans un **thread indépendant**
- Passer des arguments (tuple, dict ou unique)
- Récupérer la **valeur de retour** de la fonction
- Vérifier le **code de statut** d’exécution
- Capturer une éventuelle **exception**
- Forcer l’arrêt (**kill**) d’un thread (⚠️ méthode non sécurisée)

# ⚙️ Fonctionnement

### Création d’un Threader

```python
t = Threader(target=ma_fonction, args=(1, 2))
t.start()
t.join()  # attend la fin
```

- `target` → fonction à exécuter
- `args` → paramètres passés à la fonction :
    - `tuple` : `args=(1, 2)` → appel `ma_fonction(1, 2)`
    - `dict` : `args={"x": 1, "y": 2}` → appel `ma_fonction(x=1, y=2)`
    - valeur simple → `args=42` → appel `ma_fonction(42)`
    - `None` → appel sans argument

### Récupération du résultat

```python
def addition(a, b):
    return a + b

t = Threader(target=addition, args=(5, 7))
t.start()
t.join()

t.result()      # 12
t.get_stdout()  # 12 (alias)
```

### Vérification du statut

```python
t.status_code()  # 1 = succès, 0 = échec
```


### Gestion des erreurs

```python
def division(a, b):
    return a / b

t = Threader(target=division, args=(10, 0))  # division par zéro
t.start()
t.join()

t.status_code()  # 0
t.exception     # ZeroDivisionError('division by zero')
```

### Récupération de l’ID du thread

```python
t.get_id()  # Identifiant interne du thread
```


### Kill d’un thread (⚠️ non safe)

```python
import time

def boucle():
    while True:
        print("En cours...")
        time.sleep(1)

t = Threader(target=boucle)
t.start()

time.sleep(3)
t.kill()  # force l’arrêt du thread
```

⚠️ Attention :
- `kill()` utilise `ctypes` et `PyThreadState_SetAsyncExc`, ce qui peut laisser des ressources en état instable.
- À utiliser uniquement si le thread ne peut pas se terminer proprement.


# 🧩 Exemple complet

```python
import time

def job(n, delay=1):
    time.sleep(delay)
    return f"Job {n} terminé après {delay}s"

# Lancement de plusieurs threads
threads = []
for i in range(3):
    t = Threader(target=job, args=(i, i+1))
    t.start()
    threads.append(t)

# Attente + récupération des résultats
for t in threads:
    t.join()
    print(f"[{t.id}] Status: {t.status_code()} | Result: {t.result()} | Exception: {t.exception}")
```