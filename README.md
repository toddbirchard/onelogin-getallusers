# Onelogin - Get All users

Onelogin has a number of interface related issues which make large user exports difficult:

* UI limitation of 5000 users maximum
* Quickly expiring API tokens
* Results paginated at 50 users

This resolves these issues by exporting users to a single CSV.

## Usage

Clone and install dependencies:

```
git clone https://github.com/toddbirchard/onelogin-getallusers.git
cd onelogin-getallusers
pip3 install requests pandas
```

Modify onelogin_config.py with your Client ID and Client Secret:

```
client_id = 'YOUR ID'
client_secret = 'YOUR SECRET'
```

Run script

```
python3 onelogin.py
```
## Future Builds

This repository will be extended to include ways to easily extract from any similar APIs using a simple GUI.
