from angle import Angle

class Correction(object):

    def __init__(self, lat, lon, alt, assLat, assLon):
        self.setLatitude(lat)
        self.setLongitude(lon)
        self.setAltitude(alt)
        self.setAssumedLatitude(assLat)
        self.setAssumedLongitude(assLon)

    def setLatitude(self, lat):
        if float(lat) <= -90.0 \
            or float(lat) >= 90.0 \
            or lat.getMinutes() < 0 \
            or lat.getMinutes() >= 60:
            raise ValueError('latitude out of range: %s' % str(lat))
        self.lat = lat

    def getLatitude(self):
        return self.lat

    def setLongitude(self, lon):
        if float(lon) < 0.0 \
            or float(lon) >= 360.0 \
            or lon.getMinutes() < 0 \
            or lon.getMinutes() >= 60:
            raise ValueError('longitude out of range: %s' % str(lon))
        self.lon = lon

    def getLongitude(self):
        return self.lon

    def setAltitude(self, alt):
        if float(alt) <= 0.0 \
            or float(alt) >= 90.0 \
            or alt.getMinutes() < 0 \
            or alt.getMinutes() >= 60:
            raise ValueError('altitude out of range: %s' % str(alt))
        self.alt = alt

    def getAltitude(self):
        return self.alt

    def setAssumedLatitude(self, assLat):
        if float(assLat) <= -90.0 \
            or float(assLat) >= 90.0 \
            or assLat.getMinutes() < 0 \
            or assLat.getMinutes() >= 60:
            raise ValueError('assumed latitude out of range: %s' % str(assLat))
        self.assLat = assLat

    def getAssumedLatitude(self):
        return self.assLat

    def setAssumedLongitude(self, assLon):
        if float(assLon) < 0.0 \
            or float(assLon) >= 360.0 \
            or assLon.getMinutes() < 0 \
            or assLon.getMinutes() >= 60:
            raise ValueError('assumed longitude out of range: %s' %
                str(assLon))
        self.assLon = assLon

    def getAssumedLatitude(self):
        return self.assLon
