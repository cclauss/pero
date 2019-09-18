#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

# import modules
from ...drawing import Graphics
from .canvas import JsonCanvas


class Image(JsonCanvas, Graphics):
    """
    Image represents a combination of pero.JsonCanvas and pero.Graphics. This
    provides access to all the main drawing methods with a possibility to be
    later drawn into any standard canvas. In addition, two convenient methods
    are available as shortcuts to 'export' or 'show' the image using available
    default drawing backend or viewer, depending on requested format.
    """
    
    
    def __init__(self, **overrides):
        """Initializes a new instance of Image."""
        
        super(Image, self).__init__(**overrides)
    
    
    def export(self, path, width=None, height=None, **options):
        """
        Draws the image into specified file using the format determined
        automatically from the file extension. This method makes sure
        appropriate backend canvas is created and provided to the 'draw' method.
        
        Args:
            path: str
                Full path of a file to save the image into.
            
            width: float or None
                Image width in device units. If set to None, current image width
                is used.
            
            height: float or None
                Image height in device units. If set to None, current image
                height is used.
            
            options: str:any pairs
                Additional parameters for specific backend.
        """
        
        # get size
        if width is None:
            width = self.width
        if height is None:
            height = self.height
        
        # export image
        super().export(path, width, height, **options)
    
    
    def show(self, title=None, width=None, height=None):
        """
        Shows the image in available viewer app. This method makes sure
        appropriate backend canvas is created and provided to the 'draw' method.
        
        Args:
            title: str or None
                Viewer frame title.
            
            width: float or None
                Image width in device units. If set to None, current image width
                is used.
            
            height: float or None
                Image height in device units. If set to None, current image
                height is used.
        """
        
        # get size
        if width is None:
            width = self.width
        if height is None:
            height = self.height
        
        # show image
        super().show(title, width, height)
    
    
    def draw(self, canvas, *args, **kwargs):
        """
        Uses given canvas to draw the image.
        
        Args:
            canvas: pero.Canvas
                Canvas to be used for rendering.
        """
        
        canvas.draw_json(self.get_json())
    
    
    @staticmethod
    def from_json(dump):
        """
        Creates a new pero.Image from given JSON dump.
        
        Args:
            dump: str or dict
                Image JSON dump.
        
        Returns:
            pero.Image
        """
        
        return Image().draw_json(dump)
