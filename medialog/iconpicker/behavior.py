from zope import schema
#from plone.directives import dexterity
from plone.directives import form
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides
from zope.i18nmessageid import MessageFactory

from medialog.iconpicker.widgets.widget import IconPickerWidget

_ = MessageFactory('medialog.iconpicker')


class IIconPicker(form.Schema):
    """ A field for icons"""
    
    
    icon = schema.TextLine(
        title = _("icon", default=u"Icon"),
        description = _("help_icon",
                      default="Choose SIcon"),
    )

    form.widget(
            icon=IconPickerWidget
    )

alsoProvides(IIconPicker, IFormFieldProvider)

