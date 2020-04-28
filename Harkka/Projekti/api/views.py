from django.shortcuts import render
import requests



url = 'https://data.tampere.fi/data/api/action/datastore_search?resource_id=16b6e9d3-edad-4cfe-a585-a1c6edc93e5e&'

def show_data(request):
        response = requests.get(url)
        geodata = response.json()
        geodata = geodata['result']
        geodata = geodata['records']
        cleanData = []

        viikinsaari = 0
        pyynikki = 0
        iidesjarvi = 0
        niihamajarvi = 0
        rantaperkio = 0
        vaakkolammi = 0
        tohloppi = 0

        for field in geodata:
                cleanData.append(field)
                if field['TUNNUS'] == 1:
                        viikinsaari += 1
                if field['TUNNUS'] == 2:
                        pyynikki += 1
                if field['TUNNUS'] == 3:
                        iidesjarvi += 1
                if field['TUNNUS'] == 4:
                        niihamajarvi += 1
                if field['TUNNUS'] == 5:
                        rantaperkio += 1
                if field['TUNNUS'] == 6:
                        vaakkolammi += 1
                if field['TUNNUS'] == 7:
                        tohloppi += 1


        return render(request, 'api.html', {
                        'geodata': cleanData, 'viikinsaari': viikinsaari, 'pyynikki': pyynikki, 'iidesjarvi': iidesjarvi, 'niihamajarvi': niihamajarvi,
                        'rantaperkio': rantaperkio, 'vaakkolammi': vaakkolammi, 'tohloppi': tohloppi
        })

def dashboard(request):
        response = requests.get(url)
        geodata = response.json()
        geodata = geodata['result']
        geodata = geodata['records']
        cleanData = []

        viikinsaari = 0
        pyynikki = 0
        iidesjarvi = 0
        niihamajarvi = 0
        rantaperkio = 0
        vaakkolammi = 0
        tohloppi = 0

        for field in geodata:
                cleanData.append(field)
                if field['TUNNUS'] == 1:
                        viikinsaari += 1
                if field['TUNNUS'] == 2:
                        pyynikki += 1
                if field['TUNNUS'] == 3:
                        iidesjarvi += 1
                if field['TUNNUS'] == 4:
                        niihamajarvi += 1
                if field['TUNNUS'] == 5:
                        rantaperkio += 1
                if field['TUNNUS'] == 6:
                        vaakkolammi += 1
                if field['TUNNUS'] == 7:
                        tohloppi += 1


        return render(request, 'dashboard.html', {
                        'geodata': cleanData, 'viikinsaari': viikinsaari, 'pyynikki': pyynikki, 'iidesjarvi': iidesjarvi, 'niihamajarvi': niihamajarvi,
                        'rantaperkio': rantaperkio, 'vaakkolammi': vaakkolammi, 'tohloppi': tohloppi
        })

