from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello chiku and chiklu")
def abu(request):
    return HttpResponse("Good night")
def calc(request):
    a=28
    b=21
    c=20
    d=19
    e=18
    total=a+b+c+d+e
    return HttpResponse("<h3><em>The total is: </em> " +str(total) +"</h3>")