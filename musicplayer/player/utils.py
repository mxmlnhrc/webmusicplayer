import musicplayer.settings as settings, os
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError


def check_format(file):
    if '.mp3' in file or '.wav' in file or '.ogg' in file:
        return file
    else:
        raise ValidationError(
            "This Field only accepts .mp3, .wav or .ogg files.")
