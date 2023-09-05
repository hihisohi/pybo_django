"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pybo.views import base_views

# 브라우저에서 페이지 요청이 발생하면 가장 먼저 호출되는 파일
# URL과 뷰 함수 간의 매핑을 정의

# 장고 개발 흐름
# 1) 브라우저에서 로컬 서버로 페이지(http://localhost:8000/pybo)를 요청
# 2) urls.py에서 /pybo URL 매핑을 확인하여 views.py 파일의 index 함수를 호출
# 3) 호출한 결과를 브라우저에 반영

# from pybo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('pybo/', views.index), # URL 정규화하는 장고의 기능 때문 끝에 / 안붙여도 장고가 자동으로 / 붙임 ===> 특별한 경우 아니면 URL매핑 시 항상 끝에 / 붙이기
    path('pybo/', include('pybo.urls')), # url 분리를 위해 루트의 config/urls.py(프로젝트 단위)가 아니라 pybo/urls.py(앱 단위)를 사용
    path('common/', include('common.urls')),
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
]
