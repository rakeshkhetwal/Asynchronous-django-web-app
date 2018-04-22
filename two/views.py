from django.shortcuts import render
from .models import names
from django.template import RequestContext
from django.http import response
from django.http import HttpResponse

# Create your views here.


def x(request):
    # user = request.user
    if request.method == "POST":  # and request.is_ajax():
        name = request.POST['name']
        email= request.POST['email']
        password= request.POST['pass']

        f = names.objects.create(your_name =name, passwod=password, email=email)
        f.save()

        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            request.session.set_test_cookie()
            return HttpResponse("Please enable cookies and try again.")
            #return render(request, 'two/home.html')
        else:
            return HttpResponse("Please enable cookies and try again.")



    else:
        status = "Bad"
        return HttpResponse(status)



        #if f.is_valid():
    #    username = f.cleaned_data['your_name']

    #response = render_to_response(request, 'loggedin.html', {"username": username},                                  context_instance=RequestContext(request))
    #response = get_response(request)
    #.set_cookie()

    #response = render(request, 'two/loginid.html', {"username": name},
    #                              context_instance=RequestContext(request))
    #HttpResponse.set_cookie('name', name) #datetime.datetime.now()
    #HttpResponse.set_cookie('email', email)

    #response.set_cookie('last_connection', datetime.datetime.now())
    #response.set_cookie('username', datetime.datetime.now())
    #return render(request, "two/home.html")





def login(request):
    if request.method == 'POST':
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            return HttpResponse("You're logged in.")
        else:
            return HttpResponse("Please enable cookies and try again.")
    request.session.set_test_cookie()
    return render(request, 'foo/login_form.html')


def index(request):
    return render(request, "two/home.html")