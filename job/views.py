from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from job.forms import CompanyRegistrationForm, CompanyUpdateForm


def register(request):
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('login')
    form = CompanyRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'company/register.html', context)


@login_required
def company(request):
    if request.method == 'POST':
        form = CompanyUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
    form = CompanyUpdateForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'company/company.html', context)

    def __str__(self):
        return self.title

