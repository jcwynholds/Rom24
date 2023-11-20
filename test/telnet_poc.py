#!/usr/bin/env python3

import time
import asyncio
import telnetlib3
import threading
import re

# this is still a proof of concept
# it's not working
# Need to understand await/asyncio better
# it's ugly and procedural
# need to break it out to sequenced challenge/responce
# need to figure out wait on this until state emulating syncronous action
#    e.g have to enter player name before password


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

def choose_player():
    # need some locking for threads
    # return avail_players.popitem()
    return all_players.popitem()

async def login_player(player, reader, writer):
    login_rules = {
        'known?': 'player[0]',
        'Password:': 'player[1]' 
    }
    keys_matched = set(login_rules.keys())
    print(f"login_rules {login_rules}")

    while len(keys_matched) > 0:
        try:
            response = await asyncio.wait_for(reader.read(4096), timeout=.300)
            for k, v in login_rules.items():
                prompt, action = k, eval(v)
                if re.search(str(prompt), response, re.MULTILINE):
                    writer.write(action + "\n")
                    keys_matched.discard(k)
        except asyncio.exceptions.TimeoutError:
            return -1
    return 0



async def read_motd(reader, writer):
    try:
        response = await asyncio.wait_for(reader.read(4096), timeout=.300)
        writer.write('\n')
        response = await asyncio.wait_for(reader.read(4096), timeout=.300)
        writer.write('\n')
    except asyncio.exceptions.TimeoutError:
        return -1
    return

async def disconnect(reader, writer):
    reader.close()
    writer.close()
    return

async def do_loop():
    # connect via telnet and wait on chained async actions
    # todo ooda loop
    read, write = await telnetlib3.open_connection(host='localhost', port=4000)
    plyr = choose_player()
    res = await login_player(plyr, read, write)
    if res != 0:
        return
    res = await read_motd(read, write)
    if res != 0:
        return
    asyncio.sleep(1)
    disconnect(read, write)

async def main():
    print("start main")
    avail_players = all_players.items()
    print(f"avail_players {avail_players}")
    print(f"len avail_pl {len(avail_players)}")
    # while len(avail_players) > 0:
    # todo iterate over players here
    if True:
        print(f"thr st avail_players {avail_players}")
        thing = await do_loop()
    print("end main")

asyncio.run(main())