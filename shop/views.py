import logging
import re
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from shop.models import Item


def archives_year(request, year):
    return HttpResponse('{}년도에 대한 내용'.format(year))


def item_list(request):
    qs = Item.objects.all()

    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(name__icontains=q)

    return render(request, 'shop/item_list.html', {
        'item_list': qs,
        'q': q,
    })
#장고 폼을 안쓰면 이렇게 힘들다.
def item_detail(request,pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'shop/item_detail.html', {
        'item':item,
    })

def item_new(request, item=None):
    error_list = []
    initial = {}

    if request.method == 'POST':
        data = request.POST
        files = request.FILES

        name = data.get('name')
        desc = data.get('desc')
        price = data.get('price')
        photo = files.get('photo')
        is_published = data.get('is_published') in (True, 't', 'True', '1')

        # 유효성 검사
        if len(name) < 2:
            error_list.append('name을 2글자 이상 입력해주세요.')

        if re.match(r'^[\da-zA-Z\s]+$', desc):
            error_list.append('한글을 입력해주세요.')

        if not error_list:
            # 저장 시도
            if item is None:
                item = Item()

            item.name = name
            item.desc = desc
            item.price = price
            item.is_published = is_published

            if photo:
                item.photo.save(photo.name, photo, save=False)

            try:
                item.save()
            except Exception as e:
                error_list.append(e)
            else:
                return redirect(item)

        initial = {
            'name': name,
            'desc': desc,
            'price': price,
            'photo': photo,
            'is_published': is_published,
        }
    else:
        if item is not None:
            initial = {
                'name': item.name,
                'desc': item.desc,
                'price': item.price,
                'photo': item.photo,
                'is_published': item.is_published,
            }

    return render(request, 'shop/item_form.html', {
        'error_list': error_list,
        'initial': initial,
    })


def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return item_new(request, item)