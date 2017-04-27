from angle import Angle
import math

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
            or abs(lat.getMinutes()) < 0.0 \
            or abs(lat.getMinutes()) >= 60.0:
            raise ValueError('latitude out of range: %s' % str(lat))
        self.lat = lat

    def getLatitude(self):
        return self.lat

    def setLongitude(self, lon):
        if float(lon) < 0.0 \
            or float(lon) >= 360.0 \
            or abs(lon.getMinutes()) < 0.0 \
            or abs(lon.getMinutes()) >= 60.0:
            raise ValueError('longitude out of range: %s' % str(lon))
        self.lon = lon

    def getLongitude(self):
        return self.lon

    def setAltitude(self, alt):
        if float(alt) <= 0.0 \
            or float(alt) >= 90.0 \
            or abs(alt.getMinutes()) < 0.0 \
            or abs(alt.getMinutes()) >= 60.0:
            raise ValueError('altitude out of range: %s' % str(alt))
        self.alt = alt

    def getAltitude(self):
        return self.alt

    def setAssumedLatitude(self, assLat):
        if float(assLat) <= -90.0 \
            or float(assLat) >= 90.0 \
            or abs(assLat.getMinutes()) < 0.0 \
            or abs(assLat.getMinutes()) >= 60.0:
            raise ValueError('assumed latitude out of range: %s' % str(assLat))
        self.assLat = assLat

    def getAssumedLatitude(self):
        return self.assLat

    def setAssumedLongitude(self, assLon):
        if float(assLon) < 0.0 \
            or float(assLon) >= 360.0 \
            or abs(assLon.getMinutes()) < 0.0 \
            or abs(assLon.getMinutes()) >= 60.0:
            raise ValueError('assumed longitude out of range: %s' %
                str(assLon))
        self.assLon = assLon

    def getAssumedLongitude(self):
        return self.assLon

    def intermediateDistance(self):
        return (math.sin(math.radians(self.getLatitude())) \
            * math.sin(math.radians(self.getAssumedLatitude()))) \
            + (math.cos(math.radians(self.getLatitude())) \
            * math.cos(math.radians(self.getAssumedLatitude())) \
            * math.cos(math.radians(float(self.getLongitude()) \
            + float(self.getAssumedLongitude()))))

    def correctedDistance(self):
        return int((math.degrees(math.asin(self.intermediateDistance()))
            - float(self.getAltitude())) * 60)

    def correctedAzimuth(self):
        return Angle(math.degrees(math.acos((math.sin(
            math.radians(self.getLatitude()))
            - (math.sin(math.radians(self.getAssumedLatitude()))
            * self.intermediateDistance()))
            / (math.cos(math.radians(self.getAssumedLatitude()))
            * math.cos(math.asin(self.intermediateDistance()))))))
