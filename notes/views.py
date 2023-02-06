from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Notes
from .serializers import NoteSerializer


# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes=[
        {
            'endpoint':'/notes',
            'method':'GET',
            'body':None,
            'description':'returns an array of the notes'
        },
          {
            'endpoint':'/notes/id',
            'method':'GET',
            'body':None,
            'description':'returns a single notes object'
        },
          {
            'endpoint':'/notes/create',
            'method':'POST',
            'body':{'body':""},
            'description':'creates new notes with data sent in post request'
        },
          {
            'endpoint':'/notes/id/update/',
            'method':'PUT',
            'body':{'body':""},
            'description':'creates an existing notes with data sent in post request'
        },
          {
            'endpoint':'/notes/id/delete/',
            'method':'DELETE',
            'body':None,
            'description':'delete an existing note'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
  notes = Notes.objects.all().order_by()
  serializer = NoteSerializer(notes, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def getNote(request, pk):
  notes = Notes.objects.get(id=pk)
  serializer = NoteSerializer(notes, many=False)
  return Response(serializer.data)


@api_view(['put'])
def updateNote(request, pk):
  data = request.data
  note = Notes.objects.get(id=pk)
  serializer = NoteSerializer( instance = note, data = data)

  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request, pk):
  note = Notes.objects.get(id = pk)
  note.delete()
  return Response('Notes was succesfully Deleted')