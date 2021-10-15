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


class ListingDetailView(DetailView):
    model = Listing
    template_name = "listings/listing_detail.html"


class ListingCreateView(LoginRequiredMixin, CreateView):
    model = Listing
    fields = ["price", "venue", "description"]
    template_name = "listings/listing_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("listing-detail", args=(self.object.id,))

