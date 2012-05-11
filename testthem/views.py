from django.http import HttpResponse
import json

def track(request):
    print "got this far"
    my_data= [{'person': 12345}, {"locations":[[17, 18],[12,14]]}]
    response =  HttpResponse(my_data, content_type='application/json')
    return response
