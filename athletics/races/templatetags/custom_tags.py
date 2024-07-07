import datetime
from django.template import Library
from races.models import RaceResult

register = Library()


@register.simple_tag
def times_competed(athlete, race):
    """
        Cette fonction utilise RaceResult.objects.filter(athlete=athlete, race=race).count()
        pour compter le nombre de fois qu'un athlète a concouru dans une course spécifique.
        La méthode count() renvoyer le nombre d'instances correspondant aux critères donnés.
    """

    # {%times_competed result.athlete result.race %}
    return RaceResult.objects.filter(athlete=athlete, race=race).count()

    # {%times_competed result.athlete.last_name result.race.name %}
    # return RaceResult.objects.filter(athlete__last_name=athlete, race__name=race).count()


