import django


def settings(request):
    return {
            'STADTGESTALTEN_LOGO_URL': django.conf.settings.STADTGESTALTEN_LOGO_URL,
            'STADTGESTALTEN_SHOW_HEADER': django.conf.settings.STADTGESTALTEN_SHOW_HEADER,
            }