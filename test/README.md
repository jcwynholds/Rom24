Testing for Rom
===============

Here's some basic python tests for rom24.  The goal now is to do load testing for profiling network response.

Goal is something like apachebench to fire up 10-500 players to emulate a popping mud.

Using asyncio in python for brevity and ease.  

Mvp is pre-created level 1 player able to login and look for mobs in mud school.


Current Problems
================

Only one player per connection.  Player creation is hard to automate and track.  New player login and play needs work.

Player creation and tracking needs:
- multithread/multiprocess locking (only one player per connection)
- storage of player name and password
- something easy to load/store like sqlite or python pickle
- 

Old player login:
- picking player and locking
- getting to proper place for good mobs
- evaluating mobs
- maximizing silver and experience points

New player creation:
- easy is to pick defaults and go
- harder is random picks
- hardest is solver for local minima
- load/store player for locking

Automata
- maybe area-based lists of automata
    - mud school with list of mobs
    - other areas as exp + level go up
- hunger/thirst/items/mobility
- rules based responses
- special prompts?
- 