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
git clone https://github.com/RPowell-C/Sentinel Sentinel
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
### Javascript/Node
There is a optional webserver that displays the last message, follow node install intructions to install and run the HTML file in a webbrowser if you want this, it isn't complete yet.
### Updater
There is an included updater, you will not have to do anything outside of compile the updater with 
```
g++ updater.cpp -o updater.out -lcurl
```
and then run it when it's updated, Sentinel will not inform you when it's time to update, this is being worked on

# Community
## Discord
> https://discord.gg/sMPWUe6x9
## Y99
> https://y99.in/r/1229078