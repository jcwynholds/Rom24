#!/usr/bin/env python3

import time
import asyncio
import telnetlib3
import threading
import re


# finite state automata
# telnet_connection -> choose_player -> login_player -> read_motd -> reset_to_mse -> ooda_loop -> disconnect
# goal #1 mud school and level 5
# threading object starts fsa
# telnet_connection returns telnetlib object
# choose_player reads from available players and returns name/password pair
# login_player does login chat and returns logged in player object
# read_motd reads messages writes to stdout
# reset_to_mse resets the character into known room
# ooda_loop 
#   looks for enemies
#   attack enemies
#   if no enemies look for exits
#   move to random exit
#   repeat
# disconnect after timer pops

#all_players = {
#    "Abrazak": "qwerty",
#    "Bannyboy": "qwerty",
#    "Borkeez": "qwerty"
#}

all_players = {
    "Abrazak": "qwerty",
}
avail_players = {}

async def telnet_connection(host, port):
    reader, writer = await telnetlib3.open_connection(host, port)
    return reader, writer

def choose_player():
    # need some locking for threads
    # return avail_players.popitem()
    return all_players.popitem()

async def login_player(player, reader, writer):
    try:
        response = await asyncio.wait_for(reader.read(4096), timeout=.300)
        writer.write(player[0])
        response = await asyncio.wait_for(reader.read(4096), timeout=.300)
        writer.write(player[1])
    except asyncio.exceptions.TimeoutError:
        return -1
    return

async def read_motd(reader, writer):
    try:
        response = await asyncio.wait_for(reader.read(4096), timeout=.300)
        writer.write('\n')
        response = await asyncio.wait_for(reader.read(4096), timeout=.300)
        writer.write('\n')
        writer.write('\n')
    except asyncio.exceptions.TimeoutError:
        return -1
    return

async def disconnect(reader, writer):
    reader.close()
    writer.close()
    return

async def do_loop():
    read, write = await telnetlib3.open_connection(host='localhost', port=4000)
    plyr = choose_player()
    login_player(plyr, read, write)

    read_motd(read, write)
    time.sleep(1.0)
    disconnect(read, write)

async def main():
    print("start main")
    avail_players = all_players.items()
    print("avail_players %s" % avail_players)
    print("len avail_pl %d" % len(avail_players))
    # while len(avail_players) > 0:
    if True:
        print("thread st players %s" % avail_players )
        thing = await do_loop()
    print("end main")

asyncio.run(main())