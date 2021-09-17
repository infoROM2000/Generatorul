"""
Not final.
"""
import requests
import urllib.parse


def translate(what: str, source: str = "ro", target: str = "en"):
    """

    :param what: string to be translated
    :param source: language of input
    :param target: language of output
    :return: translated string
    """
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    payload = urllib.parse.urlencode(
        {
            "q": what,
            "target": target,
            "source": source
        }
    )
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'accept-encoding': "application/gzip",
        'x-rapidapi-key': "SIGN-UP-FOR-KEY",
        'x-rapidapi-host': "google-translate1.p.rapidapi.com"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text
