from django.http import HttpResponse


def say_hello(request):
    return HttpResponse('Hello World!')


def say_hello_with_name(request, name):
    print(request.headers)
    return HttpResponse(f'Hello from scaler {name}')