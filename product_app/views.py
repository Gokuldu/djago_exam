from django.shortcuts import render,get_object_404
from django.contrib.auth.models import User
from rest_framework.views import APIView
from product_app.models import productDb
from product_app.serializers import ProductSerializer,RegisterSerializer
from rest_framework.response import Response



# Create your views here.

class RegisterView(APIView):
    def post(self,request):
        serialzers_instance = RegisterSerializer(data=request.data)
        if serialzers_instance.is_valid():
            serialzers_instance.save()
            return Response({
                "message":"Register created successfully..."
            })
        else:
            return Response(data=serialzers_instance.errors)

    def get(self,request):
        user = User.objects.all()
        serialzers_instance = RegisterSerializer(user,many=True)
        return Response(serialzers_instance.data)


        
class ProducListView(APIView):
    def get(self,request):
        data =  productDb.objects.all(data=request.data)
        serialzers_instance = productserializers(data,many=True)
        return Response(serialzers_instance.data)

    def post(self,request):
        serialzers_instance = productserializers(data=request.data)
        if serialzers_instance.is_valid():
            serialzers.save(user=request.user)
            return Response(serialzers_instance.data)
        return Response(serialzers_instance.errors)

class ProductRerieveUpdateDeleteView(APIView):
    def put(self,request,id):
        qs = get_object_404(productDb,id=id,user.request.user)
        serialzers_instance = productserializers(qs,data=request.data)
        if serializers_insatance.isvalid
        


