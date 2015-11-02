from zope import schema
from zope.interface import Interface
from zope.interface import implements
from plone.directives import form
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides
from zope.i18nmessageid import MessageFactory

from medialog.iconpicker.widgets.widget import IconPickerFieldWidget

_ = MessageFactory('medialog.iconpicker')


from plone import api
from medialog.iconpicker.interfaces import IIconPickerSettings




from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider


@provider(IFormFieldProvider)
class IIconPickerBehavior(model.Schema):
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
    
    
#alsoProvides(IIconPickerBehavior, IFormFieldProvider)




@implementer(IconPickerBehavior)
class IconPickerBehavior(object):
    """
    properties to be used in listing views 
    """
    
    def __init__(self, context):
        self.context = context

    @property
    def iconset(self):
        """Returns current iconset name This is also used for loading the resources below"""
        import pdb; pdb.set_trace()
        return api.portal.get_registry_record('medialog.iconpicker.interfaces.IIconPickerSettings.iconset')
  
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
        

   