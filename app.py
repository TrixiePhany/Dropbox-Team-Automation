import streamlit as st
from dropbox_team_api import DropboxTeamPOC

st.set_page_config(page_title="Dropbox Team Automation", page_icon="📦")

st.title("Dropbox Team Automation Dashboard")
st.caption("Automated Provisioning, Deprovisioning, and Member Listing via Dropbox Business API")

#  class
app = DropboxTeamPOC()

# Sidebar options
action = st.sidebar.selectbox("Select Action", ["List Members", "Invite Member", "Remove Member"])

if action == "List Members":
    st.subheader("👥 Current Team Members")
    members = app.list_members(limit=50)
    if members:
        for m in members:
            profile = m.get("profile", {})
            st.write(f"**{profile.get('name', {}).get('display_name', '(No Name)')}** - {profile.get('email')}")
            st.caption(f"Status: {profile.get('status', {}).get('.tag', 'unknown')}")

elif action == "Invite Member":
    st.subheader("➕ Invite a New Member")
    email = st.text_input("Email")
    fname = st.text_input("First Name")
    lname = st.text_input("Last Name")
    if st.button("Send Invite"):
        if email:
            resp = app.invite_user(email, fname, lname)
            st.json(resp)
        else:
            st.warning("Please enter an email address.")

elif action == "Remove Member":
    st.subheader("🗑️ Remove a Member")
    member_id = st.text_input("Team Member ID")
    if st.button("Remove User"):
        if member_id:
            resp = app.remove_user(member_id)
            st.json(resp)
        else:
            st.warning("Please enter a valid Team Member ID.")
