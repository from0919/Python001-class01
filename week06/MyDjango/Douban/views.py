from django.shortcuts import render

# Create your views here.
from .models import Movies
from django.db.models import Avg

def moives_short(request):
    ###  从models取数据传给template  ###
    shorts = Movies.objects.all()
    # # 评论数量
    # counter = Movies.objects.all().count()
    #获取星级
    star_value = Movies.objects.values('n_star')


    # # 平均星级
    # # star_value = T1.objects.values('n_star')
    # star_avg =f" {T1.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f} "
    # # 情感倾向
    # sent_avg =f" {T1.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "

    # # 正向数量
    # queryset = T1.objects.values('sentiment')
    # condtions = {'sentiment__gte': 0.5}
    # plus = queryset.filter(**condtions).count()

    # # 负向数量
    # queryset = T1.objects.values('sentiment')
    # condtions = {'sentiment__lt': 0.5}
    # minus = queryset.filter(**condtions).count()

    # # return render(request, 'douban.html', locals())
    return render(request, 'result.html', locals())