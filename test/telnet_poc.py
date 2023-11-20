#!/usr/bin/env python3

import time
import asyncio
import telnetlib3
import threading
import re

# this is still a proof of concept
# it's somewhat working
# see sequenced challenge/response in login_player for reference

# finite state automata
# do_loop -> login_player -> read_motd -> reset_to_mse -> ooda_loop -> disconnect
# goal #1 mud school and level 5
# do_loop is await'ed sequence of functions
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

all_players = {
    "Abrazak": "qwerty",
    "Bannyboy": "qwerty",
    "Borkeez": "qwerty"
}

async def login_player(player, reader, writer):
    login_rules = {
        'known?': 'player[0]',
        'Password:': 'player[1]' 
    }
    keys_matched = set(login_rules.keys())
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

async def do_loop(plyr):
    # connect via telnet and wait on chained async actions
    # todo ooda loop
    read, write = await telnetlib3.open_connection(host='localhost', port=4000)
    res = await login_player(plyr, read, write)
    if res != 0:
        return
    res = await read_motd(read, write)
    if res != 0:
        return
    asyncio.sleep(1)
    disconnect(read, write)

async def main():
    for k, v in all_players.items():
        plyr = (k,v)
        thing = await do_loop(plyr)
    print("end main")

asyncio.run(main())