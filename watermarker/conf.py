# -*- coding: utf-8 -*-

import warnings

from django.conf import settings  # pylint: disable=W0611

from appconf import AppConf


class WatermarkSettings(AppConf):
    """
    Define local app config.
    """
    QUALITY = 85
    OBSCURE_ORIGINAL = True
    RANDOM_POSITION_ONCE = True
    WATERMARK_PERCENTAGE = 40
    WATERMARK_QUALITY = 85
    WATERMARK_CACHE_BACKEND_NAME = None
    WATERMARK_OBSCURE_ORIGINAL = True
    WATERMARK_RANDOM_POSITION_ONCE = True

    class Meta:
        prefix = 'watermark'
        holder = 'watermarker.conf.settings'

    def configure_quality(self, value):
        if getattr(settings, 'WATERMARKING_QUALITY', None):
            warnings.warn(
                'WATERMARKING_QUALITY is deprecated, use WATERMARK_QUALITY',
                DeprecationWarning)

        return value
