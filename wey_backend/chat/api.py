from rest_framework.decorators import api_view
from django.http import JsonResponse
from .serializers import ConversationSerilizer,ConversationMessageSerilizer,ConversationDetailSerilaizer
from .models import Conversation,ConversationMessage
from account.models import User

@api_view(['GET'])
def conversation_list(request):
    conversations = Conversation.objects.filter(users__in=list([request.user]))
    serializer = ConversationSerilizer(conversations,many=True)

    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
def conversation_detail(request,pk):
    conversation = Conversation.objects.filter(users__in=list([request.user])).get(pk=pk)
    serializer = ConversationDetailSerilaizer(conversation)

    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def conversation_get_or_create(request, user_pk):
    user = User.objects.get(pk=user_pk)

    conversation = Conversation.objects.filter(users__in=list([request.user])).filter(users__in=list([user]))

    if conversation.exists():
        conversation = conversation.first()
    else:
        conversation = Conversation.objects.create()
        conversation.users.add(user, request.user)
        conversation.save()

    serializer = ConversationDetailSerilaizer(conversation)

    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def conversation_send_message(request,pk):
    conversation = Conversation.objects.filter(users__in=list([request.user])).get(pk=pk)

    for user in conversation.users.all():
        if user != request.user:
            sent_to = user

    conversation_message = ConversationMessage.objects.create(
        conversation=conversation,
        body=request.data.get('body'),
        created_by=request.user,
        sent_to=sent_to
    )

    serializer = ConversationMessageSerilizer(conversation_message)

    return JsonResponse(serializer.data, safe=False)

