from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect
from web_functions.web import get_data, get_token

# Create your views here.


def index(request):
    context = {}
    try:
        token = request.session['token']
        user_data = get_data(token=token)
        if user_data:
            context['details'] = user_data['user']
        else:
            return redirect('login')
    except KeyError:
        return redirect('login')
    return render(request, "index.html", context=context)


@csrf_protect
def login(request):
    context = {}
    if request.method == 'POST':
        data = request.POST  # Access items like you would in a normal dictionary
        netid = data['netid']
        password = data['password']
        token = get_token(username=netid, password=password)
        if token:
            print("[+] Token Obtained")
            # Stores the token for the session
            request.session['token'] = token
            return redirect('index')
        else:
            return redirect('error')
    return render(request, "registration/login.html", context=context)


def attendance(request):
    context = {}
    try:
        token = request.session['token']
        data = get_data(token=token)
        if data:
            attendance_data = data['courses']
            context['attendance_data'] = attendance_data
        else:
            return redirect('error')
    except KeyError:
        return redirect('login')
    return render(request, "attendance.html", context=context)

#! NOTE: To access dictionary items in a django template "myDictionary.key" is the syntax, which will give the value


def marks(request):
    context = {}
    try:
        token = request.session['token']
        data = get_data(token)
        in_marks = data['internal_marks']
        context['internals'] = in_marks
    except KeyError:
        return redirect('login')
    return render(request, "marks.html", context=context)


def error(request):
    context = {}
    return render(request, 'error.html', context=context)

# TODO: Add the obtained data to the rest of the pages, like marks, timetable, and other things
# TODO: Add requirements.txt file and poetry.lock and pyproject.toml
