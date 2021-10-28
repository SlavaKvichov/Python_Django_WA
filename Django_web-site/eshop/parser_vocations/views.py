from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def parser(request):
    return render(request, 'parser/parser.html', {
        'page': 'parser'
    })

def parser_search(request):
    keyword = request.GET.get('keyword')
    RABOTA_UA = 'https://api.rabota.ua/vacancy/search'
    RABOTA_UA += '?keyWords={}'.format(keyword)
    rabota_ua = requests.get(RABOTA_UA).json()
    vacancies_rb = rabota_ua.get('documents', [])
    return render(request, 'parser/parser.html', {
        'key': keyword,
        'page': 'parser',
        'vacancies_rb': vacancies_rb
    })
