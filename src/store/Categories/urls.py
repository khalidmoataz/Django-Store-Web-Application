from django.urls import path,re_path
from .views import Electronics_page,category_page

urlpatterns = (
    path('', Electronics_page, name='home_view'),
    re_path('Electronics/$(?i)', Electronics_page, name='Electronics_page_view'),
    re_path('(?P<cat_slug>[-@\w]+)/', category_page, name='category_page_view'),
)
