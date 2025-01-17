import turtle as te
from helper import *


def perroquet_male(x, y, scale):
    te.penup()
    te.color('#b27d37')
    te.end_fill()
    Moveto(277.0 * scale[0], 1452.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-20.0 * scale[0], -2.0 * scale[1], -35.0 *
              scale[0], -7.0 * scale[1], -32.0 * scale[0], -11.0 * scale[1])
    Curveto_r(2.0 * scale[0], -5.0 * scale[1], -18.0 * scale[0], -
              11.0 * scale[1], -46.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-31.0 * scale[0], -4.0 * scale[1], -47.0 * scale[0], -
              11.0 * scale[1], -43.0 * scale[0], -17.0 * scale[1])
    Curveto_r(3.0 * scale[0], -6.0 * scale[1], 15.0 * scale[0], -
              9.0 * scale[1], 25.0 * scale[0], -6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 3.0 * scale[1], 19.0 * scale[0],
              1.0 * scale[1], 19.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 6.0 * scale[0], -
              9.0 * scale[1], 13.0 * scale[0], -8.0 * scale[1])
    Curveto_r(6.0 * scale[0], 1.0 * scale[1], 28.0 * scale[0],
              1.0 * scale[1], 47.0 * scale[0], -1.0 * scale[1])
    Curveto_r(28.0 * scale[0], -1.0 * scale[1], 31.0 *
              scale[0], -3.0 * scale[1], 15.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -7.0 * scale[1], -17.0 *
              scale[0], -9.0 * scale[1], 10.0 * scale[0], -24.0 * scale[1])
    Lineto_r(30.0 * scale[0], -16.0 * scale[1])
    Lineto_r(-29.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-28.0 * scale[0], 0.0 * scale[1], -29.0 * scale[0], -
              1.0 * scale[1], -10.0 * scale[0], -15.0 * scale[1])
    Curveto_r(11.0 * scale[0], -8.0 * scale[1], 14.0 * scale[0], -
              15.0 * scale[1], 7.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -13.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 31.0 * scale[0], -
              10.0 * scale[1], 73.0 * scale[0], -11.0 * scale[1])
    Curveto_r(81.0 * scale[0], -1.0 * scale[1], 80.0 * scale[0], -
              6.0 * scale[1], -3.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-47.0 * scale[0], -3.0 * scale[1], -55.0 *
              scale[0], -6.0 * scale[1], -55.0 * scale[0], -23.0 * scale[1])
    Curveto_r(0.0 * scale[0], -15.0 * scale[1], 11.0 * scale[0], -
              22.0 * scale[1], 60.0 * scale[0], -32.0 * scale[1])
    Curveto_r(33.0 * scale[0], -7.0 * scale[1], 71.0 * scale[0], -
              12.0 * scale[1], 84.0 * scale[0], -13.0 * scale[1])
    Curveto_r(23.0 * scale[0], 0.0 * scale[1], 23.0 * scale[0],
              1.0 * scale[1], 7.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 16.0 * scale[1], -15.0 * scale[0],
              19.0 * scale[1], -1.0 * scale[0], 31.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 14.0 * scale[0],
              19.0 * scale[1], 11.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 7.0 * scale[1], 0.0 * scale[0],
              13.0 * scale[1], 7.0 * scale[0], 13.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 6.0 * scale[0],
              4.0 * scale[1], -3.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 7.0 * scale[1], -11.0 * scale[0],
              10.0 * scale[1], -2.0 * scale[0], 10.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              5.0 * scale[1], 6.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], -6.0 * scale[0],
              28.0 * scale[1], -6.0 * scale[0], 49.0 * scale[1])
    Curveto_r(3.0 * scale[0], 63.0 * scale[1], -42.0 * scale[0],
              81.0 * scale[1], -171.0 * scale[0], 71.0 * scale[1])
    te.end_fill()
    Moveto_r(146.0 * scale[0], -129.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              5.0 * scale[1], 12.0 * scale[0], 5.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(12.0 * scale[0], -43.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              10.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0],
              5.0 * scale[1], -11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              10.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0], -
              4.0 * scale[1], 11.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(450.0 * scale[0], 1444.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 8.0 * scale[0], -10.0 * scale[1])
    Curveto_r(4.0 * scale[0], 2.0 * scale[1], 22.0 * scale[0], -
              2.0 * scale[1], 39.0 * scale[0], -11.0 * scale[1])
    Curveto_r(22.0 * scale[0], -10.0 * scale[1], 30.0 * scale[0], -
              21.0 * scale[1], 28.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -12.0 * scale[1], 4.0 * scale[0], -
              21.0 * scale[1], 16.0 * scale[0], -25.0 * scale[1])
    Curveto_r(21.0 * scale[0], -7.0 * scale[1], 39.0 * scale[0],
              1.0 * scale[1], 39.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              7.0 * scale[1], -12.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -4.0 * scale[1], -8.0 *
              scale[0], -3.0 * scale[1], -4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(4.0 * scale[0], 7.0 * scale[1], 16.0 * scale[0],
              12.0 * scale[1], 26.0 * scale[0], 12.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 24.0 * scale[0],
              10.0 * scale[1], 31.0 * scale[0], 21.0 * scale[1])
    Curveto_r(16.0 * scale[0], 31.0 * scale[1], -2.0 * scale[0],
              39.0 * scale[1], -93.0 * scale[0], 39.0 * scale[1])
    Curveto_r(-64.0 * scale[0], 0.0 * scale[1], -78.0 * scale[0], -
              3.0 * scale[1], -78.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(648.0 * scale[0], 1442.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -13.0 * scale[1], -10.0 *
              scale[0], -15.0 * scale[1], 6.0 * scale[0], -9.0 * scale[1])
    Curveto_r(10.0 * scale[0], 4.0 * scale[1], 25.0 * scale[0],
              2.0 * scale[1], 33.0 * scale[0], -5.0 * scale[1])
    Curveto_r(8.0 * scale[0], -7.0 * scale[1], 40.0 * scale[0], -
              17.0 * scale[1], 71.0 * scale[0], -24.0 * scale[1])
    Curveto_r(32.0 * scale[0], -7.0 * scale[1], 45.0 * scale[0], -
              13.0 * scale[1], 31.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -1.0 * scale[1], -47.0 * scale[0],
              5.0 * scale[1], -72.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-26.0 * scale[0], 8.0 * scale[1], -49.0 * scale[0],
              11.0 * scale[1], -51.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -4.0 * scale[1], -3.0 * scale[0], -
              24.0 * scale[1], -2.0 * scale[0], -44.0 * scale[1])
    Curveto_r(1.0 * scale[0], -31.0 * scale[1], -1.0 * scale[0], -
              35.0 * scale[1], -15.0 * scale[0], -27.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 7.0 * scale[1], -16.0 * scale[0],
              5.0 * scale[1], -12.0 * scale[0], -11.0 * scale[1])
    Curveto_r(3.0 * scale[0], -11.0 * scale[1], 9.0 * scale[0], -
              17.0 * scale[1], 14.0 * scale[0], -15.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], 8.0 * scale[0], -
              3.0 * scale[1], 8.0 * scale[0], -12.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 3.0 * scale[0], -
              32.0 * scale[1], 7.0 * scale[0], -50.0 * scale[1])
    Curveto_r(4.0 * scale[0], -23.0 * scale[1], 1.0 * scale[0], -
              37.0 * scale[1], -10.0 * scale[0], -48.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -9.0 * scale[1], -16.0 * scale[0], -
              25.0 * scale[1], -16.0 * scale[0], -35.0 * scale[1])
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], -25.0 * scale[0], -
              34.0 * scale[1], -41.0 * scale[0], -24.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0],
              1.0 * scale[1], -9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -64.0 * scale[0], -
              9.0 * scale[1], -80.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 1.0 * scale[1], -8.0 * scale[0],
              2.0 * scale[1], -12.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -8.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -9.0 * scale[0],
              11.0 * scale[1], -20.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 4.0 * scale[1], -18.0 * scale[0],
              10.0 * scale[1], -13.0 * scale[0], 24.0 * scale[1])
    Curveto_r(3.0 * scale[0], 10.0 * scale[1], 3.0 * scale[0],
              15.0 * scale[1], -1.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -4.0 * scale[1], -39.0 * scale[0],
              0.0 * scale[1], -79.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-91.0 * scale[0], 18.0 * scale[1], -104.0 * scale[0],
              17.0 * scale[1], -111.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -9.0 * scale[1], 0.0 * scale[0], -
              15.0 * scale[1], 10.0 * scale[0], -15.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              5.0 * scale[1], 8.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 7.0 * scale[1], -3.0 * scale[0],
              8.0 * scale[1], 5.0 * scale[0], 4.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 9.0 * scale[0], -
              11.0 * scale[1], 6.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 18.0 * scale[0], -
              16.0 * scale[1], 47.0 * scale[0], -25.0 * scale[1])
    Curveto_r(55.0 * scale[0], -16.0 * scale[1], 93.0 * scale[0], -
              35.0 * scale[1], 71.0 * scale[0], -35.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -22.0 * scale[0],
              4.0 * scale[1], -35.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-40.0 * scale[0], 17.0 * scale[1], -145.0 * scale[0],
              38.0 * scale[1], -157.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -4.0 * scale[1], 19.0 * scale[0], -
              19.0 * scale[1], 56.0 * scale[0], -33.0 * scale[1])
    Curveto_r(64.0 * scale[0], -25.0 * scale[1], 79.0 * scale[0], -
              26.0 * scale[1], 268.0 * scale[0], -28.0 * scale[1])
    Curveto_r(110.0 * scale[0], -1.0 * scale[1], 214.0 *
              scale[0], -2.0 * scale[1], 230.0 * scale[0], -3.0 * scale[1])
    Curveto_r(19.0 * scale[0], -1.0 * scale[1], 29.0 * scale[0],
              2.0 * scale[1], 28.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 8.0 * scale[1], 9.0 * scale[0],
              12.0 * scale[1], 31.0 * scale[0], 12.0 * scale[1])
    Curveto_r(21.0 * scale[0], 0.0 * scale[1], 36.0 * scale[0],
              6.0 * scale[1], 39.0 * scale[0], 15.0 * scale[1])
    Curveto_r(7.0 * scale[0], 17.0 * scale[1], -9.0 * scale[0],
              30.0 * scale[1], -18.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -12.0 * scale[0], -
              10.0 * scale[1], -18.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0],
              4.0 * scale[1], 3.0 * scale[0], 10.0 * scale[1])
    Curveto_r(13.0 * scale[0], 8.0 * scale[1], 13.0 * scale[0],
              14.0 * scale[1], -4.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 37.0 * scale[1], -27.0 * scale[0],
              83.0 * scale[1], -14.0 * scale[0], 91.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], 8.0 * scale[0],
              0.0 * scale[1], 8.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], 3.0 * scale[0], -
              10.0 * scale[1], 6.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], 1.0 * scale[0],
              16.0 * scale[1], -6.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 14.0 * scale[1], -7.0 * scale[0],
              21.0 * scale[1], 0.0 * scale[0], 22.0 * scale[1])
    Curveto_r(5.0 * scale[0], 1.0 * scale[1], 14.0 * scale[0],
              2.0 * scale[1], 19.0 * scale[0], 3.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(5.0 * scale[0], 5.0 * scale[1], 3.0 * scale[0],
              6.0 * scale[1], -4.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -4.0 * scale[1], -13.0 *
              scale[0], -3.0 * scale[1], -13.0 * scale[0], 2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 10.0 * scale[0],
              14.0 * scale[1], 23.0 * scale[0], 20.0 * scale[1])
    Curveto_r(21.0 * scale[0], 10.0 * scale[1], 20.0 * scale[0],
              11.0 * scale[1], -13.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-27.0 * scale[0], 2.0 * scale[1], -22.0 * scale[0],
              4.0 * scale[1], 20.0 * scale[0], 8.0 * scale[1])
    Lineto_r(55.0 * scale[0], 6.0 * scale[1])
    Lineto_r(-85.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-104.0 * scale[0], 33.0 * scale[1], -184.0 * scale[0],
              41.0 * scale[1], -202.0 * scale[0], 19.0 * scale[1])
    te.end_fill()
    Moveto_r(-241.0 * scale[0], -268.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 17.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(408.0 * scale[0], -14.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], -12.0 * scale[0], -
              9.0 * scale[1], -42.0 * scale[0], -9.0 * scale[1])
    Lineto_r(-48.0 * scale[0], 2.0 * scale[1])
    Lineto_r(40.0 * scale[0], 7.0 * scale[1])
    Curveto_r(22.0 * scale[0], 4.0 * scale[1], 41.0 * scale[0],
              8.0 * scale[1], 42.0 * scale[0], 9.0 * scale[1])
    Curveto_r(1.0 * scale[0], 0.0 * scale[1], 5.0 * scale[0], -
              3.0 * scale[1], 8.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto_r(-132.0 * scale[0], -7.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              5.0 * scale[1], 12.0 * scale[0], 5.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(880.0 * scale[0], 1140.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              10.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              5.0 * scale[1], 9.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -10.0 * scale[0],
              10.0 * scale[1], -16.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              4.0 * scale[1], -9.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(220.0 * scale[0], 1126.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 7.0 * scale[0], -
              6.0 * scale[1], 15.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 15.0 *
              scale[0], -1.0 * scale[1], 15.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -7.0 * scale[0],
              10.0 * scale[1], -15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              2.0 * scale[1], -15.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(116.0 * scale[0], 922.0 * scale[1], x, y)
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
    Moveto(140.0 * scale[0], 896.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(53.0 * scale[0], 730.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -36.0 * scale[1], 2.0 * scale[0], -
              50.0 * scale[1], 4.0 * scale[0], -32.0 * scale[1])
    Curveto_r(2.0 * scale[0], 17.0 * scale[1], 2.0 * scale[0],
              47.0 * scale[1], 0.0 * scale[0], 65.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 17.0 * scale[1], -4.0 * scale[0],
              3.0 * scale[1], -4.0 * scale[0], -33.0 * scale[1])
    te.end_fill()
    Moveto(500.0 * scale[0], 756.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(360.0 * scale[0], 728.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], -9.0 * scale[0], -
              22.0 * scale[1], -19.0 * scale[0], -29.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -8.0 * scale[1], -22.0 * scale[0], -
              25.0 * scale[1], -26.0 * scale[0], -39.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -22.0 * scale[1], -4.0 *
              scale[0], -21.0 * scale[1], 15.0 * scale[0], 8.0 * scale[1])
    Curveto_r(12.0 * scale[0], 17.0 * scale[1], 28.0 * scale[0],
              32.0 * scale[1], 35.0 * scale[0], 32.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              7.0 * scale[1], 11.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 21.0 * scale[1], -16.0 * scale[0],
              31.0 * scale[1], -16.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(731.0 * scale[0], 724.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(77.0 * scale[0], 699.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(80.0 * scale[0], 660.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              10.0 * scale[1], 15.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -7.0 * scale[0],
              10.0 * scale[1], -15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              4.0 * scale[1], -15.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(134.0 * scale[0], 663.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], -2.0 * scale[0], -
              12.0 * scale[1], -12.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -13.0 * scale[1], -16.0 *
              scale[0], -13.0 * scale[1], 1.0 * scale[0], -14.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0], -
              7.0 * scale[1], 17.0 * scale[0], -15.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 9.0 * scale[0], -
              15.0 * scale[1], 24.0 * scale[0], -15.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 26.0 * scale[0], -
              4.0 * scale[1], 28.0 * scale[0], -9.0 * scale[1])
    Curveto_r(2.0 * scale[0], -5.0 * scale[1], 12.0 * scale[0], -
              11.0 * scale[1], 23.0 * scale[0], -13.0 * scale[1])
    Curveto_r(11.0 * scale[0], -1.0 * scale[1], 26.0 * scale[0], -
              11.0 * scale[1], 33.0 * scale[0], -20.0 * scale[1])
    Curveto_r(7.0 * scale[0], -10.0 * scale[1], 20.0 * scale[0], -
              18.0 * scale[1], 28.0 * scale[0], -18.0 * scale[1])
    Curveto_r(22.0 * scale[0], 0.0 * scale[1], -26.0 * scale[0],
              69.0 * scale[1], -53.0 * scale[0], 76.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 4.0 * scale[1], -23.0 * scale[0],
              10.0 * scale[1], -23.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -10.0 * scale[0],
              6.0 * scale[1], -22.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -4.0 * scale[1], -20.0 *
              scale[0], -2.0 * scale[1], -15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(4.0 * scale[0], 11.0 * scale[1], -1.0 * scale[0],
              18.0 * scale[1], -15.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 3.0 * scale[1], -17.0 * scale[0],
              3.0 * scale[1], -14.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(687.0 * scale[0], 635.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -32.0 * scale[1], 11.0 * scale[0], -
              41.0 * scale[1], 17.0 * scale[0], -34.0 * scale[1])
    Curveto_r(2.0 * scale[0], 2.0 * scale[1], -2.0 * scale[0],
              18.0 * scale[1], -10.0 * scale[0], 34.0 * scale[1])
    Lineto_r(-13.0 * scale[0], 30.0 * scale[1])
    Lineto_r(6.0 * scale[0], -30.0 * scale[1])
    te.end_fill()
    Moveto(541.0 * scale[0], 644.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -18.0 * scale[1], -63.0 * scale[0], -
              84.0 * scale[1], -77.0 * scale[0], -84.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0], -
              8.0 * scale[1], -14.0 * scale[0], -18.0 * scale[1])
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], 13.0 *
              scale[0], -6.0 * scale[1], 51.0 * scale[0], 30.0 * scale[1])
    Curveto_r(34.0 * scale[0], 32.0 * scale[1], 49.0 * scale[0],
              53.0 * scale[1], 46.0 * scale[0], 65.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 10.0 * scale[1], -5.0 * scale[0],
              13.0 * scale[1], -6.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(301.0 * scale[0], 594.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(436.0 * scale[0], 597.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0], -
              15.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 0.0 * scale[0],
              11.0 * scale[1], -7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              8.0 * scale[1], -5.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(973.0 * scale[0], 564.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-25.0 * scale[0], -28.0 * scale[1], -28.0 *
              scale[0], -40.0 * scale[1], -13.0 * scale[0], -49.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 12.0 * scale[1], 0.0 * scale[0],
              16.0 * scale[1], 20.0 * scale[0], 16.0 * scale[1])
    Curveto_r(16.0 * scale[0], 0.0 * scale[1], 26.0 * scale[0],
              6.0 * scale[1], 26.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 5.0 * scale[0],
              15.0 * scale[1], 11.0 * scale[0], 15.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              5.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 17.0 * scale[1], -29.0 * scale[0],
              11.0 * scale[1], -52.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(351.0 * scale[0], 527.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -40.0 * scale[1], -4.0 * scale[0], -
              56.0 * scale[1], -12.0 * scale[0], -51.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -10.0 * scale[0],
              1.0 * scale[1], -7.0 * scale[0], -6.0 * scale[1])
    Curveto_r(9.0 * scale[0], -27.0 * scale[1], 28.0 *
              scale[0], -22.0 * scale[1], 29.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 28.0 * scale[1], 0.0 * scale[0],
              28.0 * scale[1], 10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(6.0 * scale[0], -15.0 * scale[1], 14.0 * scale[0], -
              21.0 * scale[1], 25.0 * scale[0], -17.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 13.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              14.0 * scale[1], 9.0 * scale[0], -21.0 * scale[1])
    Curveto_r(12.0 * scale[0], -10.0 * scale[1], 15.0 *
              scale[0], -9.0 * scale[1], 15.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], 3.0 * scale[0],
              27.0 * scale[1], 6.0 * scale[0], 35.0 * scale[1])
    Curveto_r(4.0 * scale[0], 11.0 * scale[1], -4.0 * scale[0],
              17.0 * scale[1], -25.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-35.0 * scale[0], 7.0 * scale[1], -47.0 * scale[0],
              20.0 * scale[1], -54.0 * scale[0], 55.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 14.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -6.0 * scale[0], -33.0 * scale[1])
    te.end_fill()
    Moveto(906.0 * scale[0], 506.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -20.0 * scale[1], -13.0 *
              scale[0], -24.0 * scale[1], -2.0 * scale[0], -20.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 17.0 * scale[0],
              13.0 * scale[1], 20.0 * scale[0], 21.0 * scale[1])
    Curveto_r(10.0 * scale[0], 26.0 * scale[1], 0.0 * scale[0],
              25.0 * scale[1], -18.0 * scale[0], -1.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#c24221')
    te.end_fill()
    Moveto(973.0 * scale[0], 1053.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -2.0 * scale[1], -34.0 * scale[0], -
              19.0 * scale[1], -49.0 * scale[0], -36.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -25.0 * scale[1], -25.0 *
              scale[0], -27.0 * scale[1], -20.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 18.0 * scale[1], 4.0 * scale[0],
              21.0 * scale[1], -15.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -4.0 * scale[1], -43.0 * scale[0], -
              25.0 * scale[1], -67.0 * scale[0], -48.0 * scale[1])
    Curveto_r(-33.0 * scale[0], -31.0 * scale[1], -44.0 *
              scale[0], -50.0 * scale[1], -44.0 * scale[0], -71.0 * scale[1])
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], -5.0 * scale[0], -
              32.0 * scale[1], -11.0 * scale[0], -35.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -4.0 * scale[1], -9.0 * scale[0], -
              34.0 * scale[1], -8.0 * scale[0], -67.0 * scale[1])
    Curveto_r(2.0 * scale[0], -99.0 * scale[1], -15.0 * scale[0], -
              191.0 * scale[1], -40.0 * scale[0], -218.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -13.0 * scale[1], -25.0 *
              scale[0], -21.0 * scale[1], -28.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              9.0 * scale[1], 9.0 * scale[0], 14.0 * scale[1])
    Curveto_r(13.0 * scale[0], 8.0 * scale[1], 12.0 * scale[0],
              12.0 * scale[1], -6.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 8.0 * scale[1], -27.0 * scale[0],
              36.0 * scale[1], -34.0 * scale[0], 61.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 76.0 * scale[1], -97.0 * scale[0],
              135.0 * scale[1], -171.0 * scale[0], 133.0 * scale[1])
    Curveto_r(-43.0 * scale[0], -1.0 * scale[1], -119.0 * scale[0], -
              33.0 * scale[1], -119.0 * scale[0], -50.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 2.0 *
              scale[0], -11.0 * scale[1], 8.0 * scale[0], 0.0 * scale[1])
    Curveto_r(11.0 * scale[0], 16.0 * scale[1], 73.0 * scale[0],
              27.0 * scale[1], 107.0 * scale[0], 18.0 * scale[1])
    Curveto_r(33.0 * scale[0], -9.0 * scale[1], 65.0 * scale[0], -
              61.0 * scale[1], 65.0 * scale[0], -109.0 * scale[1])
    Curveto_r(0.0 * scale[0], -33.0 * scale[1], -7.0 * scale[0], -
              45.0 * scale[1], -54.0 * scale[0], -91.0 * scale[1])
    Curveto_r(-71.0 * scale[0], -69.0 * scale[1], -78.0 * scale[0], -
              101.0 * scale[1], -41.0 * scale[0], -194.0 * scale[1])
    Curveto_r(14.0 * scale[0], -37.0 * scale[1], 36.0 * scale[0], -
              85.0 * scale[1], 48.0 * scale[0], -107.0 * scale[1])
    Curveto_r(11.0 * scale[0], -22.0 * scale[1], 26.0 * scale[0], -
              50.0 * scale[1], 31.0 * scale[0], -62.0 * scale[1])
    Curveto_r(6.0 * scale[0], -13.0 * scale[1], 20.0 * scale[0], -
              23.0 * scale[1], 32.0 * scale[0], -23.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 35.0 * scale[0], -
              7.0 * scale[1], 52.0 * scale[0], -15.0 * scale[1])
    Curveto_r(27.0 * scale[0], -14.0 * scale[1], 33.0 *
              scale[0], -14.0 * scale[1], 66.0 * scale[0], 2.0 * scale[1])
    Curveto_r(20.0 * scale[0], 9.0 * scale[1], 36.0 * scale[0],
              20.0 * scale[1], 36.0 * scale[0], 24.0 * scale[1])
    Curveto_r(0.0 * scale[0], 15.0 * scale[1], 52.0 * scale[0],
              69.0 * scale[1], 61.0 * scale[0], 63.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 10.0 * scale[0],
              3.0 * scale[1], 10.0 * scale[0], 13.0 * scale[1])
    Curveto_r(1.0 * scale[0], 10.0 * scale[1], 5.0 * scale[0],
              5.0 * scale[1], 10.0 * scale[0], -12.0 * scale[1])
    Curveto_r(7.0 * scale[0], -26.0 * scale[1], 8.0 * scale[0], -
              25.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 135.0 * scale[1], -17.0 * scale[0],
              185.0 * scale[1], -5.0 * scale[0], 200.0 * scale[1])
    Curveto_r(7.0 * scale[0], 9.0 * scale[1], 19.0 * scale[0],
              14.0 * scale[1], 26.0 * scale[0], 11.0 * scale[1])
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 20.0 * scale[0],
              2.0 * scale[1], 31.0 * scale[0], 9.0 * scale[1])
    Curveto_r(10.0 * scale[0], 8.0 * scale[1], 24.0 * scale[0],
              15.0 * scale[1], 32.0 * scale[0], 15.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0],
              8.0 * scale[1], 27.0 * scale[0], 18.0 * scale[1])
    Curveto_r(8.0 * scale[0], 10.0 * scale[1], 13.0 * scale[0],
              12.0 * scale[1], 14.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], -18.0 * scale[1], 20.0 *
              scale[0], -16.0 * scale[1], 20.0 * scale[0], 1.0 * scale[1])
    Curveto_r(0.0 * scale[0], 22.0 * scale[1], 47.0 * scale[0],
              69.0 * scale[1], 63.0 * scale[0], 63.0 * scale[1])
    Curveto_r(10.0 * scale[0], -4.0 * scale[1], 13.0 * scale[0],
              38.0 * scale[1], 12.0 * scale[0], 222.0 * scale[1])
    Curveto_r(0.0 * scale[0], 208.0 * scale[1], -4.0 * scale[0],
              253.0 * scale[1], -23.0 * scale[0], 250.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -1.0 * scale[1], -17.0 *
              scale[0], -4.0 * scale[1], -29.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(185.0 * scale[0], 803.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -8.0 * scale[1], -18.0 * scale[0], -
              16.0 * scale[1], -35.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -4.0 * scale[1], -27.0 * scale[0], -
              10.0 * scale[1], -24.0 * scale[0], -15.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 0.0 * scale[0], -
              9.0 * scale[1], -5.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0],
              7.0 * scale[1], -11.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 18.0 * scale[1], -14.0 * scale[0],
              20.0 * scale[1], -27.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -17.0 * scale[1], -9.0 *
              scale[0], -71.0 * scale[1], 5.0 * scale[0], -76.0 * scale[1])
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 9.0 * scale[0], -
              9.0 * scale[1], 6.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -7.0 * scale[1], 7.0 * scale[0], -
              18.0 * scale[1], 21.0 * scale[0], -24.0 * scale[1])
    Curveto_r(15.0 * scale[0], -7.0 * scale[1], 24.0 *
              scale[0], -8.0 * scale[1], 21.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], 3.0 * scale[0],
              7.0 * scale[1], 13.0 * scale[0], 4.0 * scale[1])
    Curveto_r(13.0 * scale[0], -3.0 * scale[1], 18.0 * scale[0], -
              10.0 * scale[1], 14.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -12.0 * scale[1], -1.0 * scale[0], -
              14.0 * scale[1], 15.0 * scale[0], -10.0 * scale[1])
    Curveto_r(12.0 * scale[0], 4.0 * scale[1], 22.0 * scale[0],
              3.0 * scale[1], 22.0 * scale[0], -2.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 10.0 * scale[0], -
              10.0 * scale[1], 23.0 * scale[0], -14.0 * scale[1])
    Curveto_r(12.0 * scale[0], -3.0 * scale[1], 33.0 * scale[0], -
              22.0 * scale[1], 45.0 * scale[0], -42.0 * scale[1])
    Curveto_r(31.0 * scale[0], -48.0 * scale[1], 47.0 *
              scale[0], -33.0 * scale[1], 31.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 42.0 * scale[1], -11.0 * scale[0],
              47.0 * scale[1], 9.0 * scale[0], 68.0 * scale[1])
    Curveto_r(12.0 * scale[0], 13.0 * scale[1], 22.0 * scale[0],
              32.0 * scale[1], 22.0 * scale[0], 43.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], 5.0 * scale[0],
              27.0 * scale[1], 10.0 * scale[0], 38.0 * scale[1])
    Curveto_r(9.0 * scale[0], 15.0 * scale[1], 7.0 * scale[0],
              19.0 * scale[1], -5.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -19.0 * scale[0],
              10.0 * scale[1], -24.0 * scale[0], 22.0 * scale[1])
    Lineto_r(-8.0 * scale[0], 23.0 * scale[1])
    Lineto_r(-7.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -25.0 * scale[1], -44.0 *
              scale[0], -30.0 * scale[1], -52.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 8.0 * scale[1], -11.0 * scale[0],
              12.0 * scale[1], -17.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -4.0 * scale[1], -8.0 * scale[0],
              0.0 * scale[1], -4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(4.0 * scale[0], 11.0 * scale[1], 0.0 * scale[0],
              15.0 * scale[1], -13.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -1.0 * scale[1], -22.0 *
              scale[0], -7.0 * scale[1], -25.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto_r(-26.0 * scale[0], -85.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -3.0 * scale[1], -8.0 * scale[0], -
              4.0 * scale[1], -18.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 4.0 * scale[1], -18.0 * scale[0],
              8.0 * scale[1], -8.0 * scale[0], 24.0 * scale[1])
    Curveto_r(11.0 * scale[0], 18.0 * scale[1], 12.0 * scale[0],
              18.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(3.0 * scale[0], -9.0 * scale[1], 7.0 * scale[0], -
              20.0 * scale[1], 7.0 * scale[0], -24.0 * scale[1])
    te.end_fill()
    Moveto_r(81.0 * scale[0], -70.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -6.0 * scale[0], -
              5.0 * scale[1], -15.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 7.0 * scale[1], -15.0 * scale[0],
              14.0 * scale[1], -15.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 2.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 15.0 * scale[0], -2.0 * scale[1])
    Curveto_r(8.0 * scale[0], -4.0 * scale[1], 15.0 * scale[0], -
              11.0 * scale[1], 15.0 * scale[0], -16.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#1c1411')
    te.end_fill()
    Moveto(70.0 * scale[0], 1440.0 * scale[1], x, y)
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
    Moveto(945.0 * scale[0], 1455.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 27.0 * scale[0], -
              6.0 * scale[1], 48.0 * scale[0], -10.0 * scale[1])
    Curveto_r(31.0 * scale[0], -5.0 * scale[1], 37.0 * scale[0], -
              10.0 * scale[1], 37.0 * scale[0], -30.0 * scale[1])
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 5.0 * scale[0], -
              25.0 * scale[1], 10.0 * scale[0], -25.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              32.0 * scale[1], -4.0 * scale[0], 53.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 12.0 * scale[1], -26.0 * scale[0],
              17.0 * scale[1], -57.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 0.0 * scale[1], -39.0 *
              scale[0], -2.0 * scale[1], -34.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(4.0 * scale[0], 1060.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -179.0 * scale[1], 2.0 * scale[0], -
              252.0 * scale[1], 3.0 * scale[0], -162.0 * scale[1])
    Curveto_r(2.0 * scale[0], 89.0 * scale[1], 2.0 * scale[0],
              235.0 * scale[1], 0.0 * scale[0], 325.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 89.0 * scale[1], -3.0 * scale[0],
              16.0 * scale[1], -3.0 * scale[0], -163.0 * scale[1])
    te.end_fill()
    Moveto(62.0 * scale[0], 1148.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -48.0 * scale[1], 1.0 * scale[0], -
              56.0 * scale[1], 13.0 * scale[0], -52.0 * scale[1])
    Curveto_r(10.0 * scale[0], 4.0 * scale[1], 12.0 * scale[0],
              10.0 * scale[1], 6.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 6.0 * scale[1], -11.0 * scale[0],
              29.0 * scale[1], -14.0 * scale[0], 51.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 33.0 * scale[1], -4.0 * scale[0],
              30.0 * scale[1], -5.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(1028.0 * scale[0], 1135.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -30.0 * scale[1], 0.0 * scale[0], -
              55.0 * scale[1], 5.0 * scale[0], -55.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              25.0 * scale[1], 7.0 * scale[0], 55.0 * scale[1])
    Curveto_r(0.0 * scale[0], 71.0 * scale[1], -7.0 * scale[0],
              71.0 * scale[1], -12.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(423.0 * scale[0], 714.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -1.0 * scale[0], -
              20.0 * scale[1], 5.0 * scale[0], -26.0 * scale[1])
    Curveto_r(8.0 * scale[0], -8.0 * scale[1], 9.0 * scale[0], -
              4.0 * scale[1], 5.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 17.0 * scale[1], -2.0 * scale[0],
              21.0 * scale[1], 8.0 * scale[0], 18.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 13.0 * scale[0], -
              13.0 * scale[1], 13.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -9.0 * scale[1], 2.0 * scale[0], -
              16.0 * scale[1], 7.0 * scale[0], -16.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              11.0 * scale[1], 9.0 * scale[0], 25.0 * scale[1])
    Curveto_r(0.0 * scale[0], 18.0 * scale[1], -5.0 * scale[0],
              25.0 * scale[1], -20.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -23.0 * scale[0], -
              7.0 * scale[1], -27.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(367.0 * scale[0], 653.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -27.0 * scale[1], -3.0 * scale[0], -
              50.0 * scale[1], -1.0 * scale[0], -52.0 * scale[1])
    Curveto_r(9.0 * scale[0], -9.0 * scale[1], 44.0 * scale[0],
              34.0 * scale[1], 44.0 * scale[0], 54.0 * scale[1])
    Curveto_r(0.0 * scale[0], 20.0 * scale[1], -17.0 * scale[0],
              45.0 * scale[1], -31.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              21.0 * scale[1], -12.0 * scale[0], -47.0 * scale[1])
    te.end_fill()
    Moveto(63.0 * scale[0], 600.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -25.0 * scale[1], 2.0 * scale[0], -
              35.0 * scale[1], 4.0 * scale[0], -22.0 * scale[1])
    Curveto_r(2.0 * scale[0], 12.0 * scale[1], 2.0 * scale[0],
              32.0 * scale[1], 0.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 12.0 * scale[1], -4.0 * scale[0],
              2.0 * scale[1], -4.0 * scale[0], -23.0 * scale[1])
    te.end_fill()
    Moveto(388.0 * scale[0], 597.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -13.0 * scale[1], -28.0 *
              scale[0], -27.0 * scale[1], -28.0 * scale[0], -33.0 * scale[1])
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 43.0 * scale[0], -
              54.0 * scale[1], 57.0 * scale[0], -54.0 * scale[1])
    Curveto_r(21.0 * scale[0], 0.0 * scale[1], 32.0 * scale[0],
              54.0 * scale[1], 16.0 * scale[0], 83.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 15.0 * scale[1], -15.0 * scale[0],
              27.0 * scale[1], -16.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -1.0 * scale[1], -14.0 * scale[0], -
              11.0 * scale[1], -29.0 * scale[0], -23.0 * scale[1])
    te.end_fill()
    Moveto(1025.0 * scale[0], 543.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -31.0 * scale[1], -11.0 *
              scale[0], -96.0 * scale[1], 3.0 * scale[0], -101.0 * scale[1])
    Curveto_r(9.0 * scale[0], -3.0 * scale[1], 12.0 * scale[0],
              13.0 * scale[1], 12.0 * scale[0], 57.0 * scale[1])
    Curveto_r(0.0 * scale[0], 64.0 * scale[1], -3.0 * scale[0],
              73.0 * scale[1], -15.0 * scale[0], 44.0 * scale[1])
    te.end_fill()
    Moveto(946.0 * scale[0], 435.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -8.0 * scale[1], 11.0 * scale[0], -
              15.0 * scale[1], 16.0 * scale[0], -15.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 5.0 * scale[0],
              6.0 * scale[1], -2.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 8.0 * scale[1], -14.0 * scale[0],
              15.0 * scale[1], -16.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -1.0 * scale[0], -
              7.0 * scale[1], 2.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(900.0 * scale[0], 436.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 7.0 * scale[0], -
              9.0 * scale[1], 15.0 * scale[0], -16.0 * scale[1])
    Curveto_r(9.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              8.0 * scale[1], 15.0 * scale[0], -2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -7.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -15.0 * scale[0],
              4.0 * scale[1], -15.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(108.0 * scale[0], 163.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 12.0 * scale[0], -
              9.0 * scale[1], 12.0 * scale[0], -15.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -7.0 * scale[0], -
              7.0 * scale[1], -16.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 3.0 * scale[1], -12.0 * scale[0],
              2.0 * scale[1], -9.0 * scale[0], -5.0 * scale[1])
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 13.0 * scale[0], -
              8.0 * scale[1], 19.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 3.0 * scale[1], 18.0 * scale[0], -
              4.0 * scale[1], 25.0 * scale[0], -15.0 * scale[1])
    Curveto_r(10.0 * scale[0], -16.0 * scale[1], 15.0 *
              scale[0], -17.0 * scale[1], 27.0 * scale[0], -7.0 * scale[1])
    Curveto_r(18.0 * scale[0], 14.0 * scale[1], 0.0 * scale[0],
              41.0 * scale[1], -22.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -3.0 * scale[1], -14.0 * scale[0],
              1.0 * scale[1], -14.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], -8.0 * scale[0],
              16.0 * scale[1], -17.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -13.0 *
              scale[0], -3.0 * scale[1], -5.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto_r(57.0 * scale[0], -33.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              10.0 * scale[1], -10.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0],
              5.0 * scale[1], -10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 8.0 * scale[0],
              10.0 * scale[1], 10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0], -
              4.0 * scale[1], 10.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(545.0 * scale[0], 153.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -3.0 * scale[1], -36.0 * scale[0], -
              10.0 * scale[1], -43.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -8.0 * scale[1], -16.0 *
              scale[0], -8.0 * scale[1], -24.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 7.0 * scale[1], -30.0 * scale[0],
              12.0 * scale[1], -52.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 0.0 * scale[1], -36.0 *
              scale[0], -3.0 * scale[1], -33.0 * scale[0], -7.0 * scale[1])
    Curveto_r(4.0 * scale[0], -3.0 * scale[1], 1.0 * scale[0], -
              11.0 * scale[1], -7.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -14.0 * scale[1], -30.0 *
              scale[0], -66.0 * scale[1], -16.0 * scale[0], -66.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              11.0 * scale[1], 10.0 * scale[0], 24.0 * scale[1])
    Curveto_r(0.0 * scale[0], 30.0 * scale[1], 3.0 * scale[0],
              32.0 * scale[1], 58.0 * scale[0], 41.0 * scale[1])
    Curveto_r(40.0 * scale[0], 6.0 * scale[1], 42.0 * scale[0],
              5.0 * scale[1], 42.0 * scale[0], -17.0 * scale[1])
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], -5.0 * scale[0], -
              29.0 * scale[1], -12.0 * scale[0], -36.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -9.0 * scale[1], 12.0 * scale[0], -
              12.0 * scale[1], 97.0 * scale[0], -12.0 * scale[1])
    Curveto_r(117.0 * scale[0], 0.0 * scale[1], 141.0 * scale[0],
              8.0 * scale[1], 32.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-43.0 * scale[0], 1.0 * scale[1], -67.0 * scale[0],
              6.0 * scale[1], -67.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 23.0 * scale[1], 27.0 * scale[0],
              48.0 * scale[1], 53.0 * scale[0], 48.0 * scale[1])
    Curveto_r(22.0 * scale[0], 0.0 * scale[1], 25.0 * scale[0],
              2.0 * scale[1], 16.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 8.0 * scale[1], -14.0 * scale[0],
              13.0 * scale[1], -18.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -1.0 * scale[1], -19.0 *
              scale[0], -4.0 * scale[1], -36.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto_r(-20.0 * scale[0], -45.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-15.0 * scale[0], -48.0 * scale[1], -43.0 *
              scale[0], -51.0 * scale[1], -31.0 * scale[0], -3.0 * scale[1])
    Curveto_r(4.0 * scale[0], 14.0 * scale[1], 13.0 * scale[0],
              25.0 * scale[1], 22.0 * scale[0], 25.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0], -
              6.0 * scale[1], 9.0 * scale[0], -22.0 * scale[1])
    te.end_fill()
    Moveto(411.0 * scale[0], 84.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(720.0 * scale[0], 60.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 14.0 * scale[0], -
              10.0 * scale[1], 30.0 * scale[0], -10.0 * scale[1])
    Curveto_r(17.0 * scale[0], 0.0 * scale[1], 30.0 * scale[0],
              5.0 * scale[1], 30.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -13.0 * scale[0],
              10.0 * scale[1], -30.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -30.0 * scale[0], -
              4.0 * scale[1], -30.0 * scale[0], -10.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#6f9c9d')
    te.end_fill()
    Moveto(1.0 * scale[0], 1444.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(464.0 * scale[0], 1390.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 5.0 * scale[0], -
              17.0 * scale[1], 12.0 * scale[0], -17.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0],
              8.0 * scale[1], 21.0 * scale[0], 17.0 * scale[1])
    Curveto_r(9.0 * scale[0], 13.0 * scale[1], 7.0 * scale[0],
              16.0 * scale[1], -11.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -22.0 * scale[0], -
              6.0 * scale[1], -22.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(626.0 * scale[0], 1403.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -11.0 * scale[1], -7.0 *
              scale[0], -25.0 * scale[1], 6.0 * scale[0], -17.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 9.0 * scale[0],
              2.0 * scale[1], 5.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -10.0 * scale[1], -2.0 *
              scale[0], -17.0 * scale[1], 3.0 * scale[0], -17.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              37.0 * scale[1], 1.0 * scale[0], 44.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 3.0 * scale[1], -11.0 * scale[0],
              3.0 * scale[1], -15.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(159.0 * scale[0], 1341.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-34.0 * scale[0], -34.0 * scale[1], -39.0 * scale[0], -
              83.0 * scale[1], -13.0 * scale[0], -120.0 * scale[1])
    Curveto_r(13.0 * scale[0], -19.0 * scale[1], 22.0 * scale[0], -
              22.0 * scale[1], 48.0 * scale[0], -17.0 * scale[1])
    Curveto_r(17.0 * scale[0], 4.0 * scale[1], 36.0 * scale[0],
              7.0 * scale[1], 41.0 * scale[0], 8.0 * scale[1])
    Curveto_r(6.0 * scale[0], 1.0 * scale[1], 11.0 * scale[0],
              8.0 * scale[1], 12.0 * scale[0], 17.0 * scale[1])
    Curveto_r(1.0 * scale[0], 9.0 * scale[1], 5.0 * scale[0],
              32.0 * scale[1], 7.0 * scale[0], 51.0 * scale[1])
    Lineto_r(6.0 * scale[0], 35.0 * scale[1])
    Lineto_r(-10.0 * scale[0], -32.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -35.0 * scale[1], -26.0 *
              scale[0], -46.0 * scale[1], -17.0 * scale[0], -13.0 * scale[1])
    Curveto_r(3.0 * scale[0], 11.0 * scale[1], 1.0 * scale[0],
              22.0 * scale[1], -3.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0], -
              7.0 * scale[1], -12.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -16.0 * scale[1], -12.0 * scale[0], -
              32.0 * scale[1], -25.0 * scale[0], -39.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -6.0 * scale[1], -20.0 * scale[0], -
              15.0 * scale[1], -15.0 * scale[0], -20.0 * scale[1])
    Curveto_r(4.0 * scale[0], -4.0 * scale[1], -1.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 8.0 * scale[1], -14.0 * scale[0],
              16.0 * scale[1], -9.0 * scale[0], 17.0 * scale[1])
    Curveto_r(5.0 * scale[0], 2.0 * scale[1], 8.0 * scale[0],
              16.0 * scale[1], 5.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 20.0 * scale[1], 3.0 * scale[0],
              35.0 * scale[1], 20.0 * scale[0], 51.0 * scale[1])
    Curveto_r(23.0 * scale[0], 22.0 * scale[1], 23.0 * scale[0],
              22.0 * scale[1], 1.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -6.0 * scale[1], -25.0 * scale[0], -
              24.0 * scale[1], -29.0 * scale[0], -39.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -46.0 * scale[1], -12.0 *
              scale[0], -48.0 * scale[1], -13.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 23.0 * scale[1], 7.0 * scale[0],
              40.0 * scale[1], 25.0 * scale[0], 57.0 * scale[1])
    Curveto_r(33.0 * scale[0], 30.0 * scale[1], 38.0 * scale[0],
              31.0 * scale[1], 64.0 * scale[0], 5.0 * scale[1])
    Curveto_r(11.0 * scale[0], -11.0 * scale[1], 20.0 * scale[0], -
              16.0 * scale[1], 20.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], -39.0 * scale[0],
              41.0 * scale[1], -53.0 * scale[0], 41.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -22.0 * scale[0], -
              13.0 * scale[1], -38.0 * scale[0], -29.0 * scale[1])
    te.end_fill()
    Moveto(895.0 * scale[0], 1344.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -9.0 * scale[1], -20.0 * scale[0], -
              27.0 * scale[1], -21.0 * scale[0], -51.0 * scale[1])
    Curveto_r(0.0 * scale[0], -20.0 * scale[1], -6.0 * scale[0], -
              39.0 * scale[1], -11.0 * scale[0], -40.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -2.0 * scale[1], -9.0 * scale[0], -
              13.0 * scale[1], -6.0 * scale[0], -24.0 * scale[1])
    Curveto_r(3.0 * scale[0], -11.0 * scale[1], 11.0 * scale[0], -
              18.0 * scale[1], 19.0 * scale[0], -15.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 11.0 * scale[0],
              0.0 * scale[1], 7.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -21.0 * scale[1], 39.0 *
              scale[0], -18.0 * scale[1], 67.0 * scale[0], 4.0 * scale[1])
    Curveto_r(14.0 * scale[0], 12.0 * scale[1], 23.0 * scale[0],
              32.0 * scale[1], 25.0 * scale[0], 62.0 * scale[1])
    Curveto_r(3.0 * scale[0], 32.0 * scale[1], 2.0 * scale[0],
              38.0 * scale[1], -3.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -25.0 * scale[1], -9.0 * scale[0], -
              25.0 * scale[1], -16.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 34.0 * scale[1], -31.0 * scale[0],
              46.0 * scale[1], -55.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-27.0 * scale[0], -14.0 * scale[1], -27.0 *
              scale[0], 1.0 * scale[1], 0.0 * scale[0], 18.0 * scale[1])
    Curveto_r(17.0 * scale[0], 11.0 * scale[1], 25.0 * scale[0],
              11.0 * scale[1], 45.0 * scale[0], -3.0 * scale[1])
    Curveto_r(13.0 * scale[0], -8.0 * scale[1], 24.0 * scale[0], -
              11.0 * scale[1], 24.0 * scale[0], -6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], -32.0 * scale[0],
              31.0 * scale[1], -47.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0], -
              7.0 * scale[1], -28.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto_r(51.0 * scale[0], -60.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(8.0 * scale[0], -20.0 * scale[1], 13.0 * scale[0], -
              39.0 * scale[1], 10.0 * scale[0], -42.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -6.0 * scale[0],
              0.0 * scale[1], -6.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -9.0 * scale[0],
              3.0 * scale[1], -20.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -24.0 * scale[1], -20.0 *
              scale[0], -24.0 * scale[1], -35.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 30.0 * scale[1], -5.0 * scale[0],
              84.0 * scale[1], 28.0 * scale[0], 85.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0], -
              16.0 * scale[1], 23.0 * scale[0], -36.0 * scale[1])
    te.end_fill()
    Moveto(508.0 * scale[0], 1330.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-20.0 * scale[0], -10.0 * scale[1], -37.0 *
              scale[0], -17.0 * scale[1], -39.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 2.0 * scale[1], -5.0 * scale[0], -
              15.0 * scale[1], -7.0 * scale[0], -37.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -34.0 * scale[1], -1.0 * scale[0], -
              37.0 * scale[1], 12.0 * scale[0], -26.0 * scale[1])
    Curveto_r(8.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 5.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 7.0 * scale[1], -9.0 * scale[0],
              21.0 * scale[1], 9.0 * scale[0], 16.0 * scale[1])
    Curveto_r(14.0 * scale[0], -5.0 * scale[1], 15.0 *
              scale[0], -4.0 * scale[1], 2.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 8.0 * scale[1], -12.0 * scale[0],
              11.0 * scale[1], -2.0 * scale[0], 11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0],
              6.0 * scale[1], 28.0 * scale[0], 14.0 * scale[1])
    Curveto_r(7.0 * scale[0], 8.0 * scale[1], 19.0 * scale[0],
              16.0 * scale[1], 26.0 * scale[0], 19.0 * scale[1])
    Curveto_r(7.0 * scale[0], 2.0 * scale[1], 10.0 * scale[0],
              7.0 * scale[1], 7.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -21.0 * scale[0], -
              2.0 * scale[1], -41.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(567.0 * scale[0], 1325.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -9.0 * scale[1], 8.0 * scale[0], -
              13.0 * scale[1], 11.0 * scale[0], -10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 12.0 * scale[0], -
              9.0 * scale[1], 19.0 * scale[0], -26.0 * scale[1])
    Curveto_r(10.0 * scale[0], -23.0 * scale[1], 10.0 *
              scale[0], -35.0 * scale[1], 2.0 * scale[0], -45.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -10.0 * scale[1], -6.0 * scale[0], -
              21.0 * scale[1], 10.0 * scale[0], -42.0 * scale[1])
    Curveto_r(11.0 * scale[0], -16.0 * scale[1], 17.0 * scale[0], -
              33.0 * scale[1], 13.0 * scale[0], -37.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -5.0 * scale[1], -1.0 *
              scale[0], -5.0 * scale[1], 6.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 5.0 * scale[1], 10.0 * scale[0],
              11.0 * scale[1], 4.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 7.0 * scale[1], -6.0 * scale[0],
              15.0 * scale[1], 4.0 * scale[0], 25.0 * scale[1])
    Curveto_r(20.0 * scale[0], 20.0 * scale[1], 17.0 * scale[0],
              67.0 * scale[1], -6.0 * scale[0], 94.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 17.0 * scale[1], -20.0 * scale[0],
              20.0 * scale[1], -20.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -9.0 * scale[1], -5.0 *
              scale[0], -6.0 * scale[1], -10.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 12.0 * scale[1], -16.0 * scale[0],
              22.0 * scale[1], -24.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 0.0 * scale[1], -13.0 *
              scale[0], -6.0 * scale[1], -9.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto_r(68.0 * scale[0], -44.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -29.0 * scale[1], -4.0 * scale[0], -
              71.0 * scale[1], -21.0 * scale[0], -64.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -14.0 * scale[0],
              9.0 * scale[1], -14.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 5.0 * scale[0],
              6.0 * scale[1], 12.0 * scale[0], 2.0 * scale[1])
    Curveto_r(8.0 * scale[0], -5.0 * scale[1], 9.0 * scale[0],
              3.0 * scale[1], 5.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 38.0 * scale[1], 7.0 * scale[0],
              51.0 * scale[1], 18.0 * scale[0], 18.0 * scale[1])
    te.end_fill()
    Moveto(855.0 * scale[0], 1289.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0], -
              12.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 17.0 * scale[1], 1.0 * scale[0],
              20.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(490.0 * scale[0], 1186.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(540.0 * scale[0], 1165.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -9.0 * scale[1], -8.0 * scale[0], -
              15.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 26.0 * scale[0],
              19.0 * scale[1], 19.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 2.0 * scale[1], -10.0 * scale[0], -
              2.0 * scale[1], -17.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(259.0 * scale[0], 1069.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -15.0 * scale[1], -6.0 *
              scale[0], -19.0 * scale[1], 6.0 * scale[0], -19.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0], -
              4.0 * scale[1], 15.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 22.0 * scale[0], -
              39.0 * scale[1], 51.0 * scale[0], -69.0 * scale[1])
    Curveto_r(10.0 * scale[0], -10.0 * scale[1], 19.0 * scale[0], -
              42.0 * scale[1], 23.0 * scale[0], -81.0 * scale[1])
    Curveto_r(9.0 * scale[0], -86.0 * scale[1], 14.0 * scale[0], -
              93.0 * scale[1], 55.0 * scale[0], -79.0 * scale[1])
    Curveto_r(17.0 * scale[0], 6.0 * scale[1], 61.0 * scale[0],
              9.0 * scale[1], 96.0 * scale[0], 7.0 * scale[1])
    Curveto_r(52.0 * scale[0], -3.0 * scale[1], 62.0 *
              scale[0], -1.0 * scale[1], 53.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 7.0 * scale[1], -26.0 * scale[0],
              13.0 * scale[1], -44.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-33.0 * scale[0], 0.0 * scale[1], -110.0 * scale[0],
              25.0 * scale[1], -129.0 * scale[0], 42.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              12.0 * scale[1], 5.0 * scale[0], 18.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 10.0 * scale[0],
              10.0 * scale[1], 5.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0], -
              5.0 * scale[1], -22.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -9.0 * scale[1], -10.0 *
              scale[0], -7.0 * scale[1], -6.0 * scale[0], 10.0 * scale[1])
    Curveto_r(4.0 * scale[0], 15.0 * scale[1], 13.0 * scale[0],
              21.0 * scale[1], 33.0 * scale[0], 21.0 * scale[1])
    Curveto_r(28.0 * scale[0], 0.0 * scale[1], 55.0 * scale[0], -
              21.0 * scale[1], 43.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], 1.0 * scale[0], -
              7.0 * scale[1], 10.0 * scale[0], -7.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0],
              5.0 * scale[1], 17.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], 15.0 * scale[0],
              2.0 * scale[1], 15.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 9.0 * scale[0], -21.0 * scale[1])
    Curveto_r(6.0 * scale[0], -10.0 * scale[1], 5.0 * scale[0], -
              12.0 * scale[1], -2.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -12.0 * scale[0],
              2.0 * scale[1], -12.0 * scale[0], -3.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 9.0 * scale[0], -
              11.0 * scale[1], 20.0 * scale[0], -11.0 * scale[1])
    Curveto_r(21.0 * scale[0], 0.0 * scale[1], 120.0 * scale[0],
              89.0 * scale[1], 120.0 * scale[0], 107.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 6.0 * scale[0],
              13.0 * scale[1], 14.0 * scale[0], 16.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 13.0 * scale[0], -
              1.0 * scale[1], 12.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -11.0 * scale[1], 8.0 * scale[0], -
              18.0 * scale[1], 26.0 * scale[0], -20.0 * scale[1])
    Curveto_r(15.0 * scale[0], -2.0 * scale[1], 34.0 * scale[0], -
              13.0 * scale[1], 43.0 * scale[0], -24.0 * scale[1])
    Curveto_r(14.0 * scale[0], -21.0 * scale[1], 15.0 *
              scale[0], -21.0 * scale[1], 32.0 * scale[0], 18.0 * scale[1])
    Curveto_r(26.0 * scale[0], 56.0 * scale[1], 53.0 * scale[0],
              94.0 * scale[1], 68.0 * scale[0], 94.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 18.0 * scale[0],
              7.0 * scale[1], 25.0 * scale[0], 15.0 * scale[1])
    Curveto_r(7.0 * scale[0], 8.0 * scale[1], 21.0 * scale[0],
              15.0 * scale[1], 31.0 * scale[0], 15.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0],
              4.0 * scale[1], 19.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], -251.0 * scale[0],
              23.0 * scale[1], -455.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-151.0 * scale[0], -1.0 * scale[1], -167.0 *
              scale[0], -3.0 * scale[1], -176.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(581.0 * scale[0], 808.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -2.0 * scale[1], 20.0 * scale[0], -
              16.0 * scale[1], 39.0 * scale[0], -33.0 * scale[1])
    Curveto_r(20.0 * scale[0], -17.0 * scale[1], 28.0 * scale[0], -
              21.0 * scale[1], 20.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 26.0 * scale[1], -41.0 * scale[0],
              45.0 * scale[1], -54.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(3.0 * scale[0], 500.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -47.0 * scale[1], 2.0 * scale[0], -
              66.0 * scale[1], 4.0 * scale[0], -42.0 * scale[1])
    Curveto_r(2.0 * scale[0], 23.0 * scale[1], 2.0 * scale[0],
              61.0 * scale[1], 0.0 * scale[0], 85.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 23.0 * scale[1], -4.0 * scale[0],
              4.0 * scale[1], -4.0 * scale[0], -43.0 * scale[1])
    te.end_fill()
    Moveto(83.0 * scale[0], 553.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -13.0 * scale[0], -
              11.0 * scale[1], -13.0 * scale[0], -19.0 * scale[1])
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], 4.0 * scale[0], -
              12.0 * scale[1], 20.0 * scale[0], -4.0 * scale[1])
    Curveto_r(32.0 * scale[0], 17.0 * scale[1], 26.0 * scale[0],
              37.0 * scale[1], -7.0 * scale[0], 23.0 * scale[1])
    te.end_fill()
    Moveto(56.0 * scale[0], 325.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -201.0 * scale[1], 6.0 * scale[0], -
              232.0 * scale[1], 21.0 * scale[0], -242.0 * scale[1])
    Curveto_r(21.0 * scale[0], -16.0 * scale[1], 283.0 *
              scale[0], -18.0 * scale[1], 283.0 * scale[0], -3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], -15.0 * scale[0],
              14.0 * scale[1], -33.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -1.0 * scale[1], -6.0 * scale[0],
              3.0 * scale[1], -2.0 * scale[0], 9.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], 16.0 * scale[0],
              8.0 * scale[1], 27.0 * scale[0], 4.0 * scale[1])
    Curveto_r(16.0 * scale[0], -5.0 * scale[1], 20.0 *
              scale[0], -3.0 * scale[1], 15.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -1.0 * scale[0],
              18.0 * scale[1], 6.0 * scale[0], 21.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 8.0 * scale[0],
              5.0 * scale[1], -1.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 1.0 * scale[1], -10.0 * scale[0],
              5.0 * scale[1], -7.0 * scale[0], 11.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], -1.0 * scale[0],
              7.0 * scale[1], -10.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -3.0 * scale[1], -21.0 * scale[0],
              0.0 * scale[1], -26.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 11.0 * scale[1], -9.0 * scale[0],
              11.0 * scale[1], -9.0 * scale[0], -3.0 * scale[1])
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], 8.0 * scale[0], -
              18.0 * scale[1], 22.0 * scale[0], -18.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 18.0 * scale[0], -
              3.0 * scale[1], 14.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -13.0 * scale[1], -90.0 *
              scale[0], -11.0 * scale[1], -112.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 12.0 * scale[1], -22.0 * scale[0],
              11.0 * scale[1], -18.0 * scale[0], -9.0 * scale[1])
    Curveto_r(4.0 * scale[0], -21.0 * scale[1], 4.0 * scale[0], -
              21.0 * scale[1], -4.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 11.0 * scale[1], -10.0 * scale[0],
              23.0 * scale[1], -11.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 18.0 * scale[1], -80.0 * scale[0],
              85.0 * scale[1], -113.0 * scale[0], 97.0 * scale[1])
    Lineto_r(-35.0 * scale[0], 13.0 * scale[1])
    Lineto_r(5.0 * scale[0], 66.0 * scale[1])
    Curveto_r(5.0 * scale[0], 71.0 * scale[1], 28.0 * scale[0],
              117.0 * scale[1], 66.0 * scale[0], 130.0 * scale[1])
    Curveto_r(26.0 * scale[0], 10.0 * scale[1], 126.0 * scale[0], -
              22.0 * scale[1], 144.0 * scale[0], -46.0 * scale[1])
    Curveto_r(6.0 * scale[0], -9.0 * scale[1], 12.0 * scale[0], -
              13.0 * scale[1], 12.0 * scale[0], -9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 6.0 * scale[0],
              3.0 * scale[1], 13.0 * scale[0], -3.0 * scale[1])
    Curveto_r(10.0 * scale[0], -8.0 * scale[1], 14.0 *
              scale[0], -7.0 * scale[1], 14.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              15.0 * scale[1], -17.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 0.0 * scale[1], -23.0 * scale[0],
              6.0 * scale[1], -29.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 7.0 * scale[1], -39.0 * scale[0],
              21.0 * scale[1], -72.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-44.0 * scale[0], 13.0 * scale[1], -59.0 * scale[0],
              21.0 * scale[1], -55.0 * scale[0], 32.0 * scale[1])
    Curveto_r(4.0 * scale[0], 11.0 * scale[1], -4.0 * scale[0],
              14.0 * scale[1], -34.0 * scale[0], 14.0 * scale[1])
    Lineto_r(-40.0 * scale[0], 0.0 * scale[1])
    Lineto_r(-2.0 * scale[0], -52.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -49.0 * scale[1], -2.0 *
              scale[0], -47.0 * scale[1], -9.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 41.0 * scale[1], -5.0 * scale[0], -
              28.0 * scale[1], -3.0 * scale[0], -155.0 * scale[1])
    te.end_fill()
    Moveto_r(78.0 * scale[0], -160.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -9.0 * scale[1], 21.0 * scale[0], -
              17.0 * scale[1], 33.0 * scale[0], -17.0 * scale[1])
    Curveto_r(14.0 * scale[0], -2.0 * scale[1], 19.0 * scale[0], -
              7.0 * scale[1], 15.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -10.0 * scale[1], -1.0 *
              scale[0], -12.0 * scale[1], 9.0 * scale[0], -6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 6.0 * scale[1], 12.0 * scale[0],
              5.0 * scale[1], 1.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -7.0 * scale[1], -34.0 * scale[0], -
              14.0 * scale[1], -60.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-44.0 * scale[0], -2.0 * scale[1], -48.0 *
              scale[0], -1.0 * scale[1], -47.0 * scale[0], 21.0 * scale[1])
    Curveto_r(1.0 * scale[0], 22.0 * scale[1], 21.0 * scale[0],
              55.0 * scale[1], 33.0 * scale[0], 55.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              7.0 * scale[1], 16.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(971.0 * scale[0], 432.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -9.0 * scale[1], -9.0 * scale[0], -
              11.0 * scale[1], -23.0 * scale[0], -8.0 * scale[1])
    Lineto_r(-23.0 * scale[0], 6.0 * scale[1])
    Lineto_r(23.0 * scale[0], -12.0 * scale[1])
    Curveto_r(24.0 * scale[0], -12.0 * scale[1], 37.0 *
              scale[0], -7.0 * scale[1], 29.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 11.0 * scale[1], -6.0 * scale[0],
              11.0 * scale[1], -6.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(1005.0 * scale[0], 430.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(340.0 * scale[0], 410.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(860.0 * scale[0], 416.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 7.0 * scale[0], -
              7.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 12.0 *
              scale[0], -2.0 * scale[1], 9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], -25.0 * scale[0],
              14.0 * scale[1], -25.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(377.0 * scale[0], 403.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -18.0 * scale[1], 21.0 *
              scale[0], -23.0 * scale[1], 35.0 * scale[0], -5.0 * scale[1])
    Curveto_r(11.0 * scale[0], 15.0 * scale[1], 11.0 * scale[0],
              16.0 * scale[1], -4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -10.0 * scale[1], -17.0 *
              scale[0], -10.0 * scale[1], -20.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], -6.0 * scale[0],
              9.0 * scale[1], -11.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(332.0 * scale[0], 323.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-28.0 * scale[0], -26.0 * scale[1], -22.0 *
              scale[0], -60.0 * scale[1], 11.0 * scale[0], -65.0 * scale[1])
    Curveto_r(19.0 * scale[0], -3.0 * scale[1], 22.0 * scale[0], -
              9.0 * scale[1], 21.0 * scale[0], -45.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -31.0 * scale[1], 2.0 * scale[0], -
              40.0 * scale[1], 12.0 * scale[0], -36.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 14.0 * scale[0], -
              1.0 * scale[1], 14.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 8.0 * scale[0], -
              16.0 * scale[1], 22.0 * scale[0], -16.0 * scale[1])
    Curveto_r(21.0 * scale[0], 0.0 * scale[1], 21.0 * scale[0],
              0.0 * scale[1], 2.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 14.0 * scale[1], -19.0 * scale[0],
              14.0 * scale[1], 1.0 * scale[0], 13.0 * scale[1])
    Curveto_r(11.0 * scale[0], -1.0 * scale[1], 22.0 *
              scale[0], -4.0 * scale[1], 25.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 16.0 * scale[0], -
              11.0 * scale[1], 29.0 * scale[0], -18.0 * scale[1])
    Curveto_r(20.0 * scale[0], -12.0 * scale[1], 26.0 *
              scale[0], -11.0 * scale[1], 39.0 * scale[0], 2.0 * scale[1])
    Curveto_r(12.0 * scale[0], 12.0 * scale[1], 13.0 * scale[0],
              18.0 * scale[1], 3.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 8.0 * scale[1], -25.0 * scale[0],
              48.0 * scale[1], -41.0 * scale[0], 88.0 * scale[1])
    Lineto_r(-28.0 * scale[0], 72.0 * scale[1])
    Lineto_r(-44.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-31.0 * scale[0], 0.0 * scale[1], -50.0 * scale[0], -
              6.0 * scale[1], -66.0 * scale[0], -22.0 * scale[1])
    te.end_fill()
    Moveto_r(108.0 * scale[0], -4.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -4.0 * scale[0], -
              7.0 * scale[1], -10.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0],
              11.0 * scale[1], -10.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 5.0 * scale[0],
              7.0 * scale[1], 10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 10.0 * scale[0], -
              11.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto_r(-33.0 * scale[0], -31.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -6.0 *
              scale[0], -5.0 * scale[1], -6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 11.0 * scale[1], 2.0 * scale[0],
              17.0 * scale[1], 5.0 * scale[0], 13.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 4.0 * scale[0], -
              12.0 * scale[1], 1.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(1021.0 * scale[0], 289.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -56.0 * scale[1], -2.0 * scale[0], -
              57.0 * scale[1], -39.0 * scale[0], -72.0 * scale[1])
    Curveto_r(-42.0 * scale[0], -17.0 * scale[1], -112.0 * scale[0], -
              83.0 * scale[1], -112.0 * scale[0], -106.0 * scale[1])
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], -3.0 * scale[0], -
              12.0 * scale[1], -12.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-26.0 * scale[0], 26.0 * scale[1], -57.0 * scale[0],
              5.0 * scale[1], -58.0 * scale[0], -40.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], 122.0 *
              scale[0], -1.0 * scale[1], 175.0 * scale[0], 7.0 * scale[1])
    Curveto_r(11.0 * scale[0], 2.0 * scale[1], 23.0 * scale[0],
              4.0 * scale[1], 26.0 * scale[0], 4.0 * scale[1])
    Curveto_r(8.0 * scale[0], 1.0 * scale[1], 31.0 * scale[0],
              203.0 * scale[1], 27.0 * scale[0], 236.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 18.0 * scale[1], -6.0 * scale[0],
              8.0 * scale[1], -7.0 * scale[0], -26.0 * scale[1])
    te.end_fill()
    Moveto(286.0 * scale[0], 255.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -8.0 * scale[1], 8.0 * scale[0], -
              15.0 * scale[1], 10.0 * scale[0], -15.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 4.0 * scale[0],
              7.0 * scale[1], 4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -4.0 * scale[0],
              15.0 * scale[1], -10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              7.0 * scale[1], -4.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(842.0 * scale[0], 235.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(829.0 * scale[0], 172.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -20.0 * scale[1], -2.0 *
              scale[0], -29.0 * scale[1], 4.0 * scale[0], -23.0 * scale[1])
    Curveto_r(5.0 * scale[0], 5.0 * scale[1], 7.0 * scale[0],
              19.0 * scale[1], 5.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 20.0 * scale[1], -5.0 * scale[0],
              19.0 * scale[1], -9.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(435.0 * scale[0], 110.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-22.0 * scale[0], -24.0 * scale[1], -13.0 *
              scale[0], -56.0 * scale[1], 12.0 * scale[0], -42.0 * scale[1])
    Curveto_r(23.0 * scale[0], 13.0 * scale[1], 27.0 * scale[0],
              46.0 * scale[1], 5.0 * scale[0], 38.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -5.0 * scale[1], -12.0 *
              scale[0], -2.0 * scale[1], 2.0 * scale[0], 9.0 * scale[1])
    Curveto_r(11.0 * scale[0], 8.0 * scale[1], 15.0 * scale[0],
              15.0 * scale[1], 9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -18.0 * scale[0], -
              9.0 * scale[1], -28.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(393.0 * scale[0], 98.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -24.0 * scale[1], -23.0 *
              scale[0], -47.0 * scale[1], -8.0 * scale[0], -42.0 * scale[1])
    Curveto_r(14.0 * scale[0], 6.0 * scale[1], 31.0 * scale[0],
              42.0 * scale[1], 22.0 * scale[0], 50.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 2.0 * scale[1], -9.0 * scale[0], -
              1.0 * scale[1], -14.0 * scale[0], -8.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#8ec0bb')
    te.end_fill()
    Moveto(14.0 * scale[0], 1340.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -69.0 * scale[1], 1.0 * scale[0], -
              97.0 * scale[1], 3.0 * scale[0], -62.0 * scale[1])
    Curveto_r(2.0 * scale[0], 34.0 * scale[1], 2.0 * scale[0],
              90.0 * scale[1], 0.0 * scale[0], 125.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 34.0 * scale[1], -3.0 * scale[0],
              6.0 * scale[1], -3.0 * scale[0], -63.0 * scale[1])
    te.end_fill()
    Moveto(183.0 * scale[0], 1357.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -5.0 * scale[1], -4.0 * scale[0], -
              12.0 * scale[1], -12.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -3.0 * scale[1], -11.0 * scale[0],
              0.0 * scale[1], -6.0 * scale[0], 9.0 * scale[1])
    Curveto_r(5.0 * scale[0], 8.0 * scale[1], 4.0 * scale[0],
              11.0 * scale[1], -1.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -5.0 * scale[1], -10.0 * scale[0], -
              13.0 * scale[1], -10.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              14.0 * scale[1], -3.0 * scale[0], -20.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -5.0 * scale[0], -
              8.0 * scale[1], -9.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 2.0 * scale[1], -6.0 * scale[0], -
              12.0 * scale[1], -3.0 * scale[0], -32.0 * scale[1])
    Curveto_r(5.0 * scale[0], -33.0 * scale[1], 6.0 * scale[0], -
              34.0 * scale[1], 9.0 * scale[0], -9.0 * scale[1])
    Curveto_r(2.0 * scale[0], 15.0 * scale[1], 8.0 * scale[0],
              25.0 * scale[1], 13.0 * scale[0], 22.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 6.0 * scale[0],
              1.0 * scale[1], 3.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], 3.0 * scale[0],
              19.0 * scale[1], 16.0 * scale[0], 26.0 * scale[1])
    Curveto_r(18.0 * scale[0], 10.0 * scale[1], 21.0 * scale[0],
              9.0 * scale[1], 15.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -9.0 * scale[1], -3.0 * scale[0], -
              10.0 * scale[1], 11.0 * scale[0], -5.0 * scale[1])
    Curveto_r(10.0 * scale[0], 4.0 * scale[1], 15.0 * scale[0],
              4.0 * scale[1], 12.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -3.0 * scale[1], -1.0 * scale[0], -
              13.0 * scale[1], 7.0 * scale[0], -20.0 * scale[1])
    Curveto_r(7.0 * scale[0], -8.0 * scale[1], 11.0 * scale[0], -
              24.0 * scale[1], 8.0 * scale[0], -36.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -34.0 * scale[1], 12.0 *
              scale[0], -1.0 * scale[1], 21.0 * scale[0], 35.0 * scale[1])
    Curveto_r(5.0 * scale[0], 21.0 * scale[1], 4.0 * scale[0],
              27.0 * scale[1], -5.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -5.0 * scale[1], -10.0 *
              scale[0], -2.0 * scale[1], -6.0 * scale[0], 9.0 * scale[1])
    Curveto_r(3.0 * scale[0], 9.0 * scale[1], 1.0 * scale[0],
              20.0 * scale[1], -6.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 11.0 * scale[1], -56.0 * scale[0],
              11.0 * scale[1], -54.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto_r(52.0 * scale[0], -7.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -6.0 * scale[1], -1.0 * scale[0], -
              7.0 * scale[1], -9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 7.0 * scale[1], -21.0 * scale[0],
              14.0 * scale[1], -7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0], -
              4.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(888.0 * scale[0], 1349.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -6.0 * scale[1], -15.0 * scale[0], -
              16.0 * scale[1], -11.0 * scale[0], -26.0 * scale[1])
    Curveto_r(4.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], -5.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -10.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -10.0 * scale[1])
    Curveto_r(4.0 * scale[0], -11.0 * scale[1], 2.0 * scale[0], -
              15.0 * scale[1], -4.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -8.0 * scale[0], -
              4.0 * scale[1], -5.0 * scale[0], -21.0 * scale[1])
    Curveto_r(5.0 * scale[0], -23.0 * scale[1], 6.0 * scale[0], -
              24.0 * scale[1], 12.0 * scale[0], -7.0 * scale[1])
    Curveto_r(6.0 * scale[0], 16.0 * scale[1], 8.0 * scale[0],
              17.0 * scale[1], 12.0 * scale[0], 5.0 * scale[1])
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], 3.0 * scale[0], -
              2.0 * scale[1], 0.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 28.0 * scale[1], -3.0 * scale[0],
              29.0 * scale[1], 14.0 * scale[0], 15.0 * scale[1])
    Curveto_r(18.0 * scale[0], -14.0 * scale[1], 18.0 *
              scale[0], -14.0 * scale[1], 5.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 20.0 * scale[1], -9.0 * scale[0],
              22.0 * scale[1], 22.0 * scale[0], 6.0 * scale[1])
    Curveto_r(21.0 * scale[0], -10.0 * scale[1], 21.0 *
              scale[0], -10.0 * scale[1], 3.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 9.0 * scale[1], -14.0 * scale[0],
              16.0 * scale[1], -8.0 * scale[0], 16.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 21.0 * scale[0], -
              15.0 * scale[1], 32.0 * scale[0], -32.0 * scale[1])
    Curveto_r(12.0 * scale[0], -21.0 * scale[1], 20.0 * scale[0], -
              27.0 * scale[1], 20.0 * scale[0], -16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], 3.0 * scale[0],
              24.0 * scale[1], 6.0 * scale[0], 33.0 * scale[1])
    Curveto_r(4.0 * scale[0], 9.0 * scale[1], 3.0 * scale[0],
              15.0 * scale[1], -2.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -1.0 * scale[1], -23.0 * scale[0],
              5.0 * scale[1], -39.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 11.0 * scale[1], -36.0 * scale[0],
              13.0 * scale[1], -47.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto_r(17.0 * scale[0], -9.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -12.0 * scale[0], -
              10.0 * scale[1], -18.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0],
              4.0 * scale[1], 3.0 * scale[0], 10.0 * scale[1])
    Curveto_r(19.0 * scale[0], 12.0 * scale[1], 23.0 * scale[0],
              12.0 * scale[1], 15.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(940.0 * scale[0], 1356.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 7.0 * scale[0], -
              7.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 12.0 *
              scale[0], -2.0 * scale[1], 9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], -25.0 * scale[0],
              14.0 * scale[1], -25.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(558.0 * scale[0], 1343.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(476.0 * scale[0], 1332.0 * scale[1], x, y)
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
    Moveto(626.0 * scale[0], 1308.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -8.0 * scale[1], 2.0 * scale[0], -
              9.0 * scale[1], -10.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              4.0 * scale[1], -5.0 * scale[0], -14.0 * scale[1])
    Curveto_r(6.0 * scale[0], -12.0 * scale[1], 9.0 * scale[0], -
              32.0 * scale[1], 6.0 * scale[0], -45.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -42.0 * scale[1], 10.0 *
              scale[0], -36.0 * scale[1], 21.0 * scale[0], 6.0 * scale[1])
    Curveto_r(6.0 * scale[0], 26.0 * scale[1], 6.0 * scale[0],
              38.0 * scale[1], 0.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -4.0 * scale[1], -8.0 * scale[0],
              2.0 * scale[1], -3.0 * scale[0], 15.0 * scale[1])
    Curveto_r(4.0 * scale[0], 13.0 * scale[1], 2.0 * scale[0],
              21.0 * scale[1], -5.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              5.0 * scale[1], -4.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(114.0 * scale[0], 1273.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -16.0 * scale[1], 5.0 * scale[0], -
              29.0 * scale[1], 6.0 * scale[0], -30.0 * scale[1])
    Curveto_r(2.0 * scale[0], -2.0 * scale[1], 3.0 * scale[0], -
              7.0 * scale[1], 4.0 * scale[0], -13.0 * scale[1])
    Curveto_r(3.0 * scale[0], -27.0 * scale[1], 77.0 * scale[0], -
              53.0 * scale[1], 90.0 * scale[0], -32.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], -8.0 * scale[0],
              7.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-34.0 * scale[0], -5.0 * scale[1], -61.0 * scale[0],
              27.0 * scale[1], -61.0 * scale[0], 70.0 * scale[1])
    Curveto_r(0.0 * scale[0], 16.0 * scale[1], -5.0 * scale[0],
              28.0 * scale[1], -10.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              12.0 * scale[1], -6.0 * scale[0], -27.0 * scale[1])
    te.end_fill()
    Moveto(467.0 * scale[0], 1283.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -7.0 * scale[1], 6.0 * scale[0], -
              13.0 * scale[1], 8.0 * scale[0], -13.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 5.0 * scale[0],
              6.0 * scale[1], 8.0 * scale[0], 13.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], -1.0 * scale[0],
              14.0 * scale[1], -8.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              6.0 * scale[1], -8.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(942.0 * scale[0], 1265.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -14.0 * scale[1], 13.0 * scale[0], -
              24.0 * scale[1], 14.0 * scale[0], -22.0 * scale[1])
    Curveto_r(6.0 * scale[0], 6.0 * scale[1], -9.0 * scale[0],
              47.0 * scale[1], -17.0 * scale[0], 47.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -3.0 * scale[0], -
              11.0 * scale[1], 3.0 * scale[0], -25.0 * scale[1])
    te.end_fill()
    Moveto(841.0 * scale[0], 1264.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(210.0 * scale[0], 1261.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], -9.0 * scale[0], -
              11.0 * scale[1], -27.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 5.0 * scale[1], -24.0 * scale[0],
              4.0 * scale[1], -13.0 * scale[0], -4.0 * scale[1])
    Curveto_r(14.0 * scale[0], -9.0 * scale[1], 7.0 * scale[0], -
              15.0 * scale[1], -14.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 1.0 * scale[1], -4.0 * scale[0], -
              5.0 * scale[1], 4.0 * scale[0], -13.0 * scale[1])
    Curveto_r(14.0 * scale[0], -18.0 * scale[1], 25.0 *
              scale[0], -22.0 * scale[1], 15.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], 0.0 * scale[0],
              10.0 * scale[1], 8.0 * scale[0], 10.0 * scale[1])
    Curveto_r(17.0 * scale[0], 0.0 * scale[1], 43.0 * scale[0],
              28.0 * scale[1], 33.0 * scale[0], 37.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -6.0 * scale[0],
              1.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(452.0 * scale[0], 1245.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(591.0 * scale[0], 1247.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -21.0 * scale[1], -12.0 *
              scale[0], -21.0 * scale[1], 5.0 * scale[0], -5.0 * scale[1])
    Curveto_r(10.0 * scale[0], 10.0 * scale[1], 16.0 * scale[0],
              20.0 * scale[1], 13.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -11.0 * scale[0], -
              5.0 * scale[1], -18.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(920.0 * scale[0], 1241.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -6.0 * scale[1], -19.0 *
              scale[0], -7.0 * scale[1], -25.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -4.0 * scale[0],
              0.0 * scale[1], 3.0 * scale[0], -8.0 * scale[1])
    Curveto_r(10.0 * scale[0], -11.0 * scale[1], 15.0 *
              scale[0], -10.0 * scale[1], 29.0 * scale[0], 4.0 * scale[1])
    Curveto_r(19.0 * scale[0], 19.0 * scale[1], 16.0 * scale[0],
              22.0 * scale[1], -7.0 * scale[0], 8.0 * scale[1])
    te.end_fill()
    Moveto(850.0 * scale[0], 1223.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], 5.0 * scale[0], -
              25.0 * scale[1], 11.0 * scale[0], -28.0 * scale[1])
    Curveto_r(16.0 * scale[0], -11.0 * scale[1], 17.0 *
              scale[0], -2.0 * scale[1], 2.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 24.0 * scale[1], -13.0 * scale[0],
              24.0 * scale[1], -13.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(486.0 * scale[0], 1207.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0], -
              15.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 0.0 * scale[0],
              11.0 * scale[1], -7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              8.0 * scale[1], -5.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(596.0 * scale[0], 1193.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(930.0 * scale[0], 1189.0 * scale[1], x, y)
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
    Moveto(560.0 * scale[0], 1171.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              11.0 * scale[1], 14.0 * scale[0], -14.0 * scale[1])
    Curveto_r(10.0 * scale[0], -4.0 * scale[1], 13.0 *
              scale[0], -1.0 * scale[1], 9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 15.0 * scale[1], -23.0 * scale[0],
              19.0 * scale[1], -23.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(633.0 * scale[0], 973.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -13.0 * scale[0], -
              10.0 * scale[1], -13.0 * scale[0], -15.0 * scale[1])
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], -99.0 * scale[0], -
              108.0 * scale[1], -120.0 * scale[0], -108.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0],
              5.0 * scale[1], -20.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 6.0 * scale[0],
              7.0 * scale[1], 13.0 * scale[0], 3.0 * scale[1])
    Curveto_r(9.0 * scale[0], -6.0 * scale[1], 9.0 *
              scale[0], -5.0 * scale[1], 0.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 8.0 * scale[1], -10.0 * scale[0],
              17.0 * scale[1], -7.0 * scale[0], 20.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              9.0 * scale[1], -5.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -11.0 * scale[0],
              1.0 * scale[1], -11.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -8.0 * scale[0], -
              11.0 * scale[1], -17.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0],
              3.0 * scale[1], -10.0 * scale[0], 7.0 * scale[1])
    Curveto_r(12.0 * scale[0], 12.0 * scale[1], -15.0 * scale[0],
              33.0 * scale[1], -43.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 0.0 * scale[1], -29.0 * scale[0], -
              6.0 * scale[1], -33.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -17.0 * scale[1], -3.0 *
              scale[0], -19.0 * scale[1], 6.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 6.0 * scale[1], 16.0 * scale[0],
              11.0 * scale[1], 22.0 * scale[0], 11.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 3.0 * scale[0], -
              5.0 * scale[1], -5.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -6.0 * scale[1], -11.0 *
              scale[0], -12.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    Curveto_r(19.0 * scale[0], -17.0 * scale[1], 96.0 * scale[0], -
              42.0 * scale[1], 129.0 * scale[0], -42.0 * scale[1])
    Curveto_r(18.0 * scale[0], 0.0 * scale[1], 39.0 * scale[0], -
              6.0 * scale[1], 45.0 * scale[0], -14.0 * scale[1])
    Curveto_r(7.0 * scale[0], -8.0 * scale[1], 22.0 * scale[0], -
              17.0 * scale[1], 35.0 * scale[0], -20.0 * scale[1])
    Curveto_r(24.0 * scale[0], -6.0 * scale[1], 65.0 * scale[0], -
              60.0 * scale[1], 90.0 * scale[0], -120.0 * scale[1])
    Curveto_r(8.0 * scale[0], -20.0 * scale[1], 19.0 * scale[0], -
              36.0 * scale[1], 24.0 * scale[0], -36.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              55.0 * scale[1], 15.0 * scale[0], 123.0 * scale[1])
    Curveto_r(6.0 * scale[0], 137.0 * scale[1], -2.0 * scale[0],
              163.0 * scale[1], -50.0 * scale[0], 169.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 2.0 * scale[1], -28.0 * scale[0],
              8.0 * scale[1], -27.0 * scale[0], 21.0 * scale[1])
    Curveto_r(1.0 * scale[0], 9.0 * scale[1], 1.0 * scale[0],
              17.0 * scale[1], 0.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              3.0 * scale[1], -13.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(134.0 * scale[0], 459.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-38.0 * scale[0], -13.0 * scale[1], -61.0 * scale[0], -
              59.0 * scale[1], -66.0 * scale[0], -130.0 * scale[1])
    Lineto_r(-5.0 * scale[0], -66.0 * scale[1])
    Lineto_r(35.0 * scale[0], -13.0 * scale[1])
    Curveto_r(34.0 * scale[0], -12.0 * scale[1], 103.0 * scale[0], -
              72.0 * scale[1], 111.0 * scale[0], -95.0 * scale[1])
    Curveto_r(2.0 * scale[0], -5.0 * scale[1], 8.0 * scale[0], -
              19.0 * scale[1], 13.0 * scale[0], -30.0 * scale[1])
    Curveto_r(8.0 * scale[0], -19.0 * scale[1], 8.0 *
              scale[0], -19.0 * scale[1], 4.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 21.0 * scale[1], -2.0 * scale[0],
              21.0 * scale[1], 18.0 * scale[0], 7.0 * scale[1])
    Curveto_r(14.0 * scale[0], -9.0 * scale[1], 34.0 * scale[0], -
              12.0 * scale[1], 53.0 * scale[0], -8.0 * scale[1])
    Curveto_r(25.0 * scale[0], 5.0 * scale[1], 30.0 * scale[0],
              10.0 * scale[1], 26.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 15.0 * scale[1], -2.0 * scale[0],
              17.0 * scale[1], 5.0 * scale[0], 8.0 * scale[1])
    Curveto_r(10.0 * scale[0], -15.0 * scale[1], 62.0 *
              scale[0], -6.0 * scale[1], 62.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -6.0 * scale[0],
              8.0 * scale[1], -14.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -4.0 * scale[1], -13.0 * scale[0],
              5.0 * scale[1], -12.0 * scale[0], 36.0 * scale[1])
    Curveto_r(1.0 * scale[0], 36.0 * scale[1], -2.0 * scale[0],
              42.0 * scale[1], -21.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-34.0 * scale[0], 5.0 * scale[1], -39.0 * scale[0],
              39.0 * scale[1], -11.0 * scale[0], 65.0 * scale[1])
    Curveto_r(13.0 * scale[0], 12.0 * scale[1], 32.0 * scale[0],
              21.0 * scale[1], 42.0 * scale[0], 19.0 * scale[1])
    Curveto_r(10.0 * scale[0], -2.0 * scale[1], 28.0 *
              scale[0], -1.0 * scale[1], 41.0 * scale[0], 2.0 * scale[1])
    Curveto_r(21.0 * scale[0], 5.0 * scale[1], 22.0 * scale[0],
              9.0 * scale[1], 12.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 13.0 * scale[1], -16.0 * scale[0],
              22.0 * scale[1], -21.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -9.0 * scale[1], -66.0 *
              scale[0], -8.0 * scale[1], -66.0 * scale[0], 2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], -7.0 * scale[0],
              6.0 * scale[1], -15.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -4.0 * scale[1], -17.0 *
              scale[0], -2.0 * scale[1], -20.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 5.0 * scale[1], -10.0 * scale[0],
              7.0 * scale[1], -15.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -3.0 * scale[1], -10.0 * scale[0],
              1.0 * scale[1], -13.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 20.0 * scale[1], -118.0 * scale[0],
              55.0 * scale[1], -143.0 * scale[0], 45.0 * scale[1])
    te.end_fill()
    Moveto_r(166.0 * scale[0], -204.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -2.0 * scale[0], -
              15.0 * scale[1], -4.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0],
              7.0 * scale[1], -10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], -1.0 * scale[0],
              15.0 * scale[1], 4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              7.0 * scale[1], 10.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(980.0 * scale[0], 417.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -9.0 * scale[0], -
              7.0 * scale[1], -20.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 3.0 * scale[1], -22.0 * scale[0],
              2.0 * scale[1], -24.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], -19.0 *
              scale[0], -6.0 * scale[1], -35.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 1.0 * scale[1], -31.0 *
              scale[0], -2.0 * scale[1], -31.0 * scale[0], -8.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -10.0 * scale[0], -
              6.0 * scale[1], -21.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 7.0 * scale[1], -22.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], -61.0 * scale[1])
    Curveto_r(11.0 * scale[0], -88.0 * scale[1], 8.0 * scale[0], -
              173.0 * scale[1], -7.0 * scale[0], -190.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -8.0 * scale[1], -10.0 * scale[0], -
              15.0 * scale[1], -8.0 * scale[0], -17.0 * scale[1])
    Curveto_r(45.0 * scale[0], -26.0 * scale[1], 49.0 * scale[0], -
              27.0 * scale[1], 49.0 * scale[0], -14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 21.0 * scale[1], 72.0 * scale[0],
              88.0 * scale[1], 112.0 * scale[0], 104.0 * scale[1])
    Curveto_r(37.0 * scale[0], 15.0 * scale[1], 38.0 * scale[0],
              16.0 * scale[1], 40.0 * scale[0], 72.0 * scale[1])
    Curveto_r(1.0 * scale[0], 31.0 * scale[1], 5.0 * scale[0], -
              2.0 * scale[1], 8.0 * scale[0], -74.0 * scale[1])
    Lineto_r(6.0 * scale[0], -130.0 * scale[1])
    Lineto_r(2.0 * scale[0], 172.0 * scale[1])
    Lineto_r(2.0 * scale[0], 172.0 * scale[1])
    Lineto_r(-30.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -1.0 * scale[1], -30.0 *
              scale[0], -5.0 * scale[1], -30.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(4.0 * scale[0], 250.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -96.0 * scale[1], 2.0 * scale[0], -
              136.0 * scale[1], 3.0 * scale[0], -87.0 * scale[1])
    Curveto_r(2.0 * scale[0], 48.0 * scale[1], 2.0 * scale[0],
              126.0 * scale[1], 0.0 * scale[0], 175.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 48.0 * scale[1], -3.0 * scale[0],
              8.0 * scale[1], -3.0 * scale[0], -88.0 * scale[1])
    te.end_fill()
    Moveto(420.0 * scale[0], 331.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0], -
              13.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 10.0 *
              scale[0], -2.0 * scale[1], 10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -4.0 * scale[0],
              13.0 * scale[1], -10.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0],
              2.0 * scale[1], -10.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(401.0 * scale[0], 294.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(41.0 * scale[0], 194.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(406.0 * scale[0], 168.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], 12.0 * scale[0], -
              8.0 * scale[1], 20.0 * scale[0], -8.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0],
              4.0 * scale[1], 14.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], -9.0 * scale[0],
              8.0 * scale[1], -19.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -17.0 *
              scale[0], -4.0 * scale[1], -15.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(342.0 * scale[0], 112.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-23.0 * scale[0], -18.0 * scale[1])
    Lineto_r(22.0 * scale[0], -1.0 * scale[1])
    Curveto_r(12.0 * scale[0], -1.0 * scale[1], 19.0 * scale[0],
              1.0 * scale[1], 15.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              12.0 * scale[1], 5.0 * scale[0], 20.0 * scale[1])
    Curveto_r(15.0 * scale[0], 18.0 * scale[1], 9.0 * scale[0],
              16.0 * scale[1], -19.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(445.0 * scale[0], 110.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(247.0 * scale[0], 53.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(24.0 * scale[0], -2.0 * scale[1], 62.0 *
              scale[0], -2.0 * scale[1], 86.0 * scale[0], 0.0 * scale[1])
    Curveto_r(23.0 * scale[0], 2.0 * scale[1], 4.0 * scale[0],
              4.0 * scale[1], -43.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-47.0 * scale[0], 0.0 * scale[1], -66.0 *
              scale[0], -2.0 * scale[1], -43.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(398.0 * scale[0], 53.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 30.0 *
              scale[0], -2.0 * scale[1], 40.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 0.0 * scale[1], -30.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(5.0 * scale[0], 20.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 14.0 * scale[0], -
              10.0 * scale[1], 23.0 * scale[0], -10.0 * scale[1])
    Curveto_r(15.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              2.0 * scale[1], 2.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 13.0 * scale[1], -33.0 * scale[0],
              13.0 * scale[1], -25.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(163.0 * scale[0], 3.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(59.0 * scale[0], -2.0 * scale[1], 154.0 *
              scale[0], -2.0 * scale[1], 210.0 * scale[0], 0.0 * scale[1])
    Curveto_r(56.0 * scale[0], 1.0 * scale[1], 8.0 * scale[0],
              3.0 * scale[1], -108.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-116.0 * scale[0], 0.0 * scale[1], -161.0 *
              scale[0], -2.0 * scale[1], -102.0 * scale[0], -3.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#5e6562')
    te.end_fill()
    Moveto(2.0 * scale[0], 1405.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(610.0 * scale[0], 1380.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(8.0 * scale[0], -5.0 * scale[1], 20.0 * scale[0], -
              10.0 * scale[1], 25.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 3.0 * scale[0],
              5.0 * scale[1], -5.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -19.0 * scale[0],
              10.0 * scale[1], -25.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -3.0 * scale[0], -
              5.0 * scale[1], 5.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(500.0 * scale[0], 1358.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -3.0 * scale[0], -
              8.0 * scale[1], -7.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 8.0 * scale[1], -33.0 * scale[0], -
              11.0 * scale[1], -33.0 * scale[0], -24.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 13.0 * scale[0],
              0.0 * scale[1], 30.0 * scale[0], 9.0 * scale[1])
    Curveto_r(30.0 * scale[0], 17.0 * scale[1], 39.0 * scale[0],
              32.0 * scale[1], 20.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              5.0 * scale[1], -10.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(605.0 * scale[0], 1350.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(10.0 * scale[0], -11.0 * scale[1], 20.0 * scale[0], -
              20.0 * scale[1], 22.0 * scale[0], -20.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], -1.0 * scale[0],
              9.0 * scale[1], -7.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 11.0 * scale[1], -16.0 * scale[0],
              20.0 * scale[1], -22.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -3.0 * scale[0], -
              9.0 * scale[1], 7.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(662.0 * scale[0], 1250.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(467.0 * scale[0], 1247.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -19.0 * scale[1], 6.0 * scale[0], -
              61.0 * scale[1], 22.0 * scale[0], -71.0 * scale[1])
    Curveto_r(7.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0],
              3.0 * scale[1], 1.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 15.0 * scale[1], -10.0 * scale[0],
              37.0 * scale[1], -12.0 * scale[0], 48.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 18.0 * scale[1], -4.0 * scale[0],
              18.0 * scale[1], -11.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(840.0 * scale[0], 1206.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(605.0 * scale[0], 1188.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -6.0 * scale[1], -22.0 * scale[0], -
              14.0 * scale[1], -25.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], -12.0 * scale[0], -
              10.0 * scale[1], -20.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -4.0 * scale[1], -12.0 *
              scale[0], -6.0 * scale[1], 2.0 * scale[0], -6.0 * scale[1])
    Curveto_r(9.0 * scale[0], -1.0 * scale[1], 30.0 * scale[0],
              10.0 * scale[1], 45.0 * scale[0], 24.0 * scale[1])
    Curveto_r(30.0 * scale[0], 26.0 * scale[1], 30.0 * scale[0],
              31.0 * scale[1], -2.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(1043.0 * scale[0], 1135.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -33.0 * scale[1], 2.0 * scale[0], -
              45.0 * scale[1], 4.0 * scale[0], -27.0 * scale[1])
    Curveto_r(2.0 * scale[0], 18.0 * scale[1], 2.0 * scale[0],
              45.0 * scale[1], 0.0 * scale[0], 60.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 15.0 * scale[1], -4.0 * scale[0],
              0.0 * scale[1], -4.0 * scale[0], -33.0 * scale[1])
    te.end_fill()
    Moveto(530.0 * scale[0], 1170.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(160.0 * scale[0], 1090.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -7.0 * scale[1], -9.0 * scale[0], -
              11.0 * scale[1], 14.0 * scale[0], -20.0 * scale[1])
    Curveto_r(30.0 * scale[0], -11.0 * scale[1], 73.0 * scale[0], -
              43.0 * scale[1], 130.0 * scale[0], -96.0 * scale[1])
    Curveto_r(30.0 * scale[0], -28.0 * scale[1], 35.0 * scale[0], -
              40.0 * scale[1], 41.0 * scale[0], -98.0 * scale[1])
    Curveto_r(4.0 * scale[0], -36.0 * scale[1], 12.0 * scale[0], -
              69.0 * scale[1], 18.0 * scale[0], -73.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 8.0 * scale[0],
              0.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], -9.0 * scale[0],
              44.0 * scale[1], -13.0 * scale[0], 79.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 37.0 * scale[1], -13.0 * scale[0],
              70.0 * scale[1], -23.0 * scale[0], 79.0 * scale[1])
    Curveto_r(-29.0 * scale[0], 30.0 * scale[1], -51.0 * scale[0],
              59.0 * scale[1], -51.0 * scale[0], 69.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -7.0 * scale[0],
              10.0 * scale[1], -15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0],
              4.0 * scale[1], -6.0 * scale[0], 19.0 * scale[1])
    Curveto_r(10.0 * scale[0], 17.0 * scale[1], 26.0 * scale[0],
              19.0 * scale[1], 223.0 * scale[0], 20.0 * scale[1])
    Curveto_r(117.0 * scale[0], 1.0 * scale[1], 214.0 * scale[0],
              4.0 * scale[1], 217.0 * scale[0], 6.0 * scale[1])
    Curveto_r(9.0 * scale[0], 9.0 * scale[1], -524.0 * scale[0],
              4.0 * scale[1], -539.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(803.0 * scale[0], 1083.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(50.0 * scale[0], -2.0 * scale[1], 87.0 * scale[0], -
              8.0 * scale[1], 87.0 * scale[0], -14.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 5.0 * scale[0], -
              7.0 * scale[1], 10.0 * scale[0], -4.0 * scale[1])
    Curveto_r(29.0 * scale[0], 18.0 * scale[1], 1.0 * scale[0],
              25.0 * scale[1], -87.0 * scale[0], 23.0 * scale[1])
    Lineto_r(-98.0 * scale[0], -2.0 * scale[1])
    Lineto_r(88.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(840.0 * scale[0], 1045.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -8.0 * scale[1], -18.0 * scale[0], -
              15.0 * scale[1], -26.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              4.0 * scale[1], -18.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -17.0 * scale[1], 32.0 * scale[0],
              1.0 * scale[1], 50.0 * scale[0], 20.0 * scale[1])
    Curveto_r(9.0 * scale[0], 10.0 * scale[1], 15.0 * scale[0],
              19.0 * scale[1], 12.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              7.0 * scale[1], -18.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(770.0 * scale[0], 985.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -9.0 * scale[1], -11.0 * scale[0], -
              17.0 * scale[1], -9.0 * scale[0], -20.0 * scale[1])
    Curveto_r(3.0 * scale[0], -2.0 * scale[1], 10.0 * scale[0],
              5.0 * scale[1], 17.0 * scale[0], 15.0 * scale[1])
    Curveto_r(14.0 * scale[0], 24.0 * scale[1], 10.0 * scale[0],
              26.0 * scale[1], -8.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(732.0 * scale[0], 880.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(3.0 * scale[0], 660.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -47.0 * scale[1], 2.0 * scale[0], -
              66.0 * scale[1], 4.0 * scale[0], -42.0 * scale[1])
    Curveto_r(2.0 * scale[0], 23.0 * scale[1], 2.0 * scale[0],
              61.0 * scale[1], 0.0 * scale[0], 85.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 23.0 * scale[1], -4.0 * scale[0],
              4.0 * scale[1], -4.0 * scale[0], -43.0 * scale[1])
    te.end_fill()
    Moveto(412.0 * scale[0], 640.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(57.0 * scale[0], 535.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -124.0 * scale[1], 13.0 * scale[0], -
              168.0 * scale[1], 13.0 * scale[0], -77.0 * scale[1])
    Lineto_r(0.0 * scale[0], 52.0 * scale[1])
    Lineto_r(40.0 * scale[0], 0.0 * scale[1])
    Curveto_r(30.0 * scale[0], 0.0 * scale[1], 38.0 * scale[0], -
              3.0 * scale[1], 34.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -11.0 * scale[1], 11.0 * scale[0], -
              19.0 * scale[1], 55.0 * scale[0], -32.0 * scale[1])
    Curveto_r(33.0 * scale[0], -9.0 * scale[1], 66.0 * scale[0], -
              23.0 * scale[1], 72.0 * scale[0], -30.0 * scale[1])
    Curveto_r(6.0 * scale[0], -8.0 * scale[1], 20.0 * scale[0], -
              14.0 * scale[1], 31.0 * scale[0], -14.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0], -
              4.0 * scale[1], 13.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -13.0 * scale[1], 1.0 *
              scale[0], -13.0 * scale[1], 28.0 * scale[0], 2.0 * scale[1])
    Curveto_r(20.0 * scale[0], 10.0 * scale[1], 21.0 * scale[0],
              10.0 * scale[1], 8.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -15.0 * scale[1], -11.0 *
              scale[0], -17.0 * scale[1], 1.0 * scale[0], -17.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0],
              5.0 * scale[1], 26.0 * scale[0], 12.0 * scale[1])
    Curveto_r(9.0 * scale[0], 9.0 * scale[1], 12.0 * scale[0],
              9.0 * scale[1], 12.0 * scale[0], -2.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 4.0 * scale[0], -
              10.0 * scale[1], 17.0 * scale[0], 3.0 * scale[1])
    Curveto_r(14.0 * scale[0], 14.0 * scale[1], 15.0 * scale[0],
              21.0 * scale[1], 6.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 9.0 * scale[1], -19.0 * scale[0],
              16.0 * scale[1], -29.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-34.0 * scale[0], -5.0 * scale[1], -63.0 * scale[0],
              7.0 * scale[1], -69.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 11.0 * scale[1], -13.0 * scale[0],
              20.0 * scale[1], -22.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -27.0 * scale[0],
              13.0 * scale[1], -42.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 16.0 * scale[1], -48.0 * scale[0],
              39.0 * scale[1], -74.0 * scale[0], 51.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 12.0 * scale[1], -51.0 * scale[0],
              28.0 * scale[1], -58.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 20.0 * scale[1], -49.0 *
              scale[0], -1.0 * scale[1], -51.0 * scale[0], -34.0 * scale[1])
    Curveto_r(0.0 * scale[0], -15.0 * scale[1], -4.0 *
              scale[0], -5.0 * scale[1], -8.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 28.0 * scale[1], -5.0 * scale[0], -
              3.0 * scale[1], -3.0 * scale[0], -70.0 * scale[1])
    te.end_fill()
    Moveto_r(53.0 * scale[0], 15.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -9.0 * scale[0], -
              14.0 * scale[1], -20.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -8.0 * scale[1], -20.0 *
              scale[0], -8.0 * scale[1], -20.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], 13.0 * scale[0],
              23.0 * scale[1], 33.0 * scale[0], 25.0 * scale[1])
    Curveto_r(4.0 * scale[0], 1.0 * scale[1], 7.0 * scale[0], -
              3.0 * scale[1], 7.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(967.0 * scale[0], 481.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-21.0 * scale[0], -24.0 * scale[1], -23.0 *
              scale[0], -32.0 * scale[1], -12.0 * scale[0], -41.0 * scale[1])
    Curveto_r(9.0 * scale[0], -8.0 * scale[1], 15.0 *
              scale[0], -8.0 * scale[1], 20.0 * scale[0], 0.0 * scale[1])
    Curveto_r(5.0 * scale[0], 8.0 * scale[1], 10.0 * scale[0],
              8.0 * scale[1], 20.0 * scale[0], 0.0 * scale[1])
    Curveto_r(8.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              7.0 * scale[1], 19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 5.0 * scale[1], 1.0 * scale[0],
              13.0 * scale[1], -5.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -8.0 * scale[0],
              9.0 * scale[1], 1.0 * scale[0], 14.0 * scale[1])
    Curveto_r(14.0 * scale[0], 8.0 * scale[1], 7.0 * scale[0],
              40.0 * scale[1], -8.0 * scale[0], 40.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0], -
              13.0 * scale[1], -35.0 * scale[0], -29.0 * scale[1])
    te.end_fill()
    Moveto(836.0 * scale[0], 421.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              14.0 * scale[1], 8.0 * scale[0], -20.0 * scale[1])
    Curveto_r(11.0 * scale[0], -9.0 * scale[1], 16.0 *
              scale[0], -9.0 * scale[1], 22.0 * scale[0], 0.0 * scale[1])
    Curveto_r(4.0 * scale[0], 8.0 * scale[1], 3.0 * scale[0],
              9.0 * scale[1], -4.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -4.0 * scale[1], -12.0 *
              scale[0], -3.0 * scale[1], -12.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 6.0 * scale[0],
              12.0 * scale[1], 13.0 * scale[0], 14.0 * scale[1])
    Curveto_r(7.0 * scale[0], 3.0 * scale[1], 6.0 * scale[0],
              6.0 * scale[1], -5.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 1.0 * scale[1], -19.0 * scale[0], -
              3.0 * scale[1], -22.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(885.0 * scale[0], 420.0 * scale[1], x, y)
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
    Moveto(460.0 * scale[0], 295.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0], -
              17.0 * scale[1], 10.0 * scale[0], -25.0 * scale[1])
    Curveto_r(5.0 * scale[0], -8.0 * scale[1], 10.0 * scale[0], -
              10.0 * scale[1], 10.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              17.0 * scale[1], -10.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 8.0 * scale[1], -10.0 * scale[0],
              11.0 * scale[1], -10.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(833.0 * scale[0], 250.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -30.0 * scale[1], 2.0 * scale[0], -
              43.0 * scale[1], 4.0 * scale[0], -27.0 * scale[1])
    Curveto_r(2.0 * scale[0], 15.0 * scale[1], 2.0 * scale[0],
              39.0 * scale[1], 0.0 * scale[0], 55.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 15.0 * scale[1], -4.0 * scale[0],
              2.0 * scale[1], -4.0 * scale[0], -28.0 * scale[1])
    te.end_fill()
    Moveto(52.0 * scale[0], 174.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -59.0 * scale[1], 2.0 * scale[0], -
              94.0 * scale[1], 10.0 * scale[0], -102.0 * scale[1])
    Curveto_r(8.0 * scale[0], -8.0 * scale[1], 55.0 * scale[0], -
              11.0 * scale[1], 158.0 * scale[0], -10.0 * scale[1])
    Lineto_r(145.0 * scale[0], 2.0 * scale[1])
    Lineto_r(-142.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-78.0 * scale[0], 4.0 * scale[1], -147.0 * scale[0],
              11.0 * scale[1], -152.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 6.0 * scale[1], -12.0 * scale[0],
              48.0 * scale[1], -14.0 * scale[0], 95.0 * scale[1])
    Lineto_r(-3.0 * scale[0], 85.0 * scale[1])
    Lineto_r(-2.0 * scale[0], -91.0 * scale[1])
    te.end_fill()
    Moveto(480.0 * scale[0], 246.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 30.0 * scale[0], -
              66.0 * scale[1], 36.0 * scale[0], -66.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], -3.0 * scale[0],
              15.0 * scale[1], -12.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 36.0 * scale[1], -24.0 * scale[0],
              44.0 * scale[1], -24.0 * scale[0], 33.0 * scale[1])
    te.end_fill()
    Moveto(1016.0 * scale[0], 153.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -40.0 * scale[1], -11.0 * scale[0], -
              73.0 * scale[1], -15.0 * scale[0], -74.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              2.0 * scale[1], -26.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -2.0 * scale[1], -55.0 *
              scale[0], -6.0 * scale[1], -99.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-77.0 * scale[0], -6.0 * scale[1], -78.0 *
              scale[0], -5.0 * scale[1], -73.0 * scale[0], 17.0 * scale[1])
    Curveto_r(6.0 * scale[0], 21.0 * scale[1], 6.0 * scale[0],
              21.0 * scale[1], -8.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -11.0 * scale[1], -15.0 * scale[0], -
              23.0 * scale[1], -15.0 * scale[0], -28.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 51.0 * scale[0], -
              8.0 * scale[1], 114.0 * scale[0], -8.0 * scale[1])
    Curveto_r(85.0 * scale[0], 0.0 * scale[1], 116.0 * scale[0],
              3.0 * scale[1], 125.0 * scale[0], 14.0 * scale[1])
    Curveto_r(7.0 * scale[0], 9.0 * scale[1], 11.0 * scale[0],
              42.0 * scale[1], 9.0 * scale[0], 88.0 * scale[1])
    Lineto_r(-3.0 * scale[0], 73.0 * scale[1])
    Lineto_r(-9.0 * scale[0], -72.0 * scale[1])
    te.end_fill()
    Moveto(816.0 * scale[0], 159.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -42.0 * scale[1], 0.0 *
              scale[0], -50.0 * scale[1], 9.0 * scale[0], -9.0 * scale[1])
    Curveto_r(4.0 * scale[0], 17.0 * scale[1], 5.0 * scale[0],
              34.0 * scale[1], 2.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 3.0 * scale[1], -7.0 * scale[0], -
              10.0 * scale[1], -11.0 * scale[0], -27.0 * scale[1])
    te.end_fill()
    Moveto(90.0 * scale[0], 156.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 7.0 * scale[0], -
              6.0 * scale[1], 15.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 15.0 *
              scale[0], -1.0 * scale[1], 15.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -7.0 * scale[0],
              10.0 * scale[1], -15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              2.0 * scale[1], -15.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(353.0 * scale[0], 146.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -6.0 * scale[1], -23.0 * scale[0], -
              14.0 * scale[1], -23.0 * scale[0], -18.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 18.0 *
              scale[0], -10.0 * scale[1], 25.0 * scale[0], 2.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 11.0 * scale[0],
              10.0 * scale[1], 16.0 * scale[0], 10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0], -
              4.0 * scale[1], 4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 0.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 12.0 * scale[0],
              12.0 * scale[1], 9.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 16.0 * scale[1], -9.0 * scale[0],
              16.0 * scale[1], -40.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(450.0 * scale[0], 151.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(21.0 * scale[0], -6.0 * scale[1], 24.0 * scale[0], -
              12.0 * scale[1], 22.0 * scale[0], -36.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -17.0 * scale[1], -10.0 * scale[0], -
              35.0 * scale[1], -19.0 * scale[0], -42.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -10.0 * scale[1], -12.0 *
              scale[0], -13.0 * scale[1], 9.0 * scale[0], -18.0 * scale[1])
    Curveto_r(13.0 * scale[0], -3.0 * scale[1], 53.0 *
              scale[0], -4.0 * scale[1], 88.0 * scale[0], -2.0 * scale[1])
    Lineto_r(65.0 * scale[0], 3.0 * scale[1])
    Lineto_r(-79.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-62.0 * scale[0], 2.0 * scale[1], -77.0 * scale[0],
              5.0 * scale[1], -68.0 * scale[0], 14.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 12.0 * scale[0],
              22.0 * scale[1], 12.0 * scale[0], 33.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], 10.0 * scale[0],
              27.0 * scale[1], 25.0 * scale[0], 35.0 * scale[1])
    Curveto_r(14.0 * scale[0], 7.0 * scale[1], 23.0 * scale[0],
              15.0 * scale[1], 20.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 3.0 * scale[1], -12.0 * scale[0], -
              1.0 * scale[1], -20.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -10.0 * scale[1], -19.0 *
              scale[0], -10.0 * scale[1], -27.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 7.0 * scale[1], -21.0 * scale[0],
              12.0 * scale[1], -32.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -1.0 * scale[1], -17.0 *
              scale[0], -2.0 * scale[1], 4.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(139.0 * scale[0], 141.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(21.0 * scale[0], -13.0 * scale[1], -5.0 * scale[0], -
              24.0 * scale[1], -29.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 12.0 * scale[1], -29.0 *
              scale[0], -3.0 * scale[1], -8.0 * scale[0], -16.0 * scale[1])
    Curveto_r(15.0 * scale[0], -10.0 * scale[1], 47.0 *
              scale[0], -13.0 * scale[1], 46.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 18.0 * scale[1], 4.0 * scale[0],
              22.0 * scale[1], 16.0 * scale[0], 12.0 * scale[1])
    Curveto_r(12.0 * scale[0], -10.0 * scale[1], 14.0 *
              scale[0], -9.0 * scale[1], 12.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 10.0 * scale[1], -13.0 * scale[0],
              19.0 * scale[1], -27.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 2.0 * scale[1], -20.0 * scale[0],
              0.0 * scale[1], -10.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(416.0 * scale[0], 121.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -3.0 * scale[1], -31.0 * scale[0], -
              13.0 * scale[1], -33.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -11.0 * scale[1], -2.0 *
              scale[0], -12.0 * scale[1], 5.0 * scale[0], -2.0 * scale[1])
    Curveto_r(5.0 * scale[0], 7.0 * scale[1], 15.0 * scale[0],
              10.0 * scale[1], 24.0 * scale[0], 7.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 21.0 * scale[0],
              1.0 * scale[1], 28.0 * scale[0], 10.0 * scale[1])
    Curveto_r(7.0 * scale[0], 8.0 * scale[1], 11.0 * scale[0],
              14.0 * scale[1], 9.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -1.0 * scale[1], -17.0 *
              scale[0], -4.0 * scale[1], -33.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(503.0 * scale[0], 119.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -7.0 * scale[1], -13.0 * scale[0], -
              22.0 * scale[1], -13.0 * scale[0], -33.0 * scale[1])
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 1.0 * scale[0], -
              19.0 * scale[1], 16.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 8.0 * scale[1], 14.0 * scale[0],
              23.0 * scale[1], 12.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 14.0 * scale[1], -5.0 * scale[0],
              15.0 * scale[1], -15.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(576.0 * scale[0], 104.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -22.0 * scale[1], -8.0 *
              scale[0], -24.0 * scale[1], 8.0 * scale[0], -24.0 * scale[1])
    Curveto_r(15.0 * scale[0], 0.0 * scale[1], 28.0 * scale[0],
              24.0 * scale[1], 19.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 10.0 * scale[1], -21.0 * scale[0],
              7.0 * scale[1], -27.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(535.0 * scale[0], 101.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              12.0 * scale[1], 5.0 * scale[0], -16.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 10.0 * scale[0],
              1.0 * scale[1], 10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 18.0 * scale[1], -6.0 * scale[0],
              21.0 * scale[1], -15.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(400.0 * scale[0], 70.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 7.0 * scale[0], -
              10.0 * scale[1], 15.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              2.0 * scale[1], 15.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 2.0 * scale[1], -7.0 * scale[0],
              6.0 * scale[1], -15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -15.0 * scale[0],
              1.0 * scale[1], -15.0 * scale[0], -4.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#8e4622')
    te.end_fill()
    Moveto(125.0 * scale[0], 1453.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-23.0 * scale[0], -6.0 * scale[1], -35.0 * scale[0], -
              21.0 * scale[1], -35.0 * scale[0], -45.0 * scale[1])
    Curveto_r(0.0 * scale[0], -15.0 * scale[1], 9.0 * scale[0], -
              18.0 * scale[1], 55.0 * scale[0], -18.0 * scale[1])
    Curveto_r(30.0 * scale[0], 0.0 * scale[1], 55.0 * scale[0],
              4.0 * scale[1], 55.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -8.0 * scale[0],
              7.0 * scale[1], -19.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -3.0 * scale[1], -22.0 * scale[0],
              0.0 * scale[1], -25.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], 12.0 * scale[0],
              13.0 * scale[1], 43.0 * scale[0], 17.0 * scale[1])
    Curveto_r(28.0 * scale[0], 4.0 * scale[1], 48.0 * scale[0],
              10.0 * scale[1], 46.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], 12.0 * scale[0],
              10.0 * scale[1], 32.0 * scale[0], 12.0 * scale[1])
    Curveto_r(21.0 * scale[0], 2.0 * scale[1], 0.0 * scale[0],
              4.0 * scale[1], -47.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-47.0 * scale[0], 0.0 * scale[1], -94.0 * scale[0], -
              2.0 * scale[1], -105.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(328.0 * scale[0], 1453.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(415.0 * scale[0], 1450.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -3.0 * scale[1], 5.0 * scale[0], -
              11.0 * scale[1], 16.0 * scale[0], -18.0 * scale[1])
    Curveto_r(16.0 * scale[0], -10.0 * scale[1], 19.0 *
              scale[0], -9.0 * scale[1], 19.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], -26.0 * scale[0],
              26.0 * scale[1], -35.0 * scale[0], 12.0 * scale[1])
    te.end_fill()
    Moveto(627.0 * scale[0], 1439.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -20.0 * scale[1], -5.0 *
              scale[0], -20.0 * scale[1], 14.0 * scale[0], -3.0 * scale[1])
    Curveto_r(23.0 * scale[0], 20.0 * scale[1], 23.0 * scale[0],
              24.0 * scale[1], 5.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0], -
              9.0 * scale[1], -19.0 * scale[0], -21.0 * scale[1])
    te.end_fill()
    Moveto(723.0 * scale[0], 1453.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 25.0 *
              scale[0], -2.0 * scale[1], 35.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -27.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(800.0 * scale[0], 1449.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-15.0 * scale[0], -4.0 * scale[1], -18.0 *
              scale[0], -7.0 * scale[1], -8.0 * scale[0], -8.0 * scale[1])
    Curveto_r(10.0 * scale[0], -1.0 * scale[1], 56.0 * scale[0], -
              16.0 * scale[1], 103.0 * scale[0], -33.0 * scale[1])
    Curveto_r(58.0 * scale[0], -22.0 * scale[1], 84.0 * scale[0], -
              37.0 * scale[1], 80.0 * scale[0], -46.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -7.0 * scale[1], 0.0 * scale[0], -
              10.0 * scale[1], 6.0 * scale[0], -7.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 13.0 * scale[0], -
              2.0 * scale[1], 16.0 * scale[0], -14.0 * scale[1])
    Curveto_r(3.0 * scale[0], -12.0 * scale[1], 10.0 * scale[0], -
              21.0 * scale[1], 15.0 * scale[0], -21.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 6.0 * scale[0], -
              6.0 * scale[1], 2.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -8.0 * scale[1], -3.0 *
              scale[0], -10.0 * scale[1], 2.0 * scale[0], -5.0 * scale[1])
    Curveto_r(11.0 * scale[0], 11.0 * scale[1], 13.0 * scale[0],
              87.0 * scale[1], 2.0 * scale[0], 87.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0],
              9.0 * scale[1], -8.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -10.0 * scale[0],
              22.0 * scale[1], -37.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-53.0 * scale[0], 13.0 * scale[1], -143.0 * scale[0],
              18.0 * scale[1], -173.0 * scale[0], 10.0 * scale[1])
    te.end_fill()
    Moveto(660.0 * scale[0], 1423.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 2.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -11.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 26.0 * scale[0], -
              1.0 * scale[1], 51.0 * scale[0], -8.0 * scale[1])
    Curveto_r(25.0 * scale[0], -8.0 * scale[1], 58.0 * scale[0], -
              14.0 * scale[1], 72.0 * scale[0], -13.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 0.0 * scale[0],
              6.0 * scale[1], -32.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-31.0 * scale[0], 7.0 * scale[1], -63.0 * scale[0],
              18.0 * scale[1], -69.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 17.0 * scale[1], -28.0 * scale[0],
              15.0 * scale[1], -28.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(496.0 * scale[0], 1415.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(10.0 * scale[0], -8.0 * scale[1], 23.0 * scale[0], -
              15.0 * scale[1], 28.0 * scale[0], -15.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 1.0 * scale[0],
              7.0 * scale[1], -10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 8.0 * scale[1], -23.0 * scale[0],
              15.0 * scale[1], -28.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -1.0 * scale[0], -
              7.0 * scale[1], 10.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(565.0 * scale[0], 1390.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(250.0 * scale[0], 1379.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -17.0 * scale[1], 27.0 * scale[0], -
              39.0 * scale[1], 47.0 * scale[0], -39.0 * scale[1])
    Curveto_r(13.0 * scale[0], 1.0 * scale[1], 10.0 * scale[0],
              5.0 * scale[1], -12.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-27.0 * scale[0], 15.0 * scale[1], -28.0 * scale[0],
              17.0 * scale[1], -10.0 * scale[0], 24.0 * scale[1])
    Curveto_r(19.0 * scale[0], 7.0 * scale[1], 19.0 * scale[0],
              8.0 * scale[1], -2.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 1.0 * scale[1], -23.0 * scale[0], -
              4.0 * scale[1], -23.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(860.0 * scale[0], 1380.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(19.0 * scale[0], -4.0 * scale[1], 29.0 *
              scale[0], -8.0 * scale[1], 23.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              6.0 * scale[1], -13.0 * scale[0], -13.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 7.0 * scale[0], -
              4.0 * scale[1], 18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(10.0 * scale[0], 10.0 * scale[1], 22.0 * scale[0],
              14.0 * scale[1], 25.0 * scale[0], 10.0 * scale[1])
    Curveto_r(4.0 * scale[0], -3.0 * scale[1], 7.0 *
              scale[0], -1.0 * scale[1], 7.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -17.0 * scale[0],
              12.0 * scale[1], -47.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-47.0 * scale[0], -2.0 * scale[1], -47.0 *
              scale[0], -2.0 * scale[1], -13.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(90.0 * scale[0], 1366.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -23.0 * scale[1], 19.0 * scale[0], -
              29.0 * scale[1], 36.0 * scale[0], -12.0 * scale[1])
    Curveto_r(9.0 * scale[0], 9.0 * scale[1], 20.0 * scale[0],
              13.0 * scale[1], 26.0 * scale[0], 10.0 * scale[1])
    Curveto_r(7.0 * scale[0], -4.0 * scale[1], 8.0 *
              scale[0], -2.0 * scale[1], 4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 18.0 * scale[1], -66.0 * scale[0],
              15.0 * scale[1], -66.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(833.0 * scale[0], 1333.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -7.0 * scale[0], -18.0 * scale[1])
    Curveto_r(3.0 * scale[0], -7.0 * scale[1], 1.0 * scale[0], -
              15.0 * scale[1], -3.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -7.0 * scale[1], -8.0 *
              scale[0], -66.0 * scale[1], 5.0 * scale[0], -79.0 * scale[1])
    Curveto_r(6.0 * scale[0], -6.0 * scale[1], 8.0 * scale[0],
              5.0 * scale[1], 5.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 22.0 * scale[1], 1.0 * scale[0],
              50.0 * scale[1], 7.0 * scale[0], 62.0 * scale[1])
    Curveto_r(13.0 * scale[0], 24.0 * scale[1], 11.0 * scale[0],
              29.0 * scale[1], -7.0 * scale[0], 23.0 * scale[1])
    te.end_fill()
    Moveto(80.0 * scale[0], 1320.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              10.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              5.0 * scale[1], 9.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -10.0 * scale[0],
              10.0 * scale[1], -16.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              4.0 * scale[1], -9.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(398.0 * scale[0], 1323.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(80.0 * scale[0], 1290.0 * scale[1], x, y)
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
    Moveto(294.0 * scale[0], 1283.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 108.0 *
              scale[0], -5.0 * scale[1], 115.0 * scale[0], 3.0 * scale[1])
    Curveto_r(2.0 * scale[0], 2.0 * scale[1], -24.0 * scale[0],
              4.0 * scale[1], -59.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-35.0 * scale[0], 0.0 * scale[1], -60.0 *
              scale[0], -3.0 * scale[1], -56.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(420.0 * scale[0], 1280.0 * scale[1], x, y)
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
    Moveto(1010.0 * scale[0], 1278.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -70.0 * scale[1], -55.0 * scale[0], -
              126.0 * scale[1], -111.0 * scale[0], -114.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 3.0 * scale[1], -28.0 * scale[0],
              2.0 * scale[1], -28.0 * scale[0], -2.0 * scale[1])
    Curveto_r(4.0 * scale[0], -24.0 * scale[1], -4.0 * scale[0], -
              32.0 * scale[1], -34.0 * scale[0], -32.0 * scale[1])
    Curveto_r(-51.0 * scale[0], 0.0 * scale[1], -44.0 *
              scale[0], -27.0 * scale[1], 7.0 * scale[0], -29.0 * scale[1])
    Curveto_r(23.0 * scale[0], -1.0 * scale[1], 50.0 *
              scale[0], -3.0 * scale[1], 61.0 * scale[0], -3.0 * scale[1])
    Curveto_r(11.0 * scale[0], -1.0 * scale[1], 39.0 *
              scale[0], -1.0 * scale[1], 62.0 * scale[0], 0.0 * scale[1])
    Curveto_r(40.0 * scale[0], 2.0 * scale[1], 41.0 * scale[0],
              3.0 * scale[1], 47.0 * scale[0], 40.0 * scale[1])
    Curveto_r(13.0 * scale[0], 83.0 * scale[1], 16.0 * scale[0],
              152.0 * scale[1], 6.0 * scale[0], 152.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              6.0 * scale[1], -10.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto_r(-105.0 * scale[0], -138.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              10.0 * scale[1], -9.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0],
              5.0 * scale[1], -16.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 4.0 * scale[0],
              10.0 * scale[1], 9.0 * scale[0], 10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0], -
              4.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(256.0 * scale[0], 1219.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -21.0 * scale[1], -17.0 *
              scale[0], -40.0 * scale[1], -15.0 * scale[0], -42.0 * scale[1])
    Curveto_r(2.0 * scale[0], -2.0 * scale[1], 33.0 * scale[0], -
              10.0 * scale[1], 69.0 * scale[0], -19.0 * scale[1])
    Curveto_r(36.0 * scale[0], -9.0 * scale[1], 76.0 * scale[0], -
              19.0 * scale[1], 90.0 * scale[0], -23.0 * scale[1])
    Curveto_r(49.0 * scale[0], -13.0 * scale[1], -3.0 * scale[0],
              14.0 * scale[1], -58.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-29.0 * scale[0], 9.0 * scale[1], -50.0 * scale[0],
              20.0 * scale[1], -47.0 * scale[0], 25.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], 0.0 * scale[0],
              12.0 * scale[1], -6.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 4.0 * scale[1], -9.0 * scale[0],
              3.0 * scale[1], -5.0 * scale[0], -4.0 * scale[1])
    Curveto_r(4.0 * scale[0], -7.0 * scale[1], 1.0 * scale[0], -
              12.0 * scale[1], -8.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0],
              6.0 * scale[1], -10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(7.0 * scale[0], 18.0 * scale[1], 20.0 * scale[0],
              19.0 * scale[1], 112.0 * scale[0], 1.0 * scale[1])
    Curveto_r(39.0 * scale[0], -7.0 * scale[1], 72.0 * scale[0], -
              11.0 * scale[1], 72.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], -36.0 * scale[0],
              13.0 * scale[1], -80.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-44.0 * scale[0], 8.0 * scale[1], -84.0 * scale[0],
              19.0 * scale[1], -88.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 8.0 * scale[1], -13.0 * scale[0],
              0.0 * scale[1], -26.0 * scale[0], -27.0 * scale[1])
    te.end_fill()
    Moveto(425.0 * scale[0], 1251.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              12.0 * scale[1], 3.0 * scale[0], -15.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 9.0 * scale[0],
              1.0 * scale[1], 9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], -3.0 * scale[0],
              19.0 * scale[1], -12.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(86.0 * scale[0], 1192.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 4.0 * scale[0], -
              34.0 * scale[1], 8.0 * scale[0], -40.0 * scale[1])
    Curveto_r(4.0 * scale[0], -7.0 * scale[1], 2.0 * scale[0], -
              12.0 * scale[1], -5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              4.0 * scale[1], 1.0 * scale[0], -15.0 * scale[1])
    Curveto_r(9.0 * scale[0], -10.0 * scale[1], 31.0 * scale[0], -
              14.0 * scale[1], 82.0 * scale[0], -13.0 * scale[1])
    Curveto_r(41.0 * scale[0], 1.0 * scale[1], 64.0 * scale[0],
              4.0 * scale[1], 56.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 7.0 * scale[1], -9.0 * scale[0],
              9.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 18.0 * scale[0], -
              5.0 * scale[1], 20.0 * scale[0], -11.0 * scale[1])
    Curveto_r(2.0 * scale[0], -6.0 * scale[1], 21.0 * scale[0], -
              9.0 * scale[1], 43.0 * scale[0], -7.0 * scale[1])
    Lineto_r(40.0 * scale[0], 3.0 * scale[1])
    Lineto_r(-58.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-44.0 * scale[0], 17.0 * scale[1], -63.0 * scale[0],
              20.0 * scale[1], -78.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -6.0 * scale[1], -19.0 *
              scale[0], -7.0 * scale[1], -19.0 * scale[0], -2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], 10.0 * scale[0],
              13.0 * scale[1], 23.0 * scale[0], 18.0 * scale[1])
    Curveto_r(12.0 * scale[0], 6.0 * scale[1], 17.0 * scale[0],
              9.0 * scale[1], 10.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-73.0 * scale[0], -16.0 * scale[1], -83.0 *
              scale[0], -16.0 * scale[1], -83.0 * scale[0], -2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], -30.0 * scale[0],
              48.0 * scale[1], -41.0 * scale[0], 48.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              13.0 * scale[1], -3.0 * scale[0], -28.0 * scale[1])
    te.end_fill()
    Moveto_r(49.0 * scale[0], -60.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -11.0 * scale[0],
              0.0 * scale[1], -18.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 10.0 * scale[1], -8.0 * scale[0],
              11.0 * scale[1], 6.0 * scale[0], 5.0 * scale[1])
    Curveto_r(10.0 * scale[0], -3.0 * scale[1], 15.0 * scale[0], -
              9.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(1041.0 * scale[0], 1204.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(846.0 * scale[0], 1186.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -11.0 * scale[1], 2.0 * scale[0], -
              21.0 * scale[1], -7.0 * scale[0], -27.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -6.0 * scale[1], -11.0 *
              scale[0], -9.0 * scale[1], -1.0 * scale[0], -9.0 * scale[1])
    Curveto_r(18.0 * scale[0], 0.0 * scale[1], 27.0 * scale[0],
              29.0 * scale[1], 13.0 * scale[0], 43.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              8.0 * scale[1], -5.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(388.0 * scale[0], 1173.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(455.0 * scale[0], 1170.0 * scale[1], x, y)
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
    Moveto(765.0 * scale[0], 1160.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-40.0 * scale[0], -7.0 * scale[1])
    Lineto_r(48.0 * scale[0], -2.0 * scale[1])
    Curveto_r(30.0 * scale[0], 0.0 * scale[1], 46.0 * scale[0],
              3.0 * scale[1], 42.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -7.0 * scale[0],
              9.0 * scale[1], -8.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -1.0 * scale[1], -20.0 *
              scale[0], -5.0 * scale[1], -42.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(658.0 * scale[0], 1153.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(428.0 * scale[0], 1113.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(649.0 * scale[0], 1107.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -5.0 * scale[1], 32.0 * scale[0], -
              7.0 * scale[1], 62.0 * scale[0], -5.0 * scale[1])
    Lineto_r(54.0 * scale[0], 3.0 * scale[1])
    Lineto_r(-62.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-34.0 * scale[0], 3.0 * scale[1], -58.0 * scale[0],
              1.0 * scale[1], -54.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(80.0 * scale[0], 1077.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 12.0 * scale[0], -
              14.0 * scale[1], 30.0 * scale[0], -14.0 * scale[1])
    Curveto_r(18.0 * scale[0], 0.0 * scale[1], 30.0 * scale[0],
              6.0 * scale[1], 30.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -12.0 * scale[0],
              13.0 * scale[1], -30.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 0.0 * scale[1], -30.0 * scale[0], -
              5.0 * scale[1], -30.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(950.0 * scale[0], 1073.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -3.0 * scale[1], -23.0 * scale[0], -
              13.0 * scale[1], -33.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -14.0 * scale[1], -19.0 *
              scale[0], -14.0 * scale[1], -27.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 8.0 * scale[1], -10.0 * scale[0],
              13.0 * scale[1], -11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -3.0 * scale[1], -2.0 * scale[0], -
              13.0 * scale[1], -4.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -15.0 * scale[1], 1.0 * scale[0], -
              18.0 * scale[1], 16.0 * scale[0], -14.0 * scale[1])
    Curveto_r(17.0 * scale[0], 4.0 * scale[1], 19.0 * scale[0],
              2.0 * scale[1], 13.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -17.0 * scale[1], -1.0 *
              scale[0], -15.0 * scale[1], 19.0 * scale[0], 9.0 * scale[1])
    Curveto_r(32.0 * scale[0], 38.0 * scale[1], 76.0 * scale[0],
              50.0 * scale[1], 95.0 * scale[0], 26.0 * scale[1])
    Curveto_r(10.0 * scale[0], -13.0 * scale[1], 12.0 *
              scale[0], -13.0 * scale[1], 12.0 * scale[0], -1.0 * scale[1])
    Curveto_r(0.0 * scale[0], 32.0 * scale[1], -38.0 * scale[0],
              47.0 * scale[1], -80.0 * scale[0], 32.0 * scale[1])
    te.end_fill()
    Moveto(180.0 * scale[0], 1035.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(11.0 * scale[0], -12.0 * scale[1], 20.0 * scale[0], -
              28.0 * scale[1], 20.0 * scale[0], -35.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              11.0 * scale[1], 12.0 * scale[0], -2.0 * scale[1])
    Curveto_r(10.0 * scale[0], 10.0 * scale[1], 7.0 * scale[0],
              16.0 * scale[1], -10.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 8.0 * scale[1], -20.0 * scale[0],
              19.0 * scale[1], -18.0 * scale[0], 23.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], -2.0 * scale[0],
              8.0 * scale[1], -10.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -10.0 *
              scale[0], -5.0 * scale[1], 6.0 * scale[0], -22.0 * scale[1])
    te.end_fill()
    Moveto(825.0 * scale[0], 1020.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -3.0 * scale[0], -
              10.0 * scale[1], 1.0 * scale[0], -10.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], -2.0 * scale[0], -
              10.0 * scale[1], -13.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-33.0 * scale[0], -38.0 * scale[1], -38.0 *
              scale[0], -55.0 * scale[1], -8.0 * scale[0], -28.0 * scale[1])
    Curveto_r(58.0 * scale[0], 51.0 * scale[1], 58.0 * scale[0],
              50.0 * scale[1], 40.0 * scale[0], 50.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0],
              5.0 * scale[1], -10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 4.0 * scale[0],
              10.0 * scale[1], 1.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              4.0 * scale[1], -11.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(216.0 * scale[0], 989.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -23.0 * scale[1], -21.0 *
              scale[0], -33.0 * scale[1], -3.0 * scale[0], -23.0 * scale[1])
    Curveto_r(7.0 * scale[0], 4.0 * scale[1], 9.0 * scale[0],
              3.0 * scale[1], 4.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -5.0 * scale[1], -13.0 * scale[0], -
              10.0 * scale[1], -18.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-22.0 * scale[0], -3.0 * scale[1], -23.0 *
              scale[0], -5.0 * scale[1], -9.0 * scale[0], -14.0 * scale[1])
    Curveto_r(12.0 * scale[0], -8.0 * scale[1], 9.0 * scale[0], -
              10.0 * scale[1], -12.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -28.0 *
              scale[0], -4.0 * scale[1], -28.0 * scale[0], -9.0 * scale[1])
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 26.0 * scale[0], -
              32.0 * scale[1], 35.0 * scale[0], -23.0 * scale[1])
    Curveto_r(4.0 * scale[0], 4.0 * scale[1], 2.0 * scale[0], -
              4.0 * scale[1], -5.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -15.0 * scale[1], -8.0 * scale[0], -
              21.0 * scale[1], -1.0 * scale[0], -17.0 * scale[1])
    Curveto_r(7.0 * scale[0], 4.0 * scale[1], 11.0 * scale[0], -
              1.0 * scale[1], 11.0 * scale[0], -13.0 * scale[1])
    Curveto_r(0.0 * scale[0], -27.0 * scale[1], -10.0 * scale[0], -
              51.0 * scale[1], -22.0 * scale[0], -51.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0],
              6.0 * scale[1], -2.0 * scale[0], 13.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], -2.0 * scale[0],
              4.0 * scale[1], -13.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -10.0 * scale[1], -25.0 *
              scale[0], -18.0 * scale[1], -31.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              7.0 * scale[1], -12.0 * scale[0], -15.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 5.0 * scale[0], -
              15.0 * scale[1], 11.0 * scale[0], -15.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              5.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], 3.0 * scale[0],
              10.0 * scale[1], 14.0 * scale[0], 10.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 29.0 * scale[0],
              8.0 * scale[1], 39.0 * scale[0], 18.0 * scale[1])
    Curveto_r(25.0 * scale[0], 24.0 * scale[1], 54.0 * scale[0],
              28.0 * scale[1], 45.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -11.0 * scale[1], -2.0 *
              scale[0], -15.0 * scale[1], 4.0 * scale[0], -11.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 13.0 * scale[0],
              0.0 * scale[1], 17.0 * scale[0], -8.0 * scale[1])
    Curveto_r(8.0 * scale[0], -23.0 * scale[1], 44.0 *
              scale[0], -18.0 * scale[1], 52.0 * scale[0], 7.0 * scale[1])
    Lineto_r(7.0 * scale[0], 23.0 * scale[1])
    Lineto_r(8.0 * scale[0], -23.0 * scale[1])
    Curveto_r(5.0 * scale[0], -12.0 * scale[1], 15.0 * scale[0], -
              22.0 * scale[1], 24.0 * scale[0], -22.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0], -
              4.0 * scale[1], 5.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -11.0 * scale[1], -9.0 * scale[0], -
              28.0 * scale[1], -5.0 * scale[0], -37.0 * scale[1])
    Curveto_r(5.0 * scale[0], -13.0 * scale[1], 11.0 *
              scale[0], -9.0 * scale[1], 26.0 * scale[0], 20.0 * scale[1])
    Curveto_r(13.0 * scale[0], 25.0 * scale[1], 29.0 * scale[0],
              40.0 * scale[1], 54.0 * scale[0], 48.0 * scale[1])
    Curveto_r(19.0 * scale[0], 6.0 * scale[1], 33.0 * scale[0],
              16.0 * scale[1], 30.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 5.0 * scale[1], -1.0 * scale[0],
              9.0 * scale[1], 6.0 * scale[0], 9.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              2.0 * scale[1], 7.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -16.0 * scale[0],
              1.0 * scale[1], -29.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -5.0 * scale[1], -18.0 * scale[0], -
              10.0 * scale[1], -10.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -1.0 * scale[1], 12.0 *
              scale[0], -4.0 * scale[1], 9.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -11.0 * scale[1], -87.0 * scale[0],
              17.0 * scale[1], -92.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 25.0 * scale[1], -20.0 * scale[0],
              116.0 * scale[1], -18.0 * scale[0], 125.0 * scale[1])
    Curveto_r(1.0 * scale[0], 4.0 * scale[1], -5.0 * scale[0],
              7.0 * scale[1], -13.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0],
              3.0 * scale[1], -15.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], -13.0 * scale[0],
              14.0 * scale[1], -29.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-27.0 * scale[0], 16.0 * scale[1], -30.0 * scale[0],
              16.0 * scale[1], -45.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(75.0 * scale[0], 940.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -15.0 * scale[1], -1.0 * scale[0], -
              23.0 * scale[1], 21.0 * scale[0], -18.0 * scale[1])
    Curveto_r(15.0 * scale[0], 3.0 * scale[1], 16.0 * scale[0],
              4.0 * scale[1], 1.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 9.0 * scale[1], -17.0 * scale[0],
              10.0 * scale[1], -22.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(1031.0 * scale[0], 924.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(70.0 * scale[0], 899.0 * scale[1], x, y)
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
    Moveto(755.0 * scale[0], 869.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -17.0 * scale[1], -4.0 * scale[0], -
              33.0 * scale[1], -1.0 * scale[0], -36.0 * scale[1])
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], 6.0 * scale[0],
              3.0 * scale[1], 6.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], 5.0 * scale[0],
              22.0 * scale[1], 10.0 * scale[0], 22.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              7.0 * scale[1], 10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 27.0 * scale[1], -18.0 * scale[0],
              16.0 * scale[1], -25.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(1021.0 * scale[0], 864.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(733.0 * scale[0], 800.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -36.0 * scale[1], 2.0 * scale[0], -
              50.0 * scale[1], 4.0 * scale[0], -32.0 * scale[1])
    Curveto_r(2.0 * scale[0], 17.0 * scale[1], 2.0 * scale[0],
              47.0 * scale[1], 0.0 * scale[0], 65.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 17.0 * scale[1], -4.0 * scale[0],
              3.0 * scale[1], -4.0 * scale[0], -33.0 * scale[1])
    te.end_fill()
    Moveto(1027.0 * scale[0], 708.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -85.0 * scale[1], 1.0 * scale[0], -
              138.0 * scale[1], -5.0 * scale[0], -138.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              10.0 * scale[1], -15.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -22.0 * scale[1], -6.0 *
              scale[0], -22.0 * scale[1], 13.0 * scale[0], 2.0 * scale[1])
    Curveto_r(21.0 * scale[0], 27.0 * scale[1], 25.0 * scale[0],
              118.0 * scale[1], 10.0 * scale[0], 235.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 39.0 * scale[1], -6.0 * scale[0],
              13.0 * scale[1], -3.0 * scale[0], -77.0 * scale[1])
    te.end_fill()
    Moveto(70.0 * scale[0], 793.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -21.0 * scale[1], 2.0 * scale[0], -
              24.0 * scale[1], 15.0 * scale[0], -13.0 * scale[1])
    Curveto_r(8.0 * scale[0], 7.0 * scale[1], 15.0 * scale[0],
              16.0 * scale[1], 15.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], -7.0 * scale[0],
              10.0 * scale[1], -15.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 4.0 * scale[1], -15.0 * scale[0], -
              2.0 * scale[1], -15.0 * scale[0], -21.0 * scale[1])
    te.end_fill()
    Moveto(477.0 * scale[0], 814.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -12.0 * scale[1], 3.0 * scale[0], -
              22.0 * scale[1], 24.0 * scale[0], -17.0 * scale[1])
    Curveto_r(16.0 * scale[0], 4.0 * scale[1], 17.0 * scale[0],
              8.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 10.0 * scale[1], -23.0 * scale[0],
              11.0 * scale[1], -31.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(530.0 * scale[0], 806.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 5.0 * scale[0], -
              16.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              4.0 * scale[1], 10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -4.0 * scale[0],
              13.0 * scale[1], -10.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0], -
              1.0 * scale[1], -10.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(753.0 * scale[0], 765.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -33.0 * scale[1], 2.0 * scale[0], -
              45.0 * scale[1], 4.0 * scale[0], -27.0 * scale[1])
    Curveto_r(2.0 * scale[0], 18.0 * scale[1], 2.0 * scale[0],
              45.0 * scale[1], 0.0 * scale[0], 60.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 15.0 * scale[1], -4.0 * scale[0],
              0.0 * scale[1], -4.0 * scale[0], -33.0 * scale[1])
    te.end_fill()
    Moveto(572.0 * scale[0], 793.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -5.0 * scale[1], 33.0 * scale[0], -
              48.0 * scale[1], 53.0 * scale[0], -48.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              4.0 * scale[1], 11.0 * scale[0], -10.0 * scale[1])
    Curveto_r(2.0 * scale[0], -24.0 * scale[1], 21.0 * scale[0], -
              58.0 * scale[1], 27.0 * scale[0], -48.0 * scale[1])
    Curveto_r(9.0 * scale[0], 14.0 * scale[1], -33.0 * scale[0],
              75.0 * scale[1], -61.0 * scale[0], 89.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 6.0 * scale[1], -19.0 * scale[0],
              14.0 * scale[1], -15.0 * scale[0], 17.0 * scale[1])
    Curveto_r(7.0 * scale[0], 8.0 * scale[1], 4.0 * scale[0],
              8.0 * scale[1], -15.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(67.0 * scale[0], 739.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -13.0 * scale[1], 8.0 * scale[0], -
              18.0 * scale[1], 11.0 * scale[0], -10.0 * scale[1])
    Curveto_r(2.0 * scale[0], 7.0 * scale[1], -1.0 * scale[0],
              18.0 * scale[1], -6.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 8.0 * scale[1], -9.0 * scale[0],
              4.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(133.0 * scale[0], 741.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -16.0 * scale[1], -9.0 *
              scale[0], -20.0 * scale[1], 8.0 * scale[0], -24.0 * scale[1])
    Curveto_r(20.0 * scale[0], -5.0 * scale[1], 22.0 *
              scale[0], -2.0 * scale[1], 11.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 17.0 * scale[1], -8.0 * scale[0],
              17.0 * scale[1], -19.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(68.0 * scale[0], 678.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -48.0 * scale[1], 25.0 * scale[0], -
              62.0 * scale[1], 48.0 * scale[0], -37.0 * scale[1])
    Curveto_r(18.0 * scale[0], 20.0 * scale[1], 18.0 * scale[0],
              20.0 * scale[1], -10.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-25.0 * scale[0], -6.0 * scale[1], -27.0 *
              scale[0], -4.0 * scale[1], -22.0 * scale[0], 13.0 * scale[1])
    Curveto_r(4.0 * scale[0], 12.0 * scale[1], 1.0 * scale[0],
              25.0 * scale[1], -7.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 9.0 * scale[1], -13.0 * scale[0],
              6.0 * scale[1], -9.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(731.0 * scale[0], 694.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(303.0 * scale[0], 664.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-15.0 * scale[0], -15.0 * scale[1], -17.0 *
              scale[0], -54.0 * scale[1], -4.0 * scale[0], -54.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 23.0 * scale[0],
              60.0 * scale[1], 17.0 * scale[0], 66.0 * scale[1])
    Curveto_r(0.0 * scale[0], 1.0 * scale[1], -7.0 * scale[0], -
              4.0 * scale[1], -13.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(668.0 * scale[0], 670.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -17.0 * scale[1], 9.0 * scale[0], -
              66.0 * scale[1], 18.0 * scale[0], -58.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              21.0 * scale[1], -3.0 * scale[0], 39.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 21.0 * scale[1], -11.0 * scale[0],
              28.0 * scale[1], -15.0 * scale[0], 19.0 * scale[1])
    te.end_fill()
    Moveto(210.0 * scale[0], 666.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 7.0 * scale[0], -
              9.0 * scale[1], 15.0 * scale[0], -16.0 * scale[1])
    Curveto_r(9.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              8.0 * scale[1], 15.0 * scale[0], -2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -7.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -15.0 * scale[0],
              4.0 * scale[1], -15.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(110.0 * scale[0], 626.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 7.0 * scale[0], -
              9.0 * scale[1], 15.0 * scale[0], -16.0 * scale[1])
    Curveto_r(12.0 * scale[0], -10.0 * scale[1], 15.0 *
              scale[0], -10.0 * scale[1], 15.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], -7.0 * scale[0],
              16.0 * scale[1], -15.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              2.0 * scale[1], -15.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(711.0 * scale[0], 603.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -12.0 * scale[1], -7.0 * scale[0], -
              23.0 * scale[1], -13.0 * scale[0], -26.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -10.0 *
              scale[0], -7.0 * scale[1], -7.0 * scale[0], -11.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 16.0 * scale[0],
              6.0 * scale[1], 30.0 * scale[0], 21.0 * scale[1])
    Curveto_r(13.0 * scale[0], 14.0 * scale[1], 19.0 * scale[0],
              23.0 * scale[1], 12.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -4.0 * scale[1], -14.0 *
              scale[0], -1.0 * scale[1], -16.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 7.0 * scale[1], -6.0 * scale[0],
              3.0 * scale[1], -6.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(154.0 * scale[0], 591.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 14.0 * scale[0], -
              11.0 * scale[1], 25.0 * scale[0], -14.0 * scale[1])
    Curveto_r(14.0 * scale[0], -3.0 * scale[1], 18.0 *
              scale[0], -1.0 * scale[1], 14.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], -14.0 * scale[0],
              14.0 * scale[1], -25.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 0.0 * scale[1], -17.0 *
              scale[0], -4.0 * scale[1], -14.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(210.0 * scale[0], 575.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], 70.0 * scale[0], -
              75.0 * scale[1], 84.0 * scale[0], -75.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 18.0 * scale[0], -
              9.0 * scale[1], 21.0 * scale[0], -21.0 * scale[1])
    Curveto_r(4.0 * scale[0], -11.0 * scale[1], 9.0 * scale[0], -
              18.0 * scale[1], 11.0 * scale[0], -16.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              22.0 * scale[1], -7.0 * scale[0], 44.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 33.0 * scale[1], -17.0 * scale[0],
              39.0 * scale[1], -35.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -2.0 * scale[1], -27.0 * scale[0],
              3.0 * scale[1], -35.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 17.0 * scale[1], -39.0 * scale[0],
              29.0 * scale[1], -39.0 * scale[0], 18.0 * scale[1])
    te.end_fill()
    Moveto(442.0 * scale[0], 530.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(360.0 * scale[0], 536.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(963.0 * scale[0], 527.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], -3.0 * scale[0], -
              14.0 * scale[1], -14.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -1.0 * scale[1], -26.0 *
              scale[0], -9.0 * scale[1], -35.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -18.0 * scale[1], -28.0 *
              scale[0], -21.0 * scale[1], -19.0 * scale[0], -6.0 * scale[1])
    Curveto_r(9.0 * scale[0], 14.0 * scale[1], -1.0 * scale[0],
              13.0 * scale[1], -34.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -8.0 * scale[1], -31.0 *
              scale[0], -11.0 * scale[1], -34.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 3.0 * scale[1], -14.0 * scale[0],
              0.0 * scale[1], -23.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -11.0 * scale[1], -16.0 *
              scale[0], -26.0 * scale[1], -11.0 * scale[0], -94.0 * scale[1])
    Curveto_r(7.0 * scale[0], -81.0 * scale[1], 1.0 * scale[0], -
              129.0 * scale[1], -13.0 * scale[0], -120.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -60.0 * scale[0], -
              50.0 * scale[1], -60.0 * scale[0], -64.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], -15.0 * scale[0], -
              14.0 * scale[1], -33.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-33.0 * scale[0], -16.0 * scale[1], -87.0 *
              scale[0], -14.0 * scale[1], -87.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -13.0 * scale[0],
              9.0 * scale[1], -30.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -30.0 * scale[0],
              5.0 * scale[1], -30.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -13.0 * scale[0],
              31.0 * scale[1], -30.0 * scale[0], 58.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 37.0 * scale[1], -30.0 * scale[0],
              42.0 * scale[1], -30.0 * scale[0], 25.0 * scale[1])
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], 5.0 * scale[0], -
              23.0 * scale[1], 10.0 * scale[0], -23.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0], -
              3.0 * scale[1], 8.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -18.0 * scale[1], 14.0 * scale[0], -
              53.0 * scale[1], 24.0 * scale[0], -47.0 * scale[1])
    Curveto_r(7.0 * scale[0], 5.0 * scale[1], 9.0 * scale[0],
              1.0 * scale[1], 5.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -20.0 * scale[1], 9.0 * scale[0], -
              32.0 * scale[1], 44.0 * scale[0], -29.0 * scale[1])
    Curveto_r(15.0 * scale[0], 1.0 * scale[1], 33.0 * scale[0], -
              6.0 * scale[1], 45.0 * scale[0], -19.0 * scale[1])
    Curveto_r(18.0 * scale[0], -20.0 * scale[1], 18.0 *
              scale[0], -22.0 * scale[1], 1.0 * scale[0], -34.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -17.0 * scale[0], -
              15.0 * scale[1], -17.0 * scale[0], -19.0 * scale[1])
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], 145.0 *
              scale[0], -5.0 * scale[1], 170.0 * scale[0], 9.0 * scale[1])
    Curveto_r(14.0 * scale[0], 8.0 * scale[1], 22.0 * scale[0],
              14.0 * scale[1], 19.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -1.0 * scale[0],
              19.0 * scale[1], 6.0 * scale[0], 43.0 * scale[1])
    Curveto_r(7.0 * scale[0], 23.0 * scale[1], 18.0 * scale[0],
              41.0 * scale[1], 25.0 * scale[0], 39.0 * scale[1])
    Curveto_r(8.0 * scale[0], -2.0 * scale[1], 10.0 * scale[0],
              5.0 * scale[1], 7.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 79.0 * scale[1], -27.0 * scale[0],
              178.0 * scale[1], -17.0 * scale[0], 198.0 * scale[1])
    Curveto_r(7.0 * scale[0], 13.0 * scale[1], 7.0 * scale[0],
              20.0 * scale[1], 0.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0],
              4.0 * scale[1], -10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], 63.0 * scale[0],
              25.0 * scale[1], 102.0 * scale[0], 24.0 * scale[1])
    Curveto_r(16.0 * scale[0], 0.0 * scale[1], 26.0 * scale[0],
              3.0 * scale[1], 23.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], 8.0 * scale[0],
              14.0 * scale[1], 24.0 * scale[0], 21.0 * scale[1])
    Curveto_r(33.0 * scale[0], 15.0 * scale[1], 49.0 * scale[0],
              49.0 * scale[1], 24.0 * scale[0], 49.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              6.0 * scale[1], -10.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto_r(-156.0 * scale[0], -284.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -10.0 * scale[1], -5.0 *
              scale[0], -4.0 * scale[1], -5.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], 2.0 * scale[0],
              24.0 * scale[1], 5.0 * scale[0], 18.0 * scale[1])
    Curveto_r(2.0 * scale[0], -7.0 * scale[1], 2.0 * scale[0], -
              21.0 * scale[1], 0.0 * scale[0], -30.0 * scale[1])
    te.end_fill()
    Moveto(360.0 * scale[0], 466.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 5.0 * scale[0], -
              16.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              4.0 * scale[1], 10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -4.0 * scale[0],
              13.0 * scale[1], -10.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0], -
              1.0 * scale[1], -10.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(442.0 * scale[0], 370.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(11.0 * scale[0], -33.0 * scale[1], 24.0 * scale[0], -
              60.0 * scale[1], 29.0 * scale[0], -60.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              5.0 * scale[1], 9.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              10.0 * scale[1], -11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0],
              4.0 * scale[1], -5.0 * scale[0], 8.0 * scale[1])
    Curveto_r(5.0 * scale[0], 8.0 * scale[1], -29.0 * scale[0],
              92.0 * scale[1], -38.0 * scale[0], 92.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], 4.0 * scale[0], -
              27.0 * scale[1], 16.0 * scale[0], -60.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#dfb796')
    te.end_fill()
    Moveto(457.0 * scale[0], 1433.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -10.0 * scale[1], -8.0 *
              scale[0], -93.0 * scale[1], 2.0 * scale[0], -93.0 * scale[1])
    Curveto_r(15.0 * scale[0], 0.0 * scale[1], 23.0 * scale[0],
              18.0 * scale[1], 11.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 10.0 * scale[1], -12.0 * scale[0],
              43.0 * scale[1], 7.0 * scale[0], 47.0 * scale[1])
    Curveto_r(14.0 * scale[0], 3.0 * scale[1], 14.0 * scale[0],
              4.0 * scale[1], 1.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 7.0 * scale[1], -18.0 * scale[0],
              10.0 * scale[1], -21.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(620.0 * scale[0], 1415.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -13.0 * scale[1], -10.0 *
              scale[0], -14.0 * scale[1], 5.0 * scale[0], -9.0 * scale[1])
    Curveto_r(10.0 * scale[0], 4.0 * scale[1], 21.0 * scale[0],
              1.0 * scale[1], 26.0 * scale[0], -7.0 * scale[1])
    Curveto_r(6.0 * scale[0], -11.0 * scale[1], 9.0 *
              scale[0], -8.0 * scale[1], 9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 25.0 * scale[1], -22.0 * scale[0],
              29.0 * scale[1], -40.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(510.0 * scale[0], 1384.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 5.0 * scale[0], -
              12.0 * scale[1], 10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 8.0 * scale[0],
              11.0 * scale[1], 5.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 14.0 * scale[1], -15.0 * scale[0],
              11.0 * scale[1], -15.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(587.0 * scale[0], 1393.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -12.0 * scale[1], -7.0 *
              scale[0], -23.0 * scale[1], 11.0 * scale[0], -22.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              3.0 * scale[1], 4.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 2.0 * scale[1], -10.0 * scale[0],
              9.0 * scale[1], -6.0 * scale[0], 14.0 * scale[1])
    Curveto_r(6.0 * scale[0], 10.0 * scale[1], 0.0 * scale[0],
              12.0 * scale[1], -9.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(220.0 * scale[0], 1370.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(8.0 * scale[0], -5.0 * scale[1], 20.0 * scale[0], -
              10.0 * scale[1], 25.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 3.0 * scale[0],
              5.0 * scale[1], -5.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -19.0 * scale[0],
              10.0 * scale[1], -25.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -3.0 * scale[0], -
              5.0 * scale[1], 5.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(651.0 * scale[0], 1373.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -9.0 * scale[0], -
              13.0 * scale[1], -18.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -1.0 * scale[1], -17.0 *
              scale[0], -1.0 * scale[1], 0.0 * scale[0], -11.0 * scale[1])
    Curveto_r(22.0 * scale[0], -13.0 * scale[1], 30.0 *
              scale[0], -7.0 * scale[1], 24.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 10.0 * scale[1], -5.0 * scale[0],
              12.0 * scale[1], -6.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(885.0 * scale[0], 1360.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(941.0 * scale[0], 1367.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -1.0 * scale[1], 13.0 * scale[0], -
              9.0 * scale[1], 24.0 * scale[0], -17.0 * scale[1])
    Curveto_r(19.0 * scale[0], -14.0 * scale[1], 19.0 *
              scale[0], -14.0 * scale[1], 6.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 9.0 * scale[1], -18.0 * scale[0],
              17.0 * scale[1], -24.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              1.0 * scale[1], -6.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(510.0 * scale[0], 1350.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(560.0 * scale[0], 1350.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(14.0 * scale[0], -4.0 * scale[1], 32.0 *
              scale[0], -8.0 * scale[1], 40.0 * scale[0], -9.0 * scale[1])
    Curveto_r(13.0 * scale[0], -1.0 * scale[1], 13.0 * scale[0],
              0.0 * scale[1], 0.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -26.0 * scale[0],
              9.0 * scale[1], -40.0 * scale[0], 9.0 * scale[1])
    Lineto_r(-25.0 * scale[0], -1.0 * scale[1])
    Lineto_r(25.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(850.0 * scale[0], 1320.0 * scale[1], x, y)
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
    Moveto(261.0 * scale[0], 1314.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(641.0 * scale[0], 1305.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -19.0 * scale[1], 18.0 * scale[0], -
              51.0 * scale[1], 18.0 * scale[0], -35.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -4.0 * scale[0],
              22.0 * scale[1], -9.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 8.0 * scale[1], -9.0 * scale[0],
              11.0 * scale[1], -9.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(446.0 * scale[0], 1278.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -13.0 * scale[1], -5.0 * scale[0], -
              32.0 * scale[1], -5.0 * scale[0], -43.0 * scale[1])
    Curveto_r(1.0 * scale[0], -11.0 * scale[1], 5.0 * scale[0], -
              2.0 * scale[1], 10.0 * scale[0], 19.0 * scale[1])
    Curveto_r(10.0 * scale[0], 42.0 * scale[1], 6.0 * scale[0],
              62.0 * scale[1], -5.0 * scale[0], 24.0 * scale[1])
    te.end_fill()
    Moveto(831.0 * scale[0], 1264.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(642.0 * scale[0], 1208.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -30.0 * scale[1], -10.0 *
              scale[0], -31.0 * scale[1], 3.0 * scale[0], -14.0 * scale[1])
    Curveto_r(13.0 * scale[0], 17.0 * scale[1], 21.0 * scale[0],
              46.0 * scale[1], 12.0 * scale[0], 46.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              15.0 * scale[1], -15.0 * scale[0], -32.0 * scale[1])
    te.end_fill()
    Moveto(54.0 * scale[0], 1000.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -118.0 * scale[1], 2.0 * scale[0], -
              167.0 * scale[1], 3.0 * scale[0], -107.0 * scale[1])
    Curveto_r(2.0 * scale[0], 59.0 * scale[1], 2.0 * scale[0],
              155.0 * scale[1], 0.0 * scale[0], 215.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 59.0 * scale[1], -3.0 * scale[0],
              10.0 * scale[1], -3.0 * scale[0], -108.0 * scale[1])
    te.end_fill()
    Moveto(190.0 * scale[0], 1190.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-21.0 * scale[0], -7.0 * scale[1], -21.0 *
              scale[0], -8.0 * scale[1], -5.0 * scale[0], -9.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 27.0 * scale[0],
              4.0 * scale[1], 35.0 * scale[0], 9.0 * scale[1])
    Curveto_r(18.0 * scale[0], 11.0 * scale[1], 5.0 * scale[0],
              11.0 * scale[1], -30.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(460.0 * scale[0], 1186.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 7.0 * scale[0], -
              9.0 * scale[1], 15.0 * scale[0], -16.0 * scale[1])
    Curveto_r(13.0 * scale[0], -11.0 * scale[1], 14.0 *
              scale[0], -10.0 * scale[1], 9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 14.0 * scale[1], -24.0 * scale[0],
              23.0 * scale[1], -24.0 * scale[0], 12.0 * scale[1])
    te.end_fill()
    Moveto(880.0 * scale[0], 1180.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(8.0 * scale[0], -5.0 * scale[1], 22.0 * scale[0], -
              9.0 * scale[1], 30.0 * scale[0], -9.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0],
              3.0 * scale[1], -5.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-27.0 * scale[0], 12.0 * scale[1], -43.0 * scale[0],
              12.0 * scale[1], -25.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(508.0 * scale[0], 1148.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -5.0 * scale[1], 16.0 * scale[0], -
              8.0 * scale[1], 23.0 * scale[0], -6.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 3.0 * scale[0],
              7.0 * scale[1], -10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 4.0 * scale[1], -21.0 * scale[0],
              3.0 * scale[1], -13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(568.0 * scale[0], 1143.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(1044.0 * scale[0], 885.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -110.0 * scale[1], 2.0 * scale[0], -
              156.0 * scale[1], 3.0 * scale[0], -103.0 * scale[1])
    Curveto_r(2.0 * scale[0], 53.0 * scale[1], 2.0 * scale[0],
              143.0 * scale[1], 0.0 * scale[0], 200.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 57.0 * scale[1], -3.0 * scale[0],
              13.0 * scale[1], -3.0 * scale[0], -97.0 * scale[1])
    te.end_fill()
    Moveto(92.0 * scale[0], 990.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(146.0 * scale[0], 971.0 * scale[1], x, y)
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
    Moveto(143.0 * scale[0], 835.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -10.0 * scale[1], -9.0 *
              scale[0], -14.0 * scale[1], 2.0 * scale[0], -19.0 * scale[1])
    Curveto_r(17.0 * scale[0], -6.0 * scale[1], 26.0 * scale[0],
              5.0 * scale[1], 17.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 8.0 * scale[1], -11.0 * scale[0],
              7.0 * scale[1], -19.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(723.0 * scale[0], 750.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -41.0 * scale[1], 2.0 * scale[0], -
              58.0 * scale[1], 4.0 * scale[0], -37.0 * scale[1])
    Curveto_r(2.0 * scale[0], 20.0 * scale[1], 2.0 * scale[0],
              54.0 * scale[1], 0.0 * scale[0], 75.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 20.0 * scale[1], -4.0 * scale[0],
              3.0 * scale[1], -4.0 * scale[0], -38.0 * scale[1])
    te.end_fill()
    Moveto(416.0 * scale[0], 763.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-46.0 * scale[0], -12.0 * scale[1], -54.0 *
              scale[0], -42.0 * scale[1], -20.0 * scale[0], -74.0 * scale[1])
    Curveto_r(14.0 * scale[0], -13.0 * scale[1], 25.0 * scale[0], -
              19.0 * scale[1], 24.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 47.0 * scale[1], 20.0 * scale[0],
              79.0 * scale[1], 48.0 * scale[0], 51.0 * scale[1])
    Curveto_r(19.0 * scale[0], -19.0 * scale[1], 9.0 * scale[0], -
              44.0 * scale[1], -23.0 * scale[0], -56.0 * scale[1])
    Curveto_r(-28.0 * scale[0], -11.0 * scale[1], -33.0 *
              scale[0], -41.0 * scale[1], -10.0 * scale[0], -60.0 * scale[1])
    Curveto_r(8.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              21.0 * scale[1], 15.0 * scale[0], -31.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 6.0 * scale[0], -
              19.0 * scale[1], 14.0 * scale[0], -19.0 * scale[1])
    Curveto_r(17.0 * scale[0], 0.0 * scale[1], 75.0 * scale[0],
              67.0 * scale[1], 82.0 * scale[0], 96.0 * scale[1])
    Curveto_r(6.0 * scale[0], 23.0 * scale[1], -15.0 * scale[0],
              72.0 * scale[1], -39.0 * scale[0], 92.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 14.0 * scale[1], -65.0 * scale[0],
              22.0 * scale[1], -91.0 * scale[0], 15.0 * scale[1])
    te.end_fill()
    Moveto(661.0 * scale[0], 720.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(14.0 * scale[0], -31.0 * scale[1], 19.0 * scale[0], -
              36.0 * scale[1], 19.0 * scale[0], -24.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -7.0 * scale[0],
              19.0 * scale[1], -16.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 18.0 * scale[1], -14.0 * scale[0],
              18.0 * scale[1], -3.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(333.0 * scale[0], 669.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-28.0 * scale[0], -44.0 * scale[1], -30.0 * scale[0], -
              113.0 * scale[1], -6.0 * scale[0], -167.0 * scale[1])
    Lineto_r(16.0 * scale[0], -37.0 * scale[1])
    Lineto_r(9.0 * scale[0], 80.0 * scale[1])
    Curveto_r(4.0 * scale[0], 44.0 * scale[1], 7.0 * scale[0],
              98.0 * scale[1], 6.0 * scale[0], 120.0 * scale[1])
    Lineto_r(-3.0 * scale[0], 40.0 * scale[1])
    Lineto_r(-22.0 * scale[0], -36.0 * scale[1])
    te.end_fill()
    Moveto(680.0 * scale[0], 679.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 7.0 * scale[0], -
              22.0 * scale[1], 15.0 * scale[0], -40.0 * scale[1])
    Curveto_r(8.0 * scale[0], -19.0 * scale[1], 14.0 * scale[0], -
              27.0 * scale[1], 14.0 * scale[0], -19.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -28.0 * scale[0],
              72.0 * scale[1], -29.0 * scale[0], 59.0 * scale[1])
    te.end_fill()
    Moveto(1043.0 * scale[0], 630.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -30.0 * scale[1], 2.0 * scale[0], -
              43.0 * scale[1], 4.0 * scale[0], -27.0 * scale[1])
    Curveto_r(2.0 * scale[0], 15.0 * scale[1], 2.0 * scale[0],
              39.0 * scale[1], 0.0 * scale[0], 55.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 15.0 * scale[1], -4.0 * scale[0],
              2.0 * scale[1], -4.0 * scale[0], -28.0 * scale[1])
    te.end_fill()
    Moveto(817.0 * scale[0], 378.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(8.0 * scale[0], -44.0 * scale[1], 13.0 * scale[0], -
              48.0 * scale[1], 13.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], -4.0 * scale[0],
              34.0 * scale[1], -10.0 * scale[0], 37.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -7.0 * scale[0], -
              6.0 * scale[1], -3.0 * scale[0], -27.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#602b16')
    te.end_fill()
    Moveto(83.0 * scale[0], 1439.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -16.0 * scale[1], -8.0 * scale[0], -
              18.0 * scale[1], -15.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 7.0 * scale[1], -7.0 * scale[0], -
              52.0 * scale[1], -4.0 * scale[0], -144.0 * scale[1])
    Curveto_r(2.0 * scale[0], -99.0 * scale[1], 8.0 * scale[0], -
              163.0 * scale[1], 15.0 * scale[0], -172.0 * scale[1])
    Curveto_r(9.0 * scale[0], -10.0 * scale[1], 8.0 * scale[0], -
              15.0 * scale[1], -3.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -5.0 * scale[1], -14.0 * scale[0], -
              37.0 * scale[1], -14.0 * scale[0], -174.0 * scale[1])
    Curveto_r(0.0 * scale[0], -92.0 * scale[1], 3.0 * scale[0], -
              153.0 * scale[1], 7.0 * scale[0], -134.0 * scale[1])
    Curveto_r(6.0 * scale[0], 33.0 * scale[1], 7.0 * scale[0],
              34.0 * scale[1], 23.0 * scale[0], 18.0 * scale[1])
    Curveto_r(9.0 * scale[0], -9.0 * scale[1], 25.0 * scale[0], -
              17.0 * scale[1], 35.0 * scale[0], -17.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              3.0 * scale[1], -7.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-31.0 * scale[0], 16.0 * scale[1], -38.0 * scale[0],
              65.0 * scale[1], -14.0 * scale[0], 101.0 * scale[1])
    Curveto_r(18.0 * scale[0], 28.0 * scale[1], 34.0 * scale[0],
              34.0 * scale[1], 34.0 * scale[0], 13.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 9.0 * scale[0], -
              22.0 * scale[1], 20.0 * scale[0], -32.0 * scale[1])
    Curveto_r(24.0 * scale[0], -22.0 * scale[1], 25.0 *
              scale[0], -43.0 * scale[1], 5.0 * scale[0], -73.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -20.0 * scale[1], -14.0 *
              scale[0], -21.0 * scale[1], 0.0 * scale[0], -16.0 * scale[1])
    Curveto_r(8.0 * scale[0], 4.0 * scale[1], 17.0 * scale[0],
              16.0 * scale[1], 20.0 * scale[0], 28.0 * scale[1])
    Curveto_r(5.0 * scale[0], 24.0 * scale[1], 2.0 * scale[0],
              76.0 * scale[1], -4.0 * scale[0], 70.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -5.0 * scale[1], -31.0 * scale[0],
              17.0 * scale[1], -31.0 * scale[0], 27.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 12.0 * scale[0],
              9.0 * scale[1], 28.0 * scale[0], 9.0 * scale[1])
    Curveto_r(21.0 * scale[0], 0.0 * scale[1], 24.0 * scale[0],
              2.0 * scale[1], 12.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 9.0 * scale[1], -13.0 * scale[0],
              11.0 * scale[1], 9.0 * scale[0], 14.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(5.0 * scale[0], 5.0 * scale[1], 3.0 * scale[0],
              6.0 * scale[1], -5.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -10.0 * scale[1], -15.0 *
              scale[0], 0.0 * scale[1], 5.0 * scale[0], 23.0 * scale[1])
    Curveto_r(15.0 * scale[0], 18.0 * scale[1], 18.0 * scale[0],
              18.0 * scale[1], 42.0 * scale[0], 3.0 * scale[1])
    Curveto_r(14.0 * scale[0], -9.0 * scale[1], 29.0 * scale[0], -
              21.0 * scale[1], 33.0 * scale[0], -26.0 * scale[1])
    Curveto_r(9.0 * scale[0], -14.0 * scale[1], 22.0 * scale[0],
              0.0 * scale[1], 13.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -20.0 * scale[0],
              18.0 * scale[1], -37.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 9.0 * scale[1], -42.0 * scale[0],
              27.0 * scale[1], -55.0 * scale[0], 40.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 13.0 * scale[1], -33.0 * scale[0],
              24.0 * scale[1], -43.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 0.0 * scale[1], -26.0 * scale[0],
              15.0 * scale[1], -4.0 * scale[0], 24.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 122.0 * scale[0],
              6.0 * scale[1], 251.0 * scale[0], 6.0 * scale[1])
    Curveto_r(130.0 * scale[0], 0.0 * scale[1], 234.0 * scale[0],
              2.0 * scale[1], 232.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 2.0 * scale[1], -127.0 * scale[0],
              5.0 * scale[1], -276.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-222.0 * scale[0], 1.0 * scale[1], -274.0 * scale[0],
              4.0 * scale[1], -284.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 11.0 * scale[1], -9.0 * scale[0],
              14.0 * scale[1], 0.0 * scale[0], 14.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              5.0 * scale[1], 5.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 14.0 * scale[1], -11.0 * scale[0],
              68.0 * scale[1], -3.0 * scale[0], 68.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 39.0 * scale[0], -
              36.0 * scale[1], 39.0 * scale[0], -48.0 * scale[1])
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], 22.0 * scale[0], -
              14.0 * scale[1], 60.0 * scale[0], -2.0 * scale[1])
    Curveto_r(24.0 * scale[0], 8.0 * scale[1], 24.0 * scale[0],
              8.0 * scale[1], -6.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-67.0 * scale[0], 2.0 * scale[1], -97.0 * scale[0],
              88.0 * scale[1], -54.0 * scale[0], 158.0 * scale[1])
    Curveto_r(20.0 * scale[0], 34.0 * scale[1], 54.0 * scale[0],
              48.0 * scale[1], 95.0 * scale[0], 41.0 * scale[1])
    Curveto_r(14.0 * scale[0], -3.0 * scale[1], 25.0 *
              scale[0], -1.0 * scale[1], 25.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -36.0 * scale[0],
              9.0 * scale[1], -80.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-70.0 * scale[0], 0.0 * scale[1], -80.0 * scale[0],
              2.0 * scale[1], -80.0 * scale[0], 18.0 * scale[1])
    Curveto_r(0.0 * scale[0], 24.0 * scale[1], 12.0 * scale[0],
              39.0 * scale[1], 35.0 * scale[0], 45.0 * scale[1])
    Curveto_r(15.0 * scale[0], 3.0 * scale[1], 13.0 * scale[0],
              5.0 * scale[1], -8.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 1.0 * scale[1], -30.0 * scale[0], -
              4.0 * scale[1], -34.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto_r(49.0 * scale[0], -80.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-23.0 * scale[0], -21.0 * scale[1], -42.0 *
              scale[0], -18.0 * scale[1], -42.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], 11.0 * scale[0],
              14.0 * scale[1], 32.0 * scale[0], 14.0 * scale[1])
    Lineto_r(32.0 * scale[0], 0.0 * scale[1])
    Lineto_r(-22.0 * scale[0], -21.0 * scale[1])
    te.end_fill()
    Moveto_r(-27.0 * scale[0], -39.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              10.0 * scale[1], -9.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0],
              5.0 * scale[1], -16.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 4.0 * scale[0],
              10.0 * scale[1], 9.0 * scale[0], 10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0], -
              4.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto_r(-10.0 * scale[0], -30.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              10.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0],
              5.0 * scale[1], -11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              10.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0], -
              4.0 * scale[1], 11.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto_r(45.0 * scale[0], -222.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], 12.0 * scale[0], -
              34.0 * scale[1], 26.0 * scale[0], -49.0 * scale[1])
    Curveto_r(22.0 * scale[0], -23.0 * scale[1], 24.0 * scale[0], -
              30.0 * scale[1], 15.0 * scale[0], -48.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -25.0 * scale[1], -56.0 *
              scale[0], -38.0 * scale[1], -75.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 19.0 * scale[1], -24.0 * scale[0],
              57.0 * scale[1], -5.0 * scale[0], 82.0 * scale[1])
    Curveto_r(24.0 * scale[0], 31.0 * scale[1], 24.0 * scale[0],
              42.0 * scale[1], -1.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -5.0 * scale[1], -20.0 *
              scale[0], -2.0 * scale[1], -20.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], 9.0 * scale[0],
              16.0 * scale[1], 30.0 * scale[0], 16.0 * scale[1])
    Curveto_r(24.0 * scale[0], 0.0 * scale[1], 30.0 * scale[0], -
              4.0 * scale[1], 30.0 * scale[0], -22.0 * scale[1])
    te.end_fill()
    Moveto_r(44.0 * scale[0], -19.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -4.0 * scale[1], 5.0 * scale[0], -
              14.0 * scale[1], 17.0 * scale[0], -23.0 * scale[1])
    Curveto_r(12.0 * scale[0], -8.0 * scale[1], 18.0 * scale[0], -
              19.0 * scale[1], 14.0 * scale[0], -26.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -8.0 * scale[1], -11.0 *
              scale[0], -4.0 * scale[1], -19.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 12.0 * scale[1], -17.0 * scale[0],
              22.0 * scale[1], -23.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -1.0 * scale[1], -10.0 * scale[0],
              4.0 * scale[1], -10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], 6.0 * scale[0],
              13.0 * scale[1], 13.0 * scale[0], 13.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0], -
              4.0 * scale[1], 8.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto_r(-92.0 * scale[0], -140.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-21.0 * scale[0], -24.0 * scale[1], -21.0 *
              scale[0], -24.0 * scale[1], -18.0 * scale[0], 9.0 * scale[1])
    Curveto_r(5.0 * scale[0], 37.0 * scale[1], 4.0 * scale[0],
              36.0 * scale[1], 20.0 * scale[0], 23.0 * scale[1])
    Curveto_r(13.0 * scale[0], -11.0 * scale[1], 12.0 * scale[0], -
              15.0 * scale[1], -2.0 * scale[0], -32.0 * scale[1])
    te.end_fill()
    Moveto(783.0 * scale[0], 1453.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(863.0 * scale[0], 1453.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(15.0 * scale[0], -2.0 * scale[1], 39.0 *
              scale[0], -2.0 * scale[1], 55.0 * scale[0], 0.0 * scale[1])
    Curveto_r(15.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              4.0 * scale[1], -28.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 0.0 * scale[1], -43.0 *
              scale[0], -2.0 * scale[1], -27.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(978.0 * scale[0], 1439.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(22.0 * scale[0], -7.0 * scale[1], 32.0 * scale[0], -
              16.0 * scale[1], 32.0 * scale[0], -29.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 5.0 * scale[0], -
              20.0 * scale[1], 10.0 * scale[0], -20.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              12.0 * scale[1], 10.0 * scale[0], 26.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], 4.0 * scale[0],
              23.0 * scale[1], 13.0 * scale[0], 18.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 9.0 *
              scale[0], -4.0 * scale[1], 5.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 4.0 * scale[1], -29.0 * scale[0],
              9.0 * scale[1], -55.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-45.0 * scale[0], 3.0 * scale[1], -46.0 * scale[0],
              2.0 * scale[1], -15.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(944.0 * scale[0], 1376.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(16.0 * scale[0], -7.0 * scale[1], 36.0 * scale[0], -
              29.0 * scale[1], 46.0 * scale[0], -48.0 * scale[1])
    Curveto_r(15.0 * scale[0], -30.0 * scale[1], 15.0 *
              scale[0], -40.0 * scale[1], 3.0 * scale[0], -80.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -52.0 * scale[1], -30.0 *
              scale[0], -67.0 * scale[1], -76.0 * scale[0], -78.0 * scale[1])
    Curveto_r(-25.0 * scale[0], -6.0 * scale[1], -27.0 *
              scale[0], -8.0 * scale[1], -9.0 * scale[0], -9.0 * scale[1])
    Curveto_r(54.0 * scale[0], -2.0 * scale[1], 102.0 * scale[0],
              53.0 * scale[1], 102.0 * scale[0], 117.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 5.0 * scale[0],
              12.0 * scale[1], 10.0 * scale[0], 12.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0], -
              69.0 * scale[1], -6.0 * scale[0], -152.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -36.0 * scale[1], -8.0 * scale[0], -
              38.0 * scale[1], -42.0 * scale[0], -38.0 * scale[1])
    Curveto_r(-32.0 * scale[0], 0.0 * scale[1], -85.0 * scale[0], -
              19.0 * scale[1], -57.0 * scale[0], -20.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 1.0 * scale[0], -
              7.0 * scale[1], -9.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -8.0 * scale[1], -17.0 * scale[0], -
              18.0 * scale[1], -13.0 * scale[0], -22.0 * scale[1])
    Curveto_r(4.0 * scale[0], -3.0 * scale[1], 15.0 * scale[0],
              1.0 * scale[1], 26.0 * scale[0], 11.0 * scale[1])
    Curveto_r(26.0 * scale[0], 23.0 * scale[1], 84.0 * scale[0],
              32.0 * scale[1], 98.0 * scale[0], 14.0 * scale[1])
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 13.0 * scale[0], -
              36.0 * scale[1], 16.0 * scale[0], -63.0 * scale[1])
    Curveto_r(3.0 * scale[0], -48.0 * scale[1], 3.0 * scale[0], -
              48.0 * scale[1], 5.0 * scale[0], 13.0 * scale[1])
    Curveto_r(1.0 * scale[0], 34.0 * scale[1], -2.0 * scale[0],
              62.0 * scale[1], -6.0 * scale[0], 62.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0],
              28.0 * scale[1], 0.0 * scale[0], 63.0 * scale[1])
    Curveto_r(5.0 * scale[0], 34.0 * scale[1], 11.0 * scale[0],
              104.0 * scale[1], 14.0 * scale[0], 156.0 * scale[1])
    Curveto_r(5.0 * scale[0], 75.0 * scale[1], 4.0 * scale[0],
              93.0 * scale[1], -7.0 * scale[0], 89.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -3.0 * scale[1], -14.0 * scale[0], -
              19.0 * scale[1], -14.0 * scale[0], -40.0 * scale[1])
    Curveto_r(0.0 * scale[0], -20.0 * scale[1], -4.0 * scale[0], -
              40.0 * scale[1], -9.0 * scale[0], -45.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -5.0 * scale[1], -6.0 *
              scale[0], -3.0 * scale[1], -2.0 * scale[0], 5.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              12.0 * scale[1], -3.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0],
              6.0 * scale[1], -11.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 22.0 * scale[1], -26.0 * scale[0],
              46.0 * scale[1], -56.0 * scale[0], 51.0 * scale[1])
    Lineto_r(-29.0 * scale[0], 6.0 * scale[1])
    Lineto_r(29.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(184.0 * scale[0], 1289.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], -2.0 * scale[0], -
              15.0 * scale[1], 4.0 * scale[0], -21.0 * scale[1])
    Curveto_r(6.0 * scale[0], -6.0 * scale[1], 11.0 * scale[0], -
              2.0 * scale[1], 15.0 * scale[0], 11.0 * scale[1])
    Curveto_r(5.0 * scale[0], 22.0 * scale[1], -7.0 * scale[0],
              29.0 * scale[1], -19.0 * scale[0], 10.0 * scale[1])
    te.end_fill()
    Moveto(277.0 * scale[0], 1283.0 * scale[1], x, y)
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
    Moveto(905.0 * scale[0], 1269.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -20.0 * scale[1], 0.0 * scale[0], -
              37.0 * scale[1], 10.0 * scale[0], -27.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 7.0 * scale[0],
              15.0 * scale[1], 10.0 * scale[0], 27.0 * scale[1])
    Curveto_r(5.0 * scale[0], 27.0 * scale[1], -12.0 * scale[0],
              28.0 * scale[1], -20.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(225.0 * scale[0], 1190.0 * scale[1], x, y)
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
    Moveto(188.0 * scale[0], 1153.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(117.0 * scale[0], 1139.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(748.0 * scale[0], 1093.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(28.0 * scale[0], -2.0 * scale[1], 76.0 *
              scale[0], -2.0 * scale[1], 105.0 * scale[0], 0.0 * scale[1])
    Curveto_r(28.0 * scale[0], 2.0 * scale[1], 5.0 * scale[0],
              3.0 * scale[1], -53.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-58.0 * scale[0], 0.0 * scale[1], -81.0 *
              scale[0], -1.0 * scale[1], -52.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(846.0 * scale[0], 1039.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -13.0 * scale[1], -21.0 * scale[0], -
              25.0 * scale[1], -26.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -1.0 * scale[1], -14.0 *
              scale[0], -2.0 * scale[1], -19.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0], -
              22.0 * scale[1], -32.0 * scale[0], -48.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -40.0 * scale[1], -25.0 * scale[0], -
              72.0 * scale[1], -31.0 * scale[0], -183.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -74.0 * scale[1], -10.0 * scale[0], -
              146.0 * scale[1], -14.0 * scale[0], -160.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -21.0 * scale[1], -4.0 *
              scale[0], -23.0 * scale[1], 7.0 * scale[0], -12.0 * scale[1])
    Curveto_r(9.0 * scale[0], 8.0 * scale[1], 15.0 * scale[0],
              53.0 * scale[1], 19.0 * scale[0], 145.0 * scale[1])
    Curveto_r(4.0 * scale[0], 92.0 * scale[1], 11.0 * scale[0],
              144.0 * scale[1], 24.0 * scale[0], 172.0 * scale[1])
    Curveto_r(19.0 * scale[0], 44.0 * scale[1], 53.0 * scale[0],
              85.0 * scale[1], 72.0 * scale[0], 85.0 * scale[1])
    Curveto_r(18.0 * scale[0], 0.0 * scale[1], 34.0 * scale[0],
              24.0 * scale[1], 25.0 * scale[0], 39.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 10.0 * scale[1], -12.0 * scale[0],
              7.0 * scale[1], -25.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(322.0 * scale[0], 903.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -27.0 * scale[1], 12.0 * scale[0], -
              59.0 * scale[1], 14.0 * scale[0], -72.0 * scale[1])
    Curveto_r(10.0 * scale[0], -48.0 * scale[1], 16.0 *
              scale[0], -10.0 * scale[1], 9.0 * scale[0], 53.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 42.0 * scale[1], -12.0 * scale[0],
              66.0 * scale[1], -20.0 * scale[0], 66.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              11.0 * scale[1], -3.0 * scale[0], -47.0 * scale[1])
    te.end_fill()
    Moveto(1034.0 * scale[0], 825.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -49.0 * scale[1], 1.0 * scale[0], -
              71.0 * scale[1], 3.0 * scale[0], -48.0 * scale[1])
    Curveto_r(2.0 * scale[0], 23.0 * scale[1], 2.0 * scale[0],
              64.0 * scale[1], 0.0 * scale[0], 90.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 26.0 * scale[1], -3.0 * scale[0],
              8.0 * scale[1], -3.0 * scale[0], -42.0 * scale[1])
    te.end_fill()
    Moveto(500.0 * scale[0], 816.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 7.0 * scale[0], -
              6.0 * scale[1], 15.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 15.0 *
              scale[0], -1.0 * scale[1], 15.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -7.0 * scale[0],
              10.0 * scale[1], -15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              2.0 * scale[1], -15.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(448.0 * scale[0], 803.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(550.0 * scale[0], 801.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 41.0 * scale[0], -
              23.0 * scale[1], 47.0 * scale[0], -17.0 * scale[1])
    Curveto_r(2.0 * scale[0], 1.0 * scale[1], -8.0 * scale[0],
              8.0 * scale[1], -22.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -25.0 * scale[0],
              8.0 * scale[1], -25.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(408.0 * scale[0], 793.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(62.0 * scale[0], 730.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(430.0 * scale[0], 705.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0], -
              17.0 * scale[1], 10.0 * scale[0], -25.0 * scale[1])
    Curveto_r(5.0 * scale[0], -8.0 * scale[1], 10.0 * scale[0], -
              10.0 * scale[1], 10.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              17.0 * scale[1], -10.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 8.0 * scale[1], -10.0 * scale[0],
              11.0 * scale[1], -10.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(62.0 * scale[0], 675.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -41.0 * scale[1], 12.0 * scale[0], -
              73.0 * scale[1], 23.0 * scale[0], -56.0 * scale[1])
    Curveto_r(4.0 * scale[0], 7.0 * scale[1], 3.0 * scale[0],
              16.0 * scale[1], -3.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -12.0 * scale[0],
              20.0 * scale[1], -15.0 * scale[0], 36.0 * scale[1])
    Lineto_r(-4.0 * scale[0], 30.0 * scale[1])
    Lineto_r(-1.0 * scale[0], -30.0 * scale[1])
    te.end_fill()
    Moveto(661.0 * scale[0], 674.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(361.0 * scale[0], 644.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(393.0 * scale[0], 615.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -7.0 * scale[1], -18.0 * scale[0], -
              15.0 * scale[1], -25.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -10.0 *
              scale[0], -7.0 * scale[1], -7.0 * scale[0], -11.0 * scale[1])
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], 17.0 * scale[0],
              2.0 * scale[1], 30.0 * scale[0], 13.0 * scale[1])
    Curveto_r(13.0 * scale[0], 11.0 * scale[1], 22.0 * scale[0],
              21.0 * scale[1], 19.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0], -
              1.0 * scale[1], -17.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(1020.0 * scale[0], 550.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -11.0 * scale[1], -16.0 * scale[0], -
              18.0 * scale[1], -21.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -13.0 * scale[0], -
              2.0 * scale[1], -15.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -10.0 * scale[1], -18.0 * scale[0], -
              25.0 * scale[1], -35.0 * scale[0], -32.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -7.0 * scale[1], -27.0 * scale[0], -
              16.0 * scale[1], -24.0 * scale[0], -21.0 * scale[1])
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], -7.0 * scale[0], -
              7.0 * scale[1], -23.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 1.0 * scale[1], -102.0 * scale[0], -
              13.0 * scale[1], -102.0 * scale[0], -20.0 * scale[1])
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 6.0 * scale[0], -
              11.0 * scale[1], 14.0 * scale[0], -19.0 * scale[1])
    Curveto_r(10.0 * scale[0], -9.0 * scale[1], 17.0 * scale[0], -
              11.0 * scale[1], 21.0 * scale[0], -3.0 * scale[1])
    Curveto_r(4.0 * scale[0], 5.0 * scale[1], 17.0 * scale[0],
              9.0 * scale[1], 28.0 * scale[0], 7.0 * scale[1])
    Curveto_r(12.0 * scale[0], -1.0 * scale[1], 28.0 * scale[0],
              2.0 * scale[1], 36.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 7.0 * scale[1], 12.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -12.0 * scale[1], -6.0 *
              scale[0], -12.0 * scale[1], 8.0 * scale[0], -1.0 * scale[1])
    Curveto_r(9.0 * scale[0], 8.0 * scale[1], 22.0 * scale[0],
              10.0 * scale[1], 28.0 * scale[0], 6.0 * scale[1])
    Curveto_r(8.0 * scale[0], -4.0 * scale[1], 9.0 *
              scale[0], -3.0 * scale[1], 5.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 15.0 * scale[1], 44.0 * scale[0],
              74.0 * scale[1], 61.0 * scale[0], 67.0 * scale[1])
    Curveto_r(8.0 * scale[0], -2.0 * scale[1], 13.0 * scale[0],
              1.0 * scale[1], 11.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 6.0 * scale[1], 3.0 * scale[0],
              22.0 * scale[1], 10.0 * scale[0], 35.0 * scale[1])
    Curveto_r(7.0 * scale[0], 12.0 * scale[1], 10.0 * scale[0],
              22.0 * scale[1], 8.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              9.0 * scale[1], -16.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(375.0 * scale[0], 530.0 * scale[1], x, y)
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
    Moveto(431.0 * scale[0], 514.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(801.0 * scale[0], 385.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 7.0 * scale[0], -
              54.0 * scale[1], 14.0 * scale[0], -95.0 * scale[1])
    Lineto_r(14.0 * scale[0], -75.0 * scale[1])
    Lineto_r(-5.0 * scale[0], 65.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 64.0 * scale[1], -22.0 * scale[0],
              146.0 * scale[1], -23.0 * scale[0], 105.0 * scale[1])
    te.end_fill()
    Moveto(471.0 * scale[0], 294.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(807.0 * scale[0], 193.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -13.0 * scale[1], -19.0 * scale[0], -
              72.0 * scale[1], -15.0 * scale[0], -79.0 * scale[1])
    Curveto_r(9.0 * scale[0], -17.0 * scale[1], -54.0 * scale[0], -
              33.0 * scale[1], -134.0 * scale[0], -34.0 * scale[1])
    Curveto_r(-88.0 * scale[0], 0.0 * scale[1], -95.0 * scale[0],
              3.0 * scale[1], -79.0 * scale[0], 29.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 12.0 * scale[0],
              12.0 * scale[1], 24.0 * scale[0], 2.0 * scale[1])
    Curveto_r(26.0 * scale[0], -21.0 * scale[1], 32.0 * scale[0],
              9.0 * scale[1], 6.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 17.0 * scale[1], -20.0 * scale[0],
              17.0 * scale[1], -8.0 * scale[0], 2.0 * scale[1])
    Curveto_r(12.0 * scale[0], -17.0 * scale[1], 12.0 * scale[0], -
              19.0 * scale[1], -1.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -25.0 * scale[0],
              2.0 * scale[1], -37.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -6.0 * scale[1], -20.0 * scale[0], -
              13.0 * scale[1], -16.0 * scale[0], -30.0 * scale[1])
    Curveto_r(4.0 * scale[0], -15.0 * scale[1], 3.0 * scale[0], -
              20.0 * scale[1], -5.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -12.0 * scale[0],
              2.0 * scale[1], -12.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 6.0 * scale[0], -
              10.0 * scale[1], 13.0 * scale[0], -9.0 * scale[1])
    Curveto_r(6.0 * scale[0], 1.0 * scale[1], 39.0 * scale[0],
              0.0 * scale[1], 72.0 * scale[0], -1.0 * scale[1])
    Curveto_r(54.0 * scale[0], -2.0 * scale[1], 56.0 * scale[0], -
              3.0 * scale[1], 25.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-31.0 * scale[0], -7.0 * scale[1], -29.0 *
              scale[0], -8.0 * scale[1], 23.0 * scale[0], -9.0 * scale[1])
    Curveto_r(32.0 * scale[0], 0.0 * scale[1], 57.0 * scale[0],
              3.0 * scale[1], 57.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 15.0 * scale[0],
              10.0 * scale[1], 33.0 * scale[0], 10.0 * scale[1])
    Curveto_r(39.0 * scale[0], 0.0 * scale[1], 53.0 * scale[0],
              19.0 * scale[1], 62.0 * scale[0], 84.0 * scale[1])
    Curveto_r(7.0 * scale[0], 42.0 * scale[1], 3.0 * scale[0],
              58.0 * scale[1], -8.0 * scale[0], 39.0 * scale[1])
    te.penup()
