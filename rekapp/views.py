from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_name(request):
    if request.method == "GET":
        try:
            name = request.GET.get("name", None)
            message = request.GET.get("message", None)
            text = f"Hello {name}!\n{message}!"
        except:
            text = "Error"
    return HttpResponse(text, content_type="text/json")
