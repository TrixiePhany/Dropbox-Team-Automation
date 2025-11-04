import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DROPBOX_TOKEN")
TEAM_ID = os.getenv("DROPBOX_TEAM_ID")

if not TOKEN:
    raise RuntimeError("Missing DROPBOX_TOKEN in .env")

HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
BASE = "https://api.dropboxapi.com/2"


class DropboxTeamPOC:
    def __init__(self):
        print("Connected to Dropbox Business API")
        if TEAM_ID:
            print(f"📦 Team ID: {TEAM_ID}")
        print("-" * 60)

    def list_members(self, limit=10):
        print("📋 Fetching team members...\n")
        url = f"{BASE}/team/members/list_v2"
        data = {"limit": limit}
        r = requests.post(url, headers=HEADERS, json=data)

        if r.status_code != 200:
            print("❌ Error:", r.status_code, r.text)
            return

        members = r.json().get("members", [])
        if not members:
            print("⚠️  No members found.")
            return

        for m in members:
            profile = m.get("profile", {})
            name = profile.get("name", {}).get("display_name", "(no name)")
            email = profile.get("email", "N/A")
            status = profile.get("status", {}).get(".tag", "unknown")
            print(f"👤 {name:<25} | {email:<35} | Status: {status}")
        print("-" * 60)
        print(f"✅ Total members: {len(members)}")
        return members

    def invite_user(self, email, given_name="First", surname="Last"):
        print(f"📨 Inviting user: {email}")
        url = f"{BASE}/team/members/add"
        data = {
            "new_members": [
                {
                    "member_email": email,
                    "member_given_name": given_name,
                    "member_surname": surname,
                }
            ],
            "force_async": False,
        }
        r = requests.post(url, headers=HEADERS, json=data)

        if r.status_code != 200:
            print("❌ Invite failed:", r.status_code, r.text)
            return

        resp = r.json()
        print("\n✨ Invite Summary:")
        if resp.get(".tag") == "complete":
            result = resp.get("complete", [])[0]
            if result.get(".tag") == "success":
                profile = result.get("profile", {})
                print(f"✅ Successfully invited: {profile.get('email')}")
                print(f"🆔 Member ID: {profile.get('team_member_id')}")
                print(f"📅 Invited on: {profile.get('invited_on')}")
                print(f"🏷️  Status: {profile.get('status', {}).get('.tag')}")
            elif result.get(".tag") == "team_license_limit":
                print("⚠️  Team license limit reached — cannot add more users.")
            else:
                print(json.dumps(result, indent=2))
        else:
            print(json.dumps(resp, indent=2))
        print("-" * 60)
        return resp

    def remove_user(self, team_member_id):
        print(f"🗑️ Removing user with ID: {team_member_id}")
        url = f"{BASE}/team/members/remove"
        data = {
            "user": {
                ".tag": "team_member_id",
                "team_member_id": team_member_id
            },
            "wipe_data": False  # Safety flag
        }
        r = requests.post(url, headers=HEADERS, json=data)

        if r.status_code == 200:
            print("✅ User removal initiated successfully.")
        else:
            print("❌ Error:", r.status_code, r.text)
        print("-" * 60)
        return r.text


if __name__ == "__main__":
    app = DropboxTeamPOC()
    app.list_members()
