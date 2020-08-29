from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# def password_check(passwd): 
      
#     # SpecialSym =['$', '@', '#', '%', '!', '^', '&', '*', '(',')','[',']','{','}', ",", '.'] 
#     val = True
      
#     if len(passwd) < 6: 
#         print('length should be at least 6') 
#         val = False
          
#     if len(passwd) > 20: 
#         print('length should be not be greater than 8') 
#         val = False
          
#     if not any(char.isdigit() for char in passwd): 
#         print('Password should have at least one numeral') 
#         val = False
          
#     if not any(char.isupper() for char in passwd): 
#         print('Password should have at least one uppercase letter') 
#         val = False
          
#     if not any(char.islower() for char in passwd): 
#         print('Password should have at least one lowercase letter') 
#         val = False
          
#     # if not any(char in SpecialSym for char in passwd): 
#     #     print('Password should have at least one of the symbols $@#') 
#     #     val = False
#     if val: 
#         return val 

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        
        if password == password2:
            #check username
            if User.objects.filter(username= username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email= email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    user= User.objects.create_user(username= username, password= password, email= email)
                    # auth.login(request, user)
                    # messages.success(request, 'you are now logged in')
                    user.save()
                    messages.success(request, 'you are now registered in')
                    return redirect('login')
        else:
            messages.error(request, 'Password donot match')
            return redirect('register')
            
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user= auth.authenticate(username= username, password= password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def logout(request):

    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('login') 

# @login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html') 


