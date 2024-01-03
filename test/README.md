Testing for Rom
===============

Here's some basic python tests for rom24.  The goal now is to do load testing and profiling with 100+ players.

Goal is something like apachebench to fire up 10-500 players to emulate a popping mud.

Using asyncio in python for brevity and ease.  

Mvp is pre-created level 1 player able to login and look for mobs in mud school.

Directories contain a few scripts with similar requirements.txt.

Current Problems
================

Only one player per connection.  Player creation is hard to automate and track.  New player login and play needs work.

Player creation and tracking needs:
x[done] multithread/multiprocess locking (only one player per connection)
    - note: not multithread or multiprocess but async/await'ed coroutines
- storage of player name and password
    - python dict now
- something easy to load/store like sqlite or python pickle
- 

Old player login:
- picking player and locking
- area selection and navigation
- evaluating mobs
- maximizing silver and experience points

New player creation:
- easy is to pick defaults and go
- harder is random picks
- hardest is solver for local minima (most eff. sp+sk for least points)
- load/store player for locking

Automata
- maybe area-based lists of automata
    - mud school with list of mobs
    - other areas as exp + level go up
- hunger/thirst/items/mobility
- rules based responses
- special prompts?
- 
