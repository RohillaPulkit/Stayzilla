from django.shortcuts import render
from django.http import JsonResponse


def dashboard(request):
    return render(request, "dashboard/base.html", {})


def get_chart_data(request):
    labels = ["January", "February", "March", "April", "Nay", "June", "July", "August", "September", "October",
              "November", "December"]
    default_items = [123, 456, 145, 345, 365, 444, 523, 678, 769, 986, 125, 756]
    data = {
        "labels": labels,
        "def": default_items,
    }
    return JsonResponse(data)


def get_table_data(request):
    city = ["New york", "seattle", "penn state", "abc", "xyz"]
    percent = [123, 456, 145, 345, 365]
    dicts = [{
        'city': 'New York',
        'percent': 100
    }, {
        'city': 'Seattle',
        'percent': 90
    }, {
        'city': 'PennState',
        'percent': 50
    }, {
        'city': 'Florida',
        'percent': 60
    },
        {
            'city': 'PennState',
            'percent': 50
        },
        {
            'city': 'PennState',
            'percent': 50
        },
        {
            'city': 'PennState',
            'percent': 50
        },
        {
            'city': 'PennState',
            'percent': 50
        },
        {
            'city': 'PennState',
            'percent': 50
        },
        {
            'city': 'PennState',
            'percent': 50
        },
        {
            'city': 'PennState',
            'percent': 50
        },
    ]
    data = {
        'cities': city,
        'percents': percent,
    }
    return render(request, "dashboard/table1.html", {"data": dicts})
