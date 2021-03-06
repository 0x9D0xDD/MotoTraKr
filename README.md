# MotoTraKr
Rasperry Pi motorcycle tracking device. 


Background
=========

Motorcycle theft is extremely prevalent in the UK. Many of the COTS solutions charge expensive monthly fees. I wanted to design a simple rasperry pi based solution that could be discretely fitted under a motorcycle seat.

Design
---------

Using a rasperry pi with a Waveshare GSM hat, the Pi would poll the server at fixed intervals with it's current GPS position. 
The server would then store this to a local GPX file which can then be later imported into Google Maps.


<img src="https://user-images.githubusercontent.com/83759501/154311723-29a23d08-4ab9-4224-9dd2-59c3810718f7.jpg" width="450" height="450">

Very technical schematic. ;)


Requirements
---------

1. Rasperry Pi
Personally I've opted for a RPi 4, with the GSM waveshare hat. However any model of Rpi should be sufficient. The jumper position on the board should be set to "B", and the board connected to the GPIO interface on the Pi. You should test connectivity with the board by powering it up and connecting using screen.


```
$ sudo screen /dev/ttyS0
```

Issuing the command "AT" should show "OK" as a response. This indicates the board is functioning correctly.

<img src="https://user-images.githubusercontent.com/83759501/154678093-7956f429-8ad7-480f-b747-96437fcdc6d4.png" width="450" height="450">

<img src="https://user-images.githubusercontent.com/83759501/154678138-b716be57-a354-4bdb-b355-7505ad9b5a91.png" width="450" height="450">


2. Server
I'm a big fan of digital ocean. It's easy to spin up a box with no fuss, however you could use AWS or another cloud provider. You will need to install all the Python dependencies using the following command.

```
$ pip3 install -r requirements.txt
```

To set up TLS, a domain name will be required. In my testing i've used a NoIp service. This allows you to create a free API domain that can handle requests.

[NoIp Setup](https://www.noip.com/)

Then, using LetsEncrypt and certbot you can create a signed TLS certificate.

[Lets Encrypt Setup](https://certbot.eff.org/instructions?ws=other&os=ubuntufocal)

3. Viewing Geo Data
Using Google Maps, you can import the KML files directly as layers into the map.
[Google Maps KML Files](https://support.google.com/mymaps/answer/3024836?hl=en&co=GENIE.Platform=Desktop)

4. Bike install

Depending on your model of bike, the Rpi should be a snug fit under the seat. With the Royal Interceptor 650 it just about fits. I'm using an external 10,000ma battery to power the Pi.

<img src="https://user-images.githubusercontent.com/83759501/154685192-7f111da8-268f-4ea5-845a-17bdded19c2f.png" width="450" height="450">


Usage
---------

The client is deployed to the rasperry pi, where it can be executed with:

```
$ sudo python3 Client.py
```

Local client configuration options can be specified in the config.ini file. The binary needs sudo privileges in order to open 
the serial interface and communicate with the remote server. 

On the server, execute the script file as follows:

```
$ sudo ./startup.sh
```

Todo 
--------

1. Apply AES application level encryption to the messages in transit.
2. Apply some sort of authentication procedure (oAUTH) to the API requests.
