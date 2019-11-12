from .Endpoint import LeagueEndpoint


class ThirdPartyCodeApiV4Urls(object):
    by_summoner = LeagueEndpoint(
        "/platform/v4/third-party-code/by-summoner/{encrypted_summoner_id}"
    )
