from django.http import HttpResponse, JsonResponse

def homePage(request):
    x = [
        'a',
        'b'
        ]
    return JsonResponse(x,safe=False)