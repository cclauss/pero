#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

# import modules
import fitz
from .canvas import MuPDFCanvas


def export(graphics, path, width, height, **options):
    """
    Draws given graphics as PDF document into specified file.
    
    Args:
        graphics: pero.Graphics
            Graphics to be drawn.
        
        path: str
            Full path of a file to save the image into.
        
        width: float
            Image width in device units.
        
        height: float
            Image height in device units.
        
        line_scale: float
            Line scaling factor.
        
        font_scale: float
            Font scaling factor.
    """
    
    # init document
    doc = fitz.open()
    page = doc.newPage(width=width, height=height)
    
    # init canvas
    canvas = MuPDFCanvas(page)
    
    if 'line_scale' in options:
        canvas.line_scale = options['line_scale']
    
    if 'font_scale' in options:
        canvas.font_scale = options['font_scale']
    
    # draw graphics
    graphics.draw(canvas)
    
    # save to file
    doc.save(path)
    doc.close()
