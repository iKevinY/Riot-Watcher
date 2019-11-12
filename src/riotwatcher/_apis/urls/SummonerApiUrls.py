from .Endpoint import LeagueEndpoint


class SummonerV4Endpoint(LeagueEndpoint):
    def __init__(self, url, **kwargs):
        nurl = "/summoner/v4/summoners" + url
        super(SummonerV4Endpoint, self).__init__(nurl, **kwargs)


class SummonerApiV4Urls(object):
    by_account = SummonerV4Endpoint("/by-account/{encrypted_account_id}")
    by_name = SummonerV4Endpoint("/by-name/{summoner_name}")
    by_puuid = SummonerV4Endpoint("/by-puuid/{encrypted_puuid}")
    by_id = SummonerV4Endpoint("/{encrypted_summoner_id}")
