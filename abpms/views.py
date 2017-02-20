from django.views.generic.base import TemplateView

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy

# Create your views here.

#--- TemplateView
class IndexView(TemplateView):
    template_name = 'production/index.html'


class ProfileView(TemplateView):
    template_name = 'production/profile.html'

class TableView(TemplateView):
    template_name = 'production/tables_dynamic.html'

#--- User Creation
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'
