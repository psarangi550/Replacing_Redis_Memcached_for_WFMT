from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.core.cache import cache
# Create your views here.

@cache_page(60)
def index(request):
    cache.set("value",90)
    print(cache.get("value"))
    myvalue=cache.get("value")
    context={"val":myvalue}
    return render(request,"wfmtmemcachedApp/index.html",context=context)