class ActionHandler:
    def __init__(self):
        self.actions = {}
    
    def add_actions(self, actionId, func):
        self.actions[actionId] = func

    def execute_action(self, data):
        actionId = data["actionId"]
        self.actions[actionId](data)