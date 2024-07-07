from datetime import datetime
from django.utils.timezone import now
from django.db.models import Q

from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from .décorators import group_required
from .forms import RaceResultForm, ContactUsForm, SendEmailForm
from .models import Race, Athlete, RaceResult
from django.contrib.auth.decorators import login_required, permission_required


@login_required
# @group_required('resultsmanagers')
def manage_results(request):
    results = RaceResult.objects.all()
    return render(request, 'races/manage_results.html', {'results': results})


@login_required
@group_required('resultsmanagers')
def edit_result(request, result_id):
    result = get_object_or_404(RaceResult, id=result_id)

    # Take a look at « request.user»  »
    user = request.user
    print(user.get_all_permissions())
    print(user.has_perm('races.add_raceresult'))
    print(user.has_perm('races.change_raceresult'))

    # Take a look at « request.method » and « request.POST »
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)
    print('Les données login : ', request.user)
    print('Les données Media : ', request.FILES)

    if request.method == "POST":
        form = RaceResultForm(request.POST, instance=result)
        if form.is_valid():
            form.save()
            return redirect('races_list')

    else:
        form = RaceResultForm(instance=result)
    return render(request, 'races/edit_result.html', {'form': form})


def races_list(request):
    races = Race.objects.all()
    return render(request, 'races/races_list.html', {'races': races})


def race_detail(request, race_id):
    race = get_object_or_404(Race, id=race_id)
    # filtre les résultats de la course en fonction de la course donnée, et les trie par position du premier au dernier
    race_results = RaceResult.objects.filter(race=race).order_by('position')
    context = {'race': race, 'race_results': race_results}
    return render(request, 'races/race_detail.html', context)


def athlete_list(request):
    # athletes = Athlete.objects.all()
    # Ordering the queryset by a field, e.g., last_name before paginator
    athletes = Athlete.objects.all().order_by('last_name')

    paginator = Paginator(athletes, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        # 'athletes': athletes,
        'page_obj': page_obj,
    }
    return render(request, 'races/athlete_list.html', context)


def athlete_detail(request, athlete_id):
    athlete = get_object_or_404(Athlete, id=athlete_id)
    # filtre les résultats de la course en fonction d'un athlete donné, puis les trie par date de debut de la course
    # du premier au dernier
    race_results = RaceResult.objects.filter(athlete=athlete).order_by('race__event_start')
    return render(request, 'races/athlete_detail.html', {'athlete': athlete, 'race_results': race_results})


def send_email_view(request):
    """
        The event organizer wants to send a message to all athletes who competed in the event name
        Submit all athletes Using field searches (__) to navigate to raceresult, then race, and name
        Filters athletes based on the results of the race named Paris Marathon
    """
    # Take a look at « request.method » and « request.POST »
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)

    if request.method == 'POST':
        form = SendEmailForm(request.POST)

        if form.is_valid():
            race = form.cleaned_data['race']
            # Fetch all athletes who participated in the selected race
            # Filters athletes based on the results of the race named Paris Marathon,
            # Filter the athletes who competed in the selected races
            athletes = Athlete.objects.filter(raceresult__race=race)

            # Create the email content
            subject = f'Results for {race.name},Thank you for participating!'
            message = (f'Dear Athlete,\n\nHere are the results for the race {race.name}'
                       f'\n\nWe appreciate your participation in our event.\n\nBest regards,\nAthletics Team')
            from_email = "admin@athletics.xyz"
            recipient_list = [athlete.email for athlete in athletes]  # Ensure your Athlete model has an email field
            # recipient_list = ['athlete@exemple.com']  # Ensure your Athlete model has an email field
            # Send the email
            send_mail(subject, message, from_email, recipient_list)

            # Debug
            # Show email details in console
            print(f"De : {from_email}")
            print(f"À : {recipient_list[0]}")
            print(f"Date : {now().strftime('%a, %d %b %Y %H:%M:%S %z')}")
            print(f"ID du message : <{now().strftime('%s%f')}@yourdomain.com>")

            return render(request, 'races/email_sent_to_athlete.html', {'athletes': athletes, 'race': race})
    else:
        form = SendEmailForm()

    return render(request, 'races/send_email.html', {'form': form})


def contact(request):
    # Take a look at « request.method » and « request.POST »
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)

    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via Athletics Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@athletics.xyz'],
            )
            # return redirect('email-sent')
            return render(request, 'races/email_sent.html')

    else:
        form = ContactUsForm()

    context = {'form': form}
    return render(request, 'races/contact.html', context)


# for inspiration
def __orm__(request):
    athletes = Athlete.objects.filter(
        # la position dans le résultat de la course (RaceResult) doit être inférieure ou égale à 3,
        # donc les athlètes ont fini la course à la 3e place ou en dessous (1ère, 2ème ou 3ème place).
        raceresult__position__lte=3,
        # AND
        # DOB doit être supérieure ou égale au 1er janvier 2000, donc les athlètes sont nés en 2000 ou après.
        date_of_birth__gte=datetime(day=1, month=1, year=2000))

    # Vous organisez une course exclusivement sur invitation, ouverte aux athlètes :
    # Filtre les athlètes en fonction la position des résultats, soit (la position des résultats de la course nommée de
    # type "Marathon"
    Athlete.objects.filter(
        Q(raceresult__position=1) | Q(raceresult__position__lte=3, raceresult__race__name='Marathon'))

    context = {
        'athletes': athletes,
    }
    return render(request, 'races/msg_sent.html', context)
