from django.urls import path
from .views import CategoryListApiView, CountryListApiView, DisctrictListApiView, EnterprisesListApiView,CommentListApiView, ServiceListApiView, TourListApiView

urlpatterns = [
    path('listenterprises/',EnterprisesListApiView.as_view(),name='enterpriseslist'),
    path('listcomment/',CommentListApiView.as_view(),name='commentlist'),
    path('listservice/',ServiceListApiView.as_view(),name='servicelist'),
    path('listcomment/',CategoryListApiView.as_view(),name='categorylist'),
    path('listcomment/',CountryListApiView.as_view(),name='countrylist'),
    path('listcomment/',TourListApiView.as_view(),name='tourlist'),
    path('listcomment/',DisctrictListApiView.as_view(),name='disctrictlist'),

]
