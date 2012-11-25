from django.http import HttpResponse
import json

def track(request):
    print "got this far"
    my_data= [{'person': 12345}, {"locations":[[-122.4496179,37.7657324],[-122.4236498,37.7239323]]}]
    response =  HttpResponse(my_data, content_type='application/json')
    return response
