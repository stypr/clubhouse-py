#/usr/bin/python -u
#-*- coding: utf-8 -*-

"""
clubhouse.py

API for Clubhouse (v297 / 0.1.27)
Developed for education purposes only.

Please know what you're doing!
Modifying a bit of header could result a permanent block on your account.
"""

import uuid
import time
import functools
import requests

class Clubhouse:
    """
    Clubhouse Class
    """

    # App/API Information
    API_HOST = "www.clubhouseapi.com"
    API_BUILD_ID = "297"
    API_BUILD_VERSION = "0.1.27"
    API_UA = "clubhouse/297 (iPhone; iOS 13.5.1; Scale/3.00)"

    # User information
    API_USER_ID = None
    API_USER_TOKEN = None
    API_USER_DEVICE = None # str(__import__("uuid").uuid4())

    # Some useful information for commmunication
    PUBNUB_PUB_KEY = "pub-c-6878d382-5ae6-4494-9099-f930f938868b"
    PUBNUB_SUB_KEY = "sub-c-a4abea84-9ca3-11ea-8e71-f2b83ac9263d"

    TWITTER_ID = "NyJhARWVYU1X3qJZtC2154xSI"
    TWITTER_SECRET = "ylFImLBFaOE362uwr4jut8S8gXGWh93S1TUKbkfh7jDIPse02o"

    AGORA_KEY = "938de3e8055e42b281bb8c6f69c21f78"
    SENTRY_KEY = "https://5374a416cd2d4009a781b49d1bd9ef44@o325556.ingest.sentry.io/5245095"
    INSTABUG_KEY = "4e53155da9b00728caa5249f2e35d6b3"
    AMPLITUDE_KEY = "9098a21a950e7cb0933fb5b30affe5be"

    # Useful header information
    HEADERS = {
        "CH-Languages": "en-JP,ja-JP",
        "CH-Locale": "en_JP",
        "Accept": "application/json",
        "Accept-Language": "en-JP;q=1, ja-JP;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "CH-AppBuild": f"{API_BUILD_ID}",
        "CH-AppVersion": f"{API_BUILD_VERSION}",
        "User-Agent": f"{API_UA}",
        "Connection": "close",
        "Content-Type": "application/json; charset=utf-8",
        "Cookie": "__cfduid=def2c5e4b7f2e3ba18ab49625408b043d1613200581"
    }


    def require_authentication(func):
        """ Simple decorator to check for the authentication """
        @functools.wraps(func)
        def wrap(self, *args, **kwargs):
            if self.API_USER_ID is None or self.API_USER_TOKEN is None:
                raise Exception('Not Authenticated')
            return func(self, *args, **kwargs)
        return wrap


    def __init__(self, user_id='', user_token='', user_device=''):
        """ (Clubhouse, str, str, str)

        Set default information
        """
        # TODO: change design..
        self.API_USER_ID = user_id if user_id else None
        self.API_USER_TOKEN = user_token if user_token else None
        self.API_USER_DEVICE = user_device if user_device else uuid.uuid4()

        # Update code
        self.HEADERS['CH-UserID'] = "(null)" if self.API_USER_ID is None else self.API_USER_ID
        self.HEADERS['Authorization'] = f"Token {self.API_USER_TOKEN}",
        self.HEADERS['CH-DeviceId'] = self.API_USER_DEVICE


    def start_phone_number_auth(self, phone_number):
        """ (Clubhouse, str) -> dict

        Begin phone number authentication.

        Phone number examples:
            +821012341337
            +818043211234
            ...
        """
        if self.API_USER_ID is not None:
            raise Exception('Already Authenticatied')
        data = {
            "phone_number": phone_number
        }
        req = requests.post(f"https://{self.API_HOST}/api/start_phone_number_auth", headers=self.HEADERS, json=data)
        return req.json()


    def complete_phone_number_auth(self, phone_number, verification_code):
        """ (Clubhouse, str, str) -> dict

        Complete phone number authentication.
        This should return `auth_token`, `access_token`, `refresh_token`, is_waitlisted, ...

        Please note that output may be different depending on the status of the authenticated user
        """
        if self.API_USER_ID is not None:
            raise Exception('Already Authenticatied')
        data = {
            "phone_number": phone_number,
            "verification_code": verification_code
        }
        req = requests.post(f"https://{self.API_HOST}/api/complete_phone_number_auth", headers=self.HEADERS, json=data)
        # find out how userId is taken
        return req.json()


    @require_authentication
    def join_channel(self, channel, attribution_source="feed"):
        """ (Clubhouse, str, str) -> dict

        Join the given channel
        """
        # Join channel
        data = {
            "channel": channel,
            "attribution_source": attribution_source,
            "attribution_details": "eyJpc19leHBsb3JlIjpmYWxzZSwicmFuayI6MX0=",
        }
        req = requests.post(f"https://{self.API_HOST}/api/join_channel", headers=self.HEADERS, json=data)
        return req.json()


    @require_authentication
    def leave_channel(self, channel):
        """ (Clubhouse, str) -> dict

        Leave the given channel
        """
        data = {
            "channel": channel,
            "channel_id": None
        }
        req = requests.post(f"https://{self.API_HOST}/api/leave_channel", headers=self.HEADERS, json=data)
        return req.json()


    @require_authentication
    def get_profile(self, user_id):
        """ (Clubhouse, str) -> dict

        Get someone else's profile
        """
        data = {
            "user_id": user_id
        }
        req = requests.post(f"https://{self.API_HOST}/api/get_profile", headers=self.HEADERS, json=data)
        return req.json()


    @require_authentication
    def get_profile_self(self, return_blocked_ids=False, timezone_identifier="Asia/Tokyo", return_following_ids=False):
        """ (Clubhouse, bool, str, bool) -> dict

        Get my information
        """
        # Get myself
        data = {
            "return_blocked_ids": return_blocked_ids,
            "timezone_identifier": timezone_identifier,
            "return_following_ids": return_following_ids
        }
        req = requests.post(f"https://{self.API_HOST}/api/me", headers=self.HEADERS, json=data)
        return req.json()


    @require_authentication
    def get_profile_following(self, user_id):
        """ (Clubhouse, str) -> dict

        Get list of users
        """
        data = {
            "user_id": user_id
        }
        req = requests.post(f"https://{self.API_HOST}/api/get_following", headers=self.HEADERS, json=data)
        return req.json()


    @require_authentication
    def get_all_topics(self):
        """ (Clubhouse) -> dict

        Get list of topics, based on the server's channel selection algorithm
        """
        req = requests.get(f"https://{self.API_HOST}/api/get_all_topics", headers=self.HEADERS)
        return req.json()


    @require_authentication
    def get_channels(self):
        """ (Clubhouse) -> dict

        Get list of channels, based on the server's channel selection algorithm
        """
        req = requests.get(f"https://{self.API_HOST}/api/get_channels", headers=self.HEADERS)
        return req.json()


    @require_authentication
    def active_ping(self, channel):
        """ (Clubhouse, str) -> dict

        Keeping the user active while being in a chatroom
        """
        data = {
            "channel": channel,
            "chanel_id": None
        }
        req = requests.post(f"https://{self.API_HOST}/api/active_ping", headers=self.HEADERS, json=data)
        return req.json()


    @require_authentication
    def audience_reply(self, channel, raise_hands=True, unraise_hands=False):
        """ (Clubhouse, str, bool, bool) -> bool

        Request for raise_hands.
        """
        data = {
            "channel": channel,
            "raise_hands": raise_hands,
            "unraise_hands": unraise_hands
        }
        req = requests.post(f"https://{self.API_HOST}/api/audience_reply", headers=self.HEADERS, json=data)
        return req.json()


    @require_authentication
    def update_skintone(self, skintone=1):
        """ (Clubhouse, int) -> dict

        Updating skinetone for raising hands, etc.
        """
        skintone = int(skintone)
        if not 1 <= skintone <= 5:
            return False

        data = {
            "skintone": skintone
        }
        req = requests.post(f"https://{self.API_HOST}/api/update_skintone", headers=self.HEADERS, json=data)
        return req.json()


    @require_authentication
    def get_notifications(self, page_size=20, page=1):
        """ (Clubhouse, int, int) -> dict

        Get my notifications.
        """
        query = f"page_size={page_size}&page={page}"
        req = requests.get(f"https://{self.API_HOST}/api/get_notifications?{query}", headers=self.HEADERS)
        return req.json()


    @require_authentication
    def get_online_friends(self):
        """ (Clubhouse) -> dict

        Get online friends.
        """
        req = requests.post(f"https://{self.API_HOST}/api/get_online_friends", headers=self.HEADERS, json={})
        return req.json()


    @require_authentication
    def accept_speaker_invite(self, channel, user_id):
        """ (Clubhouse, str, int) -> dict

        Accept speaker's invitation, based on (channel, invited_moderator)
        `raise_hands` needs to be called first, prior to the invitation.
        """
        data = {
            "channel": channel,
            "user_id": int(user_id)
        }
        req = requests.post(f"https://{self.API_HOST}/api/accept_speaker_invite", headers=self.HEADERS, json=data)
        return req.json()


    @require_authentication
    def get_suggested_speakers(self, channel):
        """ (Clubhouse, str) -> dict

        Get suggested speakers from the given channel
        """
        data = {
            "channel": channel
        }
        req = requests.post(f"https://{self.API_HOST}/api/get_suggested_speakers", headers=self.HEADERS, json=data)
        return req.json()


    @require_authentication
    def create_channel(self, topic="", user_ids=(), is_private=False, is_social_mode=False):
        """ (Clubhouse, str, list, bool, bool) -> dict

        Create a new channel. Type of the room can be changed.
        """
        data = {
            "is_social_mode": is_social_mode,
            "is_private": is_private,
            "club_id": None,
            "user_ids": user_ids,
            "event_id": None,
            "topic": topic
        }
        req = requests.post(f"https://{self.API_HOST}/api/create_channel", headers=self.HEADERS, json=data)
        return req.json()


    @require_authentication
    def get_create_channel_targets(self):
        """ (Clubhouse) -> dict

        Not sure what this does.
        """
        data = {}
        req = requests.post(f"https://{self.API_HOST}/api/get_create_channel_targets", headers=self.HEADERS, json=data)
        return req.json()


if __name__ == "__main__":
    CLUBHOUSE = Clubhouse()

    print(CLUBHOUSE.get_channels())
    CURR_CHANNEL = "CHANGEME"
    print(CLUBHOUSE.join_channel(CURR_CHANNEL))
    time.sleep(4)
    print(CLUBHOUSE.leave_channel(CURR_CHANNEL))
    print("Clubhouse API worked successfully")

    # Check for authentication
    # if self.API_USER_ID != "CHANGEME":
    # self.HEADERS['CH-UserID'] = f"{API_USER_ID}"
    # self.HEADERS['Authorization'] = f"{API_USER_TOKEN}"
