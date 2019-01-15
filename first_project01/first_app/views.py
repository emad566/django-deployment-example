from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {"insert_content": "I'm the inserted content"}
    return render(request, "first_app/index.html", my_dict)