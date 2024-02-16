import ujson

settings = { }

def load():
    global settings
    try:
        with open('settings.json', 'r') as f:
            settings = ujson.load(f)
    except:
        settings = { }
    return settings

def save():
    with open('settings.json', 'w') as f:
        ujson.dump(settings, f)

def update(new_settings):
    global settings
    settings = new_settings

def get(key):
    return settings.get(key, None)

def set(key, value):
    settings[key] = value
    save()