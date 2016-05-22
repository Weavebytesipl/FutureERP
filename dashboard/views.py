from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect
from django.template import RequestContext

from dashboard.forms import LoginForm

@login_required
def home(request):	
    return render_to_response('index.html', context_instance=RequestContext(request))

def login_page(request):
    """
    If user is authenticated, direct them to the next page.
    Otherwise, take them to the login page.

    :param request: django HttpRequest

    :return: django HttpResponse
    """

    state = ""
    username = password = ''
    form = LoginForm()

    # default next page is index page
    next_page = "/"

    print request

    # getting next page in get request
    if request.GET:
        next_page = request.GET.get('next')

    if request.POST:
        # a form bound to the post data
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_page = request.POST.get('next')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                # redirect after post
                print "--- redirecting ---"
                return HttpResponseRedirect(next_page)
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    c = {'state': state, 'username': username, 'form': form, 'next': next_page}
    c.update(csrf(request))

    return render_to_response('login.html', c)


def logout_page(request):
    """ Log users out and re-direct them to the main page. """
    logout(request)
    return HttpResponseRedirect('/login/', {'request': request})
