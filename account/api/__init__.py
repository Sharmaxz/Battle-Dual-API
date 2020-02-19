from contrib.router import HybridRouter

from .user import UserViewSet, SignUpViewSet
from .notification import NotificationViewSet

AccountHybridRouter = HybridRouter()
AccountHybridRouter.register('user', UserViewSet)
AccountHybridRouter.register('notification', NotificationViewSet)
AccountHybridRouter.register('signup', SignUpViewSet, 'signup')

