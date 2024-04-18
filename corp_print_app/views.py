from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm, PrintTemplateForm
from .models import Profile, PrintTemplate


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Авторизация прошла успешно!')
            else:
                return HttpResponse('Учетная запись деактивирована.')
        else:
            return HttpResponse('Неправильный логин или пароль.')
    else:
        form = LoginForm()
    return render(request, 'corp_print_app/login.html', {'form': form})

@login_required
def printed_production(request):
    return render(request,
                  'corp_print_app/printed_production.html',
                  {'section': 'printed_production'})

def index(request):
    return render(request,
                  'corp_print_app/index.html')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,
                          'corp_print_app/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'corp_print_app/register.html',
                  {'user_form': user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'corp_print_app/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})
    

def edit_template(request, template_id):
    # Получаем объект шаблона по его ID
    template = get_object_or_404(PrintTemplate, pk=template_id)

    if request.method == 'POST':
        # Если данные были отправлены методом POST, обрабатываем форму
        form = PrintTemplateForm(request.POST, request.FILES, instance=template)
        if form.is_valid():
            form.save()
            # После успешного сохранения шаблона, перенаправляем пользователя на другую страницу, например на страницу с подробностями о шаблоне
            return redirect('corp_print_app/index.html', template_id=template.id)
    else:
        # Если данные не были отправлены методом POST, создаем форму на основе существующего шаблона
        form = PrintTemplateForm(instance=template)

    return render(request, 'corp_print_app/edit_template.html', {'form': form})
