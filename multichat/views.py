from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

class HomeView(TemplateView):
    template_name = "home.html"


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view=super().as_view(**initkwargs)
        return login_required(view)

