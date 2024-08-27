from .models import Post, Comment, Trends, PostAttachments
from rest_framework import serializers
from account.serializers import UserSerializers

class PostAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAttachments
        fields = ('id','get_image',) 

class PostSerializers(serializers.ModelSerializer):
    created_by = UserSerializers(read_only=True)
    attachments = PostAttachmentSerializer(read_only = True, many=True)
    class Meta:
        model = Post
        fields = ('id','body','is_private','likes_count','comments_count','created_by','created_by_formatted','attachments',)

class CommentSerializer(serializers.ModelSerializer):
    created_by = UserSerializers(read_only = True)
    class Meta:
        model = Comment
        fields = ('id','body','created_by','created_by_formatted',)


class PostDetailSerializer(serializers.ModelSerializer):
    created_by = UserSerializers(read_only = True)
    comments = CommentSerializer(read_only = True, many = True)
    attachments = PostAttachmentSerializer(read_only = True, many=True)
    class Meta:
        model = Post
        fields = ('id','body','likes_count','comments_count','created_by','created_by_formatted','comments','attachments',)

class TrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trends
        fields = ('id','hashtag','occurences',)