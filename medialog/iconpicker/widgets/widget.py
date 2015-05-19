import zope.component
import zope.interface
import zope.schema.interfaces

from z3c.form import interfaces
from z3c.form import widget
from z3c.form.browser import text


class IIconPickerWidget(interfaces.IWidget):
    """Iconpicker widget."""
 

class IconPickerWidget(text.TextWidget):
    """Iconpicker code is double here, must check."""
    
    
    zope.interface.implementsOnly(IIconPickerWidget)
    

    
    
 
def IconPickerFieldWidget(field, request):
    """IFieldWidget factory for IconPickerWidget."""
    return widget.FieldWidget(field, IconPickerWidget(request))
