# templates/urls.py

from django.urls import path
from polling.views import detail_view
from polling.views import PollListView

urlpatterns = [
    # path('', list_view, name="poll_index"),
    path("", PollListView.as_view(), name="poll_index"),
    path("polls/<int:poll_id>/", detail_view, name="poll_detail"),
]
