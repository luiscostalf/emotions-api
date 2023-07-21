# Import necessary modules and classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes
from django.http import JsonResponse
from emotions_singleton import EmotionsSingletonClass

# Endpoint for the index page
def index(request):
    return JsonResponse({'group': 'created'})

# Endpoint to get emotions of a message
@csrf_exempt
@parser_classes([JSONParser])
def get_emotions(request):
    if request.method == 'POST':
        try:
            message = JSONParser().parse(request)['message'] 
        except (KeyError):
            return JsonResponse({'error': 'Invalid request method'}, status=405)
        else:
            resp = EmotionsSingletonClass.get_instance().emotions(message)
            resp = dict(sorted(resp.items(), key=lambda item: item[1], reverse=True))
            return JsonResponse(resp)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

# Endpoint to get the irony of a message
@csrf_exempt
@parser_classes([JSONParser])
def get_irony(request):
    if request.method == 'POST':
        try:
            message = JSONParser().parse(request)['message']
        except (KeyError):
            return JsonResponse({'error': 'Invalid request method'}, status=405)
        else:
            resp = EmotionsSingletonClass.get_instance().irony(message)
            resp = dict(sorted(resp.items(), key=lambda item: item[1], reverse=True))
            return JsonResponse(resp)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

# Endpoint to get the sentiment of a message
@csrf_exempt
@parser_classes([JSONParser])
def get_sentiment(request):
    if request.method == 'POST':
        try:
            message = JSONParser().parse(request)['message']
        except (KeyError):
            return JsonResponse({'error': 'Invalid request method'}, status=405)
        else:
            resp = EmotionsSingletonClass.get_instance().sentiment(message)
            resp = dict(sorted(resp.items(), key=lambda item: item[1], reverse=True))
            return JsonResponse(resp)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

# Endpoint to interact with a bot using a message
@csrf_exempt
@parser_classes([JSONParser])
def get_bot(request):
    if request.method == 'POST':
        try:
            message = JSONParser().parse(request)['message']
        except (KeyError):
            print(KeyError)
            return JsonResponse({'error': 'Invalid request method'}, status=405)
        else:
            print(message)
            resp = EmotionsSingletonClass.get_instance().tryBot(message)
            return JsonResponse(resp)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
