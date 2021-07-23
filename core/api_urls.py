from django.urls import path

import core.api_views as api_views

urlpatterns = [
    path('update_meeting/<str:meeting_id>', api_views.update_meeting),
    path('interrupt_meeting/<str:meeting_id>', api_views.interrupt_meeting),

    path('get_meetings_from_db', api_views.get_meetings),
    path('update_all_meetings', api_views.update_all_meetings),
]
