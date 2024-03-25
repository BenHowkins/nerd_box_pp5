from django.shortcuts import render
from .views import handler404

def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)

handler404 = 'nerd_box.views.handler404'