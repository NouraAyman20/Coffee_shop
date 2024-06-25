from django.shortcuts import render ,get_object_or_404, redirect
from django.http import HttpResponse
from .models import Coffee, Add
from .form import AddCard

 
# Create your views here.

def home(request):
  coffee = Coffee.objects.all()
  context = {'coffee' : coffee}
  
  return render(request,'home.html' ,context)

def main(request):
  return render(request,'main.html')


def detail(request, coffee_id):
    coffee_detail = get_object_or_404(Coffee, id=coffee_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        quantity=request.POST.get('quantity')
        card_number = request.POST.get('card_number')
        address = request.POST.get('address')
        
        
        if name and email and card_number:
            # Check if the user is authenticated before assigning owner
            if request.user.is_authenticated:
                add_instance = Add(name=name, email=email, card_number=card_number, owner=request.user , address=address, quantity=quantity)
                add_instance.save()
                return redirect('coffee:detail', coffee_id=coffee_id)
            else:
                # Handle case where user is not authenticated (optional)
                # Redirect or display a message
                return redirect('account_login')  # Example redirect to login page

    context = {'coffee': coffee_detail}
    return render(request, 'coffee_detail.html', context)