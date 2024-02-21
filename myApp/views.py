from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Picture, PictureForm
import sqlite3

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to the main page or any desired page after successful login
            return redirect('main_page')
        else:
            # Add logic to handle invalid login attempts
            pass

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def main_page(request):
    pictures = Picture.objects.all().order_by('-id')[:5]  # Get the 5 newest pictures
    form = PictureForm()

    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.save(commit=False)
            picture.user = request.user
            picture.save()
            return redirect('main_page')

    return render(request, 'main_page.html', {'pictures': pictures, 'form': form})

@login_required
def delete_picture(request, picture_id):
    picture = get_object_or_404(Picture, id=picture_id)

    # Check if the user is the owner of the picture
    if picture.user == request.user:
        picture.delete()

    return redirect('main_page')

@login_required
def update_description(request, picture_id):
    picture = get_object_or_404(Picture, pk=picture_id)

    if request.method == 'POST':
        new_description = request.POST.get('description', '')
        query = f"UPDATE myApp_picture SET description = '{new_description}' WHERE id = {picture_id};" # comment or remove this line to fix injection vulnerability

        # comment or remove try - except clause to fix the problem
        if request.user == picture.user:
            try:
                connection = sqlite3.connect('db.sqlite3')
                cursor = connection.cursor()
                cursor.executescript(query)
                connection.commit()
                connection.close()
            except:
                print('error with connection')
        # Uncomment the next two lines
        #    picture.description = new_description
        #    picture.save()

            return JsonResponse({'success': True})

    return JsonResponse({'success': False})
