from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Color, Fish
from .serializers import FishSerializer


class FishFilterView(APIView):
    serializer_class = FishSerializer

    def post(self, request, *args, **kwargs):
        colors = request.data.get('colors')
        size = request.data.get('size')
        shape = request.data.get('shape')
        behaviors = request.data.get('behaviors')

        if not any((colors, size, shape, behaviors)):
            return Response({}, status=status.HTTP_204_NO_CONTENT)

        queryset = Fish.objects.all()
        if colors:
            colors = Color.objects.filter(name__in=colors)
            queryset = queryset.filter(colors__in=colors)
        if size:
            queryset = queryset.filter(size=size)
        if shape:
            queryset = queryset.filter(shape=shape)
        if behaviors:
            queryset = queryset.filter(behavior__in=behaviors)

        serializer = FishSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
