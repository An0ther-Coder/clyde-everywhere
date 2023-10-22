# Clyde everywhere / reClyde
## Requirements
[discord.py-self](https://github.com/dolfies/discord.py-self)
## How this userbot work?
reClyde must be on a server with Clyde for sending messages to it. Clyde's backstory must contain "You call people by the first word they wrote in message". For all the magic is responsible two message listeners:
- Listener 1
  1. Checks if message have reClyde mentions.
  2. Checks if message author is not Clyde
  3. Makes reClyde resned the message to Clyde, and declares a variable `resended_message` that contain it
  4. Appends to a `queue` variable a tuple, with the message that was listened and a resended message (First one needs to send Clyde's response to message's channel, and the second one needs for comparing future Clyde's message refernce id to resended message id, for initializing a Clyde's response)
- Listener 2
  1. Checks if message author is Clyde, and if message guild is the guild with Clyde, declared in the beginning
  2. For every tuple (pair of original and resended messages) in `queue` checks if the resneded message's id equals to message's id which Clyde replied
  3. Checks if length of message is more than 1950 characters and if it is, splitting message for pieces of 1950 characters and sends each one to original message's channel. If it not, just sends a Clyde's message to original message's channel
  4. Removing the tuple from `queue`
