from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserProfileSerializer, DailyRegisterSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def calculoTeste(request):

    if request.method == 'GET':
        # Esta linha faz o Django procurar o seu arquivo HTML e mostrá-lo
        return render(request, 'calculatorMain/index.html')
    
    # Se for POST, ele segue com a lógica que você já tinha
    if request.method == 'POST':
        serializer = UserProfileSerializer(data=request.data)
        print("entrou no post")

        if serializer.is_valid():
            serializer.save() 
            # EM VEZ DE: return Response(...)
            # FAZEMOS:
            return render(request, 'calculatorMain/success.html')
        
        # Se os dados estiverem errados, volta pro form com os erros
        print(serializer.errors)
        return render(request, 'calculatorMain/index.html', {'errors': serializer.errors})
    
def home_view(request):
    return render(request, 'calculatorMain/homepage.html')