from django.urls import path

from listings.views import (
    ListingListView,
    ListingDetailView,
)


urlpatterns = [
    path(
        "listings/<int:pk>",
        ListingDetailView.as_view(),
        name="listing-detail",
    ),
    path("", ListingListView.as_view(), name="listing-list"),
]
