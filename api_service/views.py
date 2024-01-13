import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NoteSerializer
from rest_framework import status
from .models import Note

def getRoutes(request):
    routes = [
        {
            'endpoint':'/notes/',
            'method':'GET',
            'body': None,
            'description':'Return an array of notes'
        },
        {
            'endpoint':'/notes/id',
            'method':'GET',
            'body':None , 
            'description':'Returns a single note object'
        },
        {
            'endpoint':'/notes/create/',
            'method':'POST',
            'body': {'body':''},
            'description':'Create a new Note. Returns the created '
        },
        {
            'endpoint':'/notes/update/id ',
            'method':'PUT',
            'body': {'body':''},
            'description':'Create a new Note.'
            
        },
        {
            'endpoint':'/notes/delete/id ',
            'method':'DELETE',
            'body':None,
            'description':'Delete a note .'
            
        }
    ]
    
    return JsonResponse(routes,safe=False)


def getNotes(request):
    notes = Note.objects.all()
    ser = NoteSerializer(notes,many = True)
    
    return JsonResponse(ser.data,safe=False)



def getNotebyID(request,pk):
    notes = Note.objects.get(id =pk)
    ser = NoteSerializer(notes)
    return JsonResponse(ser.data,safe=False)



@csrf_exempt
def createNote(request):
    
        data = json.loads(request.body)
        body = data['body']      # Use get to avoid KeyError if 'body' is not present
        note = Note(body=body)
        note.save()  # Use .save() method to save the instance
        ser = NoteSerializer(note, many=False)
        return JsonResponse(ser.data,safe=False)
 
 
   
@csrf_exempt
def updateNote(request,pk):
    data = request.data 
    note = Note.objects.get(id = pk)
    ser = NoteSerializer(note,data=request.data)
    if ser.is_valid():
        ser.save()
        
    return JsonResponse(ser.data,safe=False)

    
def deleteNote(request,pk):
    note = Note.objects.get(id= pk)
    note.delete()
    return JsonResponse("Note deleted",safe=False)