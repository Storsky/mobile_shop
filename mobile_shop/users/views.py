from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UpdateProfileForm, UpdateUserForm

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile is updated")
            return redirect(to='users-profile')

    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    
    
    
    goods = request.user.profile.products.all()
    
    
    template = 'users\profile.html'
    context = {'user_form': user_form, 'profile_form': profile_form, 'goods': goods}
    return render(request, template, context)

