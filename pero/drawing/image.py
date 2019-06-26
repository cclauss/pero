#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

# import modules
import json
from ..enums import *
from ..colors import Color
from ..properties import UNDEF
from .canvas import Canvas
from .graphics import Graphics


class Image(Canvas, Graphics):
    """
    Special type of drawing canvas, which does not implement any drawing itself
    but provides a way to buffer drawing commands. Its content can either be
    later drawn to specific backend canvas or it can be used to create JSON
    dump.
    
    Since the class is derived from pero.Canvas as well as from pero.Graphics,
    it can also be used as a regular graphics object.
    
    In addition to standard canvas methods, two convenient methods are available
    as shortcuts to 'export' or 'show' the image using available default drawing
    backend/viewer.
    """
    
    
    def __init__(self, **overrides):
        """Initializes a new instance of Image."""
        
        # init buffers
        self._commands = []
        
        # init base
        super(Image, self).__init__()
        
        # bind events
        self.bind(EVENT.PROPERTY_CHANGED, self._on_image_property_changed)
        
        # set overrides
        self.set_properties(overrides)
    
    
    def set_viewport(self, x=None, y=None, width=None, height=None, relative=False):
        """
        Sets rectangular region currently used for drawing. This provides an
        easy way to draw complex graphics at specific position of the
        canvas without adjusting the coordinates of the graphics. It is achieved
        by changing the origin coordinates and the logical width and height of
        the canvas.
        
        Args:
            x: int or float
                X-coordinate of the top-left corner.
            
            y: int or float
                Y-coordinate of the top-left corner.
            
            width: int, float or None
                Full width of the viewport.
            
            height: int, float or None
                Full height of the viewport.
            
            relative: bool
                If set to True the new viewport is applied relative to current
                one.
        """
        
        # set to base
        super(Image, self).set_viewport(x, y, width, height, relative)
        
        # store command
        self._store_command('set_viewport', {
            'x': x,
            'y': y,
            'width': width,
            'height': height,
            'relative': relative})
    
    
    def get_json(self):
        """
        Gets JSON string for current drawings.
        
        Returns:
            str
                Drawings JSON string.
        """
        
        return json.dumps({"commands": self._commands})
    
    
    def draw(self, canvas, *args, **kwargs):
        """
        Uses given canvas to draw the image.
        
        Args:
            canvas: pero.Canvas
                Canvas to be used for rendering.
        """
        
        # draw JSON dump
        canvas.draw_json(self.get_json())
    
    
    def draw_arc(self, x, y, radius, start_angle, end_angle, clockwise=True):
        """
        Draws an arc of specified radius centered around given coordinates.
        
        Args:
            x: int or float
                X-coordinate of the center.
            
            y: int or float
                Y-coordinate of the center.
            
            radius: int or float
                Radius of the arc.
            
            start_angle: int or float
                Angle of the starting point in radians.
            
            end_angle: int or float
                Angle of the starting point in radians.
            
            clockwise: bool
                Direction of drawing between start and end point.
        """
        
        # store command
        self._store_command('draw_arc', {
            'x': x,
            'y': y,
            'radius': radius,
            'start_angle': start_angle,
            'end_angle': end_angle,
            'clockwise': clockwise})
    
    
    def draw_circle(self, x, y, radius):
        """
        Draws a circle of specified radius centered around given coordinates.
        
        Args:
            x: int or float
                X-coordinate of the center.
            
            y: int or float
                Y-coordinate of the center.
            
            radius: int or float
                Radius of the circle.
        """
        
        # store command
        self._store_command('draw_circle', {
            'x': x,
            'y': y,
            'radius': radius})
    
    
    def draw_ellipse(self, x, y, width, height):
        """
        Draws an ellipse centered around given coordinates and fitting into the
        width and height.
        
        Args:
            x: int or float
                X-coordinate of the center.
            
            y: int or float
                Y-coordinate of the center.
            
            width: int or float
                Full width of the ellipse.
            
            height: int or float
                Full height of the ellipse.
        """
        
        # store command
        self._store_command('draw_ellipse', {
            'x': x,
            'y': y,
            'width': width,
            'height': height})
    
    
    def draw_line(self, x1, y1, x2, y2):
        """
        Draws a line between two points.
        
        Args:
            x1: int or float
                X-coordinate of the line start.
            
            y1: int or float
                Y-coordinate of the line start.
            
            x2: int or float
                X-coordinate of the line end.
            
            y2: int or float
                Y-coordinate of the line end.
        """
        
        # store command
        self._store_command('draw_line', {
            'x1': x1,
            'y1': y1,
            'x2': x2,
            'y2': y2})
    
    
    def draw_lines(self, points):
        """
        Draws continuous open line using sequence of points.
        
        Args:
            points: ((float, float),)
                Sequence of x,y coordinates of the points.
        """
        
        # disconnect points
        points = tuple((p[0], p[1]) for p in points)
        
        # store command
        self._store_command('draw_lines', {'points': points})
    
    
    def draw_path(self, path):
        """
        Draws given path using current pen and brush.
        
        Args:
            path: pero.Path
                Path to be drawn.
        """
        
        # get path dump
        path = json.loads(path.json())
        
        # store command
        self._store_command('draw_path', {'path': path})
    
    
    def draw_polygon(self, points):
        """
        Draws a closed polygon using sequence of points.
        
        Args:
            points: ((float, float),)
                Sequence of x,y coordinates of the points.
        """
        
        # disconnect points
        points = tuple((p[0], p[1]) for p in points)
        
        # store command
        self._store_command('draw_polygon', {'points': points})
    
    
    def draw_rect(self, x, y, width, height, radius=None):
        """
        Draws a rectangle specified by given top left corner and size and
        optional round corners specified as a single value or individual value
        for each corners starting from top-left.
        
        Args:
            x: int or float
                X-coordinate of the center.
            
            y: int or float
                Y-coordinate of the center.
            
            width: int or float
                Full width of the rectangle.
            
            height: int or float
                Full height of the rectangle.
            
            radius: int, float, (int,int,int,int) or (float,float,float,float)
                Radius of curved corners.
        """
        
        # store command
        self._store_command('draw_rect', {
            'x': x,
            'y': y,
            'width': width,
            'height': height,
            'radius': radius})
    
    
    def draw_text(self, text, x, y, angle=0):
        """
        Draws a text string anchored at specified point using current text
        settings.
        
        Args:
            text: str
                Text to be drawn.
            
            x: int or float
                X-coordinate of the text anchor.
            
            y: int or float
                Y-coordinate of the text anchor.
            
            angle: int or float
                Text angle in radians.
        """
        
        # store command
        self._store_command('draw_text', {
            'text': text,
            'x': x,
            'y': y,
            'angle': angle})
    
    
    def fill(self):
        """Fills current drawing region by actual fill color."""
        
        # store command
        self._store_command('fill')
    
    
    def clip(self, path):
        """
        Sets clipping path as intersection with current one.
        
        Args:
            path: pero.Path
                Path to be used for clipping.
        """
        
        # get path dump
        path = json.loads(path.json())
        
        # store command
        self._store_command('clip', {'path': path})
    
    
    def unclip(self):
        """Removes last clipping path while keeping previous if any."""
        
        # store command
        self._store_command('unclip')
    
    
    def group(self, id_tag=None, class_tag=None):
        """
        Opens new drawing group.
        
        Args:
            id_tag: str
                Unique id of the group.
            
            class_tag:
                Class of the group.
        """
        
        # store command
        self._store_command('group', {
            'id_tag': id_tag,
            'class_tag': class_tag})
    
    
    def ungroup(self):
        """Closes the last drawing group."""
        
        # store command
        self._store_command('ungroup')
    
    
    def export(self, path, **options):
        """
        Draws the image into specified file using the format determined
        automatically from the file extension. This method makes sure
        appropriate backend canvas is created and provided to the 'draw' method.
        
        Args:
            path: str
                Full path of a file to save the image into.
            
            options: str:any pairs
                Additional parameters for specific backend.
        """
        
        from .. import backends
        backends.export(self, path, self.width, self.height, **options)
    
    
    def show(self, title=None):
        """
        Shows the image in available viewer app. Currently this is only
        available if wxPython is installed or within Pythonista app on iOS. This
        method makes sure appropriate backend canvas is created and provided to
        the 'draw' method.
        
        Args:
            title: str or None
                Viewer frame title.
        """
        
        from .. import backends
        backends.show(self, title, self.width, self.height)
    
    
    def _store_command(self, command, args=None):
        """Stores command and its parameters."""
        
        if args is None:
            args = {}
        
        self._commands.append((command, args))
    
    
    def _on_image_property_changed(self, evt):
        """Called after any property has changed."""
        
        # get value
        value = evt.new_value
        
        # convert UNDEF
        if value is UNDEF:
            value = str(UNDEF)
        
        # convert color
        elif isinstance(value, Color):
            value = value.hex
        
        # store command
        self._store_command('set_property', {
            'name': evt.name,
            'value': value,
            'raise_error': False})
    
    
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
        
        # init image
        img = Image()
        
        # add JSON dump
        img.draw_json(dump)
        
        return img
