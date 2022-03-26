-- numCheckins
update business
set numCheckins = business_checkins.nci
from business as business_alias inner join
    (
        select business_id, count(time) nci
        from checkins
        group by business_id
    ) business_checkins
    on business_checkins.business_id = business_alias.business_id
where business_checkins.business_id = business.business_id

-- numTips
update business
set numTips = business_tips.nt
from business as business_alias inner join
    (
        select business_id, count(tipDate) nt
        from tip
        group by business_id
    ) business_tips
    on business_tips.business_id = business_alias.business_id
where business_tips.business_id = business.business_id

-- totalLikes
update user
set totalLikes = user_tips.tl
from user as user_alias inner join
    (
        select user_id, sum(likes) tl
        from tip
        group by user_id
    ) user_tips
    on user_tips.user_id = user_alias.user_id
where user_tips.user_id = user.user_id

-- tipCount
update user
set tipCount = user_tips.tc
from user as user_alias inner join
    (
        select user_id, count(tipDate) tc
        from tip
        group by user_id
    ) user_tips
    on user_tips.user_id = user_alias.user_id
where user_tips.user_id = user.user_id