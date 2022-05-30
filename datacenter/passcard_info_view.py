from django.shortcuts import render

from datacenter.models import Passcard, Visit, is_visit_long, get_visit_duration


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)[0]
    current_passcard_visits = Visit.objects.filter(passcard=passcard)
    current_passcard_visits_listed = []
    for visit in current_passcard_visits:
        duration = get_visit_duration(visit)
        current_visit = {
            'entered_at': visit.entered_at,
            'duration': duration,
            'is_strange': is_visit_long(visit)
        }
        current_passcard_visits_listed.append(current_visit)
    context = {
        'passcard': passcard,
        'this_passcard_visits': current_passcard_visits_listed
    }
    return render(request, 'passcard_info.html', context)
