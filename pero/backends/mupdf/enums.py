#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

# import modules
from ...enums import *


MUPDF_LINE_CAP = {
    LINE_CAP_BUTT: 0,
    LINE_CAP_ROUND: 1,
    LINE_CAP_SQUARE: 2}

MUPDF_LINE_JOIN = {
    LINE_JOIN_MITER: 0,
    LINE_JOIN_ROUND: 1,
    LINE_JOIN_BEVEL: 2}

MUPDF_LINE_STYLE = {
    LINE_STYLE_CUSTOM: 'custom',
    LINE_STYLE_SOLID: 'solid',
    LINE_STYLE_DOTTED: DASH_VALUES_DOTTED,
    LINE_STYLE_DASHED: DASH_VALUES_DASHED,
    LINE_STYLE_DASHDOTTED: DASH_VALUES_DASHDOTTED}

MUPDF_FILL_RULE = {
    FILL_RULE_EVENODD: True,
    FILL_RULE_WINDING: False}
