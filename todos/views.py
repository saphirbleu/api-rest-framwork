from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiExample,
    OpenApiParameter,
)

from .models import Todo
from .serializers import TodoSerializer
from .permissions import IsOwner
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

@extend_schema_view(
    list=extend_schema(
        tags=["Todos"],
        summary="Lister mes tâches",
        description="""
Retourne uniquement les tâches appartenant à l'utilisateur authentifié.

### Fonctionnalités disponibles
- Pagination
- Recherche
- Filtrage
- Tri
""",
        parameters=[
            OpenApiParameter(
                name="search",
                description="Recherche dans le titre ou la description",
                required=False,
                type=str,
            ),
            OpenApiParameter(
                name="completed",
                description="Filtrer par statut (true ou false)",
                required=False,
                type=bool,
            ),
            OpenApiParameter(
                name="ordering",
                description="Trier par created_at, updated_at ou title",
                required=False,
                type=str,
            ),
        ],
    ),

    create=extend_schema(
        tags=["Todos"],
        summary="Créer une tâche",
        description="Ajoute une nouvelle tâche à la liste de l'utilisateur connecté.",

        examples=[
            OpenApiExample(
                "Créer une tâche",
                value={
                    "title": "Terminer le projet Django",
                    "description": "Finaliser la partie Todo",
                    "completed": False
                },
                request_only=True,
            )
        ],
    ),

    retrieve=extend_schema(
        tags=["Todos"],
        summary="Afficher une tâche",
        description="Retourne les détails d'une tâche."
    ),

    update=extend_schema(
        tags=["Todos"],
        summary="Modifier complètement une tâche"
    ),

    partial_update=extend_schema(
        tags=["Todos"],
        summary="Modifier partiellement une tâche"
    ),

    destroy=extend_schema(
        tags=["Todos"],
        summary="Supprimer une tâche"
    ),
)
class TodoViewSet(viewsets.ModelViewSet):

    queryset = Todo.objects.all()

    serializer_class = TodoSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    search_fields = [
        "title",
        "description",
    ]

    filterset_fields = [
        "completed",
    ]

    ordering_fields = [
        "created_at",
        "updated_at",
        "title",
    ]

    def get_queryset(self):
        return Todo.objects.filter(
            owner=self.request.user
        )

    def get_permissions(self):

        if self.action in [
            "update",
            "partial_update",
            "destroy",
        ]:
            return [
                IsAuthenticated(),
                IsOwner(),
            ]

        return [
            IsAuthenticated(),
        ]

    def perform_create(self, serializer):

        serializer.save(
            owner=self.request.user
        )
    @extend_schema(
        tags=["Todos"],
        summary="Changer le statut d'une tâche",
        description="Inverse automatiquement le statut d'une tâche (terminée ↔ non terminée)."
        )
            
    @action(detail=True, methods=["post"])
    def toggle(self, request, pk=None):
        todo = self.get_object()

        todo.completed = not todo.completed
        todo.save()

        serializer = self.get_serializer(todo)

        return Response(serializer.data, status=status.HTTP_200_OK)