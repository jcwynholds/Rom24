import asyncio
import re
import telnetlib3

rules = [
    ("220 .* SMTP", "HELO localhost"),
    ("250 Hello and welcome", "MAIL FROM:<from_email_address"),
    ("250 Ok", "RCPT TO:<to_email_address>"),
    ("250 Ok", "DATA"),
    ("354 Proceed", "<email header and body>"),
    ("250 Ok", "QUIT")
]

async def main():
    reader, writer = await telnetlib3.open_connection(host, port)

    for prompt, action in rules:
        response = await reader.readline()
        print(response.strip())

        if re.match(prompt, response):
            writer.write(action + "\n")
            print(action)

asyncio.run(main())
