#!/usr/bin/env python3
import requests
import socket

localhost = socket.gethostbyname('localhost')
request = requests.get("http://www.google.com")
def check_localhost():
        return  localhost =='127.0.0.1'

def check_connectivity():
        return request.status_code ==200
