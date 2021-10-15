from django.urls import path

from listings.views import (
    ListingListView,
)


urlpatterns = [
    path("", ListingListView.as_view(), name="listing-list"),
]
