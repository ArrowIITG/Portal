from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r"login/$", views.loginView ,name='login'),
    url(r"logout/$", views.LogoutView , name="logout"),
    url(r"requestform/$", views.StudentView , name="student_request_form"),
    url(r"requests/$", views.ViewAllrequests , name="allrequests"),
    url(r"requests/(?P<pk>[0-9]+)/approve$", views.RequestApprove , name="trackrequest"),
    url(r"requests/(?P<pk>[0-9]+)/disapprove$", views.RequestDisApprove , name="disapproverequest"),
    url(r"requests/(?P<pk>[0-9]+)/view$", views.RequestView , name="ViewRequestInfo"),
    # url(r"signup/$", views.SignUp.as_view(), name="signup"),
]
