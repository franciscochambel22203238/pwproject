from django.shortcuts import render
import requests


def landing_page_view(request):

    previsao_url = "https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json"
    previsao_response = requests.get(previsao_url)
    previsao_data = previsao_response.json()
    hoje_previsao = previsao_data['data'][0]

    id_weather_type = hoje_previsao['idWeatherType']
    icone_animated = f'meteo/w_ic_d_{id_weather_type:02d}anim.svg'

    context = {
        'icone_animated': icone_animated
    }
    return render(request, 'portfolio/landing_page.html', context)

def meByMe_view(request):

    previsao_url = "https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json"
    previsao_response = requests.get(previsao_url)
    previsao_data = previsao_response.json()
    hoje_previsao = previsao_data['data'][0]

    id_weather_type = hoje_previsao['idWeatherType']
    icone_animated = f'meteo/w_ic_d_{id_weather_type:02d}anim.svg'

    context = {
        'icone_animated': icone_animated
    }

    return render(request, 'portfolio/meByme.html', context)