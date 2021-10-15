from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from ..models import Listing


class ListingListView(ListView):
    model = Listing
    context_object_name = "listings"
    template_name = "listings/listing_list.html"

