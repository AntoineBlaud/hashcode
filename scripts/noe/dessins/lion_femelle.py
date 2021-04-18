import turtle as te
from helper import *


def lion_femelle(x, y, scale):
    te.penup()
    te.color('#3f1504')
    te.end_fill()
    Moveto(868.0 * scale[0], 1389.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(97.0 * scale[0], -16.0 * scale[1], 93.0 * scale[0], -
              9.0 * scale[1], 90.0 * scale[0], -182.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -84.0 * scale[1], -7.0 * scale[0], -
              160.0 * scale[1], -12.0 * scale[0], -169.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -13.0 * scale[1], -4.0 *
              scale[0], -18.0 * scale[1], 8.0 * scale[0], -18.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0],
              21.0 * scale[1], 16.0 * scale[0], 178.0 * scale[1])
    Curveto_r(0.0 * scale[0], 125.0 * scale[1], -4.0 * scale[0],
              182.0 * scale[1], -12.0 * scale[0], 190.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 7.0 * scale[1], -38.0 * scale[0],
              12.0 * scale[1], -77.0 * scale[0], 11.0 * scale[1])
    Lineto_r(-66.0 * scale[0], -1.0 * scale[1])
    Lineto_r(53.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(6.0 * scale[0], 1374.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -29.0 * scale[1], -6.0 *
              scale[0], -39.0 * scale[1], 9.0 * scale[0], -17.0 * scale[1])
    Curveto_r(11.0 * scale[0], 16.0 * scale[1], 28.0 * scale[0],
              23.0 * scale[1], 63.0 * scale[0], 26.0 * scale[1])
    Lineto_r(47.0 * scale[0], 3.0 * scale[1])
    Lineto_r(-56.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-44.0 * scale[0], 2.0 * scale[1], -58.0 * scale[0], -
              2.0 * scale[1], -63.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(0.0 * scale[0], 1275.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 2.0 * scale[0], -
              35.0 * scale[1], 4.0 * scale[0], -35.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 6.0 * scale[0],
              16.0 * scale[1], 8.0 * scale[0], 35.0 * scale[1])
    Curveto_r(2.0 * scale[0], 19.0 * scale[1], 0.0 * scale[0],
              35.0 * scale[1], -4.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              16.0 * scale[1], -8.0 * scale[0], -35.0 * scale[1])
    te.end_fill()
    Moveto(37.0 * scale[0], 1290.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -11.0 * scale[1], 7.0 * scale[0], -
              20.0 * scale[1], 9.0 * scale[0], -20.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 4.0 * scale[0],
              9.0 * scale[1], 4.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], -4.0 * scale[0],
              20.0 * scale[1], -9.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              9.0 * scale[1], -4.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(1.0 * scale[0], 1203.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -22.0 * scale[1], 4.0 * scale[0], -
              33.0 * scale[1], 17.0 * scale[0], -36.0 * scale[1])
    Curveto_r(16.0 * scale[0], -4.0 * scale[1], 16.0 *
              scale[0], -5.0 * scale[1], 0.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -1.0 * scale[1], -18.0 * scale[0], -
              10.0 * scale[1], -18.0 * scale[0], -37.0 * scale[1])
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 4.0 * scale[0], -
              33.0 * scale[1], 9.0 * scale[0], -30.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], 6.0 * scale[0],
              18.0 * scale[1], 3.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 23.0 * scale[1], -2.0 * scale[0],
              26.0 * scale[1], 12.0 * scale[0], 21.0 * scale[1])
    Curveto_r(14.0 * scale[0], -5.0 * scale[1], 17.0 *
              scale[0], -2.0 * scale[1], 14.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 18.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 25.0 * scale[0], 25.0 * scale[1])
    Curveto_r(15.0 * scale[0], 2.0 * scale[1], 27.0 * scale[0],
              7.0 * scale[1], 27.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], -40.0 * scale[0],
              1.0 * scale[1], -57.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -14.0 *
              scale[0], -5.0 * scale[1], -17.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 8.0 * scale[1], -7.0 * scale[0],
              21.0 * scale[1], -9.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], -6.0 * scale[0],
              1.0 * scale[1], -6.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(1.0 * scale[0], 1053.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -27.0 * scale[1], 3.0 * scale[0], -
              33.0 * scale[1], 19.0 * scale[0], -33.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0],
              5.0 * scale[1], 20.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              10.0 * scale[1], -10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0],
              10.0 * scale[1], -20.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 20.0 * scale[1], -9.0 * scale[0],
              19.0 * scale[1], -9.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(128.0 * scale[0], 1023.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(18.0 * scale[0], -2.0 * scale[1], 45.0 *
              scale[0], -2.0 * scale[1], 60.0 * scale[0], 0.0 * scale[1])
    Curveto_r(15.0 * scale[0], 2.0 * scale[1], 0.0 * scale[0],
              4.0 * scale[1], -33.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-33.0 * scale[0], 0.0 * scale[1], -45.0 *
              scale[0], -2.0 * scale[1], -27.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(888.0 * scale[0], 1023.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(207.0 * scale[0], 783.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -3.0 * scale[1], -7.0 * scale[0], -
              18.0 * scale[1], -6.0 * scale[0], -32.0 * scale[1])
    Curveto_r(1.0 * scale[0], -26.0 * scale[1], 1.0 * scale[0], -
              25.0 * scale[1], 10.0 * scale[0], 3.0 * scale[1])
    Curveto_r(9.0 * scale[0], 31.0 * scale[1], 7.0 * scale[0],
              41.0 * scale[1], -4.0 * scale[0], 29.0 * scale[1])
    te.end_fill()
    Moveto(211.0 * scale[0], 706.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -19.0 * scale[1], -10.0 *
              scale[0], -68.0 * scale[1], 9.0 * scale[0], -74.0 * scale[1])
    Curveto_r(13.0 * scale[0], -5.0 * scale[1], 13.0 *
              scale[0], -3.0 * scale[1], 1.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 13.0 * scale[1], -12.0 * scale[0],
              22.0 * scale[1], -2.0 * scale[0], 42.0 * scale[1])
    Curveto_r(6.0 * scale[0], 14.0 * scale[1], 16.0 * scale[0],
              22.0 * scale[1], 22.0 * scale[0], 19.0 * scale[1])
    Curveto_r(7.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              11.0 * scale[1], -1.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -8.0 * scale[1], -7.0 * scale[0], -
              15.0 * scale[1], -1.0 * scale[0], -19.0 * scale[1])
    Curveto_r(14.0 * scale[0], -9.0 * scale[1], 23.0 * scale[0],
              11.0 * scale[1], 16.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 23.0 * scale[1], -28.0 * scale[0],
              26.0 * scale[1], -44.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(434.0 * scale[0], 668.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-34.0 * scale[0], -40.0 * scale[1], -48.0 *
              scale[0], -59.0 * scale[1], -38.0 * scale[0], -57.0 * scale[1])
    Curveto_r(5.0 * scale[0], 1.0 * scale[1], 21.0 * scale[0], -
              3.0 * scale[1], 35.0 * scale[0], -10.0 * scale[1])
    Curveto_r(51.0 * scale[0], -25.0 * scale[1], 100.0 * scale[0],
              30.0 * scale[1], 63.0 * scale[0], 70.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 25.0 * scale[1], -36.0 * scale[0],
              24.0 * scale[1], -60.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto_r(54.0 * scale[0], -24.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -25.0 * scale[1], -22.0 * scale[0], -
              49.0 * scale[1], -43.0 * scale[0], -40.0 * scale[1])
    Curveto_r(-31.0 * scale[0], 12.0 * scale[1], -9.0 * scale[0],
              70.0 * scale[1], 25.0 * scale[0], 64.0 * scale[1])
    Curveto_r(8.0 * scale[0], -2.0 * scale[1], 16.0 * scale[0], -
              13.0 * scale[1], 18.0 * scale[0], -24.0 * scale[1])
    te.end_fill()
    Moveto(455.0 * scale[0], 640.0 * scale[1], x, y)
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
    Moveto(140.0 * scale[0], 485.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 18.0 * scale[0], -
              28.0 * scale[1], 39.0 * scale[0], -46.0 * scale[1])
    Curveto_r(23.0 * scale[0], -18.0 * scale[1], 43.0 * scale[0], -
              44.0 * scale[1], 46.0 * scale[0], -60.0 * scale[1])
    Lineto_r(6.0 * scale[0], -28.0 * scale[1])
    Lineto_r(34.0 * scale[0], 33.0 * scale[1])
    Curveto_r(20.0 * scale[0], 21.0 * scale[1], 51.0 * scale[0],
              38.0 * scale[1], 81.0 * scale[0], 45.0 * scale[1])
    Curveto_r(45.0 * scale[0], 12.0 * scale[1], 47.0 * scale[0],
              14.0 * scale[1], 30.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 10.0 * scale[1], -36.0 * scale[0],
              12.0 * scale[1], -81.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-54.0 * scale[0], -5.0 * scale[1], -69.0 *
              scale[0], -2.0 * scale[1], -98.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-40.0 * scale[0], 25.0 * scale[1], -57.0 * scale[0],
              27.0 * scale[1], -57.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(454.0 * scale[0], 309.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], -1.0 * scale[0], -
              16.0 * scale[1], 6.0 * scale[0], -22.0 * scale[1])
    Curveto_r(10.0 * scale[0], -9.0 * scale[1], 11.0 *
              scale[0], -9.0 * scale[1], 5.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 8.0 * scale[1], -2.0 * scale[0],
              17.0 * scale[1], 6.0 * scale[0], 22.0 * scale[1])
    Curveto_r(9.0 * scale[0], 6.0 * scale[1], 10.0 * scale[0],
              9.0 * scale[1], 2.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              5.0 * scale[1], -19.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(411.0 * scale[0], 276.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -10.0 * scale[1], -9.0 * scale[0], -
              16.0 * scale[1], -1.0 * scale[0], -21.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 10.0 *
              scale[0], -1.0 * scale[1], 10.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], 7.0 * scale[0],
              9.0 * scale[1], 16.0 * scale[0], 6.0 * scale[1])
    Curveto_r(14.0 * scale[0], -5.0 * scale[1], 15.0 *
              scale[0], -4.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 18.0 * scale[1], -15.0 * scale[0],
              18.0 * scale[1], -29.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(346.0 * scale[0], 215.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-22.0 * scale[0], -19.0 * scale[1], -48.0 *
              scale[0], -35.0 * scale[1], -58.0 * scale[0], -35.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 0.0 * scale[1], -18.0 * scale[0], -
              8.0 * scale[1], -18.0 * scale[0], -46.0 * scale[1])
    Curveto_r(0.0 * scale[0], -25.0 * scale[1], 5.0 * scale[0], -
              65.0 * scale[1], 11.0 * scale[0], -90.0 * scale[1])
    Lineto_r(11.0 * scale[0], -44.0 * scale[1])
    Lineto_r(77.0 * scale[0], 2.0 * scale[1])
    Curveto_r(64.0 * scale[0], 1.0 * scale[1], 69.0 * scale[0],
              2.0 * scale[1], 31.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-67.0 * scale[0], 9.0 * scale[1], -86.0 * scale[0],
              27.0 * scale[1], -95.0 * scale[0], 89.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 49.0 * scale[1], -6.0 * scale[0],
              52.0 * scale[1], 15.0 * scale[0], 52.0 * scale[1])
    Curveto_r(16.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0],
              4.0 * scale[1], 16.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], -2.0 * scale[0],
              15.0 * scale[1], 3.0 * scale[0], 15.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 61.0 * scale[0],
              45.0 * scale[1], 61.0 * scale[0], 58.0 * scale[1])
    Curveto_r(0.0 * scale[0], 19.0 * scale[1], -12.0 * scale[0],
              14.0 * scale[1], -54.0 * scale[0], -23.0 * scale[1])
    te.end_fill()
    Moveto(310.0 * scale[0], 125.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 8.0 * scale[0], -
              15.0 * scale[1], 18.0 * scale[0], -14.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              3.0 * scale[1], 4.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 2.0 * scale[1], -10.0 * scale[0],
              9.0 * scale[1], -6.0 * scale[0], 14.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], 0.0 * scale[0],
              9.0 * scale[1], -5.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              7.0 * scale[1], -11.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(78.0 * scale[0], 51.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -19.0 * scale[1], -16.0 *
              scale[0], -20.0 * scale[1], 10.0 * scale[0], -18.0 * scale[1])
    Curveto_r(15.0 * scale[0], 2.0 * scale[1], 27.0 * scale[0],
              8.0 * scale[1], 27.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 22.0 * scale[1], -19.0 * scale[0],
              23.0 * scale[1], -37.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto_r(32.0 * scale[0], -1.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -4.0 * scale[0], -
              10.0 * scale[1], -10.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0],
              5.0 * scale[1], -10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 5.0 * scale[0],
              10.0 * scale[1], 10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              4.0 * scale[1], 10.0 * scale[0], -10.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#f9e2d9')
    te.end_fill()
    Moveto(93.0 * scale[0], 1303.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(15.0 * scale[0], -2.0 * scale[1], 37.0 *
              scale[0], -2.0 * scale[1], 50.0 * scale[0], 0.0 * scale[1])
    Curveto_r(12.0 * scale[0], 2.0 * scale[1], 0.0 * scale[0],
              4.0 * scale[1], -28.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-27.0 * scale[0], 0.0 * scale[1], -38.0 *
              scale[0], -2.0 * scale[1], -22.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(823.0 * scale[0], 1303.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 25.0 *
              scale[0], -2.0 * scale[1], 35.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -27.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(448.0 * scale[0], 1277.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -9.0 * scale[1], -20.0 * scale[0], -
              29.0 * scale[1], -27.0 * scale[0], -45.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -25.0 * scale[1], -10.0 *
              scale[0], -35.0 * scale[1], 4.0 * scale[0], -61.0 * scale[1])
    Curveto_r(9.0 * scale[0], -17.0 * scale[1], 13.0 * scale[0], -
              37.0 * scale[1], 9.0 * scale[0], -44.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], 1.0 *
              scale[0], -5.0 * scale[1], 12.0 * scale[0], 4.0 * scale[1])
    Curveto_r(21.0 * scale[0], 18.0 * scale[1], 54.0 * scale[0],
              21.0 * scale[1], 54.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 6.0 * scale[0], -
              4.0 * scale[1], 14.0 * scale[0], 2.0 * scale[1])
    Curveto_r(18.0 * scale[0], 15.0 * scale[1], 15.0 * scale[0],
              98.0 * scale[1], -5.0 * scale[0], 129.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 24.0 * scale[1], -29.0 * scale[0],
              29.0 * scale[1], -29.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], -2.0 *
              scale[0], -10.0 * scale[1], -9.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 11.0 * scale[1], -11.0 * scale[0],
              11.0 * scale[1], -23.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(95.0 * scale[0], 1260.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -12.0 * scale[1], 12.0 *
              scale[0], -12.0 * scale[1], 40.0 * scale[0], 0.0 * scale[1])
    Curveto_r(18.0 * scale[0], 8.0 * scale[1], 17.0 * scale[0],
              9.0 * scale[1], -7.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 1.0 * scale[1], -30.0 *
              scale[0], -3.0 * scale[1], -33.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(845.0 * scale[0], 1260.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 3.0 * scale[0], -
              10.0 * scale[1], 14.0 * scale[0], -10.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 21.0 * scale[0],
              5.0 * scale[1], 21.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -6.0 * scale[0],
              10.0 * scale[1], -14.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -18.0 * scale[0], -
              4.0 * scale[1], -21.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(802.0 * scale[0], 1235.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(51.0 * scale[0], 1233.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -20.0 * scale[1], 4.0 * scale[0], -
              23.0 * scale[1], 32.0 * scale[0], -22.0 * scale[1])
    Curveto_r(29.0 * scale[0], 2.0 * scale[1], 29.0 * scale[0],
              2.0 * scale[1], 5.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 2.0 * scale[1], -29.0 * scale[0],
              12.0 * scale[1], -31.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 12.0 * scale[1], -5.0 * scale[0],
              10.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(835.0 * scale[0], 1190.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -7.0 * scale[1], -17.0 *
              scale[0], -9.0 * scale[1], -3.0 * scale[0], -9.0 * scale[1])
    Curveto_r(9.0 * scale[0], -1.0 * scale[1], 20.0 * scale[0],
              4.0 * scale[1], 23.0 * scale[0], 9.0 * scale[1])
    Curveto_r(7.0 * scale[0], 11.0 * scale[1], 7.0 * scale[0],
              11.0 * scale[1], -20.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(48.0 * scale[0], 1173.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(125.0 * scale[0], 1149.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -10.0 * scale[1], -25.0 *
              scale[0], -19.0 * scale[1], -19.0 * scale[0], -19.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 22.0 * scale[0],
              9.0 * scale[1], 35.0 * scale[0], 20.0 * scale[1])
    Curveto_r(30.0 * scale[0], 24.0 * scale[1], 23.0 * scale[0],
              24.0 * scale[1], -16.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(809.0 * scale[0], 1137.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -5.0 * scale[1], 19.0 * scale[0], -
              7.0 * scale[1], 32.0 * scale[0], -5.0 * scale[1])
    Curveto_r(20.0 * scale[0], 3.0 * scale[1], 19.0 * scale[0],
              5.0 * scale[1], -9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 3.0 * scale[1], -29.0 * scale[0],
              2.0 * scale[1], -23.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(828.0 * scale[0], 974.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(24.0 * scale[0], -17.0 * scale[1], 39.0 *
              scale[0], -14.0 * scale[1], 27.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -16.0 * scale[0],
              11.0 * scale[1], -28.0 * scale[0], 11.0 * scale[1])
    Lineto_r(-21.0 * scale[0], 0.0 * scale[1])
    Lineto_r(22.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(40.0 * scale[0], 951.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-23.0 * scale[0], -45.0 * scale[1], 0.0 * scale[0], -
              89.0 * scale[1], 40.0 * scale[0], -76.0 * scale[1])
    Curveto_r(26.0 * scale[0], 8.0 * scale[1], 27.0 * scale[0],
              48.0 * scale[1], 0.0 * scale[0], 75.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 25.0 * scale[1], -27.0 * scale[0],
              25.0 * scale[1], -40.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto_r(50.0 * scale[0], -55.0 * scale[1], 0, 0)
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
    Moveto(782.0 * scale[0], 938.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -32.0 * scale[1], 28.0 * scale[0], -
              35.0 * scale[1], 28.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], -5.0 * scale[0],
              26.0 * scale[1], -16.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0], -
              7.0 * scale[1], -12.0 * scale[0], -22.0 * scale[1])
    te.end_fill()
    Moveto(820.0 * scale[0], 941.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], 5.0 * scale[0], -
              21.0 * scale[1], 10.0 * scale[0], -21.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              6.0 * scale[1], 10.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -4.0 * scale[0],
              18.0 * scale[1], -10.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0], -
              3.0 * scale[1], -10.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(921.0 * scale[0], 936.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -8.0 * scale[1], -19.0 * scale[0], -
              12.0 * scale[1], -27.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 6.0 * scale[1], -19.0 * scale[0], -
              11.0 * scale[1], -1.0 * scale[0], -24.0 * scale[1])
    Curveto_r(20.0 * scale[0], -15.0 * scale[1], 51.0 *
              scale[0], -9.0 * scale[1], 55.0 * scale[0], 11.0 * scale[1])
    Curveto_r(5.0 * scale[0], 26.0 * scale[1], -12.0 * scale[0],
              40.0 * scale[1], -27.0 * scale[0], 22.0 * scale[1])
    te.end_fill()
    Moveto(870.0 * scale[0], 888.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], 7.0 * scale[0], -
              18.0 * scale[1], 23.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0],
              2.0 * scale[1], 7.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -18.0 * scale[0],
              11.0 * scale[1], -22.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 7.0 * scale[1], -8.0 * scale[0],
              4.0 * scale[1], -8.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(325.0 * scale[0], 410.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -9.0 * scale[0], -
              8.0 * scale[1], -13.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 2.0 * scale[1], -16.0 * scale[0], -
              3.0 * scale[1], -27.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -15.0 * scale[1], -19.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -8.0 * scale[1])
    Curveto_r(14.0 * scale[0], 4.0 * scale[1], 22.0 * scale[0],
              4.0 * scale[1], 18.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -8.0 * scale[1], 27.0 * scale[0], -
              45.0 * scale[1], 44.0 * scale[0], -45.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 22.0 * scale[0],
              10.0 * scale[1], 34.0 * scale[0], 21.0 * scale[1])
    Curveto_r(18.0 * scale[0], 17.0 * scale[1], 21.0 * scale[0],
              26.0 * scale[1], 13.0 * scale[0], 40.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 21.0 * scale[1], -63.0 * scale[0],
              27.0 * scale[1], -74.0 * scale[0], 9.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#e7b5aa')
    te.end_fill()
    Moveto(510.0 * scale[0], 1309.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 9.0 * scale[0], -
              9.0 * scale[1], 21.0 * scale[0], -9.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 18.0 * scale[0], -
              4.0 * scale[1], 15.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -5.0 * scale[1], 0.0 * scale[0], -
              12.0 * scale[1], 6.0 * scale[0], -14.0 * scale[1])
    Curveto_r(10.0 * scale[0], -4.0 * scale[1], 9.0 * scale[0], -
              8.0 * scale[1], -2.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -9.0 * scale[1], -12.0 *
              scale[0], -10.0 * scale[1], 5.0 * scale[0], -8.0 * scale[1])
    Curveto_r(16.0 * scale[0], 2.0 * scale[1], 21.0 * scale[0], -
              3.0 * scale[1], 23.0 * scale[0], -33.0 * scale[1])
    Curveto_r(3.0 * scale[0], -40.0 * scale[1], -31.0 * scale[0], -
              94.0 * scale[1], -55.0 * scale[0], -85.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -11.0 * scale[0],
              1.0 * scale[1], -8.0 * scale[0], -4.0 * scale[1])
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], -11.0 * scale[0], -
              10.0 * scale[1], -37.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-38.0 * scale[0], 0.0 * scale[1], -40.0 * scale[0], -
              1.0 * scale[1], -19.0 * scale[0], -10.0 * scale[1])
    Curveto_r(32.0 * scale[0], -13.0 * scale[1], 85.0 * scale[0],
              5.0 * scale[1], 111.0 * scale[0], 38.0 * scale[1])
    Curveto_r(25.0 * scale[0], 33.0 * scale[1], 26.0 * scale[0],
              88.0 * scale[1], 1.0 * scale[0], 129.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 29.0 * scale[1], -61.0 * scale[0],
              53.0 * scale[1], -61.0 * scale[0], 33.0 * scale[1])
    te.end_fill()
    Moveto(870.0 * scale[0], 1310.0 * scale[1], x, y)
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
    Moveto(905.0 * scale[0], 1301.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -18.0 * scale[1], 2.0 * scale[0], -
              21.0 * scale[1], -24.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -32.0 *
              scale[0], -4.0 * scale[1], -35.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -5.0 * scale[1], 3.0 * scale[0], -
              7.0 * scale[1], 14.0 * scale[0], -4.0 * scale[1])
    Curveto_r(14.0 * scale[0], 4.0 * scale[1], 20.0 * scale[0],
              0.0 * scale[1], 20.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 2.0 * scale[0], -
              16.0 * scale[1], 4.0 * scale[0], -16.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0], -
              3.0 * scale[1], 23.0 * scale[0], -6.0 * scale[1])
    Curveto_r(17.0 * scale[0], -5.0 * scale[1], 17.0 *
              scale[0], -5.0 * scale[1], 0.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 13.0 * scale[1], -16.0 * scale[0],
              15.0 * scale[1], -2.0 * scale[0], 21.0 * scale[1])
    Curveto_r(17.0 * scale[0], 6.0 * scale[1], 20.0 * scale[0],
              42.0 * scale[1], 4.0 * scale[0], 52.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 4.0 * scale[1], -9.0 * scale[0],
              0.0 * scale[1], -4.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(55.0 * scale[0], 1297.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -20.0 * scale[1], -2.0 *
              scale[0], -47.0 * scale[1], 7.0 * scale[0], -47.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              8.0 * scale[1], 7.0 * scale[0], 26.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], 5.0 * scale[0],
              10.0 * scale[1], 11.0 * scale[0], 14.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 7.0 * scale[0],
              9.0 * scale[1], -5.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 4.0 * scale[1], -17.0 * scale[0],
              1.0 * scale[1], -20.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(406.0 * scale[0], 1289.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -11.0 * scale[1], -15.0 *
              scale[0], -19.0 * scale[1], -9.0 * scale[0], -19.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 38.0 * scale[0],
              28.0 * scale[1], 32.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 2.0 * scale[1], -13.0 * scale[0], -
              5.0 * scale[1], -23.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(802.0 * scale[0], 1284.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -15.0 * scale[1], 8.0 * scale[0], -
              29.0 * scale[1], 14.0 * scale[0], -31.0 * scale[1])
    Curveto_r(7.0 * scale[0], -2.0 * scale[1], 10.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 35.0 * scale[1], -24.0 * scale[0],
              44.0 * scale[1], -20.0 * scale[0], 9.0 * scale[1])
    te.end_fill()
    Moveto(153.0 * scale[0], 1280.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -11.0 * scale[1], 2.0 * scale[0], -
              20.0 * scale[1], 5.0 * scale[0], -20.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0],
              9.0 * scale[1], 9.0 * scale[0], 20.0 * scale[1])
    Curveto_r(1.0 * scale[0], 11.0 * scale[1], -2.0 * scale[0],
              20.0 * scale[1], -5.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              9.0 * scale[1], -9.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(110.0 * scale[0], 1250.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -8.0 * scale[1], -9.0 * scale[0], -
              10.0 * scale[1], 12.0 * scale[0], -10.0 * scale[1])
    Curveto_r(19.0 * scale[0], 0.0 * scale[1], 29.0 * scale[0], -
              7.0 * scale[1], 37.0 * scale[0], -27.0 * scale[1])
    Curveto_r(10.0 * scale[0], -26.0 * scale[1], 10.0 *
              scale[0], -26.0 * scale[1], 8.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 30.0 * scale[1], -36.0 * scale[0],
              54.0 * scale[1], -57.0 * scale[0], 41.0 * scale[1])
    te.end_fill()
    Moveto(345.0 * scale[0], 1244.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -5.0 * scale[1], -7.0 *
              scale[0], -74.0 * scale[1], 4.0 * scale[0], -74.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              18.0 * scale[1], 6.0 * scale[0], 40.0 * scale[1])
    Curveto_r(0.0 * scale[0], 22.0 * scale[1], 0.0 * scale[0],
              40.0 * scale[1], 0.0 * scale[0], 39.0 * scale[1])
    Curveto_r(0.0 * scale[0], 0.0 * scale[1], -5.0 * scale[0], -
              3.0 * scale[1], -10.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(527.0 * scale[0], 1229.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -13.0 * scale[1], 8.0 * scale[0], -
              18.0 * scale[1], 11.0 * scale[0], -10.0 * scale[1])
    Curveto_r(2.0 * scale[0], 7.0 * scale[1], -1.0 * scale[0],
              18.0 * scale[1], -6.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 8.0 * scale[1], -9.0 * scale[0],
              4.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(615.0 * scale[0], 1240.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -4.0 * scale[0], -
              22.0 * scale[1], -3.0 * scale[0], -38.0 * scale[1])
    Curveto_r(2.0 * scale[0], -28.0 * scale[1], 4.0 * scale[0], -
              29.0 * scale[1], 29.0 * scale[0], -20.0 * scale[1])
    Curveto_r(48.0 * scale[0], 17.0 * scale[1], 53.0 * scale[0],
              33.0 * scale[1], 14.0 * scale[0], 51.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 9.0 * scale[1], -37.0 * scale[0],
              12.0 * scale[1], -40.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto_r(39.0 * scale[0], -37.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-26.0 * scale[0], -19.0 * scale[1], -34.0 *
              scale[0], -16.0 * scale[1], -34.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 23.0 * scale[1], 2.0 * scale[0],
              24.0 * scale[1], 26.0 * scale[0], 13.0 * scale[1])
    Curveto_r(24.0 * scale[0], -11.0 * scale[1], 25.0 *
              scale[0], -13.0 * scale[1], 8.0 * scale[0], -25.0 * scale[1])
    te.end_fill()
    Moveto(296.0 * scale[0], 1224.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-20.0 * scale[0], -14.0 * scale[1], -20.0 *
              scale[0], -14.0 * scale[1], 0.0 * scale[0], -29.0 * scale[1])
    Curveto_r(10.0 * scale[0], -8.0 * scale[1], 24.0 * scale[0], -
              14.0 * scale[1], 29.0 * scale[0], -14.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 1.0 * scale[0],
              6.0 * scale[1], -10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 12.0 * scale[1], -18.0 * scale[0],
              16.0 * scale[1], -5.0 * scale[0], 24.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 12.0 * scale[0],
              11.0 * scale[1], 10.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 2.0 * scale[1], -14.0 * scale[0], -
              2.0 * scale[1], -24.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(550.0 * scale[0], 1225.0 * scale[1], x, y)
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
    Moveto(374.0 * scale[0], 1213.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -10.0 * scale[1], 7.0 * scale[0], -
              28.0 * scale[1], 11.0 * scale[0], -40.0 * scale[1])
    Curveto_r(3.0 * scale[0], -13.0 * scale[1], 11.0 * scale[0], -
              23.0 * scale[1], 18.0 * scale[0], -23.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0],
              3.0 * scale[1], -1.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 7.0 * scale[1], -12.0 * scale[0],
              25.0 * scale[1], -12.0 * scale[0], 40.0 * scale[1])
    Curveto_r(0.0 * scale[0], 15.0 * scale[1], -5.0 * scale[0],
              28.0 * scale[1], -11.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              8.0 * scale[1], -5.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(816.0 * scale[0], 1221.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              11.0 * scale[1], 22.0 * scale[0], -14.0 * scale[1])
    Curveto_r(15.0 * scale[0], -3.0 * scale[1], 29.0 *
              scale[0], -1.0 * scale[1], 30.0 * scale[0], 4.0 * scale[1])
    Curveto_r(2.0 * scale[0], 5.0 * scale[1], 9.0 * scale[0],
              6.0 * scale[1], 14.0 * scale[0], 3.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 8.0 *
              scale[0], -3.0 * scale[1], 5.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 13.0 * scale[1], -64.0 * scale[0],
              17.0 * scale[1], -71.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(105.0 * scale[0], 1200.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], -6.0 * scale[0], -
              10.0 * scale[1], -21.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 0.0 * scale[1], -25.0 * scale[0], -
              3.0 * scale[1], -17.0 * scale[0], -11.0 * scale[1])
    Curveto_r(8.0 * scale[0], -8.0 * scale[1], 17.0 *
              scale[0], -8.0 * scale[1], 32.0 * scale[0], 0.0 * scale[1])
    Curveto_r(22.0 * scale[0], 12.0 * scale[1], 28.0 * scale[0],
              31.0 * scale[1], 10.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              4.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(526.0 * scale[0], 1177.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0], -
              15.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 0.0 * scale[0],
              11.0 * scale[1], -7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              8.0 * scale[1], -5.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(790.0 * scale[0], 1176.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              17.0 * scale[1], 9.0 * scale[0], -20.0 * scale[1])
    Curveto_r(5.0 * scale[0], -4.0 * scale[1], 7.0 * scale[0],
              3.0 * scale[1], 4.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 23.0 * scale[1], -13.0 * scale[0],
              26.0 * scale[1], -13.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(810.0 * scale[0], 1180.0 * scale[1], x, y)
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
    Moveto(892.0 * scale[0], 1170.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-17.0 * scale[0], -28.0 * scale[1], -15.0 *
              scale[0], -32.0 * scale[1], 8.0 * scale[0], -13.0 * scale[1])
    Curveto_r(20.0 * scale[0], 18.0 * scale[1], 26.0 * scale[0],
              33.0 * scale[1], 12.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              9.0 * scale[1], -20.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(58.0 * scale[0], 1138.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -6.0 * scale[1], 18.0 * scale[0], -
              8.0 * scale[1], 28.0 * scale[0], -6.0 * scale[1])
    Curveto_r(14.0 * scale[0], 3.0 * scale[1], 12.0 * scale[0],
              5.0 * scale[1], -9.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 3.0 * scale[1], -25.0 * scale[0],
              2.0 * scale[1], -19.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(421.0 * scale[0], 1141.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -6.0 * scale[1], -9.0 * scale[0], -
              11.0 * scale[1], -3.0 * scale[0], -15.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 14.0 *
              scale[0], -1.0 * scale[1], 17.0 * scale[0], 5.0 * scale[1])
    Curveto_r(9.0 * scale[0], 14.0 * scale[1], 2.0 * scale[0],
              20.0 * scale[1], -14.0 * scale[0], 10.0 * scale[1])
    te.end_fill()
    Moveto(855.0 * scale[0], 1140.0 * scale[1], x, y)
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
    Moveto(811.0 * scale[0], 953.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -24.0 * scale[1], 2.0 * scale[0], -
              25.0 * scale[1], 8.0 * scale[0], -8.0 * scale[1])
    Curveto_r(8.0 * scale[0], 19.0 * scale[1], 8.0 * scale[0],
              19.0 * scale[1], 19.0 * scale[0], 0.0 * scale[1])
    Curveto_r(14.0 * scale[0], -25.0 * scale[1], 16.0 *
              scale[0], -11.0 * scale[1], 2.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 28.0 * scale[1], -30.0 * scale[0],
              23.0 * scale[1], -29.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(915.0 * scale[0], 940.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -11.0 *
              scale[0], -7.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -8.0 * scale[0],
              2.0 * scale[1], -4.0 * scale[0], -5.0 * scale[1])
    Curveto_r(6.0 * scale[0], -9.0 * scale[1], 11.0 *
              scale[0], -9.0 * scale[1], 22.0 * scale[0], 0.0 * scale[1])
    Curveto_r(14.0 * scale[0], 11.0 * scale[1], 18.0 * scale[0],
              19.0 * scale[1], 10.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              5.0 * scale[1], -11.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(102.0 * scale[0], 910.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(877.0 * scale[0], 901.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -23.0 * scale[1], 28.0 * scale[0], -
              28.0 * scale[1], 39.0 * scale[0], -8.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], 3.0 * scale[0],
              9.0 * scale[1], -1.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -4.0 * scale[1], -16.0 * scale[0],
              0.0 * scale[1], -26.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 15.0 * scale[1], -17.0 * scale[0],
              14.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(70.0 * scale[0], 891.0 * scale[1], x, y)
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
    Moveto(864.0 * scale[0], 880.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -9.0 * scale[1], 12.0 * scale[0], -
              16.0 * scale[1], 26.0 * scale[0], -17.0 * scale[1])
    Curveto_r(21.0 * scale[0], -1.0 * scale[1], 21.0 *
              scale[0], -1.0 * scale[1], 3.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 3.0 * scale[1], -24.0 * scale[0],
              11.0 * scale[1], -26.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 7.0 * scale[1], -3.0 * scale[0],
              5.0 * scale[1], -3.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(450.0 * scale[0], 658.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -8.0 * scale[1], -12.0 *
              scale[0], -9.0 * scale[1], 2.0 * scale[0], -4.0 * scale[1])
    Curveto_r(10.0 * scale[0], 3.0 * scale[1], 22.0 * scale[0], -
              2.0 * scale[1], 27.0 * scale[0], -12.0 * scale[1])
    Curveto_r(6.0 * scale[0], -9.0 * scale[1], 11.0 * scale[0], -
              12.0 * scale[1], 11.0 * scale[0], -6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 20.0 * scale[1], -24.0 * scale[0],
              34.0 * scale[1], -40.0 * scale[0], 22.0 * scale[1])
    te.end_fill()
    Moveto(435.0 * scale[0], 631.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              12.0 * scale[1], 5.0 * scale[0], -16.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 10.0 * scale[0],
              1.0 * scale[1], 10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 18.0 * scale[1], -6.0 * scale[0],
              21.0 * scale[1], -15.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(176.0 * scale[0], 417.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(20.0 * scale[0], -35.0 * scale[1], 47.0 * scale[0], -
              68.0 * scale[1], 51.0 * scale[0], -63.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], -29.0 * scale[0],
              65.0 * scale[1], -44.0 * scale[0], 71.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 3.0 * scale[1], -11.0 * scale[0],
              0.0 * scale[1], -7.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(350.0 * scale[0], 426.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 11.0 * scale[0], -
              6.0 * scale[1], 25.0 * scale[0], -8.0 * scale[1])
    Curveto_r(14.0 * scale[0], -3.0 * scale[1], 25.0 *
              scale[0], -1.0 * scale[1], 25.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -11.0 * scale[0],
              9.0 * scale[1], -25.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -25.0 *
              scale[0], -2.0 * scale[1], -25.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(310.0 * scale[0], 409.0 * scale[1], x, y)
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
    Moveto(289.0 * scale[0], 403.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              11.0 * scale[1], 0.0 * scale[0], -15.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -6.0 * scale[0], -
              8.0 * scale[1], -14.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              9.0 * scale[1], -15.0 * scale[0], -20.0 * scale[1])
    Curveto_r(0.0 * scale[0], -17.0 * scale[1], 3.0 * scale[0], -
              19.0 * scale[1], 19.0 * scale[0], -11.0 * scale[1])
    Curveto_r(21.0 * scale[0], 12.0 * scale[1], 36.0 * scale[0],
              41.0 * scale[1], 20.0 * scale[0], 41.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0],
              5.0 * scale[1], -4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 4.0 * scale[0],
              10.0 * scale[1], 1.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              3.0 * scale[1], -7.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(403.0 * scale[0], 395.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -11.0 * scale[1], -32.0 * scale[0], -
              55.0 * scale[1], -51.0 * scale[0], -55.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -21.0 * scale[0],
              8.0 * scale[1], -28.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 22.0 * scale[1], -18.0 * scale[0],
              1.0 * scale[1], -1.0 * scale[0], -22.0 * scale[1])
    Curveto_r(12.0 * scale[0], -17.0 * scale[1], 17.0 *
              scale[0], -17.0 * scale[1], 42.0 * scale[0], -5.0 * scale[1])
    Curveto_r(37.0 * scale[0], 19.0 * scale[1], 61.0 * scale[0],
              54.0 * scale[1], 43.0 * scale[0], 65.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -10.0 * scale[0],
              3.0 * scale[1], -5.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(250.0 * scale[0], 279.0 * scale[1], x, y)
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
    Moveto(324.0 * scale[0], 225.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -12.0 * scale[1], -16.0 *
              scale[0], -14.0 * scale[1], -3.0 * scale[0], -15.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 22.0 * scale[0],
              7.0 * scale[1], 29.0 * scale[0], 15.0 * scale[1])
    Curveto_r(16.0 * scale[0], 19.0 * scale[1], 0.0 * scale[0],
              19.0 * scale[1], -26.0 * scale[0], 0.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#f7d76b')
    te.end_fill()
    Moveto(404.0 * scale[0], 979.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-51.0 * scale[0], -19.0 * scale[1], -93.0 *
              scale[0], -53.0 * scale[1], -81.0 * scale[0], -66.0 * scale[1])
    Curveto_r(4.0 * scale[0], -3.0 * scale[1], 40.0 * scale[0], -
              5.0 * scale[1], 81.0 * scale[0], -4.0 * scale[1])
    Curveto_r(82.0 * scale[0], 2.0 * scale[1], 187.0 * scale[0], -
              13.0 * scale[1], 217.0 * scale[0], -32.0 * scale[1])
    Curveto_r(14.0 * scale[0], -9.0 * scale[1], 21.0 *
              scale[0], -9.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(20.0 * scale[0], 20.0 * scale[1], -3.0 * scale[0],
              56.0 * scale[1], -57.0 * scale[0], 91.0 * scale[1])
    Curveto_r(-57.0 * scale[0], 38.0 * scale[1], -112.0 * scale[0],
              41.0 * scale[1], -190.0 * scale[0], 11.0 * scale[1])
    te.end_fill()
    Moveto(105.0 * scale[0], 831.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -4.0 * scale[1], -47.0 * scale[0], -
              16.0 * scale[1], -69.0 * scale[0], -26.0 * scale[1])
    Lineto_r(-39.0 * scale[0], -19.0 * scale[1])
    Lineto_r(7.0 * scale[0], -125.0 * scale[1])
    Curveto_r(4.0 * scale[0], -69.0 * scale[1], 9.0 * scale[0], -
              135.0 * scale[1], 12.0 * scale[0], -147.0 * scale[1])
    Curveto_r(5.0 * scale[0], -21.0 * scale[1], 34.0 * scale[0], -
              29.0 * scale[1], 34.0 * scale[0], -9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 13.0 * scale[0],
              26.0 * scale[1], 30.0 * scale[0], 45.0 * scale[1])
    Curveto_r(19.0 * scale[0], 23.0 * scale[1], 29.0 * scale[0],
              46.0 * scale[1], 30.0 * scale[0], 68.0 * scale[1])
    Curveto_r(0.0 * scale[0], 38.0 * scale[1], 13.0 * scale[0],
              66.0 * scale[1], 45.0 * scale[0], 102.0 * scale[1])
    Curveto_r(12.0 * scale[0], 14.0 * scale[1], 27.0 * scale[0],
              39.0 * scale[1], 33.0 * scale[0], 55.0 * scale[1])
    Curveto_r(5.0 * scale[0], 17.0 * scale[1], 13.0 * scale[0],
              38.0 * scale[1], 17.0 * scale[0], 48.0 * scale[1])
    Curveto_r(6.0 * scale[0], 14.0 * scale[1], 2.0 * scale[0],
              17.0 * scale[1], -31.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-22.0 * scale[0], -1.0 * scale[1], -52.0 *
              scale[0], -4.0 * scale[1], -69.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(759.0 * scale[0], 749.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-20.0 * scale[0], -29.0 * scale[1], -21.0 *
              scale[0], -31.0 * scale[1], -2.0 * scale[0], -21.0 * scale[1])
    Curveto_r(28.0 * scale[0], 16.0 * scale[1], 46.0 * scale[0],
              39.0 * scale[1], 34.0 * scale[0], 46.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 4.0 * scale[1], -19.0 * scale[0], -
              8.0 * scale[1], -32.0 * scale[0], -25.0 * scale[1])
    te.end_fill()
    Moveto(715.0 * scale[0], 710.0 * scale[1], x, y)
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
    Moveto(754.0 * scale[0], 589.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -20.0 * scale[1], 7.0 * scale[0], -
              77.0 * scale[1], 51.0 * scale[0], -155.0 * scale[1])
    Curveto_r(25.0 * scale[0], -44.0 * scale[1], 55.0 * scale[0], -
              105.0 * scale[1], 67.0 * scale[0], -137.0 * scale[1])
    Curveto_r(11.0 * scale[0], -32.0 * scale[1], 30.0 * scale[0], -
              63.0 * scale[1], 40.0 * scale[0], -68.0 * scale[1])
    Curveto_r(19.0 * scale[0], -10.0 * scale[1], 19.0 *
              scale[0], -10.0 * scale[1], 2.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 14.0 * scale[1], -14.0 * scale[0],
              29.0 * scale[1], -10.0 * scale[0], 33.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], 11.0 * scale[0],
              0.0 * scale[1], 16.0 * scale[0], -8.0 * scale[1])
    Curveto_r(8.0 * scale[0], -13.0 * scale[1], 10.0 *
              scale[0], -13.0 * scale[1], 10.0 * scale[0], 1.0 * scale[1])
    Curveto_r(0.0 * scale[0], 20.0 * scale[1], 27.0 * scale[0],
              33.0 * scale[1], 34.0 * scale[0], 16.0 * scale[1])
    Curveto_r(2.0 * scale[0], -7.0 * scale[1], 5.0 * scale[0],
              0.0 * scale[1], 5.0 * scale[0], 15.0 * scale[1])
    Curveto_r(1.0 * scale[0], 19.0 * scale[1], -3.0 * scale[0],
              26.0 * scale[1], -13.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -4.0 * scale[1], -15.0 * scale[0],
              9.0 * scale[1], -19.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 67.0 * scale[1], -51.0 * scale[0],
              156.0 * scale[1], -90.0 * scale[0], 185.0 * scale[1])
    Curveto_r(-43.0 * scale[0], 33.0 * scale[1], -84.0 * scale[0],
              48.0 * scale[1], -93.0 * scale[0], 35.0 * scale[1])
    te.end_fill()
    Moveto(400.0 * scale[0], 412.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 5.0 * scale[0], -
              13.0 * scale[1], 11.0 * scale[0], -19.0 * scale[1])
    Curveto_r(13.0 * scale[0], -13.0 * scale[1], -26.0 * scale[0], -
              58.0 * scale[1], -58.0 * scale[0], -68.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -5.0 * scale[1], -25.0 *
              scale[0], -1.0 * scale[1], -34.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 21.0 * scale[1], -14.0 * scale[0],
              23.0 * scale[1], -30.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-27.0 * scale[0], -17.0 * scale[1], -24.0 *
              scale[0], -26.0 * scale[1], 16.0 * scale[0], -43.0 * scale[1])
    Curveto_r(50.0 * scale[0], -20.0 * scale[1], 73.0 * scale[0], -
              18.0 * scale[1], 102.0 * scale[0], 14.0 * scale[1])
    Curveto_r(14.0 * scale[0], 15.0 * scale[1], 29.0 * scale[0],
              26.0 * scale[1], 34.0 * scale[0], 25.0 * scale[1])
    Curveto_r(12.0 * scale[0], -4.0 * scale[1], 11.0 * scale[0],
              24.0 * scale[1], -1.0 * scale[0], 48.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 19.0 * scale[1], -40.0 * scale[0],
              27.0 * scale[1], -40.0 * scale[0], 11.0 * scale[1])
    te.end_fill()
    Moveto(235.0 * scale[0], 264.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -15.0 * scale[1], 10.0 * scale[0], -
              34.0 * scale[1], 24.0 * scale[0], -45.0 * scale[1])
    Curveto_r(23.0 * scale[0], -19.0 * scale[1], 24.0 *
              scale[0], -19.0 * scale[1], 60.0 * scale[0], 3.0 * scale[1])
    Curveto_r(54.0 * scale[0], 32.0 * scale[1], 57.0 * scale[0],
              36.0 * scale[1], 25.0 * scale[0], 43.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 4.0 * scale[1], -39.0 * scale[0],
              10.0 * scale[1], -50.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 5.0 * scale[1], -26.0 * scale[0],
              4.0 * scale[1], -33.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -8.0 * scale[1], -11.0 *
              scale[0], -8.0 * scale[1], -11.0 * scale[0], 1.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -4.0 * scale[0],
              12.0 * scale[1], -8.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              12.0 * scale[1], -7.0 * scale[0], -26.0 * scale[1])
    te.end_fill()
    Moveto(157.0 * scale[0], 238.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-33.0 * scale[0], -24.0 * scale[1], -105.0 * scale[0], -
              160.0 * scale[1], -75.0 * scale[0], -142.0 * scale[1])
    Curveto_r(7.0 * scale[0], 5.0 * scale[1], 9.0 * scale[0],
              2.0 * scale[1], 5.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -11.0 * scale[1], -2.0 *
              scale[0], -14.0 * scale[1], 7.0 * scale[0], -11.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 17.0 * scale[0],
              0.0 * scale[1], 21.0 * scale[0], -5.0 * scale[1])
    Curveto_r(3.0 * scale[0], -6.0 * scale[1], 12.0 * scale[0], -
              8.0 * scale[1], 18.0 * scale[0], -4.0 * scale[1])
    Curveto_r(7.0 * scale[0], 4.0 * scale[1], 5.0 * scale[0], -
              4.0 * scale[1], -4.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -19.0 * scale[1], -25.0 *
              scale[0], -25.0 * scale[1], -52.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -39.0 *
              scale[0], -4.0 * scale[1], -44.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -5.0 * scale[1], -3.0 *
              scale[0], -6.0 * scale[1], 4.0 * scale[0], -2.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 14.0 * scale[0],
              3.0 * scale[1], 16.0 * scale[0], -2.0 * scale[1])
    Curveto_r(6.0 * scale[0], -9.0 * scale[1], 227.0 * scale[0], -
              16.0 * scale[1], 227.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 3.0 * scale[1], -4.0 * scale[0],
              15.0 * scale[1], -10.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 10.0 * scale[1], -10.0 * scale[0],
              46.0 * scale[1], -11.0 * scale[0], 79.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 47.0 * scale[1], -6.0 * scale[0],
              64.0 * scale[1], -22.0 * scale[0], 78.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 10.0 * scale[1], -27.0 * scale[0],
              30.0 * scale[1], -36.0 * scale[0], 44.0 * scale[1])
    Lineto_r(-17.0 * scale[0], 27.0 * scale[1])
    Lineto_r(-27.0 * scale[0], -20.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#d2a532')
    te.end_fill()
    Moveto(397.0 * scale[0], 1369.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(466.0 * scale[0], 1355.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(22.0 * scale[0], -17.0 * scale[1], 38.0 *
              scale[0], -20.0 * scale[1], 29.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -1.0 * scale[0],
              10.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0], -
              5.0 * scale[1], 11.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 6.0 * scale[0], -
              7.0 * scale[1], 17.0 * scale[0], 2.0 * scale[1])
    Curveto_r(9.0 * scale[0], 8.0 * scale[1], 14.0 * scale[0],
              9.0 * scale[1], 10.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -18.0 * scale[1], 19.0 *
              scale[0], -37.0 * scale[1], 44.0 * scale[0], -29.0 * scale[1])
    Curveto_r(14.0 * scale[0], 5.0 * scale[1], 19.0 * scale[0],
              4.0 * scale[1], 15.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -2.0 * scale[0], -
              11.0 * scale[1], 3.0 * scale[0], -11.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              4.0 * scale[1], 11.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -24.0 * scale[0],
              29.0 * scale[1], -42.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -2.0 * scale[1], -18.0 * scale[0],
              3.0 * scale[1], -18.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], -14.0 * scale[0],
              14.0 * scale[1], -52.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-48.0 * scale[0], 0.0 * scale[1], -50.0 * scale[0], -
              1.0 * scale[1], -32.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(360.0 * scale[0], 1343.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 12.0 * scale[0], -
              9.0 * scale[1], 27.0 * scale[0], -10.0 * scale[1])
    Curveto_r(19.0 * scale[0], -1.0 * scale[1], 22.0 * scale[0],
              1.0 * scale[1], 12.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 11.0 * scale[1], -39.0 * scale[0],
              12.0 * scale[1], -39.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(368.0 * scale[0], 1313.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(600.0 * scale[0], 1290.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -8.0 * scale[1], -12.0 *
              scale[0], -10.0 * scale[1], 3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0],
              5.0 * scale[1], 17.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], -1.0 * scale[0],
              12.0 * scale[1], -20.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(140.0 * scale[0], 846.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 13.0 *
              scale[0], -7.0 * scale[1], 20.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 6.0 * scale[1], 3.0 * scale[0],
              10.0 * scale[1], -10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0], -
              4.0 * scale[1], -10.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(770.0 * scale[0], 801.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -4.0 * scale[0], -
              10.0 * scale[1], -9.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -8.0 * scale[0], -
              2.0 * scale[1], -7.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], -4.0 * scale[0], -
              18.0 * scale[1], -11.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -42.0 * scale[0], -
              34.0 * scale[1], -43.0 * scale[0], -48.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 13.0 *
              scale[0], -1.0 * scale[1], 28.0 * scale[0], 8.0 * scale[1])
    Curveto_r(28.0 * scale[0], 17.0 * scale[1], 60.0 * scale[0],
              71.0 * scale[1], 48.0 * scale[0], 82.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0],
              1.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(412.0 * scale[0], 775.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-18.0 * scale[0], -8.0 * scale[1], -31.0 * scale[0], -
              19.0 * scale[1], -28.0 * scale[0], -24.0 * scale[1])
    Curveto_r(4.0 * scale[0], -5.0 * scale[1], 2.0 * scale[0], -
              12.0 * scale[1], -4.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -10.0 * scale[1], -12.0 *
              scale[0], -28.0 * scale[1], 5.0 * scale[0], -21.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 15.0 * scale[0],
              0.0 * scale[1], 15.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 20.0 * scale[0], -4.0 * scale[1])
    Curveto_r(24.0 * scale[0], 13.0 * scale[1], 100.0 * scale[0], -
              4.0 * scale[1], 101.0 * scale[0], -23.0 * scale[1])
    Curveto_r(2.0 * scale[0], -43.0 * scale[1], 10.0 * scale[0], -
              71.0 * scale[1], 21.0 * scale[0], -78.0 * scale[1])
    Curveto_r(9.0 * scale[0], -6.0 * scale[1], 9.0 * scale[0], -
              9.0 * scale[1], 1.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 8.0 * scale[1], -11.0 * scale[0],
              7.0 * scale[1], -21.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -6.0 * scale[1], -11.0 * scale[0], -
              15.0 * scale[1], -8.0 * scale[0], -20.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 0.0 * scale[0], -
              8.0 * scale[1], -7.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 2.0 * scale[1], -17.0 * scale[0], -
              17.0 * scale[1], -24.0 * scale[0], -44.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -36.0 * scale[1], -10.0 *
              scale[0], -48.0 * scale[1], -1.0 * scale[0], -49.0 * scale[1])
    Curveto_r(6.0 * scale[0], -1.0 * scale[1], 0.0 * scale[0], -
              4.0 * scale[1], -13.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -3.0 * scale[1], -28.0 * scale[0], -
              16.0 * scale[1], -32.0 * scale[0], -29.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -20.0 * scale[1], -5.0 * scale[0], -
              22.0 * scale[1], 25.0 * scale[0], -22.0 * scale[1])
    Curveto_r(33.0 * scale[0], 0.0 * scale[1], 53.0 * scale[0], -
              20.0 * scale[1], 41.0 * scale[0], -40.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], 5.0 * scale[0], -
              6.0 * scale[1], 17.0 * scale[0], -2.0 * scale[1])
    Curveto_r(16.0 * scale[0], 4.0 * scale[1], 19.0 * scale[0],
              2.0 * scale[1], 13.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              1.0 * scale[1], 17.0 * scale[0], 15.0 * scale[1])
    Curveto_r(17.0 * scale[0], 20.0 * scale[1], 27.0 * scale[0],
              25.0 * scale[1], 32.0 * scale[0], 18.0 * scale[1])
    Curveto_r(9.0 * scale[0], -15.0 * scale[1], 26.0 * scale[0], -
              16.0 * scale[1], 26.0 * scale[0], -1.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -6.0 * scale[0],
              7.0 * scale[1], -12.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -5.0 * scale[1], -10.0 *
              scale[0], -4.0 * scale[1], -2.0 * scale[0], 5.0 * scale[1])
    Curveto_r(9.0 * scale[0], 10.0 * scale[1], 17.0 * scale[0],
              10.0 * scale[1], 34.0 * scale[0], 1.0 * scale[1])
    Curveto_r(20.0 * scale[0], -11.0 * scale[1], 27.0 *
              scale[0], -7.0 * scale[1], 71.0 * scale[0], 39.0 * scale[1])
    Curveto_r(27.0 * scale[0], 28.0 * scale[1], 49.0 * scale[0],
              60.0 * scale[1], 49.0 * scale[0], 70.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], 5.0 * scale[0],
              23.0 * scale[1], 10.0 * scale[0], 26.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 10.0 * scale[0],
              11.0 * scale[1], 10.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              7.0 * scale[1], -11.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -4.0 * scale[1], -8.0 * scale[0],
              0.0 * scale[1], 0.0 * scale[0], 15.0 * scale[1])
    Curveto_r(7.0 * scale[0], 11.0 * scale[1], 16.0 * scale[0],
              21.0 * scale[1], 21.0 * scale[0], 21.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              5.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -4.0 * scale[0],
              7.0 * scale[1], -10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -10.0 * scale[0],
              2.0 * scale[1], -11.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 16.0 * scale[1], -1.0 * scale[0],
              16.0 * scale[1], -8.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -19.0 * scale[1], -8.0 *
              scale[0], -18.0 * scale[1], -21.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 14.0 * scale[1], -19.0 * scale[0],
              31.0 * scale[1], -27.0 * scale[0], 39.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 7.0 * scale[1], -12.0 * scale[0],
              20.0 * scale[1], -9.0 * scale[0], 27.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], 0.0 * scale[0],
              11.0 * scale[1], -9.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -4.0 * scale[1], -19.0 * scale[0],
              4.0 * scale[1], -26.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 14.0 * scale[1], -22.0 * scale[0],
              30.0 * scale[1], -36.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-31.0 * scale[0], 14.0 * scale[1], -33.0 * scale[0],
              14.0 * scale[1], -33.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -20.0 * scale[1], -6.0 * scale[0], -
              19.0 * scale[1], -38.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-39.0 * scale[0], 26.0 * scale[1], -91.0 * scale[0],
              33.0 * scale[1], -130.0 * scale[0], 16.0 * scale[1])
    te.end_fill()
    Moveto_r(158.0 * scale[0], -345.0 * scale[1], 0, 0)
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
    Moveto(947.0 * scale[0], 770.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -11.0 * scale[1], -1.0 *
              scale[0], -20.0 * scale[1], 4.0 * scale[0], -20.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              9.0 * scale[1], 9.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], -2.0 * scale[0],
              20.0 * scale[1], -4.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0], -
              9.0 * scale[1], -9.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(3.0 * scale[0], 560.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -47.0 * scale[1], 2.0 * scale[0], -
              66.0 * scale[1], 4.0 * scale[0], -42.0 * scale[1])
    Curveto_r(2.0 * scale[0], 23.0 * scale[1], 2.0 * scale[0],
              61.0 * scale[1], 0.0 * scale[0], 85.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 23.0 * scale[1], -4.0 * scale[0],
              4.0 * scale[1], -4.0 * scale[0], -43.0 * scale[1])
    te.end_fill()
    Moveto(297.0 * scale[0], 602.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-23.0 * scale[0], -26.0 * scale[1], -68.0 * scale[0], -
              120.0 * scale[1], -59.0 * scale[0], -125.0 * scale[1])
    Curveto_r(8.0 * scale[0], -5.0 * scale[1], 35.0 * scale[0], -
              2.0 * scale[1], 98.0 * scale[0], 10.0 * scale[1])
    Lineto_r(41.0 * scale[0], 8.0 * scale[1])
    Lineto_r(-15.0 * scale[0], 51.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 61.0 * scale[1], -42.0 * scale[0],
              81.0 * scale[1], -65.0 * scale[0], 56.0 * scale[1])
    te.end_fill()
    Moveto(90.0 * scale[0], 551.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              12.0 * scale[1], 16.0 * scale[0], -15.0 * scale[1])
    Curveto_r(14.0 * scale[0], -5.0 * scale[1], 15.0 *
              scale[0], -4.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 17.0 * scale[1], -20.0 * scale[0],
              19.0 * scale[1], -20.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(707.0 * scale[0], 448.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -13.0 * scale[1], -29.0 * scale[0], -
              38.0 * scale[1], -46.0 * scale[0], -56.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -23.0 * scale[1], -32.0 *
              scale[0], -45.0 * scale[1], -34.0 * scale[0], -70.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -20.0 * scale[1], -6.0 * scale[0], -
              40.0 * scale[1], -12.0 * scale[0], -44.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -7.0 * scale[1], -12.0 * scale[0], -
              83.0 * scale[1], -5.0 * scale[0], -195.0 * scale[1])
    Curveto_r(4.0 * scale[0], -71.0 * scale[1], 10.0 * scale[0], -
              74.0 * scale[1], 64.0 * scale[0], -42.0 * scale[1])
    Curveto_r(26.0 * scale[0], 15.0 * scale[1], 36.0 * scale[0],
              17.0 * scale[1], 36.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 11.0 * scale[0],
              7.0 * scale[1], 25.0 * scale[0], 33.0 * scale[1])
    Curveto_r(14.0 * scale[0], 26.0 * scale[1], 25.0 * scale[0],
              58.0 * scale[1], 25.0 * scale[0], 71.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], 7.0 * scale[0],
              30.0 * scale[1], 15.0 * scale[0], 37.0 * scale[1])
    Curveto_r(12.0 * scale[0], 10.0 * scale[1], 15.0 * scale[0],
              10.0 * scale[1], 15.0 * scale[0], -2.0 * scale[1])
    Curveto_r(0.0 * scale[0], -21.0 * scale[1], 67.0 * scale[0], -
              148.0 * scale[1], 74.0 * scale[0], -140.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 6.0 * scale[0], -
              2.0 * scale[1], 6.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 67.0 * scale[0], -
              35.0 * scale[1], 83.0 * scale[0], -19.0 * scale[1])
    Curveto_r(5.0 * scale[0], 5.0 * scale[1], 10.0 * scale[0],
              30.0 * scale[1], 11.0 * scale[0], 54.0 * scale[1])
    Curveto_r(1.0 * scale[0], 35.0 * scale[1], -5.0 * scale[0],
              51.0 * scale[1], -29.0 * scale[0], 79.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 19.0 * scale[1], -43.0 * scale[0],
              42.0 * scale[1], -60.0 * scale[0], 49.0 * scale[1])
    Curveto_r(-26.0 * scale[0], 12.0 * scale[1], -31.0 * scale[0],
              21.0 * scale[1], -36.0 * scale[0], 65.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 29.0 * scale[1], -23.0 * scale[0],
              86.0 * scale[1], -43.0 * scale[0], 128.0 * scale[1])
    Curveto_r(-40.0 * scale[0], 82.0 * scale[1], -61.0 * scale[0],
              95.0 * scale[1], -89.0 * scale[0], 54.0 * scale[1])
    te.end_fill()
    Moveto(806.0 * scale[0], 417.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0], -
              15.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 0.0 * scale[0],
              11.0 * scale[1], -7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              8.0 * scale[1], -5.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(22.0 * scale[0], 261.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -51.0 * scale[1], -4.0 * scale[0], -
              111.0 * scale[1], -7.0 * scale[0], -132.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -25.0 * scale[1], -3.0 *
              scale[0], -39.0 * scale[1], 4.0 * scale[0], -39.0 * scale[1])
    Curveto_r(16.0 * scale[0], 0.0 * scale[1], 51.0 * scale[0],
              32.0 * scale[1], 51.0 * scale[0], 46.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], 12.0 * scale[0],
              26.0 * scale[1], 26.0 * scale[0], 43.0 * scale[1])
    Curveto_r(26.0 * scale[0], 31.0 * scale[1], 27.0 * scale[0],
              42.0 * scale[1], 2.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -7.0 * scale[1], -24.0 * scale[0], -
              19.0 * scale[1], -36.0 * scale[0], -26.0 * scale[1])
    Curveto_r(-30.0 * scale[0], -17.0 * scale[1], -37.0 * scale[0],
              2.0 * scale[1], -24.0 * scale[0], 64.0 * scale[1])
    Curveto_r(7.0 * scale[0], 34.0 * scale[1], 7.0 * scale[0],
              56.0 * scale[1], -2.0 * scale[0], 83.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 34.0 * scale[1], -13.0 * scale[0],
              30.0 * scale[1], -14.0 * scale[0], -58.0 * scale[1])
    te.end_fill()
    Moveto(950.0 * scale[0], 330.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(944.0 * scale[0], 292.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -9.0 * scale[1], -12.0 *
              scale[0], -28.0 * scale[1], 4.0 * scale[0], -43.0 * scale[1])
    Curveto_r(6.0 * scale[0], -7.0 * scale[1], 12.0 * scale[0], -
              26.0 * scale[1], 12.0 * scale[0], -43.0 * scale[1])
    Lineto_r(0.0 * scale[0], -30.0 * scale[1])
    Lineto_r(-32.0 * scale[0], 30.0 * scale[1])
    Lineto_r(-33.0 * scale[0], 29.0 * scale[1])
    Lineto_r(34.0 * scale[0], -38.0 * scale[1])
    Curveto_r(19.0 * scale[0], -20.0 * scale[1], 36.0 * scale[0], -
              37.0 * scale[1], 36.0 * scale[0], -37.0 * scale[1])
    Curveto_r(1.0 * scale[0], 0.0 * scale[1], 3.0 * scale[0],
              26.0 * scale[1], 3.0 * scale[0], 58.0 * scale[1])
    Curveto_r(2.0 * scale[0], 59.0 * scale[1], -6.0 * scale[0],
              86.0 * scale[1], -24.0 * scale[0], 74.0 * scale[1])
    te.end_fill()
    Moveto(870.0 * scale[0], 266.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              17.0 * scale[1], 9.0 * scale[0], -20.0 * scale[1])
    Curveto_r(5.0 * scale[0], -4.0 * scale[1], 7.0 * scale[0],
              3.0 * scale[1], 4.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 23.0 * scale[1], -13.0 * scale[0],
              26.0 * scale[1], -13.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(210.0 * scale[0], 244.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 5.0 * scale[0], -
              12.0 * scale[1], 10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 8.0 * scale[0],
              11.0 * scale[1], 5.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 14.0 * scale[1], -15.0 * scale[0],
              11.0 * scale[1], -15.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(217.0 * scale[0], 209.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(8.0 * scale[0], 69.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -5.0 * scale[0], -
              25.0 * scale[1], -4.0 * scale[0], -39.0 * scale[1])
    Curveto_r(1.0 * scale[0], -20.0 * scale[1], 7.0 * scale[0], -
              26.0 * scale[1], 30.0 * scale[0], -28.0 * scale[1])
    Curveto_r(18.0 * scale[0], -2.0 * scale[1], 26.0 * scale[0],
              0.0 * scale[1], 21.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -10.0 * scale[0],
              9.0 * scale[1], -15.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -12.0 * scale[0],
              7.0 * scale[1], -16.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 15.0 * scale[1], -7.0 * scale[0],
              32.0 * scale[1], -8.0 * scale[0], 37.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              3.0 * scale[1], -8.0 * scale[0], -5.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#d99e56')
    te.end_fill()
    Moveto(427.0 * scale[0], 1360.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(13.0 * scale[0], -13.0 * scale[1], 56.0 * scale[0], -
              23.0 * scale[1], 49.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], -17.0 * scale[0],
              12.0 * scale[1], -32.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 2.0 * scale[1], -22.0 * scale[0],
              1.0 * scale[1], -17.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(400.0 * scale[0], 1320.0 * scale[1], x, y)
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
    Moveto(468.0 * scale[0], 1323.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(620.0 * scale[0], 1320.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(19.0 * scale[0], -13.0 * scale[1], 30.0 *
              scale[0], -13.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -10.0 * scale[0],
              10.0 * scale[1], -22.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -20.0 *
              scale[0], -2.0 * scale[1], -8.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(606.0 * scale[0], 1168.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 10.0 * scale[0], -
              6.0 * scale[1], 15.0 * scale[0], -3.0 * scale[1])
    Curveto_r(13.0 * scale[0], 9.0 * scale[1], 11.0 * scale[0],
              12.0 * scale[1], -6.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -9.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(370.0 * scale[0], 1116.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 7.0 * scale[0], -
              7.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 12.0 *
              scale[0], -2.0 * scale[1], 9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], -25.0 * scale[0],
              14.0 * scale[1], -25.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(16.0 * scale[0], 996.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -12.0 * scale[1], 10.0 * scale[0], -
              14.0 * scale[1], 20.0 * scale[0], -5.0 * scale[1])
    Curveto_r(12.0 * scale[0], 10.0 * scale[1], 61.0 * scale[0],
              3.0 * scale[1], 51.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -2.0 * scale[1], 6.0 * scale[0], -
              21.0 * scale[1], 19.0 * scale[0], -40.0 * scale[1])
    Curveto_r(29.0 * scale[0], -44.0 * scale[1], 29.0 *
              scale[0], -47.0 * scale[1], 3.0 * scale[0], -72.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -19.0 * scale[1], -21.0 *
              scale[0], -19.0 * scale[1], 28.0 * scale[0], -15.0 * scale[1])
    Curveto_r(35.0 * scale[0], 4.0 * scale[1], 44.0 * scale[0],
              2.0 * scale[1], 33.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -9.0 * scale[1], -9.0 * scale[0], -
              11.0 * scale[1], 13.0 * scale[0], -11.0 * scale[1])
    Curveto_r(30.0 * scale[0], 0.0 * scale[1], 31.0 * scale[0], -
              2.0 * scale[1], 16.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -15.0 * scale[1], -2.0 *
              scale[0], -12.0 * scale[1], 15.0 * scale[0], 8.0 * scale[1])
    Curveto_r(14.0 * scale[0], 17.0 * scale[1], 25.0 * scale[0],
              35.0 * scale[1], 26.0 * scale[0], 40.0 * scale[1])
    Curveto_r(0.0 * scale[0], 16.0 * scale[1], -56.0 * scale[0],
              108.0 * scale[1], -78.0 * scale[0], 129.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 12.0 * scale[1], -42.0 * scale[0],
              20.0 * scale[1], -87.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-58.0 * scale[0], 5.0 * scale[1], -65.0 * scale[0],
              4.0 * scale[1], -59.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(483.0 * scale[0], 1003.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 25.0 *
              scale[0], -2.0 * scale[1], 35.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -27.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(374.0 * scale[0], 974.0 * scale[1], x, y)
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
    Moveto(656.0 * scale[0], 883.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(757.0 * scale[0], 827.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -20.0 * scale[1], 1.0 * scale[0], -
              37.0 * scale[1], -6.0 * scale[0], -41.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -4.0 * scale[1], -11.0 * scale[0], -
              11.0 * scale[1], -11.0 * scale[0], -16.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 19.0 *
              scale[0], -8.0 * scale[1], 37.0 * scale[0], 3.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 14.0 * scale[0],
              3.0 * scale[1], 17.0 * scale[0], -2.0 * scale[1])
    Curveto_r(8.0 * scale[0], -12.0 * scale[1], -30.0 * scale[0], -
              44.0 * scale[1], -43.0 * scale[0], -36.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 12.0 * scale[1], -28.0 * scale[0], -
              36.0 * scale[1], -12.0 * scale[0], -81.0 * scale[1])
    Curveto_r(8.0 * scale[0], -23.0 * scale[1], 19.0 * scale[0], -
              40.0 * scale[1], 23.0 * scale[0], -38.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], 33.0 * scale[0], -
              8.0 * scale[1], 64.0 * scale[0], -23.0 * scale[1])
    Curveto_r(55.0 * scale[0], -27.0 * scale[1], 94.0 * scale[0], -
              63.0 * scale[1], 94.0 * scale[0], -89.0 * scale[1])
    Curveto_r(0.0 * scale[0], -20.0 * scale[1], 26.0 *
              scale[0], -6.0 * scale[1], 26.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], 4.0 * scale[0],
              65.0 * scale[1], 9.0 * scale[0], 125.0 * scale[1])
    Curveto_r(5.0 * scale[0], 75.0 * scale[1], 4.0 * scale[0],
              107.0 * scale[1], -4.0 * scale[0], 107.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0],
              8.0 * scale[1], -1.0 * scale[0], 26.0 * scale[1])
    Curveto_r(6.0 * scale[0], 14.0 * scale[1], 10.0 * scale[0],
              27.0 * scale[1], 10.0 * scale[0], 30.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], -63.0 * scale[0],
              3.0 * scale[1], -106.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-25.0 * scale[0], -8.0 * scale[1], -52.0 * scale[0], -
              13.0 * scale[1], -59.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 2.0 * scale[1], -18.0 * scale[0], -
              1.0 * scale[1], -25.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -10.0 * scale[1], -11.0 *
              scale[0], -8.0 * scale[1], -5.0 * scale[0], 8.0 * scale[1])
    Curveto_r(16.0 * scale[0], 42.0 * scale[1], 16.0 * scale[0],
              52.0 * scale[1], 1.0 * scale[0], 64.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 11.0 * scale[1], -14.0 * scale[0],
              8.0 * scale[1], -9.0 * scale[0], -22.0 * scale[1])
    te.end_fill()
    Moveto(108.0 * scale[0], 833.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(50.0 * scale[0], 820.0 * scale[1], x, y)
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
    Moveto(153.0 * scale[0], 718.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-30.0 * scale[0], -34.0 * scale[1], -43.0 * scale[0], -
              63.0 * scale[1], -43.0 * scale[0], -100.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -22.0 * scale[1], -11.0 * scale[0], -
              45.0 * scale[1], -30.0 * scale[0], -68.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -19.0 * scale[1], -30.0 *
              scale[0], -39.0 * scale[1], -30.0 * scale[0], -45.0 * scale[1])
    Curveto_r(0.0 * scale[0], -18.0 * scale[1], -30.0 *
              scale[0], -14.0 * scale[1], -31.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], -5.0 * scale[0],
              3.0 * scale[1], -10.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -31.0 * scale[1], -3.0 *
              scale[0], -49.0 * scale[1], 9.0 * scale[0], -29.0 * scale[1])
    Curveto_r(4.0 * scale[0], 7.0 * scale[1], 7.0 * scale[0], -
              16.0 * scale[1], 6.0 * scale[0], -50.0 * scale[1])
    Curveto_r(0.0 * scale[0], -34.0 * scale[1], 5.0 * scale[0], -
              78.0 * scale[1], 12.0 * scale[0], -98.0 * scale[1])
    Curveto_r(9.0 * scale[0], -27.0 * scale[1], 9.0 * scale[0], -
              49.0 * scale[1], 2.0 * scale[0], -83.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -95.0 * scale[1], 9.0 *
              scale[0], -96.0 * scale[1], 55.0 * scale[0], -2.0 * scale[1])
    Curveto_r(29.0 * scale[0], 59.0 * scale[1], 42.0 * scale[0],
              73.0 * scale[1], 52.0 * scale[0], 56.0 * scale[1])
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 11.0 * scale[0], -
              8.0 * scale[1], 16.0 * scale[0], -4.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 7.0 * scale[0],
              10.0 * scale[1], 4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], 0.0 * scale[0],
              6.0 * scale[1], 8.0 * scale[0], 3.0 * scale[1])
    Curveto_r(18.0 * scale[0], -6.0 * scale[1], 18.0 * scale[0],
              27.0 * scale[1], 1.0 * scale[0], 41.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 6.0 * scale[1], -23.0 * scale[0],
              48.0 * scale[1], -34.0 * scale[0], 95.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 47.0 * scale[1], -28.0 * scale[0],
              90.0 * scale[1], -36.0 * scale[0], 96.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 6.0 * scale[1], -14.0 * scale[0],
              15.0 * scale[1], -14.0 * scale[0], 19.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], 7.0 * scale[0],
              2.0 * scale[1], 15.0 * scale[0], -5.0 * scale[1])
    Curveto_r(13.0 * scale[0], -11.0 * scale[1], 15.0 *
              scale[0], -5.0 * scale[1], 15.0 * scale[0], 45.0 * scale[1])
    Curveto_r(0.0 * scale[0], 47.0 * scale[1], 5.0 * scale[0],
              65.0 * scale[1], 30.0 * scale[0], 101.0 * scale[1])
    Curveto_r(33.0 * scale[0], 49.0 * scale[1], 34.0 * scale[0],
              55.0 * scale[1], 3.0 * scale[0], 22.0 * scale[1])
    te.end_fill()
    Moveto(497.0 * scale[0], 680.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(10.0 * scale[0], -11.0 * scale[1], 19.0 * scale[0], -
              20.0 * scale[1], 21.0 * scale[0], -20.0 * scale[1])
    Curveto_r(1.0 * scale[0], 0.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -8.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 11.0 * scale[1], -15.0 * scale[0],
              20.0 * scale[1], -20.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -2.0 * scale[0], -
              9.0 * scale[1], 7.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(510.0 * scale[0], 632.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], -6.0 * scale[0], -
              24.0 * scale[1], -12.0 * scale[0], -32.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -12.0 * scale[1], -10.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], -2.0 * scale[1])
    Curveto_r(9.0 * scale[0], 6.0 * scale[1], 18.0 * scale[0],
              9.0 * scale[1], 21.0 * scale[0], 7.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 3.0 * scale[0],
              6.0 * scale[1], 1.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 29.0 * scale[1], -13.0 * scale[0],
              33.0 * scale[1], -13.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(745.0 * scale[0], 589.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0], -
              12.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 17.0 * scale[1], 1.0 * scale[0],
              20.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(827.0 * scale[0], 569.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(285.0 * scale[0], 474.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-38.0 * scale[0], -14.0 * scale[1], -39.0 *
              scale[0], -14.0 * scale[1], -6.0 * scale[0], -9.0 * scale[1])
    Curveto_r(18.0 * scale[0], 3.0 * scale[1], 49.0 * scale[0],
              5.0 * scale[1], 68.0 * scale[0], 5.0 * scale[1])
    Curveto_r(20.0 * scale[0], 0.0 * scale[1], 32.0 * scale[0],
              4.0 * scale[1], 28.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 13.0 * scale[1], -41.0 * scale[0],
              11.0 * scale[1], -90.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(154.0 * scale[0], 434.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -10.0 * scale[1], 13.0 * scale[0], -
              32.0 * scale[1], 18.0 * scale[0], -49.0 * scale[1])
    Curveto_r(13.0 * scale[0], -37.0 * scale[1], 38.0 * scale[0], -
              66.0 * scale[1], 49.0 * scale[0], -59.0 * scale[1])
    Curveto_r(14.0 * scale[0], 8.0 * scale[1], 11.0 * scale[0],
              17.0 * scale[1], -21.0 * scale[0], 53.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 18.0 * scale[1], -30.0 * scale[0],
              40.0 * scale[1], -30.0 * scale[0], 47.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -5.0 * scale[0],
              16.0 * scale[1], -12.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -9.0 * scale[0],
              2.0 * scale[1], -4.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(440.0 * scale[0], 401.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -24.0 * scale[1], 13.0 *
              scale[0], -52.0 * scale[1], 1.0 * scale[0], -48.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 1.0 * scale[1], -20.0 * scale[0], -
              10.0 * scale[1], -34.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -16.0 * scale[1], -35.0 *
              scale[0], -28.0 * scale[1], -47.0 * scale[0], -28.0 * scale[1])
    Curveto_r(-36.0 * scale[0], 0.0 * scale[1], -90.0 * scale[0],
              28.0 * scale[1], -100.0 * scale[0], 52.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 16.0 * scale[1], -9.0 * scale[0],
              18.0 * scale[1], -9.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -35.0 * scale[1], 74.0 * scale[0], -
              75.0 * scale[1], 125.0 * scale[0], -65.0 * scale[1])
    Curveto_r(33.0 * scale[0], 6.0 * scale[1], 30.0 * scale[0], -
              9.0 * scale[1], -3.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -6.0 * scale[1], -22.0 * scale[0], -
              11.0 * scale[1], -15.0 * scale[0], -11.0 * scale[1])
    Curveto_r(7.0 * scale[0], -1.0 * scale[1], 10.0 * scale[0], -
              7.0 * scale[1], 7.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], 7.0 * scale[0],
              2.0 * scale[1], 24.0 * scale[0], 20.0 * scale[1])
    Curveto_r(17.0 * scale[0], 17.0 * scale[1], 33.0 * scale[0],
              32.0 * scale[1], 36.0 * scale[0], 32.0 * scale[1])
    Curveto_r(3.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              8.0 * scale[1], 23.0 * scale[0], 18.0 * scale[1])
    Curveto_r(9.0 * scale[0], 9.0 * scale[1], 31.0 * scale[0],
              27.0 * scale[1], 47.0 * scale[0], 40.0 * scale[1])
    Curveto_r(26.0 * scale[0], 21.0 * scale[1], 27.0 * scale[0],
              23.0 * scale[1], 7.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -3.0 * scale[1], -20.0 *
              scale[0], -1.0 * scale[1], -17.0 * scale[0], 3.0 * scale[1])
    Curveto_r(10.0 * scale[0], 17.0 * scale[1], -8.0 * scale[0],
              40.0 * scale[1], -31.0 * scale[0], 40.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 0.0 * scale[1], -23.0 * scale[0], -
              3.0 * scale[1], -14.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(931.0 * scale[0], 404.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(248.0 * scale[0], 293.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(190.0 * scale[0], 274.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-14.0 * scale[0], -7.0 * scale[1], -37.0 * scale[0], -
              25.0 * scale[1], -50.0 * scale[0], -40.0 * scale[1])
    Lineto_r(-25.0 * scale[0], -27.0 * scale[1])
    Lineto_r(36.0 * scale[0], 26.0 * scale[1])
    Lineto_r(36.0 * scale[0], 27.0 * scale[1])
    Lineto_r(11.0 * scale[0], -22.0 * scale[1])
    Lineto_r(11.0 * scale[0], -23.0 * scale[1])
    Lineto_r(0.0 * scale[0], 23.0 * scale[1])
    Curveto_r(1.0 * scale[0], 12.0 * scale[1], 7.0 * scale[0],
              21.0 * scale[1], 14.0 * scale[0], 20.0 * scale[1])
    Curveto_r(14.0 * scale[0], -3.0 * scale[1], 17.0 * scale[0],
              24.0 * scale[1], 2.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 1.0 * scale[1], -21.0 * scale[0], -
              4.0 * scale[1], -35.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(900.0 * scale[0], 272.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 8.0 * scale[0], -
              18.0 * scale[1], 17.0 * scale[0], -31.0 * scale[1])
    Curveto_r(12.0 * scale[0], -18.0 * scale[1], 13.0 *
              scale[0], -22.0 * scale[1], 2.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 8.0 * scale[1], -12.0 * scale[0],
              6.0 * scale[1], 0.0 * scale[0], -8.0 * scale[1])
    Curveto_r(7.0 * scale[0], -9.0 * scale[1], 18.0 * scale[0], -
              14.0 * scale[1], 24.0 * scale[0], -10.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -1.0 * scale[0], -
              16.0 * scale[1], 6.0 * scale[0], -22.0 * scale[1])
    Curveto_r(25.0 * scale[0], -20.0 * scale[1], 7.0 * scale[0],
              52.0 * scale[1], -19.0 * scale[0], 77.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 23.0 * scale[1], -34.0 * scale[0],
              27.0 * scale[1], -34.0 * scale[0], 14.0 * scale[1])
    te.end_fill()
    Moveto(230.0 * scale[0], 234.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 8.0 * scale[0], -
              16.0 * scale[1], 17.0 * scale[0], -26.0 * scale[1])
    Curveto_r(16.0 * scale[0], -18.0 * scale[1], 16.0 * scale[0], -
              18.0 * scale[1], -3.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 7.0 * scale[1], -17.0 * scale[0],
              6.0 * scale[1], -6.0 * scale[0], -8.0 * scale[1])
    Curveto_r(12.0 * scale[0], -15.0 * scale[1], 16.0 *
              scale[0], -15.0 * scale[1], 45.0 * scale[0], 0.0 * scale[1])
    Curveto_r(40.0 * scale[0], 19.0 * scale[1], 49.0 * scale[0],
              26.0 * scale[1], 21.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -4.0 * scale[1], -30.0 * scale[0],
              1.0 * scale[1], -47.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 11.0 * scale[1], -27.0 * scale[0],
              17.0 * scale[1], -27.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(91.0 * scale[0], 174.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -15.0 * scale[1], -21.0 *
              scale[0], -33.0 * scale[1], -21.0 * scale[0], -41.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -7.0 * scale[0], -
              16.0 * scale[1], -15.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -4.0 * scale[1], -15.0 * scale[0], -
              13.0 * scale[1], -15.0 * scale[0], -21.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -4.0 * scale[0], -
              11.0 * scale[1], -10.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -10.0 * scale[0], -
              6.0 * scale[1], -10.0 * scale[0], -24.0 * scale[1])
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 5.0 * scale[0], -
              33.0 * scale[1], 10.0 * scale[0], -36.0 * scale[1])
    Curveto_r(7.0 * scale[0], -4.0 * scale[1], 8.0 * scale[0],
              3.0 * scale[1], 4.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 19.0 * scale[1], -4.0 * scale[0],
              25.0 * scale[1], 5.0 * scale[0], 20.0 * scale[1])
    Curveto_r(9.0 * scale[0], -6.0 * scale[1], 15.0 * scale[0],
              4.0 * scale[1], 13.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 3.0 * scale[1], 6.0 * scale[0],
              6.0 * scale[1], 14.0 * scale[0], 6.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 18.0 * scale[0], -
              11.0 * scale[1], 15.0 * scale[0], -30.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -5.0 * scale[1], 3.0 *
              scale[0], -6.0 * scale[1], 9.0 * scale[0], -2.0 * scale[1])
    Curveto_r(7.0 * scale[0], 4.0 * scale[1], 7.0 * scale[0],
              13.0 * scale[1], -1.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 19.0 * scale[1], -1.0 * scale[0],
              51.0 * scale[1], 28.0 * scale[0], 102.0 * scale[1])
    Curveto_r(10.0 * scale[0], 17.0 * scale[1], -7.0 * scale[0],
              5.0 * scale[1], -26.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(262.0 * scale[0], 70.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 2.0 * scale[0], -
              27.0 * scale[1], 5.0 * scale[0], -17.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              25.0 * scale[1], 0.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(104.0 * scale[0], 59.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], -2.0 * scale[0], -
              15.0 * scale[1], 3.0 * scale[0], -20.0 * scale[1])
    Curveto_r(5.0 * scale[0], -5.0 * scale[1], 9.0 * scale[0], -
              1.0 * scale[1], 9.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 23.0 * scale[1], -2.0 * scale[0],
              24.0 * scale[1], -12.0 * scale[0], 9.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#733e13')
    te.end_fill()
    Moveto(310.0 * scale[0], 1390.0 * scale[1], x, y)
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
    Moveto(536.0 * scale[0], 1391.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 3.0 * scale[0], -
              11.0 * scale[1], 15.0 * scale[0], -14.0 * scale[1])
    Curveto_r(16.0 * scale[0], -4.0 * scale[1], 18.0 *
              scale[0], -3.0 * scale[1], 8.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -16.0 * scale[0],
              17.0 * scale[1], -23.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(690.0 * scale[0], 1389.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(14.0 * scale[0], -6.0 * scale[1], 71.0 * scale[0], -
              12.0 * scale[1], 127.0 * scale[0], -14.0 * scale[1])
    Curveto_r(81.0 * scale[0], -2.0 * scale[1], 105.0 * scale[0], -
              6.0 * scale[1], 119.0 * scale[0], -20.0 * scale[1])
    Curveto_r(17.0 * scale[0], -16.0 * scale[1], 14.0 * scale[0], -
              17.0 * scale[1], -47.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-39.0 * scale[0], 3.0 * scale[1], -56.0 * scale[0],
              2.0 * scale[1], -44.0 * scale[0], -3.0 * scale[1])
    Curveto_r(19.0 * scale[0], -8.0 * scale[1], 19.0 * scale[0], -
              9.0 * scale[1], -5.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -3.0 * scale[1], -1.0 *
              scale[0], -4.0 * scale[1], 28.0 * scale[0], -3.0 * scale[1])
    Lineto_r(53.0 * scale[0], 2.0 * scale[1])
    Lineto_r(-2.0 * scale[0], -40.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -23.0 * scale[1], 2.0 * scale[0], -
              50.0 * scale[1], 8.0 * scale[0], -61.0 * scale[1])
    Curveto_r(8.0 * scale[0], -13.0 * scale[1], 8.0 * scale[0], -
              26.0 * scale[1], 2.0 * scale[0], -37.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -13.0 * scale[1], -6.0 *
              scale[0], -20.0 * scale[1], 4.0 * scale[0], -24.0 * scale[1])
    Curveto_r(7.0 * scale[0], -2.0 * scale[1], 14.0 * scale[0], -
              12.0 * scale[1], 14.0 * scale[0], -20.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -5.0 * scale[0], -
              13.0 * scale[1], -11.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0],
              10.0 * scale[1], -9.0 * scale[0], 16.0 * scale[1])
    Curveto_r(4.0 * scale[0], 16.0 * scale[1], -6.0 * scale[0],
              14.0 * scale[1], -25.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -12.0 * scale[1], -13.0 *
              scale[0], -15.0 * scale[1], -2.0 * scale[0], -11.0 * scale[1])
    Curveto_r(8.0 * scale[0], 2.0 * scale[1], 23.0 * scale[0], -
              3.0 * scale[1], 34.0 * scale[0], -13.0 * scale[1])
    Curveto_r(16.0 * scale[0], -15.0 * scale[1], 17.0 *
              scale[0], -20.0 * scale[1], 5.0 * scale[0], -32.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -8.0 * scale[1], -21.0 * scale[0], -
              16.0 * scale[1], -29.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -4.0 * scale[1], -12.0 *
              scale[0], -6.0 * scale[1], 2.0 * scale[0], -6.0 * scale[1])
    Curveto_r(9.0 * scale[0], -1.0 * scale[1], 20.0 * scale[0], -
              6.0 * scale[1], 24.0 * scale[0], -13.0 * scale[1])
    Curveto_r(5.0 * scale[0], -8.0 * scale[1], -8.0 * scale[0], -
              9.0 * scale[1], -52.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-40.0 * scale[0], 4.0 * scale[1], -54.0 * scale[0],
              3.0 * scale[1], -44.0 * scale[0], -4.0 * scale[1])
    Curveto_r(13.0 * scale[0], -8.0 * scale[1], 13.0 * scale[0], -
              10.0 * scale[1], 1.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -12.0 *
              scale[0], -3.0 * scale[1], -3.0 * scale[0], -12.0 * scale[1])
    Curveto_r(10.0 * scale[0], -10.0 * scale[1], 17.0 *
              scale[0], -10.0 * scale[1], 32.0 * scale[0], 0.0 * scale[1])
    Curveto_r(23.0 * scale[0], 14.0 * scale[1], 44.0 * scale[0],
              16.0 * scale[1], 36.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -5.0 * scale[1], 3.0 * scale[0], -
              7.0 * scale[1], 13.0 * scale[0], -4.0 * scale[1])
    Curveto_r(34.0 * scale[0], 9.0 * scale[1], 42.0 * scale[0],
              50.0 * scale[1], 39.0 * scale[0], 203.0 * scale[1])
    Lineto_r(-3.0 * scale[0], 145.0 * scale[1])
    Lineto_r(-40.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-52.0 * scale[0], 17.0 * scale[1], -262.0 * scale[0],
              28.0 * scale[1], -225.0 * scale[0], 11.0 * scale[1])
    te.end_fill()
    Moveto_r(260.0 * scale[0], -69.0 * scale[1], 0, 0)
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
    Moveto_r(-5.0 * scale[0], -69.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              12.0 * scale[1], -5.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -10.0 * scale[0],
              1.0 * scale[1], -10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 18.0 * scale[1], 6.0 * scale[0],
              21.0 * scale[1], 15.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(78.0 * scale[0], 1383.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-35.0 * scale[0], -3.0 * scale[1], -52.0 * scale[0], -
              10.0 * scale[1], -63.0 * scale[0], -26.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -25.0 * scale[1], -20.0 *
              scale[0], -47.0 * scale[1], -5.0 * scale[0], -47.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              10.0 * scale[1], 10.0 * scale[0], 21.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], 5.0 * scale[0],
              20.0 * scale[1], 25.0 * scale[0], 17.0 * scale[1])
    Curveto_r(14.0 * scale[0], -3.0 * scale[1], 25.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], 42.0 * scale[0],
              23.0 * scale[1], 130.0 * scale[0], 30.0 * scale[1])
    Lineto_r(85.0 * scale[0], 7.0 * scale[1])
    Lineto_r(-80.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-44.0 * scale[0], 0.0 * scale[1], -101.0 *
              scale[0], -1.0 * scale[1], -127.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(340.0 * scale[0], 1381.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 30.0 * scale[0], -
              24.0 * scale[1], 36.0 * scale[0], -18.0 * scale[1])
    Curveto_r(2.0 * scale[0], 1.0 * scale[1], -6.0 * scale[0],
              8.0 * scale[1], -16.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 7.0 * scale[1], -20.0 * scale[0],
              8.0 * scale[1], -20.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(41.0 * scale[0], 1318.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -4.0 * scale[1], -22.0 * scale[0], -
              11.0 * scale[1], -25.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -18.0 * scale[1], -9.0 * scale[0], -
              100.0 * scale[1], 3.0 * scale[0], -115.0 * scale[1])
    Curveto_r(10.0 * scale[0], -11.0 * scale[1], 9.0 * scale[0], -
              15.0 * scale[1], -4.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -4.0 * scale[1], -11.0 *
              scale[0], -5.0 * scale[1], 2.0 * scale[0], -3.0 * scale[1])
    Curveto_r(10.0 * scale[0], 1.0 * scale[1], 19.0 * scale[0],
              7.0 * scale[1], 19.0 * scale[0], 14.0 * scale[1])
    Curveto_r(1.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              13.0 * scale[1], 3.0 * scale[0], 15.0 * scale[1])
    Curveto_r(8.0 * scale[0], 9.0 * scale[1], 7.0 * scale[0],
              75.0 * scale[1], 0.0 * scale[0], 94.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 22.0 * scale[1], -6.0 * scale[0],
              23.0 * scale[1], 31.0 * scale[0], 23.0 * scale[1])
    Curveto_r(21.0 * scale[0], 0.0 * scale[1], 41.0 * scale[0],
              4.0 * scale[1], 44.0 * scale[0], 9.0 * scale[1])
    Curveto_r(6.0 * scale[0], 9.0 * scale[1], -46.0 * scale[0],
              9.0 * scale[1], -73.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(172.0 * scale[0], 1293.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -10.0 * scale[1], -1.0 * scale[0], -
              24.0 * scale[1], -6.0 * scale[0], -31.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -8.0 * scale[1], -3.0 * scale[0], -
              18.0 * scale[1], 4.0 * scale[0], -25.0 * scale[1])
    Curveto_r(9.0 * scale[0], -9.0 * scale[1], 11.0 *
              scale[0], -9.0 * scale[1], 7.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 7.0 * scale[1], 0.0 * scale[0],
              17.0 * scale[1], 9.0 * scale[0], 24.0 * scale[1])
    Curveto_r(12.0 * scale[0], 11.0 * scale[1], 12.0 * scale[0],
              15.0 * scale[1], 2.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 6.0 * scale[1], -10.0 * scale[0],
              10.0 * scale[1], 2.0 * scale[0], 18.0 * scale[1])
    Curveto_r(13.0 * scale[0], 8.0 * scale[1], 12.0 * scale[0],
              10.0 * scale[1], -3.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0], -
              6.0 * scale[1], -15.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(792.0 * scale[0], 1275.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(331.0 * scale[0], 1261.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -5.0 * scale[1], -21.0 *
              scale[0], -7.0 * scale[1], -30.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 4.0 * scale[1], -14.0 * scale[0],
              3.0 * scale[1], -2.0 * scale[0], -5.0 * scale[1])
    Curveto_r(13.0 * scale[0], -9.0 * scale[1], 41.0 *
              scale[0], -3.0 * scale[1], 60.0 * scale[0], 14.0 * scale[1])
    Curveto_r(9.0 * scale[0], 8.0 * scale[1], -15.0 * scale[0],
              3.0 * scale[1], -28.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(360.0 * scale[0], 1239.0 * scale[1], x, y)
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
    Moveto(780.0 * scale[0], 1221.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 18.0 * scale[1], -14.0 * scale[0],
              21.0 * scale[1], -14.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(183.0 * scale[0], 1203.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 11.0 * scale[0], -
              10.0 * scale[1], 31.0 * scale[0], -6.0 * scale[1])
    Curveto_r(47.0 * scale[0], 9.0 * scale[1], 51.0 * scale[0],
              19.0 * scale[1], 8.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 0.0 * scale[1], -39.0 * scale[0], -
              5.0 * scale[1], -39.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(782.0 * scale[0], 1165.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(176.0 * scale[0], 1167.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0], -
              15.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 0.0 * scale[0],
              11.0 * scale[1], -7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              8.0 * scale[1], -5.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(12.0 * scale[0], 1125.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              28.0 * scale[1], -3.0 * scale[0], -31.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -7.0 * scale[1], 0.0 * scale[0], -
              35.0 * scale[1], 24.0 * scale[0], -58.0 * scale[1])
    Curveto_r(16.0 * scale[0], -16.0 * scale[1], 26.0 * scale[0], -
              17.0 * scale[1], 70.0 * scale[0], -10.0 * scale[1])
    Lineto_r(52.0 * scale[0], 9.0 * scale[1])
    Lineto_r(-52.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-69.0 * scale[0], 26.0 * scale[1], -58.0 * scale[0],
              38.0 * scale[1], 18.0 * scale[0], 20.0 * scale[1])
    Curveto_r(75.0 * scale[0], -18.0 * scale[1], 91.0 *
              scale[0], -11.0 * scale[1], 18.0 * scale[0], 7.0 * scale[1])
    Lineto_r(-52.0 * scale[0], 13.0 * scale[1])
    Lineto_r(29.0 * scale[0], 12.0 * scale[1])
    Curveto_r(15.0 * scale[0], 7.0 * scale[1], 35.0 * scale[0],
              9.0 * scale[1], 43.0 * scale[0], 6.0 * scale[1])
    Curveto_r(14.0 * scale[0], -5.0 * scale[1], 14.0 *
              scale[0], -4.0 * scale[1], 1.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 9.0 * scale[1], -19.0 * scale[0],
              13.0 * scale[1], -25.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -15.0 * scale[1], -81.0 *
              scale[0], -12.0 * scale[1], -94.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 24.0 * scale[1], -34.0 * scale[0],
              19.0 * scale[1], -29.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(253.0 * scale[0], 1143.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(525.0 * scale[0], 1140.0 * scale[1], x, y)
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
    Moveto(318.0 * scale[0], 1133.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(455.0 * scale[0], 1130.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -13.0 * scale[1], 5.0 *
              scale[0], -13.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(13.0 * scale[0], 8.0 * scale[1], 13.0 * scale[0],
              10.0 * scale[1], -2.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0], -
              4.0 * scale[1], -23.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(833.0 * scale[0], 1121.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-22.0 * scale[0], -6.0 * scale[1])
    Lineto_r(24.0 * scale[0], -12.0 * scale[1])
    Curveto_r(14.0 * scale[0], -6.0 * scale[1], 23.0 *
              scale[0], -7.0 * scale[1], 19.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], 5.0 * scale[0],
              9.0 * scale[1], 17.0 * scale[0], 9.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0],
              3.0 * scale[1], 15.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 10.0 * scale[1], -27.0 * scale[0],
              11.0 * scale[1], -53.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(220.0 * scale[0], 1030.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -7.0 * scale[1], -5.0 * scale[0], -
              10.0 * scale[1], 23.0 * scale[0], -10.0 * scale[1])
    Curveto_r(23.0 * scale[0], 0.0 * scale[1], 36.0 * scale[0],
              4.0 * scale[1], 32.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 13.0 * scale[1], -35.0 * scale[0],
              13.0 * scale[1], -55.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(315.0 * scale[0], 1030.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-18.0 * scale[0], -4.0 * scale[1], 43.0 *
              scale[0], -8.0 * scale[1], 145.0 * scale[0], -9.0 * scale[1])
    Curveto_r(116.0 * scale[0], 0.0 * scale[1], 170.0 * scale[0],
              3.0 * scale[1], 160.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 11.0 * scale[1], -261.0 * scale[0],
              11.0 * scale[1], -305.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(658.0 * scale[0], 1023.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(728.0 * scale[0], 1023.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(17.0 * scale[0], -2.0 * scale[1], 47.0 *
              scale[0], -2.0 * scale[1], 65.0 * scale[0], 0.0 * scale[1])
    Curveto_r(17.0 * scale[0], 2.0 * scale[1], 3.0 * scale[0],
              4.0 * scale[1], -33.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-36.0 * scale[0], 0.0 * scale[1], -50.0 *
              scale[0], -2.0 * scale[1], -32.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(790.0 * scale[0], 980.0 * scale[1], x, y)
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
    Moveto(960.0 * scale[0], 974.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], -6.0 * scale[0], -
              14.0 * scale[1], -15.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 7.0 * scale[1], -19.0 *
              scale[0], -1.0 * scale[1], -1.0 * scale[0], -20.0 * scale[1])
    Curveto_r(8.0 * scale[0], -7.0 * scale[1], 12.0 * scale[0], -
              22.0 * scale[1], 9.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -11.0 * scale[1], 0.0 * scale[0], -
              28.0 * scale[1], 6.0 * scale[0], -38.0 * scale[1])
    Curveto_r(8.0 * scale[0], -14.0 * scale[1], 10.0 *
              scale[0], -3.0 * scale[1], 11.0 * scale[0], 50.0 * scale[1])
    Curveto_r(0.0 * scale[0], 37.0 * scale[1], -2.0 * scale[0],
              67.0 * scale[1], -5.0 * scale[0], 67.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -5.0 * scale[0], -
              7.0 * scale[1], -5.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(620.0 * scale[0], 965.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -8.0 * scale[1], 17.0 * scale[0], -
              15.0 * scale[1], 22.0 * scale[0], -15.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 5.0 * scale[0],
              7.0 * scale[1], -2.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 8.0 * scale[1], -17.0 * scale[0],
              15.0 * scale[1], -22.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -5.0 * scale[0], -
              7.0 * scale[1], 2.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(861.0 * scale[0], 957.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -6.0 * scale[1], -11.0 * scale[0], -
              16.0 * scale[1], -11.0 * scale[0], -23.0 * scale[1])
    Curveto_r(0.0 * scale[0], -18.0 * scale[1], -27.0 * scale[0], -
              37.0 * scale[1], -33.0 * scale[0], -24.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -4.0 * scale[0],
              5.0 * scale[1], -3.0 * scale[0], -2.0 * scale[1])
    Curveto_r(2.0 * scale[0], -7.0 * scale[1], 9.0 * scale[0], -
              13.0 * scale[1], 16.0 * scale[0], -13.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0], -
              9.0 * scale[1], 21.0 * scale[0], -20.0 * scale[1])
    Curveto_r(6.0 * scale[0], -16.0 * scale[1], 8.0 * scale[0], -
              17.0 * scale[1], 8.0 * scale[0], -3.0 * scale[1])
    Curveto_r(1.0 * scale[0], 9.0 * scale[1], -4.0 * scale[0],
              20.0 * scale[1], -9.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -7.0 * scale[0],
              11.0 * scale[1], -4.0 * scale[0], 17.0 * scale[1])
    Curveto_r(4.0 * scale[0], 7.0 * scale[1], 9.0 * scale[0],
              6.0 * scale[1], 14.0 * scale[0], -2.0 * scale[1])
    Curveto_r(5.0 * scale[0], -8.0 * scale[1], 10.0 * scale[0], -
              3.0 * scale[1], 14.0 * scale[0], 14.0 * scale[1])
    Curveto_r(4.0 * scale[0], 15.0 * scale[1], 11.0 * scale[0],
              24.0 * scale[1], 16.0 * scale[0], 21.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 11.0 *
              scale[0], -1.0 * scale[1], 14.0 * scale[0], 4.0 * scale[1])
    Curveto_r(8.0 * scale[0], 13.0 * scale[1], -31.0 * scale[0],
              20.0 * scale[1], -43.0 * scale[0], 8.0 * scale[1])
    te.end_fill()
    Moveto(80.0 * scale[0], 956.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(300.0 * scale[0], 926.0 * scale[1], x, y)
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
    Moveto(256.0 * scale[0], 922.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 0.0 * scale[0], -
              13.0 * scale[1], 6.0 * scale[0], -15.0 * scale[1])
    Curveto_r(10.0 * scale[0], -4.0 * scale[1], 10.0 *
              scale[0], -6.0 * scale[1], 1.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -1.0 * scale[1], -13.0 * scale[0], -
              7.0 * scale[1], -13.0 * scale[0], -15.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 7.0 * scale[0], -
              12.0 * scale[1], 20.0 * scale[0], -9.0 * scale[1])
    Curveto_r(24.0 * scale[0], 6.0 * scale[1], 25.0 * scale[0],
              13.0 * scale[1], 7.0 * scale[0], 38.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 11.0 * scale[1], -16.0 * scale[0],
              14.0 * scale[1], -21.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(390.0 * scale[0], 900.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -8.0 * scale[0], -
              9.0 * scale[1], -21.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 5.0 * scale[1], -19.0 * scale[0],
              4.0 * scale[1], -14.0 * scale[0], -5.0 * scale[1])
    Curveto_r(5.0 * scale[0], -9.0 * scale[1], 4.0 * scale[0], -
              11.0 * scale[1], -3.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 11.0 * scale[1], -108.0 * scale[0], -
              40.0 * scale[1], -133.0 * scale[0], -76.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -17.0 * scale[1], -17.0 *
              scale[0], -28.0 * scale[1], -11.0 * scale[0], -24.0 * scale[1])
    Curveto_r(10.0 * scale[0], 6.0 * scale[1], 11.0 * scale[0],
              1.0 * scale[1], 6.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -37.0 * scale[1], -14.0 * scale[0], -
              42.0 * scale[1], -14.0 * scale[0], -13.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], -3.0 * scale[0],
              21.0 * scale[1], -6.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -3.0 * scale[0], -
              20.0 * scale[1], 1.0 * scale[0], -37.0 * scale[1])
    Curveto_r(5.0 * scale[0], -23.0 * scale[1], 10.0 * scale[0], -
              29.0 * scale[1], 18.0 * scale[0], -21.0 * scale[1])
    Curveto_r(14.0 * scale[0], 14.0 * scale[1], 37.0 * scale[0],
              14.0 * scale[1], 37.0 * scale[0], 0.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -4.0 * scale[0], -
              8.0 * scale[1], -8.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              1.0 * scale[1], -9.0 * scale[0], -9.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 4.0 * scale[0], -
              12.0 * scale[1], 14.0 * scale[0], -4.0 * scale[1])
    Curveto_r(20.0 * scale[0], 17.0 * scale[1], 16.0 * scale[0], -
              11.0 * scale[1], -6.0 * scale[0], -40.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -27.0 * scale[1], -41.0 *
              scale[0], -21.0 * scale[1], -41.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], -6.0 * scale[0],
              29.0 * scale[1], -13.0 * scale[0], 39.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 15.0 * scale[1], -14.0 * scale[0],
              14.0 * scale[1], -24.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -35.0 * scale[1], -36.0 * scale[0], -
              142.0 * scale[1], -30.0 * scale[0], -149.0 * scale[1])
    Curveto_r(3.0 * scale[0], -2.0 * scale[1], 22.0 * scale[0],
              12.0 * scale[1], 41.0 * scale[0], 33.0 * scale[1])
    Curveto_r(20.0 * scale[0], 21.0 * scale[1], 36.0 * scale[0],
              34.0 * scale[1], 36.0 * scale[0], 29.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -8.0 * scale[0], -
              18.0 * scale[1], -19.0 * scale[0], -29.0 * scale[1])
    Curveto_r(-23.0 * scale[0], -25.0 * scale[1], -36.0 *
              scale[0], -66.0 * scale[1], -22.0 * scale[0], -66.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              5.0 * scale[1], 16.0 * scale[0], 10.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], 11.0 * scale[0],
              7.0 * scale[1], 17.0 * scale[0], 4.0 * scale[1])
    Curveto_r(7.0 * scale[0], -4.0 * scale[1], 8.0 *
              scale[0], -2.0 * scale[1], 4.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 7.0 * scale[1], 3.0 * scale[0],
              26.0 * scale[1], 16.0 * scale[0], 44.0 * scale[1])
    Curveto_r(13.0 * scale[0], 18.0 * scale[1], 33.0 * scale[0],
              48.0 * scale[1], 45.0 * scale[0], 68.0 * scale[1])
    Curveto_r(20.0 * scale[0], 35.0 * scale[1], 20.0 * scale[0],
              36.0 * scale[1], 1.0 * scale[0], 59.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 13.0 * scale[1], -17.0 * scale[0],
              29.0 * scale[1], -14.0 * scale[0], 37.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], -1.0 * scale[0],
              13.0 * scale[1], -9.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0],
              34.0 * scale[1], 14.0 * scale[0], 64.0 * scale[1])
    Curveto_r(27.0 * scale[0], 26.0 * scale[1], 45.0 * scale[0],
              34.0 * scale[1], 84.0 * scale[0], 35.0 * scale[1])
    Curveto_r(10.0 * scale[0], 1.0 * scale[1], 15.0 * scale[0],
              6.0 * scale[1], 12.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 7.0 * scale[1], 3.0 * scale[0],
              8.0 * scale[1], 21.0 * scale[0], 4.0 * scale[1])
    Curveto_r(19.0 * scale[0], -5.0 * scale[1], 25.0 *
              scale[0], -4.0 * scale[1], 20.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 7.0 * scale[1], 6.0 * scale[0],
              11.0 * scale[1], 36.0 * scale[0], 12.0 * scale[1])
    Curveto_r(24.0 * scale[0], 1.0 * scale[1], 48.0 * scale[0],
              0.0 * scale[1], 53.0 * scale[0], -1.0 * scale[1])
    Curveto_r(38.0 * scale[0], -9.0 * scale[1], 123.0 * scale[0], -
              15.0 * scale[1], 119.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 21.0 * scale[1], -214.0 * scale[0],
              48.0 * scale[1], -214.0 * scale[0], 28.0 * scale[1])
    te.end_fill()
    Moveto(920.0 * scale[0], 880.0 * scale[1], x, y)
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
    Moveto(664.0 * scale[0], 871.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -5.0 * scale[1], -18.0 * scale[0], -
              11.0 * scale[1], -28.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -1.0 * scale[1], -20.0 * scale[0], -
              11.0 * scale[1], -22.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -15.0 * scale[1], 2.0 * scale[0], -
              17.0 * scale[1], 29.0 * scale[0], -12.0 * scale[1])
    Curveto_r(18.0 * scale[0], 4.0 * scale[1], 33.0 * scale[0],
              10.0 * scale[1], 35.0 * scale[0], 15.0 * scale[1])
    Curveto_r(2.0 * scale[0], 5.0 * scale[1], 12.0 * scale[0],
              7.0 * scale[1], 23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(13.0 * scale[0], -4.0 * scale[1], 18.0 * scale[0], -
              11.0 * scale[1], 14.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], 0.0 * scale[0], -
              22.0 * scale[1], 7.0 * scale[0], -30.0 * scale[1])
    Curveto_r(7.0 * scale[0], -9.0 * scale[1], 8.0 * scale[0], -
              13.0 * scale[1], 2.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 6.0 * scale[1], -64.0 * scale[0], -
              37.0 * scale[1], -64.0 * scale[0], -53.0 * scale[1])
    Curveto_r(0.0 * scale[0], -23.0 * scale[1], 32.0 *
              scale[0], -2.0 * scale[1], 68.0 * scale[0], 44.0 * scale[1])
    Curveto_r(25.0 * scale[0], 32.0 * scale[1], 28.0 * scale[0],
              55.0 * scale[1], 10.0 * scale[0], 78.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 19.0 * scale[1], -61.0 * scale[0],
              31.0 * scale[1], -74.0 * scale[0], 19.0 * scale[1])
    te.end_fill()
    Moveto(572.0 * scale[0], 844.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(10.0 * scale[0], -10.0 * scale[1], 20.0 * scale[0], -
              16.0 * scale[1], 22.0 * scale[0], -13.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              11.0 * scale[1], -17.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 13.0 * scale[1], -21.0 * scale[0],
              12.0 * scale[1], -5.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(878.0 * scale[0], 853.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(961.0 * scale[0], 834.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(322.0 * scale[0], 760.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -16.0 * scale[1], -22.0 *
              scale[0], -35.0 * scale[1], -22.0 * scale[0], -42.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -8.0 * scale[1], -7.0 *
              scale[0], -5.0 * scale[1], -16.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 19.0 * scale[1], -16.0 * scale[0],
              19.0 * scale[1], -12.0 * scale[0], 1.0 * scale[1])
    Curveto_r(5.0 * scale[0], -33.0 * scale[1], 22.0 * scale[0], -
              28.0 * scale[1], 61.0 * scale[0], 19.0 * scale[1])
    Curveto_r(22.0 * scale[0], 26.0 * scale[1], 32.0 * scale[0],
              45.0 * scale[1], 24.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -23.0 * scale[0], -
              13.0 * scale[1], -35.0 * scale[0], -30.0 * scale[1])
    te.end_fill()
    Moveto(395.0 * scale[0], 631.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              12.0 * scale[1], 3.0 * scale[0], -15.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 9.0 * scale[0],
              1.0 * scale[1], 9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], -3.0 * scale[0],
              19.0 * scale[1], -12.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(140.0 * scale[0], 466.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(946.0 * scale[0], 395.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -16.0 * scale[1], 8.0 * scale[0], -
              38.0 * scale[1], 8.0 * scale[0], -47.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 4.0 * scale[0], -
              14.0 * scale[1], 8.0 * scale[0], -12.0 * scale[1])
    Curveto_r(13.0 * scale[0], 8.0 * scale[1], 8.0 * scale[0],
              48.0 * scale[1], -8.0 * scale[0], 69.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 19.0 * scale[1], -15.0 * scale[0],
              18.0 * scale[1], -8.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(495.0 * scale[0], 343.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-55.0 * scale[0], -29.0 * scale[1], -81.0 *
              scale[0], -60.0 * scale[1], -51.0 * scale[0], -60.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              6.0 * scale[1], 9.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], 6.0 * scale[0],
              19.0 * scale[1], 21.0 * scale[0], 25.0 * scale[1])
    Curveto_r(20.0 * scale[0], 10.0 * scale[1], 29.0 * scale[0],
              9.0 * scale[1], 43.0 * scale[0], -2.0 * scale[1])
    Curveto_r(15.0 * scale[0], -12.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 11.0 * scale[1], -2.0 * scale[0],
              17.0 * scale[1], 8.0 * scale[0], 17.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -20.0 * scale[0],
              12.0 * scale[1], -55.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(235.0 * scale[0], 310.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(470.0 * scale[0], 310.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -5.0 * scale[1], -11.0 * scale[0], -
              12.0 * scale[1], -7.0 * scale[0], -16.0 * scale[1])
    Curveto_r(11.0 * scale[0], -11.0 * scale[1], -13.0 * scale[0], -
              33.0 * scale[1], -29.0 * scale[0], -27.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -14.0 * scale[0],
              0.0 * scale[1], -14.0 * scale[0], -6.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -7.0 * scale[0], -
              8.0 * scale[1], -15.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 5.0 * scale[1], -13.0 * scale[0],
              2.0 * scale[1], -9.0 * scale[0], -11.0 * scale[1])
    Curveto_r(5.0 * scale[0], -11.0 * scale[1], -2.0 * scale[0], -
              25.0 * scale[1], -21.0 * scale[0], -41.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -13.0 * scale[1], -32.0 *
              scale[0], -24.0 * scale[1], -36.0 * scale[0], -24.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0], -
              7.0 * scale[1], -3.0 * scale[0], -15.0 * scale[1])
    Curveto_r(4.0 * scale[0], -11.0 * scale[1], 0.0 * scale[0], -
              15.0 * scale[1], -16.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 0.0 * scale[1], -21.0 * scale[0], -
              3.0 * scale[1], -15.0 * scale[0], -52.0 * scale[1])
    Curveto_r(9.0 * scale[0], -63.0 * scale[1], 28.0 * scale[0], -
              80.0 * scale[1], 100.0 * scale[0], -90.0 * scale[1])
    Curveto_r(80.0 * scale[0], -10.0 * scale[1], 147.0 *
              scale[0], -9.0 * scale[1], 140.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], -15.0 * scale[0],
              10.0 * scale[1], -27.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -18.0 * scale[0],
              3.0 * scale[1], -9.0 * scale[0], 14.0 * scale[1])
    Curveto_r(8.0 * scale[0], 10.0 * scale[1], 9.0 * scale[0],
              16.0 * scale[1], 1.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0],
              1.0 * scale[1], -10.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -4.0 * scale[0], -
              11.0 * scale[1], -9.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0],
              32.0 * scale[1], -4.0 * scale[0], 70.0 * scale[1])
    Curveto_r(3.0 * scale[0], 39.0 * scale[1], 1.0 * scale[0],
              78.0 * scale[1], -3.0 * scale[0], 88.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 9.0 * scale[1], -8.0 * scale[0],
              19.0 * scale[1], -9.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              13.0 * scale[1], -10.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 30.0 * scale[1], 2.0 * scale[0],
              31.0 * scale[1], 20.0 * scale[0], 0.0 * scale[1])
    Curveto_r(13.0 * scale[0], -23.0 * scale[1], 15.0 *
              scale[0], -24.0 * scale[1], 10.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 13.0 * scale[1], -1.0 * scale[0],
              30.0 * scale[1], 6.0 * scale[0], 38.0 * scale[1])
    Curveto_r(17.0 * scale[0], 20.0 * scale[1], -8.0 * scale[0],
              48.0 * scale[1], -31.0 * scale[0], 34.0 * scale[1])
    te.end_fill()
    Moveto_r(-21.0 * scale[0], -143.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -21.0 * scale[1], -1.0 * scale[0], -
              21.0 * scale[1], -9.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 28.0 * scale[1], -12.0 * scale[0],
              37.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 10.0 * scale[0], -
              16.0 * scale[1], 9.0 * scale[0], -28.0 * scale[1])
    te.end_fill()
    Moveto_r(-123.0 * scale[0], -36.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -5.0 * scale[1], 0.0 * scale[0], -
              12.0 * scale[1], 6.0 * scale[0], -14.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 6.0 * scale[0], -
              6.0 * scale[1], -4.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -1.0 * scale[1], -18.0 * scale[0],
              6.0 * scale[1], -18.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 5.0 * scale[0],
              15.0 * scale[1], 11.0 * scale[0], 15.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0], -
              4.0 * scale[1], 5.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(270.0 * scale[0], 305.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 10.0 * scale[0], -
              10.0 * scale[1], 23.0 * scale[0], -16.0 * scale[1])
    Curveto_r(20.0 * scale[0], -11.0 * scale[1], 21.0 *
              scale[0], -11.0 * scale[1], 8.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -31.0 * scale[0],
              23.0 * scale[1], -31.0 * scale[0], 12.0 * scale[1])
    te.end_fill()
    Moveto(67.0 * scale[0], 69.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -13.0 * scale[1], 8.0 * scale[0], -
              18.0 * scale[1], 11.0 * scale[0], -10.0 * scale[1])
    Curveto_r(2.0 * scale[0], 7.0 * scale[1], -1.0 * scale[0],
              18.0 * scale[1], -6.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 8.0 * scale[1], -9.0 * scale[0],
              4.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(780.0 * scale[0], 10.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -7.0 * scale[1], -3.0 * scale[0], -
              10.0 * scale[1], 28.0 * scale[0], -10.0 * scale[1])
    Curveto_r(26.0 * scale[0], 0.0 * scale[1], 41.0 * scale[0],
              4.0 * scale[1], 37.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 13.0 * scale[1], -45.0 * scale[0],
              13.0 * scale[1], -65.0 * scale[0], 0.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#b97585')
    te.end_fill()
    Moveto(833.0 * scale[0], 1313.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(445.0 * scale[0], 1300.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-33.0 * scale[0], -13.0 * scale[1], -48.0 *
              scale[0], -38.0 * scale[1], -55.0 * scale[0], -90.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -40.0 * scale[1], -4.0 *
              scale[0], -47.0 * scale[1], 9.0 * scale[0], -45.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 15.0 * scale[0],
              10.0 * scale[1], 13.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 15.0 * scale[1], 1.0 * scale[0],
              32.0 * scale[1], 6.0 * scale[0], 39.0 * scale[1])
    Curveto_r(6.0 * scale[0], 7.0 * scale[1], 11.0 * scale[0],
              15.0 * scale[1], 11.0 * scale[0], 19.0 * scale[1])
    Curveto_r(7.0 * scale[0], 46.0 * scale[1], 50.0 * scale[0],
              51.0 * scale[1], 86.0 * scale[0], 11.0 * scale[1])
    Curveto_r(27.0 * scale[0], -31.0 * scale[1], 31.0 * scale[0], -
              49.0 * scale[1], 13.0 * scale[0], -56.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -3.0 * scale[1], -10.0 *
              scale[0], -7.0 * scale[1], 1.0 * scale[0], -20.0 * scale[1])
    Curveto_r(10.0 * scale[0], -13.0 * scale[1], 11.0 *
              scale[0], -20.0 * scale[1], 2.0 * scale[0], -31.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -12.0 * scale[1], -8.0 *
              scale[0], -13.0 * scale[1], 9.0 * scale[0], -9.0 * scale[1])
    Curveto_r(27.0 * scale[0], 7.0 * scale[1], 42.0 * scale[0],
              36.0 * scale[1], 38.0 * scale[0], 76.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 25.0 * scale[1], -7.0 * scale[0],
              32.0 * scale[1], -23.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -1.0 * scale[1], -14.0 *
              scale[0], 0.0 * scale[1], -7.0 * scale[0], 3.0 * scale[1])
    Curveto_r(24.0 * scale[0], 11.0 * scale[1], 12.0 * scale[0],
              26.0 * scale[1], -15.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-25.0 * scale[0], -6.0 * scale[1], -26.0 *
              scale[0], -5.0 * scale[1], -8.0 * scale[0], 6.0 * scale[1])
    Curveto_r(19.0 * scale[0], 11.0 * scale[1], 19.0 * scale[0],
              11.0 * scale[1], 0.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-26.0 * scale[0], 10.0 * scale[1], -55.0 * scale[0],
              10.0 * scale[1], -80.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto_r(119.0 * scale[0], -75.0 * scale[1], 0, 0)
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
    Moveto(85.0 * scale[0], 1293.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -5.0 * scale[1], -12.0 * scale[0], -
              15.0 * scale[1], -14.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -8.0 * scale[1], -6.0 * scale[0], -
              23.0 * scale[1], -8.0 * scale[0], -32.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -12.0 * scale[1], 2.0 * scale[0], -
              17.0 * scale[1], 23.0 * scale[0], -20.0 * scale[1])
    Curveto_r(39.0 * scale[0], -4.0 * scale[1], 41.0 * scale[0], -
              24.0 * scale[1], 3.0 * scale[0], -43.0 * scale[1])
    Curveto_r(-40.0 * scale[0], -21.0 * scale[1], -26.0 *
              scale[0], -40.0 * scale[1], 23.0 * scale[0], -29.0 * scale[1])
    Curveto_r(18.0 * scale[0], 4.0 * scale[1], 36.0 * scale[0],
              8.0 * scale[1], 40.0 * scale[0], 8.0 * scale[1])
    Curveto_r(3.0 * scale[0], 1.0 * scale[1], 10.0 * scale[0],
              5.0 * scale[1], 15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(4.0 * scale[0], 5.0 * scale[1], 3.0 * scale[0],
              7.0 * scale[1], -2.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -3.0 * scale[1], -10.0 * scale[0],
              10.0 * scale[1], -10.0 * scale[0], 33.0 * scale[1])
    Curveto_r(0.0 * scale[0], 23.0 * scale[1], 4.0 * scale[0],
              36.0 * scale[1], 10.0 * scale[0], 33.0 * scale[1])
    Curveto_r(5.0 * scale[0], -4.0 * scale[1], 7.0 *
              scale[0], -2.0 * scale[1], 2.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 5.0 * scale[1], -22.0 * scale[0],
              9.0 * scale[1], -39.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-43.0 * scale[0], 1.0 * scale[1], -48.0 * scale[0],
              24.0 * scale[1], -6.0 * scale[0], 28.0 * scale[1])
    Curveto_r(18.0 * scale[0], 2.0 * scale[1], 33.0 * scale[0],
              8.0 * scale[1], 33.0 * scale[0], 13.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], -56.0 * scale[0],
              18.0 * scale[1], -70.0 * scale[0], 8.0 * scale[1])
    te.end_fill()
    Moveto(822.0 * scale[0], 1275.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -14.0 * scale[1], 1.0 * scale[0], -
              25.0 * scale[1], -3.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              6.0 * scale[1], -9.0 * scale[0], -13.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 13.0 * scale[0], -
              12.0 * scale[1], 35.0 * scale[0], -11.0 * scale[1])
    Curveto_r(19.0 * scale[0], 1.0 * scale[1], 38.0 * scale[0], -
              3.0 * scale[1], 42.0 * scale[0], -10.0 * scale[1])
    Curveto_r(3.0 * scale[0], -6.0 * scale[1], 3.0 * scale[0], -
              8.0 * scale[1], -1.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 4.0 * scale[1], -21.0 * scale[0], -
              7.0 * scale[1], -37.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -16.0 * scale[1], -35.0 *
              scale[0], -27.0 * scale[1], -39.0 * scale[0], -24.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -12.0 * scale[0],
              0.0 * scale[1], -16.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -8.0 * scale[1], -3.0 *
              scale[0], -9.0 * scale[1], 4.0 * scale[0], -5.0 * scale[1])
    Curveto_r(7.0 * scale[0], 4.0 * scale[1], 12.0 * scale[0],
              2.0 * scale[1], 12.0 * scale[0], -3.0 * scale[1])
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], 33.0 * scale[0], -
              15.0 * scale[1], 44.0 * scale[0], -3.0 * scale[1])
    Curveto_r(4.0 * scale[0], 4.0 * scale[1], 13.0 * scale[0],
              7.0 * scale[1], 19.0 * scale[0], 7.0 * scale[1])
    Curveto_r(17.0 * scale[0], 0.0 * scale[1], 41.0 * scale[0],
              49.0 * scale[1], 34.0 * scale[0], 69.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 9.0 * scale[1], -20.0 * scale[0],
              19.0 * scale[1], -37.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-39.0 * scale[0], 7.0 * scale[1], -34.0 * scale[0],
              27.0 * scale[1], 8.0 * scale[0], 31.0 * scale[1])
    Curveto_r(49.0 * scale[0], 5.0 * scale[1], 38.0 * scale[0],
              22.0 * scale[1], -14.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-44.0 * scale[0], 0.0 * scale[1], -46.0 * scale[0], -
              1.0 * scale[1], -42.0 * scale[0], -25.0 * scale[1])
    te.end_fill()
    Moveto(624.0 * scale[0], 1235.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -8.0 * scale[1], -3.0 * scale[0], -
              22.0 * scale[1], 0.0 * scale[0], -30.0 * scale[1])
    Curveto_r(5.0 * scale[0], -13.0 * scale[1], 10.0 * scale[0], -
              14.0 * scale[1], 28.0 * scale[0], -4.0 * scale[1])
    Lineto_r(21.0 * scale[0], 12.0 * scale[1])
    Lineto_r(-22.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 7.0 * scale[1], -18.0 * scale[0],
              15.0 * scale[1], -15.0 * scale[0], 19.0 * scale[1])
    Curveto_r(4.0 * scale[0], 4.0 * scale[1], 4.0 * scale[0],
              7.0 * scale[1], 0.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              7.0 * scale[1], -12.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(352.0 * scale[0], 1215.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(313.0 * scale[0], 1223.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-18.0 * scale[0], -7.0 * scale[1], -16.0 *
              scale[0], -16.0 * scale[1], 5.0 * scale[0], -29.0 * scale[1])
    Curveto_r(15.0 * scale[0], -10.0 * scale[1], 18.0 *
              scale[0], -8.0 * scale[1], 20.0 * scale[0], 12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 24.0 * scale[1], -2.0 * scale[0],
              27.0 * scale[1], -25.0 * scale[0], 17.0 * scale[1])
    te.end_fill()
    Moveto(592.0 * scale[0], 1210.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(47.0 * scale[0], 1209.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(171.0 * scale[0], 1204.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(415.0 * scale[0], 1150.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -11.0 *
              scale[0], -7.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -8.0 * scale[0],
              2.0 * scale[1], -4.0 * scale[0], -5.0 * scale[1])
    Curveto_r(6.0 * scale[0], -9.0 * scale[1], 11.0 *
              scale[0], -9.0 * scale[1], 22.0 * scale[0], 0.0 * scale[1])
    Curveto_r(14.0 * scale[0], 11.0 * scale[1], 18.0 * scale[0],
              19.0 * scale[1], 10.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              5.0 * scale[1], -11.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(63.0 * scale[0], 1123.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 25.0 *
              scale[0], -2.0 * scale[1], 35.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -27.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(498.0 * scale[0], 1123.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(388.0 * scale[0], 1013.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(788.0 * scale[0], 963.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(770.0 * scale[0], 921.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 18.0 * scale[1], -14.0 * scale[0],
              21.0 * scale[1], -14.0 * scale[0], 7.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#b77c37')
    te.end_fill()
    Moveto(359.0 * scale[0], 1383.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(17.0 * scale[0], -12.0 * scale[1], 47.0 * scale[0], -
              16.0 * scale[1], 110.0 * scale[0], -17.0 * scale[1])
    Curveto_r(62.0 * scale[0], -1.0 * scale[1], 85.0 * scale[0], -
              4.0 * scale[1], 84.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -7.0 * scale[1], 4.0 * scale[0], -
              10.0 * scale[1], 12.0 * scale[0], -7.0 * scale[1])
    Curveto_r(9.0 * scale[0], 4.0 * scale[1], 22.0 * scale[0],
              1.0 * scale[1], 30.0 * scale[0], -6.0 * scale[1])
    Curveto_r(8.0 * scale[0], -6.0 * scale[1], 20.0 * scale[0], -
              10.0 * scale[1], 27.0 * scale[0], -8.0 * scale[1])
    Curveto_r(12.0 * scale[0], 4.0 * scale[1], -74.0 * scale[0],
              48.0 * scale[1], -94.0 * scale[0], 48.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0],
              5.0 * scale[1], -3.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 1.0 * scale[0],
              10.0 * scale[1], -4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              4.0 * scale[1], -11.0 * scale[0], -9.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -27.0 * scale[0], -
              11.0 * scale[1], -60.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-68.0 * scale[0], -3.0 * scale[1], -83.0 * scale[0],
              9.0 * scale[1], -17.0 * scale[0], 15.0 * scale[1])
    Curveto_r(29.0 * scale[0], 2.0 * scale[1], 21.0 * scale[0],
              4.0 * scale[1], -28.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-67.0 * scale[0], 2.0 * scale[1], -69.0 * scale[0],
              1.0 * scale[1], -46.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(185.0 * scale[0], 1370.0 * scale[1], x, y)
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
    Moveto(220.0 * scale[0], 1368.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -3.0 * scale[1], 6.0 * scale[0], -
              9.0 * scale[1], 13.0 * scale[0], -11.0 * scale[1])
    Curveto_r(13.0 * scale[0], -6.0 * scale[1], -25.0 * scale[0], -
              11.0 * scale[1], -55.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 1.0 * scale[1], -18.0 *
              scale[0], -2.0 * scale[1], -18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], 40.0 * scale[0], -
              31.0 * scale[1], 80.0 * scale[0], -35.0 * scale[1])
    Lineto_r(35.0 * scale[0], -4.0 * scale[1])
    Lineto_r(-39.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-35.0 * scale[0], -2.0 * scale[1], -38.0 *
              scale[0], -4.0 * scale[1], -22.0 * scale[0], -15.0 * scale[1])
    Curveto_r(10.0 * scale[0], -7.0 * scale[1], 34.0 * scale[0], -
              11.0 * scale[1], 58.0 * scale[0], -9.0 * scale[1])
    Curveto_r(28.0 * scale[0], 3.0 * scale[1], 36.0 * scale[0],
              7.0 * scale[1], 27.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              8.0 * scale[1], 31.0 * scale[0], 8.0 * scale[1])
    Curveto_r(39.0 * scale[0], -1.0 * scale[1], 41.0 *
              scale[0], -2.0 * scale[1], 15.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-28.0 * scale[0], -6.0 * scale[1], -29.0 *
              scale[0], -7.0 * scale[1], -7.0 * scale[0], -13.0 * scale[1])
    Curveto_r(13.0 * scale[0], -4.0 * scale[1], 28.0 *
              scale[0], -1.0 * scale[1], 36.0 * scale[0], 7.0 * scale[1])
    Curveto_r(7.0 * scale[0], 8.0 * scale[1], 16.0 * scale[0],
              11.0 * scale[1], 19.0 * scale[0], 8.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 13.0 * scale[0],
              2.0 * scale[1], 22.0 * scale[0], 11.0 * scale[1])
    Curveto_r(9.0 * scale[0], 9.0 * scale[1], 23.0 * scale[0],
              16.0 * scale[1], 31.0 * scale[0], 16.0 * scale[1])
    Curveto_r(19.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              23.0 * scale[1], -9.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 5.0 * scale[1], -31.0 * scale[0],
              1.0 * scale[1], -49.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-27.0 * scale[0], -14.0 * scale[1], -30.0 *
              scale[0], -14.0 * scale[1], -25.0 * scale[0], -1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 10.0 * scale[1], -2.0 * scale[0],
              18.0 * scale[1], -16.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-28.0 * scale[0], 10.0 * scale[1], -127.0 * scale[0],
              12.0 * scale[1], -127.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto_r(100.0 * scale[0], -8.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -5.0 * scale[1], -24.0 * scale[0], -
              10.0 * scale[1], -35.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-27.0 * scale[0], 0.0 * scale[1], -3.0 * scale[0],
              15.0 * scale[1], 27.0 * scale[0], 17.0 * scale[1])
    Curveto_r(18.0 * scale[0], 2.0 * scale[1], 20.0 * scale[0],
              0.0 * scale[1], 8.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto_r(100.0 * scale[0], -20.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -9.0 * scale[1], -13.0 *
              scale[0], -10.0 * scale[1], 0.0 * scale[0], -10.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0], -
              1.0 * scale[1], 0.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -5.0 * scale[1], -26.0 *
              scale[0], -9.0 * scale[1], -40.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 1.0 * scale[1], -23.0 *
              scale[0], 2.0 * scale[1], 5.0 * scale[0], 9.0 * scale[1])
    Curveto_r(17.0 * scale[0], 4.0 * scale[1], 23.0 * scale[0],
              8.0 * scale[1], 15.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 1.0 * scale[1], -13.0 * scale[0],
              2.0 * scale[1], 0.0 * scale[0], 11.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 20.0 * scale[0],
              10.0 * scale[1], 25.0 * scale[0], 10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 3.0 * scale[0], -
              5.0 * scale[1], -5.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(616.0 * scale[0], 1360.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(50.0 * scale[0], -24.0 * scale[1], 148.0 * scale[0], -
              40.0 * scale[1], 183.0 * scale[0], -31.0 * scale[1])
    Curveto_r(16.0 * scale[0], 5.0 * scale[1], 21.0 * scale[0],
              10.0 * scale[1], 13.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 19.0 * scale[1], -113.0 * scale[0],
              37.0 * scale[1], -172.0 * scale[0], 37.0 * scale[1])
    Lineto_r(-65.0 * scale[0], -1.0 * scale[1])
    Lineto_r(41.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(510.0 * scale[0], 1339.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-24.0 * scale[0], -20.0 * scale[1], -24.0 *
              scale[0], -20.0 * scale[1], -2.0 * scale[0], -14.0 * scale[1])
    Curveto_r(13.0 * scale[0], 4.0 * scale[1], 22.0 * scale[0],
              2.0 * scale[1], 22.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              9.0 * scale[1], 8.0 * scale[0], -6.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 20.0 * scale[0], -
              8.0 * scale[1], 35.0 * scale[0], -24.0 * scale[1])
    Curveto_r(17.0 * scale[0], -18.0 * scale[1], 34.0 * scale[0], -
              26.0 * scale[1], 46.0 * scale[0], -23.0 * scale[1])
    Curveto_r(10.0 * scale[0], 3.0 * scale[1], 22.0 * scale[0],
              0.0 * scale[1], 25.0 * scale[0], -6.0 * scale[1])
    Curveto_r(5.0 * scale[0], -7.0 * scale[1], 1.0 * scale[0], -
              8.0 * scale[1], -11.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 3.0 * scale[1], -15.0 * scale[0],
              3.0 * scale[1], -12.0 * scale[0], -1.0 * scale[1])
    Curveto_r(4.0 * scale[0], -4.0 * scale[1], 17.0 * scale[0], -
              9.0 * scale[1], 29.0 * scale[0], -11.0 * scale[1])
    Curveto_r(13.0 * scale[0], -3.0 * scale[1], 27.0 * scale[0], -
              10.0 * scale[1], 32.0 * scale[0], -17.0 * scale[1])
    Curveto_r(4.0 * scale[0], -7.0 * scale[1], 8.0 * scale[0], -
              8.0 * scale[1], 8.0 * scale[0], -3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], 20.0 * scale[0], -
              15.0 * scale[1], 20.0 * scale[0], -27.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -59.0 * scale[0], -
              23.0 * scale[1], -72.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 1.0 * scale[1], -8.0 * scale[0], -
              10.0 * scale[1], -9.0 * scale[0], -26.0 * scale[1])
    Curveto_r(0.0 * scale[0], -26.0 * scale[1], -1.0 * scale[0], -
              26.0 * scale[1], -9.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 15.0 * scale[1], -15.0 * scale[0],
              21.0 * scale[1], -25.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -3.0 * scale[1], -15.0 * scale[0], -
              8.0 * scale[1], -15.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -3.0 * scale[1], 6.0 * scale[0], -
              3.0 * scale[1], 13.0 * scale[0], 0.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 14.0 * scale[0], -
              1.0 * scale[1], 14.0 * scale[0], -9.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -4.0 * scale[0], -
              11.0 * scale[1], -9.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -16.0 * scale[0],
              0.0 * scale[1], -25.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -11.0 * scale[1], -16.0 *
              scale[0], -11.0 * scale[1], -9.0 * scale[0], 2.0 * scale[1])
    Curveto_r(4.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              8.0 * scale[1], -7.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -10.0 * scale[1], -17.0 * scale[0], -
              15.0 * scale[1], -20.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 3.0 * scale[1], -7.0 * scale[0],
              1.0 * scale[1], -7.0 * scale[0], -6.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -4.0 * scale[0], -
              10.0 * scale[1], -9.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -13.0 * scale[0],
              1.0 * scale[1], -16.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -14.0 * scale[1], 263.0 *
              scale[0], -6.0 * scale[1], 277.0 * scale[0], 8.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 6.0 * scale[0],
              17.0 * scale[1], -4.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 12.0 * scale[1], -18.0 * scale[0],
              18.0 * scale[1], -21.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -3.0 * scale[1], -7.0 *
              scale[0], -1.0 * scale[1], -7.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], 5.0 * scale[0],
              12.0 * scale[1], 11.0 * scale[0], 12.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0],
              4.0 * scale[1], 5.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], -16.0 * scale[0],
              7.0 * scale[1], -29.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -3.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -15.0 * scale[0], 2.0 * scale[1])
    Curveto_r(4.0 * scale[0], 4.0 * scale[1], 21.0 * scale[0],
              8.0 * scale[1], 38.0 * scale[0], 7.0 * scale[1])
    Curveto_r(16.0 * scale[0], 0.0 * scale[1], 30.0 * scale[0],
              3.0 * scale[1], 30.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], -34.0 * scale[0],
              21.0 * scale[1], -56.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -5.0 * scale[1], -16.0 *
              scale[0], -4.0 * scale[1], -4.0 * scale[0], 5.0 * scale[1])
    Curveto_r(8.0 * scale[0], 6.0 * scale[1], 27.0 * scale[0],
              11.0 * scale[1], 43.0 * scale[0], 11.0 * scale[1])
    Curveto_r(15.0 * scale[0], 0.0 * scale[1], 27.0 * scale[0],
              5.0 * scale[1], 27.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -12.0 * scale[0],
              10.0 * scale[1], -27.0 * scale[0], 11.0 * scale[1])
    Lineto_r(-28.0 * scale[0], 0.0 * scale[1])
    Lineto_r(25.0 * scale[0], 11.0 * scale[1])
    Lineto_r(25.0 * scale[0], 11.0 * scale[1])
    Lineto_r(-30.0 * scale[0], 7.0 * scale[1])
    Lineto_r(-30.0 * scale[0], 8.0 * scale[1])
    Lineto_r(28.0 * scale[0], 1.0 * scale[1])
    Curveto_r(38.0 * scale[0], 1.0 * scale[1], 34.0 * scale[0],
              19.0 * scale[1], -5.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-84.0 * scale[0], 13.0 * scale[1], -108.0 * scale[0],
              14.0 * scale[1], -108.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], -13.0 * scale[0], -
              8.0 * scale[1], -30.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -27.0 * scale[0],
              5.0 * scale[1], -23.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], -4.0 * scale[0],
              6.0 * scale[1], -16.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-23.0 * scale[0], -7.0 * scale[1], -55.0 * scale[0],
              11.0 * scale[1], -45.0 * scale[0], 26.0 * scale[1])
    Curveto_r(8.0 * scale[0], 14.0 * scale[1], 1.0 * scale[0],
              11.0 * scale[1], -26.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto_r(110.0 * scale[0], -51.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], -6.0 * scale[0], -
              8.0 * scale[1], -14.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0],
              4.0 * scale[1], -20.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 4.0 * scale[1], 4.0 * scale[0],
              8.0 * scale[1], 15.0 * scale[0], 8.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0], -
              4.0 * scale[1], 19.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto_r(90.0 * scale[0], -38.0 * scale[1], 0, 0)
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
    Moveto(276.0 * scale[0], 1261.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -26.0 *
              scale[0], -6.0 * scale[1], -51.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-31.0 * scale[0], 3.0 * scale[1], -45.0 * scale[0],
              1.0 * scale[1], -45.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], 5.0 * scale[0], -
              9.0 * scale[1], 12.0 * scale[0], -5.0 * scale[1])
    Curveto_r(7.0 * scale[0], 5.0 * scale[1], 9.0 * scale[0],
              0.0 * scale[1], 6.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -18.0 * scale[1], -2.0 * scale[0], -
              20.0 * scale[1], 31.0 * scale[0], -15.0 * scale[1])
    Curveto_r(20.0 * scale[0], 4.0 * scale[1], 38.0 * scale[0],
              10.0 * scale[1], 39.0 * scale[0], 15.0 * scale[1])
    Curveto_r(2.0 * scale[0], 4.0 * scale[1], 8.0 * scale[0],
              8.0 * scale[1], 13.0 * scale[0], 8.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0], -
              4.0 * scale[1], 4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], 1.0 * scale[0], -
              7.0 * scale[1], 11.0 * scale[0], -3.0 * scale[1])
    Curveto_r(15.0 * scale[0], 6.0 * scale[1], 15.0 * scale[0],
              7.0 * scale[1], -2.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 13.0 * scale[1], -16.0 * scale[0],
              14.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(20.0 * scale[0], -2.0 * scale[1], 34.0 * scale[0],
              0.0 * scale[1], 32.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 11.0 * scale[1], -61.0 * scale[0],
              10.0 * scale[1], -68.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(235.0 * scale[0], 1203.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -3.0 * scale[1], -34.0 *
              scale[0], -9.0 * scale[1], -40.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -8.0 * scale[1], -5.0 *
              scale[0], -9.0 * scale[1], 7.0 * scale[0], -5.0 * scale[1])
    Curveto_r(11.0 * scale[0], 4.0 * scale[1], 15.0 * scale[0],
              2.0 * scale[1], 12.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -10.0 * scale[1], 13.0 * scale[0], -
              17.0 * scale[1], 58.0 * scale[0], -24.0 * scale[1])
    Curveto_r(74.0 * scale[0], -13.0 * scale[1], 118.0 *
              scale[0], -13.0 * scale[1], 118.0 * scale[0], 0.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -4.0 * scale[0],
              6.0 * scale[1], -10.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -10.0 * scale[0],
              0.0 * scale[1], -10.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], -2.0 * scale[0],
              10.0 * scale[1], -9.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -11.0 * scale[1], -9.0 *
              scale[0], -11.0 * scale[1], -14.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 10.0 * scale[1], -6.0 * scale[0],
              10.0 * scale[1], -6.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -7.0 * scale[1], -6.0 * scale[0], -
              13.0 * scale[1], -12.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0],
              6.0 * scale[1], -6.0 * scale[0], 13.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], -1.0 * scale[0],
              14.0 * scale[1], -9.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              5.0 * scale[1], -7.0 * scale[0], -10.0 * scale[1])
    Curveto_r(3.0 * scale[0], -6.0 * scale[1], 1.0 * scale[0], -
              7.0 * scale[1], -5.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -12.0 * scale[0],
              14.0 * scale[1], -12.0 * scale[0], 21.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], -6.0 * scale[0],
              12.0 * scale[1], -17.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -4.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -9.0 * scale[0], 5.0 * scale[1])
    Curveto_r(4.0 * scale[0], 7.0 * scale[1], 6.0 * scale[0],
              11.0 * scale[1], 4.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -1.0 * scale[1], -16.0 *
              scale[0], -4.0 * scale[1], -33.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(210.0 * scale[0], 1141.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 28.0 * scale[0], -
              15.0 * scale[1], 63.0 * scale[0], -24.0 * scale[1])
    Curveto_r(56.0 * scale[0], -15.0 * scale[1], 41.0 * scale[0], -
              16.0 * scale[1], -38.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0], -
              6.0 * scale[1], 35.0 * scale[0], -20.0 * scale[1])
    Curveto_r(36.0 * scale[0], -14.0 * scale[1], 79.0 * scale[0], -
              32.0 * scale[1], 96.0 * scale[0], -41.0 * scale[1])
    Curveto_r(25.0 * scale[0], -12.0 * scale[1], 57.0 * scale[0], -
              15.0 * scale[1], 157.0 * scale[0], -12.0 * scale[1])
    Curveto_r(69.0 * scale[0], 2.0 * scale[1], 123.0 * scale[0],
              0.0 * scale[1], 120.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -5.0 * scale[1], 18.0 *
              scale[0], -8.0 * scale[1], 46.0 * scale[0], -8.0 * scale[1])
    Curveto_r(27.0 * scale[0], 0.0 * scale[1], 53.0 * scale[0],
              5.0 * scale[1], 57.0 * scale[0], 11.0 * scale[1])
    Curveto_r(5.0 * scale[0], 9.0 * scale[1], -1.0 * scale[0],
              10.0 * scale[1], -20.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -4.0 * scale[1], -25.0 *
              scale[0], -3.0 * scale[1], -22.0 * scale[0], 3.0 * scale[1])
    Curveto_r(4.0 * scale[0], 5.0 * scale[1], 27.0 * scale[0],
              13.0 * scale[1], 51.0 * scale[0], 17.0 * scale[1])
    Curveto_r(26.0 * scale[0], 3.0 * scale[1], 49.0 * scale[0],
              13.0 * scale[1], 55.0 * scale[0], 23.0 * scale[1])
    Curveto_r(6.0 * scale[0], 9.0 * scale[1], 10.0 * scale[0],
              11.0 * scale[1], 10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], 8.0 * scale[0], -
              13.0 * scale[1], 17.0 * scale[0], -13.0 * scale[1])
    Curveto_r(15.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              1.0 * scale[1], -2.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 11.0 * scale[1], -23.0 * scale[0],
              11.0 * scale[1], -43.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -8.0 * scale[1], -76.0 * scale[0], -
              13.0 * scale[1], -178.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-133.0 * scale[0], -2.0 * scale[1], -154.0 * scale[0],
              0.0 * scale[1], -154.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -4.0 * scale[0],
              15.0 * scale[1], -10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              3.0 * scale[1], -7.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], -11.0 * scale[1], -6.0 * scale[0], -
              13.0 * scale[1], -53.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 0.0 * scale[1], -40.0 * scale[0],
              4.0 * scale[1], -40.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 18.0 * scale[0],
              7.0 * scale[1], 40.0 * scale[0], 5.0 * scale[1])
    Curveto_r(22.0 * scale[0], -2.0 * scale[1], 40.0 * scale[0],
              1.0 * scale[1], 40.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -38.0 * scale[0],
              20.0 * scale[1], -45.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -7.0 *
              scale[0], -8.0 * scale[1], -11.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 7.0 * scale[1], -24.0 * scale[0],
              12.0 * scale[1], -47.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 0.0 * scale[1], -59.0 * scale[0],
              4.0 * scale[1], -79.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 5.0 * scale[1], -38.0 * scale[0],
              6.0 * scale[1], -38.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(170.0 * scale[0], 1126.0 * scale[1], x, y)
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
    Moveto(144.0 * scale[0], 1088.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -7.0 * scale[1], -3.0 *
              scale[0], -8.0 * scale[1], 5.0 * scale[0], -3.0 * scale[1])
    Curveto_r(11.0 * scale[0], 6.0 * scale[1], 29.0 * scale[0],
              0.0 * scale[1], 103.0 * scale[0], -36.0 * scale[1])
    Curveto_r(23.0 * scale[0], -12.0 * scale[1], 88.0 *
              scale[0], -11.0 * scale[1], 88.0 * scale[0], 0.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], -3.0 * scale[0],
              10.0 * scale[1], -110.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-80.0 * scale[0], 19.0 * scale[1], -77.0 * scale[0],
              19.0 * scale[1], -86.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(6.0 * scale[0], 1012.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -11.0 * scale[1], -6.0 *
              scale[0], -59.0 * scale[1], 9.0 * scale[0], -78.0 * scale[1])
    Curveto_r(13.0 * scale[0], -16.0 * scale[1], 14.0 *
              scale[0], -16.0 * scale[1], 9.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 24.0 * scale[1], 13.0 * scale[0],
              47.0 * scale[1], 45.0 * scale[0], 47.0 * scale[1])
    Curveto_r(24.0 * scale[0], 1.0 * scale[1], 24.0 * scale[0],
              2.0 * scale[1], 7.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 8.0 * scale[1], -24.0 * scale[0],
              8.0 * scale[1], -37.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -9.0 * scale[1], -19.0 *
              scale[0], -8.0 * scale[1], -23.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 14.0 * scale[1], 2.0 * scale[0],
              15.0 * scale[1], 59.0 * scale[0], 10.0 * scale[1])
    Curveto_r(78.0 * scale[0], -6.0 * scale[1], 99.0 * scale[0], -
              21.0 * scale[1], 142.0 * scale[0], -102.0 * scale[1])
    Curveto_r(27.0 * scale[0], -53.0 * scale[1], 27.0 *
              scale[0], -54.0 * scale[1], 8.0 * scale[0], -77.0 * scale[1])
    Lineto_r(-19.0 * scale[0], -23.0 * scale[1])
    Lineto_r(24.0 * scale[0], 22.0 * scale[1])
    Curveto_r(19.0 * scale[0], 18.0 * scale[1], 24.0 * scale[0],
              31.0 * scale[1], 21.0 * scale[0], 63.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 30.0 * scale[1], 1.0 * scale[0],
              40.0 * scale[1], 12.0 * scale[0], 40.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0], -
              6.0 * scale[1], 20.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], -7.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 12.0 * scale[0], -6.0 * scale[1])
    Curveto_r(5.0 * scale[0], 5.0 * scale[1], 1.0 * scale[0],
              16.0 * scale[1], -8.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 25.0 * scale[1], -21.0 * scale[0],
              35.0 * scale[1], 2.0 * scale[0], 23.0 * scale[1])
    Curveto_r(14.0 * scale[0], -8.0 * scale[1], 26.0 *
              scale[0], -4.0 * scale[1], 52.0 * scale[0], 15.0 * scale[1])
    Curveto_r(25.0 * scale[0], 19.0 * scale[1], 42.0 * scale[0],
              24.0 * scale[1], 64.0 * scale[0], 20.0 * scale[1])
    Curveto_r(20.0 * scale[0], -4.0 * scale[1], 25.0 *
              scale[0], -3.0 * scale[1], 16.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 7.0 * scale[1], -10.0 * scale[0],
              10.0 * scale[1], 5.0 * scale[0], 13.0 * scale[1])
    Curveto_r(10.0 * scale[0], 2.0 * scale[1], -79.0 * scale[0],
              4.0 * scale[1], -198.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-119.0 * scale[0], 0.0 * scale[1], -219.0 *
              scale[0], -2.0 * scale[1], -222.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(188.0 * scale[0], -28.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], 2.0 * scale[0], -
              12.0 * scale[1], -4.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0],
              10.0 * scale[1], -10.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], 7.0 * scale[0],
              11.0 * scale[1], 14.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto_r(46.0 * scale[0], -56.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], -18.0 *
              scale[0], -14.0 * scale[1], -28.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 23.0 * scale[1], -10.0 * scale[0],
              24.0 * scale[1], 8.0 * scale[0], 13.0 * scale[1])
    Curveto_r(11.0 * scale[0], -7.0 * scale[1], 20.0 * scale[0], -
              16.0 * scale[1], 20.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(608.0 * scale[0], 1003.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(683.0 * scale[0], 1002.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -4.0 * scale[1], -15.0 * scale[0], -
              20.0 * scale[1], -18.0 * scale[0], -35.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -32.0 * scale[1], -12.0 *
              scale[0], -33.0 * scale[1], -39.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 9.0 * scale[1], -6.0 * scale[0],
              0.0 * scale[1], 12.0 * scale[0], -22.0 * scale[1])
    Curveto_r(18.0 * scale[0], -21.0 * scale[1], 31.0 * scale[0], -
              44.0 * scale[1], 28.0 * scale[0], -51.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -10.0 * scale[1], 1.0 *
              scale[0], -10.0 * scale[1], 22.0 * scale[0], 1.0 * scale[1])
    Curveto_r(33.0 * scale[0], 17.0 * scale[1], 53.0 * scale[0],
              18.0 * scale[1], 51.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -24.0 * scale[1], 1.0 * scale[0], -
              41.0 * scale[1], 8.0 * scale[0], -35.0 * scale[1])
    Curveto_r(10.0 * scale[0], 10.0 * scale[1], 43.0 * scale[0], -
              24.0 * scale[1], 43.0 * scale[0], -44.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 5.0 * scale[0], -
              21.0 * scale[1], 10.0 * scale[0], -24.0 * scale[1])
    Curveto_r(12.0 * scale[0], -8.0 * scale[1], 52.0 * scale[0],
              4.0 * scale[1], 46.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 4.0 * scale[1], 23.0 * scale[0],
              8.0 * scale[1], 57.0 * scale[0], 10.0 * scale[1])
    Lineto_r(60.0 * scale[0], 3.0 * scale[1])
    Lineto_r(-7.0 * scale[0], -133.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -73.0 * scale[1], -8.0 * scale[0], -
              142.0 * scale[1], -9.0 * scale[0], -153.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -33.0 * scale[1], -21.0 *
              scale[0], -36.0 * scale[1], -33.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 28.0 * scale[1], -58.0 * scale[0],
              62.0 * scale[1], -116.0 * scale[0], 88.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 6.0 * scale[1], -28.0 * scale[0],
              8.0 * scale[1], -28.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 19.0 * scale[0], -
              16.0 * scale[1], 42.0 * scale[0], -27.0 * scale[1])
    Curveto_r(42.0 * scale[0], -19.0 * scale[1], 98.0 * scale[0], -
              83.0 * scale[1], 98.0 * scale[0], -113.0 * scale[1])
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], 2.0 * scale[0], -
              13.0 * scale[1], 9.0 * scale[0], -3.0 * scale[1])
    Curveto_r(6.0 * scale[0], 10.0 * scale[1], 12.0 * scale[0],
              5.0 * scale[1], 21.0 * scale[0], -18.0 * scale[1])
    Curveto_r(7.0 * scale[0], -17.0 * scale[1], 15.0 * scale[0], -
              29.0 * scale[1], 17.0 * scale[0], -26.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 7.0 * scale[0],
              93.0 * scale[1], 10.0 * scale[0], 200.0 * scale[1])
    Lineto_r(5.0 * scale[0], 196.0 * scale[1])
    Lineto_r(-29.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 1.0 * scale[1], -25.0 * scale[0],
              2.0 * scale[1], -10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(9.0 * scale[0], 5.0 * scale[1], 17.0 * scale[0],
              18.0 * scale[1], 16.0 * scale[0], 27.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -2.0 * scale[0],
              13.0 * scale[1], -9.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -11.0 * scale[1], -9.0 * scale[0], -
              17.0 * scale[1], -9.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 4.0 * scale[1], -15.0 * scale[0],
              3.0 * scale[1], -31.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-25.0 * scale[0], -7.0 * scale[1], -32.0 *
              scale[0], -5.0 * scale[1], -41.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 12.0 * scale[1], -16.0 * scale[0],
              18.0 * scale[1], -24.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -3.0 * scale[1], -12.0 * scale[0],
              0.0 * scale[1], -11.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -3.0 * scale[0],
              12.0 * scale[1], -9.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              4.0 * scale[1], -7.0 * scale[0], -9.0 * scale[1])
    Curveto_r(2.0 * scale[0], -5.0 * scale[1], -4.0 * scale[0], -
              4.0 * scale[1], -12.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 7.0 * scale[1], -19.0 * scale[0],
              10.0 * scale[1], -24.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -2.0 * scale[1], -9.0 * scale[0],
              14.0 * scale[1], -11.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 30.0 * scale[1], 3.0 * scale[0],
              46.0 * scale[1], 19.0 * scale[0], 60.0 * scale[1])
    Curveto_r(11.0 * scale[0], 10.0 * scale[1], 25.0 * scale[0],
              16.0 * scale[1], 30.0 * scale[0], 13.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 10.0 *
              scale[0], -1.0 * scale[1], 10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], -118.0 * scale[0],
              15.0 * scale[1], -137.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto_r(-6.0 * scale[0], -79.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -22.0 * scale[1], -1.0 * scale[0], -
              24.0 * scale[1], -8.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 9.0 * scale[1], -7.0 * scale[0],
              22.0 * scale[1], -4.0 * scale[0], 27.0 * scale[1])
    Curveto_r(9.0 * scale[0], 14.0 * scale[1], 10.0 * scale[0],
              13.0 * scale[1], 12.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(863.0 * scale[0], 996.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 8.0 * scale[0], -
              13.0 * scale[1], 20.0 * scale[0], -10.0 * scale[1])
    Curveto_r(11.0 * scale[0], 2.0 * scale[1], 27.0 * scale[0], -
              1.0 * scale[1], 36.0 * scale[0], -7.0 * scale[1])
    Curveto_r(14.0 * scale[0], -9.0 * scale[1], 14.0 * scale[0], -
              10.0 * scale[1], -1.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 3.0 * scale[1], -20.0 * scale[0],
              0.0 * scale[1], -24.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -3.0 *
              scale[0], -8.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 12.0 * scale[0],
              1.0 * scale[1], 14.0 * scale[0], -6.0 * scale[1])
    Curveto_r(2.0 * scale[0], -6.0 * scale[1], 14.0 * scale[0],
              3.0 * scale[1], 27.0 * scale[0], 20.0 * scale[1])
    Lineto_r(22.0 * scale[0], 32.0 * scale[1])
    Lineto_r(-49.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-35.0 * scale[0], 0.0 * scale[1], -49.0 * scale[0], -
              4.0 * scale[1], -49.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(349.0 * scale[0], 963.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -21.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(771.0 * scale[0], 944.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(116.0 * scale[0], 895.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -26.0 * scale[1], -7.0 *
              scale[0], -32.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(6.0 * scale[0], 10.0 * scale[1], 9.0 * scale[0],
              21.0 * scale[1], 6.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 3.0 * scale[1], -7.0 * scale[0], -
              2.0 * scale[1], -11.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(290.0 * scale[0], 890.0 * scale[1], x, y)
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
    Moveto(5.0 * scale[0], 869.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -13.0 * scale[1], 7.0 * scale[0], -
              34.0 * scale[1], 8.0 * scale[0], -46.0 * scale[1])
    Curveto_r(1.0 * scale[0], -14.0 * scale[1], 5.0 * scale[0], -
              19.0 * scale[1], 12.0 * scale[0], -13.0 * scale[1])
    Curveto_r(5.0 * scale[0], 4.0 * scale[1], 36.0 * scale[0],
              15.0 * scale[1], 68.0 * scale[0], 23.0 * scale[1])
    Curveto_r(33.0 * scale[0], 9.0 * scale[1], 62.0 * scale[0],
              19.0 * scale[1], 65.0 * scale[0], 23.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -3.0 * scale[0],
              3.0 * scale[1], -15.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -4.0 * scale[1], -28.0 *
              scale[0], -4.0 * scale[1], -35.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 11.0 * scale[1], -39.0 * scale[0],
              13.0 * scale[1], -33.0 * scale[0], 3.0 * scale[1])
    Curveto_r(6.0 * scale[0], -9.0 * scale[1], -25.0 * scale[0], -
              23.0 * scale[1], -33.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], 0.0 * scale[0],
              5.0 * scale[1], 6.0 * scale[0], 5.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              5.0 * scale[1], 12.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -7.0 * scale[0],
              7.0 * scale[1], -21.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -6.0 * scale[1], -19.0 *
              scale[0], -7.0 * scale[1], -15.0 * scale[0], -1.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], -1.0 * scale[0],
              16.0 * scale[1], -10.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 11.0 * scale[1], -14.0 * scale[0],
              9.0 * scale[1], -9.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(522.0 * scale[0], 834.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-18.0 * scale[0], -7.0 * scale[1], -32.0 * scale[0], -
              17.0 * scale[1], -32.0 * scale[0], -22.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -22.0 * scale[0], -
              12.0 * scale[1], -48.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-35.0 * scale[0], -4.0 * scale[1], -56.0 * scale[0], -
              14.0 * scale[1], -74.0 * scale[0], -34.0 * scale[1])
    Curveto_r(-25.0 * scale[0], -26.0 * scale[1], -43.0 *
              scale[0], -92.0 * scale[1], -26.0 * scale[0], -92.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0], -
              4.0 * scale[1], 3.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 4.0 * scale[0], -
              12.0 * scale[1], 15.0 * scale[0], -16.0 * scale[1])
    Curveto_r(11.0 * scale[0], -4.0 * scale[1], 18.0 * scale[0], -
              11.0 * scale[1], 15.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -22.0 * scale[1], 24.0 * scale[0],
              5.0 * scale[1], 44.0 * scale[0], 31.0 * scale[1])
    Curveto_r(12.0 * scale[0], 17.0 * scale[1], 31.0 * scale[0],
              30.0 * scale[1], 44.0 * scale[0], 30.0 * scale[1])
    Curveto_r(21.0 * scale[0], 1.0 * scale[1], 21.0 * scale[0],
              1.0 * scale[1], 3.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 8.0 * scale[1], -25.0 * scale[0],
              8.0 * scale[1], -42.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -8.0 * scale[1], -24.0 *
              scale[0], -8.0 * scale[1], -24.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], -6.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -7.0 * scale[1], -21.0 * scale[0],
              11.0 * scale[1], -5.0 * scale[0], 21.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 8.0 * scale[0],
              11.0 * scale[1], 4.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], 10.0 * scale[0],
              16.0 * scale[1], 30.0 * scale[0], 24.0 * scale[1])
    Curveto_r(40.0 * scale[0], 17.0 * scale[1], 88.0 * scale[0],
              11.0 * scale[1], 128.0 * scale[0], -16.0 * scale[1])
    Curveto_r(32.0 * scale[0], -23.0 * scale[1], 38.0 *
              scale[0], -23.0 * scale[1], 38.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 2.0 * scale[0],
              15.0 * scale[1], 5.0 * scale[0], 15.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 55.0 * scale[0], -
              24.0 * scale[1], 55.0 * scale[0], -32.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0], -
              6.0 * scale[1], 10.0 * scale[0], -3.0 * scale[1])
    Curveto_r(11.0 * scale[0], 7.0 * scale[1], -28.0 * scale[0],
              64.0 * scale[1], -45.0 * scale[0], 64.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 1.0 * scale[1], -19.0 * scale[0],
              12.0 * scale[1], -30.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 22.0 * scale[1], -23.0 * scale[0],
              23.0 * scale[1], -53.0 * scale[0], 10.0 * scale[1])
    te.end_fill()
    Moveto(752.0 * scale[0], 820.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(182.0 * scale[0], 730.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(695.0 * scale[0], 730.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -12.0 * scale[1], -25.0 *
              scale[0], -18.0 * scale[1], -34.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 4.0 * scale[1], -8.0 *
              scale[0], -1.0 * scale[1], 5.0 * scale[0], -14.0 * scale[1])
    Curveto_r(12.0 * scale[0], -11.0 * scale[1], 24.0 * scale[0], -
              26.0 * scale[1], 27.0 * scale[0], -33.0 * scale[1])
    Curveto_r(4.0 * scale[0], -10.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 17.0 * scale[0], 2.0 * scale[1])
    Curveto_r(9.0 * scale[0], 12.0 * scale[1], 10.0 * scale[0],
              12.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -11.0 * scale[1], 1.0 * scale[0], -
              29.0 * scale[1], 9.0 * scale[0], -40.0 * scale[1])
    Curveto_r(14.0 * scale[0], -19.0 * scale[1], 14.0 *
              scale[0], -19.0 * scale[1], 15.0 * scale[0], 1.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], -9.0 * scale[0],
              38.0 * scale[1], -20.0 * scale[0], 59.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 29.0 * scale[1], -18.0 * scale[0],
              41.0 * scale[1], -9.0 * scale[0], 52.0 * scale[1])
    Curveto_r(18.0 * scale[0], 22.0 * scale[1], 4.0 * scale[0],
              17.0 * scale[1], -16.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(155.0 * scale[0], 709.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0], -
              12.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 17.0 * scale[1], 1.0 * scale[0],
              20.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(135.0 * scale[0], 670.0 * scale[1], x, y)
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
    Moveto(453.0 * scale[0], 655.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              12.0 * scale[1], 9.0 * scale[0], -9.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 6.0 * scale[0],
              10.0 * scale[1], 3.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 13.0 * scale[1], -12.0 * scale[0],
              11.0 * scale[1], -12.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(122.0 * scale[0], 610.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 2.0 * scale[0], -
              27.0 * scale[1], 5.0 * scale[0], -17.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              25.0 * scale[1], 0.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(271.0 * scale[0], 606.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -18.0 * scale[1], -21.0 *
              scale[0], -37.0 * scale[1], -21.0 * scale[0], -41.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], -9.0 * scale[0], -
              18.0 * scale[1], -19.0 * scale[0], -32.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -13.0 * scale[1], -17.0 *
              scale[0], -31.0 * scale[1], -14.0 * scale[0], -40.0 * scale[1])
    Curveto_r(5.0 * scale[0], -12.0 * scale[1], 2.0 * scale[0], -
              14.0 * scale[1], -8.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 4.0 * scale[1], -5.0 * scale[0],
              0.0 * scale[1], 5.0 * scale[0], -8.0 * scale[1])
    Curveto_r(11.0 * scale[0], -9.0 * scale[1], 25.0 * scale[0], -
              16.0 * scale[1], 30.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 5.0 * scale[0],
              4.0 * scale[1], -2.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 6.0 * scale[1], -8.0 * scale[0],
              20.0 * scale[1], 16.0 * scale[0], 68.0 * scale[1])
    Curveto_r(17.0 * scale[0], 32.0 * scale[1], 36.0 * scale[0],
              64.0 * scale[1], 44.0 * scale[0], 70.0 * scale[1])
    Curveto_r(20.0 * scale[0], 17.0 * scale[1], 41.0 * scale[0], -
              5.0 * scale[1], 60.0 * scale[0], -62.0 * scale[1])
    Curveto_r(11.0 * scale[0], -31.0 * scale[1], 17.0 * scale[0], -
              41.0 * scale[1], 17.0 * scale[0], -27.0 * scale[1])
    Curveto_r(1.0 * scale[0], 14.0 * scale[1], 5.0 * scale[0],
              20.0 * scale[1], 11.0 * scale[0], 17.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 10.0 * scale[0], -
              14.0 * scale[1], 8.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -10.0 * scale[1], 1.0 * scale[0], -
              23.0 * scale[1], 5.0 * scale[0], -29.0 * scale[1])
    Curveto_r(5.0 * scale[0], -7.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 0.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0],
              6.0 * scale[1], -22.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 10.0 * scale[1], -11.0 * scale[0],
              8.0 * scale[1], -2.0 * scale[0], -11.0 * scale[1])
    Curveto_r(7.0 * scale[0], -12.0 * scale[1], 10.0 * scale[0], -
              26.0 * scale[1], 7.0 * scale[0], -30.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -4.0 * scale[1], 4.0 * scale[0], -
              8.0 * scale[1], 14.0 * scale[0], -9.0 * scale[1])
    Curveto_r(10.0 * scale[0], -1.0 * scale[1], 20.0 * scale[0],
              7.0 * scale[1], 23.0 * scale[0], 18.0 * scale[1])
    Curveto_r(3.0 * scale[0], 11.0 * scale[1], 14.0 * scale[0],
              19.0 * scale[1], 29.0 * scale[0], 20.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 18.0 * scale[0],
              3.0 * scale[1], 12.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 6.0 * scale[1], 8.0 * scale[0],
              100.0 * scale[1], 24.0 * scale[0], 97.0 * scale[1])
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 9.0 * scale[0],
              4.0 * scale[1], 5.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 11.0 * scale[1], -8.0 * scale[0],
              12.0 * scale[1], -13.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -13.0 * scale[1], -16.0 *
              scale[0], -13.0 * scale[1], -45.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 6.0 * scale[1], -37.0 * scale[0],
              12.0 * scale[1], -58.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 2.0 * scale[1], -44.0 * scale[0],
              10.0 * scale[1], -53.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 23.0 * scale[1], -30.0 * scale[0],
              20.0 * scale[1], -53.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(466.0 * scale[0], 619.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -4.0 * scale[1], -2.0 * scale[0], -
              10.0 * scale[1], -8.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -4.0 * scale[1], -9.0 *
              scale[0], -6.0 * scale[1], -2.0 * scale[0], -6.0 * scale[1])
    Curveto_r(6.0 * scale[0], -1.0 * scale[1], 17.0 * scale[0],
              5.0 * scale[1], 23.0 * scale[0], 12.0 * scale[1])
    Curveto_r(8.0 * scale[0], 10.0 * scale[1], 7.0 * scale[0],
              14.0 * scale[1], -4.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -9.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(120.0 * scale[0], 510.0 * scale[1], x, y)
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
    Moveto(717.0 * scale[0], 494.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              24.0 * scale[1], 23.0 * scale[0], -24.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0],
              5.0 * scale[1], 14.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 15.0 * scale[1], -26.0 * scale[0],
              20.0 * scale[1], -37.0 * scale[0], 9.0 * scale[1])
    te.end_fill()
    Moveto(679.0 * scale[0], 444.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -14.0 * scale[1], -23.0 *
              scale[0], -29.0 * scale[1], -22.0 * scale[0], -32.0 * scale[1])
    Curveto_r(1.0 * scale[0], -4.0 * scale[1], -6.0 * scale[0], -
              6.0 * scale[1], -15.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 2.0 * scale[1], -15.0 * scale[0],
              1.0 * scale[1], -2.0 * scale[0], -8.0 * scale[1])
    Curveto_r(13.0 * scale[0], -9.0 * scale[1], 13.0 * scale[0], -
              11.0 * scale[1], 0.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -11.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 39.0 * scale[0],
              39.0 * scale[1], 35.0 * scale[0], 53.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 4.0 * scale[1], 4.0 * scale[0],
              7.0 * scale[1], 12.0 * scale[0], 7.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0],
              9.0 * scale[1], 19.0 * scale[0], 20.0 * scale[1])
    Curveto_r(7.0 * scale[0], 26.0 * scale[1], 5.0 * scale[0],
              25.0 * scale[1], -24.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(5.0 * scale[0], 300.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -164.0 * scale[1], 14.0 * scale[0], -
              225.0 * scale[1], 16.0 * scale[0], -114.0 * scale[1])
    Curveto_r(3.0 * scale[0], 135.0 * scale[1], -3.0 * scale[0],
              260.0 * scale[1], -12.0 * scale[0], 269.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 6.0 * scale[1], -7.0 * scale[0], -
              52.0 * scale[1], -4.0 * scale[0], -155.0 * scale[1])
    te.end_fill()
    Moveto(550.0 * scale[0], 430.0 * scale[1], x, y)
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
    Moveto(140.0 * scale[0], 419.0 * scale[1], x, y)
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
    Moveto(574.0 * scale[0], 408.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], -3.0 *
              scale[0], -8.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(7.0 * scale[0], 4.0 * scale[1], 12.0 * scale[0],
              2.0 * scale[1], 12.0 * scale[0], -3.0 * scale[1])
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], -17.0 * scale[0], -
              14.0 * scale[1], -25.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 13.0 * scale[1], -22.0 * scale[0],
              5.0 * scale[1], -35.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -17.0 * scale[1], -6.0 * scale[0], -
              18.0 * scale[1], 23.0 * scale[0], -11.0 * scale[1])
    Curveto_r(66.0 * scale[0], 16.0 * scale[1], 84.0 * scale[0],
              31.0 * scale[1], 51.0 * scale[0], 44.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 8.0 * scale[1], -22.0 * scale[0],
              8.0 * scale[1], -30.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(156.0 * scale[0], 393.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(796.0 * scale[0], 397.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0], -
              15.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 0.0 * scale[0],
              11.0 * scale[1], -7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              8.0 * scale[1], -5.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(165.0 * scale[0], 370.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -8.0 * scale[1], -2.0 * scale[0], -
              17.0 * scale[1], 7.0 * scale[0], -24.0 * scale[1])
    Curveto_r(19.0 * scale[0], -14.0 * scale[1], 20.0 *
              scale[0], -49.0 * scale[1], 1.0 * scale[0], -42.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -11.0 * scale[0],
              2.0 * scale[1], -8.0 * scale[0], -3.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              12.0 * scale[1], -4.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -4.0 * scale[1], -12.0 *
              scale[0], -2.0 * scale[1], -16.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], -11.0 * scale[0],
              8.0 * scale[1], -16.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -7.0 * scale[1], -59.0 * scale[0], -
              107.0 * scale[1], -54.0 * scale[0], -113.0 * scale[1])
    Curveto_r(2.0 * scale[0], -2.0 * scale[1], 25.0 * scale[0],
              16.0 * scale[1], 50.0 * scale[0], 40.0 * scale[1])
    Curveto_r(25.0 * scale[0], 24.0 * scale[1], 62.0 * scale[0],
              51.0 * scale[1], 82.0 * scale[0], 60.0 * scale[1])
    Curveto_r(29.0 * scale[0], 13.0 * scale[1], 33.0 * scale[0],
              18.0 * scale[1], 17.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 3.0 * scale[1], -15.0 * scale[0],
              6.0 * scale[1], 10.0 * scale[0], 19.0 * scale[1])
    Curveto_r(22.0 * scale[0], 12.0 * scale[1], 25.0 * scale[0],
              17.0 * scale[1], 13.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 3.0 * scale[1], -18.0 * scale[0], -
              1.0 * scale[1], -21.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -13.0 * scale[1], -9.0 * scale[0], -
              13.0 * scale[1], -22.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 7.0 * scale[1], -19.0 * scale[0],
              22.0 * scale[1], -23.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 15.0 * scale[1], -10.0 * scale[0],
              16.0 * scale[1], -16.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(810.0 * scale[0], 365.0 * scale[1], x, y)
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
    Moveto(479.0 * scale[0], 343.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -17.0 * scale[1], -13.0 *
              scale[0], -17.0 * scale[1], 6.0 * scale[0], -3.0 * scale[1])
    Curveto_r(11.0 * scale[0], 8.0 * scale[1], 22.0 * scale[0],
              16.0 * scale[1], 24.0 * scale[0], 17.0 * scale[1])
    Curveto_r(2.0 * scale[0], 2.0 * scale[1], 0.0 * scale[0],
              3.0 * scale[1], -6.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0], -
              8.0 * scale[1], -24.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(596.0 * scale[0], 341.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -13.0 * scale[1], -15.0 *
              scale[0], -27.0 * scale[1], -10.0 * scale[0], -45.0 * scale[1])
    Lineto_r(6.0 * scale[0], -26.0 * scale[1])
    Lineto_r(-48.0 * scale[0], 27.0 * scale[1])
    Lineto_r(-49.0 * scale[0], 27.0 * scale[1])
    Lineto_r(44.0 * scale[0], -42.0 * scale[1])
    Lineto_r(44.0 * scale[0], -41.0 * scale[1])
    Lineto_r(-8.0 * scale[0], -63.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -113.0 * scale[1], -12.0 *
              scale[0], -158.0 * scale[1], 7.0 * scale[0], -158.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0], -
              5.0 * scale[1], 23.0 * scale[0], -10.0 * scale[1])
    Curveto_r(3.0 * scale[0], -6.0 * scale[1], 25.0 * scale[0], -
              8.0 * scale[1], 48.0 * scale[0], -4.0 * scale[1])
    Curveto_r(109.0 * scale[0], 14.0 * scale[1], 106.0 * scale[0],
              12.0 * scale[1], 117.0 * scale[0], 52.0 * scale[1])
    Curveto_r(5.0 * scale[0], 20.0 * scale[1], 10.0 * scale[0],
              52.0 * scale[1], 10.0 * scale[0], 71.0 * scale[1])
    Lineto_r(0.0 * scale[0], 33.0 * scale[1])
    Lineto_r(21.0 * scale[0], -23.0 * scale[1])
    Lineto_r(21.0 * scale[0], -24.0 * scale[1])
    Lineto_r(-16.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 13.0 * scale[1], -16.0 * scale[0],
              33.0 * scale[1], -16.0 * scale[0], 43.0 * scale[1])
    Curveto_r(0.0 * scale[0], 16.0 * scale[1], -3.0 * scale[0],
              17.0 * scale[1], -15.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -7.0 * scale[1], -15.0 * scale[0], -
              23.0 * scale[1], -15.0 * scale[0], -37.0 * scale[1])
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], -11.0 * scale[0], -
              45.0 * scale[1], -25.0 * scale[0], -71.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -26.0 * scale[1], -25.0 *
              scale[0], -41.0 * scale[1], -25.0 * scale[0], -33.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], -10.0 * scale[0],
              7.0 * scale[1], -36.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-54.0 * scale[0], -32.0 * scale[1], -60.0 *
              scale[0], -29.0 * scale[1], -64.0 * scale[0], 42.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 112.0 * scale[1], -5.0 * scale[0],
              188.0 * scale[1], 5.0 * scale[0], 195.0 * scale[1])
    Curveto_r(12.0 * scale[0], 9.0 * scale[1], 18.0 * scale[0],
              82.0 * scale[1], 7.0 * scale[0], 82.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0], -
              8.0 * scale[1], -26.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(941.0 * scale[0], 344.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(382.0 * scale[0], 295.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -7.0 * scale[1], -19.0 * scale[0], -
              16.0 * scale[1], -14.0 * scale[0], -19.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 17.0 * scale[0],
              0.0 * scale[1], 25.0 * scale[0], 8.0 * scale[1])
    Curveto_r(8.0 * scale[0], 8.0 * scale[1], 18.0 * scale[0],
              12.0 * scale[1], 22.0 * scale[0], 8.0 * scale[1])
    Curveto_r(5.0 * scale[0], -4.0 * scale[1], 5.0 *
              scale[0], -1.0 * scale[1], 1.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], -8.0 * scale[0],
              12.0 * scale[1], -9.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -1.0 * scale[1], -13.0 * scale[0], -
              7.0 * scale[1], -25.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(841.0 * scale[0], 254.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -33.0 * scale[1], 9.0 * scale[0], -
              46.0 * scale[1], 44.0 * scale[0], -57.0 * scale[1])
    Curveto_r(19.0 * scale[0], -7.0 * scale[1], 19.0 *
              scale[0], -6.0 * scale[1], -1.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 10.0 * scale[1], -26.0 * scale[0],
              31.0 * scale[1], -32.0 * scale[0], 47.0 * scale[1])
    Lineto_r(-10.0 * scale[0], 30.0 * scale[1])
    Lineto_r(-1.0 * scale[0], -31.0 * scale[1])
    te.end_fill()
    Moveto(885.0 * scale[0], 230.0 * scale[1], x, y)
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
    Moveto(216.0 * scale[0], 232.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 7.0 * scale[0], -
              18.0 * scale[1], 22.0 * scale[0], -27.0 * scale[1])
    Lineto_r(27.0 * scale[0], -18.0 * scale[1])
    Lineto_r(-20.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 13.0 * scale[1], -21.0 * scale[0],
              25.0 * scale[1], -21.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 2.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -8.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(349.0 * scale[0], 223.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(16.0 * scale[0], 13.0 * scale[1], 21.0 * scale[0],
              21.0 * scale[1], 13.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              8.0 * scale[1], -17.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(925.0 * scale[0], 160.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(21.0 * scale[0], -24.0 * scale[1], 26.0 *
              scale[0], -25.0 * scale[1], 19.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], -13.0 * scale[0],
              17.0 * scale[1], -22.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 5.0 * scale[1], -13.0 * scale[0],
              2.0 * scale[1], 3.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(261.0 * scale[0], 114.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(825.0 * scale[0], 97.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -11.0 * scale[1], 8.0 * scale[0], -
              31.0 * scale[1], 11.0 * scale[0], -45.0 * scale[1])
    Curveto_r(11.0 * scale[0], -45.0 * scale[1], 23.0 * scale[0], -
              53.0 * scale[1], 79.0 * scale[0], -51.0 * scale[1])
    Curveto_r(50.0 * scale[0], 2.0 * scale[1], 51.0 * scale[0],
              3.0 * scale[1], 52.0 * scale[0], 33.0 * scale[1])
    Curveto_r(1.0 * scale[0], 18.0 * scale[1], -1.0 * scale[0],
              23.0 * scale[1], -4.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -32.0 * scale[1], -18.0 * scale[0], -
              37.0 * scale[1], -57.0 * scale[0], -30.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 5.0 * scale[1], -36.0 * scale[0],
              13.0 * scale[1], -36.0 * scale[0], 23.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -3.0 * scale[0],
              12.0 * scale[1], -7.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], -15.0 * scale[0],
              10.0 * scale[1], -25.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 21.0 * scale[1], -16.0 * scale[0],
              30.0 * scale[1], -13.0 * scale[0], 20.0 * scale[1])
    te.end_fill()
    Moveto(0.0 * scale[0], 75.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 2.0 * scale[0], -
              15.0 * scale[1], 4.0 * scale[0], -15.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 6.0 * scale[0],
              7.0 * scale[1], 10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], 1.0 * scale[0],
              15.0 * scale[1], -4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              7.0 * scale[1], -10.0 * scale[0], -15.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#976024')
    te.end_fill()
    Moveto(73.0 * scale[0], 1393.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(26.0 * scale[0], -2.0 * scale[1], 67.0 *
              scale[0], -2.0 * scale[1], 90.0 * scale[0], 0.0 * scale[1])
    Curveto_r(23.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              3.0 * scale[1], -48.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-50.0 * scale[0], 0.0 * scale[1], -68.0 *
              scale[0], -1.0 * scale[1], -42.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(233.0 * scale[0], 1393.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(284.0 * scale[0], 1390.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -4.0 * scale[1], -20.0 * scale[0], -
              10.0 * scale[1], -34.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-23.0 * scale[0], -4.0 * scale[1], -22.0 *
              scale[0], -4.0 * scale[1], 5.0 * scale[0], -5.0 * scale[1])
    Curveto_r(33.0 * scale[0], -2.0 * scale[1], 63.0 * scale[0],
              12.0 * scale[1], 48.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -14.0 * scale[0],
              2.0 * scale[1], -19.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(430.0 * scale[0], 1390.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-44.0 * scale[0], -7.0 * scale[1], -44.0 *
              scale[0], -7.0 * scale[1], 18.0 * scale[0], -8.0 * scale[1])
    Curveto_r(34.0 * scale[0], -1.0 * scale[1], 62.0 * scale[0],
              2.0 * scale[1], 62.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], -22.0 * scale[0],
              10.0 * scale[1], -80.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(553.0 * scale[0], 1385.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              12.0 * scale[1], 9.0 * scale[0], -9.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], 8.0 * scale[0],
              1.0 * scale[1], 8.0 * scale[0], -3.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 79.0 * scale[0], -
              47.0 * scale[1], 87.0 * scale[0], -40.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -15.0 * scale[0],
              15.0 * scale[1], -39.0 * scale[0], 26.0 * scale[1])
    Lineto_r(-43.0 * scale[0], 20.0 * scale[1])
    Lineto_r(65.0 * scale[0], 1.0 * scale[1])
    Curveto_r(80.0 * scale[0], 2.0 * scale[1], 54.0 * scale[0],
              18.0 * scale[1], -31.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-42.0 * scale[0], 1.0 * scale[1], -56.0 * scale[0], -
              2.0 * scale[1], -56.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(355.0 * scale[0], 1380.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -10.0 * scale[1], 4.0 * scale[0], -
              12.0 * scale[1], -11.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 6.0 * scale[1], -17.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    Curveto_r(9.0 * scale[0], -9.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 23.0 * scale[0], -2.0 * scale[1])
    Curveto_r(8.0 * scale[0], 8.0 * scale[1], 7.0 * scale[0],
              13.0 * scale[1], -2.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 6.0 * scale[1], -10.0 * scale[0],
              4.0 * scale[1], -4.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(100.0 * scale[0], 1367.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-46.0 * scale[0], -21.0 * scale[1], -49.0 *
              scale[0], -54.0 * scale[1], -3.0 * scale[0], -42.0 * scale[1])
    Curveto_r(16.0 * scale[0], 4.0 * scale[1], 22.0 * scale[0],
              2.0 * scale[1], 18.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -18.0 * scale[1], 14.0 *
              scale[0], -11.0 * scale[1], 35.0 * scale[0], 10.0 * scale[1])
    Curveto_r(12.0 * scale[0], 12.0 * scale[1], 26.0 * scale[0],
              20.0 * scale[1], 33.0 * scale[0], 19.0 * scale[1])
    Curveto_r(7.0 * scale[0], -1.0 * scale[1], 22.0 *
              scale[0], -1.0 * scale[1], 35.0 * scale[0], 0.0 * scale[1])
    Curveto_r(22.0 * scale[0], 1.0 * scale[1], 23.0 * scale[0],
              2.0 * scale[1], 6.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 13.0 * scale[1], -19.0 * scale[0],
              14.0 * scale[1], -22.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -6.0 * scale[1], -8.0 * scale[0], -
              12.0 * scale[1], -13.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0],
              5.0 * scale[1], -4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 14.0 * scale[1], -54.0 * scale[0],
              12.0 * scale[1], -85.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(765.0 * scale[0], 1370.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-20.0 * scale[0], -8.0 * scale[1], -20.0 *
              scale[0], -9.0 * scale[1], 1.0 * scale[0], -9.0 * scale[1])
    Curveto_r(11.0 * scale[0], -1.0 * scale[1], 29.0 * scale[0], -
              8.0 * scale[1], 40.0 * scale[0], -16.0 * scale[1])
    Curveto_r(18.0 * scale[0], -14.0 * scale[1], 18.0 * scale[0], -
              14.0 * scale[1], -6.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-33.0 * scale[0], -3.0 * scale[1], -79.0 * scale[0],
              0.0 * scale[1], -107.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 3.0 * scale[1], -23.0 * scale[0],
              1.0 * scale[1], -23.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 18.0 * scale[0], -
              10.0 * scale[1], 39.0 * scale[0], -10.0 * scale[1])
    Curveto_r(22.0 * scale[0], 0.0 * scale[1], 51.0 * scale[0], -
              4.0 * scale[1], 65.0 * scale[0], -9.0 * scale[1])
    Curveto_r(18.0 * scale[0], -7.0 * scale[1], 28.0 *
              scale[0], -6.0 * scale[1], 36.0 * scale[0], 5.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 22.0 * scale[0],
              14.0 * scale[1], 34.0 * scale[0], 15.0 * scale[1])
    Curveto_r(21.0 * scale[0], 0.0 * scale[1], 21.0 * scale[0],
              1.0 * scale[1], 1.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              7.0 * scale[1], 44.0 * scale[0], 3.0 * scale[1])
    Curveto_r(59.0 * scale[0], -5.0 * scale[1], 63.0 *
              scale[0], -5.0 * scale[1], 49.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 18.0 * scale[1], -142.0 * scale[0],
              30.0 * scale[1], -173.0 * scale[0], 16.0 * scale[1])
    te.end_fill()
    Moveto(280.0 * scale[0], 1360.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -8.0 * scale[1], -10.0 *
              scale[0], -10.0 * scale[1], 8.0 * scale[0], -10.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0],
              4.0 * scale[1], 17.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 12.0 * scale[1], -6.0 * scale[0],
              12.0 * scale[1], -25.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(375.0 * scale[0], 1361.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -5.0 * scale[1], 8.0 * scale[0], -
              11.0 * scale[1], 23.0 * scale[0], -14.0 * scale[1])
    Curveto_r(35.0 * scale[0], -7.0 * scale[1], 38.0 *
              scale[0], -3.0 * scale[1], 7.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 6.0 * scale[1], -27.0 * scale[0],
              7.0 * scale[1], -30.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(20.0 * scale[0], 1331.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 5.0 * scale[0], -
              18.0 * scale[1], 18.0 * scale[0], -14.0 * scale[1])
    Curveto_r(24.0 * scale[0], 6.0 * scale[1], 24.0 * scale[0],
              33.0 * scale[1], 0.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -18.0 * scale[0], -
              7.0 * scale[1], -18.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(463.0 * scale[0], 1333.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(165.0 * scale[0], 1320.0 * scale[1], x, y)
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
    Moveto(190.0 * scale[0], 1299.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -8.0 * scale[1], -12.0 *
              scale[0], -12.0 * scale[1], -2.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 10.0 * scale[0], -
              9.0 * scale[1], 6.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              10.0 * scale[1], 23.0 * scale[0], -10.0 * scale[1])
    Curveto_r(15.0 * scale[0], -1.0 * scale[1], 38.0 *
              scale[0], -3.0 * scale[1], 50.0 * scale[0], -4.0 * scale[1])
    Curveto_r(12.0 * scale[0], -1.0 * scale[1], 20.0 * scale[0],
              1.0 * scale[1], 18.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], 12.0 * scale[0],
              10.0 * scale[1], 32.0 * scale[0], 12.0 * scale[1])
    Curveto_r(25.0 * scale[0], 3.0 * scale[1], 18.0 * scale[0],
              4.0 * scale[1], -22.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-33.0 * scale[0], 0.0 * scale[1], -69.0 * scale[0],
              4.0 * scale[1], -80.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 8.0 * scale[1], -14.0 * scale[0],
              10.0 * scale[1], 20.0 * scale[0], 15.0 * scale[1])
    Lineto_r(40.0 * scale[0], 6.0 * scale[1])
    Lineto_r(-35.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 1.0 * scale[1], -42.0 *
              scale[0], -3.0 * scale[1], -50.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(308.0 * scale[0], 1293.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 32.0 *
              scale[0], -2.0 * scale[1], 45.0 * scale[0], 0.0 * scale[1])
    Curveto_r(12.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              4.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 0.0 * scale[1], -35.0 *
              scale[0], -2.0 * scale[1], -22.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(372.0 * scale[0], 1279.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-14.0 * scale[0], -22.0 * scale[1], -15.0 *
              scale[0], -29.0 * scale[1], -4.0 * scale[0], -29.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 33.0 * scale[0],
              38.0 * scale[1], 24.0 * scale[0], 44.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 3.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -20.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(753.0 * scale[0], 1283.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(581.0 * scale[0], 1275.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -22.0 * scale[1], 16.0 * scale[0], -
              48.0 * scale[1], 22.0 * scale[0], -38.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], 0.0 * scale[0],
              19.0 * scale[1], -8.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 10.0 * scale[1], -14.0 * scale[0],
              15.0 * scale[1], -14.0 * scale[0], 9.0 * scale[1])
    te.end_fill()
    Moveto(626.0 * scale[0], 1260.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -5.0 * scale[1], 25.0 * scale[0], -
              13.0 * scale[1], 29.0 * scale[0], -19.0 * scale[1])
    Curveto_r(3.0 * scale[0], -6.0 * scale[1], 11.0 * scale[0], -
              11.0 * scale[1], 17.0 * scale[0], -11.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], -1.0 * scale[0],
              9.0 * scale[1], -15.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 11.0 * scale[1], -31.0 * scale[0],
              20.0 * scale[1], -39.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -3.0 *
              scale[0], -4.0 * scale[1], 8.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(765.0 * scale[0], 1260.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -8.0 * scale[1], -19.0 *
              scale[0], -9.0 * scale[1], 3.0 * scale[0], -9.0 * scale[1])
    Curveto_r(12.0 * scale[0], -1.0 * scale[1], 22.0 * scale[0],
              4.0 * scale[1], 22.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -1.0 * scale[0],
              10.0 * scale[1], -2.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              4.0 * scale[1], -23.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(930.0 * scale[0], 1250.0 * scale[1], x, y)
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
    Moveto(173.0 * scale[0], 1233.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], 6.0 * scale[0], -
              13.0 * scale[1], 14.0 * scale[0], -13.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              6.0 * scale[1], 13.0 * scale[0], 13.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -6.0 * scale[0],
              14.0 * scale[1], -13.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0], -
              6.0 * scale[1], -14.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(263.0 * scale[0], 1220.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -18.0 * scale[1], 0.0 * scale[0], -
              40.0 * scale[1], 14.0 * scale[0], -26.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], 0.0 * scale[0],
              6.0 * scale[1], -7.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0],
              6.0 * scale[1], 5.0 * scale[0], 20.0 * scale[1])
    Curveto_r(10.0 * scale[0], 11.0 * scale[1], 14.0 * scale[0],
              20.0 * scale[1], 9.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              9.0 * scale[1], -21.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(732.0 * scale[0], 1221.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -5.0 * scale[1], -3.0 *
              scale[0], -8.0 * scale[1], 17.0 * scale[0], -7.0 * scale[1])
    Curveto_r(17.0 * scale[0], 1.0 * scale[1], 31.0 * scale[0],
              4.0 * scale[1], 31.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], -32.0 * scale[0],
              9.0 * scale[1], -48.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(218.0 * scale[0], 1213.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(596.0 * scale[0], 1194.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -15.0 * scale[1], -3.0 *
              scale[0], -31.0 * scale[1], 1.0 * scale[0], -35.0 * scale[1])
    Curveto_r(4.0 * scale[0], -4.0 * scale[1], 9.0 * scale[0],
              8.0 * scale[1], 10.0 * scale[0], 27.0 * scale[1])
    Curveto_r(3.0 * scale[0], 41.0 * scale[1], -2.0 * scale[0],
              44.0 * scale[1], -11.0 * scale[0], 8.0 * scale[1])
    te.end_fill()
    Moveto(680.0 * scale[0], 1194.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-25.0 * scale[0], -15.0 * scale[1])
    Lineto_r(25.0 * scale[0], 7.0 * scale[1])
    Curveto_r(28.0 * scale[0], 7.0 * scale[1], 35.0 * scale[0],
              12.0 * scale[1], 29.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 2.0 * scale[1], -15.0 * scale[0], -
              2.0 * scale[1], -29.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(800.0 * scale[0], 1200.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(361.0 * scale[0], 1195.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -19.0 * scale[1], 18.0 * scale[0], -
              51.0 * scale[1], 18.0 * scale[0], -35.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -4.0 * scale[0],
              22.0 * scale[1], -9.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 8.0 * scale[1], -9.0 * scale[0],
              11.0 * scale[1], -9.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(735.0 * scale[0], 1188.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-18.0 * scale[0], -8.0 * scale[1], -18.0 *
              scale[0], -8.0 * scale[1], 2.0 * scale[0], -4.0 * scale[1])
    Curveto_r(13.0 * scale[0], 2.0 * scale[1], 26.0 * scale[0],
              0.0 * scale[1], 29.0 * scale[0], -5.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 0.0 * scale[0], -
              9.0 * scale[1], -5.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              5.0 * scale[1], -11.0 * scale[0], -12.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 3.0 * scale[0], -
              8.0 * scale[1], 7.0 * scale[0], -5.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], 13.0 * scale[0], -
              2.0 * scale[1], 21.0 * scale[0], -14.0 * scale[1])
    Curveto_r(9.0 * scale[0], -13.0 * scale[1], 11.0 * scale[0], -
              24.0 * scale[1], 5.0 * scale[0], -30.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -6.0 * scale[1], -68.0 * scale[0], -
              13.0 * scale[1], -138.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-104.0 * scale[0], -5.0 * scale[1], -127.0 *
              scale[0], -4.0 * scale[1], -120.0 * scale[0], 7.0 * scale[1])
    Curveto_r(6.0 * scale[0], 10.0 * scale[1], 4.0 * scale[0],
              11.0 * scale[1], -6.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -4.0 * scale[1], -24.0 *
              scale[0], -7.0 * scale[1], -36.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 1.0 * scale[1], -23.0 *
              scale[0], -3.0 * scale[1], -23.0 * scale[0], -9.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 45.0 * scale[0], -
              11.0 * scale[1], 166.0 * scale[0], -8.0 * scale[1])
    Curveto_r(139.0 * scale[0], 2.0 * scale[1], 168.0 * scale[0],
              6.0 * scale[1], 178.0 * scale[0], 19.0 * scale[1])
    Curveto_r(6.0 * scale[0], 9.0 * scale[1], 20.0 * scale[0],
              19.0 * scale[1], 31.0 * scale[0], 22.0 * scale[1])
    Curveto_r(15.0 * scale[0], 3.0 * scale[1], 13.0 * scale[0],
              5.0 * scale[1], -7.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -28.0 * scale[0],
              6.0 * scale[1], -28.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -4.0 * scale[0],
              7.0 * scale[1], -10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -3.0 * scale[1], -10.0 * scale[0],
              5.0 * scale[1], -10.0 * scale[0], 18.0 * scale[1])
    Curveto_r(0.0 * scale[0], 29.0 * scale[1], -17.0 * scale[0],
              38.0 * scale[1], -45.0 * scale[0], 25.0 * scale[1])
    te.end_fill()
    Moveto(184.0 * scale[0], 1174.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], 6.0 * scale[0], -
              18.0 * scale[1], 6.0 * scale[0], -20.0 * scale[1])
    Curveto_r(0.0 * scale[0], -3.0 * scale[1], 5.0 * scale[0], -
              2.0 * scale[1], 10.0 * scale[0], 1.0 * scale[1])
    Curveto_r(15.0 * scale[0], 9.0 * scale[1], 12.0 * scale[0],
              22.0 * scale[1], -6.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 5.0 * scale[1], -15.0 * scale[0],
              2.0 * scale[1], -10.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(290.0 * scale[0], 1179.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 4.0 * scale[0], -
              8.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 12.0 * scale[0],
              1.0 * scale[1], 16.0 * scale[0], -5.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 11.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 2.0 * scale[0],
              7.0 * scale[1], -9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 17.0 * scale[1], -34.0 * scale[0],
              19.0 * scale[1], -34.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(165.0 * scale[0], 1150.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              10.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              5.0 * scale[1], -11.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 11.0 * scale[0], -
              8.0 * scale[1], 25.0 * scale[0], -4.0 * scale[1])
    Curveto_r(14.0 * scale[0], 3.0 * scale[1], 25.0 * scale[0],
              2.0 * scale[1], 25.0 * scale[0], -3.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -12.0 * scale[0], -
              9.0 * scale[1], -27.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 1.0 * scale[1], -41.0 *
              scale[0], -4.0 * scale[1], -58.0 * scale[0], -9.0 * scale[1])
    Lineto_r(-30.0 * scale[0], -10.0 * scale[1])
    Lineto_r(25.0 * scale[0], -6.0 * scale[1])
    Curveto_r(14.0 * scale[0], -4.0 * scale[1], 30.0 *
              scale[0], -3.0 * scale[1], 36.0 * scale[0], 2.0 * scale[1])
    Curveto_r(7.0 * scale[0], 5.0 * scale[1], 40.0 * scale[0],
              2.0 * scale[1], 78.0 * scale[0], -6.0 * scale[1])
    Curveto_r(36.0 * scale[0], -7.0 * scale[1], 66.0 * scale[0], -
              10.0 * scale[1], 66.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -18.0 * scale[0],
              13.0 * scale[1], -47.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -1.0 * scale[1], -11.0 * scale[0],
              3.0 * scale[1], -8.0 * scale[0], 7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], -3.0 * scale[0],
              11.0 * scale[1], -12.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 3.0 * scale[1], -4.0 * scale[0],
              3.0 * scale[1], 12.0 * scale[0], 1.0 * scale[1])
    Curveto_r(84.0 * scale[0], -14.0 * scale[1], 94.0 *
              scale[0], -13.0 * scale[1], 38.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-35.0 * scale[0], 9.0 * scale[1], -63.0 * scale[0],
              20.0 * scale[1], -63.0 * scale[0], 24.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 6.0 * scale[0],
              6.0 * scale[1], 14.0 * scale[0], 3.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 17.0 *
              scale[0], -1.0 * scale[1], 21.0 * scale[0], 5.0 * scale[1])
    Curveto_r(9.0 * scale[0], 15.0 * scale[1], -28.0 * scale[0],
              14.0 * scale[1], -44.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -10.0 * scale[1], -14.0 *
              scale[0], -10.0 * scale[1], -18.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -9.0 * scale[0],
              12.0 * scale[1], -14.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              4.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(920.0 * scale[0], 1145.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -9.0 * scale[1], -20.0 * scale[0], -
              13.0 * scale[1], -27.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 3.0 * scale[1], -13.0 * scale[0],
              0.0 * scale[1], -11.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], -7.0 * scale[1], -5.0 * scale[0], -
              21.0 * scale[1], -18.0 * scale[0], -30.0 * scale[1])
    Curveto_r(-24.0 * scale[0], -20.0 * scale[1], -44.0 *
              scale[0], -23.0 * scale[1], -44.0 * scale[0], -8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 6.0 * scale[0],
              7.0 * scale[1], 14.0 * scale[0], 4.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -1.0 * scale[1], 19.0 * scale[0], 3.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], -3.0 * scale[0],
              10.0 * scale[1], -14.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 1.0 * scale[1], -23.0 * scale[0], -
              6.0 * scale[1], -29.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -12.0 * scale[1], -26.0 * scale[0], -
              21.0 * scale[1], -54.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-25.0 * scale[0], -4.0 * scale[1], -48.0 * scale[0], -
              12.0 * scale[1], -52.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 5.0 * scale[0], -
              7.0 * scale[1], 22.0 * scale[0], -3.0 * scale[1])
    Curveto_r(19.0 * scale[0], 5.0 * scale[1], 25.0 * scale[0],
              4.0 * scale[1], 20.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -8.0 * scale[1], 10.0 * scale[0], -
              11.0 * scale[1], 51.0 * scale[0], -11.0 * scale[1])
    Curveto_r(42.0 * scale[0], 0.0 * scale[1], 54.0 * scale[0],
              3.0 * scale[1], 43.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 7.0 * scale[1], 4.0 * scale[0],
              8.0 * scale[1], 44.0 * scale[0], 4.0 * scale[1])
    Curveto_r(44.0 * scale[0], -5.0 * scale[1], 57.0 *
              scale[0], -4.0 * scale[1], 52.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 7.0 * scale[1], -15.0 * scale[0],
              12.0 * scale[1], -24.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0],
              2.0 * scale[1], -2.0 * scale[0], 6.0 * scale[1])
    Curveto_r(8.0 * scale[0], 4.0 * scale[1], 21.0 * scale[0],
              13.0 * scale[1], 29.0 * scale[0], 21.0 * scale[1])
    Curveto_r(13.0 * scale[0], 13.0 * scale[1], 13.0 * scale[0],
              16.0 * scale[1], -2.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 15.0 * scale[1], -22.0 * scale[0],
              26.0 * scale[1], -4.0 * scale[0], 19.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 14.0 * scale[0],
              2.0 * scale[1], 14.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 19.0 * scale[1], -11.0 * scale[0],
              19.0 * scale[1], -27.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(280.0 * scale[0], 1140.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -8.0 * scale[1], -10.0 *
              scale[0], -10.0 * scale[1], 8.0 * scale[0], -10.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0],
              4.0 * scale[1], 17.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 12.0 * scale[1], -6.0 * scale[0],
              12.0 * scale[1], -25.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(566.0 * scale[0], 1134.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -14.0 * scale[1], -4.0 *
              scale[0], -15.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(17.0 * scale[0], 14.0 * scale[1], 19.0 * scale[0],
              20.0 * scale[1], 6.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              7.0 * scale[1], -15.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(355.0 * scale[0], 1130.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(28.0 * scale[0], -12.0 * scale[1], 37.0 *
              scale[0], -12.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -16.0 * scale[0],
              10.0 * scale[1], -28.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 0.0 * scale[1], -21.0 *
              scale[0], -1.0 * scale[1], -2.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(350.0 * scale[0], 1099.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 9.0 * scale[0], -
              9.0 * scale[1], 20.0 * scale[0], -9.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0],
              2.0 * scale[1], 20.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 2.0 * scale[1], -9.0 * scale[0],
              6.0 * scale[1], -20.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 3.0 * scale[1], -20.0 * scale[0],
              1.0 * scale[1], -20.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(416.0 * scale[0], 1100.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -6.0 * scale[1], -19.0 *
              scale[0], -7.0 * scale[1], 2.0 * scale[0], -12.0 * scale[1])
    Curveto_r(12.0 * scale[0], -4.0 * scale[1], 24.0 *
              scale[0], -2.0 * scale[1], 27.0 * scale[0], 2.0 * scale[1])
    Curveto_r(8.0 * scale[0], 13.0 * scale[1], -8.0 * scale[0],
              18.0 * scale[1], -29.0 * scale[0], 10.0 * scale[1])
    te.end_fill()
    Moveto(55.0 * scale[0], 1082.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -9.0 * scale[1], 106.0 * scale[0], -
              52.0 * scale[1], 139.0 * scale[0], -51.0 * scale[1])
    Curveto_r(41.0 * scale[0], 1.0 * scale[1], 73.0 * scale[0],
              13.0 * scale[1], 58.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -35.0 * scale[0],
              9.0 * scale[1], -64.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-29.0 * scale[0], 3.0 * scale[1], -70.0 * scale[0],
              9.0 * scale[1], -90.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 5.0 * scale[1], -40.0 * scale[0],
              6.0 * scale[1], -43.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(155.0 * scale[0], 1080.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 13.0 * scale[0], -
              10.0 * scale[1], 21.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              5.0 * scale[1], 9.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -13.0 * scale[0],
              10.0 * scale[1], -21.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              4.0 * scale[1], -9.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(300.0 * scale[0], 1070.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 9.0 * scale[0], -
              10.0 * scale[1], 20.0 * scale[0], -10.0 * scale[1])
    Curveto_r(37.0 * scale[0], 0.0 * scale[1], 21.0 * scale[0], -
              20.0 * scale[1], -17.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-29.0 * scale[0], -2.0 * scale[1], -32.0 *
              scale[0], -3.0 * scale[1], -12.0 * scale[0], -6.0 * scale[1])
    Curveto_r(15.0 * scale[0], -2.0 * scale[1], 42.0 * scale[0],
              0.0 * scale[1], 60.0 * scale[0], 5.0 * scale[1])
    Lineto_r(34.0 * scale[0], 10.0 * scale[1])
    Lineto_r(-37.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-44.0 * scale[0], 19.0 * scale[1], -48.0 * scale[0],
              19.0 * scale[1], -48.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(607.0 * scale[0], 1038.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -5.0 * scale[1], 10.0 * scale[0], -
              8.0 * scale[1], 18.0 * scale[0], -8.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0],
              3.0 * scale[1], 18.0 * scale[0], 8.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], -5.0 * scale[0],
              7.0 * scale[1], -18.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -21.0 *
              scale[0], -3.0 * scale[1], -18.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(148.0 * scale[0], 1013.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 32.0 *
              scale[0], -2.0 * scale[1], 45.0 * scale[0], 0.0 * scale[1])
    Curveto_r(12.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              4.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 0.0 * scale[1], -35.0 *
              scale[0], -2.0 * scale[1], -22.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(402.0 * scale[0], 1004.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-23.0 * scale[0], -7.0 * scale[1], -54.0 * scale[0], -
              22.0 * scale[1], -68.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -16.0 * scale[1], -31.0 *
              scale[0], -18.0 * scale[1], -45.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 11.0 * scale[1], -27.0 *
              scale[0], -5.0 * scale[1], -6.0 * scale[0], -18.0 * scale[1])
    Curveto_r(23.0 * scale[0], -14.0 * scale[1], 37.0 *
              scale[0], -11.0 * scale[1], 54.0 * scale[0], 11.0 * scale[1])
    Curveto_r(38.0 * scale[0], 47.0 * scale[1], 186.0 * scale[0],
              72.0 * scale[1], 232.0 * scale[0], 39.0 * scale[1])
    Curveto_r(18.0 * scale[0], -12.0 * scale[1], 22.0 *
              scale[0], -13.0 * scale[1], 17.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 8.0 * scale[1], -1.0 * scale[0],
              6.0 * scale[1], 7.0 * scale[0], -3.0 * scale[1])
    Curveto_r(8.0 * scale[0], -10.0 * scale[1], 17.0 * scale[0], -
              15.0 * scale[1], 20.0 * scale[0], -11.0 * scale[1])
    Curveto_r(9.0 * scale[0], 8.0 * scale[1], 38.0 * scale[0], -
              17.0 * scale[1], 31.0 * scale[0], -28.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -1.0 *
              scale[0], -9.0 * scale[1], 4.0 * scale[0], -9.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0], -
              10.0 * scale[1], 21.0 * scale[0], -22.0 * scale[1])
    Curveto_r(8.0 * scale[0], -16.0 * scale[1], 10.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 32.0 * scale[1], -7.0 * scale[0],
              76.0 * scale[1], 8.0 * scale[0], 86.0 * scale[1])
    Curveto_r(19.0 * scale[0], 12.0 * scale[1], 139.0 * scale[0],
              11.0 * scale[1], 139.0 * scale[0], -1.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 11.0 * scale[0], -
              10.0 * scale[1], 25.0 * scale[0], -10.0 * scale[1])
    Curveto_r(16.0 * scale[0], 0.0 * scale[1], 23.0 * scale[0], -
              4.0 * scale[1], 19.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], 3.0 * scale[0], -
              20.0 * scale[1], 13.0 * scale[0], -27.0 * scale[1])
    Curveto_r(14.0 * scale[0], -11.0 * scale[1], 15.0 *
              scale[0], -11.0 * scale[1], 6.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 7.0 * scale[1], -9.0 * scale[0],
              19.0 * scale[1], -7.0 * scale[0], 26.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], -5.0 * scale[0],
              20.0 * scale[1], -18.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 13.0 * scale[1], -53.0 * scale[0],
              16.0 * scale[1], -218.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-130.0 * scale[0], -1.0 * scale[1], -209.0 *
              scale[0], -6.0 * scale[1], -238.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto_r(225.0 * scale[0], 0.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 17.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(878.0 * scale[0], 1013.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(918.0 * scale[0], 1013.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(952.0 * scale[0], 998.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-14.0 * scale[0], -14.0 * scale[1], -16.0 *
              scale[0], -38.0 * scale[1], -3.0 * scale[0], -38.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 23.0 * scale[0],
              41.0 * scale[1], 17.0 * scale[0], 47.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 1.0 * scale[1], -8.0 * scale[0], -
              3.0 * scale[1], -14.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(180.0 * scale[0], 991.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 18.0 * scale[1], -14.0 * scale[0],
              21.0 * scale[1], -14.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(763.0 * scale[0], 965.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -24.0 * scale[1], 1.0 * scale[0], -
              27.0 * scale[1], 15.0 * scale[0], -5.0 * scale[1])
    Curveto_r(8.0 * scale[0], 13.0 * scale[1], 8.0 * scale[0],
              20.0 * scale[1], 2.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              7.0 * scale[1], -17.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(212.0 * scale[0], 935.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -13.0 * scale[1], 15.0 * scale[0], -
              22.0 * scale[1], 19.0 * scale[0], -19.0 * scale[1])
    Curveto_r(14.0 * scale[0], 8.0 * scale[1], 11.0 * scale[0],
              18.0 * scale[1], -11.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 11.0 * scale[1], -19.0 * scale[0],
              10.0 * scale[1], -8.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(0.0 * scale[0], 923.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 8.0 * scale[0], -
              37.0 * scale[1], 18.0 * scale[0], -46.0 * scale[1])
    Curveto_r(28.0 * scale[0], -25.0 * scale[1], 35.0 *
              scale[0], -20.0 * scale[1], 15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 14.0 * scale[1], -18.0 * scale[0],
              32.0 * scale[1], -19.0 * scale[0], 40.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 29.0 * scale[1], -14.0 * scale[0],
              26.0 * scale[1], -14.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(762.0 * scale[0], 907.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -14.0 * scale[1], 6.0 * scale[0], -
              23.0 * scale[1], 11.0 * scale[0], -20.0 * scale[1])
    Curveto_r(4.0 * scale[0], 2.0 * scale[1], 16.0 * scale[0], -
              1.0 * scale[1], 25.0 * scale[0], -8.0 * scale[1])
    Curveto_r(9.0 * scale[0], -8.0 * scale[1], 6.0 * scale[0],
              0.0 * scale[1], -8.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 17.0 * scale[1], -26.0 * scale[0],
              32.0 * scale[1], -28.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0], -
              7.0 * scale[1], 0.0 * scale[0], -22.0 * scale[1])
    te.end_fill()
    Moveto(845.0 * scale[0], 910.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -12.0 *
              scale[0], -7.0 * scale[1], -18.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -4.0 * scale[0], -1.0 * scale[1])
    Curveto_r(13.0 * scale[0], -15.0 * scale[1], 37.0 *
              scale[0], -14.0 * scale[1], 37.0 * scale[0], 1.0 * scale[1])
    Curveto_r(0.0 * scale[0], 16.0 * scale[1], -6.0 * scale[0],
              18.0 * scale[1], -15.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(300.0 * scale[0], 905.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 7.0 * scale[0], -
              8.0 * scale[1], 15.0 * scale[0], -15.0 * scale[1])
    Curveto_r(12.0 * scale[0], -10.0 * scale[1], 15.0 *
              scale[0], -10.0 * scale[1], 15.0 * scale[0], 2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -7.0 * scale[0],
              15.0 * scale[1], -15.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              1.0 * scale[1], -15.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(105.0 * scale[0], 889.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0], -
              12.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 17.0 * scale[1], 1.0 * scale[0],
              20.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(695.0 * scale[0], 890.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-18.0 * scale[0], -7.0 * scale[1], -18.0 *
              scale[0], -8.0 * scale[1], -2.0 * scale[0], -14.0 * scale[1])
    Curveto_r(39.0 * scale[0], -14.0 * scale[1], 43.0 *
              scale[0], -13.0 * scale[1], 44.0 * scale[0], 5.0 * scale[1])
    Curveto_r(2.0 * scale[0], 20.0 * scale[1], -10.0 * scale[0],
              23.0 * scale[1], -42.0 * scale[0], 9.0 * scale[1])
    te.end_fill()
    Moveto(432.0 * scale[0], 882.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-27.0 * scale[0], -2.0 * scale[1], -40.0 *
              scale[0], -7.0 * scale[1], -36.0 * scale[0], -14.0 * scale[1])
    Curveto_r(5.0 * scale[0], -7.0 * scale[1], -2.0 * scale[0], -
              9.0 * scale[1], -20.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 4.0 * scale[1], -25.0 * scale[0],
              3.0 * scale[1], -21.0 * scale[0], -4.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              10.0 * scale[1], -12.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-39.0 * scale[0], -1.0 * scale[1], -57.0 *
              scale[0], -9.0 * scale[1], -84.0 * scale[0], -35.0 * scale[1])
    Curveto_r(-31.0 * scale[0], -30.0 * scale[1], -39.0 *
              scale[0], -64.0 * scale[1], -14.0 * scale[0], -64.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0], -
              6.0 * scale[1], 9.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              24.0 * scale[1], 14.0 * scale[0], -37.0 * scale[1])
    Curveto_r(19.0 * scale[0], -23.0 * scale[1], 19.0 * scale[0], -
              24.0 * scale[1], -1.0 * scale[0], -59.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -20.0 * scale[1], -32.0 *
              scale[0], -50.0 * scale[1], -45.0 * scale[0], -68.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -18.0 * scale[1], -20.0 *
              scale[0], -37.0 * scale[1], -16.0 * scale[0], -44.0 * scale[1])
    Curveto_r(4.0 * scale[0], -7.0 * scale[1], 3.0 * scale[0], -
              9.0 * scale[1], -4.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -13.0 * scale[0],
              2.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -11.0 * scale[0], -
              10.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -1.0 * scale[0],
              41.0 * scale[1], 22.0 * scale[0], 66.0 * scale[1])
    Curveto_r(11.0 * scale[0], 11.0 * scale[1], 19.0 * scale[0],
              24.0 * scale[1], 19.0 * scale[0], 29.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -16.0 * scale[0], -
              8.0 * scale[1], -35.0 * scale[0], -28.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -20.0 * scale[1], -39.0 *
              scale[0], -37.0 * scale[1], -45.0 * scale[0], -37.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              17.0 * scale[1], -1.0 * scale[0], -24.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 8.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -24.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -9.0 * scale[1], 0.0 * scale[0], -
              11.0 * scale[1], 2.0 * scale[0], -4.0 * scale[1])
    Curveto_r(3.0 * scale[0], 9.0 * scale[1], 13.0 * scale[0],
              12.0 * scale[1], 26.0 * scale[0], 8.0 * scale[1])
    Curveto_r(50.0 * scale[0], -15.0 * scale[1], 59.0 *
              scale[0], -15.0 * scale[1], 54.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], 2.0 * scale[0],
              24.0 * scale[1], 10.0 * scale[0], 36.0 * scale[1])
    Curveto_r(9.0 * scale[0], 13.0 * scale[1], 26.0 * scale[0],
              41.0 * scale[1], 38.0 * scale[0], 63.0 * scale[1])
    Curveto_r(24.0 * scale[0], 46.0 * scale[1], 37.0 * scale[0],
              54.0 * scale[1], 56.0 * scale[0], 34.0 * scale[1])
    Curveto_r(8.0 * scale[0], -7.0 * scale[1], 27.0 * scale[0], -
              17.0 * scale[1], 42.0 * scale[0], -21.0 * scale[1])
    Curveto_r(36.0 * scale[0], -9.0 * scale[1], 38.0 * scale[0],
              20.0 * scale[1], 2.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 6.0 * scale[1], -22.0 * scale[0],
              15.0 * scale[1], -19.0 * scale[0], 19.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], 1.0 * scale[0],
              9.0 * scale[1], -4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 0.0 * scale[1], 1.0 * scale[0],
              66.0 * scale[1], 26.0 * scale[0], 92.0 * scale[1])
    Curveto_r(18.0 * scale[0], 20.0 * scale[1], 39.0 * scale[0],
              30.0 * scale[1], 74.0 * scale[0], 34.0 * scale[1])
    Curveto_r(26.0 * scale[0], 4.0 * scale[1], 48.0 * scale[0],
              10.0 * scale[1], 48.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 17.0 * scale[0],
              17.0 * scale[1], 39.0 * scale[0], 27.0 * scale[1])
    Curveto_r(32.0 * scale[0], 16.0 * scale[1], 41.0 * scale[0],
              17.0 * scale[1], 56.0 * scale[0], 5.0 * scale[1])
    Curveto_r(11.0 * scale[0], -7.0 * scale[1], 13.0 * scale[0], -
              13.0 * scale[1], 7.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -20.0 * scale[1], 6.0 * scale[0], -27.0 * scale[1])
    Curveto_r(22.0 * scale[0], -9.0 * scale[1], 57.0 * scale[0], -
              52.0 * scale[1], 57.0 * scale[0], -72.0 * scale[1])
    Curveto_r(0.0 * scale[0], -22.0 * scale[1], 20.0 * scale[0], -
              24.0 * scale[1], 36.0 * scale[0], -4.0 * scale[1])
    Curveto_r(11.0 * scale[0], 15.0 * scale[1], 11.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-37.0 * scale[0], -33.0 * scale[1], -40.0 *
              scale[0], -3.0 * scale[1], -3.0 * scale[0], 31.0 * scale[1])
    Curveto_r(32.0 * scale[0], 30.0 * scale[1], 39.0 * scale[0],
              72.0 * scale[1], 13.0 * scale[0], 79.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 3.0 * scale[1], -20.0 * scale[0],
              1.0 * scale[1], -22.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -5.0 * scale[1], -17.0 * scale[0], -
              11.0 * scale[1], -35.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-30.0 * scale[0], -6.0 * scale[1], -32.0 *
              scale[0], -5.0 * scale[1], -27.0 * scale[0], 19.0 * scale[1])
    Curveto_r(2.0 * scale[0], 14.0 * scale[1], -1.0 * scale[0],
              29.0 * scale[1], -7.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -9.0 * scale[0],
              3.0 * scale[1], -6.0 * scale[0], -3.0 * scale[1])
    Curveto_r(5.0 * scale[0], -8.0 * scale[1], -97.0 * scale[0], -
              2.0 * scale[1], -120.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 2.0 * scale[1], -27.0 * scale[0],
              3.0 * scale[1], -51.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto_r(-99.0 * scale[0], -137.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-39.0 * scale[0], -47.0 * scale[1], -56.0 *
              scale[0], -52.0 * scale[1], -61.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 18.0 * scale[1], -3.0 * scale[0],
              18.0 * scale[1], 12.0 * scale[0], -1.0 * scale[1])
    Curveto_r(9.0 * scale[0], -12.0 * scale[1], 15.0 * scale[0], -
              15.0 * scale[1], 16.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 20.0 * scale[1], 42.0 * scale[0],
              72.0 * scale[1], 57.0 * scale[0], 72.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], -2.0 * scale[0], -
              19.0 * scale[1], -24.0 * scale[0], -45.0 * scale[1])
    te.end_fill()
    Moveto(946.0 * scale[0], 868.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -19.0 * scale[1], 1.0 * scale[0], -
              29.0 * scale[1], -13.0 * scale[0], -37.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -10.0 * scale[1], -17.0 *
              scale[0], -10.0 * scale[1], 3.0 * scale[0], -11.0 * scale[1])
    Curveto_r(27.0 * scale[0], 0.0 * scale[1], 37.0 * scale[0],
              32.0 * scale[1], 18.0 * scale[0], 57.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -14.0 * scale[0],
              16.0 * scale[1], -8.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(255.0 * scale[0], 871.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -17.0 * scale[1], 10.0 *
              scale[0], -20.0 * scale[1], 35.0 * scale[0], -5.0 * scale[1])
    Lineto_r(25.0 * scale[0], 13.0 * scale[1])
    Lineto_r(-27.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 0.0 * scale[1], -29.0 *
              scale[0], -4.0 * scale[1], -33.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(0.0 * scale[0], 834.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 4.0 * scale[0], -
              33.0 * scale[1], 8.0 * scale[0], -30.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 4.0 * scale[0],
              66.0 * scale[1], -4.0 * scale[0], 66.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              16.0 * scale[1], -4.0 * scale[0], -36.0 * scale[1])
    te.end_fill()
    Moveto(914.0 * scale[0], 859.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], -17.0 *
              scale[0], -9.0 * scale[1], -31.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 3.0 * scale[1], -22.0 * scale[0],
              0.0 * scale[1], -20.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], -6.0 * scale[1], 10.0 * scale[0], -
              10.0 * scale[1], 16.0 * scale[0], -8.0 * scale[1])
    Curveto_r(7.0 * scale[0], 1.0 * scale[1], 23.0 * scale[0],
              3.0 * scale[1], 36.0 * scale[0], 4.0 * scale[1])
    Curveto_r(14.0 * scale[0], 1.0 * scale[1], 25.0 * scale[0],
              8.0 * scale[1], 25.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 16.0 * scale[1], -16.0 * scale[0],
              17.0 * scale[1], -26.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(560.0 * scale[0], 840.0 * scale[1], x, y)
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
    Moveto(782.0 * scale[0], 810.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(719.0 * scale[0], 763.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -21.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(187.0 * scale[0], 715.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -8.0 * scale[1], -2.0 * scale[0], -
              17.0 * scale[1], 3.0 * scale[0], -20.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 10.0 * scale[0],
              3.0 * scale[1], 10.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 25.0 * scale[1], -6.0 * scale[0],
              27.0 * scale[1], -13.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(156.0 * scale[0], 693.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(130.0 * scale[0], 626.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], -3.0 * scale[0], -
              43.0 * scale[1], -6.0 * scale[0], -53.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -14.0 * scale[1], -4.0 *
              scale[0], -15.0 * scale[1], 4.0 * scale[0], -3.0 * scale[1])
    Curveto_r(15.0 * scale[0], 24.0 * scale[1], 24.0 * scale[0],
              90.0 * scale[1], 12.0 * scale[0], 90.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              15.0 * scale[1], -10.0 * scale[0], -34.0 * scale[1])
    te.end_fill()
    Moveto(403.0 * scale[0], 595.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              12.0 * scale[1], 9.0 * scale[0], -9.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 6.0 * scale[0],
              10.0 * scale[1], 3.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 13.0 * scale[1], -12.0 * scale[0],
              11.0 * scale[1], -12.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(963.0 * scale[0], 545.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -27.0 * scale[1], 2.0 * scale[0], -
              38.0 * scale[1], 4.0 * scale[0], -22.0 * scale[1])
    Curveto_r(2.0 * scale[0], 15.0 * scale[1], 2.0 * scale[0],
              37.0 * scale[1], 0.0 * scale[0], 50.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 12.0 * scale[1], -4.0 * scale[0],
              0.0 * scale[1], -4.0 * scale[0], -28.0 * scale[1])
    te.end_fill()
    Moveto(382.0 * scale[0], 509.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -18.0 * scale[1], 9.0 * scale[0], -
              35.0 * scale[1], 17.0 * scale[0], -37.0 * scale[1])
    Curveto_r(10.0 * scale[0], -3.0 * scale[1], 11.0 * scale[0],
              0.0 * scale[1], 5.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 8.0 * scale[1], -7.0 * scale[0],
              21.0 * scale[1], -6.0 * scale[0], 31.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], -2.0 * scale[0],
              19.0 * scale[1], -8.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -10.0 * scale[0], -
              3.0 * scale[1], -8.0 * scale[0], -26.0 * scale[1])
    te.end_fill()
    Moveto(735.0 * scale[0], 527.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -19.0 * scale[1], -2.0 * scale[0], -
              31.0 * scale[1], 13.0 * scale[0], -26.0 * scale[1])
    Curveto_r(5.0 * scale[0], 2.0 * scale[1], 6.0 * scale[0],
              13.0 * scale[1], 2.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 19.0 * scale[1], -8.0 * scale[0],
              19.0 * scale[1], -15.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(710.0 * scale[0], 469.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -11.0 * scale[1], -10.0 *
              scale[0], -23.0 * scale[1], -7.0 * scale[0], -25.0 * scale[1])
    Curveto_r(2.0 * scale[0], -2.0 * scale[1], 9.0 * scale[0],
              7.0 * scale[1], 15.0 * scale[0], 21.0 * scale[1])
    Curveto_r(14.0 * scale[0], 30.0 * scale[1], 7.0 * scale[0],
              33.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(770.0 * scale[0], 454.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(35.0 * scale[0], -56.0 * scale[1], 56.0 * scale[0], -
              104.0 * scale[1], 75.0 * scale[0], -169.0 * scale[1])
    Curveto_r(13.0 * scale[0], -47.0 * scale[1], 25.0 * scale[0], -
              66.0 * scale[1], 55.0 * scale[0], -90.0 * scale[1])
    Curveto_r(21.0 * scale[0], -16.0 * scale[1], 44.0 * scale[0], -
              41.0 * scale[1], 51.0 * scale[0], -55.0 * scale[1])
    Curveto_r(11.0 * scale[0], -21.0 * scale[1], 13.0 *
              scale[0], -22.0 * scale[1], 17.0 * scale[0], -7.0 * scale[1])
    Curveto_r(2.0 * scale[0], 12.0 * scale[1], -13.0 * scale[0],
              34.0 * scale[1], -47.0 * scale[0], 65.0 * scale[1])
    Curveto_r(-31.0 * scale[0], 29.0 * scale[1], -51.0 * scale[0],
              56.0 * scale[1], -51.0 * scale[0], 69.0 * scale[1])
    Curveto_r(0.0 * scale[0], 27.0 * scale[1], -98.0 * scale[0],
              223.0 * scale[1], -111.0 * scale[0], 223.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -1.0 * scale[0], -
              16.0 * scale[1], 11.0 * scale[0], -36.0 * scale[1])
    te.end_fill()
    Moveto(925.0 * scale[0], 455.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -33.0 * scale[1], 12.0 * scale[0], -
              41.0 * scale[1], 21.0 * scale[0], -33.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], -2.0 * scale[0],
              19.0 * scale[1], -11.0 * scale[0], 35.0 * scale[1])
    Lineto_r(-16.0 * scale[0], 28.0 * scale[1])
    Lineto_r(6.0 * scale[0], -30.0 * scale[1])
    te.end_fill()
    Moveto(951.0 * scale[0], 415.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -25.0 * scale[1], -11.0 *
              scale[0], -49.0 * scale[1], -7.0 * scale[0], -52.0 * scale[1])
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], 6.0 * scale[0],
              4.0 * scale[1], 6.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              19.0 * scale[1], 10.0 * scale[0], 16.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 10.0 * scale[0],
              8.0 * scale[1], 10.0 * scale[0], 29.0 * scale[1])
    Curveto_r(0.0 * scale[0], 20.0 * scale[1], -1.0 * scale[0],
              36.0 * scale[1], -3.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              20.0 * scale[1], -16.0 * scale[0], -45.0 * scale[1])
    te.end_fill()
    Moveto(658.0 * scale[0], 418.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-20.0 * scale[0], -19.0 * scale[1], -86.0 * scale[0], -
              48.0 * scale[1], -111.0 * scale[0], -49.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -16.0 *
              scale[0], -3.0 * scale[1], -9.0 * scale[0], -6.0 * scale[1])
    Curveto_r(16.0 * scale[0], -6.0 * scale[1], 15.0 * scale[0], -
              23.0 * scale[1], -2.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              34.0 * scale[1], 26.0 * scale[0], -53.0 * scale[1])
    Lineto_r(30.0 * scale[0], -17.0 * scale[1])
    Lineto_r(-6.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 24.0 * scale[1], 0.0 * scale[0],
              34.0 * scale[1], 48.0 * scale[0], 81.0 * scale[1])
    Curveto_r(31.0 * scale[0], 29.0 * scale[1], 52.0 * scale[0],
              53.0 * scale[1], 47.0 * scale[0], 53.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0], -
              6.0 * scale[1], -23.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(151.0 * scale[0], 410.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              22.0 * scale[1], 9.0 * scale[0], -30.0 * scale[1])
    Curveto_r(12.0 * scale[0], -18.0 * scale[1], 12.0 *
              scale[0], -2.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 13.0 * scale[1], -9.0 * scale[0],
              15.0 * scale[1], -9.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(259.0 * scale[0], 383.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -21.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(3.0 * scale[0], 285.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -33.0 * scale[1], 2.0 * scale[0], -
              45.0 * scale[1], 4.0 * scale[0], -27.0 * scale[1])
    Curveto_r(2.0 * scale[0], 18.0 * scale[1], 2.0 * scale[0],
              45.0 * scale[1], 0.0 * scale[0], 60.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 15.0 * scale[1], -4.0 * scale[0],
              0.0 * scale[1], -4.0 * scale[0], -33.0 * scale[1])
    te.end_fill()
    Moveto(224.0 * scale[0], 314.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -10.0 * scale[1], -14.0 *
              scale[0], -14.0 * scale[1], -4.0 * scale[0], -11.0 * scale[1])
    Curveto_r(8.0 * scale[0], 2.0 * scale[1], 25.0 * scale[0],
              0.0 * scale[1], 38.0 * scale[0], -4.0 * scale[1])
    Curveto_r(20.0 * scale[0], -8.0 * scale[1], 21.0 *
              scale[0], -7.0 * scale[1], 12.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 24.0 * scale[1], -20.0 * scale[0],
              25.0 * scale[1], -46.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(494.0 * scale[0], 311.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(15.0 * scale[0], -17.0 * scale[1], 16.0 *
              scale[0], -24.0 * scale[1], 7.0 * scale[0], -35.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -9.0 * scale[1], -10.0 * scale[0], -
              25.0 * scale[1], -6.0 * scale[0], -38.0 * scale[1])
    Curveto_r(5.0 * scale[0], -17.0 * scale[1], 2.0 * scale[0], -
              15.0 * scale[1], -13.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 35.0 * scale[1], -42.0 * scale[0],
              51.0 * scale[1], -42.0 * scale[0], 35.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              11.0 * scale[1], 9.0 * scale[0], -11.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0], -
              10.0 * scale[1], 16.0 * scale[0], -22.0 * scale[1])
    Curveto_r(4.0 * scale[0], -13.0 * scale[1], 8.0 * scale[0], -
              25.0 * scale[1], 10.0 * scale[0], -28.0 * scale[1])
    Curveto_r(1.0 * scale[0], -3.0 * scale[1], 5.0 * scale[0], -
              13.0 * scale[1], 9.0 * scale[0], -22.0 * scale[1])
    Curveto_r(4.0 * scale[0], -10.0 * scale[1], 6.0 * scale[0], -
              49.0 * scale[1], 3.0 * scale[0], -88.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -38.0 * scale[1], -1.0 *
              scale[0], -70.0 * scale[1], 4.0 * scale[0], -70.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              5.0 * scale[1], 9.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 5.0 * scale[0],
              7.0 * scale[1], 10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(8.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              11.0 * scale[1], -1.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -11.0 * scale[1], -7.0 *
              scale[0], -14.0 * scale[1], 9.0 * scale[0], -14.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 24.0 * scale[0], -
              5.0 * scale[1], 27.0 * scale[0], -10.0 * scale[1])
    Curveto_r(3.0 * scale[0], -6.0 * scale[1], 20.0 * scale[0], -
              10.0 * scale[1], 36.0 * scale[0], -10.0 * scale[1])
    Curveto_r(18.0 * scale[0], 0.0 * scale[1], 28.0 * scale[0],
              4.0 * scale[1], 24.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -14.0 * scale[0],
              10.0 * scale[1], -23.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -21.0 * scale[0],
              45.0 * scale[1], -7.0 * scale[0], 157.0 * scale[1])
    Curveto_r(8.0 * scale[0], 62.0 * scale[1], 7.0 * scale[0],
              63.0 * scale[1], -28.0 * scale[0], 98.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 20.0 * scale[1], -36.0 * scale[0],
              39.0 * scale[1], -36.0 * scale[0], 43.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], -8.0 * scale[0],
              9.0 * scale[1], -18.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 3.0 * scale[1], -17.0 * scale[0],
              2.0 * scale[1], 1.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(308.0 * scale[0], 288.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -12.0 * scale[1], 65.0 *
              scale[0], -21.0 * scale[1], 58.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], -19.0 * scale[0],
              11.0 * scale[1], -36.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 3.0 * scale[1], -27.0 * scale[0],
              1.0 * scale[1], -22.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(3.0 * scale[0], 160.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -25.0 * scale[1], 2.0 * scale[0], -
              35.0 * scale[1], 4.0 * scale[0], -22.0 * scale[1])
    Curveto_r(2.0 * scale[0], 12.0 * scale[1], 2.0 * scale[0],
              32.0 * scale[1], 0.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 12.0 * scale[1], -4.0 * scale[0],
              2.0 * scale[1], -4.0 * scale[0], -23.0 * scale[1])
    te.end_fill()
    Moveto(431.0 * scale[0], 193.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 4.0 * scale[0], -
              17.0 * scale[1], 9.0 * scale[0], -28.0 * scale[1])
    Curveto_r(8.0 * scale[0], -19.0 * scale[1], 9.0 *
              scale[0], -19.0 * scale[1], 9.0 * scale[0], 2.0 * scale[1])
    Curveto_r(1.0 * scale[0], 12.0 * scale[1], -3.0 * scale[0],
              25.0 * scale[1], -9.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0],
              3.0 * scale[1], -9.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(780.0 * scale[0], 129.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], -5.0 * scale[0], -
              51.0 * scale[1], -10.0 * scale[0], -71.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -39.0 * scale[1], -14.0 * scale[0], -
              40.0 * scale[1], -105.0 * scale[0], -51.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -2.0 * scale[1], -3.0 *
              scale[0], -5.0 * scale[1], 29.0 * scale[0], -6.0 * scale[1])
    Curveto_r(33.0 * scale[0], 0.0 * scale[1], 75.0 * scale[0],
              4.0 * scale[1], 93.0 * scale[0], 11.0 * scale[1])
    Curveto_r(27.0 * scale[0], 10.0 * scale[1], 38.0 * scale[0],
              10.0 * scale[1], 56.0 * scale[0], -1.0 * scale[1])
    Curveto_r(19.0 * scale[0], -12.0 * scale[1], 20.0 *
              scale[0], -12.0 * scale[1], 11.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 8.0 * scale[1], -15.0 * scale[0],
              29.0 * scale[1], -19.0 * scale[0], 48.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 25.0 * scale[1], -10.0 * scale[0],
              30.0 * scale[1], -17.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -10.0 * scale[1], -7.0 *
              scale[0], -7.0 * scale[1], -3.0 * scale[0], 9.0 * scale[1])
    Curveto_r(4.0 * scale[0], 15.0 * scale[1], 0.0 * scale[0],
              31.0 * scale[1], -14.0 * scale[0], 48.0 * scale[1])
    Lineto_r(-21.0 * scale[0], 27.0 * scale[1])
    Lineto_r(0.0 * scale[0], -34.0 * scale[1])
    te.end_fill()
    Moveto(50.0 * scale[0], 69.0 * scale[1], x, y)
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
    Moveto(46.0 * scale[0], 41.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              12.0 * scale[1], 10.0 * scale[0], -15.0 * scale[1])
    Curveto_r(22.0 * scale[0], -8.0 * scale[1], 25.0 *
              scale[0], -4.0 * scale[1], 9.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 7.0 * scale[1], -16.0 * scale[0],
              9.0 * scale[1], -19.0 * scale[0], 4.0 * scale[1])
    te.penup()
