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
    
    @property
    def iconset():
        """Returns current iconset name This is also used for loading the resources below"""
        import pdb; pdb.set_trace()
        return api.portal.get_registry_record('medialog.iconpicker.interfaces.IIconPickerSettings.iconset')
    
alsoProvides(IIconPickerBehavior, IFormFieldProvider)


