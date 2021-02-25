## WARNING

* ___FOR REFERENCE AND EDUCATION PURPOSES ONLY. THIS DOES NOT COME WITH ANY KINDS OF WARRANTY.___

* ___PLEASE DO NOT CREATE BOTS OR DO ANY HARMFUL THINGS TO THE SERVICE. DON'T BREAK THINGS. DON'T BE EVIL.___

* ___THIS PROJECT WILL DISCONTINUE DEVELOPMENT ONCE DEVELOPERS RELEASE AN ANDROID BUILD.___


## Pull Requests / Issues

I have disabled PRs and issues temporarily. I may/may not continue on development.

[Closed PRs](https://github.com/stypr/clubhouse-py/pulls?q=is%3Apr+is%3Aclosed) / [Closed Issues](https://github.com/stypr/clubhouse-py/issues?q=is%3Aissue+is%3Aclosed) 


## QnA

> Are you affiliated with those guys who built the website that streamed Clubhouse rooms?

No.

I am not affiliated with anyone or any company. 

This is just my personal project.


> Why did you develop this? what is your whole intention about releasing this to public?

1. There has been a lot of articles about security concerns of Clubhouse when I joined Clubhouse.
    * [Clubhouse And Its Privacy & Security Risk](https://medium.com/technology-hits/clubhouse-and-its-security-risk-201526fd06d1)
    * [Clubhouse says it will improve security after researchers raise China spying concerns](https://www.theverge.com/2021/2/14/22282772/clubhouse-improve-security-stanford-researchers-china-security)
    * [Clubhouse: Security and privacy in the new social media app](https://blog.avast.com/clubhouse-security-and-privacy-avast)
2. I decided to take a closer look at the application by reverse engineering the app. With this I can find out what is the truth and what isn't.
3. I found some possible security risks during the analysis. However, I will not disclose this information until things are properly and safely mitigated.
4. I was planning to destroy my work after doing the analysis, but I've decided to share the code as (i) I found out that the whole authentication flow and API base may change in the future, so this src will be priceless at some point of time (ii) I think it would be better off for Android phone users to interact with others. (iii) I wanted more people to join into conversations and have fun.

> What if someone uses your code to do malicious activities? Wouldn't that be an issue?

1. Evil people with evil intentions will do bad things even if the sourcecode wasn't released.
2. There has been already numerous reports of trollers doing bad things around here and there. ([Reference](https://github.com/ai-eks/OpenClubhouse)) These trollers have also disclosed their sourcecode, so please have some time to check their source code. These guys did their stuff without even referencing other's source code. This already shows that evil people will always try to break stuff and do bad things regardless of any other helpful factors.
4. What I shared on GitHub is a very basic thing that a reverse engineer can do. It's technically not difficult to get these information snatched from the binary.
5. Clubhouse has a straightforward API with some unknown security mechanisms; They have implemented things to ban you for excessive usage.
6. DO NOT even try anything if you don't really know what you're trying to do. I have been mentioning the same message over here and there.
7. I am not liable for anything you do with this application. I already warned about this as well.

> You've released API keys and secret keys. Wouldn't that severely impact the server?

1. Let me make things clear first. Those keys are NOT confidential secrets.
2. These are just identifiers for third-party services to declare that your actions are coming from the Clubhouse app.
3. These keys are used for communication, adding your instagram/twitter accounts, chat notifications, etc.
4. I wouldn't have disclosed keys if these keys were actual secrets/confidentials.

> Can you disclose what you've found during an analysis?

No.

I will only disclose these issues to the vendor. 

I think issues I found seem to be already reported by other researchers as well and they might be already aware of these issues and circumstances.

I've already sent a twitter DM to one of Clubhouse employees as of 2021/Feb/24, but I haven't received any messages yet.

> Then, can you explain a bit on that myth about the Chinese IP thing?

1. It's fixed in the latest version. You don't have to worry about this anymore.
2. Worth reading [this technical post](https://theori.io/research/korean/analyzing-clubhouse) for more detailed information.
3. The blog post is written in Korean so please translate the page.

> I heard that the app is using iOS just to prevent the voice recording. Releasing these kinds of code can possibly make it 'easier' to make voice recording. I want to hear your opinions.

1. There is literally no way to disallow users from recording the voice. Imagine some people having a "physical" recording device next to them. How will you or the Clubhouse app detect such actions?
2. Moreover, there is no way to even catch or block the user when someone records and shares your voice record anonymously.
3. I think there are much more serious risks/problems that CH developers need to take a look at. There seem to be more high priority issues than this one. (in which I assume they're already working on atm)

> What do you think about the Clubhouse app? Is the app secure enough? Can you rate their security quality?

From my very personal perspective as a security engineer:

1. API: Well-made, and I see developers are trying to fix some security issues here. although they still haven't fixed it, yet.
2. Notifications: LGTM. but sometimes the server goes down pretty frequently. I haven't looked deep into it.
3. Interaction with voice protocol: meh, but it looks like they're trying to work on it. I think it is more fun to dig more in but doing so will go out of the scope.

> Don't you think your actions were ethically wrong?

1. I also heard that these issues were raised and discussed over several months in an open Clubhouse chatroom, and I guess I've clarified a lot of questions people had over for several months. I guess this already helped some of engineers who were pretty much concerned about things here.
2. I am pretty sure that somemone would've done this if it wasn't me anyways. At least I gave some initiative to try with good wills and share details with you guys.

> I heard that the voice communication is not encrypted. is this true?

As of 2021/Feb/24,

1. [This technical post](https://theori.io/research/korean/analyzing-clubhouse) already explains things really well about the current situation.
2. I was also curious and read some documentations in Agora.io ([Reference](https://docs.agora.io/en/Voice/channel_encryption_android))
3. As mentioned in the technical post, it looks like the communication encryption is never done. 
4. Also, ny looking at those documentations and my codes, you may have already noticed that the `enableEncryption` is never used here.
5. In the latest version, they have added the encryption routine but it is not yet used. It should be fixed in the upcoming releases.

> I heard that the app is also using Camera permissions. I am really worried right now.

You don't have to worry about this as well. There are some things to share here.

1. It may have been turned on because you tried to take a photo of yourself to put a profile image.
2. ... or the voice SDK is trying to secretly access your camera. But from my analysis, I don't see anything like that happening from the App to take photos or videos. Although they have the feature to communicate with your camera, the app does not use that part of the feature atm. (Confirmed safe as of Feb 2021)

> I heard that the app is also taking your information while adding your Instagram/Twitter accounts.  did you check that?

Yes. You don't have to worry about this as well.

Clubhouse only takes very basic part of your information just to verify that you are the owner of the given account.

* For Instagram: You're allowing Clubhouse to just take your username. That's all.
* For Twitter: You're allowing Clubhouse to read your profile, timeline and tweets. However, Clubhouse CANNOT read your personal DMs. This is the least permission they can ask to a user. 

The permission setting can also change, but in that case you will be asked again to re-authorize the application with additional permission. Don't worry so much about this part.

If you're still worried about this, You can also revoke the access by doing the following action.

* For Instagram: `Settings` -> `Security` -> `Apps and Websites` -> `Active` -> `Clubhouse` -> revoke access.
* For Twitter: `Settings` -> `Security and account access` -> `Apps and sessions` -> `Connected apps` -> `Clubhouse` -> revoke acccess.

> Do you have any plans to do further analysis if Clubhouse opens up a bug bounty programme?

Very unlikely.

> Is Clubhouse actually working hard to fix all kinds of security stuff? I'm really worried.

Yes, but there are some reasons why developers are taking some time.

1. They probably don't want to break things while updating. Developers also need time to fix and test their own code.
2. Clubhouse is a small company with ~10 employees. You also need to consider the manpower to fix issues.
3. It may take a few days to get their updates reviewed by Apple.
4. They also need to have some time to make "best moves" in order to efficiently fix issues.

> What would you do if Clubhouse tries to hire you?

This doesn't make sense in the first place.
1. I don't think Clubhouse team likes me. (Assumption)
2. I see some people who were very uncomfortable about me speaking about these issues in the first place. One guy even kicked me out of his channel for talking about this topic.
3. I'm not an American citizen. It has been always difficult to get US visas for foreigners. Also, I don't really prefer to work in US. (no offense here, it's just my preferences)

> As a typical user, what do I need to be very careful about when using Clubhouse?

1. As a speaker: Always assume that someone is recording your voice. Always think multiple times before you speak. Don't speak out confidential/personal stuff. I am not saying that the Clubhouse is recording your voice. There are chances that some trolls or reporters are trying to record multiple chatrooms. 
2. As a moderator: You need to be alert and make quick decisions to make your channel healthy. If someone says something weird or does something crazy, you need to make quick decisions. Move that speaker to audience or just kick the user out of the channel. Simple as that. Also, be aware that you have a lot of privileges. Do not give moderators to unknown people. Any moderator can destroy the channel.

> Why did you block issues / PRs?

Mainly two reasons:

1. There are some people sending me some issues without actually looking into sourcecodes and testing codes.
2. There are some people wasting their time to send worthless PRs. 

I will not open these for the time being. You can send me a message or make your own fork, and I will take a look whenever I'm free

> How can I contact you?

* Instagram: [@brokenpacifist](https://www.instagram.com/brokenpacifist/)
* Twitter: [@stereotype32](https://twitter.com/stereotype32)
* Clubhouse: @stypr


## Clubhouse API written in Python

`clubhouse-py` is originally developed for the sake of interoperability.

Standalone client is also created with very basic features, including but not limited to the audio-chat.

Please note that you may get a permanent ban for sending invalid API requests. Server's ratelimit and security mechanisms are quite strict.

## Downloads

Check [Releases](https://github.com/stypr/clubhouse-py/releases). OSX(x86_64) may not be stable for use yet.

## Demo

Please click the image to open a Youtube video demo.

[![Demo video](https://img.youtube.com/vi/1L6bEoNKego/maxresdefault.jpg)](https://www.youtube.com/watch?v=1L6bEoNKego)

## Requirements

* Windows or OSX
* Python 3.7 or higher

## Installation

### By pip 

1. Install by pip

```sh
$ pip3 install clubhouse-py
...
Successfully built clubhouse-py
Installing collected packages: clubhouse-py
Successfully installed clubhouse-py-304.0.1
```

2. You need to install Agora SDK for voice communication. Refer to [Agora-Python-SDK#installation](https://github.com/AgoraIO-Community/Agora-Python-SDK#installation).

### Manual Installation

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
from clubhouse.clubhouse import Clubhouse

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

## Reference / Recommended to read

You may also add more endpoints and features based on the following repositories.

Please note that these repositories were partially referenced to create this project.

Most of things were tested and handcrafted from scratch.

* https://github.com/Seia-Soto/clubhouse-api (NodeJS build)
* https://github.com/grishka/Houseclub (Android build)
* https://theori.io/research/korean/analyzing-clubhouse/ (Written in Korean)
