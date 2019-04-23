import numpy as np
import json
import requests
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

def climate_ctry_url(country):
    """Construct url based on ISO3 country code"""
    climate_url = "http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/a2/pr/2020/2039/"
    return climate_url + country

def get_ctry_recordings(country):
    """Get climate data for a particular country"""
    resp = requests.get(url=climate_ctry_url(country))
    return resp.json()

def get_figures():
    """Create a list of figures that have data and layout for plotly"""
    countries = {"col": [], "chl":[], "per":[], "cri":[]}
    figures =[]
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
    country_map = {"col": "Colombia", "chl": "Chile", "per": "Peru", "cri": "Costa Rica"}
    for country in countries:
        month_rainfall = np.zeros(len(months))
        num_recordings = 0
        for recordings in get_ctry_recordings(country):
            for index, rainfall in enumerate(recordings['monthVals']):
                month_rainfall[index] += rainfall
            num_recordings += 1
        countries[country] = (month_rainfall / num_recordings)
    
    for country in countries:
        graph = go.Bar(
            x = months,
            y = countries[country]
            )
        layout = dict(title = 'Average monthly rainfall in {} 2020 to 2039'.format(country_map[country]),
                    xaxis = dict(title = 'Month'),
                    yaxis = dict(title = 'Average monthly rainfall (milimeters)'),
                    )
        figures.append(dict(data=graph, layout=layout))
    return figures
