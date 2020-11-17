from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView, ListView, TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from blog.models import Post
from .models import Profile
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, PasswordUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login ')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile_update(request, *args, **kwargs):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your Profile has been Updated!')
            return reverse_lazy('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'users/profile_update.html', {'p_form': p_form})


@login_required
def account_mgt(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your Account has been Updated!')
            return redirect('blog:post_list')
    else:
        u_form = UserUpdateForm(instance=request.user)
    return render(request, 'users/account.html', {'u_form': u_form})


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordUpdateForm
    success_url = reverse_lazy('blog:post_list')

    # def success_message(self):
    #     messages.success(self, f'Your Password has been changed successfully!')
    #     return super(PasswordsChangeView, self).success_message()


class ProfilePageView(DetailView):
    model = Profile
    template_name = 'users/profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfilePageView, self).get_context_data(**kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context
