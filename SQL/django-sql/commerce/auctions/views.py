from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ListingForm
from .models import User, Listing, Bid, Comment


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.filter(open=True)
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create_listing(request):
    message = ""
    form = ListingForm()

    if not isinstance(request.user, User):
        message = "You must be logged in to create a listing."

    if request.method == "POST":
        form = ListingForm(request.POST)

        if form.is_valid():
            # Create a Listing instance from the form data but don't save it yet
            listing = form.save(commit=False)

            # Modify the instance (e.g., assign the current user)
            listing.user = request.user
            listing.price = listing.bid
            # Save the modified instance to the database
            listing.save()


            new_bid = Bid(user=request.user, listing=listing, amount=request.POST["bid"])
            new_bid.save()
            message = "Listing created."


    return render(request, "auctions/create_listing.html", {
        "message": message,
        "form": form,
    })


def _create_listing(request):
    if request.method == "POST":
        user = request.user
        title = request.POST["title"]
        description = request.POST["description"]
        bid = int(request.POST["bid"])
        img_url = request.POST["img_url"]
        category = request.POST.get("category")

        if not isinstance(user, User):
            return render(request, "auctions/create_listing.html", {
                "message": "You must be logged in to create a listing.",
                "categories": ["Fashion", "Toys", "Electronics", "Home", "Other"],
            })

        listing = Listing(title=title, description=description, bid=bid, img_url=img_url, category=category, user=user, price=bid)
        listing.save()

        new_bid = Bid(user=user, listing=listing, amount=bid)
        new_bid.save()
        return render(request, "auctions/create_listing.html", {
            "message": "Listing created.",
            "categories": ["Fashion", "Toys", "Electronics", "Home", "Other"],
        })

    return render(request, "auctions/create_listing.html", {
        "categories": ["Fashion", "Toys", "Electronics", "Home", "Other"],
    })


def return_listing(request, ls=None, bids=None, message=None, in_wishlist=None, is_owner=None):
    if not (ls or bids):
        raise ValueError("ls or bids must be provided")
    context = dict()
    context["listing"] = ls
    context["bids"] = bids
    context["comments"] = ls.comments.all()
    if message:
        context["message"] = message
    if in_wishlist:
        context["in_wishlist"] = in_wishlist
    if is_owner:
        context["is_owner"] = is_owner
    return render(request, "auctions/listing.html", context)


def listing(request, listing_id):
    ls = Listing.objects.get(pk=listing_id)
    bids = ls.bids.all()
    user = request.user
    in_wishlist = user.is_authenticated and user.wishlist.filter(pk=ls.pk).exists()
    is_owner = user.is_authenticated and ls.user == user
    message = ""

    if request.method == "POST":

        if "bid" in request.POST:
            bid_amount = int(request.POST["amount"])

            if not isinstance(user, User):  # if the user is not signed in
                message = "You must sign in for bidding"

            elif bid_amount <= ls.price:
                message = f"You must enter a value greater than {ls.price}"

            else:
                bid = Bid(user=user, listing=ls, amount=bid_amount)
                bid.save()
                ls.price = bid_amount
                ls.save()
                message = f"Your bidding has been successfully applied: {ls.price}"

        elif "add_wishlist" in request.POST:

            if not isinstance(user, User):  # if the user is not signed in
                message = "You must sign in to add this item to your wishlist"
            else:
                ls.wishlistedBy.add(user)
                ls.save()
                in_wishlist = True

        elif "remove_wishlist" in request.POST:

            ls.wishlistedBy.remove(user)
            ls.save()

            in_wishlist = False

        elif "close" in request.POST:
            ls.open = False
            ls.save()
            message = "The auction has been closed"
            if user != bids.last().user:
                ls.winner = bids.last().user  # the last bid is the highest
                ls.save()

        if "comment" in request.POST:
            comment = request.POST["comment"]
            cmmt = Comment(user=user, listing=ls, content=comment)
            cmmt.save()

    if not ls.open:
        message = f"The auction has been closed. The winner is {ls.winner.username if ls.winner else 'no one'}"
        if user.is_authenticated and user == ls.winner:
            message += " - Congratulations!"

    return return_listing(request, ls=ls, bids=bids, in_wishlist=in_wishlist, is_owner=is_owner, message=message)


def wishlist(request):
    user = request.user
    message = ""

    if request.method == "POST":
        listing_id = request.POST["remove_wishlist"]
        listing = Listing.objects.get(pk=listing_id)
        listing.wishlistedBy.remove(user)
        listing.save()

    if not user.is_authenticated:
        message = "You must be logged in to view your watchlist."

    elif not user.wishlist.all():
        message = "Your watchlist is empty"

    return render(request, "auctions/wishlist.html", {
        "listings": user.wishlist.filter(open=True),
        "message": message,
    })
