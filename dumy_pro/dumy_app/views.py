from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseForbidden,  HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist


# Create your code here

# Main page function
def main_page(request):
    return render(request, "myfile/main_page.html")

def email_user(request):
    if request.method == "POST":
        return redirect('dumy_app:register_user')
    return render(request,"myfile/email_page.html")

def register_user(request):
    if request.method == "POST":
        return redirect('dumy_app:user_page')
    return render(request,"myfile/register_user.html")

def user_page(request):
    return render(request,"myfile/user_page.html")

def profile_login(request):
    return render(request,"myfile/login_page.html")

def forgot_password_view(request):
    return render(request,"myfile/forgot_pass.html")

def user_image(request):
    return render(request,"myfile/user_profile.html")

def update_password(request):
    return render(request,"myfile/update_pass.html")

# Users Content Function
def users_cont(request):
    return render(request,"contentfile/users_content.html")

def java_cont(request):
    return render(request,"contentfile/java_content.html")

def python_cont(request):
    return render(request,"contentfile/python_content.html")

def analysis_cont(request):
    return render(request,"contentfile/analysis_content.html")

def science_cont(request):
    return render(request,"contentfile/science_content.html")




# Python compiler
def run_code(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        try:
            with open('temp_code.py', 'w') as f:
                f.write(code)
            result = subprocess.run(['python', 'temp_code.py'], capture_output=True, text=True, timeout=5)
            output = result.stdout + result.stderr
        except Exception as e:
            output = str(e)
        return JsonResponse({'output': output})

