from django.shortcuts import render, redirect

from django.conf import settings
import foursquare
from .forms import LocationForm
from .models import Place
from django.db.models import QuerySet

def home(request, tmpl='places/home.html'):
    data = {}
    place_list = Place.objects.all()
    data['place_list'] = place_list
    return render(request, tmpl, data)


def around(request, tmpl='places/around.html'):
    data = {}
    # loc_form = LocationForm(request.GET or None)
    # print loc_form.is_valid()

    # place_list = []

    # if loc_form.is_valid():
    #     frm = loc_form.cleaned_data

    lat = request.GET.get('lat')
    lng = request.GET.get('lng')
    rad = request.GET.get('radius')

    if not lat and not lng:
        return redirect('places_home')

    client = foursquare.Foursquare(client_id=settings.YOUR_CLIENT_ID, client_secret=settings.YOUR_CLIENT_SECRET)

    # list_venues = client.venues.search(params={'ll': '%s,%s' % (lat, lng), 'radius':1000})
    list_venues = client.venues.search(
        params={'ll': '%s,%s' % (lat, lng), 'radius': rad, 'categoryId': '4d4b7105d754a06374d81259'})
    # list_venues = client.venues.search(params={'ll': '%s,%s' % (lat, lng), 'categoryId':'4d4b7105d754a06374d81259'})
    place_list = []
    # pl_dict = QueryDict

    venue_list = []

    for v in list_venues['venues']:
        vid = v['id']
        vname = v['name']

        lct = v['location']
        vlat = lct['lat']
        vlng = lct['lng']
        vdist = lct['distance']

        try:
            pl = Place.objects.get(venue_uid=vid)
        except Place.DoesNotExist:
            pl = Place.objects.create(venue_uid=vid, name=vname, lat=vlat, lng=vlng)
        pl.dist = vdist
        place_list.append(pl)
        vurl = pl.get_absolute_url()
        # print pl.get_absolute_url()

        # print type(vurl

        venue = {'name': vname, 'lat': vlat, 'lng': vlng, 'dist': vdist, 'url': vurl, 'outlets': pl.has_outlets()}
        venue_list.append(venue)
            # pl.distance = lct['distance']
            # # print (list_venues)
            # # for venue in list_venues:
            # # print venue.name
            # place_list.append(pl)


            # data['venue'] = list_venues

    # for key, value in sorted(venue_list.iteritems(), key=lambda (k,v): (v,k)):
    # print "%s: %s" % (key, value)
    if request.is_ajax():
        from django.http import HttpResponse
        import json
        # print place_list
        # place_list = list(Place.objects.values('venue_uid', 'name', 'uuid'))
        # place_list = pl.values('venue_uid', 'name', 'uuid')
        # place_list = list(place_list)
        # # place_list = list(Place.objects.values('venue_uid', 'name', 'uuid'))
        #
        # # for p in place_list:

        pl_data = {'count': len(venue_list), 'places': venue_list}
        # return HttpResponse(place_list)
        # print json.dumps(place_list)

        return HttpResponse(json.dumps(pl_data), content_type="application/json")

    data['place_list'] = place_list
    data['places_count'] = len(place_list)
    return render(request, tmpl, data)


from django.shortcuts import get_object_or_404

from .forms import CommentForm, Comment
def detail(request, uid, tmpl='places/detail.html'):
    data = {}
    client = foursquare.Foursquare(client_id=settings.YOUR_CLIENT_ID, client_secret=settings.YOUR_CLIENT_SECRET)

    place = get_object_or_404(Place, uuid=uid)
    venue = client.venues(place.venue_uid)

    cmnt = Comment(place=place)

    comment_form = CommentForm(request.POST or None, instance=cmnt)
    print comment_form.errors
    if comment_form.is_valid():
        cmnt = comment_form.save()
        return redirect(place.get_absolute_url())


    data['place'] = place
    data['venue'] = venue['venue']
    data['comment_form'] = comment_form

    # data["category"] = venue["category"]

    return render(request, tmpl, data)



def outlet(request, uid, act):
    data = {}

    place = get_object_or_404(Place, uuid=uid)
    if act == '+':
        place.outlet_yes += 1
    if act == '-':
        place.outlet_no +=1
    place.save()

    return redirect(place.get_absolute_url())