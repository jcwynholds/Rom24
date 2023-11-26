#!/usr/bin/env python3

import asyncio
import re
import telnetlib3

# this is simple test using asyncio and expect-like rules

# problem is that we have to re.search each rule for each line
# probably good enough - would be nicer if rules were
# matched for given purposes like login_rules, heal_rules
# look_for_mob_rules, etc etc to keep the list of regexes
# short and keep search strings as small as possible

rules = [
    ("By what name do you wish to be known?", "Bannyboy"),
    ("Password:", "qwerty"),
    (".* continue]", "")
]

async def main():
    reader, writer = await telnetlib3.open_connection("localhost", 4000)
    print("connected to localhost 4000")
    #for prompt, action in rules:
    while True:
        try:
            response = await asyncio.wait_for(reader.read(4096), timeout=.300) 
            print(response)
            for prompt, action in rules:
                if re.search(prompt, response, re.MULTILINE):
                    writer.write(action + "\n")
                    print(action)
        except asyncio.exceptions.TimeoutError:
            pass


asyncio.run(main())
