from django.urls import path
from .views import components, contact, delete, foodss,about, project, services,edit
urlpatterns = [
        path('a/',foodss,name='foodss'),
        path('b/<int:pk>',about, name='about'),
        path('c/',contact,name='contact'),
        path('d/',components,name='components'),
        path('e/',project,name='project'),
        path('f/',services,name='services'),
        path('g/<int:pk>',delete,name='delete'),
        path('i/<int:pk>',edit,name='edit')
]
