from django.shortcuts import render, redirect
from django.views import generic as view

from carcollection_app.carcollection.forms import CreateProfileForm, CreateCarForm, EditCarForm, DeleteCarForm, \
    EditProfileForm, DeleteProfileForm
from carcollection_app.carcollection.models import Profile, Car


# Create your views here.

def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def profile_fullname():
    profile = get_profile()
    full_name = []
    if profile.first_name:
        full_name.append(profile.first_name)
    if profile.last_name:
        full_name.append(profile.last_name)
    if full_name:
        return " ".join(full_name)
    else:
        return None


def all_cars_price():
    cars = Car.objects.all()
    total_price = 0
    for car in cars:
        total_price += car.price
    return total_price


def index(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'common/index.html', context=context)


def create_profile(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form
    }
    return render(request, 'profile/profile-create.html', context=context)


def catalogue(request):
    context = {
        'cars': Car.objects.all(),
        'total_cars': Car.objects.all().count(),
    }
    return render(request, 'common/catalogue.html', context=context)


def create_car(request):
    if request.method == 'GET':
        form = CreateCarForm()
    else:
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form
    }
    return render(request, 'car/car-create.html', context=context)


def details_car(request, pk):

    context = {
        'car': Car.objects.filter(pk=pk).get()
    }

    return render(request, 'car/car-details.html', context=context)


def edit_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = EditCarForm(instance=car)
    else:
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
    }

    return render(request, 'car/car-edit.html', context=context)


def delete_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = DeleteCarForm(instance=car)
    else:
        form = DeleteCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
    }

    return render(request, 'car/car-delete.html', context=context)




def details_profile(request):
    profile = get_profile()

    context = {
        'profile': profile,
        'full_name': profile_fullname(),
        'total_price': all_cars_price(),
    }

    return render(request, 'profile/profile-details.html', context=context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile/profile-edit.html', context=context)


def delete_profile(request):
    if request.method == 'GET':
        form = DeleteProfileForm()
    else:
        form = DeleteProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'profile/profile-delete.html', context=context)

# class EditProfilePage(view.UpdateView):
    