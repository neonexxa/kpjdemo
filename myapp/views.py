from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

import json
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("kpjtawakal-firebase-adminsdk-35igj-b9bad5fa93.json")
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()
# define home function
# def home(request):
# 	db.collection(u'navigation').document(u'room107').update({u'currentpage': "haha"})
# 	return HttpResponse('Hello World!')
def webhook(request):
    # build a request object
    req = json.loads(request.body)
    # get action from json
    action = req.get('queryResult').get('action')
    print(action)
    if action == "curse" :
    	return JsonResponse({'fulfillmentText': 'Dont curse me!! '}, safe=False)
    if action == "home.menu" :
        db.collection(u'navigation').document(u'room107').update({u'currentpage': "home.menu"})
        return JsonResponse({'fulfillmentText': 'Choose Your Menu ! Services? Entertainment?'}, safe=False)
    if action == "menu.doctor" :
        db.collection(u'navigation').document(u'room107').update({u'currentpage': "menu.doctor"})
        return JsonResponse({'fulfillmentText': 'Do you want to call for doctor? See your treatment? or see your profile?'}, safe=False)
    if action == "menu.doctor.calling" :
        db.collection(u'navigation').document(u'room107').update({u'currentpage': "menu.doctor.calling"})
        return JsonResponse({'fulfillmentText': 'Calling for available doctors right away'}, safe=False)
    if action == "menu.nurse.calling" :
        db.collection(u'navigation').document(u'room107').update({u'currentpage': "menu.nurse.calling"})
        return JsonResponse({'fulfillmentText': 'Calling for available doctors right away'}, safe=False)
    if action == "menu.doctor.mytreatment" :
        db.collection(u'navigation').document(u'room107').update({u'currentpage': "menu.doctor.mytreatment"})
        return JsonResponse({'fulfillmentText': 'Heres your treatment analysis. It seems like your B P is high, and your colesterol level is very severe.'}, safe=False)
    if action == "menu.doctor.myprofile" :
        db.collection(u'navigation').document(u'room107').update({u'currentpage': "menu.doctor.myprofile"})
        return JsonResponse({'fulfillmentText': 'Here is your registered profile to this bedding found within the hospital database.'}, safe=False)
    if action == "menu.tv" :
        db.collection(u'navigation').document(u'room107').update({u'currentpage': "menu.tv"})
        return JsonResponse({'fulfillmentText': 'Streaming up to you in a moment.'}, safe=False)
    # return a fulfillment message
    fulfillmentText = {'fulfillmentText': 'Initiating Eye sara assistant '}
    # return response
    return JsonResponse(fulfillmentText, safe=False)

def root(request):
    return JsonResponse({'status': 'alive'})
def home(request):
    return render(request, 'home.html')

def menu_doctor(request):
    return render(request, 'menu_doctor.html')

def menu_doctor_calling(request):
    return render(request, 'menu_doctor_calling.html')

def menu_nurse_calling(request):
    return render(request, 'menu_nurse_calling.html')

def menu_doctor_mytreatment(request):
    return render(request, 'menu_doctor_mytreatment.html')

def menu_doctor_myprofile(request):
    return render(request, 'menu_doctor_myprofile.html')

def menu_tv(request):
    return render(request, 'menu_tv.html')

