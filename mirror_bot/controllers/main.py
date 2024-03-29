from typing import List

import pynput

from mirror_bot.controllers import keyboard, mouse
from mirror_bot.interpreters.setence import Setence


class Controller:
    """
    Class responsable for read every setence and
    execute by calling the controller of its type.
    """

    def __init__(self, stream: List[Setence]):
        self.keyboardController = pynput.keyboard.Controller()
        self.mouseController = pynput.mouse.Controller()
        self.stream = stream

    def start(self):
        """Start the main Controller to read and execute every setence."""
        for setence in self.stream:
            if setence.type == "k":
                keyboard.read_setence(self.keyboardController, setence)
            else:
                mouse.read_setence(self.mouseController, setence)
