# Sentinel


[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) ![langCount](https://img.shields.io/github/languages/count/RPowell-C/Sentinel) ![CodeFactor](https://www.codefactor.io/repository/github/rpowell-c/sentinel/badge) ![Sponsors](https://img.shields.io/github/sponsors/rpowell-c) ![issues](https://img.shields.io/github/issues/rpowell-c/sentinel) ![Maintaned](https://img.shields.io/maintenance/Yes/2024) ![discord](https://img.shields.io/discord/1145527579126808576)
### The only true community built moderation bot for Y99

---

## Requirements
* git is recommended 
* Selenium
* 4 GB of RAM
* See list below for OS's/Platforms
### Supported OS's
| Platform | Support level |
| -- | :---: |
| Arch Linux| ![](https://img.shields.io/badge/Fully_Supported-gree) |
| Manjaro | ![](https://img.shields.io/badge/Fully_Supported-gree) | 
| Arch Based Distros | ![](https://img.shields.io/badge/Supported-green) | 
| Ubuntu | ![](https://img.shields.io/badge/Untested*-f9ff12) |
| Windows 10 | ![](https://img.shields.io/badge/No_Support-None_Planned-c41616) |
| Windows 8.1 | ![](https://img.shields.io/badge/No_Support-None_Planned-c41616) |
| Windows 7 | ![](https://img.shields.io/badge/No_Support-None_Planned-c41616)
| Raspberry Pi 3B | ![](https://img.shields.io/badge/No_Support-Planned-orange) |
| Raspberry Pi 4+ | ![](https://img.shields.io/badge/Untested*-f9ff12) |

\* Should run fine

## How to use/run
```
git clone https://github.com/RPowell-C/Sentinel Sentinel && cd Sentinel
```

Sentinel is written in Python so running it super simple, first setup a virtual environment with and activate it with

```
python3 -m venv .venv && source .venv/bin/activate
```
this will setup a virtual environment at `.venv` and activate so the next command is

``` 
python3 -m pip install -r requirements.txt
```

this will install all the required parts and all you need to do is fill in the settings and you can run it with

```
python3 sentinel.py
```
## Javascript/Node
There is a optional webserver that displays the last message, follow node install intructions to install and run the HTML file in a webbrowser if you want this, it isn't complete yet.
## Updater
<<<<<<< HEAD
There is an included updater, you will not have to do anything outside of compile the updater with 
```
g++ updater.cpp -o updater.out -lcurl
```
and then run it when it's updated, Sentinel will inform you whenever it is launched if a new version is out.
There is an updater that is being worked on, the one in `cpp` isn't quite ready yet

# Settings
Sentinel comes with a lot of settings to provide the user with maximum customizability 
## Core Settings
The only things that should be edited by the user in `core` is `username`, `password`, `name` and `room`.
`username` and `password` are pretty easy to figure out, name is a kind of redundant feature that's just the nickname of the bot, put the username if you don't have one, `room` is the room code, which is the last part of the URL when in the room.
## Radio/Keys
these are being taken out in the future as they are not needed
## Function Settings
These allow the bot to use certain commands, the important ones are `LogChat` which allows Sentinel to log the chat or not, `useUCAL` which gives Sentinel access to the User Control Authentication List, a way to restrict users from using certain commands, `useDeletion` which allows Sentinel to delete messages sent in the chat, `useBan` which allows Sentinel to ban users and `useModerationTools`, which allows Sentinel to mute the chat among other things that are planned for the future.
## UCAL Levels
The aforementioned User Control Authentication List is a tool that assigns each user a level, when a command is recognized by Sentinel it will check the username of the user attempting the command against its list and if the user's level is high enough it will allow the command, if it isn't it won't, this section of `settings.json` sets the level for each command or group of commands
## Moderation
`MiniMods` is not used for the time being, but `triggers` is a list of words that will, in the future, ban users automatically for saying them.

# Community
## Discord
> https://discord.gg/XTaxm9WKFz
## Y99
> https://y99.in/r/1792519
