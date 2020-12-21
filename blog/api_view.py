from .models import Post
from .serializer import postserializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
@api_view(['GET', 'POST'])
def api_list(request):
    all_data=Post.objects.all()
    data=postserializers(all_data,many=True).data
    return Response({'data':data})
@api_view(['GET','POST'])
def api_detail(request,pk):
    post_data=Post.objects.get(id=pk)
    single_post=postserializers(post_data).data
    return Response({'post':single_post})