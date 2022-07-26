# About

This is a webapp interface for the functionality normally found in [ROBOT IS YOU](https://github.com/RocketFace/robot-is-you), a Discord bot by @RocketFace based on the indie game [Baba Is You](https://store.steampowered.com/app/736260/Baba_Is_You/) (by Arvi Teikari) and written with the [discord.py](https://discordpy.readthedocs.io/en/latest/) library.

The webapp is written in Quart (reimplementation of Flask), and aims to provide all the functionality of the bot .

99% of the code here was written by the original ROBOT IS YOU devs. Please give them some love 🧡.

Looking for the README for ROBOT? Check [the original repository](https://github.com/RocketFace/robot-is-you) or [the README in the master branch](./blob/master#README).

# To Host This Yourself

Please follow the terms of the license!

Install the requirements: `pip install -r requirements.txt`.

Run the bot using `python3 WEBAPP.py`.

(The bot may not work properly on Windows, as it makes use of some unix-ish shell commands for the convenience of the programmer.)

## Required files

Bot/webapp configuration is in `config.py`. Right now, the webapp only uses:

* `db_path`: `str` - The path to the sqlite3 database used by the bot.

