from django.shortcuts import render
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from app.models import StockData, updateLogs

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from .serializers import StockDataSerializer

from rest_framework.filters import SearchFilter


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

class StockList(GenericAPIView,ListModelMixin):
    queryset = StockData.objects.all()
    serializer_class = StockDataSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

    @method_decorator(cache_page(CACHE_TTL))
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

# Create your views here.
def home(request):
    last_updated_on = updateLogs.objects.latest('update_date')
    return render(request,'app/home.html',{'date':last_updated_on})
