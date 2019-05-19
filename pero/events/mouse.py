#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

# import modules
from ..enums import *
from .view import PositionEvt


class MouseEvt(PositionEvt):
    """
    Defines a generic event which is fired on any mouse-related event.
    
    Attributes:
        
        dragging: bool
            Indicates mouse dragging active.
        
        rotation: int
            Mouse wheel rotation.
        
        left_down: bool
            Indicates left mouse button state.
        
        middle_down: bool
            Indicates middle mouse button state.
        
        right_down: bool
            Indicates right mouse button state.
        
        alt_down: bool
            Indicates Alt key state.
        
        cmd_down: bool
            Indicates Command key state.
        
        ctrl_down: bool
            Indicates Control key state.
        
        shift_down: bool
            Indicates Shift key state.
    """
    
    TYPE = EVENT.MOUSE
    
    
    def __init__(self, **kwargs):
        """Initializes a new instance of MouseEvt."""
        
        self.dragging = None
        self.rotation = None
        
        self.left_down = None
        self.middle_down = None
        self.right_down = None
        
        self.alt_down = None
        self.cmd_down = None
        self.ctrl_down = None
        self.shift_down = None
        
        super(MouseEvt, self).__init__(**kwargs)
    
    
    @classmethod
    def from_evt(cls, evt):
        """
        Initializes a new instance of given class by copying all data.
        
        Args:
            evt: pero.MouseEvt
                Source event from which to copy the data.
        
        Returns:
            cls instance
                New instance of requested class.
        """
        
        return cls(
            
            native = evt.native,
            view = evt.view,
            graphics = evt.graphics,
            
            x = evt.x,
            y = evt.y,
            raw_x = evt.raw_x,
            raw_y = evt.raw_y,
            
            dragging = evt.dragging,
            rotation = evt.rotation,
            
            left_down = evt.left_down,
            middle_down = evt.middle_down,
            right_down = evt.right_down,
            
            alt_down = evt.alt_down,
            cmd_down = evt.cmd_down,
            ctrl_down = evt.ctrl_down,
            shift_down = evt.shift_down)


class MouseMotionEvt(MouseEvt):
    """Defines an event which is fired if mouse moves."""
    
    TYPE = EVENT.MOUSE_MOTION


class MouseDragEvt(MouseEvt):
    """Defines an event which is fired if mouse moves with button pressed."""
    
    TYPE = EVENT.MOUSE_DRAG


class MouseScrollEvt(MouseEvt):
    """Defines an event which is fired if mouse wheel rotates."""
    
    TYPE = EVENT.MOUSE_SCROLL


class MouseLeaveEvt(MouseEvt):
    """Defines an event which is fired if mouse leaves window."""
    
    TYPE = EVENT.MOUSE_LEAVE


class LeftDownEvt(MouseEvt):
    """Defines an event which is fired if left-mouse button is pressed."""
    
    TYPE = EVENT.LEFT_DOWN


class LeftUpEvt(MouseEvt):
    """Defines an event which is fired if left-mouse button is released."""
    
    TYPE = EVENT.LEFT_UP


class LeftDClickEvt(MouseEvt):
    """Defines an event which is fired if left-mouse button is double-clicked."""
    
    TYPE = EVENT.LEFT_DCLICK


class MiddleDownEvt(MouseEvt):
    """Defines an event which is fired if middle-mouse button is pressed."""
    
    TYPE = EVENT.MIDDLE_DOWN


class MiddleUpEvt(MouseEvt):
    """Defines an event which is fired if middle-mouse button is released."""
    
    TYPE = EVENT.MIDDLE_UP


class MiddleDClickEvt(MouseEvt):
    """Defines an event which is fired if middle-mouse button is double-clicked."""
    
    TYPE = EVENT.MIDDLE_DCLICK


class RightDownEvt(MouseEvt):
    """Defines an event which is fired if right-mouse button is pressed."""
    
    TYPE = EVENT.RIGHT_DOWN


class RightUpEvt(MouseEvt):
    """Defines an event which is fired if right-mouse button is released."""
    
    TYPE = EVENT.RIGHT_UP


class RightDClickEvt(MouseEvt):
    """Defines an event which is fired if right-mouse button is double-clicked."""
    
    TYPE = EVENT.RIGHT_DCLICK
