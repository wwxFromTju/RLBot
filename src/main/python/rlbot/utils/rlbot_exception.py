class RLBotException(Exception):
    """Base class for exceptions in this module."""

    def __init__(self, msg=None):
        if msg is None:
            # Set some default useful error message
            msg = "An error occurred attempting to set RLBot configuration on the dll side"
        super(RLBotException, self).__init__(msg)
        self.error_dict = {1: BufferOverfilledError(), 2: MessageLargerThanMaxError(), 3: InvalidNumPlayerError(),
                           4: InvalidBotSkillError(), 5: InvalidPlayerIndexError(), 6: InvalidName(),
                           7: InvalidTeam, 8: InvalidTeamColor(), 9: InvalidCustomColor, 10: InvalidGameValues,
                           11: InvalidThrottle, 12: InvalidSteer, 13: InvalidPitch, 14: InvalidRoll,
                           15: InvalidSteer}

    def raise_exception_from_error_code(self, error_code):
        try:
            return self.error_dict[error_code]
        except KeyError:
            return self


class BufferOverfilledError(RLBotException):
    def __init__(self):
        super(RLBotException, self).__init__("Buffer overfilled")


class MessageLargerThanMaxError(RLBotException):
    def __init__(self):
        super(RLBotException, self).__init__("Message larger than max")


class InvalidNumPlayerError(RLBotException):
    def __init__(self):
        super(RLBotException, self).__init__("Invalid number of cars specified in configuration")


class InvalidBotSkillError(RLBotException):
    def __init__(self):
        super(RLBotException, self).__init__("Invalid bot skill specified in configuration")


class InvalidPlayerIndexError(RLBotException):
    def __init__(self):
        super(RLBotException, self).__init__("Invalid player index")


class InvalidName(RLBotException):
    def __init__(self):
        super(RLBotException, self).__init__("Invalid name error. Python side was supposed to properly sanitize this!")


class InvalidTeam(RLBotException):
    def __init__(self):
        super(RLBotException, self).__init__("Invalid team specified in configuration")


class InvalidTeamColor(RLBotException):
    def __init__(self):
        super(RLBotException, self).__init__("Invalid team color specified")


class InvalidCustomColor(RLBotException):
    def __init__(self):
        super(RLBotException, self).__init__("Invalid custom color specified")


class InvalidGameValues(RLBotException):
    def __init__(self):
        super(RLBotException, self).__init__("Invalid game values")


class InvalidThrottle(RLBotException):
    def __init__(self):
        super(RLBotException, self).__init__("Invalid throttle input")


class InvalidSteer(RLBotException):
    def __init__(self):
        super(RLBotException, self).__init__("Invalid steer input")


class InvalidPitch(RLBotException):
    def __init__(self):
        super(RLBotException, self).__init__("Invalid pitch input")


class InvalidYaw(RLBotException):
    def __init__(self):
        super(RLBotException, self).__init__("Invalid yaw input")


class InvalidRoll(RLBotException):
    def __init__(self):
        super(RLBotException, self).__init__("Invalid roll input")
