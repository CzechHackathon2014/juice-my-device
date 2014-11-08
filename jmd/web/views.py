from django.shortcuts import render
from places.forms import LocationForm
# Create your views here.
def home(request, tmpl='web/home.html'):
    data = {}

    loc_form = LocationForm(request.POST or None)

    data['locaction_form'] = loc_form

    return render(request, tmpl, data)


from django.conf import settings

import foursquare
from places.models import Place

FOOD_CATEGORY = '4d4b7105d754a06374d81259'
def venues(request, tmpl='web/frsq.html'):
    data = {}
    loc_form = LocationForm(request.GET or None)
    # print loc_form.is_valid()

    if loc_form.is_valid():
        frm = loc_form.cleaned_data

        lat = frm.get('lat')
        lng = frm.get('lng')
        rad = frm.get('radius')

        client = foursquare.Foursquare(client_id=settings.YOUR_CLIENT_ID, client_secret=settings.YOUR_CLIENT_SECRET)

        # list_venues = client.venues.search(params={'ll': '%s,%s' % (lat, lng), 'radius':1000})
        list_venues = client.venues.search(params={'ll': '%s,%s' % (lat, lng),  'radius': rad, 'categoryId':FOOD_CATEGORY})
        # list_venues = client.venues.search(params={'ll': '%s,%s' % (lat, lng), 'categoryId':'4d4b7105d754a06374d81259'})

        place_list = []

        for v in list_venues['venues']:
            lct = v['location']
            # print lct['lng']
            try:
                pl = Place.objects.get(venue_uid=v['id'])
                place_list.append(pl)
            except Place.DoesNotExist:
                pl = Place.objects.create(venue_uid=v['id'], name=v['name'], lat=lct['lat'], lng=lct['lng'])

                pl.distance = lct['distance']
                # print (list_venues)
                # for venue in list_venues:
                # print venue.name
                place_list.append(pl)


                # data['venue'] = list_venues
        data['place_list'] = place_list
        data['places_count'] = len(place_list)
    return render(request, tmpl, data)


def frsq(request, tmpl='web/frsq.html'):
    data = {}

    # client = foursquare.Foursquare(client_id=settings.YOUR_CLIENT_ID, client_secret=settings.YOUR_CLIENT_SECRET, redirect_uri='http://localhost:8000/frsq/done/')
    # auth_uri = client.oauth.auth_url()

    client = foursquare.Foursquare(client_id=settings.YOUR_CLIENT_ID, client_secret=settings.YOUR_CLIENT_SECRET)


    # venues = client.venues.search(params={'query': 'coffee'})
    venues = client.venues('40a55d80f964a52020f31ee3')

    print venues
    # print auth_uri
    data['venue'] = venues
    return render(request, tmpl, data)