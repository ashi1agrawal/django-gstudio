"""Views for Attributeapp authors"""
from django.shortcuts import get_object_or_404
from django.views.generic.list_detail import object_list

from attributeapp.models import Author
from attributeapp.settings import PAGINATION
from attributeapp.views.decorators import update_queryset
from attributeapp.views.decorators import template_name_for_attributetype_queryset_filtered


author_list = update_queryset(object_list, Author.published.all)


def author_detail(request, username, page=None, **kwargs):
    """Display the attributetypes of an author"""
    extra_context = kwargs.pop('extra_context', {})

    author = get_object_or_404(Author, username=username)
    if not kwargs.get('template_name'):
        kwargs['template_name'] = template_name_for_attributetype_queryset_filtered(
            'author', author.username)

    extra_context.update({'author': author})
    kwargs['extra_context'] = extra_context

    return object_list(request, queryset=author.attributetypes_published(),
                       paginate_by=PAGINATION, page=page,
                       **kwargs)
