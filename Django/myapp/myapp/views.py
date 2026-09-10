from django.shortcuts import render

def custom_handle_error(request, exception):
    return render(request, '404.html', status=400)