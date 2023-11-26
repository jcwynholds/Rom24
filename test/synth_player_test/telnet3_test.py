#!/usr/bin/env python3

import asyncio
import telnetlib3

# this is a simple test that reads the mud banner and quits

async def telnet_welcome_message(host, port, timeout=2):
    output = ""
    # Establish a Telnet connection with timeout
    reader, writer = await telnetlib3.open_connection(host, port)
        
    try:
        # Read the Telnet output
        while True:
            data = await asyncio.wait_for(reader.read(4096), timeout=timeout)
            if data:
                output += data
    except asyncio.exceptions.TimeoutError:
        # Timeout occurred -> Exiting
        pass
    finally:
        reader.close()
        writer.close()
    return output

message = asyncio.run(telnet_welcome_message(host="localhost", port=4000))
print(message)
