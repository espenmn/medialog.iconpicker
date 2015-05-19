from zope import schema
#from plone.directives import dexterity
from plone.directives import form
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides
from zope.i18nmessageid import MessageFactory

from medialog.iconpicker.widgets.widget import IconPickerFieldWidget

_ = MessageFactory('medialog.iconpicker')


class IIconPickerBehavior(form.Schema):
    """ A field for icons"""
    
    
    iconfield = schema.TextLine(
        title = _("icon", default=u"Icon"),
        required = False,
        description = _("help_icon",
                      default="Choose Icon"),
    )

    form.widget(
            iconfield=IconPickerFieldWidget,
    )

alsoProvides(IIconPickerBehavior, IFormFieldProvider)

