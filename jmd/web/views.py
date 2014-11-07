from django.shortcuts import render

# Create your views here.
def home(request, tmpl='web/home.html'):
    data = {}

    return render(request, tmpl, data)