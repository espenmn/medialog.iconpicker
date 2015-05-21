from z3c.form import interfaces
from zope import schema
#from zope.interface import Interface
from zope.interface import alsoProvides
from plone.directives import form
from medialog.controlpanel.interfaces import IMedialogControlpanelSettingsProvider

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('medialog.iconpicker')

class IIconPickerSettings(form.Schema):
    """Adds settings to medialog.controlpanel
    """

    form.fieldset(
        'iconpicker',
        label=_(u'Iconpicker settings'),
        fields=[
             'iconset',
        ],
     )

    iconset = schema.TextLine(
        title=_(u"label_iconset", default=u"Iconset"),
        description=_(u"help_iconset",
        default=u"Choose iconset to be used for iconpicker")
        )

alsoProvides(IIconPickerSettings, IMedialogControlpanelSettingsProvider)