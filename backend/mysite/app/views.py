from django.shortcuts import render



# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets ,generics ,mixins
from .serializers import UserSerializer, CondidatSerializer
from app.models import Condidat
from rest_framework.permissions import IsAdminUser
from rest_framework import filters
from django.db.models import Count, F, Value
from django.db.models.functions import Length, Upper
from django_filters.rest_framework import DjangoFilterBackend
# from mysite.settings import EMAIL_HOST_USER
# from django.core.mail import send_mail




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]




#CRUD


#generics.ListAPIView
class  CondidatViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    lookup_fild ='pk'
    #search
    search_fields = [ "first_name","last_name","e_mail"]
    filter_backends = [DjangoFilterBackend]
    #CRUD
    queryset=Condidat.objects.all().order_by("first_name","last_name","e_mail")
    serializer_class=CondidatSerializer


    #sending mail code
    # try:
    #     {
    #     sub = queryset.get_email()
    #     subject = 'applying for a job in infinity manegment'
    #     message = '  your application is in process'
    #     recepient = str(sub['Email'].value())
    #     send_mail(subject,
    #         message, EMAIL_HOST_USER, [recepient], fail_silently = False)}
    # else :
    #     pass



    # def get_extra_actions():
    #    mixins.CreateModelMixin,generics.ListAPIView



        # def get_object(self):
        #     first_name=self.first_name.get()
        #     return Condidat.objects.get(first_name=first_name)
        #
