from contrib.router import HybridRouter

from .user import UserViewSet, SignUpViewSet


AccountHybridRouter = HybridRouter()
AccountHybridRouter.register('user', UserViewSet)
AccountHybridRouter.register('signup', SignUpViewSet, 'signup')