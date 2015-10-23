from django.shortcuts import render
from django.conf import settings
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
from disease.models import Interaction
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta

import json
# Create your views here.


@csrf_exempt
def index(request):
    return HttpResponse(json.dumps({'DiseaseServer': 'is alive'}), content_type="application/json")



def time(request):
    return HttpResponse(json.dumps({'time': str(datetime.now()) }), content_type="application/json")


@csrf_exempt
def addinteraction(request):
    if request.method == "POST":
        try:
            #read request data as json from request body
            request_data = json.loads(request.body)

            #the interaction data payload
            inter = request_data['interaction']
        except:
            return HttpResponse(json.dumps({'status': 'failed to saved data'}), content_type="application/json")
        #print(request)
        #create a log object and save it in the database
        interactionbobj = Interaction(interaction_contents=inter, pub_date=datetime.now())
        interactionbobj.save()

        return HttpResponse(json.dumps({'status': 'data saved successfully'}), content_type="application/json")

    elif request.method == "GET":
        return HttpResponse("must use post")

    return HttpResponse("must use post")


@csrf_exempt
def addinteractiongroup(request):
    if request.method == "POST":
        try:
            #read request data as json from request body
            request_data = json.loads(request.body)

            #the interaction data payload
            inters = request_data['interactions']
        except:
            return HttpResponse(json.dumps({'status': 'failed to saved data'}), content_type="application/json")
        #print(request)
        #create a log object and save it in the database

        for inter in inters:
            duplicates = Interaction.objects.filter(interaction_contents=inter)
            if duplicates.count() == 0:
                interactionbobj = Interaction(interaction_contents=inter, pub_date=datetime.now())
                interactionbobj.save()

        return HttpResponse(json.dumps({'status': 'data saved successfully'}), content_type="application/json")

    elif request.method == "GET":
        return HttpResponse("must use post")

    return HttpResponse("must use post....")


@csrf_exempt
def getall(request):
    if request.method == 'GET':

        interactions = Interaction.objects.all();
        data = {
            'interactions': interactions
        }
        #return HttpResponse(json.dumps({'data': data}), content_type="application/json")
        return render_to_response('review.html', data, RequestContext(request))
    else:
        return HttpResponse("request for recent data should not be a POST")


@csrf_exempt
def getdetails(request):
    if request.method == 'GET':

        interactions = Interaction.objects.all();
        data = {
            'interactions': interactions
        }
        #return HttpResponse(json.dumps({'data': data}), content_type="application/json")
        return render_to_response('reviewdetail.html', data, RequestContext(request))
    else:
        return HttpResponse("request for recent data should not be a POST")


@csrf_exempt
def getallsince(request):
    if request.method == 'POST':
        #print(request.POST)
        dictData = request.POST
        delt = dictData.__getitem__('delta')#['delta']
        #print(delt)
        delta = int(delt)
        #print(delta)
        limittime = datetime.now() - timedelta(minutes=delta)
        #print(limittime)

        interactions = Interaction.objects.filter(pub_date__gte=limittime)
        data = {
            'starttime' : str(limittime),
            'interactions': interactions
        }
        #return HttpResponse(json.dumps({'data': data}), content_type="application/json")
        return render_to_response('reviewsince.html', data, RequestContext(request))
    else:
        return HttpResponse("request for recent data should be a POST")


@csrf_exempt
def getdetailssince(request):
    if request.method == 'POST':
        #print(request.POST)
        dictData = request.POST
        delt = dictData.__getitem__('delta')#['delta']
        #print(delt)
        delta = int(delt)
        #print(delta)
        limittime = datetime.now() - timedelta(minutes=delta)
        #print(limittime)

        interactions = Interaction.objects.filter(pub_date__gte=limittime)
        data = {
            'starttime' : str(limittime),
            'interactions': interactions
        }
        #return HttpResponse(json.dumps({'data': data}), content_type="application/json")
        return render_to_response('reviewdetailssince.html', data, RequestContext(request))
    else:
        return HttpResponse("request for recent data should be a POST")


