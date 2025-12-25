import geocoder

def get_gps_location():
    g = geocoder.ip('me')

    if g.ok:
        return g.latlng[0], g.latlng[1]
    else:
        return None, None
