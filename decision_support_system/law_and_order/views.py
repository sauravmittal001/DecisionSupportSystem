from django.http import Http404
# from django.template import loader
from django.shortcuts import render

from .models import EventTable, Rally, Riots, VipLeader, CriticalRoute


def index(request):
    events_table = EventTable.objects.all()
    # template = loader.get_template('law_and_order/index.html')
    context = {'events_table': events_table}
    """
    html = ''
    for event in events_table:
        url = '/law_and_order/' + str(event.id) + '/'
        html += '<a href="' + url + '">' + event.name + '</a>' + '&nbsp;' + event.time_of_event + '</a>' + '&nbsp;' 
        + event.location + '</a>' + '&nbsp;' + event.date_of_event + '</a><br>'

    """
    # return HttpResponse(template.render(context, request))
    return render(request, 'law_and_order/index.html', context=context)


def detail(request, id):
    try:
        events_table = EventTable.objects.all()
    except EventTable.DoesNotExist:
        raise Http404("Event does not exist")
    # return HttpResponse("<h2> details for event_id:" + str(id) + "</h2>")
    return render(request, 'law_and_order/details.html', {'events_table': events_table})


def apiTest(request):
    print(request)
    return request


def home(request):
    return render(request, 'law_and_order/home.html')


def rally(request):
    rally_table = Rally.objects.all()
    context = {'rally_table': rally_table}
    return render(request, 'law_and_order/rally.html', context=context)


def riots(request):
    riots_table = Riots.objects.all()
    context = {'riots_table': riots_table}
    return render(request, 'law_and_order/riots.html', context=context)


def vip_leader(request):
    vip_leader_table = VipLeader.objects.all()
    context = {'vip_leader_table': vip_leader_table}
    return render(request, 'law_and_order/vip_leader.html', context=context)


def critical_route(request):
    critical_route_table = CriticalRoute.objects.all()
    context = {'critical_route_table': critical_route_table}
    return render(request, 'law_and_order/critical_route.html', context=context)


def events_table(request):
    events_table = EventTable.objects.all()
    context = {'events_table': events_table}
    return render(request, 'law_and_order/events_table.html', context=context)
