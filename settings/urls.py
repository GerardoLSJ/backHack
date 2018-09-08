"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from rest_framework import routers
#from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from django.conf.urls import url, include
from django.contrib import admin

from mxhacks import views

router = routers.DefaultRouter()
#router.register(r'formato', views.FormatoViewSet , base_name='formatoView')
router.register(r'tags', views.TagsViewSet, base_name='TagsViewSet')
router.register(r'procedure', views.ProcedureViewSet, base_name='ProcedureViewSet')
router.register(r'law', views.LawViewSet, base_name='LawViewSet')
router.register(r'city', views.CityViewSet, base_name='CityViewSet')
router.register(r'country', views.CountryViewSet, base_name='CountryViewSet')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api/test/', views.TestView.as_view()),


]
