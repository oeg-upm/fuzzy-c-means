import numpy as np
from numpy.random import random
from bokeh.plotting import figure, show, output_file
from bokeh.palettes import Category20 as pallette
import itertools
from fuzzy_clustering import FCM
import logging

def color_gen():
    for c in itertools.cycle(pallette[10]):
        yield c
colors = color_gen()


def example():
    def mscatter(p, x, y, marker):
        p.scatter(x, y, marker=marker, size=15,
                  line_color="navy", fill_color="orange", alpha=0.5)

    def mtext(p, x, y, text):
        p.text(x, y, text=[text],
               text_color="firebrick", text_align="center", text_font_size="10pt")

    p = figure(title="Bokeh Markers", toolbar_location=None)
    p.grid.grid_line_color = None
    p.background_fill_color = "#eeeeee"

    N = 10

    mscatter(p, random(N)+2, random(N)+1, "circle")
    mscatter(p, random(N)+4, random(N)+1, "square")
    mscatter(p, random(N)+6, random(N)+1, "triangle")
    mscatter(p, random(N)+8, random(N)+1, "asterisk")

    mscatter(p, random(N)+2, random(N)+4, "circle_x")
    mscatter(p, random(N)+4, random(N)+4, "square_x")
    mscatter(p, random(N)+6, random(N)+4, "inverted_triangle")
    mscatter(p, random(N)+8, random(N)+4, "x")

    mscatter(p, random(N)+2, random(N)+7, "circle_cross")
    mscatter(p, random(N)+4, random(N)+7, "square_cross")
    mscatter(p, random(N)+6, random(N)+7, "diamond")
    mscatter(p, random(N)+8, random(N)+7, "cross")

    mtext(p, 2.5, 0.5, "circle / o")
    mtext(p, 4.5, 0.5, "square")
    mtext(p, 6.5, 0.5, "triangle")
    mtext(p, 8.5, 0.5, "asterisk / *")

    mtext(p, 2.5, 3.5, "circle_x / ox")
    mtext(p, 4.5, 3.5, "square_x")
    mtext(p, 6.5, 3.5, "inverted_triangle")
    mtext(p, 8.5, 3.5, "x")

    mtext(p, 2.5, 6.5, "circle_cross / o+")
    mtext(p, 4.5, 6.5, "square_cross")
    mtext(p, 6.5, 6.5, "diamond")
    mtext(p, 8.5, 6.5, "cross / +")

    output_file("markers.html", title="markers.py example")

    show(p)  # open a browser


def draw_model_2d(model):
    title = "draw FCM model"
    fig = figure(title=title, toolbar_location=None)
    fig.grid.grid_line_color = None
    fig.background_fill_color = "#eeeeee"
    output_p = None
    for cc, color in zip(model.cluster_centers_, color_gen()):
        print cc
        fig = draw_points_2d(np.array([cc]), fig=fig, title=title, marker="circle", size=15,
                  line_color="navy", fill_color="orange", alpha=0.5)
    show(fig)


def draw_points_2d(points, fig=None, title="figure 123", **kwargs):
    if fig is None:
        fig = figure(title=title, toolbar_location=None)
        fig.grid.grid_line_color = None
        fig.background_fill_color = "#eeeeee"
    x, y = points.T
    fig.scatter(x, y, **kwargs)
    output_file("output.html", title=title+" of outputfile")
    return fig


# X = np.array([[1, 1], [1, 2], [2, 2], [9, 10], [10, 10], [10, 9], [9, 9]])
# fcm = FCM()
# fcm.set_logger(tostdout=True, level=logging.DEBUG)
# fcm.fit(X, [0, 0, 0, 1, 1, 1, 1])
# testing_data = np.array([[0, 1.9], [3, 3], [4, 4], [8, 9], [9.5, 6.5]])
# predicted_membership = fcm.predict(testing_data)
# print "\n\ntesting data"
# print testing_data
# print "predicted membership"
# print predicted_membership
# print "\n\n"
# draw_model_2d(fcm)

