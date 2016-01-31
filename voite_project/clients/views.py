from django.shortcuts import render
from django.http import HttpResponse
from clients.models import Client
from clients.tasks import create_list_clients_xlsx
from django.contrib.auth.decorators import login_required
from django.db import transaction

log_url = 'admin:login'


@login_required(login_url=log_url)
def index(request):
    return render(request, "index.html")


@login_required(login_url=log_url)
def view_photo(request):
    if request.GET:
        pk = request.GET["pk"]
        if request.GET["voite"] == u"down":
            voite = -1
        else:
            voite = 1
        voition(pk, voite)
    clients = list(Client.objects.all())
    data = []
    for client in clients:
        data.append({"pk": client.pk,
                     "photo": client.photo.url,
                     "voite": client.voite,
                     "name": u"{0} {1}".format(client.name, client.surname)})
    result = {"data": data}
    return render(request, "voition.html", result)


def voition(pk, voite):
    try:
        with transaction.atomic():
            client = Client.objects.get(pk=pk)
            client.voite += voite
            client.save()
    except:
        voition(pk, voite)


@login_required(login_url=log_url)
def return_clients_xlsx(request):
    response = HttpResponse(content_type="application/vnd.ms-excel")
    response['Content-Disposition'] = 'attachment; filename=report.xlsx'
    result = create_list_clients_xlsx.apply_async(args=(response,))
    while not(result.ready()):
        pass
    response = result.result
    return response
