from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")


# and this view
# def list_view(request):
#     published = Post.objects.exclude(published_date__exact=None)
#     posts = published.order_by('-published_date')
#     context = {'posts': posts}
#     return render(request, 'templates/list.html', context)


class BlogListView(ListView):
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )
    template_name = "blogging/list.html"


class BlogDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"


# def detail_view(request, post_id):
#     published = Post.objects.exclude(published_date__exact=None)
#     try:
#         post = published.get(pk=post_id)
#     except Post.DoesNotExist:
#         raise Http404
#     context = {"post": post}
#     return render(request, "blogging/detail.html", context)
