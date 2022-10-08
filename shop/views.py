from distutils.log import info
from socket import AddressFamily
from django.shortcuts import redirect, render
# from django.http import HttpResponse
from shop.models import Commande, Product
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    product_object = Product.objects.all()
    item_name = request.GET.get("item_name")
    if item_name != None and item_name !="":
         product_object = Product.objects.filter(title__icontains=item_name)  # des qu'il y ale mot item_name dans la phrase, alors affiche le titre
    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
    return render(request, "shop/index.html", {"product_object": product_object})


def details(request, id):
    product_detail = Product.objects.get(id=id)
    return render(request, "shop/details.html", {"product_detail": product_detail})


def checkout(request):
    if request.method == "POST":
        items = request.POST.get("items")
        total = request.POST.get("total")
        nom = request.POST.get("nom")
        email = request.POST.get("email")
        address = request.POST.get("address")
        ville = request.POST.get("ville")
        pays = request.POST.get("pays")
        zipcode = request.POST.get("zipcode")
        com = Commande(nom=nom, email=email, Address=address, ville=ville, pays=pays, zipcode=zipcode, items=items, total=total)
        com.save()
        return redirect('confirmation')
    
    return render(request, "shop/checkout.html")


def confirmation(request):

    infos = Commande.objects.all()[:1]
    for item in infos:
        nom = item.nom
        
    return render(request, "shop/confirmation.html", {"nom":nom})