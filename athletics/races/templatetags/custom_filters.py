from django import template

register = template.Library()


@register.filter
def time_display(time):
    return time.strftime("%d %b %Y %H:%M")


# {{ result|ordinal }}
@register.filter
def ordinal(race_results):
    """
        Attend un RaceResult objet en entrée. Il accède à l'attribut position du RaceResult objet directement.
        Il est utilisé avec RaceResult objets directement dans le modèle, ce qui le rend étroitement couplé au RaceResult structure du modèle.
        Utilisez-le si vous avez toujours RaceResult objets et que vous souhaitez associer étroitement le filtre à la structure du modèle.
    """
    position = race_results.position
    if position == 1:
        return f'{position}er'
    return f'{position}e'


# {{ result.position|ordinal }}
@register.filter
def ordinal(position):
    """
        Attend la position valeur directement, plutôt qu'un RaceResult Il tente de convertir l'entrée en un entier.
        Si la conversion réussit et que le poste est 1, ça revient "1er". Pour les autres positions, il renvoie la position suivie de "e".
        Si la conversion échoue (en raison d'un ValueError ou TypeError), il renvoie l'entrée d'origine
        Utilisez-le si vous souhaitez plus de flexibilité et un découplage de la structure du modèle.
        Vous pouvez appliquer ce filtre à n'importe quel entier ou chaîne représentant une position.pas seulement dans le contexte de RaceResult Objets.
 """
    try:
        position = int(position)
        if position == 1:
            return f'{position}er'
        return f'{position}e'
    except (ValueError, TypeError):
        return position

