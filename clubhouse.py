#/usr/bin/python -u
#-*- coding: utf-8 -*-

"""
clubhouse.py

API for Clubhouse (v297 / 0.1.27)
Developed for education purposes only.

Please know what you're doing!
Modifying a bit of header could result a permanent block on your account.
"""

import time
import requests

# App/API Information
API_HOST = "www.clubhouseapi.com"
API_BUILD_ID = "297"
API_BUILD_VERSION = "0.1.27"

# User information
API_USER_ID = "CHANGEME"
API_USER_TOKEN = "CHANGEME"
API_USER_DEVICE = "CHANGEME" # str(__import__("uuid").uuid4())
API_USER_AGENT = "clubhouse/297 (iPhone; iOS 13.5.1; Scale/3.00)"


# Some useful information for commmunication
PUBNUB_PUB_KEY = "pub-c-6878d382-5ae6-4494-9099-f930f938868b"
PUBNUB_SUB_KEY = "sub-c-a4abea84-9ca3-11ea-8e71-f2b83ac9263d"

TWITTER_ID = "NyJhARWVYU1X3qJZtC2154xSI"
TWITTER_SECRET = "ylFImLBFaOE362uwr4jut8S8gXGWh93S1TUKbkfh7jDIPse02o"

AGORA_KEY = "938de3e8055e42b281bb8c6f69c21f78"
SENTRY_KEY = "https://5374a416cd2d4009a781b49d1bd9ef44@o325556.ingest.sentry.io/5245095"
INSTABUG_KEY = "4e53155da9b00728caa5249f2e35d6b3"
AMPLITUDE_KEY = "9098a21a950e7cb0933fb5b30affe5be"

# Header
HEADERS = {
    "Authorization": f"Token {API_USER_TOKEN}",
    "CH-Languages": "en-JP,ja-JP",
    "CH-UserID": "(null)",
    "CH-Locale": "en_JP",
    "Accept": "application/json",
    "Accept-Language": "en-JP;q=1, ja-JP;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "CH-AppBuild": f"{API_BUILD_ID}",
    "CH-AppVersion": f"{API_BUILD_VERSION}",
    "CH-DeviceId": f"{API_USER_DEVICE}",
    "User-Agent": f"{API_USER_AGENT}",
    "Connection": "close",
    "Content-Type": "application/json; charset=utf-8",
    "Cookie": "__cfduid=def2c5e4b7f2e3ba18ab49625408b043d1613200581", # CHANGEME
}

# Check for authentication
if API_USER_ID != "CHANGEME":
    HEADERS['CH-UserID'] = f"{API_USER_ID}"
    HEADERS['Authorization'] = f"{API_USER_TOKEN}"


def start_phone_number_auth(phone_number):
    """ (str) -> dict

    Begin phone number authentication.

    Phone number examples:
        +821012341337
        +818043211234
        ...
    """
    data = {
        "phone_number": phone_number
    }
    req = requests.post(f"https://{API_HOST}/api/start_phone_number_auth", headers=HEADERS, json=data)
    return req.json()


def complete_phone_number_auth(phone_number, verification_code):
    """ (str, str) -> dict

    Complete phone number authentication.
    This should return `auth_token`, `access_token`, `refresh_token`, is_waitlisted, ...

    Please note that output may be different depending on the status of the authenticated user
    """
    data = {
        "phone_number": phone_number,
        "verification_code": verification_code
    }
    req = requests.post(f"https://{API_HOST}/api/complete_phone_number_auth", headers=HEADERS, json=data)
    return req.json()


def join_channel(channel, attribution_source="feed"):
    """ (str, str) -> dict

    Join the given channel
    """
    # Join channel
    data = {
        "channel": channel,
        "attribution_source": attribution_source,
        "attribution_details": "eyJpc19leHBsb3JlIjpmYWxzZSwicmFuayI6MX0=",
    }
    req = requests.post(f"https://{API_HOST}/api/join_channel", headers=HEADERS, json=data)
    return req.json()


def leave_channel(channel):
    """ (str) -> dict

    Leave the given channel
    """
    data = {
        "channel": channel,
        "channel_id": None
    }
    req = requests.post(f"https://{API_HOST}/api/leave_channel", headers=HEADERS, json=data)
    return req.json()


def get_profile(user_id):
    """ (str) -> dict

    Get someone else's profile
    """
    data = {
        "user_id": user_id
    }
    req = requests.post(f"https://{API_HOST}/api/get_profile", headers=HEADERS, json=data)
    return req.json()


def get_profile_self(return_blocked_ids=False, timezone_identifier="Asia/Tokyo", return_following_ids=False):
    """ (bool, str, bool) -> dict

    Get my information
    """
    # Get myself
    data = {
        "return_blocked_ids": return_blocked_ids,
        "timezone_identifier": timezone_identifier,
        "return_following_ids": return_following_ids
    }
    req = requests.post(f"https://{API_HOST}/api/me", headers=HEADERS, json=data)
    return req.json()


def get_channels():
    """ dict

    Get list of channels, based on the server's channel selection algorithm
    """
    req = requests.get(f"https://{API_HOST}/api/get_channels", headers=HEADERS)
    return req.json()


def active_ping(channel):
    """ (str) -> dict

    Keeping the user active while being in a chatroom
    """
    data = {
        "channel": channel,
        "chanel_id": None
    }
    req = requests.post(f"https://{API_HOST}/api/active_ping", headers=HEADERS, json=data)
    return req.json()


def audience_reply(channel, raise_hands=True, unraise_hands=False):
    """ (str, bool, bool) -> bool

    Request for raise_hands.
    """
    data = {
        "channel": channel,
        "raise_hands": raise_hands,
        "unraise_hands": unraise_hands
    }
    req = requests.post(f"https://{API_HOST}/api/audience_reply", headers=HEADERS, json=data)
    return req.json()


def update_skintone(skintone=1):
    """ (int) -> dict

    Updating skinetone for raising hands, etc.
    """
    skintone = int(skintone)
    if not 1 <= skintone <= 5:
        return False

    data = {
        "skintone": skintone
    }
    req = requests.post(f"https://{API_HOST}/api/update_skintone", headers=HEADERS, json=data)
    return req.json()


def get_notifications(page_size=20, page=1):
    """ (int, int) -> dict

    Get my notifications.
    """
    query = f"page_size={page_size}&page={page}"
    req = requests.get(f"https://{API_HOST}/api/get_notifications?{query}", headers=HEADERS)
    return req.json()


def get_online_friends():
    """ dict

    Get online friends.
    """
    req = requests.post(f"https://{API_HOST}/api/get_online_friends", headers=HEADERS, json={})
    return req.json()


def accept_speaker_invite(channel, user_id):
    """ (str, int) -> dict

    Accept speaker's invitation, based on (channel, invited_moderator)
    `raise_hands` needs to be called first, prior to the invitation.
    """
    data = {
        "channel": channel,
        "user_id": int(user_id)
    }
    req = requests.post(f"https://{API_HOST}/api/accept_speaker_invite", headers=HEADERS, json=data)
    return req.json()


def get_suggested_speakers(channel):
    """ (str) -> dict

    Get suggested speakers from the given channel
    """
    data = {
        "channel": channel
    }
    req = requests.post(f"https://{API_HOST}/api/get_suggested_speakers", headers=HEADERS, json=data)
    return req.json()


def create_channel(topic="", user_ids=[], is_private=False, is_social_mode=False):
    """ (str, list, bool, bool) -> dict

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
    req = requests.post(f"https://{API_HOST}/api/create_channel", headers=HEADERS, json=data)
    return req.json()


def get_create_channel_targets():
    """ dict

    Not sure what this does.
    """
    data = {}
    req = requests.post(f"https://{API_HOST}/api/get_create_channel_targets", headers=HEADERS, json=data)
    return req.json()


if __name__ == "__main__":
    CURR_CHANNEL = "CHANGEME"
    print(join_channel(CURR_CHANNEL))
    time.sleep(4)
    print(leave_channel(CURR_CHANNEL))
    print("Clubhouse API worked successfully")
