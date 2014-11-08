from django.shortcuts import render

from django.conf import settings
import foursquare
from .forms import LocationForm
from .models import Place

def home(request, tmpl='places/home.html'):
    data = {}
    place_list = Place.objects.all()
    data['place_list'] = place_list
    return render(request, tmpl, data)

def around(request, tmpl='places/around.html'):
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
        list_venues = client.venues.search(params={'ll': '%s,%s' % (lat, lng),  'radius': rad, 'categoryId':'4d4b7105d754a06374d81259'})
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


                # print (list_venues)
                # for venue in list_venues:
                # print venue.name
                place_list.append(pl)


                # data['venue'] = list_venues
        data['place_list'] = place_list
        data['places_count'] = len(place_list)
    return render(request, tmpl, data)

from django.shortcuts import get_object_or_404
def detail(request, uid, tmpl='places/detail.html'):
    data = {}

    place = get_object_or_404(Place, uuid=uid)

    data['place'] = place

    return render(request, tmpl, data)