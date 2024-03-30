########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class stores the notion of Bell-LaPadula
########################################################################

# you may need to put something here...

class BellLaPadulaControl:
    def __init__(self):
        # Define security levels
        self.security_levels = {
            "Public": 0,
            "Confidential": 1,
            "Secret": 2,
            "Privileged": 3
        }

    def can_read(self, user_level, message_level):
        # Check if user can read the message
        return self.security_levels[user_level] >= self.security_levels[message_level]

    def can_write(self, user_level, message_level):
        # Check if user can write to the message
        return self.security_levels[user_level] <= self.security_levels[message_level]