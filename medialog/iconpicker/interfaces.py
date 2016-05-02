# -*- coding: utf-8 -*-
# Default ENCODING = 'UTF-8'

####################
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
    https://erikflowers.github.io/weather-icons/
	http://www.typicons.com/
	https://octicons.github.com/
	http://ionicons.com/
	http://elusiveicons.com/cheatsheet/
	https://fortawesome.github.io/Font-Awesome/icons/
	http://map-icons.com/
    """

    form.fieldset(
        'iconpicker',
        label=_(u'Iconpicker settings'),
        fields=[
             'iconset',
             'cols',
             'rows',
             'placement',
             'loadbootstrap',
        ],
     )

    iconset = schema.Choice(
        title=_(u"label_iconset", default=u"Iconset"),
        description=_(u"help_iconset", 
        default=u"""Choose iconset to be used for iconpicker.Some links: 
        <a href="https://erikflowers.github.io/weather-icons/">Weather-icons</a> • 
        <a href="http://www.typicons.com">Typicons</a> • 
        <a href="https://octicons.github.com/">Octicons</a> •  
        <a href="http://ionicons.com/">Ionicons</a>  • 
        <a href="">http://elusiveicons.com/cheatsheet/</a>  • 
        <a href="https://fortawesome.github.io/Font-Awesome/icons/">Font Awsome</a>  •  
        <a href="http://map-icons.com/">map-icons</a>
        """),
        values=[('glyphicon'), ('ionicon'), ('fontawesome'), ('weathericon'), ('mapicon'), ('octicon'), ('typicon'), ('elusiveicon'),]
    )
    
    loadbootstrap = schema.Bool(
     	title=_(u"label_loadbootstrap", default=u"Load Bootstrap"),
        description=_(u"help_loadbootstrap", 
            default=u"""Loads ++resource++collective.js.bootstrap/js/bootstrap.min.js. <br/>
            You probably want to do this in your diazo theme instead.""")
    )
        
    cols = schema.Int (
    	title=_(u"label_columns", default=u"Columns"),
    )
    
    rows = schema.Int (
    	title=_(u"label_rows", default=u"Rows"),
    )

    placement = schema.Choice(
        title=_(u"label_placement", default=u"Placement"),
        values=[('left'), ('top'), ('bottom'), ('right'),]
    )

        
alsoProvides(IIconPickerSettings, IMedialogControlpanelSettingsProvider)