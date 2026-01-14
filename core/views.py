from django.shortcuts import render, redirect
from .data import cars
from .bought_data import bought_cars
from datetime import date

def index(request):
    filtered_cars = cars

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    company = request.GET.get('company')
    model = request.GET.get('model')
    search = request.GET.get('search')

    if min_price:
        filtered_cars = [c for c in filtered_cars if c['price'] >= int(min_price)]
    if max_price:
        filtered_cars = [c for c in filtered_cars if c['price'] <= int(max_price)]
    if company:
        filtered_cars = [c for c in filtered_cars if c['company'] == company]
    if model:
        filtered_cars = [c for c in filtered_cars if c['model'] == model]
    if search:
        filtered_cars = [
            c for c in filtered_cars
            if search.lower() in c['model'].lower()
        ]

    companies = sorted(set(c['company'] for c in cars))
    models = sorted(set(c['model'] for c in cars))

    return render(request, 'index.html', {
        'cars': filtered_cars,
        'companies': companies,
        'models': models
    })


def buy_car(request):
    if request.method == 'POST':
        bought_cars.append({
            "company": request.POST['company'],
            "model": request.POST['model'],
            "buy_price": request.POST['price'],
            "mileage": request.POST['mileage'],
            "color": request.POST['color'],
            "buy_date": date.today()
        })
        return redirect('buy')

    companies = sorted(set(c['company'] for c in cars))
    models = sorted(set(c['model'] for c in cars))

    return render(request, 'buy.html', {
        'companies': companies,
        'models': models,
        'bought_cars': bought_cars
    })