millimeter = 1000
centimeter = 100
meter = 1
kilometer = 0.001
inch = 39.3700787
feet = 3.2808399
yard = 1.0936133
mile = 0.000621371192

value = float(input())
input_units = input()
output_units = input()

# Calculate value in meters
metric_units = value
if input_units == 'mm':
    metric_units /= millimeter
elif input_units == 'cm':
    metric_units /= centimeter
elif input_units == 'm':
    metric_units /= meter
elif input_units == 'km':
    metric_units /= kilometer
elif input_units == 'in':
    metric_units /= inch
elif input_units == 'ft':
    metric_units /= feet
elif input_units == 'yd':
    metric_units /= yard
elif input_units == 'mi':
    metric_units /= mile

# Calculate from meters to wanted units
if output_units == 'mm':
    metric_units *= millimeter
elif output_units == 'cm':
    metric_units *= centimeter
elif output_units == 'm':
    metric_units *= meter
elif output_units == 'km':
    metric_units *= kilometer
elif output_units == 'in':
    metric_units *= inch
elif output_units == 'ft':
    metric_units *= feet
elif output_units == 'yd':
    metric_units *= yard
elif output_units == 'mi':
    metric_units *= mile

print(f'{metric_units} {output_units}')
