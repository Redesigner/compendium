class navitem:
    def __init__(self, name, url):
        self.name = name
        self.url = url

navitems = [
    navitem('Home','/'),
    navitem('Blog','posts'),
    navitem('Compendium','compendium'),
    navitem('Contact','contact'),
]