from apps.user.models import GDUser


class IsTriageAdminUser(object):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.type == GDUser.AccountType.TRIAGE_ADMIN
