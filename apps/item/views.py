from django.shortcuts import render, HttpResponse, redirect
from ..login_reg.models import User
from .models import Item
from django.contrib import messages

def dashboard(request):

    wisheditems = User.objects.get(id=request.session['userid']).wishfor.all()
    allitem = Item.objects.all()

    i1 = set(wisheditems)
    i2 = set(allitem)

    i2 -= i1

    context = {
        "itemsinwishlist": i1,
        "otherswishes": i2

    }

    return render(request, 'item/dashboard.html', context)

def create(request):
    return render(request, 'item/create.html')

def logout(request):
    request.session.flush()
    return redirect('/')
def home(request):
    return redirect('/wish_items/dashboard')

def add(request):
    Item.objects.creator(request.POST['item'], request.session['userid'])
    return redirect ('/wish_items/dashboard')

def adding_to_wishlist(request, item_id):
    Item.objects.adding_to_wishlist(request.session['userid'], item_id)
    return redirect ('/wish_items/dashboard')

def removing_from_wishlist(request, item_id):
    Item.objects.removing_from_wishlist(request.session['userid'], item_id)
    return redirect ('/wish_items/dashboard')

def showingitem(request,item_id):
    context = {
        "users_wished_by": Item.objects.get(id=item_id)
        }
    return render(request, 'item/show.html', context)

def delete(request, item_id):
    Item.objects.get(id=item_id).delete()
    return redirect ('/wish_items/dashboard')
