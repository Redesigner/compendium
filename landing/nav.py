class navitem:
    def __init__(self, name, url):
        self.name = name
        self.url = url

navitems = [
    navitem('Home',''),
    navitem('Posts','posts'),
    navitem('Compendium','resume'),
    navitem('Contact','contactform'),
    ]