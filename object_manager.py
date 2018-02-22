#! /usr/bin/env python3.6
import requests
import urllib3
import validators
import re
import netaddr
import getpass
from ssh_client import sshClient

class netMRIManager(object):

    def __init__(self):

        """ for other users, can alter username/password to take input
        instead of hard-coding like below. please ask if needed"""

        self.wapi_url = "https://hostname/api/3.1/"
        self.username = "username"
        self.password = "password"

    def macQuery(self, user_input):
        # If valid mac address (needs to be either ':' or '-' delimited)
        if macCheck(user_input):
            user_input = netaddr.EUI(str(user_input))
            # formats mac correctly for netmri API query
            user_input.dialect = netaddr.mac_unix_expanded
            query = "end_host_mac_addresses"
            req_params = {"MACAddress":user_input, "limit":1}
            mac_search = requests.get(self.wapi_url + query + "/find?",
                                      data=req_params,
                                      auth=(self.username,
                                            self.password),
                                      verify=False)
            # return(print(mac_search))
            mac_found = mac_search.json()
            for mac in mac_found[query]:

                """ below are API identifier names for unique
                switch ID and interface (if) ID to be used for
                further queries"""

                device_lookup = mac["InfraDeviceID"]
                if_lookup = mac["InterfaceID"]
            device_name = self.deviceQuery(device_id=device_lookup)
            if_name = self.ifQuery(if_id=if_lookup)
            return(print("MAC: %s\nDevice: %s\nInterface: %s" %
                        (user_input, device_name, if_name)))
            user_choice = input("Login to device? (y/n) \n> ")
            while True:
                if user_choice.lower() == "y":
                    username = input("username> ")
                    password = getpass.getpass(prompt="password> ")
                    x = ssh_Client.sshClient()
                    x.client_login(hostname=device_name,
                                   username=username,
                                   password=password)
                elif
        else:
            return(print("Not a valid MAC!"))
    
    def deviceQuery(self, device_id):
        query = "devices"
        req_params = {"DeviceID":device_id, "limit":1}
        device_search = requests.get(self.wapi_url + query + "/find?",
                                     data=req_params,
                                     auth=(self.username,
                                           self.password),
                                     verify=False)
        device_found = device_search.json()
        for device in device_found[query]:
            device_name = device["DeviceName"]
        return(device_name)

    def ifQuery(self, if_id):
        query = "interfaces"
        req_params = {"InterfaceID": if_id, "limit": 1}
        if_search = requests.get(self.wapi_url + query + "/find?",
                                        data=req_params,
                                        auth=(self.username,
                                              self.password),
                                        verify=False)
        if_found = if_search.json()
        for interface in if_found[query]:
            if_name = interface["ifName"]
        return(if_name)

def macCheck(address):
    if validators.mac_address(str(address)):
        return True
    else:
        return False

if __name__ == "__main__":
    address = input("> ")
    macQuery(input)
    
# suppress irrelevant messages to enduser
requests.packages.urllib3.disable_warnings()
