from re import search
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

from products.models import Product


def q_search(query):
    # поиск через id 
    if query.isdigit() and len(query) <=3:
        return Product.objects.filter(id=int(query))
    vector = SearchVector("name")
    query = SearchQuery(query)

    return Product.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")