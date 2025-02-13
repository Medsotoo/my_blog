from django.urls import path
from .views import MainView, PostDetailView, SignUpView

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('post/<slug>/', PostDetailView.as_view(), name='post_detail'),
    path('signup/', SignUpView.as_view(), name='signup')

]