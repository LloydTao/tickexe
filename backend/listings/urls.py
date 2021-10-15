from django.urls import path

from listings.views import (
    ListingListView,
    ListingDetailView,
    ListingCreateView,
    ListingUpdateView,
    ListingDeleteView,
)


urlpatterns = [
    path(
        "listings/create/",
        ListingCreateView.as_view(),
        name="listing-create",
    ),
    path(
        "listings/<int:pk>/delete/",
        ListingDeleteView.as_view(),
        name="listing-delete",
    ),
    path(
        "listings/<int:pk>/update/",
        ListingUpdateView.as_view(),
        name="listing-update",
    ),
    path(
        "listings/<int:pk>",
        ListingDetailView.as_view(),
        name="listing-detail",
    ),
    path("", ListingListView.as_view(), name="listing-list"),
]
