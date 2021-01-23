from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

app_name = 'jobs'
urlpatterns = [
    url(r"^$", views.home, name="home"),
    url(r"^jobs/(?P<href>[\d]+)/$",views.content,name="content"),
    url(r"^company/(?P<href>[\d]+)/$",views.company,name="company"),
    url(r"internship$",views.internship,name="internship"),
    url(r"fulltime$",views.fulltime,name="fulltime"),
    url(r"^status$",views.status,name="status"),
    url(r"^post$", TemplateView.as_view(template_name="jobs/post.html"), name="post"),
    #url(r"^post$", views.postjob, name="postjob"),
    url(r"^postmeetings$", TemplateView.as_view(template_name="jobs/postmeeting.html"), name="postmeetings"),
    url(r"^postcontests$", TemplateView.as_view(template_name="jobs/postcontest.html"), name="postcontests"),
    url(r"^search$",views.search,name="search"),
    url(r"^meetings$",views.meetingShow,name="meetings"),
    url(r"^meetings/(?P<href>[\d]+)/$",views.meetingcontent,name="meetingcontent"),
    url(r"^meetingpoststatus$",views.meetingpoststatus,name="meetingpoststatus"),
    url(r"^contests$",views.contestShow,name="contests"),
    url(r"^contests/(?P<href>[\d]+)/$",views.contestcontent,name="contestcontent"),
    url(r"^contestpoststatus$",views.contestpoststatus,name="contestpoststatus"),
]
