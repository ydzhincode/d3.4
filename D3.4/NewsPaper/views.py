from django.shortcuts import render, get_object_or_404, redirect, reverse
from NewsPaper.models import Post

######################################################################################################################


def index(request):
    """
    Главная страница
    :param request:
    :return:
    """
    return redirect(reverse('post_list'))


######################################################################################################################


def post_list(request):
    """
    Отображение страницы со списком новостей
    :param request:
    :return:
    """
    context = {
        'post_active': True,
        'list_post': Post.objects.all()
    }
    return render(request=request, template_name='post/list.html', context=context)


######################################################################################################################


def post_show(request, post_id: int):
    """
    Отображение страницы с конкретной новостью
    :param request:
    :param post_id:
    :return:
    """
    post = get_object_or_404(Post, id=post_id)
    context = {
        'post': post,
    }
    return render(request=request, template_name='post/show.html', context=context)


######################################################################################################################
