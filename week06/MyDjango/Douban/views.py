from django.shortcuts import render

# Create your views here.
from .models import Movies
from django.db.models import Avg

def moives_short(request):
    ###  从models取数据传给template  ###
    queryset = Movies.objects.all()
    # star_value = Movies.objects.values('n_star')
    condition = {'n_star__gt': 3}
    shorts = queryset.filter(**condition)


    return render(request, 'result.html', locals())

def search_comment(request):
    text = request.GET.get('q')
    # 大于3星的
    queryset = Movies.objects.all()
    condition = {'n_star__gt': 3, 'short_content__icontains': text}
    shorts = queryset.filter(**condition)
    # return HttpResponse('text')
    return render(request, 'result.html', locals())