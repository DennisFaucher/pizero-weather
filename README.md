# pizero-weather
## Display Time &amp; Weather on Pi Zero e-Ink Display
![Weather](https://github.com/DennisFaucher/pizero-weather/blob/master/images/now.jpg)
![Forecast](https://github.com/DennisFaucher/pizero-weather/blob/master/images/forecast.jpg)

This is a slight modification to my Holiday Greetings repo https://github.com/DennisFaucher/pizero-epaper-greetings. I built this beautiful e-Ink Pi Zero with battery to use as a pwnagotchi and then as an automagic holiday greetings badge.  It was time for something new. How about the time and weather (alternating current and forecast) so large that maybe I could even make it out without my reading glasses? Sure, why not. 
 
 ## Hardware
 Raspberry Pi Zero W. WITH PINS as I am terrible at soldering. I purchased mine here: https://www.aliexpress.com/item/32979703845.html

Waveshare 2.13" e-Paper Dsiplay HAT. I purchased mine here: https://www.aliexpress.com/item/32810080308.html
 
 ## Software
 Install Raspbian OS from here https://www.raspberrypi.org/downloads/raspbian/ and use these instructions: https://www.raspberrypi.org/documentation/installation/installing-images/README.md

Connect your Raspberry Pi Zero (rPi) to keyboard, mouse, HDMI monitor and power to run through the usual Linux setup. I picked up all the necessary cable/power accesories here: https://www.sparkfun.com/products/14298

Install the Waveshare e-Paper drivers using these instructions: https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT. Rename the awfully named directory "RaspberryPi&JetsonNano" to just "Pi".

### Install the lighttpd server and PHP somewhere. You can use a local Linux host or a cloud Linux VM. Steps are:

sudo apt install lighttpd

sudo add-apt-repository ppa:ondrej/php

sudo apt-get update

sudo apt-get install -y php5.6

sudo apt-get install php5-mysql

sudo apt install -y php5.6-cgi

sudo lighty-enable-mod fastcgi-php

sudo service lighttpd force-reload

sudo chown www-data:www-data /var/www

sudo chmod 775 /var/www

sudo usermod -a -G www-data [your_linux_username]

### Copy files into place
Copy my pi.html and action.php to your linux server directory /var/www/html

Copy my greetings.py to your rPi in the directory /home/pi/e-Paper/Pi/python/examples
### Autostart
Add this entry into /etc/rc.local on your rPi

python3 /home/pi/e-Paper/Pi/python/examples/greetings.py  > /dev/null 2>&1 &

reboot
## Test
Point your web browser to http://[address-of-your-Linux-server]/pi.html. You should see this web form:
![Web Form](https://github.com/DennisFaucher/pizero-epaper-greetings/blob/master/Screen%20Shot%202019-12-17%20at%2010.04.27%20PM.png)

Type in a greeting, click Submit and within 60 seconds the greeting should show up on the rPi
