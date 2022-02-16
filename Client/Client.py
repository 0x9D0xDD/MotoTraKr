import ConnectionHandler
import configparser
import os
import time

class Client():

  def __init__(self):
    self.config = configparser.ConfigParser()
    self.config.read("config.ini")
    self.callback_interval = self.config["CLIENT"]["callback_interval"]
    self.server_url = self.config["CLIENT"]["server_url"]

  def start(self):
    ''' Start the client
        Args: None
        Returns: None
    '''
    conn = ConnectionHandler.ConnectionHandler()
    while 1 == 1:
      gps = conn.get_lat_long()
      data = "lat=" + str(gps[0]) + "&lon=" + str(gps[1])
      print(data)
      print(self.server_url + data)
      conn.send_outbound_data(self.server_url,data)
      time.sleep(int(self.callback_interval))

if __name__ == "__main__":
  cli = Client()
  cli.start()
