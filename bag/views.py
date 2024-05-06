from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from boxes.models import Product

# Create your views here.
def view_bag(request):
    """ "
    A view that renders the view of the shopping bag's content
    """
    return render(request, "bag/bag.html")


def add_to_bag(request, item_id):
    """
    A specific product and the quantity wanted to the bag
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    size = None
    if "product_size" in request.POST:
        size = request.POST["product_size"]
    bag = request.session.get("bag", {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]["items_by_size"].keys():
                bag[item_id]["items_by_size"][size] += quantity
                messages.success(
                    request,
                    f'Updated: {size.upper()} {product.name} now has a quantity of {bag[item_id]["items_by_size"][size]} selected',
                )
            else:
                bag[item_id]["items_by_size"][size] = quantity
                messages.success(
                    request,
                    f"Added: You added a {size.upper()} {product.name} to your bag",
                )
        else:
            bag[item_id] = {"items_by_size": {size: quantity}}
            messages.success(
                request, f"Added: You added a {size.upper()} {product.name} to your bag"
            )

    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request,
                f"Updated: {product.name} now has a quantity of {bag[item_id]} selected",
            )
        else:
            bag[item_id] = quantity
            messages.success(request, f"Added: You added a {product.name} to your bag")

    request.session["bag"] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    size = None
    if "product_size" in request.POST:
        size = request.POST["product_size"]
    bag = request.session.get("bag", {})

    if size:
        if quantity > 0:
            bag[item_id]["items_by_size"][size] = quantity
            messages.success(
                request,
                f'Updated: {size.upper()} {product.name} now has a quantity of {bag[item_id]["items_by_size"][size]} selected',
            )
        else:
            del bag[item_id]["items_by_size"][size]
            if not bag[item_id]["items_by_size"]:
                bag.pop(item_id)
                messages.success(
                    request,
                    f"Removed: You removed a {size.upper()} {product.name} from your bag",
                )
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request,
                f"Updated: {product.name} now has a quantity of {bag[item_id]} selected",
            )
        else:
            bag.pop(item_id)
            messages.success(
                request, f"Removed: {product.name} has benn removed from your bag"
            )

    request.session["bag"] = bag
    return redirect(reverse("view_bag"))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if "product_size" in request.POST:
            size = request.POST["product_size"]
        bag = request.session.get("bag", {})

        if size:
            del bag[item_id]["items_by_size"][size]
            if not bag[item_id]["items_by_size"]:
                bag.pop(item_id)
            messages.success(
                request,
                f"Removed: You removed a {size.upper()} {product.name} from your bag",
            )
        else:
            bag.pop(item_id)
            messages.success(
                request, f"Removed: {product.name} has benn removed from your bag"
            )

        request.session["bag"] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return HttpResponse(status=500)
