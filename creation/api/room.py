from rest_framework import serializers, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from django.db.models import Q

from games.hash.models import Hash
from ..models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class RoomViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'owner', 'player_one', 'player_two']
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = Room.objects.filter(Q(player_one=self.request.user) | Q(player_two=self.request.user))
        serializer = RoomSerializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, pk, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = RoomSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def destroy(self, pk):
        room = Room.objects.filter(id=pk)
        if room:
            room.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)