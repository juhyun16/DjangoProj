from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import SignupForm
from django.conf import settings
from django.views.generic.edit import FormView
from .forms import LoginForm

# Create your views here.
@login_required
def profile(request):
    context=dict()
    return render(request, "accounts/profile.html", context)


def signup(request):
    if request.method == "POST":
        form=SignupForm(request.POST)
        if(form.is_valid()):
            user=form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form=SignupForm()

    context=dict()
    context["form"]=form
    return render(request, "accounts/signup_form.html", context)


class LoginView(FormView):
    form_class=LoginForm
    template_name="accounts/login_form.html"
    success_url = settings.LOGIN_REDIRECT_URL

    def form_invalid(self, form):
        context=dict()
        context["form"]=form
        return render(self.request, self.template_name, context)


