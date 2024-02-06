
# Galactic Bot

Galactic Bot is a discord bot that was created to make our discord server better and help manage the server utility-wise. However, we decide to publish this bot to GitHub as an open-source project. This project is a project that I continued against my friend's repository: [Galactic-bot](https://github.com/Duafan/Galactic-bot)

The previous project was using Node JS and Discord.js, but I plan to use Python 3 and discord-py to continue building the bot.


## Features
This is a new feature that is currently being created based on existing features in the previous project. There is still a lot that needs to be added
- Automatic notification message if a member joins and leaves the server
- Count Total Users, Members & Bots on servers in Channel Voice
- Have a general command (described below)
- *Upcoming features..*

**General Commands:**
- `.help [commands]` -> Lists all commands or just help for one command.
- `.ping` -> Mention the user
- `.say` -> Make the bot say what u said, even its mention another user if you mention it
- `.ui | .uinfo` -> Create embed of user info 

- *Upcoming commands..*




## !Prerequisites

- Python 3 (version 3.8 or higher as mentioned in [discord-py](https://discordpy.readthedocs.io/en/stable/intro.html))
- discord.py



## Setup

1. You need to clone this repository into your computer/server
```bash
  git clone https://github.com/hansrangga/galactic-bot.git
```
2. Open galactic.py
3. Change `'INSERT-YOUR-TOKEN'` on the bottom file into your token
4. Change `'INSERT-YOUR-GUILD-ID'` with your Server ID
5. Change `'INSERT-YOUR-CHANNEL-ID'` with your Channel ID based on what channel for the implementation
6. Run the bot
```bash
  python3 galactic.py
```

