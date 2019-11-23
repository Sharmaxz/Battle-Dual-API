from contrib.router import HybridRouter

from .user import UserViewSet

AccountHybridRouter = HybridRouter()
AccountHybridRouter.register('user', UserViewSet)