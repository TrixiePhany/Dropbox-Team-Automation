from dropbox_team_api import DropboxTeamPOC

p = DropboxTeamPOC()
members = p.list_members(limit=200)
target = "newuser@example.com" # replace with the email to find here 
for m in members:
    profile = m.get("profile", {})
    if profile.get("email") == target:
        team_id = profile.get("team_member_id")
        print("Found:", team_id)
        break
else:
    print("Not found")
