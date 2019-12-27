from django.db.models import Manager, QuerySet, Q, F
from django.db.models.manager import BaseManager


class NaturalPersonManager(Manager):
    def tags(self, *args, tag_name=None, **kwargs):
        model_tag = self.model._meta.get_field('address').related_model._meta.get_field('tags').related_model
        query = Q(address__person__pk__in=self.filter(*args, **kwargs))
        if tag_name:
            query = query & Q(name=tag_name)
        return model_tag.objects.filter(query)


class LegalPersonQuerySet(QuerySet):
    def tags(self, *args, tag_name=None, **kwargs):
        model_tag = self.model._meta.get_field('address').related_model._meta.get_field('tags').related_model
        query = Q(address__person__pk__in=self.filter(*args, **kwargs))
        if tag_name:
            query = query & Q(name=tag_name)
        return model_tag.objects.filter(query)


class LegalPersonManager(BaseManager.from_queryset(LegalPersonQuerySet)):
    pass
