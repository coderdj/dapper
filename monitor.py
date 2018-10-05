import urllib.request
import json
import time
import os

while(1):

    
    username = os.environ['DAQ_API_USER']
    password = os.environ['DAQ_API_KEY']

    # create a password manager
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

    # Add the username and password.
    # If we knew the realm, we could use it instead of None.
    top_level_url = "http://127.0.0.1:5000/dispatcher_status"
    password_mgr.add_password(None, top_level_url, username, password)

    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

    # create "opener" (OpenerDirector instance)
    opener = urllib.request.build_opener(handler)

    # use the opener to fetch a URL
    # opener.open('http://127.0.0.1:5000/dispatcher_status/tpc?max_results=1')

    # Install the opener.
    # Now all calls to urllib.request.urlopen use our opener.
    urllib.request.install_opener(opener)
    
    
    r = urllib.request.urlopen('http://127.0.0.1:5000/dispatcher_status/tpc?max_results=1')    

    data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))   
    print("%s: %s"%(data['update_time'], data['human_readable_status']))
    time.sleep(2)
