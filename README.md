# 📦 Dropbox Team Automation 

This project automates **user lifecycle management** for Dropbox Business Teams using the **Dropbox Business API**.

It includes:
- 👥 Listing all team members
- ➕ Provisioning (inviting) new users
- ➖ Deprovisioning (removing) existing users

The POC demonstrates how SaaS user management can be automated using Python and Dropbox APIs, a core requirement for SaaS lifecycle automation systems like **CloudEagle**.

---

## Features

| Feature | Description |
|----------|--------------|
| **List Members** | Fetch all existing Dropbox Business team members. |
| **Provision Users** | Invite new users to the team via API. |
| **Deprovision Users** | Remove existing or invited users using their `team_member_id`. |
| **Environment Configurable** | Uses `.env` for tokens and IDs to keep credentials secure. |
| **Readable Output** | Console outputs formatted in a clean, human-readable format. |

---

## 🛠️ Tech Stack

- **Python 3.12+**
- **Dropbox Business API**
- **Requests**
- **Dotenv**

---

## 📂 Folder Structure
dropbox-team-poc/

├── .env # Stores Dropbox token and team ID

├── dropbox_team_api.py # Main logic for list, invite, and remove users

├── find_and_remove.py # Helper script to find user ID by email

├── README.md # You’re reading this file

└── requirements.txt # Dependencies (optional)

## 🔧 Prerequisites

1. **Dropbox Business Account**
   - Go to [Dropbox App Console](https://www.dropbox.com/developers/apps)
   - Create an app under **Dropbox Business API**
   - Choose **Team Member Management** access
   - Enable the following scopes:
     - `team_info.read`
     - `members.read`
     - `members.add`
     - `members.delete`
   - Generate an **Access Token**

2. **Environment Setup**
   - Install dependencies:
     ```bash 
        pip install python-dotenv requests
     ```
   - Create a `.env` file:
     ```bash
     DROPBOX_TOKEN=sl.u.<your_access_token_here>
     DROPBOX_TEAM_ID=dbtid:<your_team_id_here>
     ```
---

## ⚙️ Setup and Usage

### 1 Activate Environment
```bash
cd ~/Desktop/dropbox-team-poc
export DROPBOX_TOKEN=$(grep DROPBOX_TOKEN .env | cut -d'=' -f2-)
export DROPBOX_TEAM_ID=$(grep DROPBOX_TEAM_ID .env | cut -d'=' -f2-)
```
### 2 List All Memebers
```bash
python dropbox_team_api.py
```
### 3 Povision A User
```bash
python 
```
Then in the Python shell:
```bash
>>>from dropbox_team_api import DropboxTeamPOC
>>>p = DropboxTeamPOC()
>>>p.invite_user("newuser@example.com", "FirstName", "LastName")
```

### 4 De-provision A User
First, find the user’s team_member_id:
```bash
python find_and_remove.py
```
Then remove the user:
```bash
python 
```
Then in the Python shell:
```bash
>>>from dropbox_team_api import DropboxTeamPOC
>>>p = DropboxTeamPOC()
>>>p.remove_user("dbmid:AAD0useTduC96M4wsXspFiFx-UdzxJ5_h14")
```

### 5 Verify Updated Team List
```bash
python dropbox_team_api.py
```

## API Endpoints Used
Action	                    Endpoint	                Method

List Members	            /2/team/members/list_v2	    POST

Add (Invite) Member	        /2/team/members/add	        POST

Remove Member	            /2/team/members/remove	    POST

Get Team Info	            /2/team/get_info	        POST