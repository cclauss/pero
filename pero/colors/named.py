#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

# import modules
from .color import Color
from .palette import Palette


# define colors
Transparent = Color.from_hex('#0000', name='Transparent')
AliceBlue = Color.from_hex('#F0F8FF', name='AliceBlue')
AntiqueWhite = Color.from_hex('#FAEBD7', name='AntiqueWhite')
Aqua = Color.from_hex('#00FFFF', name='Aqua')
Aquamarine = Color.from_hex('#7FFFD4', name='Aquamarine')
Azure = Color.from_hex('#F0FFFF', name='Azure')
Beige = Color.from_hex('#F5F5DC', name='Beige')
Bisque = Color.from_hex('#FFE4C4', name='Bisque')
Black = Color.from_hex('#000000', name='Black')
BlanchedAlmond = Color.from_hex('#FFEBCD', name='BlanchedAlmond')
Blue = Color.from_hex('#0000FF', name='Blue')
BlueViolet = Color.from_hex('#8A2BE2', name='BlueViolet')
Brown = Color.from_hex('#A52A2A', name='Brown')
BurlyWood = Color.from_hex('#DEB887', name='BurlyWood')
CadetBlue = Color.from_hex('#5F9EA0', name='CadetBlue')
Chartreuse = Color.from_hex('#7FFF00', name='Chartreuse')
Chocolate = Color.from_hex('#D2691E', name='Chocolate')
Coral = Color.from_hex('#FF7F50', name='Coral')
CornflowerBlue = Color.from_hex('#6495ED', name='CornflowerBlue')
Cornsilk = Color.from_hex('#FFF8DC', name='Cornsilk')
Crimson = Color.from_hex('#DC143C', name='Crimson')
Cyan = Color.from_hex('#00FFFF', name='Cyan')
DarkBlue = Color.from_hex('#00008B', name='DarkBlue')
DarkCyan = Color.from_hex('#008B8B', name='DarkCyan')
DarkGoldenRod = Color.from_hex('#B8860B', name='DarkGoldenRod')
DarkGray = Color.from_hex('#A9A9A9', name='DarkGray')
DarkGrey = Color.from_hex('#A9A9A9', name='DarkGrey')
DarkGreen = Color.from_hex('#006400', name='DarkGreen')
DarkKhaki = Color.from_hex('#BDB76B', name='DarkKhaki')
DarkMagenta = Color.from_hex('#8B008B', name='DarkMagenta')
DarkOliveGreen = Color.from_hex('#556B2F', name='DarkOliveGreen')
DarkOrange = Color.from_hex('#FF8C00', name='DarkOrange')
DarkOrchid = Color.from_hex('#9932CC', name='DarkOrchid')
DarkRed = Color.from_hex('#8B0000', name='DarkRed')
DarkSalmon = Color.from_hex('#E9967A', name='DarkSalmon')
DarkSeaGreen = Color.from_hex('#8FBC8F', name='DarkSeaGreen')
DarkSlateBlue = Color.from_hex('#483D8B', name='DarkSlateBlue')
DarkSlateGray = Color.from_hex('#2F4F4F', name='DarkSlateGray')
DarkSlateGrey = Color.from_hex('#2F4F4F', name='DarkSlateGrey')
DarkTurquoise = Color.from_hex('#00CED1', name='DarkTurquoise')
DarkViolet = Color.from_hex('#9400D3', name='DarkViolet')
DeepPink = Color.from_hex('#FF1493', name='DeepPink')
DeepSkyBlue = Color.from_hex('#00BFFF', name='DeepSkyBlue')
DimGray = Color.from_hex('#696969', name='DimGray')
DimGrey = Color.from_hex('#696969', name='DimGrey')
DodgerBlue = Color.from_hex('#1E90FF', name='DodgerBlue')
FireBrick = Color.from_hex('#B22222', name='FireBrick')
FloralWhite = Color.from_hex('#FFFAF0', name='FloralWhite')
ForestGreen = Color.from_hex('#228B22', name='ForestGreen')
Fuchsia = Color.from_hex('#FF00FF', name='Fuchsia')
Gainsboro = Color.from_hex('#DCDCDC', name='Gainsboro')
GhostWhite = Color.from_hex('#F8F8FF', name='GhostWhite')
Gold = Color.from_hex('#FFD700', name='Gold')
GoldenRod = Color.from_hex('#DAA520', name='GoldenRod')
Gray = Color.from_hex('#808080', name='Gray')
Grey = Color.from_hex('#808080', name='Grey')
Green = Color.from_hex('#008000', name='Green')
GreenYellow = Color.from_hex('#ADFF2F', name='GreenYellow')
HoneyDew = Color.from_hex('#F0FFF0', name='HoneyDew')
HotPink = Color.from_hex('#FF69B4', name='HotPink')
IndianRed = Color.from_hex('#CD5C5C', name='IndianRed')
Indigo = Color.from_hex('#4B0082', name='Indigo')
Ivory = Color.from_hex('#FFFFF0', name='Ivory')
Khaki = Color.from_hex('#F0E68C', name='Khaki')
Lavender = Color.from_hex('#E6E6FA', name='Lavender')
LavenderBlush = Color.from_hex('#FFF0F5', name='LavenderBlush')
LawnGreen = Color.from_hex('#7CFC00', name='LawnGreen')
LemonChiffon = Color.from_hex('#FFFACD', name='LemonChiffon')
LightBlue = Color.from_hex('#ADD8E6', name='LightBlue')
LightCoral = Color.from_hex('#F08080', name='LightCoral')
LightCyan = Color.from_hex('#E0FFFF', name='LightCyan')
LightGoldenRodYellow = Color.from_hex('#FAFAD2', name='LightGoldenRodYellow')
LightGray = Color.from_hex('#D3D3D3', name='LightGray')
LightGrey = Color.from_hex('#D3D3D3', name='LightGrey')
LightGreen = Color.from_hex('#90EE90', name='LightGreen')
LightPink = Color.from_hex('#FFB6C1', name='LightPink')
LightSalmon = Color.from_hex('#FFA07A', name='LightSalmon')
LightSeaGreen = Color.from_hex('#20B2AA', name='LightSeaGreen')
LightSkyBlue = Color.from_hex('#87CEFA', name='LightSkyBlue')
LightSlateGray = Color.from_hex('#778899', name='LightSlateGray')
LightSlateGrey = Color.from_hex('#778899', name='LightSlateGrey')
LightSteelBlue = Color.from_hex('#B0C4DE', name='LightSteelBlue')
LightYellow = Color.from_hex('#FFFFE0', name='LightYellow')
Lime = Color.from_hex('#00FF00', name='Lime')
LimeGreen = Color.from_hex('#32CD32', name='LimeGreen')
Linen = Color.from_hex('#FAF0E6', name='Linen')
Magenta = Color.from_hex('#FF00FF', name='Magenta')
Maroon = Color.from_hex('#800000', name='Maroon')
MediumAquaMarine = Color.from_hex('#66CDAA', name='MediumAquaMarine')
MediumBlue = Color.from_hex('#0000CD', name='MediumBlue')
MediumOrchid = Color.from_hex('#BA55D3', name='MediumOrchid')
MediumPurple = Color.from_hex('#9370DB', name='MediumPurple')
MediumSeaGreen = Color.from_hex('#3CB371', name='MediumSeaGreen')
MediumSlateBlue = Color.from_hex('#7B68EE', name='MediumSlateBlue')
MediumSpringGreen = Color.from_hex('#00FA9A', name='MediumSpringGreen')
MediumTurquoise = Color.from_hex('#48D1CC', name='MediumTurquoise')
MediumVioletRed = Color.from_hex('#C71585', name='MediumVioletRed')
MidnightBlue = Color.from_hex('#191970', name='MidnightBlue')
MintCream = Color.from_hex('#F5FFFA', name='MintCream')
MistyRose = Color.from_hex('#FFE4E1', name='MistyRose')
Moccasin = Color.from_hex('#FFE4B5', name='Moccasin')
NavajoWhite = Color.from_hex('#FFDEAD', name='NavajoWhite')
Navy = Color.from_hex('#000080', name='Navy')
OldLace = Color.from_hex('#FDF5E6', name='OldLace')
Olive = Color.from_hex('#808000', name='Olive')
OliveDrab = Color.from_hex('#6B8E23', name='OliveDrab')
Orange = Color.from_hex('#FFA500', name='Orange')
OrangeRed = Color.from_hex('#FF4500', name='OrangeRed')
Orchid = Color.from_hex('#DA70D6', name='Orchid')
PaleGoldenRod = Color.from_hex('#EEE8AA', name='PaleGoldenRod')
PaleGreen = Color.from_hex('#98FB98', name='PaleGreen')
PaleTurquoise = Color.from_hex('#AFEEEE', name='PaleTurquoise')
PaleVioletRed = Color.from_hex('#DB7093', name='PaleVioletRed')
PapayaWhip = Color.from_hex('#FFEFD5', name='PapayaWhip')
PeachPuff = Color.from_hex('#FFDAB9', name='PeachPuff')
Peru = Color.from_hex('#CD853F', name='Peru')
Pink = Color.from_hex('#FFC0CB', name='Pink')
Plum = Color.from_hex('#DDA0DD', name='Plum')
PowderBlue = Color.from_hex('#B0E0E6', name='PowderBlue')
Purple = Color.from_hex('#800080', name='Purple')
RebeccaPurple = Color.from_hex('#663399', name='RebeccaPurple')
Red = Color.from_hex('#FF0000', name='Red')
RosyBrown = Color.from_hex('#BC8F8F', name='RosyBrown')
RoyalBlue = Color.from_hex('#4169E1', name='RoyalBlue')
SaddleBrown = Color.from_hex('#8B4513', name='SaddleBrown')
Salmon = Color.from_hex('#FA8072', name='Salmon')
SandyBrown = Color.from_hex('#F4A460', name='SandyBrown')
SeaGreen = Color.from_hex('#2E8B57', name='SeaGreen')
SeaShell = Color.from_hex('#FFF5EE', name='SeaShell')
Sienna = Color.from_hex('#A0522D', name='Sienna')
Silver = Color.from_hex('#C0C0C0', name='Silver')
SkyBlue = Color.from_hex('#87CEEB', name='SkyBlue')
SlateBlue = Color.from_hex('#6A5ACD', name='SlateBlue')
SlateGray = Color.from_hex('#708090', name='SlateGray')
SlateGrey = Color.from_hex('#708090', name='SlateGrey')
Snow = Color.from_hex('#FFFAFA', name='Snow')
SpringGreen = Color.from_hex('#00FF7F', name='SpringGreen')
SteelBlue = Color.from_hex('#4682B4', name='SteelBlue')
Tan = Color.from_hex('#D2B48C', name='Tan')
Teal = Color.from_hex('#008080', name='Teal')
Thistle = Color.from_hex('#D8BFD8', name='Thistle')
Tomato = Color.from_hex('#FF6347', name='Tomato')
Turquoise = Color.from_hex('#40E0D0', name='Turquoise')
Violet = Color.from_hex('#EE82EE', name='Violet')
Wheat = Color.from_hex('#F5DEB3', name='Wheat')
White = Color.from_hex('#FFFFFF', name='White')
WhiteSmoke = Color.from_hex('#F5F5F5', name='WhiteSmoke')
Yellow = Color.from_hex('#FFFF00', name='Yellow')
YellowGreen = Color.from_hex('#9ACD32', name='YellowGreen')

R = Color.from_hex('#FF0000', name='R') # red
G = Color.from_hex('#008000', name='G') # green
B = Color.from_hex('#0000FF', name='B') # blue

C = Color.from_hex('#00FFFF', name='C') # cyan
M = Color.from_hex('#FF00FF', name='M') # magenta
Y = Color.from_hex('#FFFF00', name='Y') # yellow

T = Color.from_hex('#0000', name='T') # transparent
K = Color.from_hex('#000000', name='K') # black
W = Color.from_hex('#FFFFFF', name='W') # white
A = Color.from_hex('#808080', name='A') # gray
O = Color.from_hex('#FFA500', name='O') # orange

# define palettes
Pero = Palette(('#1047b9ff','#328c00ff','#f19000ff','#4cc7c5ff','#8f8f15ff','#edbb00ff','#786dffff','#b34e00ff','#80bfbdff','#c88812ff','#c5ca3dff','#7bb6ffff','#45438aff','#188183ff','#838183ff','#457ec6ff','#7f2200ff','#4c4e4cff'), name='Pero')
Accent = Palette(('#7fc97f', '#beaed4', '#fdc086', '#ffff99', '#386cb0', '#f0027f', '#bf5b17', '#666666'), name='Accent')
Dark = Palette(('#1b9e77', '#d95f02', '#7570b3', '#e7298a', '#66a61e', '#e6ab02', '#a6761d', '#666666'), name='Dark')
Paired = Palette(('#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99', '#e31a1c', '#fdbf6f', '#ff7f00', '#cab2d6', '#6a3d9a', '#ffff99', '#b15928'), name='Paired')
Pastel1 = Palette(('#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6', '#ffffcc', '#e5d8bd', '#fddaec', '#f2f2f2'), name='Pastel1')
Pastel2 = Palette(('#b3e2cd', '#fdcdac', '#cbd5e8', '#f4cae4', '#e6f5c9', '#fff2ae', '#f1e2cc', '#cccccc'), name='Pastel2')
Set1 = Palette(('#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', '#ffff33', '#a65628', '#f781bf', '#999999'), name='Set1')
Set2 = Palette(('#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f', '#e5c494', '#b3b3b3'), name='Set2')
Set3 = Palette(('#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69', '#fccde5', '#d9d9d9', '#bc80bd', '#ccebc5', '#ffed6f'), name='Set3')
Spectral = Palette(("#3288bd", "#66c2a5", "#abdda4", "#e6f598", "#ffffbf", "#fee08b", "#fdae61", "#f46d43", "#d53e4f"), name='Spectral')

Blues = Palette(('#f7fbff', '#deebf7', '#c6dbef', '#9ecae1', '#6baed6', '#4292c6', '#2171b5', '#08519c', '#08306b'), name='Blues')
Greens = Palette(('#f7fcf5', '#e5f5e0', '#c7e9c0', '#a1d99b', '#74c476', '#41ab5d', '#238b45', '#006d2c', '#00441b'), name='Greens')
Greys = Palette(('#ffffff', '#f0f0f0', '#d9d9d9', '#bdbdbd', '#969696', '#737373', '#525252', '#252525', '#000000'), name='Greys')
Oranges = Palette(('#fff5eb', '#fee6ce', '#fdd0a2', '#fdae6b', '#fd8d3c', '#f16913', '#d94801', '#a63603', '#7f2704'), name='Oranges')
Purples = Palette(('#fcfbfd', '#efedf5', '#dadaeb', '#bcbddc', '#9e9ac8', '#807dba', '#6a51a3', '#54278f', '#3f007d'), name='Purples')
Reds = Palette(('#fff5f0', '#fee0d2', '#fcbba1', '#fc9272', '#fb6a4a', '#ef3b2c', '#cb181d', '#a50f15', '#67000d'), name='Reds')

Inferno = Palette(('#fcfea4', '#f8c931', '#f98c09', '#e35832', '#ba3655', '#88216a', '#550f6d', '#1f0c47', '#000003'), name='Inferno')
Magma = Palette(('#fbfcbf', '#fec286', '#fb8660', '#e55063', '#b53679', '#812581', '#4f117b', '#1b1044', '#000003'), name='Magma')
Plasma = Palette(('#eff821', '#fdc328', '#f79341', '#e56b5c', '#ca4678', '#a82296', '#7c02a7', '#4a02a0', '#0c0786'), name='Plasma')
Viridis = Palette(('#fde724', '#aadb32', '#5bc862', '#27ad80', '#208f8c', '#2c718e', '#3b518a', '#472b7a', '#440154'), name='Viridis')

BrBG = Palette(('#8c510a', '#bf812d', '#dfc27d', '#f6e8c3', '#f5f5f5', '#c7eae5', '#80cdc1', '#35978f', '#01665e'), name='BrBG')
BuGn = Palette(('#f7fcfd', '#e5f5f9', '#ccece6', '#99d8c9', '#66c2a4', '#41ae76', '#238b45', '#006d2c', '#00441b'), name='BuGn')
BuPu = Palette(('#f7fcfd', '#e0ecf4', '#bfd3e6', '#9ebcda', '#8c96c6', '#8c6bb1', '#88419d', '#810f7c', '#4d004b'), name='BuPu')
GnBu = Palette(('#f7fcf0', '#e0f3db', '#ccebc5', '#a8ddb5', '#7bccc4', '#4eb3d3', '#2b8cbe', '#0868ac', '#084081'), name='GnBu')
OrRd = Palette(('#fff7ec', '#fee8c8', '#fdd49e', '#fdbb84', '#fc8d59', '#ef6548', '#d7301f', '#b30000', '#7f0000'), name='OrRd')
PiYG = Palette(('#c51b7d', '#de77ae', '#f1b6da', '#fde0ef', '#f7f7f7', '#e6f5d0', '#b8e186', '#7fbc41', '#4d9221'), name='PiYG')
PRGn = Palette(('#762a83', '#9970ab', '#c2a5cf', '#e7d4e8', '#f7f7f7', '#d9f0d3', '#a6dba0', '#5aae61', '#1b7837'), name='PRGn')
PuBu = Palette(('#fff7fb', '#ece7f2', '#d0d1e6', '#a6bddb', '#74a9cf', '#3690c0', '#0570b0', '#045a8d', '#023858'), name='PuBu')
PuBuGn = Palette(('#fff7fb', '#ece2f0', '#d0d1e6', '#a6bddb', '#67a9cf', '#3690c0', '#02818a', '#016c59', '#014636'), name='PuBuGn')
PuOr = Palette(('#542788', '#8073ac', '#b2abd2', '#d8daeb', '#f7f7f7', '#fee0b6', '#fdb863', '#e08214', '#b35806'), name='PuOr')
PuRd = Palette(('#f7f4f9', '#e7e1ef', '#d4b9da', '#c994c7', '#df65b0', '#e7298a', '#ce1256', '#980043', '#67001f'), name='PuRd')
RdBu = Palette(('#b2182b', '#d6604d', '#f4a582', '#fddbc7', '#f7f7f7', '#d1e5f0', '#92c5de', '#4393c3', '#2166ac'), name='RdBu')
RdGy = Palette(('#b2182b', '#d6604d', '#f4a582', '#fddbc7', '#ffffff', '#e0e0e0', '#bababa', '#878787', '#4d4d4d'), name='RdGy')
RdPu = Palette(('#fff7f3', '#fde0dd', '#fcc5c0', '#fa9fb5', '#f768a1', '#dd3497', '#ae017e', '#7a0177', '#49006a'), name='RdPu')
RdYlBu = Palette(('#d73027', '#f46d43', '#fdae61', '#fee090', '#ffffbf', '#e0f3f8', '#abd9e9', '#74add1', '#4575b4'), name='RdYlBu')
RdYlGn = Palette(('#d73027', '#f46d43', '#fdae61', '#fee08b', '#ffffbf', '#d9ef8b', '#a6d96a', '#66bd63', '#1a9850'), name='RdYlGn')
YlGn = Palette(('#ffffe5', '#f7fcb9', '#d9f0a3', '#addd8e', '#78c679', '#41ab5d', '#238443', '#006837', '#004529'), name='YlGn')
YlGnBu = Palette(('#ffffd9', '#edf8b1', '#c7e9b4', '#7fcdbb', '#41b6c4', '#1d91c0', '#225ea8', '#253494', '#081d58'), name='YlGnBu')
YlOrBr = Palette(('#ffffe5', '#fff7bc', '#fee391', '#fec44f', '#fe9929', '#ec7014', '#cc4c02', '#993404', '#662506'), name='YlOrBr')
YlOrRd = Palette(('#ffffcc', '#ffeda0', '#fed976', '#feb24c', '#fd8d3c', '#fc4e2a', '#e31a1c', '#bd0026', '#800026'), name='YlOrRd')
