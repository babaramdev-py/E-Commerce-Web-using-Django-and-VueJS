from django.shortcuts import render
from django.db.models import Q
from django.http import Http404
from .serializers import ProductSerializer,CategorySerializer, OrdersSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Category, Orders 
from rest_framework.decorators import api_view
# import time

# Generic List Built in DRF to list the ProductList
class LatestProductList(APIView):
    def get(self,request,format = None):
        products = Product.objects.all()[0:5]
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
        

class CategoryDetail(APIView):
    def get_object(self,category_slug):
        try:
            return Category.objects.get(slug=category_slug) # this will return all the details 
            # of the matching slugs of the product in the url. eg /winter/wool-gloves
        except Category.DoesNotExist:
            raise Http404 
    
    def get(self,request,category_slug,format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        # time.sleep(3)
        return Response(serializer.data)
            

@api_view(['POST'])
def search(request):
    query = request.data.get('query','')
    print(query)
    if query:
        products  = Product.objects.filter(Q(name__icontains=query)|Q(description__icontains=query))
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    return Response({"products":[]})

class OrdersView(APIView):
    def get(self, request):
        orders = Orders.objects.all().values()
        serializer = OrdersSerializer(orders,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = OrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
