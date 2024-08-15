import json

# !!!IMPORTANT!!! if you are just browsing these files, this is not the settintgs file, that is settings.json

# the overarching settings file
with open("json-files/settings.json", "r") as f:
    settingsdata = json.load(f)


class core:
    username = settingsdata['core']['username']
    password = settingsdata['core']['password']
    entrances = settingsdata['core']['entrances']
    name = settingsdata['core']['name']
    version = settingsdata['core']['version']
    trustedUsers = settingsdata['core']['trustedUsers']
    room = settingsdata['core']['room']

class miscSettings:
    logchat = settingsdata['functionSettings']['LogChat']


class funcSettings:
    useFilsay = settingsdata['functionSettings']['useFilesay']
    useRaiseLevel = settingsdata['functionSettings']['useRaiseLevel']
    useDeletion = settingsdata['functionSettings']['useDeletion']
    useBan = settingsdata['functionSettings']['useBan']
    useModerationTools = settingsdata['functionSettings']['useModerationTools']


class ucalLevels:
    ucal = settingsdata['ucalLevels']['UCAL']
    raiseLevel = settingsdata['ucalLevels']['raiseLevel']
    ban = settingsdata['ucalLevels']['ban']

class keys:
    deeplKey = settingsdata['keys']['DeeplKey']


class moderation:
    minimods = settingsdata['moderation']['miniMods']
    triggers = settingsdata['moderation']['triggers']
