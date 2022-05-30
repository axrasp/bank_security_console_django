import django
from django.shortcuts import render

from datacenter.models import Visit, get_visit_duration


def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at__isnull=True)
    active_visits_listed = []
    for visit in active_visits:
        local_enter_time = django.utils.timezone.localtime(visit.entered_at)
        duration = get_visit_duration(visit)
        duration_formatted = f'{duration.seconds // 3600} часов ' \
                             f'{(duration.seconds % 3600) // 60} минут'
        active_visit = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': str(local_enter_time),
            'duration': duration_formatted
        }
        active_visits_listed.append(active_visit)

    context = {
        'non_closed_visits': active_visits_listed,
    }
    return render(request, 'storage_information.html', context)
