from hoka.adapter.base import *

class IZopeRoot(Interface):
    pass

class Adapter(BaseAdapter):

    def __call__(self):
        """Return the current authenticated user"""
        return self.context.restrictedTraverse('/')