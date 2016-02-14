import gettext

from pelican import signals

_GENERATOR_DB = {}


def init_generator(generator):
    _GENERATOR_DB[generator] = []


def translate(pelican_obj):
    for generator in _GENERATOR_DB.keys():
        if 'jinja2.ext.i18n' in generator.settings['JINJA_EXTENSIONS']:
            domain = generator.settings.get('I18N_GETTEXT_DOMAIN', 'messages')
            localedir = generator.settings.get('I18N_GETTEXT_LOCALEDIR')
            langs = [generator.settings.get('DEFAULT_LANG')]
            try:
                translations = gettext.translation(domain, localedir, langs)
            except (IOError, OSError):
                translations = gettext.NullTranslations()
            generator.env.install_gettext_translations(translations, True)


def register():
    signals.generator_init.connect(init_generator)
    signals.get_writer.connect(translate)
