from django.urls import include, path

from backend.core import views as v

app_name = 'core'

v1_urlpatterns = [
    path('videos/', v.video_list, name='video_list'),
    path('videos/<int:pk>/', v.video_detail, name='video_detail'),
    path('videos/create/', v.video_create, name='video_create'),
    path('videos/<int:pk>/update/', v.video_update, name='video_update'),
    path('videos/<int:pk>/delete/', v.video_delete, name='video_delete'),
]

v2_urlpatterns = [
    path('videos/', v.videos, name='videos'),
    path('videos/<int:pk>/', v.video, name='video'),
]

urlpatterns = [
    path('api/v1/', include(v1_urlpatterns)),
    path('api/v2/', include(v2_urlpatterns)),
]
