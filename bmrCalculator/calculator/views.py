from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from calculator.models import UserProfile
from .serializers import UserProfileSerializer, DailyRegisterSerializer
from rest_framework.views import APIView

def home_view(request):
    return render(request, 'calculatorMain/homepage.html')

class TMBCalculus(APIView): # this class is called when we access the endpoint /calculator/ (see urls.py)

    def get(self, request):
        registros = UserProfile.objects.all().order_by('-id')
        return render(request, 'calculatorMain/index.html', {'registros': registros})

    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save() 
            return render(request, 'calculatorMain/success.html')
        
        print(serializer.errors)
        return render(request, 'calculatorMain/index.html', {'errors': serializer.errors})
