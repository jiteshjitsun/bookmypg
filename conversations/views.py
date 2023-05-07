from django.shortcuts import redirect
from django.urls import reverse
from users import models as user_model
from django.views.generic import DetailView
from . import models
from django.db.models import Q


# Create your views here.
def go_conversation(request, a_pk, b_pk):
    user_one = user_model.User.objects.get(pk=a_pk)
    user_two = user_model.User.objects.get(pk=b_pk)
    if user_one is not None and user_two is not None:
        try:
            conversation = models.Conversation.objects.get(
                Q(participants=user_one) & Q(participants=user_two)
            )
        except models.Conversation.DoesNotExist:
            conversation = models.Conversation.objects.create()
            conversation.participants.add(user_one, user_two)
        return redirect(reverse("conversations:detail", kwargs={"pk": conversation.pk}))
    

class ConversationDetailView(DetailView):
    model = models.Conversation