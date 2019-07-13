from lxml.html import fromstring as parse
import re
import requests

class GamertagNotFoundError(Exception):
    pass

class PlayedGame(object):
    locked = False
    def __init__(self, tr):
        if self.__class__.locked:
            raise PermissionError('this class should not be called directly')
        self.tr = tr
        self.icon = self.tr.xpath('td[1]/a/img/@src')[0]
        self.title = self._get_text('td[2]/p[2]')
        teg = self._get_text('td[3]/div[1]/div/span')
        self.total_earned_gamerscore = eval(teg[:teg.index('/')])
        tua = self._get_text('td[3]/div[2]/div/span')
        self.total_unlocked_achievements = eval(tua[:tua.index('/')])

    def _get_text(self, _path):
        els = self.tr.xpath(_path)
        if len(els) > 0:
            return els[0].text_content().strip()
        else:
            return None

    def __repr__(self):
        return '<XboxGame "{}">'.format(self.title)

    def __str__(self):
        return self.title

class Gamertag(object):
    BASE_URL = "https://www.xboxgamertag.com"
    def __init__(self, name):
        PlayedGame.locked = False
        r = requests.get(self.BASE_URL+'/search/{}/'.format(name))
        self.doc = parse(r.content)
        if "hasn't been created yet :(" in r.content.decode():
            raise GamertagNotFoundError('the gamertag "{}" has not been created yet :('.format(self.name))
        self.icon = self.doc.xpath('//div[@id="topLeft"]/img/@src')[0]
        self.gamertag = self._get_text('//div[@id="topLeft"]/h2[@class="tierGamertag"]')
        self.gamerscore = self._get_int('//div[@id="topLeft"]/p')
        topRC = self.doc.xpath('//div[@class="topRC"]/div/p')
        self.total_games_played = re.search(r": (\d+)", topRC[0].text_content()).group(1)
        self.games_completed = re.search(r": (\d+)", topRC[1].text_content()).group(1)
        self.average_completion = re.search(r": (\d+)", topRC[2].text_content()).group(1)
        self.games_played = [PlayedGame(tr) for tr in self.doc.xpath('//table/tr')]
        PlayedGame.locked = True

    def _get_text(self, _path):
        els = self.doc.xpath(_path)
        if len(els) > 0:
            return els[0].text_content().strip()
        else:
            return None

    def _get_int(self, _path):
        els = self.doc.xpath(_path)
        if len(els) > 0:
            return int(els[0].text_content().replace(',', '').strip())
        else:
            return None

    def __getattr__(self, key):
        return self.__dict__[key]

    def __iter__(self):
        for k, v in self.__dict__.items():
            yield k, v

    def __repr__(self):
        return '<XboxGamer "{}"; gamerscore={}>'.format(self.gamertag, self.gamerscore)

    def __str__(self):
        return self.title
