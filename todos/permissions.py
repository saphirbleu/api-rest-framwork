from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Autorise uniquement le propriétaire d'une tâche
    à la modifier ou la supprimer.
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user