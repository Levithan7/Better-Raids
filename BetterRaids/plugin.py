import random
import TouchPortalAPI # Import the api
import TouchPortalAPI.client as client
from tpextension import ActionHandler
import requests

# Initiate the client (replace YourPluginID with your ID)
TPClient = TouchPortalAPI.Client("BetterRaids")
handler = ActionHandler()

streamer_states = []

# This event handler will run once when the client connects to TouchPortal
@TPClient.on('info')
def onStart(data):
    print('I am Connected!', data)

# Action handlers, called when user activates one of this plugin's actions in Touch Portal.
@TPClient.on('action')
def onActions(data):
    handler.execute_action(data)

# Shutdown handler, called when Touch Portal wants to stop your plugin.
@TPClient.on('closePlugin')
def onShutdown(data):
    print('Received shutdown message!')
    TPClient.disconnect()

# Checks which streamers are online
def check_stream(data):
    global streamer_states

    names = data["data"][0]["value"].split(",")
    state_dict = []

    for channelName in names:
        contents = requests.get('https://www.twitch.tv/' + channelName).content.decode('utf-8')
        checkName = "isLiveBroadcast"

        state_dict.append({
            "id" : channelName,
            "value" : "Online" if checkName in contents else "Offline"
        })

    streamer_states = state_dict
    TPClient.stateUpdateMany(streamer_states)

    print("REFRESHED STREAMERS")

# Creates values for every streamer and sets it to "NoState"
# If a value already exists, it will be set to "NoState"
def create_values(data):
    names = names = data["data"][0]["value"].split(",")
    for name in names:
        TPClient.createState(name, f"{name} state", "NoState")

    for name in names:
        TPClient.stateUpdate(name, "NoState")
    print("CREATED STREAMERS")

# Add actions to Handler
handler.add_actions("StreamersActionId", check_stream)
handler.add_actions("CreateId", create_values)


# Connect to Touch Portal and block (wait) until disconnected
TPClient.connect()