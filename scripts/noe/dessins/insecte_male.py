import turtle as te
from helper import *


def insecte_male(x, y, scale):

    te.penup()
    te.color('#9cb1b7')
    te.end_fill()
    Moveto(384.0 * scale[0], 1356.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -4.0 * scale[0], -
              25.0 * scale[1], -1.0 * scale[0], -38.0 * scale[1])
    Curveto_r(4.0 * scale[0], -21.0 * scale[1], 4.0 *
              scale[0], -20.0 * scale[1], 6.0 * scale[0], 5.0 * scale[1])
    Curveto_r(1.0 * scale[0], 31.0 * scale[1], 13.0 * scale[0],
              35.0 * scale[1], 32.0 * scale[0], 10.0 * scale[1])
    Curveto_r(13.0 * scale[0], -16.0 * scale[1], 12.0 *
              scale[0], -17.0 * scale[1], -3.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 16.0 * scale[1], -24.0 * scale[0],
              5.0 * scale[1], -3.0 * scale[0], -15.0 * scale[1])
    Curveto_r(9.0 * scale[0], -9.0 * scale[1], 15.0 * scale[0], -
              11.0 * scale[1], 15.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 5.0 * scale[0],
              8.0 * scale[1], 11.0 * scale[0], 4.0 * scale[1])
    Curveto_r(8.0 * scale[0], -4.0 * scale[1], 8.0 * scale[0],
              0.0 * scale[1], 0.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 30.0 * scale[1], -50.0 * scale[0],
              46.0 * scale[1], -57.0 * scale[0], 27.0 * scale[1])
    te.end_fill()
    Moveto(571.0 * scale[0], 1353.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              19.0 * scale[1], 0.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -25.0 * scale[1], -2.0 * scale[0], -
              25.0 * scale[1], -11.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 30.0 * scale[1], -18.0 * scale[0],
              28.0 * scale[1], -12.0 * scale[0], -3.0 * scale[1])
    Curveto_r(7.0 * scale[0], -37.0 * scale[1], 35.0 * scale[0], -
              28.0 * scale[1], 39.0 * scale[0], 13.0 * scale[1])
    Curveto_r(3.0 * scale[0], 18.0 * scale[1], 0.0 * scale[0],
              32.0 * scale[1], -6.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              3.0 * scale[1], -10.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(878.0 * scale[0], 1313.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(811.0 * scale[0], 1296.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -11.0 * scale[1], -9.0 *
              scale[0], -16.0 * scale[1], 0.0 * scale[0], -22.0 * scale[1])
    Curveto_r(8.0 * scale[0], -5.0 * scale[1], 10.0 *
              scale[0], -3.0 * scale[1], 4.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 8.0 * scale[1], -4.0 * scale[0],
              11.0 * scale[1], 0.0 * scale[0], 6.0 * scale[1])
    Curveto_r(12.0 * scale[0], -10.0 * scale[1], 14.0 *
              scale[0], -47.0 * scale[1], 3.0 * scale[0], -47.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0],
              5.0 * scale[1], -8.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              10.0 * scale[1], -11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -2.0 * scale[0], -
              18.0 * scale[1], 21.0 * scale[0], -30.0 * scale[1])
    Curveto_r(16.0 * scale[0], -9.0 * scale[1], 18.0 *
              scale[0], -7.0 * scale[1], 15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 11.0 * scale[1], 0.0 * scale[0],
              20.0 * scale[1], 6.0 * scale[0], 20.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0], -
              12.0 * scale[1], 10.0 * scale[0], -27.0 * scale[1])
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 4.0 * scale[0], -
              37.0 * scale[1], 9.0 * scale[0], -48.0 * scale[1])
    Curveto_r(7.0 * scale[0], -15.0 * scale[1], 9.0 * scale[0], -
              10.0 * scale[1], 9.0 * scale[0], 23.0 * scale[1])
    Curveto_r(1.0 * scale[0], 24.0 * scale[1], 5.0 * scale[0],
              41.0 * scale[1], 10.0 * scale[0], 37.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 8.0 * scale[0], -
              17.0 * scale[1], 5.0 * scale[0], -31.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -17.0 * scale[1], -1.0 *
              scale[0], -23.0 * scale[1], 6.0 * scale[0], -19.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 10.0 * scale[0],
              28.0 * scale[1], 8.0 * scale[0], 54.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 43.0 * scale[1], -5.0 * scale[0],
              47.0 * scale[1], -25.0 * scale[0], 43.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -2.0 * scale[1], -29.0 * scale[0],
              1.0 * scale[1], -37.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 8.0 * scale[1], -16.0 * scale[0],
              8.0 * scale[1], -25.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(94.0 * scale[0], 1289.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -8.0 * scale[1], -3.0 *
              scale[0], -9.0 * scale[1], 7.0 * scale[0], -4.0 * scale[1])
    Curveto_r(12.0 * scale[0], 8.0 * scale[1], 12.0 * scale[0],
              6.0 * scale[1], 1.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -9.0 * scale[1], -11.0 * scale[0], -
              20.0 * scale[1], -8.0 * scale[0], -26.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              11.0 * scale[1], -6.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -3.0 * scale[1], -5.0 *
              scale[0], -7.0 * scale[1], 6.0 * scale[0], -11.0 * scale[1])
    Curveto_r(9.0 * scale[0], -4.0 * scale[1], 15.0 *
              scale[0], -3.0 * scale[1], 11.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], -1.0 * scale[0],
              12.0 * scale[1], 4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(5.0 * scale[0], 4.0 * scale[1], 13.0 * scale[0], -
              8.0 * scale[1], 17.0 * scale[0], -26.0 * scale[1])
    Curveto_r(6.0 * scale[0], -29.0 * scale[1], 8.0 * scale[0], -
              30.0 * scale[1], 15.0 * scale[0], -13.0 * scale[1])
    Lineto_r(8.0 * scale[0], 20.0 * scale[1])
    Lineto_r(1.0 * scale[0], -20.0 * scale[1])
    Curveto_r(2.0 * scale[0], -11.0 * scale[1], 2.0 * scale[0], -
              24.0 * scale[1], 1.0 * scale[0], -28.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -5.0 * scale[1], 3.0 *
              scale[0], -6.0 * scale[1], 9.0 * scale[0], -2.0 * scale[1])
    Curveto_r(13.0 * scale[0], 8.0 * scale[1], 8.0 * scale[0],
              112.0 * scale[1], -5.0 * scale[0], 112.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0],
              3.0 * scale[1], -32.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 4.0 * scale[1], -24.0 * scale[0],
              2.0 * scale[1], -29.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(460.0 * scale[0], 1290.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 12.0 * scale[0], -
              10.0 * scale[1], 26.0 * scale[0], -10.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 23.0 * scale[0],
              4.0 * scale[1], 19.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              10.0 * scale[1], -26.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 0.0 * scale[1], -19.0 * scale[0], -
              4.0 * scale[1], -19.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(409.0 * scale[0], 1271.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-21.0 * scale[0], -18.0 * scale[1], -22.0 *
              scale[0], -19.0 * scale[1], -5.0 * scale[0], -17.0 * scale[1])
    Curveto_r(11.0 * scale[0], 2.0 * scale[1], 22.0 * scale[0],
              8.0 * scale[1], 24.0 * scale[0], 14.0 * scale[1])
    Curveto_r(2.0 * scale[0], 7.0 * scale[1], 9.0 * scale[0],
              9.0 * scale[1], 14.0 * scale[0], 6.0 * scale[1])
    Curveto_r(7.0 * scale[0], -4.0 * scale[1], 8.0 *
              scale[0], -2.0 * scale[1], 4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 15.0 * scale[1], -10.0 * scale[0],
              15.0 * scale[1], -37.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(519.0 * scale[0], 1278.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -14.0 * scale[1], -4.0 *
              scale[0], -47.0 * scale[1], 4.0 * scale[0], -45.0 * scale[1])
    Curveto_r(5.0 * scale[0], 1.0 * scale[1], 12.0 * scale[0], -
              4.0 * scale[1], 15.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], -9.0 * scale[1], 0.0 * scale[0], -
              11.0 * scale[1], -8.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 5.0 * scale[1], -11.0 * scale[0],
              4.0 * scale[1], -6.0 * scale[0], -4.0 * scale[1])
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], -6.0 * scale[0], -28.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -10.0 * scale[1], -8.0 * scale[0], -
              14.0 * scale[1], -1.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 14.0 * scale[0],
              1.0 * scale[1], 16.0 * scale[0], -5.0 * scale[1])
    Curveto_r(4.0 * scale[0], -10.0 * scale[1], 6.0 * scale[0], -
              10.0 * scale[1], 6.0 * scale[0], -1.0 * scale[1])
    Curveto_r(1.0 * scale[0], 7.0 * scale[1], 8.0 * scale[0],
              10.0 * scale[1], 16.0 * scale[0], 7.0 * scale[1])
    Curveto_r(18.0 * scale[0], -7.0 * scale[1], 19.0 * scale[0],
              0.0 * scale[1], 5.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 11.0 * scale[1], -6.0 * scale[0],
              21.0 * scale[1], -1.0 * scale[0], 24.0 * scale[1])
    Curveto_r(5.0 * scale[0], 4.0 * scale[1], 14.0 * scale[0], -
              6.0 * scale[1], 19.0 * scale[0], -21.0 * scale[1])
    Curveto_r(9.0 * scale[0], -24.0 * scale[1], 11.0 * scale[0], -
              25.0 * scale[1], 11.0 * scale[0], -7.0 * scale[1])
    Curveto_r(1.0 * scale[0], 19.0 * scale[1], -26.0 * scale[0],
              53.0 * scale[1], -36.0 * scale[0], 47.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -2.0 * scale[1], -6.0 * scale[0], -
              3.0 * scale[1], -10.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], 0.0 * scale[0],
              4.0 * scale[1], 10.0 * scale[0], 8.0 * scale[1])
    Curveto_r(18.0 * scale[0], 6.0 * scale[1], 18.0 * scale[0],
              8.0 * scale[1], 2.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 10.0 * scale[1], -15.0 * scale[0],
              11.0 * scale[1], -13.0 * scale[0], 0.0 * scale[1])
    Curveto_r(2.0 * scale[0], -7.0 * scale[1], -3.0 * scale[0], -
              15.0 * scale[1], -11.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -3.0 * scale[1], -12.0 * scale[0],
              0.0 * scale[1], -8.0 * scale[0], 12.0 * scale[1])
    Curveto_r(5.0 * scale[0], 12.0 * scale[1], 1.0 * scale[0],
              24.0 * scale[1], -4.0 * scale[0], 14.0 * scale[1])
    te.end_fill()
    Moveto_r(22.0 * scale[0], -91.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -9.0 * scale[1], -11.0 *
              scale[0], -8.0 * scale[1], -5.0 * scale[0], 6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 10.0 * scale[1], 9.0 * scale[0],
              15.0 * scale[1], 12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 0.0 * scale[0], -
              11.0 * scale[1], -7.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(65.0 * scale[0], 1260.0 * scale[1], x, y)
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
    Moveto(444.0 * scale[0], 1254.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -15.0 * scale[1], -19.0 *
              scale[0], -15.0 * scale[1], 1.0 * scale[0], -6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 5.0 * scale[1], 27.0 * scale[0],
              12.0 * scale[1], 35.0 * scale[0], 15.0 * scale[1])
    Curveto_r(13.0 * scale[0], 5.0 * scale[1], 13.0 * scale[0],
              6.0 * scale[1], -1.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 1.0 * scale[1], -24.0 * scale[0], -
              6.0 * scale[1], -35.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(382.0 * scale[0], 1235.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 16.0 * scale[0], -
              8.0 * scale[1], 28.0 * scale[0], -10.0 * scale[1])
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 20.0 *
              scale[0], -1.0 * scale[1], 16.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 4.0 * scale[1], -16.0 * scale[0],
              8.0 * scale[1], -28.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 2.0 * scale[1], -19.0 * scale[0],
              1.0 * scale[1], -16.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(391.0 * scale[0], 1185.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -27.0 * scale[1], -3.0 * scale[0], -
              28.0 * scale[1], -12.0 * scale[0], -10.0 * scale[1])
    Lineto_r(-9.0 * scale[0], 20.0 * scale[1])
    Lineto_r(3.0 * scale[0], -20.0 * scale[1])
    Curveto_r(1.0 * scale[0], -13.0 * scale[1], 11.0 * scale[0], -
              21.0 * scale[1], 27.0 * scale[0], -23.0 * scale[1])
    Curveto_r(15.0 * scale[0], -2.0 * scale[1], 20.0 * scale[0],
              0.0 * scale[1], 14.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -14.0 * scale[0],
              19.0 * scale[1], -17.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 23.0 * scale[1], -4.0 * scale[0],
              23.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(575.0 * scale[0], 1160.0 * scale[1], x, y)
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
    Moveto(122.0 * scale[0], 1143.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -3.0 * scale[1], -10.0 *
              scale[0], -9.0 * scale[1], -6.0 * scale[0], -14.0 * scale[1])
    Curveto_r(7.0 * scale[0], -12.0 * scale[1], 44.0 *
              scale[0], -12.0 * scale[1], 44.0 * scale[0], 0.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], -21.0 * scale[0],
              19.0 * scale[1], -38.0 * scale[0], 14.0 * scale[1])
    te.end_fill()
    Moveto(526.0 * scale[0], 1133.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -9.0 * scale[1], -4.0 * scale[0], -
              14.0 * scale[1], 0.0 * scale[0], -10.0 * scale[1])
    Curveto_r(4.0 * scale[0], 4.0 * scale[1], 13.0 * scale[0], -
              1.0 * scale[1], 21.0 * scale[0], -11.0 * scale[1])
    Curveto_r(8.0 * scale[0], -9.0 * scale[1], 12.0 * scale[0], -
              12.0 * scale[1], 9.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], 11.0 * scale[0], 22.0 * scale[1])
    Curveto_r(10.0 * scale[0], 6.0 * scale[1], 13.0 * scale[0],
              11.0 * scale[1], 6.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -18.0 * scale[0],
              3.0 * scale[1], -26.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -17.0 * scale[0], -
              2.0 * scale[1], -21.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(410.0 * scale[0], 1110.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(19.0 * scale[0], -17.0 * scale[1], 39.0 * scale[0], -
              30.0 * scale[1], 45.0 * scale[0], -29.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 4.0 * scale[0],
              3.0 * scale[1], -3.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 4.0 * scale[1], -10.0 * scale[0],
              8.0 * scale[1], 0.0 * scale[0], 21.0 * scale[1])
    Curveto_r(8.0 * scale[0], 10.0 * scale[1], 9.0 * scale[0],
              13.0 * scale[1], 1.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -4.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -18.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], -11.0 * scale[0],
              8.0 * scale[1], -16.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -4.0 * scale[1], -9.0 *
              scale[0], -1.0 * scale[1], -9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -8.0 * scale[0],
              11.0 * scale[1], -17.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -1.0 * scale[1], -9.0 *
              scale[0], -8.0 * scale[1], 17.0 * scale[0], -30.0 * scale[1])
    te.end_fill()
    Moveto(503.0 * scale[0], 1095.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              15.0 * scale[1], 9.0 * scale[0], -15.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0],
              4.0 * scale[1], 8.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -4.0 * scale[0],
              12.0 * scale[1], -8.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              1.0 * scale[1], -9.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(470.0 * scale[0], 1015.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 2.0 * scale[0], -
              15.0 * scale[1], 4.0 * scale[0], -15.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 6.0 * scale[0],
              7.0 * scale[1], 10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], 1.0 * scale[0],
              15.0 * scale[1], -4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              7.0 * scale[1], -10.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(46.0 * scale[0], 982.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 1.0 *
              scale[0], -9.0 * scale[1], 9.0 * scale[0], -9.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              4.0 * scale[1], 15.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], -4.0 * scale[0],
              8.0 * scale[1], -9.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              4.0 * scale[1], -15.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(136.0 * scale[0], 955.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -9.0 * scale[1], -17.0 * scale[0], -
              21.0 * scale[1], -13.0 * scale[0], -34.0 * scale[1])
    Curveto_r(6.0 * scale[0], -24.0 * scale[1], -47.0 * scale[0], -
              75.0 * scale[1], -66.0 * scale[0], -65.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0], -
              3.0 * scale[1], 12.0 * scale[0], -14.0 * scale[1])
    Curveto_r(14.0 * scale[0], -11.0 * scale[1], 43.0 * scale[0], -
              22.0 * scale[1], 67.0 * scale[0], -26.0 * scale[1])
    Curveto_r(61.0 * scale[0], -8.0 * scale[1], 91.0 * scale[0], -
              25.0 * scale[1], 124.0 * scale[0], -69.0 * scale[1])
    Lineto_r(29.0 * scale[0], -40.0 * scale[1])
    Lineto_r(8.0 * scale[0], 54.0 * scale[1])
    Curveto_r(4.0 * scale[0], 30.0 * scale[1], 6.0 * scale[0],
              57.0 * scale[1], 5.0 * scale[0], 62.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 4.0 * scale[1], 7.0 * scale[0],
              2.0 * scale[1], 18.0 * scale[0], -5.0 * scale[1])
    Curveto_r(13.0 * scale[0], -8.0 * scale[1], 16.0 * scale[0], -
              16.0 * scale[1], 10.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -12.0 * scale[1], -13.0 *
              scale[0], -76.0 * scale[1], -2.0 * scale[0], -93.0 * scale[1])
    Curveto_r(4.0 * scale[0], -7.0 * scale[1], 19.0 * scale[0], -
              14.0 * scale[1], 32.0 * scale[0], -15.0 * scale[1])
    Curveto_r(20.0 * scale[0], -3.0 * scale[1], 25.0 * scale[0],
              3.0 * scale[1], 32.0 * scale[0], 33.0 * scale[1])
    Curveto_r(5.0 * scale[0], 20.0 * scale[1], 22.0 * scale[0],
              50.0 * scale[1], 37.0 * scale[0], 67.0 * scale[1])
    Curveto_r(25.0 * scale[0], 26.0 * scale[1], 28.0 * scale[0],
              36.0 * scale[1], 21.0 * scale[0], 64.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 20.0 * scale[1], -9.0 * scale[0],
              25.0 * scale[1], -10.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -19.0 * scale[1], -2.0 *
              scale[0], -18.0 * scale[1], -10.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 12.0 * scale[1], -14.0 * scale[0],
              22.0 * scale[1], -19.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              6.0 * scale[1], -5.0 * scale[0], -14.0 * scale[1])
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], 1.0 * scale[0], -
              17.0 * scale[1], -4.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -9.0 * scale[0],
              2.0 * scale[1], -8.0 * scale[0], 11.0 * scale[1])
    Curveto_r(2.0 * scale[0], 27.0 * scale[1], -49.0 * scale[0],
              47.0 * scale[1], -92.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -5.0 * scale[1], -44.0 * scale[0], -
              11.0 * scale[1], -52.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -3.0 * scale[1], -16.0 * scale[0],
              4.0 * scale[1], -18.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 13.0 * scale[1], -13.0 * scale[0],
              24.0 * scale[1], -28.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 4.0 * scale[1], -24.0 * scale[0],
              14.0 * scale[1], -25.0 * scale[0], 24.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -2.0 * scale[0],
              14.0 * scale[1], -8.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -17.0 * scale[1], -9.0 * scale[0], -
              18.0 * scale[1], -12.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 14.0 * scale[1], -6.0 * scale[0],
              15.0 * scale[1], -23.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(474.0 * scale[0], 720.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -140.0 * scale[1], 2.0 * scale[0], -
              198.0 * scale[1], 3.0 * scale[0], -128.0 * scale[1])
    Curveto_r(2.0 * scale[0], 71.0 * scale[1], 2.0 * scale[0],
              185.0 * scale[1], 0.0 * scale[0], 255.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 71.0 * scale[1], -3.0 * scale[0],
              13.0 * scale[1], -3.0 * scale[0], -127.0 * scale[1])
    te.end_fill()
    Moveto(0.0 * scale[0], 949.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0], -
              7.0 * scale[1], 10.0 * scale[0], -4.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 10.0 * scale[0],
              8.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 2.0 * scale[1], -4.0 * scale[0],
              4.0 * scale[1], -10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              5.0 * scale[1], -10.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(507.0 * scale[0], 924.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -10.0 * scale[1], -9.0 *
              scale[0], -44.0 * scale[1], 1.0 * scale[0], -44.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              4.0 * scale[1], 19.0 * scale[0], 8.0 * scale[1])
    Curveto_r(10.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              12.0 * scale[1], 0.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 9.0 * scale[1], -16.0 * scale[0],
              14.0 * scale[1], -20.0 * scale[0], 10.0 * scale[1])
    te.end_fill()
    Moveto(946.0 * scale[0], 911.0 * scale[1], x, y)
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
    Moveto(2.0 * scale[0], 845.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -36.0 * scale[1], 11.0 * scale[0], -
              48.0 * scale[1], 22.0 * scale[0], -19.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], 12.0 * scale[0],
              12.0 * scale[1], 18.0 * scale[0], 9.0 * scale[1])
    Curveto_r(7.0 * scale[0], -4.0 * scale[1], 4.0 * scale[0],
              1.0 * scale[1], -6.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 12.0 * scale[1], -16.0 * scale[0],
              16.0 * scale[1], -5.0 * scale[0], 16.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              2.0 * scale[1], -1.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 15.0 * scale[1], -26.0 * scale[0],
              13.0 * scale[1], -28.0 * scale[0], -25.0 * scale[1])
    te.end_fill()
    Moveto(501.0 * scale[0], 730.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -140.0 * scale[1], -2.0 * scale[0], -
              141.0 * scale[1], 19.0 * scale[0], -128.0 * scale[1])
    Curveto_r(25.0 * scale[0], 15.0 * scale[1], 30.0 * scale[0],
              35.0 * scale[1], 31.0 * scale[0], 108.0 * scale[1])
    Curveto_r(1.0 * scale[0], 99.0 * scale[1], -7.0 * scale[0],
              145.0 * scale[1], -26.0 * scale[0], 142.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -2.0 * scale[1], -14.0 * scale[0],
              1.0 * scale[1], -10.0 * scale[0], 7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              11.0 * scale[1], -3.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              58.0 * scale[1], -11.0 * scale[0], -140.0 * scale[1])
    te.end_fill()
    Moveto(22.0 * scale[0], 780.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(440.0 * scale[0], 786.0 * scale[1], x, y)
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
    Moveto(715.0 * scale[0], 770.0 * scale[1], x, y)
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
    Moveto(740.0 * scale[0], 758.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 7.0 * scale[0], -
              19.0 * scale[1], 16.0 * scale[0], -22.0 * scale[1])
    Curveto_r(25.0 * scale[0], -10.0 * scale[1], 27.0 *
              scale[0], -1.0 * scale[1], 4.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 15.0 * scale[1], -20.0 * scale[0],
              16.0 * scale[1], -20.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(432.0 * scale[0], 752.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-21.0 * scale[0], -14.0 * scale[1], -26.0 *
              scale[0], -88.0 * scale[1], -8.0 * scale[0], -132.0 * scale[1])
    Curveto_r(12.0 * scale[0], -30.0 * scale[1], 13.0 *
              scale[0], -46.0 * scale[1], 6.0 * scale[0], -60.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -15.0 * scale[1], -6.0 * scale[0], -
              24.0 * scale[1], 10.0 * scale[0], -40.0 * scale[1])
    Lineto_r(20.0 * scale[0], -20.0 * scale[1])
    Lineto_r(0.0 * scale[0], 124.0 * scale[1])
    Curveto_r(0.0 * scale[0], 122.0 * scale[1], -4.0 * scale[0],
              142.0 * scale[1], -28.0 * scale[0], 128.0 * scale[1])
    te.end_fill()
    Moveto(577.0 * scale[0], 696.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -10.0 * scale[1], -7.0 * scale[0], -
              25.0 * scale[1], -6.0 * scale[0], -34.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 4.0 *
              scale[0], -9.0 * scale[1], 10.0 * scale[0], 7.0 * scale[1])
    Curveto_r(5.0 * scale[0], 13.0 * scale[1], 8.0 * scale[0],
              29.0 * scale[1], 6.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 5.0 * scale[1], -6.0 * scale[0],
              2.0 * scale[1], -10.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(690.0 * scale[0], 695.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -8.0 * scale[1], -19.0 * scale[0], -
              15.0 * scale[1], -26.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0], -
              5.0 * scale[1], -14.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -20.0 * scale[1], 30.0 * scale[0], -
              22.0 * scale[1], 56.0 * scale[0], -5.0 * scale[1])
    Curveto_r(24.0 * scale[0], 16.0 * scale[1], 26.0 * scale[0],
              15.0 * scale[1], 30.0 * scale[0], -2.0 * scale[1])
    Curveto_r(8.0 * scale[0], -27.0 * scale[1], 77.0 * scale[0], -
              73.0 * scale[1], 94.0 * scale[0], -63.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 18.0 * scale[0],
              6.0 * scale[1], 24.0 * scale[0], 3.0 * scale[1])
    Curveto_r(5.0 * scale[0], -4.0 * scale[1], 6.0 *
              scale[0], -1.0 * scale[1], 1.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 7.0 * scale[1], -2.0 * scale[0],
              16.0 * scale[1], 5.0 * scale[0], 20.0 * scale[1])
    Curveto_r(7.0 * scale[0], 5.0 * scale[1], -16.0 * scale[0],
              18.0 * scale[1], -61.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-41.0 * scale[0], 15.0 * scale[1], -79.0 * scale[0],
              32.0 * scale[1], -85.0 * scale[0], 37.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 5.0 * scale[1], -16.0 * scale[0],
              2.0 * scale[1], -24.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(645.0 * scale[0], 620.0 * scale[1], x, y)
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
    Moveto(686.0 * scale[0], 628.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 10.0 * scale[0], -
              6.0 * scale[1], 15.0 * scale[0], -3.0 * scale[1])
    Curveto_r(13.0 * scale[0], 9.0 * scale[1], 11.0 * scale[0],
              12.0 * scale[1], -6.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -9.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(951.0 * scale[0], 614.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(220.0 * scale[0], 611.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 18.0 * scale[1], -14.0 * scale[0],
              21.0 * scale[1], -14.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(684.0 * scale[0], 599.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], -3.0 *
              scale[0], -10.0 * scale[1], 4.0 * scale[0], -5.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 13.0 * scale[0],
              2.0 * scale[1], 16.0 * scale[0], -3.0 * scale[1])
    Curveto_r(9.0 * scale[0], -13.0 * scale[1], -7.0 * scale[0], -
              21.0 * scale[1], -23.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -22.0 * scale[0],
              0.0 * scale[1], -38.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -12.0 * scale[1], -42.0 *
              scale[0], -31.0 * scale[1], -63.0 * scale[0], -42.0 * scale[1])
    Lineto_r(-39.0 * scale[0], -19.0 * scale[1])
    Lineto_r(22.0 * scale[0], -20.0 * scale[1])
    Curveto_r(47.0 * scale[0], -43.0 * scale[1], 119.0 * scale[0], -
              50.0 * scale[1], 159.0 * scale[0], -15.0 * scale[1])
    Curveto_r(25.0 * scale[0], 21.0 * scale[1], 60.0 * scale[0],
              91.0 * scale[1], 52.0 * scale[0], 104.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 7.0 * scale[1], -1.0 * scale[0],
              9.0 * scale[1], 9.0 * scale[0], 5.0 * scale[1])
    Curveto_r(9.0 * scale[0], -3.0 * scale[1], 19.0 *
              scale[0], -2.0 * scale[1], 21.0 * scale[0], 2.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], -11.0 * scale[0],
              11.0 * scale[1], -32.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 3.0 * scale[1], -38.0 * scale[0],
              1.0 * scale[1], -41.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -6.0 * scale[1], -10.0 *
              scale[0], -4.0 * scale[1], -21.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 12.0 * scale[1], -20.0 * scale[0],
              13.0 * scale[1], -26.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(583.0 * scale[0], 575.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              12.0 * scale[1], 9.0 * scale[0], -9.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 6.0 * scale[0],
              10.0 * scale[1], 3.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 13.0 * scale[1], -12.0 * scale[0],
              11.0 * scale[1], -12.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(810.0 * scale[0], 575.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -15.0 * scale[1], -5.0 *
              scale[0], -39.0 * scale[1], 10.0 * scale[0], -30.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 12.0 * scale[0],
              0.0 * scale[1], 16.0 * scale[0], -6.0 * scale[1])
    Curveto_r(4.0 * scale[0], -8.0 * scale[1], 3.0 * scale[0], -
              9.0 * scale[1], -4.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -12.0 * scale[0],
              3.0 * scale[1], -12.0 * scale[0], -3.0 * scale[1])
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 22.0 * scale[0], -
              25.0 * scale[1], 30.0 * scale[0], -11.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], 10.0 * scale[0],
              11.0 * scale[1], 14.0 * scale[0], 11.0 * scale[1])
    Curveto_r(3.0 * scale[0], -1.0 * scale[1], 6.0 * scale[0],
              1.0 * scale[1], 6.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 3.0 * scale[1], -3.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -1.0 * scale[1], -33.0 * scale[0],
              35.0 * scale[1], -28.0 * scale[0], 43.0 * scale[1])
    Curveto_r(9.0 * scale[0], 14.0 * scale[1], -13.0 * scale[0],
              8.0 * scale[1], -26.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(932.0 * scale[0], 546.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -24.0 * scale[1], -10.0 *
              scale[0], -25.0 * scale[1], 14.0 * scale[0], -14.0 * scale[1])
    Curveto_r(13.0 * scale[0], 6.0 * scale[1], 23.0 * scale[0],
              16.0 * scale[1], 21.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 20.0 * scale[1], -24.0 * scale[0],
              16.0 * scale[1], -35.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(886.0 * scale[0], 545.0 * scale[1], x, y)
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
    Moveto(890.0 * scale[0], 400.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0], -
              10.0 * scale[1], 11.0 * scale[0], -10.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              5.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -8.0 * scale[0],
              10.0 * scale[1], -11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              4.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#433114')
    te.end_fill()
    Moveto(16.0 * scale[0], 1388.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], 1.0 * scale[0], -
              8.0 * scale[1], -5.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              321.0 * scale[1], 4.0 * scale[0], -337.0 * scale[1])
    Curveto_r(14.0 * scale[0], -14.0 * scale[1], 80.0 * scale[0], -
              21.0 * scale[1], 91.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 7.0 * scale[1], -15.0 * scale[0],
              10.0 * scale[1], -53.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -1.0 * scale[1], -24.0 * scale[0],
              3.0 * scale[1], -29.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 18.0 * scale[1], -14.0 * scale[0],
              309.0 * scale[1], -2.0 * scale[0], 309.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              4.0 * scale[1], 3.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], 9.0 * scale[0],
              11.0 * scale[1], 27.0 * scale[0], 13.0 * scale[1])
    Lineto_r(33.0 * scale[0], 3.0 * scale[1])
    Lineto_r(-37.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 2.0 * scale[1], -34.0 * scale[0],
              1.0 * scale[1], -32.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(113.0 * scale[0], 1393.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(15.0 * scale[0], -2.0 * scale[1], 39.0 *
              scale[0], -2.0 * scale[1], 55.0 * scale[0], 0.0 * scale[1])
    Curveto_r(15.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              4.0 * scale[1], -28.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 0.0 * scale[1], -43.0 *
              scale[0], -2.0 * scale[1], -27.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(228.0 * scale[0], 1393.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(318.0 * scale[0], 1393.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(682.0 * scale[0], 1395.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -9.0 * scale[1], 197.0 * scale[0], -
              11.0 * scale[1], 191.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 4.0 * scale[1], -47.0 * scale[0],
              7.0 * scale[1], -100.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-53.0 * scale[0], 0.0 * scale[1], -94.0 *
              scale[0], -2.0 * scale[1], -91.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(930.0 * scale[0], 1383.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], 5.0 * scale[0], -
              15.0 * scale[1], 10.0 * scale[0], -18.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 11.0 * scale[0], -
              18.0 * scale[1], 11.0 * scale[0], -33.0 * scale[1])
    Curveto_r(2.0 * scale[0], -23.0 * scale[1], 2.0 * scale[0], -
              24.0 * scale[1], 6.0 * scale[0], -5.0 * scale[1])
    Curveto_r(2.0 * scale[0], 13.0 * scale[1], -3.0 * scale[0],
              33.0 * scale[1], -11.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 12.0 * scale[1], -16.0 * scale[0],
              17.0 * scale[1], -16.0 * scale[0], 11.0 * scale[1])
    te.end_fill()
    Moveto(851.0 * scale[0], 1326.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -2.0 * scale[1], 20.0 * scale[0], -
              6.0 * scale[1], 39.0 * scale[0], -10.0 * scale[1])
    Curveto_r(25.0 * scale[0], -4.0 * scale[1], 31.0 *
              scale[0], -3.0 * scale[1], 20.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 9.0 * scale[1], -69.0 * scale[0],
              15.0 * scale[1], -59.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(63.0 * scale[0], 1313.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -3.0 * scale[1], 0.0 * scale[0], -
              15.0 * scale[1], -10.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -10.0 * scale[1], -14.0 * scale[0], -
              20.0 * scale[1], -12.0 * scale[0], -23.0 * scale[1])
    Curveto_r(3.0 * scale[0], -2.0 * scale[1], 17.0 * scale[0],
              9.0 * scale[1], 31.0 * scale[0], 25.0 * scale[1])
    Curveto_r(25.0 * scale[0], 29.0 * scale[1], 25.0 * scale[0],
              30.0 * scale[1], 5.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -17.0 *
              scale[0], -3.0 * scale[1], -14.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(902.0 * scale[0], 1270.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 2.0 * scale[0], -
              27.0 * scale[1], 5.0 * scale[0], -17.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              25.0 * scale[1], 0.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(172.0 * scale[0], 1270.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(959.0 * scale[0], 1248.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -9.0 * scale[1], -5.0 * scale[0], -
              48.0 * scale[1], -1.0 * scale[0], -43.0 * scale[1])
    Curveto_r(6.0 * scale[0], 6.0 * scale[1], 11.0 * scale[0],
              45.0 * scale[1], 5.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              1.0 * scale[1], -4.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(72.0 * scale[0], 1222.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -9.0 * scale[1], 13.0 * scale[0], -
              18.0 * scale[1], 14.0 * scale[0], -20.0 * scale[1])
    Curveto_r(1.0 * scale[0], -2.0 * scale[1], 4.0 * scale[0],
              4.0 * scale[1], 7.0 * scale[0], 12.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], -2.0 * scale[0],
              16.0 * scale[1], -14.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 5.0 * scale[1], -18.0 * scale[0],
              3.0 * scale[1], -7.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(805.0 * scale[0], 1220.0 * scale[1], x, y)
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
    Moveto(903.0 * scale[0], 1175.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -27.0 * scale[1], 2.0 * scale[0], -
              38.0 * scale[1], 4.0 * scale[0], -22.0 * scale[1])
    Curveto_r(2.0 * scale[0], 15.0 * scale[1], 2.0 * scale[0],
              37.0 * scale[1], 0.0 * scale[0], 50.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 12.0 * scale[1], -4.0 * scale[0],
              0.0 * scale[1], -4.0 * scale[0], -28.0 * scale[1])
    te.end_fill()
    Moveto(170.0 * scale[0], 1199.0 * scale[1], x, y)
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
    Moveto(75.0 * scale[0], 1181.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              12.0 * scale[1], 5.0 * scale[0], -16.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 10.0 * scale[0],
              1.0 * scale[1], 10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 18.0 * scale[1], -6.0 * scale[0],
              21.0 * scale[1], -15.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(170.0 * scale[0], 1170.0 * scale[1], x, y)
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
    Moveto(951.0 * scale[0], 1164.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(952.0 * scale[0], 1100.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -14.0 * scale[1], -5.0 * scale[0], -
              36.0 * scale[1], -8.0 * scale[0], -50.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -19.0 * scale[1], -4.0 *
              scale[0], -22.0 * scale[1], 5.0 * scale[0], -14.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 11.0 * scale[0],
              28.0 * scale[1], 8.0 * scale[0], 50.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 22.0 * scale[1], -4.0 * scale[0],
              28.0 * scale[1], -5.0 * scale[0], 14.0 * scale[1])
    te.end_fill()
    Moveto(193.0 * scale[0], 1033.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(32.0 * scale[0], -2.0 * scale[1], 81.0 *
              scale[0], -2.0 * scale[1], 110.0 * scale[0], 0.0 * scale[1])
    Curveto_r(29.0 * scale[0], 2.0 * scale[1], 3.0 * scale[0],
              3.0 * scale[1], -58.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-60.0 * scale[0], 0.0 * scale[1], -84.0 *
              scale[0], -1.0 * scale[1], -52.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(618.0 * scale[0], 1033.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(537.0 * scale[0], 996.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-17.0 * scale[0], -31.0 * scale[1], -17.0 *
              scale[0], -31.0 * scale[1], 2.0 * scale[0], -8.0 * scale[1])
    Curveto_r(20.0 * scale[0], 23.0 * scale[1], 37.0 * scale[0],
              31.0 * scale[1], 25.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], -3.0 *
              scale[0], -8.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(16.0 * scale[0], 9.0 * scale[1], 15.0 * scale[0],
              23.0 * scale[1], -1.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 3.0 * scale[1], -20.0 * scale[0], -
              9.0 * scale[1], -30.0 * scale[0], -27.0 * scale[1])
    te.end_fill()
    Moveto(778.0 * scale[0], 1012.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-25.0 * scale[0], -15.0 * scale[1], -28.0 *
              scale[0], -23.0 * scale[1], -28.0 * scale[0], -70.0 * scale[1])
    Curveto_r(0.0 * scale[0], -64.0 * scale[1], 13.0 * scale[0], -
              92.0 * scale[1], 43.0 * scale[0], -92.0 * scale[1])
    Curveto_r(21.0 * scale[0], 1.0 * scale[1], 22.0 * scale[0],
              1.0 * scale[1], 2.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 17.0 * scale[1], -35.0 * scale[0],
              28.0 * scale[1], -35.0 * scale[0], 80.0 * scale[1])
    Curveto_r(0.0 * scale[0], 37.0 * scale[1], 5.0 * scale[0],
              50.0 * scale[1], 22.0 * scale[0], 62.0 * scale[1])
    Curveto_r(36.0 * scale[0], 26.0 * scale[1], 56.0 * scale[0],
              20.0 * scale[1], 61.0 * scale[0], -16.0 * scale[1])
    Curveto_r(4.0 * scale[0], -32.0 * scale[1], 4.0 *
              scale[0], -32.0 * scale[1], 5.0 * scale[0], 5.0 * scale[1])
    Curveto_r(2.0 * scale[0], 32.0 * scale[1], -1.0 * scale[0],
              37.0 * scale[1], -20.0 * scale[0], 37.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -35.0 * scale[0], -
              8.0 * scale[1], -50.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(930.0 * scale[0], 1000.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(661.0 * scale[0], 970.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -33.0 * scale[1], -4.0 * scale[0], -
              33.0 * scale[1], -11.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 23.0 * scale[1], -15.0 * scale[0],
              12.0 * scale[1], -11.0 * scale[0], -17.0 * scale[1])
    Curveto_r(1.0 * scale[0], -7.0 * scale[1], -3.0 * scale[0], -
              13.0 * scale[1], -9.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              7.0 * scale[1], -10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 5.0 * scale[0], -
              12.0 * scale[1], 12.0 * scale[0], -8.0 * scale[1])
    Curveto_r(7.0 * scale[0], 5.0 * scale[1], 9.0 * scale[0],
              2.0 * scale[1], 5.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -10.0 * scale[1], 3.0 * scale[0], -
              20.0 * scale[1], 19.0 * scale[0], -28.0 * scale[1])
    Curveto_r(13.0 * scale[0], -8.0 * scale[1], 24.0 * scale[0], -
              16.0 * scale[1], 24.0 * scale[0], -19.0 * scale[1])
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], -15.0 * scale[0], -
              28.0 * scale[1], -30.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -5.0 * scale[1], -11.0 *
              scale[0], -7.0 * scale[1], 5.0 * scale[0], -14.0 * scale[1])
    Curveto_r(11.0 * scale[0], -5.0 * scale[1], 20.0 * scale[0], -
              16.0 * scale[1], 20.0 * scale[0], -24.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 10.0 * scale[0], -
              15.0 * scale[1], 22.0 * scale[0], -16.0 * scale[1])
    Curveto_r(12.0 * scale[0], -1.0 * scale[1], 20.0 * scale[0],
              3.0 * scale[1], 17.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], -12.0 * scale[0],
              7.0 * scale[1], -20.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -3.0 * scale[1], -14.0 *
              scale[0], -1.0 * scale[1], -14.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 5.0 * scale[0],
              10.0 * scale[1], 10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              7.0 * scale[1], -1.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 28.0 * scale[1], 3.0 * scale[0],
              48.0 * scale[1], 26.0 * scale[0], 29.0 * scale[1])
    Curveto_r(11.0 * scale[0], -9.0 * scale[1], 15.0 *
              scale[0], -9.0 * scale[1], 15.0 * scale[0], -1.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], 4.0 * scale[0],
              9.0 * scale[1], 10.0 * scale[0], 6.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 9.0 * scale[1], -13.0 * scale[0],
              14.0 * scale[1], -20.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -3.0 * scale[1], -13.0 *
              scale[0], -2.0 * scale[1], -13.0 * scale[0], 2.0 * scale[1])
    Curveto_r(6.0 * scale[0], 35.0 * scale[1], -3.0 * scale[0],
              64.0 * scale[1], -20.0 * scale[0], 69.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 3.0 * scale[1], -21.0 * scale[0],
              16.0 * scale[1], -24.0 * scale[0], 37.0 * scale[1])
    Lineto_r(-4.0 * scale[0], 31.0 * scale[1])
    Lineto_r(-2.0 * scale[0], -35.0 * scale[1])
    te.end_fill()
    Moveto(887.0 * scale[0], 972.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-21.0 * scale[0], -23.0 * scale[1], -21.0 *
              scale[0], -28.0 * scale[1], -1.0 * scale[0], -36.0 * scale[1])
    Curveto_r(9.0 * scale[0], -3.0 * scale[1], 12.0 *
              scale[0], -2.0 * scale[1], 9.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 5.0 * scale[1], -1.0 * scale[0],
              17.0 * scale[1], 6.0 * scale[0], 25.0 * scale[1])
    Curveto_r(18.0 * scale[0], 22.0 * scale[1], 5.0 * scale[0],
              27.0 * scale[1], -14.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(950.0 * scale[0], 981.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 18.0 * scale[1], -14.0 * scale[0],
              21.0 * scale[1], -14.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(961.0 * scale[0], 934.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(536.0 * scale[0], 915.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(19.0 * scale[0], -29.0 * scale[1], 38.0 *
              scale[0], -28.0 * scale[1], 40.0 * scale[0], 1.0 * scale[1])
    Curveto_r(1.0 * scale[0], 15.0 * scale[1], 0.0 * scale[0],
              16.0 * scale[1], -3.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -24.0 * scale[1], -20.0 *
              scale[0], -23.0 * scale[1], -28.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 11.0 * scale[1], -11.0 * scale[0],
              20.0 * scale[1], -16.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -2.0 * scale[0], -
              11.0 * scale[1], 7.0 * scale[0], -25.0 * scale[1])
    te.end_fill()
    Moveto(879.0 * scale[0], 909.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -39.0 * scale[1], -6.0 * scale[0], -
              91.0 * scale[1], -2.0 * scale[0], -81.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 10.0 * scale[0],
              9.0 * scale[1], 16.0 * scale[0], 5.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 8.0 * scale[0],
              0.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 20.0 * scale[1], 14.0 * scale[0],
              28.0 * scale[1], 31.0 * scale[0], 11.0 * scale[1])
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 20.0 * scale[0], -
              10.0 * scale[1], 30.0 * scale[0], -6.0 * scale[1])
    Curveto_r(15.0 * scale[0], 6.0 * scale[1], 15.0 * scale[0],
              7.0 * scale[1], -3.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 2.0 * scale[1], -32.0 * scale[0],
              16.0 * scale[1], -47.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 14.0 * scale[1], -28.0 * scale[0],
              24.0 * scale[1], -29.0 * scale[0], 21.0 * scale[1])
    te.end_fill()
    Moveto(570.0 * scale[0], 865.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -8.0 * scale[1], -11.0 * scale[0], -
              15.0 * scale[1], -9.0 * scale[0], -16.0 * scale[1])
    Curveto_r(37.0 * scale[0], -7.0 * scale[1], 40.0 *
              scale[0], -7.0 * scale[1], 30.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 7.0 * scale[1], -8.0 * scale[0],
              16.0 * scale[1], -4.0 * scale[0], 19.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], 4.0 * scale[0],
              7.0 * scale[1], 1.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              7.0 * scale[1], -18.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(600.0 * scale[0], 826.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(750.0 * scale[0], 816.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -6.0 * scale[0], -
              17.0 * scale[1], -12.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -3.0 * scale[1], -3.0 *
              scale[0], -3.0 * scale[1], 10.0 * scale[0], 0.0 * scale[1])
    Curveto_r(13.0 * scale[0], 3.0 * scale[1], 22.0 * scale[0],
              1.0 * scale[1], 22.0 * scale[0], -6.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              9.0 * scale[1], 9.0 * scale[0], -5.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 12.0 * scale[0],
              1.0 * scale[1], 16.0 * scale[0], -5.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 12.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -10.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 3.0 * scale[0],
              7.0 * scale[1], -8.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 8.0 * scale[1], -28.0 * scale[0],
              21.0 * scale[1], -37.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 12.0 * scale[1], -18.0 * scale[0],
              13.0 * scale[1], -18.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(834.0 * scale[0], 812.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(11.0 * scale[0], -12.0 * scale[1], 16.0 * scale[0], -
              22.0 * scale[1], 11.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -1.0 * scale[0], -
              8.0 * scale[1], 6.0 * scale[0], -17.0 * scale[1])
    Curveto_r(12.0 * scale[0], -15.0 * scale[1], 12.0 *
              scale[0], -16.0 * scale[1], -6.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 5.0 * scale[1], -9.0 * scale[0], -
              3.0 * scale[1], 13.0 * scale[0], -22.0 * scale[1])
    Curveto_r(38.0 * scale[0], -34.0 * scale[1], 42.0 * scale[0], -
              62.0 * scale[1], 10.0 * scale[0], -63.0 * scale[1])
    Curveto_r(-25.0 * scale[0], -1.0 * scale[1], -19.0 *
              scale[0], -4.0 * scale[1], 25.0 * scale[0], -13.0 * scale[1])
    Curveto_r(18.0 * scale[0], -4.0 * scale[1], 25.0 * scale[0], -
              11.0 * scale[1], 21.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -9.0 * scale[1], -4.0 *
              scale[0], -9.0 * scale[1], 6.0 * scale[0], 0.0 * scale[1])
    Curveto_r(13.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              37.0 * scale[1], -11.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -4.0 * scale[1], -9.0 * scale[0],
              3.0 * scale[1], -9.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 24.0 * scale[1], 10.0 * scale[0],
              27.0 * scale[1], 29.0 * scale[0], 9.0 * scale[1])
    Curveto_r(11.0 * scale[0], -11.0 * scale[1], 14.0 *
              scale[0], -10.0 * scale[1], 18.0 * scale[0], 0.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 9.0 * scale[0],
              10.0 * scale[1], 14.0 * scale[0], 7.0 * scale[1])
    Curveto_r(5.0 * scale[0], -4.0 * scale[1], 6.0 * scale[0],
              1.0 * scale[1], 3.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 10.0 * scale[1], -15.0 * scale[0],
              14.0 * scale[1], -35.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-29.0 * scale[0], -4.0 * scale[1], -59.0 * scale[0],
              10.0 * scale[1], -59.0 * scale[0], 28.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 8.0 * scale[0],
              6.0 * scale[1], 18.0 * scale[0], 3.0 * scale[1])
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], -6.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 7.0 * scale[1], -21.0 * scale[0],
              17.0 * scale[1], -19.0 * scale[0], 23.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], -7.0 * scale[0],
              20.0 * scale[1], -22.0 * scale[0], 30.0 * scale[1])
    Lineto_r(-26.0 * scale[0], 20.0 * scale[1])
    Lineto_r(19.0 * scale[0], -22.0 * scale[1])
    te.end_fill()
    Moveto(558.0 * scale[0], 794.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -10.0 * scale[1], 4.0 * scale[0], -
              26.0 * scale[1], 12.0 * scale[0], -35.0 * scale[1])
    Curveto_r(34.0 * scale[0], -37.0 * scale[1], 48.0 * scale[0], -
              58.0 * scale[1], 42.0 * scale[0], -65.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -4.0 * scale[1], -1.0 *
              scale[0], -4.0 * scale[1], 6.0 * scale[0], 0.0 * scale[1])
    Curveto_r(7.0 * scale[0], 5.0 * scale[1], 12.0 * scale[0],
              1.0 * scale[1], 13.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 3.0 * scale[0], -
              13.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(2.0 * scale[0], 7.0 * scale[1], -11.0 * scale[0],
              32.0 * scale[1], -31.0 * scale[0], 54.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 23.0 * scale[1], -34.0 * scale[0],
              45.0 * scale[1], -31.0 * scale[0], 48.0 * scale[1])
    Curveto_r(2.0 * scale[0], 4.0 * scale[1], 0.0 * scale[0],
              13.0 * scale[1], -5.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 11.0 * scale[1], -9.0 * scale[0],
              10.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(123.0 * scale[0], 783.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -3.0 * scale[1], 0.0 * scale[0], -
              17.0 * scale[1], -9.0 * scale[0], -31.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -13.0 * scale[1], -12.0 *
              scale[0], -27.0 * scale[1], -8.0 * scale[0], -30.0 * scale[1])
    Curveto_r(4.0 * scale[0], -4.0 * scale[1], 9.0 * scale[0], -
              1.0 * scale[1], 11.0 * scale[0], 6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 11.0 * scale[0],
              19.0 * scale[1], 20.0 * scale[0], 27.0 * scale[1])
    Curveto_r(15.0 * scale[0], 15.0 * scale[1], 10.0 * scale[0],
              35.0 * scale[1], -9.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              3.0 * scale[1], -5.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(660.0 * scale[0], 755.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(19.0 * scale[0], -19.0 * scale[1], 36.0 * scale[0], -
              35.0 * scale[1], 39.0 * scale[0], -35.0 * scale[1])
    Curveto_r(3.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0],
              16.0 * scale[1], -29.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 19.0 * scale[1], -36.0 * scale[0],
              35.0 * scale[1], -39.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              16.0 * scale[1], 29.0 * scale[0], -35.0 * scale[1])
    te.end_fill()
    Moveto(165.0 * scale[0], 770.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 * scale[0], -
              7.0 * scale[1], 10.0 * scale[0], -4.0 * scale[1])
    Curveto_r(11.0 * scale[0], 5.0 * scale[1], 14.0 * scale[0],
              2.0 * scale[1], 8.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -12.0 * scale[1], -3.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -10.0 * scale[1])
    Curveto_r(7.0 * scale[0], 4.0 * scale[1], 20.0 * scale[0],
              0.0 * scale[1], 29.0 * scale[0], -9.0 * scale[1])
    Curveto_r(13.0 * scale[0], -13.0 * scale[1], 13.0 *
              scale[0], -19.0 * scale[1], 4.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -9.0 * scale[1], -5.0 * scale[0], -
              51.0 * scale[1], 12.0 * scale[0], -47.0 * scale[1])
    Curveto_r(7.0 * scale[0], 1.0 * scale[1], 12.0 * scale[0], -
              5.0 * scale[1], 12.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -8.0 * scale[1], 10.0 * scale[0], -
              26.0 * scale[1], 24.0 * scale[0], -39.0 * scale[1])
    Curveto_r(17.0 * scale[0], -16.0 * scale[1], 22.0 *
              scale[0], -18.0 * scale[1], 18.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 9.0 * scale[1], -7.0 * scale[0],
              21.0 * scale[1], -7.0 * scale[0], 26.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -4.0 * scale[0],
              7.0 * scale[1], -10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -10.0 * scale[0],
              1.0 * scale[1], -10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 24.0 * scale[1], 44.0 * scale[0],
              44.0 * scale[1], 55.0 * scale[0], 26.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 12.0 * scale[0], -
              7.0 * scale[1], 20.0 * scale[0], -3.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 21.0 * scale[0],
              0.0 * scale[1], 29.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], -6.0 * scale[1], 15.0 * scale[0], -
              9.0 * scale[1], 18.0 * scale[0], -6.0 * scale[1])
    Curveto_r(5.0 * scale[0], 5.0 * scale[1], 21.0 * scale[0], -
              25.0 * scale[1], 32.0 * scale[0], -59.0 * scale[1])
    Curveto_r(4.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0], -
              17.0 * scale[1], 12.0 * scale[0], -14.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -3.0 * scale[0],
              24.0 * scale[1], -13.0 * scale[0], 47.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 36.0 * scale[1], -22.0 * scale[0],
              41.0 * scale[1], -60.0 * scale[0], 47.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 4.0 * scale[1], -43.0 * scale[0],
              11.0 * scale[1], -44.0 * scale[0], 23.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], -2.0 * scale[0],
              12.0 * scale[1], -9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -12.0 * scale[1], -9.0 *
              scale[0], -14.0 * scale[1], -9.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 12.0 * scale[1], -4.0 * scale[0],
              11.0 * scale[1], -13.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -16.0 * scale[1], -14.0 *
              scale[0], -16.0 * scale[1], -26.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 15.0 * scale[1], -9.0 * scale[0],
              20.0 * scale[1], 0.0 * scale[0], 20.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], -3.0 * scale[0],
              16.0 * scale[1], -22.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-34.0 * scale[0], 35.0 * scale[1], -54.0 * scale[0],
              43.0 * scale[1], -65.0 * scale[0], 25.0 * scale[1])
    te.end_fill()
    Moveto(220.0 * scale[0], 776.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(725.0 * scale[0], 725.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(33.0 * scale[0], -27.0 * scale[1], 41.0 * scale[0], -
              29.0 * scale[1], 50.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], 11.0 * scale[1], -24.0 * scale[0],
              30.0 * scale[1], -58.0 * scale[0], 37.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 3.0 * scale[1], -18.0 * scale[0],
              1.0 * scale[1], 8.0 * scale[0], -21.0 * scale[1])
    te.end_fill()
    Moveto(5.0 * scale[0], 710.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(70.0 * scale[0], 706.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(0.0 * scale[0], 671.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 18.0 * scale[1], -14.0 * scale[0],
              21.0 * scale[1], -14.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(70.0 * scale[0], 671.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 18.0 * scale[1], -14.0 * scale[0],
              21.0 * scale[1], -14.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(106.0 * scale[0], 659.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 10.0 * scale[0], -
              6.0 * scale[1], 16.0 * scale[0], -3.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 8.0 * scale[0], -
              2.0 * scale[1], 4.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -21.0 * scale[1], -6.0 *
              scale[0], -22.0 * scale[1], 4.0 * scale[0], -6.0 * scale[1])
    Curveto_r(13.0 * scale[0], 20.0 * scale[1], 8.0 * scale[0],
              30.0 * scale[1], -15.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 1.0 * scale[1], -13.0 *
              scale[0], -2.0 * scale[1], -9.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(642.0 * scale[0], 646.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -8.0 * scale[1], 15.0 * scale[0], -
              12.0 * scale[1], 17.0 * scale[0], -11.0 * scale[1])
    Curveto_r(5.0 * scale[0], 6.0 * scale[1], -10.0 * scale[0],
              25.0 * scale[1], -20.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              6.0 * scale[1], 3.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(936.0 * scale[0], 643.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(555.0 * scale[0], 620.0 * scale[1], x, y)
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
    Moveto(20.0 * scale[0], 616.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 7.0 * scale[0], -
              7.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 12.0 *
              scale[0], -2.0 * scale[1], 9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], -25.0 * scale[0],
              14.0 * scale[1], -25.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(136.0 * scale[0], 611.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -2.0 * scale[0], -
              11.0 * scale[1], 5.0 * scale[0], -11.0 * scale[1])
    Curveto_r(18.0 * scale[0], 0.0 * scale[1], 2.0 * scale[0], -
              62.0 * scale[1], -21.0 * scale[0], -82.0 * scale[1])
    Curveto_r(-26.0 * scale[0], -21.0 * scale[1], -26.0 *
              scale[0], -32.0 * scale[1], 0.0 * scale[0], -18.0 * scale[1])
    Curveto_r(17.0 * scale[0], 9.0 * scale[1], 19.0 * scale[0],
              8.0 * scale[1], 13.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -10.0 * scale[1], -12.0 * scale[0], -
              25.0 * scale[1], -20.0 * scale[0], -34.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -13.0 * scale[1], -11.0 *
              scale[0], -16.0 * scale[1], 4.0 * scale[0], -16.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 24.0 * scale[0],
              7.0 * scale[1], 31.0 * scale[0], 16.0 * scale[1])
    Curveto_r(10.0 * scale[0], 12.0 * scale[1], 14.0 * scale[0],
              13.0 * scale[1], 19.0 * scale[0], 3.0 * scale[1])
    Curveto_r(6.0 * scale[0], -15.0 * scale[1], 63.0 * scale[0],
              40.0 * scale[1], 63.0 * scale[0], 60.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], -2.0 * scale[0],
              10.0 * scale[1], -8.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -20.0 * scale[0], -
              16.0 * scale[1], -34.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-35.0 * scale[0], -13.0 * scale[1], -42.0 *
              scale[0], -2.0 * scale[1], -34.0 * scale[0], 52.0 * scale[1])
    Curveto_r(6.0 * scale[0], 43.0 * scale[1], -5.0 * scale[0],
              79.0 * scale[1], -18.0 * scale[0], 58.0 * scale[1])
    te.end_fill()
    Moveto(256.0 * scale[0], 565.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -26.0 * scale[1], -7.0 *
              scale[0], -32.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(6.0 * scale[0], 10.0 * scale[1], 9.0 * scale[0],
              21.0 * scale[1], 6.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 3.0 * scale[1], -7.0 * scale[0], -
              2.0 * scale[1], -11.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(7.0 * scale[0], 559.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(390.0 * scale[0], 560.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 4.0 * scale[0], -
              10.0 * scale[1], 9.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              5.0 * scale[1], 16.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], -1.0 * scale[0],
              10.0 * scale[1], -9.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(96.0 * scale[0], 533.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(320.0 * scale[0], 539.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(11.0 * scale[0], -8.0 * scale[1], 12.0 * scale[0], -
              12.0 * scale[1], 3.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -13.0 * scale[0], -
              13.0 * scale[1], -13.0 * scale[0], -22.0 * scale[1])
    Curveto_r(0.0 * scale[0], -27.0 * scale[1], -12.0 * scale[0], -
              33.0 * scale[1], -26.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 15.0 * scale[1], -13.0 * scale[0],
              15.0 * scale[1], -14.0 * scale[0], -8.0 * scale[1])
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], -7.0 * scale[0], -
              36.0 * scale[1], -16.0 * scale[0], -48.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -27.0 * scale[1], -8.0 *
              scale[0], -52.0 * scale[1], 11.0 * scale[0], -25.0 * scale[1])
    Curveto_r(12.0 * scale[0], 17.0 * scale[1], 14.0 * scale[0],
              16.0 * scale[1], 32.0 * scale[0], -4.0 * scale[1])
    Curveto_r(19.0 * scale[0], -24.0 * scale[1], 82.0 * scale[0], -
              45.0 * scale[1], 69.0 * scale[0], -24.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], -3.0 * scale[0],
              11.0 * scale[1], 3.0 * scale[0], 11.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0], -
              6.0 * scale[1], 14.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], -7.0 * scale[1], 5.0 * scale[0], -
              1.0 * scale[1], 4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 15.0 * scale[1], -5.0 * scale[0],
              27.0 * scale[1], -9.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0],
              8.0 * scale[1], -9.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 13.0 * scale[1], -3.0 * scale[0],
              12.0 * scale[1], -7.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -21.0 * scale[1], -8.0 * scale[0], -
              21.0 * scale[1], -28.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 13.0 * scale[1], -20.0 * scale[0],
              25.0 * scale[1], -16.0 * scale[0], 49.0 * scale[1])
    Curveto_r(2.0 * scale[0], 18.0 * scale[1], 10.0 * scale[0],
              32.0 * scale[1], 18.0 * scale[0], 32.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0],
              4.0 * scale[1], 14.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], -22.0 * scale[0],
              32.0 * scale[1], -34.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              5.0 * scale[1], 4.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(30.0 * scale[0], 527.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -3.0 * scale[0], -
              22.0 * scale[1], -6.0 * scale[0], -31.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -12.0 * scale[1], 0.0 * scale[0], -
              16.0 * scale[1], 20.0 * scale[0], -16.0 * scale[1])
    Curveto_r(31.0 * scale[0], 0.0 * scale[1], 32.0 * scale[0],
              4.0 * scale[1], 6.0 * scale[0], 37.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 18.0 * scale[1], -20.0 * scale[0],
              21.0 * scale[1], -20.0 * scale[0], 10.0 * scale[1])
    te.end_fill()
    Moveto(370.0 * scale[0], 522.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], 3.0 * scale[0], -
              12.0 * scale[1], 18.0 * scale[0], -1.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 19.0 * scale[0],
              14.0 * scale[1], 21.0 * scale[0], 16.0 * scale[1])
    Curveto_r(2.0 * scale[0], 1.0 * scale[1], -6.0 * scale[0],
              1.0 * scale[1], -18.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -1.0 * scale[1], -21.0 *
              scale[0], -8.0 * scale[1], -21.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(383.0 * scale[0], 495.0 * scale[1], x, y)
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
    Moveto(462.0 * scale[0], 460.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(380.0 * scale[0], 444.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 5.0 * scale[0], -
              12.0 * scale[1], 10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 8.0 * scale[0],
              11.0 * scale[1], 5.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 14.0 * scale[1], -15.0 * scale[0],
              11.0 * scale[1], -15.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(930.0 * scale[0], 420.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(433.0 * scale[0], 403.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -17.0 * scale[1], 4.0 * scale[0], -
              19.0 * scale[1], 14.0 * scale[0], -11.0 * scale[1])
    Curveto_r(15.0 * scale[0], 12.0 * scale[1], 18.0 * scale[0],
              22.0 * scale[1], 4.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -4.0 * scale[1], -11.0 * scale[0],
              0.0 * scale[1], -14.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 7.0 * scale[1], -4.0 * scale[0],
              3.0 * scale[1], -4.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(959.0 * scale[0], 395.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -16.0 * scale[1], -10.0 * scale[0], -
              31.0 * scale[1], -16.0 * scale[0], -31.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -1.0 * scale[1], -33.0 *
              scale[0], -2.0 * scale[1], -58.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 0.0 * scale[1], -45.0 * scale[0], -
              6.0 * scale[1], -45.0 * scale[0], -12.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 9.0 * scale[0], -
              8.0 * scale[1], 21.0 * scale[0], -4.0 * scale[1])
    Curveto_r(25.0 * scale[0], 8.0 * scale[1], 92.0 * scale[0], -
              3.0 * scale[1], 85.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], -1.0 * scale[0], -
              21.0 * scale[1], 4.0 * scale[0], -37.0 * scale[1])
    Curveto_r(9.0 * scale[0], -25.0 * scale[1], 9.0 * scale[0], -
              23.0 * scale[1], 6.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 26.0 * scale[1], 1.0 * scale[0],
              51.0 * scale[1], 6.0 * scale[0], 56.0 * scale[1])
    Curveto_r(5.0 * scale[0], 5.0 * scale[1], 8.0 * scale[0],
              20.0 * scale[1], 6.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 21.0 * scale[1], -5.0 * scale[0],
              21.0 * scale[1], -9.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(55.0 * scale[0], 399.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0], -
              12.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 17.0 * scale[1], 1.0 * scale[0],
              20.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(655.0 * scale[0], 360.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-170.0 * scale[0], -6.0 * scale[1])
    Lineto_r(173.0 * scale[0], -2.0 * scale[1])
    Curveto_r(109.0 * scale[0], -1.0 * scale[1], 172.0 * scale[0],
              2.0 * scale[1], 172.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -1.0 * scale[0],
              9.0 * scale[1], -2.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -1.0 * scale[1], -79.0 * scale[0], -
              5.0 * scale[1], -173.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(12.0 * scale[0], 348.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -8.0 * scale[1], -11.0 * scale[0], -
              41.0 * scale[1], -10.0 * scale[0], -92.0 * scale[1])
    Curveto_r(2.0 * scale[0], -72.0 * scale[1], 2.0 * scale[0], -
              74.0 * scale[1], 5.0 * scale[0], -21.0 * scale[1])
    Curveto_r(2.0 * scale[0], 33.0 * scale[1], 6.0 * scale[0],
              67.0 * scale[1], 10.0 * scale[0], 75.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], 5.0 * scale[0],
              20.0 * scale[1], 4.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 6.0 * scale[1], 6.0 * scale[0],
              14.0 * scale[1], 16.0 * scale[0], 16.0 * scale[1])
    Curveto_r(14.0 * scale[0], 4.0 * scale[1], 14.0 * scale[0],
              5.0 * scale[1], 3.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -21.0 * scale[0], -
              4.0 * scale[1], -28.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(288.0 * scale[0], 353.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 30.0 *
              scale[0], -2.0 * scale[1], 40.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 0.0 * scale[1], -30.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(953.0 * scale[0], 200.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -28.0 * scale[1], 4.0 * scale[0], -
              45.0 * scale[1], 8.0 * scale[0], -39.0 * scale[1])
    Curveto_r(7.0 * scale[0], 12.0 * scale[1], 3.0 * scale[0],
              78.0 * scale[1], -5.0 * scale[0], 86.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 3.0 * scale[1], -4.0 * scale[0], -
              19.0 * scale[1], -3.0 * scale[0], -47.0 * scale[1])
    te.end_fill()
    Moveto(3.0 * scale[0], 110.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -36.0 * scale[1], 2.0 * scale[0], -
              50.0 * scale[1], 4.0 * scale[0], -32.0 * scale[1])
    Curveto_r(2.0 * scale[0], 17.0 * scale[1], 2.0 * scale[0],
              47.0 * scale[1], 0.0 * scale[0], 65.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 17.0 * scale[1], -4.0 * scale[0],
              3.0 * scale[1], -4.0 * scale[0], -33.0 * scale[1])
    te.end_fill()
    Moveto(950.0 * scale[0], 100.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -22.0 * scale[1], 3.0 * scale[0], -
              40.0 * scale[1], 8.0 * scale[0], -40.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 6.0 * scale[0],
              18.0 * scale[1], 4.0 * scale[0], 40.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 22.0 * scale[1], -6.0 * scale[0],
              40.0 * scale[1], -8.0 * scale[0], 40.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              18.0 * scale[1], -4.0 * scale[0], -40.0 * scale[1])
    te.end_fill()
    Moveto(42.0 * scale[0], 110.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(938.0 * scale[0], 31.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -10.0 * scale[1], -18.0 *
              scale[0], -21.0 * scale[1], -18.0 * scale[0], -24.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 8.0 * scale[0], -
              7.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              2.0 * scale[1], 2.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 8.0 * scale[1], -12.0 * scale[0],
              10.0 * scale[1], 3.0 * scale[0], 10.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0],
              7.0 * scale[1], 17.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 18.0 * scale[1], -1.0 * scale[0],
              18.0 * scale[1], -22.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(10.0 * scale[0], 20.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -14.0 * scale[1], 20.0 * scale[0], -
              20.0 * scale[1], 43.0 * scale[0], -19.0 * scale[1])
    Lineto_r(32.0 * scale[0], 1.0 * scale[1])
    Lineto_r(-32.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 5.0 * scale[1], -33.0 * scale[0],
              14.0 * scale[1], -33.0 * scale[0], 19.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              10.0 * scale[1], -10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              6.0 * scale[1], 0.0 * scale[0], -20.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#1d1505')
    te.end_fill()
    Moveto(11.0 * scale[0], 1391.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -8.0 * scale[1], 30.0 * scale[0], -4.0 * scale[1])
    Curveto_r(24.0 * scale[0], 3.0 * scale[1], 46.0 * scale[0],
              7.0 * scale[1], 48.0 * scale[0], 9.0 * scale[1])
    Curveto_r(10.0 * scale[0], 9.0 * scale[1], -65.0 * scale[0],
              3.0 * scale[1], -78.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(894.0 * scale[0], 1390.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(16.0 * scale[0], -5.0 * scale[1], 32.0 *
              scale[0], -7.0 * scale[1], 36.0 * scale[0], -5.0 * scale[1])
    Curveto_r(12.0 * scale[0], 8.0 * scale[1], 30.0 * scale[0], -
              39.0 * scale[1], 33.0 * scale[0], -90.0 * scale[1])
    Curveto_r(3.0 * scale[0], -45.0 * scale[1], 4.0 * scale[0], -
              43.0 * scale[1], 5.0 * scale[0], 16.0 * scale[1])
    Curveto_r(2.0 * scale[0], 77.0 * scale[1], -7.0 * scale[0],
              89.0 * scale[1], -62.0 * scale[0], 88.0 * scale[1])
    Curveto_r(-40.0 * scale[0], -1.0 * scale[1], -40.0 *
              scale[0], -1.0 * scale[1], -12.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(958.0 * scale[0], 1123.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-3.0 * scale[0], -88.0 * scale[1])
    Lineto_r(-52.0 * scale[0], -3.0 * scale[1])
    Lineto_r(-53.0 * scale[0], -3.0 * scale[1])
    Lineto_r(0.0 * scale[0], -50.0 * scale[1])
    Curveto_r(0.0 * scale[0], -27.0 * scale[1], 4.0 * scale[0], -
              49.0 * scale[1], 9.0 * scale[0], -49.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0], -
              8.0 * scale[1], 14.0 * scale[0], -17.0 * scale[1])
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 4.0 * scale[0],
              5.0 * scale[1], 2.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 56.0 * scale[1], 1.0 * scale[0],
              69.0 * scale[1], 22.0 * scale[0], 52.0 * scale[1])
    Curveto_r(9.0 * scale[0], -9.0 * scale[1], 13.0 *
              scale[0], -8.0 * scale[1], 13.0 * scale[0], 0.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 10.0 * scale[0],
              11.0 * scale[1], 23.0 * scale[0], 11.0 * scale[1])
    Curveto_r(19.0 * scale[0], -1.0 * scale[1], 20.0 *
              scale[0], -2.0 * scale[1], 6.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -10.0 * scale[1], -14.0 *
              scale[0], -14.0 * scale[1], -3.0 * scale[0], -25.0 * scale[1])
    Curveto_r(12.0 * scale[0], -11.0 * scale[1], 14.0 *
              scale[0], -10.0 * scale[1], 14.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 15.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], 10.0 * scale[0], 3.0 * scale[1])
    Curveto_r(7.0 * scale[0], -10.0 * scale[1], 10.0 * scale[0],
              25.0 * scale[1], 10.0 * scale[0], 108.0 * scale[1])
    Curveto_r(0.0 * scale[0], 67.0 * scale[1], -2.0 * scale[0],
              122.0 * scale[1], -5.0 * scale[0], 122.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0], -
              39.0 * scale[1], -7.0 * scale[0], -87.0 * scale[1])
    te.end_fill()
    Moveto(0.0 * scale[0], 1040.0 * scale[1], x, y)
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
    Moveto(118.0 * scale[0], 1033.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(373.0 * scale[0], 1033.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(15.0 * scale[0], -2.0 * scale[1], 37.0 *
              scale[0], -2.0 * scale[1], 50.0 * scale[0], 0.0 * scale[1])
    Curveto_r(12.0 * scale[0], 2.0 * scale[1], 0.0 * scale[0],
              4.0 * scale[1], -28.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-27.0 * scale[0], 0.0 * scale[1], -38.0 *
              scale[0], -2.0 * scale[1], -22.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(490.0 * scale[0], 1011.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -17.0 * scale[1], 5.0 * scale[0], -
              31.0 * scale[1], 10.0 * scale[0], -31.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              6.0 * scale[1], 10.0 * scale[0], -14.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              18.0 * scale[1], 10.0 * scale[0], -21.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              0.0 * scale[1], 4.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 19.0 * scale[1], 29.0 * scale[0],
              78.0 * scale[1], 41.0 * scale[0], 69.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 10.0 * scale[0], -
              39.0 * scale[1], 10.0 * scale[0], -79.0 * scale[1])
    Curveto_r(0.0 * scale[0], -39.0 * scale[1], 3.0 * scale[0], -
              69.0 * scale[1], 6.0 * scale[0], -67.0 * scale[1])
    Curveto_r(4.0 * scale[0], 2.0 * scale[1], 10.0 * scale[0], -
              8.0 * scale[1], 13.0 * scale[0], -21.0 * scale[1])
    Curveto_r(4.0 * scale[0], -14.0 * scale[1], 37.0 * scale[0], -
              56.0 * scale[1], 74.0 * scale[0], -93.0 * scale[1])
    Curveto_r(55.0 * scale[0], -55.0 * scale[1], 78.0 * scale[0], -
              71.0 * scale[1], 132.0 * scale[0], -89.0 * scale[1])
    Curveto_r(36.0 * scale[0], -11.0 * scale[1], 83.0 * scale[0], -
              24.0 * scale[1], 105.0 * scale[0], -27.0 * scale[1])
    Curveto_r(38.0 * scale[0], -5.0 * scale[1], 39.0 *
              scale[0], -4.0 * scale[1], 15.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 8.0 * scale[1], -44.0 * scale[0],
              17.0 * scale[1], -67.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 3.0 * scale[1], -52.0 * scale[0],
              15.0 * scale[1], -64.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 21.0 * scale[1], -34.0 * scale[0],
              24.0 * scale[1], -24.0 * scale[0], 9.0 * scale[1])
    Curveto_r(11.0 * scale[0], -18.0 * scale[1], -10.0 *
              scale[0], -10.0 * scale[1], -40.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 15.0 * scale[1], -24.0 * scale[0],
              23.0 * scale[1], -16.0 * scale[0], 19.0 * scale[1])
    Curveto_r(9.0 * scale[0], -5.0 * scale[1], 12.0 *
              scale[0], -3.0 * scale[1], 9.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], -13.0 * scale[0],
              14.0 * scale[1], -23.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0],
              7.0 * scale[1], -22.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 12.0 * scale[1], -3.0 * scale[0],
              12.0 * scale[1], 5.0 * scale[0], 1.0 * scale[1])
    Curveto_r(6.0 * scale[0], -8.0 * scale[1], 12.0 * scale[0], -
              9.0 * scale[1], 16.0 * scale[0], -3.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], -9.0 * scale[0],
              15.0 * scale[1], -27.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 8.0 * scale[1], -27.0 * scale[0],
              14.0 * scale[1], -17.0 * scale[0], 18.0 * scale[1])
    Curveto_r(15.0 * scale[0], 5.0 * scale[1], 30.0 * scale[0],
              21.0 * scale[1], 30.0 * scale[0], 33.0 * scale[1])
    Curveto_r(0.0 * scale[0], 3.0 * scale[1], -11.0 * scale[0],
              11.0 * scale[1], -24.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 8.0 * scale[1], -22.0 * scale[0],
              18.0 * scale[1], -19.0 * scale[0], 28.0 * scale[1])
    Curveto_r(4.0 * scale[0], 10.0 * scale[1], 2.0 * scale[0],
              13.0 * scale[1], -5.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -4.0 * scale[1], -12.0 *
              scale[0], -1.0 * scale[1], -12.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], 5.0 * scale[0],
              16.0 * scale[1], 11.0 * scale[0], 16.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], -1.0 * scale[0],
              20.0 * scale[1], 4.0 * scale[0], 28.0 * scale[1])
    Curveto_r(6.0 * scale[0], 10.0 * scale[1], 9.0 * scale[0],
              8.0 * scale[1], 10.0 * scale[0], -11.0 * scale[1])
    Curveto_r(1.0 * scale[0], -20.0 * scale[1], 3.0 * scale[0], -
              18.0 * scale[1], 9.0 * scale[0], 10.0 * scale[1])
    Lineto_r(7.0 * scale[0], 35.0 * scale[1])
    Lineto_r(2.0 * scale[0], -31.0 * scale[1])
    Curveto_r(1.0 * scale[0], -23.0 * scale[1], 7.0 * scale[0], -
              33.0 * scale[1], 21.0 * scale[0], -37.0 * scale[1])
    Curveto_r(18.0 * scale[0], -5.0 * scale[1], 27.0 * scale[0], -
              34.0 * scale[1], 21.0 * scale[0], -69.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 5.0 * scale[0], -
              5.0 * scale[1], 13.0 * scale[0], -2.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 18.0 * scale[0], -
              6.0 * scale[1], 25.0 * scale[0], -23.0 * scale[1])
    Curveto_r(6.0 * scale[0], -16.0 * scale[1], 31.0 * scale[0], -
              41.0 * scale[1], 55.0 * scale[0], -56.0 * scale[1])
    Curveto_r(47.0 * scale[0], -29.0 * scale[1], 65.0 * scale[0], -
              35.0 * scale[1], 47.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 8.0 * scale[1], -9.0 * scale[0],
              16.0 * scale[1], -6.0 * scale[0], 19.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              11.0 * scale[1], -10.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 7.0 * scale[1], -15.0 * scale[0],
              19.0 * scale[1], -15.0 * scale[0], 26.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -10.0 * scale[0],
              14.0 * scale[1], -25.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-32.0 * scale[0], 0.0 * scale[1], -45.0 * scale[0],
              26.0 * scale[1], -45.0 * scale[0], 92.0 * scale[1])
    Curveto_r(0.0 * scale[0], 47.0 * scale[1], 3.0 * scale[0],
              55.0 * scale[1], 28.0 * scale[0], 70.0 * scale[1])
    Lineto_r(27.0 * scale[0], 17.0 * scale[1])
    Lineto_r(-66.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-36.0 * scale[0], 0.0 * scale[1], -107.0 * scale[0],
              3.0 * scale[1], -157.0 * scale[0], 6.0 * scale[1])
    Lineto_r(-92.0 * scale[0], 7.0 * scale[1])
    Lineto_r(0.0 * scale[0], -32.0 * scale[1])
    te.end_fill()
    Moveto(905.0 * scale[0], 960.0 * scale[1], x, y)
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
    Moveto(890.0 * scale[0], 876.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 7.0 * scale[0], -
              7.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 12.0 *
              scale[0], -2.0 * scale[1], 9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], -25.0 * scale[0],
              14.0 * scale[1], -25.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(550.0 * scale[0], 806.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -31.0 * scale[1], 6.0 * scale[0], -
              34.0 * scale[1], 13.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 11.0 * scale[1], 1.0 * scale[0],
              23.0 * scale[1], -4.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              6.0 * scale[1], -9.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(101.0 * scale[0], 804.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(18.0 * scale[0], -22.0 * scale[1], 2.0 * scale[0], -
              63.0 * scale[1], -26.0 * scale[0], -70.0 * scale[1])
    Curveto_r(-31.0 * scale[0], -8.0 * scale[1], -55.0 * scale[0],
              11.0 * scale[1], -55.0 * scale[0], 43.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -4.0 * scale[0],
              21.0 * scale[1], -10.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -10.0 * scale[0], -
              23.0 * scale[1], -10.0 * scale[0], -43.0 * scale[1])
    Curveto_r(0.0 * scale[0], -35.0 * scale[1], 2.0 * scale[0], -
              37.0 * scale[1], 37.0 * scale[0], -40.0 * scale[1])
    Curveto_r(45.0 * scale[0], -3.0 * scale[1], 56.0 * scale[0], -
              12.0 * scale[1], 82.0 * scale[0], -65.0 * scale[1])
    Curveto_r(12.0 * scale[0], -23.0 * scale[1], 21.0 * scale[0], -
              36.0 * scale[1], 21.0 * scale[0], -29.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -7.0 * scale[0],
              27.0 * scale[1], -16.0 * scale[0], 43.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 45.0 * scale[1], -25.0 * scale[0],
              68.0 * scale[1], -9.0 * scale[0], 93.0 * scale[1])
    Curveto_r(8.0 * scale[0], 13.0 * scale[1], 12.0 * scale[0],
              26.0 * scale[1], 8.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -1.0 * scale[0],
              7.0 * scale[1], 5.0 * scale[0], 7.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0], -
              5.0 * scale[1], 17.0 * scale[0], -10.0 * scale[1])
    Curveto_r(3.0 * scale[0], -6.0 * scale[1], 16.0 * scale[0], -
              8.0 * scale[1], 28.0 * scale[0], -5.0 * scale[1])
    Curveto_r(16.0 * scale[0], 5.0 * scale[1], 31.0 * scale[0], -
              3.0 * scale[1], 57.0 * scale[0], -30.0 * scale[1])
    Curveto_r(18.0 * scale[0], -19.0 * scale[1], 28.0 * scale[0], -
              35.0 * scale[1], 21.0 * scale[0], -35.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -11.0 *
              scale[0], -3.0 * scale[1], -1.0 * scale[0], -15.0 * scale[1])
    Curveto_r(13.0 * scale[0], -15.0 * scale[1], 5.0 * scale[0], -
              39.0 * scale[1], -11.0 * scale[0], -30.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 7.0 * scale[1], -13.0 *
              scale[0], -8.0 * scale[1], -3.0 * scale[0], -18.0 * scale[1])
    Curveto_r(8.0 * scale[0], -7.0 * scale[1], 44.0 * scale[0],
              36.0 * scale[1], 44.0 * scale[0], 52.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -58.0 * scale[0],
              79.0 * scale[1], -81.0 * scale[0], 92.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 5.0 * scale[1], -39.0 * scale[0],
              13.0 * scale[1], -64.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-38.0 * scale[0], 7.0 * scale[1], -43.0 * scale[0],
              6.0 * scale[1], -34.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(304.0 * scale[0], 774.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -19.0 * scale[1], -3.0 *
              scale[0], -49.0 * scale[1], 2.0 * scale[0], -66.0 * scale[1])
    Curveto_r(7.0 * scale[0], -25.0 * scale[1], 9.0 * scale[0], -
              19.0 * scale[1], 9.0 * scale[0], 36.0 * scale[1])
    Curveto_r(0.0 * scale[0], 36.0 * scale[1], -1.0 * scale[0],
              66.0 * scale[1], -2.0 * scale[0], 66.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 0.0 * scale[1], -5.0 * scale[0], -
              16.0 * scale[1], -9.0 * scale[0], -36.0 * scale[1])
    te.end_fill()
    Moveto(414.0 * scale[0], 752.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -10.0 * scale[1], -14.0 * scale[0], -
              33.0 * scale[1], -17.0 * scale[0], -52.0 * scale[1])
    Lineto_r(-6.0 * scale[0], -35.0 * scale[1])
    Lineto_r(12.0 * scale[0], 36.0 * scale[1])
    Curveto_r(7.0 * scale[0], 20.0 * scale[1], 18.0 * scale[0],
              44.0 * scale[1], 26.0 * scale[0], 53.0 * scale[1])
    Curveto_r(7.0 * scale[0], 9.0 * scale[1], 9.0 * scale[0],
              16.0 * scale[1], 5.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0], -
              8.0 * scale[1], -20.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(561.0 * scale[0], 750.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -14.0 * scale[1], -2.0 * scale[0], -
              47.0 * scale[1], -5.0 * scale[0], -75.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -49.0 * scale[1], -5.0 *
              scale[0], -49.0 * scale[1], 4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 22.0 * scale[1], 17.0 * scale[0],
              45.0 * scale[1], 24.0 * scale[0], 50.0 * scale[1])
    Curveto_r(12.0 * scale[0], 9.0 * scale[1], 11.0 * scale[0],
              15.0 * scale[1], -5.0 * scale[0], 35.0 * scale[1])
    Lineto_r(-19.0 * scale[0], 25.0 * scale[1])
    Lineto_r(1.0 * scale[0], -25.0 * scale[1])
    te.end_fill()
    Moveto(870.0 * scale[0], 750.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -17.0 * scale[1], 30.0 * scale[0], -
              31.0 * scale[1], 59.0 * scale[0], -27.0 * scale[1])
    Curveto_r(17.0 * scale[0], 3.0 * scale[1], 32.0 * scale[0],
              0.0 * scale[1], 35.0 * scale[0], -6.0 * scale[1])
    Curveto_r(2.0 * scale[0], -7.0 * scale[1], 5.0 * scale[0], -
              2.0 * scale[1], 5.0 * scale[0], 10.0 * scale[1])
    Curveto_r(1.0 * scale[0], 15.0 * scale[1], -3.0 * scale[0],
              21.0 * scale[1], -13.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -3.0 * scale[1], -30.0 *
              scale[0], -1.0 * scale[1], -50.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 6.0 * scale[1], -36.0 * scale[0],
              7.0 * scale[1], -36.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(617.0 * scale[0], 690.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -11.0 * scale[1], 9.0 * scale[0], -
              22.0 * scale[1], 13.0 * scale[0], -25.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 6.0 * scale[0],
              4.0 * scale[1], 3.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 11.0 * scale[1], -9.0 * scale[0],
              22.0 * scale[1], -13.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -6.0 * scale[0], -
              4.0 * scale[1], -3.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(0.0 * scale[0], 651.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              15.0 * scale[1], 17.0 * scale[0], -22.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 15.0 *
              scale[0], -12.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 23.0 * scale[1], -21.0 * scale[0],
              28.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(660.0 * scale[0], 631.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 18.0 * scale[1], -14.0 * scale[0],
              21.0 * scale[1], -14.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(261.0 * scale[0], 605.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -11.0 * scale[1], 4.0 * scale[0], -
              31.0 * scale[1], 8.0 * scale[0], -45.0 * scale[1])
    Lineto_r(7.0 * scale[0], -25.0 * scale[1])
    Lineto_r(6.0 * scale[0], 27.0 * scale[1])
    Curveto_r(3.0 * scale[0], 16.0 * scale[1], -1.0 * scale[0],
              36.0 * scale[1], -8.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 17.0 * scale[1], -13.0 * scale[0],
              17.0 * scale[1], -13.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(30.0 * scale[0], 579.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -24.0 * scale[1], -4.0 * scale[0], -
              30.0 * scale[1], -15.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 5.0 * scale[1], -15.0 * scale[0], -
              11.0 * scale[1], -15.0 * scale[0], -106.0 * scale[1])
    Curveto_r(0.0 * scale[0], -98.0 * scale[1], 2.0 * scale[0], -
              109.0 * scale[1], 15.0 * scale[0], -98.0 * scale[1])
    Curveto_r(12.0 * scale[0], 10.0 * scale[1], 64.0 * scale[0],
              12.0 * scale[1], 235.0 * scale[0], 7.0 * scale[1])
    Lineto_r(220.0 * scale[0], -6.0 * scale[1])
    Lineto_r(-1.0 * scale[0], 47.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 26.0 * scale[1], -4.0 * scale[0],
              37.0 * scale[1], -6.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -12.0 * scale[1], -11.0 * scale[0], -
              27.0 * scale[1], -19.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -10.0 * scale[1], -14.0 *
              scale[0], -7.0 * scale[1], -14.0 * scale[0], 21.0 * scale[1])
    Curveto_r(0.0 * scale[0], 19.0 * scale[1], -11.0 * scale[0],
              51.0 * scale[1], -26.0 * scale[0], 74.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 22.0 * scale[1], -23.0 * scale[0],
              32.0 * scale[1], -20.0 * scale[0], 22.0 * scale[1])
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 6.0 * scale[0], -
              27.0 * scale[1], 6.0 * scale[0], -38.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 7.0 * scale[0], -
              19.0 * scale[1], 15.0 * scale[0], -19.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0], -
              9.0 * scale[1], 15.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -21.0 * scale[1], -2.0 * scale[0], -
              22.0 * scale[1], -14.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 23.0 * scale[1], -25.0 * scale[0],
              14.0 * scale[1], -20.0 * scale[0], -25.0 * scale[1])
    Curveto_r(2.0 * scale[0], -18.0 * scale[1], 1.0 * scale[0], -
              26.0 * scale[1], -2.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -10.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              5.0 * scale[1], -3.0 * scale[0], -11.0 * scale[1])
    Curveto_r(13.0 * scale[0], -21.0 * scale[1], -50.0 * scale[0],
              0.0 * scale[1], -69.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 20.0 * scale[1], -20.0 * scale[0],
              21.0 * scale[1], -32.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -28.0 * scale[1], -29.0 *
              scale[0], -2.0 * scale[1], -9.0 * scale[0], 28.0 * scale[1])
    Curveto_r(16.0 * scale[0], 25.0 * scale[1], 16.0 * scale[0],
              40.0 * scale[1], -4.0 * scale[0], 130.0 * scale[1])
    Lineto_r(-8.0 * scale[0], 40.0 * scale[1])
    Lineto_r(-8.0 * scale[0], -48.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -52.0 * scale[1], -59.0 * scale[0], -
              121.0 * scale[1], -69.0 * scale[0], -95.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 10.0 * scale[1], -9.0 * scale[0],
              9.0 * scale[1], -19.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -9.0 * scale[1], -21.0 * scale[0], -
              16.0 * scale[1], -31.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0],
              3.0 * scale[1], -4.0 * scale[0], 16.0 * scale[1])
    Curveto_r(8.0 * scale[0], 9.0 * scale[1], 17.0 * scale[0],
              24.0 * scale[1], 20.0 * scale[0], 34.0 * scale[1])
    Curveto_r(6.0 * scale[0], 15.0 * scale[1], 4.0 * scale[0],
              16.0 * scale[1], -14.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -10.0 * scale[1], -20.0 *
              scale[0], -9.0 * scale[1], -14.0 * scale[0], 13.0 * scale[1])
    Curveto_r(6.0 * scale[0], 22.0 * scale[1], 6.0 * scale[0],
              22.0 * scale[1], -18.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-28.0 * scale[0], -32.0 * scale[1], -74.0 *
              scale[0], -39.0 * scale[1], -62.0 * scale[0], -10.0 * scale[1])
    Curveto_r(10.0 * scale[0], 26.0 * scale[1], 19.0 * scale[0],
              112.0 * scale[1], 11.0 * scale[0], 112.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0], -
              14.0 * scale[1], -6.0 * scale[0], -31.0 * scale[1])
    te.end_fill()
    Moveto_r(14.0 * scale[0], -165.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], 10.0 * scale[0], -
              12.0 * scale[1], 16.0 * scale[0], -9.0 * scale[1])
    Curveto_r(14.0 * scale[0], 9.0 * scale[1], 30.0 * scale[0], -
              3.0 * scale[1], 24.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -14.0 * scale[1], -64.0 *
              scale[0], -20.0 * scale[1], -64.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 6.0 * scale[0],
              10.0 * scale[1], 13.0 * scale[0], 11.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              2.0 * scale[1], 0.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 5.0 * scale[1], -18.0 * scale[0],
              33.0 * scale[1], -4.0 * scale[0], 33.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0], -
              7.0 * scale[1], 15.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(142.0 * scale[0], 580.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(310.0 * scale[0], 530.0 * scale[1], x, y)
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
    Moveto(282.0 * scale[0], 510.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(957.0 * scale[0], 363.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -5.0 * scale[1], 0.0 * scale[0], -
              39.0 * scale[1], 3.0 * scale[0], -78.0 * scale[1])
    Lineto_r(7.0 * scale[0], -70.0 * scale[1])
    Lineto_r(1.0 * scale[0], 78.0 * scale[1])
    Curveto_r(2.0 * scale[0], 71.0 * scale[1], -1.0 * scale[0],
              89.0 * scale[1], -11.0 * scale[0], 70.0 * scale[1])
    te.end_fill()
    Moveto(963.0 * scale[0], 120.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -30.0 * scale[1], 2.0 * scale[0], -
              43.0 * scale[1], 4.0 * scale[0], -28.0 * scale[1])
    Curveto_r(2.0 * scale[0], 16.0 * scale[1], 2.0 * scale[0],
              40.0 * scale[1], 0.0 * scale[0], 55.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 16.0 * scale[1], -4.0 * scale[0],
              3.0 * scale[1], -4.0 * scale[0], -27.0 * scale[1])
    te.end_fill()
    Moveto(961.0 * scale[0], 48.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], -4.0 * scale[0], -
              25.0 * scale[1], -7.0 * scale[0], -35.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -14.0 * scale[1], -4.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -7.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 11.0 * scale[0],
              22.0 * scale[1], 8.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 13.0 * scale[1], -5.0 * scale[0],
              16.0 * scale[1], -6.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(0.0 * scale[0], 15.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              15.0 * scale[1], 10.0 * scale[0], -15.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              7.0 * scale[1], 4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 19.0 * scale[1], -14.0 * scale[0],
              19.0 * scale[1], -14.0 * scale[0], 0.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#729786')
    te.end_fill()
    Moveto(393.0 * scale[0], 1334.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -9.0 * scale[1], 3.0 * scale[0], -
              24.0 * scale[1], 18.0 * scale[0], -37.0 * scale[1])
    Curveto_r(12.0 * scale[0], -12.0 * scale[1], 18.0 *
              scale[0], -15.0 * scale[1], 11.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 9.0 * scale[1], -9.0 * scale[0],
              19.0 * scale[1], -5.0 * scale[0], 22.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], 1.0 * scale[0],
              7.0 * scale[1], -5.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0],
              5.0 * scale[1], -12.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 5.0 * scale[0],
              7.0 * scale[1], 12.0 * scale[0], 3.0 * scale[1])
    Curveto_r(7.0 * scale[0], -4.0 * scale[1], 8.0 *
              scale[0], -3.0 * scale[1], 4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 16.0 * scale[1], -15.0 * scale[0],
              15.0 * scale[1], -23.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(550.0 * scale[0], 1335.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -9.0 * scale[1], -10.0 * scale[0], -
              18.0 * scale[1], -6.0 * scale[0], -22.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 6.0 * scale[0],
              0.0 * scale[1], 6.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], 2.0 * scale[0],
              12.0 * scale[1], 9.0 * scale[0], 1.0 * scale[1])
    Curveto_r(6.0 * scale[0], -10.0 * scale[1], 10.0 *
              scale[0], -9.0 * scale[1], 14.0 * scale[0], 7.0 * scale[1])
    Curveto_r(6.0 * scale[0], 25.0 * scale[1], -5.0 * scale[0],
              27.0 * scale[1], -23.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(120.0 * scale[0], 1296.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 9.0 * scale[0], -
              6.0 * scale[1], 20.0 * scale[0], -9.0 * scale[1])
    Curveto_r(11.0 * scale[0], -3.0 * scale[1], 20.0 *
              scale[0], -1.0 * scale[1], 20.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -9.0 * scale[0],
              9.0 * scale[1], -20.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -20.0 *
              scale[0], -2.0 * scale[1], -20.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(853.0 * scale[0], 1293.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(90.0 * scale[0], 1275.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -9.0 * scale[1], -11.0 * scale[0], -
              17.0 * scale[1], -9.0 * scale[0], -20.0 * scale[1])
    Curveto_r(3.0 * scale[0], -2.0 * scale[1], 10.0 * scale[0],
              5.0 * scale[1], 17.0 * scale[0], 15.0 * scale[1])
    Curveto_r(14.0 * scale[0], 24.0 * scale[1], 10.0 * scale[0],
              26.0 * scale[1], -8.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(427.0 * scale[0], 1262.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-15.0 * scale[0], -9.0 * scale[1], -25.0 * scale[0], -
              22.0 * scale[1], -22.0 * scale[0], -29.0 * scale[1])
    Curveto_r(4.0 * scale[0], -11.0 * scale[1], -5.0 * scale[0], -
              16.0 * scale[1], -25.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -5.0 * scale[0], -
              15.0 * scale[1], -5.0 * scale[0], -33.0 * scale[1])
    Curveto_r(0.0 * scale[0], -39.0 * scale[1], 14.0 *
              scale[0], -36.0 * scale[1], 16.0 * scale[0], 3.0 * scale[1])
    Lineto_r(1.0 * scale[0], 27.0 * scale[1])
    Lineto_r(8.0 * scale[0], -30.0 * scale[1])
    Lineto_r(8.0 * scale[0], -30.0 * scale[1])
    Lineto_r(1.0 * scale[0], 31.0 * scale[1])
    Curveto_r(1.0 * scale[0], 18.0 * scale[1], 12.0 * scale[0],
              43.0 * scale[1], 27.0 * scale[0], 59.0 * scale[1])
    Curveto_r(31.0 * scale[0], 33.0 * scale[1], 28.0 * scale[0],
              39.0 * scale[1], -9.0 * scale[0], 17.0 * scale[1])
    te.end_fill()
    Moveto(488.0 * scale[0], 1262.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(15.0 * scale[0], -16.0 * scale[1], 18.0 *
              scale[0], -16.0 * scale[1], 24.0 * scale[0], -2.0 * scale[1])
    Curveto_r(4.0 * scale[0], 10.0 * scale[1], 7.0 * scale[0],
              11.0 * scale[1], 7.0 * scale[0], 2.0 * scale[1])
    Curveto_r(1.0 * scale[0], -7.0 * scale[1], 6.0 * scale[0], -
              10.0 * scale[1], 12.0 * scale[0], -6.0 * scale[1])
    Curveto_r(15.0 * scale[0], 9.0 * scale[1], -9.0 * scale[0],
              24.0 * scale[1], -38.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(840.0 * scale[0], 1203.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -43.0 * scale[1], 9.0 * scale[0], -
              58.0 * scale[1], 20.0 * scale[0], -58.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              13.0 * scale[1], 16.0 * scale[0], 50.0 * scale[1])
    Lineto_r(1.0 * scale[0], 50.0 * scale[1])
    Lineto_r(-4.0 * scale[0], -47.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -66.0 * scale[1], -23.0 *
              scale[0], -60.0 * scale[1], -23.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 30.0 * scale[1], -3.0 * scale[0],
              55.0 * scale[1], -8.0 * scale[0], 55.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -5.0 * scale[0], -
              26.0 * scale[1], -2.0 * scale[0], -57.0 * scale[1])
    te.end_fill()
    Moveto(111.0 * scale[0], 1203.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -28.0 * scale[1], 2.0 * scale[0], -
              54.0 * scale[1], 7.0 * scale[0], -57.0 * scale[1])
    Curveto_r(4.0 * scale[0], -2.0 * scale[1], 6.0 * scale[0],
              14.0 * scale[1], 4.0 * scale[0], 37.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 68.0 * scale[1], -10.0 * scale[0],
              76.0 * scale[1], -11.0 * scale[0], 20.0 * scale[1])
    te.end_fill()
    Moveto(547.0 * scale[0], 1238.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -7.0 * scale[1], 8.0 * scale[0], -
              17.0 * scale[1], 9.0 * scale[0], -23.0 * scale[1])
    Curveto_r(1.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              21.0 * scale[1], 12.0 * scale[0], -35.0 * scale[1])
    Curveto_r(10.0 * scale[0], -24.0 * scale[1], 11.0 *
              scale[0], -24.0 * scale[1], 11.0 * scale[0], -3.0 * scale[1])
    Curveto_r(1.0 * scale[0], 27.0 * scale[1], -19.0 * scale[0],
              73.0 * scale[1], -31.0 * scale[0], 73.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0], -
              6.0 * scale[1], -1.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(520.0 * scale[0], 1233.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 5.0 * scale[0], -
              15.0 * scale[1], 11.0 * scale[0], -18.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 8.0 * scale[0], -
              14.0 * scale[1], 5.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -1.0 *
              scale[0], -11.0 * scale[1], 4.0 * scale[0], -8.0 * scale[1])
    Curveto_r(14.0 * scale[0], 8.0 * scale[1], 13.0 * scale[0],
              18.0 * scale[1], -5.0 * scale[0], 41.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 10.0 * scale[1], -15.0 * scale[0],
              14.0 * scale[1], -15.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(143.0 * scale[0], 1185.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -22.0 * scale[1], 2.0 * scale[0], -
              30.0 * scale[1], 4.0 * scale[0], -17.0 * scale[1])
    Curveto_r(2.0 * scale[0], 12.0 * scale[1], 2.0 * scale[0],
              30.0 * scale[1], 0.0 * scale[0], 40.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -4.0 * scale[0], -23.0 * scale[1])
    te.end_fill()
    Moveto(892.0 * scale[0], 1170.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 2.0 * scale[0], -
              27.0 * scale[1], 5.0 * scale[0], -17.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              25.0 * scale[1], 0.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(405.0 * scale[0], 1140.0 * scale[1], x, y)
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
    Moveto(531.0 * scale[0], 1114.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(460.0 * scale[0], 1103.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 5.0 * scale[0], -
              13.0 * scale[1], 12.0 * scale[0], -11.0 * scale[1])
    Curveto_r(18.0 * scale[0], 6.0 * scale[1], 21.0 * scale[0],
              25.0 * scale[1], 3.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              7.0 * scale[1], -15.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(10.0 * scale[0], 1011.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 5.0 * scale[0], -
              12.0 * scale[1], 12.0 * scale[0], -19.0 * scale[1])
    Curveto_r(9.0 * scale[0], -9.0 * scale[1], 8.0 * scale[0], -
              12.0 * scale[1], -5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0], -
              4.0 * scale[1], -17.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -20.0 * scale[1], 27.0 *
              scale[0], -9.0 * scale[1], 39.0 * scale[0], 16.0 * scale[1])
    Curveto_r(13.0 * scale[0], 29.0 * scale[1], 36.0 * scale[0],
              27.0 * scale[1], 35.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 4.0 * scale[0], -
              20.0 * scale[1], 10.0 * scale[0], -19.0 * scale[1])
    Curveto_r(6.0 * scale[0], 1.0 * scale[1], 10.0 * scale[0], -
              4.0 * scale[1], 8.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -8.0 * scale[1], 2.0 * scale[0], -
              11.0 * scale[1], 9.0 * scale[0], -6.0 * scale[1])
    Curveto_r(9.0 * scale[0], 5.0 * scale[1], 10.0 * scale[0],
              2.0 * scale[1], 6.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -9.0 * scale[1], -1.0 * scale[0], -
              19.0 * scale[1], 4.0 * scale[0], -23.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], -3.0 * scale[0], -
              19.0 * scale[1], -23.0 * scale[0], -36.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -16.0 * scale[1], -26.0 *
              scale[0], -26.0 * scale[1], -18.0 * scale[0], -22.0 * scale[1])
    Curveto_r(34.0 * scale[0], 16.0 * scale[1], 57.0 * scale[0],
              45.0 * scale[1], 53.0 * scale[0], 67.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 14.0 * scale[1], 3.0 * scale[0],
              26.0 * scale[1], 16.0 * scale[0], 35.0 * scale[1])
    Curveto_r(18.0 * scale[0], 10.0 * scale[1], 21.0 * scale[0],
              10.0 * scale[1], 22.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 *
              scale[0], -15.0 * scale[1], 9.0 * scale[0], 2.0 * scale[1])
    Curveto_r(7.0 * scale[0], 17.0 * scale[1], 9.0 * scale[0],
              17.0 * scale[1], 9.0 * scale[0], 3.0 * scale[1])
    Curveto_r(1.0 * scale[0], -10.0 * scale[1], 12.0 * scale[0], -
              20.0 * scale[1], 25.0 * scale[0], -24.0 * scale[1])
    Curveto_r(15.0 * scale[0], -3.0 * scale[1], 26.0 * scale[0], -
              14.0 * scale[1], 28.0 * scale[0], -27.0 * scale[1])
    Curveto_r(2.0 * scale[0], -14.0 * scale[1], 9.0 * scale[0], -
              21.0 * scale[1], 18.0 * scale[0], -18.0 * scale[1])
    Curveto_r(8.0 * scale[0], 2.0 * scale[1], 31.0 * scale[0],
              8.0 * scale[1], 52.0 * scale[0], 13.0 * scale[1])
    Curveto_r(43.0 * scale[0], 12.0 * scale[1], 94.0 * scale[0], -
              8.0 * scale[1], 92.0 * scale[0], -35.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -9.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 8.0 * scale[0], -11.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 7.0 * scale[0],
              12.0 * scale[1], 4.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], -1.0 * scale[0],
              14.0 * scale[1], 5.0 * scale[0], 14.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0], -
              10.0 * scale[1], 19.0 * scale[0], -22.0 * scale[1])
    Curveto_r(8.0 * scale[0], -21.0 * scale[1], 9.0 * scale[0], -
              22.0 * scale[1], 10.0 * scale[0], -3.0 * scale[1])
    Curveto_r(1.0 * scale[0], 12.0 * scale[1], 5.0 * scale[0],
              6.0 * scale[1], 10.0 * scale[0], -15.0 * scale[1])
    Curveto_r(6.0 * scale[0], -23.0 * scale[1], 4.0 * scale[0], -
              37.0 * scale[1], -4.0 * scale[0], -45.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -5.0 * scale[1], -18.0 * scale[0], -
              19.0 * scale[1], -26.0 * scale[0], -30.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -21.0 * scale[1], -15.0 *
              scale[0], -21.0 * scale[1], 5.0 * scale[0], 0.0 * scale[1])
    Curveto_r(11.0 * scale[0], 11.0 * scale[1], 25.0 * scale[0],
              21.0 * scale[1], 30.0 * scale[0], 23.0 * scale[1])
    Curveto_r(6.0 * scale[0], 1.0 * scale[1], 9.0 * scale[0],
              28.0 * scale[1], 8.0 * scale[0], 60.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 31.0 * scale[1], -3.0 * scale[0],
              81.0 * scale[1], -3.0 * scale[0], 110.0 * scale[1])
    Curveto_r(0.0 * scale[0], 28.0 * scale[1], -2.0 * scale[0],
              52.0 * scale[1], -4.0 * scale[0], 52.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0], -
              5.0 * scale[1], -32.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -7.0 * scale[1], -30.0 *
              scale[0], -7.0 * scale[1], -40.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 13.0 * scale[1], -95.0 * scale[0],
              4.0 * scale[1], -105.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], -19.0 *
              scale[0], -5.0 * scale[1], -43.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-37.0 * scale[0], 16.0 * scale[1], -226.0 * scale[0],
              22.0 * scale[1], -226.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(240.0 * scale[0], 1016.0 * scale[1], x, y)
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
    Moveto(471.0 * scale[0], 984.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(917.0 * scale[0], 979.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(7.0 * scale[0], 943.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -12.0 * scale[1], -7.0 *
              scale[0], -61.0 * scale[1], 6.0 * scale[0], -66.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 14.0 * scale[0],
              1.0 * scale[1], 14.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -5.0 * scale[0],
              14.0 * scale[1], -10.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0],
              11.0 * scale[1], -5.0 * scale[0], 25.0 * scale[1])
    Curveto_r(6.0 * scale[0], 27.0 * scale[1], 5.0 * scale[0],
              29.0 * scale[1], -5.0 * scale[0], 18.0 * scale[1])
    te.end_fill()
    Moveto(506.0 * scale[0], 932.0 * scale[1], x, y)
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
    Moveto(532.0 * scale[0], 905.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -4.0 * scale[1], 0.0 * scale[0], -
              13.0 * scale[1], -9.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -9.0 * scale[1], -13.0 *
              scale[0], -14.0 * scale[1], -3.0 * scale[0], -20.0 * scale[1])
    Curveto_r(9.0 * scale[0], -5.0 * scale[1], 11.0 *
              scale[0], -4.0 * scale[1], 6.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 7.0 * scale[1], -1.0 * scale[0],
              12.0 * scale[1], 8.0 * scale[0], 12.0 * scale[1])
    Curveto_r(19.0 * scale[0], 0.0 * scale[1], 21.0 * scale[0],
              16.0 * scale[1], 4.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -10.0 * scale[0],
              4.0 * scale[1], -6.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(41.0 * scale[0], 864.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(75.0 * scale[0], 820.0 * scale[1], x, y)
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
    Moveto(128.0 * scale[0], 813.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(220.0 * scale[0], 786.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(435.0 * scale[0], 760.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -1.0 *
              scale[0], -9.0 * scale[1], 7.0 * scale[0], -8.0 * scale[1])
    Curveto_r(10.0 * scale[0], 2.0 * scale[1], 13.0 * scale[0], -
              24.0 * scale[1], 13.0 * scale[0], -127.0 * scale[1])
    Curveto_r(0.0 * scale[0], -123.0 * scale[1], -1.0 * scale[0], -
              130.0 * scale[1], -20.0 * scale[0], -130.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 0.0 * scale[1], -23.0 *
              scale[0], -8.0 * scale[1], -2.0 * scale[0], -48.0 * scale[1])
    Curveto_r(13.0 * scale[0], -24.0 * scale[1], 15.0 * scale[0], -
              26.0 * scale[1], 22.0 * scale[0], -10.0 * scale[1])
    Curveto_r(10.0 * scale[0], 24.0 * scale[1], 19.0 * scale[0],
              275.0 * scale[1], 11.0 * scale[0], 307.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 27.0 * scale[1], -20.0 * scale[0],
              34.0 * scale[1], -31.0 * scale[0], 16.0 * scale[1])
    te.end_fill()
    Moveto(292.0 * scale[0], 725.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(587.0 * scale[0], 702.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -10.0 * scale[1], 11.0 * scale[0], -
              19.0 * scale[1], 19.0 * scale[0], -19.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              4.0 * scale[1], -3.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 10.0 * scale[1], -17.0 * scale[0],
              18.0 * scale[1], -19.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 0.0 * scale[1], 0.0 * scale[0], -
              8.0 * scale[1], 3.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(655.0 * scale[0], 710.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 11.0 * scale[0], -
              8.0 * scale[1], 16.0 * scale[0], -5.0 * scale[1])
    Curveto_r(14.0 * scale[0], 9.0 * scale[1], 11.0 * scale[0],
              15.0 * scale[1], -7.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              5.0 * scale[1], -9.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(493.0 * scale[0], 660.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -30.0 * scale[1], 2.0 * scale[0], -
              43.0 * scale[1], 4.0 * scale[0], -27.0 * scale[1])
    Curveto_r(2.0 * scale[0], 15.0 * scale[1], 2.0 * scale[0],
              39.0 * scale[1], 0.0 * scale[0], 55.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 15.0 * scale[1], -4.0 * scale[0],
              2.0 * scale[1], -4.0 * scale[0], -28.0 * scale[1])
    te.end_fill()
    Moveto(685.0 * scale[0], 700.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -15.0 * scale[0], -
              10.0 * scale[1], -26.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -4.0 * scale[1], -19.0 * scale[0], -9.0 * scale[1])
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], 37.0 *
              scale[0], -2.0 * scale[1], 51.0 * scale[0], 15.0 * scale[1])
    Curveto_r(6.0 * scale[0], 8.0 * scale[1], 9.0 * scale[0],
              14.0 * scale[1], 6.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              4.0 * scale[1], -12.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(351.0 * scale[0], 644.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(380.0 * scale[0], 621.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              12.0 * scale[1], 8.0 * scale[0], -15.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 9.0 * scale[0],
              1.0 * scale[1], 9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -4.0 * scale[0],
              15.0 * scale[1], -9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              4.0 * scale[1], -8.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(426.0 * scale[0], 575.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -26.0 * scale[1], -7.0 *
              scale[0], -32.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(6.0 * scale[0], 10.0 * scale[1], 9.0 * scale[0],
              21.0 * scale[1], 6.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 3.0 * scale[1], -7.0 * scale[0], -
              2.0 * scale[1], -11.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(413.0 * scale[0], 523.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -13.0 * scale[0], -
              9.0 * scale[1], -13.0 * scale[0], -15.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], 4.0 * scale[0], -
              7.0 * scale[1], 13.0 * scale[0], 1.0 * scale[1])
    Curveto_r(10.0 * scale[0], 8.0 * scale[1], 17.0 * scale[0],
              7.0 * scale[1], 26.0 * scale[0], -2.0 * scale[1])
    Curveto_r(11.0 * scale[0], -9.0 * scale[1], 13.0 *
              scale[0], -9.0 * scale[1], 9.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 17.0 * scale[1], -17.0 * scale[0],
              22.0 * scale[1], -35.0 * scale[0], 14.0 * scale[1])
    te.end_fill()
    Moveto(473.0 * scale[0], 420.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -30.0 * scale[1], 2.0 * scale[0], -
              43.0 * scale[1], 4.0 * scale[0], -27.0 * scale[1])
    Curveto_r(2.0 * scale[0], 15.0 * scale[1], 2.0 * scale[0],
              39.0 * scale[1], 0.0 * scale[0], 55.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 15.0 * scale[1], -4.0 * scale[0],
              2.0 * scale[1], -4.0 * scale[0], -28.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#98642a')
    te.end_fill()
    Moveto(360.0 * scale[0], 1388.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 17.0 * scale[0], -
              11.0 * scale[1], 60.0 * scale[0], -10.0 * scale[1])
    Curveto_r(52.0 * scale[0], 0.0 * scale[1], 63.0 * scale[0],
              2.0 * scale[1], 57.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -117.0 * scale[0],
              10.0 * scale[1], -117.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(160.0 * scale[0], 1382.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-29.0 * scale[0], -4.0 * scale[1], -32.0 *
              scale[0], -6.0 * scale[1], -15.0 * scale[0], -12.0 * scale[1])
    Curveto_r(19.0 * scale[0], -8.0 * scale[1], 19.0 *
              scale[0], -9.0 * scale[1], -2.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-34.0 * scale[0], -1.0 * scale[1], -28.0 *
              scale[0], -28.0 * scale[1], 8.0 * scale[0], -35.0 * scale[1])
    Curveto_r(42.0 * scale[0], -8.0 * scale[1], 51.0 *
              scale[0], -8.0 * scale[1], 45.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], 16.0 * scale[0],
              11.0 * scale[1], 42.0 * scale[0], 15.0 * scale[1])
    Curveto_r(27.0 * scale[0], 3.0 * scale[1], 54.0 * scale[0],
              14.0 * scale[1], 63.0 * scale[0], 24.0 * scale[1])
    Curveto_r(14.0 * scale[0], 17.0 * scale[1], 12.0 * scale[0],
              18.0 * scale[1], -45.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-34.0 * scale[0], 0.0 * scale[1], -77.0 *
              scale[0], -2.0 * scale[1], -96.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto_r(113.0 * scale[0], -19.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -21.0 *
              scale[0], -2.0 * scale[1], -30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 3.0 * scale[1], -4.0 * scale[0],
              5.0 * scale[1], 12.0 * scale[0], 5.0 * scale[1])
    Curveto_r(17.0 * scale[0], 0.0 * scale[1], 24.0 * scale[0], -
              2.0 * scale[1], 18.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(578.0 * scale[0], 1383.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(607.0 * scale[0], 1370.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -12.0 * scale[1], -17.0 *
              scale[0], -28.0 * scale[1], -14.0 * scale[0], -47.0 * scale[1])
    Curveto_r(4.0 * scale[0], -27.0 * scale[1], 4.0 *
              scale[0], -27.0 * scale[1], 6.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], 6.0 * scale[0],
              32.0 * scale[1], 11.0 * scale[0], 32.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              5.0 * scale[1], 10.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0], -
              7.0 * scale[1], 11.0 * scale[0], -3.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 8.0 * scale[0],
              9.0 * scale[1], -1.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 11.0 * scale[1], 6.0 * scale[0],
              23.0 * scale[1], 33.0 * scale[0], 16.0 * scale[1])
    Curveto_r(12.0 * scale[0], -3.0 * scale[1], 29.0 *
              scale[0], -1.0 * scale[1], 37.0 * scale[0], 4.0 * scale[1])
    Curveto_r(11.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              10.0 * scale[1], -30.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 0.0 * scale[1], -51.0 * scale[0], -
              6.0 * scale[1], -63.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(726.0 * scale[0], 1371.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], 0.0 *
              scale[0], -8.0 * scale[1], 7.0 * scale[0], -9.0 * scale[1])
    Curveto_r(64.0 * scale[0], -6.0 * scale[1], 86.0 * scale[0], -
              26.0 * scale[1], 25.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 1.0 * scale[1], -28.0 *
              scale[0], -3.0 * scale[1], -28.0 * scale[0], -9.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 5.0 * scale[0], -
              12.0 * scale[1], 37.0 * scale[0], -15.0 * scale[1])
    Curveto_r(7.0 * scale[0], -1.0 * scale[1], 12.0 * scale[0], -
              6.0 * scale[1], 10.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -6.0 * scale[1], -24.0 * scale[0], -
              10.0 * scale[1], -52.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-27.0 * scale[0], 1.0 * scale[1], -35.0 *
              scale[0], -1.0 * scale[1], -17.0 * scale[0], -3.0 * scale[1])
    Curveto_r(46.0 * scale[0], -6.0 * scale[1], 40.0 * scale[0], -
              23.0 * scale[1], -10.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-55.0 * scale[0], 0.0 * scale[1], -46.0 *
              scale[0], -6.0 * scale[1], 20.0 * scale[0], -13.0 * scale[1])
    Curveto_r(48.0 * scale[0], -5.0 * scale[1], 68.0 * scale[0],
              4.0 * scale[1], 40.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -3.0 * scale[0],
              4.0 * scale[1], 10.0 * scale[0], 2.0 * scale[1])
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 20.0 * scale[0],
              0.0 * scale[1], 17.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], 0.0 * scale[0],
              12.0 * scale[1], 7.0 * scale[0], 17.0 * scale[1])
    Curveto_r(7.0 * scale[0], 4.0 * scale[1], 19.0 * scale[0],
              18.0 * scale[1], 26.0 * scale[0], 31.0 * scale[1])
    Curveto_r(14.0 * scale[0], 25.0 * scale[1], 16.0 * scale[0],
              23.0 * scale[1], -50.0 * scale[0], 41.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 5.0 * scale[1], -40.0 * scale[0],
              6.0 * scale[1], -42.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(347.0 * scale[0], 1362.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], 3.0 * scale[0], -
              18.0 * scale[1], 14.0 * scale[0], -31.0 * scale[1])
    Curveto_r(10.0 * scale[0], -13.0 * scale[1], 19.0 * scale[0], -
              19.0 * scale[1], 19.0 * scale[0], -13.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -7.0 * scale[0],
              15.0 * scale[1], -15.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 7.0 * scale[1], -12.0 * scale[0],
              16.0 * scale[1], -9.0 * scale[0], 21.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], 3.0 * scale[0],
              9.0 * scale[1], 0.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              3.0 * scale[1], -9.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(834.0 * scale[0], 1363.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(10.0 * scale[0], -10.0 * scale[1], 76.0 *
              scale[0], -12.0 * scale[1], 70.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -21.0 * scale[0],
              8.0 * scale[1], -41.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 0.0 * scale[1], -33.0 *
              scale[0], -3.0 * scale[1], -29.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(30.0 * scale[0], 1342.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -17.0 * scale[1], -5.0 *
              scale[0], -28.0 * scale[1], 14.0 * scale[0], -13.0 * scale[1])
    Curveto_r(11.0 * scale[0], 9.0 * scale[1], 15.0 * scale[0],
              9.0 * scale[1], 18.0 * scale[0], 0.0 * scale[1])
    Curveto_r(5.0 * scale[0], -15.0 * scale[1], 48.0 *
              scale[0], -2.0 * scale[1], 48.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], -64.0 * scale[0],
              15.0 * scale[1], -80.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(645.0 * scale[0], 1340.0 * scale[1], x, y)
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
    Moveto(461.0 * scale[0], 1323.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -14.0 * scale[1], 5.0 * scale[0], -
              23.0 * scale[1], 13.0 * scale[0], -23.0 * scale[1])
    Curveto_r(17.0 * scale[0], 0.0 * scale[1], 38.0 * scale[0],
              24.0 * scale[1], 29.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 12.0 * scale[1], -22.0 * scale[0],
              7.0 * scale[1], -17.0 * scale[0], -8.0 * scale[1])
    Curveto_r(4.0 * scale[0], -8.0 * scale[1], 1.0 * scale[0], -
              15.0 * scale[1], -4.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0],
              8.0 * scale[1], -15.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 13.0 * scale[1], -5.0 * scale[0],
              11.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(690.0 * scale[0], 1330.0 * scale[1], x, y)
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
    Moveto(202.0 * scale[0], 1318.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-18.0 * scale[0], -18.0 * scale[1], -15.0 *
              scale[0], -27.0 * scale[1], 11.0 * scale[0], -38.0 * scale[1])
    Curveto_r(21.0 * scale[0], -8.0 * scale[1], 21.0 *
              scale[0], -9.0 * scale[1], -5.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-24.0 * scale[0], -1.0 * scale[1], -28.0 *
              scale[0], -5.0 * scale[1], -28.0 * scale[0], -31.0 * scale[1])
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 5.0 * scale[0], -
              30.0 * scale[1], 10.0 * scale[0], -30.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0],
              14.0 * scale[1], 10.0 * scale[0], 39.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 9.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], 14.0 * scale[0], 8.0 * scale[1])
    Curveto_r(9.0 * scale[0], -4.0 * scale[1], 27.0 *
              scale[0], -1.0 * scale[1], 41.0 * scale[0], 5.0 * scale[1])
    Curveto_r(19.0 * scale[0], 8.0 * scale[1], 28.0 * scale[0],
              8.0 * scale[1], 41.0 * scale[0], -3.0 * scale[1])
    Curveto_r(13.0 * scale[0], -11.0 * scale[1], 18.0 *
              scale[0], -11.0 * scale[1], 21.0 * scale[0], -1.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 11.0 * scale[0],
              12.0 * scale[1], 19.0 * scale[0], 12.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0], -
              4.0 * scale[1], 9.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 3.0 * scale[0], -
              9.0 * scale[1], 13.0 * scale[0], -8.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0],
              9.0 * scale[1], 20.0 * scale[0], 21.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], -2.0 * scale[0],
              16.0 * scale[1], -6.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -7.0 * scale[1], -31.0 *
              scale[0], -6.0 * scale[1], -77.0 * scale[0], 2.0 * scale[1])
    Lineto_r(-70.0 * scale[0], 12.0 * scale[1])
    Lineto_r(68.0 * scale[0], -4.0 * scale[1])
    Curveto_r(46.0 * scale[0], -3.0 * scale[1], 67.0 *
              scale[0], -1.0 * scale[1], 65.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 6.0 * scale[1], -28.0 * scale[0],
              12.0 * scale[1], -58.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 2.0 * scale[1], -62.0 * scale[0],
              6.0 * scale[1], -70.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 3.0 * scale[1], -21.0 * scale[0],
              1.0 * scale[1], -28.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(35.0 * scale[0], 1290.0 * scale[1], x, y)
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
    Moveto(575.0 * scale[0], 1270.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(213.0 * scale[0], 1235.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              15.0 * scale[1], 9.0 * scale[0], -15.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0],
              4.0 * scale[1], 8.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -4.0 * scale[0],
              12.0 * scale[1], -8.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              1.0 * scale[1], -9.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(587.0 * scale[0], 1243.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 11.0 * scale[0], -
              15.0 * scale[1], 8.0 * scale[0], -31.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -26.0 * scale[1], -5.0 *
              scale[0], -26.0 * scale[1], 5.0 * scale[0], -4.0 * scale[1])
    Curveto_r(11.0 * scale[0], 26.0 * scale[1], 6.0 * scale[0],
              42.0 * scale[1], -13.0 * scale[0], 41.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -9.0 *
              scale[0], -2.0 * scale[1], 0.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(782.0 * scale[0], 1241.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-17.0 * scale[0], -10.0 * scale[1], -14.0 *
              scale[0], -22.0 * scale[1], 7.0 * scale[0], -38.0 * scale[1])
    Curveto_r(28.0 * scale[0], -20.0 * scale[1], 6.0 * scale[0], -
              23.0 * scale[1], -24.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 11.0 * scale[1], -24.0 * scale[0],
              20.0 * scale[1], -17.0 * scale[0], 20.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              5.0 * scale[1], 7.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 7.0 * scale[1], -13.0 * scale[0],
              6.0 * scale[1], -27.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -11.0 * scale[1], -21.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], -25.0 * scale[1])
    Curveto_r(34.0 * scale[0], -19.0 * scale[1], 22.0 *
              scale[0], -17.0 * scale[1], -39.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-73.0 * scale[0], 28.0 * scale[1], -88.0 * scale[0],
              25.0 * scale[1], -24.0 * scale[0], -5.0 * scale[1])
    Curveto_r(62.0 * scale[0], -29.0 * scale[1], 124.0 * scale[0], -
              74.0 * scale[1], 117.0 * scale[0], -85.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -8.0 * scale[1], -89.0 * scale[0], -
              18.0 * scale[1], -192.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-93.0 * scale[0], -4.0 * scale[1], -44.0 *
              scale[0], -17.0 * scale[1], 70.0 * scale[0], -18.0 * scale[1])
    Curveto_r(101.0 * scale[0], -1.0 * scale[1], 106.0 *
              scale[0], -2.0 * scale[1], 57.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-30.0 * scale[0], -5.0 * scale[1], -86.0 * scale[0], -
              11.0 * scale[1], -123.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-58.0 * scale[0], -4.0 * scale[1], -68.0 *
              scale[0], -2.0 * scale[1], -63.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], 4.0 * scale[0],
              15.0 * scale[1], 3.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0], -
              4.0 * scale[1], -35.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-23.0 * scale[0], -7.0 * scale[1], -32.0 *
              scale[0], -6.0 * scale[1], -32.0 * scale[0], 2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -3.0 * scale[0],
              7.0 * scale[1], -9.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -8.0 * scale[1], -11.0 *
              scale[0], -9.0 * scale[1], -15.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 14.0 * scale[1], -43.0 * scale[0],
              3.0 * scale[1], -43.0 * scale[0], -14.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              14.0 * scale[1], 9.0 * scale[0], -14.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0],
              5.0 * scale[1], 8.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 5.0 * scale[0],
              10.0 * scale[1], 11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0], -
              4.0 * scale[1], 5.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -9.0 * scale[1], 37.0 *
              scale[0], -7.0 * scale[1], 53.0 * scale[0], 3.0 * scale[1])
    Curveto_r(5.0 * scale[0], 4.0 * scale[1], 12.0 * scale[0],
              2.0 * scale[1], 15.0 * scale[0], -3.0 * scale[1])
    Curveto_r(4.0 * scale[0], -5.0 * scale[1], 73.0 * scale[0], -
              9.0 * scale[1], 157.0 * scale[0], -9.0 * scale[1])
    Curveto_r(125.0 * scale[0], 0.0 * scale[1], 147.0 * scale[0],
              2.0 * scale[1], 133.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 11.0 * scale[1], -11.0 * scale[0],
              12.0 * scale[1], 29.0 * scale[0], 9.0 * scale[1])
    Curveto_r(26.0 * scale[0], -2.0 * scale[1], 47.0 * scale[0],
              1.0 * scale[1], 47.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              10.0 * scale[1], -11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0],
              4.0 * scale[1], -5.0 * scale[0], 9.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], -4.0 * scale[0],
              11.0 * scale[1], -15.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 4.0 * scale[1], -20.0 * scale[0],
              11.0 * scale[1], -16.0 * scale[0], 27.0 * scale[1])
    Curveto_r(5.0 * scale[0], 18.0 * scale[1], 3.0 * scale[0],
              19.0 * scale[1], -10.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -11.0 * scale[1], -15.0 *
              scale[0], -10.0 * scale[1], -7.0 * scale[0], 7.0 * scale[1])
    Curveto_r(13.0 * scale[0], 27.0 * scale[1], 11.0 * scale[0],
              49.0 * scale[1], -5.0 * scale[0], 68.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 9.0 * scale[1], -10.0 * scale[0],
              21.0 * scale[1], -6.0 * scale[0], 27.0 * scale[1])
    Curveto_r(7.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], -13.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(248.0 * scale[0], 1223.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(210.0 * scale[0], 1194.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -5.0 * scale[0], -
              14.0 * scale[1], -11.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0],
              5.0 * scale[1], -4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 1.0 * scale[0],
              10.0 * scale[1], -4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0], -
              17.0 * scale[1], -1.0 * scale[0], -25.0 * scale[1])
    Curveto_r(8.0 * scale[0], -5.0 * scale[1], 70.0 * scale[0],
              20.0 * scale[1], 70.0 * scale[0], 29.0 * scale[1])
    Curveto_r(0.0 * scale[0], 2.0 * scale[1], -11.0 * scale[0],
              4.0 * scale[1], -25.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 0.0 * scale[1], -25.0 * scale[0], -
              6.0 * scale[1], -25.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(310.0 * scale[0], 1185.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 9.0 * scale[0], -
              9.0 * scale[1], 19.0 * scale[0], -14.0 * scale[1])
    Curveto_r(14.0 * scale[0], -8.0 * scale[1], 20.0 *
              scale[0], -7.0 * scale[1], 24.0 * scale[0], 2.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], -4.0 * scale[0],
              14.0 * scale[1], -19.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 1.0 * scale[1], -24.0 * scale[0],
              0.0 * scale[1], -24.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(225.0 * scale[0], 1170.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -13.0 * scale[1], 5.0 *
              scale[0], -13.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(13.0 * scale[0], 8.0 * scale[1], 13.0 * scale[0],
              10.0 * scale[1], -2.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0], -
              4.0 * scale[1], -23.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(190.0 * scale[0], 1146.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(15.0 * scale[0], -15.0 * scale[1], 13.0 * scale[0], -
              59.0 * scale[1], -2.0 * scale[0], -50.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 9.0 * scale[1], -58.0 * scale[0],
              12.0 * scale[1], -58.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 62.0 * scale[0], -
              30.0 * scale[1], 73.0 * scale[0], -23.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 2.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -10.0 * scale[1], -2.0 *
              scale[0], -12.0 * scale[1], 18.0 * scale[0], -8.0 * scale[1])
    Curveto_r(18.0 * scale[0], 4.0 * scale[1], 24.0 * scale[0],
              1.0 * scale[1], 20.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -22.0 * scale[1], 96.0 *
              scale[0], -18.0 * scale[1], 113.0 * scale[0], 5.0 * scale[1])
    Curveto_r(11.0 * scale[0], 15.0 * scale[1], 8.0 * scale[0],
              18.0 * scale[1], -29.0 * scale[0], 29.0 * scale[1])
    Lineto_r(-42.0 * scale[0], 12.0 * scale[1])
    Lineto_r(42.0 * scale[0], -3.0 * scale[1])
    Curveto_r(23.0 * scale[0], -2.0 * scale[1], 47.0 * scale[0],
              1.0 * scale[1], 55.0 * scale[0], 5.0 * scale[1])
    Curveto_r(10.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              9.0 * scale[1], -2.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -24.0 * scale[0],
              2.0 * scale[1], -35.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-48.0 * scale[0], 8.0 * scale[1], -99.0 * scale[0],
              14.0 * scale[1], -87.0 * scale[0], 9.0 * scale[1])
    Curveto_r(17.0 * scale[0], -8.0 * scale[1], 15.0 * scale[0], -
              25.0 * scale[1], -3.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 8.0 * scale[1], -20.0 * scale[0],
              34.0 * scale[1], -1.0 * scale[0], 34.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0],
              4.0 * scale[1], 20.0 * scale[0], 8.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], -17.0 * scale[0],
              8.0 * scale[1], -45.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-33.0 * scale[0], 0.0 * scale[1], -46.0 * scale[0], -
              3.0 * scale[1], -39.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto_r(50.0 * scale[0], -56.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -5.0 * scale[0], -
              10.0 * scale[1], -11.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0],
              5.0 * scale[1], -4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 8.0 * scale[0],
              10.0 * scale[1], 11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 4.0 * scale[0], -
              4.0 * scale[1], 4.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto_r(50.0 * scale[0], -20.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(8.0 * scale[0], -5.0 * scale[1], 11.0 * scale[0], -
              10.0 * scale[1], 5.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0],
              5.0 * scale[1], -25.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -10.0 * scale[0],
              10.0 * scale[1], -5.0 * scale[0], 10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0], -
              5.0 * scale[1], 25.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto_r(45.0 * scale[0], -10.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -11.0 * scale[0], -
              10.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0],
              5.0 * scale[1], -4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 11.0 * scale[0],
              10.0 * scale[1], 16.0 * scale[0], 10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0], -
              4.0 * scale[1], 4.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(330.0 * scale[0], 1144.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-35.0 * scale[0], -13.0 * scale[1])
    Lineto_r(33.0 * scale[0], 4.0 * scale[1])
    Curveto_r(33.0 * scale[0], 3.0 * scale[1], 50.0 * scale[0],
              11.0 * scale[1], 41.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 2.0 * scale[1], -20.0 * scale[0], -
              3.0 * scale[1], -39.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(575.0 * scale[0], 1129.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -17.0 * scale[1], 1.0 *
              scale[0], -21.0 * scale[1], 15.0 * scale[0], -4.0 * scale[1])
    Curveto_r(8.0 * scale[0], 9.0 * scale[1], 8.0 * scale[0],
              15.0 * scale[1], 2.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0], -
              5.0 * scale[1], -17.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(45.0 * scale[0], 1120.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(43.0 * scale[0], -15.0 * scale[1], 69.0 * scale[0], -
              20.0 * scale[1], 61.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 8.0 * scale[1], -16.0 * scale[0],
              10.0 * scale[1], -61.0 * scale[0], 18.0 * scale[1])
    Lineto_r(-30.0 * scale[0], 5.0 * scale[1])
    Lineto_r(30.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(878.0 * scale[0], 1093.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(84.0 * scale[0], 1069.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], -3.0 *
              scale[0], -9.0 * scale[1], 3.0 * scale[0], -6.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 33.0 * scale[0],
              0.0 * scale[1], 59.0 * scale[0], -8.0 * scale[1])
    Curveto_r(57.0 * scale[0], -17.0 * scale[1], 67.0 *
              scale[0], -18.0 * scale[1], 60.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], -23.0 * scale[0],
              12.0 * scale[1], -43.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 4.0 * scale[1], -45.0 * scale[0],
              9.0 * scale[1], -55.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 3.0 * scale[1], -20.0 * scale[0], -
              1.0 * scale[1], -24.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(788.0 * scale[0], 996.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -7.0 * scale[1], -18.0 * scale[0], -
              19.0 * scale[1], -18.0 * scale[0], -25.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 5.0 * scale[0], -
              7.0 * scale[1], 16.0 * scale[0], 3.0 * scale[1])
    Curveto_r(18.0 * scale[0], 18.0 * scale[1], 33.0 * scale[0],
              21.0 * scale[1], 35.0 * scale[0], 6.0 * scale[1])
    Curveto_r(1.0 * scale[0], -5.0 * scale[1], 2.0 * scale[0], -
              15.0 * scale[1], 3.0 * scale[0], -22.0 * scale[1])
    Curveto_r(1.0 * scale[0], -14.0 * scale[1], 26.0 * scale[0], -
              23.0 * scale[1], 26.0 * scale[0], -9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -4.0 * scale[0],
              13.0 * scale[1], -10.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0],
              15.0 * scale[1], -10.0 * scale[0], 26.0 * scale[1])
    Curveto_r(0.0 * scale[0], 22.0 * scale[1], -17.0 * scale[0],
              24.0 * scale[1], -42.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(767.0 * scale[0], 935.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], 9.0 * scale[0], -
              12.0 * scale[1], 14.0 * scale[0], -9.0 * scale[1])
    Curveto_r(12.0 * scale[0], 7.0 * scale[1], 11.0 * scale[0],
              11.0 * scale[1], -5.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 4.0 * scale[1], -13.0 * scale[0],
              1.0 * scale[1], -9.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(906.0 * scale[0], 889.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(17.0 * scale[0], -19.0 * scale[1], 52.0 * scale[0], -
              31.0 * scale[1], 58.0 * scale[0], -20.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], -4.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 8.0 * scale[1], -19.0 * scale[0],
              9.0 * scale[1], -19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -5.0 * scale[0], -
              7.0 * scale[1], -10.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -8.0 * scale[0],
              10.0 * scale[1], -6.0 * scale[0], 14.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], -1.0 * scale[0],
              8.0 * scale[1], -9.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -13.0 *
              scale[0], -3.0 * scale[1], 1.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(817.0 * scale[0], 886.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -13.0 * scale[1], -16.0 *
              scale[0], -14.0 * scale[1], 3.0 * scale[0], -19.0 * scale[1])
    Curveto_r(22.0 * scale[0], -6.0 * scale[1], 38.0 * scale[0],
              10.0 * scale[1], 24.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 5.0 * scale[1], -17.0 * scale[0],
              3.0 * scale[1], -27.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(702.0 * scale[0], 820.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(14.0 * scale[0], -21.0 * scale[1], 38.0 *
              scale[0], -27.0 * scale[1], 38.0 * scale[0], -9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -5.0 * scale[0],
              7.0 * scale[1], -10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -3.0 * scale[1], -13.0 * scale[0],
              1.0 * scale[1], -16.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -10.0 * scale[0],
              16.0 * scale[1], -15.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              9.0 * scale[1], 3.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(750.0 * scale[0], 781.0 * scale[1], x, y)
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
    Moveto(785.0 * scale[0], 770.0 * scale[1], x, y)
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
    Moveto(909.0 * scale[0], 757.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -5.0 * scale[1], 19.0 * scale[0], -
              7.0 * scale[1], 32.0 * scale[0], -5.0 * scale[1])
    Curveto_r(20.0 * scale[0], 3.0 * scale[1], 19.0 * scale[0],
              5.0 * scale[1], -9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 3.0 * scale[1], -29.0 * scale[0],
              2.0 * scale[1], -23.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(129.0 * scale[0], 743.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -15.0 * scale[1], -12.0 *
              scale[0], -15.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(12.0 * scale[0], 6.0 * scale[1], 28.0 * scale[0],
              9.0 * scale[1], 34.0 * scale[0], 5.0 * scale[1])
    Curveto_r(7.0 * scale[0], -4.0 * scale[1], 8.0 *
              scale[0], -3.0 * scale[1], 4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 17.0 * scale[1], -31.0 * scale[0],
              15.0 * scale[1], -47.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(836.0 * scale[0], 740.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -14.0 * scale[1], 19.0 * scale[0], -
              31.0 * scale[1], 17.0 * scale[0], -37.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -7.0 * scale[1], 2.0 * scale[0], -
              13.0 * scale[1], 11.0 * scale[0], -13.0 * scale[1])
    Curveto_r(27.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              29.0 * scale[1], -29.0 * scale[0], 60.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 13.0 * scale[1], -18.0 * scale[0],
              12.0 * scale[1], 1.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(935.0 * scale[0], 670.0 * scale[1], x, y)
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
    Moveto(87.0 * scale[0], 650.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -13.0 * scale[1], -1.0 *
              scale[0], -18.0 * scale[1], 6.0 * scale[0], -13.0 * scale[1])
    Curveto_r(7.0 * scale[0], 4.0 * scale[1], 8.0 * scale[0],
              0.0 * scale[1], 3.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -10.0 * scale[1], -4.0 *
              scale[0], -15.0 * scale[1], 0.0 * scale[0], -11.0 * scale[1])
    Curveto_r(4.0 * scale[0], 4.0 * scale[1], 13.0 * scale[0],
              2.0 * scale[1], 20.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], -8.0 * scale[1], 8.0 * scale[0],
              0.0 * scale[1], -3.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 19.0 * scale[1], -17.0 * scale[0],
              35.0 * scale[1], -18.0 * scale[0], 37.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 1.0 * scale[1], -5.0 * scale[0], -
              6.0 * scale[1], -8.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(41.0 * scale[0], 650.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -24.0 * scale[1], 15.0 * scale[0], -
              55.0 * scale[1], 21.0 * scale[0], -44.0 * scale[1])
    Curveto_r(2.0 * scale[0], 5.0 * scale[1], -1.0 * scale[0],
              20.0 * scale[1], -8.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 14.0 * scale[1], -13.0 * scale[0],
              18.0 * scale[1], -13.0 * scale[0], 10.0 * scale[1])
    te.end_fill()
    Moveto(160.0 * scale[0], 660.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -20.0 * scale[1], -7.0 *
              scale[0], -40.0 * scale[1], 1.0 * scale[0], -40.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0], -
              5.0 * scale[1], 3.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], -3.0 *
              scale[0], -8.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(7.0 * scale[0], 4.0 * scale[1], 12.0 * scale[0],
              3.0 * scale[1], 12.0 * scale[0], -3.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -5.0 * scale[0], -
              13.0 * scale[1], -10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -4.0 * scale[1], -9.0 * scale[0], -
              20.0 * scale[1], -8.0 * scale[0], -36.0 * scale[1])
    Curveto_r(3.0 * scale[0], -33.0 * scale[1], 26.0 * scale[0], -
              39.0 * scale[1], 52.0 * scale[0], -13.0 * scale[1])
    Curveto_r(19.0 * scale[0], 19.0 * scale[1], 21.0 * scale[0],
              28.0 * scale[1], 4.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-37.0 * scale[0], -22.0 * scale[1], -57.0 *
              scale[0], -4.0 * scale[1], -37.0 * scale[0], 34.0 * scale[1])
    Curveto_r(9.0 * scale[0], 17.0 * scale[1], 10.0 * scale[0],
              26.0 * scale[1], 2.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -13.0 * scale[0],
              16.0 * scale[1], -16.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 11.0 * scale[1], -6.0 * scale[0],
              18.0 * scale[1], -7.0 * scale[0], 15.0 * scale[1])
    te.end_fill()
    Moveto(130.0 * scale[0], 571.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -4.0 * scale[0], -
              9.0 * scale[1], -10.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0], -
              1.0 * scale[1], -10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(0.0 * scale[0], -24.0 * scale[1], 18.0 * scale[0], -
              28.0 * scale[1], 25.0 * scale[0], -5.0 * scale[1])
    Curveto_r(4.0 * scale[0], 11.0 * scale[1], 4.0 * scale[0],
              23.0 * scale[1], 1.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0],
              1.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(51.0 * scale[0], 549.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -9.0 * scale[1], 7.0 * scale[0], -
              23.0 * scale[1], 17.0 * scale[0], -30.0 * scale[1])
    Curveto_r(15.0 * scale[0], -12.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 6.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 8.0 * scale[1], -14.0 * scale[0],
              22.0 * scale[1], -17.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 13.0 * scale[1], -6.0 * scale[0],
              12.0 * scale[1], -6.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(163.0 * scale[0], 343.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(37.0 * scale[0], -9.0 * scale[1], 15.0 * scale[0], -
              21.0 * scale[1], -37.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 1.0 * scale[1], -52.0 *
              scale[0], -1.0 * scale[1], -49.0 * scale[0], -5.0 * scale[1])
    Curveto_r(2.0 * scale[0], -5.0 * scale[1], 10.0 * scale[0], -
              8.0 * scale[1], 16.0 * scale[0], -8.0 * scale[1])
    Curveto_r(13.0 * scale[0], -1.0 * scale[1], 57.0 * scale[0], -
              35.0 * scale[1], 57.0 * scale[0], -45.0 * scale[1])
    Curveto_r(0.0 * scale[0], -3.0 * scale[1], -6.0 * scale[0], -
              3.0 * scale[1], -12.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 6.0 * scale[1], -9.0 * scale[0],
              3.0 * scale[1], 0.0 * scale[0], -9.0 * scale[1])
    Curveto_r(8.0 * scale[0], -9.0 * scale[1], 12.0 * scale[0], -
              26.0 * scale[1], 11.0 * scale[0], -39.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -32.0 * scale[1], 10.0 * scale[0], -
              68.0 * scale[1], 26.0 * scale[0], -68.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 25.0 * scale[0],
              4.0 * scale[1], 38.0 * scale[0], 9.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 30.0 * scale[0],
              6.0 * scale[1], 43.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], -13.0 * scale[1], 18.0 *
              scale[0], -14.0 * scale[1], 0.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -4.0 * scale[1], -26.0 *
              scale[0], -3.0 * scale[1], -35.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 6.0 * scale[1], -23.0 * scale[0],
              8.0 * scale[1], -32.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -3.0 * scale[1], -15.0 *
              scale[0], -8.0 * scale[1], -5.0 * scale[0], -28.0 * scale[1])
    Curveto_r(10.0 * scale[0], -22.0 * scale[1], 17.0 * scale[0], -
              25.0 * scale[1], 66.0 * scale[0], -23.0 * scale[1])
    Curveto_r(37.0 * scale[0], 1.0 * scale[1], 44.0 * scale[0],
              3.0 * scale[1], 22.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-27.0 * scale[0], 4.0 * scale[1], -31.0 * scale[0],
              7.0 * scale[1], -22.0 * scale[0], 19.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              11.0 * scale[1], 22.0 * scale[0], 8.0 * scale[1])
    Curveto_r(13.0 * scale[0], -8.0 * scale[1], 78.0 * scale[0], -
              23.0 * scale[1], 78.0 * scale[0], -18.0 * scale[1])
    Curveto_r(0.0 * scale[0], 2.0 * scale[1], -20.0 * scale[0],
              15.0 * scale[1], -44.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-35.0 * scale[0], 20.0 * scale[1], -42.0 * scale[0],
              30.0 * scale[1], -39.0 * scale[0], 48.0 * scale[1])
    Curveto_r(4.0 * scale[0], 18.0 * scale[1], -2.0 * scale[0],
              25.0 * scale[1], -31.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 9.0 * scale[1], -34.0 * scale[0],
              18.0 * scale[1], -29.0 * scale[0], 25.0 * scale[1])
    Curveto_r(4.0 * scale[0], 7.0 * scale[1], 0.0 * scale[0],
              6.0 * scale[1], -10.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-24.0 * scale[0], -19.0 * scale[1], -21.0 *
              scale[0], 2.0 * scale[1], 3.0 * scale[0], 24.0 * scale[1])
    Curveto_r(15.0 * scale[0], 14.0 * scale[1], 44.0 * scale[0],
              19.0 * scale[1], 135.0 * scale[0], 24.0 * scale[1])
    Curveto_r(63.0 * scale[0], 3.0 * scale[1], 115.0 * scale[0],
              3.0 * scale[1], 115.0 * scale[0], -1.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -7.0 * scale[0], -
              8.0 * scale[1], -15.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              4.0 * scale[1], -15.0 * scale[0], -9.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 60.0 *
              scale[0], -5.0 * scale[1], 90.0 * scale[0], 6.0 * scale[1])
    Curveto_r(8.0 * scale[0], 4.0 * scale[1], 23.0 * scale[0],
              5.0 * scale[1], 33.0 * scale[0], 4.0 * scale[1])
    Curveto_r(9.0 * scale[0], -1.0 * scale[1], 17.0 * scale[0],
              3.0 * scale[1], 17.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -6.0 * scale[0],
              11.0 * scale[1], -12.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -23.0 * scale[0],
              3.0 * scale[1], -36.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 5.0 * scale[1], -22.0 * scale[0],
              3.0 * scale[1], -20.0 * scale[0], -6.0 * scale[1])
    Curveto_r(2.0 * scale[0], -7.0 * scale[1], -3.0 * scale[0], -
              15.0 * scale[1], -10.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -3.0 * scale[1], -11.0 * scale[0],
              1.0 * scale[1], -10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(2.0 * scale[0], 10.0 * scale[1], -24.0 * scale[0],
              14.0 * scale[1], -117.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-93.0 * scale[0], 4.0 * scale[1], -110.0 * scale[0],
              7.0 * scale[1], -75.0 * scale[0], 12.0 * scale[1])
    Curveto_r(24.0 * scale[0], 4.0 * scale[1], 57.0 * scale[0],
              4.0 * scale[1], 72.0 * scale[0], 1.0 * scale[1])
    Curveto_r(17.0 * scale[0], -3.0 * scale[1], 28.0 *
              scale[0], -1.0 * scale[1], 28.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 5.0 * scale[0],
              11.0 * scale[1], 11.0 * scale[0], 11.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0], -
              6.0 * scale[1], 3.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -9.0 * scale[1], -3.0 *
              scale[0], -9.0 * scale[1], 9.0 * scale[0], 1.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 23.0 * scale[0],
              11.0 * scale[1], 32.0 * scale[0], 8.0 * scale[1])
    Curveto_r(8.0 * scale[0], -4.0 * scale[1], 16.0 *
              scale[0], -3.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], -66.0 * scale[0],
              8.0 * scale[1], -152.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-86.0 * scale[0], 0.0 * scale[1], -149.0 *
              scale[0], -2.0 * scale[1], -139.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto_r(34.0 * scale[0], -129.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 17.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(-3.0 * scale[0], -40.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -11.0 * scale[1], 1.0 * scale[0], -
              14.0 * scale[1], -11.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 2.0 * scale[1], -17.0 * scale[0],
              11.0 * scale[1], -19.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 20.0 * scale[1], 22.0 * scale[0],
              13.0 * scale[1], 30.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(496.0 * scale[0], 341.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -5.0 * scale[1], 3.0 * scale[0], -
              7.0 * scale[1], 14.0 * scale[0], -4.0 * scale[1])
    Curveto_r(23.0 * scale[0], 6.0 * scale[1], 26.0 * scale[0],
              13.0 * scale[1], 6.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0], -
              4.0 * scale[1], -20.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(546.0 * scale[0], 338.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], -3.0 * scale[0], -
              8.0 * scale[1], -13.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -16.0 *
              scale[0], -1.0 * scale[1], 2.0 * scale[0], -8.0 * scale[1])
    Curveto_r(11.0 * scale[0], -5.0 * scale[1], 23.0 *
              scale[0], -4.0 * scale[1], 26.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], 22.0 * scale[0],
              3.0 * scale[1], 44.0 * scale[0], -6.0 * scale[1])
    Curveto_r(20.0 * scale[0], -9.0 * scale[1], 41.0 * scale[0], -
              16.0 * scale[1], 46.0 * scale[0], -16.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              22.0 * scale[1], -6.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 5.0 * scale[1], -1.0 * scale[0],
              6.0 * scale[1], 10.0 * scale[0], 2.0 * scale[1])
    Curveto_r(39.0 * scale[0], -14.0 * scale[1], 65.0 *
              scale[0], -17.0 * scale[1], 65.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -6.0 * scale[0],
              12.0 * scale[1], -13.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 8.0 * scale[1], -166.0 * scale[0],
              3.0 * scale[1], -161.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(785.0 * scale[0], 330.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(32.0 * scale[0], -11.0 * scale[1], 61.0 * scale[0], -
              17.0 * scale[1], 64.0 * scale[0], -14.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              7.0 * scale[1], -18.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 4.0 * scale[1], -19.0 * scale[0],
              8.0 * scale[1], -9.0 * scale[0], 14.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], -8.0 * scale[0],
              9.0 * scale[1], -42.0 * scale[0], 8.0 * scale[1])
    Lineto_r(-55.0 * scale[0], 0.0 * scale[1])
    Lineto_r(60.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(720.0 * scale[0], 315.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -11.0 * scale[1], -17.0 *
              scale[0], -12.0 * scale[1], -32.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 6.0 * scale[1], -22.0 * scale[0],
              8.0 * scale[1], -26.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], 1.0 *
              scale[0], -6.0 * scale[1], 9.0 * scale[0], -6.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0], -
              2.0 * scale[1], -1.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -6.0 * scale[1], -34.0 *
              scale[0], -7.0 * scale[1], -57.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-26.0 * scale[0], 4.0 * scale[1], -43.0 * scale[0],
              2.0 * scale[1], -43.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], 81.0 * scale[0], -
              26.0 * scale[1], 89.0 * scale[0], -14.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], 29.0 * scale[0],
              9.0 * scale[1], 56.0 * scale[0], 9.0 * scale[1])
    Curveto_r(28.0 * scale[0], 1.0 * scale[1], 44.0 * scale[0], -
              1.0 * scale[1], 37.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -2.0 * scale[1], -9.0 * scale[0], -
              10.0 * scale[1], -6.0 * scale[0], -15.0 * scale[1])
    Curveto_r(5.0 * scale[0], -7.0 * scale[1], 2.0 * scale[0], -
              8.0 * scale[1], -6.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 11.0 * scale[1], -60.0 * scale[0],
              13.0 * scale[1], -60.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 12.0 * scale[0], -
              8.0 * scale[1], 28.0 * scale[0], -9.0 * scale[1])
    Curveto_r(24.0 * scale[0], -1.0 * scale[1], 22.0 * scale[0], -
              3.0 * scale[1], -13.0 * scale[0], -13.0 * scale[1])
    Lineto_r(-40.0 * scale[0], -13.0 * scale[1])
    Lineto_r(36.0 * scale[0], -7.0 * scale[1])
    Curveto_r(20.0 * scale[0], -3.0 * scale[1], 47.0 *
              scale[0], -2.0 * scale[1], 60.0 * scale[0], 3.0 * scale[1])
    Curveto_r(13.0 * scale[0], 5.0 * scale[1], 18.0 * scale[0],
              10.0 * scale[1], 11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 1.0 * scale[1], -10.0 * scale[0],
              6.0 * scale[1], -7.0 * scale[0], 11.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], 10.0 * scale[0],
              8.0 * scale[1], 15.0 * scale[0], 5.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 11.0 *
              scale[0], -1.0 * scale[1], 15.0 * scale[0], 5.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], 1.0 * scale[0],
              10.0 * scale[1], -5.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-27.0 * scale[0], 0.0 * scale[1], 4.0 * scale[0],
              20.0 * scale[1], 33.0 * scale[0], 21.0 * scale[1])
    Lineto_r(32.0 * scale[0], 1.0 * scale[1])
    Lineto_r(-33.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 4.0 * scale[1], -39.0 * scale[0],
              13.0 * scale[1], -45.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 15.0 * scale[1], -32.0 * scale[0],
              14.0 * scale[1], -47.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto_r(33.0 * scale[0], -12.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              5.0 * scale[1], 12.0 * scale[0], 5.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(-20.0 * scale[0], -70.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              5.0 * scale[1], 12.0 * scale[0], 5.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(875.0 * scale[0], 310.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(27.0 * scale[0], -12.0 * scale[1], 43.0 *
              scale[0], -12.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -22.0 * scale[0],
              9.0 * scale[1], -30.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 0.0 * scale[1], -8.0 *
              scale[0], -3.0 * scale[1], 5.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(570.0 * scale[0], 247.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 15.0 * scale[0], -
              6.0 * scale[1], 34.0 * scale[0], -3.0 * scale[1])
    Curveto_r(23.0 * scale[0], 4.0 * scale[1], 35.0 * scale[0],
              3.0 * scale[1], 38.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], 6.0 * scale[0], -
              7.0 * scale[1], 10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(5.0 * scale[0], 12.0 * scale[1], -2.0 * scale[0],
              15.0 * scale[1], -38.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 0.0 * scale[1], -44.0 *
              scale[0], -4.0 * scale[1], -44.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(318.0 * scale[0], 218.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -5.0 * scale[1], 16.0 * scale[0], -
              8.0 * scale[1], 23.0 * scale[0], -6.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 3.0 * scale[0],
              7.0 * scale[1], -10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 4.0 * scale[1], -21.0 * scale[0],
              3.0 * scale[1], -13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(604.0 * scale[0], 218.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], -4.0 *
              scale[0], -10.0 * scale[1], 1.0 * scale[0], -6.0 * scale[1])
    Curveto_r(4.0 * scale[0], 4.0 * scale[1], 15.0 * scale[0],
              2.0 * scale[1], 24.0 * scale[0], -5.0 * scale[1])
    Curveto_r(14.0 * scale[0], -11.0 * scale[1], 14.0 *
              scale[0], -10.0 * scale[1], 2.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 20.0 * scale[1], -18.0 * scale[0],
              21.0 * scale[1], -27.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(656.0 * scale[0], 202.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 4.0 * scale[0], -
              12.0 * scale[1], 17.0 * scale[0], -16.0 * scale[1])
    Curveto_r(12.0 * scale[0], -3.0 * scale[1], 24.0 *
              scale[0], -1.0 * scale[1], 25.0 * scale[0], 4.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 10.0 * scale[0],
              10.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0], -
              4.0 * scale[1], 9.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], 5.0 * scale[0], -
              10.0 * scale[1], 19.0 * scale[0], -10.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 26.0 * scale[0],
              4.0 * scale[1], 26.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 15.0 * scale[1], -59.0 * scale[0],
              24.0 * scale[1], -74.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -7.0 * scale[1], -16.0 *
              scale[0], -7.0 * scale[1], -23.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 7.0 * scale[1], -13.0 * scale[0],
              7.0 * scale[1], -17.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(290.0 * scale[0], 189.0 * scale[1], x, y)
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
    Moveto(709.0 * scale[0], 163.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              14.0 * scale[1], -3.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -13.0 * scale[1], -18.0 * scale[0], -
              20.0 * scale[1], -53.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -1.0 * scale[1], -7.0 *
              scale[0], -12.0 * scale[1], 8.0 * scale[0], -14.0 * scale[1])
    Curveto_r(5.0 * scale[0], -1.0 * scale[1], 19.0 * scale[0], -
              3.0 * scale[1], 32.0 * scale[0], -4.0 * scale[1])
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 3.0 * scale[0], -
              6.0 * scale[1], -23.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-41.0 * scale[0], -6.0 * scale[1], -42.0 *
              scale[0], -7.0 * scale[1], -11.0 * scale[0], -8.0 * scale[1])
    Curveto_r(19.0 * scale[0], -1.0 * scale[1], 42.0 * scale[0], -
              9.0 * scale[1], 52.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -14.0 * scale[1], 18.0 *
              scale[0], -14.0 * scale[1], 33.0 * scale[0], 0.0 * scale[1])
    Curveto_r(18.0 * scale[0], 18.0 * scale[1], 22.0 * scale[0],
              65.0 * scale[1], 5.0 * scale[0], 65.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              4.0 * scale[1], -5.0 * scale[0], -8.0 * scale[1])
    Curveto_r(2.0 * scale[0], -4.0 * scale[1], -4.0 * scale[0], -
              9.0 * scale[1], -15.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -1.0 * scale[1], -17.0 * scale[0],
              1.0 * scale[1], -6.0 * scale[0], 11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 19.0 * scale[0],
              15.0 * scale[1], 27.0 * scale[0], 19.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 3.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 1.0 * scale[1], -26.0 * scale[0],
              5.0 * scale[1], -22.0 * scale[0], 11.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 4.0 * scale[0],
              10.0 * scale[1], 1.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              3.0 * scale[1], -7.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(738.0 * scale[0], 163.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(314.0 * scale[0], 89.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 6.0 * scale[0], -
              9.0 * scale[1], 20.0 * scale[0], -9.0 * scale[1])
    Curveto_r(31.0 * scale[0], 0.0 * scale[1], 34.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 3.0 * scale[1], -23.0 * scale[0],
              1.0 * scale[1], -26.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(114.0 * scale[0], 64.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -23.0 * scale[1], 126.0 * scale[0], -
              66.0 * scale[1], 126.0 * scale[0], -45.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], -67.0 * scale[0],
              34.0 * scale[1], -80.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -3.0 * scale[1], -7.0 * scale[0],
              0.0 * scale[1], -4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(5.0 * scale[0], 12.0 * scale[1], 11.0 * scale[0],
              13.0 * scale[1], 24.0 * scale[0], 6.0 * scale[1])
    Curveto_r(24.0 * scale[0], -13.0 * scale[1], 87.0 *
              scale[0], -13.0 * scale[1], 95.0 * scale[0], 0.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], -4.0 * scale[0],
              10.0 * scale[1], -17.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -41.0 * scale[0],
              2.0 * scale[1], -63.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 3.0 * scale[1], -42.0 * scale[0],
              0.0 * scale[1], -46.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -9.0 * scale[1], -11.0 *
              scale[0], -9.0 * scale[1], -22.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 10.0 * scale[1], -15.0 * scale[0],
              9.0 * scale[1], -13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(870.0 * scale[0], 60.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 5.0 * scale[0], -
              10.0 * scale[1], 12.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0], -
              3.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -11.0 *
              scale[0], -2.0 * scale[1], -19.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 12.0 * scale[1], -108.0 * scale[0],
              15.0 * scale[1], -108.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -22.0 * scale[0], -
              10.0 * scale[1], -50.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-36.0 * scale[0], 0.0 * scale[1], -50.0 * scale[0], -
              4.0 * scale[1], -50.0 * scale[0], -14.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -6.0 * scale[0], -
              17.0 * scale[1], -12.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -8.0 * scale[1], 58.0 *
              scale[0], -8.0 * scale[1], 137.0 * scale[0], 0.0 * scale[1])
    Curveto_r(61.0 * scale[0], 6.0 * scale[1], 66.0 * scale[0],
              8.0 * scale[1], 35.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 5.0 * scale[1], -27.0 * scale[0],
              7.0 * scale[1], 23.0 * scale[0], 8.0 * scale[1])
    Curveto_r(31.0 * scale[0], 0.0 * scale[1], 57.0 * scale[0],
              6.0 * scale[1], 57.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 5.0 * scale[0],
              9.0 * scale[1], 11.0 * scale[0], 8.0 * scale[1])
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 13.0 * scale[0],
              3.0 * scale[1], 15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(1.0 * scale[0], 7.0 * scale[1], 0.0 * scale[0],
              8.0 * scale[1], -2.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -14.0 *
              scale[0], -7.0 * scale[1], -30.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 6.0 * scale[1], -24.0 * scale[0],
              6.0 * scale[1], -24.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto_r(-160.0 * scale[0], -40.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -5.0 * scale[0], -
              10.0 * scale[1], -11.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0],
              5.0 * scale[1], -4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 8.0 * scale[0],
              10.0 * scale[1], 11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 4.0 * scale[0], -
              4.0 * scale[1], 4.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(290.0 * scale[0], 50.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -5.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -5.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0],
              5.0 * scale[1], 25.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 11.0 * scale[0],
              10.0 * scale[1], 5.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0], -
              5.0 * scale[1], -25.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(320.0 * scale[0], 40.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -8.0 * scale[1], -13.0 *
              scale[0], -10.0 * scale[1], 2.0 * scale[0], -10.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0],
              5.0 * scale[1], 23.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 13.0 * scale[1], -5.0 * scale[0],
              13.0 * scale[1], -25.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(560.0 * scale[0], 29.0 * scale[1], x, y)
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
    Moveto(375.0 * scale[0], 21.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -6.0 * scale[1], -35.0 * scale[0], -
              12.0 * scale[1], -65.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-55.0 * scale[0], -3.0 * scale[1], -54.0 *
              scale[0], -3.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    Curveto_r(54.0 * scale[0], -2.0 * scale[1], 67.0 * scale[0],
              1.0 * scale[1], 67.0 * scale[0], 13.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], -3.0 * scale[0],
              18.0 * scale[1], -15.0 * scale[0], 6.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#b37e39')
    te.end_fill()
    Moveto(294.0 * scale[0], 1371.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -12.0 * scale[1], -14.0 * scale[0], -
              19.0 * scale[1], -54.0 * scale[0], -28.0 * scale[1])
    Curveto_r(-30.0 * scale[0], -6.0 * scale[1], -53.0 * scale[0], -
              12.0 * scale[1], -50.0 * scale[0], -13.0 * scale[1])
    Curveto_r(15.0 * scale[0], -5.0 * scale[1], 61.0 * scale[0], -
              11.0 * scale[1], 107.0 * scale[0], -15.0 * scale[1])
    Curveto_r(28.0 * scale[0], -1.0 * scale[1], 57.0 * scale[0], -
              6.0 * scale[1], 63.0 * scale[0], -10.0 * scale[1])
    Curveto_r(21.0 * scale[0], -13.0 * scale[1], 21.0 * scale[0],
              2.0 * scale[1], 0.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 15.0 * scale[1], -21.0 * scale[0],
              30.0 * scale[1], -21.0 * scale[0], 34.0 * scale[1])
    Curveto_r(1.0 * scale[0], 4.0 * scale[1], -10.0 * scale[0],
              11.0 * scale[1], -23.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 5.0 * scale[1], -23.0 * scale[0],
              3.0 * scale[1], -22.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(411.0 * scale[0], 1372.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -7.0 * scale[1], -11.0 * scale[0], -
              12.0 * scale[1], -6.0 * scale[0], -11.0 * scale[1])
    Curveto_r(29.0 * scale[0], 4.0 * scale[1], 47.0 * scale[0], -
              2.0 * scale[1], 42.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -1.0 * scale[0], -
              20.0 * scale[1], 5.0 * scale[0], -28.0 * scale[1])
    Curveto_r(8.0 * scale[0], -11.0 * scale[1], 9.0 *
              scale[0], -10.0 * scale[1], 4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -1.0 * scale[0],
              17.0 * scale[1], 4.0 * scale[0], 17.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              6.0 * scale[1], 10.0 * scale[0], -14.0 * scale[1])
    Curveto_r(0.0 * scale[0], -18.0 * scale[1], 27.0 * scale[0], -
              29.0 * scale[1], 36.0 * scale[0], -14.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], 3.0 * scale[0],
              8.0 * scale[1], -3.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -4.0 * scale[1], -14.0 * scale[0],
              0.0 * scale[1], -17.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 11.0 * scale[1], 0.0 * scale[0],
              15.0 * scale[1], 12.0 * scale[0], 13.0 * scale[1])
    Curveto_r(10.0 * scale[0], -2.0 * scale[1], 16.0 * scale[0],
              2.0 * scale[1], 14.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 11.0 * scale[1], 0.0 * scale[0],
              12.0 * scale[1], 11.0 * scale[0], 2.0 * scale[1])
    Curveto_r(12.0 * scale[0], -9.0 * scale[1], 16.0 *
              scale[0], -8.0 * scale[1], 21.0 * scale[0], 5.0 * scale[1])
    Curveto_r(4.0 * scale[0], 9.0 * scale[1], 4.0 * scale[0],
              20.0 * scale[1], 0.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 11.0 * scale[1], -117.0 * scale[0],
              6.0 * scale[1], -133.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(607.0 * scale[0], 1383.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -26.0 * scale[1], 175.0 *
              scale[0], -64.0 * scale[1], 200.0 * scale[0], -40.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], -5.0 * scale[0],
              7.0 * scale[1], -18.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -34.0 * scale[0],
              6.0 * scale[1], -45.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 9.0 * scale[1], -40.0 * scale[0],
              14.0 * scale[1], -72.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-29.0 * scale[0], -2.0 * scale[1], -53.0 * scale[0],
              2.0 * scale[1], -55.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 6.0 * scale[1], -6.0 * scale[0],
              6.0 * scale[1], -10.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(243.0 * scale[0], 1363.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(355.0 * scale[0], 1350.0 * scale[1], x, y)
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
    Moveto(600.0 * scale[0], 1326.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], -4.0 * scale[0], -
              26.0 * scale[1], -9.0 * scale[0], -26.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0], -
              31.0 * scale[1], -1.0 * scale[0], -47.0 * scale[1])
    Curveto_r(21.0 * scale[0], -19.0 * scale[1], 28.0 *
              scale[0], -39.0 * scale[1], 8.0 * scale[0], -27.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 5.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -4.0 * scale[0], -5.0 * scale[1])
    Curveto_r(21.0 * scale[0], -33.0 * scale[1], -1.0 * scale[0], -
              120.0 * scale[1], -25.0 * scale[0], -105.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0],
              0.0 * scale[1], -9.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 207.0 *
              scale[0], -6.0 * scale[1], 222.0 * scale[0], 9.0 * scale[1])
    Curveto_r(12.0 * scale[0], 12.0 * scale[1], -46.0 * scale[0],
              55.0 * scale[1], -114.0 * scale[0], 87.0 * scale[1])
    Curveto_r(-64.0 * scale[0], 30.0 * scale[1], -49.0 * scale[0],
              33.0 * scale[1], 24.0 * scale[0], 5.0 * scale[1])
    Curveto_r(61.0 * scale[0], -23.0 * scale[1], 73.0 *
              scale[0], -25.0 * scale[1], 39.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 13.0 * scale[1], -23.0 * scale[0],
              14.0 * scale[1], -5.0 * scale[0], 23.0 * scale[1])
    Curveto_r(10.0 * scale[0], 6.0 * scale[1], 24.0 * scale[0],
              8.0 * scale[1], 31.0 * scale[0], 6.0 * scale[1])
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 14.0 * scale[0],
              1.0 * scale[1], 18.0 * scale[0], 6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 5.0 * scale[0],
              11.0 * scale[1], 3.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-42.0 * scale[0], 4.0 * scale[1], -114.0 * scale[0],
              13.0 * scale[1], -117.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 2.0 * scale[1], 14.0 * scale[0],
              4.0 * scale[1], 37.0 * scale[0], 4.0 * scale[1])
    Curveto_r(50.0 * scale[0], 0.0 * scale[1], 56.0 * scale[0],
              17.0 * scale[1], 10.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 2.0 * scale[1], -10.0 * scale[0],
              4.0 * scale[1], 19.0 * scale[0], 3.0 * scale[1])
    Curveto_r(60.0 * scale[0], -1.0 * scale[1], 72.0 * scale[0],
              15.0 * scale[1], 16.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-43.0 * scale[0], 5.0 * scale[1], -99.0 * scale[0],
              17.0 * scale[1], -125.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 6.0 * scale[1], -18.0 * scale[0],
              2.0 * scale[1], -18.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(285.0 * scale[0], 1290.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(33.0 * scale[0], -6.0 * scale[1], 68.0 * scale[0], -
              15.0 * scale[1], 77.0 * scale[0], -20.0 * scale[1])
    Curveto_r(12.0 * scale[0], -6.0 * scale[1], 19.0 *
              scale[0], -6.0 * scale[1], 24.0 * scale[0], 2.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], 3.0 * scale[0],
              8.0 * scale[1], -4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -2.0 * scale[1], -14.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 6.0 * scale[1], -35.0 * scale[0],
              12.0 * scale[1], -73.0 * scale[0], 15.0 * scale[1])
    Lineto_r(-70.0 * scale[0], 4.0 * scale[1])
    Lineto_r(60.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(328.0 * scale[0], 1263.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(203.0 * scale[0], 1239.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -10.0 * scale[1], 5.0 * scale[0], -
              15.0 * scale[1], 9.0 * scale[0], -13.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 6.0 * scale[0],
              11.0 * scale[1], 2.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 7.0 * scale[1], 0.0 * scale[0],
              5.0 * scale[1], 8.0 * scale[0], -3.0 * scale[1])
    Curveto_r(9.0 * scale[0], -10.0 * scale[1], 37.0 * scale[0], -
              16.0 * scale[1], 86.0 * scale[0], -19.0 * scale[1])
    Curveto_r(63.0 * scale[0], -3.0 * scale[1], 71.0 *
              scale[0], -1.0 * scale[1], 66.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 16.0 * scale[1], -18.0 * scale[0],
              18.0 * scale[1], -126.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-39.0 * scale[0], 1.0 * scale[1], -46.0 * scale[0], -
              1.0 * scale[1], -45.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(765.0 * scale[0], 1200.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(16.0 * scale[0], -10.0 * scale[1], 32.0 * scale[0], -
              17.0 * scale[1], 35.0 * scale[0], -14.0 * scale[1])
    Curveto_r(7.0 * scale[0], 8.0 * scale[1], -31.0 * scale[0],
              34.0 * scale[1], -49.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              8.0 * scale[1], 14.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(242.0 * scale[0], 1193.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -13.0 * scale[1], -25.0 *
              scale[0], -14.0 * scale[1], -32.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 8.0 * scale[1], -10.0 * scale[0],
              9.0 * scale[1], -14.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -13.0 * scale[1], 17.0 * scale[0], -
              22.0 * scale[1], 46.0 * scale[0], -15.0 * scale[1])
    Curveto_r(16.0 * scale[0], 3.0 * scale[1], 19.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -7.0 * scale[1], -5.0 * scale[0], -
              11.0 * scale[1], 18.0 * scale[0], -16.0 * scale[1])
    Curveto_r(49.0 * scale[0], -9.0 * scale[1], 90.0 *
              scale[0], -7.0 * scale[1], 90.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -4.0 * scale[0],
              8.0 * scale[1], -9.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -3.0 * scale[1], -17.0 * scale[0],
              2.0 * scale[1], -27.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 15.0 * scale[1], -18.0 * scale[0],
              15.0 * scale[1], 3.0 * scale[0], 11.0 * scale[1])
    Curveto_r(27.0 * scale[0], -6.0 * scale[1], 40.0 * scale[0],
              8.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-28.0 * scale[0], 11.0 * scale[1], -79.0 * scale[0],
              5.0 * scale[1], -102.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(261.0 * scale[0], 1131.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(40.0 * scale[0], -13.0 * scale[1], 124.0 * scale[0], -
              22.0 * scale[1], 113.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 5.0 * scale[1], -38.0 * scale[0],
              12.0 * scale[1], -74.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-42.0 * scale[0], 4.0 * scale[1], -56.0 * scale[0],
              3.0 * scale[1], -39.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(240.0 * scale[0], 1116.0 * scale[1], x, y)
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
    Moveto(328.0 * scale[0], 1087.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(24.0 * scale[0], -7.0 * scale[1], 40.0 * scale[0], -
              15.0 * scale[1], 36.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -4.0 * scale[1], -2.0 *
              scale[0], -7.0 * scale[1], 4.0 * scale[0], -7.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 18.0 * scale[0], -
              3.0 * scale[1], 28.0 * scale[0], -7.0 * scale[1])
    Curveto_r(12.0 * scale[0], -4.0 * scale[1], 15.0 *
              scale[0], -3.0 * scale[1], 10.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 8.0 * scale[1], 0.0 * scale[0],
              12.0 * scale[1], 11.0 * scale[0], 13.0 * scale[1])
    Curveto_r(36.0 * scale[0], 1.0 * scale[1], -31.0 * scale[0],
              21.0 * scale[1], -82.0 * scale[0], 24.0 * scale[1])
    Lineto_r(-50.0 * scale[0], 3.0 * scale[1])
    Lineto_r(43.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(270.0 * scale[0], 1070.0 * scale[1], x, y)
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
    Moveto(537.0 * scale[0], 1073.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -16.0 * scale[1], -4.0 *
              scale[0], -22.0 * scale[1], 38.0 * scale[0], -19.0 * scale[1])
    Curveto_r(25.0 * scale[0], 2.0 * scale[1], 48.0 * scale[0], -
              1.0 * scale[1], 51.0 * scale[0], -5.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 13.0 * scale[0], -
              9.0 * scale[1], 22.0 * scale[0], -8.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              2.0 * scale[1], -3.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], 1.0 * scale[0],
              11.0 * scale[1], 55.0 * scale[0], 18.0 * scale[1])
    Lineto_r(75.0 * scale[0], 10.0 * scale[1])
    Lineto_r(-116.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-64.0 * scale[0], 0.0 * scale[1], -119.0 *
              scale[0], -2.0 * scale[1], -122.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(480.0 * scale[0], 1050.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(786.0 * scale[0], 974.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -18.0 * scale[1], -21.0 *
              scale[0], -34.0 * scale[1], -5.0 * scale[0], -34.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0], -
              5.0 * scale[1], -1.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -12.0 * scale[1], -10.0 *
              scale[0], -18.0 * scale[1], 3.0 * scale[0], -31.0 * scale[1])
    Curveto_r(14.0 * scale[0], -15.0 * scale[1], 20.0 *
              scale[0], -15.0 * scale[1], 42.0 * scale[0], -3.0 * scale[1])
    Curveto_r(27.0 * scale[0], 15.0 * scale[1], 34.0 * scale[0],
              50.0 * scale[1], 10.0 * scale[0], 50.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0],
              6.0 * scale[1], -14.0 * scale[0], 13.0 * scale[1])
    Curveto_r(5.0 * scale[0], 39.0 * scale[1], -9.0 * scale[0],
              48.0 * scale[1], -35.0 * scale[0], 21.0 * scale[1])
    te.end_fill()
    Moveto(942.0 * scale[0], 936.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -8.0 * scale[1], 15.0 * scale[0], -
              12.0 * scale[1], 17.0 * scale[0], -11.0 * scale[1])
    Curveto_r(5.0 * scale[0], 6.0 * scale[1], -10.0 * scale[0],
              25.0 * scale[1], -20.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              6.0 * scale[1], 3.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(905.0 * scale[0], 900.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(13.0 * scale[0], -14.0 * scale[1], 21.0 *
              scale[0], -17.0 * scale[1], 26.0 * scale[0], -9.0 * scale[1])
    Curveto_r(5.0 * scale[0], 8.0 * scale[1], 8.0 * scale[0],
              8.0 * scale[1], 13.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], -14.0 * scale[1], 26.0 *
              scale[0], -14.0 * scale[1], 26.0 * scale[0], 0.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -5.0 * scale[0],
              7.0 * scale[1], -10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -3.0 * scale[1], -13.0 * scale[0],
              1.0 * scale[1], -16.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 12.0 * scale[1], -9.0 * scale[0],
              13.0 * scale[1], -20.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -8.0 * scale[1], -14.0 *
              scale[0], -8.0 * scale[1], -14.0 * scale[0], 0.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              11.0 * scale[1], -12.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -3.0 * scale[0], -
              9.0 * scale[1], 7.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(820.0 * scale[0], 853.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 3.0 * scale[0], -
              13.0 * scale[1], 7.0 * scale[0], -10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], 13.0 * scale[0],
              1.0 * scale[1], 22.0 * scale[0], -5.0 * scale[1])
    Curveto_r(10.0 * scale[0], -8.0 * scale[1], 9.0 * scale[0], -
              4.0 * scale[1], -3.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 26.0 * scale[1], -26.0 * scale[0],
              27.0 * scale[1], -26.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(911.0 * scale[0], 832.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -13.0 * scale[1], -17.0 * scale[0], -
              19.0 * scale[1], -26.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 9.0 * scale[1], -18.0 *
              scale[0], -13.0 * scale[1], 5.0 * scale[0], -36.0 * scale[1])
    Curveto_r(11.0 * scale[0], -11.0 * scale[1], 33.0 * scale[0], -
              20.0 * scale[1], 50.0 * scale[0], -20.0 * scale[1])
    Curveto_r(27.0 * scale[0], 0.0 * scale[1], 30.0 * scale[0],
              3.0 * scale[1], 30.0 * scale[0], 30.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], -5.0 * scale[0],
              30.0 * scale[1], -11.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0],
              8.0 * scale[1], -24.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 15.0 * scale[1], -13.0 * scale[0],
              15.0 * scale[1], -24.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(690.0 * scale[0], 822.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 10.0 * scale[0], -
              17.0 * scale[1], 22.0 * scale[0], -28.0 * scale[1])
    Lineto_r(21.0 * scale[0], -19.0 * scale[1])
    Lineto_r(-18.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 28.0 * scale[1], -25.0 * scale[0],
              33.0 * scale[1], -25.0 * scale[0], 19.0 * scale[1])
    te.end_fill()
    Moveto(620.0 * scale[0], 761.0 * scale[1], x, y)
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
    Moveto(772.0 * scale[0], 739.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -16.0 * scale[1], 30.0 * scale[0], -
              29.0 * scale[1], 40.0 * scale[0], -29.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0], -
              4.0 * scale[1], 13.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 0.0 * scale[0], -
              10.0 * scale[1], 8.0 * scale[0], -10.0 * scale[1])
    Curveto_r(50.0 * scale[0], 0.0 * scale[1], 3.0 * scale[0],
              68.0 * scale[1], -51.0 * scale[0], 75.0 * scale[1])
    Lineto_r(-31.0 * scale[0], 3.0 * scale[1])
    Lineto_r(21.0 * scale[0], -29.0 * scale[1])
    te.end_fill()
    Moveto(138.0 * scale[0], 739.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-21.0 * scale[0], -12.0 * scale[1], -22.0 *
              scale[0], -28.0 * scale[1], -6.0 * scale[0], -64.0 * scale[1])
    Curveto_r(7.0 * scale[0], -16.0 * scale[1], 17.0 * scale[0], -
              24.0 * scale[1], 26.0 * scale[0], -20.0 * scale[1])
    Curveto_r(11.0 * scale[0], 4.0 * scale[1], 13.0 * scale[0], -
              1.0 * scale[1], 10.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -17.0 * scale[1], -1.0 *
              scale[0], -23.0 * scale[1], 9.0 * scale[0], -19.0 * scale[1])
    Curveto_r(16.0 * scale[0], 6.0 * scale[1], 17.0 * scale[0], -
              19.0 * scale[1], 2.0 * scale[0], -34.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -42.0 * scale[1], 13.0 * scale[0], -39.0 * scale[1])
    Curveto_r(24.0 * scale[0], 3.0 * scale[1], 38.0 * scale[0],
              17.0 * scale[1], 38.0 * scale[0], 37.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], -4.0 * scale[0],
              17.0 * scale[1], -10.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -4.0 * scale[1], -7.0 * scale[0],
              6.0 * scale[1], -4.0 * scale[0], 24.0 * scale[1])
    Curveto_r(7.0 * scale[0], 32.0 * scale[1], -9.0 * scale[0],
              84.0 * scale[1], -34.0 * scale[0], 114.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 20.0 * scale[1], -21.0 * scale[0],
              20.0 * scale[1], -44.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(14.0 * scale[0], 696.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -18.0 * scale[1], 16.0 * scale[0], -
              63.0 * scale[1], 25.0 * scale[0], -48.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 11.0 * scale[0],
              0.0 * scale[1], 18.0 * scale[0], -14.0 * scale[1])
    Curveto_r(6.0 * scale[0], -14.0 * scale[1], 7.0 * scale[0], -
              26.0 * scale[1], 2.0 * scale[0], -30.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -7.0 * scale[1], -11.0 *
              scale[0], -26.0 * scale[1], 2.0 * scale[0], -61.0 * scale[1])
    Curveto_r(10.0 * scale[0], -27.0 * scale[1], 11.0 *
              scale[0], -27.0 * scale[1], 25.0 * scale[0], -9.0 * scale[1])
    Curveto_r(8.0 * scale[0], 11.0 * scale[1], 14.0 * scale[0],
              31.0 * scale[1], 15.0 * scale[0], 45.0 * scale[1])
    Lineto_r(0.0 * scale[0], 26.0 * scale[1])
    Lineto_r(11.0 * scale[0], -25.0 * scale[1])
    Curveto_r(10.0 * scale[0], -22.0 * scale[1], 12.0 *
              scale[0], -23.0 * scale[1], 15.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 10.0 * scale[1], -2.0 * scale[0],
              25.0 * scale[1], -11.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 17.0 * scale[1], -21.0 * scale[0],
              12.0 * scale[1], -29.0 * scale[0], -38.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -14.0 * scale[1], -4.0 *
              scale[0], -1.0 * scale[1], -3.0 * scale[0], 29.0 * scale[1])
    Curveto_r(0.0 * scale[0], 35.0 * scale[1], -4.0 * scale[0],
              56.0 * scale[1], -12.0 * scale[0], 59.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 2.0 * scale[1], -12.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -9.0 * scale[0],
              18.0 * scale[1], -20.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 10.0 * scale[1], -21.0 * scale[0],
              10.0 * scale[1], -26.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(359.0 * scale[0], 638.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -9.0 * scale[1], -4.0 * scale[0], -
              58.0 * scale[1], 1.0 * scale[0], -58.0 * scale[1])
    Curveto_r(17.0 * scale[0], 1.0 * scale[1], 29.0 * scale[0],
              19.0 * scale[1], 23.0 * scale[0], 38.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 18.0 * scale[1], -19.0 * scale[0],
              30.0 * scale[1], -24.0 * scale[0], 20.0 * scale[1])
    te.end_fill()
    Moveto(7.0 * scale[0], 607.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -1.0 * scale[0], -
              20.0 * scale[1], 4.0 * scale[0], -28.0 * scale[1])
    Curveto_r(6.0 * scale[0], -10.0 * scale[1], 9.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 29.0 * scale[1], -5.0 * scale[0],
              35.0 * scale[1], -13.0 * scale[0], 14.0 * scale[1])
    te.end_fill()
    Moveto(465.0 * scale[0], 340.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -4.0 * scale[1], -26.0 *
              scale[0], -5.0 * scale[1], -33.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 2.0 * scale[1], -20.0 * scale[0], -
              2.0 * scale[1], -29.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -10.0 * scale[1], -15.0 *
              scale[0], -10.0 * scale[1], -9.0 * scale[0], -1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              12.0 * scale[1], -3.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              5.0 * scale[1], -11.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -12.0 * scale[0], -
              9.0 * scale[1], -32.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 3.0 * scale[1], -51.0 * scale[0],
              2.0 * scale[1], -73.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-31.0 * scale[0], -7.0 * scale[1], -14.0 *
              scale[0], -9.0 * scale[1], 78.0 * scale[0], -11.0 * scale[1])
    Curveto_r(64.0 * scale[0], -1.0 * scale[1], 132.0 *
              scale[0], -4.0 * scale[1], 150.0 * scale[0], -6.0 * scale[1])
    Curveto_r(17.0 * scale[0], -1.0 * scale[1], 49.0 *
              scale[0], -3.0 * scale[1], 70.0 * scale[0], -4.0 * scale[1])
    Curveto_r(21.0 * scale[0], -1.0 * scale[1], 59.0 * scale[0], -
              8.0 * scale[1], 85.0 * scale[0], -16.0 * scale[1])
    Curveto_r(79.0 * scale[0], -23.0 * scale[1], 72.0 * scale[0], -
              15.0 * scale[1], -13.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-44.0 * scale[0], 16.0 * scale[1], -81.0 * scale[0],
              25.0 * scale[1], -83.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -5.0 * scale[1], -13.0 *
              scale[0], -6.0 * scale[1], -24.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 5.0 * scale[1], -21.0 * scale[0],
              6.0 * scale[1], -2.0 * scale[0], 14.0 * scale[1])
    Curveto_r(14.0 * scale[0], 6.0 * scale[1], 11.0 * scale[0],
              7.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -2.0 * scale[1], -34.0 * scale[0],
              0.0 * scale[1], -35.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 4.0 * scale[1], -12.0 * scale[0],
              4.0 * scale[1], -23.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(665.0 * scale[0], 324.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(16.0 * scale[0], -9.0 * scale[1], 43.0 * scale[0], -
              18.0 * scale[1], 60.0 * scale[0], -19.0 * scale[1])
    Curveto_r(16.0 * scale[0], -1.0 * scale[1], 22.0 * scale[0],
              0.0 * scale[1], 12.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 3.0 * scale[1], -15.0 * scale[0],
              7.0 * scale[1], -13.0 * scale[0], 11.0 * scale[1])
    Curveto_r(2.0 * scale[0], 4.0 * scale[1], -8.0 * scale[0],
              7.0 * scale[1], -22.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 0.0 * scale[1], -36.0 * scale[0],
              4.0 * scale[1], -47.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 4.0 * scale[1], -7.0 * scale[0],
              0.0 * scale[1], 10.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(72.0 * scale[0], 285.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -20.0 * scale[1], -19.0 * scale[0], -
              40.0 * scale[1], -19.0 * scale[0], -115.0 * scale[1])
    Curveto_r(0.0 * scale[0], -100.0 * scale[1], 10.0 * scale[0], -
              120.0 * scale[1], 47.0 * scale[0], -100.0 * scale[1])
    Curveto_r(14.0 * scale[0], 7.0 * scale[1], 47.0 * scale[0],
              9.0 * scale[1], 92.0 * scale[0], 6.0 * scale[1])
    Curveto_r(88.0 * scale[0], -8.0 * scale[1], 109.0 * scale[0], -
              13.0 * scale[1], 183.0 * scale[0], -44.0 * scale[1])
    Curveto_r(46.0 * scale[0], -19.0 * scale[1], 80.0 * scale[0], -
              26.0 * scale[1], 145.0 * scale[0], -28.0 * scale[1])
    Lineto_r(85.0 * scale[0], -2.0 * scale[1])
    Lineto_r(-35.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-43.0 * scale[0], 22.0 * scale[1], -15.0 * scale[0],
              26.0 * scale[1], 37.0 * scale[0], 4.0 * scale[1])
    Curveto_r(45.0 * scale[0], -19.0 * scale[1], 53.0 *
              scale[0], -19.0 * scale[1], 53.0 * scale[0], 0.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], 12.0 * scale[0],
              15.0 * scale[1], 50.0 * scale[0], 15.0 * scale[1])
    Curveto_r(28.0 * scale[0], 0.0 * scale[1], 50.0 * scale[0],
              4.0 * scale[1], 50.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 22.0 * scale[0],
              9.0 * scale[1], 50.0 * scale[0], 8.0 * scale[1])
    Curveto_r(70.0 * scale[0], -1.0 * scale[1], 93.0 * scale[0],
              22.0 * scale[1], 87.0 * scale[0], 83.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 104.0 * scale[1], -20.0 * scale[0],
              124.0 * scale[1], -55.0 * scale[0], 134.0 * scale[1])
    Curveto_r(-26.0 * scale[0], 7.0 * scale[1], -36.0 * scale[0],
              5.0 * scale[1], -52.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -10.0 * scale[1], -20.0 *
              scale[0], -26.0 * scale[1], -20.0 * scale[0], -37.0 * scale[1])
    Curveto_r(0.0 * scale[0], -18.0 * scale[1], -16.0 * scale[0], -
              19.0 * scale[1], -69.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -40.0 * scale[0],
              7.0 * scale[1], -70.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-97.0 * scale[0], 10.0 * scale[1], -86.0 * scale[0],
              27.0 * scale[1], 14.0 * scale[0], 21.0 * scale[1])
    Lineto_r(90.0 * scale[0], -6.0 * scale[1])
    Lineto_r(-65.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-74.0 * scale[0], 15.0 * scale[1], -138.0 * scale[0],
              20.0 * scale[1], -160.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-30.0 * scale[0], -11.0 * scale[1], -90.0 *
              scale[0], -16.0 * scale[1], -90.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 8.0 * scale[0],
              11.0 * scale[1], 18.0 * scale[0], 14.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], -36.0 * scale[0],
              4.0 * scale[1], -101.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-103.0 * scale[0], -2.0 * scale[1], -120.0 *
              scale[0], -5.0 * scale[1], -138.0 * scale[0], -23.0 * scale[1])
    Lineto_r(-21.0 * scale[0], -20.0 * scale[1])
    Lineto_r(46.0 * scale[0], -19.0 * scale[1])
    Curveto_r(25.0 * scale[0], -11.0 * scale[1], 46.0 * scale[0], -
              23.0 * scale[1], 46.0 * scale[0], -27.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 10.0 * scale[0], -
              5.0 * scale[1], 23.0 * scale[0], -2.0 * scale[1])
    Curveto_r(16.0 * scale[0], 6.0 * scale[1], 19.0 * scale[0],
              4.0 * scale[1], 11.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -7.0 * scale[1], -21.0 * scale[0], -
              13.0 * scale[1], -33.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -1.0 * scale[1], -21.0 *
              scale[0], -3.0 * scale[1], -21.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 23.0 * scale[0], -
              17.0 * scale[1], 50.0 * scale[0], -34.0 * scale[1])
    Curveto_r(28.0 * scale[0], -17.0 * scale[1], 50.0 * scale[0], -
              32.0 * scale[1], 50.0 * scale[0], -34.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], -66.0 * scale[0],
              11.0 * scale[1], -78.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -15.0 * scale[0], -
              1.0 * scale[1], -22.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -12.0 * scale[1], -5.0 * scale[0], -
              15.0 * scale[1], 22.0 * scale[0], -19.0 * scale[1])
    Curveto_r(22.0 * scale[0], -2.0 * scale[1], 14.0 * scale[0], -
              4.0 * scale[1], -22.0 * scale[0], -5.0 * scale[1])
    Lineto_r(-55.0 * scale[0], -2.0 * scale[1])
    Lineto_r(-25.0 * scale[0], 51.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 28.0 * scale[1], -23.0 * scale[0],
              63.0 * scale[1], -22.0 * scale[0], 79.0 * scale[1])
    Curveto_r(2.0 * scale[0], 15.0 * scale[1], -2.0 * scale[0],
              31.0 * scale[1], -8.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -15.0 * scale[0],
              18.0 * scale[1], -20.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 30.0 * scale[1], -24.0 * scale[0],
              30.0 * scale[1], -48.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto_r(269.0 * scale[0], -73.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -18.0 * scale[0],
              1.0 * scale[1], -23.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 8.0 * scale[1], -4.0 * scale[0],
              9.0 * scale[1], 13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(13.0 * scale[0], -4.0 * scale[1], 18.0 * scale[0], -
              8.0 * scale[1], 10.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto_r(335.0 * scale[0], -14.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 15.0 *
              scale[0], -3.0 * scale[1], 21.0 * scale[0], 3.0 * scale[1])
    Curveto_r(11.0 * scale[0], 11.0 * scale[1], 73.0 * scale[0],
              3.0 * scale[1], 73.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -18.0 * scale[1], -20.0 * scale[0], -
              34.0 * scale[1], -34.0 * scale[0], -29.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -18.0 * scale[0],
              2.0 * scale[1], -21.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], 6.0 * scale[0], -
              11.0 * scale[1], 22.0 * scale[0], -11.0 * scale[1])
    Curveto_r(17.0 * scale[0], -1.0 * scale[1], 21.0 *
              scale[0], -3.0 * scale[1], 11.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -2.0 * scale[1], -18.0 *
              scale[0], -8.0 * scale[1], -18.0 * scale[0], -13.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 6.0 * scale[0], -
              7.0 * scale[1], 14.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 15.0 * scale[0], -
              4.0 * scale[1], 18.0 * scale[0], -25.0 * scale[1])
    Curveto_r(3.0 * scale[0], -23.0 * scale[1], 0.0 * scale[0], -
              32.0 * scale[1], -18.0 * scale[0], -40.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -7.0 * scale[1], -25.0 *
              scale[0], -6.0 * scale[1], -34.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 8.0 * scale[1], -29.0 * scale[0],
              15.0 * scale[1], -49.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-35.0 * scale[0], 1.0 * scale[1], -35.0 *
              scale[0], 1.0 * scale[1], 9.0 * scale[0], 8.0 * scale[1])
    Curveto_r(38.0 * scale[0], 6.0 * scale[1], 40.0 * scale[0],
              7.0 * scale[1], 13.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 1.0 * scale[1], -35.0 * scale[0],
              7.0 * scale[1], -38.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], -3.0 * scale[0],
              10.0 * scale[1], 2.0 * scale[0], 9.0 * scale[1])
    Curveto_r(13.0 * scale[0], -3.0 * scale[1], 63.0 * scale[0],
              13.0 * scale[1], 63.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 19.0 * scale[1], -33.0 * scale[0],
              49.0 * scale[1], -69.0 * scale[0], 61.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 7.0 * scale[1], -38.0 * scale[0],
              17.0 * scale[1], -35.0 * scale[0], 21.0 * scale[1])
    Curveto_r(4.0 * scale[0], 8.0 * scale[1], 47.0 * scale[0], -
              6.0 * scale[1], 70.0 * scale[0], -23.0 * scale[1])
    te.end_fill()
    Moveto_r(-316.0 * scale[0], -114.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], -12.0 * scale[0], -
              4.0 * scale[1], -26.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -23.0 * scale[0],
              4.0 * scale[1], -20.0 * scale[0], 9.0 * scale[1])
    Curveto_r(6.0 * scale[0], 8.0 * scale[1], 46.0 * scale[0],
              4.0 * scale[1], 46.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(163.0 * scale[0], -41.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -21.0 *
              scale[0], -2.0 * scale[1], -30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 3.0 * scale[1], -4.0 * scale[0],
              5.0 * scale[1], 12.0 * scale[0], 5.0 * scale[1])
    Curveto_r(17.0 * scale[0], 0.0 * scale[1], 24.0 * scale[0], -
              2.0 * scale[1], 18.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(700.0 * scale[0], 190.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 4.0 * scale[0], -
              10.0 * scale[1], 9.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              5.0 * scale[1], 16.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], -1.0 * scale[0],
              10.0 * scale[1], -9.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(160.0 * scale[0], 196.0 * scale[1], x, y)
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
    Moveto(190.0 * scale[0], 149.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -9.0 * scale[1], -12.0 *
              scale[0], -10.0 * scale[1], 2.0 * scale[0], -5.0 * scale[1])
    Curveto_r(10.0 * scale[0], 3.0 * scale[1], 20.0 * scale[0],
              1.0 * scale[1], 23.0 * scale[0], -4.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 21.0 * scale[0], -
              9.0 * scale[1], 40.0 * scale[0], -8.0 * scale[1])
    Curveto_r(31.0 * scale[0], 1.0 * scale[1], 32.0 * scale[0],
              3.0 * scale[1], 17.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 16.0 * scale[1], -62.0 * scale[0],
              18.0 * scale[1], -82.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(155.0 * scale[0], 50.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 0.0 *
              scale[0], -7.0 * scale[1], 8.0 * scale[0], -4.0 * scale[1])
    Curveto_r(16.0 * scale[0], 6.0 * scale[1], 69.0 * scale[0], -
              13.0 * scale[1], 78.0 * scale[0], -27.0 * scale[1])
    Curveto_r(3.0 * scale[0], -6.0 * scale[1], 35.0 * scale[0], -
              9.0 * scale[1], 70.0 * scale[0], -7.0 * scale[1])
    Lineto_r(64.0 * scale[0], 3.0 * scale[1])
    Lineto_r(-55.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-70.0 * scale[0], 21.0 * scale[1], -158.0 * scale[0],
              31.0 * scale[1], -165.0 * scale[0], 19.0 * scale[1])
    te.end_fill()
    Moveto(695.0 * scale[0], 20.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              10.0 * scale[1], 4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              5.0 * scale[1], 11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -2.0 * scale[0],
              10.0 * scale[1], -4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              4.0 * scale[1], -11.0 * scale[0], -10.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#77461a')
    te.end_fill()
    Moveto(175.0 * scale[0], 1394.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -2.0 * scale[1], -50.0 *
              scale[0], -6.0 * scale[1], -88.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-37.0 * scale[0], -4.0 * scale[1], -65.0 * scale[0], -
              11.0 * scale[1], -62.0 * scale[0], -16.0 * scale[1])
    Curveto_r(4.0 * scale[0], -5.0 * scale[1], 2.0 * scale[0], -
              9.0 * scale[1], -3.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              290.0 * scale[1], 1.0 * scale[0], -307.0 * scale[1])
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 41.0 * scale[0], -
              11.0 * scale[1], 84.0 * scale[0], -11.0 * scale[1])
    Lineto_r(78.0 * scale[0], 0.0 * scale[1])
    Lineto_r(-44.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 7.0 * scale[1], -49.0 * scale[0],
              11.0 * scale[1], -55.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -4.0 * scale[1], -8.0 *
              scale[0], -2.0 * scale[1], -1.0 * scale[0], 5.0 * scale[1])
    Curveto_r(11.0 * scale[0], 12.0 * scale[1], 102.0 * scale[0], -
              3.0 * scale[1], 119.0 * scale[0], -19.0 * scale[1])
    Curveto_r(13.0 * scale[0], -12.0 * scale[1], 36.0 *
              scale[0], -11.0 * scale[1], 36.0 * scale[0], 1.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -6.0 * scale[0],
              10.0 * scale[1], -12.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-27.0 * scale[0], 0.0 * scale[1], -98.0 * scale[0],
              36.0 * scale[1], -98.0 * scale[0], 49.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], -4.0 * scale[0],
              10.0 * scale[1], -12.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -11.0 * scale[1], -24.0 *
              scale[0], -10.0 * scale[1], -73.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 5.0 * scale[1], -23.0 * scale[0],
              10.0 * scale[1], -12.0 * scale[0], 10.0 * scale[1])
    Curveto_r(10.0 * scale[0], 1.0 * scale[1], 27.0 * scale[0], -
              4.0 * scale[1], 37.0 * scale[0], -9.0 * scale[1])
    Curveto_r(23.0 * scale[0], -12.0 * scale[1], 40.0 * scale[0],
              7.0 * scale[1], 19.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -10.0 * scale[0],
              9.0 * scale[1], -5.0 * scale[0], 9.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 3.0 * scale[0],
              6.0 * scale[1], -3.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 10.0 * scale[1], -9.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 21.0 * scale[1])
    Curveto_r(7.0 * scale[0], 4.0 * scale[1], 6.0 * scale[0],
              13.0 * scale[1], -2.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 12.0 * scale[1], -12.0 * scale[0],
              25.0 * scale[1], -13.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 16.0 * scale[1], -17.0 * scale[0],
              21.0 * scale[1], -25.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -10.0 * scale[1], -8.0 *
              scale[0], -6.0 * scale[1], -6.0 * scale[0], 15.0 * scale[1])
    Curveto_r(2.0 * scale[0], 17.0 * scale[1], 8.0 * scale[0],
              30.0 * scale[1], 15.0 * scale[0], 30.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              3.0 * scale[1], 11.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], 0.0 * scale[0],
              14.0 * scale[1], 0.0 * scale[0], 23.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -3.0 * scale[0],
              14.0 * scale[1], -15.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -16.0 * scale[1], -32.0 *
              scale[0], -5.0 * scale[1], -14.0 * scale[0], 12.0 * scale[1])
    Curveto_r(19.0 * scale[0], 18.0 * scale[1], 79.0 * scale[0],
              20.0 * scale[1], 79.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -5.0 * scale[0], -
              15.0 * scale[1], -12.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-24.0 * scale[0], -8.0 * scale[1], 8.0 * scale[0], -
              14.0 * scale[1], 37.0 * scale[0], -7.0 * scale[1])
    Curveto_r(24.0 * scale[0], 5.0 * scale[1], 25.0 * scale[0],
              7.0 * scale[1], 8.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -23.0 * scale[0],
              7.0 * scale[1], -23.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], 9.0 * scale[0],
              15.0 * scale[1], 23.0 * scale[0], 16.0 * scale[1])
    Curveto_r(21.0 * scale[0], 0.0 * scale[1], 21.0 * scale[0],
              1.0 * scale[1], 2.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 7.0 * scale[1], -16.0 * scale[0],
              9.0 * scale[1], 10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(17.0 * scale[0], 1.0 * scale[1], 39.0 * scale[0],
              5.0 * scale[1], 50.0 * scale[0], 10.0 * scale[1])
    Curveto_r(20.0 * scale[0], 9.0 * scale[1], 9.0 * scale[0],
              10.0 * scale[1], -30.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(250.0 * scale[0], 1390.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 11.0 * scale[0], -
              8.0 * scale[1], 28.0 * scale[0], -4.0 * scale[1])
    Curveto_r(39.0 * scale[0], 10.0 * scale[1], 40.0 * scale[0],
              14.0 * scale[1], 4.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 0.0 * scale[1], -32.0 * scale[0], -
              5.0 * scale[1], -32.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(332.0 * scale[0], 1392.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -6.0 * scale[0], -
              12.0 * scale[1], 12.0 * scale[0], -20.0 * scale[1])
    Curveto_r(29.0 * scale[0], -13.0 * scale[1], 41.0 *
              scale[0], -5.0 * scale[1], 21.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 16.0 * scale[1], -16.0 * scale[0],
              16.0 * scale[1], -33.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(393.0 * scale[0], 1393.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(478.0 * scale[0], 1393.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(527.0 * scale[0], 1389.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(14.0 * scale[0], -13.0 * scale[1], 56.0 * scale[0], -
              22.0 * scale[1], 49.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 7.0 * scale[1], 14.0 * scale[0],
              12.0 * scale[1], 51.0 * scale[0], 15.0 * scale[1])
    Curveto_r(41.0 * scale[0], 3.0 * scale[1], 34.0 * scale[0],
              4.0 * scale[1], -25.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-45.0 * scale[0], 0.0 * scale[1], -79.0 *
              scale[0], -3.0 * scale[1], -75.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(734.0 * scale[0], 1382.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 21.0 * scale[0], -
              13.0 * scale[1], 40.0 * scale[0], -16.0 * scale[1])
    Curveto_r(19.0 * scale[0], -4.0 * scale[1], 48.0 * scale[0], -
              13.0 * scale[1], 64.0 * scale[0], -22.0 * scale[1])
    Curveto_r(17.0 * scale[0], -8.0 * scale[1], 44.0 * scale[0], -
              16.0 * scale[1], 61.0 * scale[0], -17.0 * scale[1])
    Curveto_r(23.0 * scale[0], -1.0 * scale[1], 28.0 * scale[0], -
              5.0 * scale[1], 19.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -7.0 * scale[1], -12.0 * scale[0], -
              35.0 * scale[1], -10.0 * scale[0], -94.0 * scale[1])
    Curveto_r(2.0 * scale[0], -46.0 * scale[1], -1.0 * scale[0], -
              88.0 * scale[1], -6.0 * scale[0], -93.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -5.0 * scale[1], -21.0 * scale[0], -
              11.0 * scale[1], -36.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -3.0 * scale[1], -30.0 * scale[0],
              3.0 * scale[1], -40.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 21.0 * scale[1], -14.0 * scale[0],
              22.0 * scale[1], -19.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -10.0 * scale[1], -3.0 *
              scale[0], -15.0 * scale[1], 3.0 * scale[0], -11.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 10.0 * scale[0], -
              1.0 * scale[1], 10.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 9.0 * scale[0], -
              19.0 * scale[1], 20.0 * scale[0], -22.0 * scale[1])
    Curveto_r(11.0 * scale[0], -3.0 * scale[1], 17.0 * scale[0], -
              9.0 * scale[1], 14.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 0.0 *
              scale[0], -9.0 * scale[1], 5.0 * scale[0], -9.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0], -
              4.0 * scale[1], 11.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -21.0 * scale[0], -
              8.0 * scale[1], -47.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-40.0 * scale[0], 3.0 * scale[1], -44.0 * scale[0],
              2.0 * scale[1], -29.0 * scale[0], -9.0 * scale[1])
    Curveto_r(16.0 * scale[0], -13.0 * scale[1], 16.0 * scale[0], -
              14.0 * scale[1], -6.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -4.0 * scale[1], -20.0 *
              scale[0], -4.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(15.0 * scale[0], 0.0 * scale[1], 27.0 * scale[0],
              4.0 * scale[1], 27.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              9.0 * scale[1], 9.0 * scale[0], -1.0 * scale[1])
    Curveto_r(5.0 * scale[0], -8.0 * scale[1], 25.0 * scale[0], -
              12.0 * scale[1], 55.0 * scale[0], -11.0 * scale[1])
    Curveto_r(36.0 * scale[0], 2.0 * scale[1], 50.0 * scale[0],
              8.0 * scale[1], 58.0 * scale[0], 23.0 * scale[1])
    Curveto_r(7.0 * scale[0], 12.0 * scale[1], 12.0 * scale[0],
              79.0 * scale[1], 12.0 * scale[0], 158.0 * scale[1])
    Curveto_r(1.0 * scale[0], 173.0 * scale[1], 3.0 * scale[0],
              171.0 * scale[1], -130.0 * scale[0], 176.0 * scale[1])
    Curveto_r(-63.0 * scale[0], 3.0 * scale[1], -94.0 * scale[0],
              1.0 * scale[1], -90.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto_r(170.0 * scale[0], -20.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -11.0 * scale[1], -60.0 *
              scale[0], -9.0 * scale[1], -70.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 4.0 * scale[1], 9.0 * scale[0],
              7.0 * scale[1], 29.0 * scale[0], 7.0 * scale[1])
    Curveto_r(20.0 * scale[0], 0.0 * scale[1], 38.0 * scale[0], -
              4.0 * scale[1], 41.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto_r(-7.0 * scale[0], -268.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 17.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(590.0 * scale[0], 1371.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 19.0 * scale[0], -
              25.0 * scale[1], 25.0 * scale[0], -20.0 * scale[1])
    Curveto_r(1.0 * scale[0], 2.0 * scale[1], -3.0 * scale[0],
              10.0 * scale[1], -11.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 7.0 * scale[1], -14.0 * scale[0],
              8.0 * scale[1], -14.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(414.0 * scale[0], 1361.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -11.0 * scale[1], 46.0 * scale[0], -
              35.0 * scale[1], 46.0 * scale[0], -28.0 * scale[1])
    Curveto_r(0.0 * scale[0], 3.0 * scale[1], -12.0 * scale[0],
              12.0 * scale[1], -26.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 9.0 * scale[1], -23.0 * scale[0],
              12.0 * scale[1], -20.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(668.0 * scale[0], 1333.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(810.0 * scale[0], 1314.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 3.0 * scale[0], -
              15.0 * scale[1], 18.0 * scale[0], -3.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 19.0 * scale[0],
              15.0 * scale[1], 21.0 * scale[0], 16.0 * scale[1])
    Curveto_r(2.0 * scale[0], 2.0 * scale[1], -5.0 * scale[0],
              3.0 * scale[1], -17.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -22.0 * scale[0], -
              6.0 * scale[1], -22.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(170.0 * scale[0], 1311.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -26.0 * scale[1], 14.0 * scale[0], -
              41.0 * scale[1], 39.0 * scale[0], -40.0 * scale[1])
    Lineto_r(26.0 * scale[0], 0.0 * scale[1])
    Lineto_r(-24.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 6.0 * scale[1], -21.0 * scale[0],
              15.0 * scale[1], -17.0 * scale[0], 24.0 * scale[1])
    Curveto_r(3.0 * scale[0], 9.0 * scale[1], 0.0 * scale[0],
              15.0 * scale[1], -9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              4.0 * scale[1], -15.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(782.0 * scale[0], 1288.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-17.0 * scale[0], -17.0 * scale[1], -15.0 *
              scale[0], -29.0 * scale[1], 9.0 * scale[0], -58.0 * scale[1])
    Lineto_r(20.0 * scale[0], -25.0 * scale[1])
    Lineto_r(-16.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 26.0 * scale[1], -14.0 * scale[0],
              37.0 * scale[1], -4.0 * scale[0], 48.0 * scale[1])
    Curveto_r(14.0 * scale[0], 17.0 * scale[1], 8.0 * scale[0],
              19.0 * scale[1], -9.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(268.0 * scale[0], 1263.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(197.0 * scale[0], 1213.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 33.0 *
              scale[0], -6.0 * scale[1], 80.0 * scale[0], -4.0 * scale[1])
    Curveto_r(83.0 * scale[0], 3.0 * scale[1], 86.0 * scale[0],
              3.0 * scale[1], 80.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -11.0 * scale[1], -1.0 *
              scale[0], -24.0 * scale[1], 4.0 * scale[0], -27.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 9.0 * scale[0],
              9.0 * scale[1], 9.0 * scale[0], 25.0 * scale[1])
    Lineto_r(0.0 * scale[0], 31.0 * scale[1])
    Lineto_r(-84.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-47.0 * scale[0], 0.0 * scale[1], -87.0 *
              scale[0], -3.0 * scale[1], -89.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(193.0 * scale[0], 1168.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(11.0 * scale[0], -10.0 * scale[1], 29.0 * scale[0], -
              18.0 * scale[1], 41.0 * scale[0], -17.0 * scale[1])
    Curveto_r(17.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              3.0 * scale[1], -9.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 6.0 * scale[1], -35.0 * scale[0],
              13.0 * scale[1], -40.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0], -
              2.0 * scale[1], 8.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(591.0 * scale[0], 1154.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(173.0 * scale[0], 1141.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -14.0 * scale[1], 3.0 * scale[0], -
              18.0 * scale[1], 13.0 * scale[0], -14.0 * scale[1])
    Curveto_r(11.0 * scale[0], 4.0 * scale[1], 12.0 * scale[0],
              9.0 * scale[1], 3.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 18.0 * scale[1], -14.0 * scale[0],
              18.0 * scale[1], -16.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(270.0 * scale[0], 1146.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 15.0 * scale[0], -
              6.0 * scale[1], 34.0 * scale[0], -8.0 * scale[1])
    Curveto_r(19.0 * scale[0], -2.0 * scale[1], 32.0 * scale[0],
              0.0 * scale[1], 30.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 8.0 * scale[1], -64.0 * scale[0],
              12.0 * scale[1], -64.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(145.0 * scale[0], 1110.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              10.0 * scale[1], 10.0 * scale[0], -10.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              5.0 * scale[1], 10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -8.0 * scale[0],
              10.0 * scale[1], -10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              4.0 * scale[1], -10.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(180.0 * scale[0], 1110.0 * scale[1], x, y)
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
    Moveto(386.0 * scale[0], 1105.0 * scale[1], x, y)
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
    Moveto(545.0 * scale[0], 1090.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(350.0 * scale[0], 1050.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 12.0 * scale[0], -
              10.0 * scale[1], 28.0 * scale[0], -9.0 * scale[1])
    Curveto_r(24.0 * scale[0], 0.0 * scale[1], 25.0 * scale[0],
              1.0 * scale[1], 7.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-27.0 * scale[0], 12.0 * scale[1], -35.0 * scale[0],
              12.0 * scale[1], -35.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(648.0 * scale[0], 1033.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(782.0 * scale[0], 1004.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -8.0 * scale[1], -21.0 * scale[0], -
              25.0 * scale[1], -21.0 * scale[0], -37.0 * scale[1])
    Curveto_r(1.0 * scale[0], -20.0 * scale[1], 2.0 * scale[0], -
              21.0 * scale[1], 6.0 * scale[0], -2.0 * scale[1])
    Curveto_r(5.0 * scale[0], 21.0 * scale[1], 24.0 * scale[0],
              35.0 * scale[1], 58.0 * scale[0], 47.0 * scale[1])
    Curveto_r(20.0 * scale[0], 6.0 * scale[1], 20.0 * scale[0],
              6.0 * scale[1], 0.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 1.0 * scale[1], -31.0 * scale[0], -
              6.0 * scale[1], -43.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(951.0 * scale[0], 954.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(911.0 * scale[0], 947.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -10.0 * scale[1], -7.0 *
              scale[0], -14.0 * scale[1], 4.0 * scale[0], -14.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0],
              6.0 * scale[1], 19.0 * scale[0], 14.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              13.0 * scale[1], -3.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0], -
              6.0 * scale[1], -20.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(762.0 * scale[0], 920.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              30.0 * scale[1], 6.0 * scale[0], -36.0 * scale[1])
    Curveto_r(10.0 * scale[0], -16.0 * scale[1], 52.0 * scale[0], -
              36.0 * scale[1], 52.0 * scale[0], -26.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -11.0 * scale[0],
              14.0 * scale[1], -24.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 7.0 * scale[1], -26.0 * scale[0],
              21.0 * scale[1], -29.0 * scale[0], 39.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 26.0 * scale[1], -4.0 * scale[0],
              26.0 * scale[1], -5.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(848.0 * scale[0], 912.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -11.0 * scale[1], -2.0 *
              scale[0], -26.0 * scale[1], 3.0 * scale[0], -33.0 * scale[1])
    Curveto_r(5.0 * scale[0], -8.0 * scale[1], 3.0 * scale[0], -
              16.0 * scale[1], -4.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -4.0 * scale[1], -3.0 *
              scale[0], -6.0 * scale[1], 9.0 * scale[0], -6.0 * scale[1])
    Curveto_r(22.0 * scale[0], 2.0 * scale[1], 25.0 * scale[0],
              30.0 * scale[1], 6.0 * scale[0], 63.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 16.0 * scale[1], -10.0 * scale[0],
              15.0 * scale[1], -14.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(900.0 * scale[0], 844.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -4.0 * scale[0], -
              12.0 * scale[1], -10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0],
              2.0 * scale[1], -10.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -22.0 * scale[1], 18.0 *
              scale[0], -19.0 * scale[1], 28.0 * scale[0], 4.0 * scale[1])
    Curveto_r(7.0 * scale[0], 15.0 * scale[1], 8.0 * scale[0],
              25.0 * scale[1], 2.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              7.0 * scale[1], -10.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(687.0 * scale[0], 843.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -3.0 * scale[1], -7.0 * scale[0], -
              11.0 * scale[1], -7.0 * scale[0], -17.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 5.0 * scale[0], -
              4.0 * scale[1], 10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(8.0 * scale[0], 13.0 * scale[1], 11.0 * scale[0],
              13.0 * scale[1], 22.0 * scale[0], -2.0 * scale[1])
    Curveto_r(11.0 * scale[0], -14.0 * scale[1], 15.0 *
              scale[0], -15.0 * scale[1], 25.0 * scale[0], -3.0 * scale[1])
    Curveto_r(8.0 * scale[0], 9.0 * scale[1], 9.0 * scale[0],
              16.0 * scale[1], 3.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0],
              1.0 * scale[1], -10.0 * scale[0], -6.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], -3.0 * scale[0], -
              10.0 * scale[1], -12.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 14.0 * scale[1], -22.0 * scale[0],
              15.0 * scale[1], -31.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(940.0 * scale[0], 829.0 * scale[1], x, y)
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
    Moveto(747.0 * scale[0], 799.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(860.0 * scale[0], 779.0 * scale[1], x, y)
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
    Moveto(170.0 * scale[0], 759.0 * scale[1], x, y)
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
    Moveto(824.0 * scale[0], 755.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(28.0 * scale[0], -15.0 * scale[1], 55.0 * scale[0], -
              42.0 * scale[1], 56.0 * scale[0], -57.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -13.0 * scale[0], -
              8.0 * scale[1], -30.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -30.0 * scale[0],
              5.0 * scale[1], -30.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -3.0 * scale[0],
              8.0 * scale[1], -7.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], -13.0 *
              scale[0], -1.0 * scale[1], -22.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 8.0 * scale[1], -9.0 * scale[0],
              4.0 * scale[1], 3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(24.0 * scale[0], -28.0 * scale[1], 96.0 *
              scale[0], -32.0 * scale[1], 96.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 20.0 * scale[1], -58.0 * scale[0],
              73.0 * scale[1], -79.0 * scale[0], 73.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -3.0 * scale[0], -
              7.0 * scale[1], 13.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(880.0 * scale[0], 766.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 7.0 * scale[0], -
              7.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 12.0 *
              scale[0], -2.0 * scale[1], 9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], -25.0 * scale[0],
              14.0 * scale[1], -25.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(185.0 * scale[0], 740.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              10.0 * scale[1], 4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0], -
              8.0 * scale[1], 14.0 * scale[0], -17.0 * scale[1])
    Curveto_r(3.0 * scale[0], -11.0 * scale[1], 5.0 *
              scale[0], -7.0 * scale[1], 6.0 * scale[0], 10.0 * scale[1])
    Curveto_r(1.0 * scale[0], 27.0 * scale[1], -12.0 * scale[0],
              36.0 * scale[1], -24.0 * scale[0], 17.0 * scale[1])
    te.end_fill()
    Moveto(900.0 * scale[0], 689.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 4.0 * scale[0], -
              18.0 * scale[1], 9.0 * scale[0], -14.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 15.0 * scale[0], -
              3.0 * scale[1], 21.0 * scale[0], -12.0 * scale[1])
    Curveto_r(11.0 * scale[0], -17.0 * scale[1], 11.0 *
              scale[0], -17.0 * scale[1], 6.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -1.0 * scale[0],
              17.0 * scale[1], 4.0 * scale[0], 17.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              6.0 * scale[1], 11.0 * scale[0], -12.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], 4.0 *
              scale[0], -4.0 * scale[1], 8.0 * scale[0], 7.0 * scale[1])
    Curveto_r(10.0 * scale[0], 24.0 * scale[1], 2.0 * scale[0],
              43.0 * scale[1], -10.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -11.0 * scale[1], -11.0 *
              scale[0], -11.0 * scale[1], -21.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 18.0 * scale[1], -28.0 * scale[0],
              15.0 * scale[1], -28.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(57.0 * scale[0], 685.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], 9.0 * scale[0], -
              12.0 * scale[1], 14.0 * scale[0], -9.0 * scale[1])
    Curveto_r(12.0 * scale[0], 7.0 * scale[1], 11.0 * scale[0],
              11.0 * scale[1], -5.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 4.0 * scale[1], -13.0 * scale[0],
              1.0 * scale[1], -9.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(110.0 * scale[0], 636.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              17.0 * scale[1], 9.0 * scale[0], -20.0 * scale[1])
    Curveto_r(5.0 * scale[0], -4.0 * scale[1], 7.0 * scale[0],
              3.0 * scale[1], 4.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 23.0 * scale[1], -13.0 * scale[0],
              26.0 * scale[1], -13.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(140.0 * scale[0], 642.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -21.0 * scale[1], 23.0 * scale[0], -
              61.0 * scale[1], 31.0 * scale[0], -56.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 9.0 * scale[0],
              10.0 * scale[1], 9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -4.0 * scale[0],
              7.0 * scale[1], -10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -11.0 *
              scale[0], -1.0 * scale[1], -11.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 26.0 * scale[1], -4.0 * scale[0],
              30.0 * scale[1], -11.0 * scale[0], 37.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 4.0 * scale[1], -8.0 * scale[0],
              2.0 * scale[1], -8.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(30.0 * scale[0], 631.0 * scale[1], x, y)
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
    Moveto(41.0 * scale[0], 584.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(101.0 * scale[0], 564.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(41.0 * scale[0], 545.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -21.0 * scale[1], 16.0 * scale[0], -
              45.0 * scale[1], 31.0 * scale[0], -45.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              10.0 * scale[1], 18.0 * scale[0], 23.0 * scale[1])
    Curveto_r(10.0 * scale[0], 20.0 * scale[1], 10.0 * scale[0],
              20.0 * scale[1], -3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -18.0 * scale[1], -27.0 *
              scale[0], -11.0 * scale[1], -40.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 11.0 * scale[1], -6.0 * scale[0],
              9.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(150.0 * scale[0], 534.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -40.0 * scale[1], 6.0 * scale[0], -
              44.0 * scale[1], 41.0 * scale[0], -32.0 * scale[1])
    Curveto_r(35.0 * scale[0], 12.0 * scale[1], 30.0 * scale[0],
              27.0 * scale[1], -7.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -3.0 * scale[1], -25.0 *
              scale[0], -1.0 * scale[1], -21.0 * scale[0], 5.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], 2.0 * scale[0],
              15.0 * scale[1], -4.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 11.0 * scale[1], -9.0 * scale[0],
              7.0 * scale[1], -9.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(130.0 * scale[0], 541.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -4.0 * scale[0], -
              9.0 * scale[1], -10.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0], -
              2.0 * scale[1], -10.0 * scale[0], -12.0 * scale[1])
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 1.0 * scale[0], -
              16.0 * scale[1], 17.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 9.0 * scale[1], 14.0 * scale[0],
              20.0 * scale[1], 10.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 4.0 * scale[1], -7.0 * scale[0],
              2.0 * scale[1], -7.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(37.0 * scale[0], 353.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -3.0 * scale[1], -16.0 * scale[0], -
              11.0 * scale[1], -14.0 * scale[0], -18.0 * scale[1])
    Curveto_r(3.0 * scale[0], -7.0 * scale[1], 1.0 * scale[0], -
              17.0 * scale[1], -4.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -11.0 * scale[1], -13.0 * scale[0], -
              250.0 * scale[1], -3.0 * scale[0], -276.0 * scale[1])
    Curveto_r(9.0 * scale[0], -24.0 * scale[1], 54.0 * scale[0], -
              34.0 * scale[1], 159.0 * scale[0], -35.0 * scale[1])
    Lineto_r(90.0 * scale[0], -2.0 * scale[1])
    Lineto_r(-80.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-97.0 * scale[0], 29.0 * scale[1], -101.0 * scale[0],
              30.0 * scale[1], -84.0 * scale[0], 8.0 * scale[1])
    Curveto_r(13.0 * scale[0], -16.0 * scale[1], 12.0 *
              scale[0], -17.0 * scale[1], -3.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 10.0 * scale[1], -17.0 * scale[0],
              10.0 * scale[1], -21.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -6.0 *
              scale[0], -8.0 * scale[1], -6.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 18.0 * scale[1], 26.0 * scale[0],
              36.0 * scale[1], 54.0 * scale[0], 36.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 25.0 * scale[0],
              5.0 * scale[1], 25.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -11.0 * scale[0],
              7.0 * scale[1], -27.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-45.0 * scale[0], -13.0 * scale[1], -93.0 *
              scale[0], -13.0 * scale[1], -85.0 * scale[0], -1.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 5.0 * scale[0],
              19.0 * scale[1], 4.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 10.0 * scale[1], 1.0 * scale[0],
              25.0 * scale[1], 7.0 * scale[0], 35.0 * scale[1])
    Curveto_r(5.0 * scale[0], 11.0 * scale[1], 6.0 * scale[0],
              44.0 * scale[1], 2.0 * scale[0], 80.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 34.0 * scale[1], -4.0 * scale[0],
              60.0 * scale[1], -1.0 * scale[0], 58.0 * scale[1])
    Curveto_r(11.0 * scale[0], -7.0 * scale[1], 39.0 * scale[0],
              32.0 * scale[1], 30.0 * scale[0], 41.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 5.0 * scale[1], 15.0 * scale[0],
              8.0 * scale[1], 45.0 * scale[0], 7.0 * scale[1])
    Curveto_r(57.0 * scale[0], -1.0 * scale[1], 72.0 * scale[0],
              9.0 * scale[1], 33.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-28.0 * scale[0], 9.0 * scale[1], -96.0 * scale[0],
              13.0 * scale[1], -121.0 * scale[0], 8.0 * scale[1])
    te.end_fill()
    Moveto(178.0 * scale[0], 353.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(17.0 * scale[0], -2.0 * scale[1], 47.0 *
              scale[0], -2.0 * scale[1], 65.0 * scale[0], 0.0 * scale[1])
    Curveto_r(17.0 * scale[0], 2.0 * scale[1], 3.0 * scale[0],
              4.0 * scale[1], -33.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-36.0 * scale[0], 0.0 * scale[1], -50.0 *
              scale[0], -2.0 * scale[1], -32.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(568.0 * scale[0], 343.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(720.0 * scale[0], 338.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(14.0 * scale[0], -5.0 * scale[1], 34.0 * scale[0], -
              15.0 * scale[1], 45.0 * scale[0], -21.0 * scale[1])
    Curveto_r(11.0 * scale[0], -6.0 * scale[1], 34.0 * scale[0], -
              14.0 * scale[1], 50.0 * scale[0], -18.0 * scale[1])
    Lineto_r(30.0 * scale[0], -7.0 * scale[1])
    Lineto_r(-32.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -1.0 * scale[1], -34.0 *
              scale[0], -5.0 * scale[1], -38.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 6.0 * scale[0], -
              8.0 * scale[1], 21.0 * scale[0], -5.0 * scale[1])
    Curveto_r(15.0 * scale[0], 3.0 * scale[1], 40.0 * scale[0],
              2.0 * scale[1], 55.0 * scale[0], -1.0 * scale[1])
    Curveto_r(25.0 * scale[0], -6.0 * scale[1], 29.0 * scale[0], -
              12.0 * scale[1], 29.0 * scale[0], -39.0 * scale[1])
    Curveto_r(0.0 * scale[0], -18.0 * scale[1], 5.0 * scale[0], -
              37.0 * scale[1], 10.0 * scale[0], -42.0 * scale[1])
    Curveto_r(15.0 * scale[0], -15.0 * scale[1], 17.0 * scale[0], -
              107.0 * scale[1], 2.0 * scale[0], -112.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -2.0 * scale[1], -12.0 * scale[0], -
              7.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], 38.0 * scale[0], -
              19.0 * scale[1], 44.0 * scale[0], -9.0 * scale[1])
    Curveto_r(2.0 * scale[0], 5.0 * scale[1], 3.0 * scale[0],
              4.0 * scale[1], 2.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -7.0 * scale[1], -9.0 * scale[0], -
              12.0 * scale[1], -15.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 2.0 * scale[1], -11.0 * scale[0], -
              2.0 * scale[1], -11.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -26.0 * scale[0], -
              11.0 * scale[1], -57.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-46.0 * scale[0], -1.0 * scale[1], -51.0 *
              scale[0], -2.0 * scale[1], -23.0 * scale[0], -7.0 * scale[1])
    Curveto_r(34.0 * scale[0], -5.0 * scale[1], 34.0 * scale[0], -
              5.0 * scale[1], -15.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-43.0 * scale[0], -6.0 * scale[1], -38.0 *
              scale[0], -7.0 * scale[1], 30.0 * scale[0], -6.0 * scale[1])
    Curveto_r(115.0 * scale[0], 2.0 * scale[1], 118.0 * scale[0],
              6.0 * scale[1], 116.0 * scale[0], 166.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 178.0 * scale[1], 0.0 * scale[0],
              170.0 * scale[1], -36.0 * scale[0], 176.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 3.0 * scale[1], -43.0 * scale[0],
              3.0 * scale[1], -60.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -3.0 * scale[1], -34.0 *
              scale[0], -5.0 * scale[1], -40.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -1.0 * scale[1], 1.0 * scale[0], -
              6.0 * scale[1], 14.0 * scale[0], -11.0 * scale[1])
    Curveto_r(47.0 * scale[0], -19.0 * scale[1], 14.0 *
              scale[0], -18.0 * scale[1], -48.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-66.0 * scale[0], 21.0 * scale[1], -103.0 * scale[0],
              26.0 * scale[1], -61.0 * scale[0], 8.0 * scale[1])
    te.end_fill()
    Moveto_r(180.0 * scale[0], -28.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(18.0 * scale[0], -12.0 * scale[1], 2.0 * scale[0], -
              12.0 * scale[1], -25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              9.0 * scale[1], -5.0 * scale[0], 9.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 22.0 * scale[0], -
              4.0 * scale[1], 30.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(657.0 * scale[0], 309.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(120.0 * scale[0], 286.0 * scale[1], x, y)
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
    Moveto(723.0 * scale[0], 283.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(618.0 * scale[0], 243.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(695.0 * scale[0], 236.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(28.0 * scale[0], -7.0 * scale[1], 56.0 * scale[0], -
              16.0 * scale[1], 63.0 * scale[0], -20.0 * scale[1])
    Curveto_r(7.0 * scale[0], -4.0 * scale[1], 12.0 *
              scale[0], -3.0 * scale[1], 12.0 * scale[0], 2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], -77.0 * scale[0],
              33.0 * scale[1], -107.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 0.0 * scale[1], 5.0 * scale[0], -
              6.0 * scale[1], 32.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(637.0 * scale[0], 209.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(168.0 * scale[0], 168.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -5.0 * scale[1], 16.0 * scale[0], -
              8.0 * scale[1], 23.0 * scale[0], -6.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 3.0 * scale[0],
              7.0 * scale[1], -10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 4.0 * scale[1], -21.0 * scale[0],
              3.0 * scale[1], -13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(695.0 * scale[0], 170.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -7.0 * scale[1], 65.0 *
              scale[0], -1.0 * scale[1], 65.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 3.0 * scale[1], -15.0 * scale[0],
              4.0 * scale[1], -34.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -1.0 * scale[1], -33.0 *
              scale[0], -5.0 * scale[1], -31.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(285.0 * scale[0], 50.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(11.0 * scale[0], -5.0 * scale[1], 27.0 *
              scale[0], -9.0 * scale[1], 35.0 * scale[0], -9.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0],
              4.0 * scale[1], -5.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 5.0 * scale[1], -27.0 * scale[0],
              9.0 * scale[1], -35.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -8.0 *
              scale[0], -4.0 * scale[1], 5.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(867.0 * scale[0], 49.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(350.0 * scale[0], 30.0 * scale[1], x, y)
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
    Moveto(586.0 * scale[0], 15.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(10.0 * scale[0], -8.0 * scale[1], 28.0 * scale[0], -
              14.0 * scale[1], 39.0 * scale[0], -14.0 * scale[1])
    Curveto_r(18.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-34.0 * scale[0], 20.0 * scale[1], -60.0 * scale[0],
              20.0 * scale[1], -34.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(390.0 * scale[0], 9.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 9.0 * scale[0], -
              9.0 * scale[1], 20.0 * scale[0], -9.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0],
              2.0 * scale[1], 20.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 2.0 * scale[1], -9.0 * scale[0],
              6.0 * scale[1], -20.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 3.0 * scale[1], -20.0 * scale[0],
              1.0 * scale[1], -20.0 * scale[0], -4.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#e0e5e5')
    te.end_fill()
    Moveto(542.0 * scale[0], 1346.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-18.0 * scale[0], -13.0 * scale[1], -30.0 *
              scale[0], -26.0 * scale[1], -25.0 * scale[0], -28.0 * scale[1])
    Curveto_r(4.0 * scale[0], -2.0 * scale[1], 21.0 * scale[0],
              8.0 * scale[1], 38.0 * scale[0], 24.0 * scale[1])
    Curveto_r(36.0 * scale[0], 34.0 * scale[1], 31.0 * scale[0],
              35.0 * scale[1], -13.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(80.0 * scale[0], 1285.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -14.0 * scale[1], -21.0 *
              scale[0], -25.0 * scale[1], -17.0 * scale[0], -25.0 * scale[1])
    Curveto_r(3.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              10.0 * scale[1], 26.0 * scale[0], 21.0 * scale[1])
    Curveto_r(14.0 * scale[0], 16.0 * scale[1], 28.0 * scale[0],
              20.0 * scale[1], 50.0 * scale[0], 17.0 * scale[1])
    Curveto_r(16.0 * scale[0], -2.0 * scale[1], 28.0 *
              scale[0], -1.0 * scale[1], 25.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 17.0 * scale[1], -61.0 * scale[0],
              7.0 * scale[1], -84.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(398.0 * scale[0], 1303.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -2.0 * scale[1], -18.0 *
              scale[0], -9.0 * scale[1], -18.0 * scale[0], -14.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 8.0 * scale[0], -
              5.0 * scale[1], 20.0 * scale[0], 1.0 * scale[1])
    Curveto_r(11.0 * scale[0], 6.0 * scale[1], 20.0 * scale[0],
              13.0 * scale[1], 20.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              4.0 * scale[1], -2.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -1.0 * scale[1], -11.0 *
              scale[0], -3.0 * scale[1], -20.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(810.0 * scale[0], 1285.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -14.0 * scale[1], -19.0 *
              scale[0], -25.0 * scale[1], -14.0 * scale[0], -25.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              9.0 * scale[1], 21.0 * scale[0], 19.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 27.0 * scale[0],
              21.0 * scale[1], 50.0 * scale[0], 24.0 * scale[1])
    Lineto_r(38.0 * scale[0], 4.0 * scale[1])
    Lineto_r(-36.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-26.0 * scale[0], 2.0 * scale[1], -42.0 * scale[0], -
              4.0 * scale[1], -59.0 * scale[0], -23.0 * scale[1])
    te.end_fill()
    Moveto(435.0 * scale[0], 1280.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(511.0 * scale[0], 1287.0 * scale[1], x, y)
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
    Moveto(399.0 * scale[0], 1253.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -21.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(440.0 * scale[0], 1240.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-28.0 * scale[0], -28.0 * scale[1], -34.0 *
              scale[0], -64.0 * scale[1], -17.0 * scale[0], -99.0 * scale[1])
    Curveto_r(11.0 * scale[0], -22.0 * scale[1], 12.0 *
              scale[0], -33.0 * scale[1], 3.0 * scale[0], -42.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -8.0 * scale[1], -2.0 *
              scale[0], -6.0 * scale[1], 10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(24.0 * scale[0], 20.0 * scale[1], 54.0 * scale[0],
              23.0 * scale[1], 54.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], 10.0 * scale[0], -
              2.0 * scale[1], 22.0 * scale[0], 10.0 * scale[1])
    Curveto_r(19.0 * scale[0], 18.0 * scale[1], 21.0 * scale[0],
              26.0 * scale[1], 11.0 * scale[0], 41.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 13.0 * scale[1], -8.0 * scale[0],
              22.0 * scale[1], -1.0 * scale[0], 29.0 * scale[1])
    Curveto_r(14.0 * scale[0], 14.0 * scale[1], -21.0 * scale[0],
              72.0 * scale[1], -44.0 * scale[0], 72.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 0.0 * scale[1], -27.0 * scale[0], -
              9.0 * scale[1], -38.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(70.0 * scale[0], 1246.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 9.0 * scale[0], -
              6.0 * scale[1], 20.0 * scale[0], -9.0 * scale[1])
    Curveto_r(11.0 * scale[0], -3.0 * scale[1], 18.0 *
              scale[0], -1.0 * scale[1], 14.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 9.0 * scale[1], -34.0 * scale[0],
              13.0 * scale[1], -34.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(810.0 * scale[0], 1246.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 7.0 * scale[0], -
              7.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 12.0 *
              scale[0], -2.0 * scale[1], 9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], -25.0 * scale[0],
              14.0 * scale[1], -25.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(103.0 * scale[0], 1175.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -27.0 * scale[1], 2.0 * scale[0], -
              38.0 * scale[1], 4.0 * scale[0], -22.0 * scale[1])
    Curveto_r(2.0 * scale[0], 15.0 * scale[1], 2.0 * scale[0],
              37.0 * scale[1], 0.0 * scale[0], 50.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 12.0 * scale[1], -4.0 * scale[0],
              0.0 * scale[1], -4.0 * scale[0], -28.0 * scale[1])
    te.end_fill()
    Moveto(121.0 * scale[0], 1188.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -21.0 * scale[1], 4.0 * scale[0], -
              38.0 * scale[1], 9.0 * scale[0], -38.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              27.0 * scale[1], 0.0 * scale[0], 55.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 16.0 * scale[1], -9.0 * scale[0],
              13.0 * scale[1], -9.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(832.0 * scale[0], 1178.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -47.0 * scale[1], -1.0 * scale[0], -
              48.0 * scale[1], 28.0 * scale[0], -48.0 * scale[1])
    Curveto_r(27.0 * scale[0], 0.0 * scale[1], 30.0 * scale[0],
              3.0 * scale[1], 29.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 30.0 * scale[1], -2.0 * scale[0],
              30.0 * scale[1], -6.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -19.0 * scale[1], -10.0 * scale[0], -
              28.0 * scale[1], -23.0 * scale[0], -28.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0],
              9.0 * scale[1], -23.0 * scale[0], 43.0 * scale[1])
    Lineto_r(-4.0 * scale[0], 42.0 * scale[1])
    Lineto_r(-1.0 * scale[0], -47.0 * scale[1])
    te.end_fill()
    Moveto(851.0 * scale[0], 1178.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -16.0 * scale[1], 4.0 * scale[0], -
              28.0 * scale[1], 9.0 * scale[0], -28.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              8.0 * scale[1], 0.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 18.0 * scale[1], -9.0 * scale[0],
              17.0 * scale[1], -9.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(542.0 * scale[0], 1163.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -9.0 * scale[1], 11.0 * scale[0], -
              17.0 * scale[1], 20.0 * scale[0], -19.0 * scale[1])
    Curveto_r(20.0 * scale[0], -3.0 * scale[1], 13.0 * scale[0],
              22.0 * scale[1], -8.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 4.0 * scale[1], -14.0 * scale[0],
              1.0 * scale[1], -12.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(151.0 * scale[0], 1154.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(541.0 * scale[0], 1110.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -11.0 * scale[1], -19.0 *
              scale[0], -20.0 * scale[1], -14.0 * scale[0], -20.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 18.0 * scale[0],
              9.0 * scale[1], 28.0 * scale[0], 20.0 * scale[1])
    Curveto_r(23.0 * scale[0], 25.0 * scale[1], 17.0 * scale[0],
              25.0 * scale[1], -14.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(484.0 * scale[0], 690.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -184.0 * scale[1], 2.0 * scale[0], -
              260.0 * scale[1], 3.0 * scale[0], -167.0 * scale[1])
    Curveto_r(2.0 * scale[0], 92.0 * scale[1], 2.0 * scale[0],
              242.0 * scale[1], 0.0 * scale[0], 335.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 92.0 * scale[1], -3.0 * scale[0],
              16.0 * scale[1], -3.0 * scale[0], -168.0 * scale[1])
    te.end_fill()
    Moveto(36.0 * scale[0], 951.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -36.0 * scale[1], -10.0 *
              scale[0], -65.0 * scale[1], 23.0 * scale[0], -74.0 * scale[1])
    Curveto_r(44.0 * scale[0], -11.0 * scale[1], 55.0 * scale[0],
              39.0 * scale[1], 17.0 * scale[0], 80.0 * scale[1])
    Lineto_r(-24.0 * scale[0], 26.0 * scale[1])
    Lineto_r(-16.0 * scale[0], -32.0 * scale[1])
    te.end_fill()
    Moveto(936.0 * scale[0], 925.0 * scale[1], x, y)
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
    Moveto(505.0 * scale[0], 850.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(42.0 * scale[0], 830.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-30.0 * scale[0], -49.0 * scale[1], -1.0 * scale[0], -
              112.0 * scale[1], 41.0 * scale[0], -89.0 * scale[1])
    Curveto_r(23.0 * scale[0], 14.0 * scale[1], 21.0 * scale[0],
              48.0 * scale[1], -6.0 * scale[0], 81.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 27.0 * scale[1], -23.0 * scale[0],
              27.0 * scale[1], -35.0 * scale[0], 8.0 * scale[1])
    te.end_fill()
    Moveto(840.0 * scale[0], 830.0 * scale[1], x, y)
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
    Moveto(220.0 * scale[0], 640.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 5.0 * scale[0], -
              22.0 * scale[1], 10.0 * scale[0], -30.0 * scale[1])
    Curveto_r(9.0 * scale[0], -13.0 * scale[1], 10.0 *
              scale[0], -13.0 * scale[1], 10.0 * scale[0], 0.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -5.0 * scale[0],
              22.0 * scale[1], -10.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 13.0 * scale[1], -10.0 * scale[0],
              13.0 * scale[1], -10.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(867.0 * scale[0], 633.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-15.0 * scale[0], -14.0 * scale[1], -6.0 *
              scale[0], -51.0 * scale[1], 17.0 * scale[0], -72.0 * scale[1])
    Curveto_r(25.0 * scale[0], -23.0 * scale[1], 29.0 *
              scale[0], -21.0 * scale[1], 45.0 * scale[0], 22.0 * scale[1])
    Curveto_r(8.0 * scale[0], 20.0 * scale[1], 7.0 * scale[0],
              30.0 * scale[1], -5.0 * scale[0], 42.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 16.0 * scale[1], -46.0 * scale[0],
              20.0 * scale[1], -57.0 * scale[0], 8.0 * scale[1])
    te.end_fill()
    Moveto(82.0 * scale[0], 580.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(872.0 * scale[0], 498.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -19.0 * scale[1], -14.0 *
              scale[0], -53.0 * scale[1], 11.0 * scale[0], -77.0 * scale[1])
    Curveto_r(22.0 * scale[0], -20.0 * scale[1], 25.0 *
              scale[0], -20.0 * scale[1], 37.0 * scale[0], -6.0 * scale[1])
    Curveto_r(12.0 * scale[0], 15.0 * scale[1], 19.0 * scale[0],
              70.0 * scale[1], 9.0 * scale[0], 79.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 12.0 * scale[1], -47.0 * scale[0],
              14.0 * scale[1], -57.0 * scale[0], 4.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#586744')
    te.end_fill()
    Moveto(435.0 * scale[0], 1300.0 * scale[1], x, y)
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
    Moveto(516.0 * scale[0], 1302.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -4.0 * scale[1], 22.0 * scale[0], -
              18.0 * scale[1], 37.0 * scale[0], -32.0 * scale[1])
    Curveto_r(20.0 * scale[0], -17.0 * scale[1], 26.0 *
              scale[0], -19.0 * scale[1], 22.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 9.0 * scale[1], -17.0 * scale[0],
              24.0 * scale[1], -30.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 16.0 * scale[1], -47.0 * scale[0],
              22.0 * scale[1], -29.0 * scale[0], 8.0 * scale[1])
    te.end_fill()
    Moveto(816.0 * scale[0], 1213.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(92.0 * scale[0], 1190.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 2.0 * scale[0], -
              27.0 * scale[1], 5.0 * scale[0], -17.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              25.0 * scale[1], 0.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(822.0 * scale[0], 1170.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(500.0 * scale[0], 1103.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-14.0 * scale[0], -7.0 * scale[1], -18.0 * scale[0], -
              13.0 * scale[1], -10.0 * scale[0], -13.0 * scale[1])
    Curveto_r(17.0 * scale[0], 0.0 * scale[1], 47.0 * scale[0],
              17.0 * scale[1], 40.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 2.0 * scale[1], -16.0 * scale[0], -
              2.0 * scale[1], -30.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(479.0 * scale[0], 1040.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -5.0 * scale[1], -119.0 * scale[0], -
              11.0 * scale[1], -245.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-229.0 * scale[0], -3.0 * scale[1], -229.0 *
              scale[0], -3.0 * scale[1], -232.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -17.0 * scale[1], 2.0 * scale[0], -
              23.0 * scale[1], 14.0 * scale[0], -23.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              3.0 * scale[1], 6.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 7.0 * scale[1], -12.0 * scale[0],
              15.0 * scale[1], -12.0 * scale[0], 19.0 * scale[1])
    Curveto_r(0.0 * scale[0], 15.0 * scale[1], 189.0 * scale[0],
              9.0 * scale[1], 226.0 * scale[0], -7.0 * scale[1])
    Curveto_r(24.0 * scale[0], -10.0 * scale[1], 39.0 *
              scale[0], -12.0 * scale[1], 43.0 * scale[0], -5.0 * scale[1])
    Curveto_r(10.0 * scale[0], 16.0 * scale[1], 89.0 * scale[0],
              25.0 * scale[1], 105.0 * scale[0], 12.0 * scale[1])
    Curveto_r(10.0 * scale[0], -8.0 * scale[1], 21.0 *
              scale[0], -8.0 * scale[1], 40.0 * scale[0], -1.0 * scale[1])
    Curveto_r(39.0 * scale[0], 14.0 * scale[1], 39.0 * scale[0],
              14.0 * scale[1], 33.0 * scale[0], -32.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -24.0 * scale[1], -1.0 *
              scale[0], -52.0 * scale[1], 3.0 * scale[0], -63.0 * scale[1])
    Curveto_r(6.0 * scale[0], -14.0 * scale[1], 9.0 * scale[0],
              1.0 * scale[1], 9.0 * scale[0], 46.0 * scale[1])
    Curveto_r(1.0 * scale[0], 58.0 * scale[1], 4.0 * scale[0],
              67.0 * scale[1], 24.0 * scale[0], 77.0 * scale[1])
    Curveto_r(12.0 * scale[0], 6.0 * scale[1], 18.0 * scale[0],
              11.0 * scale[1], 12.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0], -
              4.0 * scale[1], -26.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto_r(-209.0 * scale[0], -30.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -7.0 * scale[0], -
              7.0 * scale[1], -15.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 4.0 * scale[1], -15.0 * scale[0],
              8.0 * scale[1], -15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 2.0 * scale[1], 7.0 * scale[0],
              4.0 * scale[1], 15.0 * scale[0], 4.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0], -
              4.0 * scale[1], 15.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(693.0 * scale[0], 1033.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(15.0 * scale[0], -2.0 * scale[1], 39.0 *
              scale[0], -2.0 * scale[1], 55.0 * scale[0], 0.0 * scale[1])
    Curveto_r(15.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              4.0 * scale[1], -28.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 0.0 * scale[1], -43.0 *
              scale[0], -2.0 * scale[1], -27.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(44.0 * scale[0], 999.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -8.0 * scale[1], -3.0 *
              scale[0], -9.0 * scale[1], 6.0 * scale[0], -4.0 * scale[1])
    Curveto_r(7.0 * scale[0], 4.0 * scale[1], 16.0 * scale[0],
              2.0 * scale[1], 22.0 * scale[0], -6.0 * scale[1])
    Curveto_r(8.0 * scale[0], -12.0 * scale[1], 9.0 *
              scale[0], -12.0 * scale[1], 6.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 20.0 * scale[1], -24.0 * scale[0],
              25.0 * scale[1], -34.0 * scale[0], 10.0 * scale[1])
    te.end_fill()
    Moveto(539.0 * scale[0], 987.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -16.0 * scale[1], -14.0 *
              scale[0], -28.0 * scale[1], -7.0 * scale[0], -40.0 * scale[1])
    Curveto_r(5.0 * scale[0], -9.0 * scale[1], 6.0 * scale[0], -
              23.0 * scale[1], 2.0 * scale[0], -30.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -4.0 *
              scale[0], -9.0 * scale[1], 0.0 * scale[0], -5.0 * scale[1])
    Curveto_r(5.0 * scale[0], 4.0 * scale[1], 14.0 * scale[0],
              2.0 * scale[1], 21.0 * scale[0], -5.0 * scale[1])
    Curveto_r(9.0 * scale[0], -9.0 * scale[1], 7.0 * scale[0], -
              15.0 * scale[1], -9.0 * scale[0], -29.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -16.0 * scale[1], -19.0 *
              scale[0], -17.0 * scale[1], -2.0 * scale[0], -12.0 * scale[1])
    Curveto_r(16.0 * scale[0], 6.0 * scale[1], 17.0 * scale[0],
              5.0 * scale[1], 7.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -12.0 * scale[1], -10.0 *
              scale[0], -27.0 * scale[1], -7.0 * scale[0], -34.0 * scale[1])
    Curveto_r(2.0 * scale[0], -7.0 * scale[1], 5.0 *
              scale[0], -3.0 * scale[1], 5.0 * scale[0], 7.0 * scale[1])
    Curveto_r(1.0 * scale[0], 29.0 * scale[1], 20.0 * scale[0],
              6.0 * scale[1], 23.0 * scale[0], -28.0 * scale[1])
    Curveto_r(3.0 * scale[0], -35.0 * scale[1], 61.0 * scale[0], -
              104.0 * scale[1], 85.0 * scale[0], -101.0 * scale[1])
    Curveto_r(10.0 * scale[0], 1.0 * scale[1], 26.0 * scale[0],
              5.0 * scale[1], 36.0 * scale[0], 10.0 * scale[1])
    Curveto_r(14.0 * scale[0], 6.0 * scale[1], 16.0 * scale[0],
              10.0 * scale[1], 6.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 4.0 * scale[1], -17.0 * scale[0],
              1.0 * scale[1], -24.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -11.0 * scale[1], -14.0 *
              scale[0], -13.0 * scale[1], -19.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 7.0 * scale[1], -2.0 * scale[0],
              12.0 * scale[1], 3.0 * scale[0], 12.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              5.0 * scale[1], 11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 16.0 * scale[1], -81.0 * scale[0],
              115.0 * scale[1], -94.0 * scale[0], 115.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 1.0 * scale[1], -9.0 * scale[0],
              7.0 * scale[1], -7.0 * scale[0], 15.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], 3.0 * scale[0],
              31.0 * scale[1], 1.0 * scale[0], 50.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 19.0 * scale[1], -3.0 * scale[0],
              50.0 * scale[1], -3.0 * scale[0], 68.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 38.0 * scale[1], -6.0 * scale[0],
              39.0 * scale[1], -28.0 * scale[0], 9.0 * scale[1])
    te.end_fill()
    Moveto_r(101.0 * scale[0], -233.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -4.0 * scale[0], -
              12.0 * scale[1], -10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0],
              10.0 * scale[1], -10.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 5.0 * scale[0],
              9.0 * scale[1], 10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              7.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(910.0 * scale[0], 1000.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              7.0 * scale[1], 15.0 * scale[0], -4.0 * scale[1])
    Curveto_r(8.0 * scale[0], 4.0 * scale[1], 15.0 * scale[0],
              8.0 * scale[1], 15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 2.0 * scale[1], -7.0 * scale[0],
              4.0 * scale[1], -15.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              4.0 * scale[1], -15.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(875.0 * scale[0], 991.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 0.0 * scale[0], -
              13.0 * scale[1], 6.0 * scale[0], -17.0 * scale[1])
    Curveto_r(7.0 * scale[0], -4.0 * scale[1], 9.0 *
              scale[0], -3.0 * scale[1], 5.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], 0.0 * scale[0],
              13.0 * scale[1], 6.0 * scale[0], 15.0 * scale[1])
    Curveto_r(9.0 * scale[0], 4.0 * scale[1], 10.0 * scale[0],
              6.0 * scale[1], 1.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 1.0 * scale[1], -14.0 * scale[0], -
              3.0 * scale[1], -18.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(490.0 * scale[0], 961.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -22.0 * scale[1], 16.0 * scale[0], -
              36.0 * scale[1], 24.0 * scale[0], -22.0 * scale[1])
    Curveto_r(4.0 * scale[0], 5.0 * scale[1], 2.0 * scale[0],
              12.0 * scale[1], -4.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -8.0 * scale[0],
              11.0 * scale[1], -5.0 * scale[0], 16.0 * scale[1])
    Curveto_r(4.0 * scale[0], 5.0 * scale[1], 1.0 * scale[0],
              9.0 * scale[1], -4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              9.0 * scale[1], -11.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(20.0 * scale[0], 949.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -11.0 * scale[1], -10.0 *
              scale[0], -27.0 * scale[1], -8.0 * scale[0], -35.0 * scale[1])
    Curveto_r(2.0 * scale[0], -8.0 * scale[1], 8.0 * scale[0],
              1.0 * scale[1], 14.0 * scale[0], 20.0 * scale[1])
    Curveto_r(12.0 * scale[0], 40.0 * scale[1], 10.0 * scale[0],
              46.0 * scale[1], -6.0 * scale[0], 15.0 * scale[1])
    te.end_fill()
    Moveto(80.0 * scale[0], 966.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 7.0 * scale[0], -
              14.0 * scale[1], 15.0 * scale[0], -22.0 * scale[1])
    Curveto_r(8.0 * scale[0], -9.0 * scale[1], 15.0 * scale[0], -
              11.0 * scale[1], 15.0 * scale[0], -6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -7.0 * scale[0],
              15.0 * scale[1], -15.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 7.0 * scale[1], -15.0 * scale[0],
              9.0 * scale[1], -15.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(890.0 * scale[0], 950.0 * scale[1], x, y)
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
    Moveto(491.0 * scale[0], 874.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(493.0 * scale[0], 805.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -27.0 * scale[1], 2.0 * scale[0], -
              38.0 * scale[1], 4.0 * scale[0], -22.0 * scale[1])
    Curveto_r(2.0 * scale[0], 15.0 * scale[1], 2.0 * scale[0],
              37.0 * scale[1], 0.0 * scale[0], 50.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 12.0 * scale[1], -4.0 * scale[0],
              0.0 * scale[1], -4.0 * scale[0], -28.0 * scale[1])
    te.end_fill()
    Moveto(20.0 * scale[0], 815.0 * scale[1], x, y)
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
    Moveto(735.0 * scale[0], 820.0 * scale[1], x, y)
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
    Moveto(317.0 * scale[0], 809.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(462.0 * scale[0], 775.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(492.0 * scale[0], 730.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(311.0 * scale[0], 724.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(111.0 * scale[0], 704.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(284.0 * scale[0], 703.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -9.0 * scale[1], 3.0 * scale[0], -
              20.0 * scale[1], -6.0 * scale[0], -31.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -9.0 * scale[1], -19.0 * scale[0], -
              28.0 * scale[1], -23.0 * scale[0], -42.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -24.0 * scale[1], -6.0 *
              scale[0], -24.0 * scale[1], 8.0 * scale[0], -6.0 * scale[1])
    Curveto_r(14.0 * scale[0], 19.0 * scale[1], 15.0 * scale[0],
              19.0 * scale[1], 21.0 * scale[0], -10.0 * scale[1])
    Curveto_r(3.0 * scale[0], -16.0 * scale[1], 5.0 * scale[0], -
              36.0 * scale[1], 4.0 * scale[0], -44.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -8.0 * scale[1], 0.0 * scale[0], -
              34.0 * scale[1], 0.0 * scale[0], -58.0 * scale[1])
    Curveto_r(2.0 * scale[0], -51.0 * scale[1], 22.0 *
              scale[0], -48.0 * scale[1], 22.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 36.0 * scale[1], 8.0 * scale[0],
              42.0 * scale[1], 28.0 * scale[0], 22.0 * scale[1])
    Curveto_r(16.0 * scale[0], -16.0 * scale[1], 15.0 * scale[0], -
              28.0 * scale[1], -2.0 * scale[0], -28.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0], -
              14.0 * scale[1], -18.0 * scale[0], -32.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -24.0 * scale[1], 0.0 * scale[0], -
              36.0 * scale[1], 16.0 * scale[0], -49.0 * scale[1])
    Curveto_r(20.0 * scale[0], -17.0 * scale[1], 21.0 *
              scale[0], -17.0 * scale[1], 28.0 * scale[0], 4.0 * scale[1])
    Curveto_r(6.0 * scale[0], 21.0 * scale[1], 6.0 * scale[0],
              21.0 * scale[1], 8.0 * scale[0], 2.0 * scale[1])
    Curveto_r(2.0 * scale[0], -17.0 * scale[1], 3.0 *
              scale[0], -16.0 * scale[1], 9.0 * scale[0], 5.0 * scale[1])
    Curveto_r(4.0 * scale[0], 14.0 * scale[1], 4.0 * scale[0],
              38.0 * scale[1], -1.0 * scale[0], 55.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 41.0 * scale[1], -11.0 * scale[0],
              41.0 * scale[1], 15.0 * scale[0], 42.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0], -
              1.0 * scale[1], 10.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -3.0 * scale[1], -13.0 * scale[0], -
              9.0 * scale[1], -13.0 * scale[0], -14.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 7.0 * scale[0], -
              6.0 * scale[1], 15.0 * scale[0], -3.0 * scale[1])
    Curveto_r(8.0 * scale[0], 4.0 * scale[1], 15.0 * scale[0],
              2.0 * scale[1], 15.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 8.0 * scale[0], -
              13.0 * scale[1], 17.0 * scale[0], -16.0 * scale[1])
    Curveto_r(16.0 * scale[0], -6.0 * scale[1], 16.0 *
              scale[0], -6.0 * scale[1], 0.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 10.0 * scale[1], -17.0 * scale[0],
              26.0 * scale[1], -17.0 * scale[0], 35.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], -6.0 * scale[0],
              14.0 * scale[1], -14.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -3.0 * scale[1], -16.0 * scale[0],
              2.0 * scale[1], -19.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 10.0 * scale[1], -1.0 * scale[0],
              13.0 * scale[1], 9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(12.0 * scale[0], -4.0 * scale[1], 14.0 * scale[0],
              3.0 * scale[1], 13.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 23.0 * scale[1], -6.0 * scale[0],
              39.0 * scale[1], -11.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -3.0 * scale[1], -8.0 * scale[0],
              0.0 * scale[1], -8.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -6.0 * scale[0],
              10.0 * scale[1], -12.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -12.0 * scale[0],
              2.0 * scale[1], -11.0 * scale[0], 9.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], -4.0 * scale[0],
              10.0 * scale[1], -21.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -7.0 * scale[1], -28.0 *
              scale[0], -4.0 * scale[1], -48.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 15.0 * scale[1], -19.0 * scale[0],
              21.0 * scale[1], -14.0 * scale[0], 14.0 * scale[1])
    te.end_fill()
    Moveto_r(107.0 * scale[0], -73.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(17.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0], -
              29.0 * scale[1], -10.0 * scale[0], -40.0 * scale[1])
    Curveto_r(-27.0 * scale[0], -14.0 * scale[1], -26.0 *
              scale[0], -15.0 * scale[1], -29.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 38.0 * scale[1], -1.0 * scale[0],
              40.0 * scale[1], 13.0 * scale[0], 25.0 * scale[1])
    Curveto_r(9.0 * scale[0], -9.0 * scale[1], 21.0 * scale[0], -
              16.0 * scale[1], 26.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(60.0 * scale[0], 706.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 30.0 * scale[0], -
              39.0 * scale[1], 36.0 * scale[0], -34.0 * scale[1])
    Curveto_r(2.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              13.0 * scale[1], -16.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 10.0 * scale[1], -20.0 * scale[0],
              15.0 * scale[1], -20.0 * scale[0], 11.0 * scale[1])
    te.end_fill()
    Moveto(561.0 * scale[0], 644.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(941.0 * scale[0], 608.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], -4.0 * scale[0], -
              25.0 * scale[1], -7.0 * scale[0], -35.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -17.0 * scale[1], -5.0 *
              scale[0], -17.0 * scale[1], 6.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 10.0 * scale[1], 9.0 * scale[0],
              25.0 * scale[1], 7.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 15.0 * scale[1], -5.0 * scale[0],
              15.0 * scale[1], -6.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(251.0 * scale[0], 585.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -24.0 * scale[1], 27.0 * scale[0], -
              96.0 * scale[1], 28.0 * scale[0], -75.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -6.0 * scale[0],
              33.0 * scale[1], -14.0 * scale[0], 55.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 22.0 * scale[1], -14.0 * scale[0],
              31.0 * scale[1], -14.0 * scale[0], 20.0 * scale[1])
    te.end_fill()
    Moveto(907.0 * scale[0], 533.0 * scale[1], x, y)
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
    Moveto(491.0 * scale[0], 514.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(493.0 * scale[0], 425.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -38.0 * scale[1], 2.0 * scale[0], -
              53.0 * scale[1], 4.0 * scale[0], -32.0 * scale[1])
    Curveto_r(2.0 * scale[0], 20.0 * scale[1], 2.0 * scale[0],
              52.0 * scale[1], 0.0 * scale[0], 70.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 17.0 * scale[1], -4.0 * scale[0],
              1.0 * scale[1], -4.0 * scale[0], -38.0 * scale[1])
    te.end_fill()
    Moveto(938.0 * scale[0], 453.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -13.0 * scale[1], -2.0 *
              scale[0], -23.0 * scale[1], 3.0 * scale[0], -23.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0], -
              8.0 * scale[1], 9.0 * scale[0], -17.0 * scale[1])
    Curveto_r(0.0 * scale[0], -15.0 * scale[1], 2.0 * scale[0], -
              16.0 * scale[1], 10.0 * scale[0], -3.0 * scale[1])
    Curveto_r(5.0 * scale[0], 8.0 * scale[1], 5.0 * scale[0],
              17.0 * scale[1], 1.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -11.0 * scale[0],
              14.0 * scale[1], -13.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 19.0 * scale[1], -4.0 * scale[0],
              19.0 * scale[1], -10.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(430.0 * scale[0], 435.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -15.0 * scale[1], 7.0 * scale[0], -
              32.0 * scale[1], 3.0 * scale[0], -38.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], 1.0 *
              scale[0], -6.0 * scale[1], 10.0 * scale[0], 2.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              21.0 * scale[1], 17.0 * scale[0], 30.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -2.0 * scale[0],
              14.0 * scale[1], -10.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -13.0 * scale[1], -10.0 *
              scale[0], -13.0 * scale[1], -10.0 * scale[0], 2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], -4.0 * scale[0],
              20.0 * scale[1], -10.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -7.0 * scale[0], -
              3.0 * scale[1], 0.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(400.0 * scale[0], 434.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 5.0 * scale[0], -
              12.0 * scale[1], 10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 8.0 * scale[0],
              11.0 * scale[1], 5.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 14.0 * scale[1], -15.0 * scale[0],
              11.0 * scale[1], -15.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(850.0 * scale[0], 442.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 9.0 * scale[0], -
              18.0 * scale[1], 20.0 * scale[0], -32.0 * scale[1])
    Curveto_r(13.0 * scale[0], -17.0 * scale[1], 20.0 * scale[0], -
              20.0 * scale[1], 20.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], -9.0 * scale[0],
              23.0 * scale[1], -20.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 9.0 * scale[1], -20.0 * scale[0],
              13.0 * scale[1], -20.0 * scale[0], 9.0 * scale[1])
    te.end_fill()
    Moveto(26.0 * scale[0], 415.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -8.0 * scale[1], 10.0 * scale[0], -
              15.0 * scale[1], 15.0 * scale[0], -15.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 6.0 * scale[0],
              7.0 * scale[1], 3.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 8.0 * scale[1], -10.0 * scale[0],
              15.0 * scale[1], -15.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0], -
              7.0 * scale[1], -3.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(915.0 * scale[0], 399.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0], -
              12.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 17.0 * scale[1], 1.0 * scale[0],
              20.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(683.0 * scale[0], 363.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(26.0 * scale[0], -2.0 * scale[1], 68.0 *
              scale[0], -2.0 * scale[1], 95.0 * scale[0], 0.0 * scale[1])
    Curveto_r(26.0 * scale[0], 2.0 * scale[1], 4.0 * scale[0],
              3.0 * scale[1], -48.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-52.0 * scale[0], 0.0 * scale[1], -74.0 *
              scale[0], -1.0 * scale[1], -47.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(853.0 * scale[0], 363.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(15.0 * scale[0], -2.0 * scale[1], 39.0 *
              scale[0], -2.0 * scale[1], 55.0 * scale[0], 0.0 * scale[1])
    Curveto_r(15.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              4.0 * scale[1], -28.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 0.0 * scale[1], -43.0 *
              scale[0], -2.0 * scale[1], -27.0 * scale[0], -4.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#886ba2')
    te.end_fill()
    Moveto(576.0 * scale[0], 658.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -13.0 * scale[1], -6.0 * scale[0], -
              39.0 * scale[1], -7.0 * scale[0], -58.0 * scale[1])
    Lineto_r(-1.0 * scale[0], -35.0 * scale[1])
    Lineto_r(-9.0 * scale[0], 33.0 * scale[1])
    Lineto_r(-10.0 * scale[0], 32.0 * scale[1])
    Lineto_r(-21.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -15.0 * scale[1], -24.0 *
              scale[0], -17.0 * scale[1], -31.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 9.0 * scale[1], -7.0 * scale[0],
              7.0 * scale[1], -3.0 * scale[0], -5.0 * scale[1])
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 6.0 * scale[0], -
              68.0 * scale[1], 6.0 * scale[0], -128.0 * scale[1])
    Lineto_r(0.0 * scale[0], -108.0 * scale[1])
    Lineto_r(228.0 * scale[0], 6.0 * scale[1])
    Curveto_r(125.0 * scale[0], 3.0 * scale[1], 229.0 * scale[0],
              7.0 * scale[1], 230.0 * scale[0], 9.0 * scale[1])
    Curveto_r(2.0 * scale[0], 1.0 * scale[1], 1.0 * scale[0],
              12.0 * scale[1], -3.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 15.0 * scale[1], -10.0 * scale[0],
              18.0 * scale[1], -19.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -6.0 * scale[1], -16.0 *
              scale[0], -8.0 * scale[1], -20.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 4.0 * scale[1], -4.0 * scale[0],
              0.0 * scale[1], -1.0 * scale[0], -9.0 * scale[1])
    Curveto_r(5.0 * scale[0], -13.0 * scale[1], 2.0 * scale[0], -
              15.0 * scale[1], -14.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-28.0 * scale[0], 7.0 * scale[1], -51.0 * scale[0],
              46.0 * scale[1], -45.0 * scale[0], 74.0 * scale[1])
    Curveto_r(5.0 * scale[0], 19.0 * scale[1], 4.0 * scale[0],
              21.0 * scale[1], -5.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -13.0 * scale[1], -11.0 *
              scale[0], -13.0 * scale[1], -11.0 * scale[0], 1.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], 7.0 * scale[0],
              22.0 * scale[1], 15.0 * scale[0], 29.0 * scale[1])
    Curveto_r(8.0 * scale[0], 7.0 * scale[1], 15.0 * scale[0],
              9.0 * scale[1], 15.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 6.0 * scale[0], -
              1.0 * scale[1], 14.0 * scale[0], 6.0 * scale[1])
    Curveto_r(12.0 * scale[0], 11.0 * scale[1], 12.0 * scale[0],
              15.0 * scale[1], 0.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              19.0 * scale[1], -8.0 * scale[0], 22.0 * scale[1])
    Curveto_r(4.0 * scale[0], 4.0 * scale[1], 0.0 * scale[0],
              9.0 * scale[1], -9.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 3.0 * scale[1], -14.0 * scale[0],
              14.0 * scale[1], -11.0 * scale[0], 30.0 * scale[1])
    Lineto_r(4.0 * scale[0], 24.0 * scale[1])
    Lineto_r(-20.0 * scale[0], -20.0 * scale[1])
    Lineto_r(-21.0 * scale[0], -21.0 * scale[1])
    Lineto_r(-39.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 15.0 * scale[1], -41.0 * scale[0],
              36.0 * scale[1], -44.0 * scale[0], 46.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 17.0 * scale[1], -6.0 * scale[0],
              18.0 * scale[1], -30.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -10.0 * scale[1], -33.0 *
              scale[0], -14.0 * scale[1], -42.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 5.0 * scale[1], -15.0 * scale[0],
              4.0 * scale[1], -5.0 * scale[0], -8.0 * scale[1])
    Curveto_r(7.0 * scale[0], -8.0 * scale[1], 22.0 * scale[0], -
              13.0 * scale[1], 33.0 * scale[0], -11.0 * scale[1])
    Curveto_r(20.0 * scale[0], 4.0 * scale[1], 20.0 * scale[0],
              4.0 * scale[1], 2.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -12.0 * scale[1], -14.0 *
              scale[0], -18.0 * scale[1], -8.0 * scale[0], -15.0 * scale[1])
    Curveto_r(7.0 * scale[0], 4.0 * scale[1], 17.0 * scale[0],
              0.0 * scale[1], 24.0 * scale[0], -9.0 * scale[1])
    Curveto_r(8.0 * scale[0], -9.0 * scale[1], 16.0 * scale[0], -
              11.0 * scale[1], 20.0 * scale[0], -5.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 22.0 * scale[0],
              8.0 * scale[1], 43.0 * scale[0], 4.0 * scale[1])
    Curveto_r(20.0 * scale[0], -3.0 * scale[1], 34.0 * scale[0], -
              9.0 * scale[1], 31.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -4.0 * scale[1], -12.0 *
              scale[0], -5.0 * scale[1], -21.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 4.0 * scale[1], -14.0 * scale[0],
              2.0 * scale[1], -9.0 * scale[0], -5.0 * scale[1])
    Curveto_r(8.0 * scale[0], -13.0 * scale[1], -27.0 * scale[0], -
              83.0 * scale[1], -52.0 * scale[0], -104.0 * scale[1])
    Curveto_r(-40.0 * scale[0], -35.0 * scale[1], -112.0 *
              scale[0], -28.0 * scale[1], -159.0 * scale[0], 15.0 * scale[1])
    Lineto_r(-22.0 * scale[0], 20.0 * scale[1])
    Lineto_r(39.0 * scale[0], 19.0 * scale[1])
    Curveto_r(21.0 * scale[0], 11.0 * scale[1], 50.0 * scale[0],
              30.0 * scale[1], 63.0 * scale[0], 42.0 * scale[1])
    Curveto_r(17.0 * scale[0], 16.0 * scale[1], 30.0 * scale[0],
              20.0 * scale[1], 40.0 * scale[0], 14.0 * scale[1])
    Curveto_r(9.0 * scale[0], -5.0 * scale[1], 18.0 *
              scale[0], -4.0 * scale[1], 22.0 * scale[0], 2.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], 0.0 * scale[0],
              10.0 * scale[1], -8.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 0.0 * scale[1], -70.0 * scale[0],
              40.0 * scale[1], -63.0 * scale[0], 47.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              14.0 * scale[1], -5.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 26.0 * scale[1], -45.0 * scale[0],
              24.0 * scale[1], -53.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto_r(19.0 * scale[0], -77.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              12.0 * scale[1], -5.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -10.0 * scale[0],
              1.0 * scale[1], -10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 18.0 * scale[1], 6.0 * scale[0],
              21.0 * scale[1], 15.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto_r(241.0 * scale[0], 1.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -8.0 * scale[1], 18.0 * scale[0], -
              44.0 * scale[1], 28.0 * scale[0], -43.0 * scale[1])
    Curveto_r(3.0 * scale[0], 1.0 * scale[1], 6.0 * scale[0], -
              1.0 * scale[1], 6.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -3.0 * scale[1], -3.0 * scale[0], -
              5.0 * scale[1], -6.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              5.0 * scale[1], -14.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -14.0 * scale[1], -30.0 *
              scale[0], -5.0 * scale[1], -30.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 5.0 * scale[0],
              7.0 * scale[1], 12.0 * scale[0], 3.0 * scale[1])
    Curveto_r(7.0 * scale[0], -4.0 * scale[1], 8.0 *
              scale[0], -3.0 * scale[1], 4.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], -11.0 * scale[0],
              9.0 * scale[1], -16.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -9.0 * scale[1], -22.0 * scale[0],
              15.0 * scale[1], -10.0 * scale[0], 30.0 * scale[1])
    Curveto_r(13.0 * scale[0], 15.0 * scale[1], 35.0 * scale[0],
              21.0 * scale[1], 26.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(640.0 * scale[0], 636.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(935.0 * scale[0], 630.0 * scale[1], x, y)
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
    Moveto(953.0 * scale[0], 601.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -24.0 * scale[1], -8.0 *
              scale[0], -31.0 * scale[1], 3.0 * scale[0], -35.0 * scale[1])
    Curveto_r(10.0 * scale[0], -4.0 * scale[1], 14.0 * scale[0],
              4.0 * scale[1], 14.0 * scale[0], 29.0 * scale[1])
    Curveto_r(0.0 * scale[0], 43.0 * scale[1], -2.0 * scale[0],
              43.0 * scale[1], -17.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(915.0 * scale[0], 551.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              12.0 * scale[1], 4.0 * scale[0], -15.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 11.0 * scale[0],
              1.0 * scale[1], 15.0 * scale[0], 9.0 * scale[1])
    Curveto_r(6.0 * scale[0], 16.0 * scale[1], -9.0 * scale[0],
              21.0 * scale[1], -19.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(933.0 * scale[0], 528.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-26.0 * scale[0], -13.0 * scale[1], -31.0 *
              scale[0], -31.0 * scale[1], -6.0 * scale[0], -21.0 * scale[1])
    Curveto_r(12.0 * scale[0], 5.0 * scale[1], 15.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -9.0 * scale[1], -2.0 * scale[0], -
              19.0 * scale[1], 3.0 * scale[0], -22.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 10.0 * scale[0], -
              15.0 * scale[1], 10.0 * scale[0], -26.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 5.0 * scale[0], -
              19.0 * scale[1], 10.0 * scale[0], -19.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              25.0 * scale[1], 10.0 * scale[0], 55.0 * scale[1])
    Curveto_r(0.0 * scale[0], 58.0 * scale[1], -2.0 * scale[0],
              60.0 * scale[1], -37.0 * scale[0], 43.0 * scale[1])
    te.penup()
