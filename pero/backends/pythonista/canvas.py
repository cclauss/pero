#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

# import modules
import ui
from ...properties import *
from ...colors import Transparent, Black
from ...drawing import Canvas, Matrix
from .enums import *


class UICanvas(Canvas):
    """Pythonista UI drawing canvas."""
    
    
    def __init__(self, **overrides):
        """
        Initializes a new instance of UICanvas.
        
        Args:
            overrides: str:any pairs
                Value overwrites for specific properties.
        """
        
        # init buffers
        self._pen = {
            'color': Transparent,
            'width': 1,
            'cap': PYTHONISTA_LINE_CAP[LINE_CAP.ROUND],
            'join': PYTHONISTA_LINE_JOIN[LINE_JOIN.MITER],
            'dash': []}
        
        self._brush = Transparent
        
        self._font = {
            'name': '<system>',
            'size': 10,
            'for_color': Black,
            'bgr_color': Transparent}
        
        self._clipping = []
        
        # set font factor
        if 'font_factor' not in overrides:
            overrides['font_factor'] = 1.33
        
        # init base
        super(UICanvas, self).__init__(**overrides)
        
        # init canvas
        self._update_pen()
        self._update_brush()
        self._update_text()
        
        # bind events
        self.bind(EVENT.PEN_CHANGED, self._update_pen)
        self.bind(EVENT.BRUSH_CHANGED, self._update_brush)
        self.bind(EVENT.TEXT_CHANGED, self._update_text)
    
    
    def get_line_size(self, text):
        """
        Gets width and height of a single text line using current text settings.
        
        Args:
            text: str
                Text for which the size should be calculated.
        
        Returns:
            (float, float)
                Line width and height.
        """
        
        # check text
        if not text:
            return 0, 0
        
        # get size
        return ui.measure_string(text, font=(self._font['name'], self._font['size']))
    
    
    def draw_path(self, path):
        """
        Draws given path using current pen and brush.
        
        Args:
            path: pero.Path
                Path to be drawn.
        """
        
        # apply scaling and offset
        matrix = Matrix()
        matrix.translate(self._offset[0], self._offset[1])
        matrix.scale(self._scale[0], self._scale[1])
        path = path.transformed(matrix)
        
        # make ui path
        ui_path = self._make_native_path(path)
        
        # apply fill
        if self._brush.alpha:
            
            ui.set_color(self._brush.rgba_r)
            ui_path.eo_fill_rule = PYTHONISTA_FILL_RULE[path.fill_rule]
            ui_path.fill()
        
        # apply stroke
        if self._pen['color'].alpha:
            
            ui.set_color(self._pen['color'].rgba_r)
            ui_path.line_width = self._pen['width']
            ui_path.line_cap_style = self._pen['cap']
            ui_path.line_join_style = self._pen['join']
            ui_path.set_line_dash(self._pen['dash'])
            ui_path.stroke()
    
    
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
        
        # get full size
        full_width, full_height = self.get_text_size(text)
        
        # split lines
        lines = [text]
        if self.text_split and self.text_splitter:
            lines = text.split(self.text_splitter)
        
        # draw text and background
        with ui.GState():
            
            # apply angle transformation
            if angle:
                
                x = self._scale[0] * (x + self._offset[0])
                y = self._scale[1] * (y + self._offset[1])
                
                ui.concat_ctm(ui.Transform.translation(x, y))
                ui.concat_ctm(ui.Transform.rotation(angle))
                
                x = 0
                y = 0
            
            # draw lines
            for i, line in enumerate(lines):
                
                # init offset
                x_offset = 0
                y_offset = 0
                
                # get line size
                line_width, line_height = self.get_line_size(line)
                line_width /= self._scale[0]
                line_height /= self._scale[1]
                
                # adjust alignment
                if self.text_align == TEXT_ALIGN.CENTER:
                    x_offset -= 0.5*line_width
                
                elif self.text_align == TEXT_ALIGN.RIGHT:
                    x_offset -= line_width
                
                # adjust baseline
                if self.text_base == TEXT_BASELINE.MIDDLE:
                    y_offset -= 0.5*full_height
                
                elif self.text_base == TEXT_BASELINE.BOTTOM:
                    y_offset -= full_height
                
                # add line offset
                y_offset += i * line_height * (1 + self.text_spacing)
                
                # apply scaling and offset
                text_x = self._scale[0] * (x + x_offset + self._offset[0])
                text_y = self._scale[1] * (y + y_offset + self._offset[1])
                bgr_width = line_width * self._scale[0]
                bgr_height = line_height * self._scale[1]
                
                # draw background
                if self._font['bgr_color'].alpha:
                    
                    ui.set_color(self._font['bgr_color'].rgba_r)
                    ui.fill_rect(text_x, text_y, bgr_width, bgr_height)
                
                # draw text
                if self._font['for_color'].alpha:
                    
                    ui.draw_string(line,
                        rect = (text_x, text_y, 0, 0),
                        font = (self._font['name'], self._font['size']),
                        color = self._font['for_color'].rgba_r,
                        alignment = ui.ALIGN_LEFT,
                        line_break_mode = ui.LB_WORD_WRAP)
    
    
    def clip(self, path):
        """
        Sets clipping path as intersection with current one.
        
        Args:
            path: pero.Path
                Path to be used for clipping.
        """
        
        # apply scaling and offset
        matrix = Matrix()
        matrix.translate(self._offset[0], self._offset[1])
        matrix.scale(self._scale[0], self._scale[1])
        path = path.transformed(matrix)
        
        # save current canvas state
        state = ui.GState()
        state.__enter__()
        
        # make ui path
        ui_path = self._make_native_path(path)
        
        # set clipping
        ui_path.add_clip()
        
        # remember clipping state
        self._clipping.append(state)
    
    
    def unclip(self):
        """Removes last clipping path while keeping previous if any."""
        
        # check clip
        if not self._clipping:
            return
        
        # restore state
        state = self._clipping[-1]
        state.__exit__(None, None, None)
        
        # remove from stack
        del self._clipping[-1]
    
    
    def _make_native_path(self, path):
        """Converts given path to native path."""
        
        # init path
        ui_path = ui.Path()
        
        # convert path
        for command in path.commands:
            
            # get data
            key = command[0]
            values = command[1:]
            
            # close
            if key == PATH.CLOSE:
                ui_path.close()
            
            # move to
            elif key == PATH.MOVE:
                ui_path.move_to(*values)
            
            # line to
            elif key == PATH.LINE:
                ui_path.line_to(*values)
            
            # curve to
            elif key == PATH.CURVE:
                ui_path.add_curve(values[4], values[5], *values[:-2])
        
        return ui_path
    
    
    def _update_pen(self, evt=None):
        """Updates pen with current properties."""
        
        # get property name
        prop_name = evt.name if evt is not None else None
        
        # update color
        if prop_name is None or prop_name in ('line_color', 'line_alpha'):
            color = ColorProperties.get_color(self, "line_")
            if color is not UNDEF:
                self._pen['color'] = color
        
        # update width
        if prop_name is None or prop_name in ('line_width', 'line_scale'):
            line_width = self.line_width
            if line_width is not UNDEF:
                self._pen['width'] = line_width * self.line_scale
        
        # update cap
        if prop_name is None or prop_name == 'line_cap':
            line_cap = self.line_cap
            if line_cap is not UNDEF:
                self._pen['cap'] = PYTHONISTA_LINE_CAP[line_cap]
        
        # update join
        if prop_name is None or prop_name == 'line_join':
            line_join = self.line_join
            if line_join is not UNDEF:
                self._pen['join'] = PYTHONISTA_LINE_JOIN[line_join]
        
        # update style/dash
        if prop_name is None or prop_name in ('line_dash', 'line_style', 'line_width', 'line_scale'):
            line_style = self.line_style
            line_dash = self.line_dash if self.line_dash else []
            line_width = self._pen['width']
            
            if line_style == LINE_STYLE.SOLID:
                line_dash = []
            elif line_style not in (LINE_STYLE.CUSTOM, UNDEF):
                line_dash = PYTHONISTA_LINE_STYLE[line_style]
            
            self._pen['dash'] = [x*line_width for x in line_dash]
    
    
    def _update_brush(self, evt=None):
        """Updates brush with current properties."""
        
        color = ColorProperties.get_color(self, "fill_")
        
        if self.fill_style == FILL_STYLE.TRANS:
            self._brush = Transparent
        
        elif color is not UNDEF:
            self._brush = color
    
    
    def _update_text(self, evt=None):
        """Updates text with current properties."""
        
        # get property name
        prop_name = evt.name if evt is not None else None
        
        # update font
        if prop_name is None or prop_name in ('font_name', 'font_family', 'font_style', 'font_weight'):
            font = self.get_font()
            self._font['name'] = font.name
        
        # update font size
        if prop_name is None or prop_name in ('font_size', 'font_scale', 'font_factor'):
            font_size = self.font_size
            if font_size is None:
                self._font['size'] = 10 * self.font_scale * self.font_factor
            elif font_size is not UNDEF:
                self._font['size'] = font_size * self.font_scale * self.font_factor
        
        # update foreground color
        if prop_name is None or prop_name in ('text_color', 'text_alpha'):
            color = ColorProperties.get_color(self, "text_")
            if color is not UNDEF:
                self._font['for_color'] = color
        
        # update background color
        if prop_name is None or prop_name in ('text_bgr_color', 'text_bgr_alpha'):
            color = ColorProperties.get_color(self, "text_bgr_")
            if color is not UNDEF:
                self._font['bgr_color'] = color
