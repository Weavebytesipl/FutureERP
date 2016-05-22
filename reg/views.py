from django.shortcuts import render
from django.contrib.auth.models import User

from .forms import RegistrationForm

def regform(request):
    # If the request method is POST, it means that the form has been submitted
    # and we need to validate it.
    if request.method == 'POST':
        # Create a RegistrationForm instance with the submitted data
        form = RegistrationForm(request.POST)
    
        # is_valid validates a form and returns True if it is valid and
        # False if it is invalid.
        if form.is_valid():
            # ensure that username is unique
            try:
                if User.objects.get(username=form.cleaned_data['username']):
                    message = "Username already exists !!!"
                    return render(request, "login.html", {"message": message, "register": "register", "error": 1} )
            except:
                pass
                    
                
            # registering new username
            user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'],
                    email=form.cleaned_data['email']
                    )
            message = "Registration successful, try logging now..."
            return render(request, "login.html", {"message": message} )
        else:
            # sending back error codes for "Invalid form"
            message = "Invalid entires, try again !!!"
            return render(request, "login.html", {"message": message, "register": "register", "error": 1} )
 
    # This means that the request is a GET request. So we need to
    # create an instance of the RegistrationForm class and render it in
    # the template
    else:
        form = RegistrationForm()
 
    # Render the registration form template with a RegistrationForm instance. If the
    # form was submitted and the data found to be invalid, the template will
    # be rendered with the entered data and error messages. Otherwise an empty
    # form will be rendered. Check the comments in the registration_form.html template
    # to understand how this is done.

    # NOTE
    # pass register value to template so that template can show register form
    return render(request, "login.html", { "form" : form, "register": "register" })
