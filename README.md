# What is this?

This is the provisional early code for a bot to handle _Magic: the Gathering_ rotisserie drafts.

It's incredibly threadbare right now and is mostly an excuse for me to write dodgy Python. All code is
subject to change, and nothing can be realistically expected to work.


# Requirements

You must register a Telegram bot name and API key. See https://core.telegram.org/bots#6-botfather for
instructions.

Place them in a file named `key.yaml` in the root of this repository, in the following format:

    telegram:
        name: botname
        key: apikey

Make sure to keep this file a secret. Do not commit it to public version control. (At some point, this
will probably become a parameter passed to the bot on startup, and default to somewhere innocuous like
your home directory.)


# Licence

This code is licensed under the GPL v2 licence except where noted.


# Attribution

Scryfall refers to https://www.scryfall.com. No endorsement by them is intended or implied.
CubeCobra refers to https://cubecobra.com. No endorsement by them is intended or implied.
Magic: the Gathering is © of Wizards of the Coast. All card names, artwork, and related marks are property of Wizards. No endorsement by them is intended or implied.
