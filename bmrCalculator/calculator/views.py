from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserProfileSerializer, DailyRegisterSerializer

# Create your views here.
@api_view(['POST'])
def calculoTeste(request):
    
    serializer = UserProfileSerializer(data=request.data)
    
    if serializer.is_valid():
        
        age = serializer.validated_data['age']
        birth_date = serializer.validated_data['birth_date']
        height = serializer.validated_data['height']
        
        serializer.save() 
        
        return Response({"status": "Dados salvos e TMB calculada!"})
    
    return Response(serializer.errors, status=400)