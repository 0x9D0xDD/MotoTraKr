from gsmHat import GSMHat
import time

class ConnectionHandler():
    ''' Connection handling class for controlling
        connections to the gsm hat. Abstraction of gsmhat
        library.
    '''

    def __init__(self):
        self.serial_interface = GSMHat('/dev/ttyS0', 115200)
        time.sleep(4)
        self.gps_data = self.serial_interface.GetActualGPS()
        while self.gps_data.GNSS_status == 0:
            print('Waiting for GNSS signal')

    def sms_available(self):
        ''' Check for incoming SMS.
            Args: None
            Returns: None
        '''
        return self.serial_interface.SMS_available()

    def get_lat_long(self):
        ''' Return current lat long.
            Args: None
            Returns: None
        '''
        return [self.gps_data.Latitude, self.gps_data.Longitude]

    def send_outbound_data(self, server, data):
        ''' Send request to telemetry server.
            Args: server (string)
                  data (encrypted string)
            Returns: success (boolean)
        '''
        url = ""
        self.serial_interface.SetGPRSconnection('pp.vodafone.co.uk',
                                                'web', 'web')
        url += server
        url += data
        self.serial_interface.CallUrl(url)
        return 1

if __name__ == "__main__":
    c = ConnectionHandler()
    gps = c.get_lat_long()
    print(gps)
