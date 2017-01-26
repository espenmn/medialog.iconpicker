# -*- coding: utf-8 -*-
from plone.app.theming.utils import isThemeEnabled
from plone.app.tiles.browser.add import DefaultAddForm
from plone.app.tiles.browser.add import DefaultAddView
from plone.app.tiles.browser.edit import DefaultEditForm
from plone.app.tiles.browser.edit import DefaultEditView
from plone.memoize.view import memoize
from plone.supermodel import model
from plone.directives import form
from plone.tiles import Tile
from plone.tiles.data import TransientTileDataManager
from plone.tiles.interfaces import ITileDataManager
from zope import schema
from zope.i18nmessageid import MessageFactory
from zope.interface import provider

_ = MessageFactory('medialog.iconpicker')

 
 
 
from medialog.iconpicker.widgets.widget import IconPickerFieldWidget
from medialog.iconpicker.widgets.widget import ColorPickerFieldWidget




class IIconTile(model.Schema):
    iconfield = schema.TextLine(
        title = _("icon", default=u"Icon"),
        required = False,
        description = _("help_icon",
                      default="Choose Icon"),
    )

    form.widget(
            iconfield=IconPickerFieldWidget,
    )

    
    color = schema.TextLine(
        title = _("color", default=u"Color"),
        required = False,
        description = _("help_color",
                      default="Choose Color"),
    )

    form.widget(
            color=ColorPickerFieldWidget,
    )
    
    title =schema.TextLine(
        title = _("title", default=u"Title"),
        required = False,
        description = _("help_tittel",
                      default="Title"),
    )

    text =schema.TextLine(
        title = _("text", default=u"Text"),
        required = False,
        description = _("help_text",
                      default="Text"),
    )


class FragmentTile(Tile):
    """A tile that displays icon and some text"""

    def __call__(self):
        self.update()
        return 'xxx'	

