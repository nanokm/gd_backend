from .utils import current_year
from django.utils.text import gettext_lazy as _


def validate_current_year(value):
    if value > current_year():
        raise ValueError(_("Year cannot be greater than current year"))
