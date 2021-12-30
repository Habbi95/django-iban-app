from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages

from .models import IBANUser
from .forms import IBANUserForm

# Create your views here.
@login_required
def get_users(request):
    iban_user_list = IBANUser.objects.filter(created_by=request.user)
    context = {'iban_user_list': iban_user_list}
    return render(request, 'get_users.html', context)

@login_required
def delete_user(request, user_id):
    # Just in case, we filter again by admin
    try:
        iban_user = IBANUser.objects.filter(created_by=request.user).get(pk=user_id)
    except IBANUser.DoesNotExist:
        raise Http404("User does not exist. Please check the owner of the user")

    iban_user.delete()
    messages.success(request, 'User deleted')
    return redirect(get_users)

@login_required
def create_or_update_user(request, user_id=None):
    if request.method == 'POST':
        form = IBANUserForm(request.POST)
        if form.is_valid():
            # Extract info from form and create or update IBANUser object
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            iban = form.cleaned_data['iban']
            created_by = request.user

            defaults = dict()

            if user_id: # Looking for existing user
                iban_user = IBANUser.objects.filter(created_by=request.user).get(pk=user_id)
                defaults['first_name'] = first_name
                defaults['last_name'] = last_name
                defaults['iban'] = iban

                # Rename those vars to look for current existing user
                first_name = iban_user.first_name
                last_name = iban_user.last_name
                iban = iban_user.iban

            IBANUser.objects.update_or_create(first_name=first_name, last_name=last_name, created_by=created_by, iban=iban, defaults=defaults)
            messages.success(request, 'User created' if not user_id else 'User updated')
        else:
            list_of_errors = form.errors.as_data()
            for error in list_of_errors:
                messages.error(request, str(list_of_errors[error].pop()))

        return redirect(get_users)

    else:
        # GET method, it could be modify page or create new one
        form = IBANUserForm()
        already_exists = False
 
        if user_id:
            try:
                iban_user = IBANUser.objects.filter(created_by=request.user).get(pk=user_id)
            except IBANUser.DoesNotExist:
                raise Http404("User does not exist. Please check the owner of the user")

            fields = {
                'first_name': iban_user.first_name,
                'last_name': iban_user.last_name,
                'iban': iban_user.iban}

            already_exists = True
            form = IBANUserForm(fields)

    return render(request, 'create_modify_user.html', {'form': form, 'already_exists': already_exists, 'id': user_id})