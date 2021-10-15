from django.urls import path

from listings.views import (
    ListingListView,
    ListingDetailView,
    ListingCreateView,
)


urlpatterns = [
    path(
        "listings/create/",
        ListingCreateView.as_view(),
        name="listing-create",
    ),
    path(
        "listings/<int:pk>",
        ListingDetailView.as_view(),
        name="listing-detail",
    ),
    path("", ListingListView.as_view(), name="listing-list"),
]
