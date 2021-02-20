## WARNING

* ___FOR REFERENCE AND EDUCATION PURPOSES ONLY. THIS DOES NOT COME WITH ANY KINDS OF WARRANTY.___

* ___PLEASE DO NOT CREATE BOTS OR DO ANY HARMFUL THINGS TO THE SERVICE. DON'T BREAK THINGS. DON'T BE EVIL.___

* ___THIS PROJECT WILL DISCONTINUE DEVELOPMENT ONCE DEVELOPERS RELEASE AN ANDROID BUILD.___


## Pull Requests / Issues

1. Please DO NOT request PR for minor (documentation|typo|paragraph) changes. All of them will be rejected and closed.
2. Check closed [issues](https://github.com/stypr/clubhouse-py/issues?q=is%3Aissue+is%3Aclosed) before asking a question / feature request.

## Clubhouse API written in Python

`clubhouse-py` is originally developed for the sake of interoperability.

Standalone client is also created with very basic features, including but not limited to the audio-chat.

Please note that you may get a permanent ban for sending invalid API requests. Server's ratelimit and security mechanisms are quite strict.

## Demo

Please click the image to open a Youtube video demo.

[![Demo video](https://img.youtube.com/vi/1L6bEoNKego/maxresdefault.jpg)](https://www.youtube.com/watch?v=1L6bEoNKego)

## Requirements

* Windows or OSX
* Python 3.7 or higher

## Installation

1. Clone project

```sh
$ git clone https://github.com/stypr/clubhouse-py.git clubhouse
$ cd clubhouse
```

2. You need to install dependencies first.

```sh
$ pip3 install -r requirements.txt
```

3. You need to install Agora SDK for voice communication. Refer to [Agora-Python-SDK#installation](https://github.com/AgoraIO-Community/Agora-Python-SDK#installation).


## Usage

* For calling APIs from other script

```python
from clubhouse import Clubhouse

...

if __name__ == "__main__":
    clubhouse = Clubhouse()
```

* For running a standalone client

```sh
$ python3 cli.py
```

## Supported features

### Pre-authentication

* def start_phone_number_auth(self, phone_number):
* def call_phone_number_auth(self, phone_number):
* def resend_phone_number_auth(self, phone_number):
* def complete_phone_number_auth(self, phone_number, verification_code):
* def check_for_update(self, is_testflight=False):

### Post-authentication

* def get_release_notes(self):
* def check_waitlist_status(self):
* def add_email(self, email):
* def update_photo(self, photo_filename):
* def follow(self, user_id, user_ids=None, source=4, source_topic_id=None):
* def unfollow(self, user_id):
* def block(self, user_id):
* def unblock(self, user_id):
* def follow_multiple(self, user_ids, user_id=None, source=7, source_topic_id=None):
* def follow_club(self, club_id, source_topic_id=None):
* def unfollow_club(self, club_id, source_topic_id=None):
* def update_follow_notifications(self, user_id, notification_type=2):
* def get_suggested_follows_similar(self, user_id):
* def get_suggested_follows_friends_only(self, club_id=None, upload_contacts=True, contacts=()):
* def get_suggested_follows_all(self, in_onboarding=True, page_size=50, page=1):
* def ignore_suggested_follow(self, user_id):
* def get_event(self, event_id, user_ids=None, club_id=None, is_member_only=False, event_hashid=None, description=None, time_start_epoch=None, name=None):
* def create_event(self, name, time_start_epoch, description, event_id=None, user_ids=(), club_id=None, is_member_only=False, event_hashid=None):
* def edit_event(self, name, time_start_epoch, description, event_id=None, user_ids=(), club_id=None, is_member_only=False, event_hashid=None):
* def delete_event(self, event_id, user_ids=None, club_id=None, is_member_only=False, event_hashid=None, description=None, time_start_epoch=None, name=None):
* def get_events(self, is_filtered=True, page_size=25, page=1):
* def get_club(self, club_id, source_topic_id=None):
* def get_club_members(self, club_id, return_followers=False, return_members=True, page_size=50, page=1):
* def get_settings(self):
* def get_welcome_channel(self):
* def hide_channel(self, channel, hide=True):
* def join_channel(self, channel, attribution_source="feed"):
* def leave_channel(self, channel):
* def make_channel_public(self, channel, channel_id=None):
* def make_channel_social(self, channel, channel_id=None):
* def end_channel(self, channel, channel_id=None):
* def make_moderator(self, channel, user_id):
* def block_from_channel(self, channel, user_id):
* def get_profile(self, user_id):
* def me(self, return_blocked_ids=False, timezone_identifier="Asia/Tokyo", return_following_ids=False):
* def get_following(self, user_id, page_size=50, page=1):
* def get_followers(self, user_id, page_size=50, page=1):
* def get_mutual_follows(self, user_id, page_size=50, page=1):
* def get_all_topics(self):
* def get_channels(self):
* def get_channel(self, channel, channel_id=None):
* def active_ping(self, channel):
* def audience_reply(self, channel, raise_hands=True, unraise_hands=False):
* def change_handraise_settings(self, channel, is_enabled=True, handraise_permission=1):
* def update_skintone(self, skintone=1):
* def get_notifications(self, page_size=20, page=1):
* def get_actionable_notifications(self):
* def get_online_friends(self):
* def accept_speaker_invite(self, channel, user_id):
* def reject_speaker_invite(self, channel, user_id):
* def invite_speaker(self, channel, user_id):
* def uninvite_speaker(self, channel, user_id):
* def mute_speaker(self, channel, user_id):
* def get_suggested_speakers(self, channel):
* def create_channel(self, topic="", user_ids=(), is_private=False, is_social_mode=False):
* def get_create_channel_targets(self):
* def get_suggested_invites(self, club_id=None, upload_contacts=True, contacts=()):
* def get_suggested_club_invites(self, upload_contacts=True, contacts=()):
* def invite_to_app(self, name, phone_number, message=None):
* def invite_from_waitlist(self, user_id):
* def search_users(self, query, followers_only=False, following_only=False, cofollows_only=False):
* def search_clubs(self, query, followers_only=False, following_only=False, cofollows_only=False):
* def get_topic(self, topic_id):
* def get_clubs_for_topic(self, topic_id, page_size=25, page=1):
* def get_clubs(self, is_startable_only):
* def get_users_for_topic(self, topic_id, page_size=25, page=1):
* def invite_to_existing_channel(self, channel, user_id):
* def update_username(self, username):
* def update_name(self, name):
* def update_twitter_username(self, username, twitter_token, twitter_secret):
* def update_instagram_username(self, code):
* def update_displayname(self, name):
* def refresh_token(self, refresh_token):
* def update_bio(self, bio):
* def record_action_trails(self, action_trails=()):
* def add_user_topic(self, club_id, topic_id):
* def remove_user_topic(self, club_id, topic_id):
* def report_incident(self, user_id, channel, incident_type, incident_description, email):
* def reject_welcome_channel(self):
* def update_channel_flags(self, channel, visibility, flag_title, unflag_title):
* def ignore_actionable_notification(self, actionable_notification_id):
* def invite_to_new_channel(self, user_id, channel):
* def accept_new_channel_invite(self, channel_invite_id):
* def reject_new_channel_invite(self, channel_invite_id):
* def cancel_new_channel_invite(self, channel_invite_id):
* def add_club_admin(self, club_id, user_id):
* def remove_club_admin(self, club_id, user_id):
* def remove_club_member(self, club_id, user_id):
* def accept_club_member_invite(self, club_id, source_topic_id=None):
* def add_club_member(self, club_id, user_id, name, phone_number, message, reason):
* def get_club_nominations(self, club_id, source_topic_id):
* def approve_club_nomination(self, club_id, source_topic_id, invite_nomination_id):
* def reject_club_nomination(self, club_id, source_topic_id, invite_nomination_id):
* def add_club_topic(self, club_id, topic_id):
* def remove_club_topic(self, club_id, topic_id):
* def get_events_to_start(self):
* def update_is_follow_allowed(self, club_id, is_follow_allowed=True):
* def update_is_membership_private(self, club_id, is_membership_private):
* def update_is_community(self, club_id, is_community):
* def update_club_description(self, club_id, description):

## Unsupported features

### Endpoints

* def update_club_rules(self):
* def update_club_topics(self):
* def get_events_for_user(self):

### PubNub

PubNub is used for the notification while being in a conversation.
This has not been implemented yet. However, you may utilize the PubSub keys provided in the sourcecode to implement this.

## Reference

You may also add more endpoints and features based on the following repositories.

Please note that these repositories were partially referenced to create this project.

Most of things were tested and handcrafted from scratch.

* https://github.com/Seia-Soto/clubhouse-api (NodeJS build)
* https://theori.io/research/korean/analyzing-clubhouse/ (Written in Korean)
