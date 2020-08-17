from django.shortcuts import render


def ongoing_events(request):
    return render(request, 'events/ongoing-events.html')

def past_events(request):
    return render(request, 'events/past-events.html')

def upcoming_events(request):
    return render(request, 'events/upcoming-events.html')


def event_page(request):
    return render(request, 'events/event-page.html')