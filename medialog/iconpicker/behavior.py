from zope import schema
from zope.interface import Interface
from zope.interface import implements
from plone.directives import form
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides
from zope.i18nmessageid import MessageFactory

from medialog.iconpicker.widgets.widget import IconPickerFieldWidget
from medialog.iconpicker.widgets.widget import ColorPickerFieldWidget

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


class IColorPickerBehavior(form.Schema):
    """ A color field"""
    
    
    color = schema.TextLine(
        title = _("color", default=u"Color"),
        required = False,
        description = _("help_color",
                      default="Choose Color"),
    )

    form.widget(
            color=ColorPickerFieldWidget,
    )

alsoProvides(IColorPickerBehavior, IFormFieldProvider)


