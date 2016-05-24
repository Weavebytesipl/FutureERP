from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect
from django.template import RequestContext

from helpdesk.models import Complaint


from dashboard.forms import LoginForm

@login_required
def home(request):	
    pending_complaints_count = Complaint.objects.filter(is_active=True).count()
    total_complaints_count = Complaint.objects.all().count()
    complaints_progress = 0
    if total_complaints_count:
        complaints_progress = 100 *(total_complaints_count-pending_complaints_count)/total_complaints_count
    dash_data ={ 'pending_complaints_count' : pending_complaints_count , 'total_complaints_count' : total_complaints_count, 'complaints_progress' : complaints_progress, 'user' : request.user }
    return render_to_response('index.html', dash_data, context_instance=RequestContext(request))

def login_page(request):
    """
    If user is authenticated, direct them to the next page.
    Otherwise, take them to the login page.

    :param request: django HttpRequest

    :return: django HttpResponse
    """

    message = None
    error = None
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
                return HttpResponseRedirect(next_page)
            else:
                message = "Your account is not active, please contact the site admin."
                error = 1
        else:
            message = "Your username and/or password were incorrect."
            error = 1

    c = {'username': username, 'form': form, 'next': next_page}
    if message:
        c.update({"message": message})
    if error:
        c.update({"error": error})
    c.update(csrf(request))

    return render_to_response('login.html', c)


def logout_page(request):
    """ Log users out and re-direct them to the main page. """
    logout(request)
    return HttpResponseRedirect('/login/', {'request': request})
