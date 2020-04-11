from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.resources import INLINE
from bokeh.embed import components
x = [1,2,3,4,5,6]
y = [2,4,6,8,10,12]
f = figure()
f.line(x,y)
js, div = components(f)
# cdn_js = CDN.js_files[0]
# cdn_css = CDN.css_files[1]
cdn_js = INLINE.render_js()
cdn_css = INLINE.render_css()
# print (cdn_js, cdn_css)