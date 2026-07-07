# ✅ TodoFlow

TodoFlow est une application web de gestion de tâches (Todo List) développée avec **Django REST Framework** pour le backend et **HTML, CSS et JavaScript** pour le frontend.

Chaque utilisateur possède son propre espace et ne peut consulter que ses propres tâches grâce à une authentification sécurisée avec JWT.

---

# 📸 Aperçu

Fonctionnalités disponibles :

- Création de compte
- Connexion sécurisée avec JWT
- Déconnexion
- Gestion du profil
- Création d'une tâche
- Modification d'une tâche
- Suppression d'une tâche
- Marquer une tâche comme terminée
- Tableau de bord
- Statistiques
- Interface responsive

---

# 🛠 Technologies utilisées

## Backend

- Python 3
- Django
- Django REST Framework
- Simple JWT
- DRF Spectacular
- Django Filter

## Frontend

- HTML5
- CSS3
- JavaScript (Vanilla)

---

# 📁 Structure du projet

```
TodoFlow/

│
├── accounts/
├── todos/
├── frontend/
│
├── static/
├── templates/
│
├── manage.py
├── requirements.txt
└── README.md
```

---

# ⚙ Installation

## 1. Cloner le projet

```bash
git clone https://github.com/votre-utilisateur/todoflow.git
```

Puis :

```bash
cd todoflow
```

---

## 2. Créer un environnement virtuel

Windows

```bash
python -m venv venv
```

Linux / Mac

```bash
python3 -m venv venv
```

---

## 3. Activer l'environnement virtuel

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

---

## 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## 5. Appliquer les migrations

```bash
python manage.py migrate
```

---

## 6. Créer un super utilisateur

```bash
python manage.py createsuperuser
```

---

## 7. Lancer le serveur

```bash
python manage.py runserver
```

---

L'application sera disponible sur :

```
http://127.0.0.1:8000
```

---

# 🔐 Authentification

Le projet utilise JWT.

Après connexion, deux tokens sont générés :

- Access Token
- Refresh Token

Ils sont enregistrés dans le Local Storage du navigateur.

---

# 📚 Documentation API

Swagger

```
http://127.0.0.1:8000/api/schema/swagger-ui/
```

Redoc

```
http://127.0.0.1:8000/api/schema/redoc/
```

Schéma OpenAPI

```
http://127.0.0.1:8000/api/schema/
```

---

# 📡 Endpoints

## Comptes

POST

```
/api/accounts/register/
```

POST

```
/api/accounts/login/
```

POST

```
/api/accounts/refresh/
```

GET

```
/api/accounts/profile/
```

PUT

```
/api/accounts/profile/
```

PATCH

```
/api/accounts/profile/
```

DELETE

```
/api/accounts/profile/
```

---

## Todo

GET

```
/api/todos/
```

POST

```
/api/todos/
```

GET

```
/api/todos/{id}/
```

PUT

```
/api/todos/{id}/
```

PATCH

```
/api/todos/{id}/
```

DELETE

```
/api/todos/{id}/
```

---

# 🔒 Sécurité

- Authentification JWT
- Permissions par utilisateur
- Chaque utilisateur ne voit que ses propres tâches
- Mots de passe chiffrés par Django