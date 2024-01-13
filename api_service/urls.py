from django.urls import path
from .views import getRoutes,getNotes,getNotebyID,createNote,updateNote,deleteNote

urlpatterns = [
    path('',getRoutes),
    path('notes/',getNotes),
    path('notes/create/',createNote),
    path('notes/<int:pk>/',getNotebyID),
    path('notes/update/<int:pk>/',updateNote),
    path('notes/delete/<int:pk>/',deleteNote),
    
]
