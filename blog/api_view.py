from .models import Post
from .serializer import postserializers
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.db.models import Count, Q
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_list_or_404, get_object_or_404
@api_view(['GET', 'POST'])
#@permission_classes([IsAuthenticated])
def api_list(request):
    #all_data=Post.objects.all()
    all_data=get_list_or_404(Post)
    data=postserializers(all_data,many=True).data
    return Response({'data':data})
@api_view(['GET','POST'])
#@permission_classes([IsAuthenticated])
def api_detail(request,pk):
    #post_data=Post.objects.get(id=pk)
    post_data=get_object_or_404(Post,id=pk)
    single_post=postserializers(post_data).data
    return Response({'post':single_post})
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_api(request,q):
    required_post=Post.objects.filter(
        Q(title__icontains=q)|Q(description__icontains=q)
    )
    data=postserializers(required_post,many=True).data
    return Response({'data':data})