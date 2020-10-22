from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from aplikacja.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', GraphQLView.as_view(graphiql=True)),
]
