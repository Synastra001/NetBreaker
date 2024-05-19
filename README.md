# NetBreaker

Ce projet est un outil simple de brute force pour tester la connexion à un réseau WiFi en essayant différentes combinaisons de mots de passe. Il utilise la bibliothèque `pywifi` pour gérer les connexions WiFi en Python.

## Fonctionnalités

- **Connexion WiFi** : Tente de se connecter à un réseau WiFi donné avec un mot de passe spécifié.
- **Génération de mots de passe** : Génère toutes les combinaisons possibles de mots de passe jusqu'à une longueur maximale définie.
- **Essai de connexion** : Boucle à travers tous les mots de passe générés pour tenter de se connecter au réseau WiFi spécifié.

## Prérequis

- Python 3.x
- Bibliothèque `pywifi`

Vous pouvez installer la bibliothèque `pywifi` en utilisant pip :

```bash
pip install pywifi
```

## Utilisation

1. Clonez ce dépôt GitHub :

```bash
git clone https://github.com/Synastra01/NetBreaker.git
```

2. Modifiez le nom du réseau SSID dans la fonction `main` :

```python
ssid = "NOM WIFI"
```

3. Exécutez le script :

```bash
python netbreaker.py
```

Le script va générer des mots de passe et essayer de se connecter au réseau WiFi spécifié. Il affichera un message indiquant si la connexion a réussi ou échoué pour chaque mot de passe.

## Avertissement

Cet outil est destiné à des fins éducatives uniquement. L'utilisation de cet outil pour accéder à des réseaux WiFi sans autorisation est illégale et contraire à l'éthique. Assurez-vous d'avoir la permission explicite du propriétaire du réseau WiFi avant d'utiliser cet outil pour tenter de se connecter à un réseau.
