from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import WeightRecord
import json
from django.views.decorators.http import require_POST

def index(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse("Invalid login details")
    else:
        return render(request, 'login.html')

@csrf_exempt
@require_POST
def record_weight(request):
    try:
        data = json.loads(request.body)
        weight = data.get('weight')
        percentage = data.get('percentage')

        if weight is None or percentage is None:
            return JsonResponse({'status': 'error', 'message': 'Invalid data'}, status=400)

        # Save the data to the database
        WeightRecord.objects.create(weight=weight, percentage=percentage)
        
        return JsonResponse({'status': 'success', 'message': 'Record saved'}, status=201)

    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)

def dashboard(request):
    return render(request, 'dashboard.html')

def get_iv_percentage(request):
    # Assuming you're fetching the latest weight record
    latest_record = WeightRecord.objects.last()
    print(latest_record)

    # If no records are available, set a default percentage
    percentage = int(latest_record.percentage) if latest_record else 0

    # Return the data as JSON
    return JsonResponse({'percentage': percentage})




def logout_view(request):
    logout(request)
    return redirect('home')

