from django.shortcuts import render
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product


# Generic List Built in DRF to list the ProductList
class LatestProductList(APIView):
    def get(self,request,format = None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products,many = True) #many = true because we have more than one object
        return Response(serializer.data)
    

# 


