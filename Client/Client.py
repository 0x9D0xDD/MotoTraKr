"""
Client module for starting communication from the Rpi to the remote server.
Reads in the configuration data from the config.ini and passes it to the
relevant modules.
"""
import ConnectionHandler
import configparser
import os
import time

class Client():

  def __init__(self):
    self.config = configparser.ConfigParser()
    self.config.read("config.ini")
    self.callback_interval = self.config["CLIENT"]["callback_interval"]
    self.deployment_guid = self.config["CLIENT"]["deployment_guid"]
    self.server_url = self.config["CLIENT"]["server_url"]
    self.serial_interface = self.config["CLIENT"]["serial_interface"]

  def start(self):
    ''' Start the client
        Args: None
        Returns: None
    '''
    conn = ConnectionHandler.ConnectionHandler(self.serial_interface)
    while 1 == 1:
      gps = conn.get_lat_long()
      data = "?lat=" + str(gps[0]) + "&lon=" + str(gps[1])
      request_url = self.server_url + self.deployment_guid
      print(request_url)
      conn.send_outbound_data(request_url,data)
      time.sleep(int(self.callback_interval))

if __name__ == "__main__":
  cli = Client()
  cli.start()
