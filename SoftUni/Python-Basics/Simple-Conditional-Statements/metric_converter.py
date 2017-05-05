millimeter = 1000
centimeter = 100
meter = 1
kilometer = 0.001
inch = 39.3700787
feet = 3.2808399
yard = 1.0936133
mile = 0.000621371192

value = float(input())
inputUnits = input()
outputUnits = input()

# Calculate value in meters
metricUnits = value
if inputUnits == 'mm':
    metricUnits /= millimeter
elif inputUnits == 'cm':
    metricUnits /= centimeter
elif inputUnits == 'm':
    metricUnits /= meter
elif inputUnits == 'km':
    metricUnits /= kilometer
elif inputUnits == 'in':
    metricUnits /= inch
elif inputUnits == 'ft':
    metricUnits /= feet
elif inputUnits == 'yd':
    metricUnits /= yard
elif inputUnits == 'mi':
    metricUnits /= mile

# Calculate from meters to wanted units
if outputUnits == 'mm':
    metricUnits *= millimeter
elif outputUnits == 'cm':
    metricUnits *= centimeter
elif outputUnits == 'm':
    metricUnits *= meter
elif outputUnits == 'km':
    metricUnits *= kilometer
elif outputUnits == 'in':
    metricUnits *= inch
elif outputUnits == 'ft':
    metricUnits *= feet
elif outputUnits == 'yd':
    metricUnits *= yard
elif outputUnits == 'mi':
    metricUnits *= mile

print ('{0} {1}'.format(metricUnits, outputUnits))
