# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: steammessages_parental.steamclient.proto
# plugin: python-betterproto
# Last updated 09/09/2021

from dataclasses import dataclass
from typing import List

import betterproto


class EProfileCustomizationType(betterproto.Enum):
    Invalid = 0
    RareAchievementShowcase = 1
    GameCollector = 2
    ItemShowcase = 3
    TradeShowcase = 4
    Badges = 5
    FavoriteGame = 6
    ScreenshotShowcase = 7
    CustomText = 8
    FavoriteGroup = 9
    Recommendation = 10
    WorkshopItem = 11
    MyWorkshop = 12
    ArtworkShowcase = 13
    VideoShowcase = 14
    Guides = 15
    MyGuides = 16
    Achievements = 17
    Greenlight = 18
    MyGreenlight = 19
    Salien = 20
    LoyaltyRewardReactions = 21
    SingleArtworkShowcase = 22
    AchievementsCompletionist = 23


class EBanContentCheckResult(betterproto.Enum):
    NotScanned = 0
    Reset = 1
    NeedsChecking = 2
    VeryUnlikely = 5
    Unlikely = 30
    Possible = 50
    Likely = 75
    VeryLikely = 100


class EProfileCustomizationStyle(betterproto.Enum):
    Default = 0
    Selected = 1
    Rarest = 2
    MostRecent = 3
    Random = 4
    HighestRated = 5


class EAgreementType(betterproto.Enum):
    Invalid = -1
    GlobalSSA = 0
    ChinaSSA = 1


class ENotificationSetting(betterproto.Enum):
    UseDefault = 0
    Always = 1
    Never = 2


class ETextFilterSetting(betterproto.Enum):
    SteamLabOptedOut = 0
    Enabled = 1
    EnabledAllowProfanity = 2
    Disabled = 3


@dataclass(eq=False, repr=False)
class GetMutualFriendsForIncomingInvitesRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class IncomingInviteMutualFriendList(betterproto.Message):
    steamid: int = betterproto.fixed64_field(1)
    mutual_friend_account_ids: List[int] = betterproto.uint32_field(2)


@dataclass(eq=False, repr=False)
class GetMutualFriendsForIncomingInvitesResponse(betterproto.Message):
    incoming_invite_mutual_friends_lists: List["IncomingInviteMutualFriendList"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class GetOwnedGamesRequest(betterproto.Message):
    steamid: int = betterproto.uint64_field(1)
    include_appinfo: bool = betterproto.bool_field(2)
    include_played_free_games: bool = betterproto.bool_field(3)
    appids_filter: List[int] = betterproto.uint32_field(4)
    include_free_sub: bool = betterproto.bool_field(5)
    skip_unvetted_apps: bool = betterproto.bool_field(6)


@dataclass(eq=False, repr=False)
class GetOwnedGamesResponse(betterproto.Message):
    game_count: int = betterproto.uint32_field(1)
    games: List["GetOwnedGamesResponseGame"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class GetOwnedGamesResponseGame(betterproto.Message):
    appid: int = betterproto.int32_field(1)
    name: str = betterproto.string_field(2)
    playtime_2_weeks: int = betterproto.int32_field(3)
    playtime_forever: int = betterproto.int32_field(4)
    img_icon_url: str = betterproto.string_field(5)
    has_community_visible_stats: bool = betterproto.bool_field(7)
    playtime_windows_forever: int = betterproto.int32_field(8)
    playtime_mac_forever: int = betterproto.int32_field(9)
    playtime_linux_forever: int = betterproto.int32_field(10)


@dataclass(eq=False, repr=False)
class GetPlayNextRequest(betterproto.Message):
    max_age_seconds: int = betterproto.uint32_field(1)
    ignore_appids: List[int] = betterproto.uint32_field(2)


@dataclass(eq=False, repr=False)
class GetPlayNextResponse(betterproto.Message):
    last_update_time: int = betterproto.uint32_field(1)
    appids: List[int] = betterproto.uint32_field(2)


@dataclass(eq=False, repr=False)
class GetFriendsGameplayInfoRequest(betterproto.Message):
    appid: int = betterproto.uint32_field(1)


@dataclass(eq=False, repr=False)
class GetFriendsGameplayInfoResponse(betterproto.Message):
    your_info: "GetFriendsGameplayInfoResponseOwnGameplayInfo" = betterproto.message_field(1)
    in_game: List["GetFriendsGameplayInfoResponseFriendsGameplayInfo"] = betterproto.message_field(2)
    played_recently: List["GetFriendsGameplayInfoResponseFriendsGameplayInfo"] = betterproto.message_field(3)
    played_ever: List["GetFriendsGameplayInfoResponseFriendsGameplayInfo"] = betterproto.message_field(4)
    owns: List["GetFriendsGameplayInfoResponseFriendsGameplayInfo"] = betterproto.message_field(5)
    in_wishlist: List["GetFriendsGameplayInfoResponseFriendsGameplayInfo"] = betterproto.message_field(6)


@dataclass(eq=False, repr=False)
class GetFriendsGameplayInfoResponseFriendsGameplayInfo(betterproto.Message):
    steamid: int = betterproto.fixed64_field(1)
    minutes_played: int = betterproto.uint32_field(2)
    minutes_played_forever: int = betterproto.uint32_field(3)


@dataclass(eq=False, repr=False)
class GetFriendsGameplayInfoResponseOwnGameplayInfo(betterproto.Message):
    steamid: int = betterproto.fixed64_field(1)
    minutes_played: int = betterproto.uint32_field(2)
    minutes_played_forever: int = betterproto.uint32_field(3)
    in_wishlist: bool = betterproto.bool_field(4)
    owned: bool = betterproto.bool_field(5)


@dataclass(eq=False, repr=False)
class GetFriendsAppsActivityRequest(betterproto.Message):
    news_language: str = betterproto.string_field(1)
    request_flags: int = betterproto.uint32_field(2)


@dataclass(eq=False, repr=False)
class GetFriendsAppsActivityResponse(betterproto.Message):
    trending: List["GetFriendsAppsActivityResponseAppFriendsInfo"] = betterproto.message_field(1)
    recent_purchases: List["GetFriendsAppsActivityResponseAppFriendsInfo"] = betterproto.message_field(2)
    unowned: List["GetFriendsAppsActivityResponseAppFriendsInfo"] = betterproto.message_field(3)
    popular: List["GetFriendsAppsActivityResponseAppFriendsInfo"] = betterproto.message_field(4)
    dont_forget: List["GetFriendsAppsActivityResponseAppFriendsInfo"] = betterproto.message_field(5)
    being_discussed: List["GetFriendsAppsActivityResponseAppFriendsInfo"] = betterproto.message_field(6)
    new_to_group: List["GetFriendsAppsActivityResponseAppFriendsInfo"] = betterproto.message_field(7)
    returned_to_group: List["GetFriendsAppsActivityResponseAppFriendsInfo"] = betterproto.message_field(8)
    active_friend_count: int = betterproto.uint32_field(9)


@dataclass(eq=False, repr=False)
class GetFriendsAppsActivityResponseFriendPlayTime(betterproto.Message):
    steamid: int = betterproto.fixed64_field(1)
    minutes_played_this_week: int = betterproto.uint32_field(2)
    minutes_played_two_weeks: int = betterproto.uint32_field(3)
    minutes_played_forever: int = betterproto.uint32_field(4)
    event_count: int = betterproto.uint32_field(5)


@dataclass(eq=False, repr=False)
class GetFriendsAppsActivityResponseAppFriendsInfo(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    friends: List["GetFriendsAppsActivityResponseFriendPlayTime"] = betterproto.message_field(2)
    display_order: int = betterproto.uint32_field(3)


@dataclass(eq=False, repr=False)
class GetGameBadgeLevelsRequest(betterproto.Message):
    appid: int = betterproto.uint32_field(1)


@dataclass(eq=False, repr=False)
class GetGameBadgeLevelsResponse(betterproto.Message):
    player_level: int = betterproto.uint32_field(1)
    badges: List["GetGameBadgeLevelsResponseBadge"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class GetGameBadgeLevelsResponseBadge(betterproto.Message):
    level: int = betterproto.int32_field(1)
    series: int = betterproto.int32_field(2)
    border_color: int = betterproto.uint32_field(3)


@dataclass(eq=False, repr=False)
class GetProfileBackgroundRequest(betterproto.Message):
    steamid: int = betterproto.fixed64_field(1)
    language: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class ProfileItem(betterproto.Message):
    communityitemid: int = betterproto.uint64_field(1)
    image_small: str = betterproto.string_field(2)
    image_large: str = betterproto.string_field(3)
    name: str = betterproto.string_field(4)
    item_title: str = betterproto.string_field(5)
    item_description: str = betterproto.string_field(6)
    appid: int = betterproto.uint32_field(7)
    item_type: int = betterproto.uint32_field(8)
    item_class: int = betterproto.uint32_field(9)
    movie_webm: str = betterproto.string_field(10)
    movie_mp4: str = betterproto.string_field(11)
    movie_webm_small: str = betterproto.string_field(13)
    movie_mp4_small: str = betterproto.string_field(14)
    equipped_flags: int = betterproto.uint32_field(12)


@dataclass(eq=False, repr=False)
class GetProfileBackgroundResponse(betterproto.Message):
    profile_background: "ProfileItem" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class SetProfileBackgroundRequest(betterproto.Message):
    communityitemid: int = betterproto.uint64_field(1)


@dataclass(eq=False, repr=False)
class SetProfileBackgroundResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class GetMiniProfileBackgroundRequest(betterproto.Message):
    steamid: int = betterproto.fixed64_field(1)
    language: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class GetMiniProfileBackgroundResponse(betterproto.Message):
    profile_background: "ProfileItem" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class SetMiniProfileBackgroundRequest(betterproto.Message):
    communityitemid: int = betterproto.uint64_field(1)


@dataclass(eq=False, repr=False)
class SetMiniProfileBackgroundResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class GetAvatarFrameRequest(betterproto.Message):
    steamid: int = betterproto.fixed64_field(1)
    language: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class GetAvatarFrameResponse(betterproto.Message):
    avatar_frame: "ProfileItem" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class SetAvatarFrameRequest(betterproto.Message):
    communityitemid: int = betterproto.uint64_field(1)


@dataclass(eq=False, repr=False)
class SetAvatarFrameResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class GetAnimatedAvatarRequest(betterproto.Message):
    steamid: int = betterproto.fixed64_field(1)
    language: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class GetAnimatedAvatarResponse(betterproto.Message):
    avatar: "ProfileItem" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class SetAnimatedAvatarRequest(betterproto.Message):
    communityitemid: int = betterproto.uint64_field(1)


@dataclass(eq=False, repr=False)
class SetAnimatedAvatarResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class GetProfileItemsOwnedRequest(betterproto.Message):
    language: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class GetProfileItemsOwnedResponse(betterproto.Message):
    profile_backgrounds: List["ProfileItem"] = betterproto.message_field(1)
    mini_profile_backgrounds: List["ProfileItem"] = betterproto.message_field(2)
    avatar_frames: List["ProfileItem"] = betterproto.message_field(3)
    animated_avatars: List["ProfileItem"] = betterproto.message_field(4)
    profile_modifiers: List["ProfileItem"] = betterproto.message_field(5)


@dataclass(eq=False, repr=False)
class GetProfileItemsEquippedRequest(betterproto.Message):
    steamid: int = betterproto.fixed64_field(1)
    language: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class GetProfileItemsEquippedResponse(betterproto.Message):
    profile_background: "ProfileItem" = betterproto.message_field(1)
    mini_profile_background: "ProfileItem" = betterproto.message_field(2)
    avatar_frame: "ProfileItem" = betterproto.message_field(3)
    animated_avatar: "ProfileItem" = betterproto.message_field(4)
    profile_modifier: "ProfileItem" = betterproto.message_field(5)


@dataclass(eq=False, repr=False)
class SetEquippedProfileItemFlagsRequest(betterproto.Message):
    communityitemid: int = betterproto.uint64_field(1)
    flags: int = betterproto.uint32_field(2)


@dataclass(eq=False, repr=False)
class SetEquippedProfileItemFlagsResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class GetEmoticonListRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class GetEmoticonListResponse(betterproto.Message):
    emoticons: List["GetEmoticonListResponseEmoticon"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class GetEmoticonListResponseEmoticon(betterproto.Message):
    name: str = betterproto.string_field(1)
    count: int = betterproto.int32_field(2)
    time_last_used: int = betterproto.uint32_field(3)
    use_count: int = betterproto.uint32_field(4)
    time_received: int = betterproto.uint32_field(5)
    appid: int = betterproto.uint32_field(6)


@dataclass(eq=False, repr=False)
class GetAchievementsProgressRequest(betterproto.Message):
    steamid: int = betterproto.uint64_field(1)
    language: str = betterproto.string_field(2)
    appids: List[int] = betterproto.uint32_field(3)


@dataclass(eq=False, repr=False)
class GetAchievementsProgressResponse(betterproto.Message):
    achievement_progress: List["GetAchievementsProgressResponseAchievementProgress"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class GetAchievementsProgressResponseAchievementProgress(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    unlocked: int = betterproto.uint32_field(2)
    total: int = betterproto.uint32_field(3)
    percentage: float = betterproto.float_field(4)
    all_unlocked: bool = betterproto.bool_field(5)
    cache_time: int = betterproto.uint32_field(6)


@dataclass(eq=False, repr=False)
class GetFavoriteBadgeRequest(betterproto.Message):
    steamid: int = betterproto.uint64_field(1)


@dataclass(eq=False, repr=False)
class GetFavoriteBadgeResponse(betterproto.Message):
    has_favorite_badge: bool = betterproto.bool_field(1)
    badgeid: int = betterproto.uint32_field(2)
    communityitemid: int = betterproto.uint64_field(3)
    item_type: int = betterproto.uint32_field(4)
    border_color: int = betterproto.uint32_field(5)
    appid: int = betterproto.uint32_field(6)
    level: int = betterproto.uint32_field(7)


@dataclass(eq=False, repr=False)
class SetFavoriteBadgeRequest(betterproto.Message):
    communityitemid: int = betterproto.uint64_field(1)
    badgeid: int = betterproto.uint32_field(2)


@dataclass(eq=False, repr=False)
class SetFavoriteBadgeResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class GetProfileCustomizationRequest(betterproto.Message):
    steamid: int = betterproto.fixed64_field(1)
    include_inactive_customizations: bool = betterproto.bool_field(2)
    include_purchased_customizations: bool = betterproto.bool_field(3)


@dataclass(eq=False, repr=False)
class ProfileCustomizationSlot(betterproto.Message):
    slot: int = betterproto.uint32_field(1)
    appid: int = betterproto.uint32_field(2)
    publishedfileid: int = betterproto.uint64_field(3)
    item_assetid: int = betterproto.uint64_field(4)
    item_contextid: int = betterproto.uint64_field(5)
    notes: str = betterproto.string_field(6)
    title: str = betterproto.string_field(7)
    accountid: int = betterproto.uint32_field(8)
    badgeid: int = betterproto.uint32_field(9)
    border_color: int = betterproto.uint32_field(10)
    item_classid: int = betterproto.uint64_field(11)
    item_instanceid: int = betterproto.uint64_field(12)
    ban_check_result: "EBanContentCheckResult" = betterproto.enum_field(13)


@dataclass(eq=False, repr=False)
class ProfileCustomization(betterproto.Message):
    customization_type: "EProfileCustomizationType" = betterproto.enum_field(1)
    large: bool = betterproto.bool_field(2)
    slots: List["ProfileCustomizationSlot"] = betterproto.message_field(3)
    active: bool = betterproto.bool_field(4)
    customization_style: "EProfileCustomizationStyle" = betterproto.enum_field(5)
    purchaseid: int = betterproto.uint64_field(6)
    level: int = betterproto.uint32_field(7)


@dataclass(eq=False, repr=False)
class ProfileTheme(betterproto.Message):
    theme_id: str = betterproto.string_field(1)
    title: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class ProfilePreferences(betterproto.Message):
    hide_profile_awards: bool = betterproto.bool_field(1)


@dataclass(eq=False, repr=False)
class GetProfileCustomizationResponse(betterproto.Message):
    customizations: List["ProfileCustomization"] = betterproto.message_field(1)
    slots_available: int = betterproto.uint32_field(2)
    profile_theme: "ProfileTheme" = betterproto.message_field(3)
    purchased_customizations: List["GetProfileCustomizationResponsePurchasedCustomization"] = betterproto.message_field(
        4
    )
    profile_preferences: "ProfilePreferences" = betterproto.message_field(5)


@dataclass(eq=False, repr=False)
class GetProfileCustomizationResponsePurchasedCustomization(betterproto.Message):
    purchaseid: int = betterproto.uint64_field(1)
    customization_type: "EProfileCustomizationType" = betterproto.enum_field(2)
    level: int = betterproto.uint32_field(3)


@dataclass(eq=False, repr=False)
class GetPurchasedProfileCustomizationsRequest(betterproto.Message):
    steamid: int = betterproto.fixed64_field(1)


@dataclass(eq=False, repr=False)
class GetPurchasedProfileCustomizationsResponse(betterproto.Message):
    purchased_customizations: List[
        "GetPurchasedProfileCustomizationsResponsePurchasedCustomization"
    ] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class GetPurchasedProfileCustomizationsResponsePurchasedCustomization(betterproto.Message):
    purchaseid: int = betterproto.uint64_field(1)
    customization_type: "EProfileCustomizationType" = betterproto.enum_field(2)


@dataclass(eq=False, repr=False)
class GetPurchasedAndUpgradedProfileCustomizationsRequest(betterproto.Message):
    steamid: int = betterproto.fixed64_field(1)


@dataclass(eq=False, repr=False)
class GetPurchasedAndUpgradedProfileCustomizationsResponse(betterproto.Message):
    purchased_customizations: List[
        "GetPurchasedAndUpgradedProfileCustomizationsResponsePurchasedCustomization"
    ] = betterproto.message_field(1)
    upgraded_customizations: List[
        "GetPurchasedAndUpgradedProfileCustomizationsResponseUpgradedCustomization"
    ] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class GetPurchasedAndUpgradedProfileCustomizationsResponsePurchasedCustomization(betterproto.Message):
    customization_type: "EProfileCustomizationType" = betterproto.enum_field(1)
    count: int = betterproto.uint32_field(2)


@dataclass(eq=False, repr=False)
class GetPurchasedAndUpgradedProfileCustomizationsResponseUpgradedCustomization(betterproto.Message):
    customization_type: "EProfileCustomizationType" = betterproto.enum_field(1)
    level: int = betterproto.uint32_field(2)


@dataclass(eq=False, repr=False)
class GetProfileThemesAvailableRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class GetProfileThemesAvailableResponse(betterproto.Message):
    profile_themes: List["ProfileTheme"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class SetProfileThemeRequest(betterproto.Message):
    theme_id: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class SetProfileThemeResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class SetProfilePreferencesRequest(betterproto.Message):
    profile_preferences: "ProfilePreferences" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class SetProfilePreferencesResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class PostStatusToFriendsRequest(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    status_text: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class PostStatusToFriendsResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class GetPostedStatusRequest(betterproto.Message):
    steamid: int = betterproto.uint64_field(1)
    postid: int = betterproto.uint64_field(2)


@dataclass(eq=False, repr=False)
class GetPostedStatusResponse(betterproto.Message):
    accountid: int = betterproto.uint32_field(1)
    postid: int = betterproto.uint64_field(2)
    status_text: str = betterproto.string_field(3)
    deleted: bool = betterproto.bool_field(4)
    appid: int = betterproto.uint32_field(5)


@dataclass(eq=False, repr=False)
class DeletePostedStatusRequest(betterproto.Message):
    postid: int = betterproto.uint64_field(1)


@dataclass(eq=False, repr=False)
class DeletePostedStatusResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class GetLastPlayedTimesRequest(betterproto.Message):
    min_last_played: int = betterproto.uint32_field(1)


@dataclass(eq=False, repr=False)
class GetLastPlayedTimesResponse(betterproto.Message):
    games: List["GetLastPlayedTimesResponseGame"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class GetLastPlayedTimesResponseGame(betterproto.Message):
    appid: int = betterproto.int32_field(1)
    last_playtime: int = betterproto.uint32_field(2)
    playtime_2_weeks: int = betterproto.int32_field(3)
    playtime_forever: int = betterproto.int32_field(4)
    first_playtime: int = betterproto.uint32_field(5)
    playtime_windows_forever: int = betterproto.int32_field(6)
    playtime_mac_forever: int = betterproto.int32_field(7)
    playtime_linux_forever: int = betterproto.int32_field(8)
    first_windows_playtime: int = betterproto.uint32_field(9)
    first_mac_playtime: int = betterproto.uint32_field(10)
    first_linux_playtime: int = betterproto.uint32_field(11)
    last_windows_playtime: int = betterproto.uint32_field(12)
    last_mac_playtime: int = betterproto.uint32_field(13)
    last_linux_playtime: int = betterproto.uint32_field(14)


@dataclass(eq=False, repr=False)
class AcceptSsaRequest(betterproto.Message):
    agreement_type: "EAgreementType" = betterproto.enum_field(1)
    time_signed_utc: int = betterproto.uint32_field(2)


@dataclass(eq=False, repr=False)
class AcceptSsaResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class GetNicknameListRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class GetNicknameListResponse(betterproto.Message):
    nicknames: List["GetNicknameListResponsePlayerNickname"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class GetNicknameListResponsePlayerNickname(betterproto.Message):
    accountid: int = betterproto.fixed32_field(1)
    nickname: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class GetPerFriendPreferencesRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class PerFriendPreferences(betterproto.Message):
    accountid: int = betterproto.fixed32_field(1)
    nickname: str = betterproto.string_field(2)
    notifications_showingame: "ENotificationSetting" = betterproto.enum_field(3)
    notifications_showonline: "ENotificationSetting" = betterproto.enum_field(4)
    notifications_showmessages: "ENotificationSetting" = betterproto.enum_field(5)
    sounds_showingame: "ENotificationSetting" = betterproto.enum_field(6)
    sounds_showonline: "ENotificationSetting" = betterproto.enum_field(7)
    sounds_showmessages: "ENotificationSetting" = betterproto.enum_field(8)
    notifications_sendmobile: "ENotificationSetting" = betterproto.enum_field(9)


@dataclass(eq=False, repr=False)
class GetPerFriendPreferencesResponse(betterproto.Message):
    preferences: List["PerFriendPreferences"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class SetPerFriendPreferencesRequest(betterproto.Message):
    preferences: "PerFriendPreferences" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class SetPerFriendPreferencesResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class AddFriendRequest(betterproto.Message):
    steamid: int = betterproto.fixed64_field(1)


@dataclass(eq=False, repr=False)
class AddFriendResponse(betterproto.Message):
    invite_sent: bool = betterproto.bool_field(1)
    friend_relationship: int = betterproto.uint32_field(2)
    result: int = betterproto.int32_field(3)


@dataclass(eq=False, repr=False)
class RemoveFriendRequest(betterproto.Message):
    steamid: int = betterproto.fixed64_field(1)


@dataclass(eq=False, repr=False)
class RemoveFriendResponse(betterproto.Message):
    friend_relationship: int = betterproto.uint32_field(1)


@dataclass(eq=False, repr=False)
class IgnoreFriendRequest(betterproto.Message):
    steamid: int = betterproto.fixed64_field(1)
    unignore: bool = betterproto.bool_field(2)


@dataclass(eq=False, repr=False)
class IgnoreFriendResponse(betterproto.Message):
    friend_relationship: int = betterproto.uint32_field(1)


@dataclass(eq=False, repr=False)
class GetCommunityPreferencesRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class CommunityPreferences(betterproto.Message):
    hide_adult_content_violence: bool = betterproto.bool_field(1)
    hide_adult_content_sex: bool = betterproto.bool_field(2)
    parenthesize_nicknames: bool = betterproto.bool_field(4)
    text_filter_setting: "ETextFilterSetting" = betterproto.enum_field(5)
    text_filter_ignore_friends: bool = betterproto.bool_field(6)
    text_filter_words_revision: int = betterproto.uint32_field(7)
    timestamp_updated: int = betterproto.uint32_field(3)


@dataclass(eq=False, repr=False)
class GetCommunityPreferencesResponse(betterproto.Message):
    preferences: "CommunityPreferences" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class SetCommunityPreferencesRequest(betterproto.Message):
    preferences: "CommunityPreferences" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class SetCommunityPreferencesResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class GetTextFilterWordsRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class TextFilterWords(betterproto.Message):
    text_filter_custom_banned_words: List[str] = betterproto.string_field(1)
    text_filter_custom_clean_words: List[str] = betterproto.string_field(2)
    text_filter_words_revision: int = betterproto.uint32_field(3)


@dataclass(eq=False, repr=False)
class GetTextFilterWordsResponse(betterproto.Message):
    words: "TextFilterWords" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class GetNewSteamAnnouncementStateRequest(betterproto.Message):
    language: int = betterproto.int32_field(1)


@dataclass(eq=False, repr=False)
class GetNewSteamAnnouncementStateResponse(betterproto.Message):
    state: int = betterproto.int32_field(1)
    announcement_headline: str = betterproto.string_field(2)
    announcement_url: str = betterproto.string_field(3)
    time_posted: int = betterproto.uint32_field(4)
    announcement_gid: int = betterproto.uint64_field(5)


@dataclass(eq=False, repr=False)
class UpdateSteamAnnouncementLastReadRequest(betterproto.Message):
    announcement_gid: int = betterproto.uint64_field(1)
    time_posted: int = betterproto.uint32_field(2)


@dataclass(eq=False, repr=False)
class UpdateSteamAnnouncementLastReadResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class GetPrivacySettingsRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class CPrivacySettings(betterproto.Message):
    privacy_state: int = betterproto.int32_field(1)
    privacy_state_inventory: int = betterproto.int32_field(2)
    privacy_state_gifts: int = betterproto.int32_field(3)
    privacy_state_ownedgames: int = betterproto.int32_field(4)
    privacy_state_playtime: int = betterproto.int32_field(5)
    privacy_state_friendslist: int = betterproto.int32_field(6)


@dataclass(eq=False, repr=False)
class GetPrivacySettingsResponse(betterproto.Message):
    privacy_settings: "CPrivacySettings" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class GetDurationControlRequest(betterproto.Message):
    appid: int = betterproto.uint32_field(1)


@dataclass(eq=False, repr=False)
class GetDurationControlResponse(betterproto.Message):
    is_enabled: bool = betterproto.bool_field(1)
    seconds: int = betterproto.int32_field(2)
    seconds_today: int = betterproto.int32_field(3)
    is_steamchina_account: bool = betterproto.bool_field(4)
    is_age_verified: bool = betterproto.bool_field(5)
    seconds_allowed_today: int = betterproto.uint32_field(6)


@dataclass(eq=False, repr=False)
class LastPlayedTimesNotification(betterproto.Message):
    games: List["GetLastPlayedTimesResponseGame"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class FriendNicknameChangedNotification(betterproto.Message):
    accountid: int = betterproto.fixed32_field(1)
    nickname: str = betterproto.string_field(2)
    is_echo_to_self: bool = betterproto.bool_field(3)


@dataclass(eq=False, repr=False)
class FriendEquippedProfileItemsChangedNotification(betterproto.Message):
    accountid: int = betterproto.fixed32_field(1)


@dataclass(eq=False, repr=False)
class NewSteamAnnouncementStateNotification(betterproto.Message):
    state: int = betterproto.int32_field(1)
    announcement_headline: str = betterproto.string_field(2)
    announcement_url: str = betterproto.string_field(3)
    time_posted: int = betterproto.uint32_field(4)
    announcement_gid: int = betterproto.uint64_field(5)


@dataclass(eq=False, repr=False)
class CommunityPreferencesChangedNotification(betterproto.Message):
    preferences: "CommunityPreferences" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class TextFilterWordsChangedNotification(betterproto.Message):
    words: "TextFilterWords" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class PerFriendPreferencesChangedNotification(betterproto.Message):
    accountid: int = betterproto.fixed32_field(1)
    preferences: "PerFriendPreferences" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class PrivacySettingsChangedNotification(betterproto.Message):
    privacy_settings: "CPrivacySettings" = betterproto.message_field(1)
