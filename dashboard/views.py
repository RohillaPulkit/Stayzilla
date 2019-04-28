from django.shortcuts import render
from django.http import JsonResponse
from dashboard.database.dbmanager import DBManager


def dashboard(request):
    all_states = DBManager.get_states()
    return render(request, "dashboard/base.html", {'all_states': all_states})


def get_chart_data(request):
    selected_state = request.GET['selected_state']
    print(selected_state)

    chart_data = DBManager.get_chart_data(selected_state)
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
    selected_state = request.GET['selected_state']
    print(selected_state)

    single_private_room_data = DBManager.get_single_private_room_data(selected_state)
    entire_apt_data = DBManager.get_entire_apt_data(selected_state)
    single_shared_room_data = DBManager.get_single_shared_room_data(selected_state)
    pie_data={}
    pie_data['labels'] = ['Single Private Room', 'Entire Apartment', 'Single Shared Rooms']
    pie_data['data'] = [single_private_room_data, entire_apt_data, single_shared_room_data]
    print(pie_data)
    return JsonResponse(pie_data, safe=False)


def get_table2_data(request):

        best_state = DBManager.get_best_state()
        best_listing = DBManager.get_best_listing()
        best_host = DBManager.get_best_host()
        least_avail = DBManager.get_least_available()
        table2_data = [{"parameter": "Best state to visit in most ideal month", "values": best_state}, {"parameter": "Best listing with lowest price per night and highest rating", "values": best_listing}, {"parameter": "Host with highest booking", "values": best_host}, {"parameter": "Host with most available listing", "values": least_avail}]
        print(table2_data)
        return render(request, "dashboard/table2.html", {"table2_data": table2_data})


def get_table3_data(request):
    info_data = DBManager.get_info_table_data()

    data = []
    for item in info_data:
        dict_data = {'name': item.NAME, 'count': item.COUNT}
        data.append(dict_data)


    print(data)
    return render(request, "dashboard/table3.html", {"info_data": data})


def get_chart3(request):

    chart3_data = {}
    chart3_data['label'] = ['one', 'two', 'three']
    chart3_data['data'] = [1, 2, 3]
    print(chart3_data)
    return JsonResponse(chart3_data, safe=False)
