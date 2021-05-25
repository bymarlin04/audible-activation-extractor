#!/usr/bin/env python3
import readline
import audible
import audible.activation_bytes
import os

try:
    LOCALE = os.environ["AUDIBLE_LOCALE"]
except KeyError:
    LOCALE = "DE"

auth = audible.Authenticator.from_login_external(locale=LOCALE)
auth.register_device()
auth_bytes = audible.activation_bytes.get_activation_bytes(auth)
auth.deregister_device()

print("Activation bytes: " + str(auth_bytes))