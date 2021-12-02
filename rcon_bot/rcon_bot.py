#!/bin/env python3

from xrcon.client import XRcon
import configparser
import getopt
import sys
import random
import time

host = '127.0.0.1'
port = 2600
password = 'pass'
text_file = '/path/to/file.txt'
message_interval = 300 #in seconds

'''Requires config file in ini format:

[DEFAULT]
host=127.0.0.1
port=2600
password=pass
text_file=/path/to/file.txt
message_interval=300 #in seconds

Defaults won't work (most likely) =)'''

def load_conf():
    '''Specify config file location with -c option'''

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'c:')
    except:
        sys.exit("use -c to specify config")

    if len(opts) == 0:
        sys.exit("use -c to specify config")

    for opt, arg in opts:
        if opt in ['-c']:
            config_file = arg

    try:
        open(config_file, "r").readable()
        print('config = ' + config_file)
        sys.stdout.flush()
    except:
        sys.exit("No such file or not readable")

    read_conf = configparser.ConfigParser()
    read_conf.read(config_file)

    for ini_section in read_conf:
        if ini_section == 'DEFAULT':
            if 'host' in read_conf[ini_section]:
                global host
                host = read_conf[ini_section]['host']

            if 'port' in read_conf[ini_section]:
                global port
                port = read_conf[ini_section]['port']

            if 'password' in read_conf[ini_section]:
                global password
                password = read_conf[ini_section]['password']

            if 'text_file' in read_conf[ini_section]:
                global text_file
                text_file = read_conf[ini_section]['text_file']

            if 'message_interval' in read_conf[ini_section]:
                global message_interval
                message_interval = int(read_conf[ini_section]['message_interval'])

def doing_things():
    '''Main part is xrcon module which provides posibility to connect to xonotic (not only btw) server.
    Links: https://pypi.org/project/xrcon/, https://github.com/bacher09/xrcon
    Make sure you installed it'''

    while True:
        rcon = XRcon(host, port, password)
        rcon.connect()
        '''Reading file everytime makes possible to change content "on fly"'''

        with open(text_file, 'r') as tips:
            tips_list = tips.readlines()

        rnd_tip = random.randrange(0, len(tips_list))
        tip = tips_list[rnd_tip].strip()
        print('tip number: ' + str(rnd_tip))
        print('sending message: ' + tip)
        sys.stdout.flush()

        try:
            data = rcon.execute('say Newbie tip #' + str(rnd_tip) + ': ' + tip) # on python3 data would be bytes type
            print(data)
        finally:
            rcon.close()
        sys.stdout.flush()
        time.sleep(message_interval)

if __name__ == '__main__':
    load_conf()
    doing_things()
