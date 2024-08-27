from .models import User, FriendshipRequest
from rest_framework import serializers

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','email','friends_count','posts_count','get_avatar',)


class FriendshipRequestSerializers(serializers.ModelSerializer):
    created_by = UserSerializers(read_only = True)
    class Meta:
        model = FriendshipRequest
        fields = ('id','created_by',)