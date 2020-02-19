from contrib.router import HybridRouter

from .room import RoomViewSet

CreationHybridRouter = HybridRouter()
CreationHybridRouter.register('room', RoomViewSet)
