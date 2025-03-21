from django.shortcuts import render

# Create your views here.
def index(request):
    meetups = [
        {"title" : "A first meetup", "description" : "La la la lejla lala nij", "location" : "Paris", "slug": "a-first-meetup"},
        {"title" : "A second meetup", "description" : "jednoga dana zalice monojda", "location" : "New York", "slug" : "a-second-meetup"},
    ]
    return render(request, "meetups/index.html", {
        "meetups" : meetups
    })