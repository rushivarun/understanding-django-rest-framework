from rest_framework import serializers
from .models import questions
# from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
class question_serializer(serializers.ModelSerializer):
    class Meta:
        model = questions
        fields = ('question', 'status', 'created_by', 'id',)
