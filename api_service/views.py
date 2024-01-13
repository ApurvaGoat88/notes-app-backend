
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NoteSerializer
from rest_framework import status
from .models import Note
@api_view(['POST','GET','DELETE','PUT'])
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
    
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    ser = NoteSerializer(notes,many = True)
    
    return Response(ser.data)


@api_view(['GET'])
def getNotebyID(request,pk):
    notes = Note.objects.get(id =pk)
    ser = NoteSerializer(notes)
    return Response(ser.data)



@api_view(['POST'])
def createNote(request):
    
        body = request.data.get("body", "")  # Use get to avoid KeyError if 'body' is not present
        note = Note(body=body)
        note.save()  # Use .save() method to save the instance
        ser = NoteSerializer(note, many=False)
        return Response(ser.data, status=status.HTTP_201_CREATED)
 
 
   
@api_view(['PUT'])
def updateNote(request,pk):
    data = request.data 
    note = Note.objects.get(id = pk)
    ser = NoteSerializer(note,data=request.data)
    if ser.is_valid():
        ser.save()
        
    return Response(ser.data)

    
    
@api_view(['DELETE'])
def deleteNote(request,pk):
    note = Note.objects.get(id= pk)
    note.delete()
    return Response("Note deleted")