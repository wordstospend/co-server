from django.http import HttpResponse
import json
import datetime
import time

def track(request):
    print "got this far"
    t = datetime.datetime.now()
    my_data= {"locations":[time.mktime(t.timetuple()), [-122.4496179,37.7657324]]}
    # [1353826644.0,[-122.4236498,37.7239323]]]}
    response =  HttpResponse(my_data, content_type='application/json')
    return response
