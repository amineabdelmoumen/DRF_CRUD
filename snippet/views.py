from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BlogPostserializer

from .models import BlogPost

@api_view(['GET'])
def OverView(request):
    api_urls={  
           'overview': '/over',
           'list all the items':'/listdetail/<str:pk>',
           'detail of one specified item':'/itemdetail/<str:pk>',
           'update item':'updateblog/<str:pk>',
           'delete item':'delete/<str:pk>' }          
    return Response(api_urls)
@api_view(['POST'])
def createPost(request):
    serializer=BlogPostserializer(data=request.data)
    data={}
    if serializer.is_valid():
        serializer.save()
    else:
        raise serializer.ValidationError('this is not a valid input')
        



@api_view(['GET'])
def ListDetail(request):
    posts = BlogPost.objects.all()
    serializer = BlogPostserializer(posts,many=True)
    return Response(serializer.data)


"""
This Function going to display Detailed view of one perticuler Blog with the help of pk.
"""
@api_view(['GET'])
def BlogDetail(request, pk):
    post= BlogPost.objects.get(id=pk)
    serializer =BlogPostserializer(post, many = False)
    return Response(serializer.data)

@api_view(['POST',])
def BlogUpdate(request, pk):
    blog = BlogPost.objects.get(id = pk)
    serializer = BlogPostserializer(instance=blog, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['POST',])
def BlogDelete(request, pk):
    blog = BlogPost.objects.get(id = pk)
    blog.delete()

