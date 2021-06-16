
from django.views.generic import TemplateView


class BookView(TemplateView):
    template_name = 'home.html'
    paginate = 4


class ContactView(TemplateView):
    template_name = 'contact.html'