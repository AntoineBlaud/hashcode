import turtle as te
from helper import *


def verso(x, y, scale):

    te.penup()
    te.color('#79b5e8')
    te.end_fill()
    Moveto(340.0 * scale[0], 1376.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -2.0 * scale[1], -72.0 * scale[0], -
              7.0 * scale[1], -154.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-97.0 * scale[0], -4.0 * scale[1], -152.0 * scale[0], -
              10.0 * scale[1], -157.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -14.0 * scale[1], 0.0 * scale[0], -
              40.0 * scale[1], 18.0 * scale[0], -51.0 * scale[1])
    Curveto_r(34.0 * scale[0], -21.0 * scale[1], 69.0 * scale[0], -
              129.0 * scale[1], 48.0 * scale[0], -150.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -7.0 * scale[1], -14.0 * scale[0], -
              30.0 * scale[1], -17.0 * scale[0], -50.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -32.0 * scale[1], -2.0 * scale[0], -
              36.0 * scale[1], 14.0 * scale[0], -31.0 * scale[1])
    Curveto_r(16.0 * scale[0], 5.0 * scale[1], 18.0 * scale[0],
              0.0 * scale[1], 14.0 * scale[0], -41.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -33.0 * scale[1], -1.0 *
              scale[0], -45.0 * scale[1], 7.0 * scale[0], -42.0 * scale[1])
    Curveto_r(7.0 * scale[0], 2.0 * scale[1], 13.0 * scale[0],
              22.0 * scale[1], 15.0 * scale[0], 45.0 * scale[1])
    Curveto_r(2.0 * scale[0], 23.0 * scale[1], 7.0 * scale[0],
              42.0 * scale[1], 12.0 * scale[0], 42.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 6.0 * scale[0], -
              9.0 * scale[1], 3.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -25.0 * scale[1], 17.0 * scale[0], -
              86.0 * scale[1], 27.0 * scale[0], -70.0 * scale[1])
    Curveto_r(4.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              8.0 * scale[1], 13.0 * scale[0], 4.0 * scale[1])
    Curveto_r(7.0 * scale[0], -12.0 * scale[1], -4.0 * scale[0], -
              74.0 * scale[1], -13.0 * scale[0], -74.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -5.0 * scale[0], -
              11.0 * scale[1], -2.0 * scale[0], -25.0 * scale[1])
    Curveto_r(5.0 * scale[0], -27.0 * scale[1], 16.0 *
              scale[0], -25.0 * scale[1], 33.0 * scale[0], 7.0 * scale[1])
    Curveto_r(8.0 * scale[0], 15.0 * scale[1], 8.0 * scale[0],
              19.0 * scale[1], 0.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -4.0 * scale[1], -11.0 *
              scale[0], -2.0 * scale[1], -11.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 6.0 * scale[0],
              11.0 * scale[1], 14.0 * scale[0], 11.0 * scale[1])
    Curveto_r(19.0 * scale[0], 0.0 * scale[1], 57.0 * scale[0],
              49.0 * scale[1], 49.0 * scale[0], 64.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -3.0 * scale[0],
              8.0 * scale[1], 1.0 * scale[0], 4.0 * scale[1])
    Curveto_r(12.0 * scale[0], -10.0 * scale[1], 116.0 * scale[0],
              111.0 * scale[1], 121.0 * scale[0], 141.0 * scale[1])
    Curveto_r(3.0 * scale[0], 14.0 * scale[1], 10.0 * scale[0],
              40.0 * scale[1], 16.0 * scale[0], 56.0 * scale[1])
    Curveto_r(27.0 * scale[0], 76.0 * scale[1], 28.0 * scale[0],
              91.0 * scale[1], 16.0 * scale[0], 140.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 42.0 * scale[1], -16.0 * scale[0],
              50.0 * scale[1], -37.0 * scale[0], 53.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 2.0 * scale[1], -28.0 * scale[0],
              1.0 * scale[1], -30.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto_r(-220.0 * scale[0], -281.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -4.0 * scale[0], -
              15.0 * scale[1], -9.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -22.0 * scale[0],
              16.0 * scale[1], -14.0 * scale[0], 24.0 * scale[1])
    Curveto_r(11.0 * scale[0], 11.0 * scale[1], 23.0 * scale[0],
              6.0 * scale[1], 23.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(466.0 * scale[0], 1371.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], -5.0 * scale[0], -
              15.0 * scale[1], -2.0 * scale[0], -18.0 * scale[1])
    Curveto_r(9.0 * scale[0], -9.0 * scale[1], 19.0 * scale[0],
              4.0 * scale[1], 14.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 11.0 * scale[1], -6.0 * scale[0],
              11.0 * scale[1], -12.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(633.0 * scale[0], 1347.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(45.0 * scale[0], -39.0 * scale[1], 46.0 *
              scale[0], -47.0 * scale[1], 7.0 * scale[0], -47.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 0.0 * scale[1], -34.0 * scale[0], -
              6.0 * scale[1], -30.0 * scale[0], -45.0 * scale[1])
    Curveto_r(2.0 * scale[0], -25.0 * scale[1], 55.0 * scale[0], -
              81.0 * scale[1], 83.0 * scale[0], -89.0 * scale[1])
    Curveto_r(15.0 * scale[0], -4.0 * scale[1], 17.0 *
              scale[0], -2.0 * scale[1], 8.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 18.0 * scale[1], -13.0 * scale[0],
              31.0 * scale[1], 7.0 * scale[0], 16.0 * scale[1])
    Curveto_r(15.0 * scale[0], -12.0 * scale[1], 15.0 *
              scale[0], -11.0 * scale[1], -1.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 21.0 * scale[1], -18.0 * scale[0],
              22.0 * scale[1], 12.0 * scale[0], 37.0 * scale[1])
    Curveto_r(38.0 * scale[0], 20.0 * scale[1], 61.0 * scale[0],
              21.0 * scale[1], 35.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -13.0 * scale[1], -16.0 *
              scale[0], -14.0 * scale[1], -1.0 * scale[0], -9.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 17.0 * scale[0],
              1.0 * scale[1], 17.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 7.0 * scale[0], -
              8.0 * scale[1], 15.0 * scale[0], -5.0 * scale[1])
    Curveto_r(11.0 * scale[0], 5.0 * scale[1], 13.0 * scale[0],
              2.0 * scale[1], 9.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -10.0 * scale[1], 0.0 * scale[0], -
              18.0 * scale[1], 10.0 * scale[0], -22.0 * scale[1])
    Curveto_r(9.0 * scale[0], -3.0 * scale[1], 13.0 * scale[0], -
              11.0 * scale[1], 9.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], -2.0 *
              scale[0], -7.0 * scale[1], 2.0 * scale[0], -3.0 * scale[1])
    Curveto_r(5.0 * scale[0], 4.0 * scale[1], 10.0 * scale[0],
              14.0 * scale[1], 11.0 * scale[0], 21.0 * scale[1])
    Curveto_r(5.0 * scale[0], 35.0 * scale[1], 19.0 * scale[0],
              62.0 * scale[1], 45.0 * scale[0], 90.0 * scale[1])
    Curveto_r(16.0 * scale[0], 17.0 * scale[1], 32.0 * scale[0],
              39.0 * scale[1], 35.0 * scale[0], 49.0 * scale[1])
    Curveto_r(3.0 * scale[0], 10.0 * scale[1], 12.0 * scale[0],
              16.0 * scale[1], 19.0 * scale[0], 13.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 19.0 * scale[0],
              2.0 * scale[1], 25.0 * scale[0], 9.0 * scale[1])
    Curveto_r(7.0 * scale[0], 8.0 * scale[1], 17.0 * scale[0],
              12.0 * scale[1], 23.0 * scale[0], 8.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 7.0 *
              scale[0], -1.0 * scale[1], 3.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 9.0 * scale[1], -13.0 * scale[0],
              8.0 * scale[1], -27.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -9.0 * scale[1], -19.0 *
              scale[0], -12.0 * scale[1], -19.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 21.0 * scale[1], -29.0 * scale[0],
              22.0 * scale[1], -54.0 * scale[0], 2.0 * scale[1])
    Lineto_r(-25.0 * scale[0], -20.0 * scale[1])
    Lineto_r(-7.0 * scale[0], 25.0 * scale[1])
    Lineto_r(-6.0 * scale[0], 25.0 * scale[1])
    Lineto_r(-122.0 * scale[0], 0.0 * scale[1])
    Lineto_r(-121.0 * scale[0], 0.0 * scale[1])
    Lineto_r(38.0 * scale[0], -32.0 * scale[1])
    te.end_fill()
    Moveto(761.0 * scale[0], 1158.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -18.0 * scale[1], -21.0 *
              scale[0], -20.0 * scale[1], -32.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 4.0 * scale[1], -9.0 * scale[0],
              3.0 * scale[1], -13.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 3.0 * scale[0], -
              13.0 * scale[1], 14.0 * scale[0], -17.0 * scale[1])
    Curveto_r(11.0 * scale[0], -3.0 * scale[1], 20.0 * scale[0], -
              13.0 * scale[1], 20.0 * scale[0], -20.0 * scale[1])
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 17.0 * scale[0], -
              29.0 * scale[1], 22.0 * scale[0], -18.0 * scale[1])
    Curveto_r(2.0 * scale[0], 5.0 * scale[1], 1.0 * scale[0],
              24.0 * scale[1], -3.0 * scale[0], 43.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 19.0 * scale[1], -7.0 * scale[0],
              27.0 * scale[1], -8.0 * scale[0], 18.0 * scale[1])
    te.end_fill()
    Moveto(780.0 * scale[0], 1160.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0], -
              10.0 * scale[1], 11.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0], -
              6.0 * scale[1], -2.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 3.0 * scale[0], -5.0 * scale[1])
    Curveto_r(9.0 * scale[0], 8.0 * scale[1], 14.0 * scale[0],
              20.0 * scale[1], 11.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 16.0 * scale[1], -23.0 * scale[0],
              19.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(690.0 * scale[0], 1125.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(13.0 * scale[0], -14.0 * scale[1], 26.0 * scale[0], -
              25.0 * scale[1], 28.0 * scale[0], -25.0 * scale[1])
    Curveto_r(3.0 * scale[0], 0.0 * scale[1], -5.0 * scale[0],
              11.0 * scale[1], -18.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 14.0 * scale[1], -26.0 * scale[0],
              25.0 * scale[1], -28.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], 5.0 * scale[0], -
              11.0 * scale[1], 18.0 * scale[0], -25.0 * scale[1])
    te.end_fill()
    Moveto(650.0 * scale[0], 1020.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -11.0 * scale[1], -8.0 * scale[0], -
              20.0 * scale[1], -6.0 * scale[0], -20.0 * scale[1])
    Curveto_r(3.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              9.0 * scale[1], 16.0 * scale[0], 20.0 * scale[1])
    Curveto_r(6.0 * scale[0], 11.0 * scale[1], 8.0 * scale[0],
              20.0 * scale[1], 6.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              9.0 * scale[1], -16.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(680.0 * scale[0], 1025.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -9.0 * scale[1], -11.0 * scale[0], -
              17.0 * scale[1], -9.0 * scale[0], -20.0 * scale[1])
    Curveto_r(3.0 * scale[0], -2.0 * scale[1], 10.0 * scale[0],
              5.0 * scale[1], 17.0 * scale[0], 15.0 * scale[1])
    Curveto_r(14.0 * scale[0], 24.0 * scale[1], 10.0 * scale[0],
              26.0 * scale[1], -8.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(152.0 * scale[0], 934.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -20.0 * scale[1], -32.0 *
              scale[0], -62.0 * scale[1], -26.0 * scale[0], -79.0 * scale[1])
    Curveto_r(11.0 * scale[0], -26.0 * scale[1], 24.0 *
              scale[0], -16.0 * scale[1], 24.0 * scale[0], 18.0 * scale[1])
    Curveto_r(0.0 * scale[0], 18.0 * scale[1], 5.0 * scale[0],
              38.0 * scale[1], 11.0 * scale[0], 44.0 * scale[1])
    Curveto_r(6.0 * scale[0], 6.0 * scale[1], 10.0 * scale[0],
              16.0 * scale[1], 8.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 6.0 * scale[1], -9.0 * scale[0],
              4.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(716.0 * scale[0], 913.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(626.0 * scale[0], 903.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(929.0 * scale[0], 903.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 1.0 * scale[0], -7.0 * scale[1])
    Curveto_r(8.0 * scale[0], 6.0 * scale[1], 22.0 * scale[0],
              14.0 * scale[1], 30.0 * scale[0], 17.0 * scale[1])
    Curveto_r(13.0 * scale[0], 5.0 * scale[1], 12.0 * scale[0],
              6.0 * scale[1], -1.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 1.0 * scale[1], -23.0 * scale[0], -
              7.0 * scale[1], -30.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(690.0 * scale[0], 780.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -5.0 * scale[1], -12.0 * scale[0], -
              12.0 * scale[1], -9.0 * scale[0], -15.0 * scale[1])
    Curveto_r(4.0 * scale[0], -3.0 * scale[1], 12.0 * scale[0],
              1.0 * scale[1], 19.0 * scale[0], 10.0 * scale[1])
    Curveto_r(14.0 * scale[0], 17.0 * scale[1], 11.0 * scale[0],
              19.0 * scale[1], -10.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(622.0 * scale[0], 756.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(10.0 * scale[0], -7.0 * scale[1], 14.0 * scale[0], -
              17.0 * scale[1], 10.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -5.0 * scale[1], -1.0 *
              scale[0], -5.0 * scale[1], 6.0 * scale[0], -1.0 * scale[1])
    Curveto_r(10.0 * scale[0], 6.0 * scale[1], 10.0 * scale[0],
              11.0 * scale[1], 1.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 8.0 * scale[1], -17.0 * scale[0],
              14.0 * scale[1], -23.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -3.0 * scale[0], -
              7.0 * scale[1], 6.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(600.0 * scale[0], 719.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -7.0 * scale[0], -
              9.0 * scale[1], -15.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 8.0 * scale[1], -30.0 * scale[0], -
              12.0 * scale[1], -15.0 * scale[0], -26.0 * scale[1])
    Curveto_r(10.0 * scale[0], -9.0 * scale[1], 11.0 *
              scale[0], -9.0 * scale[1], 6.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 9.0 * scale[1], 0.0 * scale[0],
              12.0 * scale[1], 16.0 * scale[0], 10.0 * scale[1])
    Curveto_r(14.0 * scale[0], -1.0 * scale[1], 23.0 * scale[0],
              4.0 * scale[1], 26.0 * scale[0], 16.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], -1.0 * scale[0],
              17.0 * scale[1], -7.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              5.0 * scale[1], -11.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(410.0 * scale[0], 675.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -8.0 * scale[1], -17.0 * scale[0], -
              12.0 * scale[1], -23.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -7.0 * scale[0],
              1.0 * scale[1], -3.0 * scale[0], -5.0 * scale[1])
    Curveto_r(10.0 * scale[0], -17.0 * scale[1], 42.0 *
              scale[0], -10.0 * scale[1], 42.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 22.0 * scale[1], 0.0 * scale[0],
              22.0 * scale[1], -16.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(326.0 * scale[0], 626.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], -3.0 * scale[0], -
              19.0 * scale[1], -16.0 * scale[0], -26.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -6.0 * scale[1], -18.0 * scale[0], -
              16.0 * scale[1], -14.0 * scale[0], -22.0 * scale[1])
    Curveto_r(4.0 * scale[0], -7.0 * scale[1], 10.0 *
              scale[0], -5.0 * scale[1], 16.0 * scale[0], 6.0 * scale[1])
    Curveto_r(5.0 * scale[0], 9.0 * scale[1], 14.0 * scale[0],
              13.0 * scale[1], 20.0 * scale[0], 10.0 * scale[1])
    Curveto_r(7.0 * scale[0], -4.0 * scale[1], 8.0 *
              scale[0], -2.0 * scale[1], 4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 7.0 * scale[1], -3.0 * scale[0],
              12.0 * scale[1], 2.0 * scale[0], 12.0 * scale[1])
    Curveto_r(17.0 * scale[0], 0.0 * scale[1], 22.0 * scale[0], -
              13.0 * scale[1], 9.0 * scale[0], -29.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -14.0 * scale[1], -10.0 *
              scale[0], -14.0 * scale[1], 3.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 6.0 * scale[1], 16.0 * scale[0],
              24.0 * scale[1], 17.0 * scale[0], 40.0 * scale[1])
    Curveto_r(1.0 * scale[0], 15.0 * scale[1], -1.0 * scale[0],
              22.0 * scale[1], -4.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -9.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -24.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 8.0 * scale[1], -17.0 * scale[0],
              7.0 * scale[1], -13.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(870.0 * scale[0], 575.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -9.0 * scale[1], -8.0 * scale[0], -
              15.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              7.0 * scale[1], 16.0 * scale[0], 15.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], 4.0 * scale[0],
              15.0 * scale[1], 2.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              7.0 * scale[1], -16.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(840.0 * scale[0], 530.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -18.0 * scale[1], -14.0 *
              scale[0], -20.0 * scale[1], -21.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], -9.0 * scale[0],
              5.0 * scale[1], -9.0 * scale[0], -15.0 * scale[1])
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], -3.0 * scale[0], -
              26.0 * scale[1], -7.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 9.0 * scale[1], -43.0 * scale[0], -
              22.0 * scale[1], -43.0 * scale[0], -40.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -4.0 * scale[0], -
              13.0 * scale[1], -10.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              7.0 * scale[1], -10.0 * scale[0], -15.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -5.0 * scale[0], -
              15.0 * scale[1], -11.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              4.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              10.0 * scale[1], -9.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -18.0 * scale[0], -
              9.0 * scale[1], -21.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -11.0 * scale[1], -22.0 * scale[0], -
              32.0 * scale[1], -41.0 * scale[0], -47.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -14.0 * scale[1], -33.0 *
              scale[0], -32.0 * scale[1], -30.0 * scale[0], -39.0 * scale[1])
    Curveto_r(3.0 * scale[0], -7.0 * scale[1], -2.0 * scale[0], -
              15.0 * scale[1], -10.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -3.0 * scale[1], -14.0 * scale[0], -
              19.0 * scale[1], -14.0 * scale[0], -36.0 * scale[1])
    Curveto_r(0.0 * scale[0], -17.0 * scale[1], -8.0 * scale[0], -
              45.0 * scale[1], -17.0 * scale[0], -63.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -31.0 * scale[1], -19.0 *
              scale[0], -74.0 * scale[1], -7.0 * scale[0], -130.0 * scale[1])
    Lineto_r(6.0 * scale[0], -27.0 * scale[1])
    Lineto_r(177.0 * scale[0], 0.0 * scale[1])
    Curveto_r(217.0 * scale[0], 0.0 * scale[1], 232.0 * scale[0],
              6.0 * scale[1], 182.0 * scale[0], 67.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 31.0 * scale[1], -71.0 * scale[0],
              130.0 * scale[1], -71.0 * scale[0], 152.0 * scale[1])
    Curveto_r(0.0 * scale[0], 2.0 * scale[1], 10.0 * scale[0], -
              4.0 * scale[1], 21.0 * scale[0], -15.0 * scale[1])
    Lineto_r(22.0 * scale[0], -19.0 * scale[1])
    Lineto_r(-7.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 28.0 * scale[1], -3.0 * scale[0],
              38.0 * scale[1], 9.0 * scale[0], 43.0 * scale[1])
    Curveto_r(17.0 * scale[0], 6.0 * scale[1], 22.0 * scale[0],
              91.0 * scale[1], 5.0 * scale[0], 101.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -10.0 * scale[0], -
              8.0 * scale[1], -10.0 * scale[0], -30.0 * scale[1])
    Curveto_r(0.0 * scale[0], -20.0 * scale[1], -4.0 * scale[0], -
              34.0 * scale[1], -9.0 * scale[0], -31.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 6.0 * scale[1], -8.0 * scale[0],
              33.0 * scale[1], 4.0 * scale[0], 141.0 * scale[1])
    Curveto_r(4.0 * scale[0], 40.0 * scale[1], 3.0 * scale[0],
              45.0 * scale[1], -5.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -8.0 * scale[0], -
              31.0 * scale[1], -6.0 * scale[0], -38.0 * scale[1])
    Curveto_r(3.0 * scale[0], -7.0 * scale[1], 1.0 * scale[0], -
              13.0 * scale[1], -4.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              7.0 * scale[1], -10.0 * scale[0], -15.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -7.0 * scale[0], -
              15.0 * scale[1], -15.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0],
              9.0 * scale[1], -15.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], 5.0 * scale[0],
              20.0 * scale[1], 10.0 * scale[0], 20.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              14.0 * scale[1], 10.0 * scale[0], 31.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], 4.0 * scale[0],
              28.0 * scale[1], 10.0 * scale[0], 24.0 * scale[1])
    Curveto_r(15.0 * scale[0], -9.0 * scale[1], 12.0 * scale[0],
              1.0 * scale[1], -9.0 * scale[0], 36.0 * scale[1])
    Lineto_r(-19.0 * scale[0], 31.0 * scale[1])
    Lineto_r(-12.0 * scale[0], -22.0 * scale[1])
    te.end_fill()
    Moveto_r(12.0 * scale[0], -22.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -7.0 * scale[1], -12.0 *
              scale[0], -8.0 * scale[1], -12.0 * scale[0], -2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], 12.0 * scale[0],
              26.0 * scale[1], 19.0 * scale[0], 19.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], -1.0 * scale[0], -
              11.0 * scale[1], -7.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto_r(-52.0 * scale[0], -53.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -4.0 * scale[0], -
              15.0 * scale[1], -10.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0],
              7.0 * scale[1], -4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(4.0 * scale[0], 8.0 * scale[1], 8.0 * scale[0],
              15.0 * scale[1], 10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 4.0 * scale[0], -
              7.0 * scale[1], 4.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto_r(40.0 * scale[0], -29.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -4.0 * scale[0], -
              17.0 * scale[1], -9.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -7.0 * scale[1], -23.0 * scale[0],
              19.0 * scale[1], -14.0 * scale[0], 28.0 * scale[1])
    Curveto_r(11.0 * scale[0], 11.0 * scale[1], 23.0 * scale[0],
              6.0 * scale[1], 23.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto_r(30.0 * scale[0], -66.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -4.0 * scale[0], -
              10.0 * scale[1], -10.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0],
              5.0 * scale[1], -10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 5.0 * scale[0],
              10.0 * scale[1], 10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              4.0 * scale[1], 10.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto_r(-3.0 * scale[0], -46.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 17.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(-7.0 * scale[0], -58.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -4.0 * scale[0], -
              18.0 * scale[1], -10.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -10.0 * scale[0],
              3.0 * scale[1], -10.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], 5.0 * scale[0],
              21.0 * scale[1], 10.0 * scale[0], 21.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              6.0 * scale[1], 10.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(875.0 * scale[0], 540.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 11.0 * scale[0], -10.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 4.0 * scale[0],
              5.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              10.0 * scale[1], -11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              4.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(36.0 * scale[0], 465.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -8.0 * scale[1], -15.0 *
              scale[0], -15.0 * scale[1], -9.0 * scale[0], -15.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0],
              7.0 * scale[1], 23.0 * scale[0], 15.0 * scale[1])
    Curveto_r(16.0 * scale[0], 19.0 * scale[1], 11.0 * scale[0],
              19.0 * scale[1], -14.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(936.0 * scale[0], 404.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -15.0 * scale[1], -2.0 *
              scale[0], -32.0 * scale[1], 3.0 * scale[0], -37.0 * scale[1])
    Curveto_r(8.0 * scale[0], -8.0 * scale[1], 11.0 * scale[0],
              0.0 * scale[1], 11.0 * scale[0], 26.0 * scale[1])
    Curveto_r(0.0 * scale[0], 44.0 * scale[1], -5.0 * scale[0],
              47.0 * scale[1], -14.0 * scale[0], 11.0 * scale[1])
    te.end_fill()
    Moveto(362.0 * scale[0], 375.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(321.0 * scale[0], 357.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -11.0 * scale[1], -6.0 * scale[0], -
              15.0 * scale[1], -13.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 0.0 * scale[0], -
              13.0 * scale[1], -6.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -3.0 * scale[1], -8.0 *
              scale[0], -6.0 * scale[1], -3.0 * scale[0], -6.0 * scale[1])
    Curveto_r(20.0 * scale[0], -1.0 * scale[1], 37.0 * scale[0],
              17.0 * scale[1], 32.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 18.0 * scale[1], -5.0 * scale[0],
              18.0 * scale[1], -6.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(649.0 * scale[0], 343.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(16.0 * scale[0], 13.0 * scale[1], 21.0 * scale[0],
              21.0 * scale[1], 13.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              8.0 * scale[1], -17.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(235.0 * scale[0], 339.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], 2.0 * scale[0], -
              6.0 * scale[1], 10.0 * scale[0], -5.0 * scale[1])
    Curveto_r(21.0 * scale[0], 3.0 * scale[1], 28.0 * scale[0],
              13.0 * scale[1], 10.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -18.0 * scale[0], -
              4.0 * scale[1], -20.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(609.0 * scale[0], 303.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(16.0 * scale[0], 13.0 * scale[1], 21.0 * scale[0],
              21.0 * scale[1], 13.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              8.0 * scale[1], -17.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(215.0 * scale[0], 230.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -17.0 * scale[1], -4.0 * scale[0], -
              34.0 * scale[1], -1.0 * scale[0], -37.0 * scale[1])
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], 6.0 * scale[0],
              3.0 * scale[1], 6.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], 6.0 * scale[0],
              22.0 * scale[1], 13.0 * scale[0], 25.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 9.0 * scale[0],
              7.0 * scale[1], 1.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 9.0 * scale[1], -14.0 * scale[0],
              5.0 * scale[1], -19.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(941.0 * scale[0], 244.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(285.0 * scale[0], 192.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -11.0 * scale[1], 1.0 * scale[0], -
              24.0 * scale[1], -6.0 * scale[0], -27.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -6.0 * scale[1], -8.0 * scale[0], -
              10.0 * scale[1], 2.0 * scale[0], -16.0 * scale[1])
    Curveto_r(10.0 * scale[0], -6.0 * scale[1], 6.0 * scale[0], -
              11.0 * scale[1], -14.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-41.0 * scale[0], -16.0 * scale[1], -55.0 *
              scale[0], -13.0 * scale[1], -32.0 * scale[0], 6.0 * scale[1])
    Lineto_r(20.0 * scale[0], 16.0 * scale[1])
    Lineto_r(-20.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-35.0 * scale[0], -13.0 * scale[1], -39.0 *
              scale[0], -11.0 * scale[1], -45.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 21.0 * scale[1], -8.0 * scale[0],
              26.0 * scale[1], -14.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], -14.0 * scale[0], -
              11.0 * scale[1], -22.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 3.0 * scale[1], -16.0 * scale[0],
              0.0 * scale[1], -20.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -3.0 *
              scale[0], -8.0 * scale[1], 3.0 * scale[0], -5.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 13.0 * scale[0],
              1.0 * scale[1], 16.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], -1.0 * scale[0], -
              17.0 * scale[1], -9.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -3.0 * scale[1], -12.0 * scale[0], -
              11.0 * scale[1], -8.0 * scale[0], -17.0 * scale[1])
    Curveto_r(4.0 * scale[0], -7.0 * scale[1], 3.0 * scale[0], -
              10.0 * scale[1], -2.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -20.0 * scale[0], -
              12.0 * scale[1], -34.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -22.0 * scale[1], -30.0 *
              scale[0], -37.0 * scale[1], -37.0 * scale[0], -35.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 3.0 * scale[1], -15.0 * scale[0],
              0.0 * scale[1], -19.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -3.0 *
              scale[0], -8.0 * scale[1], 3.0 * scale[0], -5.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 14.0 * scale[0],
              0.0 * scale[1], 17.0 * scale[0], -9.0 * scale[1])
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], 2.0 * scale[0], -
              12.0 * scale[1], -4.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0],
              1.0 * scale[1], -10.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -18.0 * scale[1], 29.0 *
              scale[0], -13.0 * scale[1], 52.0 * scale[0], 9.0 * scale[1])
    Curveto_r(22.0 * scale[0], 20.0 * scale[1], 38.0 * scale[0],
              18.0 * scale[1], 38.0 * scale[0], -6.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 22.0 * scale[0], -
              14.0 * scale[1], 118.0 * scale[0], -14.0 * scale[1])
    Lineto_r(117.0 * scale[0], 0.0 * scale[1])
    Lineto_r(-40.0 * scale[0], 35.0 * scale[1])
    Lineto_r(-40.0 * scale[0], 35.0 * scale[1])
    Lineto_r(33.0 * scale[0], 0.0 * scale[1])
    Curveto_r(39.0 * scale[0], 0.0 * scale[1], 59.0 * scale[0],
              34.0 * scale[1], 36.0 * scale[0], 61.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 8.0 * scale[1], -14.0 * scale[0],
              20.0 * scale[1], -14.0 * scale[0], 25.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -16.0 * scale[0],
              19.0 * scale[1], -36.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-34.0 * scale[0], 22.0 * scale[1], -35.0 * scale[0],
              22.0 * scale[1], -29.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(250.0 * scale[0], 196.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(75.0 * scale[0], 119.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0], -
              12.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 17.0 * scale[1], 1.0 * scale[0],
              20.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(6.0 * scale[0], 22.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 1.0 *
              scale[0], -9.0 * scale[1], 9.0 * scale[0], -9.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              4.0 * scale[1], 9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -7.0 * scale[0],
              8.0 * scale[1], -9.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0], -
              4.0 * scale[1], -9.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(506.0 * scale[0], 21.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], -5.0 * scale[0], -
              15.0 * scale[1], -2.0 * scale[0], -18.0 * scale[1])
    Curveto_r(9.0 * scale[0], -9.0 * scale[1], 19.0 * scale[0],
              4.0 * scale[1], 14.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 11.0 * scale[1], -6.0 * scale[0],
              11.0 * scale[1], -12.0 * scale[0], 0.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#456fa2')
    te.end_fill()
    Moveto(443.0 * scale[0], 1383.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(26.0 * scale[0], -2.0 * scale[1], 68.0 *
              scale[0], -2.0 * scale[1], 95.0 * scale[0], 0.0 * scale[1])
    Curveto_r(26.0 * scale[0], 2.0 * scale[1], 4.0 * scale[0],
              3.0 * scale[1], -48.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-52.0 * scale[0], 0.0 * scale[1], -74.0 *
              scale[0], -1.0 * scale[1], -47.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(854.0 * scale[0], 1382.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 19.0 * scale[0], -
              7.0 * scale[1], 36.0 * scale[0], -4.0 * scale[1])
    Curveto_r(16.0 * scale[0], 2.0 * scale[1], 37.0 * scale[0], -
              1.0 * scale[1], 45.0 * scale[0], -8.0 * scale[1])
    Curveto_r(15.0 * scale[0], -12.0 * scale[1], 35.0 *
              scale[0], -6.0 * scale[1], 35.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -27.0 * scale[0],
              9.0 * scale[1], -61.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-33.0 * scale[0], 0.0 * scale[1], -58.0 *
              scale[0], -4.0 * scale[1], -55.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(7.0 * scale[0], 1373.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -8.0 * scale[1], -9.0 * scale[0], -
              947.0 * scale[1], -1.0 * scale[0], -956.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 45.0 * scale[0],
              26.0 * scale[1], 92.0 * scale[0], 63.0 * scale[1])
    Curveto_r(138.0 * scale[0], 110.0 * scale[1], 142.0 * scale[0],
              114.0 * scale[1], 52.0 * scale[0], 54.0 * scale[1])
    Curveto_r(-47.0 * scale[0], -31.0 * scale[1], -93.0 * scale[0], -
              66.0 * scale[1], -103.0 * scale[0], -77.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -12.0 * scale[1], -21.0 *
              scale[0], -17.0 * scale[1], -27.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 9.0 * scale[1], 53.0 * scale[0],
              120.0 * scale[1], 107.0 * scale[0], 191.0 * scale[1])
    Curveto_r(16.0 * scale[0], 21.0 * scale[1], 19.0 * scale[0],
              33.0 * scale[1], 12.0 * scale[0], 44.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 12.0 * scale[1], -10.0 * scale[0],
              12.0 * scale[1], -6.0 * scale[0], -1.0 * scale[1])
    Curveto_r(2.0 * scale[0], -8.0 * scale[1], -10.0 * scale[0], -
              33.0 * scale[1], -27.0 * scale[0], -55.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -22.0 * scale[1], -42.0 *
              scale[0], -57.0 * scale[1], -55.0 * scale[0], -77.0 * scale[1])
    Curveto_r(-25.0 * scale[0], -42.0 * scale[1], -36.0 *
              scale[0], -49.0 * scale[1], -28.0 * scale[0], -18.0 * scale[1])
    Curveto_r(3.0 * scale[0], 11.0 * scale[1], 1.0 * scale[0],
              20.0 * scale[1], -4.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0],
              170.0 * scale[1], -7.0 * scale[0], 415.0 * scale[1])
    Curveto_r(2.0 * scale[0], 228.0 * scale[1], 3.0 * scale[0],
              415.0 * scale[1], 2.0 * scale[0], 415.0 * scale[1])
    Curveto_r(0.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              3.0 * scale[1], -7.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(963.0 * scale[0], 1330.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -17.0 * scale[1], -7.0 *
              scale[0], -28.0 * scale[1], 1.0 * scale[0], -36.0 * scale[1])
    Curveto_r(8.0 * scale[0], -9.0 * scale[1], 12.0 *
              scale[0], -7.0 * scale[1], 14.0 * scale[0], 7.0 * scale[1])
    Curveto_r(2.0 * scale[0], 11.0 * scale[1], 2.0 * scale[0],
              27.0 * scale[1], -1.0 * scale[0], 37.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 14.0 * scale[1], -6.0 * scale[0],
              13.0 * scale[1], -14.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(465.0 * scale[0], 1280.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 3.0 * scale[0], -
              10.0 * scale[1], 15.0 * scale[0], -10.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 18.0 * scale[0],
              5.0 * scale[1], 15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -10.0 * scale[0],
              10.0 * scale[1], -15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              4.0 * scale[1], -15.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(525.0 * scale[0], 1280.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 11.0 * scale[0], -
              10.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              5.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -11.0 * scale[0],
              10.0 * scale[1], -16.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              4.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(577.0 * scale[0], 1254.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -15.0 * scale[1], 23.0 * scale[0], -
              19.0 * scale[1], 23.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -7.0 * scale[0],
              11.0 * scale[1], -14.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 4.0 * scale[1], -13.0 * scale[0],
              1.0 * scale[1], -9.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(620.0 * scale[0], 1200.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -16.0 * scale[1], 25.0 * scale[0], -
              30.0 * scale[1], 29.0 * scale[0], -30.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 26.0 * scale[0], -
              19.0 * scale[1], 49.0 * scale[0], -42.0 * scale[1])
    Curveto_r(23.0 * scale[0], -22.0 * scale[1], 42.0 * scale[0], -
              38.0 * scale[1], 42.0 * scale[0], -33.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -130.0 * scale[0],
              135.0 * scale[1], -138.0 * scale[0], 135.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], 6.0 * scale[0], -
              13.0 * scale[1], 18.0 * scale[0], -30.0 * scale[1])
    te.end_fill()
    Moveto(551.0 * scale[0], 1207.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -8.0 * scale[1], -8.0 * scale[0], -
              17.0 * scale[1], -4.0 * scale[0], -20.0 * scale[1])
    Curveto_r(7.0 * scale[0], -8.0 * scale[1], 33.0 * scale[0],
              11.0 * scale[1], 33.0 * scale[0], 24.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], -16.0 * scale[0],
              11.0 * scale[1], -29.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(823.0 * scale[0], 1133.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-163.0 * scale[0], -229.0 * scale[1], -227.0 *
              scale[0], -323.0 * scale[1], -220.0 * scale[0], -323.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 94.0 * scale[0],
              121.0 * scale[1], 121.0 * scale[0], 163.0 * scale[1])
    Curveto_r(9.0 * scale[0], 16.0 * scale[1], 25.0 * scale[0],
              36.0 * scale[1], 34.0 * scale[0], 46.0 * scale[1])
    Curveto_r(9.0 * scale[0], 9.0 * scale[1], 26.0 * scale[0],
              30.0 * scale[1], 37.0 * scale[0], 45.0 * scale[1])
    Curveto_r(11.0 * scale[0], 16.0 * scale[1], 25.0 * scale[0],
              33.0 * scale[1], 31.0 * scale[0], 40.0 * scale[1])
    Curveto_r(6.0 * scale[0], 6.0 * scale[1], 16.0 * scale[0],
              22.0 * scale[1], 23.0 * scale[0], 34.0 * scale[1])
    Curveto_r(7.0 * scale[0], 12.0 * scale[1], 16.0 * scale[0],
              20.0 * scale[1], 20.0 * scale[0], 17.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 8.0 * scale[0],
              6.0 * scale[1], 7.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -2.0 * scale[0],
              25.0 * scale[1], -3.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 0.0 * scale[1], -23.0 * scale[0], -
              30.0 * scale[1], -50.0 * scale[0], -67.0 * scale[1])
    te.end_fill()
    Moveto(970.0 * scale[0], 1080.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -131.0 * scale[1], 1.0 * scale[0], -
              122.0 * scale[1], -11.0 * scale[0], -137.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -7.0 * scale[1], -5.0 * scale[0], -
              13.0 * scale[1], 3.0 * scale[0], -15.0 * scale[1])
    Curveto_r(9.0 * scale[0], -3.0 * scale[1], -3.0 * scale[0], -
              31.0 * scale[1], -36.0 * scale[0], -89.0 * scale[1])
    Curveto_r(-27.0 * scale[0], -46.0 * scale[1], -52.0 *
              scale[0], -86.0 * scale[1], -56.0 * scale[0], -89.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -15.0 * scale[0], -
              20.0 * scale[1], -25.0 * scale[0], -37.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -18.0 * scale[1], -23.0 *
              scale[0], -33.0 * scale[1], -27.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              4.0 * scale[1], -8.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              10.0 * scale[1], 15.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              7.0 * scale[1], 15.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], 17.0 * scale[0],
              39.0 * scale[1], 38.0 * scale[0], 67.0 * scale[1])
    Curveto_r(22.0 * scale[0], 28.0 * scale[1], 46.0 * scale[0],
              65.0 * scale[1], 55.0 * scale[0], 83.0 * scale[1])
    Curveto_r(9.0 * scale[0], 17.0 * scale[1], 21.0 * scale[0],
              34.0 * scale[1], 25.0 * scale[0], 37.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 10.0 * scale[0], -
              77.0 * scale[1], 11.0 * scale[0], -177.0 * scale[1])
    Curveto_r(1.0 * scale[0], -100.0 * scale[1], 4.0 * scale[0], -
              184.0 * scale[1], 7.0 * scale[0], -186.0 * scale[1])
    Curveto_r(2.0 * scale[0], -2.0 * scale[1], 4.0 * scale[0],
              152.0 * scale[1], 4.0 * scale[0], 342.0 * scale[1])
    Curveto_r(0.0 * scale[0], 191.0 * scale[1], -2.0 * scale[0],
              347.0 * scale[1], -5.0 * scale[0], 347.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -5.0 * scale[0], -
              49.0 * scale[1], -5.0 * scale[0], -110.0 * scale[1])
    te.end_fill()
    Moveto(560.0 * scale[0], 1114.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -3.0 * scale[1], 11.0 * scale[0], -
              15.0 * scale[1], 25.0 * scale[0], -26.0 * scale[1])
    Curveto_r(14.0 * scale[0], -11.0 * scale[1], 25.0 * scale[0], -
              27.0 * scale[1], 26.0 * scale[0], -36.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 2.0 * scale[0], -
              13.0 * scale[1], 6.0 * scale[0], -4.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], -1.0 * scale[0],
              20.0 * scale[1], -9.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 15.0 * scale[1], -10.0 * scale[0],
              16.0 * scale[1], 17.0 * scale[0], 10.0 * scale[1])
    Curveto_r(26.0 * scale[0], -5.0 * scale[1], 24.0 * scale[0], -
              4.0 * scale[1], -10.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-44.0 * scale[0], 20.0 * scale[1], -55.0 * scale[0],
              23.0 * scale[1], -55.0 * scale[0], 14.0 * scale[1])
    te.end_fill()
    Moveto(668.0 * scale[0], 1073.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(622.0 * scale[0], 990.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 2.0 * scale[0], -
              27.0 * scale[1], 5.0 * scale[0], -17.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              25.0 * scale[1], 0.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(879.0 * scale[0], 886.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-31.0 * scale[0], -22.0 * scale[1], -64.0 *
              scale[0], -49.0 * scale[1], -73.0 * scale[0], -58.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -10.0 * scale[1], -22.0 *
              scale[0], -18.0 * scale[1], -27.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              5.0 * scale[1], -9.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 80.0 * scale[0],
              42.0 * scale[1], 146.0 * scale[0], 95.0 * scale[1])
    Curveto_r(51.0 * scale[0], 41.0 * scale[1], 21.0 * scale[0],
              34.0 * scale[1], -37.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(133.0 * scale[0], 765.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -9.0 * scale[1], -3.0 * scale[0], -
              18.0 * scale[1], -1.0 * scale[0], -21.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 8.0 * scale[0],
              4.0 * scale[1], 11.0 * scale[0], 16.0 * scale[1])
    Curveto_r(6.0 * scale[0], 23.0 * scale[1], -1.0 * scale[0],
              27.0 * scale[1], -10.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(487.0 * scale[0], 773.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -12.0 * scale[1], -7.0 *
              scale[0], -43.0 * scale[1], 8.0 * scale[0], -43.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 15.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -5.0 * scale[0],
              7.0 * scale[1], -12.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -5.0 * scale[1], -9.0 * scale[0],
              0.0 * scale[1], -6.0 * scale[0], 14.0 * scale[1])
    Curveto_r(6.0 * scale[0], 23.0 * scale[1], 5.0 * scale[0],
              26.0 * scale[1], -5.0 * scale[0], 15.0 * scale[1])
    te.end_fill()
    Moveto(401.0 * scale[0], 717.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -11.0 * scale[1], -6.0 * scale[0], -
              13.0 * scale[1], 11.0 * scale[0], -13.0 * scale[1])
    Curveto_r(17.0 * scale[0], 1.0 * scale[1], 24.0 * scale[0], -
              6.0 * scale[1], 29.0 * scale[0], -29.0 * scale[1])
    Curveto_r(6.0 * scale[0], -27.0 * scale[1], 7.0 * scale[0], -
              27.0 * scale[1], 7.0 * scale[0], -5.0 * scale[1])
    Curveto_r(1.0 * scale[0], 23.0 * scale[1], -18.0 * scale[0],
              60.0 * scale[1], -30.0 * scale[0], 60.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              6.0 * scale[1], -17.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(532.0 * scale[0], 700.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(639.0 * scale[0], 703.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -21.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(155.0 * scale[0], 699.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -17.0 * scale[1], 1.0 *
              scale[0], -21.0 * scale[1], 15.0 * scale[0], -4.0 * scale[1])
    Curveto_r(8.0 * scale[0], 9.0 * scale[1], 8.0 * scale[0],
              15.0 * scale[1], 2.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0], -
              5.0 * scale[1], -17.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(300.0 * scale[0], 639.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-35.0 * scale[0], -31.0 * scale[1])
    Lineto_r(32.0 * scale[0], 22.0 * scale[1])
    Curveto_r(29.0 * scale[0], 19.0 * scale[1], 50.0 * scale[0],
              40.0 * scale[1], 41.0 * scale[0], 40.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -19.0 * scale[0], -
              14.0 * scale[1], -38.0 * scale[0], -31.0 * scale[1])
    te.end_fill()
    Moveto(555.0 * scale[0], 650.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 11.0 * scale[0], -
              8.0 * scale[1], 16.0 * scale[0], -5.0 * scale[1])
    Curveto_r(14.0 * scale[0], 9.0 * scale[1], 11.0 * scale[0],
              15.0 * scale[1], -7.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              5.0 * scale[1], -9.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(490.0 * scale[0], 633.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 5.0 * scale[0], -
              15.0 * scale[1], 10.0 * scale[0], -23.0 * scale[1])
    Curveto_r(8.0 * scale[0], -13.0 * scale[1], 10.0 *
              scale[0], -13.0 * scale[1], 10.0 * scale[0], 2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], -4.0 * scale[0],
              20.0 * scale[1], -10.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0],
              3.0 * scale[1], -10.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(825.0 * scale[0], 590.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              10.0 * scale[1], 4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              5.0 * scale[1], 11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -2.0 * scale[0],
              10.0 * scale[1], -4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              4.0 * scale[1], -11.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(353.0 * scale[0], 528.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-15.0 * scale[0], -20.0 * scale[1], -25.0 *
              scale[0], -38.0 * scale[1], -20.0 * scale[0], -38.0 * scale[1])
    Curveto_r(3.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              11.0 * scale[1], 21.0 * scale[0], 25.0 * scale[1])
    Curveto_r(17.0 * scale[0], 26.0 * scale[1], 16.0 * scale[0],
              35.0 * scale[1], -1.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(299.0 * scale[0], 458.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -23.0 * scale[1], -12.0 *
              scale[0], -23.0 * scale[1], 10.0 * scale[0], -4.0 * scale[1])
    Curveto_r(23.0 * scale[0], 21.0 * scale[1], 26.0 * scale[0],
              26.0 * scale[1], 11.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              10.0 * scale[1], -21.0 * scale[0], -22.0 * scale[1])
    te.end_fill()
    Moveto(352.0 * scale[0], 390.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(244.0 * scale[0], 378.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -13.0 * scale[1], -28.0 *
              scale[0], -36.0 * scale[1], -38.0 * scale[0], -51.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -15.0 * scale[1], -21.0 * scale[0], -
              25.0 * scale[1], -26.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -7.0 * scale[0],
              0.0 * scale[1], -5.0 * scale[0], -8.0 * scale[1])
    Curveto_r(3.0 * scale[0], -7.0 * scale[1], -6.0 * scale[0], -
              26.0 * scale[1], -20.0 * scale[0], -41.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -15.0 * scale[1], -32.0 *
              scale[0], -41.0 * scale[1], -42.0 * scale[0], -59.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -29.0 * scale[1], -14.0 *
              scale[0], -31.0 * scale[1], 0.0 * scale[0], -19.0 * scale[1])
    Curveto_r(13.0 * scale[0], 11.0 * scale[1], 120.0 * scale[0],
              160.0 * scale[1], 150.0 * scale[0], 209.0 * scale[1])
    Curveto_r(12.0 * scale[0], 20.0 * scale[1], 3.0 * scale[0],
              15.0 * scale[1], -19.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(371.0 * scale[0], 291.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -16.0 * scale[1], 17.0 * scale[0], -
              32.0 * scale[1], 26.0 * scale[0], -35.0 * scale[1])
    Curveto_r(28.0 * scale[0], -11.0 * scale[1], 26.0 * scale[0],
              2.0 * scale[1], -5.0 * scale[0], 34.0 * scale[1])
    Lineto_r(-31.0 * scale[0], 31.0 * scale[1])
    Lineto_r(10.0 * scale[0], -30.0 * scale[1])
    te.end_fill()
    Moveto(320.0 * scale[0], 286.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 9.0 * scale[0], -
              6.0 * scale[1], 20.0 * scale[0], -9.0 * scale[1])
    Curveto_r(11.0 * scale[0], -3.0 * scale[1], 18.0 *
              scale[0], -1.0 * scale[1], 14.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 9.0 * scale[1], -34.0 * scale[0],
              13.0 * scale[1], -34.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(275.0 * scale[0], 230.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 0.0 * scale[0], -
              10.0 * scale[1], 7.0 * scale[0], -10.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 52.0 * scale[0], -
              36.0 * scale[1], 94.0 * scale[0], -88.0 * scale[1])
    Curveto_r(15.0 * scale[0], -18.0 * scale[1], 29.0 * scale[0], -
              31.0 * scale[1], 31.0 * scale[0], -28.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -6.0 * scale[0],
              19.0 * scale[1], -20.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 17.0 * scale[1], -27.0 * scale[0],
              34.0 * scale[1], -29.0 * scale[0], 38.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 18.0 * scale[1], -77.0 * scale[0],
              62.0 * scale[1], -83.0 * scale[0], 53.0 * scale[1])
    te.end_fill()
    Moveto(968.0 * scale[0], 145.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -35.0 * scale[1], 0.0 * scale[0], -
              75.0 * scale[1], 4.0 * scale[0], -87.0 * scale[1])
    Curveto_r(3.0 * scale[0], -13.0 * scale[1], 6.0 * scale[0],
              16.0 * scale[1], 7.0 * scale[0], 65.0 * scale[1])
    Curveto_r(1.0 * scale[0], 102.0 * scale[1], -6.0 * scale[0],
              116.0 * scale[1], -11.0 * scale[0], 22.0 * scale[1])
    te.end_fill()
    Moveto(411.0 * scale[0], 176.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -8.0 * scale[1], -8.0 * scale[0], -
              17.0 * scale[1], -3.0 * scale[0], -20.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 15.0 * scale[0],
              1.0 * scale[1], 21.0 * scale[0], 8.0 * scale[1])
    Curveto_r(7.0 * scale[0], 8.0 * scale[1], 8.0 * scale[0],
              17.0 * scale[1], 3.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -15.0 * scale[0], -
              1.0 * scale[1], -21.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(545.0 * scale[0], 120.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              10.0 * scale[1], 4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              5.0 * scale[1], 11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -2.0 * scale[0],
              10.0 * scale[1], -4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              4.0 * scale[1], -11.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(8.0 * scale[0], 70.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -56.0 * scale[1], -4.0 * scale[0], -
              61.0 * scale[1], 17.0 * scale[0], -20.0 * scale[1])
    Curveto_r(9.0 * scale[0], 18.0 * scale[1], 12.0 * scale[0],
              29.0 * scale[1], 7.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -3.0 * scale[1], -12.0 * scale[0],
              4.0 * scale[1], -14.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 15.0 * scale[1], -6.0 * scale[0],
              6.0 * scale[1], -10.0 * scale[0], -22.0 * scale[1])
    te.end_fill()
    Moveto(440.0 * scale[0], 91.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              11.0 * scale[1], 14.0 * scale[0], -14.0 * scale[1])
    Curveto_r(10.0 * scale[0], -4.0 * scale[1], 13.0 *
              scale[0], -1.0 * scale[1], 9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 15.0 * scale[1], -23.0 * scale[0],
              19.0 * scale[1], -23.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(490.0 * scale[0], 90.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 4.0 * scale[0], -
              10.0 * scale[1], 9.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              5.0 * scale[1], 16.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], -1.0 * scale[0],
              10.0 * scale[1], -9.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#608bc3')
    te.end_fill()
    Moveto(20.0 * scale[0], 1379.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -5.0 * scale[0], -
              7.0 * scale[1], -12.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -4.0 * scale[0], -5.0 * scale[1])
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 13.0 * scale[0], -
              8.0 * scale[1], 19.0 * scale[0], -4.0 * scale[1])
    Curveto_r(7.0 * scale[0], 5.0 * scale[1], 84.0 * scale[0],
              11.0 * scale[1], 172.0 * scale[0], 14.0 * scale[1])
    Lineto_r(160.0 * scale[0], 5.0 * scale[1])
    Lineto_r(-167.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-113.0 * scale[0], 1.0 * scale[1], -168.0 *
              scale[0], -1.0 * scale[1], -168.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(404.0 * scale[0], 1364.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(8.0 * scale[0], -16.0 * scale[1], 13.0 * scale[0], -
              19.0 * scale[1], 19.0 * scale[0], -11.0 * scale[1])
    Curveto_r(5.0 * scale[0], 7.0 * scale[1], 7.0 * scale[0], -
              1.0 * scale[1], 4.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -46.0 * scale[1], 8.0 *
              scale[0], -41.0 * scale[1], 20.0 * scale[0], 6.0 * scale[1])
    Curveto_r(10.0 * scale[0], 39.0 * scale[1], 10.0 * scale[0],
              39.0 * scale[1], -21.0 * scale[0], 43.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 3.0 * scale[1], -31.0 * scale[0],
              2.0 * scale[1], -22.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(538.0 * scale[0], 1382.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-27.0 * scale[0], -2.0 * scale[1], -48.0 *
              scale[0], -8.0 * scale[1], -48.0 * scale[0], -14.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 9.0 * scale[0], -
              8.0 * scale[1], 20.0 * scale[0], -5.0 * scale[1])
    Curveto_r(11.0 * scale[0], 3.0 * scale[1], 35.0 * scale[0],
              1.0 * scale[1], 55.0 * scale[0], -3.0 * scale[1])
    Curveto_r(19.0 * scale[0], -4.0 * scale[1], 35.0 *
              scale[0], -5.0 * scale[1], 35.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 18.0 * scale[1], -20.0 * scale[0],
              26.0 * scale[1], -62.0 * scale[0], 23.0 * scale[1])
    te.end_fill()
    Moveto(838.0 * scale[0], 1383.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 12.0 * scale[0], -
              11.0 * scale[1], 12.0 * scale[0], -19.0 * scale[1])
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 12.0 * scale[0], -
              18.0 * scale[1], 26.0 * scale[0], -5.0 * scale[1])
    Curveto_r(5.0 * scale[0], 5.0 * scale[1], 20.0 * scale[0],
              12.0 * scale[1], 34.0 * scale[0], 14.0 * scale[1])
    Curveto_r(16.0 * scale[0], 3.0 * scale[1], 12.0 * scale[0],
              5.0 * scale[1], -12.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -1.0 * scale[1], -40.0 * scale[0],
              2.0 * scale[1], -44.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 4.0 * scale[1], -12.0 * scale[0],
              7.0 * scale[1], -18.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -5.0 *
              scale[0], -3.0 * scale[1], 2.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(489.0 * scale[0], 1348.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -16.0 * scale[1], -3.0 *
              scale[0], -61.0 * scale[1], 3.0 * scale[0], -64.0 * scale[1])
    Curveto_r(4.0 * scale[0], -3.0 * scale[1], 8.0 * scale[0],
              11.0 * scale[1], 8.0 * scale[0], 30.0 * scale[1])
    Curveto_r(0.0 * scale[0], 20.0 * scale[1], -2.0 * scale[0],
              36.0 * scale[1], -5.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -6.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(600.0 * scale[0], 1331.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], 8.0 * scale[0], -
              16.0 * scale[1], 43.0 * scale[0], -25.0 * scale[1])
    Curveto_r(24.0 * scale[0], -6.0 * scale[1], 27.0 *
              scale[0], -5.0 * scale[1], 15.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 7.0 * scale[1], -16.0 * scale[0],
              12.0 * scale[1], -20.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -2.0 * scale[1], -9.0 * scale[0],
              0.0 * scale[1], -13.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 13.0 * scale[1], -25.0 * scale[0],
              13.0 * scale[1], -25.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(13.0 * scale[0], 1172.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -152.0 * scale[1], -1.0 *
              scale[0], -154.0 * scale[1], 8.0 * scale[0], -67.0 * scale[1])
    Curveto_r(5.0 * scale[0], 50.0 * scale[1], 8.0 * scale[0],
              101.0 * scale[1], 7.0 * scale[0], 115.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 14.0 * scale[1], 2.0 * scale[0],
              30.0 * scale[1], 9.0 * scale[0], 35.0 * scale[1])
    Curveto_r(8.0 * scale[0], 8.0 * scale[1], 7.0 * scale[0],
              18.0 * scale[1], -6.0 * scale[0], 42.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 31.0 * scale[1], -18.0 * scale[0],
              30.0 * scale[1], -18.0 * scale[0], -125.0 * scale[1])
    te.end_fill()
    Moveto(450.0 * scale[0], 1290.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -4.0 * scale[0], -
              9.0 * scale[1], -9.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -12.0 * scale[0],
              1.0 * scale[1], -15.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              12.0 * scale[1], 3.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 2.0 * scale[0], -
              14.0 * scale[1], -9.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -11.0 * scale[1], -20.0 *
              scale[0], -28.0 * scale[1], -19.0 * scale[0], -37.0 * scale[1])
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              15.0 * scale[1], 6.0 * scale[0], -3.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], 15.0 * scale[0],
              25.0 * scale[1], 26.0 * scale[0], 38.0 * scale[1])
    Curveto_r(11.0 * scale[0], 12.0 * scale[1], 17.0 * scale[0],
              22.0 * scale[1], 12.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -1.0 * scale[0],
              6.0 * scale[1], 10.0 * scale[0], 13.0 * scale[1])
    Curveto_r(12.0 * scale[0], 10.0 * scale[1], 14.0 * scale[0],
              16.0 * scale[1], 7.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -12.0 * scale[0],
              2.0 * scale[1], -12.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(549.0 * scale[0], 1300.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -3.0 * scale[1], -2.0 * scale[0], -
              12.0 * scale[1], -4.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -12.0 * scale[1], 2.0 * scale[0], -
              15.0 * scale[1], 18.0 * scale[0], -11.0 * scale[1])
    Curveto_r(15.0 * scale[0], 4.0 * scale[1], 18.0 * scale[0],
              2.0 * scale[1], 12.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -12.0 * scale[1], -6.0 *
              scale[0], -12.0 * scale[1], 8.0 * scale[0], 0.0 * scale[1])
    Curveto_r(20.0 * scale[0], 16.0 * scale[1], 23.0 * scale[0],
              35.0 * scale[1], 3.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -3.0 * scale[1], -19.0 * scale[0],
              0.0 * scale[1], -25.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 6.0 * scale[1], -11.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(930.0 * scale[0], 1285.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -8.0 * scale[1], -9.0 * scale[0], -
              15.0 * scale[1], -5.0 * scale[0], -15.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], -3.0 * scale[0], -
              9.0 * scale[1], -16.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -10.0 * scale[1], -20.0 *
              scale[0], -19.0 * scale[1], -14.0 * scale[0], -20.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 0.0 * scale[0], -
              7.0 * scale[1], -12.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -14.0 * scale[1], -22.0 *
              scale[0], -45.0 * scale[1], -4.0 * scale[0], -45.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 31.0 * scale[0],
              57.0 * scale[1], 28.0 * scale[0], 65.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 2.0 * scale[1], 7.0 * scale[0],
              11.0 * scale[1], 18.0 * scale[0], 19.0 * scale[1])
    Curveto_r(14.0 * scale[0], 10.0 * scale[1], 22.0 * scale[0],
              11.0 * scale[1], 27.0 * scale[0], 4.0 * scale[1])
    Curveto_r(3.0 * scale[0], -6.0 * scale[1], 6.0 * scale[0], -
              65.0 * scale[1], 6.0 * scale[0], -131.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -104.0 * scale[1], -3.0 * scale[0], -
              118.0 * scale[1], -15.0 * scale[0], -101.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 10.0 * scale[1], -19.0 * scale[0],
              35.0 * scale[1], -25.0 * scale[0], 56.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 21.0 * scale[1], -20.0 * scale[0],
              47.0 * scale[1], -31.0 * scale[0], 59.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 23.0 * scale[1], -18.0 * scale[0],
              25.0 * scale[1], -57.0 * scale[0], -31.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -12.0 * scale[1], -22.0 * scale[0], -
              30.0 * scale[1], -30.0 * scale[0], -40.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -10.0 * scale[1], -26.0 * scale[0], -
              32.0 * scale[1], -39.0 * scale[0], -49.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -16.0 * scale[1], -29.0 *
              scale[0], -28.0 * scale[1], -33.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 7.0 * scale[1], -5.0 * scale[0], -
              19.0 * scale[1], 6.0 * scale[0], -28.0 * scale[1])
    Curveto_r(11.0 * scale[0], -8.0 * scale[1], 47.0 * scale[0],
              13.0 * scale[1], 40.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -1.0 * scale[0],
              8.0 * scale[1], 5.0 * scale[0], 8.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0],
              7.0 * scale[1], 5.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 8.0 * scale[1], -2.0 * scale[0],
              15.0 * scale[1], 4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              18.0 * scale[1], 10.0 * scale[0], -39.0 * scale[1])
    Curveto_r(1.0 * scale[0], -33.0 * scale[1], -2.0 * scale[0], -
              39.0 * scale[1], -16.0 * scale[0], -34.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -2.0 * scale[0], -8.0 * scale[1])
    Curveto_r(8.0 * scale[0], -8.0 * scale[1], 24.0 * scale[0], -
              18.0 * scale[1], 35.0 * scale[0], -23.0 * scale[1])
    Curveto_r(15.0 * scale[0], -5.0 * scale[1], 16.0 *
              scale[0], -9.0 * scale[1], 6.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -6.0 * scale[1], -9.0 *
              scale[0], -10.0 * scale[1], 5.0 * scale[0], -15.0 * scale[1])
    Curveto_r(11.0 * scale[0], -4.0 * scale[1], 14.0 * scale[0], -
              10.0 * scale[1], 8.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -12.0 * scale[1], -45.0 *
              scale[0], -62.0 * scale[1], -35.0 * scale[0], -62.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              9.0 * scale[1], 16.0 * scale[0], 20.0 * scale[1])
    Curveto_r(4.0 * scale[0], 11.0 * scale[1], 11.0 * scale[0],
              18.0 * scale[1], 16.0 * scale[0], 14.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 8.0 * scale[0],
              0.0 * scale[1], 7.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 7.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], 12.0 * scale[0], 10.0 * scale[1])
    Curveto_r(11.0 * scale[0], -3.0 * scale[1], 10.0 * scale[0],
              2.0 * scale[1], -4.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 12.0 * scale[1], -14.0 * scale[0],
              21.0 * scale[1], -8.0 * scale[0], 21.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              0.0 * scale[1], 20.0 * scale[0], 0.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0], -
              4.0 * scale[1], 8.0 * scale[0], -10.0 * scale[1])
    Curveto_r(1.0 * scale[0], -5.0 * scale[1], 2.0 * scale[0], -
              13.0 * scale[1], 3.0 * scale[0], -16.0 * scale[1])
    Curveto_r(0.0 * scale[0], -3.0 * scale[1], 15.0 * scale[0],
              4.0 * scale[1], 31.0 * scale[0], 16.0 * scale[1])
    Curveto_r(17.0 * scale[0], 12.0 * scale[1], 27.0 * scale[0],
              27.0 * scale[1], 24.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 8.0 * scale[1], -2.0 * scale[0],
              8.0 * scale[1], 7.0 * scale[0], 0.0 * scale[1])
    Curveto_r(15.0 * scale[0], -15.0 * scale[1], 33.0 *
              scale[0], -17.0 * scale[1], 24.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], -1.0 * scale[0],
              12.0 * scale[1], 4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 9.0 * scale[0],
              52.0 * scale[1], 10.0 * scale[0], 108.0 * scale[1])
    Curveto_r(1.0 * scale[0], 57.0 * scale[1], 4.0 * scale[0],
              124.0 * scale[1], 7.0 * scale[0], 150.0 * scale[1])
    Curveto_r(11.0 * scale[0], 81.0 * scale[1], -13.0 * scale[0],
              123.0 * scale[1], -46.0 * scale[0], 83.0 * scale[1])
    te.end_fill()
    Moveto_r(-9.0 * scale[0], -320.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(11.0 * scale[0], 6.0 * scale[1], 11.0 * scale[0],
              5.0 * scale[1], 2.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -14.0 * scale[1], -33.0 *
              scale[0], -6.0 * scale[1], -33.0 * scale[0], 13.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 3.0 * scale[0],
              7.0 * scale[1], 9.0 * scale[0], -2.0 * scale[1])
    Curveto_r(5.0 * scale[0], -8.0 * scale[1], 14.0 * scale[0], -
              10.0 * scale[1], 22.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto_r(-11.0 * scale[0], -45.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              10.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0],
              5.0 * scale[1], -11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -1.0 * scale[0],
              10.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0], -
              4.0 * scale[1], 11.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(595.0 * scale[0], 1240.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              10.0 * scale[1], 4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              5.0 * scale[1], 11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -2.0 * scale[0],
              10.0 * scale[1], -4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              4.0 * scale[1], -11.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(653.0 * scale[0], 1175.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 3.0 * scale[0], -
              12.0 * scale[1], 7.0 * scale[0], -10.0 * scale[1])
    Curveto_r(12.0 * scale[0], 7.0 * scale[1], 51.0 * scale[0], -
              26.0 * scale[1], 44.0 * scale[0], -37.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], -2.0 *
              scale[0], -8.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(7.0 * scale[0], 4.0 * scale[1], 12.0 * scale[0],
              2.0 * scale[1], 12.0 * scale[0], -3.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 5.0 * scale[0], -
              11.0 * scale[1], 12.0 * scale[0], -11.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0],
              35.0 * scale[1], -53.0 * scale[0], 61.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 14.0 * scale[1], -26.0 * scale[0],
              15.0 * scale[1], -26.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(392.0 * scale[0], 1150.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 2.0 * scale[0], -
              27.0 * scale[1], 5.0 * scale[0], -17.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              25.0 * scale[1], 0.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(334.0 * scale[0], 1052.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-62.0 * scale[0], -70.0 * scale[1], -164.0 * scale[0], -
              207.0 * scale[1], -164.0 * scale[0], -221.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -3.0 * scale[0], -
              11.0 * scale[1], -7.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -32.0 * scale[0], -
              49.0 * scale[1], -23.0 * scale[0], -55.0 * scale[1])
    Curveto_r(4.0 * scale[0], -3.0 * scale[1], 23.0 * scale[0],
              21.0 * scale[1], 40.0 * scale[0], 52.0 * scale[1])
    Curveto_r(55.0 * scale[0], 98.0 * scale[1], 110.0 * scale[0],
              176.0 * scale[1], 163.0 * scale[0], 230.0 * scale[1])
    Curveto_r(28.0 * scale[0], 29.0 * scale[1], 49.0 * scale[0],
              55.0 * scale[1], 46.0 * scale[0], 57.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 2.0 * scale[1], -27.0 * scale[0], -
              21.0 * scale[1], -55.0 * scale[0], -52.0 * scale[1])
    te.end_fill()
    Moveto(625.0 * scale[0], 1090.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -10.0 *
              scale[0], -8.0 * scale[1], -15.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -11.0 * scale[0],
              1.0 * scale[1], -14.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -19.0 * scale[1], 12.0 *
              scale[0], -20.0 * scale[1], 29.0 * scale[0], -1.0 * scale[1])
    Curveto_r(10.0 * scale[0], 11.0 * scale[1], 15.0 * scale[0],
              20.0 * scale[1], 12.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              5.0 * scale[1], -12.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(740.0 * scale[0], 1084.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], -7.0 * scale[0], -
              15.0 * scale[1], -25.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 3.0 * scale[1], -28.0 * scale[0],
              1.0 * scale[1], -31.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0], -
              9.0 * scale[1], 17.0 * scale[0], -9.0 * scale[1])
    Curveto_r(18.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0], -
              2.0 * scale[1], 9.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-22.0 * scale[0], -26.0 * scale[1], -2.0 *
              scale[0], -16.0 * scale[1], 25.0 * scale[0], 12.0 * scale[1])
    Curveto_r(27.0 * scale[0], 29.0 * scale[1], 31.0 * scale[0],
              43.0 * scale[1], 15.0 * scale[0], 43.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              7.0 * scale[1], -10.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(645.0 * scale[0], 1080.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              10.0 * scale[1], 4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              5.0 * scale[1], 16.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              10.0 * scale[1], -4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(622.0 * scale[0], 1040.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(683.0 * scale[0], 999.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -12.0 * scale[1], -11.0 * scale[0], -
              18.0 * scale[1], -20.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -11.0 * scale[0],
              1.0 * scale[1], -8.0 * scale[0], -4.0 * scale[1])
    Curveto_r(10.0 * scale[0], -16.0 * scale[1], 22.0 *
              scale[0], -12.0 * scale[1], 39.0 * scale[0], 15.0 * scale[1])
    Curveto_r(10.0 * scale[0], 15.0 * scale[1], 12.0 * scale[0],
              25.0 * scale[1], 5.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              9.0 * scale[1], -16.0 * scale[0], -21.0 * scale[1])
    te.end_fill()
    Moveto(605.0 * scale[0], 925.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -32.0 * scale[1], -46.0 *
              scale[0], -76.0 * scale[1], -67.0 * scale[0], -98.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -22.0 * scale[1], -37.0 *
              scale[0], -42.0 * scale[1], -35.0 * scale[0], -43.0 * scale[1])
    Curveto_r(9.0 * scale[0], -9.0 * scale[1], 87.0 * scale[0],
              79.0 * scale[1], 107.0 * scale[0], 120.0 * scale[1])
    Curveto_r(13.0 * scale[0], 29.0 * scale[1], 26.0 * scale[0],
              43.0 * scale[1], 30.0 * scale[0], 36.0 * scale[1])
    Curveto_r(5.0 * scale[0], -7.0 * scale[1], 11.0 *
              scale[0], -6.0 * scale[1], 21.0 * scale[0], 6.0 * scale[1])
    Curveto_r(12.0 * scale[0], 16.0 * scale[1], 12.0 * scale[0],
              17.0 * scale[1], -3.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -4.0 * scale[1], -18.0 * scale[0],
              0.0 * scale[1], -20.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 10.0 * scale[1], -16.0 * scale[0], -
              8.0 * scale[1], -33.0 * scale[0], -42.0 * scale[1])
    te.end_fill()
    Moveto(694.0 * scale[0], 958.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], -4.0 *
              scale[0], -10.0 * scale[1], 1.0 * scale[0], -6.0 * scale[1])
    Curveto_r(4.0 * scale[0], 4.0 * scale[1], 14.0 * scale[0],
              3.0 * scale[1], 22.0 * scale[0], -4.0 * scale[1])
    Curveto_r(7.0 * scale[0], -6.0 * scale[1], 16.0 * scale[0], -
              8.0 * scale[1], 19.0 * scale[0], -5.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -3.0 * scale[0],
              10.0 * scale[1], -15.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 8.0 * scale[1], -22.0 * scale[0],
              8.0 * scale[1], -27.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(699.0 * scale[0], 937.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -4.0 * scale[1], -2.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -9.0 * scale[1], -48.0 * scale[0], -
              57.0 * scale[1], -59.0 * scale[0], -60.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -2.0 * scale[1], -10.0 *
              scale[0], -3.0 * scale[1], -13.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -1.0 * scale[0], -
              7.0 * scale[1], 6.0 * scale[0], -15.0 * scale[1])
    Curveto_r(12.0 * scale[0], -15.0 * scale[1], 4.0 * scale[0], -
              21.0 * scale[1], -23.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 1.0 * scale[1], -6.0 * scale[0], -
              3.0 * scale[1], -2.0 * scale[0], -9.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              10.0 * scale[1], -6.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -10.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], -4.0 * scale[0], -
              15.0 * scale[1], -16.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -10.0 * scale[1], -17.0 *
              scale[0], -18.0 * scale[1], -10.0 * scale[0], -19.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 22.0 * scale[0],
              13.0 * scale[1], 36.0 * scale[0], 29.0 * scale[1])
    Curveto_r(14.0 * scale[0], 17.0 * scale[1], 27.0 * scale[0],
              28.0 * scale[1], 30.0 * scale[0], 25.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 8.0 * scale[0],
              4.0 * scale[1], 12.0 * scale[0], 16.0 * scale[1])
    Curveto_r(8.0 * scale[0], 26.0 * scale[1], 51.0 * scale[0],
              70.0 * scale[1], 61.0 * scale[0], 61.0 * scale[1])
    Curveto_r(4.0 * scale[0], -3.0 * scale[1], 4.0 *
              scale[0], -1.0 * scale[1], 1.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], -1.0 * scale[0],
              13.0 * scale[1], 5.0 * scale[0], 16.0 * scale[1])
    Curveto_r(10.0 * scale[0], 4.0 * scale[1], 11.0 * scale[0],
              7.0 * scale[1], 1.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 7.0 * scale[1], -14.0 * scale[0],
              10.0 * scale[1], -14.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(730.0 * scale[0], 910.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0], -
              10.0 * scale[1], 11.0 * scale[0], -10.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              5.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -8.0 * scale[0],
              10.0 * scale[1], -11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              4.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(11.0 * scale[0], 730.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -135.0 * scale[1], 3.0 * scale[0], -
              180.0 * scale[1], 11.0 * scale[0], -166.0 * scale[1])
    Curveto_r(6.0 * scale[0], 11.0 * scale[1], 10.0 * scale[0],
              60.0 * scale[1], 8.0 * scale[0], 110.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 50.0 * scale[1], -2.0 * scale[0],
              115.0 * scale[1], -1.0 * scale[0], 144.0 * scale[1])
    Curveto_r(0.0 * scale[0], 29.0 * scale[1], -4.0 * scale[0],
              62.0 * scale[1], -9.0 * scale[0], 75.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 14.0 * scale[1], -9.0 * scale[0], -
              41.0 * scale[1], -9.0 * scale[0], -163.0 * scale[1])
    te.end_fill()
    Moveto(955.0 * scale[0], 860.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -11.0 *
              scale[0], -7.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -8.0 * scale[0],
              2.0 * scale[1], -4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 1.0 * scale[0], -
              22.0 * scale[1], -5.0 * scale[0], -34.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -20.0 * scale[1], -10.0 *
              scale[0], -21.0 * scale[1], 2.0 * scale[0], -11.0 * scale[1])
    Curveto_r(13.0 * scale[0], 10.0 * scale[1], 15.0 * scale[0],
              6.0 * scale[1], 16.0 * scale[0], -25.0 * scale[1])
    Curveto_r(1.0 * scale[0], -64.0 * scale[1], 15.0 * scale[0], -
              227.0 * scale[1], 20.0 * scale[0], -232.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], 3.0 * scale[0],
              68.0 * scale[1], 2.0 * scale[0], 158.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 89.0 * scale[1], -4.0 * scale[0],
              162.0 * scale[1], -5.0 * scale[0], 162.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0], -
              5.0 * scale[1], -9.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(721.0 * scale[0], 779.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-25.0 * scale[0], -22.0 * scale[1], -66.0 *
              scale[0], -54.0 * scale[1], -93.0 * scale[0], -71.0 * scale[1])
    Curveto_r(-26.0 * scale[0], -17.0 * scale[1], -48.0 *
              scale[0], -38.0 * scale[1], -48.0 * scale[0], -45.0 * scale[1])
    Curveto_r(0.0 * scale[0], -15.0 * scale[1], 14.0 *
              scale[0], -6.0 * scale[1], 47.0 * scale[0], 29.0 * scale[1])
    Curveto_r(9.0 * scale[0], 9.0 * scale[1], 20.0 * scale[0],
              15.0 * scale[1], 24.0 * scale[0], 13.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 18.0 * scale[0],
              5.0 * scale[1], 31.0 * scale[0], 18.0 * scale[1])
    Curveto_r(14.0 * scale[0], 12.0 * scale[1], 38.0 * scale[0],
              30.0 * scale[1], 54.0 * scale[0], 39.0 * scale[1])
    Curveto_r(16.0 * scale[0], 9.0 * scale[1], 30.0 * scale[0],
              26.0 * scale[1], 30.0 * scale[0], 37.0 * scale[1])
    Curveto_r(1.0 * scale[0], 12.0 * scale[1], 1.0 * scale[0],
              21.0 * scale[1], 0.0 * scale[0], 21.0 * scale[1])
    Curveto_r(0.0 * scale[0], -1.0 * scale[1], -21.0 * scale[0], -
              19.0 * scale[1], -45.0 * scale[0], -41.0 * scale[1])
    te.end_fill()
    Moveto(524.0 * scale[0], 775.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -14.0 * scale[1], -15.0 * scale[0], -
              28.0 * scale[1], -12.0 * scale[0], -30.0 * scale[1])
    Curveto_r(2.0 * scale[0], -2.0 * scale[1], 12.0 * scale[0],
              9.0 * scale[1], 22.0 * scale[0], 25.0 * scale[1])
    Curveto_r(21.0 * scale[0], 36.0 * scale[1], 13.0 * scale[0],
              40.0 * scale[1], -10.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(905.0 * scale[0], 780.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -10.0 *
              scale[0], -8.0 * scale[1], -14.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 2.0 * scale[1], -6.0 * scale[0], -
              8.0 * scale[1], -3.0 * scale[0], -23.0 * scale[1])
    Curveto_r(3.0 * scale[0], -17.0 * scale[1], 7.0 * scale[0], -
              21.0 * scale[1], 10.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], 9.0 * scale[0],
              23.0 * scale[1], 14.0 * scale[0], 33.0 * scale[1])
    Curveto_r(9.0 * scale[0], 18.0 * scale[1], 4.0 * scale[0],
              24.0 * scale[1], -7.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(473.0 * scale[0], 765.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -9.0 * scale[1], -3.0 * scale[0], -
              19.0 * scale[1], 1.0 * scale[0], -22.0 * scale[1])
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], 6.0 * scale[0],
              1.0 * scale[1], 6.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], 5.0 * scale[0],
              14.0 * scale[1], 12.0 * scale[0], 10.0 * scale[1])
    Curveto_r(7.0 * scale[0], -4.0 * scale[1], 8.0 *
              scale[0], -3.0 * scale[1], 4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 16.0 * scale[1], -15.0 * scale[0],
              15.0 * scale[1], -23.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(120.0 * scale[0], 740.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0], -
              10.0 * scale[1], 11.0 * scale[0], -10.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              5.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -8.0 * scale[0],
              10.0 * scale[1], -11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              4.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(554.0 * scale[0], 742.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -4.0 * scale[1], -14.0 * scale[0], -
              23.0 * scale[1], -15.0 * scale[0], -42.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -29.0 * scale[1], 0.0 * scale[0], -
              35.0 * scale[1], 16.0 * scale[0], -37.0 * scale[1])
    Curveto_r(11.0 * scale[0], -2.0 * scale[1], 14.0 * scale[0],
              0.0 * scale[1], 8.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 7.0 * scale[1], -17.0 * scale[0],
              38.0 * scale[1], -3.0 * scale[0], 65.0 * scale[1])
    Curveto_r(12.0 * scale[0], 21.0 * scale[1], 11.0 * scale[0],
              22.0 * scale[1], -6.0 * scale[0], 11.0 * scale[1])
    te.end_fill()
    Moveto(870.0 * scale[0], 735.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              14.0 * scale[1], -1.0 * scale[0], -18.0 * scale[1])
    Curveto_r(1.0 * scale[0], -4.0 * scale[1], -5.0 * scale[0], -
              7.0 * scale[1], -13.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 3.0 * scale[1], -17.0 * scale[0],
              0.0 * scale[1], -15.0 * scale[0], -29.0 * scale[1])
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              15.0 * scale[1], 6.0 * scale[0], -3.0 * scale[1])
    Curveto_r(4.0 * scale[0], 8.0 * scale[1], 13.0 * scale[0],
              20.0 * scale[1], 21.0 * scale[0], 26.0 * scale[1])
    Curveto_r(8.0 * scale[0], 6.0 * scale[1], 12.0 * scale[0],
              17.0 * scale[1], 9.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], -6.0 * scale[0],
              10.0 * scale[1], -7.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(426.0 * scale[0], 711.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              12.0 * scale[1], 3.0 * scale[0], -15.0 * scale[1])
    Curveto_r(5.0 * scale[0], -4.0 * scale[1], 12.0 *
              scale[0], -2.0 * scale[1], 15.0 * scale[0], 3.0 * scale[1])
    Curveto_r(4.0 * scale[0], 5.0 * scale[1], 2.0 * scale[0],
              12.0 * scale[1], -3.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 4.0 * scale[1], -12.0 * scale[0],
              2.0 * scale[1], -15.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(137.0 * scale[0], 704.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -3.0 * scale[0], -
              13.0 * scale[1], 0.0 * scale[0], -22.0 * scale[1])
    Curveto_r(4.0 * scale[0], -10.0 * scale[1], 2.0 * scale[0], -
              13.0 * scale[1], -6.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 5.0 * scale[1], -15.0 * scale[0], -
              3.0 * scale[1], -22.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -18.0 * scale[1], -16.0 * scale[0], -
              28.0 * scale[1], -22.0 * scale[0], -24.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -7.0 * scale[0],
              1.0 * scale[1], -3.0 * scale[0], -6.0 * scale[1])
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 0.0 * scale[0], -
              14.0 * scale[1], -8.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -3.0 * scale[1], -16.0 * scale[0], -
              12.0 * scale[1], -16.0 * scale[0], -20.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -6.0 * scale[0], -
              13.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 2.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -13.0 * scale[0], -12.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -4.0 * scale[0], -
              18.0 * scale[1], -9.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -4.0 * scale[1], -6.0 * scale[0], -
              13.0 * scale[1], -4.0 * scale[0], -20.0 * scale[1])
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], 16.0 * scale[0],
              6.0 * scale[1], 32.0 * scale[0], 33.0 * scale[1])
    Curveto_r(15.0 * scale[0], 26.0 * scale[1], 32.0 * scale[0],
              46.0 * scale[1], 38.0 * scale[0], 45.0 * scale[1])
    Curveto_r(6.0 * scale[0], -1.0 * scale[1], 12.0 * scale[0],
              6.0 * scale[1], 13.0 * scale[0], 17.0 * scale[1])
    Curveto_r(2.0 * scale[0], 10.0 * scale[1], 12.0 * scale[0],
              28.0 * scale[1], 23.0 * scale[0], 40.0 * scale[1])
    Curveto_r(22.0 * scale[0], 24.0 * scale[1], 35.0 * scale[0],
              56.0 * scale[1], 23.0 * scale[0], 56.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              3.0 * scale[1], -14.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(374.0 * scale[0], 696.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -9.0 * scale[1], -10.0 * scale[0], -
              14.0 * scale[1], -15.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 3.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -19.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -11.0 * scale[1], -16.0 * scale[0], -
              17.0 * scale[1], -22.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 5.0 * scale[1], -8.0 * scale[0],
              2.0 * scale[1], -3.0 * scale[0], -6.0 * scale[1])
    Curveto_r(6.0 * scale[0], -10.0 * scale[1], 12.0 *
              scale[0], -8.0 * scale[1], 25.0 * scale[0], 8.0 * scale[1])
    Curveto_r(10.0 * scale[0], 12.0 * scale[1], 20.0 * scale[0],
              19.0 * scale[1], 22.0 * scale[0], 16.0 * scale[1])
    Curveto_r(3.0 * scale[0], -2.0 * scale[1], 11.0 * scale[0],
              2.0 * scale[1], 18.0 * scale[0], 11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 9.0 * scale[1], 10.0 * scale[0],
              18.0 * scale[1], 7.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -13.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(857.0 * scale[0], 649.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -13.0 * scale[1], -6.0 * scale[0], -
              26.0 * scale[1], -6.0 * scale[0], -28.0 * scale[1])
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], -5.0 * scale[0], -
              7.0 * scale[1], -11.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -9.0 *
              scale[0], -9.0 * scale[1], 0.0 * scale[0], -15.0 * scale[1])
    Curveto_r(7.0 * scale[0], -4.0 * scale[1], 13.0 * scale[0],
              1.0 * scale[1], 17.0 * scale[0], 14.0 * scale[1])
    Curveto_r(3.0 * scale[0], 11.0 * scale[1], 9.0 * scale[0],
              18.0 * scale[1], 14.0 * scale[0], 15.0 * scale[1])
    Curveto_r(11.0 * scale[0], -6.0 * scale[1], 11.0 * scale[0],
              4.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 18.0 * scale[1], -8.0 * scale[0],
              18.0 * scale[1], -14.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(424.0 * scale[0], 636.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -14.0 * scale[1], -15.0 * scale[0], -
              28.0 * scale[1], -26.0 * scale[0], -32.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -3.0 * scale[1], -17.0 *
              scale[0], -8.0 * scale[1], -14.0 * scale[0], -11.0 * scale[1])
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], 1.0 * scale[0], -
              12.0 * scale[1], -6.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -10.0 * scale[1], -8.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], -8.0 * scale[1])
    Curveto_r(22.0 * scale[0], 9.0 * scale[1], 71.0 * scale[0],
              83.0 * scale[1], 59.0 * scale[0], 90.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -12.0 * scale[0], -
              5.0 * scale[1], -16.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(249.0 * scale[0], 608.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -18.0 * scale[1], -37.0 *
              scale[0], -32.0 * scale[1], -41.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              14.0 * scale[1], -5.0 * scale[0], -21.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 13.0 * scale[0],
              5.0 * scale[1], 24.0 * scale[0], 18.0 * scale[1])
    Curveto_r(10.0 * scale[0], 13.0 * scale[1], 25.0 * scale[0],
              24.0 * scale[1], 33.0 * scale[0], 26.0 * scale[1])
    Curveto_r(23.0 * scale[0], 5.0 * scale[1], 44.0 * scale[0],
              29.0 * scale[1], 32.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -25.0 * scale[0], -
              9.0 * scale[1], -43.0 * scale[0], -26.0 * scale[1])
    te.end_fill()
    Moveto(460.0 * scale[0], 608.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-14.0 * scale[0], -18.0 * scale[1], -25.0 *
              scale[0], -36.0 * scale[1], -26.0 * scale[0], -42.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -17.0 * scale[0], -
              29.0 * scale[1], -37.0 * scale[0], -50.0 * scale[1])
    Curveto_r(-41.0 * scale[0], -44.0 * scale[1], -41.0 *
              scale[0], -45.0 * scale[1], -26.0 * scale[0], -66.0 * scale[1])
    Curveto_r(8.0 * scale[0], -12.0 * scale[1], 9.0 *
              scale[0], -10.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 16.0 * scale[1], -4.0 * scale[0],
              21.0 * scale[1], 4.0 * scale[0], 17.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 11.0 * scale[0],
              0.0 * scale[1], 11.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], 5.0 * scale[0],
              13.0 * scale[1], 10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 10.0 *
              scale[0], -2.0 * scale[1], 10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 9.0 * scale[0],
              19.0 * scale[1], 21.0 * scale[0], 30.0 * scale[1])
    Curveto_r(13.0 * scale[0], 11.0 * scale[1], 18.0 * scale[0],
              24.0 * scale[1], 14.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 8.0 * scale[1], -4.0 * scale[0],
              10.0 * scale[1], 4.0 * scale[0], 5.0 * scale[1])
    Curveto_r(13.0 * scale[0], -8.0 * scale[1], 51.0 * scale[0],
              20.0 * scale[1], 51.0 * scale[0], 37.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -11.0 * scale[0],
              0.0 * scale[1], -25.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-31.0 * scale[0], -29.0 * scale[1], -33.0 *
              scale[0], -15.0 * scale[1], -3.0 * scale[0], 17.0 * scale[1])
    Curveto_r(12.0 * scale[0], 13.0 * scale[1], 19.0 * scale[0],
              25.0 * scale[1], 17.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 3.0 * scale[1], -16.0 * scale[0], -
              9.0 * scale[1], -29.0 * scale[0], -26.0 * scale[1])
    te.end_fill()
    Moveto(814.0 * scale[0], 571.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -5.0 * scale[1], 3.0 * scale[0], -
              11.0 * scale[1], -2.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -1.0 * scale[1], -21.0 * scale[0], -
              25.0 * scale[1], -37.0 * scale[0], -53.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -27.0 * scale[1], -33.0 *
              scale[0], -53.0 * scale[1], -39.0 * scale[0], -57.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -5.0 * scale[1], -4.0 *
              scale[0], -8.0 * scale[1], 7.0 * scale[0], -8.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0],
              7.0 * scale[1], 17.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 4.0 * scale[0],
              15.0 * scale[1], 9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              8.0 * scale[1], 15.0 * scale[0], 18.0 * scale[1])
    Curveto_r(4.0 * scale[0], 10.0 * scale[1], 16.0 * scale[0],
              29.0 * scale[1], 28.0 * scale[0], 42.0 * scale[1])
    Curveto_r(27.0 * scale[0], 29.0 * scale[1], 32.0 * scale[0],
              50.0 * scale[1], 12.0 * scale[0], 50.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -10.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(174.0 * scale[0], 552.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -7.0 * scale[1], 2.0 * scale[0], -
              13.0 * scale[1], -3.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -1.0 * scale[1], -17.0 *
              scale[0], -2.0 * scale[1], -23.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -1.0 * scale[1], -12.0 * scale[0], -
              10.0 * scale[1], -10.0 * scale[0], -20.0 * scale[1])
    Curveto_r(3.0 * scale[0], -15.0 * scale[1], -1.0 * scale[0], -
              18.0 * scale[1], -17.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 3.0 * scale[1], -19.0 * scale[0],
              1.0 * scale[1], -16.0 * scale[0], -3.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], -9.0 * scale[0], -
              20.0 * scale[1], -27.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-25.0 * scale[0], -20.0 * scale[1], -36.0 *
              scale[0], -24.0 * scale[1], -52.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 9.0 * scale[1], -20.0 * scale[0],
              9.0 * scale[1], -3.0 * scale[0], -4.0 * scale[1])
    Curveto_r(14.0 * scale[0], -12.0 * scale[1], 15.0 *
              scale[0], -16.0 * scale[1], 4.0 * scale[0], -26.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -6.0 * scale[1], -17.0 *
              scale[0], -8.0 * scale[1], -20.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 3.0 * scale[1], -6.0 * scale[0], -
              79.0 * scale[1], -6.0 * scale[0], -183.0 * scale[1])
    Curveto_r(1.0 * scale[0], -109.0 * scale[1], 5.0 * scale[0], -
              174.0 * scale[1], 9.0 * scale[0], -154.0 * scale[1])
    Curveto_r(5.0 * scale[0], 22.0 * scale[1], 8.0 * scale[0],
              27.0 * scale[1], 9.0 * scale[0], 13.0 * scale[1])
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], 6.0 * scale[0], -
              25.0 * scale[1], 13.0 * scale[0], -29.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 8.0 *
              scale[0], -3.0 * scale[1], 5.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], 3.0 * scale[0],
              16.0 * scale[1], 14.0 * scale[0], 23.0 * scale[1])
    Curveto_r(10.0 * scale[0], 8.0 * scale[1], 19.0 * scale[0],
              20.0 * scale[1], 19.0 * scale[0], 26.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], 7.0 * scale[0],
              15.0 * scale[1], 16.0 * scale[0], 18.0 * scale[1])
    Curveto_r(9.0 * scale[0], 4.0 * scale[1], 14.0 * scale[0],
              9.0 * scale[1], 11.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], 4.0 * scale[0],
              15.0 * scale[1], 16.0 * scale[0], 26.0 * scale[1])
    Curveto_r(12.0 * scale[0], 11.0 * scale[1], 16.0 * scale[0],
              17.0 * scale[1], 10.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-27.0 * scale[0], -13.0 * scale[1], 1.0 * scale[0],
              41.0 * scale[1], 40.0 * scale[0], 80.0 * scale[1])
    Curveto_r(10.0 * scale[0], 10.0 * scale[1], 16.0 * scale[0],
              24.0 * scale[1], 13.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 12.0 * scale[1], 8.0 * scale[0],
              18.0 * scale[1], 34.0 * scale[0], 16.0 * scale[1])
    Curveto_r(3.0 * scale[0], 0.0 * scale[1], 6.0 * scale[0],
              10.0 * scale[1], 6.0 * scale[0], 23.0 * scale[1])
    Curveto_r(1.0 * scale[0], 18.0 * scale[1], -2.0 * scale[0],
              22.0 * scale[1], -15.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -5.0 * scale[1], -15.0 *
              scale[0], -4.0 * scale[1], 1.0 * scale[0], 11.0 * scale[1])
    Curveto_r(16.0 * scale[0], 16.0 * scale[1], 14.0 * scale[0],
              52.0 * scale[1], -3.0 * scale[0], 63.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0],
              14.0 * scale[1], -9.0 * scale[0], 25.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -5.0 * scale[0],
              19.0 * scale[1], -17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -2.0 * scale[1], -17.0 * scale[0], -
              11.0 * scale[1], -15.0 * scale[0], -30.0 * scale[1])
    Curveto_r(2.0 * scale[0], -14.0 * scale[1], -2.0 * scale[0], -
              29.0 * scale[1], -8.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -11.0 * scale[1], -24.0 * scale[0],
              3.0 * scale[1], -10.0 * scale[0], 21.0 * scale[1])
    Curveto_r(17.0 * scale[0], 19.0 * scale[1], -1.0 * scale[0],
              34.0 * scale[1], -32.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-35.0 * scale[0], -9.0 * scale[1], 0.0 * scale[0],
              33.0 * scale[1], 39.0 * scale[0], 47.0 * scale[1])
    Curveto_r(19.0 * scale[0], 7.0 * scale[1], 32.0 * scale[0],
              15.0 * scale[1], 29.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -1.0 * scale[0],
              12.0 * scale[1], 5.0 * scale[0], 19.0 * scale[1])
    Curveto_r(7.0 * scale[0], 8.0 * scale[1], 6.0 * scale[0],
              14.0 * scale[1], -2.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 4.0 * scale[1], -9.0 * scale[0],
              3.0 * scale[1], -5.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto_r(-64.0 * scale[0], -126.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -7.0 * scale[0], -
              19.0 * scale[1], -15.0 * scale[0], -26.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -8.0 * scale[1], -15.0 *
              scale[0], -9.0 * scale[1], -15.0 * scale[0], -2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 5.0 * scale[0],
              14.0 * scale[1], 11.0 * scale[0], 18.0 * scale[1])
    Curveto_r(8.0 * scale[0], 4.0 * scale[1], 7.0 * scale[0],
              9.0 * scale[1], -2.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 7.0 * scale[1], -10.0 *
              scale[0], 9.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0], -
              6.0 * scale[1], 17.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto_r(87.0 * scale[0], -22.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -5.0 * scale[1], -3.0 * scale[0], -
              18.0 * scale[1], -10.0 * scale[0], -28.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -17.0 * scale[1], -14.0 *
              scale[0], -16.0 * scale[1], -14.0 * scale[0], 13.0 * scale[1])
    Curveto_r(0.0 * scale[0], 29.0 * scale[1], 16.0 * scale[0],
              39.0 * scale[1], 24.0 * scale[0], 15.0 * scale[1])
    te.end_fill()
    Moveto_r(-147.0 * scale[0], -85.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 5.0 * scale[0], -
              29.0 * scale[1], 10.0 * scale[0], -29.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              8.0 * scale[1], 10.0 * scale[0], -18.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0], -
              28.0 * scale[1], 20.0 * scale[0], -40.0 * scale[1])
    Curveto_r(12.0 * scale[0], -12.0 * scale[1], 16.0 * scale[0], -
              22.0 * scale[1], 10.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0], -
              26.0 * scale[1], -2.0 * scale[0], -33.0 * scale[1])
    Curveto_r(4.0 * scale[0], -2.0 * scale[1], 2.0 * scale[0], -
              3.0 * scale[1], -4.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 1.0 * scale[1], -21.0 * scale[0], -
              19.0 * scale[1], -35.0 * scale[0], -44.0 * scale[1])
    Lineto_r(-24.0 * scale[0], -47.0 * scale[1])
    Lineto_r(-5.0 * scale[0], 50.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 75.0 * scale[1], 0.0 * scale[0],
              226.0 * scale[1], 11.0 * scale[0], 220.0 * scale[1])
    Curveto_r(5.0 * scale[0], -4.0 * scale[1], 9.0 * scale[0], -
              19.0 * scale[1], 9.0 * scale[0], -36.0 * scale[1])
    te.end_fill()
    Moveto(344.0 * scale[0], 532.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -9.0 * scale[1], -27.0 * scale[0], -
              27.0 * scale[1], -33.0 * scale[0], -39.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -18.0 * scale[1], -8.0 *
              scale[0], -20.0 * scale[1], 9.0 * scale[0], -16.0 * scale[1])
    Curveto_r(11.0 * scale[0], 3.0 * scale[1], 19.0 * scale[0],
              8.0 * scale[1], 18.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 20.0 * scale[1], 3.0 * scale[0],
              31.0 * scale[1], 14.0 * scale[0], 25.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 8.0 *
              scale[0], -3.0 * scale[1], 4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              15.0 * scale[1], 11.0 * scale[0], 21.0 * scale[1])
    Curveto_r(10.0 * scale[0], 6.0 * scale[1], 14.0 * scale[0],
              10.0 * scale[1], 8.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 1.0 * scale[1], -20.0 * scale[0], -
              7.0 * scale[1], -31.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(964.0 * scale[0], 314.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -143.0 * scale[1], -5.0 * scale[0], -
              198.0 * scale[1], -14.0 * scale[0], -209.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -13.0 * scale[1], -11.0 *
              scale[0], -19.0 * scale[1], 3.0 * scale[0], -32.0 * scale[1])
    Curveto_r(15.0 * scale[0], -15.0 * scale[1], 16.0 *
              scale[0], -15.0 * scale[1], 16.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], 3.0 * scale[0],
              109.0 * scale[1], 7.0 * scale[0], 220.0 * scale[1])
    Curveto_r(4.0 * scale[0], 117.0 * scale[1], 3.0 * scale[0],
              203.0 * scale[1], -2.0 * scale[0], 206.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 4.0 * scale[1], -9.0 * scale[0], -
              76.0 * scale[1], -10.0 * scale[0], -188.0 * scale[1])
    te.end_fill()
    Moveto(272.0 * scale[0], 439.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -9.0 * scale[1], -22.0 * scale[0], -
              22.0 * scale[1], -22.0 * scale[0], -29.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -4.0 * scale[0], -
              9.0 * scale[1], -9.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -11.0 * scale[0], -
              6.0 * scale[1], -14.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -24.0 * scale[1], -3.0 * scale[0], -
              24.0 * scale[1], 13.0 * scale[0], -10.0 * scale[1])
    Curveto_r(9.0 * scale[0], 8.0 * scale[1], 20.0 * scale[0],
              12.0 * scale[1], 25.0 * scale[0], 8.0 * scale[1])
    Curveto_r(4.0 * scale[0], -5.0 * scale[1], 5.0 *
              scale[0], -2.0 * scale[1], 1.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 7.0 * scale[1], -2.0 * scale[0],
              12.0 * scale[1], 6.0 * scale[0], 12.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              3.0 * scale[1], -2.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 8.0 * scale[1], -13.0 * scale[0],
              10.0 * scale[1], 1.0 * scale[0], 10.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 23.0 * scale[0],
              8.0 * scale[1], 32.0 * scale[0], 18.0 * scale[1])
    Curveto_r(23.0 * scale[0], 25.0 * scale[1], -1.0 * scale[0],
              26.0 * scale[1], -31.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(317.0 * scale[0], 414.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -13.0 * scale[1], -14.0 *
              scale[0], -24.0 * scale[1], -9.0 * scale[0], -24.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 35.0 * scale[0],
              27.0 * scale[1], 30.0 * scale[0], 39.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 5.0 * scale[1], -11.0 * scale[0], -
              2.0 * scale[1], -21.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(350.0 * scale[0], 421.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 5.0 * scale[0], -
              13.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 10.0 * scale[0],
              1.0 * scale[1], 10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], -4.0 * scale[0],
              16.0 * scale[1], -10.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              4.0 * scale[1], -10.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(711.0 * scale[0], 408.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-14.0 * scale[0], -23.0 * scale[1], -14.0 *
              scale[0], -23.0 * scale[1], 8.0 * scale[0], -4.0 * scale[1])
    Curveto_r(22.0 * scale[0], 20.0 * scale[1], 25.0 * scale[0],
              26.0 * scale[1], 13.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              10.0 * scale[1], -21.0 * scale[0], -22.0 * scale[1])
    te.end_fill()
    Moveto(274.0 * scale[0], 348.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -18.0 * scale[1], -23.0 * scale[0], -
              37.0 * scale[1], -31.0 * scale[0], -41.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -5.0 * scale[1], -11.0 * scale[0], -
              12.0 * scale[1], -8.0 * scale[0], -18.0 * scale[1])
    Curveto_r(4.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              9.0 * scale[1], -5.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              7.0 * scale[1], 5.0 * scale[0], -16.0 * scale[1])
    Curveto_r(9.0 * scale[0], -9.0 * scale[1], 14.0 * scale[0], -
              22.0 * scale[1], 12.0 * scale[0], -29.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], -1.0 * scale[0], -
              18.0 * scale[1], 5.0 * scale[0], -26.0 * scale[1])
    Curveto_r(8.0 * scale[0], -11.0 * scale[1], 9.0 *
              scale[0], -10.0 * scale[1], 4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 11.0 * scale[1], 0.0 * scale[0],
              17.0 * scale[1], 9.0 * scale[0], 17.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -6.0 * scale[0],
              10.0 * scale[1], -14.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0],
              11.0 * scale[1], -13.0 * scale[0], 26.0 * scale[1])
    Curveto_r(0.0 * scale[0], 23.0 * scale[1], 2.0 * scale[0],
              25.0 * scale[1], 26.0 * scale[0], 18.0 * scale[1])
    Curveto_r(14.0 * scale[0], -4.0 * scale[1], 35.0 *
              scale[0], -6.0 * scale[1], 46.0 * scale[0], -6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 27.0 * scale[0], -
              6.0 * scale[1], 37.0 * scale[0], -15.0 * scale[1])
    Curveto_r(11.0 * scale[0], -10.0 * scale[1], 18.0 *
              scale[0], -12.0 * scale[1], 18.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], -8.0 * scale[0],
              15.0 * scale[1], -78.0 * scale[0], 42.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 6.0 * scale[1], -30.0 * scale[0],
              15.0 * scale[1], -25.0 * scale[0], 18.0 * scale[1])
    Curveto_r(15.0 * scale[0], 11.0 * scale[1], 33.0 * scale[0],
              51.0 * scale[1], 23.0 * scale[0], 51.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0], -
              15.0 * scale[1], -26.0 * scale[0], -32.0 * scale[1])
    te.end_fill()
    Moveto(676.0 * scale[0], 364.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-23.0 * scale[0], -23.0 * scale[1], -20.0 *
              scale[0], -30.0 * scale[1], 4.0 * scale[0], -9.0 * scale[1])
    Curveto_r(11.0 * scale[0], 10.0 * scale[1], 20.0 * scale[0],
              20.0 * scale[1], 20.0 * scale[0], 22.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -9.0 * scale[0],
              2.0 * scale[1], -24.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(351.0 * scale[0], 348.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -16.0 * scale[1], 4.0 * scale[0], -
              28.0 * scale[1], 10.0 * scale[0], -28.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0], -
              5.0 * scale[1], 3.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], -3.0 *
              scale[0], -8.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 9.0 * scale[0],
              13.0 * scale[1], 3.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              24.0 * scale[1], -14.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -6.0 * scale[0],
              3.0 * scale[1], -6.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(623.0 * scale[0], 306.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -12.0 * scale[1], -23.0 *
              scale[0], -28.0 * scale[1], -23.0 * scale[0], -35.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], 12.0 * scale[0],
              2.0 * scale[1], 26.0 * scale[0], 19.0 * scale[1])
    Curveto_r(31.0 * scale[0], 36.0 * scale[1], 29.0 * scale[0],
              47.0 * scale[1], -3.0 * scale[0], 16.0 * scale[1])
    te.end_fill()
    Moveto(291.0 * scale[0], 221.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -6.0 * scale[1], -9.0 *
              scale[0], -10.0 * scale[1], 3.0 * scale[0], -14.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 21.0 * scale[0], 3.0 * scale[1])
    Curveto_r(8.0 * scale[0], 13.0 * scale[1], -9.0 * scale[0],
              20.0 * scale[1], -24.0 * scale[0], 11.0 * scale[1])
    te.end_fill()
    Moveto(580.0 * scale[0], 200.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 2.0 * scale[0], -
              20.0 * scale[1], 4.0 * scale[0], -20.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 6.0 * scale[0],
              9.0 * scale[1], 9.0 * scale[0], 20.0 * scale[1])
    Curveto_r(3.0 * scale[0], 11.0 * scale[1], 1.0 * scale[0],
              20.0 * scale[1], -4.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              9.0 * scale[1], -9.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(201.0 * scale[0], 194.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(922.0 * scale[0], 125.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(387.0 * scale[0], 96.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -15.0 * scale[1], 10.0 * scale[0], -
              23.0 * scale[1], 18.0 * scale[0], -20.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 23.0 * scale[0],
              1.0 * scale[1], 34.0 * scale[0], -6.0 * scale[1])
    Curveto_r(24.0 * scale[0], -12.0 * scale[1], 27.0 *
              scale[0], -5.0 * scale[1], 7.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 8.0 * scale[1], -16.0 * scale[0],
              11.0 * scale[1], -20.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], -6.0 * scale[0],
              0.0 * scale[1], -6.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -3.0 * scale[0],
              10.0 * scale[1], -7.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], -12.0 *
              scale[0], -2.0 * scale[1], -18.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 8.0 * scale[1], -11.0 * scale[0],
              4.0 * scale[1], -8.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(516.0 * scale[0], 91.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-17.0 * scale[0], -11.0 * scale[1], -34.0 *
              scale[0], -17.0 * scale[1], -39.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -4.0 * scale[0], -
              4.0 * scale[1], 2.0 * scale[0], -14.0 * scale[1])
    Curveto_r(6.0 * scale[0], -11.0 * scale[1], 7.0 * scale[0], -
              24.0 * scale[1], 3.0 * scale[0], -28.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -5.0 * scale[1], -1.0 *
              scale[0], -5.0 * scale[1], 6.0 * scale[0], -1.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 12.0 * scale[0],
              13.0 * scale[1], 12.0 * scale[0], 21.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], 9.0 * scale[0],
              16.0 * scale[1], 19.0 * scale[0], 20.0 * scale[1])
    Curveto_r(21.0 * scale[0], 6.0 * scale[1], 49.0 * scale[0],
              35.0 * scale[1], 35.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -22.0 * scale[0], -
              9.0 * scale[1], -38.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(330.0 * scale[0], 50.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0], -
              10.0 * scale[1], 10.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              5.0 * scale[1], 10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -4.0 * scale[0],
              10.0 * scale[1], -10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              4.0 * scale[1], -10.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(972.0 * scale[0], 20.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(31.0 * scale[0], 17.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -10.0 * scale[1], -7.0 *
              scale[0], -14.0 * scale[1], 2.0 * scale[0], -14.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0],
              6.0 * scale[1], 14.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -1.0 * scale[0],
              13.0 * scale[1], -2.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              6.0 * scale[1], -14.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(540.0 * scale[0], 15.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -13.0 * scale[1], -9.0 *
              scale[0], -15.0 * scale[1], 9.0 * scale[0], -15.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 21.0 * scale[0],
              4.0 * scale[1], 21.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 18.0 * scale[1], -18.0 * scale[0],
              21.0 * scale[1], -30.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(105.0 * scale[0], 10.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              10.0 * scale[1], 9.0 * scale[0], -10.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0],
              5.0 * scale[1], 16.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -4.0 * scale[0],
              10.0 * scale[1], -9.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(468.0 * scale[0], 3.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#6c9fd8')
    te.end_fill()
    Moveto(370.0 * scale[0], 1382.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(19.0 * scale[0], -6.0 * scale[1], 28.0 * scale[0], -
              18.0 * scale[1], 36.0 * scale[0], -52.0 * scale[1])
    Curveto_r(6.0 * scale[0], -28.0 * scale[1], 16.0 * scale[0], -
              44.0 * scale[1], 27.0 * scale[0], -46.0 * scale[1])
    Curveto_r(9.0 * scale[0], -1.0 * scale[1], 17.0 * scale[0],
              1.0 * scale[1], 17.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], 8.0 * scale[0],
              7.0 * scale[1], 18.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], -1.0 * scale[1], 17.0 * scale[0],
              6.0 * scale[1], 17.0 * scale[0], 21.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              25.0 * scale[1], 8.0 * scale[0], 29.0 * scale[1])
    Curveto_r(4.0 * scale[0], 4.0 * scale[1], 7.0 * scale[0], -
              6.0 * scale[1], 7.0 * scale[0], -23.0 * scale[1])
    Curveto_r(0.0 * scale[0], -17.0 * scale[1], 8.0 * scale[0], -
              37.0 * scale[1], 18.0 * scale[0], -44.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 4.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 15.0 * scale[1], -10.0 * scale[0],
              16.0 * scale[1], 15.0 * scale[0], 13.0 * scale[1])
    Curveto_r(15.0 * scale[0], -2.0 * scale[1], 28.0 *
              scale[0], -4.0 * scale[1], 28.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], -1.0 * scale[1], 10.0 * scale[0], -
              3.0 * scale[1], 23.0 * scale[0], -4.0 * scale[1])
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 22.0 * scale[0],
              1.0 * scale[1], 22.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], 15.0 * scale[0],
              11.0 * scale[1], 33.0 * scale[0], 14.0 * scale[1])
    Lineto_r(32.0 * scale[0], 7.0 * scale[1])
    Lineto_r(-39.0 * scale[0], 32.0 * scale[1])
    Lineto_r(-40.0 * scale[0], 32.0 * scale[1])
    Lineto_r(35.0 * scale[0], 6.0 * scale[1])
    Lineto_r(34.0 * scale[0], 6.0 * scale[1])
    Lineto_r(-38.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-33.0 * scale[0], 1.0 * scale[1], -38.0 * scale[0], -
              1.0 * scale[1], -32.0 * scale[0], -18.0 * scale[1])
    Curveto_r(5.0 * scale[0], -17.0 * scale[1], 2.0 * scale[0], -
              18.0 * scale[1], -31.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 5.0 * scale[1], -43.0 * scale[0],
              6.0 * scale[1], -51.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -3.0 * scale[1], -19.0 * scale[0],
              0.0 * scale[1], -24.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 11.0 * scale[1], -9.0 * scale[0],
              11.0 * scale[1], -9.0 * scale[0], -3.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], -5.0 * scale[0], -
              18.0 * scale[1], -11.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0],
              7.0 * scale[1], -5.0 * scale[0], 16.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], 2.0 * scale[0],
              13.0 * scale[1], -3.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -12.0 * scale[0], -
              22.0 * scale[1], -15.0 * scale[0], -41.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -44.0 * scale[1], -24.0 *
              scale[0], -46.0 * scale[1], -19.0 * scale[0], -2.0 * scale[1])
    Curveto_r(2.0 * scale[0], 17.0 * scale[1], 0.0 * scale[0],
              26.0 * scale[1], -3.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -10.0 * scale[1], -10.0 *
              scale[0], -7.0 * scale[1], -18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 13.0 * scale[1], -22.0 * scale[0],
              24.0 * scale[1], -36.0 * scale[0], 25.0 * scale[1])
    Lineto_r(-25.0 * scale[0], 2.0 * scale[1])
    Lineto_r(25.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto_r(255.0 * scale[0], -52.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 11.0 * scale[0], -
              8.0 * scale[1], 16.0 * scale[0], -5.0 * scale[1])
    Curveto_r(5.0 * scale[0], 4.0 * scale[1], 9.0 * scale[0],
              1.0 * scale[1], 9.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], -15.0 * scale[1], -42.0 *
              scale[0], -8.0 * scale[1], -48.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 14.0 * scale[1], 14.0 * scale[0],
              16.0 * scale[1], 23.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(678.0 * scale[0], 1383.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(753.0 * scale[0], 1383.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(15.0 * scale[0], -2.0 * scale[1], 39.0 *
              scale[0], -2.0 * scale[1], 55.0 * scale[0], 0.0 * scale[1])
    Curveto_r(15.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              4.0 * scale[1], -28.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 0.0 * scale[1], -43.0 *
              scale[0], -2.0 * scale[1], -27.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(32.0 * scale[0], 1370.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-27.0 * scale[0], -11.0 * scale[1], -28.0 *
              scale[0], -25.0 * scale[1], -2.0 * scale[0], -73.0 * scale[1])
    Curveto_r(15.0 * scale[0], -28.0 * scale[1], 17.0 *
              scale[0], -39.0 * scale[1], 8.0 * scale[0], -42.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -8.0 * scale[1], -27.0 * scale[0], -
              219.0 * scale[1], -14.0 * scale[0], -460.0 * scale[1])
    Curveto_r(3.0 * scale[0], -60.0 * scale[1], 8.0 * scale[0], -
              115.0 * scale[1], 10.0 * scale[0], -122.0 * scale[1])
    Curveto_r(3.0 * scale[0], -7.0 * scale[1], 1.0 * scale[0], -
              36.0 * scale[1], -4.0 * scale[0], -65.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -33.0 * scale[1], -5.0 *
              scale[0], -57.0 * scale[1], 1.0 * scale[0], -63.0 * scale[1])
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 8.0 *
              scale[0], -3.0 * scale[1], 3.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 14.0 * scale[1], -4.0 * scale[0],
              17.0 * scale[1], 5.0 * scale[0], 12.0 * scale[1])
    Curveto_r(8.0 * scale[0], -5.0 * scale[1], 14.0 * scale[0], -
              1.0 * scale[1], 18.0 * scale[0], 12.0 * scale[1])
    Curveto_r(3.0 * scale[0], 11.0 * scale[1], 11.0 * scale[0],
              23.0 * scale[1], 19.0 * scale[0], 26.0 * scale[1])
    Curveto_r(20.0 * scale[0], 8.0 * scale[1], 57.0 * scale[0],
              93.0 * scale[1], 51.0 * scale[0], 117.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 22.0 * scale[1], 22.0 * scale[0],
              99.0 * scale[1], 35.0 * scale[0], 99.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0],
              6.0 * scale[1], 8.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], 6.0 * scale[0],
              19.0 * scale[1], 14.0 * scale[0], 26.0 * scale[1])
    Curveto_r(8.0 * scale[0], 6.0 * scale[1], 12.0 * scale[0],
              19.0 * scale[1], 9.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 10.0 * scale[1], -2.0 * scale[0],
              14.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 18.0 * scale[0],
              5.0 * scale[1], 27.0 * scale[0], 18.0 * scale[1])
    Curveto_r(10.0 * scale[0], 14.0 * scale[1], 22.0 * scale[0],
              23.0 * scale[1], 28.0 * scale[0], 19.0 * scale[1])
    Curveto_r(7.0 * scale[0], -5.0 * scale[1], 8.0 *
              scale[0], -3.0 * scale[1], 4.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 9.0 * scale[1], -12.0 * scale[0],
              9.0 * scale[1], -25.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -9.0 * scale[1], -23.0 * scale[0], -
              16.0 * scale[1], -29.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              6.0 * scale[1], -14.0 * scale[0], -12.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -2.0 * scale[0], -
              17.0 * scale[1], -3.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -5.0 * scale[1], -4.0 * scale[0], -
              14.0 * scale[1], -5.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -5.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 14.0 * scale[1], -4.0 * scale[0],
              27.0 * scale[1], -1.0 * scale[0], 30.0 * scale[1])
    Curveto_r(12.0 * scale[0], 9.0 * scale[1], 20.0 * scale[0],
              69.0 * scale[1], 10.0 * scale[0], 75.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0],
              0.0 * scale[1], -10.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -7.0 * scale[1], -8.0 * scale[0],
              0.0 * scale[1], -16.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 15.0 * scale[1], -14.0 * scale[0],
              39.0 * scale[1], -11.0 * scale[0], 52.0 * scale[1])
    Curveto_r(2.0 * scale[0], 13.0 * scale[1], 1.0 * scale[0],
              24.0 * scale[1], -4.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              19.0 * scale[1], -11.0 * scale[0], -42.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -23.0 * scale[1], -8.0 * scale[0], -
              43.0 * scale[1], -15.0 * scale[0], -45.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -3.0 * scale[1], -10.0 * scale[0],
              9.0 * scale[1], -7.0 * scale[0], 42.0 * scale[1])
    Curveto_r(4.0 * scale[0], 41.0 * scale[1], 2.0 * scale[0],
              46.0 * scale[1], -14.0 * scale[0], 41.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -5.0 * scale[1], -17.0 *
              scale[0], -1.0 * scale[1], -14.0 * scale[0], 31.0 * scale[1])
    Curveto_r(3.0 * scale[0], 20.0 * scale[1], 10.0 * scale[0],
              43.0 * scale[1], 17.0 * scale[0], 50.0 * scale[1])
    Curveto_r(21.0 * scale[0], 21.0 * scale[1], -14.0 * scale[0],
              129.0 * scale[1], -48.0 * scale[0], 150.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 11.0 * scale[1], -27.0 * scale[0],
              37.0 * scale[1], -18.0 * scale[0], 51.0 * scale[1])
    Curveto_r(5.0 * scale[0], 8.0 * scale[1], 60.0 * scale[0],
              14.0 * scale[1], 157.0 * scale[0], 18.0 * scale[1])
    Curveto_r(82.0 * scale[0], 3.0 * scale[1], 151.0 * scale[0],
              8.0 * scale[1], 153.0 * scale[0], 10.0 * scale[1])
    Curveto_r(9.0 * scale[0], 8.0 * scale[1], -285.0 * scale[0],
              2.0 * scale[1], -307.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto_r(129.0 * scale[0], -453.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -6.0 * scale[1], -11.0 * scale[0], -
              26.0 * scale[1], -11.0 * scale[0], -44.0 * scale[1])
    Curveto_r(0.0 * scale[0], -18.0 * scale[1], -4.0 * scale[0], -
              33.0 * scale[1], -9.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 0.0 * scale[1], -21.0 * scale[0],
              29.0 * scale[1], -11.0 * scale[0], 55.0 * scale[1])
    Curveto_r(12.0 * scale[0], 32.0 * scale[1], 34.0 * scale[0],
              56.0 * scale[1], 39.0 * scale[0], 43.0 * scale[1])
    Curveto_r(2.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              15.0 * scale[1], -8.0 * scale[0], -21.0 * scale[1])
    te.end_fill()
    Moveto(841.0 * scale[0], 1370.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -31.0 * scale[1], 13.0 * scale[0], -
              39.0 * scale[1], 38.0 * scale[0], -19.0 * scale[1])
    Curveto_r(13.0 * scale[0], 10.0 * scale[1], 18.0 * scale[0],
              19.0 * scale[1], 13.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0], -
              4.0 * scale[1], -17.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -15.0 * scale[1], -23.0 *
              scale[0], -12.0 * scale[1], -28.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 12.0 * scale[1], -5.0 * scale[0],
              13.0 * scale[1], -6.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(919.0 * scale[0], 1361.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -8.0 * scale[1], 12.0 * scale[0], -
              12.0 * scale[1], -2.0 * scale[0], -26.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -9.0 * scale[1], -17.0 * scale[0], -
              22.0 * scale[1], -17.0 * scale[0], -28.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -9.0 * scale[0], -
              18.0 * scale[1], -20.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -7.0 * scale[1], -18.0 * scale[0], -
              17.0 * scale[1], -15.0 * scale[0], -22.0 * scale[1])
    Curveto_r(3.0 * scale[0], -6.0 * scale[1], -1.0 * scale[0], -
              10.0 * scale[1], -9.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0], -
              7.0 * scale[1], -17.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -8.0 * scale[1], -3.0 * scale[0], -
              19.0 * scale[1], -4.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -5.0 * scale[1], -3.0 * scale[0], -
              13.0 * scale[1], -4.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -5.0 * scale[1], -6.0 *
              scale[0], -1.0 * scale[1], -12.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 12.0 * scale[1], -10.0 * scale[0],
              12.0 * scale[1], -5.0 * scale[0], -3.0 * scale[1])
    Curveto_r(4.0 * scale[0], -12.0 * scale[1], 2.0 * scale[0], -
              17.0 * scale[1], -6.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 2.0 * scale[1], -12.0 * scale[0],
              12.0 * scale[1], -12.0 * scale[0], 21.0 * scale[1])
    Curveto_r(1.0 * scale[0], 9.0 * scale[1], -2.0 * scale[0],
              16.0 * scale[1], -7.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              4.0 * scale[1], -9.0 * scale[0], -9.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -3.0 * scale[0], -
              16.0 * scale[1], -6.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -11.0 * scale[1], -1.0 * scale[0], -
              16.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0], -
              4.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -6.0 * scale[0], -
              10.0 * scale[1], -14.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0], -
              12.0 * scale[1], -19.0 * scale[0], -26.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -28.0 * scale[1], -5.0 *
              scale[0], -28.0 * scale[1], 43.0 * scale[0], 34.0 * scale[1])
    Curveto_r(58.0 * scale[0], 76.0 * scale[1], 130.0 * scale[0],
              186.0 * scale[1], 130.0 * scale[0], 199.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -8.0 * scale[0],
              13.0 * scale[1], -17.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 0.0 * scale[1], -15.0 *
              scale[0], -2.0 * scale[1], -4.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(415.0 * scale[0], 1259.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0], -
              12.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 17.0 * scale[1], 1.0 * scale[0],
              20.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(595.0 * scale[0], 1260.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 11.0 * scale[0], -10.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 4.0 * scale[0],
              5.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              10.0 * scale[1], -11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              4.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(922.0 * scale[0], 1242.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-36.0 * scale[0], -49.0 * scale[1], -44.0 * scale[0], -
              82.0 * scale[1], -29.0 * scale[0], -106.0 * scale[1])
    Curveto_r(7.0 * scale[0], -11.0 * scale[1], 21.0 * scale[0], -
              42.0 * scale[1], 31.0 * scale[0], -68.0 * scale[1])
    Curveto_r(10.0 * scale[0], -26.0 * scale[1], 21.0 * scale[0], -
              50.0 * scale[1], 25.0 * scale[0], -53.0 * scale[1])
    Curveto_r(10.0 * scale[0], -6.0 * scale[1], 11.0 * scale[0],
              228.0 * scale[1], 1.0 * scale[0], 244.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 9.0 * scale[1], -13.0 * scale[0],
              4.0 * scale[1], -28.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(718.0 * scale[0], 1234.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -8.0 * scale[1], -28.0 * scale[0], -
              17.0 * scale[1], -28.0 * scale[0], -19.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 72.0 * scale[0],
              24.0 * scale[1], 79.0 * scale[0], 31.0 * scale[1])
    Curveto_r(11.0 * scale[0], 10.0 * scale[1], -27.0 * scale[0],
              2.0 * scale[1], -51.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(385.0 * scale[0], 1175.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -14.0 * scale[1], -7.0 * scale[0], -
              36.0 * scale[1], -10.0 * scale[0], -49.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -23.0 * scale[1], -109.0 * scale[0], -
              148.0 * scale[1], -117.0 * scale[0], -140.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 2.0 * scale[1], -5.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -9.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 6.0 * scale[0], -
              14.0 * scale[1], 13.0 * scale[0], -14.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              3.0 * scale[1], 12.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 19.0 * scale[1], 3.0 * scale[0],
              31.0 * scale[1], 11.0 * scale[0], 27.0 * scale[1])
    Curveto_r(9.0 * scale[0], -6.0 * scale[1], 58.0 * scale[0],
              41.0 * scale[1], 54.0 * scale[0], 52.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 4.0 * scale[1], 3.0 * scale[0],
              7.0 * scale[1], 10.0 * scale[0], 7.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              8.0 * scale[1], 9.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 9.0 * scale[1], 5.0 * scale[0],
              22.0 * scale[1], 13.0 * scale[0], 29.0 * scale[1])
    Curveto_r(8.0 * scale[0], 7.0 * scale[1], 15.0 * scale[0],
              27.0 * scale[1], 15.0 * scale[0], 45.0 * scale[1])
    Curveto_r(0.0 * scale[0], 19.0 * scale[1], 5.0 * scale[0],
              35.0 * scale[1], 12.0 * scale[0], 37.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 9.0 * scale[0],
              6.0 * scale[1], 0.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -13.0 * scale[0], -
              2.0 * scale[1], -17.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto_r(-55.0 * scale[0], -138.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], -10.0 * scale[0], -
              12.0 * scale[1], -22.0 * scale[0], -23.0 * scale[1])
    Lineto_r(-23.0 * scale[0], -19.0 * scale[1])
    Lineto_r(19.0 * scale[0], 23.0 * scale[1])
    Curveto_r(18.0 * scale[0], 21.0 * scale[1], 26.0 * scale[0],
              27.0 * scale[1], 26.0 * scale[0], 19.0 * scale[1])
    te.end_fill()
    Moveto(694.0 * scale[0], 1180.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -16.0 * scale[1], 9.0 * scale[0], -
              24.0 * scale[1], 20.0 * scale[0], -23.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0], -
              4.0 * scale[1], 13.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 * scale[0], -
              20.0 * scale[1], 9.0 * scale[0], -31.0 * scale[1])
    Curveto_r(12.0 * scale[0], -17.0 * scale[1], 14.0 *
              scale[0], -17.0 * scale[1], 14.0 * scale[0], -2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], -5.0 * scale[0],
              17.0 * scale[1], -11.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0],
              4.0 * scale[1], -5.0 * scale[0], 9.0 * scale[1])
    Curveto_r(9.0 * scale[0], 14.0 * scale[1], -4.0 * scale[0],
              41.0 * scale[1], -19.0 * scale[0], 41.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0],
              6.0 * scale[1], -19.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 6.0 * scale[1], -3.0 * scale[0],
              1.0 * scale[1], -2.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(97.0 * scale[0], 1104.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -8.0 * scale[1], 1.0 * scale[0], -
              24.0 * scale[1], 14.0 * scale[0], -24.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              7.0 * scale[1], 9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 15.0 * scale[1], -12.0 * scale[0],
              20.0 * scale[1], -23.0 * scale[0], 9.0 * scale[1])
    te.end_fill()
    Moveto(619.0 * scale[0], 1071.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -9.0 * scale[1], 11.0 * scale[0], -
              37.0 * scale[1], 14.0 * scale[0], -64.0 * scale[1])
    Curveto_r(5.0 * scale[0], -40.0 * scale[1], 1.0 * scale[0], -
              56.0 * scale[1], -26.0 * scale[0], -108.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -35.0 * scale[1], -36.0 *
              scale[0], -58.0 * scale[1], -44.0 * scale[0], -55.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 3.0 * scale[1], -15.0 * scale[0],
              0.0 * scale[1], -19.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], -3.0 *
              scale[0], -8.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(7.0 * scale[0], 4.0 * scale[1], 12.0 * scale[0],
              2.0 * scale[1], 12.0 * scale[0], -3.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -4.0 * scale[0], -
              12.0 * scale[1], -10.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -1.0 * scale[1], -16.0 *
              scale[0], -2.0 * scale[1], -22.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              8.0 * scale[1], -13.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -8.0 * scale[1], -7.0 * scale[0], -
              14.0 * scale[1], -15.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 3.0 * scale[1], -11.0 * scale[0],
              0.0 * scale[1], -1.0 * scale[0], -11.0 * scale[1])
    Curveto_r(9.0 * scale[0], -12.0 * scale[1], 9.0 * scale[0], -
              16.0 * scale[1], -1.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -3.0 * scale[1], -3.0 *
              scale[0], -4.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(17.0 * scale[0], 1.0 * scale[1], 19.0 * scale[0],
              4.0 * scale[1], 11.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 12.0 * scale[1], 0.0 * scale[0],
              18.0 * scale[1], 25.0 * scale[0], 14.0 * scale[1])
    Curveto_r(5.0 * scale[0], -1.0 * scale[1], 6.0 * scale[0],
              3.0 * scale[1], 2.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], -1.0 * scale[0],
              10.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 28.0 * scale[0],
              26.0 * scale[1], 48.0 * scale[0], 58.0 * scale[1])
    Curveto_r(21.0 * scale[0], 31.0 * scale[1], 41.0 * scale[0],
              59.0 * scale[1], 46.0 * scale[0], 60.0 * scale[1])
    Curveto_r(4.0 * scale[0], 2.0 * scale[1], 4.0 * scale[0],
              8.0 * scale[1], 1.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], 0.0 * scale[0],
              16.0 * scale[1], 6.0 * scale[0], 24.0 * scale[1])
    Curveto_r(6.0 * scale[0], 8.0 * scale[1], 9.0 * scale[0],
              19.0 * scale[1], 5.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], -1.0 * scale[0],
              9.0 * scale[1], 6.0 * scale[0], 8.0 * scale[1])
    Curveto_r(7.0 * scale[0], -2.0 * scale[1], 13.0 * scale[0],
              5.0 * scale[1], 14.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], 11.0 * scale[0],
              27.0 * scale[1], 25.0 * scale[0], 37.0 * scale[1])
    Curveto_r(23.0 * scale[0], 18.0 * scale[1], 23.0 * scale[0],
              20.0 * scale[1], 5.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 1.0 * scale[1], -37.0 * scale[0],
              7.0 * scale[1], -57.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-34.0 * scale[0], 12.0 * scale[1], -36.0 * scale[0],
              12.0 * scale[1], -29.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto_r(41.0 * scale[0], -51.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -11.0 * scale[1], -13.0 * scale[0], -
              20.0 * scale[1], -16.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], 0.0 * scale[0],
              9.0 * scale[1], 6.0 * scale[0], 20.0 * scale[1])
    Curveto_r(6.0 * scale[0], 11.0 * scale[1], 13.0 * scale[0],
              20.0 * scale[1], 16.0 * scale[0], 20.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 0.0 * scale[0], -
              9.0 * scale[1], -6.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(784.0 * scale[0], 1015.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], 1.0 * scale[0], -
              15.0 * scale[1], -5.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              4.0 * scale[1], -5.0 * scale[0], -9.0 * scale[1])
    Curveto_r(7.0 * scale[0], -11.0 * scale[1], -23.0 * scale[0], -
              25.0 * scale[1], -43.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 2.0 * scale[1], -13.0 * scale[0],
              1.0 * scale[1], 0.0 * scale[0], -15.0 * scale[1])
    Curveto_r(12.0 * scale[0], -16.0 * scale[1], 12.0 * scale[0], -
              17.0 * scale[1], -3.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 9.0 * scale[1], -22.0 *
              scale[0], -1.0 * scale[1], 5.0 * scale[0], -25.0 * scale[1])
    Curveto_r(14.0 * scale[0], -13.0 * scale[1], 17.0 *
              scale[0], -18.0 * scale[1], 6.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 3.0 * scale[1], -22.0 * scale[0],
              0.0 * scale[1], -28.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -7.0 * scale[1], -11.0 *
              scale[0], -7.0 * scale[1], -9.0 * scale[0], -2.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], -1.0 * scale[0],
              11.0 * scale[1], -7.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 1.0 * scale[1], -9.0 * scale[0], -
              4.0 * scale[1], -7.0 * scale[0], -12.0 * scale[1])
    Curveto_r(1.0 * scale[0], -7.0 * scale[1], -6.0 * scale[0], -
              19.0 * scale[1], -16.0 * scale[0], -27.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -7.0 * scale[1], -21.0 * scale[0], -
              17.0 * scale[1], -23.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -5.0 * scale[1], -7.0 * scale[0], -
              9.0 * scale[1], -10.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 1.0 * scale[1], -5.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -25.0 * scale[1])
    Curveto_r(2.0 * scale[0], -15.0 * scale[1], 1.0 * scale[0], -
              19.0 * scale[1], -2.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 14.0 * scale[1], -10.0 * scale[0],
              12.0 * scale[1], -33.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-35.0 * scale[0], -40.0 * scale[1], -51.0 *
              scale[0], -70.0 * scale[1], -51.0 * scale[0], -95.0 * scale[1])
    Curveto_r(0.0 * scale[0], -25.0 * scale[1], 26.0 * scale[0], -
              36.0 * scale[1], 34.0 * scale[0], -16.0 * scale[1])
    Curveto_r(8.0 * scale[0], 21.0 * scale[1], 8.0 * scale[0],
              24.0 * scale[1], -5.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              6.0 * scale[1], -3.0 * scale[0], -12.0 * scale[1])
    Curveto_r(5.0 * scale[0], -10.0 * scale[1], 4.0 * scale[0], -
              10.0 * scale[1], -6.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 14.0 * scale[1], -4.0 * scale[0],
              34.0 * scale[1], 15.0 * scale[0], 26.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 15.0 * scale[0],
              0.0 * scale[1], 15.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 5.0 * scale[0],
              11.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              7.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 8.0 * scale[0], -
              9.0 * scale[1], 34.0 * scale[0], 11.0 * scale[1])
    Curveto_r(19.0 * scale[0], 15.0 * scale[1], 33.0 * scale[0],
              32.0 * scale[1], 30.0 * scale[0], 39.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], 12.0 * scale[0], 20.0 * scale[1])
    Curveto_r(14.0 * scale[0], 5.0 * scale[1], 15.0 * scale[0],
              4.0 * scale[1], 4.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -22.0 * scale[1], 4.0 *
              scale[0], -19.0 * scale[1], 23.0 * scale[0], 3.0 * scale[1])
    Curveto_r(10.0 * scale[0], 10.0 * scale[1], 14.0 * scale[0],
              22.0 * scale[1], 10.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 4.0 * scale[1], -3.0 * scale[0],
              5.0 * scale[1], 4.0 * scale[0], 1.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 14.0 *
              scale[0], -2.0 * scale[1], 18.0 * scale[0], 3.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 11.0 * scale[0],
              8.0 * scale[1], 19.0 * scale[0], 5.0 * scale[1])
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 20.0 * scale[0],
              10.0 * scale[1], 31.0 * scale[0], 31.0 * scale[1])
    Curveto_r(11.0 * scale[0], 19.0 * scale[1], 24.0 * scale[0],
              35.0 * scale[1], 30.0 * scale[0], 35.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 2.0 * scale[0],
              7.0 * scale[1], -8.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 10.0 * scale[1], -15.0 * scale[0],
              15.0 * scale[1], -5.0 * scale[0], 19.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 7.0 * scale[0],
              7.0 * scale[1], -7.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 4.0 * scale[1], -27.0 * scale[0],
              15.0 * scale[1], -35.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 13.0 * scale[1], -13.0 *
              scale[0], 14.0 * scale[1], 2.0 * scale[0], 8.0 * scale[1])
    Curveto_r(14.0 * scale[0], -5.0 * scale[1], 17.0 * scale[0],
              1.0 * scale[1], 16.0 * scale[0], 34.0 * scale[1])
    Curveto_r(0.0 * scale[0], 21.0 * scale[1], -5.0 * scale[0],
              39.0 * scale[1], -10.0 * scale[0], 39.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              7.0 * scale[1], -4.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto_r(-145.0 * scale[0], -259.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -11.0 * scale[1], 9.0 * scale[0], -
              16.0 * scale[1], -1.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -4.0 * scale[1], -10.0 *
              scale[0], -4.0 * scale[1], -6.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 4.0 * scale[1], 0.0 * scale[0],
              14.0 * scale[1], -10.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 7.0 * scale[1], -12.0 * scale[0],
              14.0 * scale[1], -6.0 * scale[0], 14.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0], -
              6.0 * scale[1], 23.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(890.0 * scale[0], 973.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 21.0 * scale[0], -
              27.0 * scale[1], 33.0 * scale[0], -13.0 * scale[1])
    Curveto_r(9.0 * scale[0], 10.0 * scale[1], 9.0 * scale[0],
              11.0 * scale[1], -2.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -4.0 * scale[1], -17.0 *
              scale[0], -2.0 * scale[1], -22.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 9.0 * scale[1], -9.0 * scale[0],
              10.0 * scale[1], -9.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(895.0 * scale[0], 920.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 11.0 * scale[0], -10.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 4.0 * scale[0],
              5.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              10.0 * scale[1], -11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              4.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(841.0 * scale[0], 911.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -6.0 * scale[1], -10.0 *
              scale[0], -10.0 * scale[1], -1.0 * scale[0], -16.0 * scale[1])
    Curveto_r(8.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              12.0 * scale[1], -6.0 * scale[0], -26.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -24.0 * scale[1], -14.0 *
              scale[0], -25.0 * scale[1], 12.0 * scale[0], -1.0 * scale[1])
    Curveto_r(28.0 * scale[0], 25.0 * scale[1], 24.0 * scale[0],
              61.0 * scale[1], -5.0 * scale[0], 43.0 * scale[1])
    te.end_fill()
    Moveto(920.0 * scale[0], 788.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -18.0 * scale[1], -20.0 *
              scale[0], -40.0 * scale[1], -20.0 * scale[0], -48.0 * scale[1])
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], -1.0 * scale[0], -
              13.0 * scale[1], -10.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 12.0 * scale[1], -10.0 * scale[0],
              11.0 * scale[1], -10.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], -6.0 * scale[0], -
              26.0 * scale[1], -13.0 * scale[0], -30.0 * scale[1])
    Curveto_r(-22.0 * scale[0], -13.0 * scale[1], -30.0 *
              scale[0], -44.0 * scale[1], -11.0 * scale[0], -41.0 * scale[1])
    Curveto_r(11.0 * scale[0], 2.0 * scale[1], 18.0 * scale[0], -
              6.0 * scale[1], 21.0 * scale[0], -21.0 * scale[1])
    Curveto_r(2.0 * scale[0], -14.0 * scale[1], 0.0 * scale[0], -
              22.0 * scale[1], -3.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 7.0 * scale[1], -34.0 * scale[0], -
              37.0 * scale[1], -38.0 * scale[0], -61.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -8.0 * scale[1], -7.0 * scale[0], -
              17.0 * scale[1], -14.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -4.0 * scale[1], -8.0 * scale[0], -
              12.0 * scale[1], -3.0 * scale[0], -20.0 * scale[1])
    Curveto_r(7.0 * scale[0], -11.0 * scale[1], 12.0 *
              scale[0], -9.0 * scale[1], 21.0 * scale[0], 9.0 * scale[1])
    Lineto_r(12.0 * scale[0], 22.0 * scale[1])
    Lineto_r(19.0 * scale[0], -31.0 * scale[1])
    Curveto_r(21.0 * scale[0], -35.0 * scale[1], 24.0 *
              scale[0], -45.0 * scale[1], 9.0 * scale[0], -36.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -10.0 * scale[0], -
              7.0 * scale[1], -10.0 * scale[0], -24.0 * scale[1])
    Curveto_r(0.0 * scale[0], -17.0 * scale[1], -4.0 * scale[0], -
              31.0 * scale[1], -10.0 * scale[0], -31.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              9.0 * scale[1], -10.0 * scale[0], -20.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 7.0 * scale[0], -
              20.0 * scale[1], 15.0 * scale[0], -20.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              7.0 * scale[1], 15.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 4.0 * scale[0],
              15.0 * scale[1], 10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              6.0 * scale[1], 4.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 7.0 * scale[1], 0.0 * scale[0],
              24.0 * scale[1], 6.0 * scale[0], 38.0 * scale[1])
    Curveto_r(8.0 * scale[0], 19.0 * scale[1], 9.0 * scale[0],
              14.0 * scale[1], 5.0 * scale[0], -26.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -108.0 * scale[1], -13.0 *
              scale[0], -135.0 * scale[1], -4.0 * scale[0], -141.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 9.0 * scale[0],
              11.0 * scale[1], 9.0 * scale[0], 31.0 * scale[1])
    Curveto_r(0.0 * scale[0], 22.0 * scale[1], 4.0 * scale[0],
              34.0 * scale[1], 10.0 * scale[0], 30.0 * scale[1])
    Curveto_r(17.0 * scale[0], -10.0 * scale[1], 12.0 * scale[0], -
              95.0 * scale[1], -5.0 * scale[0], -101.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -5.0 * scale[1], -14.0 *
              scale[0], -15.0 * scale[1], -9.0 * scale[0], -43.0 * scale[1])
    Lineto_r(7.0 * scale[0], -36.0 * scale[1])
    Lineto_r(-22.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-26.0 * scale[0], 23.0 * scale[1], -26.0 * scale[0],
              23.0 * scale[1], -2.0 * scale[0], -42.0 * scale[1])
    Curveto_r(20.0 * scale[0], -55.0 * scale[1], 69.0 * scale[0], -
              128.0 * scale[1], 79.0 * scale[0], -118.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -3.0 * scale[0],
              15.0 * scale[1], -13.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 17.0 * scale[1], -16.0 * scale[0],
              22.0 * scale[1], -4.0 * scale[0], 36.0 * scale[1])
    Curveto_r(11.0 * scale[0], 13.0 * scale[1], 14.0 * scale[0],
              67.0 * scale[1], 14.0 * scale[0], 248.0 * scale[1])
    Curveto_r(0.0 * scale[0], 127.0 * scale[1], -4.0 * scale[0],
              267.0 * scale[1], -9.0 * scale[0], 311.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 44.0 * scale[1], -9.0 * scale[0],
              97.0 * scale[1], -10.0 * scale[0], 118.0 * scale[1])
    Curveto_r(0.0 * scale[0], 20.0 * scale[1], -1.0 * scale[0],
              37.0 * scale[1], -3.0 * scale[0], 37.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              15.0 * scale[1], -23.0 * scale[0], -32.0 * scale[1])
    te.end_fill()
    Moveto_r(-36.0 * scale[0], -213.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -8.0 * scale[1], -11.0 * scale[0], -
              15.0 * scale[1], -16.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], 2.0 * scale[0], 15.0 * scale[1])
    Curveto_r(7.0 * scale[0], 8.0 * scale[1], 14.0 * scale[0],
              15.0 * scale[1], 16.0 * scale[0], 15.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 1.0 * scale[0], -
              7.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto_r(6.0 * scale[0], -35.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              10.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0],
              5.0 * scale[1], -11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -1.0 * scale[0],
              10.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0], -
              4.0 * scale[1], 11.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto_r(60.0 * scale[0], -147.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -26.0 * scale[1], -3.0 * scale[0], -
              34.0 * scale[1], -11.0 * scale[0], -26.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 9.0 * scale[1], -3.0 * scale[0],
              63.0 * scale[1], 7.0 * scale[0], 63.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 4.0 * scale[0], -
              17.0 * scale[1], 4.0 * scale[0], -37.0 * scale[1])
    te.end_fill()
    Moveto_r(-3.0 * scale[0], -155.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -6.0 *
              scale[0], -5.0 * scale[1], -6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 11.0 * scale[1], 2.0 * scale[0],
              17.0 * scale[1], 5.0 * scale[0], 13.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 4.0 * scale[0], -
              12.0 * scale[1], 1.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto_r(-20.0 * scale[0], -125.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -10.0 * scale[1], -5.0 *
              scale[0], -4.0 * scale[1], -5.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], 2.0 * scale[0],
              24.0 * scale[1], 5.0 * scale[0], 18.0 * scale[1])
    Curveto_r(2.0 * scale[0], -7.0 * scale[1], 2.0 * scale[0], -
              21.0 * scale[1], 0.0 * scale[0], -30.0 * scale[1])
    te.end_fill()
    Moveto(372.0 * scale[0], 679.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-23.0 * scale[0], -17.0 * scale[1], -42.0 *
              scale[0], -34.0 * scale[1], -42.0 * scale[0], -39.0 * scale[1])
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 28.0 * scale[0], -
              20.0 * scale[1], 34.0 * scale[0], -7.0 * scale[1])
    Curveto_r(2.0 * scale[0], 7.0 * scale[1], 4.0 * scale[0], -
              1.0 * scale[1], 3.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -16.0 * scale[1], -8.0 * scale[0], -
              34.0 * scale[1], -17.0 * scale[0], -40.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -10.0 * scale[1], -13.0 *
              scale[0], -10.0 * scale[1], -3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(13.0 * scale[0], 16.0 * scale[1], 8.0 * scale[0],
              29.0 * scale[1], -9.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0], -
              5.0 * scale[1], -2.0 * scale[0], -12.0 * scale[1])
    Curveto_r(4.0 * scale[0], -7.0 * scale[1], 3.0 * scale[0], -
              8.0 * scale[1], -5.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -14.0 * scale[0],
              0.0 * scale[1], -17.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -9.0 * scale[1], -11.0 * scale[0], -
              13.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -1.0 * scale[0],
              14.0 * scale[1], 13.0 * scale[0], 25.0 * scale[1])
    Curveto_r(19.0 * scale[0], 14.0 * scale[1], 22.0 * scale[0],
              20.0 * scale[1], 12.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 7.0 * scale[1], -13.0 * scale[0],
              9.0 * scale[1], -13.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -15.0 * scale[0], -
              18.0 * scale[1], -32.0 * scale[0], -29.0 * scale[1])
    Curveto_r(-51.0 * scale[0], -29.0 * scale[1], -108.0 *
              scale[0], -77.0 * scale[1], -103.0 * scale[0], -86.0 * scale[1])
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], -10.0 * scale[0], -
              13.0 * scale[1], -28.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-39.0 * scale[0], -14.0 * scale[1], -74.0 *
              scale[0], -56.0 * scale[1], -39.0 * scale[0], -47.0 * scale[1])
    Curveto_r(31.0 * scale[0], 8.0 * scale[1], 49.0 * scale[0], -
              7.0 * scale[1], 32.0 * scale[0], -26.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -18.0 * scale[1], -8.0 *
              scale[0], -32.0 * scale[1], 10.0 * scale[0], -21.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 10.0 * scale[0],
              19.0 * scale[1], 8.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 19.0 * scale[1], 2.0 * scale[0],
              28.0 * scale[1], 15.0 * scale[0], 30.0 * scale[1])
    Curveto_r(12.0 * scale[0], 2.0 * scale[1], 17.0 * scale[0], -
              3.0 * scale[1], 17.0 * scale[0], -17.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 4.0 * scale[0], -
              22.0 * scale[1], 9.0 * scale[0], -25.0 * scale[1])
    Curveto_r(16.0 * scale[0], -11.0 * scale[1], 19.0 *
              scale[0], -46.0 * scale[1], 4.0 * scale[0], -61.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -8.0 * scale[1], -11.0 * scale[0], -
              15.0 * scale[1], -6.0 * scale[0], -15.0 * scale[1])
    Curveto_r(15.0 * scale[0], 0.0 * scale[1], 33.0 * scale[0],
              23.0 * scale[1], 33.0 * scale[0], 43.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], 5.0 * scale[0],
              15.0 * scale[1], 10.0 * scale[0], 12.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 10.0 * scale[0],
              0.0 * scale[1], 10.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], 9.0 * scale[0],
              19.0 * scale[1], 20.0 * scale[0], 25.0 * scale[1])
    Curveto_r(11.0 * scale[0], 7.0 * scale[1], 27.0 * scale[0],
              27.0 * scale[1], 36.0 * scale[0], 45.0 * scale[1])
    Curveto_r(9.0 * scale[0], 18.0 * scale[1], 28.0 * scale[0],
              43.0 * scale[1], 43.0 * scale[0], 55.0 * scale[1])
    Curveto_r(21.0 * scale[0], 19.0 * scale[1], 22.0 * scale[0],
              22.0 * scale[1], 6.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -5.0 * scale[1], -18.0 *
              scale[0], -4.0 * scale[1], 2.0 * scale[0], 8.0 * scale[1])
    Curveto_r(12.0 * scale[0], 7.0 * scale[1], 23.0 * scale[0],
              18.0 * scale[1], 24.0 * scale[0], 23.0 * scale[1])
    Curveto_r(1.0 * scale[0], 6.0 * scale[1], 10.0 * scale[0],
              16.0 * scale[1], 21.0 * scale[0], 23.0 * scale[1])
    Curveto_r(10.0 * scale[0], 7.0 * scale[1], 16.0 * scale[0],
              18.0 * scale[1], 13.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 5.0 * scale[1], -1.0 * scale[0],
              9.0 * scale[1], 5.0 * scale[0], 9.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0],
              5.0 * scale[1], 5.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -2.0 * scale[0],
              10.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0],
              27.0 * scale[1], -5.0 * scale[0], 40.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 7.0 * scale[1], -24.0 * scale[0],
              0.0 * scale[1], -52.0 * scale[0], -21.0 * scale[1])
    te.end_fill()
    Moveto_r(48.0 * scale[0], -9.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -22.0 * scale[1], -25.0 *
              scale[0], -26.0 * scale[1], -36.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], -3.0 * scale[0],
              8.0 * scale[1], 3.0 * scale[0], 5.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 16.0 * scale[0],
              0.0 * scale[1], 23.0 * scale[0], 8.0 * scale[1])
    Curveto_r(18.0 * scale[0], 21.0 * scale[1], 23.0 * scale[0],
              19.0 * scale[1], 10.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(480.0 * scale[0], 609.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0], -
              7.0 * scale[1], 10.0 * scale[0], -4.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 10.0 * scale[0],
              8.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 2.0 * scale[1], -4.0 * scale[0],
              4.0 * scale[1], -10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              5.0 * scale[1], -10.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(449.0 * scale[0], 605.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -6.0 * scale[1], -2.0 * scale[0], -
              15.0 * scale[1], -3.0 * scale[0], -21.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -12.0 * scale[0], -
              21.0 * scale[1], -26.0 * scale[0], -33.0 * scale[1])
    Lineto_r(-25.0 * scale[0], -22.0 * scale[1])
    Lineto_r(25.0 * scale[0], 13.0 * scale[1])
    Curveto_r(14.0 * scale[0], 7.0 * scale[1], 29.0 * scale[0],
              11.0 * scale[1], 35.0 * scale[0], 9.0 * scale[1])
    Curveto_r(5.0 * scale[0], -1.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 3.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 4.0 * scale[1], -3.0 * scale[0],
              13.0 * scale[1], 4.0 * scale[0], 21.0 * scale[1])
    Curveto_r(8.0 * scale[0], 10.0 * scale[1], 8.0 * scale[0],
              17.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 7.0 * scale[1], -13.0 * scale[0],
              8.0 * scale[1], -13.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(847.0 * scale[0], 523.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -3.0 * scale[1], -7.0 * scale[0], -
              11.0 * scale[1], -7.0 * scale[0], -17.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 5.0 * scale[0], -
              5.0 * scale[1], 12.0 * scale[0], 2.0 * scale[1])
    Curveto_r(6.0 * scale[0], 6.0 * scale[1], 9.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0],
              2.0 * scale[1], -12.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(791.0 * scale[0], 502.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -14.0 * scale[1], -6.0 *
              scale[0], -19.0 * scale[1], 5.0 * scale[0], -19.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0],
              9.0 * scale[1], 14.0 * scale[0], 19.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], -2.0 * scale[0],
              18.0 * scale[1], -5.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              8.0 * scale[1], -14.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(374.0 * scale[0], 499.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], -3.0 *
              scale[0], -9.0 * scale[1], 4.0 * scale[0], -5.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 13.0 * scale[0],
              0.0 * scale[1], 15.0 * scale[0], -6.0 * scale[1])
    Curveto_r(4.0 * scale[0], -9.0 * scale[1], 6.0 * scale[0], -
              10.0 * scale[1], 6.0 * scale[0], -1.0 * scale[1])
    Curveto_r(1.0 * scale[0], 17.0 * scale[1], -16.0 * scale[0],
              25.0 * scale[1], -25.0 * scale[0], 12.0 * scale[1])
    te.end_fill()
    Moveto(370.0 * scale[0], 470.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0], -
              8.0 * scale[1], -10.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -13.0 * scale[0], -
              7.0 * scale[1], -16.0 * scale[0], -24.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -17.0 * scale[1], -13.0 * scale[0], -
              36.0 * scale[1], -20.0 * scale[0], -42.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -6.0 * scale[1], -14.0 * scale[0], -
              18.0 * scale[1], -14.0 * scale[0], -25.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -4.0 * scale[0], -
              14.0 * scale[1], -10.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              7.0 * scale[1], -10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], -6.0 * scale[0], -
              14.0 * scale[1], -15.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -15.0 * scale[0],
              3.0 * scale[1], -15.0 * scale[0], 1.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], 52.0 * scale[0], -
              32.0 * scale[1], 83.0 * scale[0], -39.0 * scale[1])
    Curveto_r(26.0 * scale[0], -6.0 * scale[1], 27.0 *
              scale[0], -5.0 * scale[1], 18.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 25.0 * scale[1], -14.0 * scale[0],
              121.0 * scale[1], -1.0 * scale[0], 121.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              6.0 * scale[1], 10.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 5.0 * scale[0],
              16.0 * scale[1], 12.0 * scale[0], 18.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 9.0 * scale[0],
              6.0 * scale[1], 0.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -12.0 * scale[0],
              2.0 * scale[1], -12.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto_r(-52.0 * scale[0], -141.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -5.0 * scale[1], -17.0 *
              scale[0], -8.0 * scale[1], -23.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0],
              3.0 * scale[1], 3.0 * scale[0], 6.0 * scale[1])
    Curveto_r(6.0 * scale[0], 2.0 * scale[1], 9.0 * scale[0],
              10.0 * scale[1], 6.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 7.0 * scale[1], -2.0 * scale[0],
              8.0 * scale[1], 4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(7.0 * scale[0], -4.0 * scale[1], 12.0 * scale[0],
              0.0 * scale[1], 13.0 * scale[0], 11.0 * scale[1])
    Curveto_r(1.0 * scale[0], 17.0 * scale[1], 2.0 * scale[0],
              17.0 * scale[1], 6.0 * scale[0], -1.0 * scale[1])
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], -1.0 * scale[0], -
              22.0 * scale[1], -9.0 * scale[0], -27.0 * scale[1])
    te.end_fill()
    Moveto(786.0 * scale[0], 455.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -1.0 * scale[0], -
              15.0 * scale[1], 4.0 * scale[0], -15.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              7.0 * scale[1], 10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -2.0 * scale[0],
              15.0 * scale[1], -4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0], -
              7.0 * scale[1], -10.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(89.0 * scale[0], 431.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -6.0 * scale[1], 10.0 * scale[0], -
              11.0 * scale[1], 2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -4.0 * scale[1], -11.0 * scale[0], -
              12.0 * scale[1], -11.0 * scale[0], -18.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], 6.0 * scale[0], -
              6.0 * scale[1], 15.0 * scale[0], 2.0 * scale[1])
    Curveto_r(20.0 * scale[0], 17.0 * scale[1], 19.0 * scale[0],
              40.0 * scale[1], -2.0 * scale[0], 40.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -15.0 *
              scale[0], -2.0 * scale[1], -4.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(817.0 * scale[0], 434.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -9.0 * scale[1], 4.0 * scale[0], -
              35.0 * scale[1], 14.0 * scale[0], -28.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 9.0 * scale[0],
              12.0 * scale[1], 9.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -12.0 * scale[0],
              19.0 * scale[1], -23.0 * scale[0], 8.0 * scale[1])
    te.end_fill()
    Moveto(173.0 * scale[0], 389.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -29.0 * scale[1], 1.0 * scale[0], -
              30.0 * scale[1], 14.0 * scale[0], -13.0 * scale[1])
    Curveto_r(14.0 * scale[0], 20.0 * scale[1], 13.0 * scale[0],
              36.0 * scale[1], -3.0 * scale[0], 41.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 2.0 * scale[1], -11.0 * scale[0], -
              11.0 * scale[1], -11.0 * scale[0], -28.0 * scale[1])
    te.end_fill()
    Moveto(704.0 * scale[0], 408.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], -2.0 *
              scale[0], -8.0 * scale[1], 3.0 * scale[0], -8.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 0.0 * scale[0], -
              5.0 * scale[1], -10.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -15.0 * scale[0], -
              14.0 * scale[1], -12.0 * scale[0], -19.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], -3.0 * scale[0], -
              15.0 * scale[1], -15.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -7.0 * scale[1], -20.0 * scale[0], -
              20.0 * scale[1], -20.0 * scale[0], -28.0 * scale[1])
    Curveto_r(1.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0], -
              6.0 * scale[1], 25.0 * scale[0], 13.0 * scale[1])
    Curveto_r(14.0 * scale[0], 16.0 * scale[1], 23.0 * scale[0],
              33.0 * scale[1], 20.0 * scale[0], 38.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 5.0 * scale[1], 4.0 * scale[0],
              9.0 * scale[1], 16.0 * scale[0], 9.0 * scale[1])
    Curveto_r(18.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0],
              2.0 * scale[1], 9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 13.0 * scale[1], -10.0 *
              scale[0], 14.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(9.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 16.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], -29.0 * scale[0],
              13.0 * scale[1], -36.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(850.0 * scale[0], 360.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0], -
              10.0 * scale[1], 10.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              5.0 * scale[1], 10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -4.0 * scale[0],
              10.0 * scale[1], -10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              4.0 * scale[1], -10.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(28.0 * scale[0], 273.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -49.0 * scale[1], -1.0 * scale[0], -
              110.0 * scale[1], 2.0 * scale[0], -138.0 * scale[1])
    Lineto_r(5.0 * scale[0], -50.0 * scale[1])
    Lineto_r(25.0 * scale[0], 47.0 * scale[1])
    Curveto_r(13.0 * scale[0], 26.0 * scale[1], 27.0 * scale[0],
              45.0 * scale[1], 30.0 * scale[0], 43.0 * scale[1])
    Curveto_r(11.0 * scale[0], -7.0 * scale[1], 2.0 * scale[0],
              57.0 * scale[1], -9.0 * scale[0], 68.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 6.0 * scale[1], -11.0 * scale[0],
              19.0 * scale[1], -11.0 * scale[0], 29.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], -4.0 * scale[0],
              18.0 * scale[1], -10.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0],
              13.0 * scale[1], -10.0 * scale[0], 29.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], -4.0 * scale[0],
              32.0 * scale[1], -9.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -11.0 * scale[0], -
              32.0 * scale[1], -13.0 * scale[0], -82.0 * scale[1])
    te.end_fill()
    Moveto(848.0 * scale[0], 313.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(610.0 * scale[0], 270.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -4.0 * scale[0], -
              9.0 * scale[1], -9.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -12.0 * scale[0], -
              1.0 * scale[1], -15.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -23.0 * scale[1], -7.0 *
              scale[0], -34.0 * scale[1], 4.0 * scale[0], -34.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              7.0 * scale[1], 10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], 7.0 * scale[0],
              18.0 * scale[1], 16.0 * scale[0], 23.0 * scale[1])
    Curveto_r(11.0 * scale[0], 6.0 * scale[1], 13.0 * scale[0],
              11.0 * scale[1], 5.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -11.0 * scale[0],
              2.0 * scale[1], -11.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(201.0 * scale[0], 251.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -10.0 * scale[1], -7.0 * scale[0], -
              21.0 * scale[1], -4.0 * scale[0], -25.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], -1.0 * scale[0], -
              6.0 * scale[1], -10.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0], -
              7.0 * scale[1], -17.0 * scale[0], -15.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -5.0 * scale[0], -
              15.0 * scale[1], -11.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              5.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(5.0 * scale[0], -8.0 * scale[1], 11.0 *
              scale[0], -7.0 * scale[1], 21.0 * scale[0], 1.0 * scale[1])
    Curveto_r(11.0 * scale[0], 9.0 * scale[1], 14.0 * scale[0],
              7.0 * scale[1], 14.0 * scale[0], -14.0 * scale[1])
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 5.0 * scale[0], -
              29.0 * scale[1], 10.0 * scale[0], -32.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 8.0 * scale[0],
              7.0 * scale[1], 5.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 20.0 * scale[1], 2.0 * scale[0],
              50.0 * scale[1], 9.0 * scale[0], 67.0 * scale[1])
    Curveto_r(12.0 * scale[0], 28.0 * scale[1], 15.0 * scale[0],
              30.0 * scale[1], 23.0 * scale[0], 14.0 * scale[1])
    Curveto_r(9.0 * scale[0], -16.0 * scale[1], 11.0 * scale[0], -
              16.0 * scale[1], 16.0 * scale[0], -1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 10.0 * scale[1], 3.0 * scale[0],
              15.0 * scale[1], -3.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -3.0 * scale[1], -10.0 *
              scale[0], -1.0 * scale[1], -10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 18.0 * scale[1], -29.0 * scale[0],
              12.0 * scale[1], -39.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(840.0 * scale[0], 249.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 5.0 * scale[0], -
              17.0 * scale[1], 10.0 * scale[0], -14.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 10.0 * scale[0],
              13.0 * scale[1], 10.0 * scale[0], 21.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -4.0 * scale[0],
              14.0 * scale[1], -10.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              9.0 * scale[1], -10.0 * scale[0], -21.0 * scale[1])
    te.end_fill()
    Moveto(270.0 * scale[0], 256.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(263.0 * scale[0], 211.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -11.0 * scale[1], 5.0 * scale[0], -
              26.0 * scale[1], 14.0 * scale[0], -33.0 * scale[1])
    Curveto_r(14.0 * scale[0], -11.0 * scale[1], 15.0 *
              scale[0], -10.0 * scale[1], 8.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 34.0 * scale[1], -20.0 * scale[0],
              44.0 * scale[1], -22.0 * scale[0], 21.0 * scale[1])
    te.end_fill()
    Moveto(290.0 * scale[0], 207.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -3.0 * scale[1], 12.0 * scale[0], -
              12.0 * scale[1], 26.0 * scale[0], -22.0 * scale[1])
    Curveto_r(15.0 * scale[0], -9.0 * scale[1], 23.0 * scale[0], -
              12.0 * scale[1], 20.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 11.0 * scale[1], -46.0 * scale[0],
              35.0 * scale[1], -46.0 * scale[0], 28.0 * scale[1])
    te.end_fill()
    Moveto(590.0 * scale[0], 197.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], -5.0 * scale[0], -
              17.0 * scale[1], -12.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              3.0 * scale[1], -5.0 * scale[0], -7.0 * scale[1])
    Curveto_r(4.0 * scale[0], -3.0 * scale[1], 0.0 * scale[0], -
              14.0 * scale[1], -9.0 * scale[0], -24.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -13.0 * scale[1], -12.0 *
              scale[0], -19.0 * scale[1], -3.0 * scale[0], -25.0 * scale[1])
    Curveto_r(8.0 * scale[0], -4.0 * scale[1], 10.0 *
              scale[0], -3.0 * scale[1], 5.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 7.0 * scale[1], -3.0 * scale[0],
              12.0 * scale[1], 2.0 * scale[0], 12.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 37.0 * scale[0],
              59.0 * scale[1], 28.0 * scale[0], 67.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -6.0 * scale[0], -
              1.0 * scale[1], -6.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(134.0 * scale[0], 155.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -11.0 * scale[1], -12.0 * scale[0], -
              23.0 * scale[1], -17.0 * scale[0], -26.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -1.0 *
              scale[0], -9.0 * scale[1], 8.0 * scale[0], -12.0 * scale[1])
    Curveto_r(9.0 * scale[0], -4.0 * scale[1], 13.0 *
              scale[0], -3.0 * scale[1], 10.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], 1.0 * scale[0],
              13.0 * scale[1], 9.0 * scale[0], 18.0 * scale[1])
    Curveto_r(10.0 * scale[0], 6.0 * scale[1], 12.0 * scale[0],
              13.0 * scale[1], 6.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 12.0 * scale[1], -10.0 * scale[0],
              11.0 * scale[1], -16.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(250.0 * scale[0], 139.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -4.0 * scale[0], -
              8.0 * scale[1], -9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -13.0 * scale[0],
              0.0 * scale[1], -17.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -9.0 * scale[1], 1.0 * scale[0], -
              10.0 * scale[1], 22.0 * scale[0], -5.0 * scale[1])
    Curveto_r(38.0 * scale[0], 10.0 * scale[1], 55.0 * scale[0],
              26.0 * scale[1], 26.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -22.0 * scale[0], -
              5.0 * scale[1], -22.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(350.0 * scale[0], 146.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(90.0 * scale[0], 95.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -8.0 * scale[1], -9.0 * scale[0], -
              15.0 * scale[1], -4.0 * scale[0], -15.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 0.0 * scale[0], -
              6.0 * scale[1], -11.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -11.0 * scale[1], -15.0 *
              scale[0], -16.0 * scale[1], -5.0 * scale[0], -22.0 * scale[1])
    Curveto_r(8.0 * scale[0], -5.0 * scale[1], 11.0 *
              scale[0], -4.0 * scale[1], 7.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], 0.0 * scale[0],
              13.0 * scale[1], 7.0 * scale[0], 16.0 * scale[1])
    Curveto_r(17.0 * scale[0], 7.0 * scale[1], 41.0 * scale[0],
              47.0 * scale[1], 28.0 * scale[0], 47.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              7.0 * scale[1], -22.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(367.0 * scale[0], 90.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -15.0 * scale[1], -14.0 * scale[0], -
              20.0 * scale[1], -37.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -29.0 * scale[0], -
              4.0 * scale[1], -25.0 * scale[0], -10.0 * scale[1])
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 15.0 * scale[0], -
              8.0 * scale[1], 26.0 * scale[0], -5.0 * scale[1])
    Curveto_r(11.0 * scale[0], 4.0 * scale[1], 19.0 * scale[0],
              2.0 * scale[1], 19.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0], -
              11.0 * scale[1], -11.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -1.0 * scale[0], -
              9.0 * scale[1], 13.0 * scale[0], -19.0 * scale[1])
    Curveto_r(31.0 * scale[0], -25.0 * scale[1], 136.0 *
              scale[0], -25.0 * scale[1], 155.0 * scale[0], -1.0 * scale[1])
    Curveto_r(11.0 * scale[0], 13.0 * scale[1], 12.0 * scale[0],
              12.0 * scale[1], 13.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -18.0 * scale[1], 1.0 * scale[0], -
              18.0 * scale[1], 19.0 * scale[0], -2.0 * scale[1])
    Curveto_r(18.0 * scale[0], 17.0 * scale[1], 20.0 * scale[0],
              17.0 * scale[1], 31.0 * scale[0], -1.0 * scale[1])
    Curveto_r(10.0 * scale[0], -16.0 * scale[1], 11.0 *
              scale[0], -15.0 * scale[1], 6.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 14.0 * scale[1], -6.0 * scale[0],
              39.0 * scale[1], -6.0 * scale[0], 57.0 * scale[1])
    Lineto_r(0.0 * scale[0], 32.0 * scale[1])
    Lineto_r(-35.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -12.0 * scale[1], -34.0 *
              scale[0], -27.0 * scale[1], -35.0 * scale[0], -34.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -4.0 * scale[0], -
              14.0 * scale[1], -9.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -3.0 * scale[1], -8.0 * scale[0],
              8.0 * scale[1], -6.0 * scale[0], 25.0 * scale[1])
    Curveto_r(3.0 * scale[0], 25.0 * scale[1], 2.0 * scale[0],
              28.0 * scale[1], -9.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -6.0 * scale[1], -12.0 * scale[0], -
              16.0 * scale[1], -9.0 * scale[0], -21.0 * scale[1])
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], -6.0 * scale[0],
              0.0 * scale[1], -21.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 9.0 * scale[1], -33.0 * scale[0],
              15.0 * scale[1], -41.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -4.0 * scale[1], -15.0 * scale[0],
              1.0 * scale[1], -15.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 26.0 * scale[1], -16.0 * scale[0],
              26.0 * scale[1], -23.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(425.0 * scale[0], 100.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(47.0 * scale[0], 27.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], 1.0 * scale[0], -
              14.0 * scale[1], 8.0 * scale[0], -14.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              6.0 * scale[1], 8.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 7.0 * scale[1], -6.0 * scale[0],
              13.0 * scale[1], -8.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -5.0 * scale[0], -
              6.0 * scale[1], -8.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(107.0 * scale[0], 26.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -7.0 * scale[1], -17.0 * scale[0], -
              17.0 * scale[1], -17.0 * scale[0], -21.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 7.0 * scale[0], -
              2.0 * scale[1], 16.0 * scale[0], 6.0 * scale[1])
    Curveto_r(13.0 * scale[0], 10.0 * scale[1], 17.0 * scale[0],
              10.0 * scale[1], 25.0 * scale[0], -2.0 * scale[1])
    Curveto_r(7.0 * scale[0], -12.0 * scale[1], 9.0 *
              scale[0], -11.0 * scale[1], 9.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 23.0 * scale[1], -12.0 * scale[0],
              29.0 * scale[1], -33.0 * scale[0], 14.0 * scale[1])
    te.end_fill()
    Moveto(950.0 * scale[0], 10.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -8.0 * scale[1], -12.0 *
              scale[0], -10.0 * scale[1], 3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0],
              5.0 * scale[1], 17.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], -1.0 * scale[0],
              12.0 * scale[1], -20.0 * scale[0], 0.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#bae2f8')
    te.end_fill()
    Moveto(889.0 * scale[0], 1263.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-34.0 * scale[0], -49.0 * scale[1], -67.0 * scale[0], -
              94.0 * scale[1], -72.0 * scale[0], -100.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -9.0 * scale[1], -6.0 * scale[0], -
              13.0 * scale[1], 1.0 * scale[0], -13.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 78.0 * scale[0],
              89.0 * scale[1], 75.0 * scale[0], 101.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 5.0 * scale[1], 1.0 * scale[0],
              9.0 * scale[1], 7.0 * scale[0], 9.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 23.0 * scale[0],
              20.0 * scale[1], 40.0 * scale[0], 45.0 * scale[1])
    Curveto_r(17.0 * scale[0], 25.0 * scale[1], 27.0 * scale[0],
              45.0 * scale[1], 21.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -38.0 * scale[0], -
              39.0 * scale[1], -72.0 * scale[0], -87.0 * scale[1])
    te.end_fill()
    Moveto(478.0 * scale[0], 1273.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -2.0 * scale[1], -28.0 *
              scale[0], -8.0 * scale[1], -28.0 * scale[0], -13.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 14.0 *
              scale[0], -5.0 * scale[1], 31.0 * scale[0], 0.0 * scale[1])
    Curveto_r(18.0 * scale[0], 5.0 * scale[1], 36.0 * scale[0],
              7.0 * scale[1], 42.0 * scale[0], 3.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 7.0 *
              scale[0], -1.0 * scale[1], 3.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 7.0 * scale[1], -10.0 * scale[0],
              11.0 * scale[1], -14.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -1.0 * scale[1], -19.0 *
              scale[0], -4.0 * scale[1], -34.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(420.0 * scale[0], 1219.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -11.0 * scale[1], -10.0 *
              scale[0], -23.0 * scale[1], -7.0 * scale[0], -25.0 * scale[1])
    Curveto_r(2.0 * scale[0], -2.0 * scale[1], 9.0 * scale[0],
              7.0 * scale[1], 15.0 * scale[0], 21.0 * scale[1])
    Curveto_r(14.0 * scale[0], 30.0 * scale[1], 7.0 * scale[0],
              33.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(740.0 * scale[0], 1223.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -2.0 * scale[1], -21.0 *
              scale[0], -6.0 * scale[1], -28.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -3.0 * scale[1], -5.0 * scale[0], -
              14.0 * scale[1], 14.0 * scale[0], -40.0 * scale[1])
    Curveto_r(25.0 * scale[0], -32.0 * scale[1], 29.0 * scale[0], -
              34.0 * scale[1], 35.0 * scale[0], -18.0 * scale[1])
    Curveto_r(10.0 * scale[0], 25.0 * scale[1], 11.0 * scale[0],
              74.0 * scale[1], 2.0 * scale[0], 73.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              3.0 * scale[1], -23.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto_r(20.0 * scale[0], -33.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], -4.0 * scale[0], -
              20.0 * scale[1], -9.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -32.0 * scale[0],
              26.0 * scale[1], -24.0 * scale[0], 33.0 * scale[1])
    Curveto_r(13.0 * scale[0], 14.0 * scale[1], 33.0 * scale[0],
              6.0 * scale[1], 33.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(576.0 * scale[0], 1193.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(640.0 * scale[0], 1166.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(402.0 * scale[0], 1135.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(770.0 * scale[0], 1096.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -25.0 * scale[1], -30.0 *
              scale[0], -49.0 * scale[1], -30.0 * scale[0], -55.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -4.0 * scale[0], -
              11.0 * scale[1], -9.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -48.0 * scale[0], -
              50.0 * scale[1], -53.0 * scale[0], -71.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -8.0 * scale[1], -11.0 * scale[0], -
              20.0 * scale[1], -21.0 * scale[0], -27.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -7.0 * scale[1], -15.0 * scale[0], -
              18.0 * scale[1], -12.0 * scale[0], -23.0 * scale[1])
    Curveto_r(4.0 * scale[0], -5.0 * scale[1], 2.0 * scale[0], -
              9.0 * scale[1], -3.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -118.0 * scale[0], -
              151.0 * scale[1], -114.0 * scale[0], -163.0 * scale[1])
    Curveto_r(1.0 * scale[0], -5.0 * scale[1], -11.0 * scale[0], -
              7.0 * scale[1], -27.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-35.0 * scale[0], 5.0 * scale[1], -33.0 *
              scale[0], -7.0 * scale[1], 3.0 * scale[0], -14.0 * scale[1])
    Curveto_r(18.0 * scale[0], -4.0 * scale[1], 28.0 * scale[0],
              2.0 * scale[1], 42.0 * scale[0], 26.0 * scale[1])
    Curveto_r(10.0 * scale[0], 17.0 * scale[1], 18.0 * scale[0],
              33.0 * scale[1], 18.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 3.0 * scale[1], 4.0 * scale[0],
              10.0 * scale[1], 11.0 * scale[0], 15.0 * scale[1])
    Curveto_r(23.0 * scale[0], 20.0 * scale[1], 114.0 * scale[0],
              153.0 * scale[1], 108.0 * scale[0], 159.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 3.0 * scale[1], 0.0 * scale[0],
              6.0 * scale[1], 7.0 * scale[0], 6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              3.0 * scale[1], 7.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], 2.0 * scale[0],
              14.0 * scale[1], 12.0 * scale[0], 23.0 * scale[1])
    Curveto_r(28.0 * scale[0], 25.0 * scale[1], 113.0 * scale[0],
              151.0 * scale[1], 102.0 * scale[0], 151.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -24.0 * scale[0], -
              20.0 * scale[1], -41.0 * scale[0], -44.0 * scale[1])
    te.end_fill()
    Moveto(568.0 * scale[0], 1123.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(704.0 * scale[0], 1103.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -8.0 * scale[1], 1.0 * scale[0], -
              13.0 * scale[1], -11.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -12.0 *
              scale[0], -3.0 * scale[1], 6.0 * scale[0], -10.0 * scale[1])
    Curveto_r(31.0 * scale[0], -12.0 * scale[1], 40.0 *
              scale[0], -3.0 * scale[1], 16.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -15.0 * scale[0],
              11.0 * scale[1], -11.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(575.0 * scale[0], 1080.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(10.0 * scale[0], -11.0 * scale[1], 20.0 * scale[0], -
              20.0 * scale[1], 23.0 * scale[0], -20.0 * scale[1])
    Curveto_r(3.0 * scale[0], 0.0 * scale[1], -3.0 * scale[0],
              9.0 * scale[1], -13.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 11.0 * scale[1], -20.0 * scale[0],
              20.0 * scale[1], -23.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], 3.0 * scale[0], -
              9.0 * scale[1], 13.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(340.0 * scale[0], 1035.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-24.0 * scale[0], -25.0 * scale[1], -42.0 *
              scale[0], -45.0 * scale[1], -39.0 * scale[0], -45.0 * scale[1])
    Curveto_r(3.0 * scale[0], 0.0 * scale[1], 25.0 * scale[0],
              20.0 * scale[1], 49.0 * scale[0], 45.0 * scale[1])
    Curveto_r(24.0 * scale[0], 25.0 * scale[1], 42.0 * scale[0],
              45.0 * scale[1], 39.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -25.0 * scale[0], -
              20.0 * scale[1], -49.0 * scale[0], -45.0 * scale[1])
    te.end_fill()
    Moveto(612.0 * scale[0], 995.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(279.0 * scale[0], 963.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(16.0 * scale[0], 13.0 * scale[1], 21.0 * scale[0],
              21.0 * scale[1], 13.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              8.0 * scale[1], -17.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(586.0 * scale[0], 913.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(937.0 * scale[0], 890.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -11.0 * scale[1], -10.0 * scale[0], -
              20.0 * scale[1], -17.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0],
              5.0 * scale[1], -4.0 * scale[0], 12.0 * scale[1])
    Curveto_r(4.0 * scale[0], 7.0 * scale[1], 3.0 * scale[0],
              8.0 * scale[1], -5.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -9.0 * scale[0], -
              11.0 * scale[1], 0.0 * scale[0], -22.0 * scale[1])
    Curveto_r(15.0 * scale[0], -19.0 * scale[1], 16.0 *
              scale[0], -18.0 * scale[1], 34.0 * scale[0], 16.0 * scale[1])
    Curveto_r(9.0 * scale[0], 17.0 * scale[1], 11.0 * scale[0],
              30.0 * scale[1], 6.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              9.0 * scale[1], -14.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(869.0 * scale[0], 853.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -21.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(513.0 * scale[0], 820.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-23.0 * scale[0], -22.0 * scale[1], -39.0 *
              scale[0], -40.0 * scale[1], -35.0 * scale[0], -40.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 26.0 * scale[0],
              18.0 * scale[1], 47.0 * scale[0], 40.0 * scale[1])
    Curveto_r(50.0 * scale[0], 51.0 * scale[1], 43.0 * scale[0],
              51.0 * scale[1], -12.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(759.0 * scale[0], 773.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -21.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(137.0 * scale[0], 733.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -12.0 * scale[1], -7.0 *
              scale[0], -23.0 * scale[1], 11.0 * scale[0], -23.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0],
              2.0 * scale[1], 3.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 7.0 * scale[1], -11.0 * scale[0],
              9.0 * scale[1], 0.0 * scale[0], 14.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 9.0 * scale[0],
              6.0 * scale[1], 3.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 1.0 * scale[1], -14.0 * scale[0], -
              2.0 * scale[1], -17.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(176.0 * scale[0], 703.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(449.0 * scale[0], 688.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -28.0 * scale[1], 6.0 * scale[0], -
              29.0 * scale[1], 9.0 * scale[0], -9.0 * scale[1])
    Curveto_r(2.0 * scale[0], 13.0 * scale[1], 0.0 * scale[0],
              27.0 * scale[1], -5.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 6.0 * scale[1], -7.0 * scale[0], -
              3.0 * scale[1], -4.0 * scale[0], -23.0 * scale[1])
    te.end_fill()
    Moveto(349.0 * scale[0], 693.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -21.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(649.0 * scale[0], 693.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -21.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(521.0 * scale[0], 684.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(800.0 * scale[0], 675.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -13.0 * scale[1], -11.0 *
              scale[0], -18.0 * scale[1], 0.0 * scale[0], -28.0 * scale[1])
    Curveto_r(10.0 * scale[0], -9.0 * scale[1], 11.0 *
              scale[0], -9.0 * scale[1], 6.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 7.0 * scale[1], -2.0 * scale[0],
              19.0 * scale[1], 4.0 * scale[0], 27.0 * scale[1])
    Curveto_r(7.0 * scale[0], 8.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              7.0 * scale[1], -17.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(155.0 * scale[0], 670.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(820.0 * scale[0], 652.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              9.0 * scale[1], 15.0 * scale[0], -9.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              4.0 * scale[1], 15.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], -7.0 * scale[0],
              8.0 * scale[1], -15.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              4.0 * scale[1], -15.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(438.0 * scale[0], 626.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-71.0 * scale[0], -96.0 * scale[1], -138.0 * scale[0], -
              206.0 * scale[1], -125.0 * scale[0], -206.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 39.0 * scale[0],
              49.0 * scale[1], 82.0 * scale[0], 109.0 * scale[1])
    Curveto_r(48.0 * scale[0], 68.0 * scale[1], 86.0 * scale[0],
              112.0 * scale[1], 99.0 * scale[0], 114.0 * scale[1])
    Curveto_r(12.0 * scale[0], 3.0 * scale[1], 9.0 * scale[0],
              4.0 * scale[1], -10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -1.0 * scale[1], -36.0 *
              scale[0], -9.0 * scale[1], -46.0 * scale[0], -21.0 * scale[1])
    te.end_fill()
    Moveto(511.0 * scale[0], 607.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -10.0 * scale[1], -8.0 * scale[0], -
              20.0 * scale[1], -16.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -4.0 * scale[1], -15.0 * scale[0], -
              11.0 * scale[1], -15.0 * scale[0], -17.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 10.0 * scale[0], -
              2.0 * scale[1], 21.0 * scale[0], 10.0 * scale[1])
    Curveto_r(12.0 * scale[0], 11.0 * scale[1], 19.0 * scale[0],
              27.0 * scale[1], 16.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 10.0 * scale[1], -6.0 * scale[0],
              8.0 * scale[1], -6.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(166.0 * scale[0], 565.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -8.0 * scale[1], -15.0 *
              scale[0], -15.0 * scale[1], -9.0 * scale[0], -15.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0],
              7.0 * scale[1], 23.0 * scale[0], 15.0 * scale[1])
    Curveto_r(16.0 * scale[0], 19.0 * scale[1], 11.0 * scale[0],
              19.0 * scale[1], -14.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(449.0 * scale[0], 543.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -21.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(770.0 * scale[0], 520.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -11.0 * scale[1], -8.0 * scale[0], -
              20.0 * scale[1], -6.0 * scale[0], -20.0 * scale[1])
    Curveto_r(3.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              9.0 * scale[1], 16.0 * scale[0], 20.0 * scale[1])
    Curveto_r(6.0 * scale[0], 11.0 * scale[1], 8.0 * scale[0],
              20.0 * scale[1], 6.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              9.0 * scale[1], -16.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(100.0 * scale[0], 520.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -5.0 * scale[1], -12.0 * scale[0], -
              12.0 * scale[1], -9.0 * scale[0], -15.0 * scale[1])
    Curveto_r(4.0 * scale[0], -3.0 * scale[1], 12.0 * scale[0],
              1.0 * scale[1], 19.0 * scale[0], 10.0 * scale[1])
    Curveto_r(14.0 * scale[0], 17.0 * scale[1], 11.0 * scale[0],
              19.0 * scale[1], -10.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(66.0 * scale[0], 493.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(25.0 * scale[0], 470.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              10.0 * scale[1], 4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              5.0 * scale[1], 11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -2.0 * scale[0],
              10.0 * scale[1], -4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              4.0 * scale[1], -11.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(382.0 * scale[0], 445.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -14.0 * scale[1], -12.0 * scale[0], -
              34.0 * scale[1], -12.0 * scale[0], -43.0 * scale[1])
    Curveto_r(1.0 * scale[0], -9.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 15.0 * scale[0], 23.0 * scale[1])
    Curveto_r(16.0 * scale[0], 45.0 * scale[1], 14.0 * scale[0],
              58.0 * scale[1], -3.0 * scale[0], 20.0 * scale[1])
    te.end_fill()
    Moveto(709.0 * scale[0], 428.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-17.0 * scale[0], -24.0 * scale[1], -18.0 *
              scale[0], -29.0 * scale[1], -6.0 * scale[0], -19.0 * scale[1])
    Curveto_r(18.0 * scale[0], 14.0 * scale[1], 42.0 * scale[0],
              51.0 * scale[1], 33.0 * scale[0], 51.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              15.0 * scale[1], -27.0 * scale[0], -32.0 * scale[1])
    te.end_fill()
    Moveto(291.0 * scale[0], 408.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -10.0 * scale[1], -5.0 * scale[0], -
              18.0 * scale[1], -11.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -34.0 * scale[0], -
              39.0 * scale[1], -27.0 * scale[0], -46.0 * scale[1])
    Curveto_r(8.0 * scale[0], -9.0 * scale[1], 49.0 * scale[0],
              56.0 * scale[1], 44.0 * scale[0], 69.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 7.0 * scale[1], -6.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(664.0 * scale[0], 368.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-19.0 * scale[0], -23.0 * scale[1])
    Lineto_r(23.0 * scale[0], 19.0 * scale[1])
    Curveto_r(21.0 * scale[0], 18.0 * scale[1], 27.0 * scale[0],
              26.0 * scale[1], 19.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              10.0 * scale[1], -23.0 * scale[0], -22.0 * scale[1])
    te.end_fill()
    Moveto(163.0 * scale[0], 233.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-84.0 * scale[0], -119.0 * scale[1], -86.0 * scale[0], -
              123.0 * scale[1], -75.0 * scale[0], -123.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 23.0 * scale[0],
              21.0 * scale[1], 42.0 * scale[0], 47.0 * scale[1])
    Curveto_r(102.0 * scale[0], 144.0 * scale[1], 121.0 * scale[0],
              173.0 * scale[1], 112.0 * scale[0], 173.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -41.0 * scale[0], -
              44.0 * scale[1], -79.0 * scale[0], -97.0 * scale[1])
    te.end_fill()
    Moveto(250.0 * scale[0], 292.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              15.0 * scale[1], 15.0 * scale[0], -22.0 * scale[1])
    Curveto_r(9.0 * scale[0], -8.0 * scale[1], 15.0 * scale[0], -
              8.0 * scale[1], 15.0 * scale[0], -2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 8.0 * scale[0],
              13.0 * scale[1], 18.0 * scale[0], 16.0 * scale[1])
    Curveto_r(13.0 * scale[0], 4.0 * scale[1], 13.0 * scale[0],
              4.0 * scale[1], -3.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -1.0 * scale[1], -26.0 * scale[0],
              2.0 * scale[1], -32.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 5.0 * scale[1], -13.0 * scale[0],
              4.0 * scale[1], -13.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(585.0 * scale[0], 279.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0], -
              12.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 17.0 * scale[1], 1.0 * scale[0],
              20.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(305.0 * scale[0], 230.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(10.0 * scale[0], -11.0 * scale[1], 20.0 * scale[0], -
              20.0 * scale[1], 23.0 * scale[0], -20.0 * scale[1])
    Curveto_r(3.0 * scale[0], 0.0 * scale[1], -3.0 * scale[0],
              9.0 * scale[1], -13.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 11.0 * scale[1], -20.0 * scale[0],
              20.0 * scale[1], -23.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], 3.0 * scale[0], -
              9.0 * scale[1], 13.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(572.0 * scale[0], 215.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(216.0 * scale[0], 199.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -55.0 * scale[1], -9.0 *
              scale[0], -60.0 * scale[1], 22.0 * scale[0], -53.0 * scale[1])
    Curveto_r(38.0 * scale[0], 9.0 * scale[1], 45.0 * scale[0],
              19.0 * scale[1], 26.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 12.0 * scale[1], -17.0 * scale[0],
              12.0 * scale[1], -12.0 * scale[0], -3.0 * scale[1])
    Curveto_r(5.0 * scale[0], -11.0 * scale[1], 0.0 * scale[0], -
              18.0 * scale[1], -13.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -3.0 * scale[1], -19.0 *
              scale[0], -1.0 * scale[1], -19.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 5.0 * scale[0],
              9.0 * scale[1], 10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              5.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -6.0 * scale[0],
              7.0 * scale[1], -12.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -4.0 * scale[1], -6.0 *
              scale[0], -1.0 * scale[1], 3.0 * scale[0], 7.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 14.0 * scale[0],
              19.0 * scale[1], 12.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 22.0 * scale[1], -20.0 * scale[0],
              13.0 * scale[1], -27.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(365.0 * scale[0], 178.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(31.0 * scale[0], -43.0 * scale[1], 32.0 * scale[0], -
              44.0 * scale[1], 32.0 * scale[0], -23.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -2.0 * scale[0],
              13.0 * scale[1], -5.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -3.0 * scale[1], -15.0 * scale[0],
              7.0 * scale[1], -29.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 25.0 * scale[1], -22.0 * scale[0],
              24.0 * scale[1], 2.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(441.0 * scale[0], 178.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -9.0 * scale[1], -9.0 * scale[0], -
              22.0 * scale[1], -18.0 * scale[0], -27.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -6.0 * scale[1], -13.0 *
              scale[0], -11.0 * scale[1], -7.0 * scale[0], -11.0 * scale[1])
    Curveto_r(17.0 * scale[0], 0.0 * scale[1], 37.0 * scale[0],
              27.0 * scale[1], 31.0 * scale[0], 42.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 8.0 * scale[1], -6.0 * scale[0],
              7.0 * scale[1], -6.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(540.0 * scale[0], 138.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -19.0 * scale[1], -36.0 *
              scale[0], -29.0 * scale[1], -57.0 * scale[0], -31.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -1.0 * scale[1], -29.0 *
              scale[0], -5.0 * scale[1], -25.0 * scale[0], -8.0 * scale[1])
    Curveto_r(15.0 * scale[0], -15.0 * scale[1], 68.0 * scale[0],
              5.0 * scale[1], 91.0 * scale[0], 33.0 * scale[1])
    Curveto_r(31.0 * scale[0], 38.0 * scale[1], 23.0 * scale[0],
              43.0 * scale[1], -9.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(416.0 * scale[0], 108.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 10.0 * scale[0], -
              6.0 * scale[1], 15.0 * scale[0], -3.0 * scale[1])
    Curveto_r(13.0 * scale[0], 9.0 * scale[1], 11.0 * scale[0],
              12.0 * scale[1], -6.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -9.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(32.0 * scale[0], 50.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-48.0 * scale[0], -74.0 * scale[1], -28.0 *
              scale[0], -66.0 * scale[1], 31.0 * scale[0], 13.0 * scale[1])
    Curveto_r(17.0 * scale[0], 22.0 * scale[1], 23.0 * scale[0],
              37.0 * scale[1], 15.0 * scale[0], 37.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -28.0 * scale[0], -
              23.0 * scale[1], -46.0 * scale[0], -50.0 * scale[1])
    te.penup()
