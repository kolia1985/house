from django.dispatch import Signal


# A user has activated his or her account.
user_activated = Signal(providing_args=["user"])
