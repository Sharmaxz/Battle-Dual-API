from contrib.router import HybridRouter

from .hash import HashViewSet

HashHybridRouter = HybridRouter()
HashHybridRouter.register('hash', HashViewSet)