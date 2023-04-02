# Programme qui convertisse en degrés Celsius une température exprimée au départ en degrés Fahrenheit, ou l’inverse.
# La formule de conversion est : TF =TC ×1,8+32

temperature_fahrenheit = 83.8
temperature_celcius = (temperature_fahrenheit-32) / 1.8

print(temperature_fahrenheit,"°F =",temperature_celcius,"°C")