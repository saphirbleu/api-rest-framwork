from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import RegisterSerializer, ProfileSerializer

from drf_spectacular.utils import extend_schema, OpenApiExample

@extend_schema(
    tags=["Authentification"],
    summary="Créer un compte",
    description="""
        Permet de créer un nouveau compte utilisateur.

        ### Authentification
        Aucune authentification n'est requise.
        Aucun token n'est nécessaire.

        ### Informations
        - Le nom d'utilisateur doit être unique.
        - L'adresse email est utilisée pour identifier le compte.
        - Le mot de passe est automatiquement chiffré avant d'être enregistré.
        """,
    examples=[
        OpenApiExample(
            "Exemple de requête",
            value={
                "username": "gradi",
                "email": "gradi@email.com",
                "password": "MonMotDePasse123"
            },
            request_only=True,
        ),
        OpenApiExample(
            "Exemple de réponse",
            value={
                "id": 1,
                "username": "gradi",
                "email": "gradi@email.com"
            },
            response_only=True,
        ),
    ],
)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

@extend_schema(
    summary="Mon profil",
    description="""
    Consulter, modifier ou supprimer
    le profil de l'utilisateur connecté.
    """
)

class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user