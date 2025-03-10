from django.shortcuts import render
from django.shortcuts import HttpResponse
from Chapter_02.models import Bookmark
from django.http import Http404
from django.shortcuts import get_object_or_404

def bookmark_list(request):
    bookmarks = Bookmark.objects.filter(id__gte=50)
    # SELECT * FROM bookmark

    context = {'bookmarks': bookmarks}
    template_name = 'bookmark_list.html'
    return render(request, template_name, context)

def bookmark_detail(request, pk):
    # try:
    #     bookmark = Bookmark.objects.get(pk=pk)
    # except:
    #     raise Http404
    bookmark = get_object_or_404(Bookmark, pk=pk)

    template_name = 'bookmark_detail.html'
    context={'bookmark': bookmark}
    return render(request, template_name, context)
