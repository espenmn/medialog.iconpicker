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
             'cols',
             'rows',
             'placement',
             'loadbootstrap',
        ],
     )

    iconset = schema.Choice(
        title=_(u"label_iconset", default=u"Iconset"),
        description=_(u"help_iconset", default=u"Choose iconset to be used for iconpicker"),
        values=[('glyphicon'), ('ionicon'), ('fontawesome'), ('weathericon'), ('mapicon'), ('octicon'), ('typicon'), ('elusiveicon'),]
        )
    
    loadbootstrap = schema.Bool (
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
        values=[('top'), ('bottom'), ('right'),]
        )

        
alsoProvides(IIconPickerSettings, IMedialogControlpanelSettingsProvider)