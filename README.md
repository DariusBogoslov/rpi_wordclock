## Software to create a Raspberry Pi based wordclock

### :vertical_traffic_light: Repo status

<p align="left">
 <img alt="Source code license" src="https://img.shields.io/badge/license-GPL--3.0-informational"/>
 <img alt="GitHub Issue Count" src="https://img.shields.io/github/issues/bk1285/rpi_wordclock"/>
 <img alt="GitHub (Pre-)Release Date" src="https://img.shields.io/github/release-date-pre/bk1285/rpi_wordclock">
 <img alt="Build status documentation" src="https://readthedocs.org/projects/rpi-wordclock/badge/"/>
</p>

### ✔️ Features
 * [Various language layouts](https://github.com/bk1285/rpi_wordclock/tree/master/wordclock_layouts)
 * [Various plugins](https://github.com/bk1285/rpi_wordclock/tree/master/wordclock_plugins) to
     * display the current time
     * get information on current temperature, sunrise, sunset, IP-settings, ...
     * play tetris (credits to [@mrksngl](https://github.com/mrksngl))
     * View a demo [here](https://youtu.be/wcLQDykRBbM?t=84)
 * RESTful, [swagger](https://swagger.io/specification/)-based API to access and control the wordclock functionality
 * [Documentation](http://rpi-wordclock.readthedocs.io/en/master/) on how to build the clock.
 * Remote control via webinterface (credits to [@FrankX0](https://github.com/FrankX0))
     * Control the wordclock with a browser within your local network
     * Linking the webinterface to your smartphones homescreen provides an app-like usage of the interface
     * Hardware buttons are not mandatory anymore.
 * Integration to your instance of [home-assistant](https://www.home-assistant.io/) using [this repository](https://github.com/bk1285/rpi_wordclock_for_homeassistant/)
  
### ⏳ In progress
 * Integration of a brightness sensor

### :books: Further reading
 * Exemplary builds are available at [pinterest](https://www.pinterest.de/berndkrolla/wordclock-gallery/)
 * [Roadmap](https://github.com/bk1285/rpi_wordclock/projects)
 * [Excellent starting point](https://simongolms.github.io/QLOCKGENERATOR/#/home) to create your own layout

### 👏 Support 
 * Star this repo, if you like the project. 
 * Request a new feature by [opening a issue](https://github.com/bk1285/rpi_wordclock/issues), describing your feature request.
 * Contribute your code: [Learn how to create your own plugin](https://rpi-wordclock.readthedocs.io/en/master/doc_further_reading.html#adding-a-new-plugin)

### Python3
When using the Python 3 branch the follwing changes have to be made during installation.
Tested on latest Raspian Buster (02.12.2020)

#### System Packages
```
sudo apt-get install python3-pip python3-scipy scons git swig fonts-freefont-ttf python3-rpi.gpio
```

#### Python Packages
Instead of *flask-restplus* which is no longer maintained we are using now *flask-restx*.
For the great *rpi-ws281x* Library there is no need to compile it yourself. It is just installed via pip now.

```
sudo pip3 install pytz astral feedparser pillow svgwrite freetype-py netifaces monotonic flask-restx rpi-ws281x
```

#### Repository
For using pyhton3 branch:

```
git clone https://github.com/phenze/rpi_wordclock.git
cd rpi_wordclock/
git checkout --track origin/master-python3
```

#### Cronjob
For the cronjob you have to use python3 instead of python command

```
@reboot sudo python3 /home/pi/rpi_wordclock/wordclock.py
```
