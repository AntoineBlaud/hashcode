import turtle as te
from helper import *


def ours_femelle(x, y, scale):
    te.penup()
    te.color('#be93ba')
    te.end_fill()
    Moveto(460.0 * scale[0], 1325.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -3.0 * scale[1], 12.0 * scale[0], -
              10.0 * scale[1], 26.0 * scale[0], -15.0 * scale[1])
    Curveto_r(15.0 * scale[0], -6.0 * scale[1], 22.0 * scale[0], -
              14.0 * scale[1], 18.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], -3.0 *
              scale[0], -8.0 * scale[1], 5.0 * scale[0], -4.0 * scale[1])
    Curveto_r(8.0 * scale[0], 6.0 * scale[1], 9.0 * scale[0],
              12.0 * scale[1], 2.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 7.0 * scale[1], -8.0 * scale[0],
              16.0 * scale[1], -4.0 * scale[0], 19.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0],
              7.0 * scale[1], -20.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 0.0 * scale[1], -27.0 *
              scale[0], -2.0 * scale[1], -27.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(128.0 * scale[0], 1313.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(823.0 * scale[0], 1313.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(166.0 * scale[0], 1303.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -4.0 * scale[1], -25.0 *
              scale[0], -6.0 * scale[1], -46.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-47.0 * scale[0], 3.0 * scale[1], -77.0 * scale[0], -
              10.0 * scale[1], -41.0 * scale[0], -19.0 * scale[1])
    Curveto_r(29.0 * scale[0], -7.0 * scale[1], 60.0 * scale[0], -
              47.0 * scale[1], 36.0 * scale[0], -47.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0],
              6.0 * scale[1], -15.0 * scale[0], 13.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -9.0 * scale[0],
              14.0 * scale[1], -20.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 3.0 * scale[1], -20.0 * scale[0],
              2.0 * scale[1], -20.0 * scale[0], -2.0 * scale[1])
    Curveto_r(0.0 * scale[0], -3.0 * scale[1], 9.0 * scale[0], -
              14.0 * scale[1], 20.0 * scale[0], -24.0 * scale[1])
    Curveto_r(12.0 * scale[0], -10.0 * scale[1], 20.0 * scale[0], -
              29.0 * scale[1], 20.0 * scale[0], -49.0 * scale[1])
    Curveto_r(1.0 * scale[0], -29.0 * scale[1], 2.0 * scale[0], -
              31.0 * scale[1], 14.0 * scale[0], -16.0 * scale[1])
    Curveto_r(10.0 * scale[0], 14.0 * scale[1], 15.0 * scale[0],
              15.0 * scale[1], 25.0 * scale[0], 5.0 * scale[1])
    Curveto_r(10.0 * scale[0], -9.0 * scale[1], 10.0 *
              scale[0], -6.0 * scale[1], 2.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 19.0 * scale[1], -7.0 * scale[0],
              29.0 * scale[1], 1.0 * scale[0], 34.0 * scale[1])
    Curveto_r(7.0 * scale[0], 5.0 * scale[1], 8.0 * scale[0],
              3.0 * scale[1], 3.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -9.0 * scale[1], -4.0 *
              scale[0], -11.0 * scale[1], 3.0 * scale[0], -6.0 * scale[1])
    Curveto_r(9.0 * scale[0], 5.0 * scale[1], 9.0 * scale[0],
              13.0 * scale[1], 1.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 25.0 * scale[1], -2.0 * scale[0],
              40.0 * scale[1], 12.0 * scale[0], 19.0 * scale[1])
    Curveto_r(9.0 * scale[0], -12.0 * scale[1], 10.0 *
              scale[0], -11.0 * scale[1], 5.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 10.0 * scale[1], -1.0 * scale[0],
              25.0 * scale[1], 5.0 * scale[0], 32.0 * scale[1])
    Curveto_r(12.0 * scale[0], 14.0 * scale[1], 8.0 * scale[0],
              20.0 * scale[1], -5.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(440.0 * scale[0], 1300.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -3.0 * scale[0], -
              9.0 * scale[1], -8.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 2.0 * scale[1], -16.0 * scale[0], -
              2.0 * scale[1], -27.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -8.0 * scale[1], -13.0 *
              scale[0], -14.0 * scale[1], -6.0 * scale[0], -14.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              7.0 * scale[1], 6.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -11.0 * scale[1], -1.0 *
              scale[0], -22.0 * scale[1], 4.0 * scale[0], -26.0 * scale[1])
    Curveto_r(7.0 * scale[0], -4.0 * scale[1], 8.0 * scale[0],
              1.0 * scale[1], 4.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 12.0 * scale[1], -3.0 * scale[0],
              15.0 * scale[1], 5.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -5.0 * scale[1], 10.0 *
              scale[0], -1.0 * scale[1], 5.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 12.0 * scale[1], -3.0 * scale[0],
              15.0 * scale[1], 6.0 * scale[0], 10.0 * scale[1])
    Curveto_r(7.0 * scale[0], -5.0 * scale[1], 10.0 *
              scale[0], -2.0 * scale[1], 9.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 8.0 * scale[1], 6.0 * scale[0],
              13.0 * scale[1], 20.0 * scale[0], 12.0 * scale[1])
    Curveto_r(27.0 * scale[0], -2.0 * scale[1], 28.0 * scale[0],
              2.0 * scale[1], 2.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 8.0 * scale[1], -20.0 * scale[0],
              8.0 * scale[1], -20.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(872.0 * scale[0], 1293.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -10.0 * scale[1], -7.0 * scale[0], -
              24.0 * scale[1], -4.0 * scale[0], -32.0 * scale[1])
    Curveto_r(2.0 * scale[0], -8.0 * scale[1], -2.0 * scale[0], -
              19.0 * scale[1], -11.0 * scale[0], -26.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -8.0 * scale[1], -13.0 *
              scale[0], -19.0 * scale[1], -7.0 * scale[0], -45.0 * scale[1])
    Curveto_r(4.0 * scale[0], -19.0 * scale[1], 8.0 * scale[0], -
              31.0 * scale[1], 9.0 * scale[0], -26.0 * scale[1])
    Curveto_r(1.0 * scale[0], 5.0 * scale[1], 9.0 * scale[0],
              2.0 * scale[1], 19.0 * scale[0], -5.0 * scale[1])
    Curveto_r(14.0 * scale[0], -11.0 * scale[1], 15.0 *
              scale[0], -11.0 * scale[1], 5.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 8.0 * scale[1], -13.0 * scale[0],
              25.0 * scale[1], -13.0 * scale[0], 39.0 * scale[1])
    Curveto_r(0.0 * scale[0], 23.0 * scale[1], 1.0 * scale[0],
              24.0 * scale[1], 13.0 * scale[0], 6.0 * scale[1])
    Curveto_r(9.0 * scale[0], -11.0 * scale[1], 16.0 * scale[0], -
              14.0 * scale[1], 21.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              14.0 * scale[1], -4.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -9.0 * scale[0],
              14.0 * scale[1], -6.0 * scale[0], 23.0 * scale[1])
    Curveto_r(14.0 * scale[0], 46.0 * scale[1], 14.0 * scale[0],
              72.0 * scale[1], 1.0 * scale[0], 72.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -18.0 * scale[0], -
              8.0 * scale[1], -23.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(41.0 * scale[0], 1284.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(548.0 * scale[0], 1289.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -6.0 * scale[1], -15.0 * scale[0], -
              16.0 * scale[1], -11.0 * scale[0], -26.0 * scale[1])
    Curveto_r(5.0 * scale[0], -12.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], -7.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 5.0 * scale[1], -11.0 * scale[0],
              4.0 * scale[1], -6.0 * scale[0], -4.0 * scale[1])
    Curveto_r(5.0 * scale[0], -8.0 * scale[1], 12.0 * scale[0], -
              9.0 * scale[1], 20.0 * scale[0], -2.0 * scale[1])
    Curveto_r(9.0 * scale[0], 8.0 * scale[1], 11.0 * scale[0],
              2.0 * scale[1], 8.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -25.0 * scale[1], 2.0 * scale[0], -
              35.0 * scale[1], 20.0 * scale[0], -46.0 * scale[1])
    Curveto_r(21.0 * scale[0], -13.0 * scale[1], 22.0 *
              scale[0], -13.0 * scale[1], 9.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 10.0 * scale[1], -10.0 * scale[0],
              24.0 * scale[1], -6.0 * scale[0], 34.0 * scale[1])
    Curveto_r(7.0 * scale[0], 17.0 * scale[1], 8.0 * scale[0],
              16.0 * scale[1], 15.0 * scale[0], -2.0 * scale[1])
    Curveto_r(7.0 * scale[0], -16.0 * scale[1], 9.0 * scale[0], -
              17.0 * scale[1], 9.0 * scale[0], -3.0 * scale[1])
    Curveto_r(1.0 * scale[0], 9.0 * scale[1], -6.0 * scale[0],
              21.0 * scale[1], -14.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -16.0 * scale[0],
              21.0 * scale[1], -17.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 15.0 * scale[1], -3.0 * scale[0],
              27.0 * scale[1], -3.0 * scale[0], 27.0 * scale[1])
    Curveto_r(0.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              5.0 * scale[1], -17.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(798.0 * scale[0], 1282.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              30.0 * scale[1], 15.0 * scale[0], -43.0 * scale[1])
    Lineto_r(19.0 * scale[0], -24.0 * scale[1])
    Lineto_r(-16.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 27.0 * scale[1], -16.0 * scale[0],
              29.0 * scale[1], 16.0 * scale[0], 31.0 * scale[1])
    Curveto_r(27.0 * scale[0], 2.0 * scale[1], 22.0 * scale[0],
              21.0 * scale[1], -5.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 2.0 * scale[1], -26.0 * scale[0], -
              3.0 * scale[1], -29.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(625.0 * scale[0], 1250.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              10.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              9.0 * scale[1], -11.0 * scale[0], -20.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 5.0 * scale[0], -
              20.0 * scale[1], 10.0 * scale[0], -20.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              9.0 * scale[1], 10.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], 5.0 * scale[0],
              20.0 * scale[1], 11.0 * scale[0], 20.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0], -
              6.0 * scale[1], 6.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], 2.0 * scale[0], -
              20.0 * scale[1], 11.0 * scale[0], -28.0 * scale[1])
    Curveto_r(15.0 * scale[0], -12.0 * scale[1], 16.0 *
              scale[0], -11.0 * scale[1], 3.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 11.0 * scale[1], -10.0 * scale[0],
              17.0 * scale[1], -2.0 * scale[0], 17.0 * scale[1])
    Curveto_r(20.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              17.0 * scale[1], -15.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 7.0 * scale[1], -23.0 * scale[0],
              8.0 * scale[1], -19.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(845.0 * scale[0], 1250.0 * scale[1], x, y)
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
    Moveto(333.0 * scale[0], 1236.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -14.0 * scale[1], 4.0 * scale[0], -
              17.0 * scale[1], -8.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 3.0 * scale[1], -13.0 * scale[0],
              2.0 * scale[1], -10.0 * scale[0], -4.0 * scale[1])
    Curveto_r(3.0 * scale[0], -6.0 * scale[1], -1.0 * scale[0], -
              10.0 * scale[1], -10.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              5.0 * scale[1], -10.0 * scale[0], -11.0 * scale[1])
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 9.0 * scale[0], -
              8.0 * scale[1], 12.0 * scale[0], -5.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 12.0 * scale[0], -
              2.0 * scale[1], 20.0 * scale[0], -10.0 * scale[1])
    Curveto_r(9.0 * scale[0], -8.0 * scale[1], 18.0 * scale[0], -
              12.0 * scale[1], 21.0 * scale[0], -9.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -3.0 * scale[0],
              12.0 * scale[1], -14.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 15.0 * scale[1], -18.0 *
              scale[0], 15.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(27.0 * scale[0], -8.0 * scale[1], 29.0 * scale[0],
              9.0 * scale[1], 5.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 16.0 * scale[1], -16.0 * scale[0],
              16.0 * scale[1], -10.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(907.0 * scale[0], 1243.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -9.0 * scale[1], -9.0 *
              scale[0], -23.0 * scale[1], 1.0 * scale[0], -23.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              7.0 * scale[1], 9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], -1.0 * scale[0],
              18.0 * scale[1], -10.0 * scale[0], 8.0 * scale[1])
    te.end_fill()
    Moveto(520.0 * scale[0], 1206.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              17.0 * scale[1], 8.0 * scale[0], -20.0 * scale[1])
    Curveto_r(4.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0],
              4.0 * scale[1], 8.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], -4.0 * scale[0],
              19.0 * scale[1], -8.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              6.0 * scale[1], -8.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(824.0 * scale[0], 1199.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], -2.0 * scale[0], -
              15.0 * scale[1], 3.0 * scale[0], -20.0 * scale[1])
    Curveto_r(5.0 * scale[0], -5.0 * scale[1], 9.0 * scale[0], -
              1.0 * scale[1], 9.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 23.0 * scale[1], -2.0 * scale[0],
              24.0 * scale[1], -12.0 * scale[0], 9.0 * scale[1])
    te.end_fill()
    Moveto(396.0 * scale[0], 1161.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 2.0 * scale[0], -
              15.0 * scale[1], 12.0 * scale[0], -22.0 * scale[1])
    Curveto_r(15.0 * scale[0], -12.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 5.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 9.0 * scale[1], -10.0 * scale[0],
              19.0 * scale[1], -6.0 * scale[0], 22.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], 4.0 * scale[0],
              7.0 * scale[1], 0.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              4.0 * scale[1], -11.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(510.0 * scale[0], 1136.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              17.0 * scale[1], 9.0 * scale[0], -20.0 * scale[1])
    Curveto_r(5.0 * scale[0], -4.0 * scale[1], 7.0 * scale[0],
              3.0 * scale[1], 4.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 23.0 * scale[1], -13.0 * scale[0],
              26.0 * scale[1], -13.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(825.0 * scale[0], 1140.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(640.0 * scale[0], 951.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-41.0 * scale[0], -13.0 * scale[1], -111.0 *
              scale[0], -61.0 * scale[1], -105.0 * scale[0], -71.0 * scale[1])
    Curveto_r(10.0 * scale[0], -16.0 * scale[1], 45.0 *
              scale[0], -11.0 * scale[1], 75.0 * scale[0], 10.0 * scale[1])
    Curveto_r(35.0 * scale[0], 25.0 * scale[1], 58.0 * scale[0],
              17.0 * scale[1], 68.0 * scale[0], -24.0 * scale[1])
    Curveto_r(6.0 * scale[0], -24.0 * scale[1], 4.0 * scale[0], -
              35.0 * scale[1], -11.0 * scale[0], -51.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -20.0 * scale[1], -18.0 *
              scale[0], -20.0 * scale[1], 14.0 * scale[0], -45.0 * scale[1])
    Curveto_r(75.0 * scale[0], -58.0 * scale[1], 119.0 * scale[0], -
              104.0 * scale[1], 119.0 * scale[0], -124.0 * scale[1])
    Curveto_r(1.0 * scale[0], -29.0 * scale[1], 34.0 * scale[0], -
              70.0 * scale[1], 51.0 * scale[0], -63.0 * scale[1])
    Curveto_r(11.0 * scale[0], 4.0 * scale[1], 10.0 * scale[0],
              6.0 * scale[1], -2.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 1.0 * scale[1], -20.0 * scale[0],
              8.0 * scale[1], -23.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 22.0 * scale[1], 3.0 * scale[0],
              32.0 * scale[1], 15.0 * scale[0], 14.0 * scale[1])
    Curveto_r(9.0 * scale[0], -13.0 * scale[1], 10.0 *
              scale[0], -13.0 * scale[1], 8.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 8.0 * scale[1], 5.0 * scale[0],
              31.0 * scale[1], 13.0 * scale[0], 49.0 * scale[1])
    Curveto_r(9.0 * scale[0], 19.0 * scale[1], 14.0 * scale[0],
              40.0 * scale[1], 11.0 * scale[0], 47.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 7.0 * scale[1], 0.0 * scale[0],
              15.0 * scale[1], 6.0 * scale[0], 19.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 11.0 * scale[0],
              19.0 * scale[1], 11.0 * scale[0], 36.0 * scale[1])
    Curveto_r(0.0 * scale[0], 23.0 * scale[1], -4.0 * scale[0],
              29.0 * scale[1], -21.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0],
              6.0 * scale[1], -18.0 * scale[0], 23.0 * scale[1])
    Curveto_r(2.0 * scale[0], 12.0 * scale[1], -3.0 * scale[0],
              33.0 * scale[1], -11.0 * scale[0], 47.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 14.0 * scale[1], -13.0 * scale[0],
              29.0 * scale[1], -12.0 * scale[0], 33.0 * scale[1])
    Curveto_r(1.0 * scale[0], 4.0 * scale[1], -10.0 * scale[0],
              19.0 * scale[1], -24.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 21.0 * scale[1], -37.0 * scale[0],
              25.0 * scale[1], -83.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-31.0 * scale[0], 0.0 * scale[1], -67.0 *
              scale[0], -4.0 * scale[1], -81.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(285.0 * scale[0], 892.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-46.0 * scale[0], -15.0 * scale[1], -87.0 * scale[0], -
              63.0 * scale[1], -101.0 * scale[0], -117.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -25.0 * scale[1], -5.0 * scale[0], -
              28.0 * scale[1], 15.0 * scale[0], -22.0 * scale[1])
    Curveto_r(16.0 * scale[0], 4.0 * scale[1], 21.0 * scale[0],
              1.0 * scale[1], 21.0 * scale[0], -15.0 * scale[1])
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 1.0 * scale[0], -
              19.0 * scale[1], 20.0 * scale[0], 5.0 * scale[1])
    Curveto_r(15.0 * scale[0], 18.0 * scale[1], 18.0 * scale[0],
              33.0 * scale[1], 14.0 * scale[0], 56.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 22.0 * scale[1], -3.0 * scale[0],
              31.0 * scale[1], 7.0 * scale[0], 32.0 * scale[1])
    Curveto_r(28.0 * scale[0], 3.0 * scale[1], 35.0 * scale[0],
              4.0 * scale[1], 59.0 * scale[0], 18.0 * scale[1])
    Curveto_r(14.0 * scale[0], 8.0 * scale[1], 37.0 * scale[0],
              14.0 * scale[1], 52.0 * scale[0], 13.0 * scale[1])
    Curveto_r(31.0 * scale[0], -3.0 * scale[1], 46.0 * scale[0],
              15.0 * scale[1], 28.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 10.0 * scale[1], -12.0 * scale[0],
              8.0 * scale[1], -6.0 * scale[0], -8.0 * scale[1])
    Curveto_r(6.0 * scale[0], -19.0 * scale[1], 5.0 * scale[0], -
              19.0 * scale[1], -8.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 17.0 * scale[1], -61.0 * scale[0],
              21.0 * scale[1], -101.0 * scale[0], 9.0 * scale[1])
    te.end_fill()
    Moveto(67.0 * scale[0], 567.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-37.0 * scale[0], -21.0 * scale[1], -37.0 *
              scale[0], -21.0 * scale[1], -37.0 * scale[0], -86.0 * scale[1])
    Curveto_r(1.0 * scale[0], -60.0 * scale[1], 3.0 * scale[0], -
              69.0 * scale[1], 30.0 * scale[0], -95.0 * scale[1])
    Curveto_r(16.0 * scale[0], -16.0 * scale[1], 32.0 * scale[0], -
              36.0 * scale[1], 35.0 * scale[0], -45.0 * scale[1])
    Curveto_r(6.0 * scale[0], -19.0 * scale[1], 62.0 * scale[0], -
              56.0 * scale[1], 85.0 * scale[0], -56.0 * scale[1])
    Curveto_r(9.0 * scale[0], 1.0 * scale[1], 14.0 * scale[0],
              9.0 * scale[1], 13.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 11.0 * scale[1], 4.0 * scale[0],
              26.0 * scale[1], 12.0 * scale[0], 33.0 * scale[1])
    Curveto_r(11.0 * scale[0], 10.0 * scale[1], 12.0 * scale[0],
              17.0 * scale[1], 3.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 11.0 * scale[1], -14.0 * scale[0],
              23.0 * scale[1], -17.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 12.0 * scale[1], -32.0 * scale[0],
              85.0 * scale[1], -32.0 * scale[0], 134.0 * scale[1])
    Curveto_r(0.0 * scale[0], 51.0 * scale[1], -2.0 * scale[0],
              53.0 * scale[1], -28.0 * scale[0], 54.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -43.0 * scale[0], -
              9.0 * scale[1], -64.0 * scale[0], -21.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#9872ad')
    te.end_fill()
    Moveto(433.0 * scale[0], 1293.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -3.0 * scale[1], 1.0 * scale[0], -
              13.0 * scale[1], -6.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -14.0 * scale[1], -10.0 *
              scale[0], -14.0 * scale[1], 5.0 * scale[0], -2.0 * scale[1])
    Curveto_r(16.0 * scale[0], 12.0 * scale[1], 16.0 * scale[0],
              31.0 * scale[1], 1.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -3.0 *
              scale[0], -3.0 * scale[1], 0.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(515.0 * scale[0], 1290.0 * scale[1], x, y)
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
    Moveto(68.0 * scale[0], 1273.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(535.0 * scale[0], 1270.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(856.0 * scale[0], 1262.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -14.0 * scale[1], 0.0 * scale[0], -
              22.0 * scale[1], -13.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -4.0 * scale[1], -17.0 *
              scale[0], -5.0 * scale[1], 0.0 * scale[0], -6.0 * scale[1])
    Curveto_r(21.0 * scale[0], -1.0 * scale[1], 34.0 * scale[0],
              26.0 * scale[1], 19.0 * scale[0], 41.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 8.0 * scale[1], -9.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(106.0 * scale[0], 1243.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(542.0 * scale[0], 1219.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -20.0 * scale[1], 4.0 * scale[0], -
              42.0 * scale[1], 11.0 * scale[0], -48.0 * scale[1])
    Curveto_r(10.0 * scale[0], -8.0 * scale[1], 14.0 *
              scale[0], -7.0 * scale[1], 14.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -4.0 * scale[0],
              15.0 * scale[1], -8.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0],
              15.0 * scale[1], -12.0 * scale[0], 33.0 * scale[1])
    Lineto_r(-4.0 * scale[0], 32.0 * scale[1])
    Lineto_r(-1.0 * scale[0], -36.0 * scale[1])
    te.end_fill()
    Moveto(139.0 * scale[0], 1223.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -21.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(634.0 * scale[0], 1223.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -10.0 * scale[1], -2.0 * scale[0], -
              21.0 * scale[1], -8.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -6.0 * scale[1], -8.0 *
              scale[0], -8.0 * scale[1], 0.0 * scale[0], -8.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0],
              6.0 * scale[1], 23.0 * scale[0], 14.0 * scale[1])
    Curveto_r(9.0 * scale[0], 10.0 * scale[1], 8.0 * scale[0],
              16.0 * scale[1], -3.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 10.0 * scale[1], -14.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(317.0 * scale[0], 1223.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -8.0 * scale[1], 12.0 * scale[0], -
              33.0 * scale[1], 27.0 * scale[0], -33.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 3.0 * scale[0],
              5.0 * scale[1], -7.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              14.0 * scale[1], -12.0 * scale[0], 20.0 * scale[1])
    Curveto_r(7.0 * scale[0], 10.0 * scale[1], 2.0 * scale[0],
              12.0 * scale[1], -8.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(88.0 * scale[0], 1185.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -22.0 * scale[1], -4.0 * scale[0], -
              41.0 * scale[1], -4.0 * scale[0], -42.0 * scale[1])
    Curveto_r(1.0 * scale[0], -1.0 * scale[1], 12.0 * scale[0],
              0.0 * scale[1], 24.0 * scale[0], 4.0 * scale[1])
    Curveto_r(14.0 * scale[0], 3.0 * scale[1], 22.0 * scale[0],
              13.0 * scale[1], 22.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 21.0 * scale[1], -1.0 * scale[0],
              21.0 * scale[1], -13.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -19.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], -17.0 * scale[0], 15.0 * scale[1])
    Lineto_r(-6.0 * scale[0], 35.0 * scale[1])
    Lineto_r(-6.0 * scale[0], -40.0 * scale[1])
    te.end_fill()
    Moveto(837.0 * scale[0], 1192.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -53.0 * scale[1], 13.0 * scale[0], -
              57.0 * scale[1], 29.0 * scale[0], -34.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 13.0 * scale[0],
              32.0 * scale[1], 11.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 19.0 * scale[1], -4.0 * scale[0],
              18.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -34.0 * scale[1], -21.0 * scale[0], -
              48.0 * scale[1], -21.0 * scale[0], -14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -4.0 * scale[0],
              27.0 * scale[1], -9.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 3.0 * scale[1], -6.0 * scale[0], -
              7.0 * scale[1], -4.0 * scale[0], -22.0 * scale[1])
    te.end_fill()
    Moveto(363.0 * scale[0], 1004.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(28.0 * scale[0], -15.0 * scale[1], 37.0 * scale[0], -
              30.0 * scale[1], 12.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 4.0 * scale[1], -17.0 * scale[0],
              2.0 * scale[1], -20.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -15.0 * scale[1], -25.0 *
              scale[0], -12.0 * scale[1], -25.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -9.0 * scale[0],
              16.0 * scale[1], -19.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 5.0 * scale[1], -41.0 * scale[0], -
              9.0 * scale[1], -41.0 * scale[0], -30.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -16.0 * scale[0], -
              15.0 * scale[1], -35.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-25.0 * scale[0], -4.0 * scale[1], -39.0 * scale[0], -
              14.0 * scale[1], -50.0 * scale[0], -37.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -37.0 * scale[1], -18.0 *
              scale[0], -34.0 * scale[1], 1.0 * scale[0], -41.0 * scale[1])
    Curveto_r(9.0 * scale[0], -3.0 * scale[1], 27.0 * scale[0],
              3.0 * scale[1], 41.0 * scale[0], 14.0 * scale[1])
    Curveto_r(14.0 * scale[0], 11.0 * scale[1], 41.0 * scale[0],
              22.0 * scale[1], 62.0 * scale[0], 25.0 * scale[1])
    Curveto_r(20.0 * scale[0], 4.0 * scale[1], 46.0 * scale[0],
              8.0 * scale[1], 59.0 * scale[0], 11.0 * scale[1])
    Curveto_r(12.0 * scale[0], 2.0 * scale[1], 22.0 * scale[0],
              0.0 * scale[1], 22.0 * scale[0], -6.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -16.0 * scale[0], -
              10.0 * scale[1], -36.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-42.0 * scale[0], 0.0 * scale[1], -102.0 * scale[0], -
              26.0 * scale[1], -126.0 * scale[0], -55.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -11.0 * scale[1], -26.0 *
              scale[0], -41.0 * scale[1], -35.0 * scale[0], -67.0 * scale[1])
    Lineto_r(-17.0 * scale[0], -47.0 * scale[1])
    Lineto_r(-31.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-33.0 * scale[0], 26.0 * scale[1], -95.0 * scale[0],
              44.0 * scale[1], -95.0 * scale[0], 28.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 6.0 * scale[0], -
              13.0 * scale[1], 13.0 * scale[0], -15.0 * scale[1])
    Curveto_r(9.0 * scale[0], -4.0 * scale[1], 9.0 * scale[0], -
              6.0 * scale[1], 0.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -1.0 * scale[1], -13.0 * scale[0], -
              29.0 * scale[1], -13.0 * scale[0], -105.0 * scale[1])
    Curveto_r(0.0 * scale[0], -65.0 * scale[1], -4.0 * scale[0], -
              107.0 * scale[1], -11.0 * scale[0], -112.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -4.0 * scale[1], -10.0 * scale[0], -
              43.0 * scale[1], -7.0 * scale[0], -110.0 * scale[1])
    Lineto_r(3.0 * scale[0], -104.0 * scale[1])
    Lineto_r(62.0 * scale[0], -31.0 * scale[1])
    Curveto_r(42.0 * scale[0], -21.0 * scale[1], 60.0 * scale[0], -
              35.0 * scale[1], 56.0 * scale[0], -45.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -1.0 * scale[0], -
              14.0 * scale[1], 3.0 * scale[0], -14.0 * scale[1])
    Curveto_r(13.0 * scale[0], 1.0 * scale[1], 60.0 * scale[0],
              29.0 * scale[1], 52.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 1.0 * scale[1], -11.0 * scale[0],
              2.0 * scale[1], -15.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 4.0 * scale[1], -74.0 * scale[0],
              42.0 * scale[1], -78.0 * scale[0], 57.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -19.0 * scale[0],
              29.0 * scale[1], -35.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-27.0 * scale[0], 26.0 * scale[1], -29.0 * scale[0],
              35.0 * scale[1], -30.0 * scale[0], 94.0 * scale[1])
    Lineto_r(0.0 * scale[0], 65.0 * scale[1])
    Lineto_r(44.0 * scale[0], 27.0 * scale[1])
    Curveto_r(28.0 * scale[0], 17.0 * scale[1], 47.0 * scale[0],
              23.0 * scale[1], 54.0 * scale[0], 16.0 * scale[1])
    Curveto_r(13.0 * scale[0], -13.0 * scale[1], 42.0 * scale[0],
              18.0 * scale[1], 42.0 * scale[0], 47.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], 13.0 * scale[0],
              35.0 * scale[1], 28.0 * scale[0], 50.0 * scale[1])
    Curveto_r(35.0 * scale[0], 32.0 * scale[1], 34.0 * scale[0],
              76.0 * scale[1], 0.0 * scale[0], 67.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -4.0 * scale[1], -20.0 *
              scale[0], -2.0 * scale[1], -14.0 * scale[0], 22.0 * scale[1])
    Curveto_r(9.0 * scale[0], 35.0 * scale[1], 45.0 * scale[0],
              91.0 * scale[1], 69.0 * scale[0], 106.0 * scale[1])
    Curveto_r(10.0 * scale[0], 6.0 * scale[1], 41.0 * scale[0],
              14.0 * scale[1], 68.0 * scale[0], 17.0 * scale[1])
    Curveto_r(41.0 * scale[0], 5.0 * scale[1], 52.0 * scale[0],
              3.0 * scale[1], 63.0 * scale[0], -13.0 * scale[1])
    Curveto_r(8.0 * scale[0], -10.0 * scale[1], 12.0 * scale[0], -
              22.0 * scale[1], 10.0 * scale[0], -26.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -13.0 * scale[1], 4.0 *
              scale[0], -9.0 * scale[1], 46.0 * scale[0], 12.0 * scale[1])
    Curveto_r(43.0 * scale[0], 22.0 * scale[1], 70.0 * scale[0],
              25.0 * scale[1], 88.0 * scale[0], 10.0 * scale[1])
    Curveto_r(6.0 * scale[0], -6.0 * scale[1], 10.0 *
              scale[0], -7.0 * scale[1], 7.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], 0.0 * scale[0],
              13.0 * scale[1], 7.0 * scale[0], 21.0 * scale[1])
    Curveto_r(8.0 * scale[0], 11.0 * scale[1], 7.0 * scale[0],
              12.0 * scale[1], -6.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -8.0 * scale[1], -21.0 *
              scale[0], 5.0 * scale[1], 0.0 * scale[0], 34.0 * scale[1])
    Curveto_r(13.0 * scale[0], 19.0 * scale[1], 13.0 * scale[0],
              22.0 * scale[1], 1.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0],
              10.0 * scale[1], -20.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 14.0 * scale[1], -11.0 * scale[0],
              20.0 * scale[1], -21.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -3.0 * scale[1], -18.0 *
              scale[0], -2.0 * scale[1], -21.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], -11.0 * scale[0],
              10.0 * scale[1], -17.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              3.0 * scale[1], -5.0 * scale[0], -7.0 * scale[1])
    Curveto_r(11.0 * scale[0], -10.0 * scale[1], -14.0 * scale[0], -
              33.0 * scale[1], -37.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -18.0 * scale[0],
              2.0 * scale[1], -7.0 * scale[0], 9.0 * scale[1])
    Curveto_r(11.0 * scale[0], 7.0 * scale[1], 7.0 * scale[0],
              13.0 * scale[1], -17.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-39.0 * scale[0], 20.0 * scale[1], -67.0 * scale[0],
              20.0 * scale[1], -29.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto_r(47.0 * scale[0], -125.0 * scale[1], 0, 0)
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
    Moveto(725.0 * scale[0], 962.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(43.0 * scale[0], -5.0 * scale[1], 66.0 * scale[0], -
              13.0 * scale[1], 83.0 * scale[0], -29.0 * scale[1])
    Curveto_r(12.0 * scale[0], -13.0 * scale[1], 21.0 * scale[0], -
              26.0 * scale[1], 20.0 * scale[0], -30.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -5.0 * scale[1], 4.0 * scale[0], -
              19.0 * scale[1], 12.0 * scale[0], -33.0 * scale[1])
    Curveto_r(8.0 * scale[0], -14.0 * scale[1], 13.0 * scale[0], -
              35.0 * scale[1], 11.0 * scale[0], -47.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -17.0 * scale[1], 3.0 * scale[0], -
              23.0 * scale[1], 18.0 * scale[0], -23.0 * scale[1])
    Curveto_r(17.0 * scale[0], 0.0 * scale[1], 21.0 * scale[0], -
              6.0 * scale[1], 21.0 * scale[0], -29.0 * scale[1])
    Curveto_r(0.0 * scale[0], -17.0 * scale[1], -5.0 * scale[0], -
              33.0 * scale[1], -11.0 * scale[0], -36.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -4.0 * scale[1], -8.0 * scale[0], -
              12.0 * scale[1], -6.0 * scale[0], -19.0 * scale[1])
    Curveto_r(3.0 * scale[0], -7.0 * scale[1], -2.0 * scale[0], -
              28.0 * scale[1], -11.0 * scale[0], -47.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -18.0 * scale[1], -15.0 * scale[0], -
              41.0 * scale[1], -14.0 * scale[0], -49.0 * scale[1])
    Curveto_r(1.0 * scale[0], -10.0 * scale[1], 0.0 * scale[0], -
              11.0 * scale[1], -4.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 22.0 * scale[1], -26.0 * scale[0],
              13.0 * scale[1], -19.0 * scale[0], -10.0 * scale[1])
    Curveto_r(7.0 * scale[0], -23.0 * scale[1], 7.0 * scale[0], -
              23.0 * scale[1], -10.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 20.0 * scale[1], -16.0 * scale[0],
              20.0 * scale[1], -6.0 * scale[0], -2.0 * scale[1])
    Curveto_r(8.0 * scale[0], -15.0 * scale[1], 17.0 * scale[0], -
              20.0 * scale[1], 32.0 * scale[0], -16.0 * scale[1])
    Curveto_r(14.0 * scale[0], 4.0 * scale[1], 20.0 * scale[0],
              2.0 * scale[1], 16.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], 3.0 * scale[0], -
              13.0 * scale[1], 16.0 * scale[0], -17.0 * scale[1])
    Curveto_r(31.0 * scale[0], -8.0 * scale[1], 31.0 *
              scale[0], -8.0 * scale[1], 57.0 * scale[0], 14.0 * scale[1])
    Curveto_r(22.0 * scale[0], 19.0 * scale[1], 23.0 * scale[0],
              27.0 * scale[1], 22.0 * scale[0], 132.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 62.0 * scale[1], -4.0 * scale[0],
              124.0 * scale[1], -6.0 * scale[0], 138.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 14.0 * scale[1], -5.0 * scale[0],
              28.0 * scale[1], -5.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 4.0 * scale[1], -8.0 * scale[0],
              7.0 * scale[1], -17.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0],
              4.0 * scale[1], -9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], -21.0 * scale[0],
              22.0 * scale[1], -52.0 * scale[0], 38.0 * scale[1])
    Curveto_r(-44.0 * scale[0], 21.0 * scale[1], -74.0 * scale[0],
              28.0 * scale[1], -128.0 * scale[0], 29.0 * scale[1])
    Lineto_r(-70.0 * scale[0], 2.0 * scale[1])
    Lineto_r(60.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(593.0 * scale[0], 939.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-18.0 * scale[0], -12.0 * scale[1], -33.0 *
              scale[0], -23.0 * scale[1], -33.0 * scale[0], -26.0 * scale[1])
    Curveto_r(0.0 * scale[0], -3.0 * scale[1], 12.0 * scale[0],
              3.0 * scale[1], 27.0 * scale[0], 12.0 * scale[1])
    Curveto_r(14.0 * scale[0], 10.0 * scale[1], 38.0 * scale[0],
              21.0 * scale[1], 52.0 * scale[0], 25.0 * scale[1])
    Curveto_r(20.0 * scale[0], 7.0 * scale[1], 22.0 * scale[0],
              8.0 * scale[1], 6.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -35.0 * scale[0], -
              9.0 * scale[1], -52.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(140.0 * scale[0], 840.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 3.0 * scale[0], -
              21.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(9.0 * scale[0], 9.0 * scale[1], 9.0 * scale[0],
              15.0 * scale[1], 0.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 9.0 * scale[1], -12.0 * scale[0],
              7.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(299.0 * scale[0], 833.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -21.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(252.0 * scale[0], 810.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(645.0 * scale[0], 801.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              12.0 * scale[1], 3.0 * scale[0], -15.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 9.0 * scale[0],
              1.0 * scale[1], 9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], -3.0 * scale[0],
              19.0 * scale[1], -12.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(770.0 * scale[0], 686.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(162.0 * scale[0], 480.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(200.0 * scale[0], 335.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -9.0 * scale[1], -11.0 * scale[0], -
              17.0 * scale[1], -9.0 * scale[0], -20.0 * scale[1])
    Curveto_r(3.0 * scale[0], -2.0 * scale[1], 10.0 * scale[0],
              5.0 * scale[1], 17.0 * scale[0], 15.0 * scale[1])
    Curveto_r(14.0 * scale[0], 24.0 * scale[1], 10.0 * scale[0],
              26.0 * scale[1], -8.0 * scale[0], 5.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#523561')
    te.end_fill()
    Moveto(410.0 * scale[0], 1170.0 * scale[1], x, y)
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
    Moveto(470.0 * scale[0], 1130.0 * scale[1], x, y)
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
    Moveto(228.0 * scale[0], 1023.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(29.0 * scale[0], -2.0 * scale[1], 74.0 *
              scale[0], -2.0 * scale[1], 100.0 * scale[0], 0.0 * scale[1])
    Curveto_r(26.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              3.0 * scale[1], -53.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-55.0 * scale[0], 0.0 * scale[1], -76.0 *
              scale[0], -1.0 * scale[1], -47.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(540.0 * scale[0], 1020.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(85.0 * scale[0], -4.0 * scale[1], 163.0 *
              scale[0], -8.0 * scale[1], 172.0 * scale[0], -9.0 * scale[1])
    Curveto_r(11.0 * scale[0], -1.0 * scale[1], 15.0 * scale[0], -
              6.0 * scale[1], 12.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -11.0 * scale[1], 1.0 * scale[0], -
              15.0 * scale[1], 24.0 * scale[0], -15.0 * scale[1])
    Curveto_r(61.0 * scale[0], 0.0 * scale[1], 184.0 * scale[0], -
              62.0 * scale[1], 206.0 * scale[0], -104.0 * scale[1])
    Curveto_r(13.0 * scale[0], -25.0 * scale[1], 15.0 *
              scale[0], -26.0 * scale[1], 10.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 14.0 * scale[1], -8.0 * scale[0],
              50.0 * scale[1], -8.0 * scale[0], 80.0 * scale[1])
    Lineto_r(-1.0 * scale[0], 55.0 * scale[1])
    Lineto_r(-55.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 4.0 * scale[1], -158.0 * scale[0],
              9.0 * scale[1], -285.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-180.0 * scale[0], 4.0 * scale[1], -196.0 * scale[0],
              3.0 * scale[1], -75.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(32.0 * scale[0], 1011.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -8.0 * scale[1], -21.0 * scale[0], -
              111.0 * scale[1], -25.0 * scale[0], -311.0 * scale[1])
    Lineto_r(-4.0 * scale[0], -155.0 * scale[1])
    Lineto_r(6.0 * scale[0], 138.0 * scale[1])
    Curveto_r(4.0 * scale[0], 87.0 * scale[1], 10.0 * scale[0],
              140.0 * scale[1], 17.0 * scale[0], 145.0 * scale[1])
    Curveto_r(15.0 * scale[0], 9.0 * scale[1], 64.0 * scale[0],
              101.0 * scale[1], 64.0 * scale[0], 119.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 7.0 * scale[0],
              27.0 * scale[1], 15.0 * scale[0], 42.0 * scale[1])
    Lineto_r(14.0 * scale[0], 28.0 * scale[1])
    Lineto_r(-39.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 0.0 * scale[1], -43.0 *
              scale[0], -2.0 * scale[1], -48.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(473.0 * scale[0], 873.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 25.0 *
              scale[0], -2.0 * scale[1], 35.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -27.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(671.0 * scale[0], 844.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(343.0 * scale[0], 843.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 25.0 *
              scale[0], -2.0 * scale[1], 35.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -27.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(962.0 * scale[0], 810.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 2.0 * scale[0], -
              27.0 * scale[1], 5.0 * scale[0], -17.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              25.0 * scale[1], 0.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(765.0 * scale[0], 680.0 * scale[1], x, y)
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
    Moveto(194.0 * scale[0], 665.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -13.0 * scale[1], -14.0 * scale[0], -
              29.0 * scale[1], -12.0 * scale[0], -34.0 * scale[1])
    Curveto_r(1.0 * scale[0], -5.0 * scale[1], 11.0 * scale[0],
              6.0 * scale[1], 20.0 * scale[0], 25.0 * scale[1])
    Curveto_r(20.0 * scale[0], 40.0 * scale[1], 16.0 * scale[0],
              45.0 * scale[1], -8.0 * scale[0], 9.0 * scale[1])
    te.end_fill()
    Moveto(166.0 * scale[0], 595.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -9.0 * scale[1], -5.0 * scale[0], -
              33.0 * scale[1], -5.0 * scale[0], -53.0 * scale[1])
    Curveto_r(2.0 * scale[0], -33.0 * scale[1], 2.0 * scale[0], -
              32.0 * scale[1], 9.0 * scale[0], 13.0 * scale[1])
    Curveto_r(8.0 * scale[0], 53.0 * scale[1], 6.0 * scale[0],
              66.0 * scale[1], -4.0 * scale[0], 40.0 * scale[1])
    te.end_fill()
    Moveto(963.0 * scale[0], 555.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -27.0 * scale[1], 2.0 * scale[0], -
              38.0 * scale[1], 4.0 * scale[0], -22.0 * scale[1])
    Curveto_r(2.0 * scale[0], 15.0 * scale[1], 2.0 * scale[0],
              37.0 * scale[1], 0.0 * scale[0], 50.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 12.0 * scale[1], -4.0 * scale[0],
              0.0 * scale[1], -4.0 * scale[0], -28.0 * scale[1])
    te.end_fill()
    Moveto(807.0 * scale[0], 579.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(855.0 * scale[0], 560.0 * scale[1], x, y)
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
    Moveto(890.0 * scale[0], 543.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 69.0 * scale[0], -
              58.0 * scale[1], 74.0 * scale[0], -52.0 * scale[1])
    Curveto_r(3.0 * scale[0], 2.0 * scale[1], -13.0 * scale[0],
              17.0 * scale[1], -35.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 16.0 * scale[1], -39.0 * scale[0],
              25.0 * scale[1], -39.0 * scale[0], 20.0 * scale[1])
    te.end_fill()
    Moveto(180.0 * scale[0], 434.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              18.0 * scale[1], 15.0 * scale[0], -28.0 * scale[1])
    Curveto_r(8.0 * scale[0], -11.0 * scale[1], 15.0 * scale[0], -
              16.0 * scale[1], 15.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -7.0 * scale[0],
              18.0 * scale[1], -15.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 11.0 * scale[1], -15.0 * scale[0],
              16.0 * scale[1], -15.0 * scale[0], 10.0 * scale[1])
    te.end_fill()
    Moveto(3.0 * scale[0], 214.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(2.0 * scale[0], -210.0 * scale[1])
    Lineto_r(23.0 * scale[0], -2.0 * scale[1])
    Curveto_r(22.0 * scale[0], -2.0 * scale[1], 22.0 *
              scale[0], -1.0 * scale[1], 7.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 13.0 * scale[1], -16.0 * scale[0],
              34.0 * scale[1], -14.0 * scale[0], 122.0 * scale[1])
    Curveto_r(3.0 * scale[0], 97.0 * scale[1], -8.0 * scale[0],
              270.0 * scale[1], -17.0 * scale[0], 280.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 2.0 * scale[1], -3.0 * scale[0], -
              90.0 * scale[1], -1.0 * scale[0], -205.0 * scale[1])
    te.end_fill()
    Moveto(177.0 * scale[0], 262.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -10.0 * scale[1], -14.0 *
              scale[0], -21.0 * scale[1], -11.0 * scale[0], -25.0 * scale[1])
    Curveto_r(4.0 * scale[0], -3.0 * scale[1], -3.0 * scale[0], -
              22.0 * scale[1], -14.0 * scale[0], -41.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -20.0 * scale[1], -26.0 *
              scale[0], -64.0 * scale[1], -32.0 * scale[0], -98.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -34.0 * scale[1], -16.0 * scale[0], -
              70.0 * scale[1], -21.0 * scale[0], -80.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -10.0 * scale[1], -6.0 * scale[0], -
              18.0 * scale[1], -1.0 * scale[0], -18.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 30.0 * scale[0],
              42.0 * scale[1], 36.0 * scale[0], 96.0 * scale[1])
    Curveto_r(4.0 * scale[0], 44.0 * scale[1], 22.0 * scale[0],
              97.0 * scale[1], 57.0 * scale[0], 167.0 * scale[1])
    Curveto_r(12.0 * scale[0], 22.0 * scale[1], 6.0 * scale[0],
              22.0 * scale[1], -14.0 * scale[0], -1.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#bd8043')
    te.end_fill()
    Moveto(370.0 * scale[0], 1386.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 92.0 * scale[0], -
              46.0 * scale[1], 114.0 * scale[0], -46.0 * scale[1])
    Curveto_r(43.0 * scale[0], 0.0 * scale[1], 102.0 * scale[0], -
              33.0 * scale[1], 91.0 * scale[0], -50.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -3.0 * scale[1], 8.0 * scale[0], -
              7.0 * scale[1], 21.0 * scale[0], -8.0 * scale[1])
    Curveto_r(35.0 * scale[0], -3.0 * scale[1], 66.0 * scale[0], -
              21.0 * scale[1], 58.0 * scale[0], -34.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -3.0 *
              scale[0], -8.0 * scale[1], 3.0 * scale[0], -5.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 22.0 * scale[0],
              0.0 * scale[1], 37.0 * scale[0], -8.0 * scale[1])
    Curveto_r(17.0 * scale[0], -9.0 * scale[1], 35.0 * scale[0], -
              11.0 * scale[1], 49.0 * scale[0], -6.0 * scale[1])
    Curveto_r(12.0 * scale[0], 4.0 * scale[1], 29.0 * scale[0],
              6.0 * scale[1], 37.0 * scale[0], 3.0 * scale[1])
    Curveto_r(13.0 * scale[0], -5.0 * scale[1], 13.0 *
              scale[0], -3.0 * scale[1], 1.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 10.0 * scale[1], -21.0 * scale[0],
              17.0 * scale[1], -30.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 1.0 * scale[1], -5.0 * scale[0],
              4.0 * scale[1], 9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(18.0 * scale[0], 6.0 * scale[1], 20.0 * scale[0],
              9.0 * scale[1], 8.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 1.0 * scale[1], -22.0 * scale[0],
              3.0 * scale[1], -27.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 5.0 * scale[1], 4.0 * scale[0],
              6.0 * scale[1], 20.0 * scale[0], 2.0 * scale[1])
    Curveto_r(20.0 * scale[0], -5.0 * scale[1], 27.0 *
              scale[0], -3.0 * scale[1], 27.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], -11.0 * scale[0],
              15.0 * scale[1], -40.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-39.0 * scale[0], 0.0 * scale[1], -156.0 * scale[0],
              37.0 * scale[1], -146.0 * scale[0], 47.0 * scale[1])
    Curveto_r(2.0 * scale[0], 3.0 * scale[1], 26.0 * scale[0], -
              2.0 * scale[1], 53.0 * scale[0], -10.0 * scale[1])
    Curveto_r(64.0 * scale[0], -21.0 * scale[1], 163.0 * scale[0], -
              32.0 * scale[1], 163.0 * scale[0], -19.0 * scale[1])
    Curveto_r(0.0 * scale[0], 22.0 * scale[1], -82.0 * scale[0],
              43.0 * scale[1], -164.0 * scale[0], 42.0 * scale[1])
    Curveto_r(-44.0 * scale[0], 0.0 * scale[1], -123.0 * scale[0],
              1.0 * scale[1], -173.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-51.0 * scale[0], 3.0 * scale[1], -93.0 * scale[0],
              4.0 * scale[1], -93.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto_r(353.0 * scale[0], -123.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -21.0 *
              scale[0], -2.0 * scale[1], -30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 3.0 * scale[1], -4.0 * scale[0],
              5.0 * scale[1], 12.0 * scale[0], 5.0 * scale[1])
    Curveto_r(17.0 * scale[0], 0.0 * scale[1], 24.0 * scale[0], -
              2.0 * scale[1], 18.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(235.0 * scale[0], 1370.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], 5.0 * scale[0], -
              10.0 * scale[1], 20.0 * scale[0], -10.0 * scale[1])
    Curveto_r(15.0 * scale[0], 0.0 * scale[1], 24.0 * scale[0],
              4.0 * scale[1], 20.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -12.0 * scale[0],
              10.0 * scale[1], -20.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0], -
              4.0 * scale[1], -20.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(296.0 * scale[0], 1365.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -11.0 * scale[1], -2.0 * scale[0], -
              15.0 * scale[1], -27.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -1.0 * scale[1], -38.0 *
              scale[0], -2.0 * scale[1], -44.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -1.0 * scale[1], -21.0 *
              scale[0], -3.0 * scale[1], -35.0 * scale[0], -4.0 * scale[1])
    Lineto_r(-25.0 * scale[0], -2.0 * scale[1])
    Lineto_r(24.0 * scale[0], -10.0 * scale[1])
    Curveto_r(14.0 * scale[0], -5.0 * scale[1], 31.0 *
              scale[0], -7.0 * scale[1], 38.0 * scale[0], -4.0 * scale[1])
    Curveto_r(8.0 * scale[0], 2.0 * scale[1], 11.0 * scale[0],
              0.0 * scale[1], 8.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], 11.0 * scale[0], -
              10.0 * scale[1], 37.0 * scale[0], -11.0 * scale[1])
    Curveto_r(24.0 * scale[0], 0.0 * scale[1], 65.0 * scale[0], -
              4.0 * scale[1], 91.0 * scale[0], -8.0 * scale[1])
    Curveto_r(42.0 * scale[0], -7.0 * scale[1], 49.0 *
              scale[0], -5.0 * scale[1], 58.0 * scale[0], 11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 13.0 * scale[1], 16.0 * scale[0],
              17.0 * scale[1], 27.0 * scale[0], 13.0 * scale[1])
    Curveto_r(9.0 * scale[0], -3.0 * scale[1], 13.0 *
              scale[0], -3.0 * scale[1], 9.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 9.0 * scale[1], -137.0 * scale[0],
              53.0 * scale[1], -154.0 * scale[0], 54.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              7.0 * scale[1], -7.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(88.0 * scale[0], 1313.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(520.0 * scale[0], 1310.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(211.0 * scale[0], 1295.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -2.0 * scale[1], 35.0 * scale[0], -
              6.0 * scale[1], 72.0 * scale[0], -9.0 * scale[1])
    Curveto_r(36.0 * scale[0], -3.0 * scale[1], 75.0 * scale[0], -
              10.0 * scale[1], 86.0 * scale[0], -16.0 * scale[1])
    Curveto_r(16.0 * scale[0], -8.0 * scale[1], 19.0 *
              scale[0], -8.0 * scale[1], 15.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 7.0 * scale[1], -22.0 * scale[0],
              16.0 * scale[1], -42.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-44.0 * scale[0], 7.0 * scale[1], -137.0 * scale[0],
              8.0 * scale[1], -131.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(575.0 * scale[0], 1259.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0], -
              12.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 17.0 * scale[1], 1.0 * scale[0],
              20.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(203.0 * scale[0], 1247.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], -1.0 *
              scale[0], -7.0 * scale[1], 5.0 * scale[0], -3.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 10.0 * scale[0],
              1.0 * scale[1], 6.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -13.0 * scale[1], 0.0 * scale[0], -
              16.0 * scale[1], 34.0 * scale[0], -14.0 * scale[1])
    Curveto_r(23.0 * scale[0], 2.0 * scale[1], 39.0 * scale[0],
              5.0 * scale[1], 37.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 2.0 * scale[1], 0.0 * scale[0],
              10.0 * scale[1], 6.0 * scale[0], 17.0 * scale[1])
    Curveto_r(9.0 * scale[0], 11.0 * scale[1], 2.0 * scale[0],
              13.0 * scale[1], -35.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-26.0 * scale[0], 0.0 * scale[1], -49.0 * scale[0], -
              5.0 * scale[1], -53.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(305.0 * scale[0], 1240.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(683.0 * scale[0], 1215.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              12.0 * scale[1], 8.0 * scale[0], -9.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 28.0 * scale[0], -
              5.0 * scale[1], 51.0 * scale[0], -16.0 * scale[1])
    Curveto_r(24.0 * scale[0], -12.0 * scale[1], 35.0 *
              scale[0], -14.0 * scale[1], 25.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 12.0 * scale[1], -15.0 * scale[0],
              16.0 * scale[1], -3.0 * scale[0], 20.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 17.0 * scale[0],
              2.0 * scale[1], 20.0 * scale[0], -4.0 * scale[1])
    Curveto_r(2.0 * scale[0], -5.0 * scale[1], 3.0 *
              scale[0], -4.0 * scale[1], 2.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 16.0 * scale[1], -46.0 * scale[0],
              24.0 * scale[1], -46.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -10.0 *
              scale[0], -5.0 * scale[1], -28.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 13.0 * scale[1], -29.0 * scale[0],
              13.0 * scale[1], -29.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(251.0 * scale[0], 1203.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -3.0 * scale[1], -30.0 * scale[0], -
              11.0 * scale[1], -38.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -11.0 * scale[1], -4.0 *
              scale[0], -15.0 * scale[1], 42.0 * scale[0], -25.0 * scale[1])
    Curveto_r(30.0 * scale[0], -6.0 * scale[1], 65.0 * scale[0], -
              10.0 * scale[1], 78.0 * scale[0], -9.0 * scale[1])
    Curveto_r(12.0 * scale[0], 2.0 * scale[1], 27.0 * scale[0],
              0.0 * scale[1], 33.0 * scale[0], -4.0 * scale[1])
    Curveto_r(7.0 * scale[0], -4.0 * scale[1], 15.0 * scale[0],
              0.0 * scale[1], 18.0 * scale[0], 9.0 * scale[1])
    Curveto_r(4.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              13.0 * scale[1], -5.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -4.0 * scale[1], -15.0 * scale[0],
              0.0 * scale[1], -20.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], -9.0 * scale[0],
              11.0 * scale[1], -9.0 * scale[0], 2.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -5.0 * scale[0], -
              13.0 * scale[1], -11.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0],
              4.0 * scale[1], -5.0 * scale[0], 8.0 * scale[1])
    Curveto_r(2.0 * scale[0], 4.0 * scale[1], -4.0 * scale[0],
              9.0 * scale[1], -15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-42.0 * scale[0], 4.0 * scale[1], -49.0 * scale[0],
              6.0 * scale[1], -49.0 * scale[0], 13.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], 6.0 * scale[0],
              10.0 * scale[1], 13.0 * scale[0], 12.0 * scale[1])
    Curveto_r(14.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              6.0 * scale[1], -32.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(670.0 * scale[0], 1180.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0], -
              10.0 * scale[1], 12.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0], -
              2.0 * scale[1], 7.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -2.0 * scale[1], -20.0 *
              scale[0], -1.0 * scale[1], -37.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 5.0 * scale[1], -30.0 * scale[0],
              5.0 * scale[1], -27.0 * scale[0], -1.0 * scale[1])
    Curveto_r(4.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              9.0 * scale[1], -10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0],
              4.0 * scale[1], -10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], 0.0 * scale[0],
              7.0 * scale[1], -9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -3.0 * scale[1], -13.0 * scale[0], -
              11.0 * scale[1], -10.0 * scale[0], -18.0 * scale[1])
    Curveto_r(6.0 * scale[0], -17.0 * scale[1], -22.0 * scale[0], -
              40.0 * scale[1], -37.0 * scale[0], -30.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 4.0 * scale[1], -9.0 * scale[0],
              3.0 * scale[1], -5.0 * scale[0], -4.0 * scale[1])
    Curveto_r(4.0 * scale[0], -7.0 * scale[1], 1.0 * scale[0], -
              12.0 * scale[1], -9.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              5.0 * scale[1], -9.0 * scale[0], -11.0 * scale[1])
    Curveto_r(4.0 * scale[0], -7.0 * scale[1], 23.0 * scale[0], -
              9.0 * scale[1], 48.0 * scale[0], -5.0 * scale[1])
    Curveto_r(22.0 * scale[0], 3.0 * scale[1], 75.0 * scale[0],
              6.0 * scale[1], 116.0 * scale[0], 7.0 * scale[1])
    Curveto_r(41.0 * scale[0], 1.0 * scale[1], 81.0 * scale[0],
              4.0 * scale[1], 88.0 * scale[0], 7.0 * scale[1])
    Curveto_r(22.0 * scale[0], 8.0 * scale[1], 12.0 * scale[0],
              31.0 * scale[1], -25.0 * scale[0], 57.0 * scale[1])
    Curveto_r(-38.0 * scale[0], 25.0 * scale[1], -83.0 * scale[0],
              34.0 * scale[1], -83.0 * scale[0], 15.0 * scale[1])
    te.end_fill()
    Moveto(260.0 * scale[0], 1131.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(13.0 * scale[0], -9.0 * scale[1], 39.0 * scale[0], -
              13.0 * scale[1], 152.0 * scale[0], -26.0 * scale[1])
    Curveto_r(15.0 * scale[0], -2.0 * scale[1], 31.0 * scale[0],
              1.0 * scale[1], 34.0 * scale[0], 7.0 * scale[1])
    Curveto_r(4.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              8.0 * scale[1], -4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -4.0 * scale[1], -12.0 *
              scale[0], -3.0 * scale[1], -12.0 * scale[0], 1.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -15.0 * scale[0],
              9.0 * scale[1], -32.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 0.0 * scale[1], -60.0 * scale[0],
              4.0 * scale[1], -93.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-41.0 * scale[0], 5.0 * scale[1], -55.0 * scale[0],
              4.0 * scale[1], -45.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(254.0 * scale[0], 1104.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(11.0 * scale[0], -8.0 * scale[1], 28.0 * scale[0], -
              14.0 * scale[1], 38.0 * scale[0], -14.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 33.0 * scale[0], -
              8.0 * scale[1], 51.0 * scale[0], -17.0 * scale[1])
    Curveto_r(51.0 * scale[0], -26.0 * scale[1], 123.0 * scale[0], -
              33.0 * scale[1], 247.0 * scale[0], -21.0 * scale[1])
    Curveto_r(125.0 * scale[0], 11.0 * scale[1], 194.0 * scale[0],
              26.0 * scale[1], 130.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-208.0 * scale[0], 4.0 * scale[1], -348.0 * scale[0],
              12.0 * scale[1], -410.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-64.0 * scale[0], 12.0 * scale[1], -72.0 * scale[0],
              12.0 * scale[1], -56.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(460.0 * scale[0], 1106.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 11.0 * scale[0], -
              6.0 * scale[1], 25.0 * scale[0], -8.0 * scale[1])
    Curveto_r(13.0 * scale[0], -3.0 * scale[1], 22.0 *
              scale[0], -1.0 * scale[1], 19.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 9.0 * scale[1], -44.0 * scale[0],
              13.0 * scale[1], -44.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(205.0 * scale[0], 1083.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(11.0 * scale[0], -3.0 * scale[1], 23.0 * scale[0], -
              9.0 * scale[1], 26.0 * scale[0], -14.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 27.0 * scale[0], -
              11.0 * scale[1], 55.0 * scale[0], -14.0 * scale[1])
    Lineto_r(49.0 * scale[0], -5.0 * scale[1])
    Lineto_r(-28.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 8.0 * scale[1], -35.0 * scale[0],
              13.0 * scale[1], -43.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -3.0 * scale[1], -16.0 *
              scale[0], -1.0 * scale[1], -19.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], -18.0 * scale[0],
              9.0 * scale[1], -33.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -1.0 * scale[1], -23.0 *
              scale[0], -2.0 * scale[1], -7.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(638.0 * scale[0], 1043.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 30.0 *
              scale[0], -2.0 * scale[1], 40.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 0.0 * scale[1], -30.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(422.0 * scale[0], 794.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -7.0 * scale[1], -22.0 *
              scale[0], -11.0 * scale[1], -25.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 8.0 * scale[1], -50.0 * scale[0], -
              16.0 * scale[1], -60.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -7.0 * scale[1], -12.0 * scale[0], -
              11.0 * scale[1], -17.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -3.0 * scale[0], -
              9.0 * scale[1], 4.0 * scale[0], -26.0 * scale[1])
    Curveto_r(13.0 * scale[0], -30.0 * scale[1], 12.0 * scale[0], -
              36.0 * scale[1], -12.0 * scale[0], -71.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -21.0 * scale[1], -23.0 *
              scale[0], -40.0 * scale[1], -21.0 * scale[0], -43.0 * scale[1])
    Curveto_r(3.0 * scale[0], -2.0 * scale[1], 22.0 * scale[0], -
              5.0 * scale[1], 44.0 * scale[0], -6.0 * scale[1])
    Lineto_r(40.0 * scale[0], -3.0 * scale[1])
    Lineto_r(-3.0 * scale[0], -55.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -37.0 * scale[1], 0.0 * scale[0], -
              51.0 * scale[1], 6.0 * scale[0], -42.0 * scale[1])
    Curveto_r(6.0 * scale[0], 8.0 * scale[1], 15.0 * scale[0],
              10.0 * scale[1], 23.0 * scale[0], 6.0 * scale[1])
    Curveto_r(8.0 * scale[0], -5.0 * scale[1], 11.0 *
              scale[0], -5.0 * scale[1], 7.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 4.0 * scale[1], 0.0 * scale[0],
              14.0 * scale[1], 8.0 * scale[0], 23.0 * scale[1])
    Curveto_r(10.0 * scale[0], 10.0 * scale[1], 14.0 * scale[0],
              24.0 * scale[1], 9.0 * scale[0], 41.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 29.0 * scale[1], -7.0 * scale[0],
              82.0 * scale[1], 0.0 * scale[0], 90.0 * scale[1])
    Curveto_r(3.0 * scale[0], 2.0 * scale[1], 24.0 * scale[0], -
              5.0 * scale[1], 46.0 * scale[0], -17.0 * scale[1])
    Curveto_r(32.0 * scale[0], -17.0 * scale[1], 45.0 * scale[0], -
              20.0 * scale[1], 55.0 * scale[0], -11.0 * scale[1])
    Curveto_r(25.0 * scale[0], 21.0 * scale[1], 15.0 * scale[0],
              99.0 * scale[1], -12.0 * scale[0], 99.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 0.0 * scale[1], -19.0 * scale[0], -
              16.0 * scale[1], -5.0 * scale[0], -22.0 * scale[1])
    Curveto_r(5.0 * scale[0], -2.0 * scale[1], 5.0 * scale[0], -
              13.0 * scale[1], 0.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -48.0 * scale[1], -92.0 *
              scale[0], -13.0 * scale[1], -87.0 * scale[0], 40.0 * scale[1])
    Curveto_r(3.0 * scale[0], 27.0 * scale[1], 7.0 * scale[0],
              32.0 * scale[1], 29.0 * scale[0], 31.0 * scale[1])
    Curveto_r(14.0 * scale[0], -1.0 * scale[1], 39.0 *
              scale[0], -4.0 * scale[1], 54.0 * scale[0], -8.0 * scale[1])
    Curveto_r(25.0 * scale[0], -6.0 * scale[1], 26.0 *
              scale[0], -6.0 * scale[1], 11.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 9.0 * scale[1], -16.0 * scale[0],
              20.0 * scale[1], -16.0 * scale[0], 24.0 * scale[1])
    Curveto_r(0.0 * scale[0], 3.0 * scale[1], -13.0 * scale[0],
              12.0 * scale[1], -29.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 8.0 * scale[1], -34.0 * scale[0],
              8.0 * scale[1], -49.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto_r(-102.0 * scale[0], -174.0 * scale[1], 0, 0)
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
    Moveto_r(47.0 * scale[0], -6.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 17.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(531.0 * scale[0], 254.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-26.0 * scale[0], -23.0 * scale[1], -54.0 *
              scale[0], -37.0 * scale[1], -72.0 * scale[0], -38.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -1.0 * scale[1], -29.0 *
              scale[0], -4.0 * scale[1], -29.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], -11.0 * scale[0], -
              10.0 * scale[1], -25.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -4.0 * scale[1], -25.0 * scale[0], -
              10.0 * scale[1], -25.0 * scale[0], -14.0 * scale[1])
    Curveto_r(1.0 * scale[0], -12.0 * scale[1], 55.0 * scale[0], -
              68.0 * scale[1], 73.0 * scale[0], -75.0 * scale[1])
    Curveto_r(9.0 * scale[0], -3.0 * scale[1], 17.0 * scale[0], -
              12.0 * scale[1], 17.0 * scale[0], -19.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 3.0 *
              scale[0], -9.0 * scale[1], 9.0 * scale[0], 1.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 12.0 * scale[0],
              12.0 * scale[1], 25.0 * scale[0], 2.0 * scale[1])
    Curveto_r(16.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -14.0 * scale[1], 32.0 * scale[0], 66.0 * scale[1])
    Curveto_r(2.0 * scale[0], 12.0 * scale[1], 10.0 * scale[0],
              28.0 * scale[1], 17.0 * scale[0], 35.0 * scale[1])
    Curveto_r(8.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              25.0 * scale[1], 20.0 * scale[0], 40.0 * scale[1])
    Curveto_r(4.0 * scale[0], 14.0 * scale[1], 10.0 * scale[0],
              33.0 * scale[1], 13.0 * scale[0], 42.0 * scale[1])
    Curveto_r(10.0 * scale[0], 26.0 * scale[1], -9.0 * scale[0],
              19.0 * scale[1], -55.0 * scale[0], -20.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#9b5f2c')
    te.end_fill()
    Moveto(354.0 * scale[0], 1392.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -9.0 * scale[1], 64.0 *
              scale[0], -7.0 * scale[1], 73.0 * scale[0], 2.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -13.0 * scale[0],
              6.0 * scale[1], -36.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 0.0 * scale[1], -40.0 *
              scale[0], -4.0 * scale[1], -37.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(464.0 * scale[0], 1389.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -8.0 * scale[1], 25.0 *
              scale[0], -8.0 * scale[1], 40.0 * scale[0], -1.0 * scale[1])
    Curveto_r(18.0 * scale[0], 9.0 * scale[1], 16.0 * scale[0],
              11.0 * scale[1], -19.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-33.0 * scale[0], 0.0 * scale[1], -37.0 * scale[0], -
              1.0 * scale[1], -21.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(566.0 * scale[0], 1385.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -7.0 * scale[1], 2.0 * scale[0], -
              16.0 * scale[1], 10.0 * scale[0], -19.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 13.0 *
              scale[0], -2.0 * scale[1], 10.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], 24.0 * scale[0],
              9.0 * scale[1], 61.0 * scale[0], 10.0 * scale[1])
    Curveto_r(84.0 * scale[0], 2.0 * scale[1], 97.0 * scale[0],
              11.0 * scale[1], 17.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-32.0 * scale[0], 0.0 * scale[1], -67.0 * scale[0],
              2.0 * scale[1], -76.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 2.0 * scale[1], -19.0 * scale[0], -
              3.0 * scale[1], -22.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(157.0 * scale[0], 1383.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-20.0 * scale[0], -2.0 * scale[1], -35.0 *
              scale[0], -8.0 * scale[1], -32.0 * scale[0], -13.0 * scale[1])
    Curveto_r(8.0 * scale[0], -13.0 * scale[1], -78.0 * scale[0], -
              29.0 * scale[1], -87.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 7.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -8.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], -15.0 * scale[1], 5.0 * scale[0], -
              17.0 * scale[1], 30.0 * scale[0], -12.0 * scale[1])
    Curveto_r(46.0 * scale[0], 10.0 * scale[1], 130.0 * scale[0], -
              13.0 * scale[1], 130.0 * scale[0], -35.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 6.0 * scale[0], -
              21.0 * scale[1], 13.0 * scale[0], -23.0 * scale[1])
    Curveto_r(7.0 * scale[0], -4.0 * scale[1], 6.0 * scale[0], -
              6.0 * scale[1], -4.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -1.0 * scale[1], -20.0 * scale[0], -
              8.0 * scale[1], -23.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -2.0 * scale[0], -
              13.0 * scale[1], 3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 11.0 * scale[0], -
              1.0 * scale[1], 14.0 * scale[0], -9.0 * scale[1])
    Curveto_r(4.0 * scale[0], -10.0 * scale[1], 1.0 * scale[0], -
              12.0 * scale[1], -10.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 4.0 * scale[1], -14.0 * scale[0],
              3.0 * scale[1], -9.0 * scale[0], -6.0 * scale[1])
    Curveto_r(5.0 * scale[0], -7.0 * scale[1], 14.0 * scale[0], -
              10.0 * scale[1], 22.0 * scale[0], -7.0 * scale[1])
    Curveto_r(7.0 * scale[0], 3.0 * scale[1], 16.0 * scale[0],
              1.0 * scale[1], 19.0 * scale[0], -4.0 * scale[1])
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], -3.0 * scale[0], -
              10.0 * scale[1], -14.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -23.0 * scale[0], -
              5.0 * scale[1], -27.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -3.0 *
              scale[0], -8.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 12.0 * scale[0],
              1.0 * scale[1], 14.0 * scale[0], -5.0 * scale[1])
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], 9.0 * scale[0], -
              6.0 * scale[1], 20.0 * scale[0], 5.0 * scale[1])
    Curveto_r(17.0 * scale[0], 17.0 * scale[1], 58.0 * scale[0],
              22.0 * scale[1], 58.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              9.0 * scale[1], 15.0 * scale[0], -9.0 * scale[1])
    Curveto_r(31.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              16.0 * scale[1], -27.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-31.0 * scale[0], 7.0 * scale[1], -43.0 * scale[0],
              14.0 * scale[1], -42.0 * scale[0], 26.0 * scale[1])
    Curveto_r(1.0 * scale[0], 9.0 * scale[1], -3.0 * scale[0],
              14.0 * scale[1], -9.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -7.0 *
              scale[0], -1.0 * scale[1], -4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], 27.0 * scale[0],
              11.0 * scale[1], 53.0 * scale[0], 11.0 * scale[1])
    Curveto_r(39.0 * scale[0], 1.0 * scale[1], 44.0 * scale[0], -
              1.0 * scale[1], 34.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -12.0 * scale[1], -10.0 *
              scale[0], -15.0 * scale[1], 0.0 * scale[0], -15.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0],
              9.0 * scale[1], 17.0 * scale[0], 20.0 * scale[1])
    Curveto_r(3.0 * scale[0], 12.0 * scale[1], 10.0 * scale[0],
              17.0 * scale[1], 17.0 * scale[0], 13.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 18.0 * scale[0], -
              8.0 * scale[1], 26.0 * scale[0], -8.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0], -
              8.0 * scale[1], 12.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -16.0 * scale[1], -1.0 *
              scale[0], -17.0 * scale[1], 7.0 * scale[0], -6.0 * scale[1])
    Curveto_r(12.0 * scale[0], 19.0 * scale[1], -4.0 * scale[0],
              51.0 * scale[1], -27.0 * scale[0], 52.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 1.0 * scale[1], -41.0 * scale[0],
              3.0 * scale[1], -71.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 2.0 * scale[1], -57.0 * scale[0],
              6.0 * scale[1], -60.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], 32.0 * scale[0],
              4.0 * scale[1], 79.0 * scale[0], 2.0 * scale[1])
    Curveto_r(47.0 * scale[0], -3.0 * scale[1], 74.0 *
              scale[0], -2.0 * scale[1], 60.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 5.0 * scale[1], -47.0 * scale[0],
              8.0 * scale[1], -73.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-29.0 * scale[0], 1.0 * scale[1], -46.0 * scale[0],
              5.0 * scale[1], -42.0 * scale[0], 11.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], 0.0 * scale[0],
              7.0 * scale[1], -8.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -3.0 * scale[1], -24.0 *
              scale[0], -1.0 * scale[1], -38.0 * scale[0], 4.0 * scale[1])
    Lineto_r(-24.0 * scale[0], 10.0 * scale[1])
    Lineto_r(25.0 * scale[0], 2.0 * scale[1])
    Curveto_r(14.0 * scale[0], 1.0 * scale[1], 30.0 * scale[0],
              3.0 * scale[1], 35.0 * scale[0], 4.0 * scale[1])
    Curveto_r(6.0 * scale[0], 2.0 * scale[1], 25.0 * scale[0],
              3.0 * scale[1], 44.0 * scale[0], 4.0 * scale[1])
    Curveto_r(26.0 * scale[0], 1.0 * scale[1], 32.0 * scale[0],
              4.0 * scale[1], 27.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 14.0 * scale[1], -1.0 * scale[0],
              15.0 * scale[1], 21.0 * scale[0], 10.0 * scale[1])
    Curveto_r(16.0 * scale[0], -4.0 * scale[1], 35.0 * scale[0], -
              8.0 * scale[1], 43.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -1.0 * scale[1], 25.0 * scale[0], -
              8.0 * scale[1], 37.0 * scale[0], -14.0 * scale[1])
    Curveto_r(12.0 * scale[0], -7.0 * scale[1], 30.0 * scale[0], -
              12.0 * scale[1], 39.0 * scale[0], -12.0 * scale[1])
    Curveto_r(16.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0], -
              1.0 * scale[1], -2.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -14.0 * scale[1], -18.0 *
              scale[0], -15.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(12.0 * scale[0], 6.0 * scale[1], 22.0 * scale[0],
              13.0 * scale[1], 22.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -70.0 * scale[0],
              37.0 * scale[1], -95.0 * scale[0], 41.0 * scale[1])
    Curveto_r(-58.0 * scale[0], 9.0 * scale[1], -90.0 * scale[0],
              7.0 * scale[1], -88.0 * scale[0], -4.0 * scale[1])
    Curveto_r(2.0 * scale[0], -8.0 * scale[1], -8.0 * scale[0], -
              13.0 * scale[1], -25.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-26.0 * scale[0], 1.0 * scale[1], -26.0 * scale[0],
              1.0 * scale[1], -8.0 * scale[0], 15.0 * scale[1])
    Curveto_r(19.0 * scale[0], 14.0 * scale[1], 18.0 * scale[0],
              15.0 * scale[1], -15.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -1.0 * scale[1], -51.0 *
              scale[0], -3.0 * scale[1], -72.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(764.0 * scale[0], 1362.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(20.0 * scale[0], -8.0 * scale[1], 36.0 * scale[0], -
              18.0 * scale[1], 36.0 * scale[0], -23.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 15.0 * scale[0], -
              9.0 * scale[1], 33.0 * scale[0], -9.0 * scale[1])
    Curveto_r(24.0 * scale[0], 0.0 * scale[1], 28.0 * scale[0],
              3.0 * scale[1], 17.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 8.0 * scale[1], -11.0 * scale[0],
              10.0 * scale[1], 7.0 * scale[0], 10.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 27.0 * scale[0],
              2.0 * scale[1], 35.0 * scale[0], 5.0 * scale[1])
    Curveto_r(7.0 * scale[0], 3.0 * scale[1], 20.0 * scale[0],
              0.0 * scale[1], 28.0 * scale[0], -5.0 * scale[1])
    Curveto_r(13.0 * scale[0], -9.0 * scale[1], 13.0 * scale[0], -
              11.0 * scale[1], 0.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -9.0 * scale[1], -12.0 *
              scale[0], -10.0 * scale[1], -1.0 * scale[0], -7.0 * scale[1])
    Curveto_r(19.0 * scale[0], 5.0 * scale[1], 23.0 * scale[0],
              19.0 * scale[1], 12.0 * scale[0], 37.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 11.0 * scale[1], -34.0 * scale[0],
              15.0 * scale[1], -106.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-94.0 * scale[0], 2.0 * scale[1], -96.0 * scale[0],
              1.0 * scale[1], -61.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(600.0 * scale[0], 1360.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], 89.0 * scale[0], -
              40.0 * scale[1], 132.0 * scale[0], -40.0 * scale[1])
    Curveto_r(29.0 * scale[0], 0.0 * scale[1], 38.0 * scale[0], -
              4.0 * scale[1], 38.0 * scale[0], -17.0 * scale[1])
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 11.0 * scale[0], -6.0 * scale[1])
    Curveto_r(18.0 * scale[0], 18.0 * scale[1], 1.0 * scale[0],
              31.0 * scale[1], -49.0 * scale[0], 38.0 * scale[1])
    Curveto_r(-26.0 * scale[0], 4.0 * scale[1], -66.0 * scale[0],
              13.0 * scale[1], -89.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 8.0 * scale[1], -43.0 * scale[0],
              10.0 * scale[1], -43.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(525.0 * scale[0], 1323.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(44.0 * scale[0], -23.0 * scale[1], 65.0 * scale[0], -
              44.0 * scale[1], 65.0 * scale[0], -65.0 * scale[1])
    Curveto_r(0.0 * scale[0], -20.0 * scale[1], 16.0 * scale[0], -
              25.0 * scale[1], 23.0 * scale[0], -5.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], 22.0 * scale[0],
              2.0 * scale[1], 65.0 * scale[0], -21.0 * scale[1])
    Curveto_r(38.0 * scale[0], -20.0 * scale[1], 62.0 * scale[0], -
              28.0 * scale[1], 64.0 * scale[0], -21.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 13.0 * scale[0],
              9.0 * scale[1], 23.0 * scale[0], 7.0 * scale[1])
    Curveto_r(19.0 * scale[0], -4.0 * scale[1], 19.0 * scale[0], -
              5.0 * scale[1], -2.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -9.0 * scale[1], -29.0 *
              scale[0], -10.0 * scale[1], -42.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 7.0 * scale[1], -31.0 * scale[0],
              4.0 * scale[1], -70.0 * scale[0], -14.0 * scale[1])
    Lineto_r(-50.0 * scale[0], -23.0 * scale[1])
    Lineto_r(44.0 * scale[0], 1.0 * scale[1])
    Curveto_r(25.0 * scale[0], 1.0 * scale[1], 40.0 * scale[0],
              3.0 * scale[1], 35.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 7.0 * scale[1], -10.0 * scale[0],
              22.0 * scale[1], 13.0 * scale[0], 22.0 * scale[1])
    Curveto_r(28.0 * scale[0], 0.0 * scale[1], 97.0 * scale[0], -
              46.0 * scale[1], 97.0 * scale[0], -64.0 * scale[1])
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], -14.0 * scale[0], -
              23.0 * scale[1], -100.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-41.0 * scale[0], -1.0 * scale[1], -94.0 *
              scale[0], -4.0 * scale[1], -116.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-25.0 * scale[0], -4.0 * scale[1], -44.0 *
              scale[0], -2.0 * scale[1], -48.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], -12.0 * scale[0],
              11.0 * scale[1], -17.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              4.0 * scale[1], -5.0 * scale[0], -8.0 * scale[1])
    Curveto_r(7.0 * scale[0], -12.0 * scale[1], -25.0 *
              scale[0], -8.0 * scale[1], -50.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 6.0 * scale[1], -25.0 * scale[0],
              7.0 * scale[1], -30.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -8.0 * scale[1], -117.0 * scale[0],
              2.0 * scale[1], -157.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 6.0 * scale[1], -18.0 * scale[0],
              6.0 * scale[1], 0.0 * scale[0], 21.0 * scale[1])
    Curveto_r(17.0 * scale[0], 14.0 * scale[1], 17.0 * scale[0],
              14.0 * scale[1], -2.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -3.0 * scale[1], -29.0 *
              scale[0], -8.0 * scale[1], -40.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -7.0 * scale[1], -18.0 *
              scale[0], -6.0 * scale[1], -6.0 * scale[0], 9.0 * scale[1])
    Curveto_r(17.0 * scale[0], 21.0 * scale[1], 2.0 * scale[0],
              22.0 * scale[1], -25.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -8.0 * scale[1], -23.0 * scale[0], -
              14.0 * scale[1], -29.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -3.0 * scale[0],
              5.0 * scale[1], 5.0 * scale[0], 11.0 * scale[1])
    Curveto_r(13.0 * scale[0], 9.0 * scale[1], 13.0 * scale[0],
              10.0 * scale[1], 0.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-22.0 * scale[0], -6.0 * scale[1], -25.0 *
              scale[0], -37.0 * scale[1], -3.0 * scale[0], -39.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              4.0 * scale[1], -32.0 * scale[0], -7.0 * scale[1])
    Lineto_r(-50.0 * scale[0], -7.0 * scale[1])
    Lineto_r(63.0 * scale[0], -18.0 * scale[1])
    Curveto_r(84.0 * scale[0], -25.0 * scale[1], 71.0 * scale[0], -
              32.0 * scale[1], -22.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-41.0 * scale[0], 9.0 * scale[1], -81.0 * scale[0],
              15.0 * scale[1], -88.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -3.0 * scale[1], -1.0 *
              scale[0], -6.0 * scale[1], 13.0 * scale[0], -6.0 * scale[1])
    Curveto_r(14.0 * scale[0], -1.0 * scale[1], 29.0 *
              scale[0], -4.0 * scale[1], 33.0 * scale[0], -8.0 * scale[1])
    Curveto_r(4.0 * scale[0], -5.0 * scale[1], 11.0 * scale[0], -
              8.0 * scale[1], 14.0 * scale[0], -9.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0], -
              6.0 * scale[1], 35.0 * scale[0], -12.0 * scale[1])
    Curveto_r(18.0 * scale[0], -8.0 * scale[1], 84.0 * scale[0], -
              12.0 * scale[1], 180.0 * scale[0], -11.0 * scale[1])
    Curveto_r(94.0 * scale[0], 1.0 * scale[1], 135.0 * scale[0],
              4.0 * scale[1], 107.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 4.0 * scale[1], -59.0 * scale[0],
              15.0 * scale[1], -77.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 9.0 * scale[1], -37.0 * scale[0],
              17.0 * scale[1], -43.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              17.0 * scale[1], 13.0 * scale[0], -28.0 * scale[1])
    Curveto_r(18.0 * scale[0], -10.0 * scale[1], 14.0 * scale[0], -
              11.0 * scale[1], -27.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-28.0 * scale[0], 3.0 * scale[1], -52.0 * scale[0],
              9.0 * scale[1], -55.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], -15.0 * scale[0],
              11.0 * scale[1], -26.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 4.0 * scale[1], -15.0 *
              scale[0], 5.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 30.0 * scale[0], -
              4.0 * scale[1], 36.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -8.0 * scale[1], 13.0 *
              scale[0], -8.0 * scale[1], 18.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], -1.0 * scale[0],
              17.0 * scale[1], -11.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 10.0 * scale[1], 4.0 * scale[0],
              10.0 * scale[1], 75.0 * scale[0], -3.0 * scale[1])
    Curveto_r(76.0 * scale[0], -13.0 * scale[1], 94.0 * scale[0], -
              13.0 * scale[1], 100.0 * scale[0], -2.0 * scale[1])
    Curveto_r(7.0 * scale[0], 11.0 * scale[1], 9.0 * scale[0],
              11.0 * scale[1], 13.0 * scale[0], 0.0 * scale[1])
    Curveto_r(4.0 * scale[0], -11.0 * scale[1], 34.0 * scale[0], -
              15.0 * scale[1], 129.0 * scale[0], -16.0 * scale[1])
    Curveto_r(68.0 * scale[0], -2.0 * scale[1], 138.0 *
              scale[0], -3.0 * scale[1], 154.0 * scale[0], -4.0 * scale[1])
    Lineto_r(30.0 * scale[0], -1.0 * scale[1])
    Lineto_r(-30.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -4.0 * scale[1], -68.0 * scale[0], -
              12.0 * scale[1], -115.0 * scale[0], -18.0 * scale[1])
    Lineto_r(-85.0 * scale[0], -10.0 * scale[1])
    Lineto_r(85.0 * scale[0], 5.0 * scale[1])
    Curveto_r(56.0 * scale[0], 2.0 * scale[1], 78.0 * scale[0],
              0.0 * scale[1], 65.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-24.0 * scale[0], -10.0 * scale[1], 103.0 *
              scale[0], -14.0 * scale[1], 131.0 * scale[0], -3.0 * scale[1])
    Curveto_r(16.0 * scale[0], 6.0 * scale[1], 16.0 * scale[0],
              7.0 * scale[1], -2.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 5.0 * scale[1], 5.0 * scale[0],
              8.0 * scale[1], 46.0 * scale[0], 8.0 * scale[1])
    Curveto_r(61.0 * scale[0], 1.0 * scale[1], 73.0 * scale[0],
              12.0 * scale[1], 25.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 4.0 * scale[1], -11.0 * scale[0],
              5.0 * scale[1], 10.0 * scale[0], 6.0 * scale[1])
    Curveto_r(59.0 * scale[0], 2.0 * scale[1], 62.0 * scale[0],
              3.0 * scale[1], 61.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 17.0 * scale[1], -7.0 * scale[0],
              32.0 * scale[1], -16.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 5.0 * scale[1], -13.0 * scale[0],
              3.0 * scale[1], -1.0 * scale[0], -11.0 * scale[1])
    Curveto_r(7.0 * scale[0], -10.0 * scale[1], 10.0 * scale[0], -
              18.0 * scale[1], 5.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -1.0 * scale[1], -13.0 *
              scale[0], -2.0 * scale[1], -19.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -1.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -20.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -1.0 * scale[1], -3.0 *
              scale[0], -6.0 * scale[1], 5.0 * scale[0], -11.0 * scale[1])
    Curveto_r(10.0 * scale[0], -6.0 * scale[1], 2.0 * scale[0], -
              7.0 * scale[1], -25.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 3.0 * scale[1], -41.0 * scale[0],
              10.0 * scale[1], -43.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 4.0 * scale[1], -8.0 * scale[0],
              8.0 * scale[1], -13.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              4.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              10.0 * scale[1], -6.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0],
              8.0 * scale[1], -6.0 * scale[0], 20.0 * scale[1])
    Curveto_r(3.0 * scale[0], 13.0 * scale[1], 1.0 * scale[0],
              18.0 * scale[1], -6.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -4.0 * scale[1], -8.0 * scale[0],
              0.0 * scale[1], -4.0 * scale[0], 11.0 * scale[1])
    Curveto_r(4.0 * scale[0], 10.0 * scale[1], 7.0 * scale[0],
              20.0 * scale[1], 7.0 * scale[0], 22.0 * scale[1])
    Curveto_r(0.0 * scale[0], 3.0 * scale[1], 5.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], -1.0 * scale[1])
    Curveto_r(20.0 * scale[0], -12.0 * scale[1], 5.0 * scale[0],
              19.0 * scale[1], -20.0 * scale[0], 41.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 17.0 * scale[1], -30.0 * scale[0],
              20.0 * scale[1], -48.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-23.0 * scale[0], -9.0 * scale[1], -42.0 *
              scale[0], -2.0 * scale[1], -91.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 9.0 * scale[1], -32.0 * scale[0],
              17.0 * scale[1], -42.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 0.0 * scale[1], -24.0 * scale[0],
              8.0 * scale[1], -31.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 9.0 * scale[1], -26.0 * scale[0],
              23.0 * scale[1], -41.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-40.0 * scale[0], 17.0 * scale[1], -48.0 * scale[0],
              14.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(250.0 * scale[0], -143.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -6.0 * scale[1], -1.0 * scale[0], -
              7.0 * scale[1], -9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 7.0 * scale[1], -21.0 * scale[0],
              14.0 * scale[1], -7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0], -
              4.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(391.0 * scale[0], 1301.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -5.0 * scale[1], -11.0 * scale[0], -
              15.0 * scale[1], -9.0 * scale[0], -22.0 * scale[1])
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 8.0 *
              scale[0], -7.0 * scale[1], 17.0 * scale[0], 9.0 * scale[1])
    Curveto_r(13.0 * scale[0], 24.0 * scale[1], 12.0 * scale[0],
              26.0 * scale[1], -8.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(724.0 * scale[0], 1293.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(10.0 * scale[0], -11.0 * scale[1], 37.0 *
              scale[0], -12.0 * scale[1], 30.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], -12.0 * scale[0],
              9.0 * scale[1], -21.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -13.0 *
              scale[0], -3.0 * scale[1], -9.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(693.0 * scale[0], 1263.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(750.0 * scale[0], 1263.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 23.0 * scale[0], -
              12.0 * scale[1], 33.0 * scale[0], -21.0 * scale[1])
    Curveto_r(20.0 * scale[0], -18.0 * scale[1], 23.0 *
              scale[0], -7.0 * scale[1], 3.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 8.0 * scale[1], -23.0 * scale[0],
              14.0 * scale[1], -33.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -15.0 *
              scale[0], -2.0 * scale[1], -3.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(930.0 * scale[0], 1189.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 4.0 * scale[0], -
              18.0 * scale[1], 10.0 * scale[0], -14.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 7.0 * scale[0],
              12.0 * scale[1], 3.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 21.0 * scale[1], -13.0 * scale[0],
              19.0 * scale[1], -13.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(360.0 * scale[0], 1180.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], -12.0 * scale[0], -
              25.0 * scale[1], -32.0 * scale[0], -35.0 * scale[1])
    Lineto_r(-33.0 * scale[0], -14.0 * scale[1])
    Lineto_r(35.0 * scale[0], 2.0 * scale[1])
    Curveto_r(22.0 * scale[0], 1.0 * scale[1], 34.0 * scale[0],
              7.0 * scale[1], 33.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              12.0 * scale[1], 8.0 * scale[0], 12.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0], -
              9.0 * scale[1], 3.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -20.0 * scale[1], -5.0 *
              scale[0], -21.0 * scale[1], 10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(14.0 * scale[0], 12.0 * scale[1], 15.0 * scale[0],
              16.0 * scale[1], 3.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 9.0 * scale[1], -12.0 * scale[0],
              22.0 * scale[1], -10.0 * scale[0], 29.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 0.0 * scale[0],
              12.0 * scale[1], -6.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              9.0 * scale[1], -11.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(595.0 * scale[0], 1190.0 * scale[1], x, y)
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
    Moveto(417.0 * scale[0], 1149.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(551.0 * scale[0], 1130.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -11.0 * scale[1], -19.0 *
              scale[0], -20.0 * scale[1], -13.0 * scale[0], -20.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0],
              9.0 * scale[1], 33.0 * scale[0], 20.0 * scale[1])
    Curveto_r(13.0 * scale[0], 10.0 * scale[1], 20.0 * scale[0],
              19.0 * scale[1], 14.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -21.0 * scale[0], -
              9.0 * scale[1], -34.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(78.0 * scale[0], 1123.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(858.0 * scale[0], 1123.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(848.0 * scale[0], 1043.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(558.0 * scale[0], 863.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(405.0 * scale[0], 850.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -7.0 * scale[1], -17.0 *
              scale[0], -9.0 * scale[1], -3.0 * scale[0], -9.0 * scale[1])
    Curveto_r(9.0 * scale[0], -1.0 * scale[1], 20.0 * scale[0],
              4.0 * scale[1], 23.0 * scale[0], 9.0 * scale[1])
    Curveto_r(7.0 * scale[0], 11.0 * scale[1], 7.0 * scale[0],
              11.0 * scale[1], -20.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(479.0 * scale[0], 844.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              12.0 * scale[1], 0.0 * scale[0], -16.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], -20.0 * scale[0], -
              10.0 * scale[1], -46.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-25.0 * scale[0], -4.0 * scale[1], -58.0 * scale[0], -
              13.0 * scale[1], -72.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -8.0 * scale[1], -31.0 * scale[0], -
              14.0 * scale[1], -37.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0], -
              10.0 * scale[1], -32.0 * scale[0], -23.0 * scale[1])
    Lineto_r(-22.0 * scale[0], -23.0 * scale[1])
    Lineto_r(30.0 * scale[0], -11.0 * scale[1])
    Curveto_r(28.0 * scale[0], -11.0 * scale[1], 29.0 *
              scale[0], -10.0 * scale[1], 19.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 13.0 * scale[1], -7.0 * scale[0],
              18.0 * scale[1], -1.0 * scale[0], 14.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 14.0 * scale[0],
              0.0 * scale[1], 19.0 * scale[0], 7.0 * scale[1])
    Curveto_r(11.0 * scale[0], 19.0 * scale[1], 51.0 * scale[0],
              39.0 * scale[1], 63.0 * scale[0], 32.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 11.0 *
              scale[0], -1.0 * scale[1], 15.0 * scale[0], 5.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 79.0 * scale[0],
              4.0 * scale[1], 83.0 * scale[0], -10.0 * scale[1])
    Curveto_r(2.0 * scale[0], -6.0 * scale[1], 11.0 * scale[0], -
              17.0 * scale[1], 19.0 * scale[0], -26.0 * scale[1])
    Curveto_r(14.0 * scale[0], -13.0 * scale[1], 13.0 * scale[0], -
              14.0 * scale[1], -10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 7.0 * scale[1], -25.0 * scale[0],
              6.0 * scale[1], -17.0 * scale[0], -29.0 * scale[1])
    Curveto_r(9.0 * scale[0], -42.0 * scale[1], 6.0 * scale[0], -
              46.0 * scale[1], -28.0 * scale[0], -37.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 7.0 * scale[1], -27.0 * scale[0],
              13.0 * scale[1], -27.0 * scale[0], 43.0 * scale[1])
    Curveto_r(0.0 * scale[0], 20.0 * scale[1], -3.0 * scale[0],
              34.0 * scale[1], -7.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -2.0 * scale[1], -8.0 * scale[0], -
              17.0 * scale[1], -8.0 * scale[0], -33.0 * scale[1])
    Curveto_r(0.0 * scale[0], -31.0 * scale[1], 30.0 * scale[0], -
              60.0 * scale[1], 63.0 * scale[0], -60.0 * scale[1])
    Curveto_r(18.0 * scale[0], 0.0 * scale[1], 41.0 * scale[0],
              42.0 * scale[1], 26.0 * scale[0], 48.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -10.0 * scale[0],
              22.0 * scale[1], 5.0 * scale[0], 22.0 * scale[1])
    Curveto_r(27.0 * scale[0], 0.0 * scale[1], 37.0 * scale[0], -
              79.0 * scale[1], 12.0 * scale[0], -99.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -9.0 * scale[1], -22.0 *
              scale[0], -7.0 * scale[1], -51.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 12.0 * scale[1], -42.0 * scale[0],
              19.0 * scale[1], -49.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -3.0 * scale[1], -7.0 *
              scale[0], -5.0 * scale[1], 1.0 * scale[0], -5.0 * scale[1])
    Curveto_r(7.0 * scale[0], -1.0 * scale[1], 34.0 * scale[0], -
              14.0 * scale[1], 60.0 * scale[0], -31.0 * scale[1])
    Curveto_r(69.0 * scale[0], -44.0 * scale[1], 73.0 *
              scale[0], -42.0 * scale[1], 68.0 * scale[0], 38.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 84.0 * scale[1], -7.0 * scale[0],
              93.0 * scale[1], -28.0 * scale[0], 125.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 15.0 * scale[1], -17.0 * scale[0],
              30.0 * scale[1], -17.0 * scale[0], 35.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], -30.0 * scale[0],
              37.0 * scale[1], -31.0 * scale[0], 26.0 * scale[1])
    te.end_fill()
    Moveto(266.0 * scale[0], 645.0 * scale[1], x, y)
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
    Moveto(285.0 * scale[0], 620.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -11.0 *
              scale[0], -7.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -8.0 * scale[0],
              2.0 * scale[1], -4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(10.0 * scale[0], -16.0 * scale[1], 23.0 *
              scale[0], -15.0 * scale[1], 30.0 * scale[0], 3.0 * scale[1])
    Curveto_r(6.0 * scale[0], 17.0 * scale[1], 0.0 * scale[0],
              20.0 * scale[1], -9.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(420.0 * scale[0], 590.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(13.0 * scale[0], -24.0 * scale[1], 6.0 * scale[0], -
              70.0 * scale[1], -11.0 * scale[0], -70.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              4.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(3.0 * scale[0], -6.0 * scale[1], -1.0 * scale[0], -
              7.0 * scale[1], -9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 4.0 * scale[1], -16.0 * scale[0],
              1.0 * scale[1], -17.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -4.0 *
              scale[0], -5.0 * scale[1], -9.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 17.0 * scale[1], -9.0 * scale[0],
              17.0 * scale[1], -9.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -10.0 * scale[1], -6.0 * scale[0], -
              18.0 * scale[1], -12.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              4.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 0.0 * scale[0], -
              7.0 * scale[1], -8.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 9.0 * scale[1], -29.0 * scale[0], -
              13.0 * scale[1], -12.0 * scale[0], -40.0 * scale[1])
    Curveto_r(9.0 * scale[0], -14.0 * scale[1], 29.0 * scale[0], -
              26.0 * scale[1], 46.0 * scale[0], -28.0 * scale[1])
    Curveto_r(25.0 * scale[0], -4.0 * scale[1], 34.0 * scale[0],
              0.0 * scale[1], 47.0 * scale[0], 21.0 * scale[1])
    Curveto_r(9.0 * scale[0], 14.0 * scale[1], 21.0 * scale[0],
              29.0 * scale[1], 26.0 * scale[0], 33.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 10.0 * scale[0],
              17.0 * scale[1], 12.0 * scale[0], 30.0 * scale[1])
    Curveto_r(1.0 * scale[0], 12.0 * scale[1], 3.0 * scale[0],
              26.0 * scale[1], 3.0 * scale[0], 30.0 * scale[1])
    Curveto_r(1.0 * scale[0], 3.0 * scale[1], 7.0 * scale[0],
              8.0 * scale[1], 14.0 * scale[0], 10.0 * scale[1])
    Curveto_r(7.0 * scale[0], 2.0 * scale[1], -3.0 * scale[0],
              18.0 * scale[1], -26.0 * scale[0], 41.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 23.0 * scale[1], -34.0 * scale[0],
              30.0 * scale[1], -27.0 * scale[0], 17.0 * scale[1])
    te.end_fill()
    Moveto(598.0 * scale[0], 315.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-27.0 * scale[0], -20.0 * scale[1], -48.0 *
              scale[0], -38.0 * scale[1], -48.0 * scale[0], -41.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 7.0 * scale[0], -
              1.0 * scale[1], 15.0 * scale[0], 6.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              11.0 * scale[1], 20.0 * scale[0], 8.0 * scale[1])
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], -18.0 * scale[0], -
              82.0 * scale[1], -32.0 * scale[0], -96.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -7.0 * scale[1], -15.0 * scale[0], -
              24.0 * scale[1], -18.0 * scale[0], -38.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -79.0 * scale[1], -15.0 *
              scale[0], -76.0 * scale[1], -31.0 * scale[0], -63.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 10.0 * scale[1], -17.0 * scale[0],
              10.0 * scale[1], -23.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -10.0 * scale[1], -10.0 *
              scale[0], -9.0 * scale[1], -14.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              16.0 * scale[1], -17.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -69.0 * scale[0],
              60.0 * scale[1], -70.0 * scale[0], 72.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], 11.0 * scale[0],
              10.0 * scale[1], 25.0 * scale[0], 14.0 * scale[1])
    Curveto_r(14.0 * scale[0], 3.0 * scale[1], 25.0 * scale[0],
              11.0 * scale[1], 25.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -8.0 * scale[0],
              7.0 * scale[1], -17.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-24.0 * scale[0], -10.0 * scale[1], -116.0 *
              scale[0], -24.0 * scale[1], -125.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 2.0 * scale[1], -8.0 * scale[0], -
              20.0 * scale[1], -8.0 * scale[0], -50.0 * scale[1])
    Curveto_r(0.0 * scale[0], -55.0 * scale[1], 20.0 * scale[0], -
              120.0 * scale[1], 41.0 * scale[0], -133.0 * scale[1])
    Curveto_r(19.0 * scale[0], -11.0 * scale[1], 220.0 *
              scale[0], -6.0 * scale[1], 235.0 * scale[0], 7.0 * scale[1])
    Curveto_r(7.0 * scale[0], 6.0 * scale[1], 16.0 * scale[0],
              26.0 * scale[1], 20.0 * scale[0], 45.0 * scale[1])
    Curveto_r(3.0 * scale[0], 19.0 * scale[1], 10.0 * scale[0],
              34.0 * scale[1], 15.0 * scale[0], 34.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              8.0 * scale[1], 9.0 * scale[0], 18.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], 5.0 * scale[0],
              23.0 * scale[1], 10.0 * scale[0], 28.0 * scale[1])
    Curveto_r(6.0 * scale[0], 6.0 * scale[1], 11.0 * scale[0],
              33.0 * scale[1], 11.0 * scale[0], 60.0 * scale[1])
    Curveto_r(1.0 * scale[0], 27.0 * scale[1], 7.0 * scale[0],
              56.0 * scale[1], 14.0 * scale[0], 64.0 * scale[1])
    Curveto_r(14.0 * scale[0], 17.0 * scale[1], 28.0 * scale[0],
              80.0 * scale[1], 17.0 * scale[0], 80.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -28.0 * scale[0], -
              16.0 * scale[1], -54.0 * scale[0], -35.0 * scale[1])
    te.end_fill()
    Moveto(496.0 * scale[0], 235.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -8.0 * scale[1], -15.0 *
              scale[0], -15.0 * scale[1], -9.0 * scale[0], -15.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0],
              7.0 * scale[1], 23.0 * scale[0], 15.0 * scale[1])
    Curveto_r(16.0 * scale[0], 19.0 * scale[1], 11.0 * scale[0],
              19.0 * scale[1], -14.0 * scale[0], 0.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#74401b')
    te.end_fill()
    Moveto(95.0 * scale[0], 1386.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-73.0 * scale[0], -13.0 * scale[1], -85.0 *
              scale[0], -21.0 * scale[1], -85.0 * scale[0], -50.0 * scale[1])
    Curveto_r(0.0 * scale[0], -21.0 * scale[1], 4.0 * scale[0], -
              23.0 * scale[1], 33.0 * scale[0], -21.0 * scale[1])
    Curveto_r(17.0 * scale[0], 2.0 * scale[1], 52.0 * scale[0],
              4.0 * scale[1], 77.0 * scale[0], 5.0 * scale[1])
    Curveto_r(44.0 * scale[0], 2.0 * scale[1], 44.0 * scale[0],
              2.0 * scale[1], 15.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 5.0 * scale[1], -47.0 * scale[0],
              7.0 * scale[1], -67.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-32.0 * scale[0], -4.0 * scale[1], -38.0 *
              scale[0], -2.0 * scale[1], -38.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], 3.0 * scale[0],
              14.0 * scale[1], 8.0 * scale[0], 7.0 * scale[1])
    Curveto_r(8.0 * scale[0], -12.0 * scale[1], 95.0 * scale[0],
              3.0 * scale[1], 87.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], 120.0 * scale[0],
              25.0 * scale[1], 134.0 * scale[0], 17.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 20.0 *
              scale[0], -2.0 * scale[1], 33.0 * scale[0], 3.0 * scale[1])
    Curveto_r(34.0 * scale[0], 14.0 * scale[1], -121.0 * scale[0],
              12.0 * scale[1], -197.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(334.0 * scale[0], 1388.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], -3.0 *
              scale[0], -8.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(7.0 * scale[0], 4.0 * scale[1], 12.0 * scale[0],
              3.0 * scale[1], 12.0 * scale[0], -2.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 8.0 * scale[0], -
              13.0 * scale[1], 17.0 * scale[0], -16.0 * scale[1])
    Curveto_r(15.0 * scale[0], -6.0 * scale[1], 15.0 *
              scale[0], -4.0 * scale[1], -2.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 23.0 * scale[1], -22.0 * scale[0],
              24.0 * scale[1], -31.0 * scale[0], 8.0 * scale[1])
    te.end_fill()
    Moveto(550.0 * scale[0], 1390.0 * scale[1], x, y)
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
    Moveto(623.0 * scale[0], 1393.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(15.0 * scale[0], -2.0 * scale[1], 37.0 *
              scale[0], -2.0 * scale[1], 50.0 * scale[0], 0.0 * scale[1])
    Curveto_r(12.0 * scale[0], 2.0 * scale[1], 0.0 * scale[0],
              4.0 * scale[1], -28.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-27.0 * scale[0], 0.0 * scale[1], -38.0 *
              scale[0], -2.0 * scale[1], -22.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(724.0 * scale[0], 1383.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], 49.0 * scale[0], -
              7.0 * scale[1], 102.0 * scale[0], -8.0 * scale[1])
    Curveto_r(71.0 * scale[0], -1.0 * scale[1], 98.0 * scale[0], -
              5.0 * scale[1], 104.0 * scale[0], -15.0 * scale[1])
    Curveto_r(10.0 * scale[0], -16.0 * scale[1], 9.0 * scale[0], -
              38.0 * scale[1], -3.0 * scale[0], -57.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], 0.0 * scale[0], -
              16.0 * scale[1], 10.0 * scale[0], -22.0 * scale[1])
    Curveto_r(14.0 * scale[0], -8.0 * scale[1], 15.0 * scale[0], -
              11.0 * scale[1], 3.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -1.0 * scale[1], -19.0 *
              scale[0], -1.0 * scale[1], -25.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 1.0 * scale[1], -2.0 * scale[0], -
              7.0 * scale[1], 8.0 * scale[0], -18.0 * scale[1])
    Curveto_r(9.0 * scale[0], -10.0 * scale[1], 14.0 * scale[0], -
              21.0 * scale[1], 11.0 * scale[0], -24.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], -1.0 * scale[0], -
              15.0 * scale[1], 5.0 * scale[0], -27.0 * scale[1])
    Curveto_r(7.0 * scale[0], -13.0 * scale[1], 8.0 * scale[0], -
              22.0 * scale[1], 1.0 * scale[0], -26.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -10.0 * scale[0],
              1.0 * scale[1], -10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], -4.0 * scale[0],
              16.0 * scale[1], -9.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -25.0 * scale[0], -
              39.0 * scale[1], -17.0 * scale[0], -47.0 * scale[1])
    Curveto_r(11.0 * scale[0], -11.0 * scale[1], -34.0 * scale[0], -
              34.0 * scale[1], -54.0 * scale[0], -28.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 4.0 * scale[1], -20.0 * scale[0],
              2.0 * scale[1], -20.0 * scale[0], -3.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 6.0 * scale[0], -
              9.0 * scale[1], 13.0 * scale[0], -9.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 26.0 * scale[0], -
              3.0 * scale[1], 42.0 * scale[0], -7.0 * scale[1])
    Curveto_r(22.0 * scale[0], -5.0 * scale[1], 26.0 *
              scale[0], -4.0 * scale[1], 15.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -10.0 * scale[0],
              10.0 * scale[1], -5.0 * scale[0], 11.0 * scale[1])
    Curveto_r(6.0 * scale[0], 1.0 * scale[1], 15.0 * scale[0],
              3.0 * scale[1], 20.0 * scale[0], 4.0 * scale[1])
    Curveto_r(6.0 * scale[0], 2.0 * scale[1], 14.0 * scale[0],
              3.0 * scale[1], 19.0 * scale[0], 4.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 2.0 * scale[0],
              8.0 * scale[1], -5.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 14.0 * scale[1], -12.0 * scale[0],
              16.0 * scale[1], 1.0 * scale[0], 11.0 * scale[1])
    Curveto_r(9.0 * scale[0], -3.0 * scale[1], 15.0 * scale[0], -
              18.0 * scale[1], 16.0 * scale[0], -35.0 * scale[1])
    Curveto_r(1.0 * scale[0], -31.0 * scale[1], -2.0 * scale[0], -
              32.0 * scale[1], -61.0 * scale[0], -34.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -1.0 * scale[1], -24.0 *
              scale[0], -2.0 * scale[1], -10.0 * scale[0], -6.0 * scale[1])
    Curveto_r(48.0 * scale[0], -12.0 * scale[1], 36.0 * scale[0], -
              23.0 * scale[1], -26.0 * scale[0], -24.0 * scale[1])
    Curveto_r(-35.0 * scale[0], -1.0 * scale[1], -55.0 *
              scale[0], -4.0 * scale[1], -45.0 * scale[0], -6.0 * scale[1])
    Curveto_r(15.0 * scale[0], -4.0 * scale[1], 16.0 *
              scale[0], -7.0 * scale[1], 5.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -5.0 * scale[1], 12.0 *
              scale[0], -9.0 * scale[1], 56.0 * scale[0], -9.0 * scale[1])
    Curveto_r(39.0 * scale[0], 0.0 * scale[1], 75.0 * scale[0],
              4.0 * scale[1], 82.0 * scale[0], 8.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 11.0 * scale[0],
              56.0 * scale[1], 11.0 * scale[0], 164.0 * scale[1])
    Curveto_r(0.0 * scale[0], 129.0 * scale[1], -3.0 * scale[0],
              160.0 * scale[1], -16.0 * scale[0], 170.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 13.0 * scale[1], -231.0 * scale[0],
              24.0 * scale[1], -218.0 * scale[0], 11.0 * scale[1])
    te.end_fill()
    Moveto_r(149.0 * scale[0], -340.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              5.0 * scale[1], 12.0 * scale[0], 5.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(865.0 * scale[0], 1351.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-30.0 * scale[0], -7.0 * scale[1])
    Lineto_r(31.0 * scale[0], -11.0 * scale[1])
    Curveto_r(23.0 * scale[0], -8.0 * scale[1], 34.0 *
              scale[0], -8.0 * scale[1], 47.0 * scale[0], 2.0 * scale[1])
    Curveto_r(16.0 * scale[0], 11.0 * scale[1], 16.0 * scale[0],
              13.0 * scale[1], 1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -16.0 * scale[0],
              5.0 * scale[1], -17.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -1.0 * scale[1], -15.0 *
              scale[0], -4.0 * scale[1], -32.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(468.0 * scale[0], 1333.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(793.0 * scale[0], 1323.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 25.0 *
              scale[0], -2.0 * scale[1], 35.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -27.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(178.0 * scale[0], 1298.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -24.0 * scale[1], -2.0 * scale[0], -
              28.0 * scale[1], 16.0 * scale[0], -28.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0],
              3.0 * scale[1], 10.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -14.0 * scale[0],
              16.0 * scale[1], -16.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 17.0 * scale[1], -5.0 * scale[0],
              15.0 * scale[1], -10.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(19.0 * scale[0], 1295.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -50.0 * scale[1], -5.0 * scale[0], -
              181.0 * scale[1], 4.0 * scale[0], -187.0 * scale[1])
    Curveto_r(9.0 * scale[0], -6.0 * scale[1], 9.0 * scale[0], -
              8.0 * scale[1], 1.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -50.0 * scale[1], 5.0 * scale[0], -59.0 * scale[1])
    Curveto_r(9.0 * scale[0], -5.0 * scale[1], 61.0 * scale[0], -
              9.0 * scale[1], 116.0 * scale[0], -9.0 * scale[1])
    Curveto_r(88.0 * scale[0], 1.0 * scale[1], 93.0 * scale[0],
              2.0 * scale[1], 43.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-32.0 * scale[0], 4.0 * scale[1], -65.0 * scale[0],
              13.0 * scale[1], -73.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 7.0 * scale[1], -15.0 * scale[0],
              9.0 * scale[1], -15.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], -5.0 * scale[0], -
              3.0 * scale[1], -12.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 7.0 * scale[1], -23.0 * scale[0],
              12.0 * scale[1], -37.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0],
              3.0 * scale[1], -13.0 * scale[0], 6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 3.0 * scale[1], 47.0 * scale[0], -
              3.0 * scale[1], 88.0 * scale[0], -12.0 * scale[1])
    Curveto_r(42.0 * scale[0], -9.0 * scale[1], 78.0 * scale[0], -
              15.0 * scale[1], 80.0 * scale[0], -12.0 * scale[1])
    Curveto_r(5.0 * scale[0], 5.0 * scale[1], -81.0 * scale[0],
              30.0 * scale[1], -103.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0],
              6.0 * scale[1], -8.0 * scale[0], 15.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], 0.0 * scale[0],
              12.0 * scale[1], -7.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-23.0 * scale[0], -8.0 * scale[1], -42.0 * scale[0],
              23.0 * scale[1], -40.0 * scale[0], 66.0 * scale[1])
    Curveto_r(2.0 * scale[0], 36.0 * scale[1], -24.0 * scale[0],
              137.0 * scale[1], -29.0 * scale[0], 111.0 * scale[1])
    te.end_fill()
    Moveto(770.0 * scale[0], 1290.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0], -
              8.0 * scale[1], 16.0 * scale[0], -17.0 * scale[1])
    Curveto_r(3.0 * scale[0], -11.0 * scale[1], 5.0 *
              scale[0], -7.0 * scale[1], 6.0 * scale[0], 10.0 * scale[1])
    Curveto_r(1.0 * scale[0], 30.0 * scale[1], 1.0 * scale[0],
              30.0 * scale[1], -19.0 * scale[0], 17.0 * scale[1])
    te.end_fill()
    Moveto(366.0 * scale[0], 1253.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(793.0 * scale[0], 1235.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -10.0 * scale[1], -10.0 *
              scale[0], -15.0 * scale[1], 0.0 * scale[0], -23.0 * scale[1])
    Curveto_r(9.0 * scale[0], -8.0 * scale[1], 12.0 * scale[0], -
              4.0 * scale[1], 13.0 * scale[0], 14.0 * scale[1])
    Curveto_r(1.0 * scale[0], 13.0 * scale[1], 1.0 * scale[0],
              24.0 * scale[1], 0.0 * scale[0], 24.0 * scale[1])
    Curveto_r(0.0 * scale[0], -1.0 * scale[1], -6.0 * scale[0], -
              7.0 * scale[1], -13.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(602.0 * scale[0], 1220.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(245.0 * scale[0], 1221.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-17.0 * scale[0], -4.0 * scale[1], -40.0 *
              scale[0], -7.0 * scale[1], -52.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 1.0 * scale[1], -20.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -6.0 * scale[1])
    Curveto_r(2.0 * scale[0], -4.0 * scale[1], 1.0 * scale[0], -
              9.0 * scale[1], -3.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -2.0 * scale[1], -2.0 *
              scale[0], -2.0 * scale[1], 5.0 * scale[0], 0.0 * scale[1])
    Curveto_r(8.0 * scale[0], 2.0 * scale[1], 31.0 * scale[0],
              6.0 * scale[1], 53.0 * scale[0], 9.0 * scale[1])
    Curveto_r(22.0 * scale[0], 4.0 * scale[1], 42.0 * scale[0],
              11.0 * scale[1], 45.0 * scale[0], 15.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], 4.0 * scale[0],
              9.0 * scale[1], 2.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -1.0 * scale[1], -17.0 *
              scale[0], -4.0 * scale[1], -33.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(805.0 * scale[0], 1179.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0], -
              12.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 17.0 * scale[1], 1.0 * scale[0],
              20.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(158.0 * scale[0], 1169.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -5.0 * scale[1], -18.0 * scale[0], -
              18.0 * scale[1], -18.0 * scale[0], -27.0 * scale[1])
    Curveto_r(1.0 * scale[0], -16.0 * scale[1], 1.0 * scale[0], -
              16.0 * scale[1], 11.0 * scale[0], 1.0 * scale[1])
    Curveto_r(5.0 * scale[0], 9.0 * scale[1], 22.0 * scale[0],
              17.0 * scale[1], 37.0 * scale[0], 17.0 * scale[1])
    Curveto_r(21.0 * scale[0], 0.0 * scale[1], 24.0 * scale[0],
              2.0 * scale[1], 12.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 12.0 * scale[1], -21.0 * scale[0],
              12.0 * scale[1], -42.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(228.0 * scale[0], 1153.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(283.0 * scale[0], 1143.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(797.0 * scale[0], 1130.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -11.0 * scale[1], 9.0 * scale[0], -
              20.0 * scale[1], 15.0 * scale[0], -20.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 4.0 * scale[0],
              9.0 * scale[1], -2.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 11.0 * scale[1], -12.0 * scale[0],
              20.0 * scale[1], -14.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -2.0 * scale[0], -
              9.0 * scale[1], 1.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(133.0 * scale[0], 1113.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 25.0 *
              scale[0], -2.0 * scale[1], 35.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -27.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(628.0 * scale[0], 1033.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(431.0 * scale[0], 853.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -7.0 * scale[1], -29.0 * scale[0], -
              13.0 * scale[1], -46.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 0.0 * scale[1], -27.0 * scale[0], -
              2.0 * scale[1], -15.0 * scale[0], -11.0 * scale[1])
    Curveto_r(12.0 * scale[0], -9.0 * scale[1], 11.0 * scale[0], -
              10.0 * scale[1], -8.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 4.0 * scale[1], -25.0 * scale[0], -
              1.0 * scale[1], -32.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -10.0 * scale[1], -17.0 * scale[0], -
              19.0 * scale[1], -24.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -18.0 * scale[0], -
              12.0 * scale[1], -25.0 * scale[0], -27.0 * scale[1])
    Lineto_r(-13.0 * scale[0], -28.0 * scale[1])
    Lineto_r(24.0 * scale[0], 21.0 * scale[1])
    Curveto_r(12.0 * scale[0], 12.0 * scale[1], 34.0 * scale[0],
              25.0 * scale[1], 48.0 * scale[0], 29.0 * scale[1])
    Curveto_r(14.0 * scale[0], 4.0 * scale[1], 30.0 * scale[0],
              11.0 * scale[1], 35.0 * scale[0], 15.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 31.0 * scale[0],
              11.0 * scale[1], 57.0 * scale[0], 14.0 * scale[1])
    Curveto_r(26.0 * scale[0], 4.0 * scale[1], 47.0 * scale[0],
              10.0 * scale[1], 45.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 17.0 * scale[1], 19.0 * scale[0],
              13.0 * scale[1], 28.0 * scale[0], -4.0 * scale[1])
    Curveto_r(6.0 * scale[0], -11.0 * scale[1], 17.0 * scale[0], -
              30.0 * scale[1], 25.0 * scale[0], -44.0 * scale[1])
    Curveto_r(19.0 * scale[0], -33.0 * scale[1], 21.0 * scale[0], -
              43.0 * scale[1], 25.0 * scale[0], -122.0 * scale[1])
    Curveto_r(5.0 * scale[0], -80.0 * scale[1], 1.0 * scale[0], -
              82.0 * scale[1], -68.0 * scale[0], -38.0 * scale[1])
    Curveto_r(-58.0 * scale[0], 37.0 * scale[1], -67.0 * scale[0],
              37.0 * scale[1], -67.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -18.0 * scale[1], 12.0 * scale[0], -
              38.0 * scale[1], 36.0 * scale[0], -60.0 * scale[1])
    Curveto_r(23.0 * scale[0], -22.0 * scale[1], 30.0 * scale[0], -
              34.0 * scale[1], 20.0 * scale[0], -34.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0], -
              3.0 * scale[1], -17.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              19.0 * scale[1], -3.0 * scale[0], -31.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -13.0 * scale[1], -7.0 * scale[0], -
              27.0 * scale[1], -12.0 * scale[0], -30.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -4.0 * scale[1], -17.0 * scale[0], -
              19.0 * scale[1], -26.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -21.0 * scale[1], -22.0 *
              scale[0], -25.0 * scale[1], -47.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-29.0 * scale[0], 4.0 * scale[1], -67.0 * scale[0],
              44.0 * scale[1], -57.0 * scale[0], 60.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], -9.0 * scale[0],
              13.0 * scale[1], -25.0 * scale[0], 19.0 * scale[1])
    Lineto_r(-30.0 * scale[0], 12.0 * scale[1])
    Lineto_r(7.0 * scale[0], -32.0 * scale[1])
    Curveto_r(6.0 * scale[0], -29.0 * scale[1], 44.0 * scale[0], -
              76.0 * scale[1], 62.0 * scale[0], -78.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 18.0 * scale[0], -
              2.0 * scale[1], 32.0 * scale[0], -4.0 * scale[1])
    Curveto_r(19.0 * scale[0], -2.0 * scale[1], 37.0 * scale[0],
              10.0 * scale[1], 77.0 * scale[0], 51.0 * scale[1])
    Curveto_r(61.0 * scale[0], 64.0 * scale[1], 81.0 * scale[0],
              57.0 * scale[1], 23.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-22.0 * scale[0], -25.0 * scale[1], -36.0 *
              scale[0], -48.0 * scale[1], -32.0 * scale[0], -52.0 * scale[1])
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], -1.0 * scale[0], -
              4.0 * scale[1], -9.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 8.0 * scale[1], -52.0 * scale[0], -
              29.0 * scale[1], -45.0 * scale[0], -53.0 * scale[1])
    Curveto_r(4.0 * scale[0], -11.0 * scale[1], 17.0 * scale[0], -
              22.0 * scale[1], 31.0 * scale[0], -24.0 * scale[1])
    Curveto_r(19.0 * scale[0], -4.0 * scale[1], 26.0 * scale[0],
              1.0 * scale[1], 36.0 * scale[0], 23.0 * scale[1])
    Curveto_r(7.0 * scale[0], 18.0 * scale[1], 19.0 * scale[0],
              29.0 * scale[1], 30.0 * scale[0], 29.0 * scale[1])
    Curveto_r(15.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0],
              8.0 * scale[1], 19.0 * scale[0], 40.0 * scale[1])
    Curveto_r(0.0 * scale[0], 48.0 * scale[1], 26.0 * scale[0],
              95.0 * scale[1], 44.0 * scale[0], 81.0 * scale[1])
    Curveto_r(18.0 * scale[0], -15.0 * scale[1], 60.0 * scale[0],
              11.0 * scale[1], 64.0 * scale[0], 39.0 * scale[1])
    Curveto_r(2.0 * scale[0], 14.0 * scale[1], 12.0 * scale[0],
              34.0 * scale[1], 22.0 * scale[0], 45.0 * scale[1])
    Curveto_r(37.0 * scale[0], 42.0 * scale[1], 34.0 * scale[0],
              76.0 * scale[1], -12.0 * scale[0], 128.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 20.0 * scale[1], -33.0 * scale[0],
              85.0 * scale[1], -24.0 * scale[0], 95.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 6.0 * scale[0], -
              1.0 * scale[1], 6.0 * scale[0], -9.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 6.0 * scale[0], -
              4.0 * scale[1], 16.0 * scale[0], 9.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 12.0 * scale[0],
              27.0 * scale[1], 9.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -1.0 * scale[0],
              10.0 * scale[1], 6.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 6.0 * scale[0],
              6.0 * scale[1], -4.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 10.0 * scale[1], -14.0 * scale[0],
              22.0 * scale[1], -10.0 * scale[0], 25.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], -2.0 * scale[0],
              7.0 * scale[1], -12.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 0.0 * scale[1], -15.0 *
              scale[0], -3.0 * scale[1], -5.0 * scale[0], -15.0 * scale[1])
    Curveto_r(11.0 * scale[0], -13.0 * scale[1], 11.0 *
              scale[0], -18.0 * scale[1], 0.0 * scale[0], -28.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -10.0 * scale[1], -12.0 *
              scale[0], -9.0 * scale[1], -7.0 * scale[0], 6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 18.0 * scale[1], 1.0 * scale[0],
              20.0 * scale[1], -43.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-23.0 * scale[0], -1.0 * scale[1], -23.0 *
              scale[0], 0.0 * scale[1], -5.0 * scale[0], 9.0 * scale[1])
    Curveto_r(15.0 * scale[0], 7.0 * scale[1], 6.0 * scale[0],
              9.0 * scale[1], -34.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-30.0 * scale[0], -1.0 * scale[1], -61.0 *
              scale[0], -7.0 * scale[1], -70.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto_r(19.0 * scale[0], -23.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -5.0 * scale[1], -22.0 * scale[0], -
              10.0 * scale[1], -30.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0],
              1.0 * scale[1], 0.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 22.0 * scale[0],
              10.0 * scale[1], 30.0 * scale[0], 10.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0], -
              1.0 * scale[1], 0.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(250.0 * scale[0], 745.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -5.0 * scale[1], -4.0 * scale[0], -
              24.0 * scale[1], -6.0 * scale[0], -42.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -18.0 * scale[1], -8.0 * scale[0], -
              50.0 * scale[1], -13.0 * scale[0], -73.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -23.0 * scale[1], -5.0 *
              scale[0], -40.0 * scale[1], 0.0 * scale[0], -40.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0], -
              5.0 * scale[1], 9.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -4.0 * scale[0], -
              8.0 * scale[1], -9.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 4.0 * scale[1], -7.0 * scale[0], -
              3.0 * scale[1], -4.0 * scale[0], -14.0 * scale[1])
    Curveto_r(7.0 * scale[0], -27.0 * scale[1], 23.0 * scale[0], -
              36.0 * scale[1], 18.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 11.0 * scale[1], 3.0 * scale[0],
              27.0 * scale[1], 11.0 * scale[0], 35.0 * scale[1])
    Curveto_r(9.0 * scale[0], 8.0 * scale[1], 12.0 * scale[0],
              20.0 * scale[1], 8.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 7.0 * scale[1], -3.0 * scale[0],
              9.0 * scale[1], 3.0 * scale[0], 6.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 16.0 * scale[0],
              0.0 * scale[1], 23.0 * scale[0], 8.0 * scale[1])
    Curveto_r(9.0 * scale[0], 11.0 * scale[1], 9.0 * scale[0],
              19.0 * scale[1], -3.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 11.0 * scale[1], -16.0 * scale[0],
              18.0 * scale[1], -19.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -3.0 * scale[1], -4.0 * scale[0],
              5.0 * scale[1], -3.0 * scale[0], 18.0 * scale[1])
    Curveto_r(2.0 * scale[0], 12.0 * scale[1], 8.0 * scale[0],
              21.0 * scale[1], 14.0 * scale[0], 20.0 * scale[1])
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 11.0 * scale[0],
              2.0 * scale[1], 11.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -6.0 * scale[0],
              10.0 * scale[1], -14.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0],
              6.0 * scale[1], -19.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -6.0 * scale[0],
              8.0 * scale[1], -7.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto_r(30.0 * scale[0], -100.0 * scale[1], 0, 0)
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
    Moveto(659.0 * scale[0], 368.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -18.0 * scale[1], -31.0 *
              scale[0], -30.0 * scale[1], -25.0 * scale[0], -25.0 * scale[1])
    Curveto_r(5.0 * scale[0], 4.0 * scale[1], 13.0 * scale[0],
              7.0 * scale[1], 18.0 * scale[0], 7.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], -2.0 * scale[0], -
              62.0 * scale[1], -17.0 * scale[0], -80.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -8.0 * scale[1], -13.0 * scale[0], -
              37.0 * scale[1], -14.0 * scale[0], -64.0 * scale[1])
    Curveto_r(0.0 * scale[0], -27.0 * scale[1], -5.0 * scale[0], -
              54.0 * scale[1], -11.0 * scale[0], -60.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -5.0 * scale[1], -10.0 * scale[0], -
              18.0 * scale[1], -10.0 * scale[0], -28.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], -4.0 * scale[0], -
              18.0 * scale[1], -9.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              15.0 * scale[1], -15.0 * scale[0], -34.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -45.0 * scale[1], -22.0 * scale[0], -
              54.0 * scale[1], -86.0 * scale[0], -59.0 * scale[1])
    Curveto_r(-30.0 * scale[0], -2.0 * scale[1], -8.0 *
              scale[0], -2.0 * scale[1], 50.0 * scale[0], 0.0 * scale[1])
    Curveto_r(138.0 * scale[0], 6.0 * scale[1], 191.0 * scale[0],
              15.0 * scale[1], 200.0 * scale[0], 33.0 * scale[1])
    Curveto_r(5.0 * scale[0], 8.0 * scale[1], 13.0 * scale[0],
              26.0 * scale[1], 19.0 * scale[0], 40.0 * scale[1])
    Curveto_r(10.0 * scale[0], 23.0 * scale[1], 11.0 * scale[0],
              22.0 * scale[1], 8.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -24.0 * scale[1], 1.0 * scale[0], -
              38.0 * scale[1], 9.0 * scale[0], -38.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              11.0 * scale[1], 7.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 22.0 * scale[1], -2.0 * scale[0],
              23.0 * scale[1], 5.0 * scale[0], 7.0 * scale[1])
    Curveto_r(6.0 * scale[0], -13.0 * scale[1], 11.0 * scale[0],
              20.0 * scale[1], 16.0 * scale[0], 101.0 * scale[1])
    Curveto_r(8.0 * scale[0], 143.0 * scale[1], -2.0 * scale[0],
              182.0 * scale[1], -47.0 * scale[0], 175.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -2.0 * scale[1], -34.0 * scale[0],
              24.0 * scale[1], -29.0 * scale[0], 41.0 * scale[1])
    Curveto_r(7.0 * scale[0], 30.0 * scale[1], -31.0 * scale[0],
              22.0 * scale[1], -69.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(544.0 * scale[0], 278.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-29.0 * scale[0], -33.0 * scale[1])
    Lineto_r(33.0 * scale[0], 29.0 * scale[1])
    Curveto_r(30.0 * scale[0], 28.0 * scale[1], 37.0 * scale[0],
              36.0 * scale[1], 29.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0], -
              15.0 * scale[1], -33.0 * scale[0], -32.0 * scale[1])
    te.end_fill()
    Moveto(273.0 * scale[0], 288.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-32.0 * scale[0], -41.0 * scale[1], -50.0 * scale[0], -
              199.0 * scale[1], -29.0 * scale[0], -244.0 * scale[1])
    Curveto_r(12.0 * scale[0], -25.0 * scale[1], 72.0 * scale[0], -
              45.0 * scale[1], 128.0 * scale[0], -42.0 * scale[1])
    Curveto_r(28.0 * scale[0], 1.0 * scale[1], 26.0 * scale[0],
              2.0 * scale[1], -12.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-39.0 * scale[0], 5.0 * scale[1], -47.0 * scale[0],
              11.0 * scale[1], -62.0 * scale[0], 41.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 19.0 * scale[1], -17.0 * scale[0],
              59.0 * scale[1], -18.0 * scale[0], 90.0 * scale[1])
    Lineto_r(0.0 * scale[0], 55.0 * scale[1])
    Lineto_r(50.0 * scale[0], 3.0 * scale[1])
    Curveto_r(51.0 * scale[0], 3.0 * scale[1], 135.0 * scale[0],
              31.0 * scale[1], 95.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -31.0 * scale[0],
              7.0 * scale[1], -43.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 8.0 * scale[1], -22.0 * scale[0],
              13.0 * scale[1], -22.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -3.0 * scale[1], -12.0 * scale[0],
              6.0 * scale[1], -26.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 28.0 * scale[1], -47.0 * scale[0],
              31.0 * scale[1], -61.0 * scale[0], 13.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#26100c')
    te.end_fill()
    Moveto(16.0 * scale[0], 1384.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -8.0 * scale[1], -16.0 * scale[0], -
              21.0 * scale[1], -16.0 * scale[0], -27.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], 5.0 * scale[0], -
              4.0 * scale[1], 11.0 * scale[0], 5.0 * scale[1])
    Curveto_r(5.0 * scale[0], 10.0 * scale[1], 17.0 * scale[0],
              22.0 * scale[1], 27.0 * scale[0], 27.0 * scale[1])
    Curveto_r(9.0 * scale[0], 6.0 * scale[1], 12.0 * scale[0],
              11.0 * scale[1], 5.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -19.0 * scale[0], -
              7.0 * scale[1], -27.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(900.0 * scale[0], 1393.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(42.0 * scale[0], -5.0 * scale[1], 57.0 * scale[0], -
              17.0 * scale[1], 63.0 * scale[0], -46.0 * scale[1])
    Curveto_r(3.0 * scale[0], -16.0 * scale[1], 5.0 *
              scale[0], -13.0 * scale[1], 6.0 * scale[0], 9.0 * scale[1])
    Curveto_r(1.0 * scale[0], 36.0 * scale[1], -12.0 * scale[0],
              45.0 * scale[1], -67.0 * scale[0], 42.0 * scale[1])
    Lineto_r(-37.0 * scale[0], -1.0 * scale[1])
    Lineto_r(35.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(1.0 * scale[0], 1304.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(960.0 * scale[0], 1050.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], -7.0 * scale[0], -
              20.0 * scale[1], -20.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-26.0 * scale[0], 0.0 * scale[1], -26.0 * scale[0], -
              16.0 * scale[1], -1.0 * scale[0], -23.0 * scale[1])
    Curveto_r(17.0 * scale[0], -4.0 * scale[1], 19.0 * scale[0], -
              11.0 * scale[1], 15.0 * scale[0], -51.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -25.0 * scale[1], -1.0 *
              scale[0], -54.0 * scale[1], 5.0 * scale[0], -63.0 * scale[1])
    Curveto_r(8.0 * scale[0], -13.0 * scale[1], 10.0 * scale[0],
              8.0 * scale[1], 11.0 * scale[0], 80.0 * scale[1])
    Curveto_r(0.0 * scale[0], 53.0 * scale[1], -2.0 * scale[0],
              97.0 * scale[1], -5.0 * scale[0], 97.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -5.0 * scale[0], -
              9.0 * scale[1], -5.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(0.0 * scale[0], 934.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -59.0 * scale[1], 3.0 * scale[0], -
              104.0 * scale[1], 7.0 * scale[0], -101.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], 9.0 * scale[0],
              46.0 * scale[1], 12.0 * scale[0], 94.0 * scale[1])
    Lineto_r(6.0 * scale[0], 88.0 * scale[1])
    Lineto_r(50.0 * scale[0], 6.0 * scale[1])
    Lineto_r(50.0 * scale[0], 6.0 * scale[1])
    Lineto_r(-47.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 1.0 * scale[1], -53.0 * scale[0],
              5.0 * scale[1], -62.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 5.0 * scale[1], -16.0 * scale[0], -
              7.0 * scale[1], -16.0 * scale[0], -102.0 * scale[1])
    te.end_fill()
    Moveto(717.0 * scale[0], 1023.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(18.0 * scale[0], -2.0 * scale[1], 50.0 *
              scale[0], -2.0 * scale[1], 70.0 * scale[0], 0.0 * scale[1])
    Curveto_r(21.0 * scale[0], 2.0 * scale[1], 7.0 * scale[0],
              4.0 * scale[1], -32.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-38.0 * scale[0], 0.0 * scale[1], -55.0 *
              scale[0], -2.0 * scale[1], -38.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(615.0 * scale[0], 869.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -14.0 * scale[1], -3.0 *
              scale[0], -25.0 * scale[1], 4.0 * scale[0], -27.0 * scale[1])
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 11.0 * scale[0], -
              10.0 * scale[1], 11.0 * scale[0], -19.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 7.0 * scale[0], -
              13.0 * scale[1], 18.0 * scale[0], -11.0 * scale[1])
    Curveto_r(12.0 * scale[0], 2.0 * scale[1], 17.0 * scale[0],
              13.0 * scale[1], 17.0 * scale[0], 38.0 * scale[1])
    Curveto_r(0.0 * scale[0], 28.0 * scale[1], -4.0 * scale[0],
              36.0 * scale[1], -22.0 * scale[0], 38.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 2.0 * scale[1], -23.0 * scale[0], -
              4.0 * scale[1], -28.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(263.0 * scale[0], 814.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -1.0 * scale[0], -
              20.0 * scale[1], 6.0 * scale[0], -27.0 * scale[1])
    Curveto_r(8.0 * scale[0], -8.0 * scale[1], 11.0 * scale[0], -
              4.0 * scale[1], 11.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 30.0 * scale[1], -7.0 * scale[0],
              35.0 * scale[1], -17.0 * scale[0], 11.0 * scale[1])
    te.end_fill()
    Moveto(637.0 * scale[0], 768.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -7.0 * scale[1], 6.0 * scale[0], -
              21.0 * scale[1], 4.0 * scale[0], -32.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -10.0 * scale[1], 1.0 * scale[0], -
              16.0 * scale[1], 6.0 * scale[0], -13.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 15.0 * scale[0],
              2.0 * scale[1], 23.0 * scale[0], -3.0 * scale[1])
    Curveto_r(12.0 * scale[0], -7.0 * scale[1], 12.0 * scale[0], -
              11.0 * scale[1], 0.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -14.0 * scale[1], -11.0 *
              scale[0], -16.0 * scale[1], 11.0 * scale[0], -10.0 * scale[1])
    Curveto_r(23.0 * scale[0], 6.0 * scale[1], 25.0 * scale[0],
              3.0 * scale[1], 28.0 * scale[0], -37.0 * scale[1])
    Curveto_r(1.0 * scale[0], -23.0 * scale[1], 5.0 * scale[0], -
              45.0 * scale[1], 9.0 * scale[0], -48.0 * scale[1])
    Curveto_r(4.0 * scale[0], -3.0 * scale[1], 13.0 * scale[0], -
              15.0 * scale[1], 19.0 * scale[0], -27.0 * scale[1])
    Curveto_r(10.0 * scale[0], -18.0 * scale[1], 10.0 * scale[0], -
              25.0 * scale[1], -2.0 * scale[0], -36.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -8.0 * scale[1], -11.0 * scale[0], -
              24.0 * scale[1], -8.0 * scale[0], -35.0 * scale[1])
    Curveto_r(4.0 * scale[0], -16.0 * scale[1], 0.0 * scale[0], -
              21.0 * scale[1], -19.0 * scale[0], -24.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -2.0 * scale[1], -22.0 *
              scale[0], -9.0 * scale[1], -20.0 * scale[0], -21.0 * scale[1])
    Curveto_r(3.0 * scale[0], -20.0 * scale[1], -53.0 * scale[0], -
              78.0 * scale[1], -120.0 * scale[0], -124.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -14.0 * scale[1], -38.0 *
              scale[0], -30.0 * scale[1], -38.0 * scale[0], -35.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -4.0 * scale[0], -
              6.0 * scale[1], -10.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0], -
              1.0 * scale[1], -10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], -3.0 * scale[0], -
              15.0 * scale[1], -7.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 3.0 * scale[1], -33.0 * scale[0], -
              2.0 * scale[1], -27.0 * scale[0], -12.0 * scale[1])
    Curveto_r(4.0 * scale[0], -8.0 * scale[1], 0.0 * scale[0], -
              8.0 * scale[1], -15.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 8.0 * scale[1], -21.0 * scale[0],
              8.0 * scale[1], -21.0 * scale[0], 1.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -5.0 * scale[0], -
              10.0 * scale[1], -11.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0],
              5.0 * scale[1], -4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], -4.0 * scale[0],
              10.0 * scale[1], -16.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 0.0 * scale[1], -21.0 *
              scale[0], -1.0 * scale[1], -5.0 * scale[0], -19.0 * scale[1])
    Curveto_r(10.0 * scale[0], -10.0 * scale[1], 25.0 * scale[0], -
              21.0 * scale[1], 34.0 * scale[0], -23.0 * scale[1])
    Curveto_r(33.0 * scale[0], -9.0 * scale[1], 36.0 * scale[0], -
              8.0 * scale[1], 215.0 * scale[0], 150.0 * scale[1])
    Curveto_r(33.0 * scale[0], 28.0 * scale[1], 63.0 * scale[0],
              52.0 * scale[1], 68.0 * scale[0], 52.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              6.0 * scale[1], 9.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 9.0 * scale[0],
              18.0 * scale[1], 21.0 * scale[0], 21.0 * scale[1])
    Curveto_r(12.0 * scale[0], 4.0 * scale[1], 18.0 * scale[0],
              12.0 * scale[1], 15.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], -3.0 * scale[0],
              14.0 * scale[1], -1.0 * scale[0], 14.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 45.0 * scale[0], -
              34.0 * scale[1], 45.0 * scale[0], -43.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 10.0 * scale[0], -
              21.0 * scale[1], 22.0 * scale[0], -37.0 * scale[1])
    Curveto_r(16.0 * scale[0], -22.0 * scale[1], 25.0 * scale[0], -
              27.0 * scale[1], 34.0 * scale[0], -19.0 * scale[1])
    Curveto_r(18.0 * scale[0], 15.0 * scale[1], 51.0 * scale[0], -
              60.0 * scale[1], 57.0 * scale[0], -131.0 * scale[1])
    Curveto_r(2.0 * scale[0], -30.0 * scale[1], 2.0 * scale[0], -
              47.0 * scale[1], 0.0 * scale[0], -38.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 10.0 * scale[1], -9.0 * scale[0],
              18.0 * scale[1], -14.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -3.0 * scale[0], -
              12.0 * scale[1], 4.0 * scale[0], -28.0 * scale[1])
    Curveto_r(18.0 * scale[0], -34.0 * scale[1], 20.0 * scale[0], -
              192.0 * scale[1], 3.0 * scale[0], -193.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0], -
              3.0 * scale[1], -31.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -3.0 * scale[1], -60.0 * scale[0], -
              8.0 * scale[1], -110.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-89.0 * scale[0], -8.0 * scale[1], -89.0 *
              scale[0], -8.0 * scale[1], 53.0 * scale[0], -9.0 * scale[1])
    Lineto_r(142.0 * scale[0], -2.0 * scale[1])
    Lineto_r(0.0 * scale[0], 244.0 * scale[1])
    Curveto_r(0.0 * scale[0], 224.0 * scale[1], -1.0 * scale[0],
              245.0 * scale[1], -17.0 * scale[0], 250.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 3.0 * scale[1], -29.0 * scale[0],
              16.0 * scale[1], -43.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-33.0 * scale[0], 30.0 * scale[1], -66.0 * scale[0],
              48.0 * scale[1], -85.0 * scale[0], 48.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 0.0 * scale[1], -35.0 * scale[0],
              30.0 * scale[1], -35.0 * scale[0], 62.0 * scale[1])
    Curveto_r(0.0 * scale[0], 27.0 * scale[1], -56.0 * scale[0],
              89.0 * scale[1], -112.0 * scale[0], 124.0 * scale[1])
    Curveto_r(-42.0 * scale[0], 27.0 * scale[1], -53.0 * scale[0],
              30.0 * scale[1], -41.0 * scale[0], 12.0 * scale[1])
    te.end_fill()
    Moveto(435.0 * scale[0], 740.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -4.0 * scale[0], -
              22.0 * scale[1], -1.0 * scale[0], -36.0 * scale[1])
    Curveto_r(7.0 * scale[0], -28.0 * scale[1], 43.0 * scale[0], -
              33.0 * scale[1], 53.0 * scale[0], -8.0 * scale[1])
    Curveto_r(12.0 * scale[0], 32.0 * scale[1], -35.0 * scale[0],
              71.0 * scale[1], -52.0 * scale[0], 44.0 * scale[1])
    te.end_fill()
    Moveto_r(25.0 * scale[0], -20.0 * scale[1], 0, 0)
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
    Moveto(296.0 * scale[0], 705.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -11.0 * scale[1], 2.0 * scale[0], -
              13.0 * scale[1], -11.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 6.0 * scale[1], -16.0 * scale[0],
              4.0 * scale[1], -6.0 * scale[0], -14.0 * scale[1])
    Curveto_r(7.0 * scale[0], -12.0 * scale[1], 16.0 * scale[0], -
              22.0 * scale[1], 21.0 * scale[0], -22.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 32.0 * scale[0],
              38.0 * scale[1], 25.0 * scale[0], 50.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 16.0 * scale[1], -35.0 * scale[0],
              12.0 * scale[1], -29.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(190.0 * scale[0], 615.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-20.0 * scale[0], -38.0 * scale[1], -22.0 * scale[0], -
              54.0 * scale[1], -16.0 * scale[0], -106.0 * scale[1])
    Curveto_r(3.0 * scale[0], -34.0 * scale[1], 11.0 * scale[0], -
              68.0 * scale[1], 17.0 * scale[0], -75.0 * scale[1])
    Curveto_r(6.0 * scale[0], -7.0 * scale[1], 19.0 * scale[0], -
              29.0 * scale[1], 29.0 * scale[0], -48.0 * scale[1])
    Curveto_r(15.0 * scale[0], -30.0 * scale[1], 15.0 *
              scale[0], -37.0 * scale[1], 4.0 * scale[0], -47.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -6.0 * scale[1], -14.0 * scale[0], -
              19.0 * scale[1], -14.0 * scale[0], -28.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], -7.0 * scale[0], -
              27.0 * scale[1], -16.0 * scale[0], -39.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -12.0 * scale[1], -14.0 * scale[0], -
              28.0 * scale[1], -12.0 * scale[0], -34.0 * scale[1])
    Curveto_r(3.0 * scale[0], -7.0 * scale[1], -6.0 * scale[0], -
              28.0 * scale[1], -19.0 * scale[0], -47.0 * scale[1])
    Curveto_r(-23.0 * scale[0], -34.0 * scale[1], -28.0 * scale[0], -
              57.0 * scale[1], -24.0 * scale[0], -124.0 * scale[1])
    Curveto_r(1.0 * scale[0], -26.0 * scale[1], -3.0 * scale[0], -
              39.0 * scale[1], -14.0 * scale[0], -43.0 * scale[1])
    Curveto_r(-35.0 * scale[0], -14.0 * scale[1], -10.0 *
              scale[0], -24.0 * scale[1], 58.0 * scale[0], -23.0 * scale[1])
    Lineto_r(72.0 * scale[0], 1.0 * scale[1])
    Lineto_r(-40.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 7.0 * scale[1], -40.0 * scale[0],
              19.0 * scale[1], -40.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 16.0 * scale[1], 26.0 * scale[0],
              135.0 * scale[1], 52.0 * scale[0], 231.0 * scale[1])
    Curveto_r(15.0 * scale[0], 58.0 * scale[1], 21.0 * scale[0],
              67.0 * scale[1], 37.0 * scale[0], 62.0 * scale[1])
    Curveto_r(17.0 * scale[0], -6.0 * scale[1], 17.0 *
              scale[0], -4.0 * scale[1], -3.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 13.0 * scale[1], -20.0 * scale[0],
              32.0 * scale[1], -19.0 * scale[0], 44.0 * scale[1])
    Curveto_r(2.0 * scale[0], 11.0 * scale[1], -3.0 * scale[0],
              20.0 * scale[1], -11.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0],
              14.0 * scale[1], -18.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 19.0 * scale[1], -8.0 * scale[0],
              39.0 * scale[1], -13.0 * scale[0], 44.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 13.0 * scale[1], -13.0 * scale[0],
              29.0 * scale[1], 0.0 * scale[0], 21.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 8.0 * scale[0],
              12.0 * scale[1], 6.0 * scale[0], 42.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 26.0 * scale[1], 1.0 * scale[0],
              59.0 * scale[1], 6.0 * scale[0], 72.0 * scale[1])
    Curveto_r(15.0 * scale[0], 41.0 * scale[1], 2.0 * scale[0],
              33.0 * scale[1], -22.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(278.0 * scale[0], 593.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-25.0 * scale[0], -6.0 * scale[1], -24.0 *
              scale[0], -65.0 * scale[1], 1.0 * scale[0], -87.0 * scale[1])
    Curveto_r(42.0 * scale[0], -38.0 * scale[1], 101.0 * scale[0],
              11.0 * scale[1], 87.0 * scale[0], 70.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 20.0 * scale[1], -12.0 * scale[0],
              24.0 * scale[1], -39.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -1.0 * scale[1], -40.0 *
              scale[0], -3.0 * scale[1], -49.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto_r(55.0 * scale[0], -10.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              5.0 * scale[1], 12.0 * scale[0], 5.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(700.0 * scale[0], 500.0 * scale[1], x, y)
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
    Moveto(370.0 * scale[0], 369.0 * scale[1], x, y)
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
    Moveto(2.0 * scale[0], 138.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -70.0 * scale[1], 1.0 * scale[0], -
              129.0 * scale[1], 5.0 * scale[0], -131.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              34.0 * scale[1], 5.0 * scale[0], 81.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 160.0 * scale[1], -8.0 * scale[0],
              178.0 * scale[1], -10.0 * scale[0], 50.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#f7d0d2')
    te.end_fill()
    Moveto(103.0 * scale[0], 1313.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-52.0 * scale[0], -4.0 * scale[1], -53.0 *
              scale[0], -4.0 * scale[1], -52.0 * scale[0], -36.0 * scale[1])
    Curveto_r(2.0 * scale[0], -30.0 * scale[1], 2.0 * scale[0], -
              31.0 * scale[1], 6.0 * scale[0], -4.0 * scale[1])
    Curveto_r(4.0 * scale[0], 26.0 * scale[1], 7.0 * scale[0],
              27.0 * scale[1], 59.0 * scale[0], 27.0 * scale[1])
    Curveto_r(30.0 * scale[0], 0.0 * scale[1], 54.0 * scale[0],
              5.0 * scale[1], 54.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -3.0 * scale[0],
              9.0 * scale[1], -7.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -1.0 * scale[1], -32.0 *
              scale[0], -3.0 * scale[1], -60.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(414.0 * scale[0], 1298.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -13.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], -3.0 * scale[0], -11.0 * scale[1])
    Curveto_r(8.0 * scale[0], 7.0 * scale[1], 26.0 * scale[0],
              17.0 * scale[1], 40.0 * scale[0], 22.0 * scale[1])
    Curveto_r(22.0 * scale[0], 9.0 * scale[1], 22.0 * scale[0],
              10.0 * scale[1], 3.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 1.0 * scale[1], -29.0 * scale[0], -
              9.0 * scale[1], -40.0 * scale[0], -21.0 * scale[1])
    te.end_fill()
    Moveto(529.0 * scale[0], 1302.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(18.0 * scale[0], -10.0 * scale[1], 39.0 * scale[0], -
              29.0 * scale[1], 47.0 * scale[0], -42.0 * scale[1])
    Curveto_r(7.0 * scale[0], -14.0 * scale[1], 13.0 * scale[0], -
              19.0 * scale[1], 14.0 * scale[0], -12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 20.0 * scale[1], -55.0 * scale[0],
              72.0 * scale[1], -77.0 * scale[0], 72.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0], -
              6.0 * scale[1], 16.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(827.0 * scale[0], 1313.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-33.0 * scale[0], -4.0 * scale[1], -38.0 *
              scale[0], -7.0 * scale[1], -35.0 * scale[0], -26.0 * scale[1])
    Curveto_r(2.0 * scale[0], -17.0 * scale[1], 10.0 * scale[0], -
              22.0 * scale[1], 33.0 * scale[0], -23.0 * scale[1])
    Curveto_r(28.0 * scale[0], -1.0 * scale[1], 28.0 *
              scale[0], -1.0 * scale[1], 3.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-40.0 * scale[0], 6.0 * scale[1], -36.0 * scale[0],
              33.0 * scale[1], 5.0 * scale[0], 33.0 * scale[1])
    Curveto_r(17.0 * scale[0], 0.0 * scale[1], 42.0 * scale[0],
              3.0 * scale[1], 55.0 * scale[0], 6.0 * scale[1])
    Curveto_r(22.0 * scale[0], 6.0 * scale[1], 23.0 * scale[0],
              5.0 * scale[1], 17.0 * scale[0], -29.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -19.0 * scale[1], -3.0 *
              scale[0], -37.0 * scale[1], 2.0 * scale[0], -40.0 * scale[1])
    Curveto_r(4.0 * scale[0], -3.0 * scale[1], 9.0 * scale[0],
              15.0 * scale[1], 10.0 * scale[0], 39.0 * scale[1])
    Curveto_r(2.0 * scale[0], 49.0 * scale[1], 7.0 * scale[0],
              47.0 * scale[1], -90.0 * scale[0], 37.0 * scale[1])
    te.end_fill()
    Moveto(454.0 * scale[0], 1281.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-36.0 * scale[0], -33.0 * scale[1], -47.0 * scale[0], -
              73.0 * scale[1], -30.0 * scale[0], -106.0 * scale[1])
    Curveto_r(20.0 * scale[0], -38.0 * scale[1], 10.0 * scale[0], -
              47.0 * scale[1], -16.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 19.0 * scale[1], -19.0 * scale[0],
              35.0 * scale[1], -15.0 * scale[0], 67.0 * scale[1])
    Curveto_r(2.0 * scale[0], 24.0 * scale[1], 1.0 * scale[0],
              40.0 * scale[1], -4.0 * scale[0], 37.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -9.0 * scale[0], -
              23.0 * scale[1], -9.0 * scale[0], -44.0 * scale[1])
    Curveto_r(0.0 * scale[0], -30.0 * scale[1], 7.0 * scale[0], -
              48.0 * scale[1], 30.0 * scale[0], -72.0 * scale[1])
    Curveto_r(27.0 * scale[0], -30.0 * scale[1], 31.0 * scale[0], -
              31.0 * scale[1], 41.0 * scale[0], -15.0 * scale[1])
    Curveto_r(11.0 * scale[0], 18.0 * scale[1], 49.0 * scale[0],
              24.0 * scale[1], 49.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 9.0 * scale[0], -
              2.0 * scale[1], 21.0 * scale[0], 9.0 * scale[1])
    Curveto_r(18.0 * scale[0], 16.0 * scale[1], 19.0 * scale[0],
              22.0 * scale[1], 7.0 * scale[0], 40.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 18.0 * scale[1], -11.0 * scale[0],
              23.0 * scale[1], 1.0 * scale[0], 31.0 * scale[1])
    Curveto_r(12.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], -13.0 * scale[0], 44.0 * scale[1])
    Curveto_r(-31.0 * scale[0], 41.0 * scale[1], -35.0 * scale[0],
              43.0 * scale[1], -62.0 * scale[0], 17.0 * scale[1])
    te.end_fill()
    Moveto(155.0 * scale[0], 1270.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -11.0 * scale[1], -4.0 * scale[0], -
              24.0 * scale[1], -1.0 * scale[0], -29.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              22.0 * scale[1], -9.0 * scale[0], -37.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -16.0 * scale[1], -15.0 * scale[0], -
              37.0 * scale[1], -15.0 * scale[0], -46.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], -8.0 * scale[0], -
              18.0 * scale[1], -17.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -3.0 * scale[1], -14.0 *
              scale[0], -4.0 * scale[1], 1.0 * scale[0], -3.0 * scale[1])
    Curveto_r(14.0 * scale[0], 1.0 * scale[1], 23.0 * scale[0],
              11.0 * scale[1], 28.0 * scale[0], 34.0 * scale[1])
    Curveto_r(5.0 * scale[0], 17.0 * scale[1], 13.0 * scale[0],
              32.0 * scale[1], 18.0 * scale[0], 32.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              20.0 * scale[1], 8.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 51.0 * scale[1], -4.0 * scale[0],
              53.0 * scale[1], -13.0 * scale[0], 25.0 * scale[1])
    te.end_fill()
    Moveto(80.0 * scale[0], 1263.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 18.0 * scale[0], -
              11.0 * scale[1], 22.0 * scale[0], -17.0 * scale[1])
    Curveto_r(5.0 * scale[0], -7.0 * scale[1], 8.0 *
              scale[0], -4.0 * scale[1], 8.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], -7.0 * scale[0],
              17.0 * scale[1], -22.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -18.0 *
              scale[0], -2.0 * scale[1], -8.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(345.0 * scale[0], 1251.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              12.0 * scale[1], 5.0 * scale[0], -16.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 10.0 * scale[0],
              1.0 * scale[1], 10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 18.0 * scale[1], -6.0 * scale[0],
              21.0 * scale[1], -15.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(610.0 * scale[0], 1250.0 * scale[1], x, y)
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
    Moveto(816.0 * scale[0], 1234.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -9.0 * scale[1], -2.0 * scale[0], -
              22.0 * scale[1], 4.0 * scale[0], -29.0 * scale[1])
    Curveto_r(7.0 * scale[0], -8.0 * scale[1], 7.0 * scale[0], -
              21.0 * scale[1], 1.0 * scale[0], -38.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -20.0 * scale[1], -6.0 *
              scale[0], -27.0 * scale[1], 5.0 * scale[0], -31.0 * scale[1])
    Curveto_r(36.0 * scale[0], -14.0 * scale[1], 52.0 *
              scale[0], -6.0 * scale[1], 59.0 * scale[0], 27.0 * scale[1])
    Curveto_r(4.0 * scale[0], 17.0 * scale[1], 12.0 * scale[0],
              39.0 * scale[1], 19.0 * scale[0], 47.0 * scale[1])
    Curveto_r(9.0 * scale[0], 13.0 * scale[1], 9.0 * scale[0],
              13.0 * scale[1], -5.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -7.0 * scale[1], -19.0 * scale[0], -
              26.0 * scale[1], -23.0 * scale[0], -42.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -22.0 * scale[1], -11.0 * scale[0], -
              30.0 * scale[1], -27.0 * scale[0], -30.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0],
              4.0 * scale[1], -16.0 * scale[0], 27.0 * scale[1])
    Curveto_r(3.0 * scale[0], 15.0 * scale[1], 1.0 * scale[0],
              35.0 * scale[1], -4.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 12.0 * scale[1], -4.0 * scale[0],
              20.0 * scale[1], 8.0 * scale[0], 27.0 * scale[1])
    Curveto_r(16.0 * scale[0], 9.0 * scale[1], 16.0 * scale[0],
              10.0 * scale[1], 2.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0], -
              7.0 * scale[1], -23.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(73.0 * scale[0], 1185.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -31.0 * scale[1], 2.0 * scale[0], -
              53.0 * scale[1], 4.0 * scale[0], -51.0 * scale[1])
    Curveto_r(8.0 * scale[0], 8.0 * scale[1], 10.0 * scale[0],
              106.0 * scale[1], 3.0 * scale[0], 106.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              25.0 * scale[1], -7.0 * scale[0], -55.0 * scale[1])
    te.end_fill()
    Moveto(294.0 * scale[0], 1225.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -8.0 * scale[1], -14.0 *
              scale[0], -14.0 * scale[1], -9.0 * scale[0], -14.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0],
              6.0 * scale[1], 29.0 * scale[0], 14.0 * scale[1])
    Curveto_r(11.0 * scale[0], 8.0 * scale[1], 15.0 * scale[0],
              15.0 * scale[1], 10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -19.0 * scale[0], -
              7.0 * scale[1], -30.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(580.0 * scale[0], 1207.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -38.0 * scale[1], -39.0 * scale[0], -
              78.0 * scale[1], -86.0 * scale[0], -87.0 * scale[1])
    Curveto_r(-34.0 * scale[0], -7.0 * scale[1], -35.0 *
              scale[0], -8.0 * scale[1], -10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(43.0 * scale[0], -2.0 * scale[1], 95.0 * scale[0],
              37.0 * scale[1], 102.0 * scale[0], 77.0 * scale[1])
    Curveto_r(4.0 * scale[0], 18.0 * scale[1], 4.0 * scale[0],
              36.0 * scale[1], 0.0 * scale[0], 39.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              5.0 * scale[1], -6.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(658.0 * scale[0], 1208.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-21.0 * scale[0], -21.0 * scale[1], -10.0 *
              scale[0], -24.0 * scale[1], 17.0 * scale[0], -5.0 * scale[1])
    Curveto_r(10.0 * scale[0], 8.0 * scale[1], 14.0 * scale[0],
              16.0 * scale[1], 9.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -17.0 * scale[0], -
              3.0 * scale[1], -26.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(610.0 * scale[0], 1184.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 5.0 * scale[0], -
              12.0 * scale[1], 10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 8.0 * scale[0],
              11.0 * scale[1], 5.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 14.0 * scale[1], -15.0 * scale[0],
              11.0 * scale[1], -15.0 * scale[0], -7.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#4b2710')
    te.end_fill()
    Moveto(26.0 * scale[0], 1388.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], 0.0 * scale[0], -
              9.0 * scale[1], -6.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -10.0 *
              scale[0], -1.0 * scale[1], -10.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -3.0 * scale[0],
              10.0 * scale[1], -6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -10.0 * scale[1], 7.0 * scale[0], -
              28.0 * scale[1], 19.0 * scale[0], -20.0 * scale[1])
    Curveto_r(7.0 * scale[0], 5.0 * scale[1], 39.0 * scale[0],
              13.0 * scale[1], 72.0 * scale[0], 20.0 * scale[1])
    Lineto_r(60.0 * scale[0], 11.0 * scale[1])
    Lineto_r(-67.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-36.0 * scale[0], -1.0 * scale[1], -64.0 *
              scale[0], -5.0 * scale[1], -62.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(310.0 * scale[0], 1396.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 9.0 * scale[0], -
              6.0 * scale[1], 20.0 * scale[0], -9.0 * scale[1])
    Curveto_r(11.0 * scale[0], -3.0 * scale[1], 18.0 *
              scale[0], -1.0 * scale[1], 14.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 9.0 * scale[1], -34.0 * scale[0],
              13.0 * scale[1], -34.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(733.0 * scale[0], 1393.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(26.0 * scale[0], -2.0 * scale[1], 68.0 *
              scale[0], -2.0 * scale[1], 95.0 * scale[0], 0.0 * scale[1])
    Curveto_r(26.0 * scale[0], 2.0 * scale[1], 4.0 * scale[0],
              3.0 * scale[1], -48.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-52.0 * scale[0], 0.0 * scale[1], -74.0 *
              scale[0], -1.0 * scale[1], -47.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(920.0 * scale[0], 1383.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 22.0 * scale[0], -
              11.0 * scale[1], 30.0 * scale[0], -17.0 * scale[1])
    Curveto_r(13.0 * scale[0], -10.0 * scale[1], 13.0 *
              scale[0], -9.0 * scale[1], 1.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 9.0 * scale[1], -21.0 * scale[0],
              17.0 * scale[1], -30.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -1.0 * scale[1], -1.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(1.0 * scale[0], 1334.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(905.0 * scale[0], 1330.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(853.0 * scale[0], 1323.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(962.0 * scale[0], 1330.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -14.0 * scale[1], -6.0 * scale[0], -
              277.0 * scale[1], 1.0 * scale[0], -265.0 * scale[1])
    Curveto_r(4.0 * scale[0], 8.0 * scale[1], 6.0 * scale[0],
              72.0 * scale[1], 4.0 * scale[0], 142.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 70.0 * scale[1], -4.0 * scale[0],
              126.0 * scale[1], -5.0 * scale[0], 123.0 * scale[1])
    te.end_fill()
    Moveto(16.0 * scale[0], 1304.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -12.0 * scale[1], -16.0 * scale[0], -
              38.0 * scale[1], -14.0 * scale[0], -137.0 * scale[1])
    Curveto_r(1.0 * scale[0], -116.0 * scale[1], 6.0 * scale[0], -
              137.0 * scale[1], 33.0 * scale[0], -137.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 3.0 * scale[0],
              5.0 * scale[1], -5.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 11.0 * scale[1], -22.0 * scale[0],
              52.0 * scale[1], -6.0 * scale[0], 62.0 * scale[1])
    Curveto_r(8.0 * scale[0], 6.0 * scale[1], 8.0 * scale[0],
              8.0 * scale[1], -1.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0],
              25.0 * scale[1], -9.0 * scale[0], 88.0 * scale[1])
    Curveto_r(4.0 * scale[0], 106.0 * scale[1], 6.0 * scale[0],
              114.0 * scale[1], 17.0 * scale[0], 82.0 * scale[1])
    Lineto_r(9.0 * scale[0], -25.0 * scale[1])
    Lineto_r(-4.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 15.0 * scale[1], 2.0 * scale[0],
              29.0 * scale[1], 8.0 * scale[0], 32.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 7.0 * scale[0],
              5.0 * scale[1], -1.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 1.0 * scale[1], -19.0 * scale[0], -
              6.0 * scale[1], -27.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(920.0 * scale[0], 1276.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              17.0 * scale[1], 9.0 * scale[0], -20.0 * scale[1])
    Curveto_r(5.0 * scale[0], -4.0 * scale[1], 7.0 * scale[0],
              3.0 * scale[1], 4.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 23.0 * scale[1], -13.0 * scale[0],
              26.0 * scale[1], -13.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(46.0 * scale[0], 1194.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -51.0 * scale[1], 13.0 * scale[0], -
              91.0 * scale[1], 15.0 * scale[0], -48.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], 1.0 * scale[0],
              38.0 * scale[1], 2.0 * scale[0], 62.0 * scale[1])
    Curveto_r(1.0 * scale[0], 23.0 * scale[1], -2.0 * scale[0],
              42.0 * scale[1], -8.0 * scale[0], 42.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              24.0 * scale[1], -9.0 * scale[0], -56.0 * scale[1])
    te.end_fill()
    Moveto(920.0 * scale[0], 1220.0 * scale[1], x, y)
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
    Moveto(155.0 * scale[0], 1180.0 * scale[1], x, y)
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
    Moveto(891.0 * scale[0], 1154.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(120.0 * scale[0], 1030.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 14.0 * scale[0], -
              10.0 * scale[1], 32.0 * scale[0], -10.0 * scale[1])
    Curveto_r(36.0 * scale[0], 0.0 * scale[1], 35.0 * scale[0],
              4.0 * scale[1], -4.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 4.0 * scale[1], -28.0 * scale[0],
              2.0 * scale[1], -28.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(248.0 * scale[0], 1033.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(393.0 * scale[0], 1033.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(42.0 * scale[0], -2.0 * scale[1], 112.0 *
              scale[0], -2.0 * scale[1], 155.0 * scale[0], 0.0 * scale[1])
    Curveto_r(42.0 * scale[0], 1.0 * scale[1], 7.0 * scale[0],
              3.0 * scale[1], -78.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-85.0 * scale[0], 0.0 * scale[1], -120.0 *
              scale[0], -2.0 * scale[1], -77.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(668.0 * scale[0], 1023.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(840.0 * scale[0], 1020.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(36.0 * scale[0], -12.0 * scale[1], 80.0 *
              scale[0], -12.0 * scale[1], 80.0 * scale[0], 0.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -24.0 * scale[0],
              10.0 * scale[1], -52.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-42.0 * scale[0], -1.0 * scale[1], -48.0 *
              scale[0], -3.0 * scale[1], -28.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(528.0 * scale[0], 853.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(305.0 * scale[0], 822.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-22.0 * scale[0], -18.0 * scale[1], -51.0 *
              scale[0], -79.0 * scale[1], -43.0 * scale[0], -88.0 * scale[1])
    Curveto_r(3.0 * scale[0], -2.0 * scale[1], 11.0 * scale[0],
              9.0 * scale[1], 18.0 * scale[0], 26.0 * scale[1])
    Curveto_r(7.0 * scale[0], 16.0 * scale[1], 18.0 * scale[0],
              30.0 * scale[1], 26.0 * scale[0], 30.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 18.0 * scale[0],
              9.0 * scale[1], 24.0 * scale[0], 19.0 * scale[1])
    Curveto_r(7.0 * scale[0], 13.0 * scale[1], 17.0 * scale[0],
              18.0 * scale[1], 32.0 * scale[0], 14.0 * scale[1])
    Curveto_r(19.0 * scale[0], -4.0 * scale[1], 20.0 *
              scale[0], -3.0 * scale[1], 8.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 15.0 * scale[1], -42.0 * scale[0],
              13.0 * scale[1], -65.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(420.0 * scale[0], 830.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -9.0 * scale[1], -13.0 *
              scale[0], -10.0 * scale[1], 0.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 22.0 * scale[0],
              5.0 * scale[1], 30.0 * scale[0], 10.0 * scale[1])
    Curveto_r(13.0 * scale[0], 9.0 * scale[1], 13.0 * scale[0],
              10.0 * scale[1], 0.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -22.0 * scale[0], -
              5.0 * scale[1], -30.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(580.0 * scale[0], 829.0 * scale[1], x, y)
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
    Moveto(614.0 * scale[0], 811.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 0.0 * scale[0], -
              21.0 * scale[1], -8.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -13.0 * scale[1], -16.0 *
              scale[0], -17.0 * scale[1], -16.0 * scale[0], -9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -3.0 * scale[0],
              12.0 * scale[1], -6.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -10.0 * scale[1], 7.0 * scale[0], -
              75.0 * scale[1], 24.0 * scale[0], -95.0 * scale[1])
    Curveto_r(46.0 * scale[0], -52.0 * scale[1], 49.0 * scale[0], -
              86.0 * scale[1], 12.0 * scale[0], -128.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -11.0 * scale[1], -20.0 *
              scale[0], -31.0 * scale[1], -22.0 * scale[0], -45.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -28.0 * scale[1], -46.0 * scale[0], -
              54.0 * scale[1], -64.0 * scale[0], -39.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 14.0 * scale[1], -44.0 * scale[0], -
              33.0 * scale[1], -44.0 * scale[0], -81.0 * scale[1])
    Curveto_r(0.0 * scale[0], -32.0 * scale[1], -4.0 * scale[0], -
              40.0 * scale[1], -19.0 * scale[0], -40.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -23.0 * scale[0], -
              11.0 * scale[1], -30.0 * scale[0], -29.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -22.0 * scale[1], -17.0 *
              scale[0], -27.0 * scale[1], -36.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-49.0 * scale[0], 9.0 * scale[1], -41.0 * scale[0],
              38.0 * scale[1], 30.0 * scale[0], 107.0 * scale[1])
    Curveto_r(37.0 * scale[0], 35.0 * scale[1], 64.0 * scale[0],
              69.0 * scale[1], 60.0 * scale[0], 75.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 11.0 * scale[1], -112.0 * scale[0], -
              89.0 * scale[1], -107.0 * scale[0], -102.0 * scale[1])
    Curveto_r(1.0 * scale[0], -4.0 * scale[1], -2.0 * scale[0], -
              9.0 * scale[1], -8.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -10.0 * scale[0],
              1.0 * scale[1], -10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], -6.0 * scale[0],
              15.0 * scale[1], -12.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-41.0 * scale[0], -5.0 * scale[1], -82.0 * scale[0],
              31.0 * scale[1], -93.0 * scale[0], 79.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 32.0 * scale[1], -6.0 * scale[0],
              33.0 * scale[1], 15.0 * scale[0], 22.0 * scale[1])
    Curveto_r(11.0 * scale[0], -6.0 * scale[1], 29.0 *
              scale[0], -9.0 * scale[1], 38.0 * scale[0], -7.0 * scale[1])
    Curveto_r(13.0 * scale[0], 4.0 * scale[1], 12.0 * scale[0],
              5.0 * scale[1], -4.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-31.0 * scale[0], 2.0 * scale[1], -54.0 * scale[0],
              33.0 * scale[1], -54.0 * scale[0], 72.0 * scale[1])
    Curveto_r(0.0 * scale[0], 24.0 * scale[1], -3.0 * scale[0],
              30.0 * scale[1], -9.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -8.0 * scale[1], -8.0 * scale[0], -
              23.0 * scale[1], -6.0 * scale[0], -33.0 * scale[1])
    Curveto_r(5.0 * scale[0], -25.0 * scale[1], -11.0 * scale[0], -
              14.0 * scale[1], -18.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 11.0 * scale[1], -1.0 * scale[0],
              18.0 * scale[1], 4.0 * scale[0], 14.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 9.0 * scale[0],
              0.0 * scale[1], 9.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -4.0 * scale[0],
              11.0 * scale[1], -9.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -3.0 * scale[0],
              27.0 * scale[1], 4.0 * scale[0], 61.0 * scale[1])
    Curveto_r(12.0 * scale[0], 57.0 * scale[1], 12.0 * scale[0],
              59.0 * scale[1], -5.0 * scale[0], 44.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -9.0 * scale[1], -18.0 * scale[0], -
              26.0 * scale[1], -19.0 * scale[0], -38.0 * scale[1])
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], -1.0 * scale[0], -
              50.0 * scale[1], -2.0 * scale[0], -85.0 * scale[1])
    Curveto_r(0.0 * scale[0], -34.0 * scale[1], -5.0 * scale[0], -
              60.0 * scale[1], -10.0 * scale[0], -56.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 7.0 * scale[1], -12.0 *
              scale[0], -9.0 * scale[1], 0.0 * scale[0], -21.0 * scale[1])
    Curveto_r(5.0 * scale[0], -6.0 * scale[1], 11.0 * scale[0], -
              23.0 * scale[1], 13.0 * scale[0], -40.0 * scale[1])
    Curveto_r(2.0 * scale[0], -22.0 * scale[1], -1.0 * scale[0], -
              29.0 * scale[1], -12.0 * scale[0], -27.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 2.0 * scale[1], -11.0 * scale[0],
              0.0 * scale[1], -7.0 * scale[0], -5.0 * scale[1])
    Curveto_r(5.0 * scale[0], -4.0 * scale[1], 18.0 * scale[0], -
              8.0 * scale[1], 30.0 * scale[0], -8.0 * scale[1])
    Curveto_r(16.0 * scale[0], 0.0 * scale[1], 21.0 * scale[0], -
              6.0 * scale[1], 19.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -12.0 * scale[1], 7.0 * scale[0], -
              31.0 * scale[1], 19.0 * scale[0], -44.0 * scale[1])
    Curveto_r(20.0 * scale[0], -21.0 * scale[1], 20.0 *
              scale[0], -23.0 * scale[1], 3.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 5.0 * scale[1], -22.0 * scale[0], -
              4.0 * scale[1], -37.0 * scale[0], -62.0 * scale[1])
    Curveto_r(-26.0 * scale[0], -95.0 * scale[1], -53.0 * scale[0], -
              215.0 * scale[1], -52.0 * scale[0], -231.0 * scale[1])
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 76.0 * scale[0], -
              41.0 * scale[1], 120.0 * scale[0], -40.0 * scale[1])
    Lineto_r(30.0 * scale[0], 1.0 * scale[1])
    Lineto_r(-35.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 6.0 * scale[1], -39.0 * scale[0],
              19.0 * scale[1], -46.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 35.0 * scale[1], -7.0 * scale[0],
              165.0 * scale[1], 15.0 * scale[0], 220.0 * scale[1])
    Curveto_r(14.0 * scale[0], 36.0 * scale[1], 33.0 * scale[0],
              42.0 * scale[1], 64.0 * scale[0], 22.0 * scale[1])
    Curveto_r(20.0 * scale[0], -13.0 * scale[1], 26.0 *
              scale[0], -13.0 * scale[1], 31.0 * scale[0], -3.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 3.0 * scale[0],
              2.0 * scale[1], 0.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -14.0 * scale[1], -3.0 *
              scale[0], -22.0 * scale[1], 1.0 * scale[0], -18.0 * scale[1])
    Curveto_r(4.0 * scale[0], 4.0 * scale[1], 17.0 * scale[0],
              1.0 * scale[1], 29.0 * scale[0], -7.0 * scale[1])
    Curveto_r(30.0 * scale[0], -21.0 * scale[1], 42.0 *
              scale[0], -18.0 * scale[1], 21.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 19.0 * scale[1], -17.0 * scale[0],
              20.0 * scale[1], 4.0 * scale[0], 20.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0], -
              4.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              10.0 * scale[1], 4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              5.0 * scale[1], 11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], 7.0 * scale[0],
              7.0 * scale[1], 21.0 * scale[0], -1.0 * scale[1])
    Curveto_r(15.0 * scale[0], -8.0 * scale[1], 19.0 *
              scale[0], -8.0 * scale[1], 15.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], 6.0 * scale[0],
              15.0 * scale[1], 27.0 * scale[0], 12.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              6.0 * scale[1], 7.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 5.0 * scale[0],
              12.0 * scale[1], 10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 10.0 *
              scale[0], -2.0 * scale[1], 10.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 17.0 * scale[0],
              21.0 * scale[1], 38.0 * scale[0], 35.0 * scale[1])
    Curveto_r(67.0 * scale[0], 46.0 * scale[1], 123.0 * scale[0],
              104.0 * scale[1], 120.0 * scale[0], 124.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              19.0 * scale[1], 20.0 * scale[0], 21.0 * scale[1])
    Curveto_r(19.0 * scale[0], 3.0 * scale[1], 23.0 * scale[0],
              8.0 * scale[1], 19.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 11.0 * scale[1], 1.0 * scale[0],
              27.0 * scale[1], 8.0 * scale[0], 35.0 * scale[1])
    Curveto_r(12.0 * scale[0], 11.0 * scale[1], 12.0 * scale[0],
              18.0 * scale[1], 2.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 12.0 * scale[1], -15.0 * scale[0],
              24.0 * scale[1], -19.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 3.0 * scale[1], -8.0 * scale[0],
              25.0 * scale[1], -9.0 * scale[0], 48.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 40.0 * scale[1], -5.0 * scale[0],
              43.0 * scale[1], -28.0 * scale[0], 37.0 * scale[1])
    Curveto_r(-22.0 * scale[0], -6.0 * scale[1], -23.0 *
              scale[0], -4.0 * scale[1], -11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(12.0 * scale[0], 14.0 * scale[1], 12.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -18.0 * scale[0],
              6.0 * scale[1], -23.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -7.0 * scale[0], 13.0 * scale[1])
    Curveto_r(1.0 * scale[0], 11.0 * scale[1], 1.0 * scale[0],
              22.0 * scale[1], 0.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 4.0 * scale[1], -3.0 * scale[0],
              17.0 * scale[1], -4.0 * scale[0], 29.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], -7.0 * scale[0],
              23.0 * scale[1], -15.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -11.0 * scale[0],
              0.0 * scale[1], -7.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto_r(106.0 * scale[0], -311.0 * scale[1], 0, 0)
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
    Moveto(270.0 * scale[0], 710.0 * scale[1], x, y)
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
    Moveto(285.0 * scale[0], 671.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -15.0 * scale[1], 15.0 * scale[0], -
              25.0 * scale[1], 28.0 * scale[0], -12.0 * scale[1])
    Curveto_r(9.0 * scale[0], 9.0 * scale[1], 7.0 * scale[0],
              10.0 * scale[1], -7.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -5.0 * scale[1], -17.0 *
              scale[0], -4.0 * scale[1], -12.0 * scale[0], 4.0 * scale[1])
    Curveto_r(4.0 * scale[0], 7.0 * scale[1], 5.0 * scale[0],
              12.0 * scale[1], 2.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              4.0 * scale[1], -11.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(197.0 * scale[0], 653.0 * scale[1], x, y)
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
    Moveto(766.0 * scale[0], 486.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -9.0 * scale[1], -3.0 * scale[0], -
              17.0 * scale[1], -15.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -3.0 * scale[1], -21.0 * scale[0], -
              12.0 * scale[1], -21.0 * scale[0], -19.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -12.0 * scale[0], -
              19.0 * scale[1], -27.0 * scale[0], -28.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -9.0 * scale[1], -44.0 * scale[0], -
              33.0 * scale[1], -63.0 * scale[0], -54.0 * scale[1])
    Lineto_r(-35.0 * scale[0], -38.0 * scale[1])
    Lineto_r(44.0 * scale[0], 37.0 * scale[1])
    Curveto_r(48.0 * scale[0], 40.0 * scale[1], 87.0 * scale[0],
              49.0 * scale[1], 79.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -17.0 * scale[1], 14.0 * scale[0], -
              43.0 * scale[1], 29.0 * scale[0], -41.0 * scale[1])
    Curveto_r(45.0 * scale[0], 7.0 * scale[1], 55.0 * scale[0], -
              32.0 * scale[1], 47.0 * scale[0], -175.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -81.0 * scale[1], -10.0 * scale[0], -
              114.0 * scale[1], -16.0 * scale[0], -101.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 16.0 * scale[1], -8.0 * scale[0],
              15.0 * scale[1], -5.0 * scale[0], -8.0 * scale[1])
    Curveto_r(3.0 * scale[0], -16.0 * scale[1], 0.0 * scale[0], -
              27.0 * scale[1], -7.0 * scale[0], -27.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0],
              14.0 * scale[1], -9.0 * scale[0], 38.0 * scale[1])
    Curveto_r(3.0 * scale[0], 34.0 * scale[1], 2.0 * scale[0],
              35.0 * scale[1], -8.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -14.0 * scale[0], -
              32.0 * scale[1], -19.0 * scale[0], -40.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -9.0 * scale[1], -35.0 * scale[0], -
              19.0 * scale[1], -81.0 * scale[0], -27.0 * scale[1])
    Lineto_r(-74.0 * scale[0], -11.0 * scale[1])
    Lineto_r(115.0 * scale[0], 4.0 * scale[1])
    Curveto_r(98.0 * scale[0], 4.0 * scale[1], 158.0 * scale[0],
              10.0 * scale[1], 193.0 * scale[0], 19.0 * scale[1])
    Curveto_r(4.0 * scale[0], 2.0 * scale[1], 14.0 * scale[0],
              3.0 * scale[1], 22.0 * scale[0], 4.0 * scale[1])
    Curveto_r(12.0 * scale[0], 1.0 * scale[1], 13.0 * scale[0],
              25.0 * scale[1], 10.0 * scale[0], 149.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 124.0 * scale[1], -7.0 * scale[0],
              154.0 * scale[1], -25.0 * scale[0], 190.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 33.0 * scale[1], -24.0 * scale[0],
              41.0 * scale[1], -34.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -8.0 * scale[1], -18.0 *
              scale[0], -3.0 * scale[1], -34.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 16.0 * scale[1], -22.0 * scale[0],
              33.0 * scale[1], -22.0 * scale[0], 37.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], -36.0 * scale[0],
              43.0 * scale[1], -45.0 * scale[0], 43.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -2.0 * scale[0], -
              6.0 * scale[1], 1.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto_r(154.0 * scale[0], -251.0 * scale[1], 0, 0)
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
    Moveto(580.0 * scale[0], 320.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(509.0 * scale[0], 253.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(16.0 * scale[0], 13.0 * scale[1], 21.0 * scale[0],
              21.0 * scale[1], 13.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              8.0 * scale[1], -17.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(128.0 * scale[0], 47.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -19.0 * scale[1], -2.0 *
              scale[0], -25.0 * scale[1], 4.0 * scale[0], -19.0 * scale[1])
    Curveto_r(6.0 * scale[0], 6.0 * scale[1], 8.0 * scale[0],
              18.0 * scale[1], 6.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 14.0 * scale[1], -5.0 * scale[0],
              12.0 * scale[1], -10.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(558.0 * scale[0], 3.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#7a599a')
    te.end_fill()
    Moveto(468.0 * scale[0], 1303.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(520.0 * scale[0], 1271.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 18.0 * scale[1], -14.0 * scale[0],
              21.0 * scale[1], -14.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(390.0 * scale[0], 1205.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 5.0 * scale[0], -
              15.0 * scale[1], 10.0 * scale[0], -15.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              7.0 * scale[1], 10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -4.0 * scale[0],
              15.0 * scale[1], -10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              7.0 * scale[1], -10.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(540.0 * scale[0], 1168.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 4.0 * scale[0], -
              8.0 * scale[1], 9.0 * scale[0], -8.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              4.0 * scale[1], 15.0 * scale[0], 8.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], -1.0 * scale[0],
              9.0 * scale[1], -9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              4.0 * scale[1], -15.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(468.0 * scale[0], 1143.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(526.0 * scale[0], 1138.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 10.0 * scale[0], -
              6.0 * scale[1], 15.0 * scale[0], -3.0 * scale[1])
    Curveto_r(13.0 * scale[0], 9.0 * scale[1], 11.0 * scale[0],
              12.0 * scale[1], -6.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -9.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(370.0 * scale[0], 1022.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 12.0 * scale[0], -
              14.0 * scale[1], 27.0 * scale[0], -21.0 * scale[1])
    Curveto_r(22.0 * scale[0], -10.0 * scale[1], 24.0 * scale[0], -
              14.0 * scale[1], 12.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -7.0 * scale[1], -9.0 *
              scale[0], -9.0 * scale[1], 7.0 * scale[0], -9.0 * scale[1])
    Curveto_r(23.0 * scale[0], 0.0 * scale[1], 48.0 * scale[0],
              23.0 * scale[1], 37.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -1.0 * scale[0],
              7.0 * scale[1], 5.0 * scale[0], 7.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0], -
              4.0 * scale[1], 17.0 * scale[0], -10.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 13.0 * scale[0], -
              6.0 * scale[1], 21.0 * scale[0], -3.0 * scale[1])
    Curveto_r(10.0 * scale[0], 4.0 * scale[1], 17.0 * scale[0], -
              2.0 * scale[1], 21.0 * scale[0], -16.0 * scale[1])
    Curveto_r(3.0 * scale[0], -11.0 * scale[1], 12.0 * scale[0], -
              21.0 * scale[1], 19.0 * scale[0], -21.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0], -
              5.0 * scale[1], -2.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-26.0 * scale[0], -39.0 * scale[1], -10.0 *
              scale[0], -41.0 * scale[1], 48.0 * scale[0], -4.0 * scale[1])
    Curveto_r(49.0 * scale[0], 31.0 * scale[1], 57.0 * scale[0],
              34.0 * scale[1], 139.0 * scale[0], 34.0 * scale[1])
    Curveto_r(48.0 * scale[0], 0.0 * scale[1], 82.0 * scale[0],
              3.0 * scale[1], 75.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -26.0 * scale[0],
              8.0 * scale[1], -45.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 0.0 * scale[1], -32.0 * scale[0],
              4.0 * scale[1], -28.0 * scale[0], 14.0 * scale[1])
    Curveto_r(7.0 * scale[0], 18.0 * scale[1], -76.0 * scale[0],
              28.0 * scale[1], -222.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-60.0 * scale[0], -1.0 * scale[1], -114.0 * scale[0],
              2.0 * scale[1], -120.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -11.0 * scale[0],
              3.0 * scale[1], -11.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(105.0 * scale[0], 990.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -16.0 * scale[1], -15.0 * scale[0], -
              35.0 * scale[1], -15.0 * scale[0], -43.0 * scale[1])
    Curveto_r(0.0 * scale[0], -18.0 * scale[1], -46.0 * scale[0], -
              104.0 * scale[1], -65.0 * scale[0], -124.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -11.0 * scale[1], -15.0 * scale[0], -
              43.0 * scale[1], -15.0 * scale[0], -144.0 * scale[1])
    Curveto_r(0.0 * scale[0], -84.0 * scale[1], 4.0 * scale[0], -
              128.0 * scale[1], 10.0 * scale[0], -124.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 10.0 * scale[0],
              51.0 * scale[1], 10.0 * scale[0], 110.0 * scale[1])
    Curveto_r(0.0 * scale[0], 73.0 * scale[1], 4.0 * scale[0],
              105.0 * scale[1], 13.0 * scale[0], 108.0 * scale[1])
    Curveto_r(10.0 * scale[0], 4.0 * scale[1], 10.0 * scale[0],
              6.0 * scale[1], 0.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 1.0 * scale[1], -13.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], 60.0 * scale[0],
              0.0 * scale[1], 95.0 * scale[0], -27.0 * scale[1])
    Lineto_r(31.0 * scale[0], -23.0 * scale[1])
    Lineto_r(17.0 * scale[0], 47.0 * scale[1])
    Curveto_r(9.0 * scale[0], 26.0 * scale[1], 25.0 * scale[0],
              56.0 * scale[1], 35.0 * scale[0], 67.0 * scale[1])
    Curveto_r(24.0 * scale[0], 29.0 * scale[1], 84.0 * scale[0],
              55.0 * scale[1], 126.0 * scale[0], 55.0 * scale[1])
    Curveto_r(20.0 * scale[0], 0.0 * scale[1], 36.0 * scale[0],
              5.0 * scale[1], 36.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -10.0 * scale[0],
              8.0 * scale[1], -22.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -3.0 * scale[1], -39.0 *
              scale[0], -7.0 * scale[1], -59.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -3.0 * scale[1], -48.0 * scale[0], -
              14.0 * scale[1], -62.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -11.0 * scale[1], -32.0 *
              scale[0], -17.0 * scale[1], -41.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 7.0 * scale[1], -19.0 * scale[0],
              4.0 * scale[1], -1.0 * scale[0], 41.0 * scale[1])
    Curveto_r(11.0 * scale[0], 23.0 * scale[1], 25.0 * scale[0],
              33.0 * scale[1], 50.0 * scale[0], 37.0 * scale[1])
    Curveto_r(19.0 * scale[0], 4.0 * scale[1], 35.0 * scale[0],
              13.0 * scale[1], 35.0 * scale[0], 19.0 * scale[1])
    Curveto_r(0.0 * scale[0], 21.0 * scale[1], 20.0 * scale[0],
              35.0 * scale[1], 41.0 * scale[0], 30.0 * scale[1])
    Curveto_r(10.0 * scale[0], -3.0 * scale[1], 19.0 * scale[0], -
              12.0 * scale[1], 19.0 * scale[0], -19.0 * scale[1])
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 16.0 * scale[0], -
              19.0 * scale[1], 25.0 * scale[0], -4.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], 12.0 * scale[0],
              7.0 * scale[1], 20.0 * scale[0], 3.0 * scale[1])
    Curveto_r(27.0 * scale[0], -10.0 * scale[1], 16.0 * scale[0],
              6.0 * scale[1], -15.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 11.0 * scale[1], -59.0 * scale[0],
              15.0 * scale[1], -134.0 * scale[0], 15.0 * scale[1])
    Lineto_r(-105.0 * scale[0], 0.0 * scale[1])
    Lineto_r(-16.0 * scale[0], -30.0 * scale[1])
    te.end_fill()
    Moveto_r(47.0 * scale[0], -162.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -9.0 * scale[1], -12.0 *
              scale[0], -7.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 19.0 * scale[1], 3.0 * scale[0],
              21.0 * scale[1], 12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(9.0 * scale[0], -9.0 * scale[1], 9.0 * scale[0], -
              15.0 * scale[1], 0.0 * scale[0], -24.0 * scale[1])
    te.end_fill()
    Moveto(820.0 * scale[0], 956.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 9.0 * scale[0], -
              6.0 * scale[1], 20.0 * scale[0], -9.0 * scale[1])
    Curveto_r(11.0 * scale[0], -3.0 * scale[1], 18.0 *
              scale[0], -1.0 * scale[1], 14.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 9.0 * scale[1], -34.0 * scale[0],
              13.0 * scale[1], -34.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(893.0 * scale[0], 923.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(15.0 * scale[0], -11.0 * scale[1], 24.0 * scale[0], -
              23.0 * scale[1], 20.0 * scale[0], -26.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], 1.0 * scale[0], -
              7.0 * scale[1], 10.0 * scale[0], -7.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0], -
              3.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 3.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -33.0 * scale[1])
    Curveto_r(2.0 * scale[0], -14.0 * scale[1], 5.0 * scale[0], -
              76.0 * scale[1], 6.0 * scale[0], -138.0 * scale[1])
    Curveto_r(1.0 * scale[0], -106.0 * scale[1], 0.0 * scale[0], -
              113.0 * scale[1], -23.0 * scale[0], -133.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -11.0 * scale[1], -32.0 *
              scale[0], -18.0 * scale[1], -43.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 3.0 * scale[1], -15.0 * scale[0],
              2.0 * scale[1], -10.0 * scale[0], -3.0 * scale[1])
    Curveto_r(18.0 * scale[0], -15.0 * scale[1], 83.0 * scale[0], -
              61.0 * scale[1], 86.0 * scale[0], -61.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 3.0 * scale[0],
              80.0 * scale[1], 3.0 * scale[0], 178.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 192.0 * scale[1], -7.0 * scale[0],
              220.0 * scale[1], -54.0 * scale[0], 243.0 * scale[1])
    Curveto_r(-42.0 * scale[0], 22.0 * scale[1], -48.0 * scale[0],
              22.0 * scale[1], -18.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(470.0 * scale[0], 886.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 13.0 * scale[0], -
              6.0 * scale[1], 29.0 * scale[0], -8.0 * scale[1])
    Curveto_r(17.0 * scale[0], -2.0 * scale[1], 28.0 *
              scale[0], -1.0 * scale[1], 25.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 8.0 * scale[1], -54.0 * scale[0],
              12.0 * scale[1], -54.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(353.0 * scale[0], 853.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(191.0 * scale[0], 679.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -11.0 * scale[1], -21.0 *
              scale[0], -35.0 * scale[1], -24.0 * scale[0], -52.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -45.0 * scale[1], 0.0 * scale[0], -
              46.0 * scale[1], 12.0 * scale[0], -2.0 * scale[1])
    Curveto_r(5.0 * scale[0], 21.0 * scale[1], 18.0 * scale[0],
              46.0 * scale[1], 27.0 * scale[0], 56.0 * scale[1])
    Curveto_r(9.0 * scale[0], 11.0 * scale[1], 14.0 * scale[0],
              19.0 * scale[1], 11.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              9.0 * scale[1], -26.0 * scale[0], -21.0 * scale[1])
    te.end_fill()
    Moveto(791.0 * scale[0], 644.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(800.0 * scale[0], 601.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 18.0 * scale[1], -14.0 * scale[0],
              21.0 * scale[1], -14.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(3.0 * scale[0], 480.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -36.0 * scale[1], 2.0 * scale[0], -
              50.0 * scale[1], 4.0 * scale[0], -32.0 * scale[1])
    Curveto_r(2.0 * scale[0], 17.0 * scale[1], 2.0 * scale[0],
              47.0 * scale[1], 0.0 * scale[0], 65.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 17.0 * scale[1], -4.0 * scale[0],
              3.0 * scale[1], -4.0 * scale[0], -33.0 * scale[1])
    te.end_fill()
    Moveto(12.0 * scale[0], 380.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 2.0 * scale[0], -
              27.0 * scale[1], 5.0 * scale[0], -17.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              25.0 * scale[1], 0.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(17.0 * scale[0], 313.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -15.0 * scale[1], 5.0 * scale[0], -
              84.0 * scale[1], 4.0 * scale[0], -153.0 * scale[1])
    Curveto_r(0.0 * scale[0], -69.0 * scale[1], 3.0 * scale[0], -
              131.0 * scale[1], 8.0 * scale[0], -138.0 * scale[1])
    Curveto_r(12.0 * scale[0], -20.0 * scale[1], 60.0 *
              scale[0], -22.0 * scale[1], 71.0 * scale[0], -3.0 * scale[1])
    Curveto_r(4.0 * scale[0], 9.0 * scale[1], 13.0 * scale[0],
              45.0 * scale[1], 20.0 * scale[0], 79.0 * scale[1])
    Curveto_r(6.0 * scale[0], 34.0 * scale[1], 20.0 * scale[0],
              78.0 * scale[1], 32.0 * scale[0], 98.0 * scale[1])
    Curveto_r(11.0 * scale[0], 19.0 * scale[1], 18.0 * scale[0],
              38.0 * scale[1], 14.0 * scale[0], 41.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], 0.0 * scale[0],
              13.0 * scale[1], 7.0 * scale[0], 21.0 * scale[1])
    Curveto_r(10.0 * scale[0], 13.0 * scale[1], 9.0 * scale[0],
              14.0 * scale[1], -10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-29.0 * scale[0], -16.0 * scale[1], -36.0 *
              scale[0], -15.0 * scale[1], -30.0 * scale[0], 3.0 * scale[1])
    Curveto_r(5.0 * scale[0], 13.0 * scale[1], -15.0 * scale[0],
              25.0 * scale[1], -114.0 * scale[0], 73.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 1.0 * scale[1], -4.0 * scale[0], -
              10.0 * scale[1], -2.0 * scale[0], -25.0 * scale[1])
    te.end_fill()
    Moveto(201.0 * scale[0], 314.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.penup()
