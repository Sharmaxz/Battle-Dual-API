from rest_framework import serializers, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from creation.models import Room
from ..models import Hash


class HashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hash
        fields = '__all__'


class HashViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Hash.objects.all()
    serializer_class = HashSerializer
    filter_backends = [SearchFilter]
    search_fields = ['turn', 'player_one', 'player_two']
    permission_classes = (IsAuthenticated,)

    def update(self, request, pk, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = HashSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        room = Room.objects.get(game_id=instance.id)
        room .is_end = serializer.data['is_end']
        room.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def destroy(self, pk):
        hash = Hash.objects.filter(id=pk)
        if hash:
            hash.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)