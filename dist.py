from haversine import haversine


class Finder(object):
    def __init__(self, location, name):
        self.location = location
        self.distance = 0
        self.time = (0, 0)
        self.name = name

    def distance_calculate(self, other, miles=False):
        self.distance = haversine(self.location, other.location, miles)
        return str(round(self.distance, 2)) + ' km from ' + \
            self.name + ' to ' + other.name if not miles else \
            str(round(self.distance, 2)) + ' miles from ' + \
            self.name + ' to ' + other.name + '.'

    def time_calculate(self, other):
        time1 = self.location[1] * 4
        time2 = other.location[1] * 4
        time = time1 - time2 if time1 > time2 else time2 - time1
        hours = int(time // 60)
        minutes = int(round(time % 60))
        self.time = (hours, minutes)
        return 'Time difference between ' + self.name + ' and ' + \
               other.name + ' is ' + str(self.time[0]) + ' hours and ' + \
               str(self.time[1]) + ' minutes.'


Gurgaon = Finder((28.4700, 77.0300), 'Gurgaon')
Waterloo = Finder((43.4689, -80.5400), 'Waterloo')
Delhi = Finder((28.6139, 77.2090), 'Delhi')
F2016 = Finder((1.3329, 103.7361), 'Singapore')
Googleplex = Finder((37.4184, 122.0880), 'Googleplex')

print Gurgaon.distance_calculate(Waterloo)
print Gurgaon.time_calculate(Waterloo)
print '\n'
print Gurgaon.distance_calculate(Delhi)
print Gurgaon.time_calculate(Delhi)
print '\n'
print Gurgaon.distance_calculate(F2016)
print Gurgaon.time_calculate(F2016)
print '\n'
print Gurgaon.distance_calculate(Googleplex)
print Gurgaon.time_calculate(Googleplex)
