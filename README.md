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
