import turtle as te
from helper import *


def panda_male(x, y, scale):

    te.penup()
    te.color('#6d9fae')
    te.end_fill()
    Moveto(416.0 * scale[0], 1352.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], -1.0 * scale[0], -
              14.0 * scale[1], 5.0 * scale[0], -17.0 * scale[1])
    Curveto_r(14.0 * scale[0], -9.0 * scale[1], 20.0 *
              scale[0], -2.0 * scale[1], 10.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 8.0 * scale[1], -11.0 * scale[0],
              9.0 * scale[1], -15.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(557.0 * scale[0], 1347.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], 1.0 * scale[0], -
              14.0 * scale[1], 9.0 * scale[0], -14.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              6.0 * scale[1], 18.0 * scale[0], 14.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], -1.0 * scale[0],
              13.0 * scale[1], -8.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0], -
              6.0 * scale[1], -19.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(102.0 * scale[0], 1287.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-22.0 * scale[0], -23.0 * scale[1], -32.0 *
              scale[0], -42.0 * scale[1], -32.0 * scale[0], -65.0 * scale[1])
    Curveto_r(0.0 * scale[0], -29.0 * scale[1], 3.0 * scale[0], -
              32.0 * scale[1], 29.0 * scale[0], -32.0 * scale[1])
    Curveto_r(20.0 * scale[0], 0.0 * scale[1], 30.0 * scale[0], -
              6.0 * scale[1], 34.0 * scale[0], -20.0 * scale[1])
    Curveto_r(6.0 * scale[0], -23.0 * scale[1], 37.0 *
              scale[0], -17.0 * scale[1], 37.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 4.0 * scale[0],
              14.0 * scale[1], 9.0 * scale[0], 14.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              9.0 * scale[1], 4.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 20.0 * scale[1], -21.0 * scale[0],
              24.0 * scale[1], -73.0 * scale[0], 20.0 * scale[1])
    Lineto_r(-25.0 * scale[0], -1.0 * scale[1])
    Lineto_r(23.0 * scale[0], 16.0 * scale[1])
    Curveto_r(23.0 * scale[0], 17.0 * scale[1], 31.0 * scale[0],
              42.0 * scale[1], 10.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -4.0 * scale[1], -4.0 * scale[0],
              2.0 * scale[1], 6.0 * scale[0], 14.0 * scale[1])
    Curveto_r(22.0 * scale[0], 26.0 * scale[1], 35.0 * scale[0],
              30.0 * scale[1], 15.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -14.0 * scale[1], -12.0 *
              scale[0], -16.0 * scale[1], 1.0 * scale[0], -11.0 * scale[1])
    Curveto_r(8.0 * scale[0], 2.0 * scale[1], 15.0 * scale[0],
              11.0 * scale[1], 15.0 * scale[0], 18.0 * scale[1])
    Curveto_r(0.0 * scale[0], 25.0 * scale[1], -21.0 * scale[0],
              20.0 * scale[1], -53.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(831.0 * scale[0], 1285.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-17.0 * scale[0], -20.0 * scale[1], -31.0 *
              scale[0], -43.0 * scale[1], -31.0 * scale[0], -51.0 * scale[1])
    Curveto_r(0.0 * scale[0], -20.0 * scale[1], 24.0 * scale[0], -
              44.0 * scale[1], 44.0 * scale[0], -44.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 18.0 * scale[0], -
              9.0 * scale[1], 21.0 * scale[0], -20.0 * scale[1])
    Curveto_r(3.0 * scale[0], -11.0 * scale[1], 10.0 * scale[0], -
              20.0 * scale[1], 15.0 * scale[0], -20.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              9.0 * scale[1], 15.0 * scale[0], 20.0 * scale[1])
    Curveto_r(3.0 * scale[0], 11.0 * scale[1], 10.0 * scale[0],
              20.0 * scale[1], 14.0 * scale[0], 20.0 * scale[1])
    Curveto_r(18.0 * scale[0], 0.0 * scale[1], 5.0 * scale[0],
              45.0 * scale[1], -14.0 * scale[0], 49.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 3.0 * scale[1], -18.0 * scale[0],
              2.0 * scale[1], -5.0 * scale[0], -15.0 * scale[1])
    Curveto_r(14.0 * scale[0], -18.0 * scale[1], 14.0 *
              scale[0], -18.0 * scale[1], -5.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 9.0 * scale[1], -26.0 * scale[0],
              14.0 * scale[1], -32.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -6.0 * scale[1], -16.0 * scale[0],
              12.0 * scale[1], 1.0 * scale[0], 26.0 * scale[1])
    Curveto_r(11.0 * scale[0], 9.0 * scale[1], 20.0 * scale[0],
              61.0 * scale[1], 11.0 * scale[0], 61.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0], -
              16.0 * scale[1], -34.0 * scale[0], -35.0 * scale[1])
    te.end_fill()
    Moveto_r(29.0 * scale[0], 1.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], -8.0 * scale[0], -
              10.0 * scale[1], -17.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -13.0 * scale[1], -17.0 *
              scale[0], -12.0 * scale[1], -4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(13.0 * scale[0], 16.0 * scale[1], 21.0 * scale[0],
              21.0 * scale[1], 21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(505.0 * scale[0], 1280.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 13.0 * scale[0], -
              10.0 * scale[1], 21.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0], -
              4.0 * scale[1], 9.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 3.0 * scale[0], -
              10.0 * scale[1], 14.0 * scale[0], -10.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 21.0 * scale[0], -
              2.0 * scale[1], 21.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 3.0 * scale[0], -
              13.0 * scale[1], 6.0 * scale[0], -23.0 * scale[1])
    Curveto_r(5.0 * scale[0], -17.0 * scale[1], 5.0 * scale[0], -
              17.0 * scale[1], -6.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 18.0 * scale[1], -36.0 * scale[0],
              25.0 * scale[1], -25.0 * scale[0], 7.0 * scale[1])
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 1.0 * scale[0], -
              18.0 * scale[1], -7.0 * scale[0], -27.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -14.0 * scale[1], -11.0 *
              scale[0], -16.0 * scale[1], 1.0 * scale[0], -8.0 * scale[1])
    Curveto_r(11.0 * scale[0], 6.0 * scale[1], 13.0 * scale[0],
              4.0 * scale[1], 8.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -9.0 * scale[1], 0.0 * scale[0], -
              21.0 * scale[1], 6.0 * scale[0], -27.0 * scale[1])
    Curveto_r(14.0 * scale[0], -14.0 * scale[1], 30.0 *
              scale[0], -15.0 * scale[1], 22.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -1.0 * scale[0],
              10.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0],
              59.0 * scale[1], 2.0 * scale[0], 78.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 14.0 * scale[1], -57.0 * scale[0],
              42.0 * scale[1], -73.0 * scale[0], 42.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0], -
              4.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(424.0 * scale[0], 1265.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -14.0 * scale[1], -19.0 *
              scale[0], -14.0 * scale[1], 2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 24.0 * scale[0],
              7.0 * scale[1], 28.0 * scale[0], 15.0 * scale[1])
    Curveto_r(7.0 * scale[0], 19.0 * scale[1], -5.0 * scale[0],
              19.0 * scale[1], -30.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(400.0 * scale[0], 1233.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -18.0 * scale[1], 18.0 * scale[0], -
              35.0 * scale[1], 24.0 * scale[0], -24.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], 4.0 * scale[0],
              11.0 * scale[1], -1.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], 7.0 * scale[0], 10.0 * scale[1])
    Curveto_r(12.0 * scale[0], 8.0 * scale[1], 11.0 * scale[0],
              10.0 * scale[1], -7.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -23.0 *
              scale[0], -3.0 * scale[1], -23.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(465.0 * scale[0], 1130.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#cfe0a4')
    te.end_fill()
    Moveto(419.0 * scale[0], 801.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -9.0 * scale[1], -33.0 * scale[0], -
              27.0 * scale[1], -53.0 * scale[0], -41.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -14.0 * scale[1], -36.0 *
              scale[0], -31.0 * scale[1], -36.0 * scale[0], -37.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -4.0 * scale[0], -
              13.0 * scale[1], -8.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -33.0 * scale[0], -
              50.0 * scale[1], -25.0 * scale[0], -63.0 * scale[1])
    Curveto_r(13.0 * scale[0], -21.0 * scale[1], 11.0 * scale[0], -
              52.0 * scale[1], -4.0 * scale[0], -69.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -20.0 * scale[1], -30.0 *
              scale[0], -98.0 * scale[1], -15.0 * scale[0], -98.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0], -
              8.0 * scale[1], 15.0 * scale[0], -17.0 * scale[1])
    Curveto_r(4.0 * scale[0], -17.0 * scale[1], 5.0 *
              scale[0], -17.0 * scale[1], 6.0 * scale[0], 0.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], 7.0 * scale[0],
              17.0 * scale[1], 15.0 * scale[0], 17.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0],
              9.0 * scale[1], 19.0 * scale[0], 20.0 * scale[1])
    Curveto_r(3.0 * scale[0], 13.0 * scale[1], 0.0 * scale[0],
              20.0 * scale[1], -9.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -31.0 * scale[0],
              46.0 * scale[1], -20.0 * scale[0], 57.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], 6.0 * scale[0], -
              2.0 * scale[1], 6.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 3.0 * scale[0], -
              15.0 * scale[1], 25.0 * scale[0], 5.0 * scale[1])
    Curveto_r(13.0 * scale[0], 13.0 * scale[1], 25.0 * scale[0],
              33.0 * scale[1], 25.0 * scale[0], 44.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], 17.0 * scale[0],
              40.0 * scale[1], 38.0 * scale[0], 64.0 * scale[1])
    Curveto_r(37.0 * scale[0], 43.0 * scale[1], 41.0 * scale[0],
              45.0 * scale[1], 105.0 * scale[0], 49.0 * scale[1])
    Curveto_r(65.0 * scale[0], 4.0 * scale[1], 66.0 * scale[0],
              4.0 * scale[1], 116.0 * scale[0], -38.0 * scale[1])
    Curveto_r(34.0 * scale[0], -29.0 * scale[1], 51.0 * scale[0], -
              51.0 * scale[1], 51.0 * scale[0], -66.0 * scale[1])
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], 4.0 * scale[0], -
              25.0 * scale[1], 9.0 * scale[0], -28.0 * scale[1])
    Curveto_r(4.0 * scale[0], -3.0 * scale[1], 11.0 * scale[0], -
              24.0 * scale[1], 15.0 * scale[0], -46.0 * scale[1])
    Curveto_r(3.0 * scale[0], -22.0 * scale[1], 11.0 * scale[0], -
              40.0 * scale[1], 17.0 * scale[0], -40.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0], -
              4.0 * scale[1], 4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              10.0 * scale[1], 3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              33.0 * scale[1], 16.0 * scale[0], 73.0 * scale[1])
    Curveto_r(5.0 * scale[0], 62.0 * scale[1], 3.0 * scale[0],
              81.0 * scale[1], -15.0 * scale[0], 121.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 33.0 * scale[1], -25.0 * scale[0],
              46.0 * scale[1], -35.0 * scale[0], 42.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -3.0 * scale[1], -13.0 *
              scale[0], -2.0 * scale[1], -10.0 * scale[0], 2.0 * scale[1])
    Curveto_r(6.0 * scale[0], 10.0 * scale[1], -22.0 * scale[0],
              47.0 * scale[1], -30.0 * scale[0], 39.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -22.0 * scale[0],
              3.0 * scale[1], -43.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-32.0 * scale[0], 18.0 * scale[1], -63.0 * scale[0],
              25.0 * scale[1], -141.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 1.0 * scale[1], -32.0 * scale[0], -
              5.0 * scale[1], -41.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(700.0 * scale[0], 471.0 * scale[1], x, y)
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
    Moveto(660.0 * scale[0], 80.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -12.0 * scale[1], -18.0 *
              scale[0], -26.0 * scale[1], -14.0 * scale[0], -32.0 * scale[1])
    Curveto_r(4.0 * scale[0], -7.0 * scale[1], 14.0 * scale[0], -
              2.0 * scale[1], 25.0 * scale[0], 13.0 * scale[1])
    Curveto_r(31.0 * scale[0], 40.0 * scale[1], 23.0 * scale[0],
              53.0 * scale[1], -11.0 * scale[0], 19.0 * scale[1])
    te.end_fill()
    Moveto(965.0 * scale[0], 20.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -7.0 * scale[1], -17.0 *
              scale[0], -9.0 * scale[1], -3.0 * scale[0], -9.0 * scale[1])
    Curveto_r(9.0 * scale[0], -1.0 * scale[1], 20.0 * scale[0],
              4.0 * scale[1], 23.0 * scale[0], 9.0 * scale[1])
    Curveto_r(7.0 * scale[0], 11.0 * scale[1], 7.0 * scale[0],
              11.0 * scale[1], -20.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(28.0 * scale[0], 8.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -6.0 * scale[1], 18.0 * scale[0], -
              8.0 * scale[1], 28.0 * scale[0], -6.0 * scale[1])
    Curveto_r(14.0 * scale[0], 3.0 * scale[1], 12.0 * scale[0],
              5.0 * scale[1], -9.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 3.0 * scale[1], -25.0 * scale[0],
              2.0 * scale[1], -19.0 * scale[0], -4.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#bdcc86')
    te.end_fill()
    Moveto(385.0 * scale[0], 838.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -7.0 * scale[1], -21.0 * scale[0], -
              28.0 * scale[1], -34.0 * scale[0], -46.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -18.0 * scale[1], -26.0 *
              scale[0], -30.0 * scale[1], -31.0 * scale[0], -27.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 8.0 * scale[1], -63.0 * scale[0], -
              102.0 * scale[1], -57.0 * scale[0], -124.0 * scale[1])
    Curveto_r(3.0 * scale[0], -12.0 * scale[1], -1.0 * scale[0], -
              22.0 * scale[1], -10.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -4.0 * scale[1], -13.0 * scale[0], -
              13.0 * scale[1], -9.0 * scale[0], -23.0 * scale[1])
    Curveto_r(4.0 * scale[0], -9.0 * scale[1], 1.0 * scale[0], -
              20.0 * scale[1], -5.0 * scale[0], -24.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -9.0 * scale[1], -21.0 * scale[0], -
              96.0 * scale[1], -8.0 * scale[0], -104.0 * scale[1])
    Curveto_r(5.0 * scale[0], -4.0 * scale[1], 9.0 * scale[0], -
              13.0 * scale[1], 9.0 * scale[0], -21.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 7.0 * scale[0], -
              23.0 * scale[1], 16.0 * scale[0], -31.0 * scale[1])
    Curveto_r(13.0 * scale[0], -14.0 * scale[1], 17.0 *
              scale[0], -14.0 * scale[1], 25.0 * scale[0], -2.0 * scale[1])
    Curveto_r(12.0 * scale[0], 19.0 * scale[1], 11.0 * scale[0],
              69.0 * scale[1], -1.0 * scale[0], 69.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0],
              41.0 * scale[1], 9.0 * scale[0], 102.0 * scale[1])
    Curveto_r(12.0 * scale[0], 36.0 * scale[1], 16.0 * scale[0],
              59.0 * scale[1], 10.0 * scale[0], 65.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 11.0 * scale[1], 8.0 * scale[0],
              63.0 * scale[1], 23.0 * scale[0], 63.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0],
              6.0 * scale[1], 8.0 * scale[0], 13.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 17.0 * scale[0],
              23.0 * scale[1], 36.0 * scale[0], 37.0 * scale[1])
    Curveto_r(20.0 * scale[0], 14.0 * scale[1], 44.0 * scale[0],
              33.0 * scale[1], 54.0 * scale[0], 42.0 * scale[1])
    Curveto_r(10.0 * scale[0], 9.0 * scale[1], 29.0 * scale[0],
              15.0 * scale[1], 42.0 * scale[0], 13.0 * scale[1])
    Curveto_r(13.0 * scale[0], -2.0 * scale[1], 41.0 *
              scale[0], -6.0 * scale[1], 63.0 * scale[0], -9.0 * scale[1])
    Curveto_r(22.0 * scale[0], -4.0 * scale[1], 56.0 * scale[0], -
              15.0 * scale[1], 76.0 * scale[0], -26.0 * scale[1])
    Curveto_r(21.0 * scale[0], -10.0 * scale[1], 40.0 * scale[0], -
              16.0 * scale[1], 43.0 * scale[0], -13.0 * scale[1])
    Curveto_r(8.0 * scale[0], 8.0 * scale[1], 36.0 * scale[0], -
              29.0 * scale[1], 30.0 * scale[0], -39.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], 2.0 * scale[0], -
              5.0 * scale[1], 10.0 * scale[0], -2.0 * scale[1])
    Curveto_r(10.0 * scale[0], 4.0 * scale[1], 21.0 * scale[0], -
              9.0 * scale[1], 36.0 * scale[0], -43.0 * scale[1])
    Curveto_r(20.0 * scale[0], -44.0 * scale[1], 21.0 * scale[0], -
              55.0 * scale[1], 11.0 * scale[0], -136.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -49.0 * scale[1], -6.0 * scale[0], -
              98.0 * scale[1], -2.0 * scale[0], -110.0 * scale[1])
    Curveto_r(9.0 * scale[0], -22.0 * scale[1], 11.0 * scale[0], -
              32.0 * scale[1], 11.0 * scale[0], -44.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 6.0 * scale[0],
              2.0 * scale[1], 14.0 * scale[0], 12.0 * scale[1])
    Curveto_r(8.0 * scale[0], 11.0 * scale[1], 12.0 * scale[0],
              24.0 * scale[1], 9.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 5.0 * scale[1], -1.0 * scale[0],
              6.0 * scale[1], 5.0 * scale[0], 2.0 * scale[1])
    Curveto_r(8.0 * scale[0], -5.0 * scale[1], 12.0 * scale[0],
              2.0 * scale[1], 12.0 * scale[0], 18.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -4.0 * scale[0],
              26.0 * scale[1], -9.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -1.0 * scale[0],
              74.0 * scale[1], 11.0 * scale[0], 78.0 * scale[1])
    Curveto_r(9.0 * scale[0], 4.0 * scale[1], 11.0 * scale[0],
              53.0 * scale[1], 2.0 * scale[0], 76.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -13.0 * scale[0],
              16.0 * scale[1], -21.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0],
              2.0 * scale[1], 1.0 * scale[0], 16.0 * scale[1])
    Curveto_r(9.0 * scale[0], 8.0 * scale[1], 16.0 * scale[0],
              25.0 * scale[1], 16.0 * scale[0], 37.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -3.0 * scale[0],
              18.0 * scale[1], -8.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -8.0 * scale[1], -11.0 *
              scale[0], -3.0 * scale[1], -20.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 15.0 * scale[1], -26.0 * scale[0],
              43.0 * scale[1], -43.0 * scale[0], 62.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 19.0 * scale[1], -26.0 * scale[0],
              27.0 * scale[1], -19.0 * scale[0], 18.0 * scale[1])
    Curveto_r(8.0 * scale[0], -12.0 * scale[1], 9.0 * scale[0], -
              18.0 * scale[1], 2.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0],
              9.0 * scale[1], -17.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 11.0 * scale[1], -14.0 * scale[0],
              21.0 * scale[1], -23.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 1.0 * scale[1], -28.0 * scale[0],
              3.0 * scale[1], -42.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-125.0 * scale[0], 14.0 * scale[1], -216.0 * scale[0],
              15.0 * scale[1], -225.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(1.0 * scale[0], 644.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(880.0 * scale[0], 600.0 * scale[1], x, y)
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
    Moveto(895.0 * scale[0], 570.0 * scale[1], x, y)
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
    Moveto(920.0 * scale[0], 535.0 * scale[1], x, y)
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
    Moveto(3.0 * scale[0], 475.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -22.0 * scale[1], 2.0 * scale[0], -
              30.0 * scale[1], 4.0 * scale[0], -17.0 * scale[1])
    Curveto_r(2.0 * scale[0], 12.0 * scale[1], 2.0 * scale[0],
              30.0 * scale[1], 0.0 * scale[0], 40.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -4.0 * scale[0], -23.0 * scale[1])
    te.end_fill()
    Moveto(950.0 * scale[0], 467.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 9.0 * scale[0], -
              24.0 * scale[1], 20.0 * scale[0], -44.0 * scale[1])
    Curveto_r(11.0 * scale[0], -21.0 * scale[1], 20.0 * scale[0], -
              32.0 * scale[1], 20.0 * scale[0], -26.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -9.0 * scale[0],
              27.0 * scale[1], -20.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 18.0 * scale[1], -20.0 * scale[0],
              30.0 * scale[1], -20.0 * scale[0], 25.0 * scale[1])
    te.end_fill()
    Moveto(4.0 * scale[0], 220.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -102.0 * scale[1], 2.0 * scale[0], -
              143.0 * scale[1], 3.0 * scale[0], -92.0 * scale[1])
    Curveto_r(2.0 * scale[0], 50.0 * scale[1], 2.0 * scale[0],
              134.0 * scale[1], 0.0 * scale[0], 185.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 50.0 * scale[1], -3.0 * scale[0],
              9.0 * scale[1], -3.0 * scale[0], -93.0 * scale[1])
    te.end_fill()
    Moveto(43.0 * scale[0], 115.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -22.0 * scale[1], 2.0 * scale[0], -
              30.0 * scale[1], 4.0 * scale[0], -17.0 * scale[1])
    Curveto_r(2.0 * scale[0], 12.0 * scale[1], 2.0 * scale[0],
              30.0 * scale[1], 0.0 * scale[0], 40.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -4.0 * scale[0], -23.0 * scale[1])
    te.end_fill()
    Moveto(966.0 * scale[0], 53.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -9.0 * scale[1], -3.0 * scale[0], -
              20.0 * scale[1], 1.0 * scale[0], -24.0 * scale[1])
    Curveto_r(4.0 * scale[0], -4.0 * scale[1], 9.0 * scale[0],
              3.0 * scale[1], 9.0 * scale[0], 17.0 * scale[1])
    Curveto_r(2.0 * scale[0], 28.0 * scale[1], -1.0 * scale[0],
              31.0 * scale[1], -10.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(60.0 * scale[0], 30.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(14.0 * scale[0], -26.0 * scale[1], 20.0 *
              scale[0], -26.0 * scale[1], 13.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 11.0 * scale[1], -9.0 * scale[0],
              20.0 * scale[1], -15.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              9.0 * scale[1], 2.0 * scale[0], -20.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#98651f')
    te.end_fill()
    Moveto(366.0 * scale[0], 1403.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -9.0 * scale[1], -2.0 *
              scale[0], -11.0 * scale[1], 7.0 * scale[0], -6.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 48.0 * scale[0],
              10.0 * scale[1], 92.0 * scale[0], 14.0 * scale[1])
    Lineto_r(80.0 * scale[0], 6.0 * scale[1])
    Lineto_r(-87.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-66.0 * scale[0], 0.0 * scale[1], -88.0 * scale[0], -
              3.0 * scale[1], -92.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(590.0 * scale[0], 1411.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 5.0 * scale[0], -
              13.0 * scale[1], 12.0 * scale[0], -17.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 8.0 *
              scale[0], -3.0 * scale[1], 4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], 5.0 * scale[0],
              12.0 * scale[1], 21.0 * scale[0], 15.0 * scale[1])
    Curveto_r(26.0 * scale[0], 4.0 * scale[1], 26.0 * scale[0],
              4.0 * scale[1], -4.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 0.0 * scale[1], -33.0 *
              scale[0], -3.0 * scale[1], -33.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(160.0 * scale[0], 1395.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], -12.0 * scale[0], -
              15.0 * scale[1], -47.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-55.0 * scale[0], 0.0 * scale[1], -48.0 * scale[0], -
              16.0 * scale[1], 12.0 * scale[0], -24.0 * scale[1])
    Curveto_r(31.0 * scale[0], -5.0 * scale[1], 35.0 *
              scale[0], -4.0 * scale[1], 20.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 9.0 * scale[1], -15.0 * scale[0],
              10.0 * scale[1], 12.0 * scale[0], 7.0 * scale[1])
    Curveto_r(18.0 * scale[0], -2.0 * scale[1], 30.0 * scale[0],
              0.0 * scale[1], 27.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], 16.0 * scale[0],
              9.0 * scale[1], 43.0 * scale[0], 9.0 * scale[1])
    Lineto_r(48.0 * scale[0], 2.0 * scale[1])
    Lineto_r(-40.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-39.0 * scale[0], 6.0 * scale[1], -39.0 * scale[0],
              6.0 * scale[1], -10.0 * scale[0], 12.0 * scale[1])
    Curveto_r(24.0 * scale[0], 4.0 * scale[1], 20.0 * scale[0],
              5.0 * scale[1], -17.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-37.0 * scale[0], 1.0 * scale[1], -48.0 * scale[0], -
              3.0 * scale[1], -48.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(283.0 * scale[0], 1403.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 17.0 * scale[0], -
              9.0 * scale[1], 17.0 * scale[0], -14.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 4.0 * scale[0], -
              9.0 * scale[1], 10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              7.0 * scale[1], 4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 8.0 * scale[1], -16.0 * scale[0],
              14.0 * scale[1], -28.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -1.0 * scale[1], -17.0 *
              scale[0], -2.0 * scale[1], -3.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(844.0 * scale[0], 1389.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -17.0 *
              scale[0], -7.0 * scale[1], -32.0 * scale[0], -4.0 * scale[1])
    Lineto_r(-27.0 * scale[0], 5.0 * scale[1])
    Lineto_r(25.0 * scale[0], -11.0 * scale[1])
    Curveto_r(34.0 * scale[0], -15.0 * scale[1], 124.0 * scale[0], -
              39.0 * scale[1], 115.0 * scale[0], -31.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -25.0 * scale[0],
              12.0 * scale[1], -48.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-37.0 * scale[0], 10.0 * scale[1], -39.0 * scale[0],
              11.0 * scale[1], -13.0 * scale[0], 12.0 * scale[1])
    Curveto_r(16.0 * scale[0], 1.0 * scale[1], 26.0 * scale[0],
              4.0 * scale[1], 22.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 11.0 * scale[1], -35.0 * scale[0],
              12.0 * scale[1], -42.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(615.0 * scale[0], 1380.0 * scale[1], x, y)
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
    Moveto(486.0 * scale[0], 1351.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -5.0 * scale[1], 3.0 * scale[0], -
              7.0 * scale[1], 14.0 * scale[0], -4.0 * scale[1])
    Curveto_r(23.0 * scale[0], 6.0 * scale[1], 26.0 * scale[0],
              13.0 * scale[1], 6.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0], -
              4.0 * scale[1], -20.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(750.0 * scale[0], 1351.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(21.0 * scale[0], -13.0 * scale[1], 80.0 *
              scale[0], -18.0 * scale[1], 77.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 5.0 * scale[1], -22.0 * scale[0],
              10.0 * scale[1], -47.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-29.0 * scale[0], 2.0 * scale[1], -40.0 * scale[0],
              0.0 * scale[1], -30.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(233.0 * scale[0], 1333.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(313.0 * scale[0], 1323.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(790.0 * scale[0], 1320.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -8.0 * scale[1], -10.0 *
              scale[0], -10.0 * scale[1], 8.0 * scale[0], -10.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0],
              4.0 * scale[1], 17.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 12.0 * scale[1], -6.0 * scale[0],
              12.0 * scale[1], -25.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(216.0 * scale[0], 1306.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -9.0 * scale[1], 28.0 * scale[0], -
              17.0 * scale[1], 67.0 * scale[0], -21.0 * scale[1])
    Curveto_r(34.0 * scale[0], -3.0 * scale[1], 71.0 * scale[0], -
              8.0 * scale[1], 82.0 * scale[0], -11.0 * scale[1])
    Curveto_r(11.0 * scale[0], -2.0 * scale[1], 14.0 *
              scale[0], -1.0 * scale[1], 7.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0],
              9.0 * scale[1], -8.0 * scale[0], 13.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], -12.0 * scale[0],
              5.0 * scale[1], -32.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-29.0 * scale[0], -3.0 * scale[1], -34.0 *
              scale[0], -1.0 * scale[1], -22.0 * scale[0], 8.0 * scale[1])
    Curveto_r(12.0 * scale[0], 8.0 * scale[1], 6.0 * scale[0],
              10.0 * scale[1], -27.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-23.0 * scale[0], -1.0 * scale[1], -45.0 * scale[0],
              1.0 * scale[1], -49.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 12.0 * scale[1], -24.0 * scale[0],
              8.0 * scale[1], -18.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(608.0 * scale[0], 1253.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(755.0 * scale[0], 1250.0 * scale[1], x, y)
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
    Moveto(245.0 * scale[0], 1245.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(24.0 * scale[0], -8.0 * scale[1], 116.0 * scale[0], -
              12.0 * scale[1], 103.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 5.0 * scale[1], -35.0 * scale[0],
              8.0 * scale[1], -63.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-27.0 * scale[0], 0.0 * scale[1], -45.0 *
              scale[0], -2.0 * scale[1], -40.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(756.0 * scale[0], 1193.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(30.0 * scale[0], -27.0 * scale[1], 44.0 *
              scale[0], -31.0 * scale[1], 21.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 10.0 * scale[1], -15.0 * scale[0],
              21.0 * scale[1], -12.0 * scale[0], 23.0 * scale[1])
    Curveto_r(2.0 * scale[0], 3.0 * scale[1], -4.0 * scale[0],
              5.0 * scale[1], -15.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -15.0 *
              scale[0], -3.0 * scale[1], 6.0 * scale[0], -23.0 * scale[1])
    te.end_fill()
    Moveto(360.0 * scale[0], 1199.0 * scale[1], x, y)
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
    Moveto(210.0 * scale[0], 1166.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 8.0 * scale[0], -
              16.0 * scale[1], 22.0 * scale[0], -16.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0],
              1.0 * scale[1], 17.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 1.0 * scale[1], -12.0 * scale[0],
              9.0 * scale[1], -21.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 12.0 * scale[1], -18.0 * scale[0],
              11.0 * scale[1], -18.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(285.0 * scale[0], 1170.0 * scale[1], x, y)
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
    Moveto(58.0 * scale[0], 1143.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(800.0 * scale[0], 1135.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-14.0 * scale[0], -16.0 * scale[1], -10.0 *
              scale[0], -18.0 * scale[1], 14.0 * scale[0], -9.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 16.0 * scale[0],
              10.0 * scale[1], 16.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -16.0 * scale[0],
              11.0 * scale[1], -30.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(210.0 * scale[0], 1130.0 * scale[1], x, y)
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
    Moveto(308.0 * scale[0], 1133.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(250.0 * scale[0], 1120.0 * scale[1], x, y)
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
    Moveto(680.0 * scale[0], 1123.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-41.0 * scale[0], -2.0 * scale[1], -78.0 *
              scale[0], -7.0 * scale[1], -82.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -4.0 * scale[1], 33.0 *
              scale[0], -5.0 * scale[1], 82.0 * scale[0], -2.0 * scale[1])
    Curveto_r(48.0 * scale[0], 3.0 * scale[1], 92.0 * scale[0],
              8.0 * scale[1], 96.0 * scale[0], 13.0 * scale[1])
    Curveto_r(4.0 * scale[0], 4.0 * scale[1], 1.0 * scale[0],
              6.0 * scale[1], -7.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -1.0 * scale[1], -48.0 *
              scale[0], -4.0 * scale[1], -89.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(286.0 * scale[0], 1111.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -12.0 * scale[1], 84.0 * scale[0], -
              34.0 * scale[1], 90.0 * scale[0], -28.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -16.0 * scale[0],
              12.0 * scale[1], -42.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-54.0 * scale[0], 18.0 * scale[1], -62.0 * scale[0],
              19.0 * scale[1], -48.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(825.0 * scale[0], 1110.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              10.0 * scale[1], 5.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0], -
              4.0 * scale[1], 5.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -12.0 * scale[1], 2.0 *
              scale[0], -12.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(11.0 * scale[0], 5.0 * scale[1], 14.0 * scale[0],
              9.0 * scale[1], 7.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 1.0 * scale[1], -10.0 * scale[0],
              6.0 * scale[1], -7.0 * scale[0], 11.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], -3.0 * scale[0],
              10.0 * scale[1], -14.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -23.0 * scale[0], -
              4.0 * scale[1], -26.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(180.0 * scale[0], 1106.0 * scale[1], x, y)
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
    Moveto(600.0 * scale[0], 1076.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 30.0 * scale[0], -
              14.0 * scale[1], 35.0 * scale[0], -6.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], -3.0 * scale[0],
              10.0 * scale[1], -14.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -21.0 *
              scale[0], -2.0 * scale[1], -21.0 * scale[0], -4.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#b5843d')
    te.end_fill()
    Moveto(448.0 * scale[0], 1423.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(17.0 * scale[0], -2.0 * scale[1], 47.0 *
              scale[0], -2.0 * scale[1], 65.0 * scale[0], 0.0 * scale[1])
    Curveto_r(17.0 * scale[0], 2.0 * scale[1], 3.0 * scale[0],
              4.0 * scale[1], -33.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-36.0 * scale[0], 0.0 * scale[1], -50.0 *
              scale[0], -2.0 * scale[1], -32.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(598.0 * scale[0], 1423.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(648.0 * scale[0], 1423.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(640.0 * scale[0], 1406.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 7.0 * scale[0], -
              7.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 12.0 *
              scale[0], -2.0 * scale[1], 9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], -25.0 * scale[0],
              14.0 * scale[1], -25.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(715.0 * scale[0], 1390.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -9.0 * scale[1], 1.0 * scale[0], -
              10.0 * scale[1], -13.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 4.0 * scale[1], -23.0 * scale[0],
              3.0 * scale[1], -26.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -10.0 * scale[1], 49.0 * scale[0], -
              22.0 * scale[1], 102.0 * scale[0], -22.0 * scale[1])
    Curveto_r(21.0 * scale[0], 0.0 * scale[1], 31.0 * scale[0],
              4.0 * scale[1], 26.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -17.0 * scale[0],
              8.0 * scale[1], -30.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -4.0 * scale[1], -23.0 *
              scale[0], -2.0 * scale[1], -22.0 * scale[0], 6.0 * scale[1])
    Curveto_r(2.0 * scale[0], 7.0 * scale[1], -8.0 * scale[0],
              14.0 * scale[1], -21.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 3.0 * scale[1], -21.0 * scale[0],
              0.0 * scale[1], -16.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(213.0 * scale[0], 1362.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 15.0 * scale[0], -
              7.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], 17.0 *
              scale[0], -7.0 * scale[1], 44.0 * scale[0], -7.0 * scale[1])
    Curveto_r(27.0 * scale[0], 1.0 * scale[1], 47.0 * scale[0], -
              1.0 * scale[1], 45.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], 5.0 * scale[0], -
              6.0 * scale[1], 17.0 * scale[0], -5.0 * scale[1])
    Lineto_r(21.0 * scale[0], 1.0 * scale[1])
    Lineto_r(-22.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 13.0 * scale[1], -37.0 * scale[0],
              17.0 * scale[1], -79.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-31.0 * scale[0], -1.0 * scale[1], -48.0 *
              scale[0], -3.0 * scale[1], -38.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(365.0 * scale[0], 1360.0 * scale[1], x, y)
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
    Moveto(710.0 * scale[0], 1339.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -15.0 * scale[1], 30.0 * scale[0], -
              23.0 * scale[1], 43.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 6.0 * scale[1], 7.0 * scale[0],
              11.0 * scale[1], 2.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -18.0 * scale[0],
              2.0 * scale[1], -27.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 2.0 * scale[1], -18.0 *
              scale[0], -1.0 * scale[1], -18.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(498.0 * scale[0], 1333.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(615.0 * scale[0], 1330.0 * scale[1], x, y)
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
    Moveto(776.0 * scale[0], 1331.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0], -
              8.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 22.0 * scale[0],
              4.0 * scale[1], 19.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], -31.0 * scale[0],
              9.0 * scale[1], -37.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(666.0 * scale[0], 1311.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              12.0 * scale[1], 10.0 * scale[0], -15.0 * scale[1])
    Curveto_r(20.0 * scale[0], -8.0 * scale[1], 29.0 *
              scale[0], -1.0 * scale[1], 19.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 13.0 * scale[1], -22.0 * scale[0],
              14.0 * scale[1], -29.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(710.0 * scale[0], 1306.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 40.0 * scale[0], -
              13.0 * scale[1], 46.0 * scale[0], -5.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], -6.0 * scale[0],
              9.0 * scale[1], -20.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -26.0 *
              scale[0], -2.0 * scale[1], -26.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(221.0 * scale[0], 1271.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -23.0 * scale[1], 1.0 * scale[0], -
              23.0 * scale[1], 64.0 * scale[0], -19.0 * scale[1])
    Curveto_r(39.0 * scale[0], 2.0 * scale[1], 67.0 * scale[0],
              0.0 * scale[1], 70.0 * scale[0], -7.0 * scale[1])
    Curveto_r(2.0 * scale[0], -5.0 * scale[1], 4.0 *
              scale[0], -1.0 * scale[1], 2.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 24.0 * scale[1], -54.0 * scale[0],
              33.0 * scale[1], -97.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-24.0 * scale[0], -8.0 * scale[1], -30.0 *
              scale[0], -7.0 * scale[1], -33.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 11.0 * scale[1], -5.0 * scale[0],
              9.0 * scale[1], -6.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(656.0 * scale[0], 1273.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -11.0 * scale[1], 19.0 * scale[0], -
              24.0 * scale[1], 36.0 * scale[0], -31.0 * scale[1])
    Curveto_r(27.0 * scale[0], -10.0 * scale[1], 33.0 *
              scale[0], -9.0 * scale[1], 44.0 * scale[0], 6.0 * scale[1])
    Curveto_r(20.0 * scale[0], 25.0 * scale[1], 17.0 * scale[0],
              32.0 * scale[1], -13.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -38.0 * scale[0],
              3.0 * scale[1], -50.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 5.0 * scale[1], -21.0 * scale[0],
              2.0 * scale[1], -17.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(370.0 * scale[0], 1254.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 5.0 * scale[0], -
              12.0 * scale[1], 10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 10.0 * scale[0],
              10.0 * scale[1], 10.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -4.0 * scale[0],
              9.0 * scale[1], -10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              7.0 * scale[1], -10.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(745.0 * scale[0], 1230.0 * scale[1], x, y)
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
    Moveto(253.0 * scale[0], 1223.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -2.0 * scale[1], -23.0 *
              scale[0], -9.0 * scale[1], -23.0 * scale[0], -14.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 41.0 * scale[0], -
              29.0 * scale[1], 53.0 * scale[0], -22.0 * scale[1])
    Curveto_r(4.0 * scale[0], 2.0 * scale[1], 23.0 * scale[0], -
              1.0 * scale[1], 42.0 * scale[0], -8.0 * scale[1])
    Curveto_r(29.0 * scale[0], -11.0 * scale[1], 37.0 *
              scale[0], -11.0 * scale[1], 47.0 * scale[0], 0.0 * scale[1])
    Curveto_r(8.0 * scale[0], 9.0 * scale[1], 8.0 * scale[0],
              11.0 * scale[1], 2.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -4.0 * scale[1], -15.0 * scale[0],
              0.0 * scale[1], -18.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 23.0 * scale[1], -8.0 * scale[0],
              27.0 * scale[1], 10.0 * scale[0], 20.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 12.0 *
              scale[0], -2.0 * scale[1], 9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], -78.0 * scale[0],
              11.0 * scale[1], -122.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto_r(91.0 * scale[0], -19.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -9.0 * scale[1], 4.0 * scale[0], -
              19.0 * scale[1], 1.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -5.0 * scale[0],
              0.0 * scale[1], -5.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -10.0 * scale[0],
              12.0 * scale[1], -22.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0],
              2.0 * scale[1], -8.0 * scale[0], 10.0 * scale[1])
    Curveto_r(21.0 * scale[0], 14.0 * scale[1], 27.0 * scale[0],
              12.0 * scale[1], 34.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto_r(-77.0 * scale[0], 0.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 17.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(704.0 * scale[0], 1204.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(19.0 * scale[0], -19.0 * scale[1], 21.0 *
              scale[0], -31.0 * scale[1], 3.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 6.0 * scale[1], -17.0 * scale[0],
              8.0 * scale[1], -20.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -3.0 * scale[1], -7.0 *
              scale[0], -1.0 * scale[1], -7.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -5.0 * scale[0],
              12.0 * scale[1], -11.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              4.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 3.0 * scale[0], -
              16.0 * scale[1], -2.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -23.0 * scale[1], -11.0 *
              scale[0], -58.0 * scale[1], 5.0 * scale[0], -58.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              3.0 * scale[1], 3.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 13.0 * scale[1], -7.0 * scale[0],
              13.0 * scale[1], 25.0 * scale[0], 5.0 * scale[1])
    Curveto_r(20.0 * scale[0], -6.0 * scale[1], 52.0 *
              scale[0], -8.0 * scale[1], 71.0 * scale[0], -4.0 * scale[1])
    Curveto_r(28.0 * scale[0], 5.0 * scale[1], 32.0 * scale[0],
              9.0 * scale[1], 23.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 12.0 * scale[1], -14.0 * scale[0],
              12.0 * scale[1], -27.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -19.0 * scale[1], -20.0 *
              scale[0], -19.0 * scale[1], -20.0 * scale[0], 0.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 4.0 * scale[0],
              15.0 * scale[1], 9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(19.0 * scale[0], 0.0 * scale[1], 6.0 * scale[0],
              21.0 * scale[1], -22.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-37.0 * scale[0], 19.0 * scale[1], -46.0 * scale[0],
              19.0 * scale[1], -26.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(630.0 * scale[0], 1190.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(241.0 * scale[0], 1166.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -8.0 * scale[1], 143.0 * scale[0], -
              36.0 * scale[1], 148.0 * scale[0], -30.0 * scale[1])
    Curveto_r(8.0 * scale[0], 8.0 * scale[1], -4.0 * scale[0],
              12.0 * scale[1], -49.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 4.0 * scale[1], -58.0 * scale[0],
              9.0 * scale[1], -75.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 4.0 * scale[1], -27.0 * scale[0],
              4.0 * scale[1], -24.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(605.0 * scale[0], 1139.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -14.0 * scale[1], 0.0 * scale[0], -
              22.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(13.0 * scale[0], 2.0 * scale[1], 13.0 * scale[0],
              5.0 * scale[1], 2.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -16.0 * scale[0],
              9.0 * scale[1], -20.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(301.0 * scale[0], 1126.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -2.0 * scale[1], 21.0 * scale[0], -
              11.0 * scale[1], 41.0 * scale[0], -19.0 * scale[1])
    Curveto_r(31.0 * scale[0], -13.0 * scale[1], 36.0 *
              scale[0], -13.0 * scale[1], 31.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], -9.0 * scale[0],
              12.0 * scale[1], -13.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -11.0 *
              scale[0], -1.0 * scale[1], -15.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], -16.0 * scale[0],
              10.0 * scale[1], -27.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(220.0 * scale[0], 1111.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(8.0 * scale[0], -6.0 * scale[1], 23.0 * scale[0], -
              11.0 * scale[1], 33.0 * scale[0], -11.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0], -
              5.0 * scale[1], 17.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0], -
              7.0 * scale[1], 10.0 * scale[0], -4.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 10.0 * scale[0],
              1.0 * scale[1], 10.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 12.0 * scale[0], -
              11.0 * scale[1], 28.0 * scale[0], -11.0 * scale[1])
    Curveto_r(20.0 * scale[0], 0.0 * scale[1], 23.0 * scale[0],
              3.0 * scale[1], 12.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 6.0 * scale[1], -18.0 * scale[0],
              7.0 * scale[1], -22.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -3.0 * scale[1], -8.0 *
              scale[0], -1.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -12.0 * scale[0],
              13.0 * scale[1], -27.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 4.0 * scale[1], -37.0 * scale[0],
              9.0 * scale[1], -48.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 4.0 * scale[1], -17.0 * scale[0],
              3.0 * scale[1], -5.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(397.0 * scale[0], 1099.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -25.0 * scale[1], 30.0 * scale[0], -
              36.0 * scale[1], 45.0 * scale[0], -21.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 1.0 * scale[0],
              15.0 * scale[1], -20.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-29.0 * scale[0], 15.0 * scale[1], -30.0 * scale[0],
              15.0 * scale[1], -25.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(38.0 * scale[0], -17.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -11.0 * scale[0],
              0.0 * scale[1], -18.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 10.0 * scale[1], -8.0 * scale[0],
              11.0 * scale[1], 6.0 * scale[0], 5.0 * scale[1])
    Curveto_r(10.0 * scale[0], -3.0 * scale[1], 15.0 * scale[0], -
              9.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(618.0 * scale[0], 1100.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-36.0 * scale[0], -3.0 * scale[1], -70.0 *
              scale[0], -8.0 * scale[1], -74.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -7.0 * scale[1], 18.0 * scale[0], -
              13.0 * scale[1], 39.0 * scale[0], -9.0 * scale[1])
    Curveto_r(4.0 * scale[0], 1.0 * scale[1], 34.0 * scale[0],
              3.0 * scale[1], 65.0 * scale[0], 6.0 * scale[1])
    Curveto_r(60.0 * scale[0], 4.0 * scale[1], 114.0 * scale[0],
              14.0 * scale[1], 121.0 * scale[0], 20.0 * scale[1])
    Curveto_r(4.0 * scale[0], 5.0 * scale[1], -54.0 * scale[0],
              3.0 * scale[1], -151.0 * scale[0], -5.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#aa772f')
    te.end_fill()
    Moveto(225.0 * scale[0], 1401.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-29.0 * scale[0], -5.0 * scale[1], -29.0 *
              scale[0], -5.0 * scale[1], 10.0 * scale[0], -11.0 * scale[1])
    Lineto_r(40.0 * scale[0], -7.0 * scale[1])
    Lineto_r(-48.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-27.0 * scale[0], 0.0 * scale[1], -46.0 *
              scale[0], -5.0 * scale[1], -43.0 * scale[0], -9.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], -9.0 * scale[0], -
              7.0 * scale[1], -27.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-31.0 * scale[0], 3.0 * scale[1], -31.0 * scale[0],
              3.0 * scale[1], -7.0 * scale[0], -8.0 * scale[1])
    Curveto_r(26.0 * scale[0], -11.0 * scale[1], 90.0 * scale[0], -
              21.0 * scale[1], 90.0 * scale[0], -13.0 * scale[1])
    Curveto_r(0.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0],
              8.0 * scale[1], -22.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 6.0 * scale[1], -7.0 * scale[0],
              9.0 * scale[1], 37.0 * scale[0], 10.0 * scale[1])
    Curveto_r(32.0 * scale[0], 0.0 * scale[1], 63.0 * scale[0],
              5.0 * scale[1], 69.0 * scale[0], 11.0 * scale[1])
    Curveto_r(6.0 * scale[0], 6.0 * scale[1], 6.0 * scale[0],
              10.0 * scale[1], 1.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -3.0 * scale[0],
              5.0 * scale[1], 5.0 * scale[0], 10.0 * scale[1])
    Curveto_r(13.0 * scale[0], 8.0 * scale[1], 12.0 * scale[0],
              10.0 * scale[1], -4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0], -
              5.0 * scale[1], -12.0 * scale[0], -15.0 * scale[1])
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], 1.0 * scale[0], -
              15.0 * scale[1], -3.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0],
              4.0 * scale[1], -13.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 12.0 * scale[1], -39.0 * scale[0],
              18.0 * scale[1], -73.0 * scale[0], 12.0 * scale[1])
    te.end_fill()
    Moveto(410.0 * scale[0], 1400.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(10.0 * scale[0], -6.0 * scale[1], 70.0 *
              scale[0], -1.0 * scale[1], 70.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 2.0 * scale[1], -18.0 * scale[0],
              3.0 * scale[1], -40.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-23.0 * scale[0], -1.0 * scale[1], -36.0 *
              scale[0], -4.0 * scale[1], -30.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(538.0 * scale[0], 1403.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(608.0 * scale[0], 1398.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -9.0 * scale[1], 15.0 *
              scale[0], -9.0 * scale[1], 24.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 9.0 * scale[1], 7.0 * scale[0],
              12.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -21.0 * scale[0], -
              3.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(666.0 * scale[0], 1401.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(14.0 * scale[0], -14.0 * scale[1], 58.0 * scale[0], -
              25.0 * scale[1], 50.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], 0.0 * scale[0],
              13.0 * scale[1], 6.0 * scale[0], 15.0 * scale[1])
    Curveto_r(7.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], -26.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 1.0 * scale[1], -36.0 *
              scale[0], -3.0 * scale[1], -30.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(350.0 * scale[0], 1396.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -3.0 * scale[1], 9.0 * scale[0], -
              10.0 * scale[1], 20.0 * scale[0], -16.0 * scale[1])
    Curveto_r(11.0 * scale[0], -6.0 * scale[1], 20.0 *
              scale[0], -8.0 * scale[1], 20.0 * scale[0], -6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0],
              10.0 * scale[1], -20.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 6.0 * scale[1], -20.0 * scale[0],
              8.0 * scale[1], -20.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(753.0 * scale[0], 1384.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 6.0 * scale[0], -
              17.0 * scale[1], 25.0 * scale[0], -5.0 * scale[1])
    Curveto_r(11.0 * scale[0], 6.0 * scale[1], 9.0 * scale[0],
              9.0 * scale[1], -5.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 3.0 * scale[1], -20.0 * scale[0],
              0.0 * scale[1], -20.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(805.0 * scale[0], 1371.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], -3.0 * scale[0], -
              12.0 * scale[1], -12.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -3.0 * scale[1], -3.0 *
              scale[0], -5.0 * scale[1], 15.0 * scale[0], -4.0 * scale[1])
    Curveto_r(34.0 * scale[0], 1.0 * scale[1], 42.0 * scale[0],
              11.0 * scale[1], 16.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 8.0 * scale[1], -26.0 * scale[0],
              8.0 * scale[1], -19.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(470.0 * scale[0], 1360.0 * scale[1], x, y)
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
    Moveto(698.0 * scale[0], 1363.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(745.0 * scale[0], 1342.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 10.0 * scale[0], -
              16.0 * scale[1], 10.0 * scale[0], -27.0 * scale[1])
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], -6.0 * scale[0], -
              19.0 * scale[1], -20.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-27.0 * scale[0], 5.0 * scale[1], -32.0 * scale[0],
              12.0 * scale[1], -9.0 * scale[0], 12.0 * scale[1])
    Curveto_r(16.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0],
              2.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -35.0 * scale[0],
              9.0 * scale[1], -60.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-43.0 * scale[0], -2.0 * scale[1], -43.0 *
              scale[0], -2.0 * scale[1], -11.0 * scale[0], -8.0 * scale[1])
    Curveto_r(19.0 * scale[0], -3.0 * scale[1], 36.0 * scale[0], -
              12.0 * scale[1], 39.0 * scale[0], -18.0 * scale[1])
    Curveto_r(3.0 * scale[0], -12.0 * scale[1], -32.0 *
              scale[0], -11.0 * scale[1], -75.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 2.0 * scale[1], -13.0 * scale[0], -
              2.0 * scale[1], -16.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], 17.0 * scale[0], -
              13.0 * scale[1], 66.0 * scale[0], -14.0 * scale[1])
    Curveto_r(38.0 * scale[0], -2.0 * scale[1], 72.0 *
              scale[0], -5.0 * scale[1], 75.0 * scale[0], -7.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], -6.0 * scale[0], -
              19.0 * scale[1], -18.0 * scale[0], -35.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -31.0 * scale[1], -18.0 *
              scale[0], -36.0 * scale[1], 19.0 * scale[0], -32.0 * scale[1])
    Curveto_r(7.0 * scale[0], 2.0 * scale[1], 10.0 * scale[0], -
              2.0 * scale[1], 7.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -5.0 * scale[1], -3.0 * scale[0], -
              12.0 * scale[1], 2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(4.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0],
              6.0 * scale[1], 8.0 * scale[0], 19.0 * scale[1])
    Curveto_r(0.0 * scale[0], 15.0 * scale[1], -5.0 * scale[0],
              21.0 * scale[1], -13.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -4.0 * scale[1], -11.0 *
              scale[0], -1.0 * scale[1], -2.0 * scale[0], 20.0 * scale[1])
    Curveto_r(7.0 * scale[0], 15.0 * scale[1], 16.0 * scale[0],
              24.0 * scale[1], 20.0 * scale[0], 21.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 9.0 *
              scale[0], -1.0 * scale[1], 9.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -6.0 * scale[0],
              12.0 * scale[1], -12.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 3.0 * scale[1], -3.0 * scale[0],
              6.0 * scale[1], 9.0 * scale[0], 6.0 * scale[1])
    Curveto_r(27.0 * scale[0], 1.0 * scale[1], 41.0 * scale[0],
              21.0 * scale[1], 16.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 1.0 * scale[1], -21.0 * scale[0],
              1.0 * scale[1], -25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0],
              4.0 * scale[1], -8.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 6.0 * scale[0],
              10.0 * scale[1], 13.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              4.0 * scale[1], -3.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 12.0 * scale[1], -40.0 * scale[0],
              14.0 * scale[1], -25.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(242.0 * scale[0], 1333.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-31.0 * scale[0], -4.0 * scale[1], -32.0 *
              scale[0], -6.0 * scale[1], -16.0 * scale[0], -18.0 * scale[1])
    Curveto_r(12.0 * scale[0], -9.0 * scale[1], 26.0 * scale[0], -
              10.0 * scale[1], 41.0 * scale[0], -4.0 * scale[1])
    Curveto_r(28.0 * scale[0], 11.0 * scale[1], 62.0 * scale[0],
              1.0 * scale[1], 41.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -8.0 *
              scale[0], -9.0 * scale[1], 7.0 * scale[0], -9.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 26.0 * scale[0],
              4.0 * scale[1], 33.0 * scale[0], 9.0 * scale[1])
    Curveto_r(10.0 * scale[0], 6.0 * scale[1], 4.0 * scale[0],
              10.0 * scale[1], -18.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 4.0 * scale[1], -29.0 * scale[0],
              11.0 * scale[1], -25.0 * scale[0], 17.0 * scale[1])
    Curveto_r(6.0 * scale[0], 10.0 * scale[1], -1.0 * scale[0],
              10.0 * scale[1], -63.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(204.0 * scale[0], 1282.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -10.0 * scale[1], -2.0 *
              scale[0], -37.0 * scale[1], 21.0 * scale[0], -40.0 * scale[1])
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 16.0 * scale[0],
              0.0 * scale[1], 9.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -13.0 * scale[0],
              16.0 * scale[1], -15.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 10.0 * scale[1], -9.0 * scale[0],
              14.0 * scale[1], -15.0 * scale[0], 10.0 * scale[1])
    te.end_fill()
    Moveto(230.0 * scale[0], 1276.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 7.0 * scale[0], -
              12.0 * scale[1], 20.0 * scale[0], -9.0 * scale[1])
    Curveto_r(31.0 * scale[0], 8.0 * scale[1], 34.0 * scale[0],
              23.0 * scale[1], 6.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -26.0 * scale[0], -
              6.0 * scale[1], -26.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(644.0 * scale[0], 1244.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(35.0 * scale[0], -18.0 * scale[1], 51.0 * scale[0], -
              23.0 * scale[1], 59.0 * scale[0], -15.0 * scale[1])
    Curveto_r(6.0 * scale[0], 6.0 * scale[1], 7.0 * scale[0],
              12.0 * scale[1], 1.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 1.0 * scale[1], -19.0 * scale[0],
              3.0 * scale[1], -32.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 1.0 * scale[1], -28.0 * scale[0],
              7.0 * scale[1], -35.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 6.0 * scale[1], -18.0 * scale[0],
              11.0 * scale[1], -26.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], 6.0 * scale[0], -
              12.0 * scale[1], 33.0 * scale[0], -26.0 * scale[1])
    te.end_fill()
    Moveto(611.0 * scale[0], 1234.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(238.0 * scale[0], 1223.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(312.0 * scale[0], 1211.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -6.0 * scale[1], -7.0 * scale[0], -
              10.0 * scale[1], 12.0 * scale[0], -13.0 * scale[1])
    Curveto_r(15.0 * scale[0], -3.0 * scale[1], 29.0 *
              scale[0], -1.0 * scale[1], 33.0 * scale[0], 5.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 1.0 * scale[0],
              7.0 * scale[1], -5.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -4.0 * scale[1], -12.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], -10.0 * scale[0],
              14.0 * scale[1], -28.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(226.0 * scale[0], 1199.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -7.0 * scale[1], 44.0 * scale[0],
              0.0 * scale[1], 44.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 2.0 * scale[1], -11.0 * scale[0],
              3.0 * scale[1], -24.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -1.0 * scale[1], -23.0 *
              scale[0], -5.0 * scale[1], -20.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(295.0 * scale[0], 1180.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(27.0 * scale[0], -12.0 * scale[1], 43.0 *
              scale[0], -12.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -22.0 * scale[0],
              9.0 * scale[1], -30.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 0.0 * scale[1], -8.0 *
              scale[0], -3.0 * scale[1], 5.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(225.0 * scale[0], 1170.0 * scale[1], x, y)
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
    Moveto(615.0 * scale[0], 1169.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -4.0 * scale[0], -
              13.0 * scale[1], -1.0 * scale[0], -16.0 * scale[1])
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], 6.0 *
              scale[0], -1.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 6.0 * scale[0],
              11.0 * scale[1], 16.0 * scale[0], 7.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 12.0 *
              scale[0], -2.0 * scale[1], 9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 13.0 * scale[1], -22.0 * scale[0],
              13.0 * scale[1], -30.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(240.0 * scale[0], 1154.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -7.0 * scale[1], -30.0 * scale[0], -
              13.0 * scale[1], -23.0 * scale[0], -13.0 * scale[1])
    Curveto_r(6.0 * scale[0], -1.0 * scale[1], 17.0 * scale[0], -
              3.0 * scale[1], 25.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 19.0 * scale[0],
              4.0 * scale[1], 26.0 * scale[0], 15.0 * scale[1])
    Curveto_r(7.0 * scale[0], 11.0 * scale[1], 11.0 * scale[0],
              19.0 * scale[1], 10.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -1.0 * scale[1], -19.0 * scale[0], -
              7.0 * scale[1], -38.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(743.0 * scale[0], 1156.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 6.0 * scale[0], -
              12.0 * scale[1], 14.0 * scale[0], -9.0 * scale[1])
    Curveto_r(7.0 * scale[0], 3.0 * scale[1], 10.0 * scale[0],
              9.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 14.0 * scale[1], -21.0 * scale[0],
              11.0 * scale[1], -21.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(789.0 * scale[0], 1158.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -16.0 * scale[1], 11.0 * scale[0], -
              18.0 * scale[1], -3.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0], -
              4.0 * scale[1], -11.0 * scale[0], -10.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              10.0 * scale[1], -5.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              4.0 * scale[1], -5.0 * scale[0], -9.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], -3.0 * scale[0], -
              12.0 * scale[1], -12.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -4.0 * scale[1], -15.0 *
              scale[0], -5.0 * scale[1], 3.0 * scale[0], -6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 26.0 * scale[0],
              5.0 * scale[1], 33.0 * scale[0], 12.0 * scale[1])
    Curveto_r(11.0 * scale[0], 10.0 * scale[1], 12.0 * scale[0],
              9.0 * scale[1], 6.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -11.0 * scale[1], -3.0 *
              scale[0], -12.0 * scale[1], 13.0 * scale[0], -3.0 * scale[1])
    Curveto_r(35.0 * scale[0], 19.0 * scale[1], 39.0 * scale[0],
              35.0 * scale[1], 7.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-24.0 * scale[0], -6.0 * scale[1], -27.0 *
              scale[0], -5.0 * scale[1], -17.0 * scale[0], 7.0 * scale[1])
    Curveto_r(10.0 * scale[0], 11.0 * scale[1], 9.0 * scale[0],
              17.0 * scale[1], -5.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 13.0 * scale[1], -17.0 * scale[0],
              12.0 * scale[1], -4.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(276.0 * scale[0], 1135.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -1.0 * scale[0], -
              15.0 * scale[1], 3.0 * scale[0], -15.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 18.0 * scale[0], -
              3.0 * scale[1], 28.0 * scale[0], -6.0 * scale[1])
    Curveto_r(15.0 * scale[0], -5.0 * scale[1], 16.0 *
              scale[0], -4.0 * scale[1], 3.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 10.0 * scale[1], -13.0 * scale[0],
              12.0 * scale[1], 0.0 * scale[0], 21.0 * scale[1])
    Curveto_r(12.0 * scale[0], 8.0 * scale[1], 11.0 * scale[0],
              10.0 * scale[1], -6.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -24.0 * scale[0], -
              7.0 * scale[1], -28.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(336.0 * scale[0], 1128.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -5.0 * scale[1], 9.0 * scale[0], -
              7.0 * scale[1], 12.0 * scale[0], -4.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 11.0 * scale[0],
              1.0 * scale[1], 18.0 * scale[0], -5.0 * scale[1])
    Curveto_r(15.0 * scale[0], -12.0 * scale[1], 34.0 *
              scale[0], -4.0 * scale[1], 34.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -4.0 * scale[0],
              6.0 * scale[1], -10.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -10.0 * scale[1], -12.0 *
              scale[0], -12.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 13.0 * scale[1], -45.0 * scale[0],
              15.0 * scale[1], -37.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(180.0 * scale[0], 1120.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -8.0 * scale[1], -10.0 *
              scale[0], -10.0 * scale[1], 8.0 * scale[0], -10.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 22.0 * scale[0], -
              4.0 * scale[1], 22.0 * scale[0], -9.0 * scale[1])
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 53.0 * scale[0], -
              20.0 * scale[1], 67.0 * scale[0], -5.0 * scale[1])
    Curveto_r(12.0 * scale[0], 12.0 * scale[1], 9.0 * scale[0],
              13.0 * scale[1], -19.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-27.0 * scale[0], -5.0 * scale[1], -30.0 *
              scale[0], -3.0 * scale[1], -18.0 * scale[0], 6.0 * scale[1])
    Curveto_r(13.0 * scale[0], 10.0 * scale[1], 12.0 * scale[0],
              11.0 * scale[1], -4.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -4.0 * scale[1], -24.0 *
              scale[0], -2.0 * scale[1], -30.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 6.0 * scale[1], -17.0 * scale[0],
              6.0 * scale[1], -26.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(698.0 * scale[0], 1123.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 30.0 *
              scale[0], -2.0 * scale[1], 40.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 0.0 * scale[1], -30.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(618.0 * scale[0], 1103.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 32.0 *
              scale[0], -2.0 * scale[1], 45.0 * scale[0], 0.0 * scale[1])
    Curveto_r(12.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              4.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 0.0 * scale[1], -35.0 *
              scale[0], -2.0 * scale[1], -22.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(714.0 * scale[0], 1102.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -6.0 * scale[1], -2.0 * scale[0], -
              13.0 * scale[1], -11.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -4.0 * scale[1], -16.0 *
              scale[0], -5.0 * scale[1], -1.0 * scale[0], -6.0 * scale[1])
    Curveto_r(21.0 * scale[0], -1.0 * scale[1], 32.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -9.0 * scale[0],
              3.0 * scale[1], -5.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(300.0 * scale[0], 1092.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 12.0 * scale[0], -
              8.0 * scale[1], 28.0 * scale[0], -9.0 * scale[1])
    Curveto_r(23.0 * scale[0], -1.0 * scale[1], 24.0 *
              scale[0], -1.0 * scale[1], 7.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-26.0 * scale[0], 11.0 * scale[1], -35.0 * scale[0],
              12.0 * scale[1], -35.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(380.0 * scale[0], 1091.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              11.0 * scale[1], 14.0 * scale[0], -14.0 * scale[1])
    Curveto_r(10.0 * scale[0], -4.0 * scale[1], 13.0 *
              scale[0], -1.0 * scale[1], 9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 15.0 * scale[1], -23.0 * scale[0],
              19.0 * scale[1], -23.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(424.0 * scale[0], 1086.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(22.0 * scale[0], -18.0 * scale[1], 61.0 *
              scale[0], -22.0 * scale[1], 51.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 5.0 * scale[1], -12.0 * scale[0],
              8.0 * scale[1], -18.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -21.0 * scale[0],
              0.0 * scale[1], -32.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 9.0 * scale[1], -20.0 * scale[0],
              9.0 * scale[1], -1.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(533.0 * scale[0], 1073.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#9ea141')
    te.end_fill()
    Moveto(430.0 * scale[0], 1027.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 5.0 * scale[0], -
              27.0 * scale[1], 11.0 * scale[0], -29.0 * scale[1])
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 11.0 * scale[0], -
              26.0 * scale[1], 12.0 * scale[0], -53.0 * scale[1])
    Lineto_r(2.0 * scale[0], -50.0 * scale[1])
    Lineto_r(68.0 * scale[0], -3.0 * scale[1])
    Curveto_r(39.0 * scale[0], -1.0 * scale[1], 67.0 * scale[0],
              1.0 * scale[1], 67.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 16.0 * scale[0],
              13.0 * scale[1], 35.0 * scale[0], 17.0 * scale[1])
    Curveto_r(20.0 * scale[0], 3.0 * scale[1], 42.0 * scale[0],
              12.0 * scale[1], 48.0 * scale[0], 19.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 26.0 * scale[0],
              20.0 * scale[1], 42.0 * scale[0], 29.0 * scale[1])
    Lineto_r(30.0 * scale[0], 17.0 * scale[1])
    Lineto_r(-28.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -4.0 * scale[1], -33.0 * scale[0],
              0.0 * scale[1], -43.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 10.0 * scale[1], -11.0 * scale[0],
              15.0 * scale[1], -3.0 * scale[0], 15.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0],
              4.0 * scale[1], -1.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 13.0 * scale[1], -10.0 *
              scale[0], 14.0 * scale[1], 6.0 * scale[0], 9.0 * scale[1])
    Curveto_r(10.0 * scale[0], -4.0 * scale[1], 24.0 * scale[0], -
              10.0 * scale[1], 29.0 * scale[0], -14.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 24.0 *
              scale[0], -3.0 * scale[1], 40.0 * scale[0], 1.0 * scale[1])
    Curveto_r(17.0 * scale[0], 3.0 * scale[1], 23.0 * scale[0],
              7.0 * scale[1], 13.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -18.0 * scale[0],
              5.0 * scale[1], -20.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 6.0 * scale[1], -69.0 * scale[0],
              13.0 * scale[1], -155.0 * scale[0], 17.0 * scale[1])
    Lineto_r(-153.0 * scale[0], 6.0 * scale[1])
    Lineto_r(0.0 * scale[0], -26.0 * scale[1])
    te.end_fill()
    Moveto_r(220.0 * scale[0], -21.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], -19.0 * scale[0], -
              15.0 * scale[1], -25.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], 1.0 * scale[0],
              10.0 * scale[1], 9.0 * scale[0], 10.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0], -
              2.0 * scale[1], 16.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(758.0 * scale[0], 1033.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(690.0 * scale[0], 929.0 * scale[1], x, y)
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
    Moveto(401.0 * scale[0], 918.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -10.0 * scale[1], 1.0 * scale[0], -
              18.0 * scale[1], 3.0 * scale[0], -18.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0], -
              3.0 * scale[1], 20.0 * scale[0], -6.0 * scale[1])
    Curveto_r(9.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -1.0 * scale[1], 16.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -6.0 * scale[0],
              11.0 * scale[1], -14.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0],
              6.0 * scale[1], -19.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 7.0 * scale[1], -6.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(384.0 * scale[0], 882.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -22.0 * scale[1], 5.0 * scale[0], -
              23.0 * scale[1], 83.0 * scale[0], -25.0 * scale[1])
    Curveto_r(53.0 * scale[0], -1.0 * scale[1], 74.0 * scale[0],
              1.0 * scale[1], 60.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 5.0 * scale[1], -48.0 * scale[0],
              7.0 * scale[1], -79.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-51.0 * scale[0], -3.0 * scale[1], -58.0 *
              scale[0], -1.0 * scale[1], -61.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 15.0 * scale[1], -4.0 * scale[0],
              15.0 * scale[1], -3.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(603.0 * scale[0], 843.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(240.0 * scale[0], 726.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -10.0 * scale[1], -8.0 * scale[0], -
              21.0 * scale[1], -2.0 * scale[0], -32.0 * scale[1])
    Curveto_r(8.0 * scale[0], -14.0 * scale[1], 10.0 * scale[0], -
              11.0 * scale[1], 14.0 * scale[0], 15.0 * scale[1])
    Curveto_r(5.0 * scale[0], 36.0 * scale[1], 5.0 * scale[0],
              36.0 * scale[1], -12.0 * scale[0], 17.0 * scale[1])
    te.end_fill()
    Moveto(924.0 * scale[0], 698.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-29.0 * scale[0], -33.0 * scale[1])
    Lineto_r(33.0 * scale[0], 29.0 * scale[1])
    Curveto_r(17.0 * scale[0], 17.0 * scale[1], 32.0 * scale[0],
              31.0 * scale[1], 32.0 * scale[0], 33.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              1.0 * scale[1], -36.0 * scale[0], -29.0 * scale[1])
    te.end_fill()
    Moveto(982.0 * scale[0], 705.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(22.0 * scale[0], 594.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -36.0 * scale[1], 10.0 *
              scale[0], -38.0 * scale[1], 28.0 * scale[0], -4.0 * scale[1])
    Curveto_r(8.0 * scale[0], 15.0 * scale[1], 6.0 * scale[0],
              21.0 * scale[1], -8.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 9.0 * scale[1], -19.0 * scale[0],
              6.0 * scale[1], -20.0 * scale[0], -25.0 * scale[1])
    te.end_fill()
    Moveto(96.0 * scale[0], 602.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              15.0 * scale[1], 9.0 * scale[0], -22.0 * scale[1])
    Curveto_r(16.0 * scale[0], -14.0 * scale[1], 20.0 *
              scale[0], -3.0 * scale[1], 6.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 8.0 * scale[1], -11.0 * scale[0],
              9.0 * scale[1], -15.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(981.0 * scale[0], 514.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(24.0 * scale[0], 466.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -13.0 * scale[1], 1.0 * scale[0], -
              72.0 * scale[1], -4.0 * scale[0], -131.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -59.0 * scale[1], -8.0 * scale[0], -
              110.0 * scale[1], -5.0 * scale[0], -113.0 * scale[1])
    Curveto_r(14.0 * scale[0], -14.0 * scale[1], 25.0 * scale[0],
              20.0 * scale[1], 26.0 * scale[0], 86.0 * scale[1])
    Curveto_r(1.0 * scale[0], 40.0 * scale[1], 5.0 * scale[0],
              75.0 * scale[1], 10.0 * scale[0], 78.0 * scale[1])
    Curveto_r(12.0 * scale[0], 7.0 * scale[1], 11.0 * scale[0],
              44.0 * scale[1], -1.0 * scale[0], 44.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0],
              4.0 * scale[1], -10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 7.0 * scale[0],
              7.0 * scale[1], 15.0 * scale[0], 4.0 * scale[1])
    Curveto_r(20.0 * scale[0], -8.0 * scale[1], 19.0 *
              scale[0], -2.0 * scale[1], -4.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 29.0 * scale[1], -35.0 * scale[0],
              28.0 * scale[1], -27.0 * scale[0], -2.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#b2cc4b')
    te.end_fill()
    Moveto(500.0 * scale[0], 850.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(34.0 * scale[0], -11.0 * scale[1], 60.0 *
              scale[0], -11.0 * scale[1], 35.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 5.0 * scale[1], -29.0 * scale[0],
              8.0 * scale[1], -40.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -15.0 *
              scale[0], -2.0 * scale[1], 5.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(933.0 * scale[0], 698.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-55.0 * scale[0], -58.0 * scale[1], -56.0 * scale[0], -
              68.0 * scale[1], -21.0 * scale[0], -139.0 * scale[1])
    Curveto_r(17.0 * scale[0], -35.0 * scale[1], 38.0 * scale[0], -
              79.0 * scale[1], 47.0 * scale[0], -97.0 * scale[1])
    Curveto_r(9.0 * scale[0], -19.0 * scale[1], 19.0 * scale[0], -
              35.0 * scale[1], 22.0 * scale[0], -38.0 * scale[1])
    Curveto_r(8.0 * scale[0], -4.0 * scale[1], 10.0 * scale[0],
              208.0 * scale[1], 2.0 * scale[0], 264.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 23.0 * scale[1], -8.0 * scale[0],
              42.0 * scale[1], -12.0 * scale[0], 42.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -21.0 * scale[0], -
              15.0 * scale[1], -38.0 * scale[0], -32.0 * scale[1])
    te.end_fill()
    Moveto(3.0 * scale[0], 580.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -30.0 * scale[1], 2.0 * scale[0], -
              43.0 * scale[1], 4.0 * scale[0], -27.0 * scale[1])
    Curveto_r(2.0 * scale[0], 15.0 * scale[1], 2.0 * scale[0],
              39.0 * scale[1], 0.0 * scale[0], 55.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 15.0 * scale[1], -4.0 * scale[0],
              2.0 * scale[1], -4.0 * scale[0], -28.0 * scale[1])
    te.end_fill()
    Moveto(40.0 * scale[0], 440.0 * scale[1], x, y)
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
    Moveto(22.0 * scale[0], 222.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -12.0 * scale[0], -
              36.0 * scale[1], -11.0 * scale[0], -100.0 * scale[1])
    Curveto_r(1.0 * scale[0], -92.0 * scale[1], 8.0 * scale[0], -
              110.0 * scale[1], 41.0 * scale[0], -109.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              4.0 * scale[1], 7.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 10.0 * scale[1], -7.0 * scale[0],
              18.0 * scale[1], -4.0 * scale[0], 18.0 * scale[1])
    Curveto_r(3.0 * scale[0], 0.0 * scale[1], 1.0 * scale[0],
              8.0 * scale[1], -4.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], -11.0 * scale[0],
              50.0 * scale[1], -12.0 * scale[0], 90.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 39.0 * scale[1], -2.0 * scale[0],
              71.0 * scale[1], -3.0 * scale[0], 71.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              4.0 * scale[1], -14.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(974.0 * scale[0], 55.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              25.0 * scale[1], 7.0 * scale[0], -25.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              11.0 * scale[1], 9.0 * scale[0], 25.0 * scale[1])
    Curveto_r(0.0 * scale[0], 33.0 * scale[1], -15.0 * scale[0],
              33.0 * scale[1], -16.0 * scale[0], 0.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#938e37')
    te.end_fill()
    Moveto(409.0 * scale[0], 1034.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -11.0 * scale[1], -14.0 * scale[0], -
              25.0 * scale[1], -12.0 * scale[0], -31.0 * scale[1])
    Curveto_r(3.0 * scale[0], -7.0 * scale[1], -1.0 * scale[0], -
              13.0 * scale[1], -9.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 0.0 * scale[1], -9.0 *
              scale[0], -3.0 * scale[1], 2.0 * scale[0], -11.0 * scale[1])
    Curveto_r(11.0 * scale[0], -8.0 * scale[1], 8.0 * scale[0], -
              9.0 * scale[1], -15.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 4.0 * scale[1], -25.0 * scale[0],
              3.0 * scale[1], -19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(19.0 * scale[0], -13.0 * scale[1], 34.0 * scale[0], -
              50.0 * scale[1], 34.0 * scale[0], -81.0 * scale[1])
    Curveto_r(0.0 * scale[0], -28.0 * scale[1], 2.0 * scale[0], -
              30.0 * scale[1], 27.0 * scale[0], -23.0 * scale[1])
    Curveto_r(15.0 * scale[0], 4.0 * scale[1], 46.0 * scale[0],
              4.0 * scale[1], 70.0 * scale[0], 1.0 * scale[1])
    Curveto_r(24.0 * scale[0], -4.0 * scale[1], 43.0 *
              scale[0], -3.0 * scale[1], 43.0 * scale[0], 2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 19.0 * scale[0],
              7.0 * scale[1], 43.0 * scale[0], 4.0 * scale[1])
    Curveto_r(23.0 * scale[0], -2.0 * scale[1], 50.0 *
              scale[0], -5.0 * scale[1], 61.0 * scale[0], -5.0 * scale[1])
    Curveto_r(13.0 * scale[0], -1.0 * scale[1], 16.0 * scale[0], -
              6.0 * scale[1], 12.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -14.0 * scale[1], -4.0 *
              scale[0], -15.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(8.0 * scale[0], 6.0 * scale[1], 17.0 * scale[0],
              28.0 * scale[1], 21.0 * scale[0], 47.0 * scale[1])
    Curveto_r(7.0 * scale[0], 36.0 * scale[1], 30.0 * scale[0],
              52.0 * scale[1], 89.0 * scale[0], 60.0 * scale[1])
    Curveto_r(38.0 * scale[0], 6.0 * scale[1], 48.0 * scale[0],
              16.0 * scale[1], 51.0 * scale[0], 52.0 * scale[1])
    Curveto_r(2.0 * scale[0], 28.0 * scale[1], 0.0 * scale[0],
              29.0 * scale[1], -37.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-38.0 * scale[0], -1.0 * scale[1], -55.0 * scale[0], -
              15.0 * scale[1], -21.0 * scale[0], -17.0 * scale[1])
    Curveto_r(9.0 * scale[0], -1.0 * scale[1], 4.0 * scale[0], -
              5.0 * scale[1], -13.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -4.0 * scale[1], -34.0 *
              scale[0], -4.0 * scale[1], -40.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 4.0 * scale[1], -19.0 * scale[0],
              10.0 * scale[1], -29.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 5.0 * scale[1], -17.0 * scale[0],
              4.0 * scale[1], -6.0 * scale[0], -9.0 * scale[1])
    Curveto_r(9.0 * scale[0], -11.0 * scale[1], 9.0 * scale[0], -
              15.0 * scale[1], 1.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              5.0 * scale[1], 3.0 * scale[0], -15.0 * scale[1])
    Curveto_r(10.0 * scale[0], -10.0 * scale[1], 25.0 * scale[0], -
              14.0 * scale[1], 43.0 * scale[0], -10.0 * scale[1])
    Lineto_r(28.0 * scale[0], 6.0 * scale[1])
    Lineto_r(-30.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -9.0 * scale[1], -35.0 * scale[0], -
              22.0 * scale[1], -42.0 * scale[0], -29.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -7.0 * scale[1], -28.0 * scale[0], -
              16.0 * scale[1], -48.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -4.0 * scale[1], -35.0 * scale[0], -
              11.0 * scale[1], -35.0 * scale[0], -17.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -28.0 * scale[0], -
              8.0 * scale[1], -67.0 * scale[0], -7.0 * scale[1])
    Lineto_r(-68.0 * scale[0], 3.0 * scale[1])
    Lineto_r(-2.0 * scale[0], 49.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 27.0 * scale[1], -6.0 * scale[0],
              52.0 * scale[1], -11.0 * scale[0], 55.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -12.0 * scale[0],
              17.0 * scale[1], -13.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 23.0 * scale[1], -5.0 * scale[0],
              23.0 * scale[1], -20.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto_r(17.0 * scale[0], -124.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0], -
              5.0 * scale[1], 14.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -7.0 * scale[0], -
              8.0 * scale[1], -16.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 3.0 * scale[1], -18.0 * scale[0],
              6.0 * scale[1], -20.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0],
              8.0 * scale[1], -3.0 * scale[0], 18.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], 3.0 * scale[0],
              12.0 * scale[1], 6.0 * scale[0], 5.0 * scale[1])
    Curveto_r(2.0 * scale[0], -7.0 * scale[1], 11.0 * scale[0], -
              13.0 * scale[1], 19.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(638.0 * scale[0], 1043.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(277.0 * scale[0], 1023.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -10.0 * scale[1], -8.0 *
              scale[0], -23.0 * scale[1], 4.0 * scale[0], -23.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0],
              4.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], 3.0 * scale[0],
              12.0 * scale[1], 12.0 * scale[0], 14.0 * scale[1])
    Curveto_r(14.0 * scale[0], 4.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 2.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -19.0 * scale[0], -
              2.0 * scale[1], -22.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(625.0 * scale[0], 1000.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 11.0 * scale[0], -
              8.0 * scale[1], 16.0 * scale[0], -5.0 * scale[1])
    Curveto_r(14.0 * scale[0], 9.0 * scale[1], 11.0 * scale[0],
              15.0 * scale[1], -7.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              5.0 * scale[1], -9.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(900.0 * scale[0], 902.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -3.0 * scale[1], 8.0 * scale[0], -
              11.0 * scale[1], 18.0 * scale[0], -19.0 * scale[1])
    Curveto_r(9.0 * scale[0], -8.0 * scale[1], 11.0 * scale[0], -
              12.0 * scale[1], 5.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 4.0 * scale[1], -13.0 * scale[0], -
              3.0 * scale[1], -13.0 * scale[0], -23.0 * scale[1])
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], -3.0 * scale[0], -
              44.0 * scale[1], -6.0 * scale[0], -61.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -26.0 * scale[1], -4.0 * scale[0], -
              31.0 * scale[1], 12.0 * scale[0], -30.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0],
              3.0 * scale[1], 7.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 9.0 * scale[1], -13.0 * scale[0],
              21.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(29.0 * scale[0], -5.0 * scale[1], 30.0 *
              scale[0], -4.0 * scale[1], 30.0 * scale[0], 35.0 * scale[1])
    Curveto_r(0.0 * scale[0], 23.0 * scale[1], -4.0 * scale[0],
              41.0 * scale[1], -10.0 * scale[0], 41.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0],
              7.0 * scale[1], -4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(4.0 * scale[0], 9.0 * scale[1], 0.0 * scale[0],
              15.0 * scale[1], -10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0],
              4.0 * scale[1], -16.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -7.0 * scale[0],
              9.0 * scale[1], -15.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              2.0 * scale[1], -15.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(563.0 * scale[0], 853.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(950.0 * scale[0], 759.0 * scale[1], x, y)
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
    Moveto(895.0 * scale[0], 740.0 * scale[1], x, y)
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
    Moveto(861.0 * scale[0], 655.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 3.0 * scale[0], -
              16.0 * scale[1], 8.0 * scale[0], -23.0 * scale[1])
    Curveto_r(7.0 * scale[0], -11.0 * scale[1], 9.0 * scale[0], -
              10.0 * scale[1], 14.0 * scale[0], 3.0 * scale[1])
    Curveto_r(4.0 * scale[0], 9.0 * scale[1], 3.0 * scale[0],
              14.0 * scale[1], -2.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -12.0 * scale[0],
              1.0 * scale[1], -14.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 7.0 * scale[1], -6.0 * scale[0],
              9.0 * scale[1], -6.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(110.0 * scale[0], 600.0 * scale[1], x, y)
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
    Moveto(22.0 * scale[0], 430.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 2.0 * scale[0], -
              27.0 * scale[1], 5.0 * scale[0], -17.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              25.0 * scale[1], 0.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#8d6b35')
    te.end_fill()
    Moveto(738.0 * scale[0], 1423.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(788.0 * scale[0], 1423.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(70.0 * scale[0], 1354.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 8.0 * scale[0], -
              13.0 * scale[1], 20.0 * scale[0], -11.0 * scale[1])
    Curveto_r(31.0 * scale[0], 5.0 * scale[1], 33.0 * scale[0],
              14.0 * scale[1], 5.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 4.0 * scale[1], -25.0 * scale[0],
              1.0 * scale[1], -25.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(130.0 * scale[0], 1340.0 * scale[1], x, y)
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
    Moveto(770.0 * scale[0], 1234.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 5.0 * scale[0], -
              12.0 * scale[1], 10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 10.0 * scale[0],
              10.0 * scale[1], 10.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -4.0 * scale[0],
              9.0 * scale[1], -10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              7.0 * scale[1], -10.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(210.0 * scale[0], 1209.0 * scale[1], x, y)
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
    Moveto(797.0 * scale[0], 1159.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(195.0 * scale[0], 1150.0 * scale[1], x, y)
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
    Moveto(165.0 * scale[0], 1130.0 * scale[1], x, y)
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
    Moveto(420.0 * scale[0], 1110.0 * scale[1], x, y)
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
    Moveto(570.0 * scale[0], 1110.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -8.0 * scale[1], -13.0 *
              scale[0], -10.0 * scale[1], 2.0 * scale[0], -10.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0],
              5.0 * scale[1], 23.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 13.0 * scale[1], -5.0 * scale[0],
              13.0 * scale[1], -25.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(100.0 * scale[0], 1100.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 7.0 * scale[0], -
              10.0 * scale[1], 15.0 * scale[0], -10.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 26.0 * scale[0], -
              6.0 * scale[1], 38.0 * scale[0], -14.0 * scale[1])
    Curveto_r(23.0 * scale[0], -14.0 * scale[1], 184.0 *
              scale[0], -20.0 * scale[1], 205.0 * scale[0], -7.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -8.0 * scale[0],
              7.0 * scale[1], -31.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-73.0 * scale[0], 1.0 * scale[1], -172.0 * scale[0],
              12.0 * scale[1], -200.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 7.0 * scale[1], -27.0 * scale[0],
              7.0 * scale[1], -27.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(713.0 * scale[0], 1087.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-40.0 * scale[0], -6.0 * scale[1], -73.0 * scale[0], -
              14.0 * scale[1], -73.0 * scale[0], -18.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 137.0 *
              scale[0], -10.0 * scale[1], 164.0 * scale[0], 1.0 * scale[1])
    Curveto_r(20.0 * scale[0], 8.0 * scale[1], 20.0 * scale[0],
              9.0 * scale[1], -2.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 1.0 * scale[1], -20.0 * scale[0],
              5.0 * scale[1], -17.0 * scale[0], 11.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 5.0 * scale[0],
              9.0 * scale[1], 3.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -1.0 * scale[1], -36.0 * scale[0], -
              6.0 * scale[1], -75.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(808.0 * scale[0], 1093.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(875.0 * scale[0], 1090.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], 3.0 * scale[0], -
              10.0 * scale[1], 14.0 * scale[0], -10.0 * scale[1])
    Curveto_r(25.0 * scale[0], 0.0 * scale[1], 27.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 4.0 * scale[1], -17.0 * scale[0],
              2.0 * scale[1], -20.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(474.0 * scale[0], 1081.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -8.0 * scale[1], 56.0 *
              scale[0], -3.0 * scale[1], 56.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 2.0 * scale[1], -14.0 * scale[0],
              4.0 * scale[1], -31.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -28.0 *
              scale[0], -4.0 * scale[1], -25.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(298.0 * scale[0], 1043.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 32.0 *
              scale[0], -2.0 * scale[1], 45.0 * scale[0], 0.0 * scale[1])
    Curveto_r(12.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              4.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 0.0 * scale[1], -35.0 *
              scale[0], -2.0 * scale[1], -22.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(866.0 * scale[0], 1029.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 12.0 * scale[0], -
              9.0 * scale[1], 21.0 * scale[0], -9.0 * scale[1])
    Curveto_r(19.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              13.0 * scale[1], -12.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 1.0 * scale[1], -13.0 *
              scale[0], -2.0 * scale[1], -9.0 * scale[0], -7.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#837f2a')
    te.end_fill()
    Moveto(673.0 * scale[0], 1043.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(316.0 * scale[0], 1032.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], -39.0 *
              scale[0], -9.0 * scale[1], -81.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-68.0 * scale[0], 3.0 * scale[1], -76.0 * scale[0],
              1.0 * scale[1], -90.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -28.0 * scale[1], -19.0 *
              scale[0], -38.0 * scale[1], -4.0 * scale[0], -28.0 * scale[1])
    Curveto_r(8.0 * scale[0], 4.0 * scale[1], 9.0 * scale[0], -
              1.0 * scale[1], 4.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -21.0 * scale[1], -6.0 *
              scale[0], -22.0 * scale[1], 9.0 * scale[0], -7.0 * scale[1])
    Curveto_r(9.0 * scale[0], 9.0 * scale[1], 16.0 * scale[0],
              21.0 * scale[1], 16.0 * scale[0], 27.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 40.0 * scale[0],
              21.0 * scale[1], 80.0 * scale[0], 26.0 * scale[1])
    Curveto_r(3.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              4.0 * scale[1], 18.0 * scale[0], 8.0 * scale[1])
    Curveto_r(11.0 * scale[0], 7.0 * scale[1], 16.0 * scale[0],
              2.0 * scale[1], 14.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -4.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 36.0 * scale[0], -14.0 * scale[1])
    Curveto_r(20.0 * scale[0], -3.0 * scale[1], 48.0 * scale[0], -
              9.0 * scale[1], 62.0 * scale[0], -11.0 * scale[1])
    Curveto_r(20.0 * scale[0], -5.0 * scale[1], 22.0 *
              scale[0], -3.0 * scale[1], 10.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 7.0 * scale[1], -10.0 * scale[0],
              11.0 * scale[1], -3.0 * scale[0], 11.0 * scale[1])
    Curveto_r(18.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              40.0 * scale[1], -7.0 * scale[0], 40.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -25.0 * scale[0],
              3.0 * scale[1], -36.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 3.0 * scale[1], -25.0 * scale[0],
              1.0 * scale[1], -28.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(819.0 * scale[0], 1033.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -50.0 * scale[1], -4.0 *
              scale[0], -63.0 * scale[1], 8.0 * scale[0], -63.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              7.0 * scale[1], 13.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], 7.0 * scale[0],
              15.0 * scale[1], 30.0 * scale[0], 10.0 * scale[1])
    Curveto_r(29.0 * scale[0], -5.0 * scale[1], 30.0 *
              scale[0], -5.0 * scale[1], 13.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 21.0 * scale[1], -62.0 * scale[0],
              37.0 * scale[1], -64.0 * scale[0], 24.0 * scale[1])
    te.end_fill()
    Moveto(904.0 * scale[0], 1025.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -14.0 * scale[1], -18.0 *
              scale[0], -14.0 * scale[1], 4.0 * scale[0], -15.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 22.0 * scale[0], -
              6.0 * scale[1], 22.0 * scale[0], -12.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 7.0 * scale[0], -
              5.0 * scale[1], 15.0 * scale[0], 6.0 * scale[1])
    Curveto_r(12.0 * scale[0], 16.0 * scale[1], 12.0 * scale[0],
              22.0 * scale[1], 2.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 11.0 * scale[1], -20.0 * scale[0],
              10.0 * scale[1], -43.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(930.0 * scale[0], 900.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              10.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0], -
              6.0 * scale[1], 10.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -1.0 * scale[0], -
              15.0 * scale[1], 4.0 * scale[0], -15.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              18.0 * scale[1], 10.0 * scale[0], -41.0 * scale[1])
    Curveto_r(0.0 * scale[0], -39.0 * scale[1], -1.0 * scale[0], -
              40.0 * scale[1], -30.0 * scale[0], -35.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 4.0 * scale[1], -42.0 * scale[0], -
              8.0 * scale[1], -17.0 * scale[0], -17.0 * scale[1])
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 5.0 * scale[0], -
              6.0 * scale[1], -5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -1.0 * scale[1], -15.0 *
              scale[0], -6.0 * scale[1], -12.0 * scale[0], -16.0 * scale[1])
    Curveto_r(5.0 * scale[0], -11.0 * scale[1], 2.0 * scale[0], -
              13.0 * scale[1], -10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 4.0 * scale[1], -18.0 * scale[0],
              0.0 * scale[1], -22.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -9.0 * scale[1], -10.0 * scale[0], -
              13.0 * scale[1], -15.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 7.0 * scale[1], -11.0 * scale[0],
              7.0 * scale[1], 4.0 * scale[0], -38.0 * scale[1])
    Lineto_r(13.0 * scale[0], -38.0 * scale[1])
    Lineto_r(23.0 * scale[0], 30.0 * scale[1])
    Curveto_r(12.0 * scale[0], 17.0 * scale[1], 19.0 * scale[0],
              36.0 * scale[1], 15.0 * scale[0], 42.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 7.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], 8.0 * scale[0], 5.0 * scale[1])
    Curveto_r(9.0 * scale[0], -3.0 * scale[1], 23.0 * scale[0],
              2.0 * scale[1], 32.0 * scale[0], 12.0 * scale[1])
    Curveto_r(18.0 * scale[0], 20.0 * scale[1], 21.0 * scale[0],
              36.0 * scale[1], 6.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -10.0 *
              scale[0], -2.0 * scale[1], -10.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 7.0 * scale[0],
              12.0 * scale[1], 15.0 * scale[0], 16.0 * scale[1])
    Curveto_r(17.0 * scale[0], 6.0 * scale[1], 20.0 * scale[0],
              70.0 * scale[1], 5.0 * scale[0], 110.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 25.0 * scale[1], -40.0 * scale[0],
              37.0 * scale[1], -40.0 * scale[0], 16.0 * scale[1])
    te.end_fill()
    Moveto(129.0 * scale[0], 898.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -2.0 * scale[1], -3.0 * scale[0], -
              13.0 * scale[1], -4.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              20.0 * scale[1], 11.0 * scale[0], -16.0 * scale[1])
    Curveto_r(16.0 * scale[0], 6.0 * scale[1], 19.0 * scale[0],
              23.0 * scale[1], 3.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0],
              5.0 * scale[1], -4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 4.0 * scale[0],
              10.0 * scale[1], 1.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              1.0 * scale[1], -7.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(906.0 * scale[0], 882.0 * scale[1], x, y)
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
    Moveto(530.0 * scale[0], 872.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 109.0 * scale[0], -
              26.0 * scale[1], 118.0 * scale[0], -17.0 * scale[1])
    Curveto_r(10.0 * scale[0], 10.0 * scale[1], -4.0 * scale[0],
              14.0 * scale[1], -61.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-33.0 * scale[0], 4.0 * scale[1], -57.0 * scale[0],
              3.0 * scale[1], -57.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(901.0 * scale[0], 844.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(144.0 * scale[0], 745.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-14.0 * scale[0], -11.0 * scale[1], -15.0 *
              scale[0], -14.0 * scale[1], -3.0 * scale[0], -9.0 * scale[1])
    Curveto_r(10.0 * scale[0], 3.0 * scale[1], 20.0 * scale[0],
              0.0 * scale[1], 25.0 * scale[0], -7.0 * scale[1])
    Curveto_r(4.0 * scale[0], -8.0 * scale[1], 3.0 * scale[0], -
              10.0 * scale[1], -4.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -12.0 * scale[0],
              3.0 * scale[1], -12.0 * scale[0], -3.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -3.0 * scale[0], -
              17.0 * scale[1], -7.0 * scale[0], -26.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -15.0 * scale[1], -3.0 *
              scale[0], -16.0 * scale[1], 15.0 * scale[0], -6.0 * scale[1])
    Curveto_r(22.0 * scale[0], 12.0 * scale[1], 31.0 * scale[0],
              51.0 * scale[1], 11.0 * scale[0], 51.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0],
              5.0 * scale[1], -4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(9.0 * scale[0], 14.0 * scale[1], 2.0 * scale[0],
              12.0 * scale[1], -21.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(13.0 * scale[0], 518.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -84.0 * scale[1], 3.0 * scale[0], -
              125.0 * scale[1], 5.0 * scale[0], -90.0 * scale[1])
    Curveto_r(1.0 * scale[0], 34.0 * scale[1], 7.0 * scale[0],
              62.0 * scale[1], 11.0 * scale[0], 62.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 5.0 * scale[0],
              17.0 * scale[1], 0.0 * scale[0], 38.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 49.0 * scale[1], -11.0 * scale[0],
              115.0 * scale[1], 0.0 * scale[0], 108.0 * scale[1])
    Curveto_r(5.0 * scale[0], -4.0 * scale[1], 7.0 * scale[0],
              3.0 * scale[1], 4.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 54.0 * scale[1], -22.0 * scale[0],
              5.0 * scale[1], -20.0 * scale[0], -132.0 * scale[1])
    te.end_fill()
    Moveto(12.0 * scale[0], 325.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#746b2c')
    te.end_fill()
    Moveto(213.0 * scale[0], 1043.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(373.0 * scale[0], 1043.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(728.0 * scale[0], 1043.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 32.0 *
              scale[0], -2.0 * scale[1], 45.0 * scale[0], 0.0 * scale[1])
    Curveto_r(12.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              4.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 0.0 * scale[1], -35.0 *
              scale[0], -2.0 * scale[1], -22.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(33.0 * scale[0], 1021.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -11.0 * scale[1], 6.0 * scale[0], -
              17.0 * scale[1], 14.0 * scale[0], -14.0 * scale[1])
    Curveto_r(10.0 * scale[0], 4.0 * scale[1], 11.0 * scale[0],
              9.0 * scale[1], 2.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 19.0 * scale[1], -18.0 * scale[0],
              18.0 * scale[1], -16.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(67.0 * scale[0], 1024.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -11.0 * scale[1], 8.0 * scale[0], -
              12.0 * scale[1], 13.0 * scale[0], -4.0 * scale[1])
    Curveto_r(11.0 * scale[0], 17.0 * scale[1], 53.0 * scale[0],
              2.0 * scale[1], 46.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -20.0 * scale[1], 0.0 * scale[0], -
              17.0 * scale[1], 27.0 * scale[0], 10.0 * scale[1])
    Lineto_r(24.0 * scale[0], 24.0 * scale[1])
    Lineto_r(-58.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-49.0 * scale[0], 0.0 * scale[1], -57.0 * scale[0], -
              2.0 * scale[1], -52.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(898.0 * scale[0], 1033.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(962.0 * scale[0], 1024.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -8.0 * scale[1], -20.0 * scale[0], -
              27.0 * scale[1], -29.0 * scale[0], -42.0 * scale[1])
    Lineto_r(-15.0 * scale[0], -27.0 * scale[1])
    Lineto_r(6.0 * scale[0], 26.0 * scale[1])
    Curveto_r(5.0 * scale[0], 23.0 * scale[1], 2.0 * scale[0],
              27.0 * scale[1], -19.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-26.0 * scale[0], 5.0 * scale[1], -35.0 * scale[0], -
              6.0 * scale[1], -12.0 * scale[0], -15.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], -3.0 * scale[0], -
              3.0 * scale[1], -20.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 4.0 * scale[1], -33.0 * scale[0],
              2.0 * scale[1], -33.0 * scale[0], -6.0 * scale[1])
    Curveto_r(0.0 * scale[0], -18.0 * scale[1], 28.0 * scale[0], -
              43.0 * scale[1], 40.0 * scale[0], -36.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 10.0 * scale[0],
              3.0 * scale[1], 9.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -4.0 * scale[1], -1.0 * scale[0], -
              19.0 * scale[1], 0.0 * scale[0], -33.0 * scale[1])
    Lineto_r(2.0 * scale[0], -25.0 * scale[1])
    Lineto_r(17.0 * scale[0], 28.0 * scale[1])
    Curveto_r(11.0 * scale[0], 17.0 * scale[1], 26.0 * scale[0],
              27.0 * scale[1], 42.0 * scale[0], 28.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0],
              3.0 * scale[1], 13.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 5.0 * scale[1], -18.0 * scale[0],
              33.0 * scale[1], -4.0 * scale[0], 33.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 24.0 * scale[0],
              41.0 * scale[1], 18.0 * scale[0], 46.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 1.0 * scale[1], -8.0 * scale[0], -
              5.0 * scale[1], -15.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(208.0 * scale[0], 983.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(133.0 * scale[0], 923.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -10.0 * scale[1], -8.0 * scale[0], -
              22.0 * scale[1], -11.0 * scale[0], -27.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 0.0 *
              scale[0], -6.0 * scale[1], 5.0 * scale[0], -3.0 * scale[1])
    Curveto_r(11.0 * scale[0], 7.0 * scale[1], 25.0 * scale[0],
              47.0 * scale[1], 17.0 * scale[0], 47.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              8.0 * scale[1], -11.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(934.0 * scale[0], 911.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(16.0 * scale[0], -3.0 * scale[1], 33.0 * scale[0], -
              15.0 * scale[1], 37.0 * scale[0], -26.0 * scale[1])
    Curveto_r(5.0 * scale[0], -14.0 * scale[1], 8.0 * scale[0], -
              15.0 * scale[1], 8.0 * scale[0], -4.0 * scale[1])
    Curveto_r(1.0 * scale[0], 23.0 * scale[1], -20.0 * scale[0],
              39.0 * scale[1], -48.0 * scale[0], 38.0 * scale[1])
    Curveto_r(-25.0 * scale[0], -1.0 * scale[1], -25.0 *
              scale[0], -2.0 * scale[1], 3.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(151.0 * scale[0], 882.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -19.0 * scale[1], -5.0 * scale[0], -
              21.0 * scale[1], -26.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 4.0 * scale[1], -25.0 * scale[0],
              2.0 * scale[1], -25.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 6.0 * scale[0], -
              8.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 14.0 * scale[0], -
              1.0 * scale[1], 15.0 * scale[0], -8.0 * scale[1])
    Curveto_r(1.0 * scale[0], -7.0 * scale[1], 5.0 * scale[0], -
              32.0 * scale[1], 8.0 * scale[0], -56.0 * scale[1])
    Curveto_r(5.0 * scale[0], -32.0 * scale[1], 10.0 * scale[0], -
              42.0 * scale[1], 21.0 * scale[0], -38.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 11.0 * scale[0],
              1.0 * scale[1], 8.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], -1.0 * scale[0], -
              10.0 * scale[1], 4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0], -
              9.0 * scale[1], 11.0 * scale[0], -21.0 * scale[1])
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], -4.0 * scale[0], -
              18.0 * scale[1], -12.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 0.0 * scale[0], -
              13.0 * scale[1], -6.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -4.0 * scale[1], -10.0 *
              scale[0], -6.0 * scale[1], 0.0 * scale[0], -6.0 * scale[1])
    Curveto_r(8.0 * scale[0], -1.0 * scale[1], 10.0 * scale[0], -
              6.0 * scale[1], 6.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], 9.0 * scale[0],
              5.0 * scale[1], 29.0 * scale[0], 27.0 * scale[1])
    Curveto_r(31.0 * scale[0], 35.0 * scale[1], 33.0 * scale[0],
              40.0 * scale[1], 16.0 * scale[0], 43.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 4.0 * scale[1], -42.0 * scale[0],
              35.0 * scale[1], -31.0 * scale[0], 47.0 * scale[1])
    Curveto_r(4.0 * scale[0], 5.0 * scale[1], 2.0 * scale[0],
              5.0 * scale[1], -4.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -10.0 * scale[1], -41.0 * scale[0],
              52.0 * scale[1], -25.0 * scale[0], 63.0 * scale[1])
    Curveto_r(7.0 * scale[0], 4.0 * scale[1], 11.0 * scale[0],
              18.0 * scale[1], 8.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 24.0 * scale[1], -4.0 * scale[0],
              24.0 * scale[1], -6.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(120.0 * scale[0], 729.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 7.0 * scale[0], -
              12.0 * scale[1], 15.0 * scale[0], -19.0 * scale[1])
    Curveto_r(12.0 * scale[0], -10.0 * scale[1], 15.0 *
              scale[0], -9.0 * scale[1], 15.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], 5.0 * scale[0],
              14.0 * scale[1], 12.0 * scale[0], 10.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 8.0 *
              scale[0], -3.0 * scale[1], 4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 11.0 * scale[1], -46.0 * scale[0],
              12.0 * scale[1], -46.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(826.0 * scale[0], 694.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(28.0 * scale[0], -27.0 * scale[1], 39.0 * scale[0], -
              32.0 * scale[1], 45.0 * scale[0], -22.0 * scale[1])
    Curveto_r(5.0 * scale[0], 7.0 * scale[1], 8.0 * scale[0],
              18.0 * scale[1], 8.0 * scale[0], 23.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -3.0 * scale[0],
              4.0 * scale[1], -6.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -20.0 * scale[1], -23.0 *
              scale[0], -15.0 * scale[1], -23.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], -3.0 * scale[0],
              20.0 * scale[1], -7.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -18.0 * scale[0],
              2.0 * scale[1], -31.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 3.0 * scale[1], -17.0 *
              scale[0], -1.0 * scale[1], 14.0 * scale[0], -32.0 * scale[1])
    te.end_fill()
    Moveto(119.0 * scale[0], 623.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(16.0 * scale[0], 13.0 * scale[1], 21.0 * scale[0],
              21.0 * scale[1], 13.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              8.0 * scale[1], -17.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(80.0 * scale[0], 590.0 * scale[1], x, y)
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
    te.color('#81511c')
    te.end_fill()
    Moveto(288.0 * scale[0], 1413.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(658.0 * scale[0], 1413.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(97.0 * scale[0], 1400.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-42.0 * scale[0], -8.0 * scale[1], -73.0 * scale[0], -
              32.0 * scale[1], -63.0 * scale[0], -49.0 * scale[1])
    Curveto_r(12.0 * scale[0], -20.0 * scale[1], 36.0 *
              scale[0], -12.0 * scale[1], 36.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 20.0 * scale[1], 4.0 * scale[0],
              22.0 * scale[1], 45.0 * scale[0], 19.0 * scale[1])
    Curveto_r(36.0 * scale[0], -3.0 * scale[1], 45.0 *
              scale[0], -1.0 * scale[1], 45.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], -5.0 * scale[0],
              18.0 * scale[1], -63.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(780.0 * scale[0], 1401.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 10.0 * scale[0], -
              11.0 * scale[1], 23.0 * scale[0], -14.0 * scale[1])
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 31.0 * scale[0], -
              8.0 * scale[1], 42.0 * scale[0], -12.0 * scale[1])
    Curveto_r(16.0 * scale[0], -5.0 * scale[1], 17.0 *
              scale[0], -5.0 * scale[1], 5.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 10.0 * scale[1], -7.0 * scale[0],
              16.0 * scale[1], 13.0 * scale[0], 12.0 * scale[1])
    Curveto_r(5.0 * scale[0], -1.0 * scale[1], 6.0 * scale[0],
              2.0 * scale[1], 3.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 12.0 * scale[1], -86.0 * scale[0],
              14.0 * scale[1], -86.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(904.0 * scale[0], 1391.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(17.0 * scale[0], -6.0 * scale[1], 15.0 * scale[0], -
              9.0 * scale[1], -13.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-39.0 * scale[0], -16.0 * scale[1], -35.0 *
              scale[0], -23.0 * scale[1], 7.0 * scale[0], -11.0 * scale[1])
    Curveto_r(21.0 * scale[0], 6.0 * scale[1], 31.0 * scale[0],
              6.0 * scale[1], 29.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 11.0 * scale[0], -15.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 11.0 * scale[0],
              3.0 * scale[1], 8.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 12.0 * scale[1], -5.0 * scale[0],
              26.0 * scale[1], -5.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 4.0 * scale[1], -13.0 * scale[0],
              7.0 * scale[1], -28.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 0.0 * scale[1], -25.0 *
              scale[0], -2.0 * scale[1], -9.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(1.0 * scale[0], 1354.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(670.0 * scale[0], 1360.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(8.0 * scale[0], -5.0 * scale[1], 24.0 * scale[0], -
              10.0 * scale[1], 34.0 * scale[0], -10.0 * scale[1])
    Curveto_r(26.0 * scale[0], 0.0 * scale[1], 18.0 * scale[0],
              6.0 * scale[1], -19.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 5.0 * scale[1], -26.0 * scale[0],
              4.0 * scale[1], -15.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(39.0 * scale[0], 1320.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -36.0 * scale[1], -2.0 *
              scale[0], -50.0 * scale[1], 6.0 * scale[0], -49.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              7.0 * scale[1], 7.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 9.0 * scale[1], 6.0 * scale[0],
              18.0 * scale[1], 17.0 * scale[0], 21.0 * scale[1])
    Curveto_r(12.0 * scale[0], 3.0 * scale[1], 21.0 * scale[0],
              8.0 * scale[1], 21.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], -50.0 * scale[0],
              12.0 * scale[1], -51.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(936.0 * scale[0], 1305.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -15.0 * scale[1], 2.0 * scale[0], -
              25.0 * scale[1], -5.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              4.0 * scale[1], -11.0 * scale[0], -8.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 11.0 * scale[0], -
              8.0 * scale[1], 25.0 * scale[0], -8.0 * scale[1])
    Curveto_r(21.0 * scale[0], 0.0 * scale[1], 24.0 * scale[0],
              4.0 * scale[1], 19.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 11.0 * scale[1], -11.0 * scale[0],
              23.0 * scale[1], -16.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -5.0 * scale[0],
              9.0 * scale[1], 3.0 * scale[0], 12.0 * scale[1])
    Curveto_r(10.0 * scale[0], 4.0 * scale[1], 9.0 * scale[0],
              6.0 * scale[1], -4.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 1.0 * scale[1], -16.0 * scale[0], -
              4.0 * scale[1], -11.0 * scale[0], -24.0 * scale[1])
    te.end_fill()
    Moveto(206.0 * scale[0], 1307.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0], -
              15.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 0.0 * scale[0],
              11.0 * scale[1], -7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              8.0 * scale[1], -5.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(2.0 * scale[0], 1275.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(790.0 * scale[0], 1290.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(390.0 * scale[0], 1280.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(185.0 * scale[0], 1260.0 * scale[1], x, y)
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
    Moveto(950.0 * scale[0], 1240.0 * scale[1], x, y)
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
    Moveto(263.0 * scale[0], 1233.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(15.0 * scale[0], -2.0 * scale[1], 39.0 *
              scale[0], -2.0 * scale[1], 55.0 * scale[0], 0.0 * scale[1])
    Curveto_r(15.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              4.0 * scale[1], -28.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 0.0 * scale[1], -43.0 *
              scale[0], -2.0 * scale[1], -27.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(229.0 * scale[0], 1188.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -10.0 * scale[1], 25.0 * scale[0], -
              17.0 * scale[1], 40.0 * scale[0], -17.0 * scale[1])
    Lineto_r(26.0 * scale[0], 2.0 * scale[1])
    Lineto_r(-25.0 * scale[0], 4.0 * scale[1])
    te.penup()
    te.color('#c1cca1')
    te.end_fill()
    Moveto(9.0 * scale[0], 1413.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -21.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(397.0 * scale[0], 1362.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -30.0 * scale[1], 9.0 * scale[0], -
              66.0 * scale[1], 24.0 * scale[0], -57.0 * scale[1])
    Curveto_r(5.0 * scale[0], 4.0 * scale[1], 9.0 * scale[0],
              11.0 * scale[1], 9.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -4.0 * scale[0],
              7.0 * scale[1], -10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -4.0 * scale[1], -10.0 * scale[0],
              5.0 * scale[1], -10.0 * scale[0], 19.0 * scale[1])
    Curveto_r(0.0 * scale[0], 23.0 * scale[1], 2.0 * scale[0],
              25.0 * scale[1], 19.0 * scale[0], 14.0 * scale[1])
    Curveto_r(10.0 * scale[0], -6.0 * scale[1], 18.0 * scale[0], -
              16.0 * scale[1], 17.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -6.0 * scale[1], -1.0 *
              scale[0], -8.0 * scale[1], 1.0 * scale[0], -3.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], 9.0 * scale[0],
              5.0 * scale[1], 14.0 * scale[0], 1.0 * scale[1])
    Curveto_r(16.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0],
              8.0 * scale[1], -8.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-43.0 * scale[0], 33.0 * scale[1], -51.0 * scale[0],
              34.0 * scale[1], -56.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(587.0 * scale[0], 1354.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -32.0 * scale[1], 4.0 * scale[0], -
              36.0 * scale[1], -13.0 * scale[0], -32.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 3.0 * scale[1], -18.0 * scale[0],
              11.0 * scale[1], -16.0 * scale[0], 28.0 * scale[1])
    Curveto_r(2.0 * scale[0], 24.0 * scale[1], 2.0 * scale[0],
              24.0 * scale[1], -16.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -19.0 * scale[1], -17.0 *
              scale[0], -20.0 * scale[1], 12.0 * scale[0], -36.0 * scale[1])
    Curveto_r(17.0 * scale[0], -9.0 * scale[1], 34.0 * scale[0], -
              15.0 * scale[1], 39.0 * scale[0], -12.0 * scale[1])
    Curveto_r(10.0 * scale[0], 6.0 * scale[1], 9.0 * scale[0],
              83.0 * scale[1], -2.0 * scale[0], 83.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              16.0 * scale[1], -4.0 * scale[0], -36.0 * scale[1])
    te.end_fill()
    Moveto(85.0 * scale[0], 1288.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-40.0 * scale[0], -43.0 * scale[1])
    Lineto_r(43.0 * scale[0], 40.0 * scale[1])
    Curveto_r(39.0 * scale[0], 36.0 * scale[1], 47.0 * scale[0],
              45.0 * scale[1], 39.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -21.0 * scale[0], -
              19.0 * scale[1], -42.0 * scale[0], -42.0 * scale[1])
    te.end_fill()
    Moveto(131.0 * scale[0], 1297.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-25.0 * scale[0], -32.0 * scale[1])
    Lineto_r(27.0 * scale[0], 24.0 * scale[1])
    Curveto_r(15.0 * scale[0], 14.0 * scale[1], 29.0 * scale[0],
              22.0 * scale[1], 32.0 * scale[0], 19.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], -1.0 * scale[0], -
              11.0 * scale[1], -10.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -7.0 * scale[1], -15.0 * scale[0], -
              17.0 * scale[1], -15.0 * scale[0], -22.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 11.0 * scale[0],
              3.0 * scale[1], 25.0 * scale[0], 18.0 * scale[1])
    Curveto_r(26.0 * scale[0], 28.0 * scale[1], 32.0 * scale[0],
              40.0 * scale[1], 15.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -10.0 *
              scale[0], -1.0 * scale[1], -10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 19.0 * scale[1], -14.0 * scale[0],
              11.0 * scale[1], -39.0 * scale[0], -22.0 * scale[1])
    te.end_fill()
    Moveto(822.0 * scale[0], 1297.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-34.0 * scale[0], -35.0 * scale[1], -39.0 *
              scale[0], -47.0 * scale[1], -20.0 * scale[0], -47.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0],
              3.0 * scale[1], 4.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], 8.0 * scale[0],
              22.0 * scale[1], 26.0 * scale[0], 40.0 * scale[1])
    Curveto_r(17.0 * scale[0], 18.0 * scale[1], 30.0 * scale[0],
              33.0 * scale[1], 27.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -19.0 * scale[0], -
              15.0 * scale[1], -37.0 * scale[0], -33.0 * scale[1])
    te.end_fill()
    Moveto(900.0 * scale[0], 1328.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -5.0 * scale[1], -3.0 * scale[0], -
              14.0 * scale[1], -4.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -7.0 * scale[1], -8.0 * scale[0], -
              12.0 * scale[1], -17.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 1.0 * scale[1], -24.0 * scale[0], -
              8.0 * scale[1], -35.0 * scale[0], -20.0 * scale[1])
    Lineto_r(-19.0 * scale[0], -23.0 * scale[1])
    Lineto_r(22.0 * scale[0], 18.0 * scale[1])
    Curveto_r(12.0 * scale[0], 11.0 * scale[1], 26.0 * scale[0],
              16.0 * scale[1], 31.0 * scale[0], 13.0 * scale[1])
    Curveto_r(13.0 * scale[0], -8.0 * scale[1], 35.0 * scale[0],
              20.0 * scale[1], 29.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 7.0 * scale[1], -6.0 * scale[0],
              10.0 * scale[1], -7.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(473.0 * scale[0], 1313.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-34.0 * scale[0], -7.0 * scale[1], -28.0 *
              scale[0], -20.0 * scale[1], 7.0 * scale[0], -15.0 * scale[1])
    Curveto_r(16.0 * scale[0], 2.0 * scale[1], 27.0 * scale[0],
              8.0 * scale[1], 24.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], -6.0 * scale[0],
              8.0 * scale[1], -7.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -1.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -24.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(415.0 * scale[0], 1278.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-20.0 * scale[0], -21.0 * scale[1])
    Lineto_r(23.0 * scale[0], 12.0 * scale[1])
    Curveto_r(12.0 * scale[0], 6.0 * scale[1], 22.0 * scale[0],
              16.0 * scale[1], 22.0 * scale[0], 21.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], -2.0 * scale[0],
              12.0 * scale[1], -25.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(574.0 * scale[0], 1264.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -9.0 * scale[1], 16.0 * scale[0], -
              32.0 * scale[1], 16.0 * scale[0], -55.0 * scale[1])
    Curveto_r(0.0 * scale[0], -58.0 * scale[1], -44.0 * scale[0], -
              102.0 * scale[1], -97.0 * scale[0], -97.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 2.0 * scale[1], -37.0 * scale[0],
              8.0 * scale[1], -36.0 * scale[0], 15.0 * scale[1])
    Curveto_r(2.0 * scale[0], 7.0 * scale[1], -3.0 * scale[0],
              10.0 * scale[1], -10.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -8.0 * scale[1], -36.0 * scale[0],
              9.0 * scale[1], -46.0 * scale[0], 50.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 23.0 * scale[1], -9.0 * scale[0],
              30.0 * scale[1], -10.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -37.0 * scale[1], 17.0 * scale[0], -
              71.0 * scale[1], 48.0 * scale[0], -88.0 * scale[1])
    Curveto_r(77.0 * scale[0], -39.0 * scale[1], 161.0 * scale[0],
              4.0 * scale[1], 161.0 * scale[0], 85.0 * scale[1])
    Curveto_r(0.0 * scale[0], 44.0 * scale[1], -14.0 * scale[0],
              80.0 * scale[1], -31.0 * scale[0], 80.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -3.0 * scale[0], -
              7.0 * scale[1], 5.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(871.0 * scale[0], 1254.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(562.0 * scale[0], 1230.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -10.0 * scale[1], 14.0 * scale[0], -
              18.0 * scale[1], 15.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], 6.0 * scale[1], -9.0 * scale[0],
              36.0 * scale[1], -18.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              9.0 * scale[1], 3.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(918.0 * scale[0], 1218.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -10.0 * scale[1], 7.0 * scale[0], -
              18.0 * scale[1], 11.0 * scale[0], -18.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              8.0 * scale[1], 8.0 * scale[0], 18.0 * scale[1])
    Curveto_r(1.0 * scale[0], 10.0 * scale[1], -4.0 * scale[0],
              19.0 * scale[1], -11.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              8.0 * scale[1], -8.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(790.0 * scale[0], 1190.0 * scale[1], x, y)
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
    Moveto(76.0 * scale[0], 1178.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 10.0 * scale[0], -
              6.0 * scale[1], 15.0 * scale[0], -3.0 * scale[1])
    Curveto_r(13.0 * scale[0], 9.0 * scale[1], 11.0 * scale[0],
              12.0 * scale[1], -6.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -9.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(116.0 * scale[0], 1181.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], -5.0 * scale[0], -
              15.0 * scale[1], -2.0 * scale[0], -18.0 * scale[1])
    Curveto_r(9.0 * scale[0], -9.0 * scale[1], 19.0 * scale[0],
              4.0 * scale[1], 14.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 11.0 * scale[1], -6.0 * scale[0],
              11.0 * scale[1], -12.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(841.0 * scale[0], 1154.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(165.0 * scale[0], 1150.0 * scale[1], x, y)
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
    Moveto(895.0 * scale[0], 1150.0 * scale[1], x, y)
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
    Moveto(100.0 * scale[0], 931.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 18.0 * scale[1], -14.0 * scale[0],
              21.0 * scale[1], -14.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(403.0 * scale[0], 834.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -3.0 * scale[1], -13.0 * scale[0], -
              11.0 * scale[1], -13.0 * scale[0], -19.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -7.0 * scale[0], -
              18.0 * scale[1], -15.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -7.0 * scale[1], -15.0 *
              scale[0], -8.0 * scale[1], -15.0 * scale[0], -3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 27.0 * scale[1], -73.0 * scale[0], -
              62.0 * scale[1], -86.0 * scale[0], -104.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -27.0 * scale[1], -18.0 * scale[0], -
              55.0 * scale[1], -22.0 * scale[0], -63.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -17.0 * scale[1], -8.0 * scale[0], -
              30.0 * scale[1], -11.0 * scale[0], -80.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -27.0 * scale[1], -4.0 * scale[0], -
              31.0 * scale[1], -11.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 13.0 * scale[1], -10.0 * scale[0],
              13.0 * scale[1], -10.0 * scale[0], 0.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 5.0 * scale[0], -
              21.0 * scale[1], 12.0 * scale[0], -28.0 * scale[1])
    Curveto_r(9.0 * scale[0], -9.0 * scale[1], 9.0 * scale[0], -
              12.0 * scale[1], -2.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -11.0 *
              scale[0], -3.0 * scale[1], -2.0 * scale[0], -12.0 * scale[1])
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 12.0 * scale[0], -
              19.0 * scale[1], 12.0 * scale[0], -28.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 9.0 * scale[0], -
              22.0 * scale[1], 20.0 * scale[0], -30.0 * scale[1])
    Curveto_r(11.0 * scale[0], -8.0 * scale[1], 20.0 * scale[0], -
              20.0 * scale[1], 20.0 * scale[0], -26.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], 12.0 * scale[0], -
              22.0 * scale[1], 26.0 * scale[0], -33.0 * scale[1])
    Curveto_r(21.0 * scale[0], -17.0 * scale[1], 30.0 *
              scale[0], -18.0 * scale[1], 48.0 * scale[0], -9.0 * scale[1])
    Curveto_r(11.0 * scale[0], 6.0 * scale[1], 18.0 * scale[0],
              7.0 * scale[1], 14.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -9.0 * scale[1], 53.0 * scale[0], -
              66.0 * scale[1], 63.0 * scale[0], -59.0 * scale[1])
    Curveto_r(4.0 * scale[0], 2.0 * scale[1], 12.0 * scale[0], -
              3.0 * scale[1], 19.0 * scale[0], -11.0 * scale[1])
    Curveto_r(7.0 * scale[0], -8.0 * scale[1], 20.0 * scale[0], -
              15.0 * scale[1], 29.0 * scale[0], -15.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 3.0 * scale[0],
              8.0 * scale[1], -16.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-36.0 * scale[0], 22.0 * scale[1], -43.0 * scale[0],
              40.0 * scale[1], -15.0 * scale[0], 40.0 * scale[1])
    Curveto_r(16.0 * scale[0], 1.0 * scale[1], 16.0 * scale[0],
              1.0 * scale[1], -1.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              14.0 * scale[1], -12.0 * scale[0], 19.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], -2.0 * scale[0],
              11.0 * scale[1], -11.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -13.0 * scale[0],
              10.0 * scale[1], -10.0 * scale[0], 14.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], -5.0 * scale[0],
              7.0 * scale[1], -17.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -3.0 * scale[1], -29.0 * scale[0],
              3.0 * scale[1], -39.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 15.0 * scale[1], -15.0 * scale[0],
              24.0 * scale[1], -5.0 * scale[0], 63.0 * scale[1])
    Curveto_r(7.0 * scale[0], 25.0 * scale[1], 16.0 * scale[0],
              51.0 * scale[1], 21.0 * scale[0], 58.0 * scale[1])
    Curveto_r(4.0 * scale[0], 7.0 * scale[1], 5.0 * scale[0],
              16.0 * scale[1], 2.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 10.0 * scale[1], -36.0 * scale[0], -
              30.0 * scale[1], -31.0 * scale[0], -47.0 * scale[1])
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], -4.0 * scale[0], -
              4.0 * scale[1], -15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 14.0 * scale[1], -20.0 * scale[0],
              32.0 * scale[1], -19.0 * scale[0], 40.0 * scale[1])
    Curveto_r(0.0 * scale[0], 18.0 * scale[1], 23.0 * scale[0],
              50.0 * scale[1], 36.0 * scale[0], 50.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              13.0 * scale[1], 11.0 * scale[0], 30.0 * scale[1])
    Curveto_r(1.0 * scale[0], 31.0 * scale[1], 9.0 * scale[0],
              44.0 * scale[1], 54.0 * scale[0], 87.0 * scale[1])
    Curveto_r(23.0 * scale[0], 22.0 * scale[1], 36.0 * scale[0],
              25.0 * scale[1], 99.0 * scale[0], 26.0 * scale[1])
    Lineto_r(72.0 * scale[0], 2.0 * scale[1])
    Lineto_r(47.0 * scale[0], -45.0 * scale[1])
    Curveto_r(51.0 * scale[0], -49.0 * scale[1], 72.0 * scale[0], -
              111.0 * scale[1], 51.0 * scale[0], -147.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -10.0 * scale[1], -11.0 *
              scale[0], -12.0 * scale[1], -11.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              12.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0], -
              6.0 * scale[1], 4.0 * scale[0], -17.0 * scale[1])
    Curveto_r(14.0 * scale[0], -17.0 * scale[1], 20.0 * scale[0], -
              35.0 * scale[1], 34.0 * scale[0], -103.0 * scale[1])
    Curveto_r(4.0 * scale[0], -17.0 * scale[1], -1.0 * scale[0], -
              31.0 * scale[1], -13.0 * scale[0], -42.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -15.0 * scale[1], -22.0 *
              scale[0], -16.0 * scale[1], -45.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-31.0 * scale[0], 16.0 * scale[1], -43.0 * scale[0],
              10.0 * scale[1], -25.0 * scale[0], -12.0 * scale[1])
    Curveto_r(8.0 * scale[0], -10.0 * scale[1], 8.0 * scale[0], -
              13.0 * scale[1], 1.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -15.0 * scale[0],
              0.0 * scale[1], -18.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -22.0 * scale[1], -8.0 *
              scale[0], -24.0 * scale[1], 9.0 * scale[0], -24.0 * scale[1])
    Curveto_r(21.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0], -
              22.0 * scale[1], -28.0 * scale[0], -47.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -14.0 * scale[1], -26.0 *
              scale[0], -23.0 * scale[1], -16.0 * scale[0], -23.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 26.0 * scale[0],
              9.0 * scale[1], 39.0 * scale[0], 20.0 * scale[1])
    Curveto_r(12.0 * scale[0], 11.0 * scale[1], 26.0 * scale[0],
              17.0 * scale[1], 31.0 * scale[0], 15.0 * scale[1])
    Curveto_r(4.0 * scale[0], -3.0 * scale[1], 10.0 *
              scale[0], -1.0 * scale[1], 14.0 * scale[0], 4.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 12.0 * scale[0],
              8.0 * scale[1], 20.0 * scale[0], 5.0 * scale[1])
    Curveto_r(9.0 * scale[0], -4.0 * scale[1], 18.0 * scale[0],
              2.0 * scale[1], 22.0 * scale[0], 12.0 * scale[1])
    Curveto_r(4.0 * scale[0], 11.0 * scale[1], 15.0 * scale[0],
              26.0 * scale[1], 25.0 * scale[0], 35.0 * scale[1])
    Curveto_r(10.0 * scale[0], 9.0 * scale[1], 18.0 * scale[0],
              22.0 * scale[1], 18.0 * scale[0], 28.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], 4.0 * scale[0],
              10.0 * scale[1], 9.0 * scale[0], 7.0 * scale[1])
    Curveto_r(11.0 * scale[0], -7.0 * scale[1], 24.0 * scale[0],
              41.0 * scale[1], 16.0 * scale[0], 54.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], -1.0 * scale[0],
              10.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0], -
              5.0 * scale[1], 11.0 * scale[0], -12.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 3.0 * scale[0], -
              8.0 * scale[1], 7.0 * scale[0], -5.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], 0.0 * scale[0],
              18.0 * scale[1], -7.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 22.0 * scale[1], -12.0 * scale[0],
              33.0 * scale[1], 0.0 * scale[0], 73.0 * scale[1])
    Curveto_r(7.0 * scale[0], 26.0 * scale[1], 13.0 * scale[0],
              61.0 * scale[1], 12.0 * scale[0], 77.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 17.0 * scale[1], -2.0 * scale[0],
              47.0 * scale[1], -2.0 * scale[0], 68.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 25.0 * scale[1], -5.0 * scale[0],
              35.0 * scale[1], -12.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -5.0 * scale[1], -9.0 *
              scale[0], -1.0 * scale[1], -5.0 * scale[0], 10.0 * scale[1])
    Curveto_r(4.0 * scale[0], 10.0 * scale[1], 1.0 * scale[0],
              19.0 * scale[1], -7.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -26.0 * scale[0],
              24.0 * scale[1], -41.0 * scale[0], 46.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 22.0 * scale[1], -29.0 * scale[0],
              37.0 * scale[1], -33.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], 0.0 * scale[0], -
              12.0 * scale[1], 6.0 * scale[0], -18.0 * scale[1])
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 12.0 * scale[0], -
              19.0 * scale[1], 12.0 * scale[0], -27.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], -8.0 * scale[0], -
              1.0 * scale[1], -16.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 30.0 * scale[1], -44.0 * scale[0],
              45.0 * scale[1], -44.0 * scale[0], 22.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -8.0 * scale[0], -
              10.0 * scale[1], -17.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0],
              2.0 * scale[1], -3.0 * scale[0], 10.0 * scale[1])
    Curveto_r(11.0 * scale[0], 8.0 * scale[1], 6.0 * scale[0],
              10.0 * scale[1], -20.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -1.0 * scale[1], -69.0 * scale[0],
              1.0 * scale[1], -110.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-41.0 * scale[0], 4.0 * scale[1], -81.0 * scale[0],
              4.0 * scale[1], -87.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(95.0 * scale[0], 560.0 * scale[1], x, y)
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
    Moveto(420.0 * scale[0], 546.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(926.0 * scale[0], 517.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0], -
              15.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 0.0 * scale[0],
              11.0 * scale[1], -7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              8.0 * scale[1], -5.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(40.0 * scale[0], 506.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(3.0 * scale[0], 200.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -47.0 * scale[1], 2.0 * scale[0], -
              66.0 * scale[1], 4.0 * scale[0], -42.0 * scale[1])
    Curveto_r(2.0 * scale[0], 23.0 * scale[1], 2.0 * scale[0],
              61.0 * scale[1], 0.0 * scale[0], 85.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 23.0 * scale[1], -4.0 * scale[0],
              4.0 * scale[1], -4.0 * scale[0], -43.0 * scale[1])
    te.end_fill()
    Moveto(518.0 * scale[0], 253.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(310.0 * scale[0], 144.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -59.0 * scale[1], 25.0 * scale[0], -
              99.0 * scale[1], 72.0 * scale[0], -117.0 * scale[1])
    Curveto_r(57.0 * scale[0], -22.0 * scale[1], 240.0 *
              scale[0], -24.0 * scale[1], 280.0 * scale[0], -3.0 * scale[1])
    Curveto_r(20.0 * scale[0], 11.0 * scale[1], 28.0 * scale[0],
              11.0 * scale[1], 32.0 * scale[0], 3.0 * scale[1])
    Curveto_r(2.0 * scale[0], -7.0 * scale[1], 5.0 *
              scale[0], -3.0 * scale[1], 6.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], 7.0 * scale[0],
              29.0 * scale[1], 15.0 * scale[0], 39.0 * scale[1])
    Curveto_r(8.0 * scale[0], 11.0 * scale[1], 15.0 * scale[0],
              34.0 * scale[1], 15.0 * scale[0], 52.0 * scale[1])
    Lineto_r(0.0 * scale[0], 31.0 * scale[1])
    Lineto_r(-45.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-34.0 * scale[0], -8.0 * scale[1], -55.0 *
              scale[0], -7.0 * scale[1], -85.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 7.0 * scale[1], -64.0 * scale[0],
              12.0 * scale[1], -93.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-150.0 * scale[0], -6.0 * scale[1], -183.0 *
              scale[0], -6.0 * scale[1], -189.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 5.0 * scale[1], -8.0 * scale[0], -
              4.0 * scale[1], -8.0 * scale[0], -21.0 * scale[1])
    te.end_fill()
    Moveto_r(214.0 * scale[0], -40.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(44.0 * scale[0], 15.0 * scale[1], 76.0 * scale[0],
              11.0 * scale[1], 76.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              14.0 * scale[1], 8.0 * scale[0], -14.0 * scale[1])
    Curveto_r(20.0 * scale[0], 0.0 * scale[1], 6.0 * scale[0], -
              33.0 * scale[1], -17.0 * scale[0], -42.0 * scale[1])
    Curveto_r(-28.0 * scale[0], -10.0 * scale[1], -141.0 *
              scale[0], -1.0 * scale[1], -141.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], -10.0 * scale[0],
              6.0 * scale[1], -22.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -4.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -13.0 * scale[0], 8.0 * scale[1])
    Curveto_r(6.0 * scale[0], 10.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], -8.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -5.0 * scale[1], -14.0 *
              scale[0], -2.0 * scale[1], -8.0 * scale[0], 16.0 * scale[1])
    Curveto_r(5.0 * scale[0], 12.0 * scale[1], 13.0 * scale[0],
              22.0 * scale[1], 19.0 * scale[0], 22.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              3.0 * scale[1], 17.0 * scale[0], 7.0 * scale[1])
    Curveto_r(4.0 * scale[0], 4.0 * scale[1], 17.0 * scale[0],
              1.0 * scale[1], 29.0 * scale[0], -7.0 * scale[1])
    Curveto_r(18.0 * scale[0], -12.0 * scale[1], 27.0 *
              scale[0], -12.0 * scale[1], 60.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(1.0 * scale[0], 84.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(0.0 * scale[0], 44.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -28.0 * scale[1], 61.0 * scale[0], -
              57.0 * scale[1], 74.0 * scale[0], -35.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], -18.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -4.0 * scale[1], -28.0 * scale[0],
              2.0 * scale[1], -40.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 13.0 * scale[1], -16.0 * scale[0],
              19.0 * scale[1], -16.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(965.0 * scale[0], 20.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -7.0 * scale[1], -17.0 *
              scale[0], -9.0 * scale[1], -3.0 * scale[0], -9.0 * scale[1])
    Curveto_r(9.0 * scale[0], -1.0 * scale[1], 20.0 * scale[0],
              4.0 * scale[1], 23.0 * scale[0], 9.0 * scale[1])
    Curveto_r(7.0 * scale[0], 11.0 * scale[1], 7.0 * scale[0],
              11.0 * scale[1], -20.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(153.0 * scale[0], 3.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(37.0 * scale[0], -2.0 * scale[1], 96.0 *
              scale[0], -2.0 * scale[1], 130.0 * scale[0], 0.0 * scale[1])
    Curveto_r(34.0 * scale[0], 2.0 * scale[1], 4.0 * scale[0],
              3.0 * scale[1], -68.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-72.0 * scale[0], 0.0 * scale[1], -99.0 *
              scale[0], -1.0 * scale[1], -62.0 * scale[0], -3.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#312c0f')
    te.end_fill()
    Moveto(840.0 * scale[0], 1419.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-55.0 * scale[0], -6.0 * scale[1])
    Lineto_r(65.0 * scale[0], -2.0 * scale[1])
    Curveto_r(99.0 * scale[0], -2.0 * scale[1], 113.0 * scale[0], -
              13.0 * scale[1], 117.0 * scale[0], -88.0 * scale[1])
    Curveto_r(3.0 * scale[0], -57.0 * scale[1], 2.0 * scale[0], -
              62.0 * scale[1], -19.0 * scale[0], -66.0 * scale[1])
    Curveto_r(-22.0 * scale[0], -4.0 * scale[1], -22.0 *
              scale[0], -4.0 * scale[1], -1.0 * scale[0], -6.0 * scale[1])
    Curveto_r(20.0 * scale[0], -1.0 * scale[1], 21.0 * scale[0], -
              6.0 * scale[1], 21.0 * scale[0], -96.0 * scale[1])
    Lineto_r(0.0 * scale[0], -95.0 * scale[1])
    Lineto_r(-41.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 0.0 * scale[1], -49.0 * scale[0], -
              4.0 * scale[1], -57.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], 9.0 * scale[0], -
              9.0 * scale[1], 55.0 * scale[0], -9.0 * scale[1])
    Curveto_r(38.0 * scale[0], 0.0 * scale[1], 65.0 * scale[0],
              3.0 * scale[1], 59.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 4.0 * scale[1], -8.0 * scale[0],
              18.0 * scale[1], -6.0 * scale[0], 32.0 * scale[1])
    Curveto_r(1.0 * scale[0], 14.0 * scale[1], 5.0 * scale[0],
              84.0 * scale[1], 8.0 * scale[0], 155.0 * scale[1])
    Curveto_r(6.0 * scale[0], 128.0 * scale[1], 5.0 * scale[0],
              131.0 * scale[1], -19.0 * scale[0], 157.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 17.0 * scale[1], -21.0 * scale[0],
              29.0 * scale[1], -14.0 * scale[0], 32.0 * scale[1])
    Curveto_r(15.0 * scale[0], 5.0 * scale[1], -40.0 * scale[0],
              3.0 * scale[1], -113.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(35.0 * scale[0], 1410.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -10.0 *
              scale[0], -8.0 * scale[1], -14.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 2.0 * scale[1], -9.0 * scale[0], -
              159.0 * scale[1], -10.0 * scale[0], -359.0 * scale[1])
    Curveto_r(0.0 * scale[0], -313.0 * scale[1], 1.0 * scale[0], -
              365.0 * scale[1], 14.0 * scale[0], -370.0 * scale[1])
    Curveto_r(10.0 * scale[0], -3.0 * scale[1], 15.0 * scale[0],
              1.0 * scale[1], 15.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], 7.0 * scale[0],
              25.0 * scale[1], 15.0 * scale[0], 34.0 * scale[1])
    Curveto_r(8.0 * scale[0], 8.0 * scale[1], 15.0 * scale[0],
              19.0 * scale[1], 15.0 * scale[0], 25.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -7.0 * scale[0],
              11.0 * scale[1], -15.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0],
              78.0 * scale[1], 2.0 * scale[0], 102.0 * scale[1])
    Curveto_r(15.0 * scale[0], 17.0 * scale[1], 15.0 * scale[0],
              19.0 * scale[1], -3.0 * scale[0], 39.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 22.0 * scale[1], -21.0 * scale[0],
              73.0 * scale[1], -1.0 * scale[0], 98.0 * scale[1])
    Curveto_r(11.0 * scale[0], 14.0 * scale[1], 10.0 * scale[0],
              14.0 * scale[1], -5.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -11.0 * scale[1], -19.0 *
              scale[0], -11.0 * scale[1], -24.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 44.0 * scale[1], -6.0 * scale[0],
              46.0 * scale[1], 207.0 * scale[0], 46.0 * scale[1])
    Curveto_r(111.0 * scale[0], 0.0 * scale[1], 199.0 * scale[0],
              3.0 * scale[1], 196.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 4.0 * scale[1], -93.0 * scale[0],
              7.0 * scale[1], -199.0 * scale[0], 8.0 * scale[1])
    Lineto_r(-193.0 * scale[0], 1.0 * scale[1])
    Lineto_r(-7.0 * scale[0], 50.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 27.0 * scale[1], -5.0 * scale[0],
              51.0 * scale[1], -3.0 * scale[0], 53.0 * scale[1])
    Curveto_r(2.0 * scale[0], 2.0 * scale[1], 20.0 * scale[0], -
              1.0 * scale[1], 41.0 * scale[0], -7.0 * scale[1])
    Curveto_r(21.0 * scale[0], -6.0 * scale[1], 40.0 *
              scale[0], -8.0 * scale[1], 42.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 2.0 * scale[1], -16.0 * scale[0],
              10.0 * scale[1], -42.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 7.0 * scale[1], -46.0 * scale[0],
              16.0 * scale[1], -46.0 * scale[0], 21.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 7.0 * scale[0],
              7.0 * scale[1], 15.0 * scale[0], 3.0 * scale[1])
    Curveto_r(11.0 * scale[0], -4.0 * scale[1], 15.0 * scale[0],
              2.0 * scale[1], 15.0 * scale[0], 27.0 * scale[1])
    Curveto_r(0.0 * scale[0], 25.0 * scale[1], 9.0 * scale[0],
              42.0 * scale[1], 35.0 * scale[0], 67.0 * scale[1])
    Curveto_r(36.0 * scale[0], 35.0 * scale[1], 43.0 * scale[0],
              50.0 * scale[1], 24.0 * scale[0], 50.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              4.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], -4.0 * scale[0], -
              15.0 * scale[1], -17.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-25.0 * scale[0], -12.0 * scale[1], -48.0 *
              scale[0], -52.0 * scale[1], -48.0 * scale[0], -84.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], -3.0 * scale[0], -
              16.0 * scale[1], -7.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -7.0 * scale[0],
              39.0 * scale[1], -8.0 * scale[0], 79.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 103.0 * scale[1], 7.0 * scale[0],
              116.0 * scale[1], 92.0 * scale[0], 121.0 * scale[1])
    Lineto_r(68.0 * scale[0], 3.0 * scale[1])
    Lineto_r(-72.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-40.0 * scale[0], 1.0 * scale[1], -75.0 *
              scale[0], -2.0 * scale[1], -78.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto_r(14.0 * scale[0], -541.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-14.0 * scale[0], -26.0 * scale[1], -29.0 *
              scale[0], -24.0 * scale[1], -29.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 19.0 * scale[1], 4.0 * scale[0],
              23.0 * scale[1], 20.0 * scale[0], 19.0 * scale[1])
    Curveto_r(16.0 * scale[0], -4.0 * scale[1], 18.0 *
              scale[0], -9.0 * scale[1], 9.0 * scale[0], -24.0 * scale[1])
    te.end_fill()
    Moveto_r(-2.0 * scale[0], -140.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-14.0 * scale[0], -23.0 * scale[1], -27.0 *
              scale[0], -15.0 * scale[1], -27.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 21.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 19.0 * scale[0], 12.0 * scale[1])
    Curveto_r(15.0 * scale[0], -9.0 * scale[1], 17.0 * scale[0], -
              15.0 * scale[1], 8.0 * scale[0], -29.0 * scale[1])
    te.end_fill()
    Moveto(338.0 * scale[0], 1413.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(728.0 * scale[0], 1413.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(886.0 * scale[0], 1339.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 12.0 * scale[0], -
              9.0 * scale[1], 21.0 * scale[0], -9.0 * scale[1])
    Curveto_r(19.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              13.0 * scale[1], -12.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 1.0 * scale[1], -13.0 *
              scale[0], -2.0 * scale[1], -9.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(169.0 * scale[0], 1273.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-24.0 * scale[0], -28.0 * scale[1])
    Lineto_r(28.0 * scale[0], 24.0 * scale[1])
    Curveto_r(15.0 * scale[0], 14.0 * scale[1], 27.0 * scale[0],
              26.0 * scale[1], 27.0 * scale[0], 28.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              1.0 * scale[1], -31.0 * scale[0], -24.0 * scale[1])
    te.end_fill()
    Moveto(900.0 * scale[0], 1275.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -12.0 * scale[1], -9.0 *
              scale[0], -15.0 * scale[1], 4.0 * scale[0], -15.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              4.0 * scale[1], 12.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 5.0 * scale[1], 0.0 * scale[0],
              12.0 * scale[1], 6.0 * scale[0], 14.0 * scale[1])
    Curveto_r(8.0 * scale[0], 4.0 * scale[1], 9.0 * scale[0],
              6.0 * scale[1], 2.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 1.0 * scale[1], -17.0 * scale[0], -
              6.0 * scale[1], -24.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(940.0 * scale[0], 1209.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 4.0 * scale[0], -
              28.0 * scale[1], 9.0 * scale[0], -25.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 3.0 * scale[0],
              56.0 * scale[1], -5.0 * scale[0], 56.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              14.0 * scale[1], -4.0 * scale[0], -31.0 * scale[1])
    te.end_fill()
    Moveto(921.0 * scale[0], 1164.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(825.0 * scale[0], 1160.0 * scale[1], x, y)
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
    Moveto(653.0 * scale[0], 1053.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(26.0 * scale[0], -2.0 * scale[1], 67.0 *
              scale[0], -2.0 * scale[1], 90.0 * scale[0], 0.0 * scale[1])
    Curveto_r(23.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              3.0 * scale[1], -48.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-49.0 * scale[0], 0.0 * scale[1], -68.0 *
              scale[0], -1.0 * scale[1], -42.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(820.0 * scale[0], 1050.0 * scale[1], x, y)
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
    Moveto(977.0 * scale[0], 978.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -29.0 * scale[1], -1.0 *
              scale[0], -60.0 * scale[1], 4.0 * scale[0], -68.0 * scale[1])
    Curveto_r(5.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0],
              10.0 * scale[1], 9.0 * scale[0], 53.0 * scale[1])
    Curveto_r(0.0 * scale[0], 37.0 * scale[1], -2.0 * scale[0],
              67.0 * scale[1], -4.0 * scale[0], 67.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0], -
              24.0 * scale[1], -9.0 * scale[0], -52.0 * scale[1])
    te.end_fill()
    Moveto(88.0 * scale[0], 1003.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 9.0 * scale[0], -
              10.0 * scale[1], 6.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -2.0 *
              scale[0], -8.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 14.0 * scale[0], -
              3.0 * scale[1], 17.0 * scale[0], -15.0 * scale[1])
    Curveto_r(4.0 * scale[0], -11.0 * scale[1], 9.0 * scale[0], -
              18.0 * scale[1], 12.0 * scale[0], -15.0 * scale[1])
    Curveto_r(9.0 * scale[0], 8.0 * scale[1], -26.0 * scale[0],
              56.0 * scale[1], -40.0 * scale[0], 55.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -9.0 *
              scale[0], -2.0 * scale[1], 1.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(193.0 * scale[0], 968.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -7.0 * scale[1], -13.0 * scale[0], -
              20.0 * scale[1], -17.0 * scale[0], -28.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -12.0 * scale[1], -4.0 *
              scale[0], -11.0 * scale[1], 6.0 * scale[0], 1.0 * scale[1])
    Curveto_r(8.0 * scale[0], 10.0 * scale[1], 20.0 * scale[0],
              14.0 * scale[1], 33.0 * scale[0], 9.0 * scale[1])
    Curveto_r(18.0 * scale[0], -6.0 * scale[1], 18.0 *
              scale[0], -7.0 * scale[1], 1.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -8.0 * scale[1], -18.0 * scale[0], -
              19.0 * scale[1], -14.0 * scale[0], -51.0 * scale[1])
    Curveto_r(2.0 * scale[0], -23.0 * scale[1], -1.0 * scale[0], -
              44.0 * scale[1], -7.0 * scale[0], -46.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -2.0 * scale[1], -3.0 *
              scale[0], -5.0 * scale[1], 6.0 * scale[0], -5.0 * scale[1])
    Curveto_r(9.0 * scale[0], -1.0 * scale[1], 20.0 * scale[0], -
              8.0 * scale[1], 23.0 * scale[0], -17.0 * scale[1])
    Curveto_r(4.0 * scale[0], -10.0 * scale[1], 15.0 * scale[0], -
              14.0 * scale[1], 33.0 * scale[0], -12.0 * scale[1])
    Curveto_r(24.0 * scale[0], 3.0 * scale[1], 29.0 * scale[0],
              8.0 * scale[1], 31.0 * scale[0], 37.0 * scale[1])
    Curveto_r(8.0 * scale[0], 77.0 * scale[1], -19.0 * scale[0],
              119.0 * scale[1], -77.0 * scale[0], 122.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -10.0 *
              scale[0], 3.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(15.0 * scale[0], 7.0 * scale[1], 16.0 * scale[0],
              9.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 1.0 * scale[1], -21.0 * scale[0], -
              5.0 * scale[1], -26.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(850.0 * scale[0], 947.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 9.0 * scale[0], -
              14.0 * scale[1], 20.0 * scale[0], -27.0 * scale[1])
    Curveto_r(22.0 * scale[0], -26.0 * scale[1], 27.0 *
              scale[0], -15.0 * scale[1], 6.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 15.0 * scale[1], -26.0 * scale[0],
              23.0 * scale[1], -26.0 * scale[0], 14.0 * scale[1])
    te.end_fill()
    Moveto(102.0 * scale[0], 902.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -20.0 * scale[1], -21.0 *
              scale[0], -26.0 * scale[1], -10.0 * scale[0], -36.0 * scale[1])
    Curveto_r(7.0 * scale[0], -6.0 * scale[1], 9.0 * scale[0], -
              7.0 * scale[1], 5.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 5.0 * scale[1], 3.0 * scale[0],
              20.0 * scale[1], 15.0 * scale[0], 33.0 * scale[1])
    Curveto_r(12.0 * scale[0], 12.0 * scale[1], 20.0 * scale[0],
              24.0 * scale[1], 17.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 2.0 * scale[1], -14.0 * scale[0], -
              8.0 * scale[1], -27.0 * scale[0], -21.0 * scale[1])
    te.end_fill()
    Moveto(710.0 * scale[0], 915.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -13.0 * scale[1], -10.0 *
              scale[0], -14.0 * scale[1], 4.0 * scale[0], -9.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 16.0 * scale[0],
              10.0 * scale[1], 16.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], -6.0 * scale[0],
              11.0 * scale[1], -20.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(799.0 * scale[0], 911.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-21.0 * scale[0], -6.0 * scale[1], -59.0 * scale[0], -
              54.0 * scale[1], -59.0 * scale[0], -73.0 * scale[1])
    Curveto_r(0.0 * scale[0], -21.0 * scale[1], 39.0 * scale[0], -
              62.0 * scale[1], 63.0 * scale[0], -66.0 * scale[1])
    Curveto_r(10.0 * scale[0], -2.0 * scale[1], 31.0 * scale[0],
              11.0 * scale[1], 47.0 * scale[0], 29.0 * scale[1])
    Curveto_r(33.0 * scale[0], 34.0 * scale[1], 33.0 * scale[0],
              35.0 * scale[1], 19.0 * scale[0], 64.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 17.0 * scale[1], -8.0 * scale[0],
              16.0 * scale[1], -4.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], -15.0 * scale[1], 1.0 * scale[0], -
              30.0 * scale[1], -5.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -10.0 * scale[0],
              3.0 * scale[1], -10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -4.0 * scale[0],
              19.0 * scale[1], -12.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -5.0 * scale[1], -9.0 *
              scale[0], -2.0 * scale[1], 1.0 * scale[0], 9.0 * scale[1])
    Curveto_r(7.0 * scale[0], 9.0 * scale[1], 10.0 * scale[0],
              17.0 * scale[1], 5.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -2.0 * scale[0],
              5.0 * scale[1], 6.0 * scale[0], 10.0 * scale[1])
    Curveto_r(11.0 * scale[0], 7.0 * scale[1], 11.0 * scale[0],
              10.0 * scale[1], 2.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0],
              4.0 * scale[1], -8.0 * scale[0], 8.0 * scale[1])
    Curveto_r(5.0 * scale[0], 8.0 * scale[1], -23.0 * scale[0],
              10.0 * scale[1], -45.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto_r(41.0 * scale[0], -14.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], -9.0 * scale[0], -
              12.0 * scale[1], -19.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -17.0 * scale[1], -19.0 *
              scale[0], -17.0 * scale[1], -16.0 * scale[0], 1.0 * scale[1])
    Curveto_r(2.0 * scale[0], 10.0 * scale[1], 4.0 * scale[0],
              19.0 * scale[1], 4.0 * scale[0], 21.0 * scale[1])
    Curveto_r(1.0 * scale[0], 3.0 * scale[1], 31.0 * scale[0],
              2.0 * scale[1], 31.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(161.0 * scale[0], 894.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(893.0 * scale[0], 845.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -22.0 * scale[1], 2.0 * scale[0], -
              30.0 * scale[1], 4.0 * scale[0], -17.0 * scale[1])
    Curveto_r(2.0 * scale[0], 12.0 * scale[1], 2.0 * scale[0],
              30.0 * scale[1], 0.0 * scale[0], 40.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -4.0 * scale[0], -23.0 * scale[1])
    te.end_fill()
    Moveto(161.0 * scale[0], 834.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(329.0 * scale[0], 833.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -21.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(116.0 * scale[0], 827.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0], -
              15.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 0.0 * scale[0],
              11.0 * scale[1], -7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              8.0 * scale[1], -5.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(176.0 * scale[0], 797.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0], -
              15.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 0.0 * scale[0],
              11.0 * scale[1], -7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              8.0 * scale[1], -5.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(103.0 * scale[0], 765.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-22.0 * scale[0], -21.0 * scale[1], -22.0 *
              scale[0], -21.0 * scale[1], -3.0 * scale[0], -51.0 * scale[1])
    Curveto_r(11.0 * scale[0], -16.0 * scale[1], 20.0 * scale[0], -
              24.0 * scale[1], 20.0 * scale[0], -18.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -5.0 * scale[0],
              15.0 * scale[1], -11.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 8.0 * scale[1], -6.0 * scale[0],
              18.0 * scale[1], 6.0 * scale[0], 37.0 * scale[1])
    Curveto_r(22.0 * scale[0], 34.0 * scale[1], 17.0 * scale[0],
              38.0 * scale[1], -12.0 * scale[0], 11.0 * scale[1])
    te.end_fill()
    Moveto(859.0 * scale[0], 753.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -21.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(125.0 * scale[0], 670.0 * scale[1], x, y)
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
    Moveto(116.0 * scale[0], 633.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(169.0 * scale[0], 633.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -21.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(201.0 * scale[0], 584.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(201.0 * scale[0], 534.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(631.0 * scale[0], 537.0 * scale[1], x, y)
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
    Moveto(627.0 * scale[0], 455.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -12.0 * scale[1], -16.0 *
              scale[0], -13.0 * scale[1], -1.0 * scale[0], -19.0 * scale[1])
    Curveto_r(21.0 * scale[0], -8.0 * scale[1], 36.0 * scale[0],
              5.0 * scale[1], 26.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 8.0 * scale[1], -12.0 * scale[0],
              8.0 * scale[1], -25.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(396.0 * scale[0], 452.0 * scale[1], x, y)
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
    Moveto(419.0 * scale[0], 403.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(16.0 * scale[0], 13.0 * scale[1], 21.0 * scale[0],
              21.0 * scale[1], 13.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              8.0 * scale[1], -17.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(870.0 * scale[0], 410.0 * scale[1], x, y)
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
    Moveto(804.0 * scale[0], 386.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -20.0 * scale[1], -9.0 *
              scale[0], -23.0 * scale[1], 2.0 * scale[0], -19.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 14.0 * scale[0],
              14.0 * scale[1], 14.0 * scale[0], 24.0 * scale[1])
    Curveto_r(0.0 * scale[0], 25.0 * scale[1], -3.0 * scale[0],
              24.0 * scale[1], -16.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(210.0 * scale[0], 396.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(255.0 * scale[0], 340.0 * scale[1], x, y)
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
    Moveto(213.0 * scale[0], 301.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -12.0 * scale[1], -26.0 *
              scale[0], -21.0 * scale[1], -31.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              16.0 * scale[1], -16.0 * scale[0], -35.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -21.0 * scale[1], -13.0 * scale[0], -
              35.0 * scale[1], -21.0 * scale[0], -35.0 * scale[1])
    Curveto_r(-29.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              76.0 * scale[1], 17.0 * scale[0], -83.0 * scale[1])
    Curveto_r(11.0 * scale[0], -3.0 * scale[1], 17.0 * scale[0], -
              10.0 * scale[1], 13.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], -12.0 *
              scale[0], -9.0 * scale[1], -18.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              0.0 * scale[1], 4.0 * scale[0], -8.0 * scale[1])
    Curveto_r(9.0 * scale[0], -7.0 * scale[1], 14.0 * scale[0], -
              19.0 * scale[1], 12.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -17.0 * scale[1], 14.0 *
              scale[0], -17.0 * scale[1], 20.0 * scale[0], 0.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 6.0 * scale[0],
              5.0 * scale[1], 6.0 * scale[0], -5.0 * scale[1])
    Curveto_r(1.0 * scale[0], -23.0 * scale[1], 18.0 *
              scale[0], -23.0 * scale[1], 24.0 * scale[0], 0.0 * scale[1])
    Curveto_r(4.0 * scale[0], 16.0 * scale[1], 5.0 * scale[0],
              16.0 * scale[1], 6.0 * scale[0], 0.0 * scale[1])
    Curveto_r(1.0 * scale[0], -12.0 * scale[1], 9.0 * scale[0], -
              18.0 * scale[1], 26.0 * scale[0], -18.0 * scale[1])
    Curveto_r(24.0 * scale[0], 0.0 * scale[1], 25.0 * scale[0],
              2.0 * scale[1], 27.0 * scale[0], 73.0 * scale[1])
    Curveto_r(0.0 * scale[0], 39.0 * scale[1], 0.0 * scale[0],
              80.0 * scale[1], 0.0 * scale[0], 90.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 10.0 * scale[1], 3.0 * scale[0],
              15.0 * scale[1], 8.0 * scale[0], 12.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 10.0 *
              scale[0], -1.0 * scale[1], 10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              11.0 * scale[1], -10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0],
              6.0 * scale[1], -9.0 * scale[0], 13.0 * scale[1])
    Curveto_r(3.0 * scale[0], 26.0 * scale[1], -2.0 * scale[0],
              35.0 * scale[1], -18.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -2.0 * scale[1], -20.0 * scale[0],
              5.0 * scale[1], -23.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 19.0 * scale[1], -6.0 * scale[0],
              19.0 * scale[1], -27.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(776.0 * scale[0], 312.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -3.0 * scale[0], -
              21.0 * scale[1], 0.0 * scale[0], -37.0 * scale[1])
    Curveto_r(4.0 * scale[0], -21.0 * scale[1], 2.0 * scale[0], -
              26.0 * scale[1], -10.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -17.0 * scale[0], -
              1.0 * scale[1], -20.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -1.0 * scale[0], -
              14.0 * scale[1], 4.0 * scale[0], -14.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0], -
              8.0 * scale[1], 8.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -10.0 * scale[1], 0.0 * scale[0], -
              51.0 * scale[1], 0.0 * scale[0], -90.0 * scale[1])
    Lineto_r(2.0 * scale[0], -73.0 * scale[1])
    Lineto_r(40.0 * scale[0], 0.0 * scale[1])
    Curveto_r(33.0 * scale[0], 0.0 * scale[1], 40.0 * scale[0],
              3.0 * scale[1], 40.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], 7.0 * scale[0],
              20.0 * scale[1], 15.0 * scale[0], 20.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              9.0 * scale[1], 15.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], 4.0 * scale[0],
              20.0 * scale[1], 9.0 * scale[0], 20.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0],
              24.0 * scale[1], 8.0 * scale[0], 53.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 56.0 * scale[1], -20.0 * scale[0],
              87.0 * scale[1], -50.0 * scale[0], 87.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -12.0 * scale[0], 10.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], 1.0 * scale[0],
              17.0 * scale[1], -5.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 17.0 * scale[1], -36.0 * scale[0],
              20.0 * scale[1], -44.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(321.0 * scale[0], 307.0 * scale[1], x, y)
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
    Moveto(43.0 * scale[0], 240.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -30.0 * scale[1], 2.0 * scale[0], -
              43.0 * scale[1], 4.0 * scale[0], -27.0 * scale[1])
    Curveto_r(2.0 * scale[0], 15.0 * scale[1], 2.0 * scale[0],
              39.0 * scale[1], 0.0 * scale[0], 55.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 15.0 * scale[1], -4.0 * scale[0],
              2.0 * scale[1], -4.0 * scale[0], -28.0 * scale[1])
    te.end_fill()
    Moveto(610.0 * scale[0], 260.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -11.0 * scale[1], -30.0 *
              scale[0], -19.0 * scale[1], -24.0 * scale[0], -20.0 * scale[1])
    Curveto_r(15.0 * scale[0], 0.0 * scale[1], 64.0 * scale[0],
              24.0 * scale[1], 64.0 * scale[0], 33.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], 1.0 * scale[0],
              9.0 * scale[1], -40.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(336.0 * scale[0], 253.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(51.0 * scale[0], 104.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(86.0 * scale[0], 87.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0], -
              15.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 0.0 * scale[0],
              11.0 * scale[1], -7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              8.0 * scale[1], -5.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(116.0 * scale[0], 87.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0], -
              15.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 0.0 * scale[0],
              11.0 * scale[1], -7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              8.0 * scale[1], -5.0 * scale[0], -6.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#839288')
    te.end_fill()
    Moveto(53.0 * scale[0], 1423.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(15.0 * scale[0], -2.0 * scale[1], 37.0 *
              scale[0], -2.0 * scale[1], 50.0 * scale[0], 0.0 * scale[1])
    Curveto_r(12.0 * scale[0], 2.0 * scale[1], 0.0 * scale[0],
              4.0 * scale[1], -28.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-27.0 * scale[0], 0.0 * scale[1], -38.0 *
              scale[0], -2.0 * scale[1], -22.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(562.0 * scale[0], 1372.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -4.0 * scale[1], -3.0 * scale[0], -
              16.0 * scale[1], -9.0 * scale[0], -28.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -18.0 * scale[1], -9.0 *
              scale[0], -20.0 * scale[1], 10.0 * scale[0], -19.0 * scale[1])
    Curveto_r(26.0 * scale[0], 2.0 * scale[1], 36.0 * scale[0],
              39.0 * scale[1], 13.0 * scale[0], 48.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 4.0 * scale[1], -15.0 * scale[0],
              3.0 * scale[1], -14.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(410.0 * scale[0], 1346.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -24.0 * scale[1], 2.0 * scale[0], -
              26.0 * scale[1], 21.0 * scale[0], -16.0 * scale[1])
    Curveto_r(11.0 * scale[0], 7.0 * scale[1], 19.0 * scale[0],
              13.0 * scale[1], 17.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 1.0 * scale[1], -11.0 * scale[0],
              8.0 * scale[1], -20.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 12.0 * scale[1], -18.0 * scale[0],
              11.0 * scale[1], -18.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(102.0 * scale[0], 1287.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-22.0 * scale[0], -23.0 * scale[1], -32.0 *
              scale[0], -43.0 * scale[1], -32.0 * scale[0], -65.0 * scale[1])
    Curveto_r(0.0 * scale[0], -29.0 * scale[1], 3.0 * scale[0], -
              32.0 * scale[1], 31.0 * scale[0], -32.0 * scale[1])
    Curveto_r(26.0 * scale[0], 0.0 * scale[1], 31.0 * scale[0], -
              3.0 * scale[1], 26.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -16.0 * scale[1], 0.0 * scale[0], -
              20.0 * scale[1], 19.0 * scale[0], -20.0 * scale[1])
    Curveto_r(17.0 * scale[0], 0.0 * scale[1], 24.0 * scale[0],
              6.0 * scale[1], 24.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], 5.0 * scale[0],
              20.0 * scale[1], 10.0 * scale[0], 20.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              9.0 * scale[1], 10.0 * scale[0], 19.0 * scale[1])
    Curveto_r(0.0 * scale[0], 22.0 * scale[1], -30.0 * scale[0],
              35.0 * scale[1], -60.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-29.0 * scale[0], -9.0 * scale[1], -25.0 * scale[0],
              7.0 * scale[1], 10.0 * scale[0], 40.0 * scale[1])
    Curveto_r(22.0 * scale[0], 21.0 * scale[1], 27.0 * scale[0],
              31.0 * scale[1], 18.0 * scale[0], 37.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 12.0 * scale[1], -21.0 * scale[0],
              11.0 * scale[1], -56.0 * scale[0], -25.0 * scale[1])
    te.end_fill()
    Moveto_r(48.0 * scale[0], 20.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], -10.0 * scale[0], -
              12.0 * scale[1], -22.0 * scale[0], -23.0 * scale[1])
    Lineto_r(-23.0 * scale[0], -19.0 * scale[1])
    Lineto_r(19.0 * scale[0], 23.0 * scale[1])
    Curveto_r(18.0 * scale[0], 21.0 * scale[1], 26.0 * scale[0],
              27.0 * scale[1], 26.0 * scale[0], 19.0 * scale[1])
    te.end_fill()
    Moveto(830.0 * scale[0], 1284.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-40.0 * scale[0], -46.0 * scale[1], -39.0 *
              scale[0], -87.0 * scale[1], 3.0 * scale[0], -92.0 * scale[1])
    Curveto_r(19.0 * scale[0], -2.0 * scale[1], 27.0 * scale[0], -
              9.0 * scale[1], 27.0 * scale[0], -23.0 * scale[1])
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], 7.0 * scale[0], -
              19.0 * scale[1], 20.0 * scale[0], -19.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0],
              7.0 * scale[1], 20.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], 5.0 * scale[0],
              20.0 * scale[1], 11.0 * scale[0], 20.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              10.0 * scale[1], 7.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 19.0 * scale[1], -9.0 * scale[0],
              22.0 * scale[1], -40.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -1.0 * scale[1], -38.0 * scale[0],
              2.0 * scale[1], -38.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], 13.0 * scale[0],
              20.0 * scale[1], 30.0 * scale[0], 36.0 * scale[1])
    Curveto_r(16.0 * scale[0], 15.0 * scale[1], 27.0 * scale[0],
              32.0 * scale[1], 24.0 * scale[0], 37.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 17.0 * scale[1], -33.0 * scale[0],
              7.0 * scale[1], -64.0 * scale[0], -28.0 * scale[1])
    te.end_fill()
    Moveto_r(50.0 * scale[0], 19.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -13.0 * scale[0], -
              17.0 * scale[1], -28.0 * scale[0], -27.0 * scale[1])
    Lineto_r(-27.0 * scale[0], -19.0 * scale[1])
    Lineto_r(24.0 * scale[0], 26.0 * scale[1])
    Curveto_r(26.0 * scale[0], 28.0 * scale[1], 31.0 * scale[0],
              32.0 * scale[1], 31.0 * scale[0], 20.0 * scale[1])
    te.end_fill()
    Moveto(434.0 * scale[0], 1277.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -16.0 * scale[1], -29.0 *
              scale[0], -37.0 * scale[1], -34.0 * scale[0], -70.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -26.0 * scale[1], -5.0 * scale[0], -
              45.0 * scale[1], -2.0 * scale[0], -42.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 11.0 * scale[0], -
              4.0 * scale[1], 19.0 * scale[0], -15.0 * scale[1])
    Curveto_r(8.0 * scale[0], -11.0 * scale[1], 20.0 * scale[0], -
              20.0 * scale[1], 26.0 * scale[0], -20.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0],
              3.0 * scale[1], -1.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 4.0 * scale[1], -13.0 * scale[0],
              11.0 * scale[1], -13.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              13.0 * scale[1], -6.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 22.0 * scale[1], 31.0 * scale[0],
              100.0 * scale[1], 54.0 * scale[0], 106.0 * scale[1])
    Curveto_r(37.0 * scale[0], 10.0 * scale[1], 85.0 * scale[0], -
              50.0 * scale[1], 62.0 * scale[0], -78.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -10.0 * scale[1], -8.0 *
              scale[0], -14.0 * scale[1], 0.0 * scale[0], -14.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              3.0 * scale[1], 10.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -37.0 * scale[1], 28.0 * scale[0], -
              47.0 * scale[1], 35.0 * scale[0], -10.0 * scale[1])
    Curveto_r(11.0 * scale[0], 52.0 * scale[1], 12.0 * scale[0],
              86.0 * scale[1], 2.0 * scale[0], 80.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -4.0 * scale[1], -7.0 * scale[0],
              1.0 * scale[1], -3.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 9.0 * scale[1], 1.0 * scale[0],
              19.0 * scale[1], -5.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(4.0 * scale[0], -7.0 * scale[1], -1.0 * scale[0], -
              10.0 * scale[1], -14.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 1.0 * scale[1], -22.0 * scale[0],
              7.0 * scale[1], -24.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 22.0 * scale[1], -72.0 * scale[0],
              15.0 * scale[1], -102.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto_r(140.0 * scale[0], -43.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -24.0 * scale[1], 2.0 * scale[0], -
              26.0 * scale[1], -12.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 11.0 * scale[1], -8.0 * scale[0],
              20.0 * scale[1], -3.0 * scale[0], 20.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0], -
              7.0 * scale[1], 15.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(888.0 * scale[0], 1253.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(52.0 * scale[0], 1225.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(123.0 * scale[0], 1133.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(460.0 * scale[0], 1119.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -17.0 * scale[1], -10.0 *
              scale[0], -20.0 * scale[1], 2.0 * scale[0], -13.0 * scale[1])
    Curveto_r(7.0 * scale[0], 5.0 * scale[1], 18.0 * scale[0],
              9.0 * scale[1], 23.0 * scale[0], 9.0 * scale[1])
    Curveto_r(16.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0],
              20.0 * scale[1], 1.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 2.0 * scale[1], -20.0 * scale[0], -
              7.0 * scale[1], -26.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(524.0 * scale[0], 1128.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -5.0 * scale[1], -3.0 * scale[0], -
              12.0 * scale[1], 0.0 * scale[0], -15.0 * scale[1])
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], 6.0 *
              scale[0], -1.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], 4.0 * scale[0],
              10.0 * scale[1], 9.0 * scale[0], 6.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 12.0 *
              scale[0], -2.0 * scale[1], 15.0 * scale[0], 3.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0], -
              4.0 * scale[1], -20.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(483.0 * scale[0], 1093.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(685.0 * scale[0], 830.0 * scale[1], x, y)
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
    Moveto(255.0 * scale[0], 760.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(740.0 * scale[0], 756.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 7.0 * scale[0], -
              7.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 12.0 *
              scale[0], -2.0 * scale[1], 9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], -25.0 * scale[0],
              14.0 * scale[1], -25.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(224.0 * scale[0], 655.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -4.0 * scale[0], -
              20.0 * scale[1], -2.0 * scale[0], -27.0 * scale[1])
    Curveto_r(3.0 * scale[0], -7.0 * scale[1], 7.0 * scale[0], -
              1.0 * scale[1], 10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(6.0 * scale[0], 29.0 * scale[1], 1.0 * scale[0],
              36.0 * scale[1], -8.0 * scale[0], 12.0 * scale[1])
    te.end_fill()
    Moveto(807.0 * scale[0], 590.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -36.0 * scale[1], 7.0 * scale[0], -
              87.0 * scale[1], 6.0 * scale[0], -115.0 * scale[1])
    Lineto_r(0.0 * scale[0], -50.0 * scale[1])
    Lineto_r(9.0 * scale[0], 51.0 * scale[1])
    Curveto_r(8.0 * scale[0], 40.0 * scale[1], 7.0 * scale[0],
              66.0 * scale[1], -5.0 * scale[0], 115.0 * scale[1])
    Lineto_r(-16.0 * scale[0], 64.0 * scale[1])
    Lineto_r(6.0 * scale[0], -65.0 * scale[1])
    te.end_fill()
    Moveto(212.0 * scale[0], 560.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 2.0 * scale[0], -
              27.0 * scale[1], 5.0 * scale[0], -17.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              25.0 * scale[1], 0.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(386.0 * scale[0], 541.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -5.0 * scale[1], 3.0 * scale[0], -
              7.0 * scale[1], 14.0 * scale[0], -4.0 * scale[1])
    Curveto_r(23.0 * scale[0], 6.0 * scale[1], 26.0 * scale[0],
              13.0 * scale[1], 6.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0], -
              4.0 * scale[1], -20.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(648.0 * scale[0], 534.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -8.0 * scale[1], 23.0 * scale[0], -
              25.0 * scale[1], 23.0 * scale[0], -37.0 * scale[1])
    Curveto_r(1.0 * scale[0], -18.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 6.0 * scale[0], -4.0 * scale[1])
    Curveto_r(5.0 * scale[0], 19.0 * scale[1], -22.0 * scale[0],
              57.0 * scale[1], -41.0 * scale[0], 57.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], 0.0 * scale[0], -
              7.0 * scale[1], 12.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(599.0 * scale[0], 523.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(16.0 * scale[0], 13.0 * scale[1], 21.0 * scale[0],
              21.0 * scale[1], 13.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              8.0 * scale[1], -17.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(364.0 * scale[0], 505.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -4.0 * scale[0], -
              20.0 * scale[1], -2.0 * scale[0], -27.0 * scale[1])
    Curveto_r(3.0 * scale[0], -7.0 * scale[1], 7.0 * scale[0], -
              1.0 * scale[1], 10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(6.0 * scale[0], 29.0 * scale[1], 1.0 * scale[0],
              36.0 * scale[1], -8.0 * scale[0], 12.0 * scale[1])
    te.end_fill()
    Moveto(582.0 * scale[0], 480.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(212.0 * scale[0], 445.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(691.0 * scale[0], 431.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], -9.0 * scale[0], -
              34.0 * scale[1], -18.0 * scale[0], -45.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -20.0 * scale[1], -17.0 *
              scale[0], -20.0 * scale[1], 6.0 * scale[0], 0.0 * scale[1])
    Curveto_r(15.0 * scale[0], 14.0 * scale[1], 21.0 * scale[0],
              29.0 * scale[1], 18.0 * scale[0], 45.0 * scale[1])
    Lineto_r(-4.0 * scale[0], 24.0 * scale[1])
    Lineto_r(-2.0 * scale[0], -24.0 * scale[1])
    te.end_fill()
    Moveto(340.0 * scale[0], 424.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 38.0 * scale[0], -
              46.0 * scale[1], 57.0 * scale[0], -41.0 * scale[1])
    Curveto_r(15.0 * scale[0], 4.0 * scale[1], 14.0 * scale[0],
              5.0 * scale[1], -4.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -29.0 * scale[0],
              11.0 * scale[1], -37.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 12.0 * scale[1], -16.0 * scale[0],
              18.0 * scale[1], -16.0 * scale[0], 12.0 * scale[1])
    te.end_fill()
    Moveto(610.0 * scale[0], 405.0 * scale[1], x, y)
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
    Moveto(796.0 * scale[0], 405.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -12.0 * scale[0], -
              15.0 * scale[1], -21.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              5.0 * scale[1], -15.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0], -
              9.0 * scale[1], -12.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 5.0 * scale[1], -51.0 * scale[0], -
              28.0 * scale[1], -61.0 * scale[0], -56.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -10.0 * scale[1], -13.0 * scale[0], -
              16.0 * scale[1], -22.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -17.0 * scale[0],
              1.0 * scale[1], -20.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -5.0 * scale[1], -10.0 *
              scale[0], -7.0 * scale[1], -14.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 2.0 * scale[1], -19.0 * scale[0], -
              4.0 * scale[1], -31.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -11.0 * scale[1], -30.0 *
              scale[0], -20.0 * scale[1], -38.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0],
              3.0 * scale[1], 4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(18.0 * scale[0], 14.0 * scale[1], 17.0 * scale[0],
              15.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -7.0 * scale[1], -25.0 * scale[0], -
              16.0 * scale[1], -22.0 * scale[0], -20.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              9.0 * scale[1], -11.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0],
              5.0 * scale[1], -10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              10.0 * scale[1], -4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -18.0 * scale[0],
              3.0 * scale[1], -28.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 5.0 * scale[1], -16.0 * scale[0],
              4.0 * scale[1], -3.0 * scale[0], -6.0 * scale[1])
    Curveto_r(13.0 * scale[0], -9.0 * scale[1], 12.0 * scale[0], -
              11.0 * scale[1], -5.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 2.0 * scale[1], -20.0 * scale[0],
              8.0 * scale[1], -20.0 * scale[0], 13.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -6.0 * scale[0],
              19.0 * scale[1], -14.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 15.0 * scale[1], -11.0 * scale[0],
              15.0 * scale[1], -7.0 * scale[0], 3.0 * scale[1])
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], -2.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -74.0 * scale[0],
              49.0 * scale[1], -66.0 * scale[0], 56.0 * scale[1])
    Curveto_r(2.0 * scale[0], 3.0 * scale[1], -8.0 * scale[0],
              4.0 * scale[1], -24.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -2.0 * scale[1], -35.0 * scale[0],
              3.0 * scale[1], -47.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 11.0 * scale[1], -22.0 * scale[0],
              17.0 * scale[1], -26.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -9.0 *
              scale[0], -1.0 * scale[1], -9.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -9.0 * scale[0],
              15.0 * scale[1], -21.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 11.0 * scale[1], -20.0 * scale[0],
              10.0 * scale[1], 3.0 * scale[0], -20.0 * scale[1])
    Curveto_r(12.0 * scale[0], -18.0 * scale[1], 43.0 * scale[0], -
              43.0 * scale[1], 68.0 * scale[0], -56.0 * scale[1])
    Curveto_r(25.0 * scale[0], -13.0 * scale[1], 52.0 * scale[0], -
              28.0 * scale[1], 60.0 * scale[0], -32.0 * scale[1])
    Curveto_r(100.0 * scale[0], -55.0 * scale[1], 149.0 *
              scale[0], -62.0 * scale[1], 215.0 * scale[0], -33.0 * scale[1])
    Curveto_r(54.0 * scale[0], 24.0 * scale[1], 91.0 * scale[0],
              27.0 * scale[1], 99.0 * scale[0], 9.0 * scale[1])
    Curveto_r(3.0 * scale[0], -7.0 * scale[1], 4.0 *
              scale[0], -4.0 * scale[1], 1.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 15.0 * scale[1], 11.0 * scale[0],
              33.0 * scale[1], 60.0 * scale[0], 74.0 * scale[1])
    Curveto_r(36.0 * scale[0], 29.0 * scale[1], 65.0 * scale[0],
              58.0 * scale[1], 65.0 * scale[0], 62.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -7.0 * scale[0],
              11.0 * scale[1], -14.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(685.0 * scale[0], 230.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -15.0 * scale[1], 1.0 * scale[0], -
              22.0 * scale[1], -17.0 * scale[0], -29.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -5.0 * scale[1], -28.0 *
              scale[0], -5.0 * scale[1], -33.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -70.0 * scale[0],
              10.0 * scale[1], -142.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-72.0 * scale[0], 3.0 * scale[1], -136.0 * scale[0],
              7.0 * scale[1], -141.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 9.0 * scale[1], -44.0 * scale[0], -
              37.0 * scale[1], -37.0 * scale[0], -55.0 * scale[1])
    Curveto_r(5.0 * scale[0], -14.0 * scale[1], 28.0 * scale[0], -
              15.0 * scale[1], 197.0 * scale[0], -8.0 * scale[1])
    Curveto_r(26.0 * scale[0], 1.0 * scale[1], 65.0 * scale[0], -
              4.0 * scale[1], 87.0 * scale[0], -11.0 * scale[1])
    Curveto_r(24.0 * scale[0], -8.0 * scale[1], 50.0 * scale[0], -
              10.0 * scale[1], 68.0 * scale[0], -5.0 * scale[1])
    Curveto_r(15.0 * scale[0], 5.0 * scale[1], 33.0 * scale[0],
              7.0 * scale[1], 40.0 * scale[0], 6.0 * scale[1])
    Curveto_r(21.0 * scale[0], -3.0 * scale[1], 24.0 * scale[0],
              17.0 * scale[1], 7.0 * scale[0], 58.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 41.0 * scale[1], -41.0 * scale[0],
              59.0 * scale[1], -29.0 * scale[0], 21.0 * scale[1])
    te.end_fill()
    Moveto(302.0 * scale[0], 135.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -16.0 * scale[1], 9.0 * scale[0], -
              50.0 * scale[1], 21.0 * scale[0], -75.0 * scale[1])
    Curveto_r(19.0 * scale[0], -39.0 * scale[1], 26.0 * scale[0], -
              45.0 * scale[1], 57.0 * scale[0], -47.0 * scale[1])
    Lineto_r(35.0 * scale[0], -2.0 * scale[1])
    Lineto_r(-40.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-40.0 * scale[0], 18.0 * scale[1], -53.0 * scale[0],
              40.0 * scale[1], -69.0 * scale[0], 116.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 12.0 * scale[1], -4.0 * scale[0],
              8.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(732.0 * scale[0], 130.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(60.0 * scale[0], 104.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0], -
              12.0 * scale[1], 15.0 * scale[0], -20.0 * scale[1])
    Curveto_r(16.0 * scale[0], -17.0 * scale[1], 18.0 *
              scale[0], -14.0 * scale[1], 9.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 15.0 * scale[1], -24.0 * scale[0],
              23.0 * scale[1], -24.0 * scale[0], 10.0 * scale[1])
    te.end_fill()
    Moveto(706.0 * scale[0], 43.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -11.0 * scale[1], -17.0 * scale[0], -
              20.0 * scale[1], -33.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-38.0 * scale[0], -3.0 * scale[1], -42.0 *
              scale[0], -12.0 * scale[1], -5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(21.0 * scale[0], 0.0 * scale[1], 35.0 * scale[0],
              7.0 * scale[1], 42.0 * scale[0], 21.0 * scale[1])
    Curveto_r(7.0 * scale[0], 11.0 * scale[1], 9.0 * scale[0],
              23.0 * scale[1], 7.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 2.0 * scale[1], -8.0 * scale[0], -
              4.0 * scale[1], -11.0 * scale[0], -14.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#745c29')
    te.end_fill()
    Moveto(665.0 * scale[0], 1419.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-23.0 * scale[0], -6.0 * scale[1], -15.0 *
              scale[0], -7.0 * scale[1], 30.0 * scale[0], -5.0 * scale[1])
    Curveto_r(33.0 * scale[0], 2.0 * scale[1], 54.0 * scale[0],
              2.0 * scale[1], 46.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -6.0 * scale[1], 91.0 * scale[0], -
              43.0 * scale[1], 124.0 * scale[0], -43.0 * scale[1])
    Curveto_r(32.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              19.0 * scale[1], -40.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -1.0 * scale[1], -22.0 *
              scale[0], -3.0 * scale[1], -12.0 * scale[0], -6.0 * scale[1])
    Curveto_r(23.0 * scale[0], -6.0 * scale[1], 22.0 * scale[0], -
              11.0 * scale[1], -8.0 * scale[0], -39.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -13.0 * scale[1], -25.0 *
              scale[0], -26.0 * scale[1], -25.0 * scale[0], -30.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], -8.0 * scale[0], -
              13.0 * scale[1], -17.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -8.0 * scale[1], -13.0 *
              scale[0], -13.0 * scale[1], -5.0 * scale[0], -14.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0], -
              7.0 * scale[1], 12.0 * scale[0], -15.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 5.0 * scale[0], -
              15.0 * scale[1], 11.0 * scale[0], -15.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              9.0 * scale[1], 5.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 17.0 * scale[1], 5.0 * scale[0],
              34.0 * scale[1], 39.0 * scale[0], 70.0 * scale[1])
    Curveto_r(25.0 * scale[0], 28.0 * scale[1], 46.0 * scale[0],
              43.0 * scale[1], 50.0 * scale[0], 37.0 * scale[1])
    Curveto_r(5.0 * scale[0], -8.0 * scale[1], 11.0 *
              scale[0], -8.0 * scale[1], 20.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 8.0 * scale[1], 15.0 * scale[0],
              8.0 * scale[1], 20.0 * scale[0], 0.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 3.0 * scale[0], -
              10.0 * scale[1], -2.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -1.0 * scale[0], -
              5.0 * scale[1], 7.0 * scale[0], -10.0 * scale[1])
    Curveto_r(13.0 * scale[0], -9.0 * scale[1], 13.0 * scale[0], -
              11.0 * scale[1], 0.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -9.0 * scale[1], -13.0 *
              scale[0], -10.0 * scale[1], 0.0 * scale[0], -10.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0], -
              3.0 * scale[1], 5.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -15.0 * scale[1], -13.0 *
              scale[0], -28.0 * scale[1], 16.0 * scale[0], -24.0 * scale[1])
    Curveto_r(29.0 * scale[0], 4.0 * scale[1], 29.0 * scale[0],
              4.0 * scale[1], 26.0 * scale[0], 66.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 74.0 * scale[1], -19.0 * scale[0],
              85.0 * scale[1], -117.0 * scale[0], 87.0 * scale[1])
    Lineto_r(-65.0 * scale[0], 2.0 * scale[1])
    Lineto_r(55.0 * scale[0], 7.0 * scale[1])
    Curveto_r(46.0 * scale[0], 6.0 * scale[1], 39.0 * scale[0],
              7.0 * scale[1], -45.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-55.0 * scale[0], 0.0 * scale[1], -113.0 *
              scale[0], -3.0 * scale[1], -130.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(117.0 * scale[0], 1413.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-85.0 * scale[0], -5.0 * scale[1], -94.0 * scale[0], -
              18.0 * scale[1], -92.0 * scale[0], -121.0 * scale[1])
    Curveto_r(1.0 * scale[0], -40.0 * scale[1], 5.0 * scale[0], -
              75.0 * scale[1], 8.0 * scale[0], -79.0 * scale[1])
    Curveto_r(4.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              3.0 * scale[1], 7.0 * scale[0], 13.0 * scale[1])
    Curveto_r(0.0 * scale[0], 32.0 * scale[1], 23.0 * scale[0],
              72.0 * scale[1], 48.0 * scale[0], 84.0 * scale[1])
    Curveto_r(13.0 * scale[0], 5.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 18.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 4.0 * scale[1], 12.0 * scale[0],
              8.0 * scale[1], 32.0 * scale[0], 8.0 * scale[1])
    Curveto_r(39.0 * scale[0], 0.0 * scale[1], 67.0 * scale[0], -
              18.0 * scale[1], 59.0 * scale[0], -39.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -9.0 * scale[1], 8.0 * scale[0], -
              11.0 * scale[1], 42.0 * scale[0], -7.0 * scale[1])
    Curveto_r(37.0 * scale[0], 3.0 * scale[1], 40.0 * scale[0],
              5.0 * scale[1], 16.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-41.0 * scale[0], 5.0 * scale[1], -52.0 * scale[0],
              25.0 * scale[1], -17.0 * scale[0], 33.0 * scale[1])
    Curveto_r(25.0 * scale[0], 6.0 * scale[1], 25.0 * scale[0],
              7.0 * scale[1], -8.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-41.0 * scale[0], 2.0 * scale[1], -133.0 * scale[0],
              29.0 * scale[1], -107.0 * scale[0], 32.0 * scale[1])
    Curveto_r(24.0 * scale[0], 2.0 * scale[1], 28.0 * scale[0],
              3.0 * scale[1], 69.0 * scale[0], 21.0 * scale[1])
    Curveto_r(21.0 * scale[0], 9.0 * scale[1], 51.0 * scale[0],
              15.0 * scale[1], 68.0 * scale[0], 13.0 * scale[1])
    Curveto_r(17.0 * scale[0], -2.0 * scale[1], 41.0 * scale[0],
              0.0 * scale[1], 53.0 * scale[0], 5.0 * scale[1])
    Curveto_r(23.0 * scale[0], 9.0 * scale[1], -52.0 * scale[0],
              10.0 * scale[1], -196.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(351.0 * scale[0], 1411.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -5.0 * scale[1], -3.0 * scale[0], -
              11.0 * scale[1], 14.0 * scale[0], -19.0 * scale[1])
    Curveto_r(20.0 * scale[0], -9.0 * scale[1], 25.0 *
              scale[0], -9.0 * scale[1], 25.0 * scale[0], 2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], -23.0 * scale[0],
              27.0 * scale[1], -39.0 * scale[0], 17.0 * scale[1])
    te.end_fill()
    Moveto(423.0 * scale[0], 1413.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(560.0 * scale[0], 1411.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 24.0 * scale[0], -
              18.0 * scale[1], 50.0 * scale[0], -4.0 * scale[1])
    Curveto_r(25.0 * scale[0], 13.0 * scale[1], 25.0 * scale[0],
              13.0 * scale[1], -12.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 0.0 * scale[1], -38.0 *
              scale[0], -4.0 * scale[1], -38.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(600.0 * scale[0], 1392.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 105.0 * scale[0], -
              44.0 * scale[1], 135.0 * scale[0], -39.0 * scale[1])
    Curveto_r(27.0 * scale[0], 4.0 * scale[1], 27.0 * scale[0],
              4.0 * scale[1], -7.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 0.0 * scale[1], -57.0 * scale[0],
              10.0 * scale[1], -82.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 10.0 * scale[1], -46.0 * scale[0],
              16.0 * scale[1], -46.0 * scale[0], 12.0 * scale[1])
    te.end_fill()
    Moveto(4.0 * scale[0], 1210.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -102.0 * scale[1], 2.0 * scale[0], -
              143.0 * scale[1], 3.0 * scale[0], -92.0 * scale[1])
    Curveto_r(2.0 * scale[0], 50.0 * scale[1], 2.0 * scale[0],
              134.0 * scale[1], 0.0 * scale[0], 185.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 50.0 * scale[1], -3.0 * scale[0],
              9.0 * scale[1], -3.0 * scale[0], -93.0 * scale[1])
    te.end_fill()
    Moveto(430.0 * scale[0], 1382.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 9.0 * scale[0], -
              13.0 * scale[1], 20.0 * scale[0], -20.0 * scale[1])
    Curveto_r(11.0 * scale[0], -7.0 * scale[1], 20.0 *
              scale[0], -9.0 * scale[1], 20.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], -9.0 * scale[0],
              13.0 * scale[1], -20.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 7.0 * scale[1], -20.0 * scale[0],
              9.0 * scale[1], -20.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(430.0 * scale[0], 1310.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -12.0 * scale[1], -26.0 *
              scale[0], -18.0 * scale[1], -32.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(5.0 * scale[0], -8.0 * scale[1], -1.0 * scale[0], -
              12.0 * scale[1], -14.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -18.0 * scale[0],
              4.0 * scale[1], -15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], -1.0 * scale[0],
              7.0 * scale[1], -12.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -6.0 * scale[1], -13.0 *
              scale[0], -9.0 * scale[1], 12.0 * scale[0], -19.0 * scale[1])
    Curveto_r(27.0 * scale[0], -11.0 * scale[1], 33.0 *
              scale[0], -10.0 * scale[1], 55.0 * scale[0], 11.0 * scale[1])
    Curveto_r(14.0 * scale[0], 13.0 * scale[1], 36.0 * scale[0],
              28.0 * scale[1], 50.0 * scale[0], 34.0 * scale[1])
    Curveto_r(24.0 * scale[0], 9.0 * scale[1], 24.0 * scale[0],
              10.0 * scale[1], 3.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 1.0 * scale[1], -32.0 * scale[0], -
              8.0 * scale[1], -43.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(535.0 * scale[0], 1314.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(37.0 * scale[0], -29.0 * scale[1], 55.0 * scale[0], -
              36.0 * scale[1], 49.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], -20.0 * scale[0],
              19.0 * scale[1], -37.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 10.0 * scale[1], -31.0 * scale[0],
              10.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(601.0 * scale[0], 1304.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(298.0 * scale[0], 1283.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(153.0 * scale[0], 1268.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], -1.0 *
              scale[0], -8.0 * scale[1], 5.0 * scale[0], -4.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 13.0 * scale[0],
              2.0 * scale[1], 17.0 * scale[0], -4.0 * scale[1])
    Curveto_r(8.0 * scale[0], -12.0 * scale[1], 25.0 * scale[0], -
              13.0 * scale[1], 25.0 * scale[0], -1.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], -39.0 * scale[0],
              21.0 * scale[1], -47.0 * scale[0], 9.0 * scale[1])
    te.end_fill()
    Moveto(596.0 * scale[0], 1257.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0], -
              15.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 0.0 * scale[0],
              11.0 * scale[1], -7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              8.0 * scale[1], -5.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(210.0 * scale[0], 1223.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -18.0 * scale[1], -3.0 * scale[0], -
              41.0 * scale[1], -4.0 * scale[0], -50.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -12.0 * scale[1], 7.0 * scale[0], -
              19.0 * scale[1], 24.0 * scale[0], -20.0 * scale[1])
    Curveto_r(14.0 * scale[0], -1.0 * scale[1], 18.0 * scale[0],
              0.0 * scale[1], 8.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 3.0 * scale[1], -18.0 * scale[0],
              10.0 * scale[1], -18.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 6.0 * scale[0],
              8.0 * scale[1], 14.0 * scale[0], 5.0 * scale[1])
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 35.0 * scale[0], -
              8.0 * scale[1], 62.0 * scale[0], -12.0 * scale[1])
    Curveto_r(27.0 * scale[0], -3.0 * scale[1], 59.0 * scale[0], -
              8.0 * scale[1], 72.0 * scale[0], -11.0 * scale[1])
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 22.0 * scale[0],
              0.0 * scale[1], 22.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -29.0 * scale[0],
              12.0 * scale[1], -65.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-132.0 * scale[0], 12.0 * scale[1], -141.0 * scale[0],
              49.0 * scale[1], -14.0 * scale[0], 58.0 * scale[1])
    Lineto_r(84.0 * scale[0], 6.0 * scale[1])
    Lineto_r(-88.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-49.0 * scale[0], -1.0 * scale[1], -89.0 * scale[0],
              3.0 * scale[1], -91.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              5.0 * scale[1], -6.0 * scale[0], -22.0 * scale[1])
    te.end_fill()
    Moveto(950.0 * scale[0], 1219.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -23.0 * scale[1], 6.0 * scale[0], -
              31.0 * scale[1], -6.0 * scale[0], -36.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -3.0 * scale[1], -14.0 * scale[0], -
              11.0 * scale[1], -14.0 * scale[0], -19.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -5.0 * scale[0], -
              14.0 * scale[1], -11.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              3.0 * scale[1], -5.0 * scale[0], -8.0 * scale[1])
    Curveto_r(8.0 * scale[0], -13.0 * scale[1], -73.0 * scale[0],
              0.0 * scale[1], -85.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 8.0 * scale[1], -16.0 * scale[0],
              14.0 * scale[1], -21.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0], -
              5.0 * scale[1], 1.0 * scale[0], -13.0 * scale[1])
    Curveto_r(6.0 * scale[0], -8.0 * scale[1], 8.0 * scale[0], -
              17.0 * scale[1], 4.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], 1.0 * scale[0], -
              7.0 * scale[1], 10.0 * scale[0], -7.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0], -
              6.0 * scale[1], 17.0 * scale[0], -14.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 7.0 * scale[0], -
              12.0 * scale[1], 19.0 * scale[0], -9.0 * scale[1])
    Curveto_r(10.0 * scale[0], 3.0 * scale[1], 21.0 * scale[0],
              1.0 * scale[1], 24.0 * scale[0], -4.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              9.0 * scale[1], -11.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -44.0 * scale[0], -
              2.0 * scale[1], -77.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-50.0 * scale[0], -3.0 * scale[1], -55.0 *
              scale[0], -5.0 * scale[1], -30.0 * scale[0], -11.0 * scale[1])
    Curveto_r(20.0 * scale[0], -5.0 * scale[1], 24.0 *
              scale[0], -8.0 * scale[1], 10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -1.0 * scale[1], -17.0 *
              scale[0], -3.0 * scale[1], -5.0 * scale[0], -11.0 * scale[1])
    Curveto_r(10.0 * scale[0], -6.0 * scale[1], -2.0 * scale[0], -
              10.0 * scale[1], -40.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-50.0 * scale[0], -3.0 * scale[1], -49.0 *
              scale[0], -3.0 * scale[1], 18.0 * scale[0], -5.0 * scale[1])
    Curveto_r(42.0 * scale[0], -1.0 * scale[1], 72.0 * scale[0],
              2.0 * scale[1], 72.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 5.0 * scale[0],
              10.0 * scale[1], 11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0], -
              7.0 * scale[1], 5.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -11.0 * scale[1], 2.0 * scale[0], -
              15.0 * scale[1], 22.0 * scale[0], -16.0 * scale[1])
    Curveto_r(23.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-26.0 * scale[0], -5.0 * scale[1], -41.0 * scale[0], -
              42.0 * scale[1], -22.0 * scale[0], -53.0 * scale[1])
    Curveto_r(8.0 * scale[0], -6.0 * scale[1], 1.0 * scale[0], -
              10.0 * scale[1], -22.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-33.0 * scale[0], -4.0 * scale[1], -33.0 *
              scale[0], -4.0 * scale[1], 7.0 * scale[0], -5.0 * scale[1])
    Curveto_r(40.0 * scale[0], -2.0 * scale[1], 51.0 * scale[0], -
              12.0 * scale[1], 67.0 * scale[0], -62.0 * scale[1])
    Curveto_r(4.0 * scale[0], -12.0 * scale[1], 6.0 *
              scale[0], -11.0 * scale[1], 6.0 * scale[0], 3.0 * scale[1])
    Curveto_r(1.0 * scale[0], 12.0 * scale[1], 9.0 * scale[0],
              17.0 * scale[1], 30.0 * scale[0], 17.0 * scale[1])
    Curveto_r(17.0 * scale[0], 0.0 * scale[1], 32.0 * scale[0], -
              4.0 * scale[1], 35.0 * scale[0], -8.0 * scale[1])
    Curveto_r(8.0 * scale[0], -14.0 * scale[1], 10.0 * scale[0], -
              116.0 * scale[1], 2.0 * scale[0], -139.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -17.0 * scale[1], -4.0 *
              scale[0], -23.0 * scale[1], 8.0 * scale[0], -23.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0],
              14.0 * scale[1], 16.0 * scale[0], 76.0 * scale[1])
    Curveto_r(0.0 * scale[0], 41.0 * scale[1], -4.0 * scale[0],
              83.0 * scale[1], -9.0 * scale[0], 93.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], -6.0 * scale[0],
              42.0 * scale[1], -2.0 * scale[0], 74.0 * scale[1])
    Curveto_r(4.0 * scale[0], 31.0 * scale[1], 4.0 * scale[0],
              57.0 * scale[1], -1.0 * scale[0], 57.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              4.0 * scale[1], -8.0 * scale[0], -8.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], -9.0 * scale[0], -
              8.0 * scale[1], -20.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0],
              5.0 * scale[1], -20.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -15.0 * scale[0],
              10.0 * scale[1], -37.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-29.0 * scale[0], -2.0 * scale[1], -34.0 *
              scale[0], -1.0 * scale[1], -23.0 * scale[0], 7.0 * scale[1])
    Curveto_r(8.0 * scale[0], 6.0 * scale[1], 34.0 * scale[0],
              11.0 * scale[1], 57.0 * scale[0], 11.0 * scale[1])
    Lineto_r(41.0 * scale[0], 0.0 * scale[1])
    Lineto_r(0.0 * scale[0], 95.0 * scale[1])
    Curveto_r(0.0 * scale[0], 73.0 * scale[1], -3.0 * scale[0],
              95.0 * scale[1], -13.0 * scale[0], 95.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 0.0 * scale[1], -12.0 *
              scale[0], -7.0 * scale[1], -5.0 * scale[0], -31.0 * scale[1])
    te.end_fill()
    Moveto(360.0 * scale[0], 1199.0 * scale[1], x, y)
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
    Moveto(766.0 * scale[0], 1189.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(20.0 * scale[0], -23.0 * scale[1], 24.0 *
              scale[0], -23.0 * scale[1], 24.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -9.0 * scale[0],
              16.0 * scale[1], -21.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 5.0 * scale[1], -20.0 * scale[0],
              5.0 * scale[1], -3.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(20.0 * scale[0], 1189.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 9.0 * scale[0], -
              9.0 * scale[1], 20.0 * scale[0], -9.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0],
              4.0 * scale[1], 20.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], -9.0 * scale[0],
              8.0 * scale[1], -20.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 1.0 * scale[1], -20.0 *
              scale[0], -2.0 * scale[1], -20.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(26.0 * scale[0], 1128.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -24.0 * scale[1], 7.0 * scale[0], -
              49.0 * scale[1], 10.0 * scale[0], -55.0 * scale[1])
    Curveto_r(2.0 * scale[0], -10.0 * scale[1], 37.0 * scale[0], -
              13.0 * scale[1], 131.0 * scale[0], -12.0 * scale[1])
    Curveto_r(99.0 * scale[0], 0.0 * scale[1], 122.0 * scale[0],
              3.0 * scale[1], 103.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -42.0 * scale[0],
              17.0 * scale[1], -62.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-44.0 * scale[0], 18.0 * scale[1], -50.0 * scale[0],
              32.0 * scale[1], -10.0 * scale[0], 27.0 * scale[1])
    Curveto_r(41.0 * scale[0], -5.0 * scale[1], 116.0 * scale[0], -
              23.0 * scale[1], 148.0 * scale[0], -35.0 * scale[1])
    Curveto_r(17.0 * scale[0], -7.0 * scale[1], 25.0 *
              scale[0], -7.0 * scale[1], 19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 5.0 * scale[1], -44.0 * scale[0],
              19.0 * scale[1], -85.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-41.0 * scale[0], 12.0 * scale[1], -81.0 * scale[0],
              29.0 * scale[1], -87.0 * scale[0], 38.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 15.0 * scale[1], -13.0 * scale[0],
              15.0 * scale[1], -13.0 * scale[0], 1.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], -7.0 * scale[0], -
              19.0 * scale[1], -16.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-24.0 * scale[0], -9.0 * scale[1], -54.0 *
              scale[0], -7.0 * scale[1], -54.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -60.0 * scale[0],
              30.0 * scale[1], -83.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -5.0 * scale[0], -
              19.0 * scale[1], -1.0 * scale[0], -42.0 * scale[1])
    te.end_fill()
    Moveto_r(169.0 * scale[0], -48.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(19.0 * scale[0], -8.0 * scale[1], 19.0 *
              scale[0], -9.0 * scale[1], -2.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -1.0 * scale[1], -25.0 * scale[0],
              4.0 * scale[1], -28.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 12.0 * scale[1], 2.0 * scale[0],
              12.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(596.0 * scale[0], 1153.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(410.0 * scale[0], 1115.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -9.0 * scale[1], 15.0 * scale[0], -
              13.0 * scale[1], 17.0 * scale[0], -11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], -7.0 * scale[0],
              26.0 * scale[1], -19.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0], -
              6.0 * scale[1], 2.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(555.0 * scale[0], 1110.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-17.0 * scale[0], -11.0 * scale[1], -25.0 *
              scale[0], -20.0 * scale[1], -18.0 * scale[0], -20.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], 10.0 * scale[0],
              8.0 * scale[1], 15.0 * scale[0], 5.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 12.0 * scale[0],
              0.0 * scale[1], 15.0 * scale[0], 6.0 * scale[1])
    Curveto_r(12.0 * scale[0], 19.0 * scale[1], 0.0 * scale[0],
              19.0 * scale[1], -30.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(637.0 * scale[0], 1113.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(24.0 * scale[0], -2.0 * scale[1], 62.0 *
              scale[0], -2.0 * scale[1], 86.0 * scale[0], 0.0 * scale[1])
    Curveto_r(23.0 * scale[0], 2.0 * scale[1], 4.0 * scale[0],
              4.0 * scale[1], -43.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-47.0 * scale[0], 0.0 * scale[1], -66.0 *
              scale[0], -2.0 * scale[1], -43.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(460.0 * scale[0], 1090.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(8.0 * scale[0], -5.0 * scale[1], 26.0 * scale[0], -
              10.0 * scale[1], 39.0 * scale[0], -10.0 * scale[1])
    Curveto_r(32.0 * scale[0], 0.0 * scale[1], 24.0 * scale[0],
              6.0 * scale[1], -19.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 4.0 * scale[1], -31.0 * scale[0],
              3.0 * scale[1], -20.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(517.0 * scale[0], 1073.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-119.0 * scale[0], -4.0 * scale[1], -122.0 *
              scale[0], -23.0 * scale[1], -4.0 * scale[0], -23.0 * scale[1])
    Curveto_r(89.0 * scale[0], 0.0 * scale[1], 130.0 * scale[0],
              7.0 * scale[1], 121.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], -8.0 * scale[0],
              8.0 * scale[1], -12.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -1.0 * scale[1], -51.0 * scale[0], -
              4.0 * scale[1], -105.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(328.0 * scale[0], 1063.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 32.0 *
              scale[0], -2.0 * scale[1], 45.0 * scale[0], 0.0 * scale[1])
    Curveto_r(12.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              4.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 0.0 * scale[1], -35.0 *
              scale[0], -2.0 * scale[1], -22.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(24.0 * scale[0], 1035.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -21.0 * scale[1], 0.0 * scale[0], -
              38.0 * scale[1], 19.0 * scale[0], -41.0 * scale[1])
    Curveto_r(9.0 * scale[0], -1.0 * scale[1], 15.0 * scale[0],
              2.0 * scale[1], 11.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 13.0 * scale[1], 40.0 * scale[0],
              11.0 * scale[1], 54.0 * scale[0], -3.0 * scale[1])
    Curveto_r(15.0 * scale[0], -15.0 * scale[1], 16.0 *
              scale[0], -31.0 * scale[1], 0.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -4.0 * scale[0], -5.0 * scale[1])
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 11.0 * scale[0], -
              9.0 * scale[1], 16.0 * scale[0], -6.0 * scale[1])
    Curveto_r(10.0 * scale[0], 6.0 * scale[1], 7.0 * scale[0], -
              46.0 * scale[1], -3.0 * scale[0], -63.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -7.0 * scale[1], -14.0 *
              scale[0], -9.0 * scale[1], -20.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -9.0 * scale[0],
              4.0 * scale[1], -5.0 * scale[0], -1.0 * scale[1])
    Curveto_r(4.0 * scale[0], -4.0 * scale[1], 2.0 * scale[0], -
              15.0 * scale[1], -5.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -13.0 * scale[1], -9.0 *
              scale[0], -14.0 * scale[1], 2.0 * scale[0], -7.0 * scale[1])
    Curveto_r(11.0 * scale[0], 6.0 * scale[1], 13.0 * scale[0],
              4.0 * scale[1], 8.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -9.0 * scale[1], -3.0 * scale[0], -
              15.0 * scale[1], 2.0 * scale[0], -12.0 * scale[1])
    Curveto_r(27.0 * scale[0], 17.0 * scale[1], 37.0 * scale[0], -
              68.0 * scale[1], 12.0 * scale[0], -98.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -13.0 * scale[1], -9.0 *
              scale[0], -21.0 * scale[1], 9.0 * scale[0], -47.0 * scale[1])
    Curveto_r(13.0 * scale[0], -17.0 * scale[1], 19.0 * scale[0], -
              34.0 * scale[1], 14.0 * scale[0], -38.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -9.0 * scale[0], -
              13.0 * scale[1], -9.0 * scale[0], -21.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], -11.0 * scale[0], -
              15.0 * scale[1], -40.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-33.0 * scale[0], 0.0 * scale[1], -40.0 * scale[0],
              4.0 * scale[1], -45.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 24.0 * scale[1], -30.0 * scale[0],
              42.0 * scale[1], -30.0 * scale[0], 23.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 74.0 * scale[0], -
              92.0 * scale[1], 84.0 * scale[0], -92.0 * scale[1])
    Curveto_r(3.0 * scale[0], 0.0 * scale[1], 3.0 * scale[0],
              7.0 * scale[1], 0.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 9.0 * scale[1], 0.0 * scale[0],
              15.0 * scale[1], 8.0 * scale[0], 15.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 25.0 * scale[0],
              9.0 * scale[1], 38.0 * scale[0], 20.0 * scale[1])
    Curveto_r(12.0 * scale[0], 11.0 * scale[1], 26.0 * scale[0],
              18.0 * scale[1], 30.0 * scale[0], 15.0 * scale[1])
    Curveto_r(4.0 * scale[0], -2.0 * scale[1], 18.0 * scale[0],
              8.0 * scale[1], 31.0 * scale[0], 23.0 * scale[1])
    Curveto_r(21.0 * scale[0], 23.0 * scale[1], 21.0 * scale[0],
              24.0 * scale[1], 2.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -10.0 * scale[1], -26.0 *
              scale[0], -15.0 * scale[1], -32.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -12.0 * scale[0],
              0.0 * scale[1], -14.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -6.0 *
              scale[0], -5.0 * scale[1], -6.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 11.0 * scale[1], 4.0 * scale[0],
              17.0 * scale[1], 11.0 * scale[0], 15.0 * scale[1])
    Curveto_r(18.0 * scale[0], -6.0 * scale[1], 41.0 * scale[0],
              19.0 * scale[1], 32.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 8.0 * scale[1], 0.0 * scale[0],
              7.0 * scale[1], 11.0 * scale[0], -2.0 * scale[1])
    Curveto_r(10.0 * scale[0], -8.0 * scale[1], 16.0 * scale[0], -
              10.0 * scale[1], 12.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 7.0 * scale[1], 5.0 * scale[0],
              24.0 * scale[1], 20.0 * scale[0], 38.0 * scale[1])
    Curveto_r(14.0 * scale[0], 15.0 * scale[1], 19.0 * scale[0],
              24.0 * scale[1], 10.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -4.0 * scale[1], -26.0 *
              scale[0], -1.0 * scale[1], -39.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 11.0 * scale[1], -22.0 * scale[0],
              10.0 * scale[1], -4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(11.0 * scale[0], -9.0 * scale[1], 16.0 * scale[0], -
              19.0 * scale[1], 12.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], -19.0 * scale[0],
              6.0 * scale[1], -34.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              25.0 * scale[1], -13.0 * scale[0], 21.0 * scale[1])
    Curveto_r(11.0 * scale[0], -7.0 * scale[1], 13.0 *
              scale[0], -4.0 * scale[1], 6.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 39.0 * scale[1], -16.0 * scale[0],
              108.0 * scale[1], 2.0 * scale[0], 144.0 * scale[1])
    Curveto_r(15.0 * scale[0], 29.0 * scale[1], 25.0 * scale[0],
              36.0 * scale[1], 58.0 * scale[0], 41.0 * scale[1])
    Lineto_r(40.0 * scale[0], 6.0 * scale[1])
    Lineto_r(-35.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-36.0 * scale[0], 1.0 * scale[1], -74.0 * scale[0], -
              15.0 * scale[1], -76.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -37.0 * scale[1], -18.0 * scale[0], -
              95.0 * scale[1], -25.0 * scale[0], -95.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0],
              5.0 * scale[1], -9.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -6.0 * scale[0],
              7.0 * scale[1], -12.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -4.0 * scale[1], -5.0 * scale[0],
              2.0 * scale[1], 6.0 * scale[0], 14.0 * scale[1])
    Curveto_r(16.0 * scale[0], 19.0 * scale[1], 22.0 * scale[0],
              48.0 * scale[1], 16.0 * scale[0], 77.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 24.0 * scale[1], 1.0 * scale[0],
              45.0 * scale[1], 14.0 * scale[0], 45.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 26.0 * scale[0],
              15.0 * scale[1], 54.0 * scale[0], 18.0 * scale[1])
    Curveto_r(36.0 * scale[0], 5.0 * scale[1], 16.0 * scale[0],
              8.0 * scale[1], -74.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-99.0 * scale[0], 1.0 * scale[1], -124.0 * scale[0], -
              2.0 * scale[1], -128.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto_r(129.0 * scale[0], -205.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -11.0 * scale[1], 1.0 * scale[0], -
              18.0 * scale[1], -4.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0],
              12.0 * scale[1], -9.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 20.0 * scale[1], 7.0 * scale[0],
              17.0 * scale[1], 13.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto_r(24.0 * scale[0], -112.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -12.0 * scale[1], -9.0 * scale[0], -
              24.0 * scale[1], -15.0 * scale[0], -26.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -5.0 * scale[1], -15.0 *
              scale[0], 3.0 * scale[1], 0.0 * scale[0], 28.0 * scale[1])
    Curveto_r(16.0 * scale[0], 25.0 * scale[1], 19.0 * scale[0],
              25.0 * scale[1], 15.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(307.0 * scale[0], 1043.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(18.0 * scale[0], -2.0 * scale[1], 50.0 *
              scale[0], -2.0 * scale[1], 70.0 * scale[0], 0.0 * scale[1])
    Curveto_r(21.0 * scale[0], 2.0 * scale[1], 7.0 * scale[0],
              4.0 * scale[1], -32.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-38.0 * scale[0], 0.0 * scale[1], -55.0 *
              scale[0], -2.0 * scale[1], -38.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(2.0 * scale[0], 975.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(311.0 * scale[0], 967.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -1.0 * scale[1], 14.0 * scale[0], -
              11.0 * scale[1], 27.0 * scale[0], -21.0 * scale[1])
    Curveto_r(12.0 * scale[0], -11.0 * scale[1], 22.0 * scale[0], -
              16.0 * scale[1], 22.0 * scale[0], -13.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], -31.0 * scale[0],
              37.0 * scale[1], -42.0 * scale[0], 37.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              1.0 * scale[1], -7.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(736.0 * scale[0], 941.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], 6.0 * scale[0], -
              6.0 * scale[1], 19.0 * scale[0], -3.0 * scale[1])
    Curveto_r(14.0 * scale[0], 2.0 * scale[1], 25.0 * scale[0],
              6.0 * scale[1], 25.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -39.0 * scale[0],
              4.0 * scale[1], -44.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(20.0 * scale[0], 873.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -15.0 * scale[1], 6.0 * scale[0], -
              21.0 * scale[1], 19.0 * scale[0], -20.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0],
              5.0 * scale[1], 14.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 4.0 * scale[1], 0.0 * scale[0],
              13.0 * scale[1], 5.0 * scale[0], 20.0 * scale[1])
    Curveto_r(8.0 * scale[0], 9.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], -14.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 0.0 * scale[1], -24.0 * scale[0], -
              5.0 * scale[1], -24.0 * scale[0], -22.0 * scale[1])
    te.end_fill()
    Moveto(548.0 * scale[0], 863.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(681.0 * scale[0], 859.0 * scale[1], x, y)
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
    Moveto(334.0 * scale[0], 828.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-29.0 * scale[0], -33.0 * scale[1])
    Lineto_r(33.0 * scale[0], 29.0 * scale[1])
    Curveto_r(30.0 * scale[0], 28.0 * scale[1], 37.0 * scale[0],
              36.0 * scale[1], 29.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0], -
              15.0 * scale[1], -33.0 * scale[0], -32.0 * scale[1])
    te.end_fill()
    Moveto(730.0 * scale[0], 786.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(863.0 * scale[0], 753.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -13.0 * scale[1], -19.0 *
              scale[0], -23.0 * scale[1], -14.0 * scale[0], -23.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 46.0 * scale[0],
              39.0 * scale[1], 40.0 * scale[0], 43.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 2.0 * scale[1], -14.0 * scale[0], -
              7.0 * scale[1], -26.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(20.0 * scale[0], 746.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -32.0 * scale[1], 13.0 * scale[0], -
              40.0 * scale[1], 27.0 * scale[0], -17.0 * scale[1])
    Curveto_r(9.0 * scale[0], 14.0 * scale[1], 7.0 * scale[0],
              20.0 * scale[1], -8.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 11.0 * scale[1], -19.0 * scale[0],
              9.0 * scale[1], -19.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(800.0 * scale[0], 708.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(18.0 * scale[0], -27.0 * scale[1], 35.0 * scale[0], -
              48.0 * scale[1], 37.0 * scale[0], -48.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -2.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -2.0 * scale[0],
              10.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              9.0 * scale[1], 21.0 * scale[0], 20.0 * scale[1])
    Curveto_r(6.0 * scale[0], 11.0 * scale[1], 7.0 * scale[0],
              19.0 * scale[1], 3.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -3.0 * scale[1], -67.0 * scale[0],
              13.0 * scale[1], -83.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 6.0 * scale[1], 1.0 * scale[0], -
              10.0 * scale[1], 20.0 * scale[0], -36.0 * scale[1])
    te.end_fill()
    Moveto(890.0 * scale[0], 724.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -1.0 * scale[1], 6.0 * scale[0], -
              7.0 * scale[1], 14.0 * scale[0], -13.0 * scale[1])
    Curveto_r(10.0 * scale[0], -8.0 * scale[1], 16.0 *
              scale[0], -8.0 * scale[1], 25.0 * scale[0], 3.0 * scale[1])
    Curveto_r(10.0 * scale[0], 11.0 * scale[1], 7.0 * scale[0],
              14.0 * scale[1], -14.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -25.0 *
              scale[0], -2.0 * scale[1], -25.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(876.0 * scale[0], 702.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], -3.0 * scale[0], -
              18.0 * scale[1], 0.0 * scale[0], -29.0 * scale[1])
    Curveto_r(5.0 * scale[0], -15.0 * scale[1], 4.0 * scale[0], -
              15.0 * scale[1], -5.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 8.0 * scale[1], -13.0 * scale[0],
              11.0 * scale[1], -17.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], 0.0 * scale[0], -
              14.0 * scale[1], 8.0 * scale[0], -21.0 * scale[1])
    Curveto_r(13.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 27.0 * scale[0], 4.0 * scale[1])
    Curveto_r(7.0 * scale[0], 13.0 * scale[1], 8.0 * scale[0],
              26.0 * scale[1], 3.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 9.0 * scale[1], -12.0 * scale[0],
              12.0 * scale[1], -16.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(851.0 * scale[0], 633.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -12.0 * scale[1], 15.0 * scale[0], -
              20.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(3.0 * scale[0], 2.0 * scale[1], -3.0 * scale[0],
              12.0 * scale[1], -13.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 16.0 * scale[1], -18.0 * scale[0],
              16.0 * scale[1], -5.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(811.0 * scale[0], 624.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(212.0 * scale[0], 610.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(145.0 * scale[0], 609.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0], -
              12.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 17.0 * scale[1], 1.0 * scale[0],
              20.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(27.0 * scale[0], 554.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -18.0 * scale[1], -14.0 *
              scale[0], -22.0 * scale[1], -3.0 * scale[0], -18.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 17.0 * scale[0],
              13.0 * scale[1], 20.0 * scale[0], 21.0 * scale[1])
    Curveto_r(10.0 * scale[0], 25.0 * scale[1], 3.0 * scale[0],
              23.0 * scale[1], -17.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(31.0 * scale[0], 513.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -12.0 * scale[1], 4.0 * scale[0], -
              25.0 * scale[1], 9.0 * scale[0], -28.0 * scale[1])
    Curveto_r(12.0 * scale[0], -7.0 * scale[1], 12.0 * scale[0],
              2.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 19.0 * scale[1], -9.0 * scale[0],
              19.0 * scale[1], -9.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(202.0 * scale[0], 495.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(822.0 * scale[0], 460.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(12.0 * scale[0], 440.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 2.0 * scale[0], -
              27.0 * scale[1], 5.0 * scale[0], -17.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              25.0 * scale[1], 0.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(210.0 * scale[0], 414.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -18.0 * scale[1], 76.0 * scale[0], -
              93.0 * scale[1], 100.0 * scale[0], -99.0 * scale[1])
    Curveto_r(20.0 * scale[0], -4.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], -9.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 11.0 * scale[1], -47.0 * scale[0],
              36.0 * scale[1], -62.0 * scale[0], 57.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 21.0 * scale[1], -29.0 * scale[0],
              34.0 * scale[1], -29.0 * scale[0], 29.0 * scale[1])
    te.end_fill()
    Moveto(775.0 * scale[0], 374.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-25.0 * scale[0], -20.0 * scale[1], -26.0 *
              scale[0], -22.0 * scale[1], -8.0 * scale[0], -18.0 * scale[1])
    Curveto_r(12.0 * scale[0], 4.0 * scale[1], 28.0 * scale[0],
              13.0 * scale[1], 34.0 * scale[0], 20.0 * scale[1])
    Curveto_r(20.0 * scale[0], 24.0 * scale[1], 5.0 * scale[0],
              23.0 * scale[1], -26.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(347.0 * scale[0], 301.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -7.0 * scale[1], 9.0 * scale[0], -
              20.0 * scale[1], 6.0 * scale[0], -27.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], 1.0 * scale[0], -
              22.0 * scale[1], 8.0 * scale[0], -32.0 * scale[1])
    Curveto_r(13.0 * scale[0], -15.0 * scale[1], 12.0 *
              scale[0], -16.0 * scale[1], -3.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 11.0 * scale[1], -18.0 * scale[0],
              10.0 * scale[1], -29.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -20.0 * scale[1], -10.0 *
              scale[0], -21.0 * scale[1], 3.0 * scale[0], -11.0 * scale[1])
    Curveto_r(8.0 * scale[0], 7.0 * scale[1], 18.0 * scale[0],
              10.0 * scale[1], 21.0 * scale[0], 7.0 * scale[1])
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], 66.0 * scale[0], -
              8.0 * scale[1], 139.0 * scale[0], -11.0 * scale[1])
    Curveto_r(72.0 * scale[0], -2.0 * scale[1], 137.0 * scale[0], -
              8.0 * scale[1], 143.0 * scale[0], -12.0 * scale[1])
    Curveto_r(5.0 * scale[0], -5.0 * scale[1], 20.0 *
              scale[0], -5.0 * scale[1], 33.0 * scale[0], 0.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 22.0 * scale[0],
              14.0 * scale[1], 17.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 11.0 * scale[1], -2.0 * scale[0],
              20.0 * scale[1], 4.0 * scale[0], 20.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              5.0 * scale[1], 11.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -4.0 * scale[0],
              7.0 * scale[1], -10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -8.0 * scale[1], -13.0 *
              scale[0], 1.0 * scale[1], 1.0 * scale[0], 28.0 * scale[1])
    Curveto_r(9.0 * scale[0], 20.0 * scale[1], 9.0 * scale[0],
              20.0 * scale[1], -4.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -10.0 * scale[1], -19.0 * scale[0], -
              18.0 * scale[1], -26.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              3.0 * scale[1], -11.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], -49.0 * scale[0], -
              33.0 * scale[1], -64.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 1.0 * scale[1], 5.0 * scale[0],
              9.0 * scale[1], 24.0 * scale[0], 20.0 * scale[1])
    Curveto_r(47.0 * scale[0], 26.0 * scale[1], 34.0 * scale[0],
              25.0 * scale[1], -25.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-53.0 * scale[0], -24.0 * scale[1], -119.0 *
              scale[0], -21.0 * scale[1], -158.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 8.0 * scale[1], -28.0 * scale[0],
              15.0 * scale[1], -36.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -24.0 * scale[0],
              8.0 * scale[1], -35.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 10.0 * scale[1], -16.0 * scale[0],
              11.0 * scale[1], -9.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(100.0 * scale[0], 81.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 18.0 * scale[1], -14.0 * scale[0],
              21.0 * scale[1], -14.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(946.0 * scale[0], 33.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#0c0e04')
    te.end_fill()
    Moveto(20.0 * scale[0], 1405.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -9.0 * scale[1], -11.0 * scale[0], -
              17.0 * scale[1], -9.0 * scale[0], -20.0 * scale[1])
    Curveto_r(3.0 * scale[0], -2.0 * scale[1], 10.0 * scale[0],
              5.0 * scale[1], 17.0 * scale[0], 15.0 * scale[1])
    Curveto_r(14.0 * scale[0], 24.0 * scale[1], 10.0 * scale[0],
              26.0 * scale[1], -8.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(963.0 * scale[0], 1396.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(25.0 * scale[0], -28.0 * scale[1], 34.0 *
              scale[0], -27.0 * scale[1], 17.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 12.0 * scale[1], -17.0 * scale[0],
              21.0 * scale[1], -25.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              7.0 * scale[1], 8.0 * scale[0], -24.0 * scale[1])
    te.end_fill()
    Moveto(981.0 * scale[0], 1184.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(979.0 * scale[0], 1108.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -2.0 * scale[0], -
              23.0 * scale[1], -3.0 * scale[0], -35.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -13.0 * scale[1], 1.0 * scale[0], -
              23.0 * scale[1], 6.0 * scale[0], -23.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0],
              16.0 * scale[1], 8.0 * scale[0], 35.0 * scale[1])
    Curveto_r(0.0 * scale[0], 32.0 * scale[1], -9.0 * scale[0],
              51.0 * scale[1], -11.0 * scale[0], 23.0 * scale[1])
    te.end_fill()
    Moveto(218.0 * scale[0], 973.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-26.0 * scale[0], -7.0 * scale[1], -49.0 * scale[0], -
              51.0 * scale[1], -51.0 * scale[0], -97.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -75.0 * scale[1], 40.0 * scale[0], -
              123.0 * scale[1], 93.0 * scale[0], -104.0 * scale[1])
    Curveto_r(21.0 * scale[0], 7.0 * scale[1], 110.0 * scale[0],
              93.0 * scale[1], 110.0 * scale[0], 106.0 * scale[1])
    Curveto_r(0.0 * scale[0], 2.0 * scale[1], -7.0 * scale[0],
              19.0 * scale[1], -16.0 * scale[0], 37.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 41.0 * scale[1], -89.0 * scale[0],
              71.0 * scale[1], -136.0 * scale[0], 58.0 * scale[1])
    te.end_fill()
    Moveto_r(35.0 * scale[0], -25.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(29.0 * scale[0], -14.0 * scale[1], 41.0 * scale[0], -
              50.0 * scale[1], 35.0 * scale[0], -109.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -29.0 * scale[1], -7.0 * scale[0], -
              34.0 * scale[1], -31.0 * scale[0], -37.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -2.0 * scale[1], -29.0 * scale[0],
              2.0 * scale[1], -33.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -14.0 * scale[0],
              16.0 * scale[1], -23.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0],
              3.0 * scale[1], -6.0 * scale[0], 5.0 * scale[1])
    Curveto_r(6.0 * scale[0], 2.0 * scale[1], 9.0 * scale[0],
              23.0 * scale[1], 7.0 * scale[0], 46.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 32.0 * scale[1], 0.0 * scale[0],
              43.0 * scale[1], 14.0 * scale[0], 51.0 * scale[1])
    Curveto_r(17.0 * scale[0], 10.0 * scale[1], 17.0 * scale[0],
              11.0 * scale[1], -1.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 5.0 * scale[1], -15.0 * scale[0],
              8.0 * scale[1], -4.0 * scale[0], 8.0 * scale[1])
    Curveto_r(8.0 * scale[0], 1.0 * scale[1], 27.0 * scale[0], -
              5.0 * scale[1], 42.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(772.0 * scale[0], 940.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-18.0 * scale[0], -4.0 * scale[1], -44.0 * scale[0], -
              20.0 * scale[1], -57.0 * scale[0], -34.0 * scale[1])
    Curveto_r(-25.0 * scale[0], -27.0 * scale[1], -34.0 *
              scale[0], -66.0 * scale[1], -15.0 * scale[0], -66.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              5.0 * scale[1], 10.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 21.0 * scale[0], -
              31.0 * scale[1], 46.0 * scale[0], -56.0 * scale[1])
    Curveto_r(35.0 * scale[0], -33.0 * scale[1], 51.0 * scale[0], -
              42.0 * scale[1], 68.0 * scale[0], -37.0 * scale[1])
    Curveto_r(42.0 * scale[0], 12.0 * scale[1], 59.0 * scale[0],
              40.0 * scale[1], 64.0 * scale[0], 101.0 * scale[1])
    Curveto_r(3.0 * scale[0], 50.0 * scale[1], 1.0 * scale[0],
              62.0 * scale[1], -20.0 * scale[0], 86.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 28.0 * scale[1], -39.0 * scale[0],
              31.0 * scale[1], -96.0 * scale[0], 17.0 * scale[1])
    te.end_fill()
    Moveto_r(72.0 * scale[0], -32.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], 1.0 *
              scale[0], -8.0 * scale[1], 8.0 * scale[0], -8.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0], -
              3.0 * scale[1], -2.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -5.0 * scale[1], -11.0 * scale[0], -
              10.0 * scale[1], -6.0 * scale[0], -10.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 2.0 * scale[0], -
              8.0 * scale[1], -5.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -11.0 * scale[1], -10.0 *
              scale[0], -14.0 * scale[1], -1.0 * scale[0], -9.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 12.0 * scale[0],
              0.0 * scale[1], 12.0 * scale[0], -14.0 * scale[1])
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], 5.0 * scale[0], -
              18.0 * scale[1], 10.0 * scale[0], -15.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 8.0 * scale[0],
              18.0 * scale[1], 5.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 23.0 * scale[1], -4.0 * scale[0],
              24.0 * scale[1], 4.0 * scale[0], 7.0 * scale[1])
    Curveto_r(14.0 * scale[0], -29.0 * scale[1], 14.0 * scale[0], -
              30.0 * scale[1], -19.0 * scale[0], -64.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -18.0 * scale[1], -37.0 *
              scale[0], -31.0 * scale[1], -47.0 * scale[0], -29.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 4.0 * scale[1], -63.0 * scale[0],
              45.0 * scale[1], -63.0 * scale[0], 66.0 * scale[1])
    Curveto_r(0.0 * scale[0], 19.0 * scale[1], 38.0 * scale[0],
              67.0 * scale[1], 59.0 * scale[0], 73.0 * scale[1])
    Curveto_r(22.0 * scale[0], 7.0 * scale[1], 50.0 * scale[0],
              5.0 * scale[1], 45.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(809.0 * scale[0], 898.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], -2.0 * scale[0], -
              11.0 * scale[1], -4.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -18.0 * scale[1], -3.0 *
              scale[0], -18.0 * scale[1], 16.0 * scale[0], -1.0 * scale[1])
    Curveto_r(10.0 * scale[0], 9.0 * scale[1], 19.0 * scale[0],
              19.0 * scale[1], 19.0 * scale[0], 21.0 * scale[1])
    Curveto_r(0.0 * scale[0], 3.0 * scale[1], -30.0 * scale[0],
              4.0 * scale[1], -31.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(805.0 * scale[0], 673.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -10.0 * scale[1], 14.0 * scale[0], -
              51.0 * scale[1], 21.0 * scale[0], -92.0 * scale[1])
    Curveto_r(11.0 * scale[0], -58.0 * scale[1], 11.0 * scale[0], -
              89.0 * scale[1], 2.0 * scale[0], -142.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -65.0 * scale[1], -13.0 *
              scale[0], -69.0 * scale[1], -47.0 * scale[0], -83.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -9.0 * scale[1], -48.0 * scale[0], -
              26.0 * scale[1], -63.0 * scale[0], -40.0 * scale[1])
    Lineto_r(-28.0 * scale[0], -25.0 * scale[1])
    Lineto_r(25.0 * scale[0], -66.0 * scale[1])
    Curveto_r(29.0 * scale[0], -75.0 * scale[1], 31.0 * scale[0], -
              121.0 * scale[1], 10.0 * scale[0], -172.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -19.0 * scale[1], -15.0 * scale[0], -
              37.0 * scale[1], -15.0 * scale[0], -39.0 * scale[1])
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 49.0 * scale[0], -
              4.0 * scale[1], 109.0 * scale[0], -4.0 * scale[1])
    Curveto_r(124.0 * scale[0], 0.0 * scale[1], 121.0 *
              scale[0], -1.0 * scale[1], 151.0 * scale[0], 85.0 * scale[1])
    Curveto_r(24.0 * scale[0], 70.0 * scale[1], 27.0 * scale[0],
              221.0 * scale[1], 6.0 * scale[0], 282.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 69.0 * scale[1], -78.0 * scale[0],
              176.0 * scale[1], -117.0 * scale[0], 236.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 32.0 * scale[1], -39.0 * scale[0],
              63.0 * scale[1], -39.0 * scale[0], 68.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -5.0 * scale[0],
              9.0 * scale[1], -11.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              7.0 * scale[1], -4.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto_r(85.0 * scale[0], -263.0 * scale[1], 0, 0)
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
    Moveto_r(-70.0 * scale[0], -105.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -8.0 * scale[1], 9.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 2.0 * scale[0], -
              10.0 * scale[1], 12.0 * scale[0], -10.0 * scale[1])
    Curveto_r(30.0 * scale[0], 0.0 * scale[1], 48.0 * scale[0], -
              31.0 * scale[1], 50.0 * scale[0], -87.0 * scale[1])
    Curveto_r(0.0 * scale[0], -29.0 * scale[1], -3.0 * scale[0], -
              53.0 * scale[1], -8.0 * scale[0], -53.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              9.0 * scale[1], -9.0 * scale[0], -20.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], -7.0 * scale[0], -
              20.0 * scale[1], -15.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              9.0 * scale[1], -15.0 * scale[0], -20.0 * scale[1])
    Curveto_r(0.0 * scale[0], -17.0 * scale[1], -7.0 * scale[0], -
              20.0 * scale[1], -40.0 * scale[0], -20.0 * scale[1])
    Lineto_r(-40.0 * scale[0], 0.0 * scale[1])
    Lineto_r(-2.0 * scale[0], 73.0 * scale[1])
    Curveto_r(0.0 * scale[0], 39.0 * scale[1], -1.0 * scale[0],
              80.0 * scale[1], 0.0 * scale[0], 90.0 * scale[1])
    Curveto_r(1.0 * scale[0], 9.0 * scale[1], -3.0 * scale[0],
              17.0 * scale[1], -8.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0],
              6.0 * scale[1], -4.0 * scale[0], 14.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], 12.0 * scale[0],
              12.0 * scale[1], 20.0 * scale[0], 9.0 * scale[1])
    Curveto_r(12.0 * scale[0], -4.0 * scale[1], 14.0 * scale[0],
              1.0 * scale[1], 10.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 16.0 * scale[1], -3.0 * scale[0],
              32.0 * scale[1], 0.0 * scale[0], 37.0 * scale[1])
    Curveto_r(8.0 * scale[0], 13.0 * scale[1], 30.0 * scale[0],
              10.0 * scale[1], 44.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(190.0 * scale[0], 648.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -17.0 * scale[1], -34.0 *
              scale[0], -44.0 * scale[1], -41.0 * scale[0], -60.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -15.0 * scale[1], -15.0 * scale[0], -
              28.0 * scale[1], -20.0 * scale[0], -28.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              11.0 * scale[1], -3.0 * scale[0], -25.0 * scale[1])
    Curveto_r(4.0 * scale[0], -18.0 * scale[1], 0.0 * scale[0], -
              30.0 * scale[1], -18.0 * scale[0], -47.0 * scale[1])
    Curveto_r(-35.0 * scale[0], -34.0 * scale[1], -60.0 * scale[0], -
              157.0 * scale[1], -56.0 * scale[0], -278.0 * scale[1])
    Curveto_r(2.0 * scale[0], -52.0 * scale[1], 7.0 * scale[0], -
              93.0 * scale[1], 12.0 * scale[0], -92.0 * scale[1])
    Curveto_r(5.0 * scale[0], 2.0 * scale[1], 12.0 * scale[0], -
              2.0 * scale[1], 17.0 * scale[0], -10.0 * scale[1])
    Curveto_r(5.0 * scale[0], -7.0 * scale[1], 16.0 * scale[0], -
              13.0 * scale[1], 26.0 * scale[0], -13.0 * scale[1])
    Curveto_r(22.0 * scale[0], 0.0 * scale[1], 24.0 * scale[0], -
              30.0 * scale[1], 3.0 * scale[0], -31.0 * scale[1])
    Curveto_r(-40.0 * scale[0], -3.0 * scale[1], -41.0 *
              scale[0], -3.0 * scale[1], -24.0 * scale[0], -29.0 * scale[1])
    Curveto_r(16.0 * scale[0], -24.0 * scale[1], 20.0 * scale[0], -
              25.0 * scale[1], 130.0 * scale[0], -25.0 * scale[1])
    Curveto_r(63.0 * scale[0], 0.0 * scale[1], 114.0 * scale[0],
              2.0 * scale[1], 114.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 2.0 * scale[1], -7.0 * scale[0],
              23.0 * scale[1], -15.0 * scale[0], 46.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 61.0 * scale[1], -19.0 * scale[0],
              114.0 * scale[1], 10.0 * scale[0], 170.0 * scale[1])
    Curveto_r(14.0 * scale[0], 27.0 * scale[1], 25.0 * scale[0],
              52.0 * scale[1], 25.0 * scale[0], 55.0 * scale[1])
    Curveto_r(0.0 * scale[0], 3.0 * scale[1], -19.0 * scale[0],
              14.0 * scale[1], -43.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 10.0 * scale[1], -55.0 * scale[0],
              35.0 * scale[1], -71.0 * scale[0], 55.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 33.0 * scale[1], -28.0 * scale[0],
              48.0 * scale[1], -33.0 * scale[0], 129.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 65.0 * scale[1], 0.0 * scale[0],
              106.0 * scale[1], 10.0 * scale[0], 140.0 * scale[1])
    Curveto_r(8.0 * scale[0], 26.0 * scale[1], 13.0 * scale[0],
              47.0 * scale[1], 10.0 * scale[0], 47.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0], -
              14.0 * scale[1], -33.0 * scale[0], -32.0 * scale[1])
    te.end_fill()
    Moveto_r(73.0 * scale[0], -362.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(16.0 * scale[0], 2.0 * scale[1], 21.0 * scale[0], -
              7.0 * scale[1], 18.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -7.0 * scale[1], 3.0 * scale[0], -
              13.0 * scale[1], 9.0 * scale[0], -13.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              5.0 * scale[1], 10.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -4.0 * scale[0], -
              7.0 * scale[1], -10.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -8.0 * scale[0], -12.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 0.0 * scale[0], -
              51.0 * scale[1], 0.0 * scale[0], -90.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -71.0 * scale[1], -3.0 * scale[0], -
              73.0 * scale[1], -27.0 * scale[0], -73.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 0.0 * scale[1], -25.0 * scale[0],
              6.0 * scale[1], -26.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 16.0 * scale[1], -2.0 * scale[0],
              16.0 * scale[1], -6.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -23.0 * scale[1], -23.0 *
              scale[0], -23.0 * scale[1], -24.0 * scale[0], 0.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], -3.0 * scale[0],
              12.0 * scale[1], -6.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -17.0 * scale[1], -26.0 *
              scale[0], -17.0 * scale[1], -20.0 * scale[0], 0.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], -3.0 * scale[0],
              18.0 * scale[1], -12.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 8.0 * scale[1], -11.0 * scale[0],
              11.0 * scale[1], -4.0 * scale[0], 8.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 15.0 *
              scale[0], -1.0 * scale[1], 18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], -2.0 * scale[0],
              13.0 * scale[1], -13.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 7.0 * scale[1], -46.0 * scale[0],
              83.0 * scale[1], -17.0 * scale[0], 83.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0],
              14.0 * scale[1], 21.0 * scale[0], 35.0 * scale[1])
    Curveto_r(3.0 * scale[0], 19.0 * scale[1], 10.0 * scale[0],
              35.0 * scale[1], 16.0 * scale[0], 35.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0],
              9.0 * scale[1], 31.0 * scale[0], 21.0 * scale[1])
    Curveto_r(21.0 * scale[0], 20.0 * scale[1], 22.0 * scale[0],
              20.0 * scale[1], 27.0 * scale[0], 1.0 * scale[1])
    Curveto_r(3.0 * scale[0], -11.0 * scale[1], 12.0 * scale[0], -
              18.0 * scale[1], 23.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(385.0 * scale[0], 517.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -13.0 * scale[1], -18.0 * scale[0], -
              44.0 * scale[1], -21.0 * scale[0], -69.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -42.0 * scale[1], -4.0 * scale[0], -
              47.0 * scale[1], 17.0 * scale[0], -53.0 * scale[1])
    Curveto_r(51.0 * scale[0], -17.0 * scale[1], 94.0 * scale[0],
              90.0 * scale[1], 51.0 * scale[0], 128.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 22.0 * scale[1], -29.0 * scale[0],
              21.0 * scale[1], -47.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto_r(28.0 * scale[0], -57.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -12.0 * scale[1], 0.0 * scale[0], -
              20.0 * scale[1], -8.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -27.0 * scale[0],
              25.0 * scale[1], -18.0 * scale[0], 34.0 * scale[1])
    Curveto_r(11.0 * scale[0], 11.0 * scale[1], 21.0 * scale[0],
              6.0 * scale[1], 26.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(607.0 * scale[0], 512.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-25.0 * scale[0], -27.0 * scale[1], -21.0 *
              scale[0], -67.0 * scale[1], 8.0 * scale[0], -97.0 * scale[1])
    Curveto_r(30.0 * scale[0], -29.0 * scale[1], 47.0 * scale[0], -
              31.0 * scale[1], 65.0 * scale[0], -10.0 * scale[1])
    Curveto_r(11.0 * scale[0], 13.0 * scale[1], 10.0 * scale[0],
              24.0 * scale[1], 0.0 * scale[0], 58.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 70.0 * scale[1], -42.0 * scale[0],
              83.0 * scale[1], -73.0 * scale[0], 49.0 * scale[1])
    te.end_fill()
    Moveto_r(44.0 * scale[0], -75.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -4.0 * scale[1], -15.0 *
              scale[0], -5.0 * scale[1], -25.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              7.0 * scale[1], 1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(13.0 * scale[0], 10.0 * scale[1], 20.0 * scale[0],
              10.0 * scale[1], 25.0 * scale[0], 2.0 * scale[1])
    Curveto_r(4.0 * scale[0], -7.0 * scale[1], 4.0 * scale[0], -
              15.0 * scale[1], -1.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(565.0 * scale[0], 315.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-27.0 * scale[0], -13.0 * scale[1], -58.0 *
              scale[0], -12.0 * scale[1], -107.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-34.0 * scale[0], 10.0 * scale[1], -18.0 *
              scale[0], -13.0 * scale[1], 22.0 * scale[0], -31.0 * scale[1])
    Curveto_r(39.0 * scale[0], -17.0 * scale[1], 41.0 *
              scale[0], -17.0 * scale[1], 80.0 * scale[0], 0.0 * scale[1])
    Curveto_r(22.0 * scale[0], 10.0 * scale[1], 40.0 * scale[0],
              24.0 * scale[1], 40.0 * scale[0], 32.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -1.0 * scale[0],
              13.0 * scale[1], -2.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0], -
              7.0 * scale[1], -33.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(60.0 * scale[0], 80.0 * scale[1], x, y)
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
    te.color('#e6ebd6')
    te.end_fill()
    Moveto(0.0 * scale[0], 1424.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 14.0 * scale[0], -5.0 * scale[1])
    Curveto_r(10.0 * scale[0], 8.0 * scale[1], 145.0 * scale[0],
              11.0 * scale[1], 495.0 * scale[0], 9.0 * scale[1])
    Curveto_r(264.0 * scale[0], -2.0 * scale[1], 481.0 * scale[0],
              0.0 * scale[1], 481.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], -223.0 * scale[0],
              7.0 * scale[1], -495.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-450.0 * scale[0], 0.0 * scale[1], -495.0 *
              scale[0], -1.0 * scale[1], -495.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(95.0 * scale[0], 1290.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-21.0 * scale[0], -22.0 * scale[1], -37.0 *
              scale[0], -41.0 * scale[1], -34.0 * scale[0], -42.0 * scale[1])
    Curveto_r(2.0 * scale[0], -2.0 * scale[1], 23.0 * scale[0],
              16.0 * scale[1], 45.0 * scale[0], 39.0 * scale[1])
    Curveto_r(23.0 * scale[0], 24.0 * scale[1], 39.0 * scale[0],
              43.0 * scale[1], 35.0 * scale[0], 43.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -24.0 * scale[0], -
              18.0 * scale[1], -46.0 * scale[0], -40.0 * scale[1])
    te.end_fill()
    Moveto(829.0 * scale[0], 1293.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-34.0 * scale[0], -38.0 * scale[1])
    Lineto_r(35.0 * scale[0], 32.0 * scale[1])
    Curveto_r(19.0 * scale[0], 17.0 * scale[1], 44.0 * scale[0],
              33.0 * scale[1], 55.0 * scale[0], 36.0 * scale[1])
    Curveto_r(20.0 * scale[0], 5.0 * scale[1], 20.0 * scale[0],
              5.0 * scale[1], -1.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 1.0 * scale[1], -34.0 * scale[0], -
              15.0 * scale[1], -55.0 * scale[0], -36.0 * scale[1])
    te.end_fill()
    Moveto(878.0 * scale[0], 1279.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-39.0 * scale[0], -39.0 * scale[1], -45.0 *
              scale[0], -49.0 * scale[1], -28.0 * scale[0], -49.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0],
              8.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(4.0 * scale[0], 9.0 * scale[1], 18.0 * scale[0],
              27.0 * scale[1], 32.0 * scale[0], 39.0 * scale[1])
    Curveto_r(14.0 * scale[0], 12.0 * scale[1], 24.0 * scale[0],
              24.0 * scale[1], 21.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 2.0 * scale[1], -22.0 * scale[0], -
              13.0 * scale[1], -42.0 * scale[0], -33.0 * scale[1])
    te.end_fill()
    Moveto(542.0 * scale[0], 1294.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(10.0 * scale[0], -10.0 * scale[1], 20.0 * scale[0], -
              16.0 * scale[1], 22.0 * scale[0], -13.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              11.0 * scale[1], -17.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 13.0 * scale[1], -21.0 * scale[0],
              12.0 * scale[1], -5.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(463.0 * scale[0], 1272.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -4.0 * scale[1], -19.0 * scale[0], -
              24.0 * scale[1], -27.0 * scale[0], -44.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -29.0 * scale[1], -13.0 *
              scale[0], -41.0 * scale[1], -3.0 * scale[0], -62.0 * scale[1])
    Curveto_r(7.0 * scale[0], -14.0 * scale[1], 16.0 * scale[0], -
              26.0 * scale[1], 20.0 * scale[0], -26.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 5.0 * scale[0], -
              6.0 * scale[1], 1.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -10.0 * scale[1], -4.0 *
              scale[0], -10.0 * scale[1], 7.0 * scale[0], 0.0 * scale[1])
    Curveto_r(16.0 * scale[0], 15.0 * scale[1], 49.0 * scale[0],
              16.0 * scale[1], 49.0 * scale[0], 2.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 9.0 * scale[0], -
              2.0 * scale[1], 21.0 * scale[0], 9.0 * scale[1])
    Curveto_r(18.0 * scale[0], 16.0 * scale[1], 19.0 * scale[0],
              22.0 * scale[1], 7.0 * scale[0], 40.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 18.0 * scale[1], -11.0 * scale[0],
              23.0 * scale[1], 1.0 * scale[0], 30.0 * scale[1])
    Curveto_r(11.0 * scale[0], 7.0 * scale[1], 9.0 * scale[0],
              15.0 * scale[1], -10.0 * scale[0], 40.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 31.0 * scale[1], -43.0 * scale[0],
              38.0 * scale[1], -66.0 * scale[0], 23.0 * scale[1])
    te.end_fill()
    Moveto(121.0 * scale[0], 1256.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -9.0 * scale[1], -11.0 * scale[0], -
              19.0 * scale[1], -7.0 * scale[0], -23.0 * scale[1])
    Curveto_r(9.0 * scale[0], -9.0 * scale[1], 29.0 * scale[0],
              13.0 * scale[1], 24.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              7.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(175.0 * scale[0], 1240.0 * scale[1], x, y)
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
    Moveto(792.0 * scale[0], 1225.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(880.0 * scale[0], 1246.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 11.0 * scale[0], -
              6.0 * scale[1], 25.0 * scale[0], -8.0 * scale[1])
    Curveto_r(13.0 * scale[0], -3.0 * scale[1], 22.0 *
              scale[0], -1.0 * scale[1], 19.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 9.0 * scale[1], -44.0 * scale[0],
              13.0 * scale[1], -44.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(62.0 * scale[0], 1205.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(191.0 * scale[0], 1194.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(911.0 * scale[0], 1191.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -5.0 * scale[1], -12.0 * scale[0], -
              14.0 * scale[1], -10.0 * scale[0], -20.0 * scale[1])
    Curveto_r(2.0 * scale[0], -6.0 * scale[1], 10.0 *
              scale[0], -2.0 * scale[1], 17.0 * scale[0], 9.0 * scale[1])
    Curveto_r(14.0 * scale[0], 22.0 * scale[1], 13.0 * scale[0],
              23.0 * scale[1], -7.0 * scale[0], 11.0 * scale[1])
    te.end_fill()
    Moveto(171.0 * scale[0], 1174.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(827.0 * scale[0], 1183.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(13.0 * scale[0], -2.0 * scale[1], 24.0 * scale[0], -
              13.0 * scale[1], 26.0 * scale[0], -26.0 * scale[1])
    Curveto_r(4.0 * scale[0], -18.0 * scale[1], 5.0 *
              scale[0], -17.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(1.0 * scale[0], 23.0 * scale[1], -3.0 * scale[0],
              27.0 * scale[1], -26.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-23.0 * scale[0], -1.0 * scale[1], -24.0 *
              scale[0], -2.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(54.0 * scale[0], 977.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-20.0 * scale[0], -41.0 * scale[1], -12.0 *
              scale[0], -69.0 * scale[1], 20.0 * scale[0], -75.0 * scale[1])
    Curveto_r(36.0 * scale[0], -7.0 * scale[1], 59.0 * scale[0],
              34.0 * scale[1], 33.0 * scale[0], 60.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 7.0 * scale[1], -18.0 * scale[0],
              22.0 * scale[1], -24.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 18.0 * scale[1], -13.0 * scale[0],
              17.0 * scale[1], -29.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(60.0 * scale[0], 855.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-34.0 * scale[0], -41.0 * scale[1], -3.0 * scale[0], -
              114.0 * scale[1], 38.0 * scale[0], -89.0 * scale[1])
    Curveto_r(26.0 * scale[0], 17.0 * scale[1], 26.0 * scale[0],
              41.0 * scale[1], -1.0 * scale[0], 74.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 25.0 * scale[1], -27.0 * scale[0],
              27.0 * scale[1], -37.0 * scale[0], 15.0 * scale[1])
    te.end_fill()
    Moveto(412.0 * scale[0], 708.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-46.0 * scale[0], -46.0 * scale[1], -53.0 *
              scale[0], -58.0 * scale[1], -54.0 * scale[0], -88.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -17.0 * scale[1], -5.0 * scale[0], -
              30.0 * scale[1], -11.0 * scale[0], -30.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -36.0 * scale[0], -
              32.0 * scale[1], -36.0 * scale[0], -50.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -8.0 * scale[1], 8.0 * scale[0], -
              26.0 * scale[1], 19.0 * scale[0], -40.0 * scale[1])
    Curveto_r(11.0 * scale[0], -14.0 * scale[1], 18.0 * scale[0], -
              18.0 * scale[1], 15.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 22.0 * scale[1], 18.0 * scale[0],
              49.0 * scale[1], 52.0 * scale[0], 56.0 * scale[1])
    Curveto_r(25.0 * scale[0], 5.0 * scale[1], 34.0 * scale[0],
              1.0 * scale[1], 47.0 * scale[0], -17.0 * scale[1])
    Curveto_r(24.0 * scale[0], -35.0 * scale[1], 20.0 * scale[0], -
              87.0 * scale[1], -9.0 * scale[0], -125.0 * scale[1])
    Curveto_r(-22.0 * scale[0], -29.0 * scale[1], -23.0 *
              scale[0], -34.0 * scale[1], -9.0 * scale[0], -42.0 * scale[1])
    Curveto_r(9.0 * scale[0], -5.0 * scale[1], 14.0 * scale[0], -
              13.0 * scale[1], 13.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -5.0 * scale[1], 14.0 * scale[0], -
              15.0 * scale[1], 36.0 * scale[0], -22.0 * scale[1])
    Curveto_r(31.0 * scale[0], -10.0 * scale[1], 49.0 *
              scale[0], -11.0 * scale[1], 78.0 * scale[0], -2.0 * scale[1])
    Curveto_r(20.0 * scale[0], 6.0 * scale[1], 37.0 * scale[0],
              15.0 * scale[1], 37.0 * scale[0], 21.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 4.0 * scale[0],
              7.0 * scale[1], 10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 3.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 11.0 * scale[1], -3.0 * scale[0],
              15.0 * scale[1], 5.0 * scale[0], 10.0 * scale[1])
    Curveto_r(16.0 * scale[0], -10.0 * scale[1], 6.0 * scale[0],
              31.0 * scale[1], -12.0 * scale[0], 50.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 24.0 * scale[1], -20.0 * scale[0],
              86.0 * scale[1], 7.0 * scale[0], 112.0 * scale[1])
    Curveto_r(25.0 * scale[0], 24.0 * scale[1], 67.0 * scale[0],
              30.0 * scale[1], 67.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], 5.0 * scale[0], -
              5.0 * scale[1], 11.0 * scale[0], 5.0 * scale[1])
    Curveto_r(21.0 * scale[0], 36.0 * scale[1], 0.0 * scale[0],
              98.0 * scale[1], -51.0 * scale[0], 147.0 * scale[1])
    Curveto_r(-47.0 * scale[0], 45.0 * scale[1], -47.0 * scale[0],
              45.0 * scale[1], -118.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-65.0 * scale[0], 0.0 * scale[1], -75.0 * scale[0], -
              3.0 * scale[1], -100.0 * scale[0], -27.0 * scale[1])
    te.end_fill()
    Moveto(55.0 * scale[0], 700.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-26.0 * scale[0], -51.0 * scale[1], 2.0 * scale[0], -
              93.0 * scale[1], 46.0 * scale[0], -70.0 * scale[1])
    Curveto_r(25.0 * scale[0], 14.0 * scale[1], 24.0 * scale[0],
              29.0 * scale[1], -5.0 * scale[0], 69.0 * scale[1])
    Lineto_r(-25.0 * scale[0], 33.0 * scale[1])
    Lineto_r(-16.0 * scale[0], -32.0 * scale[1])
    te.end_fill()
    Moveto(62.0 * scale[0], 577.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-37.0 * scale[0], -44.0 * scale[1], -8.0 * scale[0], -
              112.0 * scale[1], 37.0 * scale[0], -87.0 * scale[1])
    Curveto_r(27.0 * scale[0], 14.0 * scale[1], 26.0 * scale[0],
              36.0 * scale[1], -3.0 * scale[0], 71.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 21.0 * scale[1], -27.0 * scale[0],
              25.0 * scale[1], -34.0 * scale[0], 16.0 * scale[1])
    te.end_fill()
    Moveto(435.0 * scale[0], 112.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -4.0 * scale[1], -11.0 *
              scale[0], -7.0 * scale[1], -17.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0], -
              10.0 * scale[1], -19.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -18.0 * scale[1], -5.0 *
              scale[0], -21.0 * scale[1], 8.0 * scale[0], -16.0 * scale[1])
    Curveto_r(12.0 * scale[0], 5.0 * scale[1], 14.0 * scale[0],
              3.0 * scale[1], 8.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -10.0 * scale[1], -3.0 *
              scale[0], -12.0 * scale[1], 13.0 * scale[0], -8.0 * scale[1])
    Curveto_r(12.0 * scale[0], 4.0 * scale[1], 22.0 * scale[0],
              2.0 * scale[1], 22.0 * scale[0], -2.0 * scale[1])
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], 113.0 * scale[0], -
              22.0 * scale[1], 141.0 * scale[0], -12.0 * scale[1])
    Curveto_r(23.0 * scale[0], 9.0 * scale[1], 37.0 * scale[0],
              42.0 * scale[1], 17.0 * scale[0], 42.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0],
              6.0 * scale[1], -8.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 21.0 * scale[1], -32.0 * scale[0],
              25.0 * scale[1], -76.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-33.0 * scale[0], -11.0 * scale[1], -42.0 *
              scale[0], -11.0 * scale[1], -60.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 8.0 * scale[1], -25.0 * scale[0],
              11.0 * scale[1], -29.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(0.0 * scale[0], 15.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 7.0 * scale[0], -
              15.0 * scale[1], 16.0 * scale[0], -15.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0],
              3.0 * scale[1], 4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 19.0 * scale[1], -20.0 * scale[0],
              19.0 * scale[1], -20.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(850.0 * scale[0], 10.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-135.0 * scale[0], -6.0 * scale[1])
    Lineto_r(138.0 * scale[0], -2.0 * scale[1])
    Curveto_r(86.0 * scale[0], -1.0 * scale[1], 137.0 * scale[0],
              2.0 * scale[1], 137.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -1.0 * scale[0],
              9.0 * scale[1], -2.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -1.0 * scale[1], -64.0 * scale[0], -
              5.0 * scale[1], -138.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(433.0 * scale[0], 3.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(54.0 * scale[0], -2.0 * scale[1], 139.0 *
              scale[0], -2.0 * scale[1], 190.0 * scale[0], 0.0 * scale[1])
    Curveto_r(51.0 * scale[0], 1.0 * scale[1], 7.0 * scale[0],
              3.0 * scale[1], -98.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-104.0 * scale[0], 0.0 * scale[1], -146.0 *
              scale[0], -2.0 * scale[1], -92.0 * scale[0], -3.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#a08538')
    te.end_fill()
    Moveto(128.0 * scale[0], 1423.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(318.0 * scale[0], 1423.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(460.0 * scale[0], 1421.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], -11.0 * scale[0], -
              12.0 * scale[1], -47.0 * scale[0], -6.0 * scale[1])
    Lineto_r(-48.0 * scale[0], 7.0 * scale[1])
    Lineto_r(28.0 * scale[0], -23.0 * scale[1])
    Curveto_r(24.0 * scale[0], -18.0 * scale[1], 31.0 *
              scale[0], -20.0 * scale[1], 38.0 * scale[0], -8.0 * scale[1])
    Curveto_r(7.0 * scale[0], 12.0 * scale[1], 9.0 * scale[0],
              12.0 * scale[1], 10.0 * scale[0], -1.0 * scale[1])
    Curveto_r(1.0 * scale[0], -8.0 * scale[1], 1.0 * scale[0], -
              18.0 * scale[1], 0.0 * scale[0], -22.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 6.0 * scale[0], -
              5.0 * scale[1], 14.0 * scale[0], -2.0 * scale[1])
    Curveto_r(10.0 * scale[0], 4.0 * scale[1], 15.0 * scale[0],
              0.0 * scale[1], 15.0 * scale[0], -14.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 7.0 * scale[0], -
              23.0 * scale[1], 16.0 * scale[0], -26.0 * scale[1])
    Curveto_r(23.0 * scale[0], -9.0 * scale[1], 34.0 *
              scale[0], -7.0 * scale[1], 34.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -4.0 * scale[0],
              8.0 * scale[1], -9.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -7.0 * scale[1], -8.0 * scale[0],
              21.0 * scale[1], 4.0 * scale[0], 31.0 * scale[1])
    Curveto_r(4.0 * scale[0], 4.0 * scale[1], 5.0 * scale[0],
              2.0 * scale[1], 1.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -8.0 * scale[1], -1.0 * scale[0], -
              13.0 * scale[1], 9.0 * scale[0], -13.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0],
              9.0 * scale[1], 22.0 * scale[0], 19.0 * scale[1])
    Curveto_r(3.0 * scale[0], 12.0 * scale[1], 11.0 * scale[0],
              17.0 * scale[1], 19.0 * scale[0], 14.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 14.0 * scale[0],
              0.0 * scale[1], 14.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -10.0 * scale[0],
              14.0 * scale[1], -22.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 7.0 * scale[1], -22.0 * scale[0],
              7.0 * scale[1], -3.0 * scale[0], 15.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 18.0 * scale[0],
              8.0 * scale[1], 2.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 1.0 * scale[1], -28.0 * scale[0], -
              4.0 * scale[1], -39.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -8.0 * scale[1], -19.0 *
              scale[0], -8.0 * scale[1], -14.0 * scale[0], 0.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], 0.0 * scale[0],
              11.0 * scale[1], -8.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0], -
              6.0 * scale[1], -16.0 * scale[0], -12.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], -4.0 * scale[0], -
              8.0 * scale[1], -10.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 12.0 * scale[1], -10.0 * scale[0],
              12.0 * scale[1], -10.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(610.0 * scale[0], 1420.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(16.0 * scale[0], -5.0 * scale[1], 19.0 *
              scale[0], -8.0 * scale[1], 8.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -1.0 * scale[1], -20.0 * scale[0], -
              7.0 * scale[1], -24.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], -4.0 *
              scale[0], -10.0 * scale[1], 0.0 * scale[0], -6.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], 24.0 * scale[0], -
              1.0 * scale[1], 44.0 * scale[0], -10.0 * scale[1])
    Curveto_r(20.0 * scale[0], -8.0 * scale[1], 57.0 * scale[0], -
              19.0 * scale[1], 82.0 * scale[0], -22.0 * scale[1])
    Curveto_r(44.0 * scale[0], -7.0 * scale[1], 44.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 0.0 * scale[1], -53.0 * scale[0],
              6.0 * scale[1], -72.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-50.0 * scale[0], 21.0 * scale[1], -57.0 * scale[0],
              19.0 * scale[1], -57.0 * scale[0], -15.0 * scale[1])
    Curveto_r(0.0 * scale[0], -21.0 * scale[1], 5.0 * scale[0], -
              30.0 * scale[1], 16.0 * scale[0], -30.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0], -
              1.0 * scale[1], 0.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -9.0 * scale[1], -21.0 * scale[0], -
              12.0 * scale[1], -28.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 5.0 * scale[1], -5.0 * scale[0], -
              4.0 * scale[1], 5.0 * scale[0], -20.0 * scale[1])
    Curveto_r(10.0 * scale[0], -15.0 * scale[1], 16.0 * scale[0], -
              30.0 * scale[1], 13.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], -1.0 * scale[0], -
              12.0 * scale[1], 5.0 * scale[0], -19.0 * scale[1])
    Curveto_r(7.0 * scale[0], -9.0 * scale[1], 7.0 * scale[0], -
              19.0 * scale[1], 0.0 * scale[0], -32.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -11.0 * scale[1], -7.0 * scale[0], -
              23.0 * scale[1], -3.0 * scale[0], -26.0 * scale[1])
    Curveto_r(4.0 * scale[0], -4.0 * scale[1], -4.0 * scale[0], -
              16.0 * scale[1], -18.0 * scale[0], -28.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -11.0 * scale[1], -19.0 *
              scale[0], -16.0 * scale[1], -11.0 * scale[0], -12.0 * scale[1])
    Curveto_r(9.0 * scale[0], 4.0 * scale[1], 12.0 * scale[0],
              2.0 * scale[1], 9.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -9.0 * scale[0], -
              14.0 * scale[1], -14.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              4.0 * scale[1], -21.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -5.0 * scale[1], -17.0 *
              scale[0], -5.0 * scale[1], -23.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0],
              1.0 * scale[1], -10.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -17.0 * scale[1], -47.0 *
              scale[0], -13.0 * scale[1], -64.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 8.0 * scale[1], -20.0 * scale[0],
              13.0 * scale[1], -25.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -13.0 * scale[0],
              0.0 * scale[1], -18.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 13.0 * scale[1], -9.0 * scale[0],
              19.0 * scale[1], -12.0 * scale[0], 39.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 8.0 * scale[1], -6.0 * scale[0],
              8.0 * scale[1], -16.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -7.0 * scale[1], -15.0 *
              scale[0], -8.0 * scale[1], -15.0 * scale[0], -3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -26.0 * scale[0],
              13.0 * scale[1], -58.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-32.0 * scale[0], 4.0 * scale[1], -66.0 * scale[0],
              9.0 * scale[1], -75.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 3.0 * scale[1], -17.0 * scale[0],
              1.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 6.0 * scale[0], -
              13.0 * scale[1], 13.0 * scale[0], -15.0 * scale[1])
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], -1.0 * scale[0], -
              3.0 * scale[1], -18.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-53.0 * scale[0], 7.0 * scale[1], -13.0 * scale[0], -
              15.0 * scale[1], 66.0 * scale[0], -37.0 * scale[1])
    Curveto_r(41.0 * scale[0], -11.0 * scale[1], 79.0 * scale[0], -
              25.0 * scale[1], 84.0 * scale[0], -30.0 * scale[1])
    Curveto_r(6.0 * scale[0], -6.0 * scale[1], -2.0 * scale[0], -
              6.0 * scale[1], -19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-62.0 * scale[0], 23.0 * scale[1], -176.0 * scale[0],
              43.0 * scale[1], -176.0 * scale[0], 31.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], 57.0 * scale[0], -
              34.0 * scale[1], 105.0 * scale[0], -50.0 * scale[1])
    Curveto_r(11.0 * scale[0], -3.0 * scale[1], 94.0 * scale[0], -
              4.0 * scale[1], 185.0 * scale[0], -1.0 * scale[1])
    Curveto_r(91.0 * scale[0], 3.0 * scale[1], 169.0 * scale[0],
              2.0 * scale[1], 174.0 * scale[0], -2.0 * scale[1])
    Curveto_r(12.0 * scale[0], -10.0 * scale[1], 103.0 *
              scale[0], -10.0 * scale[1], 136.0 * scale[0], -1.0 * scale[1])
    Lineto_r(25.0 * scale[0], 7.0 * scale[1])
    Lineto_r(-30.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 5.0 * scale[1], -18.0 * scale[0],
              7.0 * scale[1], 30.0 * scale[0], 10.0 * scale[1])
    Curveto_r(33.0 * scale[0], 1.0 * scale[1], 68.0 * scale[0],
              3.0 * scale[1], 77.0 * scale[0], 3.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0],
              4.0 * scale[1], 11.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], -14.0 * scale[0],
              7.0 * scale[1], -24.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -3.0 * scale[1], -19.0 * scale[0],
              0.0 * scale[1], -19.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -7.0 * scale[0],
              14.0 * scale[1], -15.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0],
              3.0 * scale[1], -13.0 * scale[0], 8.0 * scale[1])
    Curveto_r(2.0 * scale[0], 13.0 * scale[1], -14.0 * scale[0],
              42.0 * scale[1], -22.0 * scale[0], 37.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -2.0 * scale[1], -15.0 * scale[0],
              4.0 * scale[1], -25.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 18.0 * scale[1], -16.0 * scale[0],
              18.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 17.0 *
              scale[0], -2.0 * scale[1], 11.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 3.0 * scale[1], -13.0 * scale[0],
              12.0 * scale[1], -13.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -6.0 * scale[0],
              14.0 * scale[1], -12.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 1.0 * scale[1], -6.0 * scale[0],
              6.0 * scale[1], 5.0 * scale[0], 14.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              16.0 * scale[1], 17.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], 11.0 * scale[0],
              17.0 * scale[1], 25.0 * scale[0], 30.0 * scale[1])
    Curveto_r(30.0 * scale[0], 28.0 * scale[1], 31.0 * scale[0],
              33.0 * scale[1], 8.0 * scale[0], 39.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              5.0 * scale[1], 12.0 * scale[0], 6.0 * scale[1])
    Curveto_r(36.0 * scale[0], 2.0 * scale[1], 72.0 * scale[0],
              21.0 * scale[1], 40.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -49.0 * scale[0],
              9.0 * scale[1], -83.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-35.0 * scale[0], 11.0 * scale[1], -83.0 * scale[0],
              21.0 * scale[1], -105.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-40.0 * scale[0], 1.0 * scale[1], -40.0 * scale[0],
              2.0 * scale[1], -12.0 * scale[0], 9.0 * scale[1])
    Curveto_r(25.0 * scale[0], 6.0 * scale[1], 20.0 * scale[0],
              8.0 * scale[1], -25.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-42.0 * scale[0], 0.0 * scale[1], -49.0 *
              scale[0], -2.0 * scale[1], -30.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto_r(113.0 * scale[0], -307.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-24.0 * scale[0], -2.0 * scale[1], -62.0 *
              scale[0], -2.0 * scale[1], -86.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 2.0 * scale[1], -4.0 * scale[0],
              4.0 * scale[1], 43.0 * scale[0], 4.0 * scale[1])
    Curveto_r(47.0 * scale[0], 0.0 * scale[1], 66.0 * scale[0], -
              2.0 * scale[1], 43.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(189.0 * scale[0], 1391.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-40.0 * scale[0], -20.0 * scale[1], -43.0 *
              scale[0], -21.0 * scale[1], -66.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-29.0 * scale[0], -1.0 * scale[1], 69.0 * scale[0], -
              29.0 * scale[1], 107.0 * scale[0], -30.0 * scale[1])
    Curveto_r(30.0 * scale[0], -2.0 * scale[1], 31.0 *
              scale[0], -3.0 * scale[1], 8.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-37.0 * scale[0], -6.0 * scale[1], -25.0 *
              scale[0], -33.0 * scale[1], 15.0 * scale[0], -33.0 * scale[1])
    Curveto_r(44.0 * scale[0], 0.0 * scale[1], 30.0 * scale[0], -
              6.0 * scale[1], -26.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-35.0 * scale[0], -3.0 * scale[1], -46.0 *
              scale[0], -2.0 * scale[1], -38.0 * scale[0], 6.0 * scale[1])
    Curveto_r(6.0 * scale[0], 6.0 * scale[1], 11.0 * scale[0],
              15.0 * scale[1], 11.0 * scale[0], 21.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -7.0 * scale[0],
              1.0 * scale[1], -15.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -17.0 * scale[1], -12.0 *
              scale[0], -20.0 * scale[1], 1.0 * scale[0], -31.0 * scale[1])
    Curveto_r(9.0 * scale[0], -6.0 * scale[1], 14.0 * scale[0], -
              16.0 * scale[1], 11.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              15.0 * scale[1], 4.0 * scale[0], -23.0 * scale[1])
    Curveto_r(7.0 * scale[0], -13.0 * scale[1], 9.0 *
              scale[0], -13.0 * scale[1], 9.0 * scale[0], 0.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], 15.0 * scale[0],
              14.0 * scale[1], 86.0 * scale[0], 12.0 * scale[1])
    Curveto_r(97.0 * scale[0], -4.0 * scale[1], 127.0 * scale[0],
              9.0 * scale[1], 73.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-27.0 * scale[0], 12.0 * scale[1], -30.0 * scale[0],
              15.0 * scale[1], -16.0 * scale[0], 21.0 * scale[1])
    Curveto_r(11.0 * scale[0], 4.0 * scale[1], 16.0 * scale[0],
              3.0 * scale[1], 12.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 3.0 * scale[0], -
              10.0 * scale[1], 14.0 * scale[0], -10.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 23.0 * scale[0],
              5.0 * scale[1], 27.0 * scale[0], 12.0 * scale[1])
    Curveto_r(4.0 * scale[0], 7.0 * scale[1], 3.0 * scale[0],
              8.0 * scale[1], -4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -7.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -14.0 * scale[0], 52.0 * scale[1])
    Curveto_r(0.0 * scale[0], 23.0 * scale[1], -7.0 * scale[0],
              36.0 * scale[1], -22.0 * scale[0], 44.0 * scale[1])
    Curveto_r(-33.0 * scale[0], 19.0 * scale[1], -138.0 * scale[0],
              17.0 * scale[1], -177.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto_r(128.0 * scale[0], -107.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 17.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(224.0 * scale[0], 1219.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -16.0 * scale[1], 8.0 * scale[0], -
              29.0 * scale[1], 52.0 * scale[0], -40.0 * scale[1])
    Curveto_r(64.0 * scale[0], -14.0 * scale[1], 114.0 *
              scale[0], -11.0 * scale[1], 114.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], -6.0 * scale[0],
              14.0 * scale[1], -15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -7.0 * scale[1], -19.0 *
              scale[0], 4.0 * scale[1], 3.0 * scale[0], 20.0 * scale[1])
    Curveto_r(15.0 * scale[0], 11.0 * scale[1], 5.0 * scale[0],
              13.0 * scale[1], -65.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-48.0 * scale[0], 0.0 * scale[1], -85.0 * scale[0], -
              4.0 * scale[1], -89.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(165.0 * scale[0], 1080.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 16.0 * scale[0], -
              10.0 * scale[1], 28.0 * scale[0], -9.0 * scale[1])
    Curveto_r(21.0 * scale[0], 0.0 * scale[1], 21.0 * scale[0],
              1.0 * scale[1], 2.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-28.0 * scale[0], 12.0 * scale[1], -37.0 * scale[0],
              12.0 * scale[1], -30.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(226.0 * scale[0], 1039.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-28.0 * scale[0], -3.0 * scale[1], -52.0 * scale[0], -
              11.0 * scale[1], -54.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -7.0 * scale[1], -10.0 * scale[0], -
              12.0 * scale[1], -18.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0], -
              21.0 * scale[1], -14.0 * scale[0], -45.0 * scale[1])
    Curveto_r(6.0 * scale[0], -29.0 * scale[1], 0.0 * scale[0], -
              58.0 * scale[1], -16.0 * scale[0], -77.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -12.0 * scale[1], -13.0 *
              scale[0], -18.0 * scale[1], -6.0 * scale[0], -14.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 12.0 * scale[0],
              2.0 * scale[1], 12.0 * scale[0], -3.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              11.0 * scale[1], 9.0 * scale[0], -11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 23.0 * scale[0],
              58.0 * scale[1], 25.0 * scale[0], 95.0 * scale[1])
    Curveto_r(1.0 * scale[0], 15.0 * scale[1], 38.0 * scale[0],
              34.0 * scale[1], 67.0 * scale[0], 35.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 46.0 * scale[0], -
              7.0 * scale[1], 71.0 * scale[0], -15.0 * scale[1])
    Curveto_r(46.0 * scale[0], -16.0 * scale[1], 68.0 * scale[0], -
              44.0 * scale[1], 68.0 * scale[0], -85.0 * scale[1])
    Curveto_r(0.0 * scale[0], -25.0 * scale[1], 19.0 * scale[0], -
              29.0 * scale[1], 161.0 * scale[0], -32.0 * scale[1])
    Curveto_r(64.0 * scale[0], -2.0 * scale[1], 115.0 * scale[0], -
              6.0 * scale[1], 112.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -5.0 * scale[1], 3.0 * scale[0], -
              8.0 * scale[1], 12.0 * scale[0], -8.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 24.0 * scale[0],
              18.0 * scale[1], 34.0 * scale[0], 43.0 * scale[1])
    Curveto_r(22.0 * scale[0], 50.0 * scale[1], 43.0 * scale[0],
              64.0 * scale[1], 111.0 * scale[0], 73.0 * scale[1])
    Curveto_r(29.0 * scale[0], 4.0 * scale[1], 46.0 * scale[0],
              10.0 * scale[1], 40.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 12.0 * scale[1], -2.0 * scale[0],
              50.0 * scale[1], 23.0 * scale[0], 51.0 * scale[1])
    Curveto_r(14.0 * scale[0], 1.0 * scale[1], 10.0 * scale[0],
              4.0 * scale[1], -13.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 5.0 * scale[1], -116.0 * scale[0],
              11.0 * scale[1], -215.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-102.0 * scale[0], 2.0 * scale[1], -152.0 * scale[0],
              1.0 * scale[1], -115.0 * scale[0], -3.0 * scale[1])
    Curveto_r(55.0 * scale[0], -6.0 * scale[1], 59.0 * scale[0], -
              8.0 * scale[1], 25.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-22.0 * scale[0], -2.0 * scale[1], -32.0 *
              scale[0], -5.0 * scale[1], -23.0 * scale[0], -8.0 * scale[1])
    Curveto_r(14.0 * scale[0], -3.0 * scale[1], 15.0 *
              scale[0], -8.0 * scale[1], 6.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -26.0 * scale[1], -58.0 *
              scale[0], -15.0 * scale[1], -69.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 26.0 * scale[1], -11.0 * scale[0],
              27.0 * scale[1], -97.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-48.0 * scale[0], 0.0 * scale[1], -109.0 *
              scale[0], -3.0 * scale[1], -136.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto_r(347.0 * scale[0], -176.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              5.0 * scale[1], 12.0 * scale[0], 5.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(930.0 * scale[0], 1032.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 9.0 * scale[0], -
              8.0 * scale[1], 20.0 * scale[0], -8.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0],
              4.0 * scale[1], 20.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], -9.0 * scale[0],
              8.0 * scale[1], -20.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -20.0 *
              scale[0], -4.0 * scale[1], -20.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(4.0 * scale[0], 835.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -55.0 * scale[1], 1.0 * scale[0], -
              76.0 * scale[1], 3.0 * scale[0], -47.0 * scale[1])
    Curveto_r(2.0 * scale[0], 29.0 * scale[1], 2.0 * scale[0],
              74.0 * scale[1], 0.0 * scale[0], 100.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 26.0 * scale[1], -3.0 * scale[0],
              2.0 * scale[1], -3.0 * scale[0], -53.0 * scale[1])
    te.end_fill()
    Moveto(901.0 * scale[0], 856.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -64.0 * scale[1], -16.0 * scale[0], -
              106.0 * scale[1], -51.0 * scale[0], -123.0 * scale[1])
    Curveto_r(-22.0 * scale[0], -11.0 * scale[1], -15.0 *
              scale[0], -19.0 * scale[1], 13.0 * scale[0], -14.0 * scale[1])
    Curveto_r(11.0 * scale[0], 2.0 * scale[1], -11.0 * scale[0], -
              37.0 * scale[1], -24.0 * scale[0], -41.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -2.0 * scale[1], -2.0 * scale[0], -
              15.0 * scale[1], 11.0 * scale[0], -31.0 * scale[1])
    Lineto_r(22.0 * scale[0], -28.0 * scale[1])
    Lineto_r(30.0 * scale[0], 46.0 * scale[1])
    Curveto_r(31.0 * scale[0], 47.0 * scale[1], 61.0 * scale[0],
              70.0 * scale[1], 78.0 * scale[0], 60.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 10.0 *
              scale[0], -1.0 * scale[1], 10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -7.0 * scale[0],
              11.0 * scale[1], -16.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0],
              6.0 * scale[1], -8.0 * scale[0], 23.0 * scale[1])
    Curveto_r(8.0 * scale[0], 23.0 * scale[1], 6.0 * scale[0],
              125.0 * scale[1], -2.0 * scale[0], 139.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -18.0 * scale[0],
              8.0 * scale[1], -34.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-29.0 * scale[0], 0.0 * scale[1], -29.0 * scale[0], -
              1.0 * scale[1], -29.0 * scale[0], -54.0 * scale[1])
    te.end_fill()
    Moveto_r(28.0 * scale[0], -142.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -11.0 * scale[1], -15.0 *
              scale[0], -11.0 * scale[1], -25.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 15.0 * scale[1], -18.0 * scale[0],
              14.0 * scale[1], 11.0 * scale[0], 15.0 * scale[1])
    Curveto_r(21.0 * scale[0], 2.0 * scale[1], 24.0 * scale[0], -
              1.0 * scale[1], 14.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto_r(-40.0 * scale[0], -53.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -16.0 * scale[1], -14.0 *
              scale[0], -17.0 * scale[1], -27.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 7.0 * scale[1], -11.0 * scale[0],
              17.0 * scale[1], -8.0 * scale[0], 21.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], 12.0 * scale[0],
              0.0 * scale[1], 17.0 * scale[0], -8.0 * scale[1])
    Curveto_r(9.0 * scale[0], -12.0 * scale[1], 10.0 *
              scale[0], -12.0 * scale[1], 5.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 26.0 * scale[1], 4.0 * scale[0],
              44.0 * scale[1], 16.0 * scale[0], 24.0 * scale[1])
    Curveto_r(5.0 * scale[0], -10.0 * scale[1], 4.0 * scale[0], -
              23.0 * scale[1], -3.0 * scale[0], -36.0 * scale[1])
    te.end_fill()
    Moveto(140.0 * scale[0], 836.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              17.0 * scale[1], 9.0 * scale[0], -20.0 * scale[1])
    Curveto_r(5.0 * scale[0], -4.0 * scale[1], 7.0 * scale[0],
              3.0 * scale[1], 4.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 23.0 * scale[1], -13.0 * scale[0],
              26.0 * scale[1], -13.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(179.0 * scale[0], 767.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(24.0 * scale[0], -27.0 * scale[1], 41.0 * scale[0], -
              34.0 * scale[1], 41.0 * scale[0], -19.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], -15.0 * scale[0],
              16.0 * scale[1], -32.0 * scale[0], 26.0 * scale[1])
    Lineto_r(-33.0 * scale[0], 19.0 * scale[1])
    Lineto_r(24.0 * scale[0], -26.0 * scale[1])
    te.end_fill()
    Moveto(224.0 * scale[0], 733.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -10.0 * scale[1], -6.0 * scale[0], -
              22.0 * scale[1], -5.0 * scale[0], -27.0 * scale[1])
    Curveto_r(1.0 * scale[0], -5.0 * scale[1], -6.0 * scale[0], -
              3.0 * scale[1], -15.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 9.0 * scale[1], -15.0 * scale[0],
              10.0 * scale[1], -10.0 * scale[0], 1.0 * scale[1])
    Curveto_r(9.0 * scale[0], -15.0 * scale[1], -14.0 * scale[0], -
              40.0 * scale[1], -33.0 * scale[0], -34.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 3.0 * scale[1], -12.0 *
              scale[0], -1.0 * scale[1], -9.0 * scale[0], -14.0 * scale[1])
    Curveto_r(5.0 * scale[0], -21.0 * scale[1], -10.0 * scale[0], -
              40.0 * scale[1], -43.0 * scale[0], -52.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -8.0 * scale[1], -20.0 *
              scale[0], -8.0 * scale[1], 5.0 * scale[0], -20.0 * scale[1])
    Curveto_r(21.0 * scale[0], -9.0 * scale[1], 26.0 *
              scale[0], -9.0 * scale[1], 26.0 * scale[0], 2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], 7.0 * scale[0],
              19.0 * scale[1], 15.0 * scale[0], 26.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 13.0 * scale[0],
              21.0 * scale[1], 10.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 14.0 * scale[1], -2.0 * scale[0],
              17.0 * scale[1], 9.0 * scale[0], 13.0 * scale[1])
    Curveto_r(10.0 * scale[0], -4.0 * scale[1], 18.0 * scale[0],
              0.0 * scale[1], 22.0 * scale[0], 10.0 * scale[1])
    Curveto_r(7.0 * scale[0], 19.0 * scale[1], 30.0 * scale[0],
              21.0 * scale[1], 37.0 * scale[0], 4.0 * scale[1])
    Curveto_r(3.0 * scale[0], -7.0 * scale[1], 6.0 * scale[0], -
              1.0 * scale[1], 6.0 * scale[0], 14.0 * scale[1])
    Curveto_r(1.0 * scale[0], 14.0 * scale[1], 4.0 * scale[0],
              33.0 * scale[1], 7.0 * scale[0], 42.0 * scale[1])
    Curveto_r(8.0 * scale[0], 22.0 * scale[1], -12.0 * scale[0],
              20.0 * scale[1], -22.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(162.0 * scale[0], 720.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-15.0 * scale[0], -25.0 * scale[1], -15.0 *
              scale[0], -33.0 * scale[1], 0.0 * scale[0], -28.0 * scale[1])
    Curveto_r(6.0 * scale[0], 2.0 * scale[1], 13.0 * scale[0],
              14.0 * scale[1], 15.0 * scale[0], 26.0 * scale[1])
    Curveto_r(4.0 * scale[0], 27.0 * scale[1], 1.0 * scale[0],
              27.0 * scale[1], -15.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(2.0 * scale[0], 710.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(19.0 * scale[0], 668.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -17.0 * scale[1], -6.0 * scale[0], -
              438.0 * scale[1], 1.0 * scale[0], -438.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              35.0 * scale[1], 9.0 * scale[0], 77.0 * scale[1])
    Curveto_r(1.0 * scale[0], 121.0 * scale[1], 4.0 * scale[0],
              153.0 * scale[1], 13.0 * scale[0], 147.0 * scale[1])
    Curveto_r(4.0 * scale[0], -3.0 * scale[1], 4.0 * scale[0],
              6.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 35.0 * scale[1], -17.0 * scale[0],
              82.0 * scale[1], -6.0 * scale[0], 80.0 * scale[1])
    Curveto_r(6.0 * scale[0], -1.0 * scale[1], 10.0 * scale[0],
              18.0 * scale[1], 10.0 * scale[0], 42.0 * scale[1])
    Curveto_r(0.0 * scale[0], 24.0 * scale[1], -3.0 * scale[0],
              41.0 * scale[1], -7.0 * scale[0], 38.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -4.0 * scale[1], -12.0 * scale[0],
              12.0 * scale[1], -9.0 * scale[0], 30.0 * scale[1])
    Curveto_r(1.0 * scale[0], 6.0 * scale[1], -8.0 * scale[0],
              11.0 * scale[1], -10.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(42.0 * scale[0], 330.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#afbb61')
    te.end_fill()
    Moveto(183.0 * scale[0], 1423.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(15.0 * scale[0], -2.0 * scale[1], 39.0 *
              scale[0], -2.0 * scale[1], 55.0 * scale[0], 0.0 * scale[1])
    Curveto_r(15.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              4.0 * scale[1], -28.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 0.0 * scale[1], -43.0 *
              scale[0], -2.0 * scale[1], -27.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(278.0 * scale[0], 1423.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(368.0 * scale[0], 1423.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 30.0 *
              scale[0], -2.0 * scale[1], 40.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 0.0 * scale[1], -30.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(438.0 * scale[0], 1423.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(392.0 * scale[0], 1380.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(391.0 * scale[0], 1314.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(601.0 * scale[0], 1214.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(450.0 * scale[0], 1043.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -1.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 9.0 * scale[0], -26.0 * scale[1])
    Curveto_r(12.0 * scale[0], -31.0 * scale[1], 54.0 * scale[0], -
              41.0 * scale[1], 70.0 * scale[0], -15.0 * scale[1])
    Curveto_r(9.0 * scale[0], 15.0 * scale[1], 8.0 * scale[0],
              18.0 * scale[1], -6.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 1.0 * scale[1], 0.0 * scale[0],
              5.0 * scale[1], 22.0 * scale[0], 9.0 * scale[1])
    Curveto_r(37.0 * scale[0], 6.0 * scale[1], 35.0 * scale[0],
              7.0 * scale[1], -28.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-37.0 * scale[0], 2.0 * scale[1], -67.0 * scale[0],
              3.0 * scale[1], -67.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(332.0 * scale[0], 815.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-26.0 * scale[0], -27.0 * scale[1], -55.0 *
              scale[0], -55.0 * scale[1], -66.0 * scale[0], -60.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -8.0 * scale[1], -22.0 * scale[0], -
              36.0 * scale[1], -37.0 * scale[0], -130.0 * scale[1])
    Curveto_r(-23.0 * scale[0], -145.0 * scale[1], -18.0 *
              scale[0], -207.0 * scale[1], 18.0 * scale[0], -230.0 * scale[1])
    Curveto_r(32.0 * scale[0], -21.0 * scale[1], 43.0 *
              scale[0], -11.0 * scale[1], 15.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 10.0 * scale[1], -22.0 * scale[0],
              25.0 * scale[1], -22.0 * scale[0], 33.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -5.0 * scale[0],
              19.0 * scale[1], -12.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 9.0 * scale[1], -9.0 * scale[0],
              12.0 * scale[1], 2.0 * scale[0], 12.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              3.0 * scale[1], 2.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 7.0 * scale[1], -12.0 * scale[0],
              19.0 * scale[1], -12.0 * scale[0], 28.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], 1.0 * scale[0],
              13.0 * scale[1], 10.0 * scale[0], 0.0 * scale[1])
    Curveto_r(7.0 * scale[0], -11.0 * scale[1], 10.0 *
              scale[0], -7.0 * scale[1], 11.0 * scale[0], 20.0 * scale[1])
    Curveto_r(3.0 * scale[0], 50.0 * scale[1], 4.0 * scale[0],
              63.0 * scale[1], 11.0 * scale[0], 80.0 * scale[1])
    Curveto_r(4.0 * scale[0], 8.0 * scale[1], 13.0 * scale[0],
              36.0 * scale[1], 22.0 * scale[0], 63.0 * scale[1])
    Curveto_r(13.0 * scale[0], 42.0 * scale[1], 86.0 * scale[0],
              131.0 * scale[1], 86.0 * scale[0], 104.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              4.0 * scale[1], 15.0 * scale[0], 3.0 * scale[1])
    Curveto_r(8.0 * scale[0], 7.0 * scale[1], 15.0 * scale[0],
              18.0 * scale[1], 15.0 * scale[0], 26.0 * scale[1])
    Curveto_r(0.0 * scale[0], 20.0 * scale[1], 36.0 * scale[0],
              26.0 * scale[1], 103.0 * scale[0], 18.0 * scale[1])
    Curveto_r(34.0 * scale[0], -4.0 * scale[1], 80.0 * scale[0], -
              6.0 * scale[1], 102.0 * scale[0], -6.0 * scale[1])
    Curveto_r(29.0 * scale[0], 1.0 * scale[1], 36.0 * scale[0], -
              1.0 * scale[1], 25.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -8.0 * scale[1], -12.0 *
              scale[0], -10.0 * scale[1], 3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0],
              5.0 * scale[1], 17.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 23.0 * scale[1], 29.0 * scale[0],
              8.0 * scale[1], 44.0 * scale[0], -22.0 * scale[1])
    Curveto_r(18.0 * scale[0], -39.0 * scale[1], 22.0 *
              scale[0], -25.0 * scale[1], 4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 30.0 * scale[1], -31.0 * scale[0],
              34.0 * scale[1], -201.0 * scale[0], 45.0 * scale[1])
    Lineto_r(-108.0 * scale[0], 7.0 * scale[1])
    Lineto_r(-47.0 * scale[0], -50.0 * scale[1])
    te.end_fill()
    Moveto(767.0 * scale[0], 733.0 * scale[1], x, y)
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
    Moveto(942.0 * scale[0], 713.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -10.0 * scale[1], -32.0 *
              scale[0], -36.0 * scale[1], -46.0 * scale[0], -57.0 * scale[1])
    Curveto_r(-25.0 * scale[0], -38.0 * scale[1], -26.0 *
              scale[0], -40.0 * scale[1], -9.0 * scale[0], -59.0 * scale[1])
    Curveto_r(13.0 * scale[0], -15.0 * scale[1], 14.0 *
              scale[0], -18.0 * scale[1], 3.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 6.0 * scale[1], -10.0 * scale[0],
              3.0 * scale[1], 3.0 * scale[0], -12.0 * scale[1])
    Curveto_r(9.0 * scale[0], -11.0 * scale[1], 17.0 * scale[0], -
              24.0 * scale[1], 17.0 * scale[0], -30.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 6.0 * scale[0], -
              13.0 * scale[1], 14.0 * scale[0], -16.0 * scale[1])
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 * scale[0], -
              24.0 * scale[1], 20.0 * scale[0], -46.0 * scale[1])
    Curveto_r(3.0 * scale[0], -23.0 * scale[1], 11.0 * scale[0], -
              41.0 * scale[1], 17.0 * scale[0], -41.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0], -
              4.0 * scale[1], 5.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], 1.0 * scale[0], -
              17.0 * scale[1], 9.0 * scale[0], -27.0 * scale[1])
    Curveto_r(12.0 * scale[0], -17.0 * scale[1], 13.0 * scale[0],
              3.0 * scale[1], 12.0 * scale[0], 150.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 178.0 * scale[1], -6.0 * scale[0],
              192.0 * scale[1], -45.0 * scale[0], 159.0 * scale[1])
    te.end_fill()
    Moveto(777.0 * scale[0], 690.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -12.0 * scale[1], -1.0 *
              scale[0], -35.0 * scale[1], 5.0 * scale[0], -51.0 * scale[1])
    Curveto_r(7.0 * scale[0], -22.0 * scale[1], 6.0 * scale[0], -
              40.0 * scale[1], -6.0 * scale[0], -76.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -53.0 * scale[1], -20.0 *
              scale[0], -89.0 * scale[1], -6.0 * scale[0], -98.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 10.0 * scale[0], -
              14.0 * scale[1], 9.0 * scale[0], -23.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], -3.0 * scale[0], -
              12.0 * scale[1], -6.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 6.0 * scale[1], -9.0 * scale[0],
              12.0 * scale[1], -14.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              4.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(9.0 * scale[0], -15.0 * scale[1], -6.0 * scale[0], -
              61.0 * scale[1], -19.0 * scale[0], -53.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              0.0 * scale[1], 2.0 * scale[0], -8.0 * scale[1])
    Curveto_r(9.0 * scale[0], -9.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 20.0 * scale[0], -3.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], 15.0 * scale[0],
              13.0 * scale[1], 24.0 * scale[0], 17.0 * scale[1])
    Curveto_r(12.0 * scale[0], 4.0 * scale[1], 15.0 * scale[0],
              12.0 * scale[1], 11.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 11.0 * scale[1], -2.0 * scale[0],
              15.0 * scale[1], 4.0 * scale[0], 11.0 * scale[1])
    Curveto_r(10.0 * scale[0], -6.0 * scale[1], 27.0 * scale[0],
              78.0 * scale[1], 19.0 * scale[0], 92.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 3.0 * scale[1], -7.0 * scale[0],
              29.0 * scale[1], -10.0 * scale[0], 56.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 141.0 * scale[1], -20.0 * scale[0],
              149.0 * scale[1], -29.0 * scale[0], 115.0 * scale[1])
    te.end_fill()
    Moveto(4.0 * scale[0], 485.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -116.0 * scale[1], 2.0 * scale[0], -
              161.0 * scale[1], 3.0 * scale[0], -102.0 * scale[1])
    Curveto_r(2.0 * scale[0], 59.0 * scale[1], 2.0 * scale[0],
              154.0 * scale[1], 0.0 * scale[0], 210.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 56.0 * scale[1], -3.0 * scale[0],
              8.0 * scale[1], -3.0 * scale[0], -108.0 * scale[1])
    te.end_fill()
    Moveto(47.0 * scale[0], 623.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -3.0 * scale[1], -7.0 * scale[0], -
              15.0 * scale[1], -7.0 * scale[0], -26.0 * scale[1])
    Curveto_r(0.0 * scale[0], -25.0 * scale[1], 9.0 * scale[0], -
              17.0 * scale[1], 15.0 * scale[0], 12.0 * scale[1])
    Curveto_r(4.0 * scale[0], 22.0 * scale[1], 2.0 * scale[0],
              25.0 * scale[1], -8.0 * scale[0], 14.0 * scale[1])
    te.end_fill()
    Moveto(103.0 * scale[0], 583.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -9.0 * scale[1], 20.0 * scale[0], -
              13.0 * scale[1], 24.0 * scale[0], -9.0 * scale[1])
    Curveto_r(4.0 * scale[0], 4.0 * scale[1], 1.0 * scale[0],
              11.0 * scale[1], -7.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 16.0 * scale[1], -35.0 * scale[0],
              11.0 * scale[1], -17.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(39.0 * scale[0], 472.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -60.0 * scale[1], -12.0 * scale[0], -
              119.0 * scale[1], -11.0 * scale[0], -171.0 * scale[1])
    Curveto_r(1.0 * scale[0], -36.0 * scale[1], -2.0 * scale[0], -
              67.0 * scale[1], -7.0 * scale[0], -70.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -11.0 * scale[0], -
              45.0 * scale[1], -13.0 * scale[0], -94.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -93.0 * scale[1], 6.0 * scale[0], -
              127.0 * scale[1], 41.0 * scale[0], -127.0 * scale[1])
    Curveto_r(29.0 * scale[0], 0.0 * scale[1], 32.0 * scale[0],
              11.0 * scale[1], 13.0 * scale[0], 44.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 26.0 * scale[1], -17.0 * scale[0],
              54.0 * scale[1], -16.0 * scale[0], 171.0 * scale[1])
    Curveto_r(1.0 * scale[0], 141.0 * scale[1], 4.0 * scale[0],
              179.0 * scale[1], 17.0 * scale[0], 191.0 * scale[1])
    Curveto_r(13.0 * scale[0], 13.0 * scale[1], 7.0 * scale[0],
              52.0 * scale[1], -8.0 * scale[0], 58.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -15.0 * scale[0],
              2.0 * scale[1], -16.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(968.0 * scale[0], 66.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-15.0 * scale[0], -40.0 * scale[1], -15.0 *
              scale[0], -46.0 * scale[1], -2.0 * scale[0], -46.0 * scale[1])
    Curveto_r(19.0 * scale[0], 0.0 * scale[1], 26.0 * scale[0],
              20.0 * scale[1], 22.0 * scale[0], 60.0 * scale[1])
    Lineto_r(-3.0 * scale[0], 33.0 * scale[1])
    Lineto_r(-17.0 * scale[0], -47.0 * scale[1])
    te.end_fill()
    Moveto(705.0 * scale[0], 59.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0], -
              12.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 17.0 * scale[1], 1.0 * scale[0],
              20.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    te.penup()
