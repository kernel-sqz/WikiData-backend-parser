from WikiData.models import MovieInstance
from datetime import datetime
import requests


endpoint_url = "https://query.wikidata.org/sparql"

query = """SELECT DISTINCT ?movie ?imdb_id ?title ?date WHERE {
  ?movie wdt:P31 wd:Q11424;   
         wdt:P345 ?imdb_id;
         wdt:P577 ?date;      
         rdfs:label ?title.
  FILTER(YEAR(?date) > 2013)
  FILTER(LANG(?title) = "en")
}"""

headers = {
    "Accept": "application/json"
}


def getMoviesFromWiki():

    response = requests.get(endpoint_url, headers=headers, params={"query": query})
    data = response.json()
    for object in data['results']['bindings']:

        new_object = MovieInstance(
            movie= object['movie']['value'],
            imdb_id= object['imdb_id']['value'],
            title= object['title']['value'],
            date= datetime.strptime(object['date']['value'], '%Y-%m-%dT%H:%M:%SZ').date()
        )
        try:
            new_object.save()
            print(f"{object['title']['value']} ☑️")
        except:
            print(f"Object already exist, skipping... ({object['title']['value']})")