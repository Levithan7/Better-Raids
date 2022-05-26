import random
from unicodedata import name
import TouchPortalAPI # Import the api
import TouchPortalAPI.client as client
from tpextension import ActionHandler
import requests

# Initiate the client (replace YourPluginID with your ID)
TPClient = TouchPortalAPI.Client("BetterRaids")
handler = ActionHandler()

streamer_states = []
streamer_index = -1

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
    print(streamer_states)

    print("REFRESHED STREAMERS")

    handler.execute_action({"actionId" : "NextStreamerActionId"})

def update_current_streamer():
    global streamer_states
    global streamer_index

    state = streamer_states[streamer_index]["value"]
    streamer_name = streamer_states[streamer_index]["id"]

    TPClient.stateUpdate("CurrentStreamerId", streamer_name)
    TPClient.stateUpdate("CurrentStreamerStateId", state)
    print(f"Updated streamer {streamer_name} to {state}")

def update_next_streamer(data):
    global streamer_index
    global streamer_states
    
    #print("In update: " + str(streamer_states))

    streamer_index += 1
    #print(f"{streamer_index}    {len(streamer_states)}")
    print(len(streamer_states))
    print(streamer_index)
    if streamer_index < len(streamer_states):
        update_current_streamer()
    else:
        streamer_index = -1
        TPClient.stateUpdate("CurrentStreamerId", "NoName")
        TPClient.stateUpdate("CurrentStreamerStateId", "NoState")
        return

# Add actions to Handler
handler.add_actions("StreamersActionId", check_stream)
handler.add_actions("NextStreamerActionId", update_next_streamer)


# Connect to Touch Portal and block (wait) until disconnected
TPClient.connect()