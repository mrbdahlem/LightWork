import ujson

def load():
    try:
        with open('settings.json', 'r') as f:
            settings = ujson.load(f)
    except:
        settings = { }
    return settings

def save(settings):
    with open('settings.json', 'w') as f:
        ujson.dump(settings, f)

