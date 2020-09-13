from django.views.generic import (
    View,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)

from .models import Notes


class NotesListView(ListView):
    model = Notes
    queryset = Notes.objects.all()
    context_object_name = 'notes'
    template_name = 'notes_list.html'
