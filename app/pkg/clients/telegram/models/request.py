"""Request models for telegram webhook."""

from typing import Any, List, Optional, Union

from pydantic import BaseModel, Field


class Update(BaseModel):
    """This object represents an incoming update.At most one of the optional
    parameters can be present in any given update."""

    update_id: int
    """The update's unique identifier.

    Update identifiers start from a certain positive number and increase
    sequentially. This identifier becomes especially handy if you're
    using webhooks, since it allows you to ignore repeated updates or to
    restore the correct update sequence, should they get out of order.
    If there are no new updates for at least a week, then identifier of
    the next update will be chosen randomly instead of sequentially.
    """

    message: Optional["Message"] = None
    """Optional.

    New incoming message of any kind - text, photo, sticker,
    etc.
    """

    edited_message: Optional["Message"] = None
    """Optional.

    New version of a message that is known to the bot and was edited.
    This update may at times be triggered by changes to message fields
    that are either unavailable or not actively used by your bot.
    """

    channel_post: Optional["Message"] = None
    """Optional.

    New incoming channel post of any kind - text, photo,
    sticker, etc.
    """

    edited_channel_post: Optional["Message"] = None
    """Optional.

    New version of a channel post that is known to the bot and was
    edited. This update may at times be triggered by changes to message
    fields that are either unavailable or not actively used by your bot.
    """

    business_connection: Optional["BusinessConnection"] = None
    """Optional.

    The bot was connected to or disconnected from a business account, or
    a user edited an existing connection with the bot
    """

    business_message: Optional["Message"] = None
    """Optional.

    New message from a connected business account
    """

    edited_business_message: Optional["Message"] = None
    """Optional.

    New version of a message from a connected business account
    """

    deleted_business_messages: Optional["BusinessMessagesDeleted"] = None
    """Optional.

    Messages were deleted from a connected business account
    """

    message_reaction: Optional["MessageReactionUpdated"] = None
    """Optional.

    A reaction to a message was changed by a user. The bot must be an
    administrator in the chat and must explicitly specify
    \"message_reaction\" in the list of allowed_updates to receive these
    updates. The update isn't received for reactions set by bots.
    """

    message_reaction_count: Optional["MessageReactionCountUpdated"] = None
    """Optional.

    Reactions to a message with anonymous reactions were changed. The
    bot must be an administrator in the chat and must explicitly specify
    \"message_reaction_count\" in the list of allowed_updates to receive
    these updates. The updates are grouped and can be sent with delay up
    to a few minutes.
    """

    inline_query: Optional["InlineQuery"] = None
    """Optional.

    New incoming inline query
    """

    chosen_inline_result: Optional["ChosenInlineResult"] = None
    """Optional.

    The result of an inline query that was chosen by a user and sent to
    their chat partner. Please see our documentation on the feedback
    collecting for details on how to enable these updates for your bot.
    """

    callback_query: Optional["CallbackQuery"] = None
    """Optional.

    New incoming callback query
    """

    shipping_query: Optional["ShippingQuery"] = None
    """Optional.

    New incoming shipping query. Only for invoices with flexible price
    """

    pre_checkout_query: Optional["PreCheckoutQuery"] = None
    """Optional.

    New incoming pre-checkout query. Contains full information about
    checkout
    """

    poll: Optional["Poll"] = None
    """Optional.

    New poll state. Bots receive only updates about manually stopped
    polls and polls, which are sent by the bot
    """

    poll_answer: Optional["PollAnswer"] = None
    """Optional.

    A user changed their answer in a non-anonymous poll. Bots receive
    new votes only in polls that were sent by the bot itself.
    """

    my_chat_member: Optional["ChatMemberUpdated"] = None
    """Optional.

    The bot's chat member status was updated in a chat. For private
    chats, this update is received only when the bot is blocked or
    unblocked by the user.
    """

    chat_member: Optional["ChatMemberUpdated"] = None
    """Optional.

    A chat member's status was updated in a chat. The bot must be an
    administrator in the chat and must explicitly specify
    \"chat_member\" in the list of allowed_updates to receive these
    updates.
    """

    chat_join_request: Optional["ChatJoinRequest"] = None
    """Optional.

    A request to join the chat has been sent. The bot must have the
    can_invite_users administrator right in the chat to receive these
    updates.
    """

    chat_boost: Optional["ChatBoostUpdated"] = None
    """Optional.

    A chat boost was added or changed. The bot must be an administrator
    in the chat to receive these updates.
    """

    removed_chat_boost: Optional["ChatBoostRemoved"] = None
    """Optional.

    A boost was removed from a chat. The bot must be an administrator in
    the chat to receive these updates.
    """


class WebhookInfo(BaseModel):
    """Describes the current status of a webhook."""

    url: str
    """Webhook URL, may be empty if webhook is not set up."""

    has_custom_certificate: bool
    """True, if a custom certificate was provided for webhook certificate
    checks."""

    pending_update_count: int
    """Number of updates awaiting delivery."""

    ip_address: Optional[str] = None
    """Optional.

    Currently used webhook IP address
    """

    last_error_date: Optional[int] = None
    """Optional.

    Unix time for the most recent error that happened when trying to
    deliver an update via webhook
    """

    last_error_message: Optional[str] = None
    """Optional.

    Error message in human-readable format for the most recent error
    that happened when trying to deliver an update via webhook
    """

    last_synchronization_error_date: Optional[int] = None
    """Optional.

    Unix time of the most recent error that happened when trying to
    synchronize available updates with Telegram datacenters
    """

    max_connections: Optional[int] = None
    """Optional.

    The maximum allowed number of simultaneous HTTPS connections to the
    webhook for update delivery
    """

    allowed_updates: Optional[List[str]] = None
    """Optional.

    A list of update types the bot is subscribed to. Defaults to all
    update types except chat_member
    """


class User(BaseModel):
    """This object represents a Telegram user or bot."""

    id: int
    """Unique identifier for this user or bot.

    This number may have more than 32 significant bits and some
    programming languages may have difficulty/silent defects in
    interpreting it. But it has at most 52 significant bits, so a 64-bit
    integer or double-precision float type are safe for storing this
    identifier.
    """

    is_bot: bool
    """True, if this user is a bot."""

    first_name: str
    """User's or bot's first name."""

    last_name: Optional[str] = None
    """Optional.

    User's or bot's last name
    """

    username: Optional[str] = None
    """Optional.

    User's or bot's username
    """

    language_code: Optional[str] = None
    """Optional.

    IETF language tag of the user's language
    """

    is_premium: Optional[bool] = None
    """Optional.

    True, if this user is a Telegram Premium user
    """

    added_to_attachment_menu: Optional[bool] = None
    """Optional.

    True, if this user added the bot to the attachment menu
    """

    can_join_groups: Optional[bool] = None
    """Optional.

    True, if the bot can be invited to groups. Returned only in getMe.
    """

    can_read_all_group_messages: Optional[bool] = None
    """Optional.

    True, if privacy mode is disabled for the bot. Returned only in
    getMe.
    """

    supports_inline_queries: Optional[bool] = None
    """Optional.

    True, if the bot supports inline queries. Returned only in getMe.
    """

    can_connect_to_business: Optional[bool] = None
    """Optional.

    True, if the bot can be connected to a Telegram Business account to
    receive its messages. Returned only in getMe.
    """


class Chat(BaseModel):
    """This object represents a chat."""

    id: int
    """Unique identifier for this chat.

    This number may have more than 32 significant bits and some
    programming languages may have difficulty/silent defects in
    interpreting it. But it has at most 52 significant bits, so a signed
    64-bit integer or double-precision float type are safe for storing
    this identifier.
    """

    type: str
    """Type of the chat, can be either “private”, “group”, “supergroup” or
    “channel”"""

    title: Optional[str] = None
    """Optional.

    Title, for supergroups, channels and group chats
    """

    username: Optional[str] = None
    """Optional.

    Username, for private chats, supergroups and channels if available
    """

    first_name: Optional[str] = None
    """Optional.

    First name of the other party in a private chat
    """

    last_name: Optional[str] = None
    """Optional.

    Last name of the other party in a private chat
    """

    is_forum: Optional[bool] = None
    """Optional.

    True, if the supergroup chat is a forum (has topics enabled)
    """


class ChatFullInfo(BaseModel):
    """This object contains full information about a chat."""

    id: int
    """Unique identifier for this chat.

    This number may have more than 32 significant bits and some
    programming languages may have difficulty/silent defects in
    interpreting it. But it has at most 52 significant bits, so a signed
    64-bit integer or double-precision float type are safe for storing
    this identifier.
    """

    type: str
    """Type of the chat, can be either “private”, “group”, “supergroup” or
    “channel”"""

    accent_color_id: int
    """Identifier of the accent color for the chat name and backgrounds of the
    chat photo, reply header, and link preview.

    See accent colors for more details.
    """

    max_reaction_count: int
    """The maximum number of reactions that can be set on a message in the
    chat."""

    title: Optional[str] = None
    """Optional.

    Title, for supergroups, channels and group chats
    """

    username: Optional[str] = None
    """Optional.

    Username, for private chats, supergroups and channels if available
    """

    first_name: Optional[str] = None
    """Optional.

    First name of the other party in a private chat
    """

    last_name: Optional[str] = None
    """Optional.

    Last name of the other party in a private chat
    """

    is_forum: Optional[bool] = None
    """Optional.

    True, if the supergroup chat is a forum (has topics enabled)
    """

    photo: Optional["ChatPhoto"] = None
    """Optional.

    Chat photo
    """

    active_usernames: Optional[List[str]] = None
    """Optional.

    If non-empty, the list of all active chat usernames; for private
    chats, supergroups and channels
    """

    birthdate: Optional["Birthdate"] = None
    """Optional.

    For private chats, the date of birth of the user
    """

    business_intro: Optional["BusinessIntro"] = None
    """Optional.

    For private chats with business accounts, the intro of the business
    """

    business_location: Optional["BusinessLocation"] = None
    """Optional.

    For private chats with business accounts, the location of the
    business
    """

    business_opening_hours: Optional["BusinessOpeningHours"] = None
    """Optional.

    For private chats with business accounts, the opening hours of the
    business
    """

    personal_chat: Optional["Chat"] = None
    """Optional.

    For private chats, the personal channel of the user
    """

    available_reactions: Optional[List["ReactionType"]] = None
    """Optional.

    List of available reactions allowed in the chat. If omitted, then
    all emoji reactions are allowed.
    """

    background_custom_emoji_id: Optional[str] = None
    """Optional.

    Custom emoji identifier of the emoji chosen by the chat for the
    reply header and link preview background
    """

    profile_accent_color_id: Optional[int] = None
    """Optional.

    Identifier of the accent color for the chat's profile background.
    See profile accent colors for more details.
    """

    profile_background_custom_emoji_id: Optional[str] = None
    """Optional.

    Custom emoji identifier of the emoji chosen by the chat for its
    profile background
    """

    emoji_status_custom_emoji_id: Optional[str] = None
    """Optional.

    Custom emoji identifier of the emoji status of the chat or the other
    party in a private chat
    """

    emoji_status_expiration_date: Optional[int] = None
    """Optional.

    Expiration date of the emoji status of the chat or the other party
    in a private chat, in Unix time, if any
    """

    bio: Optional[str] = None
    """Optional.

    Bio of the other party in a private chat
    """

    has_private_forwards: Optional[bool] = None
    """Optional.

    True, if privacy settings of the other party in the private chat
    allows to use tg://user?id=<user_id> links only in chats with the
    user
    """

    has_restricted_voice_and_video_messages: Optional[bool] = None
    """Optional.

    True, if the privacy settings of the other party restrict sending
    voice and video note messages in the private chat
    """

    join_to_send_messages: Optional[bool] = None
    """Optional.

    True, if users need to join the supergroup before they can send
    messages
    """

    join_by_request: Optional[bool] = None
    """Optional.

    True, if all users directly joining the supergroup without using an
    invite link need to be approved by supergroup administrators
    """

    description: Optional[str] = None
    """Optional.

    Description, for groups, supergroups and channel chats
    """

    invite_link: Optional[str] = None
    """Optional.

    Primary invite link, for groups, supergroups and channel chats
    """

    pinned_message: Optional["Message"] = None
    """Optional.

    The most recent pinned message (by sending date)
    """

    permissions: Optional["ChatPermissions"] = None
    """Optional.

    Default chat member permissions, for groups and supergroups
    """

    can_send_paid_media: Optional[bool] = None
    """Optional.

    True, if paid media messages can be sent or forwarded to the channel
    chat. The field is available only for channel chats.
    """

    slow_mode_delay: Optional[int] = None
    """Optional.

    For supergroups, the minimum allowed delay between consecutive
    messages sent by each unprivileged user; in seconds
    """

    unrestrict_boost_count: Optional[int] = None
    """Optional.

    For supergroups, the minimum number of boosts that a non-
    administrator user needs to add in order to ignore slow mode and
    chat permissions
    """

    message_auto_delete_time: Optional[int] = None
    """Optional.

    The time after which all messages sent to the chat will be
    automatically deleted; in seconds
    """

    has_aggressive_anti_spam_enabled: Optional[bool] = None
    """Optional.

    True, if aggressive anti-spam checks are enabled in the supergroup.
    The field is only available to chat administrators.
    """

    has_hidden_members: Optional[bool] = None
    """Optional.

    True, if non-administrators can only get the list of bots and
    administrators in the chat
    """

    has_protected_content: Optional[bool] = None
    """Optional.

    True, if messages from the chat can't be forwarded to other chats
    """

    has_visible_history: Optional[bool] = None
    """Optional.

    True, if new chat members will have access to old messages;
    available only to chat administrators
    """

    sticker_set_name: Optional[str] = None
    """Optional.

    For supergroups, name of the group sticker set
    """

    can_set_sticker_set: Optional[bool] = None
    """Optional.

    True, if the bot can change the group sticker set
    """

    custom_emoji_sticker_set_name: Optional[str] = None
    """Optional.

    For supergroups, the name of the group's custom emoji sticker set.
    Custom emoji from this set can be used by all users and bots in the
    group.
    """

    linked_chat_id: Optional[int] = None
    """Optional.

    Unique identifier for the linked chat, i.e. the discussion group
    identifier for a channel and vice versa; for supergroups and channel
    chats. This identifier may be greater than 32 bits and some
    programming languages may have difficulty/silent defects in
    interpreting it. But it is smaller than 52 bits, so a signed 64 bit
    integer or double-precision float type are safe for storing this
    identifier.
    """

    location: Optional["ChatLocation"] = None
    """Optional.

    For supergroups, the location to which the supergroup is connected
    """


class Message(BaseModel):
    """This object represents a message."""

    message_id: int
    """Unique message identifier inside this chat."""

    date: int
    """Date the message was sent in Unix time.

    It is always a positive number, representing a valid date.
    """

    chat: "Chat"
    """Chat the message belongs to."""

    message_thread_id: Optional[int] = None
    """Optional.

    Unique identifier of a message thread to which the message belongs;
    for supergroups only
    """

    from_: Optional["User"] = Field(None, alias="from")
    """Optional.

    Sender of the message; empty for messages sent to channels. For
    backward compatibility, the field contains a fake sender user in
    non-channel chats, if the message was sent on behalf of a chat.
    """

    sender_chat: Optional["Chat"] = None
    """Optional.

    Sender of the message, sent on behalf of a chat. For example, the
    channel itself for channel posts, the supergroup itself for messages
    from anonymous group administrators, the linked channel for messages
    automatically forwarded to the discussion group. For backward
    compatibility, the field from contains a fake sender user in non-
    channel chats, if the message was sent on behalf of a chat.
    """

    sender_boost_count: Optional[int] = None
    """Optional.

    If the sender of the message boosted the chat, the number of boosts
    added by the user
    """

    sender_business_bot: Optional["User"] = None
    """Optional.

    The bot that actually sent the message on behalf of the business
    account. Available only for outgoing messages sent on behalf of the
    connected business account.
    """

    business_connection_id: Optional[str] = None
    """Optional.

    Unique identifier of the business connection from which the message
    was received. If non-empty, the message belongs to a chat of the
    corresponding business account that is independent from any
    potential bot chat which might share the same identifier.
    """

    forward_origin: Optional["MessageOrigin"] = None
    """Optional.

    Information about the original message for forwarded messages
    """

    is_topic_message: Optional[bool] = None
    """Optional.

    True, if the message is sent to a forum topic
    """

    is_automatic_forward: Optional[bool] = None
    """Optional.

    True, if the message is a channel post that was automatically
    forwarded to the connected discussion group
    """

    reply_to_message: Optional["Message"] = None
    """Optional.

    For replies in the same chat and message thread, the original
    message. Note that the Message object in this field will not contain
    further reply_to_message fields even if it itself is a reply.
    """

    external_reply: Optional["ExternalReplyInfo"] = None
    """Optional.

    Information about the message that is being replied to, which may
    come from another chat or forum topic
    """

    quote: Optional["TextQuote"] = None
    """Optional.

    For replies that quote part of the original message, the quoted part
    of the message
    """

    reply_to_story: Optional["Story"] = None
    """Optional.

    For replies to a story, the original story
    """

    via_bot: Optional["User"] = None
    """Optional.

    Bot through which the message was sent
    """

    edit_date: Optional[int] = None
    """Optional.

    Date the message was last edited in Unix time
    """

    has_protected_content: Optional[bool] = None
    """Optional.

    True, if the message can't be forwarded
    """

    is_from_offline: Optional[bool] = None
    """Optional.

    True, if the message was sent by an implicit action, for example, as
    an away or a greeting business message, or as a scheduled message
    """

    media_group_id: Optional[str] = None
    """Optional.

    The unique identifier of a media message group this message belongs
    to
    """

    author_signature: Optional[str] = None
    """Optional.

    Signature of the post author for messages in channels, or the custom
    title of an anonymous group administrator
    """

    text: Optional[str] = None
    """Optional.

    For text messages, the actual UTF-8 text of the message
    """

    entities: Optional[List["MessageEntity"]] = None
    """Optional.

    For text messages, special entities like usernames, URLs, bot
    commands, etc. that appear in the text
    """

    link_preview_options: Optional["LinkPreviewOptions"] = None
    """Optional.

    Options used for link preview generation for the message, if it is a
    text message and link preview options were changed
    """

    effect_id: Optional[str] = None
    """Optional.

    Unique identifier of the message effect added to the message
    """

    animation: Optional["Animation"] = None
    """Optional.

    Message is an animation, information about the animation. For
    backward compatibility, when this field is set, the document field
    will also be set
    """

    audio: Optional["Audio"] = None
    """Optional.

    Message is an audio file, information about the file
    """

    document: Optional["Document"] = None
    """Optional.

    Message is a general file, information about the file
    """

    paid_media: Optional["PaidMediaInfo"] = None
    """Optional.

    Message contains paid media; information about the paid media
    """

    photo: Optional[List["PhotoSize"]] = None
    """Optional.

    Message is a photo, available sizes of the photo
    """

    sticker: Optional["Sticker"] = None
    """Optional.

    Message is a sticker, information about the sticker
    """

    story: Optional["Story"] = None
    """Optional.

    Message is a forwarded story
    """

    video: Optional["Video"] = None
    """Optional.

    Message is a video, information about the video
    """

    video_note: Optional["VideoNote"] = None
    """Optional.

    Message is a video note, information about the video message
    """

    voice: Optional["Voice"] = None
    """Optional.

    Message is a voice message, information about the file
    """

    caption: Optional[str] = None
    """Optional.

    Caption for the animation, audio, document, paid media, photo, video
    or voice
    """

    caption_entities: Optional[List["MessageEntity"]] = None
    """Optional.

    For messages with a caption, special entities like usernames, URLs,
    bot commands, etc. that appear in the caption
    """

    show_caption_above_media: Optional[bool] = None
    """Optional.

    True, if the caption must be shown above the message media
    """

    has_media_spoiler: Optional[bool] = None
    """Optional.

    True, if the message media is covered by a spoiler animation
    """

    contact: Optional["Contact"] = None
    """Optional.

    Message is a shared contact, information about the contact
    """

    dice: Optional["Dice"] = None
    """Optional.

    Message is a dice with random value
    """

    game: Optional["Game"] = None
    """Optional.

    Message is a game, information about the game. More about games »
    """

    poll: Optional["Poll"] = None
    """Optional.

    Message is a native poll, information about the poll
    """

    venue: Optional["Venue"] = None
    """Optional.

    Message is a venue, information about the venue. For backward
    compatibility, when this field is set, the location field will also
    be set
    """

    location: Optional["Location"] = None
    """Optional.

    Message is a shared location, information about the location
    """

    new_chat_members: Optional[List["User"]] = None
    """Optional.

    New members that were added to the group or supergroup and
    information about them (the bot itself may be one of these members)
    """

    left_chat_member: Optional["User"] = None
    """Optional.

    A member was removed from the group, information about them (this
    member may be the bot itself)
    """

    new_chat_title: Optional[str] = None
    """Optional.

    A chat title was changed to this value
    """

    new_chat_photo: Optional[List["PhotoSize"]] = None
    """Optional.

    A chat photo was change to this value
    """

    delete_chat_photo: Optional[bool] = None
    """Optional.

    Service message: the chat photo was deleted
    """

    group_chat_created: Optional[bool] = None
    """Optional.

    Service message: the group has been created
    """

    supergroup_chat_created: Optional[bool] = None
    """Optional.

    Service message: the supergroup has been created. This field
    can't be received in a message coming through updates, because bot
    can't be a member of a supergroup when it is created. It can only be
    found in reply_to_message if someone replies to a very first message
    in a directly created supergroup.
    """

    channel_chat_created: Optional[bool] = None
    """Optional.

    Service message: the channel has been created. This field
    can't be received in a message coming through updates, because bot
    can't be a member of a channel when it is created. It can only be
    found in reply_to_message if someone replies to a very first message
    in a channel.
    """

    message_auto_delete_timer_changed: Optional["MessageAutoDeleteTimerChanged"] = None
    """Optional.

    Service message: auto-delete timer settings changed in the
    chat
    """

    migrate_to_chat_id: Optional[int] = None
    """Optional.

    The group has been migrated to a supergroup with the specified
    identifier. This number may have more than 32 significant bits and
    some programming languages may have difficulty/silent defects in
    interpreting it. But it has at most 52 significant bits, so a signed
    64-bit integer or double-precision float type are safe for storing
    this identifier.
    """

    migrate_from_chat_id: Optional[int] = None
    """Optional.

    The supergroup has been migrated from a group with the specified
    identifier. This number may have more than 32 significant bits and
    some programming languages may have difficulty/silent defects in
    interpreting it. But it has at most 52 significant bits, so a signed
    64-bit integer or double-precision float type are safe for storing
    this identifier.
    """

    pinned_message: Optional["MaybeInaccessibleMessage"] = None
    """Optional.

    Specified message was pinned. Note that the Message object in this
    field will not contain further reply_to_message fields even if it
    itself is a reply.
    """

    invoice: Optional["Invoice"] = None
    """Optional.

    Message is an invoice for a payment, information about the invoice.
    More about payments »
    """

    successful_payment: Optional["SuccessfulPayment"] = None
    """Optional.

    Message is a service message about a successful payment, information
    about the payment. More about payments »
    """

    users_shared: Optional["UsersShared"] = None
    """Optional.

    Service message: users were shared with the bot
    """

    chat_shared: Optional["ChatShared"] = None
    """Optional.

    Service message: a chat was shared with the bot
    """

    connected_website: Optional[str] = None
    """Optional.

    The domain name of the website on which the user has logged in. More
    about Telegram Login »
    """

    write_access_allowed: Optional["WriteAccessAllowed"] = None
    """Optional.

    Service message: the user allowed the bot to write messages
    after adding it to the attachment or side menu, launching a Web App
    from a link, or accepting an explicit request from a Web App sent by
    the method requestWriteAccess
    """

    passport_data: Optional["PassportData"] = None
    """Optional.

    Telegram Passport data
    """

    proximity_alert_triggered: Optional["ProximityAlertTriggered"] = None
    """Optional.

    Service message. A user in the chat triggered another user's
    proximity alert while sharing Live Location.
    """

    boost_added: Optional["ChatBoostAdded"] = None
    """Optional.

    Service message: user boosted the chat
    """

    chat_background_set: Optional["ChatBackground"] = None
    """Optional.

    Service message: chat background set
    """

    forum_topic_created: Optional["ForumTopicCreated"] = None
    """Optional.

    Service message: forum topic created
    """

    forum_topic_edited: Optional["ForumTopicEdited"] = None
    """Optional.

    Service message: forum topic edited
    """

    forum_topic_closed: Optional["ForumTopicClosed"] = None
    """Optional.

    Service message: forum topic closed
    """

    forum_topic_reopened: Optional["ForumTopicReopened"] = None
    """Optional.

    Service message: forum topic reopened
    """

    general_forum_topic_hidden: Optional["GeneralForumTopicHidden"] = None
    """Optional.

    Service message: the 'General' forum topic hidden
    """

    general_forum_topic_unhidden: Optional["GeneralForumTopicUnhidden"] = None
    """Optional.

    Service message: the 'General' forum topic unhidden
    """

    giveaway_created: Optional["GiveawayCreated"] = None
    """Optional.

    Service message: a scheduled giveaway was created
    """

    giveaway: Optional["Giveaway"] = None
    """Optional.

    The message is a scheduled giveaway message
    """

    giveaway_winners: Optional["GiveawayWinners"] = None
    """Optional.

    A giveaway with public winners was completed
    """

    giveaway_completed: Optional["GiveawayCompleted"] = None
    """Optional.

    Service message: a giveaway without public winners was
    completed
    """

    video_chat_scheduled: Optional["VideoChatScheduled"] = None
    """Optional.

    Service message: video chat scheduled
    """

    video_chat_started: Optional["VideoChatStarted"] = None
    """Optional.

    Service message: video chat started
    """

    video_chat_ended: Optional["VideoChatEnded"] = None
    """Optional.

    Service message: video chat ended
    """

    video_chat_participants_invited: Optional["VideoChatParticipantsInvited"] = None
    """Optional.

    Service message: new participants invited to a video chat
    """

    web_app_data: Optional["WebAppData"] = None
    """Optional.

    Service message: data sent by a Web App
    """

    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """Optional.

    Inline keyboard attached to the message. login_url buttons are
    represented as ordinary url buttons.
    """


class MessageId(BaseModel):
    """This object represents a unique message identifier."""

    message_id: int
    """Unique message identifier."""


class InaccessibleMessage(BaseModel):
    """This object describes a message that was deleted or is otherwise
    inaccessible to the bot."""

    chat: "Chat"
    """Chat the message belonged to."""

    message_id: int
    """Unique message identifier inside the chat."""

    date: int
    """Always 0.

    The field can be used to differentiate regular and inaccessible
    messages.
    """


class MessageEntity(BaseModel):
    """This object represents one special entity in a text message.

    For example, hashtags, usernames, URLs, etc.
    """

    type: str
    """Type of the entity.

    Currently, can be “mention” (@username), “hashtag” (#hashtag),
    “cashtag” ($USD), “bot_command” (/start@jobs_bot), “url” (
    https://telegram.org),
    “email” (do-not-reply@telegram.org),
    “phone_number” (+1-212-555-0123), “bold” (bold text), “italic” (italic
    text), “underline” (underlined text), “strikethrough” (strikethrough
    text), “spoiler” (spoiler message), “blockquote” (block quotation),
    “expandable_blockquote” (collapsed-by-default block quotation), “code”
    (monowidth string), “pre” (monowidth block), “text_link” (for
    clickable text URLs), “text_mention” (for users without usernames),
    “custom_emoji” (for inline custom emoji stickers)
    """

    offset: int
    """Offset in UTF-16 code units to the start of the entity."""

    length: int
    """Length of the entity in UTF-16 code units."""

    url: Optional[str] = None
    """Optional.

    For “text_link” only, URL that will be opened after user taps on the
    text
    """

    user: Optional["User"] = None
    """Optional.

    For “text_mention” only, the mentioned user
    """

    language: Optional[str] = None
    """Optional.

    For “pre” only, the programming language of the entity text
    """

    custom_emoji_id: Optional[str] = None
    """Optional.

    For “custom_emoji” only, unique identifier of the custom emoji. Use
    getCustomEmojiStickers to get full information about the sticker
    """


class TextQuote(BaseModel):
    """This object contains information about the quoted part of a message that
    is replied to by the given message."""

    text: str
    """Text of the quoted part of a message that is replied to by the given
    message."""

    position: int
    """Approximate quote position in the original message in UTF-16 code units
    as specified by the sender."""

    entities: Optional[List["MessageEntity"]] = None
    """Optional.

    Special entities that appear in the quote. Currently, only bold,
    italic, underline, strikethrough, spoiler, and custom_emoji entities
    are kept in quotes.
    """

    is_manual: Optional[bool] = None
    """Optional.

    True, if the quote was chosen manually by the message sender.
    Otherwise, the quote was added automatically by the server.
    """


class ExternalReplyInfo(BaseModel):
    """This object contains information about a message that is being replied
    to, which may come from another chat or forum topic."""

    origin: "MessageOrigin"
    """Origin of the message replied to by the given message."""

    chat: Optional["Chat"] = None
    """Optional.

    Chat the original message belongs to. Available only if the chat is
    a supergroup or a channel.
    """

    message_id: Optional[int] = None
    """Optional.

    Unique message identifier inside the original chat. Available only
    if the original chat is a supergroup or a channel.
    """

    link_preview_options: Optional["LinkPreviewOptions"] = None
    """Optional.

    Options used for link preview generation for the original message,
    if it is a text message
    """

    animation: Optional["Animation"] = None
    """Optional.

    Message is an animation, information about the animation
    """

    audio: Optional["Audio"] = None
    """Optional.

    Message is an audio file, information about the file
    """

    document: Optional["Document"] = None
    """Optional.

    Message is a general file, information about the file
    """

    paid_media: Optional["PaidMediaInfo"] = None
    """Optional.

    Message contains paid media; information about the paid media
    """

    photo: Optional[List["PhotoSize"]] = None
    """Optional.

    Message is a photo, available sizes of the photo
    """

    sticker: Optional["Sticker"] = None
    """Optional.

    Message is a sticker, information about the sticker
    """

    story: Optional["Story"] = None
    """Optional.

    Message is a forwarded story
    """

    video: Optional["Video"] = None
    """Optional.

    Message is a video, information about the video
    """

    video_note: Optional["VideoNote"] = None
    """Optional.

    Message is a video note, information about the video message
    """

    voice: Optional["Voice"] = None
    """Optional.

    Message is a voice message, information about the file
    """

    has_media_spoiler: Optional[bool] = None
    """Optional.

    True, if the message media is covered by a spoiler animation
    """

    contact: Optional["Contact"] = None
    """Optional.

    Message is a shared contact, information about the contact
    """

    dice: Optional["Dice"] = None
    """Optional.

    Message is a dice with random value
    """

    game: Optional["Game"] = None
    """Optional.

    Message is a game, information about the game. More about games »
    """

    giveaway: Optional["Giveaway"] = None
    """Optional.

    Message is a scheduled giveaway, information about the giveaway
    """

    giveaway_winners: Optional["GiveawayWinners"] = None
    """Optional.

    A giveaway with public winners was completed
    """

    invoice: Optional["Invoice"] = None
    """Optional.

    Message is an invoice for a payment, information about the invoice.
    More about payments »
    """

    location: Optional["Location"] = None
    """Optional.

    Message is a shared location, information about the location
    """

    poll: Optional["Poll"] = None
    """Optional.

    Message is a native poll, information about the poll
    """

    venue: Optional["Venue"] = None
    """Optional.

    Message is a venue, information about the venue
    """


class ReplyParameters(BaseModel):
    """Describes reply parameters for the message that is being sent."""

    message_id: int
    """Identifier of the message that will be replied to in the current chat,
    or in the chat chat_id if it is specified."""

    chat_id: Optional[Union[int, str]] = None
    """Optional.

    If the message to be replied to is from a different chat, unique
    identifier for the chat or username of the channel (in the format
    @channelusername). Not supported for messages sent on behalf of a
    business account.
    """

    allow_sending_without_reply: Optional[bool] = None
    """Optional.

    Pass True if the message should be sent even if the specified
    message to be replied to is not found. Always False for replies in
    another chat or forum topic. Always True for messages sent on behalf
    of a business account.
    """

    quote: Optional[str] = None
    """Optional.

    Quoted part of the message to be replied to; 0-1024 characters after
    entities parsing. The quote must be an exact substring of the
    message to be replied to, including bold, italic, underline,
    strikethrough, spoiler, and custom_emoji entities. The message will
    fail to send if the quote isn't found in the original message.
    """

    quote_parse_mode: Optional[str] = None
    """Optional.

    Mode for parsing entities in the quote. See formatting options for
    more details.
    """

    quote_entities: Optional[List["MessageEntity"]] = None
    """Optional.

    A JSON-serialized list of special entities that appear in the quote.
    It can be specified instead of quote_parse_mode.
    """

    quote_position: Optional[int] = None
    """Optional.

    Position of the quote in the original message in UTF-16 code units
    """


class MessageOriginUser(BaseModel):
    """The message was originally sent by a known user."""

    type: str
    """Type of the message origin, always “user”"""

    date: int
    """Date the message was sent originally in Unix time."""

    sender_user: "User"
    """User that sent the message originally."""


class MessageOriginHiddenUser(BaseModel):
    """The message was originally sent by an unknown user."""

    type: str
    """Type of the message origin, always “hidden_user”"""

    date: int
    """Date the message was sent originally in Unix time."""

    sender_user_name: str
    """Name of the user that sent the message originally."""


class MessageOriginChat(BaseModel):
    """The message was originally sent on behalf of a chat to a group chat."""

    type: str
    """Type of the message origin, always “chat”"""

    date: int
    """Date the message was sent originally in Unix time."""

    sender_chat: "Chat"
    """Chat that sent the message originally."""

    author_signature: Optional[str] = None
    """Optional.

    For messages originally sent by an anonymous chat administrator,
    original message author signature
    """


class MessageOriginChannel(BaseModel):
    """The message was originally sent to a channel chat."""

    type: str
    """Type of the message origin, always “channel”"""

    date: int
    """Date the message was sent originally in Unix time."""

    chat: "Chat"
    """Channel chat to which the message was originally sent."""

    message_id: int
    """Unique message identifier inside the chat."""

    author_signature: Optional[str] = None
    """Optional.

    Signature of the original post author
    """


class PhotoSize(BaseModel):
    """This object represents one size of a photo or a file / sticker
    thumbnail."""

    file_id: str
    """Identifier for this file, which can be used to download or reuse the
    file."""

    file_unique_id: str
    """Unique identifier for this file, which is supposed to be the same over
    time and for different bots.

    Can't be used to download or reuse the file.
    """

    width: int
    """Photo width."""

    height: int
    """Photo height."""

    file_size: Optional[int] = None
    """Optional.

    File size in bytes
    """


class Animation(BaseModel):
    """This object represents an animation file (GIF or H.264/MPEG-4 AVC video
    without sound)."""

    file_id: str
    """Identifier for this file, which can be used to download or reuse the
    file."""

    file_unique_id: str
    """Unique identifier for this file, which is supposed to be the same over
    time and for different bots.

    Can't be used to download or reuse the file.
    """

    width: int
    """Video width as defined by the sender."""

    height: int
    """Video height as defined by the sender."""

    duration: int
    """Duration of the video in seconds as defined by the sender."""

    thumbnail: Optional["PhotoSize"] = None
    """Optional.

    Animation thumbnail as defined by the sender
    """

    file_name: Optional[str] = None
    """Optional.

    Original animation filename as defined by the sender
    """

    mime_type: Optional[str] = None
    """Optional.

    MIME type of the file as defined by the sender
    """

    file_size: Optional[int] = None
    """Optional.

    File size in bytes. It can be bigger than 2^31 and some programming
    languages may have difficulty/silent defects in interpreting it. But
    it has at most 52 significant bits, so a signed 64-bit integer or
    double-precision float type are safe for storing this value.
    """


class Audio(BaseModel):
    """This object represents an audio file to be treated as music by the
    Telegram clients."""

    file_id: str
    """Identifier for this file, which can be used to download or reuse the
    file."""

    file_unique_id: str
    """Unique identifier for this file, which is supposed to be the same over
    time and for different bots.

    Can't be used to download or reuse the file.
    """

    duration: int
    """Duration of the audio in seconds as defined by the sender."""

    performer: Optional[str] = None
    """Optional.

    Performer of the audio as defined by the sender or by audio tags
    """

    title: Optional[str] = None
    """Optional.

    Title of the audio as defined by the sender or by audio tags
    """

    file_name: Optional[str] = None
    """Optional.

    Original filename as defined by the sender
    """

    mime_type: Optional[str] = None
    """Optional.

    MIME type of the file as defined by the sender
    """

    file_size: Optional[int] = None
    """Optional.

    File size in bytes. It can be bigger than 2^31 and some programming
    languages may have difficulty/silent defects in interpreting it. But
    it has at most 52 significant bits, so a signed 64-bit integer or
    double-precision float type are safe for storing this value.
    """

    thumbnail: Optional["PhotoSize"] = None
    """Optional.

    Thumbnail of the album cover to which the music file belongs
    """


class Document(BaseModel):
    """This object represents a general file (as opposed to photos, voice
    messages and audio files)."""

    file_id: str
    """Identifier for this file, which can be used to download or reuse the
    file."""

    file_unique_id: str
    """Unique identifier for this file, which is supposed to be the same over
    time and for different bots.

    Can't be used to download or reuse the file.
    """

    thumbnail: Optional["PhotoSize"] = None
    """Optional.

    Document thumbnail as defined by the sender
    """

    file_name: Optional[str] = None
    """Optional.

    Original filename as defined by the sender
    """

    mime_type: Optional[str] = None
    """Optional.

    MIME type of the file as defined by the sender
    """

    file_size: Optional[int] = None
    """Optional.

    File size in bytes. It can be bigger than 2^31 and some programming
    languages may have difficulty/silent defects in interpreting it. But
    it has at most 52 significant bits, so a signed 64-bit integer or
    double-precision float type are safe for storing this value.
    """


class Story(BaseModel):
    """This object represents a story."""

    chat: "Chat"
    """Chat that posted the story."""

    id: int
    """Unique identifier for the story in the chat."""


class Video(BaseModel):
    """This object represents a video file."""

    file_id: str
    """Identifier for this file, which can be used to download or reuse the
    file."""

    file_unique_id: str
    """Unique identifier for this file, which is supposed to be the same over
    time and for different bots.

    Can't be used to download or reuse the file.
    """

    width: int
    """Video width as defined by the sender."""

    height: int
    """Video height as defined by the sender."""

    duration: int
    """Duration of the video in seconds as defined by the sender."""

    thumbnail: Optional["PhotoSize"] = None
    """Optional.

    Video thumbnail
    """

    file_name: Optional[str] = None
    """Optional.

    Original filename as defined by the sender
    """

    mime_type: Optional[str] = None
    """Optional.

    MIME type of the file as defined by the sender
    """

    file_size: Optional[int] = None
    """Optional.

    File size in bytes. It can be bigger than 2^31 and some programming
    languages may have difficulty/silent defects in interpreting it. But
    it has at most 52 significant bits, so a signed 64-bit integer or
    double-precision float type are safe for storing this value.
    """


class VideoNote(BaseModel):
    """This object represents a video message (available in Telegram apps as of
    v.4.0)."""

    file_id: str
    """Identifier for this file, which can be used to download or reuse the
    file."""

    file_unique_id: str
    """Unique identifier for this file, which is supposed to be the same over
    time and for different bots.

    Can't be used to download or reuse the file.
    """

    length: int
    """Video width and height (diameter of the video message) as defined by the
    sender."""

    duration: int
    """Duration of the video in seconds as defined by the sender."""

    thumbnail: Optional["PhotoSize"] = None
    """Optional.

    Video thumbnail
    """

    file_size: Optional[int] = None
    """Optional.

    File size in bytes
    """


class Voice(BaseModel):
    """This object represents a voice note."""

    file_id: str
    """Identifier for this file, which can be used to download or reuse the
    file."""

    file_unique_id: str
    """Unique identifier for this file, which is supposed to be the same over
    time and for different bots.

    Can't be used to download or reuse the file.
    """

    duration: int
    """Duration of the audio in seconds as defined by the sender."""

    mime_type: Optional[str] = None
    """Optional.

    MIME type of the file as defined by the sender
    """

    file_size: Optional[int] = None
    """Optional.

    File size in bytes. It can be bigger than 2^31 and some programming
    languages may have difficulty/silent defects in interpreting it. But
    it has at most 52 significant bits, so a signed 64-bit integer or
    double-precision float type are safe for storing this value.
    """


class PaidMediaInfo(BaseModel):
    """Describes the paid media added to a message."""

    star_count: int
    """The number of Telegram Stars that must be paid to buy access to the
    media."""

    paid_media: List["PaidMedia"]
    """Information about the paid media."""


class PaidMediaPreview(BaseModel):
    """The paid media isn't available before the payment."""

    type: str
    """Type of the paid media, always “preview”"""

    width: Optional[int] = None
    """Optional.

    Media width as defined by the sender
    """

    height: Optional[int] = None
    """Optional.

    Media height as defined by the sender
    """

    duration: Optional[int] = None
    """Optional.

    Duration of the media in seconds as defined by the sender
    """


class PaidMediaPhoto(BaseModel):
    """The paid media is a photo."""

    type: str
    """Type of the paid media, always “photo”"""

    photo: List["PhotoSize"]
    """The photo."""


class PaidMediaVideo(BaseModel):
    """The paid media is a video."""

    type: str
    """Type of the paid media, always “video”"""

    video: "Video"
    """The video."""


class Contact(BaseModel):
    """This object represents a phone contact."""

    phone_number: str
    """Contact's phone number."""

    first_name: str
    """Contact's first name."""

    last_name: Optional[str] = None
    """Optional.

    Contact's last name
    """

    user_id: Optional[int] = None
    """Optional.

    Contact's user identifier in Telegram. This number may have more
    than 32 significant bits and some programming languages may have
    difficulty/silent defects in interpreting it. But it has at most 52
    significant bits, so a 64-bit integer or double-precision float type
    are safe for storing this identifier.
    """

    vcard: Optional[str] = None
    """Optional.

    Additional data about the contact in the form of a vCard
    """


class Dice(BaseModel):
    """This object represents an animated emoji that displays a random
    value."""

    emoji: str
    """Emoji on which the dice throw animation is based."""

    value: int
    """Value of the dice, 1-6 for “”, “” and “” base emoji, 1-5 for “” and “”
    base emoji, 1-64 for “” base emoji."""


class PollOption(BaseModel):
    """This object contains information about one answer option in a poll."""

    text: str
    """Option text, 1-100 characters."""

    voter_count: int
    """Number of users that voted for this option."""

    text_entities: Optional[List["MessageEntity"]] = None
    """Optional.

    Special entities that appear in the option text. Currently, only
    custom emoji entities are allowed in poll option texts
    """


class InputPollOption(BaseModel):
    """This object contains information about one answer option in a poll to be
    sent."""

    text: str
    """Option text, 1-100 characters."""

    text_parse_mode: Optional[str] = None
    """Optional.

    Mode for parsing entities in the text. See formatting options for
    more details. Currently, only custom emoji entities are allowed
    """

    text_entities: Optional[List["MessageEntity"]] = None
    """Optional.

    A JSON-serialized list of special entities that appear in the poll
    option text. It can be specified instead of text_parse_mode
    """


class PollAnswer(BaseModel):
    """This object represents an answer of a user in a non-anonymous poll."""

    poll_id: str
    """Unique poll identifier."""

    option_ids: List[int]
    """0-based identifiers of chosen answer options.

    May be empty if the vote was retracted.
    """

    voter_chat: Optional["Chat"] = None
    """Optional.

    The chat that changed the answer to the poll, if the voter is
    anonymous
    """

    user: Optional["User"] = None
    """Optional.

    The user that changed the answer to the poll, if the voter isn't
    anonymous
    """


class Poll(BaseModel):
    """This object contains information about a poll."""

    id: str
    """Unique poll identifier."""

    question: str
    """Poll question, 1-300 characters."""

    options: List["PollOption"]
    """List of poll options."""

    total_voter_count: int
    """Total number of users that voted in the poll."""

    is_closed: bool
    """True, if the poll is closed."""

    is_anonymous: bool
    """True, if the poll is anonymous."""

    type: str
    """Poll type, currently can be “regular” or “quiz”"""

    allows_multiple_answers: bool
    """True, if the poll allows multiple answers."""

    question_entities: Optional[List["MessageEntity"]] = None
    """Optional.

    Special entities that appear in the question. Currently, only custom
    emoji entities are allowed in poll questions
    """

    correct_option_id: Optional[int] = None
    """Optional.

    0-based identifier of the correct answer option. Available only for
    polls in the quiz mode, which are closed, or was sent (not
    forwarded) by the bot or to the private chat with the bot.
    """

    explanation: Optional[str] = None
    """Optional.

    Text that is shown when a user chooses an incorrect answer or taps
    on the lamp icon in a quiz-style poll, 0-200 characters
    """

    explanation_entities: Optional[List["MessageEntity"]] = None
    """Optional.

    Special entities like usernames, URLs, bot commands, etc. that
    appear in the explanation
    """

    open_period: Optional[int] = None
    """Optional.

    Amount of time in seconds the poll will be active after creation
    """

    close_date: Optional[int] = None
    """Optional.

    Point in time (Unix timestamp) when the poll will be automatically
    closed
    """


class Location(BaseModel):
    """This object represents a point on the map."""

    latitude: float
    """Latitude as defined by the sender."""

    longitude: float
    """Longitude as defined by the sender."""

    horizontal_accuracy: Optional[float] = None
    """Optional.

    The radius of uncertainty for the location, measured in meters;
    0-1500
    """

    live_period: Optional[int] = None
    """Optional.

    Time relative to the message sending date, during which the location
    can be updated; in seconds. For active live locations only.
    """

    heading: Optional[int] = None
    """Optional.

    The direction in which user is moving, in degrees; 1-360. For active
    live locations only.
    """

    proximity_alert_radius: Optional[int] = None
    """Optional.

    The maximum distance for proximity alerts about approaching another
    chat member, in meters. For sent live locations only.
    """


class Venue(BaseModel):
    """This object represents a venue."""

    location: "Location"
    """Venue location.

    Can't be a live location
    """

    title: str
    """Name of the venue."""

    address: str
    """Address of the venue."""

    foursquare_id: Optional[str] = None
    """Optional.

    Foursquare identifier of the venue
    """

    foursquare_type: Optional[str] = None
    """Optional.

    Foursquare type of the venue. (For example,
    “arts_entertainment/default”, “arts_entertainment/aquarium” or
    “food/icecream”.)
    """

    google_place_id: Optional[str] = None
    """Optional.

    Google Places identifier of the venue
    """

    google_place_type: Optional[str] = None
    """Optional.

    Google Places type of the venue. (See supported types.)
    """


class WebAppData(BaseModel):
    """Describes data sent from a Web App to the bot."""

    data: str
    """The data.

    Be aware that a bad client can send arbitrary data in this field.
    """

    button_text: str
    """Text of the web_app keyboard button from which the Web App was opened.

    Be aware that a bad client can send arbitrary data in this field.
    """


class ProximityAlertTriggered(BaseModel):
    """This object represents the content of a service message, sent whenever a
    user in the chat triggers a proximity alert set by another user."""

    traveler: "User"
    """User that triggered the alert."""

    watcher: "User"
    """User that set the alert."""

    distance: int
    """The distance between the users."""


class MessageAutoDeleteTimerChanged(BaseModel):
    """This object represents a service message about a change in auto-delete
    timer settings."""

    message_auto_delete_time: int
    """New auto-delete time for messages in the chat; in seconds."""


class ChatBoostAdded(BaseModel):
    """This object represents a service message about a user boosting a
    chat."""

    boost_count: int
    """Number of boosts added by the user."""


class BackgroundFillSolid(BaseModel):
    """The background is filled using the selected color."""

    type: str
    """Type of the background fill, always “solid”"""

    color: int
    """The color of the background fill in the RGB24 format."""


class BackgroundFillGradient(BaseModel):
    """The background is a gradient fill."""

    type: str
    """Type of the background fill, always “gradient”"""

    top_color: int
    """Top color of the gradient in the RGB24 format."""

    bottom_color: int
    """Bottom color of the gradient in the RGB24 format."""

    rotation_angle: int
    """Clockwise rotation angle of the background fill in degrees; 0-359."""


class BackgroundFillFreeformGradient(BaseModel):
    """The background is a freeform gradient that rotates after every message
    in the chat."""

    type: str
    """Type of the background fill, always “freeform_gradient”"""

    colors: List[int]
    """A list of the 3 or 4 base colors that are used to generate the freeform
    gradient in the RGB24 format."""


class BackgroundTypeFill(BaseModel):
    """The background is automatically filled based on the selected colors."""

    type: str
    """Type of the background, always “fill”"""

    fill: "BackgroundFill"
    """The background fill."""

    dark_theme_dimming: int
    """Dimming of the background in dark themes, as a percentage; 0-100."""


class BackgroundTypeWallpaper(BaseModel):
    """The background is a wallpaper in the JPEG format."""

    type: str
    """Type of the background, always “wallpaper”"""

    document: "Document"
    """Document with the wallpaper."""

    dark_theme_dimming: int
    """Dimming of the background in dark themes, as a percentage; 0-100."""

    is_blurred: Optional[bool] = None
    """Optional.

    True, if the wallpaper is downscaled to fit in a 450x450 square and
    then box-blurred with radius 12
    """

    is_moving: Optional[bool] = None
    """Optional.

    True, if the background moves slightly when the device is tilted
    """


class BackgroundTypePattern(BaseModel):
    """The background is a PNG or TGV (gzipped subset of SVG with MIME type.

    “application/x-tgwallpattern”) pattern to be combined with the
    background fill chosen by the user.
    """

    type: str
    """Type of the background, always “pattern”"""

    document: "Document"
    """Document with the pattern."""

    fill: "BackgroundFill"
    """The background fill that is combined with the pattern."""

    intensity: int
    """Intensity of the pattern when it is shown above the filled background;
    0-100."""

    is_inverted: Optional[bool] = None
    """Optional.

    True, if the background fill must be applied only to the pattern
    itself. All other pixels are black in this case. For dark themes
    only
    """

    is_moving: Optional[bool] = None
    """Optional.

    True, if the background moves slightly when the device is tilted
    """


class BackgroundTypeChatTheme(BaseModel):
    """The background is taken directly from a built-in chat theme."""

    type: str
    """Type of the background, always “chat_theme”"""

    theme_name: str
    """Name of the chat theme, which is usually an emoji."""


class ChatBackground(BaseModel):
    """This object represents a chat background."""

    type: "BackgroundType"
    """Type of the background."""


class ForumTopicCreated(BaseModel):
    """This object represents a service message about a new forum topic created
    in the chat."""

    name: str
    """Name of the topic."""

    icon_color: int
    """Color of the topic icon in RGB format."""

    icon_custom_emoji_id: Optional[str] = None
    """Optional.

    Unique identifier of the custom emoji shown as the topic icon
    """


class ForumTopicClosed(BaseModel):
    """This object represents a service message about a forum topic closed in
    the chat.

    Currently holds no information.
    """


class ForumTopicEdited(BaseModel):
    """This object represents a service message about an edited forum topic."""

    name: Optional[str] = None
    """Optional.

    New name of the topic, if it was edited
    """

    icon_custom_emoji_id: Optional[str] = None
    """Optional.

    New identifier of the custom emoji shown as the topic icon, if it
    was edited; an empty string if the icon was removed
    """


class ForumTopicReopened(BaseModel):
    """This object represents a service message about a forum topic reopened in
    the chat.

    Currently holds no information.
    """


class GeneralForumTopicHidden(BaseModel):
    """This object represents a service message about General forum topic
    hidden in the chat.

    Currently holds no information.
    """


class GeneralForumTopicUnhidden(BaseModel):
    """This object represents a service message about General forum topic
    unhidden in the chat.

    Currently holds no information.
    """


class SharedUser(BaseModel):
    """This object contains information about a user that was shared with the
    bot using a KeyboardButtonRequestUsers button."""

    user_id: int
    """Identifier of the shared user.

    This number may have more than 32 significant bits and some
    programming languages may have difficulty/silent defects in
    interpreting it. But it has at most 52 significant bits, so 64-bit
    integers or double-precision float types are safe for storing these
    identifiers. The bot may not have access to the user and could be
    unable to use this identifier, unless the user is already known to
    the bot by some other means.
    """

    first_name: Optional[str] = None
    """Optional.

    First name of the user, if the name was requested by the bot
    """

    last_name: Optional[str] = None
    """Optional.

    Last name of the user, if the name was requested by the bot
    """

    username: Optional[str] = None
    """Optional.

    Username of the user, if the username was requested by the bot
    """

    photo: Optional[List["PhotoSize"]] = None
    """Optional.

    Available sizes of the chat photo, if the photo was requested by the
    bot
    """


class UsersShared(BaseModel):
    """This object contains information about the users whose identifiers were
    shared with the bot using a KeyboardButtonRequestUsers button."""

    request_id: int
    """Identifier of the request."""

    users: List["SharedUser"]
    """Information about users shared with the bot."""


class ChatShared(BaseModel):
    """This object contains information about a chat that was shared with the
    bot using a KeyboardButtonRequestChat button."""

    request_id: int
    """Identifier of the request."""

    chat_id: int
    """Identifier of the shared chat.

    This number may have more than 32 significant bits and some
    programming languages may have difficulty/silent defects in
    interpreting it. But it has at most 52 significant bits, so a 64-bit
    integer or double-precision float type are safe for storing this
    identifier. The bot may not have access to the chat and could be
    unable to use this identifier, unless the chat is already known to
    the bot by some other means.
    """

    title: Optional[str] = None
    """Optional.

    Title of the chat, if the title was requested by the bot.
    """

    username: Optional[str] = None
    """Optional.

    Username of the chat, if the username was requested by the bot and
    available.
    """

    photo: Optional[List["PhotoSize"]] = None
    """Optional.

    Available sizes of the chat photo, if the photo was requested by the
    bot
    """


class WriteAccessAllowed(BaseModel):
    """This object represents a service message about a user allowing a bot to
    write messages after adding it to the attachment menu, launching a Web App
    from a link, or accepting an explicit request from a Web App sent by the
    method requestWriteAccess."""

    from_request: Optional[bool] = None
    """Optional.

    True, if the access was granted after the user accepted an explicit
    request from a Web App sent by the method requestWriteAccess
    """

    web_app_name: Optional[str] = None
    """Optional.

    Name of the Web App, if the access was granted when the Web App was
    launched from a link
    """

    from_attachment_menu: Optional[bool] = None
    """Optional.

    True, if the access was granted when the bot was added to the
    attachment or side menu
    """


class VideoChatScheduled(BaseModel):
    """This object represents a service message about a video chat scheduled in
    the chat."""

    start_date: int
    """Point in time (Unix timestamp) when the video chat is supposed to be
    started by a chat administrator."""


class VideoChatStarted(BaseModel):
    """This object represents a service message about a video chat started in
    the chat.

    Currently holds no information.
    """


class VideoChatEnded(BaseModel):
    """This object represents a service message about a video chat ended in the
    chat."""

    duration: int
    """Video chat duration in seconds."""


class VideoChatParticipantsInvited(BaseModel):
    """This object represents a service message about new members invited to a
    video chat."""

    users: List["User"]
    """New members that were invited to the video chat."""


class GiveawayCreated(BaseModel):
    """This object represents a service message about the creation of a
    scheduled giveaway.

    Currently holds no information.
    """


class Giveaway(BaseModel):
    """This object represents a message about a scheduled giveaway."""

    chats: List["Chat"]
    """The list of chats which the user must join to participate in the
    giveaway."""

    winners_selection_date: int
    """Point in time (Unix timestamp) when winners of the giveaway will be
    selected."""

    winner_count: int
    """The number of users which are supposed to be selected as winners of the
    giveaway."""

    only_new_members: Optional[bool] = None
    """Optional.

    True, if only users who join the chats after the giveaway started
    should be eligible to win
    """

    has_public_winners: Optional[bool] = None
    """Optional.

    True, if the list of giveaway winners will be visible to everyone
    """

    prize_description: Optional[str] = None
    """Optional.

    Description of additional giveaway prize
    """

    country_codes: Optional[List[str]] = None
    """Optional.

    A list of two-letter ISO 3166-1 alpha-2 country codes indicating the
    countries from which eligible users for the giveaway must come. If
    empty, then all users can participate in the giveaway. Users with a
    phone number that was bought on Fragment can always participate in
    giveaways.
    """

    premium_subscription_month_count: Optional[int] = None
    """Optional.

    The number of months the Telegram Premium subscription won from the
    giveaway will be active for
    """


class GiveawayWinners(BaseModel):
    """This object represents a message about the completion of a giveaway with
    public winners."""

    chat: "Chat"
    """The chat that created the giveaway."""

    giveaway_message_id: int
    """Identifier of the message with the giveaway in the chat."""

    winners_selection_date: int
    """Point in time (Unix timestamp) when winners of the giveaway were
    selected."""

    winner_count: int
    """Total number of winners in the giveaway."""

    winners: List["User"]
    """List of up to 100 winners of the giveaway."""

    additional_chat_count: Optional[int] = None
    """Optional.

    The number of other chats the user had to join in order to be
    eligible for the giveaway
    """

    premium_subscription_month_count: Optional[int] = None
    """Optional.

    The number of months the Telegram Premium subscription won from the
    giveaway will be active for
    """

    unclaimed_prize_count: Optional[int] = None
    """Optional.

    Number of undistributed prizes
    """

    only_new_members: Optional[bool] = None
    """Optional.

    True, if only users who had joined the chats after the giveaway
    started were eligible to win
    """

    was_refunded: Optional[bool] = None
    """Optional.

    True, if the giveaway was canceled because the payment for it was
    refunded
    """

    prize_description: Optional[str] = None
    """Optional.

    Description of additional giveaway prize
    """


class GiveawayCompleted(BaseModel):
    """This object represents a service message about the completion of a
    giveaway without public winners."""

    winner_count: int
    """Number of winners in the giveaway."""

    unclaimed_prize_count: Optional[int] = None
    """Optional.

    Number of undistributed prizes
    """

    giveaway_message: Optional["Message"] = None
    """Optional.

    Message with the giveaway that was completed, if it wasn't deleted
    """


class LinkPreviewOptions(BaseModel):
    """Describes the options used for link preview generation."""

    is_disabled: Optional[bool] = None
    """Optional.

    True, if the link preview is disabled
    """

    url: Optional[str] = None
    """Optional.

    URL to use for the link preview. If empty, then the first URL found
    in the message text will be used
    """

    prefer_small_media: Optional[bool] = None
    """Optional.

    True, if the media in the link preview is supposed to be shrunk;
    ignored if the URL isn't explicitly specified or media size change
    isn't supported for the preview
    """

    prefer_large_media: Optional[bool] = None
    """Optional.

    True, if the media in the link preview is supposed to be enlarged;
    ignored if the URL isn't explicitly specified or media size change
    isn't supported for the preview
    """

    show_above_text: Optional[bool] = None
    """Optional.

    True, if the link preview must be shown above the message text;
    otherwise, the link preview will be shown below the message text
    """


class UserProfilePhotos(BaseModel):
    """This object represent a user's profile pictures."""

    total_count: int
    """Total number of profile pictures the target user has."""

    photos: List[List["PhotoSize"]]
    """Requested profile pictures (in up to 4 sizes each)"""


class File(BaseModel):
    """This object represents a file ready to be downloaded.

    The file can be downloaded via the link
    https://api.telegram.org/file/bot<token>/<file_path>.
    It is guaranteed
    that the link will be valid for at least 1 hour. When the link
    expires, a new one can be requested by calling getFile.
    """

    file_id: str
    """Identifier for this file, which can be used to download or reuse the
    file."""

    file_unique_id: str
    """Unique identifier for this file, which is supposed to be the same over
    time and for different bots.

    Can't be used to download or reuse the file.
    """

    file_size: Optional[int] = None
    """Optional.

    File size in bytes. It can be bigger than 2^31 and some programming
    languages may have difficulty/silent defects in interpreting it. But
    it has at most 52 significant bits, so a signed 64-bit integer or
    double-precision float type are safe for storing this value.
    """

    file_path: Optional[str] = None
    """Optional.

    File path. Use
    https://api.telegram.org/file/bot<token>/<file_path>
    to get the file.
    """


class WebAppInfo(BaseModel):
    """Describes a Web App."""

    url: str
    """An HTTPS URL of a Web App to be opened with additional data as specified
    in Initializing Web Apps."""


class ReplyKeyboardMarkup(BaseModel):
    """This object represents a custom keyboard with reply options (see
    Introduction to bots for details and examples).

    Not supported in channels and for messages sent on behalf of a
    Telegram Business account.
    """

    keyboard: List[List["KeyboardButton"]]
    """Array of button rows, each represented by an Array of KeyboardButton
    objects."""

    is_persistent: Optional[bool] = None
    """Optional.

    Requests clients to always show the keyboard when the regular
    keyboard is hidden. Defaults to false, in which case the custom
    keyboard can be hidden and opened with a keyboard icon.
    """

    resize_keyboard: Optional[bool] = None
    """Optional.

    Requests clients to resize the keyboard vertically for optimal fit
    (e.g., make the keyboard smaller if there are just two rows of
    buttons). Defaults to false, in which case the custom keyboard is
    always of the same height as the app's standard keyboard.
    """

    one_time_keyboard: Optional[bool] = None
    """Optional. Requests clients to hide the keyboard as soon as it's been.

    used. The keyboard will still be available, but clients will
    automatically display the usual letter-keyboard in the chat - the user
    can press a special button in the input field to see the custom
    keyboard again. Defaults to false.
    """

    input_field_placeholder: Optional[str] = None
    """Optional.

    The placeholder to be shown in the input field when the keyboard is
    active; 1-64 characters
    """

    selective: Optional[bool] = None
    """Optional.

    Use this parameter if you want to show the keyboard to specific
    users only. Targets: 1) users that are @mentioned in the text of the
    Message object; 2) if the bot's message is a reply to a message in
    the same chat and forum topic, sender of the original
    message.Example: A user requests to change the bot's language, bot
    replies to the request with a keyboard to select the new language.
    Other users in the group don't see the keyboard.
    """


class KeyboardButton(BaseModel):
    """This object represents one button of the reply keyboard.

    At most one of the optional fields must be used to specify type of
    the button. For simple text buttons, String can be used instead of
    this object to specify the button text.
    """

    text: str
    """Text of the button.

    If none of the optional fields are used, it will be sent as a
    message when the button is pressed
    """

    request_users: Optional["KeyboardButtonRequestUsers"] = None
    """Optional.

    If specified, pressing the button will open a list of suitable
    users. Identifiers of selected users will be sent to the bot in a
    “users_shared” service message. Available in private chats only.
    """

    request_chat: Optional["KeyboardButtonRequestChat"] = None
    """Optional.

    If specified, pressing the button will open a list of suitable
    chats. Tapping on a chat will send its identifier to the bot in a
    “chat_shared” service message. Available in private chats only.
    """

    request_contact: Optional[bool] = None
    """Optional.

    If True, the user's phone number will be sent as a contact when the
    button is pressed. Available in private chats only.
    """

    request_location: Optional[bool] = None
    """Optional.

    If True, the user's current location will be sent when the button is
    pressed. Available in private chats only.
    """

    request_poll: Optional["KeyboardButtonPollType"] = None
    """Optional.

    If specified, the user will be asked to create a poll and send it to
    the bot when the button is pressed. Available in private chats only.
    """

    web_app: Optional["WebAppInfo"] = None
    """Optional.

    If specified, the described Web App will be launched when the button
    is pressed. The Web App will be able to send a “web_app_data”
    service message. Available in private chats only.
    """


class KeyboardButtonRequestUsers(BaseModel):
    """This object defines the criteria used to request suitable users.

    Information about the selected users will be shared with the bot
    when the corresponding button is pressed. More about requesting
    users »
    """

    request_id: int
    """Signed 32-bit identifier of the request that will be received back in
    the UsersShared object.

    Must be unique within the message
    """

    user_is_bot: Optional[bool] = None
    """Optional.

    Pass True to request bots, pass False to request regular users. If
    not specified, no additional restrictions are applied.
    """

    user_is_premium: Optional[bool] = None
    """Optional.

    Pass True to request premium users, pass False to request non-
    premium users. If not specified, no additional restrictions are
    applied.
    """

    max_quantity: Optional[int] = None
    """Optional.

    The maximum number of users to be selected; 1-10. Defaults to 1.
    """

    request_name: Optional[bool] = None
    """Optional.

    Pass True to request the users' first and last names
    """

    request_username: Optional[bool] = None
    """Optional.

    Pass True to request the users' usernames
    """

    request_photo: Optional[bool] = None
    """Optional.

    Pass True to request the users' photos
    """


class KeyboardButtonRequestChat(BaseModel):
    """This object defines the criteria used to request a suitable chat.

    Information about the selected chat will be shared with the bot when
    the corresponding button is pressed. The bot will be granted
    requested rights in the chat if appropriate. More about requesting
    chats ».
    """

    request_id: int
    """Signed 32-bit identifier of the request, which will be received back in
    the ChatShared object.

    Must be unique within the message
    """

    chat_is_channel: bool
    """Pass True to request a channel chat, pass False to request a group or a
    supergroup chat."""

    chat_is_forum: Optional[bool] = None
    """Optional.

    Pass True to request a forum supergroup, pass False to request a
    non-forum chat. If not specified, no additional restrictions are
    applied.
    """

    chat_has_username: Optional[bool] = None
    """Optional.

    Pass True to request a supergroup or a channel with a username, pass
    False to request a chat without a username. If not specified, no
    additional restrictions are applied.
    """

    chat_is_created: Optional[bool] = None
    """Optional.

    Pass True to request a chat owned by the user. Otherwise, no
    additional restrictions are applied.
    """

    user_administrator_rights: Optional["ChatAdministratorRights"] = None
    """Optional.

    A JSON-serialized object listing the required administrator rights
    of the user in the chat. The rights must be a superset of
    bot_administrator_rights. If not specified, no additional
    restrictions are applied.
    """

    bot_administrator_rights: Optional["ChatAdministratorRights"] = None
    """Optional.

    A JSON-serialized object listing the required administrator rights
    of the bot in the chat. The rights must be a subset of
    user_administrator_rights. If not specified, no additional
    restrictions are applied.
    """

    bot_is_member: Optional[bool] = None
    """Optional.

    Pass True to request a chat with the bot as a member. Otherwise, no
    additional restrictions are applied.
    """

    request_title: Optional[bool] = None
    """Optional.

    Pass True to request the chat's title
    """

    request_username: Optional[bool] = None
    """Optional.

    Pass True to request the chat's username
    """

    request_photo: Optional[bool] = None
    """Optional.

    Pass True to request the chat's photo
    """


class KeyboardButtonPollType(BaseModel):
    """This object represents type of a poll, which is allowed to be created
    and sent when the corresponding button is pressed."""

    type: Optional[str] = None
    """Optional.

    If quiz is passed, the user will be allowed to create only polls in
    the quiz mode. If regular is passed, only regular polls will be
    allowed. Otherwise, the user will be allowed to create a poll of any
    type.
    """


class ReplyKeyboardRemove(BaseModel):
    """Upon receiving a message with this object, Telegram clients will remove
    the current custom keyboard and display the default letter- keyboard.

    By default, custom keyboards are displayed until a new keyboard is
    sent by a bot. An exception is made for one-time keyboards that are
    hidden immediately after the user presses a button (see
    ReplyKeyboardMarkup). Not supported in channels and for messages
    sent on behalf of a Telegram Business account.
    """

    remove_keyboard: bool
    """Requests clients to remove the custom keyboard (user will not be able to
    summon this keyboard; if you want to hide the keyboard from sight but keep
    it accessible, use one_time_keyboard in ReplyKeyboardMarkup)"""

    selective: Optional[bool] = None
    """Optional.

    Use this parameter if you want to remove the keyboard for specific
    users only. Targets: 1) users that are @mentioned in the text of the
    Message object; 2) if the bot's message is a reply to a message in
    the same chat and forum topic, sender of the original
    message.Example: A user votes in a poll, bot returns confirmation
    message in reply to the vote and removes the keyboard for that user,
    while still showing the keyboard with poll options to users who
    haven't voted yet.
    """


class InlineKeyboardMarkup(BaseModel):
    """This object represents an inline keyboard that appears right next to the
    message it belongs to."""

    inline_keyboard: List[List["InlineKeyboardButton"]]
    """Array of button rows, each represented by an Array of
    InlineKeyboardButton objects."""


class InlineKeyboardButton(BaseModel):
    """This object represents one button of an inline keyboard.

    Exactly one of the optional fields must be used to specify type of
    the button.
    """

    text: str
    """Label text on the button."""

    url: Optional[str] = None
    """Optional.

    HTTP or tg:// URL to be opened when the button is pressed. Links
    tg://user?id=<user_id> can be used to mention a user by their
    identifier without using a username, if this is allowed by their
    privacy settings.
    """

    callback_data: Optional[str] = None
    """Optional.

    Data to be sent in a callback query to the bot when the button is
    pressed, 1-64 bytes
    """

    web_app: Optional["WebAppInfo"] = None
    """Optional.

    Description of the Web App that will be launched when the user
    presses the button. The Web App will be able to send an arbitrary
    message on behalf of the user using the method answerWebAppQuery.
    Available only in private chats between a user and the bot. Not
    supported for messages sent on behalf of a Telegram Business
    account.
    """

    login_url: Optional["LoginUrl"] = None
    """Optional.

    An HTTPS URL used to automatically authorize the user. Can be used
    as a replacement for the Telegram Login Widget.
    """

    switch_inline_query: Optional[str] = None
    """Optional.

    If set, pressing the button will prompt the user to select one of
    their chats, open that chat and insert the bot's username and the
    specified inline query in the input field. May be empty, in which
    case just the bot's username will be inserted. Not supported for
    messages sent on behalf of a Telegram Business account.
    """

    switch_inline_query_current_chat: Optional[str] = None
    """Optional. If set, pressing the button will insert the bot's username and
    the specified inline query in the current chat's input field. May be empty,
    in which case only the bot's username will be inserted.This.

    offers a quick way for the user to open your bot in inline mode in the
    same chat - good for selecting something from multiple options. Not
    supported in channels and for messages sent on behalf of a Telegram
    Business account.
    """

    switch_inline_query_chosen_chat: Optional["SwitchInlineQueryChosenChat"] = None
    """Optional.

    If set, pressing the button will prompt the user to select one of
    their chats of the specified type, open that chat and insert the
    bot's username and the specified inline query in the input field.
    Not supported for messages sent on behalf of a Telegram Business
    account.
    """

    callback_game: Optional["CallbackGame"] = None
    """Optional.

    Description of the game that will be launched when the user presses
    the button.NOTE: This type of button must always be the first button
    in the first row.
    """

    pay: Optional[bool] = None
    """Optional.

    Specify True, to send a Pay button. Substrings “” and “XTR” in the
    buttons's text will be replaced with a Telegram Star icon.NOTE: This
    type of button must always be the first button in the first row and
    can only be used in invoice messages.
    """


class LoginUrl(BaseModel):
    """This object represents a parameter of the inline keyboard button used to
    automatically authorize a user.

    Serves as a great replacement for the Telegram Login Widget when the
    user is coming from Telegram. All the user needs to do is tap/click
    a button and confirm that they want to log in:
    """

    url: str
    """An HTTPS URL to be opened with user authorization data added to the
    query string when the button is pressed.

    If the user refuses to provide authorization data, the original URL
    without information about the user will be opened. The data added is
    the same as described in Receiving authorization data.NOTE: You must
    always check the hash of the received data to verify the
    authentication and the integrity of the data as described in
    Checking authorization.
    """

    forward_text: Optional[str] = None
    """Optional.

    New text of the button in forwarded messages.
    """

    bot_username: Optional[str] = None
    """Optional.

    Username of a bot, which will be used for user authorization. See
    Setting up a bot for more details. If not specified, the current
    bot's username will be assumed. The url's domain must be the same as
    the domain linked with the bot. See Linking your domain to the bot
    for more details.
    """

    request_write_access: Optional[bool] = None
    """Optional.

    Pass True to request the permission for your bot to send messages to
    the user.
    """


class SwitchInlineQueryChosenChat(BaseModel):
    """This object represents an inline button that switches the current user
    to inline mode in a chosen chat, with an optional default inline query."""

    query: Optional[str] = None
    """Optional.

    The default inline query to be inserted in the input field. If left
    empty, only the bot's username will be inserted
    """

    allow_user_chats: Optional[bool] = None
    """Optional.

    True, if private chats with users can be chosen
    """

    allow_bot_chats: Optional[bool] = None
    """Optional.

    True, if private chats with bots can be chosen
    """

    allow_group_chats: Optional[bool] = None
    """Optional.

    True, if group and supergroup chats can be chosen
    """

    allow_channel_chats: Optional[bool] = None
    """Optional.

    True, if channel chats can be chosen
    """


class CallbackQuery(BaseModel):
    """This object represents an incoming callback query from a callback button
    in an inline keyboard.

    If the button that originated the query was attached to a message
    sent by the bot, the field message will be present. If the button
    was attached to a message sent via the bot (in inline mode), the
    field inline_message_id will be present. Exactly one of the fields
    data or game_short_name will be present.
    """

    id: str
    """Unique identifier for this query."""

    from_: "User" = Field(None, alias="from")
    """Sender."""

    chat_instance: str
    """Global identifier, uniquely corresponding to the chat to which the
    message with the callback button was sent.

    Useful for high scores in games.
    """

    message: Optional["MaybeInaccessibleMessage"] = None
    """Optional.

    Message sent by the bot with the callback button that originated the
    query
    """

    inline_message_id: Optional[str] = None
    """Optional.

    Identifier of the message sent via the bot in inline mode, that
    originated the query.
    """

    data: Optional[str] = None
    """Optional.

    Data associated with the callback button. Be aware that the message
    originated the query can contain no callback buttons with this data.
    """

    game_short_name: Optional[str] = None
    """Optional.

    Short name of a Game to be returned, serves as the unique identifier
    for the game
    """


class ForceReply(BaseModel):
    """Upon receiving a message with this object, Telegram clients will display
    a reply interface to the user (act as if the user has selected the bot's
    message and tapped 'Reply').

    This can be extremely useful if you want to create user-friendly
    step-by-step interfaces without having to sacrifice privacy mode.
    Not supported in channels and for messages sent on behalf of a
    Telegram Business account.
    """

    force_reply: bool
    """Shows reply interface to the user, as if they manually selected the
    bot's message and tapped 'Reply'."""

    input_field_placeholder: Optional[str] = None
    """Optional.

    The placeholder to be shown in the input field when the reply is
    active; 1-64 characters
    """

    selective: Optional[bool] = None
    """Optional.

    Use this parameter if you want to force reply from specific users
    only. Targets: 1) users that are @mentioned in the text of the
    Message object; 2) if the bot's message is a reply to a message in
    the same chat and forum topic, sender of the original message.
    """


class ChatPhoto(BaseModel):
    """This object represents a chat photo."""

    small_file_id: str
    """File identifier of small (160x160) chat photo.

    This file_id can be used only for photo download and only for as
    long as the photo is not changed.
    """

    small_file_unique_id: str
    """Unique file identifier of small (160x160) chat photo, which is supposed
    to be the same over time and for different bots.

    Can't be used to download or reuse the file.
    """

    big_file_id: str
    """File identifier of big (640x640) chat photo.

    This file_id can be used only for photo download and only for as
    long as the photo is not changed.
    """

    big_file_unique_id: str
    """Unique file identifier of big (640x640) chat photo, which is supposed to
    be the same over time and for different bots.

    Can't be used to download or reuse the file.
    """


class ChatInviteLink(BaseModel):
    """Represents an invite link for a chat."""

    invite_link: str
    """The invite link.

    If the link was created by another chat administrator, then the
    second part of the link will be replaced with “…”.
    """

    creator: "User"
    """Creator of the link."""

    creates_join_request: bool
    """True, if users joining the chat via the link need to be approved by chat
    administrators."""

    is_primary: bool
    """True, if the link is primary."""

    is_revoked: bool
    """True, if the link is revoked."""

    name: Optional[str] = None
    """Optional.

    Invite link name
    """

    expire_date: Optional[int] = None
    """Optional.

    Point in time (Unix timestamp) when the link will expire or has been
    expired
    """

    member_limit: Optional[int] = None
    """Optional.

    The maximum number of users that can be members of the chat
    simultaneously after joining the chat via this invite link; 1-99999
    """

    pending_join_request_count: Optional[int] = None
    """Optional.

    Number of pending join requests created using this link
    """


class ChatAdministratorRights(BaseModel):
    """Represents the rights of an administrator in a chat."""

    is_anonymous: bool
    """True, if the user's presence in the chat is hidden."""

    can_manage_chat: bool
    """True, if the administrator can access the chat event log, get boost
    list, see hidden supergroup and channel members, report spam messages and
    ignore slow mode.

    Implied by any other administrator privilege.
    """

    can_delete_messages: bool
    """True, if the administrator can delete messages of other users."""

    can_manage_video_chats: bool
    """True, if the administrator can manage video chats."""

    can_restrict_members: bool
    """True, if the administrator can restrict, ban or unban chat members, or
    access supergroup statistics."""

    can_promote_members: bool
    """True, if the administrator can add new administrators with a subset of
    their own privileges or demote administrators that they have promoted,
    directly or indirectly (promoted by administrators that were appointed by
    the user)"""

    can_change_info: bool
    """True, if the user is allowed to change the chat title, photo and other
    settings."""

    can_invite_users: bool
    """True, if the user is allowed to invite new users to the chat."""

    can_post_stories: bool
    """True, if the administrator can post stories to the chat."""

    can_edit_stories: bool
    """True, if the administrator can edit stories posted by other users, post
    stories to the chat page, pin chat stories, and access the chat's story
    archive."""

    can_delete_stories: bool
    """True, if the administrator can delete stories posted by other users."""

    can_post_messages: Optional[bool] = None
    """Optional.

    True, if the administrator can post messages in the channel, or
    access channel statistics; for channels only
    """

    can_edit_messages: Optional[bool] = None
    """Optional.

    True, if the administrator can edit messages of other users and can
    pin messages; for channels only
    """

    can_pin_messages: Optional[bool] = None
    """Optional.

    True, if the user is allowed to pin messages; for groups and
    supergroups only
    """

    can_manage_topics: Optional[bool] = None
    """Optional.

    True, if the user is allowed to create, rename, close, and reopen
    forum topics; for supergroups only
    """


class ChatMemberUpdated(BaseModel):
    """This object represents changes in the status of a chat member."""

    chat: "Chat"
    """Chat the user belongs to."""

    from_: "User" = Field(alias="from")
    """Performer of the action, which resulted in the change."""

    date: int
    """Date the change was done in Unix time."""

    old_chat_member: "ChatMember"
    """Previous information about the chat member."""

    new_chat_member: "ChatMember"
    """New information about the chat member."""

    invite_link: Optional["ChatInviteLink"] = None
    """Optional.

    Chat invite link, which was used by the user to join the chat; for
    joining by invite link events only.
    """

    via_join_request: Optional[bool] = None
    """Optional.

    True, if the user joined the chat after sending a direct join
    request without using an invite link and being approved by an
    administrator
    """

    via_chat_folder_invite_link: Optional[bool] = None
    """Optional.

    True, if the user joined the chat via a chat folder invite link
    """


class ChatMemberOwner(BaseModel):
    """Represents a chat member that owns the chat and has all administrator
    privileges."""

    status: str
    """The member's status in the chat, always “creator”"""

    user: "User"
    """Information about the user."""

    is_anonymous: bool
    """True, if the user's presence in the chat is hidden."""

    custom_title: Optional[str] = None
    """Optional.

    Custom title for this user
    """


class ChatMemberAdministrator(BaseModel):
    """Represents a chat member that has some additional privileges."""

    status: str
    """The member's status in the chat, always “administrator”"""

    user: "User"
    """Information about the user."""

    can_be_edited: bool
    """True, if the bot is allowed to edit administrator privileges of that
    user."""

    is_anonymous: bool
    """True, if the user's presence in the chat is hidden."""

    can_manage_chat: bool
    """True, if the administrator can access the chat event log, get boost
    list, see hidden supergroup and channel members, report spam messages and
    ignore slow mode.

    Implied by any other administrator privilege.
    """

    can_delete_messages: bool
    """True, if the administrator can delete messages of other users."""

    can_manage_video_chats: bool
    """True, if the administrator can manage video chats."""

    can_restrict_members: bool
    """True, if the administrator can restrict, ban or unban chat members, or
    access supergroup statistics."""

    can_promote_members: bool
    """True, if the administrator can add new administrators with a subset of
    their own privileges or demote administrators that they have promoted,
    directly or indirectly (promoted by administrators that were appointed by
    the user)"""

    can_change_info: bool
    """True, if the user is allowed to change the chat title, photo and other
    settings."""

    can_invite_users: bool
    """True, if the user is allowed to invite new users to the chat."""

    can_post_stories: bool
    """True, if the administrator can post stories to the chat."""

    can_edit_stories: bool
    """True, if the administrator can edit stories posted by other users, post
    stories to the chat page, pin chat stories, and access the chat's story
    archive."""

    can_delete_stories: bool
    """True, if the administrator can delete stories posted by other users."""

    can_post_messages: Optional[bool] = None
    """Optional.

    True, if the administrator can post messages in the channel, or
    access channel statistics; for channels only
    """

    can_edit_messages: Optional[bool] = None
    """Optional.

    True, if the administrator can edit messages of other users and can
    pin messages; for channels only
    """

    can_pin_messages: Optional[bool] = None
    """Optional.

    True, if the user is allowed to pin messages; for groups and
    supergroups only
    """

    can_manage_topics: Optional[bool] = None
    """Optional.

    True, if the user is allowed to create, rename, close, and reopen
    forum topics; for supergroups only
    """

    custom_title: Optional[str] = None
    """Optional.

    Custom title for this user
    """


class ChatMemberMember(BaseModel):
    """Represents a chat member that has no additional privileges or
    restrictions."""

    status: str
    """The member's status in the chat, always “member”"""

    user: "User"
    """Information about the user."""


class ChatMemberRestricted(BaseModel):
    """Represents a chat member that is under certain restrictions in the chat.

    Supergroups only.
    """

    status: str
    """The member's status in the chat, always “restricted”"""

    user: "User"
    """Information about the user."""

    is_member: bool
    """True, if the user is a member of the chat at the moment of the
    request."""

    can_send_messages: bool
    """True, if the user is allowed to send text messages, contacts, giveaways,
    giveaway winners, invoices, locations and venues."""

    can_send_audios: bool
    """True, if the user is allowed to send audios."""

    can_send_documents: bool
    """True, if the user is allowed to send documents."""

    can_send_photos: bool
    """True, if the user is allowed to send photos."""

    can_send_videos: bool
    """True, if the user is allowed to send videos."""

    can_send_video_notes: bool
    """True, if the user is allowed to send video notes."""

    can_send_voice_notes: bool
    """True, if the user is allowed to send voice notes."""

    can_send_polls: bool
    """True, if the user is allowed to send polls."""

    can_send_other_messages: bool
    """True, if the user is allowed to send animations, games, stickers and use
    inline bots."""

    can_add_web_page_previews: bool
    """True, if the user is allowed to add web page previews to their
    messages."""

    can_change_info: bool
    """True, if the user is allowed to change the chat title, photo and other
    settings."""

    can_invite_users: bool
    """True, if the user is allowed to invite new users to the chat."""

    can_pin_messages: bool
    """True, if the user is allowed to pin messages."""

    can_manage_topics: bool
    """True, if the user is allowed to create forum topics."""

    until_date: int
    """Date when restrictions will be lifted for this user; Unix time.

    If 0, then the user is restricted forever
    """


class ChatMemberLeft(BaseModel):
    """Represents a chat member that isn't currently a member of the chat, but
    may join it themselves."""

    status: str
    """The member's status in the chat, always “left”"""

    user: "User"
    """Information about the user."""


class ChatMemberBanned(BaseModel):
    """Represents a chat member that was banned in the chat and can't return to
    the chat or view chat messages."""

    status: str
    """The member's status in the chat, always “kicked”"""

    user: "User"
    """Information about the user."""

    until_date: int
    """Date when restrictions will be lifted for this user; Unix time.

    If 0, then the user is banned forever
    """


class ChatJoinRequest(BaseModel):
    """Represents a join request sent to a chat."""

    chat: "Chat"
    """Chat to which the request was sent."""

    from_: "User" = Field(alias="from")
    """User that sent the join request."""

    user_chat_id: int
    """Identifier of a private chat with the user who sent the join request.

    This number may have more than 32 significant bits and some
    programming languages may have difficulty/silent defects in
    interpreting it. But it has at most 52 significant bits, so a 64-bit
    integer or double-precision float type are safe for storing this
    identifier. The bot can use this identifier for 5 minutes to send
    messages until the join request is processed, assuming no other
    administrator contacted the user.
    """

    date: int
    """Date the request was sent in Unix time."""

    bio: Optional[str] = None
    """Optional.

    Bio of the user.
    """

    invite_link: Optional["ChatInviteLink"] = None
    """Optional.

    Chat invite link that was used by the user to send the join request
    """


class ChatPermissions(BaseModel):
    """Describes actions that a non-administrator user is allowed to take in a
    chat."""

    can_send_messages: Optional[bool] = None
    """Optional.

    True, if the user is allowed to send text messages, contacts,
    giveaways, giveaway winners, invoices, locations and venues
    """

    can_send_audios: Optional[bool] = None
    """Optional.

    True, if the user is allowed to send audios
    """

    can_send_documents: Optional[bool] = None
    """Optional.

    True, if the user is allowed to send documents
    """

    can_send_photos: Optional[bool] = None
    """Optional.

    True, if the user is allowed to send photos
    """

    can_send_videos: Optional[bool] = None
    """Optional.

    True, if the user is allowed to send videos
    """

    can_send_video_notes: Optional[bool] = None
    """Optional.

    True, if the user is allowed to send video notes
    """

    can_send_voice_notes: Optional[bool] = None
    """Optional.

    True, if the user is allowed to send voice notes
    """

    can_send_polls: Optional[bool] = None
    """Optional.

    True, if the user is allowed to send polls
    """

    can_send_other_messages: Optional[bool] = None
    """Optional.

    True, if the user is allowed to send animations, games, stickers and
    use inline bots
    """

    can_add_web_page_previews: Optional[bool] = None
    """Optional.

    True, if the user is allowed to add web page previews to their
    messages
    """

    can_change_info: Optional[bool] = None
    """Optional.

    True, if the user is allowed to change the chat title, photo and
    other settings. Ignored in public supergroups
    """

    can_invite_users: Optional[bool] = None
    """Optional.

    True, if the user is allowed to invite new users to the chat
    """

    can_pin_messages: Optional[bool] = None
    """Optional.

    True, if the user is allowed to pin messages. Ignored in public
    supergroups
    """

    can_manage_topics: Optional[bool] = None
    """Optional.

    True, if the user is allowed to create forum topics. If omitted
    defaults to the value of can_pin_messages
    """


class Birthdate(BaseModel):
    """Describes the birthdate of a user."""

    day: int
    """Day of the user's birth; 1-31."""

    month: int
    """Month of the user's birth; 1-12."""

    year: Optional[int] = None
    """Optional.

    Year of the user's birth
    """


class BusinessIntro(BaseModel):
    """Contains information about the start page settings of a Telegram
    Business account."""

    title: Optional[str] = None
    """Optional.

    Title text of the business intro
    """

    message: Optional[str] = None
    """Optional.

    Message text of the business intro
    """

    sticker: Optional["Sticker"] = None
    """Optional.

    Sticker of the business intro
    """


class BusinessLocation(BaseModel):
    """Contains information about the location of a Telegram Business
    account."""

    address: str
    """Address of the business."""

    location: Optional["Location"] = None
    """Optional.

    Location of the business
    """


class BusinessOpeningHoursInterval(BaseModel):
    """Describes an interval of time during which a business is open."""

    opening_minute: int
    """The minute's sequence number in a week, starting on Monday, marking.

    the start of the time interval during which the business is open; 0
    - 7 * 24 * 60
    """

    closing_minute: int
    """The minute's sequence number in a week, starting on Monday, marking.

    the end of the time interval during which the business is open; 0 - 8
    * 24 * 60
    """


class BusinessOpeningHours(BaseModel):
    """Describes the opening hours of a business."""

    time_zone_name: str
    """Unique name of the time zone for which the opening hours are defined."""

    opening_hours: List["BusinessOpeningHoursInterval"]
    """List of time intervals describing business opening hours."""


class ChatLocation(BaseModel):
    """Represents a location to which a chat is connected."""

    location: "Location"
    """The location to which the supergroup is connected.

    Can't be a live location.
    """

    address: str
    """Location address; 1-64 characters, as defined by the chat owner."""


class ReactionTypeEmoji(BaseModel):
    """The reaction is based on an emoji."""

    type: str
    """Type of the reaction, always “emoji”"""

    emoji: str
    """Reaction emoji.

    Currently, it can be one of \"\", \"\", \"\", \"\", \"\", \"\",
    \"\", \"\", \"\", \"\", \"\", \"\", \"\", \"\", \"\", \"\", \"\",
    \"\", \"\", \"\", \"\", \"\", \"\", \"\", \"\", \"\", \"\", \"\",
    \"\", \"\", \"\", \"\", \"\", \"\", \"\", \"\", \"\", \"\", \"\",
    \"\", \"\", \"\", \"\", \"\", \"\", \"\", \"\", \"\", \"\", \"\",
    \"\", \"\", \"\", \"\", \"\", \"\", \"\", \"\", \"\", \"\", \"\",
    \"\", \"\", \"\", \"\", \"\", \"\", \"\", \"\", \"\", \"\", \"\",
    \"\"
    """


class ReactionTypeCustomEmoji(BaseModel):
    """The reaction is based on a custom emoji."""

    type: str
    """Type of the reaction, always “custom_emoji”"""

    custom_emoji_id: str
    """Custom emoji identifier."""


class ReactionCount(BaseModel):
    """Represents a reaction added to a message along with the number of times
    it was added."""

    type: "ReactionType"
    """Type of the reaction."""

    total_count: int
    """Number of times the reaction was added."""


class MessageReactionUpdated(BaseModel):
    """This object represents a change of a reaction on a message performed by
    a user."""

    chat: "Chat"
    """The chat containing the message the user reacted to."""

    message_id: int
    """Unique identifier of the message inside the chat."""

    date: int
    """Date of the change in Unix time."""

    old_reaction: List["ReactionType"]
    """Previous list of reaction types that were set by the user."""

    new_reaction: List["ReactionType"]
    """New list of reaction types that have been set by the user."""

    user: Optional["User"] = None
    """Optional.

    The user that changed the reaction, if the user isn't anonymous
    """

    actor_chat: Optional["Chat"] = None
    """Optional.

    The chat on behalf of which the reaction was changed, if the user is
    anonymous
    """


class MessageReactionCountUpdated(BaseModel):
    """This object represents reaction changes on a message with anonymous
    reactions."""

    chat: "Chat"
    """The chat containing the message."""

    message_id: int
    """Unique message identifier inside the chat."""

    date: int
    """Date of the change in Unix time."""

    reactions: List["ReactionCount"]
    """List of reactions that are present on the message."""


class ForumTopic(BaseModel):
    """This object represents a forum topic."""

    message_thread_id: int
    """Unique identifier of the forum topic."""

    name: str
    """Name of the topic."""

    icon_color: int
    """Color of the topic icon in RGB format."""

    icon_custom_emoji_id: Optional[str] = None
    """Optional.

    Unique identifier of the custom emoji shown as the topic icon
    """


class BotCommand(BaseModel):
    """This object represents a bot command."""

    command: str
    """Text of the command; 1-32 characters.

    Can contain only lowercase English letters, digits and underscores.
    """

    description: str
    """Description of the command; 1-256 characters."""


class BotCommandScopeDefault(BaseModel):
    """Represents the default scope of bot commands.

    Default commands are used if no commands with a narrower scope are
    specified for the user.
    """

    type: str
    """Scope type, must be default."""


class BotCommandScopeAllPrivateChats(BaseModel):
    """Represents the scope of bot commands, covering all private chats."""

    type: str
    """Scope type, must be all_private_chats."""


class BotCommandScopeAllGroupChats(BaseModel):
    """Represents the scope of bot commands, covering all group and supergroup
    chats."""

    type: str
    """Scope type, must be all_group_chats."""


class BotCommandScopeAllChatAdministrators(BaseModel):
    """Represents the scope of bot commands, covering all group and supergroup
    chat administrators."""

    type: str
    """Scope type, must be all_chat_administrators."""


class BotCommandScopeChat(BaseModel):
    """Represents the scope of bot commands, covering a specific chat."""

    type: str
    """Scope type, must be chat."""

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target
    supergroup (in the format @supergroupusername)"""


class BotCommandScopeChatAdministrators(BaseModel):
    """Represents the scope of bot commands, covering all administrators of a
    specific group or supergroup chat."""

    type: str
    """Scope type, must be chat_administrators."""

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target
    supergroup (in the format @supergroupusername)"""


class BotCommandScopeChatMember(BaseModel):
    """Represents the scope of bot commands, covering a specific member of a
    group or supergroup chat."""

    type: str
    """Scope type, must be chat_member."""

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target
    supergroup (in the format @supergroupusername)"""

    user_id: int
    """Unique identifier of the target user."""


class BotName(BaseModel):
    """This object represents the bot's name."""

    name: str
    """The bot's name."""


class BotDescription(BaseModel):
    """This object represents the bot's description."""

    description: str
    """The bot's description."""


class BotShortDescription(BaseModel):
    """This object represents the bot's short description."""

    short_description: str
    """The bot's short description."""


class MenuButtonCommands(BaseModel):
    """Represents a menu button, which opens the bot's list of commands."""

    type: str
    """Type of the button, must be commands."""


class MenuButtonWebApp(BaseModel):
    """Represents a menu button, which launches a Web App."""

    type: str
    """Type of the button, must be web_app."""

    text: str
    """Text on the button."""

    web_app: "WebAppInfo"
    """Description of the Web App that will be launched when the user presses
    the button.

    The Web App will be able to send an arbitrary message on behalf of
    the user using the method answerWebAppQuery. Alternatively, a t.me
    link to a Web App of the bot can be specified in the object instead
    of the Web App's URL, in which case the Web App will be opened as if
    the user pressed the link.
    """


class MenuButtonDefault(BaseModel):
    """Describes that no specific value for the menu button was set."""

    type: str
    """Type of the button, must be default."""


class ChatBoostSourcePremium(BaseModel):
    """The boost was obtained by subscribing to Telegram Premium or by gifting
    a Telegram Premium subscription to another user."""

    source: str
    """Source of the boost, always “premium”"""

    user: "User"
    """User that boosted the chat."""


class ChatBoostSourceGiftCode(BaseModel):
    """The boost was obtained by the creation of Telegram Premium gift codes to
    boost a chat.

    Each such code boosts the chat 4 times for the duration of the
    corresponding Telegram Premium subscription.
    """

    source: str
    """Source of the boost, always “gift_code”"""

    user: "User"
    """User for which the gift code was created."""


class ChatBoostSourceGiveaway(BaseModel):
    """The boost was obtained by the creation of a Telegram Premium giveaway.

    This boosts the chat 4 times for the duration of the corresponding
    Telegram Premium subscription.
    """

    source: str
    """Source of the boost, always “giveaway”"""

    giveaway_message_id: int
    """Identifier of a message in the chat with the giveaway; the message could
    have been deleted already.

    May be 0 if the message isn't sent yet.
    """

    user: Optional["User"] = None
    """Optional.

    User that won the prize in the giveaway if any
    """

    is_unclaimed: Optional[bool] = None
    """Optional.

    True, if the giveaway was completed, but there was no user to win
    the prize
    """


class ChatBoost(BaseModel):
    """This object contains information about a chat boost."""

    boost_id: str
    """Unique identifier of the boost."""

    add_date: int
    """Point in time (Unix timestamp) when the chat was boosted."""

    expiration_date: int
    """Point in time (Unix timestamp) when the boost will automatically expire,
    unless the booster's Telegram Premium subscription is prolonged."""

    source: "ChatBoostSource"
    """Source of the added boost."""


class ChatBoostUpdated(BaseModel):
    """This object represents a boost added to a chat or changed."""

    chat: "Chat"
    """Chat which was boosted."""

    boost: "ChatBoost"
    """Information about the chat boost."""


class ChatBoostRemoved(BaseModel):
    """This object represents a boost removed from a chat."""

    chat: "Chat"
    """Chat which was boosted."""

    boost_id: str
    """Unique identifier of the boost."""

    remove_date: int
    """Point in time (Unix timestamp) when the boost was removed."""

    source: "ChatBoostSource"
    """Source of the removed boost."""


class UserChatBoosts(BaseModel):
    """This object represents a list of boosts added to a chat by a user."""

    boosts: List["ChatBoost"]
    """The list of boosts added to the chat by the user."""


class BusinessConnection(BaseModel):
    """Describes the connection of the bot with a business account."""

    id: str
    """Unique identifier of the business connection."""

    user: "User"
    """Business account user that created the business connection."""

    user_chat_id: int
    """Identifier of a private chat with the user who created the business
    connection.

    This number may have more than 32 significant bits and some
    programming languages may have difficulty/silent defects in
    interpreting it. But it has at most 52 significant bits, so a 64-bit
    integer or double-precision float type are safe for storing this
    identifier.
    """

    date: int
    """Date the connection was established in Unix time."""

    can_reply: bool
    """True, if the bot can act on behalf of the business account in chats that
    were active in the last 24 hours."""

    is_enabled: bool
    """True, if the connection is active."""


class BusinessMessagesDeleted(BaseModel):
    """This object is received when messages are deleted from a connected
    business account."""

    business_connection_id: str
    """Unique identifier of the business connection."""

    chat: "Chat"
    """Information about a chat in the business account.

    The bot may not have access to the chat or the corresponding user.
    """

    message_ids: List[int]
    """The list of identifiers of deleted messages in the chat of the business
    account."""


class ResponseParameters(BaseModel):
    """Describes why a request was unsuccessful."""

    migrate_to_chat_id: Optional[int] = None
    """Optional.

    The group has been migrated to a supergroup with the specified
    identifier. This number may have more than 32 significant bits and
    some programming languages may have difficulty/silent defects in
    interpreting it. But it has at most 52 significant bits, so a signed
    64-bit integer or double-precision float type are safe for storing
    this identifier.
    """

    retry_after: Optional[int] = None
    """Optional.

    In case of exceeding flood control, the number of seconds left to
    wait before the request can be repeated
    """


class InputMediaPhoto(BaseModel):
    """Represents a photo to be sent."""

    type: str
    """Type of the result, must be photo."""

    media: str
    """File to send.

    Pass a file_id to send a file that exists on the Telegram servers
    (recommended), pass an HTTP URL for Telegram to get a file from the
    Internet, or pass “attach://<file_attach_name>” to upload a new one
    using multipart/form-data under <file_attach_name> name. More
    information on Sending Files »
    """

    caption: Optional[str] = None
    """Optional.

    Caption of the photo to be sent, 0-1024 characters after entities
    parsing
    """

    parse_mode: Optional[str] = None
    """Optional.

    Mode for parsing entities in the photo caption. See formatting
    options for more details.
    """

    caption_entities: Optional[List["MessageEntity"]] = None
    """Optional.

    List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    """

    show_caption_above_media: Optional[bool] = None
    """Optional.

    Pass True, if the caption must be shown above the message media
    """

    has_spoiler: Optional[bool] = None
    """Optional.

    Pass True if the photo needs to be covered with a spoiler animation
    """


class InputMediaVideo(BaseModel):
    """Represents a video to be sent."""

    type: str
    """Type of the result, must be video."""

    media: str
    """File to send.

    Pass a file_id to send a file that exists on the Telegram servers
    (recommended), pass an HTTP URL for Telegram to get a file from the
    Internet, or pass “attach://<file_attach_name>” to upload a new one
    using multipart/form-data under <file_attach_name> name. More
    information on Sending Files »
    """

    thumbnail: Optional[Union["InputFile", str]] = None
    """Optional.

    Thumbnail of the file sent; can be ignored if thumbnail generation
    for the file is supported server-side. The thumbnail should be in
    JPEG format and less than 200 kB in size. A thumbnail's width and
    height should not exceed 320. Ignored if the file is not uploaded
    using multipart/form-data. Thumbnails can't be reused and can be
    only uploaded as a new file, so you can pass
    “attach://<file_attach_name>” if the thumbnail was uploaded using
    multipart/form-data under <file_attach_name>. More information on
    Sending Files »
    """

    caption: Optional[str] = None
    """Optional.

    Caption of the video to be sent, 0-1024 characters after entities
    parsing
    """

    parse_mode: Optional[str] = None
    """Optional.

    Mode for parsing entities in the video caption. See formatting
    options for more details.
    """

    caption_entities: Optional[List["MessageEntity"]] = None
    """Optional.

    List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    """

    show_caption_above_media: Optional[bool] = None
    """Optional.

    Pass True, if the caption must be shown above the message media
    """

    width: Optional[int] = None
    """Optional.

    Video width
    """

    height: Optional[int] = None
    """Optional.

    Video height
    """

    duration: Optional[int] = None
    """Optional.

    Video duration in seconds
    """

    supports_streaming: Optional[bool] = None
    """Optional.

    Pass True if the uploaded video is suitable for streaming
    """

    has_spoiler: Optional[bool] = None
    """Optional.

    Pass True if the video needs to be covered with a spoiler animation
    """


class InputMediaAnimation(BaseModel):
    """Represents an animation file (GIF or H.264/MPEG-4 AVC video without
    sound) to be sent."""

    type: str
    """Type of the result, must be animation."""

    media: str
    """File to send.

    Pass a file_id to send a file that exists on the Telegram servers
    (recommended), pass an HTTP URL for Telegram to get a file from the
    Internet, or pass “attach://<file_attach_name>” to upload a new one
    using multipart/form-data under <file_attach_name> name. More
    information on Sending Files »
    """

    thumbnail: Optional[Union["InputFile", str]] = None
    """Optional.

    Thumbnail of the file sent; can be ignored if thumbnail generation
    for the file is supported server-side. The thumbnail should be in
    JPEG format and less than 200 kB in size. A thumbnail's width and
    height should not exceed 320. Ignored if the file is not uploaded
    using multipart/form-data. Thumbnails can't be reused and can be
    only uploaded as a new file, so you can pass
    “attach://<file_attach_name>” if the thumbnail was uploaded using
    multipart/form-data under <file_attach_name>. More information on
    Sending Files »
    """

    caption: Optional[str] = None
    """Optional.

    Caption of the animation to be sent, 0-1024 characters after
    entities parsing
    """

    parse_mode: Optional[str] = None
    """Optional.

    Mode for parsing entities in the animation caption. See formatting
    options for more details.
    """

    caption_entities: Optional[List["MessageEntity"]] = None
    """Optional.

    List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    """

    show_caption_above_media: Optional[bool] = None
    """Optional.

    Pass True, if the caption must be shown above the message media
    """

    width: Optional[int] = None
    """Optional.

    Animation width
    """

    height: Optional[int] = None
    """Optional.

    Animation height
    """

    duration: Optional[int] = None
    """Optional.

    Animation duration in seconds
    """

    has_spoiler: Optional[bool] = None
    """Optional.

    Pass True if the animation needs to be covered with a spoiler
    animation
    """


class InputMediaAudio(BaseModel):
    """Represents an audio file to be treated as music to be sent."""

    type: str
    """Type of the result, must be audio."""

    media: str
    """File to send.

    Pass a file_id to send a file that exists on the Telegram servers
    (recommended), pass an HTTP URL for Telegram to get a file from the
    Internet, or pass “attach://<file_attach_name>” to upload a new one
    using multipart/form-data under <file_attach_name> name. More
    information on Sending Files »
    """

    thumbnail: Optional[Union["InputFile", str]] = None
    """Optional.

    Thumbnail of the file sent; can be ignored if thumbnail generation
    for the file is supported server-side. The thumbnail should be in
    JPEG format and less than 200 kB in size. A thumbnail's width and
    height should not exceed 320. Ignored if the file is not uploaded
    using multipart/form-data. Thumbnails can't be reused and can be
    only uploaded as a new file, so you can pass
    “attach://<file_attach_name>” if the thumbnail was uploaded using
    multipart/form-data under <file_attach_name>. More information on
    Sending Files »
    """

    caption: Optional[str] = None
    """Optional.

    Caption of the audio to be sent, 0-1024 characters after entities
    parsing
    """

    parse_mode: Optional[str] = None
    """Optional.

    Mode for parsing entities in the audio caption. See formatting
    options for more details.
    """

    caption_entities: Optional[List["MessageEntity"]] = None
    """Optional.

    List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    """

    duration: Optional[int] = None
    """Optional.

    Duration of the audio in seconds
    """

    performer: Optional[str] = None
    """Optional.

    Performer of the audio
    """

    title: Optional[str] = None
    """Optional.

    Title of the audio
    """


class InputMediaDocument(BaseModel):
    """Represents a general file to be sent."""

    type: str
    """Type of the result, must be document."""

    media: str
    """File to send.

    Pass a file_id to send a file that exists on the Telegram servers
    (recommended), pass an HTTP URL for Telegram to get a file from the
    Internet, or pass “attach://<file_attach_name>” to upload a new one
    using multipart/form-data under <file_attach_name> name. More
    information on Sending Files »
    """

    thumbnail: Optional[Union["InputFile", str]] = None
    """Optional.

    Thumbnail of the file sent; can be ignored if thumbnail generation
    for the file is supported server-side. The thumbnail should be in
    JPEG format and less than 200 kB in size. A thumbnail's width and
    height should not exceed 320. Ignored if the file is not uploaded
    using multipart/form-data. Thumbnails can't be reused and can be
    only uploaded as a new file, so you can pass
    “attach://<file_attach_name>” if the thumbnail was uploaded using
    multipart/form-data under <file_attach_name>. More information on
    Sending Files »
    """

    caption: Optional[str] = None
    """Optional.

    Caption of the document to be sent, 0-1024 characters after entities
    parsing
    """

    parse_mode: Optional[str] = None
    """Optional.

    Mode for parsing entities in the document caption. See formatting
    options for more details.
    """

    caption_entities: Optional[List["MessageEntity"]] = None
    """Optional.

    List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    """

    disable_content_type_detection: Optional[bool] = None
    """Optional.

    Disables automatic server-side content type detection for files
    uploaded using multipart/form-data. Always True, if the document is
    sent as part of an album.
    """


class InputPaidMediaPhoto(BaseModel):
    """The paid media to send is a photo."""

    type: str
    """Type of the media, must be photo."""

    media: str
    """File to send.

    Pass a file_id to send a file that exists on the Telegram servers
    (recommended), pass an HTTP URL for Telegram to get a file from the
    Internet, or pass “attach://<file_attach_name>” to upload a new one
    using multipart/form-data under <file_attach_name> name. More
    information on Sending Files »
    """


class InputPaidMediaVideo(BaseModel):
    """The paid media to send is a video."""

    type: str
    """Type of the media, must be video."""

    media: str
    """File to send.

    Pass a file_id to send a file that exists on the Telegram servers
    (recommended), pass an HTTP URL for Telegram to get a file from the
    Internet, or pass “attach://<file_attach_name>” to upload a new one
    using multipart/form-data under <file_attach_name> name. More
    information on Sending Files »
    """

    thumbnail: Optional[Union["InputFile", str]] = None
    """Optional.

    Thumbnail of the file sent; can be ignored if thumbnail generation
    for the file is supported server-side. The thumbnail should be in
    JPEG format and less than 200 kB in size. A thumbnail's width and
    height should not exceed 320. Ignored if the file is not uploaded
    using multipart/form-data. Thumbnails can't be reused and can be
    only uploaded as a new file, so you can pass
    “attach://<file_attach_name>” if the thumbnail was uploaded using
    multipart/form-data under <file_attach_name>. More information on
    Sending Files »
    """

    width: Optional[int] = None
    """Optional.

    Video width
    """

    height: Optional[int] = None
    """Optional.

    Video height
    """

    duration: Optional[int] = None
    """Optional.

    Video duration in seconds
    """

    supports_streaming: Optional[bool] = None
    """Optional.

    Pass True if the uploaded video is suitable for streaming
    """


class Sticker(BaseModel):
    """This object represents a sticker."""

    file_id: str
    """Identifier for this file, which can be used to download or reuse the
    file."""

    file_unique_id: str
    """Unique identifier for this file, which is supposed to be the same over
    time and for different bots.

    Can't be used to download or reuse the file.
    """

    type: str
    """Type of the sticker, currently one of “regular”, “mask”, “custom_emoji”.

    The type of the sticker is independent from its format, which is
    determined by the fields is_animated and is_video.
    """

    width: int
    """Sticker width."""

    height: int
    """Sticker height."""

    is_animated: bool
    """True, if the sticker is animated."""

    is_video: bool
    """True, if the sticker is a video sticker."""

    thumbnail: Optional["PhotoSize"] = None
    """Optional.

    Sticker thumbnail in the .WEBP or .JPG format
    """

    emoji: Optional[str] = None
    """Optional.

    Emoji associated with the sticker
    """

    set_name: Optional[str] = None
    """Optional.

    Name of the sticker set to which the sticker belongs
    """

    premium_animation: Optional["File"] = None
    """Optional.

    For premium regular stickers, premium animation for the sticker
    """

    mask_position: Optional["MaskPosition"] = None
    """Optional.

    For mask stickers, the position where the mask should be placed
    """

    custom_emoji_id: Optional[str] = None
    """Optional.

    For custom emoji stickers, unique identifier of the custom emoji
    """

    needs_repainting: Optional[bool] = None
    """Optional.

    True, if the sticker must be repainted to a text color in messages,
    the color of the Telegram Premium badge in emoji status, white color
    on chat photos, or another appropriate color in other places
    """

    file_size: Optional[int] = None
    """Optional.

    File size in bytes
    """


class StickerSet(BaseModel):
    """This object represents a sticker set."""

    name: str
    """Sticker set name."""

    title: str
    """Sticker set title."""

    sticker_type: str
    """Type of stickers in the set, currently one of “regular”, “mask”,
    “custom_emoji”"""

    stickers: List["Sticker"]
    """List of all set stickers."""

    thumbnail: Optional["PhotoSize"] = None
    """Optional.

    Sticker set thumbnail in the .WEBP, .TGS, or .WEBM format
    """


class MaskPosition(BaseModel):
    """This object describes the position on faces where a mask should be
    placed by default."""

    point: str
    """The part of the face relative to which the mask should be placed.

    One of “forehead”, “eyes”, “mouth”, or “chin”.
    """

    x_shift: float
    """Shift by X-axis measured in widths of the mask scaled to the face size,
    from left to right.

    For example, choosing -1.0 will place mask just to the left of the
    default mask position.
    """

    y_shift: float
    """Shift by Y-axis measured in heights of the mask scaled to the face size,
    from top to bottom.

    For example, 1.0 will place the mask just below the default mask
    position.
    """

    scale: float
    """Mask scaling coefficient.

    For example, 2.0 means double size.
    """


class InputSticker(BaseModel):
    """This object describes a sticker to be added to a sticker set."""

    sticker: Union["InputFile", str]
    """The added sticker.

    Pass a file_id as a String to send a file that already exists on the
    Telegram servers, pass an HTTP URL as a String for Telegram to get a
    file from the Internet, upload a new one using multipart/form-data,
    or pass “attach://<file_attach_name>” to upload a new one using
    multipart/form-data under <file_attach_name> name. Animated and
    video stickers can't be uploaded via HTTP URL. More information on
    Sending Files »
    """

    format: str
    """Format of the added sticker, must be one of “static” for a .WEBP or .PNG
    image, “animated” for a .TGS animation, “video” for a WEBM video."""

    emoji_list: List[str]
    """List of 1-20 emoji associated with the sticker."""

    mask_position: Optional["MaskPosition"] = None
    """Optional.

    Position where the mask should be placed on faces. For “mask”
    stickers only.
    """

    keywords: Optional[List[str]] = None
    """Optional.

    List of 0-20 search keywords for the sticker with total length of up
    to 64 characters. For “regular” and “custom_emoji” stickers only.
    """


class InlineQuery(BaseModel):
    """This object represents an incoming inline query.

    When the user sends an empty query, your bot could return some
    default or trending results.
    """

    id: str
    """Unique identifier for this query."""

    from_: "User" = Field(alias="from")
    """Sender."""

    query: str
    """Text of the query (up to 256 characters)"""

    offset: str
    """Offset of the results to be returned, can be controlled by the bot."""

    chat_type: Optional[str] = None
    """Optional.

    Type of the chat from which the inline query was sent. Can be either
    “sender” for a private chat with the inline query sender, “private”,
    “group”, “supergroup”, or “channel”. The chat type should be always
    known for requests sent from official clients and most third-party
    clients, unless the request was sent from a secret chat
    """

    location: Optional["Location"] = None
    """Optional.

    Sender location, only for bots that request user location
    """


class InlineQueryResultsButton(BaseModel):
    """This object represents a button to be shown above inline query results.

    You must use exactly one of the optional fields.
    """

    text: str
    """Label text on the button."""

    web_app: Optional["WebAppInfo"] = None
    """Optional.

    Description of the Web App that will be launched when the user
    presses the button. The Web App will be able to switch back to the
    inline mode using the method switchInlineQuery inside the Web App.
    """

    start_parameter: Optional[str] = None
    """Optional. Deep-linking parameter for the /start message sent to the.

    bot when a user presses the button. 1-64 characters, only A-Z, a-z,
    0-9, _ and - are allowed.Example: An inline bot that sends YouTube
    videos can ask the user to connect the bot to their YouTube account to
    adapt search results accordingly. To do this, it displays a 'Connect
    your YouTube account' button above the results, or even before showing
    any. The user presses the button, switches to a private chat with the
    bot and, in doing so, passes a start parameter that instructs the bot
    to return an OAuth link. Once done, the bot can offer a switch_inline
    button so that the user can easily return to the chat where they
    wanted to use the bot's inline capabilities.
    """


class InlineQueryResultArticle(BaseModel):
    """Represents a link to an article or web page."""

    type: str
    """Type of the result, must be article."""

    id: str
    """Unique identifier for this result, 1-64 Bytes."""

    title: str
    """Title of the result."""

    input_message_content: "InputMessageContent"
    """Content of the message to be sent."""

    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """Optional.

    Inline keyboard attached to the message
    """

    url: Optional[str] = None
    """Optional.

    URL of the result
    """

    hide_url: Optional[bool] = None
    """Optional.

    Pass True if you don't want the URL to be shown in the message
    """

    description: Optional[str] = None
    """Optional.

    Short description of the result
    """

    thumbnail_url: Optional[str] = None
    """Optional.

    Url of the thumbnail for the result
    """

    thumbnail_width: Optional[int] = None
    """Optional.

    Thumbnail width
    """

    thumbnail_height: Optional[int] = None
    """Optional.

    Thumbnail height
    """


class InlineQueryResultPhoto(BaseModel):
    """Represents a link to a photo.

    By default, this photo will be sent by the user with optional
    caption. Alternatively, you can use input_message_content to send a
    message with the specified content instead of the photo.
    """

    type: str
    """Type of the result, must be photo."""

    id: str
    """Unique identifier for this result, 1-64 bytes."""

    photo_url: str
    """A valid URL of the photo.

    Photo must be in JPEG format. Photo size must not exceed 5MB
    """

    thumbnail_url: str
    """URL of the thumbnail for the photo."""

    photo_width: Optional[int] = None
    """Optional.

    Width of the photo
    """

    photo_height: Optional[int] = None
    """Optional.

    Height of the photo
    """

    title: Optional[str] = None
    """Optional.

    Title for the result
    """

    description: Optional[str] = None
    """Optional.

    Short description of the result
    """

    caption: Optional[str] = None
    """Optional.

    Caption of the photo to be sent, 0-1024 characters after entities
    parsing
    """

    parse_mode: Optional[str] = None
    """Optional.

    Mode for parsing entities in the photo caption. See formatting
    options for more details.
    """

    caption_entities: Optional[List["MessageEntity"]] = None
    """Optional.

    List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    """

    show_caption_above_media: Optional[bool] = None
    """Optional.

    Pass True, if the caption must be shown above the message media
    """

    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """Optional.

    Inline keyboard attached to the message
    """

    input_message_content: Optional["InputMessageContent"] = None
    """Optional.

    Content of the message to be sent instead of the photo
    """


class InlineQueryResultGif(BaseModel):
    """Represents a link to an animated GIF file.

    By default, this animated GIF file will be sent by the user with
    optional caption. Alternatively, you can use input_message_content
    to send a message with the specified content instead of the
    animation.
    """

    type: str
    """Type of the result, must be gif."""

    id: str
    """Unique identifier for this result, 1-64 bytes."""

    gif_url: str
    """A valid URL for the GIF file.

    File size must not exceed 1MB
    """

    thumbnail_url: str
    """URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the
    result."""

    gif_width: Optional[int] = None
    """Optional.

    Width of the GIF
    """

    gif_height: Optional[int] = None
    """Optional.

    Height of the GIF
    """

    gif_duration: Optional[int] = None
    """Optional.

    Duration of the GIF in seconds
    """

    thumbnail_mime_type: Optional[str] = None
    """Optional.

    MIME type of the thumbnail, must be one of “image/jpeg”,
    “image/gif”, or “video/mp4”. Defaults to “image/jpeg”
    """

    title: Optional[str] = None
    """Optional.

    Title for the result
    """

    caption: Optional[str] = None
    """Optional.

    Caption of the GIF file to be sent, 0-1024 characters after entities
    parsing
    """

    parse_mode: Optional[str] = None
    """Optional.

    Mode for parsing entities in the caption. See formatting options for
    more details.
    """

    caption_entities: Optional[List["MessageEntity"]] = None
    """Optional.

    List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    """

    show_caption_above_media: Optional[bool] = None
    """Optional.

    Pass True, if the caption must be shown above the message media
    """

    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """Optional.

    Inline keyboard attached to the message
    """

    input_message_content: Optional["InputMessageContent"] = None
    """Optional.

    Content of the message to be sent instead of the GIF animation
    """


class InlineQueryResultMpeg4Gif(BaseModel):
    """Represents a link to a video animation (H.264/MPEG-4 AVC video without
    sound).

    By default, this animated MPEG-4 file will be sent by the user with
    optional caption. Alternatively, you can use input_message_content
    to send a message with the specified content instead of the
    animation.
    """

    type: str
    """Type of the result, must be mpeg4_gif."""

    id: str
    """Unique identifier for this result, 1-64 bytes."""

    mpeg4_url: str
    """A valid URL for the MPEG4 file.

    File size must not exceed 1MB
    """

    thumbnail_url: str
    """URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the
    result."""

    mpeg4_width: Optional[int] = None
    """Optional.

    Video width
    """

    mpeg4_height: Optional[int] = None
    """Optional.

    Video height
    """

    mpeg4_duration: Optional[int] = None
    """Optional.

    Video duration in seconds
    """

    thumbnail_mime_type: Optional[str] = None
    """Optional.

    MIME type of the thumbnail, must be one of “image/jpeg”,
    “image/gif”, or “video/mp4”. Defaults to “image/jpeg”
    """

    title: Optional[str] = None
    """Optional.

    Title for the result
    """

    caption: Optional[str] = None
    """Optional.

    Caption of the MPEG-4 file to be sent, 0-1024 characters after
    entities parsing
    """

    parse_mode: Optional[str] = None
    """Optional.

    Mode for parsing entities in the caption. See formatting options for
    more details.
    """

    caption_entities: Optional[List["MessageEntity"]] = None
    """Optional.

    List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    """

    show_caption_above_media: Optional[bool] = None
    """Optional.

    Pass True, if the caption must be shown above the message media
    """

    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """Optional.

    Inline keyboard attached to the message
    """

    input_message_content: Optional["InputMessageContent"] = None
    """Optional.

    Content of the message to be sent instead of the video animation
    """


class InlineQueryResultVideo(BaseModel):
    """Represents a link to a page containing an embedded video player or a
    video file.

    By default, this video file will be sent by the user with an
    optional caption. Alternatively, you can use input_message_content
    to send a message with the specified content instead of the video.
    """

    type: str
    """Type of the result, must be video."""

    id: str
    """Unique identifier for this result, 1-64 bytes."""

    video_url: str
    """A valid URL for the embedded video player or video file."""

    mime_type: str
    """MIME type of the content of the video URL, “text/html” or “video/mp4”"""

    thumbnail_url: str
    """URL of the thumbnail (JPEG only) for the video."""

    title: str
    """Title for the result."""

    caption: Optional[str] = None
    """Optional.

    Caption of the video to be sent, 0-1024 characters after entities
    parsing
    """

    parse_mode: Optional[str] = None
    """Optional.

    Mode for parsing entities in the video caption. See formatting
    options for more details.
    """

    caption_entities: Optional[List["MessageEntity"]] = None
    """Optional.

    List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    """

    show_caption_above_media: Optional[bool] = None
    """Optional.

    Pass True, if the caption must be shown above the message media
    """

    video_width: Optional[int] = None
    """Optional.

    Video width
    """

    video_height: Optional[int] = None
    """Optional.

    Video height
    """

    video_duration: Optional[int] = None
    """Optional.

    Video duration in seconds
    """

    description: Optional[str] = None
    """Optional.

    Short description of the result
    """

    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """Optional.

    Inline keyboard attached to the message
    """

    input_message_content: Optional["InputMessageContent"] = None
    """Optional.

    Content of the message to be sent instead of the video. This field
    is required if InlineQueryResultVideo is used to send an HTML- page
    as a result (e.g., a YouTube video).
    """


class InlineQueryResultAudio(BaseModel):
    """Represents a link to an MP3 audio file.

    By default, this audio file will be sent by the user. Alternatively,
    you can use input_message_content to send a message with the
    specified content instead of the audio.
    """

    type: str
    """Type of the result, must be audio."""

    id: str
    """Unique identifier for this result, 1-64 bytes."""

    audio_url: str
    """A valid URL for the audio file."""

    title: str
    """Title."""

    caption: Optional[str] = None
    """Optional.

    Caption, 0-1024 characters after entities parsing
    """

    parse_mode: Optional[str] = None
    """Optional.

    Mode for parsing entities in the audio caption. See formatting
    options for more details.
    """

    caption_entities: Optional[List["MessageEntity"]] = None
    """Optional.

    List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    """

    performer: Optional[str] = None
    """Optional.

    Performer
    """

    audio_duration: Optional[int] = None
    """Optional.

    Audio duration in seconds
    """

    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """Optional.

    Inline keyboard attached to the message
    """

    input_message_content: Optional["InputMessageContent"] = None
    """Optional.

    Content of the message to be sent instead of the audio
    """


class InlineQueryResultVoice(BaseModel):
    """Represents a link to a voice recording in an .OGG container encoded with
    OPUS.

    By default, this voice recording will be sent by the user.
    Alternatively, you can use input_message_content to send a message
    with the specified content instead of the the voice message.
    """

    type: str
    """Type of the result, must be voice."""

    id: str
    """Unique identifier for this result, 1-64 bytes."""

    voice_url: str
    """A valid URL for the voice recording."""

    title: str
    """Recording title."""

    caption: Optional[str] = None
    """Optional.

    Caption, 0-1024 characters after entities parsing
    """

    parse_mode: Optional[str] = None
    """Optional.

    Mode for parsing entities in the voice message caption. See
    formatting options for more details.
    """

    caption_entities: Optional[List["MessageEntity"]] = None
    """Optional.

    List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    """

    voice_duration: Optional[int] = None
    """Optional.

    Recording duration in seconds
    """

    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """Optional.

    Inline keyboard attached to the message
    """

    input_message_content: Optional["InputMessageContent"] = None
    """Optional.

    Content of the message to be sent instead of the voice recording
    """


class InlineQueryResultDocument(BaseModel):
    """Represents a link to a file.

    By default, this file will be sent by the user with an optional
    caption. Alternatively, you can use input_message_content to send a
    message with the specified content instead of the file. Currently,
    only .PDF and .ZIP files can be sent using this method.
    """

    type: str
    """Type of the result, must be document."""

    id: str
    """Unique identifier for this result, 1-64 bytes."""

    title: str
    """Title for the result."""

    document_url: str
    """A valid URL for the file."""

    mime_type: str
    """MIME type of the content of the file, either “application/pdf” or
    “application/zip”"""

    caption: Optional[str] = None
    """Optional.

    Caption of the document to be sent, 0-1024 characters after entities
    parsing
    """

    parse_mode: Optional[str] = None
    """Optional.

    Mode for parsing entities in the document caption. See formatting
    options for more details.
    """

    caption_entities: Optional[List["MessageEntity"]] = None
    """Optional.

    List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    """

    description: Optional[str] = None
    """Optional.

    Short description of the result
    """

    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """Optional.

    Inline keyboard attached to the message
    """

    input_message_content: Optional["InputMessageContent"] = None
    """Optional.

    Content of the message to be sent instead of the file
    """

    thumbnail_url: Optional[str] = None
    """Optional.

    URL of the thumbnail (JPEG only) for the file
    """

    thumbnail_width: Optional[int] = None
    """Optional.

    Thumbnail width
    """

    thumbnail_height: Optional[int] = None
    """Optional.

    Thumbnail height
    """


class InlineQueryResultLocation(BaseModel):
    """Represents a location on a map.

    By default, the location will be sent by the user. Alternatively,
    you can use input_message_content to send a message with the
    specified content instead of the location.
    """

    type: str
    """Type of the result, must be location."""

    id: str
    """Unique identifier for this result, 1-64 Bytes."""

    latitude: float
    """Location latitude in degrees."""

    longitude: float
    """Location longitude in degrees."""

    title: str
    """Location title."""

    horizontal_accuracy: Optional[float] = None
    """Optional.

    The radius of uncertainty for the location, measured in meters;
    0-1500
    """

    live_period: Optional[int] = None
    """Optional.

    Period in seconds during which the location can be updated, should
    be between 60 and 86400, or 0x7FFFFFFF for live locations that can
    be edited indefinitely.
    """

    heading: Optional[int] = None
    """Optional.

    For live locations, a direction in which the user is moving, in
    degrees. Must be between 1 and 360 if specified.
    """

    proximity_alert_radius: Optional[int] = None
    """Optional.

    For live locations, a maximum distance for proximity alerts about
    approaching another chat member, in meters. Must be between 1 and
    100000 if specified.
    """

    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """Optional.

    Inline keyboard attached to the message
    """

    input_message_content: Optional["InputMessageContent"] = None
    """Optional.

    Content of the message to be sent instead of the location
    """

    thumbnail_url: Optional[str] = None
    """Optional.

    Url of the thumbnail for the result
    """

    thumbnail_width: Optional[int] = None
    """Optional.

    Thumbnail width
    """

    thumbnail_height: Optional[int] = None
    """Optional.

    Thumbnail height
    """


class InlineQueryResultVenue(BaseModel):
    """Represents a venue.

    By default, the venue will be sent by the user. Alternatively, you
    can use input_message_content to send a message with the specified
    content instead of the venue.
    """

    type: str
    """Type of the result, must be venue."""

    id: str
    """Unique identifier for this result, 1-64 Bytes."""

    latitude: float
    """Latitude of the venue location in degrees."""

    longitude: float
    """Longitude of the venue location in degrees."""

    title: str
    """Title of the venue."""

    address: str
    """Address of the venue."""

    foursquare_id: Optional[str] = None
    """Optional.

    Foursquare identifier of the venue if known
    """

    foursquare_type: Optional[str] = None
    """Optional.

    Foursquare type of the venue, if known. (For example,
    “arts_entertainment/default”, “arts_entertainment/aquarium” or
    “food/icecream”.)
    """

    google_place_id: Optional[str] = None
    """Optional.

    Google Places identifier of the venue
    """

    google_place_type: Optional[str] = None
    """Optional.

    Google Places type of the venue. (See supported types.)
    """

    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """Optional.

    Inline keyboard attached to the message
    """

    input_message_content: Optional["InputMessageContent"] = None
    """Optional.

    Content of the message to be sent instead of the venue
    """

    thumbnail_url: Optional[str] = None
    """Optional.

    Url of the thumbnail for the result
    """

    thumbnail_width: Optional[int] = None
    """Optional.

    Thumbnail width
    """

    thumbnail_height: Optional[int] = None
    """Optional.

    Thumbnail height
    """


class InlineQueryResultContact(BaseModel):
    """Represents a contact with a phone number.

    By default, this contact will be sent by the user. Alternatively,
    you can use input_message_content to send a message with the
    specified content instead of the contact.
    """

    type: str
    """Type of the result, must be contact."""

    id: str
    """Unique identifier for this result, 1-64 Bytes."""

    phone_number: str
    """Contact's phone number."""

    first_name: str
    """Contact's first name."""

    last_name: Optional[str] = None
    """Optional.

    Contact's last name
    """

    vcard: Optional[str] = None
    """Optional.

    Additional data about the contact in the form of a vCard, 0-2048
    bytes
    """

    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """Optional.

    Inline keyboard attached to the message
    """

    input_message_content: Optional["InputMessageContent"] = None
    """Optional.

    Content of the message to be sent instead of the contact
    """

    thumbnail_url: Optional[str] = None
    """Optional.

    Url of the thumbnail for the result
    """

    thumbnail_width: Optional[int] = None
    """Optional.

    Thumbnail width
    """

    thumbnail_height: Optional[int] = None
    """Optional.

    Thumbnail height
    """


class InlineQueryResultGame(BaseModel):
    """Represents a Game."""

    type: str
    """Type of the result, must be game."""

    id: str
    """Unique identifier for this result, 1-64 bytes."""

    game_short_name: str
    """Short name of the game."""

    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """Optional.

    Inline keyboard attached to the message
    """


class InlineQueryResultCachedPhoto(BaseModel):
    """Represents a link to a photo stored on the Telegram servers.

    By default, this photo will be sent by the user with an optional
    caption. Alternatively, you can use input_message_content to send a
    message with the specified content instead of the photo.
    """

    type: str
    """Type of the result, must be photo."""

    id: str
    """Unique identifier for this result, 1-64 bytes."""

    photo_file_id: str
    """A valid file identifier of the photo."""

    title: Optional[str] = None
    """Optional.

    Title for the result
    """

    description: Optional[str] = None
    """Optional.

    Short description of the result
    """

    caption: Optional[str] = None
    """Optional.

    Caption of the photo to be sent, 0-1024 characters after entities
    parsing
    """

    parse_mode: Optional[str] = None
    """Optional.

    Mode for parsing entities in the photo caption. See formatting
    options for more details.
    """

    caption_entities: Optional[List["MessageEntity"]] = None
    """Optional.

    List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    """

    show_caption_above_media: Optional[bool] = None
    """Optional.

    Pass True, if the caption must be shown above the message media
    """

    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """Optional.

    Inline keyboard attached to the message
    """

    input_message_content: Optional["InputMessageContent"] = None
    """Optional.

    Content of the message to be sent instead of the photo
    """


class InlineQueryResultCachedGif(BaseModel):
    """Represents a link to an animated GIF file stored on the Telegram
    servers.

    By default, this animated GIF file will be sent by the user with an
    optional caption. Alternatively, you can use input_message_content
    to send a message with specified content instead of the animation.
    """

    type: str
    """Type of the result, must be gif."""

    id: str
    """Unique identifier for this result, 1-64 bytes."""

    gif_file_id: str
    """A valid file identifier for the GIF file."""

    title: Optional[str] = None
    """Optional.

    Title for the result
    """

    caption: Optional[str] = None
    """Optional.

    Caption of the GIF file to be sent, 0-1024 characters after entities
    parsing
    """

    parse_mode: Optional[str] = None
    """Optional.

    Mode for parsing entities in the caption. See formatting options for
    more details.
    """

    caption_entities: Optional[List["MessageEntity"]] = None
    """Optional.

    List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    """

    show_caption_above_media: Optional[bool] = None
    """Optional.

    Pass True, if the caption must be shown above the message media
    """

    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """Optional.

    Inline keyboard attached to the message
    """

    input_message_content: Optional["InputMessageContent"] = None
    """Optional.

    Content of the message to be sent instead of the GIF animation
    """


class InlineQueryResultCachedMpeg4Gif(BaseModel):
    """Represents a link to a video animation (H.264/MPEG-4 AVC video without
    sound) stored on the Telegram servers.

    By default, this animated MPEG-4 file will be sent by the user with
    an optional caption. Alternatively, you can use
    input_message_content to send a message with the specified content
    instead of the animation.
    """

    type: str
    """Type of the result, must be mpeg4_gif."""

    id: str
    """Unique identifier for this result, 1-64 bytes."""

    mpeg4_file_id: str
    """A valid file identifier for the MPEG4 file."""

    title: Optional[str] = None
    """Optional.

    Title for the result
    """

    caption: Optional[str] = None
    """Optional.

    Caption of the MPEG-4 file to be sent, 0-1024 characters after
    entities parsing
    """

    parse_mode: Optional[str] = None
    """Optional.

    Mode for parsing entities in the caption. See formatting options for
    more details.
    """

    caption_entities: Optional[List["MessageEntity"]] = None
    """Optional.

    List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    """

    show_caption_above_media: Optional[bool] = None
    """Optional.

    Pass True, if the caption must be shown above the message media
    """

    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """Optional.

    Inline keyboard attached to the message
    """

    input_message_content: Optional["InputMessageContent"] = None
    """Optional.

    Content of the message to be sent instead of the video animation
    """


class InlineQueryResultCachedSticker(BaseModel):
    """Represents a link to a sticker stored on the Telegram servers.

    By default, this sticker will be sent by the user. Alternatively,
    you can use input_message_content to send a message with the
    specified content instead of the sticker.
    """

    type: str
    """Type of the result, must be sticker."""

    id: str
    """Unique identifier for this result, 1-64 bytes."""

    sticker_file_id: str
    """A valid file identifier of the sticker."""

    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """Optional.

    Inline keyboard attached to the message
    """

    input_message_content: Optional["InputMessageContent"] = None
    """Optional.

    Content of the message to be sent instead of the sticker
    """


class InlineQueryResultCachedDocument(BaseModel):
    """Represents a link to a file stored on the Telegram servers.

    By default, this file will be sent by the user with an optional
    caption. Alternatively, you can use input_message_content to send a
    message with the specified content instead of the file.
    """

    type: str
    """Type of the result, must be document."""

    id: str
    """Unique identifier for this result, 1-64 bytes."""

    title: str
    """Title for the result."""

    document_file_id: str
    """A valid file identifier for the file."""

    description: Optional[str] = None
    """Optional.

    Short description of the result
    """

    caption: Optional[str] = None
    """Optional.

    Caption of the document to be sent, 0-1024 characters after entities
    parsing
    """

    parse_mode: Optional[str] = None
    """Optional.

    Mode for parsing entities in the document caption. See formatting
    options for more details.
    """

    caption_entities: Optional[List["MessageEntity"]] = None
    """Optional.

    List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    """

    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """Optional.

    Inline keyboard attached to the message
    """

    input_message_content: Optional["InputMessageContent"] = None
    """Optional.

    Content of the message to be sent instead of the file
    """


class InlineQueryResultCachedVideo(BaseModel):
    """Represents a link to a video file stored on the Telegram servers.

    By default, this video file will be sent by the user with an
    optional caption. Alternatively, you can use input_message_content
    to send a message with the specified content instead of the video.
    """

    type: str
    """Type of the result, must be video."""

    id: str
    """Unique identifier for this result, 1-64 bytes."""

    video_file_id: str
    """A valid file identifier for the video file."""

    title: str
    """Title for the result."""

    description: Optional[str] = None
    """Optional.

    Short description of the result
    """

    caption: Optional[str] = None
    """Optional.

    Caption of the video to be sent, 0-1024 characters after entities
    parsing
    """

    parse_mode: Optional[str] = None
    """Optional.

    Mode for parsing entities in the video caption. See formatting
    options for more details.
    """

    caption_entities: Optional[List["MessageEntity"]] = None
    """Optional.

    List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    """

    show_caption_above_media: Optional[bool] = None
    """Optional.

    Pass True, if the caption must be shown above the message media
    """

    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """Optional.

    Inline keyboard attached to the message
    """

    input_message_content: Optional["InputMessageContent"] = None
    """Optional.

    Content of the message to be sent instead of the video
    """


class InlineQueryResultCachedVoice(BaseModel):
    """Represents a link to a voice message stored on the Telegram servers.

    By default, this voice message will be sent by the user.
    Alternatively, you can use input_message_content to send a message
    with the specified content instead of the voice message.
    """

    type: str
    """Type of the result, must be voice."""

    id: str
    """Unique identifier for this result, 1-64 bytes."""

    voice_file_id: str
    """A valid file identifier for the voice message."""

    title: str
    """Voice message title."""

    caption: Optional[str] = None
    """Optional.

    Caption, 0-1024 characters after entities parsing
    """

    parse_mode: Optional[str] = None
    """Optional.

    Mode for parsing entities in the voice message caption. See
    formatting options for more details.
    """

    caption_entities: Optional[List["MessageEntity"]] = None
    """Optional.

    List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    """

    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """Optional.

    Inline keyboard attached to the message
    """

    input_message_content: Optional["InputMessageContent"] = None
    """Optional.

    Content of the message to be sent instead of the voice message
    """


class InlineQueryResultCachedAudio(BaseModel):
    """Represents a link to an MP3 audio file stored on the Telegram servers.

    By default, this audio file will be sent by the user. Alternatively,
    you can use input_message_content to send a message with the
    specified content instead of the audio.
    """

    type: str
    """Type of the result, must be audio."""

    id: str
    """Unique identifier for this result, 1-64 bytes."""

    audio_file_id: str
    """A valid file identifier for the audio file."""

    caption: Optional[str] = None
    """Optional.

    Caption, 0-1024 characters after entities parsing
    """

    parse_mode: Optional[str] = None
    """Optional.

    Mode for parsing entities in the audio caption. See formatting
    options for more details.
    """

    caption_entities: Optional[List["MessageEntity"]] = None
    """Optional.

    List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    """

    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """Optional.

    Inline keyboard attached to the message
    """

    input_message_content: Optional["InputMessageContent"] = None
    """Optional.

    Content of the message to be sent instead of the audio
    """


class InputTextMessageContent(BaseModel):
    """Represents the content of a text message to be sent as the result of an
    inline query."""

    message_text: str
    """Text of the message to be sent, 1-4096 characters."""

    parse_mode: Optional[str] = None
    """Optional.

    Mode for parsing entities in the message text. See formatting
    options for more details.
    """

    entities: Optional[List["MessageEntity"]] = None
    """Optional.

    List of special entities that appear in message text, which can be
    specified instead of parse_mode
    """

    link_preview_options: Optional["LinkPreviewOptions"] = None
    """Optional.

    Link preview generation options for the message
    """


class InputLocationMessageContent(BaseModel):
    """Represents the content of a location message to be sent as the result of
    an inline query."""

    latitude: float
    """Latitude of the location in degrees."""

    longitude: float
    """Longitude of the location in degrees."""

    horizontal_accuracy: Optional[float] = None
    """Optional.

    The radius of uncertainty for the location, measured in meters;
    0-1500
    """

    live_period: Optional[int] = None
    """Optional.

    Period in seconds during which the location can be updated, should
    be between 60 and 86400, or 0x7FFFFFFF for live locations that can
    be edited indefinitely.
    """

    heading: Optional[int] = None
    """Optional.

    For live locations, a direction in which the user is moving, in
    degrees. Must be between 1 and 360 if specified.
    """

    proximity_alert_radius: Optional[int] = None
    """Optional.

    For live locations, a maximum distance for proximity alerts about
    approaching another chat member, in meters. Must be between 1 and
    100000 if specified.
    """


class InputVenueMessageContent(BaseModel):
    """Represents the content of a venue message to be sent as the result of an
    inline query."""

    latitude: float
    """Latitude of the venue in degrees."""

    longitude: float
    """Longitude of the venue in degrees."""

    title: str
    """Name of the venue."""

    address: str
    """Address of the venue."""

    foursquare_id: Optional[str] = None
    """Optional.

    Foursquare identifier of the venue, if known
    """

    foursquare_type: Optional[str] = None
    """Optional.

    Foursquare type of the venue, if known. (For example,
    “arts_entertainment/default”, “arts_entertainment/aquarium” or
    “food/icecream”.)
    """

    google_place_id: Optional[str] = None
    """Optional.

    Google Places identifier of the venue
    """

    google_place_type: Optional[str] = None
    """Optional.

    Google Places type of the venue. (See supported types.)
    """


class InputContactMessageContent(BaseModel):
    """Represents the content of a contact message to be sent as the result of
    an inline query."""

    phone_number: str
    """Contact's phone number."""

    first_name: str
    """Contact's first name."""

    last_name: Optional[str] = None
    """Optional.

    Contact's last name
    """

    vcard: Optional[str] = None
    """Optional.

    Additional data about the contact in the form of a vCard, 0-2048
    bytes
    """


class InputInvoiceMessageContent(BaseModel):
    """Represents the content of an invoice message to be sent as the result of
    an inline query."""

    title: str
    """Product name, 1-32 characters."""

    description: str
    """Product description, 1-255 characters."""

    payload: str
    """Bot-defined invoice payload, 1-128 bytes.

    This will not be displayed to the user, use for your internal
    processes.
    """

    currency: str
    """Three-letter ISO 4217 currency code, see more on currencies.

    Pass “XTR” for payments in Telegram Stars.
    """

    prices: List["LabeledPrice"]
    """Price breakdown, a JSON-serialized list of components (e.g. product
    price, tax, discount, delivery cost, delivery tax, bonus, etc.).

    Must contain exactly one item for payments in Telegram Stars.
    """

    provider_token: Optional[str] = None
    """Optional.

    Payment provider token, obtained via @BotFather. Pass an empty
    string for payments in Telegram Stars.
    """

    max_tip_amount: Optional[int] = None
    """Optional.

    The maximum accepted amount for tips in the smallest units of the
    currency (integer, not float/double). For example, for a maximum tip
    of US$ 1.45 pass max_tip_amount = 145. See the exp parameter in
    currencies.json, it shows the number of digits past the decimal
    point for each currency (2 for the majority of currencies). Defaults
    to 0. Not supported for payments in Telegram Stars.
    """

    suggested_tip_amounts: Optional[List[int]] = None
    """Optional.

    A JSON-serialized array of suggested amounts of tip in the smallest
    units of the currency (integer, not float/double). At most 4
    suggested tip amounts can be specified. The suggested tip amounts
    must be positive, passed in a strictly increased order and must not
    exceed max_tip_amount.
    """

    provider_data: Optional[str] = None
    """Optional.

    A JSON-serialized object for data about the invoice, which will be
    shared with the payment provider. A detailed description of the
    required fields should be provided by the payment provider.
    """

    photo_url: Optional[str] = None
    """Optional.

    URL of the product photo for the invoice. Can be a photo of the
    goods or a marketing image for a service.
    """

    photo_size: Optional[int] = None
    """Optional.

    Photo size in bytes
    """

    photo_width: Optional[int] = None
    """Optional.

    Photo width
    """

    photo_height: Optional[int] = None
    """Optional.

    Photo height
    """

    need_name: Optional[bool] = None
    """Optional.

    Pass True if you require the user's full name to complete the order.
    Ignored for payments in Telegram Stars.
    """

    need_phone_number: Optional[bool] = None
    """Optional.

    Pass True if you require the user's phone number to complete the
    order. Ignored for payments in Telegram Stars.
    """

    need_email: Optional[bool] = None
    """Optional.

    Pass True if you require the user's email address to complete the
    order. Ignored for payments in Telegram Stars.
    """

    need_shipping_address: Optional[bool] = None
    """Optional.

    Pass True if you require the user's shipping address to complete the
    order. Ignored for payments in Telegram Stars.
    """

    send_phone_number_to_provider: Optional[bool] = None
    """Optional.

    Pass True if the user's phone number should be sent to the provider.
    Ignored for payments in Telegram Stars.
    """

    send_email_to_provider: Optional[bool] = None
    """Optional.

    Pass True if the user's email address should be sent to the
    provider. Ignored for payments in Telegram Stars.
    """

    is_flexible: Optional[bool] = None
    """Optional.

    Pass True if the final price depends on the shipping method. Ignored
    for payments in Telegram Stars.
    """


class ChosenInlineResult(BaseModel):
    """Represents a result of an inline query that was chosen by the user and
    sent to their chat partner."""

    result_id: str
    """The unique identifier for the result that was chosen."""

    from_: "User" = Field(alias="from")
    """The user that chose the result."""

    query: str
    """The query that was used to obtain the result."""

    location: Optional["Location"] = None
    """Optional.

    Sender location, only for bots that require user location
    """

    inline_message_id: Optional[str] = None
    """Optional.

    Identifier of the sent inline message. Available only if there is an
    inline keyboard attached to the message. Will be also received in
    callback queries and can be used to edit the message.
    """


class SentWebAppMessage(BaseModel):
    """Describes an inline message sent by a Web App on behalf of a user."""

    inline_message_id: Optional[str] = None
    """Optional.

    Identifier of the sent inline message. Available only if there is an
    inline keyboard attached to the message.
    """


class LabeledPrice(BaseModel):
    """This object represents a portion of the price for goods or services."""

    label: str
    """Portion label."""

    amount: int
    """Price of the product in the smallest units of the currency (integer, not
    float/double).

    For example, for a price of US$ 1.45 pass amount = 145. See the exp
    parameter in currencies.json, it shows the number of digits past the
    decimal point for each currency (2 for the majority of currencies).
    """


class Invoice(BaseModel):
    """This object contains basic information about an invoice."""

    title: str
    """Product name."""

    description: str
    """Product description."""

    start_parameter: str
    """Unique bot deep-linking parameter that can be used to generate this
    invoice."""

    currency: str
    """Three-letter ISO 4217 currency code, or “XTR” for payments in Telegram
    Stars."""

    total_amount: int
    """Total price in the smallest units of the currency (integer, not
    float/double).

    For example, for a price of US$ 1.45 pass amount = 145. See the exp
    parameter in currencies.json, it shows the number of digits past the
    decimal point for each currency (2 for the majority of currencies).
    """


class ShippingAddress(BaseModel):
    """This object represents a shipping address."""

    country_code: str
    """Two-letter ISO 3166-1 alpha-2 country code."""

    state: str
    """State, if applicable."""

    city: str
    """City."""

    street_line1: str
    """First line for the address."""

    street_line2: str
    """Second line for the address."""

    post_code: str
    """Address post code."""


class OrderInfo(BaseModel):
    """This object represents information about an order."""

    name: Optional[str] = None
    """Optional.

    User name
    """

    phone_number: Optional[str] = None
    """Optional.

    User's phone number
    """

    email: Optional[str] = None
    """Optional.

    User email
    """

    shipping_address: Optional["ShippingAddress"] = None
    """Optional.

    User shipping address
    """


class ShippingOption(BaseModel):
    """This object represents one shipping option."""

    id: str
    """Shipping option identifier."""

    title: str
    """Option title."""

    prices: List["LabeledPrice"]
    """List of price portions."""


class SuccessfulPayment(BaseModel):
    """This object contains basic information about a successful payment."""

    currency: str
    """Three-letter ISO 4217 currency code, or “XTR” for payments in Telegram
    Stars."""

    total_amount: int
    """Total price in the smallest units of the currency (integer, not
    float/double).

    For example, for a price of US$ 1.45 pass amount = 145. See the exp
    parameter in currencies.json, it shows the number of digits past the
    decimal point for each currency (2 for the majority of currencies).
    """

    invoice_payload: str
    """Bot-specified invoice payload."""

    telegram_payment_charge_id: str
    """Telegram payment identifier."""

    provider_payment_charge_id: str
    """Provider payment identifier."""

    shipping_option_id: Optional[str] = None
    """Optional.

    Identifier of the shipping option chosen by the user
    """

    order_info: Optional["OrderInfo"] = None
    """Optional.

    Order information provided by the user
    """


class ShippingQuery(BaseModel):
    """This object contains information about an incoming shipping query."""

    id: str
    """Unique query identifier."""

    from_: "User" = Field(alias="from")
    """User who sent the query."""

    invoice_payload: str
    """Bot-specified invoice payload."""

    shipping_address: "ShippingAddress"
    """User specified shipping address."""


class PreCheckoutQuery(BaseModel):
    """This object contains information about an incoming pre-checkout
    query."""

    id: str
    """Unique query identifier."""

    from_: "User" = Field(None, alias="from")
    """User who sent the query."""

    currency: str
    """Three-letter ISO 4217 currency code, or “XTR” for payments in Telegram
    Stars."""

    total_amount: int
    """Total price in the smallest units of the currency (integer, not
    float/double).

    For example, for a price of US$ 1.45 pass amount = 145. See the exp
    parameter in currencies.json, it shows the number of digits past the
    decimal point for each currency (2 for the majority of currencies).
    """

    invoice_payload: str
    """Bot-specified invoice payload."""

    shipping_option_id: Optional[str] = None
    """Optional.

    Identifier of the shipping option chosen by the user
    """

    order_info: Optional["OrderInfo"] = None
    """Optional.

    Order information provided by the user
    """


class RevenueWithdrawalStatePending(BaseModel):
    """The withdrawal is in progress."""

    type: str
    """Type of the state, always “pending”"""


class RevenueWithdrawalStateSucceeded(BaseModel):
    """The withdrawal succeeded."""

    type: str
    """Type of the state, always “succeeded”"""

    date: int
    """Date the withdrawal was completed in Unix time."""

    url: str
    """An HTTPS URL that can be used to see transaction details."""


class RevenueWithdrawalStateFailed(BaseModel):
    """The withdrawal failed and the transaction was refunded."""

    type: str
    """Type of the state, always “failed”"""


class TransactionPartnerUser(BaseModel):
    """Describes a transaction with a user."""

    type: str
    """Type of the transaction partner, always “user”"""

    user: "User"
    """Information about the user."""

    invoice_payload: Optional[str] = None
    """Optional.

    Bot-specified invoice payload
    """


class TransactionPartnerFragment(BaseModel):
    """Describes a withdrawal transaction with Fragment."""

    type: str
    """Type of the transaction partner, always “fragment”"""

    withdrawal_state: Optional["RevenueWithdrawalState"] = None
    """Optional.

    State of the transaction if the transaction is outgoing
    """


class TransactionPartnerTelegramAds(BaseModel):
    """Describes a withdrawal transaction to the Telegram Ads platform."""

    type: str
    """Type of the transaction partner, always “telegram_ads”"""


class TransactionPartnerOther(BaseModel):
    """Describes a transaction with an unknown source or recipient."""

    type: str
    """Type of the transaction partner, always “other”"""


class StarTransaction(BaseModel):
    """Describes a Telegram Star transaction."""

    id: str
    """Unique identifier of the transaction.

    Coincides with the identifer of the original transaction for refund
    transactions. Coincides with
    SuccessfulPayment.telegram_payment_charge_id for successful incoming
    payments from users.
    """

    amount: int
    """Number of Telegram Stars transferred by the transaction."""

    date: int
    """Date the transaction was created in Unix time."""

    source: Optional["TransactionPartner"] = None
    """Optional.

    Source of an incoming transaction (e.g., a user purchasing goods or
    services, Fragment refunding a failed withdrawal). Only for incoming
    transactions
    """

    receiver: Optional["TransactionPartner"] = None
    """Optional.

    Receiver of an outgoing transaction (e.g., a user for a purchase
    refund, Fragment for a withdrawal). Only for outgoing transactions
    """


class StarTransactions(BaseModel):
    """Contains a list of Telegram Star transactions."""

    transactions: List["StarTransaction"]
    """The list of transactions."""


class PassportData(BaseModel):
    """Describes Telegram Passport data shared with the bot by the user."""

    data: List["EncryptedPassportElement"]
    """Array with information about documents and other Telegram Passport
    elements that was shared with the bot."""

    credentials: "EncryptedCredentials"
    """Encrypted credentials required to decrypt the data."""


class PassportFile(BaseModel):
    """This object represents a file uploaded to Telegram Passport.

    Currently all Telegram Passport files are in JPEG format when
    decrypted and don't exceed 10MB.
    """

    file_id: str
    """Identifier for this file, which can be used to download or reuse the
    file."""

    file_unique_id: str
    """Unique identifier for this file, which is supposed to be the same over
    time and for different bots.

    Can't be used to download or reuse the file.
    """

    file_size: int
    """File size in bytes."""

    file_date: int
    """Unix time when the file was uploaded."""


class EncryptedPassportElement(BaseModel):
    """Describes documents or other Telegram Passport elements shared with the
    bot by the user."""

    type: str
    """Element type.

    One of “personal_details”, “passport”, “driver_license”,
    “identity_card”, “internal_passport”, “address”, “utility_bill”,
    “bank_statement”, “rental_agreement”, “passport_registration”,
    “temporary_registration”, “phone_number”, “email”.
    """

    hash: str
    """Base64-encoded element hash for using in
    PassportElementErrorUnspecified."""

    data: Optional[str] = None
    """Optional.

    Base64-encoded encrypted Telegram Passport element data provided by
    the user; available only for “personal_details”, “passport”,
    “driver_license”, “identity_card”, “internal_passport” and “address”
    types. Can be decrypted and verified using the accompanying
    EncryptedCredentials.
    """

    phone_number: Optional[str] = None
    """Optional.

    User's verified phone number; available only for “phone_number” type
    """

    email: Optional[str] = None
    """Optional.

    User's verified email address; available only for “email” type
    """

    files: Optional[List["PassportFile"]] = None
    """Optional.

    Array of encrypted files with documents provided by the user;
    available only for “utility_bill”, “bank_statement”,
    “rental_agreement”, “passport_registration” and
    “temporary_registration” types. Files can be decrypted and verified
    using the accompanying EncryptedCredentials.
    """

    front_side: Optional["PassportFile"] = None
    """Optional.

    Encrypted file with the front side of the document, provided by the
    user; available only for “passport”, “driver_license”,
    “identity_card” and “internal_passport”. The file can be decrypted
    and verified using the accompanying EncryptedCredentials.
    """

    reverse_side: Optional["PassportFile"] = None
    """Optional.

    Encrypted file with the reverse side of the document, provided by
    the user; available only for “driver_license” and “identity_card”.
    The file can be decrypted and verified using the accompanying
    EncryptedCredentials.
    """

    selfie: Optional["PassportFile"] = None
    """Optional.

    Encrypted file with the selfie of the user holding a document,
    provided by the user; available if requested for “passport”,
    “driver_license”, “identity_card” and “internal_passport”. The file
    can be decrypted and verified using the accompanying
    EncryptedCredentials.
    """

    translation: Optional[List["PassportFile"]] = None
    """Optional.

    Array of encrypted files with translated versions of documents
    provided by the user; available if requested for “passport”,
    “driver_license”, “identity_card”, “internal_passport”,
    “utility_bill”, “bank_statement”, “rental_agreement”,
    “passport_registration” and “temporary_registration” types. Files
    can be decrypted and verified using the accompanying
    EncryptedCredentials.
    """


class EncryptedCredentials(BaseModel):
    """Describes data required for decrypting and authenticating
    EncryptedPassportElement.

    See the Telegram Passport Documentation for a complete description
    of the data decryption and authentication processes.
    """

    data: str
    """Base64-encoded encrypted JSON-serialized data with unique user's
    payload, data hashes and secrets required for EncryptedPassportElement
    decryption and authentication."""

    hash: str
    """Base64-encoded data hash for data authentication."""

    secret: str
    """Base64-encoded secret, encrypted with the bot's public RSA key, required
    for data decryption."""


class PassportElementErrorDataField(BaseModel):
    """Represents an issue in one of the data fields that was provided by the
    user.

    The error is considered resolved when the field's value changes.
    """

    source: str
    """Error source, must be data."""

    type: str
    """The section of the user's Telegram Passport which has the error, one of
    “personal_details”, “passport”, “driver_license”, “identity_card”,
    “internal_passport”, “address”"""

    field_name: str
    """Name of the data field which has the error."""

    data_hash: str
    """Base64-encoded data hash."""

    message: str
    """Error message."""


class PassportElementErrorFrontSide(BaseModel):
    """Represents an issue with the front side of a document.

    The error is considered resolved when the file with the front side
    of the document changes.
    """

    source: str
    """Error source, must be front_side."""

    type: str
    """The section of the user's Telegram Passport which has the issue, one of
    “passport”, “driver_license”, “identity_card”, “internal_passport”"""

    file_hash: str
    """Base64-encoded hash of the file with the front side of the document."""

    message: str
    """Error message."""


class PassportElementErrorReverseSide(BaseModel):
    """Represents an issue with the reverse side of a document.

    The error is considered resolved when the file with reverse side of
    the document changes.
    """

    source: str
    """Error source, must be reverse_side."""

    type: str
    """The section of the user's Telegram Passport which has the issue, one of
    “driver_license”, “identity_card”"""

    file_hash: str
    """Base64-encoded hash of the file with the reverse side of the
    document."""

    message: str
    """Error message."""


class PassportElementErrorSelfie(BaseModel):
    """Represents an issue with the selfie with a document.

    The error is considered resolved when the file with the selfie
    changes.
    """

    source: str
    """Error source, must be selfie."""

    type: str
    """The section of the user's Telegram Passport which has the issue, one of
    “passport”, “driver_license”, “identity_card”, “internal_passport”"""

    file_hash: str
    """Base64-encoded hash of the file with the selfie."""

    message: str
    """Error message."""


class PassportElementErrorFile(BaseModel):
    """Represents an issue with a document scan.

    The error is considered resolved when the file with the document
    scan changes.
    """

    source: str
    """Error source, must be file."""

    type: str
    """The section of the user's Telegram Passport which has the issue, one of
    “utility_bill”, “bank_statement”, “rental_agreement”,
    “passport_registration”, “temporary_registration”"""

    file_hash: str
    """Base64-encoded file hash."""

    message: str
    """Error message."""


class PassportElementErrorFiles(BaseModel):
    """Represents an issue with a list of scans.

    The error is considered resolved when the list of files containing
    the scans changes.
    """

    source: str
    """Error source, must be files."""

    type: str
    """The section of the user's Telegram Passport which has the issue, one of
    “utility_bill”, “bank_statement”, “rental_agreement”,
    “passport_registration”, “temporary_registration”"""

    file_hashes: List[str]
    """List of base64-encoded file hashes."""

    message: str
    """Error message."""


class PassportElementErrorTranslationFile(BaseModel):
    """Represents an issue with one of the files that constitute the
    translation of a document.

    The error is considered resolved when the file changes.
    """

    source: str
    """Error source, must be translation_file."""

    type: str
    """Type of element of the user's Telegram Passport which has the issue, one
    of “passport”, “driver_license”, “identity_card”, “internal_passport”,
    “utility_bill”, “bank_statement”, “rental_agreement”,
    “passport_registration”, “temporary_registration”"""

    file_hash: str
    """Base64-encoded file hash."""

    message: str
    """Error message."""


class PassportElementErrorTranslationFiles(BaseModel):
    """Represents an issue with the translated version of a document.

    The error is considered resolved when a file with the document
    translation change.
    """

    source: str
    """Error source, must be translation_files."""

    type: str
    """Type of element of the user's Telegram Passport which has the issue, one
    of “passport”, “driver_license”, “identity_card”, “internal_passport”,
    “utility_bill”, “bank_statement”, “rental_agreement”,
    “passport_registration”, “temporary_registration”"""

    file_hashes: List[str]
    """List of base64-encoded file hashes."""

    message: str
    """Error message."""


class PassportElementErrorUnspecified(BaseModel):
    """Represents an issue in an unspecified place.

    The error is considered resolved when new data is added.
    """

    source: str
    """Error source, must be unspecified."""

    type: str
    """Type of element of the user's Telegram Passport which has the issue."""

    element_hash: str
    """Base64-encoded element hash."""

    message: str
    """Error message."""


class Game(BaseModel):
    """This object represents a game.

    Use BotFather to create and edit games, their short names will act
    as unique identifiers.
    """

    title: str
    """Title of the game."""

    description: str
    """Description of the game."""

    photo: List["PhotoSize"]
    """Photo that will be displayed in the game message in chats."""

    text: Optional[str] = None
    """Optional.

    Brief description of the game or high scores included in the game
    message. Can be automatically edited to include current high scores
    for the game when the bot calls setGameScore, or manually edited
    using editMessageText. 0-4096 characters.
    """

    text_entities: Optional[List["MessageEntity"]] = None
    """Optional.

    Special entities that appear in text, such as usernames, URLs, bot
    commands, etc.
    """

    animation: Optional["Animation"] = None
    """Optional.

    Animation that will be displayed in the game message in chats.
    Upload via BotFather
    """


class CallbackGame(BaseModel):
    """A placeholder, currently holds no information.

    Use BotFather to set up your game.
    """


class GameHighScore(BaseModel):
    """This object represents one row of the high scores table for a game."""

    position: int
    """Position in high score table for the game."""

    user: "User"
    """User."""

    score: int
    """Score."""


MaybeInaccessibleMessage = Union[
    Message,
    InaccessibleMessage,
]


MessageOrigin = Union[
    MessageOriginUser,
    MessageOriginHiddenUser,
    MessageOriginChat,
    MessageOriginChannel,
]


PaidMedia = Union[
    PaidMediaPreview,
    PaidMediaPhoto,
    PaidMediaVideo,
]


BackgroundFill = Union[
    BackgroundFillSolid,
    BackgroundFillGradient,
    BackgroundFillFreeformGradient,
]


BackgroundType = Union[
    BackgroundTypeFill,
    BackgroundTypeWallpaper,
    BackgroundTypePattern,
    BackgroundTypeChatTheme,
]


ChatMember = Union[
    ChatMemberOwner,
    ChatMemberAdministrator,
    ChatMemberMember,
    ChatMemberRestricted,
    ChatMemberLeft,
    ChatMemberBanned,
]


ReactionType = Union[
    ReactionTypeEmoji,
    ReactionTypeCustomEmoji,
]


BotCommandScope = Union[
    BotCommandScopeDefault,
    BotCommandScopeAllPrivateChats,
    BotCommandScopeAllGroupChats,
    BotCommandScopeAllChatAdministrators,
    BotCommandScopeChat,
    BotCommandScopeChatAdministrators,
    BotCommandScopeChatMember,
]


MenuButton = Union[
    MenuButtonCommands,
    MenuButtonWebApp,
    MenuButtonDefault,
]


ChatBoostSource = Union[
    ChatBoostSourcePremium,
    ChatBoostSourceGiftCode,
    ChatBoostSourceGiveaway,
]


InputMedia = Union[
    InputMediaAnimation,
    InputMediaDocument,
    InputMediaAudio,
    InputMediaPhoto,
    InputMediaVideo,
]


InputPaidMedia = Union[
    InputPaidMediaPhoto,
    InputPaidMediaVideo,
]


InlineQueryResult = Union[
    InlineQueryResultCachedAudio,
    InlineQueryResultCachedDocument,
    InlineQueryResultCachedGif,
    InlineQueryResultCachedMpeg4Gif,
    InlineQueryResultCachedPhoto,
    InlineQueryResultCachedSticker,
    InlineQueryResultCachedVideo,
    InlineQueryResultCachedVoice,
    InlineQueryResultArticle,
    InlineQueryResultAudio,
    InlineQueryResultContact,
    InlineQueryResultGame,
    InlineQueryResultDocument,
    InlineQueryResultGif,
    InlineQueryResultLocation,
    InlineQueryResultMpeg4Gif,
    InlineQueryResultPhoto,
    InlineQueryResultVenue,
    InlineQueryResultVideo,
    InlineQueryResultVoice,
]


InputMessageContent = Union[
    InputTextMessageContent,
    InputLocationMessageContent,
    InputVenueMessageContent,
    InputContactMessageContent,
    InputInvoiceMessageContent,
]


RevenueWithdrawalState = Union[
    RevenueWithdrawalStatePending,
    RevenueWithdrawalStateSucceeded,
    RevenueWithdrawalStateFailed,
]


TransactionPartner = Union[
    TransactionPartnerUser,
    TransactionPartnerFragment,
    TransactionPartnerTelegramAds,
    TransactionPartnerOther,
]


PassportElementError = Union[
    PassportElementErrorDataField,
    PassportElementErrorFrontSide,
    PassportElementErrorReverseSide,
    PassportElementErrorSelfie,
    PassportElementErrorFile,
    PassportElementErrorFiles,
    PassportElementErrorTranslationFile,
    PassportElementErrorTranslationFiles,
    PassportElementErrorUnspecified,
]


InputFile = Any

Update.update_forward_refs()

WebhookInfo.update_forward_refs()

User.update_forward_refs()

Chat.update_forward_refs()

ChatFullInfo.update_forward_refs()

Message.update_forward_refs()

MessageId.update_forward_refs()

InaccessibleMessage.update_forward_refs()

MessageEntity.update_forward_refs()

TextQuote.update_forward_refs()

ExternalReplyInfo.update_forward_refs()

ReplyParameters.update_forward_refs()

MessageOriginUser.update_forward_refs()

MessageOriginHiddenUser.update_forward_refs()

MessageOriginChat.update_forward_refs()

MessageOriginChannel.update_forward_refs()

PhotoSize.update_forward_refs()

Animation.update_forward_refs()

Audio.update_forward_refs()

Document.update_forward_refs()

Story.update_forward_refs()

Video.update_forward_refs()

VideoNote.update_forward_refs()

Voice.update_forward_refs()

PaidMediaInfo.update_forward_refs()

PaidMediaPreview.update_forward_refs()

PaidMediaPhoto.update_forward_refs()

PaidMediaVideo.update_forward_refs()

Contact.update_forward_refs()

Dice.update_forward_refs()

PollOption.update_forward_refs()

InputPollOption.update_forward_refs()

PollAnswer.update_forward_refs()

Poll.update_forward_refs()

Location.update_forward_refs()

Venue.update_forward_refs()

WebAppData.update_forward_refs()

ProximityAlertTriggered.update_forward_refs()

MessageAutoDeleteTimerChanged.update_forward_refs()

ChatBoostAdded.update_forward_refs()

BackgroundFillSolid.update_forward_refs()

BackgroundFillGradient.update_forward_refs()

BackgroundFillFreeformGradient.update_forward_refs()

BackgroundTypeFill.update_forward_refs()

BackgroundTypeWallpaper.update_forward_refs()

BackgroundTypePattern.update_forward_refs()

BackgroundTypeChatTheme.update_forward_refs()

ChatBackground.update_forward_refs()

ForumTopicCreated.update_forward_refs()

ForumTopicClosed.update_forward_refs()

ForumTopicEdited.update_forward_refs()

ForumTopicReopened.update_forward_refs()

GeneralForumTopicHidden.update_forward_refs()

GeneralForumTopicUnhidden.update_forward_refs()

SharedUser.update_forward_refs()

UsersShared.update_forward_refs()

ChatShared.update_forward_refs()

WriteAccessAllowed.update_forward_refs()

VideoChatScheduled.update_forward_refs()

VideoChatStarted.update_forward_refs()

VideoChatEnded.update_forward_refs()

VideoChatParticipantsInvited.update_forward_refs()

GiveawayCreated.update_forward_refs()

Giveaway.update_forward_refs()

GiveawayWinners.update_forward_refs()

GiveawayCompleted.update_forward_refs()

LinkPreviewOptions.update_forward_refs()

UserProfilePhotos.update_forward_refs()

File.update_forward_refs()

WebAppInfo.update_forward_refs()

ReplyKeyboardMarkup.update_forward_refs()

KeyboardButton.update_forward_refs()

KeyboardButtonRequestUsers.update_forward_refs()

KeyboardButtonRequestChat.update_forward_refs()

KeyboardButtonPollType.update_forward_refs()

ReplyKeyboardRemove.update_forward_refs()

InlineKeyboardMarkup.update_forward_refs()

InlineKeyboardButton.update_forward_refs()

LoginUrl.update_forward_refs()

SwitchInlineQueryChosenChat.update_forward_refs()

CallbackQuery.update_forward_refs()

ForceReply.update_forward_refs()

ChatPhoto.update_forward_refs()

ChatInviteLink.update_forward_refs()

ChatAdministratorRights.update_forward_refs()

ChatMemberUpdated.update_forward_refs()

ChatMemberOwner.update_forward_refs()

ChatMemberAdministrator.update_forward_refs()

ChatMemberMember.update_forward_refs()

ChatMemberRestricted.update_forward_refs()

ChatMemberLeft.update_forward_refs()

ChatMemberBanned.update_forward_refs()

ChatJoinRequest.update_forward_refs()

ChatPermissions.update_forward_refs()

Birthdate.update_forward_refs()

BusinessIntro.update_forward_refs()

BusinessLocation.update_forward_refs()

BusinessOpeningHoursInterval.update_forward_refs()

BusinessOpeningHours.update_forward_refs()

ChatLocation.update_forward_refs()

ReactionTypeEmoji.update_forward_refs()

ReactionTypeCustomEmoji.update_forward_refs()

ReactionCount.update_forward_refs()

MessageReactionUpdated.update_forward_refs()

MessageReactionCountUpdated.update_forward_refs()

ForumTopic.update_forward_refs()

BotCommand.update_forward_refs()

BotCommandScopeDefault.update_forward_refs()

BotCommandScopeAllPrivateChats.update_forward_refs()

BotCommandScopeAllGroupChats.update_forward_refs()

BotCommandScopeAllChatAdministrators.update_forward_refs()

BotCommandScopeChat.update_forward_refs()

BotCommandScopeChatAdministrators.update_forward_refs()

BotCommandScopeChatMember.update_forward_refs()

BotName.update_forward_refs()

BotDescription.update_forward_refs()

BotShortDescription.update_forward_refs()

MenuButtonCommands.update_forward_refs()

MenuButtonWebApp.update_forward_refs()

MenuButtonDefault.update_forward_refs()

ChatBoostSourcePremium.update_forward_refs()

ChatBoostSourceGiftCode.update_forward_refs()

ChatBoostSourceGiveaway.update_forward_refs()

ChatBoost.update_forward_refs()

ChatBoostUpdated.update_forward_refs()

ChatBoostRemoved.update_forward_refs()

UserChatBoosts.update_forward_refs()

BusinessConnection.update_forward_refs()

BusinessMessagesDeleted.update_forward_refs()

ResponseParameters.update_forward_refs()

InputMediaPhoto.update_forward_refs()

InputMediaVideo.update_forward_refs()

InputMediaAnimation.update_forward_refs()

InputMediaAudio.update_forward_refs()

InputMediaDocument.update_forward_refs()

InputPaidMediaPhoto.update_forward_refs()

InputPaidMediaVideo.update_forward_refs()

Sticker.update_forward_refs()

StickerSet.update_forward_refs()

MaskPosition.update_forward_refs()

InputSticker.update_forward_refs()

InlineQuery.update_forward_refs()

InlineQueryResultsButton.update_forward_refs()

InlineQueryResultArticle.update_forward_refs()

InlineQueryResultPhoto.update_forward_refs()

InlineQueryResultGif.update_forward_refs()

InlineQueryResultMpeg4Gif.update_forward_refs()

InlineQueryResultVideo.update_forward_refs()

InlineQueryResultAudio.update_forward_refs()

InlineQueryResultVoice.update_forward_refs()

InlineQueryResultDocument.update_forward_refs()

InlineQueryResultLocation.update_forward_refs()

InlineQueryResultVenue.update_forward_refs()

InlineQueryResultContact.update_forward_refs()

InlineQueryResultGame.update_forward_refs()

InlineQueryResultCachedPhoto.update_forward_refs()

InlineQueryResultCachedGif.update_forward_refs()

InlineQueryResultCachedMpeg4Gif.update_forward_refs()

InlineQueryResultCachedSticker.update_forward_refs()

InlineQueryResultCachedDocument.update_forward_refs()

InlineQueryResultCachedVideo.update_forward_refs()

InlineQueryResultCachedVoice.update_forward_refs()

InlineQueryResultCachedAudio.update_forward_refs()

InputTextMessageContent.update_forward_refs()

InputLocationMessageContent.update_forward_refs()

InputVenueMessageContent.update_forward_refs()

InputContactMessageContent.update_forward_refs()

InputInvoiceMessageContent.update_forward_refs()

ChosenInlineResult.update_forward_refs()

SentWebAppMessage.update_forward_refs()

LabeledPrice.update_forward_refs()

Invoice.update_forward_refs()

ShippingAddress.update_forward_refs()

OrderInfo.update_forward_refs()

ShippingOption.update_forward_refs()

SuccessfulPayment.update_forward_refs()

ShippingQuery.update_forward_refs()

PreCheckoutQuery.update_forward_refs()

RevenueWithdrawalStatePending.update_forward_refs()

RevenueWithdrawalStateSucceeded.update_forward_refs()

RevenueWithdrawalStateFailed.update_forward_refs()

TransactionPartnerUser.update_forward_refs()

TransactionPartnerFragment.update_forward_refs()

TransactionPartnerTelegramAds.update_forward_refs()

TransactionPartnerOther.update_forward_refs()

StarTransaction.update_forward_refs()

StarTransactions.update_forward_refs()

PassportData.update_forward_refs()

PassportFile.update_forward_refs()

EncryptedPassportElement.update_forward_refs()

EncryptedCredentials.update_forward_refs()

PassportElementErrorDataField.update_forward_refs()

PassportElementErrorFrontSide.update_forward_refs()

PassportElementErrorReverseSide.update_forward_refs()

PassportElementErrorSelfie.update_forward_refs()

PassportElementErrorFile.update_forward_refs()

PassportElementErrorFiles.update_forward_refs()

PassportElementErrorTranslationFile.update_forward_refs()

PassportElementErrorTranslationFiles.update_forward_refs()

PassportElementErrorUnspecified.update_forward_refs()

Game.update_forward_refs()

CallbackGame.update_forward_refs()

GameHighScore.update_forward_refs()
