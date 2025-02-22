from django.urls import path
from .views import MainView, PostDetailView, SignUpView, SignInView, LogoutView
from blog.blog import settings

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('post/<slug>/', PostDetailView.as_view(), name='post_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout',)

]