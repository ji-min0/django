# from django.http import Http404
from django.shortcuts import render, get_object_or_404

from bookmark.models import Bookmark


def bookmark_list(request):
    # bookmarks = Bookmark.objects.all()
    # SELECT * FROM bookmark
    bookmarks = Bookmark.objects.filter(id__gte=50)

    # return HttpResponse('<h1>Bookmark List Page</h1>')
    return render(request, 'bookmark_list.html', {'bookmarks': bookmarks})

def bookmark_detail(request, pk):
    # bookmark = Bookmark.objects.get(pk=pk)

    # try:
    #     bookmark = Bookmark.objects.get(pk=pk)
    # except Bookmark.DoesNotExist:
    #     raise Http404

    bookmark = get_object_or_404(Bookmark, pk=pk)

    return render(request, 'bookmark_detail.html', {'bookmark': bookmark})