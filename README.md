

```
/api/v1/videos/                 backend.core.views.video_list   core:video_list
/api/v1/videos/<int:pk>/        backend.core.views.video_detail core:video_detail
/api/v1/videos/<int:pk>/delete/ backend.core.views.video_delete core:video_delete
/api/v1/videos/<int:pk>/update/ backend.core.views.video_update core:video_update
/api/v1/videos/create/          backend.core.views.video_create core:video_create
/api/v2/videos/                 backend.core.views.videos       core:videos
/api/v2/videos/<int:pk>/        backend.core.views.video        core:video
```