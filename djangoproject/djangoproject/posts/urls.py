from django.conf.urls import url
from . import views as posts_views
from django.views.generic import ListView, DetailView
from .models import Post
from django.contrib.auth.views import  login, logout

# lista dei post | homepage del sito
# post singoli del blog
# sezione contatti

urlpatterns = [
    url(r'^$', ListView.as_view(
        queryset = Post.objects.all().order_by('-data'),
        template_name = "lista_post.html",
        paginate_by = 3), name="lista"),

    url(r'^(?P<id>\d+)/(?P<slug>[\w-]+)/$', DetailView.as_view(
        model = Post,
        template_name = "post_singolo.html"), name="singolo"),
    url(r'^contatti/$', posts_views.contatti, name="contatti"),
    url(r'^login/$', login, {'template_name': 'login.html'}),  # Cambio template  di login
    url(r'^logout/$', logout, {'template_name': 'logout.html'}),
    url(r'^profile/$', posts_views.profile, name='profile'),
]
