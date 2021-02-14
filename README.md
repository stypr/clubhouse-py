## Clubhouse API for python

WARNING: Make sure to take a look at the source code before starting.

For reference and education purposes only. 

Note that the software comes without any kinds of warranty.

This piece of code was originally developed for the sake of interoperability, but was never used.

Currently, audio-related features (agora.io / pubnub) are not yet implemented.

Please note that you may get a permanent ban for invalid API requests. Clubhouse's rate limit and security mechanisms are quite strict.

## Supported features

### Pre-authentication

* def start_phone_number_auth(self, phone_number):
* def complete_phone_number_auth(self, phone_number, verification_code):

### Post-authentication

* def check_for_update(self, is_testflight=False):
* add_email(self, email):
* update_photo(self, photo_filename):
* unfollow(self, user_id):
* follow(self, user_id, user_ids=None, source=4, source_topic_id=None):
* follow_club(self, club_id, source_topic_id=None):
* unfollow_club(self, club_id, source_topic_id=None):
* update_follow_notifications(self, user_id, notification_type=2):
* get_suggested_follows_similar(self, user_id):
* get_events(self, is_filtered=True, page_size=25, page=1):
* get_club(self, club_id, source_topic_id=None):
* get_club_members(self, club_id, return_followers=False, return_members=True, page_size=50, page=1):
* join_channel(self, channel, attribution_source="feed"):
* leave_channel(self, channel):
* get_profile(self, user_id):
* get_profile_self(self, return_blocked_ids=False, timezone_identifier="Asia/Tokyo", return_following_ids=False):
* get_profile_following(self, user_id):
* get_all_topics(self):
* get_channels(self):
* active_ping(self, channel):
* audience_reply(self, channel, raise_hands=True, unraise_hands=False):
* update_skintone(self, skintone=1):
* get_notifications(self, page_size=20, page=1):
* get_online_friends(self):
* accept_speaker_invite(self, channel, user_id):
* get_suggested_speakers(self, channel):
* create_channel(self, topic="", user_ids=(), is_private=False, is_social_mode=False):
* get_create_channel_targets(self):
* get_suggested_invites(self, club_id=None, upload_contacts=True, contacts=()):
* search_users(self, query, followers_only=False, following_only=False, cofollows_only=False):
* search_clubs(self, query, followers_only=False, following_only=False, cofollows_only=False):
* get_clubs_for_topic(self, topic_id, page_size=25, page=1):
* get_users_for_topic(self, topic_id, page_size=25, page=1):
* invite_to_existing_channel(self, channel, user_id):

## Reference

There are also some useful references for you.

You may also add more endpoints and features based on the following repositories.

Please note that these repositories were not used to develop this repository. Most of things were tested and handcrafted from scratch.

* https://github.com/zhuowei/ClubhouseAPI
* https://github.com/Seia-Soto/clubhouse-api
