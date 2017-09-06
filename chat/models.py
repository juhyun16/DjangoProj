import json
from django.db import models
from django.utils.six import python_2_unicode_compatible
from channels import Group
from django.utils import timezone
from .settings import MSG_TYPE_MESSAGE
from django.contrib.auth import get_user_model

@python_2_unicode_compatible
class Room(models.Model):
    """
    A room for people to chat in.
    """

    # Room title
    title = models.CharField(max_length=255)

    # If only "staff" users are allowed (is_staff on django's User)
    staff_only = models.BooleanField(default=False)

    users=models.ManyToManyField(get_user_model())


    def __str__(self):
        return self.title


    @property
    def websocket_group(self):
        """
        Returns the Channels Group that sockets should subscribe to to get sent
        messages as they are generated.
        """
        return Group("room-%s" % self.id)


    def send_message(self, message, user, msg_type=MSG_TYPE_MESSAGE):
        """
        Called to send a message to the room on behalf of a user.
        """
        final_msg = {'room': str(self.id), 'message': message, 'username': user.username, 'msg_type': msg_type}

        # Send out the message to everyone in the room
        self.websocket_group.send(
            {"text": json.dumps(final_msg)}
        )


class Message(models.Model):
    room=models.ForeignKey(Room, related_name="messages")
    handle=models.TextField()
    message=models.TextField()
    timestamp=models.DateTimeField(default=timezone.now)


    def as_dict(self):
        return {"handle":self.handle, "message":self.message, "timestamp": self.timestamp}


    def __str__(self):
        return "[{timestamp}] {handle}: {message}".format(**self.as_dict())


    @property
    def formatted_timestamp(self):
        return self.timestamp.strftime("%b %-d %-I:%M %p")

