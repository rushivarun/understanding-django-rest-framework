from django.shortcuts import render
from .models import questions
from .serializers import question_serializer
from django.http import JsonResponse, HttpResponse
from rest_framework import parsers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
# using inbuilt classes


class PollListView(generics.GenericAPIView, mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin):
    serializer_class = question_serializer
    queryset = questions.objects.all()
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication,
                              SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


# self developed classes

class PollAPIView(APIView):
    def get(self, request):
        poll_questions = questions.objects.all()
        serializer = question_serializer(poll_questions, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        data = request.data
        print(data)
        serializer = question_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PollDetailView(APIView):

    def get_object_instance(self, id):
        try:
            instance = questions.objects.get(id=id)
        except questions.DoesNotExist as e:
            return Response({"error": "the question does not exist"}, status=404)

    def get(self, request, id=None):
        instance = self.get_object_instance(id)
        print(instance)
        serializer = question_serializer(instance)
        return Response(serializer.data)

    def put(self, request, id=None):
        data = request.data
        instance = self.get_object_instance(id)
        serializer = question_serializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, id=None):
        instance = self.get_object_instance(id)
        instance.delete()
        return Response(status=204)


# self developed methods

@csrf_exempt
def poll(request):
    if request.method == "GET":

        poll_questions = questions.objects.all()
        serializer = question_serializer(poll_questions, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        json_parser = parsers.JSONParser()
        data = json_parser.parse(request)
        print(data)
        serializer = question_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def poll_details(request, id):

    try:
        instance = questions.objects.get(id=id)
    except questions.DoesNotExist as e:
        return JsonResponse({'error': 'the requested question does not exist'}, status=404)

    if request.method == "GET":
        serializer = question_serializer(instance)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        json_parser = parsers.JSONParser()
        data = json_parser.parse(request)
        print(data)
        serializer = question_serializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        instance.delete()
        return HttpResponse(status=204)
