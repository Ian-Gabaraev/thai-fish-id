from rest_framework import generics, throttling

from .models import Fish
from .serializers import FishSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class FishFilterView(APIView):
    serializer_class = FishSerializer

    def post(self, request, format=None):
        colors = request.data.get('colors', [])
        size = request.data.get('size', '')

        # Filter queryset based on non-null user-supplied attributes
        queryset = Fish.objects.all()
        if colors:
            queryset = queryset.filter(color__in=colors)
        if size:
            queryset = queryset.filter(size=size)

        serializer = FishSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
