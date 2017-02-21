# -*- coding: utf-8 -*-

from plone import api
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
#from zope.interface import provider


#????
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.publisher.browser import BrowserView
from zope.schema import getFields
from plone.tiles.interfaces import ITileType


from collective.z3cform.datagridfield import DataGridFieldFactory 
from collective.z3cform.datagridfield import DictRow


_ = MessageFactory('medialog.iconpicker')

 
from medialog.iconpicker.widgets.widget import IconPickerFieldWidget
from medialog.iconpicker.widgets.widget import ColorPickerFieldWidget
from medialog.iconpicker.interfaces import IIconPickerSettings


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
     
    link = schema.URI(title=u"Link",
      required = False,
    )
    
    
    css_class =schema.TextLine(
        title = _("css class", default=u"CSS class"),
        required = False,
        description = _("help_css_class",
                      default="CSS Class"),
    )
    


class IconTile(Tile):
    """A tile that displays icon and some text"""

    def __init__(self, context, request):
        super(IconTile, self).__init__(context, request)
        
    @property
    def data(self):
        data = super(IconTile, self).data
        return data
        
    @property
    def family_css(self):
        #return css_family_class, like fa, wi
        iconset = self.iconset()
        if iconset == 'glyphicon':
             return 'glyphicon'
        if iconset == 'mapicon':
            return 'map-icons'
        if iconset == 'typicon':
            return 'typcn'
        if iconset == 'ionicon':
            return 'ionicons'
        if iconset == 'weathericon':
            return 'wi'
        if iconset == 'octicon' :
            return 'octicon'
        if iconset == 'elusiveicon':
            return 'el-icon'
        if iconset == 'medialogfont':
            return 'medialogfont-icon'
        
        return 'fa'
        
    def iconset(self):
        """Returns current iconset name This is also used for loading the resources below"""
        return api.portal.get_registry_record('medialog.iconpicker.interfaces.IIconPickerSettings.iconset')
        
        
        
#class IconTileAddView(DefaultAddView):
#    form = IconTileAddForm


#class IconTileEditView(DefaultEditView):
#    form = IconTileEditForm















class IPair(model.Schema):
    iconfield = schema.TextLine(
        title = _("icon", default=u"Icon"),
        required = False,
        description = _("help_icon",
                      default="Choose Icon"),
    )

    form.widget(
            iconfield=IconPickerFieldWidget,
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
    
    
class IMultiIconTile(model.Schema):
    
    color = schema.TextLine(
        title = _("color", default=u"Color"),
        required = False,
        description = _("help_color",
                      default="Choose Color"),
    )

    form.widget(
            color=ColorPickerFieldWidget,
    )
    
    
    css_class =schema.TextLine(
        title = _("css class", default=u"CSS class"),
        required = False,
        description = _("help_css_class",
                      default="CSS Class"),
    )
    
    form.widget(iconpairs=DataGridFieldFactory)
    iconpairs = schema.List(
        title = _(u"icon text_pairs", 
            default=u"Icon Text pairs"),
        value_type= DictRow(schema=IPair),
        required=False
    )