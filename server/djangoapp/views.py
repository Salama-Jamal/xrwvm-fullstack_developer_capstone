# Uncomment the required imports before adding the code

from django.shortcuts import render
# from django.http import HttpResponseRedirect, HttpResponse
# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404, render, redirect
# from django.contrib.auth import logout
# from django.contrib import messages
# from datetime import datetime

from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt
# from .populate import initiate


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"username": user.username, "status": "success"})
        else:
            return JsonResponse({"status": "failed", "message": "Invalid credentials"})
    else:
        return JsonResponse({"status": "failed", "message": "POST request required"})

# Create a `logout_request` view to handle sign out request
def logout_user(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({"status": "success", "message": "Logged out"})
    return JsonResponse({"status": "failed", "message": "POST request required"})

# Create a `registration` view to handle sign up request
@csrf_exempt
def register_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        if not username or not password:
            return JsonResponse({"status": "failed", "message": "Username and password required"})
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        login(request, user)  # Log the user in immediately
        return JsonResponse({"status": "success", "username": username})
    return JsonResponse({"status": "failed", "message": "POST request required"})

# # Update the `get_dealerships` view to render the index page with
# a list of dealerships
def get_dealerships(request):
    if request.method == "GET":
        # Call get_dealers_from_cf method from the imported module
        dealerships = initiate.get_dealers_from_cf()
        return JsonResponse(dealerships, safe=False)
    return JsonResponse({"status": "failed", "message": "GET request required"})

# Create a `get_dealer_reviews` view to render the reviews of a dealer
# def get_dealer_reviews(request,dealer_id):
def get_dealer_reviews(request):
    if request.method == "GET":
        dealer_id = request.GET.get("dealer_id")
        if not dealer_id:
            return JsonResponse({"status": "failed", "message": "dealer_id parameter required"})
        reviews = initiate.get_dealer_reviews_from_cf(dealer_id)
        return JsonResponse(reviews, safe=False)
    return JsonResponse({"status": "failed", "message": "GET request required"})

# Create a `get_dealer_details` view to render the dealer details
def get_dealer_details(request, dealer_id):
    if request.method == "GET":
        dealer = initiate.get_dealer_by_id_from_cf(dealer_id)
        if dealer:
            return JsonResponse(dealer, safe=False)
        else:
            return JsonResponse({"status": "failed", "message": "Dealer not found"})
    return JsonResponse({"status": "failed", "message": "GET request required"})

# Create a `add_review` view to submit a review
# def add_review(request):
@csrf_exempt
def add_review(request):
    if request.method == "POST":
        review_data = json.loads(request.body)
        if not review_data:
            return JsonResponse({"status": "failed", "message": "Review data required"})
        response = initiate.post_request(review_data)
        if response.get("status") == "success":
            return JsonResponse({"status": "success", "message": "Review submitted"})
        else:
            return JsonResponse({"status": "failed", "message": "Failed to submit review"})
    return JsonResponse({"status": "failed", "message": "POST request required"})
