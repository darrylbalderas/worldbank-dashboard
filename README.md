# worldbank-dashboard

## Table of Contents
1. [Motivation](#motivation)
2. [Installation](#installation)

## Motivation <a name="motivation"></a>


Display a web-based dashboard to show data from [worldbank website](https://data.worldbank.org/)

Looking at information for mostly free and free economy countries. The [list of rankings](https://www.heritage.org/index/ranking) for countries based on their free economy

Here is the link to the [dashboard](https://worldbank-dash.herokuapp.com/)

Using [heroku](https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true) to host my dashboard

### Countries that I will be analyzing
- Hong Kong
- Singapore
- New Zealand
- Switzerland
- Australia
- Ireland
- United Kingdom
- Denmark
- Chile
- Sweden
- Finland
- Germany
- Norway
- Israel
- South Korea
- Japan
- Austria



## Installation <a name="installation"></a>

- Create a python3 virtual environment

    `python3 -m venv ./venv `

- Start virtual environment

    `source venv/bin/activate`

- Stop virtual environment

    `deactivate`

- Install project dependencies 

    > (virtual env must be started to install dependencies)
     
    `pip install -r requirements.txt`
    
- Start notebook 
     
    `jupyter notebook survey-analysis.ipynb`
