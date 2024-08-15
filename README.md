# Sentinel
### The only true community built moderation bot for Y99

---

## Requirements
* git is recommended 
* Arch or Linux is required
### OS's tested on
* Arch Linux :white_check_mark:
* Ubuntu :gray_question:
* Windows :x:
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