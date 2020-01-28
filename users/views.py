from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from .forms import FormularioLogin

from django.contrib.auth import login,logout
from django.contrib.auth.models import User
# Create your views here.


class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)
                

def authentication(request):
    template = "login.html"
    if request.method == 'POST':
        action = request.POST.get('action', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('products/')
        else:
            print("No login")               

    return render(request, 'login.html', {})

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('accounts/login/')

def register(request):
    if request.method == 'POST':
        action = request.POST.get('action', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)

        if action == 'signup':
            user = User.objects.create_user(username=username, password=password, email=email, first_name= first_name, last_name=last_name)
            user.save()

    return render(request, 'register.html', {})