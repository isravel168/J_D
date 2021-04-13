"""1"""
#ENDPOINTS and payloads for city
# https://homeurl/api/city/
# https://homeurl/api/detailed/city/(key for process(CityId))
# https://homeurl/api/create/city/
# https://homeurl/api/update/city/(key for process(CityId))
# https://homeurl/api/delete/city/(key for process(CityId))

"""
{
    "CityId": 101010,
    "StateId": 43,
    "Name": "chennai",
    "Description": "one of my famous",
    "TimeZone": "2021-03-28T16:38:00Z",
    "ActiveFlag": true
}
"""
"""2"""
#ENDPOINTS and payloads for state

# https://homeurl/api/state/
# https://homeurl/api/detailed/state/(key for process(StateId))
# https://homeurl/api/create/state/
# https://homeurl/api/update/state/(key for process(StateId))
# https://homeurl/api/delete/state/(key for process(StateId))
"""
{
    "StateId": 101010,
    "CountryId": 1234,
    "Name": "tamil nadu",
    "Description": "famous of mine",
    "ActiveFlag": true
}
"""
"""3"""
#ENDPOINTS and payloads for country

# https://homeurl/api/country/
# https://homeurl/api/detailed/country/(key for process(CountryId))
# https://homeurl/api/create/country/
# https://homeurl/api/update/country/(key for process(CountryId))
# https://homeurl/api/delete/country/(key for process(CountryId))
"""
{
    "CountryId": 101010,
    "CountryName": "india",
    "Description": "famous of mine",
    "ActiveFlag": true
}
"""
"""4"""
#ENDPOINTS and payloads for qualification

# https://homeurl/api/qualification/
# https://homeurl/api/detailed/qualification/(key for process(QualificationID))
# https://homeurl/api/create/qualification/
# https://homeurl/api/update/qualification/(key for process(QualificationID))
# https://homeurl/api/delete/qualification/(key for process(QualificationID))
"""
{
    "QualificationID": 101010,
    "QualificationName": "M.E",
    "Description": "xyz",
    "SubscriberId": 22,
    "ApprovalFlag": true,
    "ClientSpecificFlg": true,
    "CreatedBy": "kumar",
    "CreatedDate": "2021-03-28",
    "ModifiedBy": "isravel",
    "ModifiedDate": "2021-03-27",
    "ActiveFlag": false
}
"""
"""5"""
#ENDPOINTS and payloads for qualification

# https://homeurl/api/qualification/
# https://homeurl/api/detailed/qualification/(key for process(SkillId))
# https://homeurl/api/create/qualification/
# https://homeurl/api/update/qualification/(key for process(SkillId))
# https://homeurl/api/delete/qualification/(key for process(SkillId))
"""
{
    "SkillId": 101010,
    "SkillName": "java",
    "Description": "xyz",
    "SubscriberId": 31,
    "ApprovalFlag": true,
    "ClientSpecificFlg": true,
    "CreatedBy": "kumar",
    "CreatedDate": "2021-03-26",
    "ModifiedBy": "isravel",
    "ModifiedDate": "2021-03-19",
    "ActiveFlag": true
}
"""
"""6"""
#ENDPOINTS and payloads for perks
# https://homeurl/api/perks/
# https://homeurl/api/detailed/perks/(key for process(PerksID))
# https://homeurl/api/create/perks/
# https://homeurl/api/update/perks/(key for process(PerksID))
# https://homeurl/api/delete/perks/(key for process(PerksID))
"""
{
    "PerksId": 101010,
    "PerksName": "abcx",
    "Description": "xcba",
    "SubscriberId": 17,
    "ApprovalFlag": true,
    "ClientSpecificFlg": true,
    "CreatedBy": "kumar",
    "CreatedDate": "2021-03-24",
    "ModifiedBy": "isravel",
    "ModifiedDate": "2021-03-24",
    "ActiveFlag": true
}
"""