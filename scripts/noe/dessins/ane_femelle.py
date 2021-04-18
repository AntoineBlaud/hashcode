import turtle as te
from helper import *


def ane_femelle(x, y, scale):

    te.penup()
    te.color('#af86b5')
    te.end_fill()
    Moveto(433.0 * scale[0], 1317.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 6.0 * scale[0], -
              14.0 * scale[1], 14.0 * scale[0], -14.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              4.0 * scale[1], 2.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 7.0 * scale[1], -12.0 * scale[0],
              13.0 * scale[1], -14.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 0.0 * scale[1], -2.0 * scale[0], -
              6.0 * scale[1], -2.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(494.0 * scale[0], 1318.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], -4.0 *
              scale[0], -10.0 * scale[1], 1.0 * scale[0], -6.0 * scale[1])
    Curveto_r(4.0 * scale[0], 4.0 * scale[1], 17.0 * scale[0],
              3.0 * scale[1], 27.0 * scale[0], -3.0 * scale[1])
    Curveto_r(16.0 * scale[0], -9.0 * scale[1], 19.0 *
              scale[0], -8.0 * scale[1], 16.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 18.0 * scale[1], -34.0 * scale[0],
              22.0 * scale[1], -44.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(844.0 * scale[0], 1309.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -11.0 * scale[1], -14.0 *
              scale[0], -20.0 * scale[1], -9.0 * scale[0], -19.0 * scale[1])
    Curveto_r(34.0 * scale[0], 7.0 * scale[1], 38.0 * scale[0], -
              2.0 * scale[1], 12.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -14.0 * scale[1], -27.0 *
              scale[0], -32.0 * scale[1], -27.0 * scale[0], -40.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -6.0 * scale[0], -
              16.0 * scale[1], -12.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -4.0 * scale[1], -10.0 *
              scale[0], -8.0 * scale[1], 1.0 * scale[0], -15.0 * scale[1])
    Curveto_r(12.0 * scale[0], -8.0 * scale[1], 12.0 * scale[0], -
              14.0 * scale[1], 3.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -21.0 * scale[1], 6.0 * scale[0], -
              36.0 * scale[1], 38.0 * scale[0], -26.0 * scale[1])
    Lineto_r(25.0 * scale[0], 8.0 * scale[1])
    Lineto_r(-27.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-34.0 * scale[0], -3.0 * scale[1], -42.0 * scale[0],
              15.0 * scale[1], -9.0 * scale[0], 20.0 * scale[1])
    Curveto_r(14.0 * scale[0], 2.0 * scale[1], 27.0 * scale[0],
              6.0 * scale[1], 30.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -4.0 * scale[0],
              4.0 * scale[1], -16.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -4.0 * scale[1], -24.0 * scale[0],
              0.0 * scale[1], -27.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 21.0 * scale[1], -7.0 * scale[0],
              25.0 * scale[1], 4.0 * scale[0], 18.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 12.0 * scale[1], -2.0 * scale[0],
              14.0 * scale[1], 12.0 * scale[0], 8.0 * scale[1])
    Curveto_r(16.0 * scale[0], -6.0 * scale[1], 17.0 *
              scale[0], -4.0 * scale[1], 7.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 13.0 * scale[1], -10.0 * scale[0],
              16.0 * scale[1], 2.0 * scale[0], 16.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0], -
              4.0 * scale[1], 9.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -4.0 * scale[1], 0.0 * scale[0], -
              10.0 * scale[1], 6.0 * scale[0], -14.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 7.0 * scale[0], -
              11.0 * scale[1], 4.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], -2.0 *
              scale[0], -8.0 * scale[1], 5.0 * scale[0], -4.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 8.0 * scale[0],
              12.0 * scale[1], 5.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], -2.0 * scale[0],
              8.0 * scale[1], 3.0 * scale[0], 5.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 16.0 * scale[0],
              0.0 * scale[1], 23.0 * scale[0], 8.0 * scale[1])
    Curveto_r(11.0 * scale[0], 13.0 * scale[1], 10.0 * scale[0],
              14.0 * scale[1], -3.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -3.0 * scale[1], -23.0 * scale[0],
              1.0 * scale[1], -31.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 13.0 * scale[1], -14.0 * scale[0],
              16.0 * scale[1], 1.0 * scale[0], 21.0 * scale[1])
    Curveto_r(14.0 * scale[0], 6.0 * scale[1], 14.0 * scale[0],
              8.0 * scale[1], -1.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 9.0 * scale[1], -13.0 * scale[0],
              21.0 * scale[1], -9.0 * scale[0], 24.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], 4.0 * scale[0],
              7.0 * scale[1], 1.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              9.0 * scale[1], -24.0 * scale[0], -21.0 * scale[1])
    te.end_fill()
    Moveto(115.0 * scale[0], 1277.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -17.0 * scale[1], 4.0 * scale[0], -
              33.0 * scale[1], 8.0 * scale[0], -34.0 * scale[1])
    Curveto_r(5.0 * scale[0], -1.0 * scale[1], 19.0 * scale[0], -
              13.0 * scale[1], 31.0 * scale[0], -28.0 * scale[1])
    Lineto_r(22.0 * scale[0], -25.0 * scale[1])
    Lineto_r(-1.0 * scale[0], 24.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], -4.0 * scale[0],
              28.0 * scale[1], -9.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 5.0 * scale[1], -6.0 * scale[0],
              2.0 * scale[1], -1.0 * scale[0], -6.0 * scale[1])
    Curveto_r(6.0 * scale[0], -10.0 * scale[1], 4.0 * scale[0], -
              12.0 * scale[1], -4.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 5.0 * scale[1], -10.0 * scale[0],
              15.0 * scale[1], -6.0 * scale[0], 23.0 * scale[1])
    Curveto_r(4.0 * scale[0], 13.0 * scale[1], 3.0 * scale[0],
              14.0 * scale[1], -10.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -11.0 * scale[1], -15.0 *
              scale[0], -9.0 * scale[1], -15.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 18.0 * scale[1], 4.0 * scale[0],
              25.0 * scale[1], 12.0 * scale[0], 20.0 * scale[1])
    Curveto_r(7.0 * scale[0], -4.0 * scale[1], 8.0 *
              scale[0], -3.0 * scale[1], 4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 23.0 * scale[1], -31.0 * scale[0],
              12.0 * scale[1], -31.0 * scale[0], -21.0 * scale[1])
    te.end_fill()
    Moveto(416.0 * scale[0], 1273.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -9.0 * scale[1], -1.0 * scale[0], -
              21.0 * scale[1], 5.0 * scale[0], -27.0 * scale[1])
    Curveto_r(9.0 * scale[0], -8.0 * scale[1], 10.0 *
              scale[0], -8.0 * scale[1], 5.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], -2.0 * scale[0],
              12.0 * scale[1], 4.0 * scale[0], 12.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              4.0 * scale[1], 6.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 5.0 * scale[1], 0.0 * scale[0],
              12.0 * scale[1], 6.0 * scale[0], 14.0 * scale[1])
    Curveto_r(8.0 * scale[0], 4.0 * scale[1], 7.0 * scale[0],
              6.0 * scale[1], -3.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 1.0 * scale[1], -20.0 * scale[0], -
              7.0 * scale[1], -23.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(535.0 * scale[0], 1274.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(10.0 * scale[0], -8.0 * scale[1], 22.0 * scale[0], -
              14.0 * scale[1], 27.0 * scale[0], -14.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 3.0 * scale[0], -
              11.0 * scale[1], -2.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -14.0 * scale[1], -7.0 * scale[0], -
              31.0 * scale[1], -4.0 * scale[0], -39.0 * scale[1])
    Curveto_r(9.0 * scale[0], -24.0 * scale[1], 31.0 * scale[0],
              3.0 * scale[1], 26.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 13.0 * scale[1], 1.0 * scale[0],
              29.0 * scale[1], 7.0 * scale[0], 37.0 * scale[1])
    Curveto_r(10.0 * scale[0], 12.0 * scale[1], 8.0 * scale[0],
              13.0 * scale[1], -10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -4.0 * scale[1], -20.0 *
              scale[0], -2.0 * scale[1], -16.0 * scale[0], 4.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], -4.0 * scale[0],
              11.0 * scale[1], -20.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 0.0 * scale[1], -26.0 *
              scale[0], -1.0 * scale[1], -8.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(90.0 * scale[0], 1265.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -4.0 * scale[0], -
              15.0 * scale[1], -9.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -22.0 * scale[1])
    Curveto_r(3.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], -6.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 11.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], 7.0 * scale[0], -26.0 * scale[1])
    Lineto_r(20.0 * scale[0], -21.0 * scale[1])
    Lineto_r(-4.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 23.0 * scale[1], -1.0 * scale[0],
              30.0 * scale[1], 8.0 * scale[0], 25.0 * scale[1])
    Curveto_r(9.0 * scale[0], -5.0 * scale[1], 9.0 *
              scale[0], -4.0 * scale[1], 0.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 9.0 * scale[1], -9.0 * scale[0],
              19.0 * scale[1], -2.0 * scale[0], 32.0 * scale[1])
    Curveto_r(6.0 * scale[0], 12.0 * scale[1], 6.0 * scale[0],
              18.0 * scale[1], -1.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              7.0 * scale[1], -10.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(125.0 * scale[0], 1200.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -5.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -11.0 * scale[1])
    Curveto_r(33.0 * scale[0], -8.0 * scale[1], 38.0 *
              scale[0], -7.0 * scale[1], 27.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 17.0 * scale[1], -16.0 * scale[0],
              17.0 * scale[1], -24.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(395.0 * scale[0], 1191.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              12.0 * scale[1], 3.0 * scale[0], -15.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 9.0 * scale[0],
              1.0 * scale[1], 9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], -3.0 * scale[0],
              19.0 * scale[1], -12.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(426.0 * scale[0], 1172.0 * scale[1], x, y)
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
    Moveto(465.0 * scale[0], 1160.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(337.0 * scale[0], 1030.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-20.0 * scale[0], -4.0 * scale[1], -39.0 *
              scale[0], -9.0 * scale[1], -40.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -2.0 * scale[1], -11.0 * scale[0], -
              15.0 * scale[1], -20.0 * scale[0], -29.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -19.0 * scale[1], -17.0 *
              scale[0], -21.0 * scale[1], -17.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], -9.0 * scale[0],
              17.0 * scale[1], -27.0 * scale[0], 18.0 * scale[1])
    Lineto_r(-28.0 * scale[0], 1.0 * scale[1])
    Lineto_r(25.0 * scale[0], 8.0 * scale[1])
    Lineto_r(25.0 * scale[0], 8.0 * scale[1])
    Lineto_r(-25.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -32.0 *
              scale[0], -4.0 * scale[1], -40.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -8.0 * scale[1], -12.0 *
              scale[0], -10.0 * scale[1], 3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0], -
              5.0 * scale[1], 17.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 4.0 * scale[0], -
              8.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 12.0 * scale[0],
              1.0 * scale[1], 15.0 * scale[0], -4.0 * scale[1])
    Curveto_r(4.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              12.0 * scale[1], -11.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -3.0 * scale[1], -8.0 *
              scale[0], -5.0 * scale[1], 10.0 * scale[0], -6.0 * scale[1])
    Curveto_r(15.0 * scale[0], 0.0 * scale[1], 27.0 * scale[0], -
              5.0 * scale[1], 27.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], 51.0 * scale[0], -
              21.0 * scale[1], 137.0 * scale[0], -24.0 * scale[1])
    Curveto_r(47.0 * scale[0], -2.0 * scale[1], 78.0 * scale[0], -
              8.0 * scale[1], 90.0 * scale[0], -18.0 * scale[1])
    Curveto_r(10.0 * scale[0], -9.0 * scale[1], 38.0 * scale[0], -
              27.0 * scale[1], 63.0 * scale[0], -42.0 * scale[1])
    Curveto_r(54.0 * scale[0], -31.0 * scale[1], 137.0 * scale[0], -
              110.0 * scale[1], 134.0 * scale[0], -127.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -3.0 * scale[1], 2.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -25.0 * scale[1])
    Curveto_r(5.0 * scale[0], -11.0 * scale[1], 18.0 * scale[0], -
              47.0 * scale[1], 30.0 * scale[0], -80.0 * scale[1])
    Curveto_r(41.0 * scale[0], -112.0 * scale[1], 44.0 * scale[0], -
              118.0 * scale[1], 48.0 * scale[0], -107.0 * scale[1])
    Curveto_r(10.0 * scale[0], 32.0 * scale[1], 124.0 * scale[0],
              1.0 * scale[1], 175.0 * scale[0], -46.0 * scale[1])
    Lineto_r(28.0 * scale[0], -27.0 * scale[1])
    Lineto_r(-5.0 * scale[0], 159.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 95.0 * scale[1], -10.0 * scale[0],
              163.0 * scale[1], -17.0 * scale[0], 166.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -7.0 * scale[0],
              18.0 * scale[1], -3.0 * scale[0], 35.0 * scale[1])
    Curveto_r(6.0 * scale[0], 26.0 * scale[1], 5.0 * scale[0],
              28.0 * scale[1], -16.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-25.0 * scale[0], -6.0 * scale[1], -71.0 * scale[0],
              8.0 * scale[1], -82.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 9.0 * scale[1], -8.0 * scale[0],
              8.0 * scale[1], -8.0 * scale[0], -3.0 * scale[1])
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], -2.0 * scale[0], -
              12.0 * scale[1], -9.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 7.0 * scale[1], -19.0 * scale[0],
              14.0 * scale[1], -32.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-34.0 * scale[0], 5.0 * scale[1], -59.0 * scale[0],
              16.0 * scale[1], -59.0 * scale[0], 28.0 * scale[1])
    Curveto_r(0.0 * scale[0], 15.0 * scale[1], -98.0 * scale[0],
              105.0 * scale[1], -133.0 * scale[0], 123.0 * scale[1])
    Curveto_r(-32.0 * scale[0], 16.0 * scale[1], -198.0 * scale[0],
              19.0 * scale[1], -270.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto_r(437.0 * scale[0], -475.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -8.0 * scale[1], -8.0 * scale[0], -
              15.0 * scale[1], -10.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0],
              7.0 * scale[1], -4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 4.0 * scale[0],
              15.0 * scale[1], 10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0], -
              7.0 * scale[1], 4.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(178.0 * scale[0], 973.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(140.0 * scale[0], 914.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 5.0 * scale[0], -
              15.0 * scale[1], 11.0 * scale[0], -21.0 * scale[1])
    Curveto_r(8.0 * scale[0], -8.0 * scale[1], 7.0 * scale[0], -
              13.0 * scale[1], -2.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -5.0 * scale[1], -10.0 *
              scale[0], -4.0 * scale[1], -6.0 * scale[0], 2.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], 0.0 * scale[0],
              13.0 * scale[1], -8.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 7.0 * scale[1], -19.0 * scale[0],
              5.0 * scale[1], 2.0 * scale[0], -39.0 * scale[1])
    Curveto_r(9.0 * scale[0], -19.0 * scale[1], 24.0 * scale[0], -
              35.0 * scale[1], 32.0 * scale[0], -35.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              2.0 * scale[1], 2.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 7.0 * scale[1], -8.0 * scale[0],
              10.0 * scale[1], 10.0 * scale[0], 16.0 * scale[1])
    Curveto_r(22.0 * scale[0], 7.0 * scale[1], 22.0 * scale[0],
              8.0 * scale[1], 3.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 14.0 * scale[1], -18.0 *
              scale[0], 15.0 * scale[1], 6.0 * scale[0], 9.0 * scale[1])
    Curveto_r(23.0 * scale[0], -6.0 * scale[1], 23.0 *
              scale[0], -6.0 * scale[1], 5.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 6.0 * scale[1], -28.0 * scale[0],
              19.0 * scale[1], -37.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 8.0 * scale[1], -18.0 * scale[0],
              11.0 * scale[1], -18.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(919.0 * scale[0], 893.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -21.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(90.0 * scale[0], 876.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 7.0 * scale[0], -
              7.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 12.0 *
              scale[0], -2.0 * scale[1], 9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], -25.0 * scale[0],
              14.0 * scale[1], -25.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(71.0 * scale[0], 687.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-49.0 * scale[0], -35.0 * scale[1], -59.0 * scale[0], -
              68.0 * scale[1], -63.0 * scale[0], -217.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -108.0 * scale[1], -2.0 *
              scale[0], -126.0 * scale[1], 7.0 * scale[0], -93.0 * scale[1])
    Curveto_r(9.0 * scale[0], 39.0 * scale[1], 49.0 * scale[0],
              83.0 * scale[1], 74.0 * scale[0], 83.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              7.0 * scale[1], 11.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 5.0 * scale[0],
              12.0 * scale[1], 10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(9.0 * scale[0], -5.0 * scale[1], 12.0 * scale[0],
              1.0 * scale[1], 9.0 * scale[0], 21.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], 5.0 * scale[0],
              10.0 * scale[1], 12.0 * scale[0], 15.0 * scale[1])
    Curveto_r(9.0 * scale[0], 5.0 * scale[1], 12.0 * scale[0],
              28.0 * scale[1], 11.0 * scale[0], 70.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 52.0 * scale[1], 1.0 * scale[0],
              66.0 * scale[1], 19.0 * scale[0], 86.0 * scale[1])
    Curveto_r(13.0 * scale[0], 12.0 * scale[1], 18.0 * scale[0],
              24.0 * scale[1], 13.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-50.0 * scale[0], 8.0 * scale[1], -75.0 * scale[0],
              5.0 * scale[1], -103.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(204.0 * scale[0], 365.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -11.0 * scale[1], -16.0 * scale[0], -
              32.0 * scale[1], -27.0 * scale[0], -47.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -24.0 * scale[1], -18.0 *
              scale[0], -28.0 * scale[1], -4.0 * scale[0], -48.0 * scale[1])
    Lineto_r(15.0 * scale[0], -21.0 * scale[1])
    Lineto_r(28.0 * scale[0], 26.0 * scale[1])
    Curveto_r(17.0 * scale[0], 16.0 * scale[1], 22.0 * scale[0],
              25.0 * scale[1], 12.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -4.0 * scale[1], -15.0 *
              scale[0], -1.0 * scale[1], -6.0 * scale[0], 24.0 * scale[1])
    Curveto_r(6.0 * scale[0], 19.0 * scale[1], 6.0 * scale[0],
              35.0 * scale[1], -1.0 * scale[0], 47.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 17.0 * scale[1], -10.0 * scale[0],
              17.0 * scale[1], -17.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(6.0 * scale[0], 314.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -21.0 * scale[1], -8.0 *
              scale[0], -59.0 * scale[1], 1.0 * scale[0], -51.0 * scale[1])
    Curveto_r(7.0 * scale[0], 8.0 * scale[1], 15.0 * scale[0],
              67.0 * scale[1], 9.0 * scale[0], 67.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              7.0 * scale[1], -10.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(959.0 * scale[0], 268.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], -2.0 * scale[0], -
              33.0 * scale[1], -5.0 * scale[0], -45.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -13.0 * scale[1], 1.0 * scale[0], -
              23.0 * scale[1], 6.0 * scale[0], -23.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              20.0 * scale[1], 10.0 * scale[0], 45.0 * scale[1])
    Curveto_r(0.0 * scale[0], 45.0 * scale[1], -9.0 * scale[0],
              65.0 * scale[1], -11.0 * scale[0], 23.0 * scale[1])
    te.end_fill()
    Moveto(909.0 * scale[0], 237.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(26.0 * scale[0], -28.0 * scale[1], 31.0 * scale[0], -
              32.0 * scale[1], 31.0 * scale[0], -19.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], -13.0 * scale[0],
              16.0 * scale[1], -28.0 * scale[0], 26.0 * scale[1])
    Lineto_r(-27.0 * scale[0], 19.0 * scale[1])
    Lineto_r(24.0 * scale[0], -26.0 * scale[1])
    te.end_fill()
    Moveto(383.0 * scale[0], 65.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -27.0 * scale[1], 2.0 * scale[0], -
              38.0 * scale[1], 4.0 * scale[0], -22.0 * scale[1])
    Curveto_r(2.0 * scale[0], 15.0 * scale[1], 2.0 * scale[0],
              37.0 * scale[1], 0.0 * scale[0], 50.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 12.0 * scale[1], -4.0 * scale[0],
              0.0 * scale[1], -4.0 * scale[0], -28.0 * scale[1])
    te.end_fill()
    Moveto(2.0 * scale[0], 42.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -22.0 * scale[1], 8.0 * scale[0], -
              23.0 * scale[1], 101.0 * scale[0], -28.0 * scale[1])
    Curveto_r(68.0 * scale[0], -4.0 * scale[1], 97.0 *
              scale[0], -2.0 * scale[1], 92.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -42.0 * scale[0],
              11.0 * scale[1], -90.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-69.0 * scale[0], 0.0 * scale[1], -86.0 * scale[0],
              3.0 * scale[1], -95.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 15.0 * scale[1], -10.0 * scale[0],
              14.0 * scale[1], -8.0 * scale[0], -6.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#b77f3e')
    te.end_fill()
    Moveto(396.0 * scale[0], 1389.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(19.0 * scale[0], -22.0 * scale[1], 19.0 * scale[0], -
              22.0 * scale[1], -6.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 4.0 * scale[1], -29.0 * scale[0],
              11.0 * scale[1], -34.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 5.0 * scale[1], -41.0 * scale[0],
              9.0 * scale[1], -79.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-64.0 * scale[0], 0.0 * scale[1], -68.0 * scale[0], -
              1.0 * scale[1], -56.0 * scale[0], -17.0 * scale[1])
    Curveto_r(12.0 * scale[0], -15.0 * scale[1], 12.0 * scale[0], -
              16.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 4.0 * scale[1], -29.0 * scale[0],
              4.0 * scale[1], -42.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-35.0 * scale[0], -9.0 * scale[1], -20.0 *
              scale[0], -34.0 * scale[1], 21.0 * scale[0], -34.0 * scale[1])
    Curveto_r(19.0 * scale[0], 0.0 * scale[1], 34.0 * scale[0], -
              5.0 * scale[1], 34.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -4.0 * scale[0], -
              8.0 * scale[1], -8.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 2.0 * scale[1], -14.0 * scale[0],
              1.0 * scale[1], -22.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -7.0 * scale[1], -8.0 * scale[0], -
              10.0 * scale[1], 11.0 * scale[0], -14.0 * scale[1])
    Curveto_r(13.0 * scale[0], -4.0 * scale[1], 51.0 * scale[0], -
              12.0 * scale[1], 84.0 * scale[0], -20.0 * scale[1])
    Lineto_r(60.0 * scale[0], -14.0 * scale[1])
    Lineto_r(-89.0 * scale[0], 6.0 * scale[1])
    Lineto_r(-88.0 * scale[0], 5.0 * scale[1])
    Lineto_r(13.0 * scale[0], -21.0 * scale[1])
    Curveto_r(12.0 * scale[0], -20.0 * scale[1], 23.0 * scale[0], -
              22.0 * scale[1], 101.0 * scale[0], -22.0 * scale[1])
    Curveto_r(83.0 * scale[0], 0.0 * scale[1], 117.0 * scale[0],
              10.0 * scale[1], 81.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              9.0 * scale[1], -3.0 * scale[0], 16.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 17.0 * scale[0],
              7.0 * scale[1], 21.0 * scale[0], 4.0 * scale[1])
    Curveto_r(4.0 * scale[0], -2.0 * scale[1], 5.0 * scale[0],
              5.0 * scale[1], 2.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 12.0 * scale[1], 0.0 * scale[0],
              20.0 * scale[1], 6.0 * scale[0], 20.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0], -
              6.0 * scale[1], 6.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], 2.0 *
              scale[0], -4.0 * scale[1], 12.0 * scale[0], 7.0 * scale[1])
    Curveto_r(12.0 * scale[0], 14.0 * scale[1], 33.0 * scale[0],
              22.0 * scale[1], 63.0 * scale[0], 24.0 * scale[1])
    Curveto_r(25.0 * scale[0], 1.0 * scale[1], 48.0 * scale[0],
              5.0 * scale[1], 52.0 * scale[0], 7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 2.0 * scale[1], 13.0 * scale[0], -
              2.0 * scale[1], 21.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -8.0 * scale[1], 18.0 * scale[0], -
              12.0 * scale[1], 22.0 * scale[0], -8.0 * scale[1])
    Curveto_r(4.0 * scale[0], 4.0 * scale[1], 6.0 * scale[0],
              2.0 * scale[1], 5.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -20.0 * scale[1], 0.0 * scale[0], -
              36.0 * scale[1], 8.0 * scale[0], -31.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 9.0 * scale[0],
              0.0 * scale[1], 10.0 * scale[0], -7.0 * scale[1])
    Curveto_r(10.0 * scale[0], -85.0 * scale[1], 9.0 * scale[0], -
              96.0 * scale[1], -6.0 * scale[0], -102.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -8.0 * scale[1], -9.0 * scale[0], -12.0 * scale[1])
    Curveto_r(4.0 * scale[0], -3.0 * scale[1], -1.0 * scale[0], -
              12.0 * scale[1], -11.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -9.0 * scale[1], -11.0 *
              scale[0], -12.0 * scale[1], -2.0 * scale[0], -7.0 * scale[1])
    Curveto_r(12.0 * scale[0], 5.0 * scale[1], 13.0 * scale[0],
              4.0 * scale[1], 3.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -7.0 * scale[1], -23.0 * scale[0], -
              14.0 * scale[1], -35.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-36.0 * scale[0], -4.0 * scale[1], -36.0 *
              scale[0], -6.0 * scale[1], 2.0 * scale[0], -14.0 * scale[1])
    Curveto_r(32.0 * scale[0], -7.0 * scale[1], 30.0 * scale[0], -
              7.0 * scale[1], -20.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 0.0 * scale[1], -62.0 * scale[0],
              4.0 * scale[1], -70.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              10.0 * scale[1], 8.0 * scale[0], 6.0 * scale[1])
    Curveto_r(12.0 * scale[0], -3.0 * scale[1], 20.0 *
              scale[0], -2.0 * scale[1], 17.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 9.0 * scale[1], -42.0 * scale[0],
              17.0 * scale[1], -130.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-33.0 * scale[0], 5.0 * scale[1], -78.0 * scale[0],
              11.0 * scale[1], -100.0 * scale[0], 15.0 * scale[1])
    Lineto_r(-40.0 * scale[0], 7.0 * scale[1])
    Lineto_r(30.0 * scale[0], -15.0 * scale[1])
    Lineto_r(30.0 * scale[0], -15.0 * scale[1])
    Lineto_r(-37.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-59.0 * scale[0], 9.0 * scale[1], -45.0 *
              scale[0], -1.0 * scale[1], 35.0 * scale[0], -26.0 * scale[1])
    Curveto_r(39.0 * scale[0], -12.0 * scale[1], 89.0 * scale[0], -
              31.0 * scale[1], 109.0 * scale[0], -41.0 * scale[1])
    Curveto_r(32.0 * scale[0], -16.0 * scale[1], 61.0 * scale[0], -
              19.0 * scale[1], 205.0 * scale[0], -19.0 * scale[1])
    Curveto_r(112.0 * scale[0], 0.0 * scale[1], 163.0 * scale[0],
              4.0 * scale[1], 153.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 7.0 * scale[1], 0.0 * scale[0],
              10.0 * scale[1], 38.0 * scale[0], 10.0 * scale[1])
    Curveto_r(31.0 * scale[0], 0.0 * scale[1], 52.0 * scale[0],
              4.0 * scale[1], 52.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 7.0 * scale[0],
              8.0 * scale[1], 16.0 * scale[0], 5.0 * scale[1])
    Curveto_r(14.0 * scale[0], -5.0 * scale[1], 15.0 *
              scale[0], -4.0 * scale[1], 5.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 10.0 * scale[1], -19.0 * scale[0],
              12.0 * scale[1], -34.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-24.0 * scale[0], -9.0 * scale[1], -235.0 *
              scale[0], -16.0 * scale[1], -226.0 * scale[0], -7.0 * scale[1])
    Curveto_r(2.0 * scale[0], 3.0 * scale[1], 46.0 * scale[0],
              6.0 * scale[1], 97.0 * scale[0], 7.0 * scale[1])
    Curveto_r(60.0 * scale[0], 1.0 * scale[1], 92.0 * scale[0],
              5.0 * scale[1], 92.0 * scale[0], 13.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 4.0 * scale[0],
              5.0 * scale[1], 9.0 * scale[0], -3.0 * scale[1])
    Curveto_r(6.0 * scale[0], -9.0 * scale[1], 11.0 * scale[0], -
              10.0 * scale[1], 15.0 * scale[0], -2.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], -3.0 * scale[0],
              25.0 * scale[1], -15.0 * scale[0], 43.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 17.0 * scale[1], -17.0 * scale[0],
              28.0 * scale[1], -10.0 * scale[0], 23.0 * scale[1])
    Curveto_r(9.0 * scale[0], -5.0 * scale[1], 12.0 *
              scale[0], -3.0 * scale[1], 9.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], -1.0 * scale[0],
              27.0 * scale[1], 3.0 * scale[0], 43.0 * scale[1])
    Curveto_r(6.0 * scale[0], 21.0 * scale[1], 5.0 * scale[0],
              32.0 * scale[1], -4.0 * scale[0], 38.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -7.0 * scale[0],
              8.0 * scale[1], 6.0 * scale[0], 8.0 * scale[1])
    Curveto_r(20.0 * scale[0], 0.0 * scale[1], 23.0 * scale[0],
              16.0 * scale[1], 5.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              6.0 * scale[1], 14.0 * scale[0], 6.0 * scale[1])
    Curveto_r(42.0 * scale[0], 1.0 * scale[1], 43.0 * scale[0],
              19.0 * scale[1], 1.0 * scale[0], 24.0 * scale[1])
    Lineto_r(-38.0 * scale[0], 4.0 * scale[1])
    Lineto_r(43.0 * scale[0], 1.0 * scale[1])
    Curveto_r(58.0 * scale[0], 3.0 * scale[1], 46.0 * scale[0],
              17.0 * scale[1], -34.0 * scale[0], 42.0 * scale[1])
    Curveto_r(-60.0 * scale[0], 18.0 * scale[1], -174.0 * scale[0],
              26.0 * scale[1], -174.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 78.0 * scale[0], -
              32.0 * scale[1], 135.0 * scale[0], -45.0 * scale[1])
    Curveto_r(11.0 * scale[0], -3.0 * scale[1], 0.0 * scale[0], -
              4.0 * scale[1], -25.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 2.0 * scale[1], -72.0 * scale[0],
              16.0 * scale[1], -105.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-47.0 * scale[0], 22.0 * scale[1], -78.0 * scale[0],
              29.0 * scale[1], -144.0 * scale[0], 32.0 * scale[1])
    Lineto_r(-85.0 * scale[0], 4.0 * scale[1])
    Lineto_r(20.0 * scale[0], -22.0 * scale[1])
    te.end_fill()
    Moveto_r(91.0 * scale[0], -35.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 17.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(-194.0 * scale[0], -31.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -21.0 *
              scale[0], -2.0 * scale[1], -30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 3.0 * scale[1], -4.0 * scale[0],
              5.0 * scale[1], 12.0 * scale[0], 5.0 * scale[1])
    Curveto_r(17.0 * scale[0], 0.0 * scale[1], 24.0 * scale[0], -
              2.0 * scale[1], 18.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(80.0 * scale[0], -10.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              5.0 * scale[1], 12.0 * scale[0], 5.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(34.0 * scale[0], -199.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 17.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(880.0 * scale[0], 1326.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(241.0 * scale[0], 1221.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-66.0 * scale[0], -18.0 * scale[1], -13.0 *
              scale[0], -46.0 * scale[1], 109.0 * scale[0], -58.0 * scale[1])
    Curveto_r(64.0 * scale[0], -6.0 * scale[1], 65.0 *
              scale[0], -6.0 * scale[1], 47.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 11.0 * scale[1], -14.0 * scale[0],
              23.0 * scale[1], -11.0 * scale[0], 26.0 * scale[1])
    Curveto_r(20.0 * scale[0], 20.0 * scale[1], -91.0 * scale[0],
              33.0 * scale[1], -145.0 * scale[0], 18.0 * scale[1])
    te.end_fill()
    Moveto(168.0 * scale[0], 1114.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(13.0 * scale[0], -9.0 * scale[1], 26.0 * scale[0], -
              14.0 * scale[1], 29.0 * scale[0], -10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 12.0 * scale[0], -
              1.0 * scale[1], 20.0 * scale[0], -9.0 * scale[1])
    Curveto_r(18.0 * scale[0], -19.0 * scale[1], 87.0 * scale[0], -
              37.0 * scale[1], 121.0 * scale[0], -32.0 * scale[1])
    Curveto_r(24.0 * scale[0], 3.0 * scale[1], 25.0 * scale[0],
              4.0 * scale[1], 7.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 4.0 * scale[1], -28.0 * scale[0],
              12.0 * scale[1], -37.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 8.0 * scale[1], -80.0 * scale[0],
              25.0 * scale[1], -138.0 * scale[0], 35.0 * scale[1])
    Lineto_r(-25.0 * scale[0], 5.0 * scale[1])
    Lineto_r(23.0 * scale[0], -17.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#200d0c')
    te.end_fill()
    Moveto(905.0 * scale[0], 1401.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(22.0 * scale[0], -4.0 * scale[1], 46.0 * scale[0], -
              11.0 * scale[1], 54.0 * scale[0], -15.0 * scale[1])
    Curveto_r(9.0 * scale[0], -6.0 * scale[1], 12.0 *
              scale[0], -5.0 * scale[1], 9.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -22.0 * scale[0],
              15.0 * scale[1], -54.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-48.0 * scale[0], 1.0 * scale[1], -48.0 * scale[0],
              1.0 * scale[1], -9.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(10.0 * scale[0], 1385.0 * scale[1], x, y)
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
    Moveto(11.0 * scale[0], 1214.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(0.0 * scale[0], 1130.0 * scale[1], x, y)
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
    Moveto(0.0 * scale[0], 1081.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -20.0 * scale[1], 5.0 * scale[0], -
              31.0 * scale[1], 14.0 * scale[0], -31.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              8.0 * scale[1], 8.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 37.0 * scale[1], -22.0 * scale[0],
              41.0 * scale[1], -22.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(101.0 * scale[0], 973.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(28.0 * scale[0], -35.0 * scale[1], 54.0 * scale[0], -
              52.0 * scale[1], 173.0 * scale[0], -114.0 * scale[1])
    Curveto_r(49.0 * scale[0], -25.0 * scale[1], 85.0 * scale[0], -
              48.0 * scale[1], 80.0 * scale[0], -52.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -3.0 * scale[1], -34.0 * scale[0],
              8.0 * scale[1], -63.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-41.0 * scale[0], 22.0 * scale[1], -57.0 * scale[0],
              26.0 * scale[1], -68.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -6.0 * scale[1], -13.0 *
              scale[0], -8.0 * scale[1], -14.0 * scale[0], -3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -5.0 * scale[0], -
              4.0 * scale[1], -10.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -19.0 * scale[1], -5.0 *
              scale[0], -31.0 * scale[1], 2.0 * scale[0], -36.0 * scale[1])
    Curveto_r(18.0 * scale[0], -11.0 * scale[1], -36.0 * scale[0], -
              19.0 * scale[1], -88.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-34.0 * scale[0], 4.0 * scale[1], -42.0 * scale[0],
              3.0 * scale[1], -28.0 * scale[0], -4.0 * scale[1])
    Curveto_r(11.0 * scale[0], -5.0 * scale[1], 33.0 * scale[0], -
              10.0 * scale[1], 48.0 * scale[0], -10.0 * scale[1])
    Curveto_r(23.0 * scale[0], -1.0 * scale[1], 27.0 * scale[0], -
              4.0 * scale[1], 22.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -11.0 * scale[1], -1.0 *
              scale[0], -22.0 * scale[1], 5.0 * scale[0], -26.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 10.0 * scale[0],
              3.0 * scale[1], 10.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], 6.0 * scale[0],
              21.0 * scale[1], 20.0 * scale[0], 21.0 * scale[1])
    Curveto_r(29.0 * scale[0], 0.0 * scale[1], 25.0 * scale[0], -
              31.0 * scale[1], -8.0 * scale[0], -68.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -21.0 * scale[1], -28.0 *
              scale[0], -43.0 * scale[1], -29.0 * scale[0], -69.0 * scale[1])
    Lineto_r(-2.0 * scale[0], -38.0 * scale[1])
    Lineto_r(12.0 * scale[0], 36.0 * scale[1])
    Curveto_r(13.0 * scale[0], 40.0 * scale[1], 49.0 * scale[0],
              89.0 * scale[1], 65.0 * scale[0], 89.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0],
              10.0 * scale[1], 18.0 * scale[0], 23.0 * scale[1])
    Curveto_r(9.0 * scale[0], 29.0 * scale[1], 38.0 * scale[0],
              57.0 * scale[1], 60.0 * scale[0], 57.0 * scale[1])
    Curveto_r(23.0 * scale[0], 0.0 * scale[1], 94.0 * scale[0],
              32.0 * scale[1], 94.0 * scale[0], 42.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], -4.0 * scale[0],
              8.0 * scale[1], -8.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 0.0 * scale[1], -215.0 * scale[0],
              109.0 * scale[1], -222.0 * scale[0], 118.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -25.0 * scale[0],
              18.0 * scale[1], -49.0 * scale[0], 31.0 * scale[1])
    Lineto_r(-45.0 * scale[0], 24.0 * scale[1])
    Lineto_r(25.0 * scale[0], -30.0 * scale[1])
    te.end_fill()
    Moveto_r(134.0 * scale[0], -243.0 * scale[1], 0, 0)
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
    Moveto(878.0 * scale[0], 983.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(905.0 * scale[0], 930.0 * scale[1], x, y)
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
    Moveto(270.0 * scale[0], 921.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(8.0 * scale[0], -5.0 * scale[1], 31.0 * scale[0], -
              11.0 * scale[1], 50.0 * scale[0], -15.0 * scale[1])
    Lineto_r(35.0 * scale[0], -6.0 * scale[1])
    Lineto_r(-35.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-41.0 * scale[0], 17.0 * scale[1], -75.0 * scale[0],
              21.0 * scale[1], -50.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(400.0 * scale[0], 902.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -7.0 * scale[1], 54.0 * scale[0], -
              46.0 * scale[1], 130.0 * scale[0], -95.0 * scale[1])
    Curveto_r(43.0 * scale[0], -28.0 * scale[1], 60.0 * scale[0], -
              60.0 * scale[1], 60.0 * scale[0], -114.0 * scale[1])
    Curveto_r(0.0 * scale[0], -23.0 * scale[1], 5.0 * scale[0], -
              45.0 * scale[1], 10.0 * scale[0], -48.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 10.0 * scale[0],
              11.0 * scale[1], 10.0 * scale[0], 37.0 * scale[1])
    Curveto_r(0.0 * scale[0], 24.0 * scale[1], 5.0 * scale[0],
              50.0 * scale[1], 11.0 * scale[0], 58.0 * scale[1])
    Curveto_r(9.0 * scale[0], 13.0 * scale[1], 10.0 * scale[0],
              12.0 * scale[1], 5.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -10.0 * scale[1], -1.0 *
              scale[0], -18.0 * scale[1], 3.0 * scale[0], -18.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0], -
              7.0 * scale[1], 15.0 * scale[0], -16.0 * scale[1])
    Curveto_r(3.0 * scale[0], -9.0 * scale[1], 2.0 * scale[0], -
              12.0 * scale[1], -5.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -9.0 * scale[0], -
              10.0 * scale[1], -5.0 * scale[0], -42.0 * scale[1])
    Curveto_r(2.0 * scale[0], -27.0 * scale[1], 5.0 * scale[0], -
              70.0 * scale[1], 5.0 * scale[0], -96.0 * scale[1])
    Curveto_r(1.0 * scale[0], -27.0 * scale[1], 6.0 * scale[0], -
              48.0 * scale[1], 12.0 * scale[0], -48.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0],
              28.0 * scale[1], 4.0 * scale[0], 85.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 53.0 * scale[1], -3.0 * scale[0],
              85.0 * scale[1], 3.0 * scale[0], 85.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 4.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -14.0 * scale[1], -1.0 *
              scale[0], -19.0 * scale[1], 6.0 * scale[0], -14.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 10.0 * scale[0],
              2.0 * scale[1], 6.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -10.0 * scale[1], -1.0 *
              scale[0], -16.0 * scale[1], 7.0 * scale[0], -16.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0], -
              3.0 * scale[1], -1.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -8.0 * scale[1], -13.0 *
              scale[0], -10.0 * scale[1], 0.0 * scale[0], -10.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0], -
              3.0 * scale[1], 2.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -14.0 * scale[1], -16.0 *
              scale[0], -32.0 * scale[1], -3.0 * scale[0], -23.0 * scale[1])
    Curveto_r(19.0 * scale[0], 11.0 * scale[1], 34.0 * scale[0], -
              40.0 * scale[1], 33.0 * scale[0], -112.0 * scale[1])
    Curveto_r(0.0 * scale[0], -40.0 * scale[1], 4.0 * scale[0], -
              73.0 * scale[1], 9.0 * scale[0], -73.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              24.0 * scale[1], 9.0 * scale[0], 53.0 * scale[1])
    Curveto_r(0.0 * scale[0], 75.0 * scale[1], 16.0 * scale[0],
              40.0 * scale[1], 19.0 * scale[0], -41.0 * scale[1])
    Curveto_r(1.0 * scale[0], -37.0 * scale[1], 7.0 * scale[0], -
              71.0 * scale[1], 12.0 * scale[0], -77.0 * scale[1])
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 8.0 * scale[0],
              8.0 * scale[1], 4.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 71.0 * scale[1], 12.0 * scale[0],
              48.0 * scale[1], 21.0 * scale[0], -25.0 * scale[1])
    Curveto_r(6.0 * scale[0], -38.0 * scale[1], 9.0 * scale[0], -
              45.0 * scale[1], 15.0 * scale[0], -30.0 * scale[1])
    Curveto_r(7.0 * scale[0], 17.0 * scale[1], 8.0 * scale[0],
              16.0 * scale[1], 8.0 * scale[0], -7.0 * scale[1])
    Curveto_r(1.0 * scale[0], -20.0 * scale[1], 5.0 * scale[0], -
              26.0 * scale[1], 16.0 * scale[0], -22.0 * scale[1])
    Curveto_r(8.0 * scale[0], 4.0 * scale[1], 15.0 * scale[0],
              1.0 * scale[1], 15.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 7.0 * scale[0], -
              11.0 * scale[1], 15.0 * scale[0], -11.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0], -
              5.0 * scale[1], 15.0 * scale[0], -12.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 2.0 * scale[0], -
              9.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -15.0 * scale[0],
              48.0 * scale[1], -41.0 * scale[0], 99.0 * scale[1])
    Curveto_r(-58.0 * scale[0], 116.0 * scale[1], -66.0 * scale[0],
              135.0 * scale[1], -99.0 * scale[0], 229.0 * scale[1])
    Curveto_r(-48.0 * scale[0], 134.0 * scale[1], -56.0 * scale[0],
              155.0 * scale[1], -71.0 * scale[0], 171.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 8.0 * scale[1], -14.0 * scale[0],
              20.0 * scale[1], -14.0 * scale[0], 26.0 * scale[1])
    Curveto_r(0.0 * scale[0], 16.0 * scale[1], -88.0 * scale[0],
              87.0 * scale[1], -130.0 * scale[0], 105.0 * scale[1])
    Curveto_r(-74.0 * scale[0], 33.0 * scale[1], -121.0 * scale[0],
              44.0 * scale[1], -120.0 * scale[0], 30.0 * scale[1])
    te.end_fill()
    Moveto_r(207.0 * scale[0], -154.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -7.0 * scale[1], -5.0 *
              scale[0], -2.0 * scale[1], -5.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], 2.0 * scale[0],
              19.0 * scale[1], 5.0 * scale[0], 13.0 * scale[1])
    Curveto_r(2.0 * scale[0], -7.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 0.0 * scale[0], -25.0 * scale[1])
    te.end_fill()
    Moveto(237.0 * scale[0], 677.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -29.0 * scale[1], -22.0 *
              scale[0], -57.0 * scale[1], -7.0 * scale[0], -57.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              8.0 * scale[1], 10.0 * scale[0], 18.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], 5.0 * scale[0],
              23.0 * scale[1], 11.0 * scale[0], 29.0 * scale[1])
    Curveto_r(6.0 * scale[0], 6.0 * scale[1], 9.0 * scale[0],
              17.0 * scale[1], 7.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 8.0 * scale[1], -11.0 * scale[0],
              2.0 * scale[1], -21.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(304.0 * scale[0], 657.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -26.0 * scale[1], 0.0 * scale[0], -
              72.0 * scale[1], 16.0 * scale[0], -74.0 * scale[1])
    Curveto_r(8.0 * scale[0], -2.0 * scale[1], 24.0 * scale[0],
              4.0 * scale[1], 34.0 * scale[0], 12.0 * scale[1])
    Curveto_r(16.0 * scale[0], 12.0 * scale[1], 18.0 * scale[0],
              20.0 * scale[1], 10.0 * scale[0], 43.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 30.0 * scale[1], -50.0 * scale[0],
              43.0 * scale[1], -60.0 * scale[0], 19.0 * scale[1])
    te.end_fill()
    Moveto_r(41.0 * scale[0], -56.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -8.0 * scale[1], -18.0 * scale[0], -
              11.0 * scale[1], -22.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 5.0 * scale[1], -2.0 * scale[0],
              11.0 * scale[1], 5.0 * scale[0], 13.0 * scale[1])
    Curveto_r(17.0 * scale[0], 6.0 * scale[1], 15.0 * scale[0],
              23.0 * scale[1], -3.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0],
              12.0 * scale[1], -8.0 * scale[0], 24.0 * scale[1])
    Curveto_r(4.0 * scale[0], 4.0 * scale[1], 15.0 * scale[0], -
              3.0 * scale[1], 25.0 * scale[0], -16.0 * scale[1])
    Curveto_r(15.0 * scale[0], -20.0 * scale[1], 15.0 *
              scale[0], -25.0 * scale[1], 3.0 * scale[0], -37.0 * scale[1])
    te.end_fill()
    Moveto(601.0 * scale[0], 574.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(141.0 * scale[0], 520.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -17.0 * scale[1], -24.0 * scale[0], -
              44.0 * scale[1], -38.0 * scale[0], -60.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -17.0 * scale[1], -20.0 *
              scale[0], -30.0 * scale[1], -15.0 * scale[0], -30.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 72.0 * scale[0],
              88.0 * scale[1], 72.0 * scale[0], 107.0 * scale[1])
    Curveto_r(0.0 * scale[0], 20.0 * scale[1], -4.0 * scale[0],
              16.0 * scale[1], -19.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(681.0 * scale[0], 490.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(1.0 * scale[0], -65.0 * scale[1])
    Lineto_r(9.0 * scale[0], 55.0 * scale[1])
    Curveto_r(4.0 * scale[0], 32.0 * scale[1], 4.0 * scale[0],
              59.0 * scale[1], -2.0 * scale[0], 65.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 5.0 * scale[1], -9.0 * scale[0], -
              16.0 * scale[1], -8.0 * scale[0], -55.0 * scale[1])
    te.end_fill()
    Moveto(152.0 * scale[0], 413.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-23.0 * scale[0], -45.0 * scale[1], -24.0 * scale[0], -
              103.0 * scale[1], -2.0 * scale[0], -103.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 52.0 * scale[0],
              89.0 * scale[1], 46.0 * scale[0], 105.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 20.0 * scale[1], -33.0 * scale[0],
              19.0 * scale[1], -44.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(511.0 * scale[0], 360.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -21.0 * scale[1], -32.0 *
              scale[0], -40.0 * scale[1], -41.0 * scale[0], -43.0 * scale[1])
    Curveto_r(-22.0 * scale[0], -6.0 * scale[1], -66.0 * scale[0], -
              147.0 * scale[1], -75.0 * scale[0], -238.0 * scale[1])
    Lineto_r(-6.0 * scale[0], -66.0 * scale[1])
    Lineto_r(177.0 * scale[0], -7.0 * scale[1])
    Curveto_r(158.0 * scale[0], -6.0 * scale[1], 197.0 *
              scale[0], -4.0 * scale[1], 183.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 4.0 * scale[1], -227.0 * scale[0],
              19.0 * scale[1], -292.0 * scale[0], 19.0 * scale[1])
    Lineto_r(-48.0 * scale[0], 0.0 * scale[1])
    Lineto_r(7.0 * scale[0], 55.0 * scale[1])
    Curveto_r(7.0 * scale[0], 60.0 * scale[1], 41.0 * scale[0],
              152.0 * scale[1], 67.0 * scale[0], 182.0 * scale[1])
    Curveto_r(8.0 * scale[0], 10.0 * scale[1], 13.0 * scale[0],
              21.0 * scale[1], 10.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              6.0 * scale[1], 5.0 * scale[0], 6.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 48.0 * scale[0],
              87.0 * scale[1], 41.0 * scale[0], 94.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 2.0 * scale[1], -15.0 * scale[0], -
              13.0 * scale[1], -28.0 * scale[0], -34.0 * scale[1])
    te.end_fill()
    Moveto(23.0 * scale[0], 345.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -22.0 * scale[1], 2.0 * scale[0], -
              30.0 * scale[1], 4.0 * scale[0], -17.0 * scale[1])
    Curveto_r(2.0 * scale[0], 12.0 * scale[1], 2.0 * scale[0],
              30.0 * scale[1], 0.0 * scale[0], 40.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -4.0 * scale[0], -23.0 * scale[1])
    te.end_fill()
    Moveto(391.0 * scale[0], 307.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -5.0 * scale[1], -33.0 * scale[0], -
              10.0 * scale[1], -61.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-51.0 * scale[0], -2.0 * scale[1], -90.0 * scale[0], -
              22.0 * scale[1], -90.0 * scale[0], -46.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], 8.0 * scale[0], -
              5.0 * scale[1], 19.0 * scale[0], 5.0 * scale[1])
    Curveto_r(11.0 * scale[0], 10.0 * scale[1], 41.0 * scale[0],
              19.0 * scale[1], 75.0 * scale[0], 21.0 * scale[1])
    Curveto_r(56.0 * scale[0], 5.0 * scale[1], 96.0 * scale[0],
              18.0 * scale[1], 96.0 * scale[0], 34.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], -27.0 * scale[0],
              10.0 * scale[1], -39.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(45.0 * scale[0], 263.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(18.0 * scale[0], -42.0 * scale[1], 25.0 * scale[0], -
              52.0 * scale[1], 25.0 * scale[0], -34.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -28.0 * scale[0],
              71.0 * scale[1], -35.0 * scale[0], 71.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], 2.0 * scale[0], -
              17.0 * scale[1], 10.0 * scale[0], -37.0 * scale[1])
    te.end_fill()
    Moveto(85.0 * scale[0], 210.0 * scale[1], x, y)
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
    Moveto(110.0 * scale[0], 196.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 7.0 * scale[0], -
              7.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 12.0 *
              scale[0], -2.0 * scale[1], 9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], -25.0 * scale[0],
              14.0 * scale[1], -25.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(958.0 * scale[0], 117.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -40.0 * scale[1], -1.0 * scale[0], -
              78.0 * scale[1], -6.0 * scale[0], -85.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -7.0 * scale[1], -28.0 * scale[0], -
              15.0 * scale[1], -53.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-61.0 * scale[0], -7.0 * scale[1], -62.0 *
              scale[0], -14.0 * scale[1], -3.0 * scale[0], -14.0 * scale[1])
    Curveto_r(28.0 * scale[0], 0.0 * scale[1], 55.0 * scale[0],
              5.0 * scale[1], 62.0 * scale[0], 12.0 * scale[1])
    Curveto_r(13.0 * scale[0], 13.0 * scale[1], 17.0 * scale[0],
              164.0 * scale[1], 4.0 * scale[0], 172.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 2.0 * scale[1], -6.0 * scale[0], -
              28.0 * scale[1], -4.0 * scale[0], -67.0 * scale[1])
    te.end_fill()
    Moveto(770.0 * scale[0], 10.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0], -
              10.0 * scale[1], 10.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              5.0 * scale[1], 10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -4.0 * scale[0],
              10.0 * scale[1], -10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              4.0 * scale[1], -10.0 * scale[0], -10.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#906498')
    te.end_fill()
    Moveto(464.0 * scale[0], 1319.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], 1.0 * scale[0], -
              9.0 * scale[1], 13.0 * scale[0], -7.0 * scale[1])
    Curveto_r(10.0 * scale[0], 1.0 * scale[1], 31.0 * scale[0], -
              5.0 * scale[1], 45.0 * scale[0], -14.0 * scale[1])
    Curveto_r(14.0 * scale[0], -9.0 * scale[1], 28.0 * scale[0], -
              14.0 * scale[1], 31.0 * scale[0], -11.0 * scale[1])
    Curveto_r(6.0 * scale[0], 5.0 * scale[1], -59.0 * scale[0],
              43.0 * scale[1], -75.0 * scale[0], 43.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              5.0 * scale[1], -14.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(420.0 * scale[0], 1290.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-21.0 * scale[0], -21.0 * scale[1], -27.0 *
              scale[0], -50.0 * scale[1], -11.0 * scale[0], -50.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              5.0 * scale[1], 17.0 * scale[0], 12.0 * scale[1])
    Curveto_r(5.0 * scale[0], 7.0 * scale[1], 3.0 * scale[0],
              8.0 * scale[1], -6.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -6.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -7.0 * scale[0], 9.0 * scale[1])
    Curveto_r(4.0 * scale[0], 10.0 * scale[1], 7.0 * scale[0],
              20.0 * scale[1], 7.0 * scale[0], 22.0 * scale[1])
    Curveto_r(0.0 * scale[0], 2.0 * scale[1], 7.0 * scale[0],
              4.0 * scale[1], 15.0 * scale[0], 4.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 15.0 * scale[1], -8.0 * scale[0],
              12.0 * scale[1], -30.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(545.0 * scale[0], 1244.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], 3.0 * scale[0], -
              24.0 * scale[1], 8.0 * scale[0], -24.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              9.0 * scale[1], 7.0 * scale[0], 19.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], -3.0 * scale[0],
              22.0 * scale[1], -7.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -8.0 * scale[0], -
              6.0 * scale[1], -8.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(581.0 * scale[0], 1244.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(71.0 * scale[0], 1224.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(95.0 * scale[0], 1229.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -16.0 * scale[1], -1.0 *
              scale[0], -19.0 * scale[1], 13.0 * scale[0], -3.0 * scale[1])
    Curveto_r(7.0 * scale[0], 8.0 * scale[1], 8.0 * scale[0],
              14.0 * scale[1], 3.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              5.0 * scale[1], -16.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(400.0 * scale[0], 1221.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 6.0 * scale[0], -
              14.0 * scale[1], 14.0 * scale[0], -20.0 * scale[1])
    Curveto_r(12.0 * scale[0], -10.0 * scale[1], 13.0 *
              scale[0], -8.0 * scale[1], 9.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 21.0 * scale[1], -23.0 * scale[0],
              30.0 * scale[1], -23.0 * scale[0], 12.0 * scale[1])
    te.end_fill()
    Moveto(886.0 * scale[0], 1219.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 12.0 * scale[0], -
              9.0 * scale[1], 21.0 * scale[0], -9.0 * scale[1])
    Curveto_r(19.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              13.0 * scale[1], -12.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 1.0 * scale[1], -13.0 *
              scale[0], -2.0 * scale[1], -9.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(150.0 * scale[0], 1210.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], -8.0 * scale[0], -
              23.0 * scale[1], -18.0 * scale[0], -31.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -15.0 * scale[1], -20.0 *
              scale[0], -15.0 * scale[1], -31.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 12.0 * scale[1], -10.0 * scale[0],
              12.0 * scale[1], -6.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], -8.0 * scale[1], -1.0 *
              scale[0], -6.0 * scale[1], -9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -16.0 * scale[0],
              17.0 * scale[1], -16.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -25.0 * scale[1], 30.0 * scale[0], -
              40.0 * scale[1], 55.0 * scale[0], -28.0 * scale[1])
    Curveto_r(3.0 * scale[0], 1.0 * scale[1], 10.0 * scale[0],
              3.0 * scale[1], 15.0 * scale[0], 4.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              4.0 * scale[1], 8.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 4.0 * scale[1], 6.0 * scale[0],
              14.0 * scale[1], 17.0 * scale[0], 22.0 * scale[1])
    Curveto_r(11.0 * scale[0], 8.0 * scale[1], 17.0 * scale[0],
              18.0 * scale[1], 12.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 4.0 * scale[1], -7.0 * scale[0],
              1.0 * scale[1], -7.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], -2.0 * scale[0], -
              11.0 * scale[1], -10.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 13.0 * scale[1], -10.0 * scale[0],
              13.0 * scale[1], -10.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(550.0 * scale[0], 1192.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(11.0 * scale[0], -22.0 * scale[1], 31.0 *
              scale[0], -22.0 * scale[1], 29.0 * scale[0], 1.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -2.0 * scale[0],
              8.0 * scale[1], -6.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -10.0 * scale[1], -9.0 *
              scale[0], -9.0 * scale[1], -20.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 17.0 * scale[1], -13.0 * scale[0],
              16.0 * scale[1], -3.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(817.0 * scale[0], 1196.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -11.0 * scale[1], -3.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 9.0 * scale[0],
              2.0 * scale[1], 5.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -10.0 * scale[1], -3.0 *
              scale[0], -15.0 * scale[1], 3.0 * scale[0], -11.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 10.0 * scale[0],
              1.0 * scale[1], 10.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 9.0 * scale[0], -
              11.0 * scale[1], 20.0 * scale[0], -11.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0],
              5.0 * scale[1], 20.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 3.0 * scale[0],
              9.0 * scale[1], 8.0 * scale[0], 8.0 * scale[1])
    Curveto_r(4.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0],
              1.0 * scale[1], 9.0 * scale[0], 6.0 * scale[1])
    Curveto_r(1.0 * scale[0], 5.0 * scale[1], 7.0 * scale[0],
              13.0 * scale[1], 15.0 * scale[0], 17.0 * scale[1])
    Curveto_r(10.0 * scale[0], 7.0 * scale[1], 9.0 * scale[0],
              9.0 * scale[1], -3.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -22.0 * scale[0], -
              7.0 * scale[1], -29.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -21.0 * scale[1], -35.0 *
              scale[0], -19.0 * scale[1], -47.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 19.0 * scale[1], -10.0 * scale[0],
              20.0 * scale[1], -16.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(17.0 * scale[0], 1033.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -9.0 * scale[1], -8.0 *
              scale[0], -51.0 * scale[1], 2.0 * scale[0], -57.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 12.0 * scale[0],
              1.0 * scale[1], 15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], 10.0 * scale[0],
              12.0 * scale[1], 16.0 * scale[0], 9.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 21.0 * scale[1], 4.0 * scale[0],
              20.0 * scale[1], 45.0 * scale[0], -5.0 * scale[1])
    Curveto_r(19.0 * scale[0], -12.0 * scale[1], 50.0 * scale[0], -
              21.0 * scale[1], 69.0 * scale[0], -21.0 * scale[1])
    Curveto_r(21.0 * scale[0], 0.0 * scale[1], 30.0 * scale[0], -
              3.0 * scale[1], 23.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -5.0 * scale[1], -5.0 * scale[0], -
              9.0 * scale[1], 12.0 * scale[0], -14.0 * scale[1])
    Curveto_r(14.0 * scale[0], -3.0 * scale[1], 32.0 * scale[0], -
              9.0 * scale[1], 41.0 * scale[0], -12.0 * scale[1])
    Curveto_r(9.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -1.0 * scale[1], 16.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -12.0 * scale[0],
              12.0 * scale[1], -27.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 1.0 * scale[1], -21.0 * scale[0],
              3.0 * scale[1], -10.0 * scale[0], 6.0 * scale[1])
    Curveto_r(9.0 * scale[0], 2.0 * scale[1], 15.0 * scale[0],
              9.0 * scale[1], 11.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], -10.0 * scale[0],
              7.0 * scale[1], -15.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -4.0 * scale[1], -9.0 *
              scale[0], -1.0 * scale[1], -9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -8.0 * scale[0],
              11.0 * scale[1], -17.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0],
              2.0 * scale[1], -3.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 26.0 * scale[0],
              9.0 * scale[1], 40.0 * scale[0], 9.0 * scale[1])
    Lineto_r(25.0 * scale[0], -1.0 * scale[1])
    Lineto_r(-25.0 * scale[0], -8.0 * scale[1])
    Lineto_r(-25.0 * scale[0], -8.0 * scale[1])
    Lineto_r(28.0 * scale[0], -1.0 * scale[1])
    Curveto_r(18.0 * scale[0], -1.0 * scale[1], 27.0 * scale[0], -
              6.0 * scale[1], 27.0 * scale[0], -18.0 * scale[1])
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 4.0 * scale[0], -
              12.0 * scale[1], 17.0 * scale[0], 7.0 * scale[1])
    Curveto_r(9.0 * scale[0], 14.0 * scale[1], 18.0 * scale[0],
              27.0 * scale[1], 20.0 * scale[0], 29.0 * scale[1])
    Curveto_r(1.0 * scale[0], 2.0 * scale[1], 20.0 * scale[0],
              7.0 * scale[1], 40.0 * scale[0], 11.0 * scale[1])
    Curveto_r(23.0 * scale[0], 5.0 * scale[1], -33.0 * scale[0],
              8.0 * scale[1], -138.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-97.0 * scale[0], 0.0 * scale[1], -179.0 *
              scale[0], -2.0 * scale[1], -182.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(594.0 * scale[0], 1032.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -7.0 * scale[1], 13.0 * scale[0], -
              12.0 * scale[1], 20.0 * scale[0], -12.0 * scale[1])
    Curveto_r(15.0 * scale[0], 0.0 * scale[1], 126.0 * scale[0], -
              103.0 * scale[1], 126.0 * scale[0], -117.0 * scale[1])
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], 25.0 * scale[0], -
              24.0 * scale[1], 59.0 * scale[0], -29.0 * scale[1])
    Curveto_r(13.0 * scale[0], -2.0 * scale[1], 27.0 * scale[0], -
              8.0 * scale[1], 31.0 * scale[0], -14.0 * scale[1])
    Curveto_r(5.0 * scale[0], -8.0 * scale[1], 9.0 * scale[0], -
              6.0 * scale[1], 14.0 * scale[0], 6.0 * scale[1])
    Curveto_r(4.0 * scale[0], 9.0 * scale[1], 1.0 * scale[0],
              22.0 * scale[1], -5.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 8.0 * scale[1], -10.0 * scale[0],
              7.0 * scale[1], -4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(4.0 * scale[0], -8.0 * scale[1], -3.0 * scale[0], -
              5.0 * scale[1], -16.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 18.0 * scale[1], -21.0 * scale[0],
              24.0 * scale[1], -10.0 * scale[0], 31.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 11.0 * scale[0],
              16.0 * scale[1], 6.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 21.0 * scale[1], 13.0 * scale[0],
              51.0 * scale[1], 34.0 * scale[0], 51.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              5.0 * scale[1], 11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -41.0 * scale[0],
              10.0 * scale[1], -104.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-57.0 * scale[0], 0.0 * scale[1], -118.0 * scale[0],
              3.0 * scale[1], -136.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 4.0 * scale[1], -31.0 * scale[0],
              3.0 * scale[1], -26.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(913.0 * scale[0], 1014.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-15.0 * scale[0], -12.0 * scale[1], -15.0 *
              scale[0], -13.0 * scale[1], -2.0 * scale[0], -8.0 * scale[1])
    Curveto_r(10.0 * scale[0], 3.0 * scale[1], 20.0 * scale[0],
              0.0 * scale[1], 25.0 * scale[0], -7.0 * scale[1])
    Curveto_r(5.0 * scale[0], -8.0 * scale[1], 3.0 * scale[0], -
              10.0 * scale[1], -7.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -11.0 * scale[0],
              4.0 * scale[1], -6.0 * scale[0], -1.0 * scale[1])
    Curveto_r(5.0 * scale[0], -5.0 * scale[1], 12.0 * scale[0], -
              9.0 * scale[1], 15.0 * scale[0], -9.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0], -
              3.0 * scale[1], 17.0 * scale[0], -7.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 11.0 * scale[0],
              4.0 * scale[1], 11.0 * scale[0], 17.0 * scale[1])
    Curveto_r(2.0 * scale[0], 28.0 * scale[1], -27.0 * scale[0],
              39.0 * scale[1], -53.0 * scale[0], 19.0 * scale[1])
    te.end_fill()
    Moveto(868.0 * scale[0], 973.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(288.0 * scale[0], 933.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(955.0 * scale[0], 930.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              10.0 * scale[1], -5.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              4.0 * scale[1], -6.0 * scale[0], -9.0 * scale[1])
    Curveto_r(8.0 * scale[0], -12.0 * scale[1], -31.0 * scale[0], -
              44.0 * scale[1], -43.0 * scale[0], -36.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 8.0 * scale[1], -51.0 * scale[0], -
              3.0 * scale[1], -51.0 * scale[0], -15.0 * scale[1])
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], 56.0 * scale[0], -
              29.0 * scale[1], 80.0 * scale[0], -23.0 * scale[1])
    Curveto_r(20.0 * scale[0], 5.0 * scale[1], 22.0 * scale[0],
              3.0 * scale[1], 15.0 * scale[0], -26.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -19.0 * scale[1], -3.0 *
              scale[0], -31.0 * scale[1], 4.0 * scale[0], -31.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0], -
              26.0 * scale[1], 14.0 * scale[0], -57.0 * scale[1])
    Curveto_r(2.0 * scale[0], -32.0 * scale[1], 4.0 * scale[0],
              4.0 * scale[1], 5.0 * scale[0], 80.0 * scale[1])
    Curveto_r(1.0 * scale[0], 91.0 * scale[1], -2.0 * scale[0],
              137.0 * scale[1], -9.0 * scale[0], 137.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              4.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(131.0 * scale[0], 922.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -7.0 * scale[1], -6.0 * scale[0], -
              10.0 * scale[1], -11.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -9.0 * scale[0],
              1.0 * scale[1], -8.0 * scale[0], -6.0 * scale[1])
    Curveto_r(2.0 * scale[0], -7.0 * scale[1], -2.0 * scale[0], -
              13.0 * scale[1], -9.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              3.0 * scale[1], -19.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -15.0 * scale[1], -43.0 *
              scale[0], -8.0 * scale[1], -57.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 19.0 * scale[1], -15.0 * scale[0],
              16.0 * scale[1], -15.0 * scale[0], -36.0 * scale[1])
    Curveto_r(1.0 * scale[0], -30.0 * scale[1], 5.0 * scale[0], -
              58.0 * scale[1], 10.0 * scale[0], -61.0 * scale[1])
    Curveto_r(5.0 * scale[0], -4.0 * scale[1], 44.0 *
              scale[0], -3.0 * scale[1], 86.0 * scale[0], 2.0 * scale[1])
    Curveto_r(42.0 * scale[0], 4.0 * scale[1], 70.0 * scale[0],
              9.0 * scale[1], 61.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 2.0 * scale[1], -23.0 * scale[0],
              20.0 * scale[1], -32.0 * scale[0], 39.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 42.0 * scale[1], -21.0 * scale[0],
              45.0 * scale[1], -2.0 * scale[0], 38.0 * scale[1])
    Curveto_r(8.0 * scale[0], -4.0 * scale[1], 12.0 * scale[0], -
              11.0 * scale[1], 8.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], -1.0 *
              scale[0], -7.0 * scale[1], 6.0 * scale[0], -3.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 9.0 * scale[0],
              12.0 * scale[1], 3.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 7.0 * scale[1], -12.0 * scale[0],
              19.0 * scale[1], -15.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 10.0 * scale[1], -6.0 * scale[0],
              11.0 * scale[1], -6.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto_r(-21.0 * scale[0], -47.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(11.0 * scale[0], -13.0 * scale[1], 10.0 *
              scale[0], -14.0 * scale[1], -4.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 3.0 * scale[1], -16.0 * scale[0],
              10.0 * scale[1], -16.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], 6.0 * scale[0],
              11.0 * scale[1], 20.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(355.0 * scale[0], 920.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -12.0 * scale[1], 2.0 *
              scale[0], -12.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(19.0 * scale[0], 8.0 * scale[1], 19.0 * scale[0],
              9.0 * scale[1], -2.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 1.0 * scale[1], -25.0 *
              scale[0], -3.0 * scale[1], -28.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(410.0 * scale[0], 919.0 * scale[1], x, y)
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
    Moveto(450.0 * scale[0], 922.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 9.0 * scale[0], -
              12.0 * scale[1], 20.0 * scale[0], -15.0 * scale[1])
    Curveto_r(11.0 * scale[0], -3.0 * scale[1], 20.0 *
              scale[0], -3.0 * scale[1], 20.0 * scale[0], -1.0 * scale[1])
    Curveto_r(0.0 * scale[0], 2.0 * scale[1], -9.0 * scale[0],
              8.0 * scale[1], -20.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 6.0 * scale[1], -20.0 * scale[0],
              7.0 * scale[1], -20.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(182.0 * scale[0], 881.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -7.0 * scale[1], -10.0 *
              scale[0], -10.0 * scale[1], 3.0 * scale[0], -15.0 * scale[1])
    Curveto_r(24.0 * scale[0], -9.0 * scale[1], 35.0 *
              scale[0], -8.0 * scale[1], 35.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -7.0 * scale[0],
              6.0 * scale[1], -17.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -4.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -9.0 * scale[0], 5.0 * scale[1])
    Curveto_r(8.0 * scale[0], 14.0 * scale[1], 6.0 * scale[0],
              15.0 * scale[1], -12.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(170.0 * scale[0], 840.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -7.0 * scale[1], -10.0 *
              scale[0], -9.0 * scale[1], 8.0 * scale[0], -7.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 22.0 * scale[0],
              5.0 * scale[1], 22.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], -12.0 * scale[0],
              10.0 * scale[1], -30.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(10.0 * scale[0], 763.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], -2.0 * scale[0], -
              92.0 * scale[1], -4.0 * scale[0], -183.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -120.0 * scale[1], -2.0 *
              scale[0], -136.0 * scale[1], 3.0 * scale[0], -60.0 * scale[1])
    Curveto_r(4.0 * scale[0], 61.0 * scale[1], 12.0 * scale[0],
              114.0 * scale[1], 20.0 * scale[0], 126.0 * scale[1])
    Curveto_r(15.0 * scale[0], 23.0 * scale[1], 74.0 * scale[0],
              66.0 * scale[1], 87.0 * scale[0], 63.0 * scale[1])
    Curveto_r(23.0 * scale[0], -4.0 * scale[1], 35.0 * scale[0],
              2.0 * scale[1], 32.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 10.0 * scale[1], -26.0 * scale[0],
              24.0 * scale[1], -63.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-74.0 * scale[0], 23.0 * scale[1], -75.0 * scale[0],
              23.0 * scale[1], -75.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(176.0 * scale[0], 728.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              16.0 * scale[1], -12.0 * scale[0], -24.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -13.0 * scale[1], -18.0 *
              scale[0], -14.0 * scale[1], 1.0 * scale[0], -7.0 * scale[1])
    Curveto_r(32.0 * scale[0], 11.0 * scale[1], 47.0 * scale[0],
              40.0 * scale[1], 20.0 * scale[0], 40.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -9.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(281.0 * scale[0], 614.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(207.0 * scale[0], 386.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -10.0 * scale[1], -1.0 *
              scale[0], -13.0 * scale[1], 8.0 * scale[0], -9.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 12.0 * scale[0],
              9.0 * scale[1], 9.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 12.0 * scale[1], -11.0 * scale[0],
              11.0 * scale[1], -17.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(217.0 * scale[0], 311.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -17.0 * scale[1], -3.0 *
              scale[0], -21.0 * scale[1], 5.0 * scale[0], -13.0 * scale[1])
    Curveto_r(5.0 * scale[0], 5.0 * scale[1], 8.0 * scale[0],
              16.0 * scale[1], 6.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], -7.0 * scale[0],
              3.0 * scale[1], -11.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(146.0 * scale[0], 282.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 * scale[0], -
              13.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(23.0 * scale[0], -9.0 * scale[1], 28.0 *
              scale[0], -2.0 * scale[1], 10.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 7.0 * scale[1], -17.0 * scale[0],
              8.0 * scale[1], -20.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(19.0 * scale[0], 17.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -5.0 * scale[1], 26.0 * scale[0], -
              7.0 * scale[1], 47.0 * scale[0], -5.0 * scale[1])
    Lineto_r(39.0 * scale[0], 3.0 * scale[1])
    Lineto_r(-47.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-26.0 * scale[0], 3.0 * scale[1], -43.0 * scale[0],
              1.0 * scale[1], -39.0 * scale[0], -3.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#483026')
    te.end_fill()
    Moveto(21.0 * scale[0], 1403.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -20.0 * scale[1], -2.0 * scale[0], -
              34.0 * scale[1], -10.0 * scale[0], -29.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0], -
              46.0 * scale[1], -10.0 * scale[0], -114.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -85.0 * scale[1], 2.0 * scale[0], -
              120.0 * scale[1], 10.0 * scale[0], -120.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              8.0 * scale[1], 6.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 18.0 * scale[1], -4.0 * scale[0],
              18.0 * scale[1], 19.0 * scale[0], 3.0 * scale[1])
    Curveto_r(13.0 * scale[0], -8.0 * scale[1], 24.0 * scale[0], -
              22.0 * scale[1], 24.0 * scale[0], -29.0 * scale[1])
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], 12.0 * scale[0], -
              16.0 * scale[1], 36.0 * scale[0], -13.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0], -
              5.0 * scale[1], 16.0 * scale[0], -13.0 * scale[1])
    Curveto_r(8.0 * scale[0], -10.0 * scale[1], 9.0 *
              scale[0], -10.0 * scale[1], 5.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 8.0 * scale[1], -13.0 * scale[0],
              16.0 * scale[1], -24.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 3.0 * scale[1], -43.0 * scale[0],
              40.0 * scale[1], -43.0 * scale[0], 72.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], -4.0 * scale[0],
              20.0 * scale[1], -10.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0],
              8.0 * scale[1], -10.0 * scale[0], 18.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], 2.0 * scale[0],
              15.0 * scale[1], 10.0 * scale[0], 2.0 * scale[1])
    Curveto_r(7.0 * scale[0], -11.0 * scale[1], 10.0 * scale[0], -
              12.0 * scale[1], 10.0 * scale[0], -2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -9.0 * scale[0],
              16.0 * scale[1], -20.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 5.0 * scale[1], -28.0 * scale[0],
              23.0 * scale[1], -10.0 * scale[0], 23.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              5.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -3.0 * scale[0],
              8.0 * scale[1], -7.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -9.0 * scale[0],
              6.0 * scale[1], -10.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 16.0 * scale[1], 2.0 * scale[0],
              21.0 * scale[1], 7.0 * scale[0], 13.0 * scale[1])
    Curveto_r(5.0 * scale[0], -8.0 * scale[1], 10.0 * scale[0], -
              8.0 * scale[1], 14.0 * scale[0], -2.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 1.0 * scale[0],
              12.0 * scale[1], -6.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 8.0 * scale[1], 18.0 * scale[0],
              56.0 * scale[1], 49.0 * scale[0], 61.0 * scale[1])
    Curveto_r(20.0 * scale[0], 3.0 * scale[1], 16.0 * scale[0],
              4.0 * scale[1], -14.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 0.0 * scale[1], -42.0 *
              scale[0], -2.0 * scale[1], -42.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto_r(-4.0 * scale[0], -195.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -6.0 *
              scale[0], -5.0 * scale[1], -6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 11.0 * scale[1], 2.0 * scale[0],
              17.0 * scale[1], 5.0 * scale[0], 13.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 4.0 * scale[0], -
              12.0 * scale[1], 1.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(728.0 * scale[0], 1403.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(808.0 * scale[0], 1403.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 32.0 *
              scale[0], -2.0 * scale[1], 45.0 * scale[0], 0.0 * scale[1])
    Curveto_r(12.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              4.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 0.0 * scale[1], -35.0 *
              scale[0], -2.0 * scale[1], -22.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(908.0 * scale[0], 1393.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(956.0 * scale[0], 1363.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -38.0 * scale[1], 14.0 * scale[0], -
              42.0 * scale[1], 14.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -5.0 * scale[0],
              29.0 * scale[1], -10.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -8.0 * scale[0], -
              3.0 * scale[1], -4.0 * scale[0], -22.0 * scale[1])
    te.end_fill()
    Moveto(66.0 * scale[0], 1328.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 10.0 * scale[0], -
              6.0 * scale[1], 15.0 * scale[0], -3.0 * scale[1])
    Curveto_r(13.0 * scale[0], 9.0 * scale[1], 11.0 * scale[0],
              12.0 * scale[1], -6.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -9.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(150.0 * scale[0], 1330.0 * scale[1], x, y)
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
    Moveto(908.0 * scale[0], 1273.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(922.0 * scale[0], 1246.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -8.0 * scale[1], 15.0 * scale[0], -
              12.0 * scale[1], 17.0 * scale[0], -11.0 * scale[1])
    Curveto_r(5.0 * scale[0], 6.0 * scale[1], -10.0 * scale[0],
              25.0 * scale[1], -20.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              6.0 * scale[1], 3.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(940.0 * scale[0], 1212.0 * scale[1], x, y)
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
    Moveto(925.0 * scale[0], 1168.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -13.0 * scale[1], -21.0 * scale[0], -
              28.0 * scale[1], -35.0 * scale[0], -35.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -8.0 * scale[1], -19.0 *
              scale[0], -13.0 * scale[1], -9.0 * scale[0], -13.0 * scale[1])
    Curveto_r(20.0 * scale[0], 0.0 * scale[1], 59.0 * scale[0],
              36.0 * scale[1], 59.0 * scale[0], 55.0 * scale[1])
    Curveto_r(0.0 * scale[0], 21.0 * scale[1], -4.0 * scale[0],
              19.0 * scale[1], -15.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(961.0 * scale[0], 1174.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(13.0 * scale[0], 1123.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -3.0 * scale[1], -9.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -21.0 * scale[1])
    Curveto_r(5.0 * scale[0], -9.0 * scale[1], 11.0 * scale[0], -
              25.0 * scale[1], 14.0 * scale[0], -34.0 * scale[1])
    Curveto_r(4.0 * scale[0], -15.0 * scale[1], 16.0 * scale[0], -
              18.0 * scale[1], 73.0 * scale[0], -16.0 * scale[1])
    Lineto_r(68.0 * scale[0], 1.0 * scale[1])
    Lineto_r(-65.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-36.0 * scale[0], 3.0 * scale[1], -65.0 * scale[0],
              11.0 * scale[1], -65.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -4.0 * scale[0],
              16.0 * scale[1], -8.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              17.0 * scale[1], -2.0 * scale[0], 22.0 * scale[1])
    Curveto_r(7.0 * scale[0], 11.0 * scale[1], 6.0 * scale[0],
              11.0 * scale[1], -12.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(959.0 * scale[0], 1088.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -7.0 * scale[1], -1.0 * scale[0], -
              18.0 * scale[1], 0.0 * scale[0], -23.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -12.0 * scale[0], -
              12.0 * scale[1], -28.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -1.0 * scale[1], -40.0 *
              scale[0], -6.0 * scale[1], -53.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -8.0 * scale[1], -11.0 *
              scale[0], -10.0 * scale[1], 35.0 * scale[0], -10.0 * scale[1])
    Lineto_r(57.0 * scale[0], -1.0 * scale[1])
    Lineto_r(0.0 * scale[0], 35.0 * scale[1])
    Curveto_r(0.0 * scale[0], 33.0 * scale[1], -9.0 * scale[0],
              50.0 * scale[1], -11.0 * scale[0], 23.0 * scale[1])
    te.end_fill()
    Moveto(258.0 * scale[0], 1053.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(363.0 * scale[0], 1053.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(603.0 * scale[0], 1043.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(15.0 * scale[0], -2.0 * scale[1], 37.0 *
              scale[0], -2.0 * scale[1], 50.0 * scale[0], 0.0 * scale[1])
    Curveto_r(12.0 * scale[0], 2.0 * scale[1], 0.0 * scale[0],
              4.0 * scale[1], -28.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-27.0 * scale[0], 0.0 * scale[1], -38.0 *
              scale[0], -2.0 * scale[1], -22.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(895.0 * scale[0], 970.0 * scale[1], x, y)
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
    Moveto(170.0 * scale[0], 949.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 15.0 * scale[0], -
              13.0 * scale[1], 33.0 * scale[0], -10.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0], -
              3.0 * scale[1], 7.0 * scale[0], -9.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 15.0 * scale[0], -
              17.0 * scale[1], 33.0 * scale[0], -25.0 * scale[1])
    Curveto_r(28.0 * scale[0], -14.0 * scale[1], 30.0 *
              scale[0], -14.0 * scale[1], 13.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 8.0 * scale[1], -14.0 * scale[0],
              15.0 * scale[1], -8.0 * scale[0], 15.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              5.0 * scale[1], 12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], -3.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -15.0 * scale[1], -29.0 *
              scale[0], -16.0 * scale[1], -25.0 * scale[0], -1.0 * scale[1])
    Curveto_r(1.0 * scale[0], 7.0 * scale[1], -10.0 * scale[0],
              15.0 * scale[1], -25.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 4.0 * scale[1], -28.0 * scale[0],
              3.0 * scale[1], -28.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(310.0 * scale[0], 910.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(380.0 * scale[0], 905.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -4.0 * scale[0], -
              15.0 * scale[1], -10.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0],
              4.0 * scale[1], -10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -8.0 * scale[0],
              6.0 * scale[1], -17.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -6.0 * scale[1], -15.0 *
              scale[0], -7.0 * scale[1], 3.0 * scale[0], -14.0 * scale[1])
    Curveto_r(10.0 * scale[0], -4.0 * scale[1], 33.0 *
              scale[0], -8.0 * scale[1], 49.0 * scale[0], -8.0 * scale[1])
    Curveto_r(17.0 * scale[0], 1.0 * scale[1], 24.0 * scale[0],
              3.0 * scale[1], 18.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 2.0 * scale[1], -13.0 * scale[0],
              11.0 * scale[1], -13.0 * scale[0], 19.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -4.0 * scale[0],
              14.0 * scale[1], -10.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              7.0 * scale[1], -10.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(468.0 * scale[0], 893.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(230.0 * scale[0], 869.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(14.0 * scale[0], -12.0 * scale[1], 46.0 * scale[0], -
              32.0 * scale[1], 73.0 * scale[0], -45.0 * scale[1])
    Curveto_r(49.0 * scale[0], -26.0 * scale[1], 54.0 * scale[0], -
              44.0 * scale[1], 11.0 * scale[0], -44.0 * scale[1])
    Curveto_r(-29.0 * scale[0], 0.0 * scale[1], -58.0 * scale[0], -
              25.0 * scale[1], -68.0 * scale[0], -57.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -13.0 * scale[1], -13.0 * scale[0], -
              23.0 * scale[1], -19.0 * scale[0], -24.0 * scale[1])
    Curveto_r(-35.0 * scale[0], -1.0 * scale[1], -88.0 * scale[0], -
              122.0 * scale[1], -68.0 * scale[0], -156.0 * scale[1])
    Curveto_r(8.0 * scale[0], -14.0 * scale[1], 10.0 * scale[0], -
              11.0 * scale[1], 16.0 * scale[0], 19.0 * scale[1])
    Curveto_r(6.0 * scale[0], 29.0 * scale[1], 11.0 * scale[0],
              35.0 * scale[1], 31.0 * scale[0], 36.0 * scale[1])
    Curveto_r(28.0 * scale[0], 0.0 * scale[1], 45.0 * scale[0],
              12.0 * scale[1], 27.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 7.0 * scale[1], -15.0 * scale[0],
              34.0 * scale[1], 7.0 * scale[0], 63.0 * scale[1])
    Curveto_r(15.0 * scale[0], 20.0 * scale[1], 20.0 * scale[0],
              21.0 * scale[1], 20.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], -5.0 * scale[0], -
              20.0 * scale[1], -10.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -3.0 * scale[1], -10.0 * scale[0], -
              14.0 * scale[1], -10.0 * scale[0], -23.0 * scale[1])
    Curveto_r(1.0 * scale[0], -12.0 * scale[1], 6.0 * scale[0], -
              8.0 * scale[1], 16.0 * scale[0], 11.0 * scale[1])
    Curveto_r(8.0 * scale[0], 15.0 * scale[1], 17.0 * scale[0],
              27.0 * scale[1], 20.0 * scale[0], 27.0 * scale[1])
    Curveto_r(3.0 * scale[0], 0.0 * scale[1], 3.0 * scale[0], -
              4.0 * scale[1], 0.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -4.0 * scale[1], 4.0 * scale[0], -
              8.0 * scale[1], 14.0 * scale[0], -8.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0],
              4.0 * scale[1], 13.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], 1.0 * scale[0],
              13.0 * scale[1], 8.0 * scale[0], 18.0 * scale[1])
    Curveto_r(10.0 * scale[0], 6.0 * scale[1], 10.0 * scale[0],
              9.0 * scale[1], 2.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0],
              7.0 * scale[1], -5.0 * scale[0], 18.0 * scale[1])
    Curveto_r(20.0 * scale[0], 49.0 * scale[1], 70.0 * scale[0],
              89.0 * scale[1], 99.0 * scale[0], 78.0 * scale[1])
    Curveto_r(9.0 * scale[0], -4.0 * scale[1], 13.0 *
              scale[0], -1.0 * scale[1], 10.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 7.0 * scale[1], -11.0 * scale[0],
              11.0 * scale[1], -18.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -2.0 * scale[1], -23.0 *
              scale[0], -6.0 * scale[1], -33.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -3.0 * scale[1], -17.0 *
              scale[0], -1.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], -29.0 * scale[0],
              26.0 * scale[1], -71.0 * scale[0], 46.0 * scale[1])
    Curveto_r(-54.0 * scale[0], 26.0 * scale[1], -70.0 * scale[0],
              31.0 * scale[1], -52.0 * scale[0], 16.0 * scale[1])
    te.end_fill()
    Moveto(472.0 * scale[0], 838.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(16.0 * scale[0], -16.0 * scale[1], 34.0 * scale[0], -
              28.0 * scale[1], 41.0 * scale[0], -28.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 3.0 * scale[0],
              6.0 * scale[1], -8.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 6.0 * scale[1], -29.0 * scale[0],
              18.0 * scale[1], -40.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 9.0 * scale[1], -8.0 * scale[0],
              4.0 * scale[1], 7.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(367.0 * scale[0], 839.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(570.0 * scale[0], 846.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(180.0 * scale[0], 816.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], -9.0 * scale[0], -
              16.0 * scale[1], -25.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -25.0 * scale[0], -
              6.0 * scale[1], -25.0 * scale[0], -15.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0], -
              15.0 * scale[1], 28.0 * scale[0], -14.0 * scale[1])
    Lineto_r(27.0 * scale[0], 1.0 * scale[1])
    Lineto_r(-25.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 7.0 * scale[1], -23.0 * scale[0],
              8.0 * scale[1], -4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(26.0 * scale[0], 1.0 * scale[1], 50.0 * scale[0],
              26.0 * scale[1], 34.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0], -
              1.0 * scale[1], -10.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(13.0 * scale[0], 796.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(14.0 * scale[0], -14.0 * scale[1], 38.0 * scale[0], -
              20.0 * scale[1], 67.0 * scale[0], -16.0 * scale[1])
    Curveto_r(8.0 * scale[0], 1.0 * scale[1], -5.0 * scale[0],
              8.0 * scale[1], -30.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-56.0 * scale[0], 17.0 * scale[1], -54.0 * scale[0],
              17.0 * scale[1], -37.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(550.0 * scale[0], 785.0 * scale[1], x, y)
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
    Moveto(602.0 * scale[0], 760.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(145.0 * scale[0], 750.0 * scale[1], x, y)
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
    Moveto(614.0 * scale[0], 724.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -14.0 * scale[1], -2.0 *
              scale[0], -30.0 * scale[1], 5.0 * scale[0], -37.0 * scale[1])
    Curveto_r(8.0 * scale[0], -8.0 * scale[1], 11.0 *
              scale[0], -8.0 * scale[1], 11.0 * scale[0], 2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], 4.0 * scale[0],
              9.0 * scale[1], 10.0 * scale[0], 6.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -10.0 * scale[0],
              16.0 * scale[1], -15.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0],
              7.0 * scale[1], -3.0 * scale[0], 15.0 * scale[1])
    Curveto_r(4.0 * scale[0], 8.0 * scale[1], 3.0 * scale[0],
              15.0 * scale[1], 0.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              12.0 * scale[1], -12.0 * scale[0], -26.0 * scale[1])
    te.end_fill()
    Moveto(220.0 * scale[0], 730.0 * scale[1], x, y)
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
    Moveto(582.0 * scale[0], 720.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(655.0 * scale[0], 608.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(13.0 * scale[0], -142.0 * scale[1], 20.0 * scale[0], -
              183.0 * scale[1], 30.0 * scale[0], -183.0 * scale[1])
    Curveto_r(15.0 * scale[0], 0.0 * scale[1], 27.0 * scale[0],
              103.0 * scale[1], 15.0 * scale[0], 126.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 11.0 * scale[1], -15.0 * scale[0],
              17.0 * scale[1], -21.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -9.0 * scale[1], -11.0 *
              scale[0], 9.0 * scale[1], 3.0 * scale[0], 23.0 * scale[1])
    Curveto_r(9.0 * scale[0], 9.0 * scale[1], 9.0 * scale[0],
              12.0 * scale[1], -3.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0],
              2.0 * scale[1], 1.0 * scale[0], 10.0 * scale[1])
    Curveto_r(12.0 * scale[0], 7.0 * scale[1], 12.0 * scale[0],
              10.0 * scale[1], 1.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0],
              6.0 * scale[1], -7.0 * scale[0], 16.0 * scale[1])
    Curveto_r(4.0 * scale[0], 10.0 * scale[1], 2.0 * scale[0],
              13.0 * scale[1], -6.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -5.0 * scale[1], -9.0 * scale[0],
              0.0 * scale[1], -6.0 * scale[0], 14.0 * scale[1])
    Curveto_r(4.0 * scale[0], 12.0 * scale[1], 2.0 * scale[0],
              22.0 * scale[1], -4.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              26.0 * scale[1], -3.0 * scale[0], -72.0 * scale[1])
    te.end_fill()
    Moveto_r(36.0 * scale[0], -128.0 * scale[1], 0, 0)
    te.begin_fill()
    Lineto_r(-9.0 * scale[0], -55.0 * scale[1])
    Lineto_r(-1.0 * scale[0], 65.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 39.0 * scale[1], 3.0 * scale[0],
              60.0 * scale[1], 8.0 * scale[0], 55.0 * scale[1])
    Curveto_r(6.0 * scale[0], -6.0 * scale[1], 6.0 * scale[0], -
              33.0 * scale[1], 2.0 * scale[0], -65.0 * scale[1])
    te.end_fill()
    Moveto(330.0 * scale[0], 640.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -11.0 * scale[1], 13.0 * scale[0], -
              20.0 * scale[1], 16.0 * scale[0], -20.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 0.0 * scale[0],
              9.0 * scale[1], -6.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 11.0 * scale[1], -13.0 * scale[0],
              20.0 * scale[1], -16.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], 0.0 * scale[0], -
              9.0 * scale[1], 6.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(631.0 * scale[0], 604.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(277.0 * scale[0], 563.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -12.0 * scale[1], -7.0 *
              scale[0], -40.0 * scale[1], 8.0 * scale[0], -40.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              6.0 * scale[1], 15.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -5.0 * scale[0],
              13.0 * scale[1], -11.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0],
              5.0 * scale[1], -4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(7.0 * scale[0], 11.0 * scale[1], 2.0 * scale[0],
              13.0 * scale[1], -8.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(375.0 * scale[0], 550.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -17.0 * scale[1], -16.0 *
              scale[0], -20.0 * scale[1], -3.0 * scale[0], -15.0 * scale[1])
    Curveto_r(9.0 * scale[0], 4.0 * scale[1], 19.0 * scale[0],
              13.0 * scale[1], 22.0 * scale[0], 21.0 * scale[1])
    Curveto_r(7.0 * scale[0], 19.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], -19.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(595.0 * scale[0], 550.0 * scale[1], x, y)
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
    Moveto(316.0 * scale[0], 488.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -18.0 * scale[1], -11.0 *
              scale[0], -36.0 * scale[1], -9.0 * scale[0], -41.0 * scale[1])
    Curveto_r(7.0 * scale[0], -13.0 * scale[1], 23.0 * scale[0],
              3.0 * scale[1], 23.0 * scale[0], 23.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], 5.0 * scale[0],
              22.0 * scale[1], 10.0 * scale[0], 25.0 * scale[1])
    Curveto_r(13.0 * scale[0], 8.0 * scale[1], 13.0 * scale[0],
              25.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0], -
              15.0 * scale[1], -24.0 * scale[0], -32.0 * scale[1])
    te.end_fill()
    Moveto(257.0 * scale[0], 504.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -25.0 *
              scale[0], -7.0 * scale[1], -49.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-26.0 * scale[0], 0.0 * scale[1], -42.0 * scale[0], -
              6.0 * scale[1], -41.0 * scale[0], -12.0 * scale[1])
    Curveto_r(1.0 * scale[0], -7.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -28.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 1.0 * scale[1], -28.0 * scale[0],
              0.0 * scale[1], -25.0 * scale[0], -2.0 * scale[1])
    Curveto_r(8.0 * scale[0], -8.0 * scale[1], -13.0 * scale[0], -
              43.0 * scale[1], -26.0 * scale[0], -43.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0],
              5.0 * scale[1], -2.0 * scale[0], 13.0 * scale[1])
    Curveto_r(5.0 * scale[0], 7.0 * scale[1], 1.0 * scale[0],
              4.0 * scale[1], -9.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -11.0 * scale[1], -17.0 * scale[0], -
              16.0 * scale[1], -17.0 * scale[0], -12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 3.0 * scale[1], -8.0 * scale[0], -
              1.0 * scale[1], -17.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-24.0 * scale[0], -24.0 * scale[1], -24.0 *
              scale[0], -102.0 * scale[1], 0.0 * scale[0], -127.0 * scale[1])
    Curveto_r(10.0 * scale[0], -10.0 * scale[1], 20.0 * scale[0], -
              31.0 * scale[1], 24.0 * scale[0], -48.0 * scale[1])
    Curveto_r(3.0 * scale[0], -17.0 * scale[1], 9.0 * scale[0], -
              27.0 * scale[1], 14.0 * scale[0], -22.0 * scale[1])
    Curveto_r(10.0 * scale[0], 10.0 * scale[1], 0.0 * scale[0],
              53.0 * scale[1], -12.0 * scale[0], 53.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0],
              13.0 * scale[1], -9.0 * scale[0], 28.0 * scale[1])
    Curveto_r(0.0 * scale[0], 15.0 * scale[1], -6.0 * scale[0],
              34.0 * scale[1], -13.0 * scale[0], 41.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 11.0 * scale[1], -9.0 * scale[0],
              13.0 * scale[1], 1.0 * scale[0], 7.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 12.0 *
              scale[0], -3.0 * scale[1], 12.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 7.0 * scale[0],
              8.0 * scale[1], 15.0 * scale[0], 5.0 * scale[1])
    Curveto_r(8.0 * scale[0], -4.0 * scale[1], 15.0 *
              scale[0], -1.0 * scale[1], 15.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], 11.0 * scale[0],
              28.0 * scale[1], 25.0 * scale[0], 48.0 * scale[1])
    Curveto_r(13.0 * scale[0], 20.0 * scale[1], 22.0 * scale[0],
              39.0 * scale[1], 20.0 * scale[0], 43.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 4.0 * scale[1], 20.0 * scale[0],
              7.0 * scale[1], 50.0 * scale[0], 8.0 * scale[1])
    Curveto_r(49.0 * scale[0], 0.0 * scale[1], 56.0 * scale[0], -
              3.0 * scale[1], 59.0 * scale[0], -21.0 * scale[1])
    Curveto_r(2.0 * scale[0], -12.0 * scale[1], 9.0 * scale[0], -
              47.0 * scale[1], 14.0 * scale[0], -77.0 * scale[1])
    Curveto_r(8.0 * scale[0], -45.0 * scale[1], 8.0 * scale[0], -
              57.0 * scale[1], -4.0 * scale[0], -66.0 * scale[1])
    Curveto_r(-22.0 * scale[0], -17.0 * scale[1], -16.0 *
              scale[0], -26.0 * scale[1], 8.0 * scale[0], -13.0 * scale[1])
    Curveto_r(13.0 * scale[0], 7.0 * scale[1], 44.0 * scale[0],
              13.0 * scale[1], 70.0 * scale[0], 14.0 * scale[1])
    Curveto_r(27.0 * scale[0], 2.0 * scale[1], 56.0 * scale[0],
              9.0 * scale[1], 65.0 * scale[0], 16.0 * scale[1])
    Curveto_r(15.0 * scale[0], 12.0 * scale[1], 16.0 * scale[0],
              12.0 * scale[1], 8.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -13.0 * scale[1], -6.0 *
              scale[0], -13.0 * scale[1], 7.0 * scale[0], -2.0 * scale[1])
    Curveto_r(13.0 * scale[0], 10.0 * scale[1], 17.0 * scale[0],
              10.0 * scale[1], 23.0 * scale[0], -5.0 * scale[1])
    Curveto_r(6.0 * scale[0], -17.0 * scale[1], 7.0 * scale[0], -
              17.0 * scale[1], 16.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 9.0 * scale[1], 16.0 * scale[0],
              17.0 * scale[1], 22.0 * scale[0], 17.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 24.0 * scale[0],
              18.0 * scale[1], 37.0 * scale[0], 39.0 * scale[1])
    Curveto_r(16.0 * scale[0], 25.0 * scale[1], 28.0 * scale[0],
              35.0 * scale[1], 32.0 * scale[0], 27.0 * scale[1])
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 7.0 * scale[0],
              12.0 * scale[1], 7.0 * scale[0], 39.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 48.0 * scale[1], -1.0 * scale[0],
              49.0 * scale[1], -11.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -16.0 * scale[1], -20.0 * scale[0], -
              36.0 * scale[1], -30.0 * scale[0], -43.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -7.0 * scale[1], -16.0 * scale[0], -
              18.0 * scale[1], -13.0 * scale[0], -23.0 * scale[1])
    Curveto_r(4.0 * scale[0], -5.0 * scale[1], 0.0 * scale[0], -
              10.0 * scale[1], -7.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-56.0 * scale[0], -5.0 * scale[1], -84.0 * scale[0], -
              11.0 * scale[1], -92.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -14.0 * scale[1], -22.0 *
              scale[0], -13.0 * scale[1], -40.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 12.0 * scale[1], -16.0 * scale[0],
              12.0 * scale[1], -17.0 * scale[0], 2.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -5.0 * scale[0], -
              2.0 * scale[1], -10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 15.0 * scale[1], -15.0 * scale[0],
              21.0 * scale[1], -24.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -6.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -6.0 * scale[0], 22.0 * scale[1])
    Curveto_r(5.0 * scale[0], 11.0 * scale[1], 3.0 * scale[0],
              28.0 * scale[1], -6.0 * scale[0], 47.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 21.0 * scale[1], -13.0 * scale[0],
              23.0 * scale[1], -9.0 * scale[0], 8.0 * scale[1])
    Curveto_r(3.0 * scale[0], -16.0 * scale[1], -1.0 * scale[0], -
              23.0 * scale[1], -11.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0],
              8.0 * scale[1], -10.0 * scale[0], 35.0 * scale[1])
    Curveto_r(6.0 * scale[0], 36.0 * scale[1], 5.0 * scale[0],
              40.0 * scale[1], -6.0 * scale[0], 29.0 * scale[1])
    te.end_fill()
    Moveto(602.0 * scale[0], 480.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(732.0 * scale[0], 447.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -20.0 * scale[1], 5.0 * scale[0], -
              34.0 * scale[1], 10.0 * scale[0], -31.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], 6.0 * scale[0],
              17.0 * scale[1], 4.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 40.0 * scale[1], -16.0 * scale[0],
              40.0 * scale[1], -14.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(640.0 * scale[0], 438.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 2.0 * scale[0], -
              20.0 * scale[1], 10.0 * scale[0], -8.0 * scale[1])
    Curveto_r(13.0 * scale[0], 19.0 * scale[1], 13.0 * scale[0],
              30.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -10.0 * scale[0], -22.0 * scale[1])
    te.end_fill()
    Moveto(150.0 * scale[0], 425.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -22.0 * scale[1], -8.0 *
              scale[0], -25.0 * scale[1], 13.0 * scale[0], -3.0 * scale[1])
    Curveto_r(9.0 * scale[0], 10.0 * scale[1], 13.0 * scale[0],
              18.0 * scale[1], 8.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0], -
              7.0 * scale[1], -21.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(610.0 * scale[0], 375.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -33.0 * scale[1], -2.0 * scale[0], -
              66.0 * scale[1], -1.0 * scale[0], -73.0 * scale[1])
    Curveto_r(1.0 * scale[0], -7.0 * scale[1], -6.0 * scale[0], -
              25.0 * scale[1], -16.0 * scale[0], -40.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -15.0 * scale[1], -24.0 *
              scale[0], -38.0 * scale[1], -31.0 * scale[0], -52.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -14.0 * scale[1], -21.0 * scale[0], -
              36.0 * scale[1], -31.0 * scale[0], -49.0 * scale[1])
    Lineto_r(-19.0 * scale[0], -24.0 * scale[1])
    Lineto_r(-15.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 27.0 * scale[1], -22.0 * scale[0],
              21.0 * scale[1], -18.0 * scale[0], -13.0 * scale[1])
    Curveto_r(1.0 * scale[0], -7.0 * scale[1], -2.0 * scale[0], -
              13.0 * scale[1], -7.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -21.0 * scale[0],
              12.0 * scale[1], -13.0 * scale[0], 29.0 * scale[1])
    Curveto_r(5.0 * scale[0], 9.0 * scale[1], 13.0 * scale[0],
              27.0 * scale[1], 19.0 * scale[0], 41.0 * scale[1])
    Curveto_r(6.0 * scale[0], 14.0 * scale[1], 20.0 * scale[0],
              47.0 * scale[1], 32.0 * scale[0], 73.0 * scale[1])
    Curveto_r(12.0 * scale[0], 26.0 * scale[1], 20.0 * scale[0],
              50.0 * scale[1], 17.0 * scale[0], 53.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -8.0 * scale[0], -
              4.0 * scale[1], -12.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -12.0 * scale[1], -11.0 * scale[0], -
              21.0 * scale[1], -17.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              3.0 * scale[1], -5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], -2.0 * scale[0], -
              14.0 * scale[1], -10.0 * scale[0], -24.0 * scale[1])
    Curveto_r(-27.0 * scale[0], -31.0 * scale[1], -64.0 * scale[0], -
              133.0 * scale[1], -60.0 * scale[0], -163.0 * scale[1])
    Curveto_r(2.0 * scale[0], -15.0 * scale[1], 0.0 * scale[0], -
              27.0 * scale[1], -5.0 * scale[0], -27.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              11.0 * scale[1], -8.0 * scale[0], -24.0 * scale[1])
    Curveto_r(0.0 * scale[0], -21.0 * scale[1], 4.0 * scale[0], -
              23.0 * scale[1], 48.0 * scale[0], -23.0 * scale[1])
    Curveto_r(108.0 * scale[0], 0.0 * scale[1], 287.0 * scale[0], -
              16.0 * scale[1], 295.0 * scale[0], -27.0 * scale[1])
    Curveto_r(5.0 * scale[0], -8.0 * scale[1], 10.0 *
              scale[0], -6.0 * scale[1], 17.0 * scale[0], 4.0 * scale[1])
    Curveto_r(8.0 * scale[0], 13.0 * scale[1], 11.0 * scale[0],
              13.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(7.0 * scale[0], -10.0 * scale[1], 20.0 * scale[0], -
              12.0 * scale[1], 57.0 * scale[0], -6.0 * scale[1])
    Curveto_r(27.0 * scale[0], 4.0 * scale[1], 60.0 * scale[0],
              9.0 * scale[1], 73.0 * scale[0], 11.0 * scale[1])
    Curveto_r(34.0 * scale[0], 4.0 * scale[1], 41.0 * scale[0],
              20.0 * scale[1], 41.0 * scale[0], 92.0 * scale[1])
    Curveto_r(0.0 * scale[0], 61.0 * scale[1], -2.0 * scale[0],
              65.0 * scale[1], -39.0 * scale[0], 102.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 21.0 * scale[1], -42.0 * scale[0],
              36.0 * scale[1], -47.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -4.0 * scale[1], -5.0 * scale[0],
              0.0 * scale[1], -1.0 * scale[0], 9.0 * scale[1])
    Curveto_r(4.0 * scale[0], 13.0 * scale[1], 1.0 * scale[0],
              16.0 * scale[1], -14.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -3.0 * scale[1], -19.0 * scale[0],
              0.0 * scale[1], -19.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              11.0 * scale[1], -10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -3.0 * scale[0], -
              11.0 * scale[1], 6.0 * scale[0], -25.0 * scale[1])
    Curveto_r(9.0 * scale[0], -14.0 * scale[1], 24.0 * scale[0], -
              25.0 * scale[1], 33.0 * scale[0], -25.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 31.0 * scale[0], -
              15.0 * scale[1], 49.0 * scale[0], -33.0 * scale[1])
    Curveto_r(28.0 * scale[0], -29.0 * scale[1], 32.0 * scale[0], -
              39.0 * scale[1], 32.0 * scale[0], -89.0 * scale[1])
    Curveto_r(0.0 * scale[0], -65.0 * scale[1], -19.0 * scale[0], -
              95.0 * scale[1], -50.0 * scale[0], -78.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 7.0 * scale[1], -20.0 * scale[0],
              6.0 * scale[1], -22.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -18.0 * scale[1], -71.0 * scale[0], -
              14.0 * scale[1], -195.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-29.0 * scale[0], 6.0 * scale[1], -60.0 * scale[0],
              8.0 * scale[1], -68.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -7.0 * scale[1], -21.0 * scale[0],
              11.0 * scale[1], -4.0 * scale[0], 21.0 * scale[1])
    Curveto_r(9.0 * scale[0], 6.0 * scale[1], 7.0 * scale[0],
              57.0 * scale[1], -5.0 * scale[0], 140.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 18.0 * scale[1], 5.0 * scale[0],
              38.0 * scale[1], 29.0 * scale[0], 75.0 * scale[1])
    Curveto_r(10.0 * scale[0], 17.0 * scale[1], 7.0 * scale[0],
              90.0 * scale[1], -5.0 * scale[0], 105.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], -10.0 * scale[0],
              19.0 * scale[1], -13.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 11.0 * scale[1], -6.0 * scale[0], -
              7.0 * scale[1], -7.0 * scale[0], -40.0 * scale[1])
    te.end_fill()
    Moveto(763.0 * scale[0], 383.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -21.0 * scale[1], 5.0 * scale[0], -
              29.0 * scale[1], 11.0 * scale[0], -23.0 * scale[1])
    Curveto_r(6.0 * scale[0], 6.0 * scale[1], 5.0 * scale[0],
              18.0 * scale[1], -2.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 22.0 * scale[1], -11.0 * scale[0],
              21.0 * scale[1], -9.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(131.0 * scale[0], 374.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(681.0 * scale[0], 354.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(780.0 * scale[0], 315.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 4.0 * scale[0], -
              35.0 * scale[1], 8.0 * scale[0], -35.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 6.0 * scale[0],
              16.0 * scale[1], 4.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 19.0 * scale[1], -6.0 * scale[0],
              35.0 * scale[1], -8.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              16.0 * scale[1], -4.0 * scale[0], -35.0 * scale[1])
    te.end_fill()
    Moveto(130.0 * scale[0], 321.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 18.0 * scale[1], -14.0 * scale[0],
              21.0 * scale[1], -14.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(721.0 * scale[0], 314.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(318.0 * scale[0], 273.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(750.0 * scale[0], 263.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0], -
              15.0 * scale[1], 10.0 * scale[0], -23.0 * scale[1])
    Curveto_r(7.0 * scale[0], -12.0 * scale[1], 9.0 *
              scale[0], -10.0 * scale[1], 7.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 19.0 * scale[1], -17.0 * scale[0],
              33.0 * scale[1], -17.0 * scale[0], 15.0 * scale[1])
    te.end_fill()
    Moveto(201.0 * scale[0], 223.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-20.0 * scale[0], -17.0 * scale[1], -21.0 *
              scale[0], -21.0 * scale[1], -7.0 * scale[0], -16.0 * scale[1])
    Curveto_r(16.0 * scale[0], 5.0 * scale[1], 18.0 * scale[0],
              3.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -18.0 * scale[1], -6.0 *
              scale[0], -18.0 * scale[1], 14.0 * scale[0], 0.0 * scale[1])
    Curveto_r(12.0 * scale[0], 11.0 * scale[1], 26.0 * scale[0],
              27.0 * scale[1], 30.0 * scale[0], 36.0 * scale[1])
    Curveto_r(14.0 * scale[0], 25.0 * scale[1], -18.0 * scale[0],
              20.0 * scale[1], -49.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto_r(29.0 * scale[0], 3.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -3.0 * scale[1], -4.0 * scale[0], -
              8.0 * scale[1], -10.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -10.0 *
              scale[0], -1.0 * scale[1], -10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 5.0 * scale[0],
              11.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              2.0 * scale[1], 10.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(101.0 * scale[0], 204.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(124.0 * scale[0], 188.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], -3.0 *
              scale[0], -8.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(7.0 * scale[0], 4.0 * scale[1], 12.0 * scale[0],
              2.0 * scale[1], 12.0 * scale[0], -3.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 12.0 * scale[0], -
              10.0 * scale[1], 28.0 * scale[0], -10.0 * scale[1])
    Curveto_r(23.0 * scale[0], 2.0 * scale[1], 24.0 * scale[0],
              2.0 * scale[1], 5.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 2.0 * scale[1], -23.0 * scale[0],
              9.0 * scale[1], -23.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], -17.0 * scale[0],
              11.0 * scale[1], -26.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(391.0 * scale[0], 84.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(468.0 * scale[0], 3.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(29.0 * scale[0], -2.0 * scale[1], 74.0 *
              scale[0], -2.0 * scale[1], 100.0 * scale[0], 0.0 * scale[1])
    Curveto_r(26.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              3.0 * scale[1], -53.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-55.0 * scale[0], 0.0 * scale[1], -76.0 *
              scale[0], -1.0 * scale[1], -47.0 * scale[0], -3.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#82665a')
    te.end_fill()
    Moveto(109.0 * scale[0], 1323.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -21.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(931.0 * scale[0], 1204.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(406.0 * scale[0], 1197.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0], -
              15.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 0.0 * scale[0],
              11.0 * scale[1], -7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              8.0 * scale[1], -5.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(546.0 * scale[0], 1163.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(480.0 * scale[0], 1150.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(178.0 * scale[0], 1063.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(268.0 * scale[0], 1063.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(368.0 * scale[0], 1063.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(653.0 * scale[0], 1053.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(26.0 * scale[0], -2.0 * scale[1], 68.0 *
              scale[0], -2.0 * scale[1], 95.0 * scale[0], 0.0 * scale[1])
    Curveto_r(26.0 * scale[0], 2.0 * scale[1], 4.0 * scale[0],
              3.0 * scale[1], -48.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-52.0 * scale[0], 0.0 * scale[1], -74.0 *
              scale[0], -1.0 * scale[1], -47.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(398.0 * scale[0], 1043.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(29.0 * scale[0], -2.0 * scale[1], 74.0 *
              scale[0], -2.0 * scale[1], 100.0 * scale[0], 0.0 * scale[1])
    Curveto_r(26.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              3.0 * scale[1], -53.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-55.0 * scale[0], 0.0 * scale[1], -76.0 *
              scale[0], -1.0 * scale[1], -47.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(638.0 * scale[0], 1033.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(868.0 * scale[0], 1023.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(908.0 * scale[0], 1023.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(121.0 * scale[0], 924.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(800.0 * scale[0], 919.0 * scale[1], x, y)
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
    Moveto(448.0 * scale[0], 908.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -5.0 * scale[1], 16.0 * scale[0], -
              8.0 * scale[1], 23.0 * scale[0], -6.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 3.0 * scale[0],
              7.0 * scale[1], -10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 4.0 * scale[1], -21.0 * scale[0],
              3.0 * scale[1], -13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(880.0 * scale[0], 900.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(410.0 * scale[0], 822.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(26.0 * scale[0], -32.0 * scale[1], 28.0 *
              scale[0], -61.0 * scale[1], 3.0 * scale[0], -41.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 10.0 * scale[1], -14.0 * scale[0],
              10.0 * scale[1], -9.0 * scale[0], 2.0 * scale[1])
    Curveto_r(4.0 * scale[0], -7.0 * scale[1], 3.0 * scale[0], -
              13.0 * scale[1], -3.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -18.0 * scale[0], -
              11.0 * scale[1], -27.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -21.0 * scale[1], -14.0 *
              scale[0], -28.0 * scale[1], -3.0 * scale[0], -42.0 * scale[1])
    Curveto_r(12.0 * scale[0], -15.0 * scale[1], 12.0 * scale[0], -
              16.0 * scale[1], -8.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 3.0 * scale[1], -30.0 * scale[0],
              0.0 * scale[1], -40.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -12.0 * scale[1], -17.0 *
              scale[0], -13.0 * scale[1], 3.0 * scale[0], -8.0 * scale[1])
    Curveto_r(22.0 * scale[0], 6.0 * scale[1], 38.0 * scale[0], -
              9.0 * scale[1], 46.0 * scale[0], -42.0 * scale[1])
    Curveto_r(7.0 * scale[0], -29.0 * scale[1], -12.0 * scale[0], -
              51.0 * scale[1], -47.0 * scale[0], -56.0 * scale[1])
    Curveto_r(-25.0 * scale[0], -2.0 * scale[1], -29.0 * scale[0],
              0.0 * scale[1], -27.0 * scale[0], 16.0 * scale[1])
    Curveto_r(2.0 * scale[0], 10.0 * scale[1], -1.0 * scale[0],
              15.0 * scale[1], -6.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -12.0 * scale[0],
              3.0 * scale[1], -15.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 30.0 * scale[1], -27.0 * scale[0],
              24.0 * scale[1], -28.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], -3.0 * scale[0], -
              40.0 * scale[1], -5.0 * scale[0], -55.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -14.0 * scale[1], 1.0 * scale[0], -
              30.0 * scale[1], 7.0 * scale[0], -34.0 * scale[1])
    Curveto_r(8.0 * scale[0], -5.0 * scale[1], 11.0 *
              scale[0], -1.0 * scale[1], 7.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 11.0 * scale[1], 1.0 * scale[0],
              25.0 * scale[1], 8.0 * scale[0], 32.0 * scale[1])
    Curveto_r(11.0 * scale[0], 10.0 * scale[1], 19.0 * scale[0],
              9.0 * scale[1], 42.0 * scale[0], -8.0 * scale[1])
    Lineto_r(29.0 * scale[0], -21.0 * scale[1])
    Lineto_r(38.0 * scale[0], 25.0 * scale[1])
    Curveto_r(46.0 * scale[0], 31.0 * scale[1], 54.0 * scale[0],
              28.0 * scale[1], 25.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-26.0 * scale[0], -36.0 * scale[1], -20.0 * scale[0], -
              108.0 * scale[1], 11.0 * scale[0], -116.0 * scale[1])
    Curveto_r(24.0 * scale[0], -6.0 * scale[1], 80.0 * scale[0],
              31.0 * scale[1], 96.0 * scale[0], 63.0 * scale[1])
    Curveto_r(11.0 * scale[0], 22.0 * scale[1], 13.0 * scale[0],
              23.0 * scale[1], 13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(1.0 * scale[0], -18.0 * scale[1], 2.0 * scale[0], -
              17.0 * scale[1], 14.0 * scale[0], 5.0 * scale[1])
    Curveto_r(14.0 * scale[0], 24.0 * scale[1], 14.0 * scale[0],
              23.0 * scale[1], 21.0 * scale[0], -24.0 * scale[1])
    Curveto_r(5.0 * scale[0], -33.0 * scale[1], 2.0 * scale[0], -
              74.0 * scale[1], -9.0 * scale[0], -125.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -42.0 * scale[1], -16.0 * scale[0], -
              80.0 * scale[1], -16.0 * scale[0], -84.0 * scale[1])
    Curveto_r(0.0 * scale[0], -17.0 * scale[1], 38.0 * scale[0],
              33.0 * scale[1], 45.0 * scale[0], 59.0 * scale[1])
    Curveto_r(14.0 * scale[0], 49.0 * scale[1], 15.0 * scale[0],
              57.0 * scale[1], 14.0 * scale[0], 124.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 110.0 * scale[1], -2.0 * scale[0],
              131.0 * scale[1], -9.0 * scale[0], 119.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -20.0 * scale[1], -21.0 * scale[0],
              8.0 * scale[1], -10.0 * scale[0], 36.0 * scale[1])
    Curveto_r(5.0 * scale[0], 14.0 * scale[1], 10.0 * scale[0],
              50.0 * scale[1], 10.0 * scale[0], 79.0 * scale[1])
    Curveto_r(0.0 * scale[0], 47.0 * scale[1], -4.0 * scale[0],
              57.0 * scale[1], -32.0 * scale[0], 85.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 17.0 * scale[1], -37.0 * scale[0],
              31.0 * scale[1], -44.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -22.0 * scale[0],
              8.0 * scale[1], -35.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 10.0 * scale[1], -36.0 * scale[0],
              19.0 * scale[1], -51.0 * scale[0], 19.0 * scale[1])
    Lineto_r(-27.0 * scale[0], 0.0 * scale[1])
    Lineto_r(19.0 * scale[0], -26.0 * scale[1])
    te.end_fill()
    Moveto_r(0.0 * scale[0], -185.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -20.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 10.0 * scale[1], -17.0 * scale[0],
              22.0 * scale[1], -13.0 * scale[0], 28.0 * scale[1])
    Curveto_r(6.0 * scale[0], 10.0 * scale[1], 33.0 * scale[0], -
              19.0 * scale[1], 33.0 * scale[0], -36.0 * scale[1])
    te.end_fill()
    Moveto_r(30.0 * scale[0], -27.0 * scale[1], 0, 0)
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
    Moveto_r(-90.0 * scale[0], -44.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -3.0 * scale[1], -4.0 * scale[0], -
              8.0 * scale[1], -10.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -10.0 *
              scale[0], -1.0 * scale[1], -10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 5.0 * scale[0],
              11.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              2.0 * scale[1], 10.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(118.0 * scale[0], 803.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(179.0 * scale[0], 733.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(16.0 * scale[0], 13.0 * scale[1], 21.0 * scale[0],
              21.0 * scale[1], 13.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              8.0 * scale[1], -17.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(603.0 * scale[0], 633.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -13.0 * scale[0], -
              11.0 * scale[1], -13.0 * scale[0], -19.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 9.0 * scale[0], -10.0 * scale[1])
    Curveto_r(5.0 * scale[0], 4.0 * scale[1], 12.0 * scale[0],
              0.0 * scale[1], 14.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], -7.0 * scale[1], 6.0 * scale[0], -
              1.0 * scale[1], 6.0 * scale[0], 15.0 * scale[1])
    Curveto_r(1.0 * scale[0], 15.0 * scale[1], 0.0 * scale[0],
              27.0 * scale[1], -1.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              3.0 * scale[1], -15.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(172.0 * scale[0], 535.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-17.0 * scale[0], -37.0 * scale[1], -14.0 *
              scale[0], -45.0 * scale[1], 4.0 * scale[0], -12.0 * scale[1])
    Curveto_r(9.0 * scale[0], 16.0 * scale[1], 14.0 * scale[0],
              31.0 * scale[1], 11.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 2.0 * scale[1], -9.0 * scale[0], -
              7.0 * scale[1], -15.0 * scale[0], -21.0 * scale[1])
    te.end_fill()
    Moveto(622.0 * scale[0], 535.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(648.0 * scale[0], 502.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -5.0 * scale[1], -15.0 *
              scale[0], -11.0 * scale[1], -8.0 * scale[0], -22.0 * scale[1])
    Curveto_r(5.0 * scale[0], -8.0 * scale[1], 10.0 * scale[0], -
              10.0 * scale[1], 10.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 5.0 * scale[0],
              3.0 * scale[1], 10.0 * scale[0], -5.0 * scale[1])
    Curveto_r(8.0 * scale[0], -12.0 * scale[1], 10.0 *
              scale[0], -9.0 * scale[1], 10.0 * scale[0], 13.0 * scale[1])
    Curveto_r(0.0 * scale[0], 15.0 * scale[1], -1.0 * scale[0],
              27.0 * scale[1], -2.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              3.0 * scale[1], -20.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(196.0 * scale[0], 425.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -13.0 * scale[1], 1.0 * scale[0], -
              38.0 * scale[1], -4.0 * scale[0], -55.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -16.0 * scale[1], -9.0 * scale[0], -
              30.0 * scale[1], -6.0 * scale[0], -30.0 * scale[1])
    Curveto_r(3.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              13.0 * scale[1], 15.0 * scale[0], 30.0 * scale[1])
    Curveto_r(14.0 * scale[0], 39.0 * scale[1], 24.0 * scale[0],
              31.0 * scale[1], 28.0 * scale[0], -21.0 * scale[1])
    Curveto_r(1.0 * scale[0], -23.0 * scale[1], 4.0 * scale[0], -
              46.0 * scale[1], 7.0 * scale[0], -50.0 * scale[1])
    Curveto_r(2.0 * scale[0], -4.0 * scale[1], -8.0 * scale[0], -
              17.0 * scale[1], -23.0 * scale[0], -29.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -12.0 * scale[1], -28.0 *
              scale[0], -25.0 * scale[1], -28.0 * scale[0], -28.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], -4.0 * scale[0], -
              13.0 * scale[1], -8.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -24.0 * scale[1], 9.0 *
              scale[0], -13.0 * scale[1], 34.0 * scale[0], 15.0 * scale[1])
    Curveto_r(42.0 * scale[0], 46.0 * scale[1], 49.0 * scale[0],
              74.0 * scale[1], 38.0 * scale[0], 141.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 34.0 * scale[1], -15.0 * scale[0],
              58.0 * scale[1], -20.0 * scale[0], 55.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -9.0 * scale[0],
              0.0 * scale[1], -9.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -7.0 * scale[0],
              11.0 * scale[1], -15.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -7.0 * scale[1], -9.0 * scale[0], -25.0 * scale[1])
    te.end_fill()
    Moveto(670.0 * scale[0], 405.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 7.0 * scale[0], -
              15.0 * scale[1], 15.0 * scale[0], -15.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              7.0 * scale[1], 15.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -7.0 * scale[0],
              15.0 * scale[1], -15.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              7.0 * scale[1], -15.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(1.0 * scale[0], 400.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              24.0 * scale[1], 9.0 * scale[0], -35.0 * scale[1])
    Curveto_r(5.0 * scale[0], -13.0 * scale[1], 9.0 * scale[0], -
              14.0 * scale[1], 9.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -4.0 * scale[0],
              24.0 * scale[1], -9.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 13.0 * scale[1], -9.0 * scale[0],
              14.0 * scale[1], -9.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(704.0 * scale[0], 354.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -9.0 * scale[1], 6.0 * scale[0], -
              21.0 * scale[1], 6.0 * scale[0], -27.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 29.0 * scale[0],
              22.0 * scale[1], 30.0 * scale[0], 33.0 * scale[1])
    Curveto_r(0.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0],
              6.0 * scale[1], -21.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 1.0 * scale[1], -19.0 * scale[0], -
              2.0 * scale[1], -15.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(101.0 * scale[0], 326.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -8.0 * scale[1], -9.0 * scale[0], -
              21.0 * scale[1], -5.0 * scale[0], -27.0 * scale[1])
    Curveto_r(4.0 * scale[0], -7.0 * scale[1], 3.0 * scale[0], -
              9.0 * scale[1], -3.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -14.0 * scale[0],
              0.0 * scale[1], -17.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -2.0 *
              scale[0], -13.0 * scale[1], 3.0 * scale[0], -9.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 12.0 * scale[0], -
              8.0 * scale[1], 16.0 * scale[0], -25.0 * scale[1])
    Curveto_r(5.0 * scale[0], -24.0 * scale[1], 12.0 * scale[0], -
              30.0 * scale[1], 33.0 * scale[0], -30.0 * scale[1])
    Curveto_r(46.0 * scale[0], 0.0 * scale[1], 69.0 * scale[0],
              33.0 * scale[1], 32.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 6.0 * scale[1], -20.0 * scale[0],
              7.0 * scale[1], 2.0 * scale[0], 38.0 * scale[1])
    Curveto_r(21.0 * scale[0], 31.0 * scale[1], 21.0 * scale[0],
              31.0 * scale[1], 1.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -18.0 * scale[1], -21.0 *
              scale[0], -18.0 * scale[1], -36.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 18.0 * scale[1], -16.0 * scale[0],
              18.0 * scale[1], -26.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(737.0 * scale[0], 303.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -2.0 * scale[1], 9.0 * scale[0], -
              11.0 * scale[1], 6.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -10.0 * scale[1], 0.0 * scale[0], -
              12.0 * scale[1], 11.0 * scale[0], -8.0 * scale[1])
    Curveto_r(13.0 * scale[0], 5.0 * scale[1], 16.0 * scale[0],
              0.0 * scale[1], 16.0 * scale[0], -25.0 * scale[1])
    Curveto_r(0.0 * scale[0], -17.0 * scale[1], 0.0 * scale[0], -
              34.0 * scale[1], 1.0 * scale[0], -38.0 * scale[1])
    Curveto_r(1.0 * scale[0], -14.0 * scale[1], 32.0 * scale[0], -
              43.0 * scale[1], 44.0 * scale[0], -43.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0], -
              11.0 * scale[1], 19.0 * scale[0], -25.0 * scale[1])
    Curveto_r(6.0 * scale[0], -25.0 * scale[1], 7.0 * scale[0], -
              25.0 * scale[1], 30.0 * scale[0], -8.0 * scale[1])
    Curveto_r(22.0 * scale[0], 17.0 * scale[1], 23.0 * scale[0],
              19.0 * scale[1], 8.0 * scale[0], 50.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 30.0 * scale[1], -52.0 * scale[0],
              50.0 * scale[1], -72.0 * scale[0], 38.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -4.0 * scale[1], -10.0 * scale[0],
              4.0 * scale[1], -10.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 18.0 * scale[1], 2.0 * scale[0],
              19.0 * scale[1], 15.0 * scale[0], 9.0 * scale[1])
    Curveto_r(8.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              9.0 * scale[1], 15.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 5.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], -6.0 * scale[1])
    Curveto_r(5.0 * scale[0], -8.0 * scale[1], 10.0 * scale[0], -
              10.0 * scale[1], 10.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], -16.0 * scale[0],
              37.0 * scale[1], -24.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-25.0 * scale[0], -4.0 * scale[1], -36.0 * scale[0],
              1.0 * scale[1], -36.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], -8.0 * scale[0],
              17.0 * scale[1], -28.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 1.0 * scale[1], -22.0 *
              scale[0], -1.0 * scale[1], -15.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(890.0 * scale[0], 246.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(189.0 * scale[0], 193.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(16.0 * scale[0], 13.0 * scale[1], 21.0 * scale[0],
              21.0 * scale[1], 13.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              8.0 * scale[1], -17.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(219.0 * scale[0], 193.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(16.0 * scale[0], 13.0 * scale[1], 21.0 * scale[0],
              21.0 * scale[1], 13.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              8.0 * scale[1], -17.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(732.0 * scale[0], 152.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(27.0 * scale[0], -62.0 * scale[1], 65.0 * scale[0], -
              122.0 * scale[1], 82.0 * scale[0], -126.0 * scale[1])
    Curveto_r(24.0 * scale[0], -6.0 * scale[1], 40.0 * scale[0],
              14.0 * scale[1], 22.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 6.0 * scale[1], -28.0 * scale[0],
              32.0 * scale[1], -45.0 * scale[0], 59.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 26.0 * scale[1], -39.0 * scale[0],
              47.0 * scale[1], -47.0 * scale[0], 47.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0], -
              3.0 * scale[1], -12.0 * scale[0], -8.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#8c5321')
    te.end_fill()
    Moveto(77.0 * scale[0], 1403.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-31.0 * scale[0], -5.0 * scale[1], -71.0 * scale[0], -
              53.0 * scale[1], -49.0 * scale[0], -61.0 * scale[1])
    Curveto_r(7.0 * scale[0], -2.0 * scale[1], 9.0 * scale[0], -
              9.0 * scale[1], 5.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -17.0 * scale[1], -12.0 *
              scale[0], -67.0 * scale[1], -3.0 * scale[0], -67.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 6.0 * scale[0], -
              10.0 * scale[1], 4.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -17.0 * scale[1], -1.0 *
              scale[0], -16.0 * scale[1], 7.0 * scale[0], 5.0 * scale[1])
    Curveto_r(6.0 * scale[0], 15.0 * scale[1], 15.0 * scale[0],
              24.0 * scale[1], 21.0 * scale[0], 21.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 8.0 *
              scale[0], -2.0 * scale[1], 4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], 6.0 * scale[0],
              24.0 * scale[1], 20.0 * scale[0], 41.0 * scale[1])
    Curveto_r(20.0 * scale[0], 24.0 * scale[1], 33.0 * scale[0],
              31.0 * scale[1], 53.0 * scale[0], 28.0 * scale[1])
    Curveto_r(23.0 * scale[0], -3.0 * scale[1], 26.0 * scale[0], -
              8.0 * scale[1], 25.0 * scale[0], -40.0 * scale[1])
    Curveto_r(0.0 * scale[0], -29.0 * scale[1], 3.0 * scale[0], -
              34.0 * scale[1], 13.0 * scale[0], -25.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 42.0 * scale[0],
              9.0 * scale[1], 96.0 * scale[0], 5.0 * scale[1])
    Lineto_r(82.0 * scale[0], -5.0 * scale[1])
    Lineto_r(-60.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-33.0 * scale[0], 8.0 * scale[1], -71.0 * scale[0],
              16.0 * scale[1], -84.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 4.0 * scale[1], -22.0 * scale[0],
              7.0 * scale[1], -11.0 * scale[0], 14.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 18.0 * scale[0],
              6.0 * scale[1], 22.0 * scale[0], 4.0 * scale[1])
    Curveto_r(4.0 * scale[0], -3.0 * scale[1], 8.0 * scale[0],
              0.0 * scale[1], 8.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              11.0 * scale[1], -34.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-41.0 * scale[0], 0.0 * scale[1], -56.0 * scale[0],
              25.0 * scale[1], -21.0 * scale[0], 34.0 * scale[1])
    Curveto_r(13.0 * scale[0], 3.0 * scale[1], 32.0 * scale[0],
              3.0 * scale[1], 42.0 * scale[0], -1.0 * scale[1])
    Curveto_r(16.0 * scale[0], -6.0 * scale[1], 16.0 *
              scale[0], -5.0 * scale[1], 5.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 14.0 * scale[1], -7.0 * scale[0],
              16.0 * scale[1], 55.0 * scale[0], 20.0 * scale[1])
    Curveto_r(37.0 * scale[0], 2.0 * scale[1], 14.0 * scale[0],
              3.0 * scale[1], -52.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-66.0 * scale[0], 0.0 * scale[1], -132.0 *
              scale[0], -2.0 * scale[1], -148.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto_r(13.0 * scale[0], -69.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -19.0 * scale[0], -
              13.0 * scale[1], -24.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], 1.0 * scale[0],
              9.0 * scale[1], 9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0], -
              2.0 * scale[1], 15.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(355.0 * scale[0], 1400.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 6.0 * scale[0], -
              15.0 * scale[1], 20.0 * scale[0], -20.0 * scale[1])
    Curveto_r(37.0 * scale[0], -14.0 * scale[1], 40.0 *
              scale[0], -13.0 * scale[1], 20.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 22.0 * scale[1], -31.0 * scale[0],
              25.0 * scale[1], -40.0 * scale[0], 10.0 * scale[1])
    te.end_fill()
    Moveto(488.0 * scale[0], 1403.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(600.0 * scale[0], 1378.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(36.0 * scale[0], -17.0 * scale[1], 85.0 * scale[0], -
              32.0 * scale[1], 110.0 * scale[0], -34.0 * scale[1])
    Curveto_r(25.0 * scale[0], -2.0 * scale[1], 36.0 *
              scale[0], -1.0 * scale[1], 25.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-57.0 * scale[0], 13.0 * scale[1], -135.0 * scale[0],
              40.0 * scale[1], -135.0 * scale[0], 45.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], 24.0 * scale[0],
              7.0 * scale[1], 54.0 * scale[0], 8.0 * scale[1])
    Curveto_r(61.0 * scale[0], 1.0 * scale[1], 177.0 * scale[0], -
              31.0 * scale[1], 196.0 * scale[0], -54.0 * scale[1])
    Curveto_r(7.0 * scale[0], -9.0 * scale[1], 19.0 * scale[0], -
              14.0 * scale[1], 26.0 * scale[0], -11.0 * scale[1])
    Curveto_r(6.0 * scale[0], 2.0 * scale[1], 20.0 * scale[0], -
              2.0 * scale[1], 31.0 * scale[0], -10.0 * scale[1])
    Curveto_r(10.0 * scale[0], -9.0 * scale[1], 12.0 *
              scale[0], -13.0 * scale[1], 6.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 7.0 * scale[1], -5.0 * scale[0], -
              26.0 * scale[1], 11.0 * scale[0], -37.0 * scale[1])
    Curveto_r(7.0 * scale[0], -5.0 * scale[1], 6.0 * scale[0], -
              8.0 * scale[1], -3.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -10.0 *
              scale[0], -4.0 * scale[1], 4.0 * scale[0], -13.0 * scale[1])
    Curveto_r(10.0 * scale[0], -8.0 * scale[1], 15.0 * scale[0], -
              19.0 * scale[1], 11.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -8.0 * scale[1], 1.0 * scale[0], -
              12.0 * scale[1], 15.0 * scale[0], -12.0 * scale[1])
    Curveto_r(21.0 * scale[0], 0.0 * scale[1], 21.0 * scale[0],
              3.0 * scale[1], 17.0 * scale[0], 70.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 38.0 * scale[1], -11.0 * scale[0],
              76.0 * scale[1], -17.0 * scale[0], 84.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 21.0 * scale[1], -63.0 * scale[0],
              26.0 * scale[1], -248.0 * scale[0], 31.0 * scale[1])
    Lineto_r(-168.0 * scale[0], 4.0 * scale[1])
    Lineto_r(65.0 * scale[0], -31.0 * scale[1])
    te.end_fill()
    Moveto(468.0 * scale[0], 1353.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(537.0 * scale[0], 1339.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(803.0 * scale[0], 1333.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(42.0 * scale[0], -5.0 * scale[1], 41.0 * scale[0], -
              23.0 * scale[1], -1.0 * scale[0], -24.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 0.0 * scale[1], -21.0 *
              scale[0], -3.0 * scale[1], -14.0 * scale[0], -6.0 * scale[1])
    Curveto_r(18.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              23.0 * scale[1], -5.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -8.0 * scale[1])
    Curveto_r(9.0 * scale[0], -6.0 * scale[1], 10.0 * scale[0], -
              17.0 * scale[1], 4.0 * scale[0], -38.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -16.0 * scale[1], -6.0 * scale[0], -
              35.0 * scale[1], -3.0 * scale[0], -43.0 * scale[1])
    Curveto_r(3.0 * scale[0], -9.0 * scale[1], 0.0 * scale[0], -
              11.0 * scale[1], -9.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 5.0 * scale[1], -3.0 * scale[0], -
              6.0 * scale[1], 10.0 * scale[0], -23.0 * scale[1])
    Curveto_r(12.0 * scale[0], -18.0 * scale[1], 19.0 * scale[0], -
              37.0 * scale[1], 15.0 * scale[0], -43.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -8.0 * scale[1], -9.0 *
              scale[0], -7.0 * scale[1], -15.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 8.0 * scale[1], -9.0 * scale[0],
              9.0 * scale[1], -9.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -32.0 * scale[0], -
              12.0 * scale[1], -92.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-51.0 * scale[0], -1.0 * scale[1], -95.0 *
              scale[0], -4.0 * scale[1], -97.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -8.0 * scale[1], 201.0 *
              scale[0], -2.0 * scale[1], 224.0 * scale[0], 6.0 * scale[1])
    Curveto_r(22.0 * scale[0], 8.0 * scale[1], 45.0 * scale[0],
              3.0 * scale[1], 45.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], -7.0 * scale[0], -
              6.0 * scale[1], -15.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 4.0 * scale[1], -15.0 * scale[0],
              1.0 * scale[1], -15.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -21.0 * scale[0], -
              11.0 * scale[1], -52.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-78.0 * scale[0], -1.0 * scale[1], -37.0 *
              scale[0], -20.0 * scale[1], 56.0 * scale[0], -27.0 * scale[1])
    Curveto_r(90.0 * scale[0], -7.0 * scale[1], 119.0 * scale[0],
              0.0 * scale[1], 133.0 * scale[0], 29.0 * scale[1])
    Curveto_r(8.0 * scale[0], 18.0 * scale[1], 10.0 * scale[0],
              100.0 * scale[1], 3.0 * scale[0], 128.0 * scale[1])
    Curveto_r(0.0 * scale[0], 3.0 * scale[1], -7.0 * scale[0], -
              10.0 * scale[1], -15.0 * scale[0], -28.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -41.0 * scale[1], -56.0 *
              scale[0], -74.0 * scale[1], -69.0 * scale[0], -61.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 5.0 * scale[1], -20.0 * scale[0],
              9.0 * scale[1], -32.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-54.0 * scale[0], 0.0 * scale[1], -70.0 * scale[0],
              68.0 * scale[1], -33.0 * scale[0], 140.0 * scale[1])
    Curveto_r(12.0 * scale[0], 22.0 * scale[1], 25.0 * scale[0],
              40.0 * scale[1], 30.0 * scale[0], 40.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              7.0 * scale[1], 9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], -11.0 * scale[0],
              15.0 * scale[1], -42.0 * scale[0], 13.0 * scale[1])
    Lineto_r(-43.0 * scale[0], -1.0 * scale[1])
    Lineto_r(38.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(263.0 * scale[0], 1323.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(348.0 * scale[0], 1313.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(390.0 * scale[0], 1305.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -7.0 * scale[0], -
              18.0 * scale[1], -16.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -6.0 * scale[1], -13.0 *
              scale[0], -12.0 * scale[1], -6.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 18.0 * scale[0],
              7.0 * scale[1], 27.0 * scale[0], 24.0 * scale[1])
    Curveto_r(9.0 * scale[0], 17.0 * scale[1], 11.0 * scale[0],
              30.0 * scale[1], 5.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              7.0 * scale[1], -10.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(186.0 * scale[0], 1250.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -14.0 * scale[1], 8.0 * scale[0], -
              33.0 * scale[1], 8.0 * scale[0], -42.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 4.0 * scale[0], -
              18.0 * scale[1], 9.0 * scale[0], -18.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 4.0 * scale[0], -
              7.0 * scale[1], -3.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -19.0 * scale[1], -14.0 *
              scale[0], -21.0 * scale[1], 30.0 * scale[0], -29.0 * scale[1])
    Lineto_r(35.0 * scale[0], -6.0 * scale[1])
    Lineto_r(-30.0 * scale[0], 16.0 * scale[1])
    Lineto_r(-30.0 * scale[0], 15.0 * scale[1])
    Lineto_r(30.0 * scale[0], -5.0 * scale[1])
    Curveto_r(17.0 * scale[0], -3.0 * scale[1], 59.0 * scale[0], -
              9.0 * scale[1], 95.0 * scale[0], -12.0 * scale[1])
    Curveto_r(36.0 * scale[0], -4.0 * scale[1], 73.0 * scale[0], -
              11.0 * scale[1], 82.0 * scale[0], -16.0 * scale[1])
    Curveto_r(13.0 * scale[0], -6.0 * scale[1], 16.0 *
              scale[0], -5.0 * scale[1], 12.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -29.0 * scale[0],
              16.0 * scale[1], -72.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-84.0 * scale[0], 8.0 * scale[1], -144.0 * scale[0],
              25.0 * scale[1], -139.0 * scale[0], 40.0 * scale[1])
    Curveto_r(5.0 * scale[0], 17.0 * scale[1], 67.0 * scale[0],
              30.0 * scale[1], 120.0 * scale[0], 23.0 * scale[1])
    Curveto_r(27.0 * scale[0], -3.0 * scale[1], 47.0 *
              scale[0], -1.0 * scale[1], 47.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -38.0 * scale[0],
              10.0 * scale[1], -86.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-71.0 * scale[0], 0.0 * scale[1], -89.0 * scale[0],
              3.0 * scale[1], -101.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 15.0 * scale[1], -13.0 * scale[0],
              15.0 * scale[1], -7.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(22.0 * scale[0], 1137.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -61.0 * scale[1], 14.0 * scale[0], -
              67.0 * scale[1], 134.0 * scale[0], -72.0 * scale[1])
    Curveto_r(96.0 * scale[0], -3.0 * scale[1], 107.0 *
              scale[0], -2.0 * scale[1], 89.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 8.0 * scale[1], -25.0 * scale[0],
              19.0 * scale[1], -31.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 5.0 * scale[1], -14.0 * scale[0],
              7.0 * scale[1], -17.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -20.0 * scale[0],
              5.0 * scale[1], -36.0 * scale[0], 17.0 * scale[1])
    Lineto_r(-31.0 * scale[0], 21.0 * scale[1])
    Lineto_r(-9.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -13.0 * scale[1], -10.0 *
              scale[0], -16.0 * scale[1], -11.0 * scale[0], -8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], -1.0 * scale[0],
              13.0 * scale[1], -10.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -10.0 * scale[1], -10.0 *
              scale[0], -11.0 * scale[1], -10.0 * scale[0], -2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -7.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0],
              7.0 * scale[1], -15.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -9.0 * scale[0],
              19.0 * scale[1], -20.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 9.0 * scale[1], -19.0 * scale[0],
              7.0 * scale[1], -18.0 * scale[0], -23.0 * scale[1])
    te.end_fill()
    Moveto(904.0 * scale[0], 1148.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-19.0 * scale[0], -23.0 * scale[1])
    Lineto_r(23.0 * scale[0], 19.0 * scale[1])
    Curveto_r(21.0 * scale[0], 18.0 * scale[1], 27.0 * scale[0],
              26.0 * scale[1], 19.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              10.0 * scale[1], -23.0 * scale[0], -22.0 * scale[1])
    te.end_fill()
    Moveto(170.0 * scale[0], 1151.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -4.0 * scale[0], -
              9.0 * scale[1], -10.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0],
              2.0 * scale[1], -10.0 * scale[0], -3.0 * scale[1])
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], 27.0 * scale[0], -
              24.0 * scale[1], 74.0 * scale[0], -28.0 * scale[1])
    Curveto_r(22.0 * scale[0], -2.0 * scale[1], 52.0 * scale[0], -
              11.0 * scale[1], 68.0 * scale[0], -18.0 * scale[1])
    Curveto_r(15.0 * scale[0], -8.0 * scale[1], 42.0 * scale[0], -
              17.0 * scale[1], 60.0 * scale[0], -21.0 * scale[1])
    Curveto_r(55.0 * scale[0], -10.0 * scale[1], 12.0 * scale[0],
              12.0 * scale[1], -77.0 * scale[0], 41.0 * scale[1])
    Curveto_r(-44.0 * scale[0], 14.0 * scale[1], -86.0 * scale[0],
              30.0 * scale[1], -92.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 7.0 * scale[1], -13.0 * scale[0],
              7.0 * scale[1], -13.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(388.0 * scale[0], 1113.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(450.0 * scale[0], 1110.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(14.0 * scale[0], -9.0 * scale[1], 128.0 * scale[0], -
              15.0 * scale[1], 119.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 3.0 * scale[1], -34.0 * scale[0],
              7.0 * scale[1], -69.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-45.0 * scale[0], 4.0 * scale[1], -60.0 * scale[0],
              3.0 * scale[1], -50.0 * scale[0], -4.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#eed5e7')
    te.end_fill()
    Moveto(870.0 * scale[0], 1326.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(550.0 * scale[0], 1316.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(470.0 * scale[0], 1299.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -4.0 * scale[0], -
              8.0 * scale[1], -9.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 3.0 * scale[1], -16.0 * scale[0], -
              11.0 * scale[1], -25.0 * scale[0], -32.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -34.0 * scale[1], -16.0 *
              scale[0], -40.0 * scale[1], -1.0 * scale[0], -69.0 * scale[1])
    Curveto_r(9.0 * scale[0], -18.0 * scale[1], 13.0 * scale[0], -
              38.0 * scale[1], 10.0 * scale[0], -45.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], 0.0 *
              scale[0], -5.0 * scale[1], 8.0 * scale[0], 5.0 * scale[1])
    Curveto_r(16.0 * scale[0], 19.0 * scale[1], 57.0 * scale[0],
              23.0 * scale[1], 57.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 9.0 * scale[0], -
              3.0 * scale[1], 20.0 * scale[0], 7.0 * scale[1])
    Curveto_r(15.0 * scale[0], 14.0 * scale[1], 17.0 * scale[0],
              21.0 * scale[1], 9.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 8.0 * scale[1], -9.0 * scale[0],
              24.0 * scale[1], -6.0 * scale[0], 35.0 * scale[1])
    Curveto_r(8.0 * scale[0], 30.0 * scale[1], -19.0 * scale[0],
              79.0 * scale[1], -43.0 * scale[0], 79.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0], -
              5.0 * scale[1], -20.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto_r(20.0 * scale[0], -23.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -3.0 * scale[1], -4.0 * scale[0], -
              8.0 * scale[1], -10.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -10.0 *
              scale[0], -1.0 * scale[1], -10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 5.0 * scale[0],
              11.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              2.0 * scale[1], 10.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(838.0 * scale[0], 1293.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-18.0 * scale[0], -21.0 * scale[1], -31.0 *
              scale[0], -43.0 * scale[1], -25.0 * scale[0], -43.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              14.0 * scale[1], 25.0 * scale[0], 30.0 * scale[1])
    Curveto_r(25.0 * scale[0], 33.0 * scale[1], 24.0 * scale[0],
              41.0 * scale[1], 0.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(140.0 * scale[0], 1276.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              17.0 * scale[1], 9.0 * scale[0], -20.0 * scale[1])
    Curveto_r(5.0 * scale[0], -4.0 * scale[1], 7.0 * scale[0],
              3.0 * scale[1], 4.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 23.0 * scale[1], -13.0 * scale[0],
              26.0 * scale[1], -13.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(881.0 * scale[0], 1276.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -10.0 * scale[1], -9.0 * scale[0], -
              16.0 * scale[1], -1.0 * scale[0], -21.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 14.0 * scale[0], -
              4.0 * scale[1], 17.0 * scale[0], -1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              6.0 * scale[1], -7.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0],
              3.0 * scale[1], 0.0 * scale[0], 15.0 * scale[1])
    Curveto_r(7.0 * scale[0], 8.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              6.0 * scale[1], -16.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(103.0 * scale[0], 1215.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -9.0 * scale[1], -3.0 * scale[0], -
              19.0 * scale[1], 1.0 * scale[0], -22.0 * scale[1])
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], 6.0 * scale[0],
              1.0 * scale[1], 6.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 6.0 * scale[0],
              18.0 * scale[1], 13.0 * scale[0], 20.0 * scale[1])
    Curveto_r(9.0 * scale[0], 4.0 * scale[1], 9.0 * scale[0],
              6.0 * scale[1], -1.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 1.0 * scale[1], -15.0 * scale[0], -
              6.0 * scale[1], -19.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(843.0 * scale[0], 1205.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -9.0 * scale[1], -3.0 * scale[0], -
              19.0 * scale[1], 1.0 * scale[0], -22.0 * scale[1])
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], 6.0 * scale[0],
              1.0 * scale[1], 6.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 8.0 * scale[0],
              18.0 * scale[1], 18.0 * scale[0], 20.0 * scale[1])
    Curveto_r(16.0 * scale[0], 4.0 * scale[1], 16.0 * scale[0],
              5.0 * scale[1], -1.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0], -
              6.0 * scale[1], -24.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(899.0 * scale[0], 1163.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -21.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(56.0 * scale[0], 991.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-23.0 * scale[0], -37.0 * scale[1], -25.0 *
              scale[0], -62.0 * scale[1], -6.0 * scale[0], -81.0 * scale[1])
    Curveto_r(16.0 * scale[0], -16.0 * scale[1], 25.0 * scale[0], -
              18.0 * scale[1], 40.0 * scale[0], -10.0 * scale[1])
    Curveto_r(25.0 * scale[0], 13.0 * scale[1], 25.0 * scale[0],
              48.0 * scale[1], 1.0 * scale[0], 78.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 24.0 * scale[1], -27.0 * scale[0],
              26.0 * scale[1], -35.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto_r(35.0 * scale[0], -74.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -9.0 * scale[1], -11.0 *
              scale[0], -8.0 * scale[1], -5.0 * scale[0], 6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 10.0 * scale[1], 9.0 * scale[0],
              15.0 * scale[1], 12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 0.0 * scale[0], -
              11.0 * scale[1], -7.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(837.0 * scale[0], 982.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-23.0 * scale[0], -25.0 * scale[1], -21.0 *
              scale[0], -58.0 * scale[1], 3.0 * scale[0], -82.0 * scale[1])
    Curveto_r(24.0 * scale[0], -24.0 * scale[1], 48.0 *
              scale[0], -25.0 * scale[1], 78.0 * scale[0], -4.0 * scale[1])
    Curveto_r(26.0 * scale[0], 18.0 * scale[1], 30.0 * scale[0],
              65.0 * scale[1], 6.0 * scale[0], 88.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 22.0 * scale[1], -67.0 * scale[0],
              20.0 * scale[1], -87.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto_r(81.0 * scale[0], -4.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(28.0 * scale[0], -28.0 * scale[1], 3.0 * scale[0], -
              87.0 * scale[1], -37.0 * scale[0], -88.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -51.0 * scale[0],
              30.0 * scale[1], -51.0 * scale[0], 48.0 * scale[1])
    Curveto_r(0.0 * scale[0], 38.0 * scale[1], 62.0 * scale[0],
              66.0 * scale[1], 88.0 * scale[0], 40.0 * scale[1])
    te.end_fill()
    Moveto(857.0 * scale[0], 955.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -23.0 * scale[1], 1.0 * scale[0], -
              41.0 * scale[1], 24.0 * scale[0], -42.0 * scale[1])
    Curveto_r(16.0 * scale[0], -2.0 * scale[1], 20.0 * scale[0],
              3.0 * scale[1], 17.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 30.0 * scale[1], -32.0 * scale[0],
              42.0 * scale[1], -41.0 * scale[0], 17.0 * scale[1])
    te.end_fill()
    Moveto(784.0 * scale[0], 513.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], 1.0 * scale[0], -
              11.0 * scale[1], -4.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0], -
              1.0 * scale[1], -10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 4.0 * scale[0], -
              16.0 * scale[1], 9.0 * scale[0], -16.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0], -
              15.0 * scale[1], 16.0 * scale[0], -32.0 * scale[1])
    Curveto_r(4.0 * scale[0], -18.0 * scale[1], 14.0 * scale[0], -
              42.0 * scale[1], 22.0 * scale[0], -53.0 * scale[1])
    Curveto_r(14.0 * scale[0], -19.0 * scale[1], 15.0 *
              scale[0], -18.0 * scale[1], 9.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 17.0 * scale[1], -3.0 * scale[0],
              24.0 * scale[1], 0.0 * scale[0], 17.0 * scale[1])
    Curveto_r(3.0 * scale[0], -6.0 * scale[1], 10.0 * scale[0], -
              10.0 * scale[1], 14.0 * scale[0], -7.0 * scale[1])
    Curveto_r(9.0 * scale[0], 6.0 * scale[1], 6.0 * scale[0], -
              28.0 * scale[1], -4.0 * scale[0], -44.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -13.0 * scale[1], 4.0 * scale[0], -
              41.0 * scale[1], 17.0 * scale[0], -41.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              4.0 * scale[1], -1.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              16.0 * scale[1], 0.0 * scale[0], 32.0 * scale[1])
    Curveto_r(11.0 * scale[0], 20.0 * scale[1], 11.0 * scale[0],
              20.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(7.0 * scale[0], -19.0 * scale[1], 8.0 *
              scale[0], -19.0 * scale[1], 8.0 * scale[0], 1.0 * scale[1])
    Curveto_r(1.0 * scale[0], 19.0 * scale[1], 31.0 * scale[0],
              31.0 * scale[1], 31.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 20.0 *
              scale[0], -7.0 * scale[1], 21.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], 3.0 * scale[0],
              10.0 * scale[1], 12.0 * scale[0], -8.0 * scale[1])
    Curveto_r(11.0 * scale[0], -24.0 * scale[1], 11.0 *
              scale[0], -24.0 * scale[1], 15.0 * scale[0], 14.0 * scale[1])
    Curveto_r(3.0 * scale[0], 33.0 * scale[1], -1.0 * scale[0],
              43.0 * scale[1], -28.0 * scale[0], 68.0 * scale[1])
    Curveto_r(-44.0 * scale[0], 39.0 * scale[1], -81.0 * scale[0],
              57.0 * scale[1], -119.0 * scale[0], 56.0 * scale[1])
    Curveto_r(-23.0 * scale[0], -1.0 * scale[1], -30.0 *
              scale[0], -5.0 * scale[1], -27.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(20.0 * scale[0], 251.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(8.0 * scale[0], -6.0 * scale[1], 14.0 * scale[0], -
              24.0 * scale[1], 13.0 * scale[0], -45.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -20.0 * scale[1], 3.0 * scale[0], -
              36.0 * scale[1], 9.0 * scale[0], -36.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 6.0 * scale[0],
              5.0 * scale[1], 2.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 8.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], 12.0 * scale[0], 4.0 * scale[1])
    Curveto_r(10.0 * scale[0], -5.0 * scale[1], 28.0 * scale[0], -
              10.0 * scale[1], 39.0 * scale[0], -12.0 * scale[1])
    Lineto_r(20.0 * scale[0], -5.0 * scale[1])
    Lineto_r(-20.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 10.0 * scale[1], -48.0 * scale[0],
              39.0 * scale[1], -58.0 * scale[0], 64.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -12.0 * scale[0],
              17.0 * scale[1], -19.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -9.0 *
              scale[0], -3.0 * scale[1], 2.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(118.0 * scale[0], 153.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(181.0 * scale[0], 153.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -7.0 * scale[1], -9.0 * scale[0], -
              10.0 * scale[1], -18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 5.0 * scale[1], -16.0 * scale[0],
              4.0 * scale[1], 0.0 * scale[0], -6.0 * scale[1])
    Curveto_r(21.0 * scale[0], -13.0 * scale[1], 32.0 *
              scale[0], -8.0 * scale[1], 24.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 9.0 * scale[1], -6.0 * scale[0],
              9.0 * scale[1], -6.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(297.0 * scale[0], 109.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-20.0 * scale[0], -11.0 * scale[1], -37.0 *
              scale[0], -24.0 * scale[1], -37.0 * scale[0], -29.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0], -
              9.0 * scale[1], -11.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 1.0 * scale[1], -13.0 * scale[0], -
              3.0 * scale[1], -16.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -7.0 * scale[1], 12.0 * scale[0], -
              11.0 * scale[1], 39.0 * scale[0], -11.0 * scale[1])
    Curveto_r(23.0 * scale[0], 0.0 * scale[1], 44.0 * scale[0], -
              5.0 * scale[1], 46.0 * scale[0], -11.0 * scale[1])
    Curveto_r(2.0 * scale[0], -7.0 * scale[1], 11.0 * scale[0], -
              12.0 * scale[1], 20.0 * scale[0], -12.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              3.0 * scale[1], 7.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 9.0 * scale[1], -18.0 * scale[0],
              62.0 * scale[1], -6.0 * scale[0], 62.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0], -
              12.0 * scale[1], 14.0 * scale[0], -27.0 * scale[1])
    Curveto_r(3.0 * scale[0], -23.0 * scale[1], 4.0 *
              scale[0], -22.0 * scale[1], 6.0 * scale[0], 8.0 * scale[1])
    Curveto_r(1.0 * scale[0], 46.0 * scale[1], -13.0 * scale[0],
              52.0 * scale[1], -62.0 * scale[0], 28.0 * scale[1])
    te.end_fill()
    Moveto(218.0 * scale[0], 33.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(0.0 * scale[0], 8.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 42.0 * scale[0], -
              7.0 * scale[1], 93.0 * scale[0], -6.0 * scale[1])
    Curveto_r(94.0 * scale[0], 1.0 * scale[1], 82.0 * scale[0],
              5.0 * scale[1], -31.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-34.0 * scale[0], 2.0 * scale[1], -62.0 * scale[0],
              0.0 * scale[1], -62.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(233.0 * scale[0], 3.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(26.0 * scale[0], -2.0 * scale[1], 67.0 *
              scale[0], -2.0 * scale[1], 90.0 * scale[0], 0.0 * scale[1])
    Curveto_r(23.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              3.0 * scale[1], -48.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-50.0 * scale[0], 0.0 * scale[1], -68.0 *
              scale[0], -1.0 * scale[1], -42.0 * scale[0], -3.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#dab5cd')
    te.end_fill()
    Moveto(119.0 * scale[0], 1323.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 3.0 * scale[0], -5.0 * scale[1])
    Curveto_r(14.0 * scale[0], 11.0 * scale[1], 17.0 * scale[0],
              9.0 * scale[1], 25.0 * scale[0], -15.0 * scale[1])
    Curveto_r(7.0 * scale[0], -21.0 * scale[1], 11.0 * scale[0], -
              23.0 * scale[1], 15.0 * scale[0], -11.0 * scale[1])
    Curveto_r(4.0 * scale[0], 9.0 * scale[1], -1.0 * scale[0],
              23.0 * scale[1], -11.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 15.0 * scale[1], -19.0 * scale[0],
              15.0 * scale[1], -32.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(525.0 * scale[0], 1328.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(30.0 * scale[0], -18.0 * scale[1], 54.0 *
              scale[0], -20.0 * scale[1], 31.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 8.0 * scale[1], -27.0 * scale[0],
              14.0 * scale[1], -35.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -1.0 * scale[1], -11.0 *
              scale[0], -4.0 * scale[1], 4.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(403.0 * scale[0], 1294.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -15.0 * scale[1], -17.0 * scale[0], -
              41.0 * scale[1], -17.0 * scale[0], -58.0 * scale[1])
    Curveto_r(0.0 * scale[0], -38.0 * scale[1], 40.0 * scale[0], -
              100.0 * scale[1], 57.0 * scale[0], -89.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 7.0 * scale[0],
              8.0 * scale[1], -4.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 4.0 * scale[1], -41.0 * scale[0],
              43.0 * scale[1], -41.0 * scale[0], 77.0 * scale[1])
    Curveto_r(0.0 * scale[0], 15.0 * scale[1], 9.0 * scale[0],
              40.0 * scale[1], 21.0 * scale[0], 56.0 * scale[1])
    Curveto_r(12.0 * scale[0], 16.0 * scale[1], 17.0 * scale[0],
              29.0 * scale[1], 12.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -18.0 * scale[0], -
              12.0 * scale[1], -28.0 * scale[0], -26.0 * scale[1])
    te.end_fill()
    Moveto(876.0 * scale[0], 1305.0 * scale[1], x, y)
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
    Moveto(85.0 * scale[0], 1290.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(19.0 * scale[0], 7.0 * scale[1], 20.0 * scale[0],
              0.0 * scale[1], 6.0 * scale[0], -27.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -11.0 * scale[1], -7.0 * scale[0], -
              19.0 * scale[1], -2.0 * scale[0], -19.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 23.0 * scale[0],
              40.0 * scale[1], 16.0 * scale[0], 52.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 11.0 * scale[1], -21.0 * scale[0],
              10.0 * scale[1], -29.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(580.0 * scale[0], 1281.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 18.0 * scale[1], -14.0 * scale[0],
              21.0 * scale[1], -14.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(834.0 * scale[0], 1279.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -14.0 * scale[1], 14.0 *
              scale[0], -19.0 * scale[1], 25.0 * scale[0], -6.0 * scale[1])
    Curveto_r(8.0 * scale[0], 10.0 * scale[1], 7.0 * scale[0],
              14.0 * scale[1], -5.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0], -
              4.0 * scale[1], -20.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(470.0 * scale[0], 1269.0 * scale[1], x, y)
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
    Moveto(65.0 * scale[0], 1260.0 * scale[1], x, y)
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
    Moveto(534.0 * scale[0], 1249.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 4.0 * scale[0], -
              19.0 * scale[1], 8.0 * scale[0], -19.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0],
              6.0 * scale[1], 8.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -4.0 * scale[0],
              17.0 * scale[1], -8.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 2.0 * scale[1], -8.0 * scale[0], -
              4.0 * scale[1], -8.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(897.0 * scale[0], 1253.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -4.0 * scale[1], 4.0 * scale[0], -
              17.0 * scale[1], 14.0 * scale[0], -27.0 * scale[1])
    Curveto_r(22.0 * scale[0], -22.0 * scale[1], 25.0 *
              scale[0], -10.0 * scale[1], 5.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 10.0 * scale[1], -16.0 * scale[0],
              15.0 * scale[1], -19.0 * scale[0], 10.0 * scale[1])
    te.end_fill()
    Moveto(591.0 * scale[0], 1232.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], -6.0 * scale[0], -
              33.0 * scale[1], -12.0 * scale[0], -45.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -20.0 * scale[1], -10.0 *
              scale[0], -21.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 11.0 * scale[1], 15.0 * scale[0],
              27.0 * scale[1], 12.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 23.0 * scale[1], -4.0 * scale[0],
              24.0 * scale[1], -6.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(50.0 * scale[0], 1206.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], 9.0 * scale[0], -
              34.0 * scale[1], 20.0 * scale[0], -47.0 * scale[1])
    Curveto_r(24.0 * scale[0], -29.0 * scale[1], 25.0 *
              scale[0], -22.0 * scale[1], 4.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 18.0 * scale[1], -13.0 * scale[0],
              36.0 * scale[1], -9.0 * scale[0], 42.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], 1.0 * scale[0],
              10.0 * scale[1], -4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              11.0 * scale[1], -11.0 * scale[0], -24.0 * scale[1])
    te.end_fill()
    Moveto(133.0 * scale[0], 1212.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -14.0 * scale[1], 5.0 * scale[0], -
              18.0 * scale[1], 11.0 * scale[0], -12.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 6.0 * scale[0],
              14.0 * scale[1], -1.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 9.0 * scale[1], -12.0 * scale[0],
              7.0 * scale[1], -10.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(790.0 * scale[0], 1196.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 4.0 * scale[0], -
              27.0 * scale[1], 10.0 * scale[0], -31.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 8.0 * scale[0],
              7.0 * scale[1], 7.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 36.0 * scale[1], -17.0 * scale[0],
              41.0 * scale[1], -17.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(158.0 * scale[0], 1178.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-15.0 * scale[0], -16.0 * scale[1], -21.0 *
              scale[0], -28.0 * scale[1], -15.0 * scale[0], -28.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 50.0 * scale[0],
              38.0 * scale[1], 45.0 * scale[0], 48.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 4.0 * scale[1], -15.0 * scale[0], -
              5.0 * scale[1], -30.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(426.0 * scale[0], 1197.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0], -
              15.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 0.0 * scale[0],
              11.0 * scale[1], -7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              8.0 * scale[1], -5.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(875.0 * scale[0], 1200.0 * scale[1], x, y)
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
    Moveto(495.0 * scale[0], 1160.0 * scale[1], x, y)
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
    Moveto(540.0 * scale[0], 1150.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -5.0 * scale[1], -33.0 * scale[0], -
              10.0 * scale[1], -55.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-36.0 * scale[0], -1.0 * scale[1], -37.0 *
              scale[0], -2.0 * scale[1], -16.0 * scale[0], -11.0 * scale[1])
    Curveto_r(26.0 * scale[0], -10.0 * scale[1], 54.0 *
              scale[0], -4.0 * scale[1], 86.0 * scale[0], 17.0 * scale[1])
    Curveto_r(22.0 * scale[0], 16.0 * scale[1], 8.0 * scale[0],
              19.0 * scale[1], -15.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(876.0 * scale[0], 1143.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(828.0 * scale[0], 1138.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -5.0 * scale[1], 16.0 * scale[0], -
              8.0 * scale[1], 23.0 * scale[0], -6.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 3.0 * scale[0],
              7.0 * scale[1], -10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 4.0 * scale[1], -21.0 * scale[0],
              3.0 * scale[1], -13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(941.0 * scale[0], 944.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(86.0 * scale[0], 923.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(763.0 * scale[0], 540.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -16.0 * scale[1], 7.0 * scale[0], -
              32.0 * scale[1], 14.0 * scale[0], -34.0 * scale[1])
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 10.0 * scale[0],
              1.0 * scale[1], 7.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 18.0 * scale[1], 52.0 * scale[0],
              19.0 * scale[1], 87.0 * scale[0], 1.0 * scale[1])
    Curveto_r(15.0 * scale[0], -8.0 * scale[1], 42.0 * scale[0], -
              28.0 * scale[1], 59.0 * scale[0], -43.0 * scale[1])
    Curveto_r(27.0 * scale[0], -25.0 * scale[1], 31.0 * scale[0], -
              35.0 * scale[1], 28.0 * scale[0], -68.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -38.0 * scale[1], -4.0 * scale[0], -
              38.0 * scale[1], -15.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 18.0 * scale[1], -12.0 * scale[0],
              20.0 * scale[1], -12.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -17.0 * scale[1], -21.0 * scale[0], -
              26.0 * scale[1], -21.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 19.0 * scale[1], -30.0 * scale[0],
              7.0 * scale[1], -31.0 * scale[0], -12.0 * scale[1])
    Curveto_r(0.0 * scale[0], -20.0 * scale[1], -1.0 * scale[0], -
              20.0 * scale[1], -8.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 19.0 * scale[1], -8.0 * scale[0],
              19.0 * scale[1], -19.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -14.0 * scale[1], -8.0 * scale[0], -
              24.0 * scale[1], -2.0 * scale[0], -28.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0], -
              12.0 * scale[1], 4.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], 17.0 * scale[0], -
              37.0 * scale[1], 45.0 * scale[0], -67.0 * scale[1])
    Curveto_r(28.0 * scale[0], -29.0 * scale[1], 51.0 * scale[0], -
              51.0 * scale[1], 52.0 * scale[0], -49.0 * scale[1])
    Curveto_r(0.0 * scale[0], 3.0 * scale[1], 3.0 * scale[0],
              14.0 * scale[1], 5.0 * scale[0], 25.0 * scale[1])
    Curveto_r(3.0 * scale[0], 11.0 * scale[1], 8.0 * scale[0],
              64.0 * scale[1], 11.0 * scale[0], 118.0 * scale[1])
    Curveto_r(5.0 * scale[0], 93.0 * scale[1], 5.0 * scale[0],
              99.0 * scale[1], -18.0 * scale[0], 124.0 * scale[1])
    Curveto_r(-31.0 * scale[0], 33.0 * scale[1], -101.0 * scale[0],
              63.0 * scale[1], -146.0 * scale[0], 63.0 * scale[1])
    Curveto_r(-27.0 * scale[0], 0.0 * scale[1], -34.0 * scale[0],
              3.0 * scale[1], -29.0 * scale[0], 15.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], 1.0 * scale[0],
              15.0 * scale[1], -4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              13.0 * scale[1], -7.0 * scale[0], -30.0 * scale[1])
    te.end_fill()
    Moveto(824.0 * scale[0], 403.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -18.0 * scale[1], 4.0 * scale[0], -
              33.0 * scale[1], 9.0 * scale[0], -33.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              3.0 * scale[1], 8.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], 2.0 * scale[0],
              15.0 * scale[1], 4.0 * scale[0], 25.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 0.0 * scale[0],
              15.0 * scale[1], -5.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -10.0 * scale[0],
              1.0 * scale[1], -13.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 7.0 * scale[1], -4.0 * scale[0], -
              2.0 * scale[1], -3.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(1.0 * scale[0], 324.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(14.0 * scale[0], 288.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 1.0 * scale[0], -
              20.0 * scale[1], -4.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -8.0 * scale[1], -13.0 * scale[0], -
              191.0 * scale[1], 0.0 * scale[0], -216.0 * scale[1])
    Curveto_r(9.0 * scale[0], -16.0 * scale[1], 22.0 * scale[0], -
              19.0 * scale[1], 93.0 * scale[0], -19.0 * scale[1])
    Curveto_r(46.0 * scale[0], 0.0 * scale[1], 87.0 * scale[0], -
              4.0 * scale[1], 93.0 * scale[0], -9.0 * scale[1])
    Curveto_r(5.0 * scale[0], -5.0 * scale[1], 50.0 * scale[0], -
              11.0 * scale[1], 99.0 * scale[0], -13.0 * scale[1])
    Lineto_r(90.0 * scale[0], -4.0 * scale[1])
    Lineto_r(-3.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 46.0 * scale[1], 14.0 * scale[0],
              148.0 * scale[1], 36.0 * scale[0], 203.0 * scale[1])
    Curveto_r(16.0 * scale[0], 37.0 * scale[1], 15.0 * scale[0],
              39.0 * scale[1], -6.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -3.0 * scale[1], -41.0 * scale[0], -
              8.0 * scale[1], -71.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-53.0 * scale[0], -5.0 * scale[1], -81.0 * scale[0], -
              18.0 * scale[1], -81.0 * scale[0], -37.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -16.0 * scale[0], -
              24.0 * scale[1], -35.0 * scale[0], -41.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -17.0 * scale[1], -35.0 *
              scale[0], -37.0 * scale[1], -35.0 * scale[0], -44.0 * scale[1])
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], -10.0 * scale[0], -
              16.0 * scale[1], -30.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 9.0 * scale[1], -12.0 * scale[0],
              10.0 * scale[1], 3.0 * scale[0], 5.0 * scale[1])
    Curveto_r(9.0 * scale[0], -3.0 * scale[1], 17.0 *
              scale[0], -1.0 * scale[1], 17.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -13.0 * scale[0],
              9.0 * scale[1], -37.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-28.0 * scale[0], -5.0 * scale[1], -34.0 *
              scale[0], -4.0 * scale[1], -23.0 * scale[0], 3.0 * scale[1])
    Curveto_r(16.0 * scale[0], 11.0 * scale[1], 8.0 * scale[0],
              15.0 * scale[1], -24.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -1.0 * scale[1], -15.0 * scale[0],
              3.0 * scale[1], -12.0 * scale[0], 8.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], -2.0 * scale[0],
              16.0 * scale[1], -12.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 13.0 * scale[1], -16.0 * scale[0],
              13.0 * scale[1], -2.0 * scale[0], -5.0 * scale[1])
    Curveto_r(14.0 * scale[0], -18.0 * scale[1], 13.0 * scale[0], -
              18.0 * scale[1], -9.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 5.0 * scale[1], -21.0 * scale[0],
              4.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 2.0 * scale[0], -
              11.0 * scale[1], -5.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0],
              11.0 * scale[1], 6.0 * scale[0], 55.0 * scale[1])
    Curveto_r(6.0 * scale[0], 17.0 * scale[1], 5.0 * scale[0],
              18.0 * scale[1], -5.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -13.0 * scale[1], -11.0 *
              scale[0], -12.0 * scale[1], -7.0 * scale[0], 6.0 * scale[1])
    Curveto_r(2.0 * scale[0], 12.0 * scale[1], -2.0 * scale[0],
              32.0 * scale[1], -10.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 13.0 * scale[1], -12.0 * scale[0],
              16.0 * scale[1], -9.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto_r(345.0 * scale[0], -207.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -30.0 * scale[1], -3.0 *
              scale[0], -31.0 * scale[1], -6.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 15.0 * scale[1], -9.0 * scale[0],
              27.0 * scale[1], -14.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              53.0 * scale[1], 6.0 * scale[0], -62.0 * scale[1])
    Curveto_r(6.0 * scale[0], -5.0 * scale[1], 3.0 * scale[0], -
              8.0 * scale[1], -7.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -18.0 * scale[0],
              5.0 * scale[1], -20.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 6.0 * scale[1], -23.0 * scale[0],
              11.0 * scale[1], -46.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-27.0 * scale[0], 0.0 * scale[1], -41.0 * scale[0],
              4.0 * scale[1], -39.0 * scale[0], 11.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 10.0 * scale[0],
              10.0 * scale[1], 16.0 * scale[0], 9.0 * scale[1])
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 11.0 * scale[0],
              1.0 * scale[1], 11.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], 72.0 * scale[0],
              49.0 * scale[1], 87.0 * scale[0], 43.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 12.0 * scale[0], -
              20.0 * scale[1], 12.0 * scale[0], -42.0 * scale[1])
    te.end_fill()
    Moveto_r(-116.0 * scale[0], -48.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              5.0 * scale[1], 12.0 * scale[0], 5.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#614941')
    te.end_fill()
    Moveto(39.0 * scale[0], 1067.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -5.0 * scale[1], 24.0 * scale[0], -
              7.0 * scale[1], 42.0 * scale[0], -5.0 * scale[1])
    Curveto_r(33.0 * scale[0], 3.0 * scale[1], 33.0 * scale[0],
              4.0 * scale[1], -8.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 3.0 * scale[1], -39.0 * scale[0],
              2.0 * scale[1], -34.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(90.0 * scale[0], 1050.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-56.0 * scale[0], -5.0 * scale[1], -33.0 *
              scale[0], -7.0 * scale[1], 93.0 * scale[0], -8.0 * scale[1])
    Curveto_r(92.0 * scale[0], -1.0 * scale[1], 167.0 * scale[0],
              2.0 * scale[1], 167.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], -144.0 * scale[0],
              10.0 * scale[1], -260.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(485.0 * scale[0], 1050.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(50.0 * scale[0], -4.0 * scale[1], 99.0 *
              scale[0], -4.0 * scale[1], 110.0 * scale[0], 1.0 * scale[1])
    Curveto_r(12.0 * scale[0], 4.0 * scale[1], -25.0 * scale[0],
              7.0 * scale[1], -90.0 * scale[0], 7.0 * scale[1])
    Lineto_r(-110.0 * scale[0], -1.0 * scale[1])
    Lineto_r(90.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(665.0 * scale[0], 1041.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -12.0 * scale[1], 179.0 *
              scale[0], -13.0 * scale[1], 209.0 * scale[0], -1.0 * scale[1])
    Curveto_r(14.0 * scale[0], 6.0 * scale[1], -18.0 * scale[0],
              9.0 * scale[1], -91.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-61.0 * scale[0], 1.0 * scale[1], -114.0 *
              scale[0], -3.0 * scale[1], -118.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(2.0 * scale[0], 927.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -65.0 * scale[1], 3.0 * scale[0], -
              116.0 * scale[1], 6.0 * scale[0], -112.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 5.0 * scale[0],
              28.0 * scale[1], 5.0 * scale[0], 55.0 * scale[1])
    Lineto_r(-1.0 * scale[0], 50.0 * scale[1])
    Lineto_r(19.0 * scale[0], -22.0 * scale[1])
    Curveto_r(22.0 * scale[0], -25.0 * scale[1], 21.0 *
              scale[0], -19.0 * scale[1], -1.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 23.0 * scale[1], -11.0 * scale[0],
              30.0 * scale[1], -1.0 * scale[0], 36.0 * scale[1])
    Curveto_r(10.0 * scale[0], 6.0 * scale[1], 9.0 * scale[0],
              9.0 * scale[1], -2.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 3.0 * scale[1], -18.0 * scale[0],
              21.0 * scale[1], -20.0 * scale[0], 39.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 18.0 * scale[1], -4.0 * scale[0], -
              20.0 * scale[1], -5.0 * scale[0], -85.0 * scale[1])
    te.end_fill()
    Moveto(890.0 * scale[0], 1022.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 11.0 * scale[0], -
              14.0 * scale[1], 25.0 * scale[0], -20.0 * scale[1])
    Curveto_r(14.0 * scale[0], -6.0 * scale[1], 25.0 * scale[0], -
              10.0 * scale[1], 25.0 * scale[0], -8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 2.0 * scale[1], -11.0 * scale[0],
              11.0 * scale[1], -25.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 9.0 * scale[1], -25.0 * scale[0],
              13.0 * scale[1], -25.0 * scale[0], 8.0 * scale[1])
    te.end_fill()
    Moveto(45.0 * scale[0], 1000.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -11.0 * scale[1], -14.0 *
              scale[0], -20.0 * scale[1], -9.0 * scale[0], -20.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              9.0 * scale[1], 22.0 * scale[0], 20.0 * scale[1])
    Curveto_r(7.0 * scale[0], 11.0 * scale[1], 11.0 * scale[0],
              20.0 * scale[1], 9.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              9.0 * scale[1], -22.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(848.0 * scale[0], 1013.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -2.0 * scale[1], -18.0 *
              scale[0], -9.0 * scale[1], -18.0 * scale[0], -14.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 10.0 *
              scale[0], -5.0 * scale[1], 23.0 * scale[0], 2.0 * scale[1])
    Curveto_r(37.0 * scale[0], 20.0 * scale[1], 36.0 * scale[0],
              23.0 * scale[1], -5.0 * scale[0], 12.0 * scale[1])
    te.end_fill()
    Moveto(953.0 * scale[0], 985.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -9.0 * scale[1], -9.0 * scale[0], -
              16.0 * scale[1], -3.0 * scale[0], -20.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 7.0 * scale[0], -
              11.0 * scale[1], 4.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -2.0 *
              scale[0], -8.0 * scale[1], 3.0 * scale[0], -5.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 16.0 * scale[0],
              59.0 * scale[1], 9.0 * scale[0], 57.0 * scale[1])
    Curveto_r(0.0 * scale[0], -1.0 * scale[1], -7.0 * scale[0], -
              7.0 * scale[1], -13.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(258.0 * scale[0], 904.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(23.0 * scale[0], -14.0 * scale[1], 47.0 * scale[0], -
              22.0 * scale[1], 54.0 * scale[0], -18.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 8.0 * scale[0],
              3.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -10.0 * scale[1], 17.0 * scale[0], -
              23.0 * scale[1], 38.0 * scale[0], -21.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0], -
              3.0 * scale[1], 15.0 * scale[0], -8.0 * scale[1])
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], 17.0 * scale[0], -
              17.0 * scale[1], 31.0 * scale[0], -28.0 * scale[1])
    Lineto_r(25.0 * scale[0], -20.0 * scale[1])
    Lineto_r(-18.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 21.0 * scale[1], -17.0 * scale[0],
              22.0 * scale[1], 10.0 * scale[0], 22.0 * scale[1])
    Curveto_r(15.0 * scale[0], 0.0 * scale[1], 37.0 * scale[0], -
              7.0 * scale[1], 48.0 * scale[0], -16.0 * scale[1])
    Curveto_r(11.0 * scale[0], -9.0 * scale[1], 7.0 * scale[0], -
              2.0 * scale[1], -9.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 21.0 * scale[1], -39.0 * scale[0],
              32.0 * scale[1], -56.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 0.0 * scale[1], -60.0 * scale[0],
              11.0 * scale[1], -100.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-91.0 * scale[0], 31.0 * scale[1], -95.0 * scale[0],
              31.0 * scale[1], -42.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(365.0 * scale[0], 910.0 * scale[1], x, y)
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
    Moveto(810.0 * scale[0], 911.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              15.0 * scale[1], 17.0 * scale[0], -22.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 15.0 *
              scale[0], -12.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 23.0 * scale[1], -21.0 * scale[0],
              28.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(99.0 * scale[0], 893.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -21.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(929.0 * scale[0], 893.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(16.0 * scale[0], 13.0 * scale[1], 21.0 * scale[0],
              21.0 * scale[1], 13.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              8.0 * scale[1], -17.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(160.0 * scale[0], 801.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(25.0 * scale[0], -8.0 * scale[1])
    Lineto_r(-25.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-24.0 * scale[0], -5.0 * scale[1], -24.0 *
              scale[0], -5.0 * scale[1], 3.0 * scale[0], -7.0 * scale[1])
    Curveto_r(36.0 * scale[0], -1.0 * scale[1], 32.0 * scale[0],
              23.0 * scale[1], -4.0 * scale[0], 26.0 * scale[1])
    Lineto_r(-24.0 * scale[0], 2.0 * scale[1])
    Lineto_r(25.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(520.0 * scale[0], 806.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(70.0 * scale[0], 790.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(36.0 * scale[0], -12.0 * scale[1], 60.0 *
              scale[0], -12.0 * scale[1], 60.0 * scale[0], 0.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -19.0 * scale[0],
              10.0 * scale[1], -42.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-37.0 * scale[0], -1.0 * scale[1], -39.0 *
              scale[0], -2.0 * scale[1], -18.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(365.0 * scale[0], 788.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-31.0 * scale[0], -18.0 * scale[1], -75.0 *
              scale[0], -86.0 * scale[1], -57.0 * scale[0], -89.0 * scale[1])
    Curveto_r(61.0 * scale[0], -10.0 * scale[1], 74.0 *
              scale[0], -8.0 * scale[1], 62.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 12.0 * scale[1], -9.0 * scale[0],
              20.0 * scale[1], 4.0 * scale[0], 40.0 * scale[1])
    Curveto_r(9.0 * scale[0], 14.0 * scale[1], 20.0 * scale[0],
              25.0 * scale[1], 25.0 * scale[0], 25.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0],
              7.0 * scale[1], 8.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 18.0 * scale[1], -14.0 * scale[0],
              19.0 * scale[1], -42.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(415.0 * scale[0], 791.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              12.0 * scale[1], 5.0 * scale[0], -16.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 10.0 * scale[0],
              1.0 * scale[1], 10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 18.0 * scale[1], -6.0 * scale[0],
              21.0 * scale[1], -15.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(3.0 * scale[0], 745.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -27.0 * scale[1], 2.0 * scale[0], -
              38.0 * scale[1], 4.0 * scale[0], -22.0 * scale[1])
    Curveto_r(2.0 * scale[0], 15.0 * scale[1], 2.0 * scale[0],
              37.0 * scale[1], 0.0 * scale[0], 50.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 12.0 * scale[1], -4.0 * scale[0],
              0.0 * scale[1], -4.0 * scale[0], -28.0 * scale[1])
    te.end_fill()
    Moveto(201.0 * scale[0], 734.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(179.0 * scale[0], 693.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(16.0 * scale[0], 13.0 * scale[1], 21.0 * scale[0],
              21.0 * scale[1], 13.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              8.0 * scale[1], -17.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(582.0 * scale[0], 673.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -17.0 * scale[1], -7.0 * scale[0], -
              44.0 * scale[1], -12.0 * scale[0], -59.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -16.0 * scale[1], -7.0 * scale[0], -
              31.0 * scale[1], -1.0 * scale[0], -38.0 * scale[1])
    Curveto_r(5.0 * scale[0], -6.0 * scale[1], 12.0 * scale[0], -
              28.0 * scale[1], 16.0 * scale[0], -48.0 * scale[1])
    Curveto_r(4.0 * scale[0], -21.0 * scale[1], 11.0 * scale[0], -
              35.0 * scale[1], 16.0 * scale[0], -32.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 9.0 * scale[0], -
              4.0 * scale[1], 9.0 * scale[0], -16.0 * scale[1])
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], -4.0 * scale[0], -
              18.0 * scale[1], -10.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -10.0 * scale[0], -
              12.0 * scale[1], -11.0 * scale[0], -39.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -25.0 * scale[1], -2.0 * scale[0], -
              49.0 * scale[1], -4.0 * scale[0], -53.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -55.0 * scale[1], -21.0 *
              scale[0], -69.0 * scale[1], -38.0 * scale[0], -86.0 * scale[1])
    Lineto_r(-20.0 * scale[0], -20.0 * scale[1])
    Lineto_r(6.0 * scale[0], 30.0 * scale[1])
    Curveto_r(3.0 * scale[0], 17.0 * scale[1], 9.0 * scale[0],
              44.0 * scale[1], 12.0 * scale[0], 59.0 * scale[1])
    Curveto_r(3.0 * scale[0], 16.0 * scale[1], -4.0 * scale[0],
              4.0 * scale[1], -15.0 * scale[0], -26.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -30.0 * scale[1], -25.0 *
              scale[0], -59.0 * scale[1], -30.0 * scale[0], -64.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              18.0 * scale[1], -10.0 * scale[0], -29.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], -4.0 * scale[0], -
              16.0 * scale[1], -8.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 2.0 * scale[1], -9.0 * scale[0], -
              7.0 * scale[1], -10.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -14.0 * scale[1], -6.0 * scale[0], -
              31.0 * scale[1], -12.0 * scale[0], -38.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -12.0 * scale[1], -4.0 *
              scale[0], -25.0 * scale[1], 12.0 * scale[0], -25.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0],
              6.0 * scale[1], 7.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 34.0 * scale[1], 3.0 * scale[0],
              40.0 * scale[1], 18.0 * scale[0], 13.0 * scale[1])
    Lineto_r(15.0 * scale[0], -29.0 * scale[1])
    Lineto_r(19.0 * scale[0], 24.0 * scale[1])
    Curveto_r(10.0 * scale[0], 13.0 * scale[1], 24.0 * scale[0],
              35.0 * scale[1], 31.0 * scale[0], 49.0 * scale[1])
    Curveto_r(7.0 * scale[0], 14.0 * scale[1], 21.0 * scale[0],
              37.0 * scale[1], 31.0 * scale[0], 52.0 * scale[1])
    Curveto_r(10.0 * scale[0], 15.0 * scale[1], 17.0 * scale[0],
              33.0 * scale[1], 16.0 * scale[0], 40.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 29.0 * scale[1], 4.0 * scale[0],
              131.0 * scale[1], 8.0 * scale[0], 113.0 * scale[1])
    Curveto_r(3.0 * scale[0], -11.0 * scale[1], 9.0 * scale[0], -
              24.0 * scale[1], 13.0 * scale[0], -30.0 * scale[1])
    Curveto_r(12.0 * scale[0], -15.0 * scale[1], 15.0 * scale[0], -
              88.0 * scale[1], 5.0 * scale[0], -105.0 * scale[1])
    Curveto_r(-24.0 * scale[0], -37.0 * scale[1], -31.0 *
              scale[0], -57.0 * scale[1], -29.0 * scale[0], -75.0 * scale[1])
    Curveto_r(12.0 * scale[0], -83.0 * scale[1], 14.0 * scale[0], -
              134.0 * scale[1], 5.0 * scale[0], -140.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -10.0 * scale[1], -13.0 *
              scale[0], -28.0 * scale[1], 4.0 * scale[0], -21.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 39.0 * scale[0],
              1.0 * scale[1], 68.0 * scale[0], -5.0 * scale[1])
    Curveto_r(124.0 * scale[0], -24.0 * scale[1], 189.0 *
              scale[0], -28.0 * scale[1], 195.0 * scale[0], -10.0 * scale[1])
    Curveto_r(2.0 * scale[0], 7.0 * scale[1], 9.0 * scale[0],
              8.0 * scale[1], 22.0 * scale[0], 1.0 * scale[1])
    Curveto_r(31.0 * scale[0], -17.0 * scale[1], 50.0 * scale[0],
              13.0 * scale[1], 50.0 * scale[0], 79.0 * scale[1])
    Curveto_r(0.0 * scale[0], 48.0 * scale[1], -4.0 * scale[0],
              61.0 * scale[1], -25.0 * scale[0], 81.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 12.0 * scale[1], -23.0 * scale[0],
              27.0 * scale[1], -22.0 * scale[0], 33.0 * scale[1])
    Curveto_r(1.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              10.0 * scale[1], -36.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 0.0 * scale[1], -37.0 * scale[0],
              3.0 * scale[1], -32.0 * scale[0], 15.0 * scale[1])
    Curveto_r(4.0 * scale[0], 12.0 * scale[1], 2.0 * scale[0],
              12.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -7.0 * scale[1], -16.0 *
              scale[0], -9.0 * scale[1], -19.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 2.0 * scale[1], -8.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -9.0 * scale[1], -2.0 * scale[0], -
              13.0 * scale[1], 4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(20.0 * scale[0], 12.0 * scale[1], 58.0 * scale[0], -
              8.0 * scale[1], 72.0 * scale[0], -38.0 * scale[1])
    Curveto_r(15.0 * scale[0], -31.0 * scale[1], 14.0 * scale[0], -
              33.0 * scale[1], -8.0 * scale[0], -50.0 * scale[1])
    Curveto_r(-23.0 * scale[0], -17.0 * scale[1], -24.0 *
              scale[0], -17.0 * scale[1], -30.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 14.0 * scale[1], -12.0 * scale[0],
              25.0 * scale[1], -19.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -43.0 * scale[0],
              29.0 * scale[1], -44.0 * scale[0], 43.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], -8.0 * scale[0],
              21.0 * scale[1], -16.0 * scale[0], 38.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 23.0 * scale[1], -13.0 * scale[0],
              34.0 * scale[1], -5.0 * scale[0], 44.0 * scale[1])
    Curveto_r(6.0 * scale[0], 7.0 * scale[1], 7.0 * scale[0],
              16.0 * scale[1], 2.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -7.0 * scale[0],
              29.0 * scale[1], -4.0 * scale[0], 57.0 * scale[1])
    Curveto_r(4.0 * scale[0], 39.0 * scale[1], 2.0 * scale[0],
              50.0 * scale[1], -7.0 * scale[0], 44.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -4.0 * scale[1], -10.0 * scale[0], -
              17.0 * scale[1], -6.0 * scale[0], -32.0 * scale[1])
    Curveto_r(3.0 * scale[0], -14.0 * scale[1], 1.0 * scale[0], -
              31.0 * scale[1], -5.0 * scale[0], -38.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -9.0 * scale[1], -6.0 * scale[0], -
              17.0 * scale[1], 5.0 * scale[0], -29.0 * scale[1])
    Curveto_r(14.0 * scale[0], -13.0 * scale[1], 14.0 *
              scale[0], -16.0 * scale[1], 2.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0],
              14.0 * scale[1], -26.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 41.0 * scale[1], -14.0 * scale[0],
              42.0 * scale[1], 7.0 * scale[0], 34.0 * scale[1])
    Curveto_r(14.0 * scale[0], -5.0 * scale[1], 15.0 *
              scale[0], -4.0 * scale[1], 5.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 8.0 * scale[1], -13.0 * scale[0],
              38.0 * scale[1], -13.0 * scale[0], 73.0 * scale[1])
    Curveto_r(0.0 * scale[0], 79.0 * scale[1], -7.0 * scale[0],
              68.0 * scale[1], -14.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -102.0 * scale[1], -16.0 * scale[0], -
              107.0 * scale[1], -20.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 22.0 * scale[1], -18.0 * scale[0],
              34.0 * scale[1], -28.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -7.0 * scale[1], -8.0 *
              scale[0], -3.0 * scale[1], -8.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 16.0 * scale[1], 4.0 * scale[0],
              21.0 * scale[1], 14.0 * scale[0], 18.0 * scale[1])
    Curveto_r(10.0 * scale[0], -4.0 * scale[1], 13.0 *
              scale[0], -1.0 * scale[1], 9.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], -9.0 * scale[0],
              13.0 * scale[1], -13.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -3.0 * scale[1], -10.0 * scale[0],
              2.0 * scale[1], -14.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], -1.0 * scale[0],
              15.0 * scale[1], 3.0 * scale[0], 15.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              10.0 * scale[1], 3.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 21.0 * scale[1], -6.0 * scale[0],
              21.0 * scale[1], -13.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -16.0 * scale[1], -8.0 *
              scale[0], -15.0 * scale[1], -8.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 15.0 * scale[1], 3.0 * scale[0],
              27.0 * scale[1], 8.0 * scale[0], 27.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 2.0 * scale[0],
              111.0 * scale[1], -10.0 * scale[0], 125.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 5.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -9.0 * scale[0], -18.0 * scale[1])
    Curveto_r(0.0 * scale[0], -38.0 * scale[1], -18.0 *
              scale[0], -34.0 * scale[1], -23.0 * scale[0], 6.0 * scale[1])
    Lineto_r(-4.0 * scale[0], 32.0 * scale[1])
    Lineto_r(-1.0 * scale[0], -32.0 * scale[1])
    te.end_fill()
    Moveto_r(33.0 * scale[0], -87.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -25.0 * scale[1], -11.0 * scale[0], -
              46.0 * scale[1], -15.0 * scale[0], -46.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0],
              10.0 * scale[1], -2.0 * scale[0], 22.0 * scale[1])
    Curveto_r(3.0 * scale[0], 14.0 * scale[1], 2.0 * scale[0],
              19.0 * scale[1], -6.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -11.0 * scale[1], -14.0 *
              scale[0], 5.0 * scale[1], 6.0 * scale[0], 21.0 * scale[1])
    Curveto_r(9.0 * scale[0], 8.0 * scale[1], 11.0 * scale[0],
              12.0 * scale[1], 5.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -4.0 * scale[1], -13.0 * scale[0],
              0.0 * scale[1], -13.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], 20.0 * scale[0],
              28.0 * scale[1], 28.0 * scale[0], 21.0 * scale[1])
    Curveto_r(2.0 * scale[0], -2.0 * scale[1], 0.0 * scale[0], -
              24.0 * scale[1], -3.0 * scale[0], -49.0 * scale[1])
    te.end_fill()
    Moveto_r(176.0 * scale[0], -473.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(17.0 * scale[0], -27.0 * scale[1], 38.0 * scale[0], -
              53.0 * scale[1], 45.0 * scale[0], -59.0 * scale[1])
    Curveto_r(18.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              34.0 * scale[1], -22.0 * scale[0], -28.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 3.0 * scale[1], -33.0 * scale[0],
              29.0 * scale[1], -50.0 * scale[0], 62.0 * scale[1])
    Curveto_r(-39.0 * scale[0], 75.0 * scale[1], -38.0 * scale[0],
              72.0 * scale[1], -20.0 * scale[0], 72.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 29.0 * scale[0], -
              21.0 * scale[1], 47.0 * scale[0], -47.0 * scale[1])
    te.end_fill()
    Moveto(2.0 * scale[0], 660.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 2.0 * scale[0], -
              27.0 * scale[1], 5.0 * scale[0], -17.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              25.0 * scale[1], 0.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(292.0 * scale[0], 674.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -8.0 * scale[1], -17.0 * scale[0], -
              12.0 * scale[1], -22.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0], -
              1.0 * scale[1], -13.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], 21.0 * scale[0], -
              32.0 * scale[1], 31.0 * scale[0], -21.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 0.0 * scale[0],
              5.0 * scale[1], -7.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], 10.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], 10.0 * scale[0],
              8.0 * scale[1], 15.0 * scale[0], 5.0 * scale[1])
    Curveto_r(4.0 * scale[0], -3.0 * scale[1], 11.0 * scale[0],
              2.0 * scale[1], 14.0 * scale[0], 11.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], 11.0 * scale[0],
              12.0 * scale[1], 17.0 * scale[0], 8.0 * scale[1])
    Curveto_r(8.0 * scale[0], -4.0 * scale[1], 9.0 *
              scale[0], -3.0 * scale[1], 5.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 16.0 * scale[1], -18.0 * scale[0],
              15.0 * scale[1], -34.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(371.0 * scale[0], 666.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -9.0 * scale[1], -11.0 * scale[0], -
              19.0 * scale[1], -7.0 * scale[0], -23.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 6.0 * scale[0],
              0.0 * scale[1], 6.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], 6.0 * scale[0],
              8.0 * scale[1], 20.0 * scale[0], -5.0 * scale[1])
    Curveto_r(22.0 * scale[0], -20.0 * scale[1], 27.0 *
              scale[0], -8.0 * scale[1], 7.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 16.0 * scale[1], -14.0 * scale[0],
              16.0 * scale[1], -26.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(240.0 * scale[0], 615.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], -17.0 * scale[0], -
              20.0 * scale[1], -47.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 1.0 * scale[1], -13.0 * scale[0], -
              5.0 * scale[1], -13.0 * scale[0], -13.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -3.0 * scale[0], -
              23.0 * scale[1], -6.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -15.0 * scale[1], -4.0 *
              scale[0], -16.0 * scale[1], 6.0 * scale[0], -3.0 * scale[1])
    Curveto_r(10.0 * scale[0], 13.0 * scale[1], 11.0 * scale[0],
              12.0 * scale[1], 6.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -10.0 * scale[1], -6.0 * scale[0], -
              21.0 * scale[1], -6.0 * scale[0], -23.0 * scale[1])
    Curveto_r(0.0 * scale[0], -3.0 * scale[1], -4.0 * scale[0], -
              2.0 * scale[1], -10.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -7.0 * scale[0], -
              1.0 * scale[1], -3.0 * scale[0], -11.0 * scale[1])
    Curveto_r(4.0 * scale[0], -11.0 * scale[1], 2.0 * scale[0], -
              15.0 * scale[1], -4.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -14.0 * scale[0],
              0.0 * scale[1], -17.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -26.0 * scale[1], -7.0 *
              scale[0], -28.0 * scale[1], 12.0 * scale[0], -11.0 * scale[1])
    Curveto_r(10.0 * scale[0], 10.0 * scale[1], 33.0 * scale[0],
              16.0 * scale[1], 53.0 * scale[0], 15.0 * scale[1])
    Curveto_r(20.0 * scale[0], -1.0 * scale[1], 41.0 * scale[0],
              2.0 * scale[1], 47.0 * scale[0], 6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 4.0 * scale[1], 9.0 * scale[0], -
              5.0 * scale[1], 5.0 * scale[0], -29.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -27.0 * scale[1], -2.0 * scale[0], -
              35.0 * scale[1], 10.0 * scale[0], -35.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0],
              7.0 * scale[1], 11.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 15.0 * scale[1], -1.0 * scale[0],
              13.0 * scale[1], 9.0 * scale[0], -8.0 * scale[1])
    Curveto_r(9.0 * scale[0], -19.0 * scale[1], 11.0 * scale[0], -
              36.0 * scale[1], 6.0 * scale[0], -47.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -24.0 * scale[1], -11.0 *
              scale[0], -28.0 * scale[1], 6.0 * scale[0], -22.0 * scale[1])
    Curveto_r(9.0 * scale[0], 4.0 * scale[1], 18.0 * scale[0], -
              2.0 * scale[1], 24.0 * scale[0], -17.0 * scale[1])
    Curveto_r(5.0 * scale[0], -13.0 * scale[1], 10.0 * scale[0], -
              18.0 * scale[1], 10.0 * scale[0], -11.0 * scale[1])
    Curveto_r(1.0 * scale[0], 10.0 * scale[1], 5.0 * scale[0],
              10.0 * scale[1], 17.0 * scale[0], -2.0 * scale[1])
    Curveto_r(18.0 * scale[0], -19.0 * scale[1], 26.0 *
              scale[0], -20.0 * scale[1], 40.0 * scale[0], -6.0 * scale[1])
    Curveto_r(8.0 * scale[0], 8.0 * scale[1], 36.0 * scale[0],
              14.0 * scale[1], 92.0 * scale[0], 19.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              5.0 * scale[1], 7.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], 3.0 * scale[0],
              16.0 * scale[1], 13.0 * scale[0], 23.0 * scale[1])
    Curveto_r(10.0 * scale[0], 7.0 * scale[1], 24.0 * scale[0],
              27.0 * scale[1], 30.0 * scale[0], 43.0 * scale[1])
    Lineto_r(10.0 * scale[0], 30.0 * scale[1])
    Lineto_r(3.0 * scale[0], -40.0 * scale[1])
    Curveto_r(1.0 * scale[0], -27.0 * scale[1], 3.0 * scale[0], -
              32.0 * scale[1], 6.0 * scale[0], -16.0 * scale[1])
    Curveto_r(3.0 * scale[0], 13.0 * scale[1], 2.0 * scale[0],
              45.0 * scale[1], -2.0 * scale[0], 70.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 45.0 * scale[1], -7.0 * scale[0],
              45.0 * scale[1], -21.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -22.0 * scale[1], -13.0 *
              scale[0], -23.0 * scale[1], -14.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 18.0 * scale[1], -2.0 * scale[0],
              17.0 * scale[1], -13.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -32.0 * scale[1], -72.0 *
              scale[0], -69.0 * scale[1], -96.0 * scale[0], -63.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 5.0 * scale[1], -38.0 * scale[0],
              74.0 * scale[1], -25.0 * scale[0], 95.0 * scale[1])
    Curveto_r(5.0 * scale[0], 8.0 * scale[1], 1.0 * scale[0],
              9.0 * scale[1], -11.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -5.0 * scale[1], -16.0 *
              scale[0], -4.0 * scale[1], -5.0 * scale[0], 9.0 * scale[1])
    Curveto_r(7.0 * scale[0], 8.0 * scale[1], 16.0 * scale[0],
              13.0 * scale[1], 20.0 * scale[0], 10.0 * scale[1])
    Curveto_r(9.0 * scale[0], -6.0 * scale[1], 35.0 * scale[0],
              23.0 * scale[1], 28.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -22.0 * scale[0], -
              6.0 * scale[1], -42.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-41.0 * scale[0], -27.0 * scale[1], -51.0 *
              scale[0], -31.0 * scale[1], -40.0 * scale[0], -13.0 * scale[1])
    Curveto_r(5.0 * scale[0], 7.0 * scale[1], 3.0 * scale[0],
              8.0 * scale[1], -5.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -5.0 * scale[1], -21.0 * scale[0],
              0.0 * scale[1], -31.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 14.0 * scale[1], -21.0 * scale[0],
              15.0 * scale[1], -33.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -7.0 * scale[1], -12.0 * scale[0], -
              22.0 * scale[1], -9.0 * scale[0], -33.0 * scale[1])
    Curveto_r(3.0 * scale[0], -13.0 * scale[1], 1.0 * scale[0], -
              17.0 * scale[1], -6.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -10.0 * scale[0],
              24.0 * scale[1], -6.0 * scale[0], 57.0 * scale[1])
    Curveto_r(3.0 * scale[0], 27.0 * scale[1], 3.0 * scale[0],
              49.0 * scale[1], 0.0 * scale[0], 49.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0], -
              7.0 * scale[1], -6.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto_r(45.0 * scale[0], -55.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              10.0 * scale[1], 4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0], -
              6.0 * scale[1], 11.0 * scale[0], -13.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -7.0 * scale[0], -
              14.0 * scale[1], -15.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 0.0 * scale[1], -21.0 * scale[0],
              28.0 * scale[1], -8.0 * scale[0], 40.0 * scale[1])
    Curveto_r(10.0 * scale[0], 10.0 * scale[1], 15.0 * scale[0],
              8.0 * scale[1], 8.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto_r(65.0 * scale[0], -49.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -4.0 * scale[0], -
              13.0 * scale[1], -10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -10.0 * scale[0], -
              15.0 * scale[1], -10.0 * scale[0], -25.0 * scale[1])
    Curveto_r(0.0 * scale[0], -20.0 * scale[1], -16.0 * scale[0], -
              36.0 * scale[1], -23.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 12.0 * scale[1], 21.0 * scale[0],
              73.0 * scale[1], 33.0 * scale[0], 73.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              4.0 * scale[1], 10.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(141.0 * scale[0], 604.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(338.0 * scale[0], 613.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -2.0 * scale[1], -18.0 *
              scale[0], -9.0 * scale[1], -18.0 * scale[0], -14.0 * scale[1])
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 16.0 *
              scale[0], -11.0 * scale[1], 30.0 * scale[0], 6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 8.0 * scale[1], 11.0 * scale[0],
              14.0 * scale[1], 9.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -1.0 * scale[1], -12.0 *
              scale[0], -3.0 * scale[1], -21.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(420.0 * scale[0], 610.0 * scale[1], x, y)
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
    Moveto(135.0 * scale[0], 434.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -14.0 * scale[1], -30.0 *
              scale[0], -39.0 * scale[1], -37.0 * scale[0], -55.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -16.0 * scale[1], -19.0 * scale[0], -
              27.0 * scale[1], -25.0 * scale[0], -24.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 2.0 * scale[1], -13.0 * scale[0],
              0.0 * scale[1], -13.0 * scale[0], -6.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -6.0 * scale[0], -
              7.0 * scale[1], -12.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 6.0 * scale[1], -11.0 * scale[0],
              4.0 * scale[1], 0.0 * scale[0], -7.0 * scale[1])
    Curveto_r(6.0 * scale[0], -7.0 * scale[1], 12.0 * scale[0], -
              26.0 * scale[1], 12.0 * scale[0], -42.0 * scale[1])
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 4.0 * scale[0], -
              26.0 * scale[1], 10.0 * scale[0], -22.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 10.0 * scale[0], -
              2.0 * scale[1], 10.0 * scale[0], -12.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 5.0 * scale[0], -
              25.0 * scale[1], 11.0 * scale[0], -33.0 * scale[1])
    Curveto_r(8.0 * scale[0], -12.0 * scale[1], 9.0 *
              scale[0], -9.0 * scale[1], 5.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 14.0 * scale[1], -9.0 * scale[0],
              34.0 * scale[1], -13.0 * scale[0], 44.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 13.0 * scale[1], -3.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 9.0 * scale[1])
    Curveto_r(9.0 * scale[0], -5.0 * scale[1], 11.0 *
              scale[0], -4.0 * scale[1], 6.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], -2.0 * scale[0],
              19.0 * scale[1], 5.0 * scale[0], 27.0 * scale[1])
    Curveto_r(10.0 * scale[0], 12.0 * scale[1], 14.0 * scale[0],
              12.0 * scale[1], 21.0 * scale[0], 2.0 * scale[1])
    Curveto_r(7.0 * scale[0], -9.0 * scale[1], 8.0 * scale[0], -
              5.0 * scale[1], 5.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 35.0 * scale[1], 24.0 * scale[0],
              94.0 * scale[1], 45.0 * scale[0], 93.0 * scale[1])
    Curveto_r(9.0 * scale[0], -1.0 * scale[1], 19.0 * scale[0],
              5.0 * scale[1], 22.0 * scale[0], 12.0 * scale[1])
    Curveto_r(9.0 * scale[0], 25.0 * scale[1], -33.0 * scale[0],
              16.0 * scale[1], -59.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(216.0 * scale[0], 445.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -8.0 * scale[1], 10.0 * scale[0], -
              12.0 * scale[1], 15.0 * scale[0], -9.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 9.0 * scale[0], -
              5.0 * scale[1], 9.0 * scale[0], -17.0 * scale[1])
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], 3.0 * scale[0], -
              20.0 * scale[1], 6.0 * scale[0], -16.0 * scale[1])
    Curveto_r(11.0 * scale[0], 11.0 * scale[1], -6.0 * scale[0],
              57.0 * scale[1], -21.0 * scale[0], 57.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              6.0 * scale[1], -9.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(769.0 * scale[0], 338.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -28.0 * scale[1], 6.0 * scale[0], -
              29.0 * scale[1], 9.0 * scale[0], -9.0 * scale[1])
    Curveto_r(2.0 * scale[0], 13.0 * scale[1], 0.0 * scale[0],
              27.0 * scale[1], -5.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 6.0 * scale[1], -7.0 * scale[0], -
              3.0 * scale[1], -4.0 * scale[0], -23.0 * scale[1])
    te.end_fill()
    Moveto(257.0 * scale[0], 313.0 * scale[1], x, y)
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
    Moveto(800.0 * scale[0], 296.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -6.0 * scale[0], -
              16.0 * scale[1], -12.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -3.0 * scale[1], -3.0 *
              scale[0], -7.0 * scale[1], 8.0 * scale[0], -10.0 * scale[1])
    Curveto_r(17.0 * scale[0], -4.0 * scale[1], 20.0 *
              scale[0], -1.0 * scale[1], 16.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 26.0 * scale[1], -12.0 * scale[0],
              32.0 * scale[1], -12.0 * scale[0], 10.0 * scale[1])
    te.end_fill()
    Moveto(229.0 * scale[0], 253.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -21.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(170.0 * scale[0], 230.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -5.0 * scale[1], -25.0 * scale[0], -
              10.0 * scale[1], -37.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -23.0 * scale[0], -
              4.0 * scale[1], -23.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 9.0 * scale[0], -
              10.0 * scale[1], 20.0 * scale[0], -10.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0], -
              5.0 * scale[1], 20.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 9.0 * scale[0], -
              9.0 * scale[1], 20.0 * scale[0], -6.0 * scale[1])
    Curveto_r(10.0 * scale[0], 3.0 * scale[1], 21.0 * scale[0],
              0.0 * scale[1], 24.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], -7.0 * scale[1], 5.0 *
              scale[0], -7.0 * scale[1], 5.0 * scale[0], 2.0 * scale[1])
    Curveto_r(2.0 * scale[0], 24.0 * scale[1], 1.0 * scale[0],
              27.0 * scale[1], -9.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 3.0 * scale[1], -22.0 * scale[0],
              4.0 * scale[1], -10.0 * scale[0], 19.0 * scale[1])
    Curveto_r(14.0 * scale[0], 17.0 * scale[1], 11.0 * scale[0],
              19.0 * scale[1], -10.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(920.0 * scale[0], 216.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(398.0 * scale[0], 3.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.penup()
