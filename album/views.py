from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import AlbumInfo


# Create your views here.
def album(request, id, page):
    albumList = AlbumInfo.objects.filter(user_id=id).order_by('id')
    paginator = Paginator(albumList, 8)
    try:
        pageInfo = paginator.page(page)
    except PageNotAnInteger:
        # 如果参数page的数据类型不是整型，返回第一页
        pageInfo = paginator.page(1)
    except EmptyPage:
        # 若用户访问的页数大于实际页数，则返回最后一页的数据
        pageInfo = paginator.page(paginator.num_pages)
    return render(request, 'album.html', locals())
