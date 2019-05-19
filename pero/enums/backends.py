#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

# load modules
from .enum import Enum

# define backends
BACKEND = Enum(
    SVG = 'svg',
    WX = 'wx',
    CAIRO = 'cairo',
    MUPDF = 'mupdf',
    PYTHONISTA = 'pythonista')

# define image formats supported by SVG backend
EXPORT_SVG = {
    '.svg'}

# define image formats supported by WX backend
EXPORT_WX = {
    '.bmp',
    '.jpg',
    '.jpeg',
    '.png',
    '.tif',
    '.tiff',
    '.pcx',
    '.pnm',
    '.xpm',
    '.ico',
    '.cur'}

# define formats supported by Cairo backend
EXPORT_CAIRO = {
    '.bmp',
    '.jpg',
    '.jpeg',
    '.png',
    '.tif',
    '.tiff',
    '.gif',
    '.svg',
    '.pdf',
    '.eps'}

# define image formats supported by MuPDF backend
EXPORT_MUPDF = {
    '.pdf'}

# define image formats supported by Pythonista backend
EXPORT_PYTHONISTA = {
    '.png'}

# define available formats
EXPORT_FORMATS = {
    BACKEND.SVG: EXPORT_SVG,
    BACKEND.WX: EXPORT_WX,
    BACKEND.CAIRO: EXPORT_CAIRO,
    BACKEND.MUPDF: EXPORT_MUPDF,
    BACKEND.PYTHONISTA: EXPORT_PYTHONISTA}

# define export backend priorities
EXPORT_PRIORITY = [
    BACKEND.SVG,
    BACKEND.WX,
    BACKEND.CAIRO,
    BACKEND.MUPDF,
    BACKEND.PYTHONISTA]
