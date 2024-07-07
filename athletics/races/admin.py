from django.contrib import admin
from .models import Race, Athlete, RaceResult

from django.core.mail import send_mail


def send_email_to_athletes(modeladmin, request, queryset):
    """
    L’organisateur des événements veut envoyer un message à tous les athlètes qui ont concouru dans l’événement name
    Envoyer tous les athlètes En utilisant les recherches de champ (__) pour accéder à raceresult, puis à race,
    et à name.
    Filtre les athlètes en fonction des résultats de la course nommée Marathon de Paris
    """
    # Fetch all athletes who participated in the selected race
    # Filters athletes based on the results of the race named Paris Marathon,
    # Filter the athletes who competed in the selected races
    athletes = Athlete.objects.filter(raceresult__race__in=queryset)

    # Create the email content
    subject = f'Thank you for participating!'
    message = (f'Dear Athlete,\n\nHere are the results for the race ' #{race.name}'
               f'\n\nWe appreciate your participation in our event.\n\nBest regards,\nAthletics Team')
    from_email = "admin@athletics.xyz"
    # recipient_list = [athlete.email for athlete in athletes]  # Ensure your Athlete model has an email field
    # Debug
    recipient_list = ['athlete@exemple.com']  # Ensure your Athlete model has an email field
    # Send the email
    send_mail(subject, message, from_email, recipient_list)

    modeladmin.message_user(request, "Emails have been sent to the selected athletes.")

    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)


send_email_to_athletes.short_description = "Send email to athletes"


class RaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_start')
    list_filter = ("name",)
    list_editable = ("event_start",)
    actions = [send_email_to_athletes]


class AthleteAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth')
    search_fields = ['first_name', 'last_name']
    list_editable = ("date_of_birth",)


class RaceResultAdmin(admin.ModelAdmin):
    list_display = ('athlete', 'race', 'position')
    search_fields = ['athlete', 'race']
    list_editable = ("position",)


admin.site.register(Race, RaceAdmin)
admin.site.register(Athlete, AthleteAdmin)
admin.site.register(RaceResult, RaceResultAdmin)
