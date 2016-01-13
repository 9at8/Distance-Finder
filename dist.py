from haversine import haversine


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
Waterloo = Finder((43.4689, -80.5400), 'Waterloo')
Delhi = Finder((28.6139, 77.2090), 'Delhi')
F2016 = Finder((1.3329, 103.7361), 'Singapore')
Googleplex = Finder((37.4184, -122.0880), 'Googleplex')

print Gurgaon.distance_calculate(Waterloo)
print Gurgaon.time_calculate(Waterloo)
print '\n'
print Gurgaon.distance_calculate(Delhi)
print Gurgaon.time_calculate(Delhi)
print '\n'
print Gurgaon.distance_calculate(F2016)
print Gurgaon.time_calculate(F2016)
print '\n'
print Gurgaon.distance_calculate(Googleplex, miles=True)
print Gurgaon.time_calculate(Googleplex)
