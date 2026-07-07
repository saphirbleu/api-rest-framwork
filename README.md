# ✅ TodoFlow - API REST

**TodoFlow** est une API REST complète pour la gestion de tâches (Todo List) développée avec **Django REST Framework**.

L'application offre une authentification sécurisée par JWT, permettant à chaque utilisateur de gérer ses propres tâches de manière isolée et sécurisée.

---

## 📋 Table des matières

- [Fonctionnalités](#-fonctionnalités)
- [Technologies](#-technologies-utilisées)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Démarrage](#-démarrage)
- [Endpoints API](#-endpoints-api)
- [Authentification](#-authentification)
- [Structure du projet](#-structure-du-projet)

---

## ✨ Fonctionnalités

### Authentification & Comptes
- ✅ Création de compte utilisateur
- ✅ Connexion sécurisée avec JWT
- ✅ Rafraîchissement du token JWT
- ✅ Déconnexion
- ✅ Gestion du profil utilisateur

### Gestion des Tâches
- ✅ Création de tâches
- ✅ Lecture (liste complète et détails)
- ✅ Modification de tâches
- ✅ Suppression de tâches
- ✅ Marquer une tâche comme terminée/en cours
- ✅ Filtrage et recherche avancée
- ✅ Tri par date et statut

### Documentation
- ✅ Documentation interactive Swagger/OpenAPI
- ✅ Schéma API accessible

---

## 🛠 Technologies utilisées

### Backend
- **Python 3** - Langage de programmation
- **Django 6.0.6** - Framework web
- **Django REST Framework 3.17.1** - Framework REST
- **djangorestframework-simplejwt 5.5.1** - Authentification JWT
- **drf-spectacular 0.29.0** - Documentation OpenAPI/Swagger
- **django-filter 25.2** - Filtrage avancé

### Base de données
- **SQLite3** - Base de données (développement)

---

## 📥 Installation

### Prérequis
- Python 3.8+ installé
- pip (gestionnaire de paquets Python)
- Git (optionnel, pour cloner le repo)

### Étapes

1. **Cloner le repository**
   ```bash
   git clone  https://github.com/saphirbleu/api-rest-framwork.git
   cd todo-list-rest-api
   ```

2. **Créer un environnement virtuel**
   ```bash
   python -m venv venv
   ```

3. **Activer l'environnement virtuel**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

5. **Appliquer les migrations**
   ```bash
   python manage.py migrate
   ```

6. **Créer un superutilisateur**
   ```bash
   python manage.py createsuperuser
   ```

---

## ⚙️ Configuration

### Paramètres importants dans `todo_api/settings.py`

```python
# Base de données
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Applications installées
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'drf_spectacular',
    'django_filters',
    'accounts',
    'todos',
]

# Configuration REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# Configuration CORS (si nécessaire)
# Décommenter et configurer pour permettre les requêtes cross-origin
```

---

## 🚀 Démarrage

### Lancer le serveur de développement

```bash
python manage.py runserver
```

Le serveur démarre sur `http://127.0.0.1:8000/`

### Accéder à l'API

- **Swagger/OpenAPI UI:** `http://127.0.0.1:8000/api/schema/swagger-ui/`
- **ReDoc Documentation:** `http://127.0.0.1:8000/api/schema/redoc/`
- **Admin Django:** `http://127.0.0.1:8000/admin/`

---

## 🔗 Endpoints API

### Authentification

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| `POST` | `/api/accounts/register/` | Créer un nouveau compte |
| `POST` | `/api/accounts/login/` | Connexion (obtenir les tokens) |
| `POST` | `/api/accounts/token/refresh/` | Rafraîchir le token d'accès |
| `POST` | `/api/accounts/logout/` | Déconnexion |
| `GET` | `/api/accounts/profile/` | Récupérer le profil utilisateur |
| `PUT` | `/api/accounts/profile/` | Mettre à jour le profil |

### Tâches (Todos)

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| `GET` | `/api/todos/` | Lister toutes les tâches de l'utilisateur |
| `POST` | `/api/todos/` | Créer une nouvelle tâche |
| `GET` | `/api/todos/{id}/` | Récupérer les détails d'une tâche |
| `PUT` | `/api/todos/{id}/` | Mettre à jour une tâche |
| `PATCH` | `/api/todos/{id}/` | Mise à jour partielle d'une tâche |
| `DELETE` | `/api/todos/{id}/` | Supprimer une tâche |

### Filtrage & Recherche

```bash
# Filtrer par statut
GET /api/todos/?status=pending

# Filtrer par date
GET /api/todos/?created_at__gte=2024-01-01

# Recherche par titre
GET /api/todos/?search=mon+titre

# Pagination
GET /api/todos/?page=2
```

---

## 🔐 Authentification

L'API utilise **JWT (JSON Web Token)** pour l'authentification.

### Flux d'authentification

1. **Enregistrement**
   ```bash
   POST /api/accounts/register/
   Content-Type: application/json

   {
     "username": "john_doe",
     "email": "john@example.com",
     "password": "secure_password123"
   }
   ```

2. **Connexion**
   ```bash
   POST /api/accounts/login/
   Content-Type: application/json

   {
     "username": "john_doe",
     "password": "secure_password123"
   }

   Response:
   {
     "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
   }
   ```

3. **Utiliser le token**
   ```bash
   GET /api/todos/
   Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...
   ```

4. **Rafraîchir le token**
   ```bash
   POST /api/accounts/token/refresh/
   Content-Type: application/json

   {
     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
   }
   ```

---

## 📁 Structure du projet

```
todo-list-rest-api/
├── accounts/                    # App de gestion des comptes
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py               # Configuration admin Django
│   ├── apps.py
│   ├── models.py              # Modèles utilisateur
│   ├── serializers.py         # Sérialiseurs pour API
│   ├── tests.py
│   ├── urls.py                # Routes de l'app accounts
│   └── views.py               # Vues/Contrôleurs
│
├── todos/                       # App de gestion des tâches
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   └── 0002_alter_todo_options.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py              # Modèle Todo
│   ├── permissions.py         # Permissions personnalisées
│   ├── serializers.py         # Sérialiseurs Todo
│   ├── tests.py
│   ├── urls.py                # Routes de l'app todos
│   └── views.py               # Vues/Contrôleurs Todo
│
├── todo_api/                    # Config principale Django
│   ├── __init__.py
│   ├── settings.py            # Configuration Django
│   ├── urls.py                # Routes principales
│   ├── asgi.py                # Config ASGI
│   └── wsgi.py                # Config WSGI
│
├── db.sqlite3                   # Base de données
├── manage.py                    # Script de gestion Django
├── requirements.txt             # Dépendances Python
└── README.md                    # Ce fichier
```

---

## 🔒 Sécurité

- ✅ Authentification JWT sécurisée
- ✅ Permissions par utilisateur (chaque utilisateur n'accède qu'à ses tâches)
- ✅ Passwords chiffrés (hash PBKDF2 de Django)
- ✅ Tokens JWT avec expiration
- ✅ Protection CSRF activée

### Bonnes pratiques appliquées
- Séparation des responsabilités (models, views, serializers)
- Permissions personnalisées (`permissions.py`)
- Validation des données avec DRF Serializers
- Documentation OpenAPI automatique

---

## 🧪 Tests

Exécuter les tests unitaires :

```bash
python manage.py test
```

Avec couverture verbose :

```bash
python manage.py test -v 2
```

---

## 📝 Exemples de requêtes

### 1. Créer un compte

```bash
curl -X POST http://127.0.0.1:8000/api/accounts/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "alice",
    "email": "alice@example.com",
    "password": "SecurePass123!"
  }'
```

### 2. Se connecter

```bash
curl -X POST http://127.0.0.1:8000/api/accounts/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "alice",
    "password": "SecurePass123!"
  }'
```

**Réponse:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### 3. Créer une tâche

```bash
curl -X POST http://127.0.0.1:8000/api/todos/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..." \
  -d '{
    "title": "Faire les courses",
    "description": "Acheter du lait et du pain",
    "priority": "high"
  }'
```

### 4. Lister les tâches

```bash
curl -X GET http://127.0.0.1:8000/api/todos/ \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
```

---

## 🐛 Dépannage

### Le serveur ne démarre pas
```bash
# Vérifier si le port 8000 est libre
python manage.py runserver 8000

# Ou vérifier les migrations
python manage.py migrate
python manage.py makemigrations
```

### Erreur d'authentification JWT
```bash
# Vérifier que le token n'est pas expiré
# Rafraîchir le token si nécessaire
POST /api/accounts/token/refresh/
```

### Erreur de base de données
```bash
# Supprimer et réinitialiser la base
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

---

## 📚 Ressources

- [Documentation Django](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [djangorestframework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/)
- [drf-spectacular](https://drf-spectacular.readthedocs.io/)

---

## 📄 Licence

Projet open source - Libre d'utilisation.

---

## 👨‍💻 Auteur

Développé avec ❤️ par **Codex Nova** etudiant Licence 3

Questions? Contactez-nous ou ouvrez une issue!

---

**Dernière mise à jour:** 2026-07-07