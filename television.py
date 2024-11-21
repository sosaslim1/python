class Television:
    # Class variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        # Instance variables (all private)
        self.__status = False  # Television is off initially
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        # Toggle the power status
        self.__status = not self.__status

    def mute(self):
        # Toggle the muted status, but only if the TV is on
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        # Increase the channel by 1, wrap to MIN_CHANNEL if it reaches MAX_CHANNEL
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        # Decrease the channel by 1, wrap to MAX_CHANNEL if it reaches MIN_CHANNEL
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        # Increase the volume by 1, unmute if muted, stay within MAX_VOLUME
        if self.__status:
            if self.__muted:
                self.__muted = False  # Unmute if muted
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        # Decrease the volume by 1, unmute if muted, stay within MIN_VOLUME
        if self.__status:
            if self.__muted:
                self.__muted = False  # Unmute if muted
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        # Return the string representation of the TV state
        volume_display = Television.MIN_VOLUME if self.__muted else self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {volume_display}"


