from django.conf.urls import url

def fake_view(request):
    pass

urlpatterns = [
    url(r'^cmstest/', fake_view, name='fake'),
]
