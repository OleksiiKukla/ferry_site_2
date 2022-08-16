import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from datetime import datetime
from .models import Ferry, Port
from django.views.generic import ListView, DetailView

def parser_polferries():
    '''Parser timetable https://polferries.pl/cargo/rozklad.html?code=sy '''

    utl = 'https://polferries.pl/cargo/rozklad.html?code=sy'

    r = requests.get(utl)
    soup = BeautifulSoup(r.text, 'lxml')
    find_month = soup.find('ul', class_='nav nav-tabs')
    month = []

    for items in find_month:
        month.append(items.get_text())

    month_list = []

    for i in month:             # выделяем в словарь месяц и год
        month_in_polish = {'Styczeń' : 1,
                           "Luty": 2,
                           'Marzec': 3,
                           'Kwiecień': 4,
                           'Maj': 5,
                           'Czerwiec': 6,
                           'Lipiec': 7,
                           'Sierpień': 8,
                           'Wrzesień': 9,
                           'Październik': 10,
                           'Listopad': 11,
                           'Grudzień': 12}
        word = "".join(" " if el.isdigit() else el for el in i).split()
        number = "".join(el if el.isdigit() else " " for el in i).split()
        word = month_in_polish[word[0]]

        month_list.append([word, number[0]])

    name_of_ferry_dir = {
        'BAL': 'Baltivia',
        'CRA': 'Cracovia',
        'MAZ': 'Mazovia'
    }
    find_all_table = soup.find_all('div', class_='tab-content')         #выделяем 2 таблицы

    for div_num in range(len(find_all_table)):
        find_all_month = find_all_table[div_num].find_all('div', class_='panel-collapse')  # находим месяца
        for month_num in range(len(find_all_month)):
            all_str_table = find_all_month[month_num].find('table', class_='rozklad-tabela').find_all('tr')  #в каждой таблице выделяем строки
            for one_str_of_table_num in range(len(all_str_table)):      # проходим строки таблицы
                if one_str_of_table_num == 1:
                    arrival_sailing = all_str_table[one_str_of_table_num].find('td')
                    arrival_sailing = arrival_sailing.get_text()
                    arrival_sailing = arrival_sailing.split('-')
                    arrival = arrival_sailing[1].replace(' ', '')
                    sailing = arrival_sailing[0].replace(' ', '')

                if one_str_of_table_num >= 2:
                    date_time_ferry = all_str_table[one_str_of_table_num].find_all('td')
                    for day in range(len(date_time_ferry)):                 # проходим дни по каждой строке таблицы
                        if day == 0:                            # находим время прибытия отплытия
                            time_arrival_sailing = date_time_ferry[day].get_text().split(' - ')
                            time_arrival = time_arrival_sailing[1]
                            time_sailing = time_arrival_sailing[0]

                        else:                                           # при наличии создаем обьект
                            if date_time_ferry[day].get_text():
                                name_one = date_time_ferry[day].get_text()
                                date_ferry = f'{month_list[month_num][1]}-{month_list[month_num][0]}-{day}'
                                name_ferry = name_of_ferry_dir[name_one]
                                # print(name_ferry, date_ferry , time_sailing, time_arrival, sailing, arrival)
                                a = Ferry.objects.create(name = name_ferry, date = date_ferry , time_departure = time_sailing, time_arrival = time_arrival, port_departure = sailing, port_arrival = arrival )
                                a.save()


def ferry_home(request):
    return render(request, 'timetable/ferry_home.html')



def ferry_timetable(request, country_departure:str , country_arrival:str):
    country_arrival = Port.objects.get(country=country_arrival)
    port_arrival = country_arrival.name
    current_datetime = datetime.now()
    date = f'{current_datetime.year}-{current_datetime.month}-{current_datetime.day}'
    ferries = Ferry.objects.all()
    ferries = ferries.filter(port_arrival = port_arrival).filter(date__gte = date).order_by('date')[:10]
    port_departure = Port.objects.get(country=country_departure)
    port_departure = port_departure.name
    return render(request, 'timetable/ferry_timetable.html', context={'ferries':ferries, 'departure': country_departure, 'arrival': country_arrival})


