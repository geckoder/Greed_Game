from game.casting.actor import Actor
from game.directing.director import Director


class Artifact(Actor):
    """
    An item of cultural or historical interest. 

    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
        _score (integer): The score given to the artifact.
    """

    def __init__(self):
        super().__init__()
        self._message = ""
        self._score = 0

    def get_score(self):
        """Gets the artifact's score.

        Returns:
            integer: The score.
        """
        return self._score

    def set_score(self):
        """Updates the score to the given one.

        Args:
            score (integer): The given score.
        """
        self._score += 1

    def get_message(self):
        """Gets the artifact's message.

        Returns:
            string: The message.
        """
        return self._message

    def set_message(self):
        """Updates the message to the given one.

        Args:
            message (string): The given message.
        """
        self._message = f"Score: {self._score} "
