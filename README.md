# MotoTraKr
Rasperry Pi motorcycle tracking device. 


Background
=========

Motorcycle theft is extremely prevalent in the UK. Many of the COTS solutions charge expensive monthly fees. I wanted to design a simple rasperry pi based solution that could be discretely fitted under a motorcycle seat.

Design
---------

Using a rasperry pi with a Waveshare GSM hat, the Pi would poll the server at fixed intervals with it's current GPS position. 
The server would then store this to a local GPX file which can then be later imported into Google Maps.



![Schematic](https://user-images.githubusercontent.com/83759501/154311723-29a23d08-4ab9-4224-9dd2-59c3810718f7.jpg)

Very technical schematic. ;)


Hardware Requirements
---------

1. Rasperry Pi
Personally I've opted for a RPi 4, with the GSM waveshare hat. However any model of Rpi should be sufficient. The jumper position on the board should be set to "B", and the board connected to the GPIO interface on the Pi. You should test connectivity with the board by powering it up and connecting using screen.


```
$ sudo screen /dev/ttyS0
```

Issuing the command "AT" should show "OK" as a response. This indicates the board is functioning correctly.

![image](https://user-images.githubusercontent.com/83759501/154678093-7956f429-8ad7-480f-b747-96437fcdc6d4.png)

![image](https://user-images.githubusercontent.com/83759501/154678138-b716be57-a354-4bdb-b355-7505ad9b5a91.png)

2. Server
I'm a big fan of digital ocean. It's easy to spin up a box with no fuss, however you could use AWS or another cloud provider. You will need to install all the Python dependencies using the following command.

```
$ pip3 -r requirements.txt
```

To set up TLS, a domain name will be required. In my testing i've used a dynamic DNS service. 

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

1. Re-implement with support for TLS.
2. Apply AES application level encryption to the messages in transit.
3. Apply some sort of authentication procedure (oAUTH) to the API requests.
