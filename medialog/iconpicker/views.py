from Products.Five import BrowserView
from plone import api
from medialog.iconpicker.interfaces import IIconPickerSettings

class FontLoad(BrowserView):
    """ """
    
    def value(self):
    	return self.context

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
        return 'fa'
        

    def iconset(self):
        """Returns current iconset name This is also used for loading the resources below"""
        return api.portal.get_registry_record('medialog.iconpicker.interfaces.IIconPickerSettings.iconset')
        
    def glyphicon(self):
        return """
        <script type="text/javascript" src="++resource++medialog.iconpicker/bootstrap-iconpicker/js/iconset/iconset-glyphicon.min.js"></script>
        """

    def fontawesome(self):
        return """
        <script type="text/javascript" src="++resource++medialog.iconpicker/bootstrap-iconpicker/js/iconset/iconset-fontawesome-4.2.0.js"></script>
        <link rel="stylesheet" href="++resource++medialog.iconpicker/icon-fonts/font-awesome-4.2.0/css/font-awesome.min.css"/>
        """
        
    def  mapicon(self):
        return """
        <link rel="stylesheet" href="++resource++medialog.iconpicker/icon-fonts/map-icons-2.1.0/css/map-icons.min.css"/>
        <script type="text/javascript" src="++resource++medialog.iconpicker/bootstrap-iconpicker/js/iconset/iconset-mapicon-2.1.0.min.js"></script>
        """

    def typicon(self):
        return """
        <link rel="stylesheet" href="++resource++medialog.iconpicker/icon-fonts/typicons-2.0.6/css/typicons.min.css"/>
        <script type="text/javascript" src="++resource++medialog.iconpicker/bootstrap-iconpicker/js/iconset/iconset-typicon-2.0.6.min.js"></script>
        """
        
    def ionicon(self):
       return """
        <link rel="stylesheet" href="++resource++medialog.iconpicker/icon-fonts/ionicons-1.5.2/css/ionicons.min.css"/>
        <script type="text/javascript" src="++resource++medialog.iconpicker/bootstrap-iconpicker/js/iconset/iconset-ionicon-1.5.2.min.js"></script>
       """
    
    def weathericon(self):
        return """
        <link rel="stylesheet" href="++resource++medialog.iconpicker/icon-fonts/weather-icons-1.2.0/css/weather-icons.min.css"/>
        <script type="text/javascript" src="++resource++medialog.iconpicker/bootstrap-iconpicker/js/iconset/iconset-weathericon-1.2.0.min.js"></script>
        """
            
    def octicon(self):
        return """
        <link rel="stylesheet" href="++resource++medialog.iconpicker/icon-fonts/octicons-2.1.2/css/octicons.min.css"/>
        <script type="text/javascript" src="++resource++medialog.iconpicker/bootstrap-iconpicker/js/iconset/iconset-octicon-2.1.2.min.js"></script>
        """
    
    def elusiveicon(self):
        return """
        <link rel="stylesheet" href="++resource++medialog.iconpicker/icon-fonts/elusive-icons-2.0.0/css/elusive-icons.min.css"/>
        <script type="text/javascript" src="++resource++medialog.iconpicker/bootstrap-iconpicker/js/iconset/iconset-elusiveicon-2.0.0.min.js"></script>
        """

    def color(self):
        context = self.context
        color = getattr(context, "color", None)
        if color: 
            return '#' + color
        return "inherit"