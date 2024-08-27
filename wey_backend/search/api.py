from django.http import JsonResponse
from rest_framework.decorators import api_view
from account.models import User
from account.serializers import UserSerializers
from post.models import Post
from post.serializers import PostSerializers
from django.db.models import Q

@api_view(['POST'])
def search(request):
    data = request.data
    query = data['query']
    user_ids = [request.user.id]

    for user in request.user.friends.all():
        user_ids.append(user.id)

    users = User.objects.filter(name__icontains=query)
    user_serializer = UserSerializers(users, many=True)

    posts = Post.objects.filter(
        Q(body__icontains=query,is_private = False) | 
        Q(created_by_id__in=list(user_ids),body__icontains=query)
    )


    posts_serilizer=PostSerializers(posts, many=True)

    return JsonResponse({
        'users':user_serializer.data,
        'posts':posts_serilizer.data
        }, safe=False)