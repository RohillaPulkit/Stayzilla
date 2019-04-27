from django.shortcuts import render
from django.http import JsonResponse
from dashboard.database.dbmanager import DBManager


def dashboard(request):
    return render(request, "dashboard/base.html", {})


def get_chart_data(request):
    chart_data = DBManager.get_chart_data()
    print(chart_data)
    months = []
    bookings = []
    for item in chart_data:
        mont = item.MONT
        booking = item.BOOKING
        months.append(mont)
        bookings.append(booking)

    data = {}
    data['months'] = months
    data['bookings'] = bookings
    return JsonResponse(data, safe=False)


def get_table_data(request):
    location_data = DBManager.get_location_percent()
    print(location_data)
    return render(request, "dashboard/table1.html", {"location_data": location_data})


def get_pie_graph_data(request):
    single_private_room_data = DBManager.get_single_private_room_data()
    entire_apt_data = DBManager.get_entire_apt_data()
    single_shared_room_data = DBManager.get_single_shared_room_data()
    pie_data={}
    pie_data['labels'] = ['Single Private Room', 'Entire Apartment', 'Single Shared Rooms']
    pie_data['data'] = [single_private_room_data, entire_apt_data, single_shared_room_data]
    print(pie_data)
    return JsonResponse(pie_data, safe=False)


def get_table2_data(request):
    # location_data = DBManager.get_location_percent()
    # print(location_data)
    # return render(request, "dashboard/table1.html", {"location_data": location_data})
    table2_data = [{"parameter": "abc", "values": "123"}, {"parameter": "xyz", "values": "456"}, {"parameter": "abc", "values": "123"}, {"parameter": "abc", "values": "123"}]

    print(table2_data)
    return render(request, "dashboard/table2.html", {"table2_data": table2_data})


def get_table3_data(request):
    # location_data = DBManager.get_location_percent()
    # print(location_data)
    # return render(request, "dashboard/table1.html", {"location_data": location_data})
    table3_data = [{"param1": "abc", "param2": "123", "param3": "abc", "param4": "123"}, {"param1": "abc", "param2": "123", "param3": "abc", "param4": "123"}, {"param1": "abc", "param2": "123", "param3": "abc", "param4": "123"}, {"param1": "abc", "param2": "123", "param3": "abc", "param4": "123"}]
    print(table3_data)
    return render(request, "dashboard/table3.html", {"table3_data": table3_data})


def get_chart3(request):

    chart3_data = {}
    chart3_data['label'] = ['one', 'two', 'three']
    chart3_data['data'] = [1, 2, 3]
    print(chart3_data)
    return JsonResponse(chart3_data, safe=False)
