from zope import schema
from zope.interface import Interface
from zope.interface import implements
from plone.supermodel import model
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides
from zope.i18nmessageid import MessageFactory
from plone.autoform.directives import widget

from medialog.iconpicker.widgets.widget import IconPickerFieldWidget
from medialog.iconpicker.widgets.widget import ColorPickerFieldWidget

_ = MessageFactory('medialog.iconpicker')


class IIconPickerBehavior(model.Schema):
    """ A field for icons"""
    
    iconfield = schema.TextLine(
        title = _("icon", default=u"Icon"),
        required = False,
        description = _("help_icon",
                      default="Choose Icon"),
    )

    widget(
            iconfield=IconPickerFieldWidget,
    )

alsoProvides(IIconPickerBehavior, IFormFieldProvider)


class IColorPickerBehavior(model.Schema):
    """ A color field"""
    
    color = schema.TextLine(
        title = _("color", default=u"Color"),
        required = False,
        description = _("help_color",
                      default="Choose Color"),
    )

    widget(
            color=ColorPickerFieldWidget,
    )

alsoProvides(IColorPickerBehavior, IFormFieldProvider)


