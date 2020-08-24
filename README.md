# pizero-weather
## Display Time &amp; Weather on Pi Zero e-Paper Display
![Weather](https://github.com/DennisFaucher/pizero-weather/blob/master/images/now.jpg)
![Forecast](https://github.com/DennisFaucher/pizero-weather/blob/master/images/forecast.jpg)

This is a slight modification to my Holiday Greetings repo https://github.com/DennisFaucher/pizero-epaper-greetings. I built this beautiful e-Paper Pi Zero with battery to use as a pwnagotchi and then as an automagic holiday greetings badge.  It was time for something new. How about the time and weather (alternating current and forecast) so large that maybe I could even make it out without my reading glasses? Sure, why not. 
 
 ## Hardware
 Raspberry Pi Zero W. WITH PINS as I am terrible at soldering. I purchased mine here: https://www.aliexpress.com/item/32979703845.html

Waveshare 2.13" e-Paper Dsiplay HAT. I purchased mine here: https://www.aliexpress.com/item/32810080308.html
 
 ## Software
 ### Raspian
 Install Raspbian OS from here https://www.raspberrypi.org/downloads/raspbian/ and use these instructions: https://www.raspberrypi.org/documentation/installation/installing-images/README.md

Connect your Raspberry Pi Zero (rPi) to keyboard, mouse, HDMI monitor and power to run through the usual Linux setup. I picked up all the necessary cable/power accesories here: https://www.sparkfun.com/products/14298

### e-Paper Drivers
Install the Waveshare e-Paper drivers using these instructions: https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT. Rename the awfully named directory "RaspberryPi&JetsonNano" to just "Pi".

### Weather Forecast
I'm using OpenWeatherMap JSON for my forecasts as the API is free for up to 1,000 calls a day.

I could have called the API directly from the Pi Zero with python, but I am lazy and Node-Red makes parsing JSON *so* easy. Install Node-Red from [here](https://nodered.org/) and feel free to use my flow export which you can find [here](https://github.com/DennisFaucher/pizero-weather/blob/master/weather_large.json). Change the OpenWeatherMap API to your personal API. This flow writes a weather text file to my web server every 15 minutes which the python script running on the Pi Zero picks up for display.

### Python Script
The script is pretty simple and based on the e-Paper examples. From a high level the script:

* Initalized the e-Paper display
* Gets the current time into a variable
* Gets the current weather into a variable
* Gets the weather forecast into a variable
* Defines font sizes
* Draws borders
* Alternates between time + current conditions and time + forecast every 10 seconds

Not very elegant, but gets the job done

### Copy files into place
Import my weather flow into your node-red. Change the OpenWeatherMap API as well as the fiel save location for einklarge.txt.

Copy my weatherbig.py to your rPi in the directory /home/pi/e-Paper/Pi/python/examples. Change as needed to pull your copy of einklarge.txt.

### Autostart
Add this entry into /etc/rc.local on your rPi

python3 /home/pi/e-Paper/Pi/python/examples/weatherbig.py  > /dev/null 2>&1 &

reboot

Enjoy!

Demo video [here](https://youtu.be/eoPMCVJt_kg)
