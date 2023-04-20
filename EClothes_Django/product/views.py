from django.shortcuts import render
from django.http import Http404
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
# import time

# Generic List Built in DRF to list the ProductList
class LatestProductList(APIView):
    def get(self,request,format = None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products,many = True) #many = true because we have more than one object
        return Response(serializer.data)
    
class ProductDetail(APIView):
    def get_object(self,category_slug,product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug) # this will return all the details 
            # of the matching slugs of the product in the url. eg /winter/wool-gloves
        except Product.DoesNotExist:
            raise Http404 # if the query fails
        
    def get(self,request,category_slug,product_slug,format=None):
        product = self.get_object(category_slug,product_slug)
        serializer = ProductSerializer(product)
        # time.sleep(3)
        return Response(serializer.data)
        

