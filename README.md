## Clubhouse API for python

___FOR REFERENCE AND EDUCATION PURPOSES ONLY. THIS DOES NOT COME WITH ANY KINDS OF WARRANTY.___

`clubhouse-py` is originally developed for the sake of interoperability.

Currently, audio-related features (agora.io / pubnub) are not yet implemented.

Please note that you may get a permanent ban for sending invalid API requests. Server's ratelimit and security mechanisms are quite strict.

## Demo

Please note that the SDK may be a bit unstable for using the standalone client.

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/1L6bEoNKego/0.jpg)](https://www.youtube.com/watch?v=1L6bEoNKego)

## Requirements

* Windows or OSX
* Python 3.7 or higher

## Installation

1. You need to install dependencies first.

```bash
# pip3 install -r requirements.txt
```

2. You need to install Agora SDK for voice communication. Refer to [Agora-Python-SDK#installation](https://github.com/AgoraIO-Community/Agora-Python-SDK#installation).

## Usage

* For calling APIs from other script

```
from clubhouse import Clubhouse

...

if __name__ == "__main__":
    clubhouse = Clubhouse()
```

* For running a standalone test client

```bash
# python3 clubhouse.py
```

## Supported features

### Pre-authentication

* def start_phone_number_auth(self, phone_number):
* def complete_phone_number_auth(self, phone_number, verification_code):

### Post-authentication

* def check_for_update(self, is_testflight=False):
* def add_email(self, email):
* def update_photo(self, photo_filename):
* def unfollow(self, user_id):
* def follow(self, user_id, user_ids=None, source=4, source_topic_id=None):
* def follow_club(self, club_id, source_topic_id=None):
* def unfollow_club(self, club_id, source_topic_id=None):
* def update_follow_notifications(self, user_id, notification_type=2):
* def get_suggested_follows_similar(self, user_id):
* def get_suggested_follows_friends_only(self, club_id=None, upload_contacts=True, contacts=()):
* def get_suggested_follows_all(self, in_onboarding=True, page_size=50, page=1):
* def get_events(self, is_filtered=True, page_size=25, page=1):
* def get_club(self, club_id, source_topic_id=None):
* def get_club_members(self, club_id, return_followers=False, return_members=True, page_size=50, page=1):
* def get_settings(self):
* def get_welcome_channel(self):
* def join_channel(self, channel, attribution_source="feed"):
* def leave_channel(self, channel):
* def get_profile(self, user_id):
* def get_profile_self(self, return_blocked_ids=False, timezone_identifier="Asia/Tokyo", return_following_ids=False):
* def get_following(self, user_id):
* def get_all_topics(self):
* def get_channels(self):
* def get_channel(self, channel, channel_id=None):
* def active_ping(self, channel):
* def audience_reply(self, channel, raise_hands=True, unraise_hands=False):
* def update_skintone(self, skintone=1):
* def get_notifications(self, page_size=20, page=1):
* def get_actionable_notifications(self):
* def get_online_friends(self):
* def accept_speaker_invite(self, channel, user_id):
* def uninvite_speaker(self, channel, user_id):
* def get_suggested_speakers(self, channel):
* def create_channel(self, topic="", user_ids=(), is_private=False, is_social_mode=False):
* def get_create_channel_targets(self):
* def get_suggested_invites(self, club_id=None, upload_contacts=True, contacts=()):
* def get_suggested_club_invites(self, upload_contacts=True, contacts=()):
* def invite_to_app(self, name, phone_number, message=None):
* def invite_from_waitlist(self, user_id):
* def search_users(self, query, followers_only=False, following_only=False, cofollows_only=False):
* def search_clubs(self, query, followers_only=False, following_only=False, cofollows_only=False):
* def get_clubs_for_topic(self, topic_id, page_size=25, page=1):
* def get_users_for_topic(self, topic_id, page_size=25, page=1):
* def invite_to_existing_channel(self, channel, user_id):
* def update_username(self, username):
* def refresh_token(self, refresh_token):
* def update_bio(self, bio):

## Reference

You may also add more endpoints and features based on the following repositories.

Please note that these repositories were not used to develop this repository.

Most of things were tested and handcrafted from scratch.

* https://github.com/zhuowei/ClubhouseAPI
* https://github.com/Seia-Soto/clubhouse-api
* https://theori.io/research/korean/analyzing-clubhouse/ (Korean)
