from haversine import haversine


# -> Calculate the distance between 2 points on Earth.
# -> Calculate the distance (in km or in miles) between two points on Earth,
#       located by their latitude and longitude.
# -> haversine takes a tuple of gps co-ordinates as parameters and returns
#       distance in kilometers (miles if miles is passed as true)
# -> hav(d / r) = hav(w2 - w1) + { cos(w2).cos(w1).hav(l2 - l1) }
# ------------------------Assumptions and other things------------------------
# -> Earth is a perfect sphere
# -> hav(c) = sin^2 (c / 2)
# -> d is the distance between the two points
# -> r is the radius of earth
# -> w1, w2 = latitudes of point 1 and point 2 respectively
# -> l1, l2 = latitudes of point 1 and point 2 respectively
# -> All angles are measured in radians,
#       so we have to convert latitudes and longitudes

class Finder(object):
    def __init__(self, location, name):
        # location is a tuple of GPS Coordinates
        self.location = location
        self.distance = 0
        self.time = 0
        self.name = name

    def distance_calculate(self, other, miles=False):
        # other is an object of class Finder
        self.distance = haversine(self.location, other.location, miles)
        # using haversine module to get the distance
        # conditional return: returns distance in miles if miles is True;
        #                     returns distance in kilometer by default.
        return str(round(self.distance, 2)) + ' km from ' + \
            self.name + ' to ' + other.name + '.' if not miles else \
            str(round(self.distance, 2)) + ' miles from ' + \
            self.name + ' to ' + other.name + '.'

    def time_calculate(self, other):
        # other is an object of class Finder
        # The earth is divided into 360 longitudes
        #   When it completes 24 hours, it revolves 360 degrees
        #   So time taken to cover 1 degree = 24/360 hours or 4 minutes
        time1 = self.location[1] * 4
        # time1 is the time difference of self from GMT. (minutes)
        time2 = other.location[1] * 4
        # time2 is the time difference of other from GMT. (minutes)
        time = time1 - time2 if time1 > time2 else time2 - time1
        # Conditional Assignment of time: for maintaining positive
        #                                 value of time (minutes)
        hours = int(time // 60)
        # hours = floor division of minutes by 60 (integer)
        minutes = int(round(time % 60))
        # minutes = modulus of time by 60 (integer)(round figure)
        self.time = (hours, minutes)
        # self.time = tuple of hours and minutes
        # returns time difference
        return 'Time difference between ' + self.name + ' and ' + \
               other.name + ' is ' + str(self.time[0]) + ' hours and ' + \
               str(self.time[1]) + ' minutes.'


# -------------------------------Test data------------------------------------
Gurgaon = Finder((28.4700, 77.0300), 'Gurgaon')
# Gurgaon is a city in India. It comes under NCR (Near Capital Region).
Waterloo = Finder((43.4689, -80.5400), 'Waterloo')
# Waterloo is in Canada, near Toronto.
Delhi = Finder((28.6139, 77.2090), 'Delhi')
# Delhi is the Capital of India
F2016 = Finder((1.3329, 103.7361), 'Singapore')
# Singapore is the venue for the FOSSASIA annual conference (2016).
Googleplex = Finder((37.4184, -122.0880), 'Googleplex')
# Googleplex is the GoogleHQ.

# Distance and Time between Waterloo and Gurgaon.
print Gurgaon.distance_calculate(Waterloo)
print Gurgaon.time_calculate(Waterloo)
print '\n'
# Distance and Time between Delhi and Gurgaon.
print Gurgaon.distance_calculate(Delhi)
print Gurgaon.time_calculate(Delhi)
print '\n'
# Distance and Time between Singapore and Googleplex.
print F2016.distance_calculate(Googleplex)
print F2016.time_calculate(Googleplex)
print '\n'
# Distance and Time between Singapore and Googleplex. (in miles)
print F2016.distance_calculate(Googleplex, miles=True)
print F2016.time_calculate(Googleplex)
