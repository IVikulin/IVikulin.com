from sorl.thumbnail.engines.pil_engine import Engine
from django.conf import settings
import os
import logging

logger = logging.getLogger('django')


class CustomEngine(Engine):
    def write(self, image, options, thumbnail):
        super(CustomEngine, self).write(image, options, thumbnail)

        try:
            extension = thumbnail.name.split('.')[-1].lower()
            img = os.path.join(settings.MEDIA_ROOT, thumbnail.name)

            if extension == 'jpg' or extension == 'jpeg':
                os.system('jpegoptim -f --strip-all %s' % img)
            elif extension == 'png':
                os.system('optipng -force -o7 %s' % img)
            elif extension == 'gif':
                call('gifsicle', '-O2 %s > %s' % (img, img))
        except:
            logger.error('Cannot optimize %s' % thumbnail.name)