from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import District, Branch


# Create your views here.
def home(request):
    districts = District.objects.all()
    branches = Branch.objects.all()
    return render(request, 'home.html', {'districts': districts, 'branches': branches})
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('profile')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('password1')

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, "Registration successful. You can now log in.")
                return redirect('login')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('register')

    return render(request, "register.html")


def profile(request):
    return render(request, 'profile.html')


def form(request):
    districts = District.objects.all()
    branches = Branch.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone_number = request.POST['phone_number']
        mail_id = request.POST['mail_id']
        address = request.POST['address']
        district_id = request.POST['district']
        branch_id = request.POST['branch']
        account_type = request.POST['account_type']

        materials_provided = request.POST.getlist('materials_provided')

        district = None
        branch = None

        if district_id:
            district = District.objects.get(pk=district_id)

        if branch_id:
            branch = Branch.objects.get(pk=branch_id)

        messages.success(request, "Application Accepted")

    return render(request, 'form.html', {'districts': districts, 'branches': branches})
