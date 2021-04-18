
import turtle as te
from helper import *


def perroquet_femelle(x, y, scale):
    te.penup()
    te.color('#b7a4cf')
    te.end_fill()
    Moveto(465.0 * scale[0], 1280.0 * scale[1], x, y)
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
    Moveto(39.0 * scale[0], 833.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -21.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(500.0 * scale[0], 754.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -4.0 * scale[0], -
              13.0 * scale[1], -8.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0],
              0.0 * scale[1], -9.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -3.0 * scale[0], -
              19.0 * scale[1], -5.0 * scale[0], -27.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -3.0 * scale[0], -
              12.0 * scale[1], -1.0 * scale[0], -8.0 * scale[1])
    Curveto_r(2.0 * scale[0], 4.0 * scale[1], 11.0 * scale[0],
              4.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 11.0 * scale[0], -
              9.0 * scale[1], 8.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -1.0 *
              scale[0], -9.0 * scale[1], 5.0 * scale[0], -9.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0], -
              8.0 * scale[1], 4.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -19.0 * scale[1], -5.0 *
              scale[0], -18.0 * scale[1], 17.0 * scale[0], 11.0 * scale[1])
    Curveto_r(10.0 * scale[0], 13.0 * scale[1], 10.0 * scale[0],
              17.0 * scale[1], 3.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -4.0 * scale[1], -13.0 *
              scale[0], -2.0 * scale[1], -13.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 5.0 * scale[0],
              11.0 * scale[1], 11.0 * scale[0], 11.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              5.0 * scale[1], 3.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 8.0 * scale[1], -9.0 * scale[0],
              8.0 * scale[1], -13.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], -12.0 *
              scale[0], -8.0 * scale[1], -21.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 5.0 * scale[1], -11.0 * scale[0],
              12.0 * scale[1], -5.0 * scale[0], 17.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 16.0 * scale[0],
              15.0 * scale[1], 24.0 * scale[0], 25.0 * scale[1])
    Curveto_r(12.0 * scale[0], 15.0 * scale[1], 11.0 * scale[0],
              17.0 * scale[1], -3.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0], -
              7.0 * scale[1], -16.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(619.0 * scale[0], 713.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -21.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(710.0 * scale[0], 713.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0], -
              15.0 * scale[1], 10.0 * scale[0], -23.0 * scale[1])
    Curveto_r(8.0 * scale[0], -12.0 * scale[1], 10.0 *
              scale[0], -11.0 * scale[1], 10.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], -4.0 * scale[0],
              22.0 * scale[1], -10.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              3.0 * scale[1], -10.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(565.0 * scale[0], 630.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 14.0 * scale[0], -
              10.0 * scale[1], 23.0 * scale[0], -10.0 * scale[1])
    Curveto_r(15.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              2.0 * scale[1], 2.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 13.0 * scale[1], -33.0 * scale[0],
              13.0 * scale[1], -25.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(11.0 * scale[0], 555.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -56.0 * scale[1], 6.0 * scale[0], -
              78.0 * scale[1], 17.0 * scale[0], -84.0 * scale[1])
    Curveto_r(13.0 * scale[0], -7.0 * scale[1], 11.0 * scale[0], -
              10.0 * scale[1], -7.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -6.0 * scale[1], -22.0 * scale[0], -
              12.0 * scale[1], -19.0 * scale[0], -88.0 * scale[1])
    Curveto_r(3.0 * scale[0], -73.0 * scale[1], 5.0 * scale[0], -
              82.0 * scale[1], 23.0 * scale[0], -85.0 * scale[1])
    Curveto_r(11.0 * scale[0], -2.0 * scale[1], 25.0 *
              scale[0], -5.0 * scale[1], 30.0 * scale[0], -6.0 * scale[1])
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 15.0 * scale[0], -
              4.0 * scale[1], 20.0 * scale[0], -6.0 * scale[1])
    Curveto_r(6.0 * scale[0], -1.0 * scale[1], 17.0 * scale[0], -
              6.0 * scale[1], 26.0 * scale[0], -11.0 * scale[1])
    Curveto_r(14.0 * scale[0], -7.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 24.0 * scale[0], 28.0 * scale[1])
    Curveto_r(3.0 * scale[0], 20.0 * scale[1], 13.0 * scale[0],
              46.0 * scale[1], 20.0 * scale[0], 57.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 16.0 * scale[0],
              32.0 * scale[1], 18.0 * scale[0], 45.0 * scale[1])
    Curveto_r(2.0 * scale[0], 12.0 * scale[1], 8.0 * scale[0],
              26.0 * scale[1], 13.0 * scale[0], 29.0 * scale[1])
    Curveto_r(12.0 * scale[0], 8.0 * scale[1], 54.0 * scale[0],
              68.0 * scale[1], 72.0 * scale[0], 101.0 * scale[1])
    Curveto_r(15.0 * scale[0], 28.0 * scale[1], 16.0 * scale[0],
              51.0 * scale[1], 2.0 * scale[0], 51.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0],
              7.0 * scale[1], -10.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], -5.0 * scale[0],
              12.0 * scale[1], -12.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -5.0 * scale[1], -9.0 * scale[0],
              0.0 * scale[1], -5.0 * scale[0], 15.0 * scale[1])
    Curveto_r(4.0 * scale[0], 17.0 * scale[1], 3.0 * scale[0],
              20.0 * scale[1], -7.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -6.0 * scale[1], -16.0 *
              scale[0], -7.0 * scale[1], -20.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 4.0 * scale[1], -7.0 * scale[0],
              0.0 * scale[1], -5.0 * scale[0], -8.0 * scale[1])
    Curveto_r(1.0 * scale[0], -8.0 * scale[1], -1.0 * scale[0], -
              27.0 * scale[1], -5.0 * scale[0], -42.0 * scale[1])
    Lineto_r(-8.0 * scale[0], -27.0 * scale[1])
    Lineto_r(-32.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-32.0 * scale[0], 25.0 * scale[1], -113.0 * scale[0],
              66.0 * scale[1], -128.0 * scale[0], 66.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              34.0 * scale[1], -7.0 * scale[0], -75.0 * scale[1])
    te.end_fill()
    Moveto(702.0 * scale[0], 471.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -6.0 * scale[1], -11.0 *
              scale[0], -20.0 * scale[1], -2.0 * scale[0], -72.0 * scale[1])
    Curveto_r(7.0 * scale[0], -36.0 * scale[1], 9.0 * scale[0], -
              91.0 * scale[1], 5.0 * scale[0], -130.0 * scale[1])
    Lineto_r(-7.0 * scale[0], -67.0 * scale[1])
    Lineto_r(39.0 * scale[0], -4.0 * scale[1])
    Curveto_r(21.0 * scale[0], -3.0 * scale[1], 49.0 * scale[0],
              0.0 * scale[1], 63.0 * scale[0], 7.0 * scale[1])
    Curveto_r(14.0 * scale[0], 6.0 * scale[1], 33.0 * scale[0],
              10.0 * scale[1], 43.0 * scale[0], 7.0 * scale[1])
    Curveto_r(11.0 * scale[0], -2.0 * scale[1], 28.0 * scale[0],
              6.0 * scale[1], 39.0 * scale[0], 17.0 * scale[1])
    Curveto_r(10.0 * scale[0], 12.0 * scale[1], 23.0 * scale[0],
              19.0 * scale[1], 29.0 * scale[0], 16.0 * scale[1])
    Curveto_r(14.0 * scale[0], -9.0 * scale[1], 28.0 * scale[0],
              38.0 * scale[1], 33.0 * scale[0], 115.0 * scale[1])
    Curveto_r(4.0 * scale[0], 65.0 * scale[1], -3.0 * scale[0],
              86.0 * scale[1], -19.0 * scale[0], 59.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -7.0 * scale[1], -15.0 *
              scale[0], -4.0 * scale[1], -29.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 11.0 * scale[1], -35.0 * scale[0],
              27.0 * scale[1], -53.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-34.0 * scale[0], 17.0 * scale[1], -119.0 * scale[0],
              21.0 * scale[1], -141.0 * scale[0], 7.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#aa7933')
    te.end_fill()
    Moveto(132.0 * scale[0], 1363.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -9.0 * scale[1], -32.0 * scale[0], -
              17.0 * scale[1], -45.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-35.0 * scale[0], -4.0 * scale[1], -37.0 *
              scale[0], -5.0 * scale[1], -37.0 * scale[0], -14.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 65.0 *
              scale[0], -5.0 * scale[1], 81.0 * scale[0], 5.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 9.0 * scale[0],
              1.0 * scale[1], 9.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -8.0 * scale[0], -
              12.0 * scale[1], -17.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -3.0 * scale[1], -2.0 *
              scale[0], -4.0 * scale[1], 18.0 * scale[0], -2.0 * scale[1])
    Curveto_r(40.0 * scale[0], 3.0 * scale[1], 54.0 * scale[0], -
              3.0 * scale[1], 54.0 * scale[0], -25.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 13.0 * scale[0], -
              18.0 * scale[1], 30.0 * scale[0], -21.0 * scale[1])
    Lineto_r(30.0 * scale[0], -7.0 * scale[1])
    Lineto_r(-27.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-23.0 * scale[0], -1.0 * scale[1], -27.0 *
              scale[0], -5.0 * scale[1], -24.0 * scale[0], -23.0 * scale[1])
    Curveto_r(2.0 * scale[0], -17.0 * scale[1], 10.0 * scale[0], -
              23.0 * scale[1], 27.0 * scale[0], -23.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 27.0 * scale[0], -
              4.0 * scale[1], 31.0 * scale[0], -10.0 * scale[1])
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 8.0 *
              scale[0], -2.0 * scale[1], 8.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], 4.0 * scale[0],
              15.0 * scale[1], 10.0 * scale[0], 12.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 19.0 * scale[0],
              6.0 * scale[1], 32.0 * scale[0], 20.0 * scale[1])
    Curveto_r(20.0 * scale[0], 23.0 * scale[1], 46.0 * scale[0],
              36.0 * scale[1], 34.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -4.0 * scale[1], -1.0 * scale[0], -
              14.0 * scale[1], 5.0 * scale[0], -22.0 * scale[1])
    Curveto_r(7.0 * scale[0], -13.0 * scale[1], 9.0 *
              scale[0], -12.0 * scale[1], 9.0 * scale[0], 2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], 8.0 * scale[0],
              22.0 * scale[1], 18.0 * scale[0], 27.0 * scale[1])
    Curveto_r(9.0 * scale[0], 6.0 * scale[1], 13.0 * scale[0],
              11.0 * scale[1], 7.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              11.0 * scale[1], 37.0 * scale[0], 25.0 * scale[1])
    Curveto_r(43.0 * scale[0], 23.0 * scale[1], 51.0 * scale[0],
              24.0 * scale[1], 86.0 * scale[0], 13.0 * scale[1])
    Curveto_r(25.0 * scale[0], -8.0 * scale[1], 47.0 * scale[0], -
              24.0 * scale[1], 60.0 * scale[0], -45.0 * scale[1])
    Curveto_r(13.0 * scale[0], -20.0 * scale[1], 27.0 * scale[0], -
              30.0 * scale[1], 36.0 * scale[0], -27.0 * scale[1])
    Curveto_r(13.0 * scale[0], 5.0 * scale[1], 96.0 * scale[0], -
              40.0 * scale[1], 96.0 * scale[0], -52.0 * scale[1])
    Curveto_r(0.0 * scale[0], -3.0 * scale[1], -4.0 *
              scale[0], -3.0 * scale[1], -9.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -17.0 * scale[0], -
              2.0 * scale[1], -25.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -8.0 * scale[1], -16.0 * scale[0], -
              13.0 * scale[1], -16.0 * scale[0], -9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0],
              1.0 * scale[1], -21.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -9.0 * scale[1], -24.0 *
              scale[0], -8.0 * scale[1], -37.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 11.0 * scale[1], -15.0 * scale[0],
              11.0 * scale[1], -9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(4.0 * scale[0], -12.0 * scale[1], 0.0 * scale[0], -
              21.0 * scale[1], -14.0 * scale[0], -28.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -6.0 * scale[1], -16.0 * scale[0], -
              16.0 * scale[1], -13.0 * scale[0], -22.0 * scale[1])
    Curveto_r(4.0 * scale[0], -7.0 * scale[1], 3.0 * scale[0], -
              8.0 * scale[1], -4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -12.0 * scale[0],
              3.0 * scale[1], -12.0 * scale[0], -2.0 * scale[1])
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], -90.0 * scale[0], -
              14.0 * scale[1], -113.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 8.0 * scale[1], -30.0 * scale[0],
              13.0 * scale[1], -40.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -1.0 * scale[1], -15.0 * scale[0],
              2.0 * scale[1], -11.0 * scale[0], 7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], 10.0 * scale[0],
              6.0 * scale[1], 17.0 * scale[0], 2.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 1.0 * scale[0],
              7.0 * scale[1], -11.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 17.0 * scale[1], -18.0 * scale[0],
              34.0 * scale[1], -14.0 * scale[0], 38.0 * scale[1])
    Curveto_r(4.0 * scale[0], 5.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -5.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -4.0 * scale[1], -13.0 * scale[0], -
              17.0 * scale[1], -13.0 * scale[0], -29.0 * scale[1])
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], -3.0 * scale[0], -
              18.0 * scale[1], -9.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 7.0 * scale[1], -15.0 * scale[0],
              14.0 * scale[1], -23.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 1.0 * scale[1], -22.0 * scale[0],
              7.0 * scale[1], -29.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 6.0 * scale[1], -33.0 * scale[0],
              11.0 * scale[1], -57.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-41.0 * scale[0], 1.0 * scale[1], -42.0 * scale[0],
              0.0 * scale[1], -29.0 * scale[0], -21.0 * scale[1])
    Curveto_r(8.0 * scale[0], -11.0 * scale[1], 27.0 * scale[0], -
              24.0 * scale[1], 43.0 * scale[0], -28.0 * scale[1])
    Curveto_r(20.0 * scale[0], -5.0 * scale[1], 16.0 * scale[0], -
              6.0 * scale[1], -13.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-28.0 * scale[0], 4.0 * scale[1], -43.0 * scale[0],
              1.0 * scale[1], -43.0 * scale[0], -6.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -7.0 * scale[0], -
              9.0 * scale[1], -14.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 4.0 * scale[1], -13.0 * scale[0],
              1.0 * scale[1], -10.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], -7.0 * scale[1], 20.0 * scale[0], -
              18.0 * scale[1], 37.0 * scale[0], -23.0 * scale[1])
    Curveto_r(27.0 * scale[0], -9.0 * scale[1], 23.0 * scale[0], -
              10.0 * scale[1], -28.0 * scale[0], -6.0 * scale[1])
    Lineto_r(-60.0 * scale[0], 3.0 * scale[1])
    Lineto_r(70.0 * scale[0], -33.0 * scale[1])
    Lineto_r(70.0 * scale[0], -34.0 * scale[1])
    Lineto_r(205.0 * scale[0], -1.0 * scale[1])
    Curveto_r(113.0 * scale[0], -1.0 * scale[1], 223.0 *
              scale[0], -5.0 * scale[1], 245.0 * scale[0], -8.0 * scale[1])
    Curveto_r(22.0 * scale[0], -3.0 * scale[1], 51.0 *
              scale[0], -1.0 * scale[1], 65.0 * scale[0], 5.0 * scale[1])
    Curveto_r(21.0 * scale[0], 8.0 * scale[1], 22.0 * scale[0],
              10.0 * scale[1], 5.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0],
              2.0 * scale[1], -5.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 32.0 * scale[0],
              7.0 * scale[1], 54.0 * scale[0], 3.0 * scale[1])
    Curveto_r(36.0 * scale[0], -6.0 * scale[1], 38.0 *
              scale[0], -5.0 * scale[1], 27.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 27.0 * scale[1], -48.0 * scale[0],
              37.0 * scale[1], -69.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -11.0 * scale[1], -15.0 *
              scale[0], -11.0 * scale[1], -6.0 * scale[0], 2.0 * scale[1])
    Curveto_r(7.0 * scale[0], 9.0 * scale[1], 8.0 * scale[0],
              23.0 * scale[1], 3.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 11.0 * scale[1], -8.0 * scale[0],
              16.0 * scale[1], -8.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -6.0 * scale[1], -7.0 *
              scale[0], -1.0 * scale[1], -15.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 10.0 * scale[1], -11.0 * scale[0],
              27.0 * scale[1], -8.0 * scale[0], 38.0 * scale[1])
    Curveto_r(3.0 * scale[0], 10.0 * scale[1], -1.0 * scale[0],
              23.0 * scale[1], -9.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 7.0 * scale[1], -11.0 *
              scale[0], 9.0 * scale[1], 3.0 * scale[0], 9.0 * scale[1])
    Curveto_r(18.0 * scale[0], 0.0 * scale[1], 33.0 * scale[0],
              33.0 * scale[1], 23.0 * scale[0], 50.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], -1.0 * scale[0],
              11.0 * scale[1], 4.0 * scale[0], 11.0 * scale[1])
    Curveto_r(6.0 * scale[0], 1.0 * scale[1], 17.0 * scale[0],
              2.0 * scale[1], 24.0 * scale[0], 3.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              8.0 * scale[1], 12.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 11.0 * scale[0],
              17.0 * scale[1], 25.0 * scale[0], 20.0 * scale[1])
    Curveto_r(21.0 * scale[0], 6.0 * scale[1], 11.0 * scale[0],
              11.0 * scale[1], -55.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-73.0 * scale[0], 23.0 * scale[1], -96.0 * scale[0],
              25.0 * scale[1], -250.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-151.0 * scale[0], 0.0 * scale[1], -168.0 *
              scale[0], -2.0 * scale[1], -151.0 * scale[0], -14.0 * scale[1])
    Curveto_r(25.0 * scale[0], -19.0 * scale[1], 9.0 * scale[0], -
              19.0 * scale[1], -24.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-36.0 * scale[0], 21.0 * scale[1], -187.0 * scale[0],
              19.0 * scale[1], -218.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto_r(555.0 * scale[0], -39.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 17.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(-359.0 * scale[0], -191.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -2.0 * scale[1], -26.0 *
              scale[0], -2.0 * scale[1], -35.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              5.0 * scale[1], 17.0 * scale[0], 5.0 * scale[1])
    Curveto_r(19.0 * scale[0], 0.0 * scale[1], 27.0 * scale[0], -
              2.0 * scale[1], 18.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(-61.0 * scale[0], -49.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 17.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(853.0 * scale[0], 1353.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 25.0 *
              scale[0], -2.0 * scale[1], 35.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -27.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(27.0 * scale[0], 1343.0 * scale[1], x, y)
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
    Moveto(895.0 * scale[0], 1090.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -11.0 * scale[1], -15.0 *
              scale[0], -20.0 * scale[1], -11.0 * scale[0], -20.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 39.0 * scale[0],
              30.0 * scale[1], 34.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 2.0 * scale[1], -13.0 * scale[0], -
              5.0 * scale[1], -23.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(855.0 * scale[0], 1090.0 * scale[1], x, y)
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
    Moveto(64.0 * scale[0], 1078.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], -2.0 *
              scale[0], -7.0 * scale[1], 3.0 * scale[0], -6.0 * scale[1])
    Curveto_r(4.0 * scale[0], 1.0 * scale[1], 30.0 * scale[0], -
              8.0 * scale[1], 58.0 * scale[0], -20.0 * scale[1])
    Curveto_r(27.0 * scale[0], -13.0 * scale[1], 59.0 * scale[0], -
              21.0 * scale[1], 70.0 * scale[0], -19.0 * scale[1])
    Curveto_r(18.0 * scale[0], 3.0 * scale[1], 18.0 * scale[0],
              4.0 * scale[1], -5.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-51.0 * scale[0], 23.0 * scale[1], -121.0 * scale[0],
              40.0 * scale[1], -126.0 * scale[0], 31.0 * scale[1])
    te.end_fill()
    Moveto(365.0 * scale[0], 790.0 * scale[1], x, y)
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
    Moveto(437.0 * scale[0], 298.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -18.0 * scale[1], -27.0 * scale[0], -
              50.0 * scale[1], -41.0 * scale[0], -71.0 * scale[1])
    Curveto_r(-28.0 * scale[0], -41.0 * scale[1], -32.0 *
              scale[0], -52.0 * scale[1], -15.0 * scale[0], -41.0 * scale[1])
    Curveto_r(8.0 * scale[0], 4.0 * scale[1], 8.0 * scale[0],
              0.0 * scale[1], 0.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -19.0 * scale[1], -22.0 *
              scale[0], -25.0 * scale[1], -42.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 1.0 * scale[1], -4.0 * scale[0], -
              9.0 * scale[1], -2.0 * scale[0], -22.0 * scale[1])
    Curveto_r(4.0 * scale[0], -17.0 * scale[1], -1.0 * scale[0], -
              25.0 * scale[1], -16.0 * scale[0], -29.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -3.0 * scale[1], -21.0 * scale[0], -
              13.0 * scale[1], -21.0 * scale[0], -22.0 * scale[1])
    Curveto_r(0.0 * scale[0], -26.0 * scale[1], 22.0 * scale[0], -
              12.0 * scale[1], 43.0 * scale[0], 28.0 * scale[1])
    Curveto_r(10.0 * scale[0], 20.0 * scale[1], 25.0 * scale[0],
              37.0 * scale[1], 32.0 * scale[0], 37.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 21.0 * scale[0],
              23.0 * scale[1], 31.0 * scale[0], 50.0 * scale[1])
    Curveto_r(10.0 * scale[0], 28.0 * scale[1], 21.0 * scale[0],
              50.0 * scale[1], 26.0 * scale[0], 50.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 32.0 * scale[0],
              80.0 * scale[1], 25.0 * scale[0], 86.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 3.0 * scale[1], -11.0 * scale[0], -
              10.0 * scale[1], -20.0 * scale[0], -28.0 * scale[1])
    te.end_fill()
    Moveto(175.0 * scale[0], 280.0 * scale[1], x, y)
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
    Moveto(266.0 * scale[0], 33.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#6c4e95')
    te.end_fill()
    Moveto(401.0 * scale[0], 1163.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -12.0 * scale[1], 15.0 * scale[0], -
              20.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(3.0 * scale[0], 2.0 * scale[1], -3.0 * scale[0],
              12.0 * scale[1], -13.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 16.0 * scale[1], -18.0 * scale[0],
              16.0 * scale[1], -5.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(450.0 * scale[0], 1130.0 * scale[1], x, y)
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
    Moveto(0.0 * scale[0], 976.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -25.0 * scale[1], 4.0 * scale[0], -
              48.0 * scale[1], 10.0 * scale[0], -51.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 10.0 * scale[1], -1.0 * scale[0],
              16.0 * scale[1], 7.0 * scale[0], 16.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              3.0 * scale[1], 6.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              12.0 * scale[1], 11.0 * scale[0], 19.0 * scale[1])
    Curveto_r(18.0 * scale[0], 13.0 * scale[1], 47.0 * scale[0],
              0.0 * scale[1], 36.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 0.0 *
              scale[0], -8.0 * scale[1], 8.0 * scale[0], -7.0 * scale[1])
    Curveto_r(7.0 * scale[0], 2.0 * scale[1], 12.0 * scale[0], -
              3.0 * scale[1], 10.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -8.0 * scale[1], 2.0 * scale[0], -
              11.0 * scale[1], 7.0 * scale[0], -8.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 8.0 * scale[0], -
              5.0 * scale[1], 7.0 * scale[0], -19.0 * scale[1])
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], -5.0 * scale[0], -
              25.0 * scale[1], -9.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -5.0 * scale[0], -
              4.0 * scale[1], -2.0 * scale[0], -10.0 * scale[1])
    Curveto_r(9.0 * scale[0], -15.0 * scale[1], 25.0 *
              scale[0], -12.0 * scale[1], 25.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 4.0 * scale[0],
              13.0 * scale[1], 8.0 * scale[0], 10.0 * scale[1])
    Curveto_r(4.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0],
              4.0 * scale[1], 8.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], -4.0 * scale[0],
              16.0 * scale[1], -9.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -8.0 * scale[0],
              1.0 * scale[1], -6.0 * scale[0], 8.0 * scale[1])
    Curveto_r(3.0 * scale[0], 24.0 * scale[1], -1.0 * scale[0],
              40.0 * scale[1], -8.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -2.0 * scale[1], -18.0 * scale[0],
              6.0 * scale[1], -31.0 * scale[0], 19.0 * scale[1])
    Lineto_r(-22.0 * scale[0], 23.0 * scale[1])
    Lineto_r(157.0 * scale[0], 4.0 * scale[1])
    Lineto_r(158.0 * scale[0], 3.0 * scale[1])
    Lineto_r(-187.0 * scale[0], 2.0 * scale[1])
    Lineto_r(-188.0 * scale[0], 2.0 * scale[1])
    Lineto_r(0.0 * scale[0], -44.0 * scale[1])
    te.end_fill()
    Moveto_r(46.0 * scale[0], 27.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -11.0 * scale[1], -36.0 *
              scale[0], -12.0 * scale[1], -36.0 * scale[0], -2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 10.0 * scale[0],
              9.0 * scale[1], 22.0 * scale[0], 9.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 18.0 * scale[0], -
              3.0 * scale[1], 14.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(470.0 * scale[0], 1011.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(22.0 * scale[0], -6.0 * scale[1], 25.0 * scale[0], -
              12.0 * scale[1], 25.0 * scale[0], -59.0 * scale[1])
    Curveto_r(1.0 * scale[0], -49.0 * scale[1], -1.0 * scale[0], -
              52.0 * scale[1], -25.0 * scale[0], -53.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -1.0 * scale[1], -32.0 *
              scale[0], -2.0 * scale[1], -40.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -1.0 * scale[1], -27.0 * scale[0],
              7.0 * scale[1], -41.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 17.0 * scale[1], -27.0 * scale[0],
              17.0 * scale[1], -33.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -32.0 * scale[1], 62.0 * scale[0], -
              56.0 * scale[1], 124.0 * scale[0], -40.0 * scale[1])
    Curveto_r(19.0 * scale[0], 5.0 * scale[1], 49.0 * scale[0],
              10.0 * scale[1], 67.0 * scale[0], 11.0 * scale[1])
    Curveto_r(17.0 * scale[0], 0.0 * scale[1], 29.0 * scale[0],
              4.0 * scale[1], 27.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], 7.0 * scale[0],
              15.0 * scale[1], 21.0 * scale[0], 24.0 * scale[1])
    Curveto_r(32.0 * scale[0], 21.0 * scale[1], 32.0 * scale[0],
              32.0 * scale[1], 0.0 * scale[0], 44.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 6.0 * scale[1], -23.0 * scale[0],
              15.0 * scale[1], -19.0 * scale[0], 24.0 * scale[1])
    Curveto_r(3.0 * scale[0], 9.0 * scale[1], -2.0 * scale[0],
              16.0 * scale[1], -13.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 2.0 * scale[1], -7.0 * scale[0],
              3.0 * scale[1], 7.0 * scale[0], 0.0 * scale[1])
    Curveto_r(14.0 * scale[0], -2.0 * scale[1], 103.0 *
              scale[0], -3.0 * scale[1], 198.0 * scale[0], -3.0 * scale[1])
    Lineto_r(172.0 * scale[0], 1.0 * scale[1])
    Lineto_r(0.0 * scale[0], -145.0 * scale[1])
    Curveto_r(0.0 * scale[0], -106.0 * scale[1], -3.0 * scale[0], -
              145.0 * scale[1], -12.0 * scale[0], -148.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -3.0 * scale[1], -8.0 *
              scale[0], -9.0 * scale[1], 5.0 * scale[0], -22.0 * scale[1])
    Curveto_r(16.0 * scale[0], -17.0 * scale[1], 17.0 *
              scale[0], -9.0 * scale[1], 17.0 * scale[0], 149.0 * scale[1])
    Curveto_r(0.0 * scale[0], 124.0 * scale[1], -3.0 * scale[0],
              167.0 * scale[1], -12.0 * scale[0], 169.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 3.0 * scale[1], -121.0 * scale[0],
              7.0 * scale[1], -253.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-132.0 * scale[0], 3.0 * scale[1], -229.0 * scale[0],
              2.0 * scale[1], -215.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(460.0 * scale[0], 930.0 * scale[1], x, y)
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
    Moveto(7.0 * scale[0], 903.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -16.0 * scale[1], -7.0 * scale[0], -
              112.0 * scale[1], 2.0 * scale[0], -117.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              4.0 * scale[1], 3.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 16.0 * scale[1], -2.0 * scale[0],
              19.0 * scale[1], 8.0 * scale[0], 13.0 * scale[1])
    Curveto_r(7.0 * scale[0], -5.0 * scale[1], 11.0 *
              scale[0], -4.0 * scale[1], 7.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 20.0 * scale[1], 19.0 * scale[0],
              44.0 * scale[1], 53.0 * scale[0], 39.0 * scale[1])
    Curveto_r(19.0 * scale[0], -2.0 * scale[1], 29.0 * scale[0],
              0.0 * scale[1], 24.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 5.0 * scale[1], -27.0 * scale[0],
              10.0 * scale[1], -49.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-32.0 * scale[0], 2.0 * scale[1], -39.0 * scale[0],
              7.0 * scale[1], -37.0 * scale[0], 21.0 * scale[1])
    Curveto_r(3.0 * scale[0], 17.0 * scale[1], -3.0 * scale[0],
              23.0 * scale[1], -11.0 * scale[0], 10.0 * scale[1])
    te.end_fill()
    Moveto(275.0 * scale[0], 880.0 * scale[1], x, y)
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
    Moveto(598.0 * scale[0], 873.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(74.0 * scale[0], 826.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -9.0 * scale[1], 8.0 * scale[0], -
              22.0 * scale[1], 14.0 * scale[0], -28.0 * scale[1])
    Curveto_r(27.0 * scale[0], -27.0 * scale[1], 6.0 * scale[0], -
              68.0 * scale[1], -36.0 * scale[0], -68.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -26.0 * scale[0],
              7.0 * scale[1], -29.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 27.0 * scale[1], -23.0 * scale[0],
              5.0 * scale[1], -23.0 * scale[0], -31.0 * scale[1])
    Curveto_r(0.0 * scale[0], -17.0 * scale[1], 3.0 * scale[0], -
              21.0 * scale[1], 9.0 * scale[0], -12.0 * scale[1])
    Curveto_r(5.0 * scale[0], 9.0 * scale[1], 17.0 * scale[0],
              11.0 * scale[1], 35.0 * scale[0], 6.0 * scale[1])
    Curveto_r(36.0 * scale[0], -9.0 * scale[1], 66.0 * scale[0],
              19.0 * scale[1], 66.0 * scale[0], 61.0 * scale[1])
    Curveto_r(0.0 * scale[0], 23.0 * scale[1], 6.0 * scale[0],
              35.0 * scale[1], 23.0 * scale[0], 43.0 * scale[1])
    Curveto_r(20.0 * scale[0], 9.0 * scale[1], 20.0 * scale[0],
              10.0 * scale[1], 2.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -30.0 * scale[0],
              3.0 * scale[1], -42.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 5.0 * scale[1], -21.0 * scale[0],
              3.0 * scale[1], -19.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto_r(30.0 * scale[0], -17.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -10.0 *
              scale[0], -7.0 * scale[1], -15.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -7.0 * scale[0],
              10.0 * scale[1], -3.0 * scale[0], 15.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], 10.0 * scale[0],
              7.0 * scale[1], 15.0 * scale[0], 3.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0], -
              10.0 * scale[1], 3.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(308.0 * scale[0], 803.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(731.0 * scale[0], 699.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-1.0 * scale[0], -37.0 * scale[1])
    Lineto_r(38.0 * scale[0], 14.0 * scale[1])
    Curveto_r(20.0 * scale[0], 7.0 * scale[1], 51.0 * scale[0],
              14.0 * scale[1], 67.0 * scale[0], 15.0 * scale[1])
    Curveto_r(17.0 * scale[0], 0.0 * scale[1], 41.0 * scale[0],
              5.0 * scale[1], 55.0 * scale[0], 10.0 * scale[1])
    Curveto_r(17.0 * scale[0], 5.0 * scale[1], -3.0 * scale[0],
              7.0 * scale[1], -62.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-71.0 * scale[0], -2.0 * scale[1], -88.0 * scale[0],
              1.0 * scale[1], -92.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 8.0 * scale[1], -4.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -21.0 * scale[1])
    te.end_fill()
    Moveto(570.0 * scale[0], 650.0 * scale[1], x, y)
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
    Moveto(940.0 * scale[0], 545.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -54.0 * scale[1], -25.0 * scale[0], -
              91.0 * scale[1], -48.0 * scale[0], -72.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 20.0 * scale[1], -135.0 * scale[0],
              47.0 * scale[1], -149.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -7.0 * scale[1], -13.0 *
              scale[0], -5.0 * scale[1], -16.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 17.0 * scale[1], -5.0 * scale[0],
              17.0 * scale[1], -6.0 * scale[0], 1.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], -5.0 * scale[0], -
              18.0 * scale[1], -11.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              4.0 * scale[1], -10.0 * scale[0], -8.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 24.0 * scale[0], -
              7.0 * scale[1], 53.0 * scale[0], -4.0 * scale[1])
    Curveto_r(57.0 * scale[0], 5.0 * scale[1], 127.0 * scale[0], -
              21.0 * scale[1], 145.0 * scale[0], -54.0 * scale[1])
    Curveto_r(7.0 * scale[0], -13.0 * scale[1], 13.0 * scale[0], -
              14.0 * scale[1], 31.0 * scale[0], -5.0 * scale[1])
    Curveto_r(19.0 * scale[0], 10.0 * scale[1], 21.0 * scale[0],
              20.0 * scale[1], 21.0 * scale[0], 86.0 * scale[1])
    Curveto_r(0.0 * scale[0], 41.0 * scale[1], -2.0 * scale[0],
              75.0 * scale[1], -5.0 * scale[0], 75.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -5.0 * scale[0], -
              20.0 * scale[1], -5.0 * scale[0], -45.0 * scale[1])
    te.end_fill()
    Moveto(2.0 * scale[0], 138.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(3.0 * scale[0], -133.0 * scale[1])
    Lineto_r(111.0 * scale[0], -3.0 * scale[1])
    Lineto_r(111.0 * scale[0], -3.0 * scale[1])
    Lineto_r(-5.0 * scale[0], 73.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 80.0 * scale[1], -16.0 * scale[0],
              112.0 * scale[1], -37.0 * scale[0], 104.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -16.0 * scale[0],
              5.0 * scale[1], -20.0 * scale[0], 17.0 * scale[1])
    Lineto_r(-6.0 * scale[0], 22.0 * scale[1])
    Lineto_r(-10.0 * scale[0], -24.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -33.0 * scale[1], -21.0 *
              scale[0], -21.0 * scale[1], -10.0 * scale[0], 17.0 * scale[1])
    Curveto_r(8.0 * scale[0], 26.0 * scale[1], 7.0 * scale[0],
              30.0 * scale[1], -7.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -5.0 * scale[1], -13.0 *
              scale[0], -3.0 * scale[1], -7.0 * scale[0], 8.0 * scale[1])
    Curveto_r(6.0 * scale[0], 11.0 * scale[1], 5.0 * scale[0],
              12.0 * scale[1], -5.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -9.0 * scale[1], -10.0 *
              scale[0], -16.0 * scale[1], -2.0 * scale[0], -25.0 * scale[1])
    Curveto_r(8.0 * scale[0], -11.0 * scale[1], 6.0 * scale[0], -
              14.0 * scale[1], -9.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -19.0 * scale[0],
              5.0 * scale[1], -14.0 * scale[0], 23.0 * scale[1])
    Curveto_r(5.0 * scale[0], 20.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], -25.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 0.0 * scale[1], -40.0 * scale[0],
              5.0 * scale[1], -51.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 10.0 * scale[1], -20.0 * scale[0],
              7.0 * scale[1], -17.0 * scale[0], -123.0 * scale[1])
    te.end_fill()
    Moveto_r(48.0 * scale[0], 82.0 * scale[1], 0, 0)
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
    Moveto(942.0 * scale[0], 204.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -6.0 * scale[1], -15.0 * scale[0], -
              17.0 * scale[1], -32.0 * scale[0], -24.0 * scale[1])
    Curveto_r(-37.0 * scale[0], -15.0 * scale[1], -107.0 * scale[0], -
              90.0 * scale[1], -126.0 * scale[0], -135.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -24.0 * scale[1], -21.0 *
              scale[0], -35.0 * scale[1], -41.0 * scale[0], -38.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -2.0 * scale[1], 20.0 *
              scale[0], -5.0 * scale[1], 78.0 * scale[0], -6.0 * scale[1])
    Curveto_r(81.0 * scale[0], -1.0 * scale[1], 109.0 * scale[0],
              2.0 * scale[1], 118.0 * scale[0], 13.0 * scale[1])
    Curveto_r(8.0 * scale[0], 9.0 * scale[1], 11.0 * scale[0],
              47.0 * scale[1], 8.0 * scale[0], 107.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 52.0 * scale[1], -4.0 * scale[0],
              89.0 * scale[1], -5.0 * scale[0], 83.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#f2d7e0')
    te.end_fill()
    Moveto(118.0 * scale[0], 1303.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(520.0 * scale[0], 1306.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(70.0 * scale[0], 1275.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -14.0 * scale[1], -22.0 *
              scale[0], -27.0 * scale[1], -19.0 * scale[0], -29.0 * scale[1])
    Curveto_r(2.0 * scale[0], -2.0 * scale[1], 14.0 * scale[0],
              10.0 * scale[1], 27.0 * scale[0], 25.0 * scale[1])
    Curveto_r(29.0 * scale[0], 36.0 * scale[1], 24.0 * scale[0],
              38.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(815.0 * scale[0], 1290.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(120.0 * scale[0], 1286.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(451.0 * scale[0], 1281.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -5.0 * scale[1], -22.0 * scale[0], -
              26.0 * scale[1], -31.0 * scale[0], -46.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -34.0 * scale[1], -16.0 *
              scale[0], -40.0 * scale[1], -2.0 * scale[0], -67.0 * scale[1])
    Curveto_r(12.0 * scale[0], -26.0 * scale[1], 12.0 *
              scale[0], -32.0 * scale[1], 1.0 * scale[0], -40.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -7.0 * scale[1], -8.0 *
              scale[0], -8.0 * scale[1], 6.0 * scale[0], -2.0 * scale[1])
    Curveto_r(11.0 * scale[0], 4.0 * scale[1], 34.0 * scale[0],
              8.0 * scale[1], 52.0 * scale[0], 8.0 * scale[1])
    Curveto_r(42.0 * scale[0], 2.0 * scale[1], 58.0 * scale[0],
              17.0 * scale[1], 44.0 * scale[0], 43.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 14.0 * scale[1], -7.0 * scale[0],
              23.0 * scale[1], 1.0 * scale[0], 31.0 * scale[1])
    Curveto_r(17.0 * scale[0], 17.0 * scale[1], -21.0 * scale[0],
              74.0 * scale[1], -45.0 * scale[0], 66.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -4.0 * scale[1], -17.0 *
              scale[0], -2.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(9.0 * scale[0], 13.0 * scale[1], 6.0 * scale[0],
              14.0 * scale[1], -13.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(891.0 * scale[0], 1273.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -12.0 * scale[1], 15.0 * scale[0], -
              20.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(3.0 * scale[0], 2.0 * scale[1], -3.0 * scale[0],
              12.0 * scale[1], -13.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 16.0 * scale[1], -18.0 * scale[0],
              16.0 * scale[1], -5.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(780.0 * scale[0], 1259.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -11.0 * scale[1], -10.0 *
              scale[0], -23.0 * scale[1], -7.0 * scale[0], -25.0 * scale[1])
    Curveto_r(2.0 * scale[0], -2.0 * scale[1], 9.0 * scale[0],
              7.0 * scale[1], 15.0 * scale[0], 21.0 * scale[1])
    Curveto_r(14.0 * scale[0], 30.0 * scale[1], 7.0 * scale[0],
              33.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(180.0 * scale[0], 1221.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -50.0 * scale[1], -30.0 * scale[0], -
              88.0 * scale[1], -73.0 * scale[0], -94.0 * scale[1])
    Lineto_r(-32.0 * scale[0], -4.0 * scale[1])
    Lineto_r(32.0 * scale[0], -1.0 * scale[1])
    Curveto_r(43.0 * scale[0], -3.0 * scale[1], 83.0 * scale[0],
              44.0 * scale[1], 83.0 * scale[0], 99.0 * scale[1])
    Curveto_r(0.0 * scale[0], 21.0 * scale[1], -2.0 * scale[0],
              39.0 * scale[1], -5.0 * scale[0], 39.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -5.0 * scale[0], -
              17.0 * scale[1], -5.0 * scale[0], -39.0 * scale[1])
    te.end_fill()
    Moveto(93.0 * scale[0], 1235.0 * scale[1], x, y)
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
    Moveto(131.0 * scale[0], 1234.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(819.0 * scale[0], 1233.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 3.0 * scale[0], -5.0 * scale[1])
    Curveto_r(20.0 * scale[0], 16.0 * scale[1], 38.0 * scale[0],
              8.0 * scale[1], 39.0 * scale[0], -16.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 2.0 * scale[0], -
              12.0 * scale[1], 6.0 * scale[0], -4.0 * scale[1])
    Curveto_r(5.0 * scale[0], 13.0 * scale[1], -13.0 * scale[0],
              42.0 * scale[1], -27.0 * scale[0], 42.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0], -
              8.0 * scale[1], -21.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(42.0 * scale[0], 1205.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(372.0 * scale[0], 1210.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(762.0 * scale[0], 1200.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(811.0 * scale[0], 1194.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(842.0 * scale[0], 1174.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -8.0 * scale[1], -8.0 * scale[0], -
              14.0 * scale[1], -3.0 * scale[0], -14.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 25.0 * scale[0],
              19.0 * scale[1], 20.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 1.0 * scale[1], -10.0 * scale[0], -
              3.0 * scale[1], -17.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(50.0 * scale[0], 1161.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 18.0 * scale[1], -14.0 * scale[0],
              21.0 * scale[1], -14.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(828.0 * scale[0], 1113.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(36.0 * scale[0], 958.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-22.0 * scale[0], -31.0 * scale[1], -20.0 *
              scale[0], -65.0 * scale[1], 3.0 * scale[0], -78.0 * scale[1])
    Curveto_r(49.0 * scale[0], -26.0 * scale[1], 76.0 * scale[0],
              25.0 * scale[1], 37.0 * scale[0], 70.0 * scale[1])
    Lineto_r(-25.0 * scale[0], 30.0 * scale[1])
    Lineto_r(-15.0 * scale[0], -22.0 * scale[1])
    te.end_fill()
    Moveto(36.0 * scale[0], 819.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-38.0 * scale[0], -55.0 * scale[1], 3.0 * scale[0], -
              118.0 * scale[1], 48.0 * scale[0], -73.0 * scale[1])
    Curveto_r(19.0 * scale[0], 19.0 * scale[1], 20.0 * scale[0],
              29.0 * scale[1], 3.0 * scale[0], 46.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 7.0 * scale[1], -18.0 * scale[0],
              21.0 * scale[1], -24.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 18.0 * scale[1], -11.0 * scale[0],
              17.0 * scale[1], -27.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(593.0 * scale[0], 828.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -7.0 * scale[1], -6.0 * scale[0], -
              12.0 * scale[1], -15.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 3.0 * scale[1], -97.0 * scale[0], -
              39.0 * scale[1], -133.0 * scale[0], -72.0 * scale[1])
    Curveto_r(-23.0 * scale[0], -22.0 * scale[1], -24.0 *
              scale[0], -24.0 * scale[1], -6.0 * scale[0], -19.0 * scale[1])
    Curveto_r(28.0 * scale[0], 7.0 * scale[1], 27.0 * scale[0], -
              11.0 * scale[1], -1.0 * scale[0], -30.0 * scale[1])
    Lineto_r(-23.0 * scale[0], -16.0 * scale[1])
    Lineto_r(23.0 * scale[0], 6.0 * scale[1])
    Curveto_r(17.0 * scale[0], 4.0 * scale[1], 21.0 * scale[0],
              2.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -1.0 * scale[0], -
              18.0 * scale[1], 5.0 * scale[0], -22.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 9.0 * scale[0],
              0.0 * scale[1], 5.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 11.0 * scale[1], 2.0 * scale[0],
              14.0 * scale[1], 28.0 * scale[0], 11.0 * scale[1])
    Curveto_r(24.0 * scale[0], -3.0 * scale[1], 29.0 *
              scale[0], -1.0 * scale[1], 18.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -10.0 * scale[0],
              10.0 * scale[1], -5.0 * scale[0], 10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 3.0 * scale[0],
              4.0 * scale[1], -5.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 6.0 * scale[1], -17.0 * scale[0],
              5.0 * scale[1], -23.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -7.0 * scale[1], -6.0 *
              scale[0], -4.0 * scale[1], -2.0 * scale[0], 8.0 * scale[1])
    Curveto_r(4.0 * scale[0], 11.0 * scale[1], 8.0 * scale[0],
              25.0 * scale[1], 8.0 * scale[0], 32.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], 4.0 * scale[0],
              10.0 * scale[1], 9.0 * scale[0], 7.0 * scale[1])
    Curveto_r(4.0 * scale[0], -3.0 * scale[1], 8.0 * scale[0],
              2.0 * scale[1], 8.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], 10.0 * scale[0],
              16.0 * scale[1], 34.0 * scale[0], 16.0 * scale[1])
    Curveto_r(42.0 * scale[0], 0.0 * scale[1], 62.0 * scale[0], -
              21.0 * scale[1], 46.0 * scale[0], -49.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -25.0 * scale[1], -60.0 *
              scale[0], -29.0 * scale[1], -60.0 * scale[0], -6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -7.0 * scale[0],
              15.0 * scale[1], -15.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -6.0 * scale[1], 4.0 * scale[0], -29.0 * scale[1])
    Curveto_r(11.0 * scale[0], -11.0 * scale[1], 23.0 * scale[0], -
              16.0 * scale[1], 27.0 * scale[0], -13.0 * scale[1])
    Curveto_r(4.0 * scale[0], 4.0 * scale[1], -3.0 * scale[0], -
              8.0 * scale[1], -15.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-26.0 * scale[0], -39.0 * scale[1], -26.0 *
              scale[0], -39.0 * scale[1], 32.0 * scale[0], -14.0 * scale[1])
    Curveto_r(38.0 * scale[0], 16.0 * scale[1], 45.0 * scale[0],
              23.0 * scale[1], 40.0 * scale[0], 41.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 11.0 * scale[1], -2.0 * scale[0],
              20.0 * scale[1], 3.0 * scale[0], 19.0 * scale[1])
    Curveto_r(13.0 * scale[0], -4.0 * scale[1], 84.0 * scale[0],
              41.0 * scale[1], 84.0 * scale[0], 53.0 * scale[1])
    Curveto_r(0.0 * scale[0], 19.0 * scale[1], -21.0 * scale[0],
              48.0 * scale[1], -34.0 * scale[0], 48.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0],
              7.0 * scale[1], -20.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 18.0 * scale[1], -37.0 * scale[0],
              20.0 * scale[1], -33.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(596.0 * scale[0], 649.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-15.0 * scale[0], -9.0 * scale[1], -16.0 *
              scale[0], -13.0 * scale[1], -5.0 * scale[0], -20.0 * scale[1])
    Curveto_r(11.0 * scale[0], -7.0 * scale[1], 10.0 *
              scale[0], -9.0 * scale[1], -3.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -22.0 * scale[0], -
              11.0 * scale[1], -12.0 * scale[0], -47.0 * scale[1])
    Curveto_r(9.0 * scale[0], -34.0 * scale[1], 21.0 * scale[0], -
              28.0 * scale[1], 31.0 * scale[0], 15.0 * scale[1])
    Curveto_r(5.0 * scale[0], 20.0 * scale[1], 15.0 * scale[0],
              36.0 * scale[1], 21.0 * scale[0], 35.0 * scale[1])
    Curveto_r(7.0 * scale[0], -2.0 * scale[1], 11.0 * scale[0],
              3.0 * scale[1], 10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 6.0 * scale[1], 3.0 * scale[0],
              11.0 * scale[1], 10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(8.0 * scale[0], -1.0 * scale[1], 11.0 * scale[0],
              2.0 * scale[1], 7.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 13.0 * scale[1], -35.0 * scale[0],
              12.0 * scale[1], -59.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(535.0 * scale[0], 620.0 * scale[1], x, y)
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
    Moveto(360.0 * scale[0], 530.0 * scale[1], x, y)
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
    te.color('#b26081')
    te.end_fill()
    Moveto(458.0 * scale[0], 1302.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -2.0 * scale[1], -18.0 *
              scale[0], -8.0 * scale[1], -18.0 * scale[0], -13.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -4.0 * scale[0], -
              8.0 * scale[1], -9.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 14.0 * scale[1], -61.0 * scale[0], -
              69.0 * scale[1], -45.0 * scale[0], -96.0 * scale[1])
    Curveto_r(5.0 * scale[0], -7.0 * scale[1], 9.0 * scale[0], -
              19.0 * scale[1], 10.0 * scale[0], -26.0 * scale[1])
    Curveto_r(2.0 * scale[0], -8.0 * scale[1], 5.0 * scale[0], -
              17.0 * scale[1], 9.0 * scale[0], -20.0 * scale[1])
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], 3.0 * scale[0],
              8.0 * scale[1], 0.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 20.0 * scale[1], 0.0 * scale[0],
              44.0 * scale[1], 9.0 * scale[0], 63.0 * scale[1])
    Curveto_r(13.0 * scale[0], 26.0 * scale[1], 14.0 * scale[0],
              28.0 * scale[1], 1.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -7.0 * scale[1], -15.0 *
              scale[0], -8.0 * scale[1], -15.0 * scale[0], -2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 18.0 * scale[0],
              19.0 * scale[1], 39.0 * scale[0], 30.0 * scale[1])
    Lineto_r(39.0 * scale[0], 21.0 * scale[1])
    Lineto_r(26.0 * scale[0], -32.0 * scale[1])
    Curveto_r(28.0 * scale[0], -34.0 * scale[1], 36.0 * scale[0], -
              103.0 * scale[1], 14.0 * scale[0], -125.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -17.0 * scale[1], -1.0 *
              scale[0], -27.0 * scale[1], 18.0 * scale[0], -11.0 * scale[1])
    Curveto_r(19.0 * scale[0], 16.0 * scale[1], 48.0 * scale[0],
              78.0 * scale[1], 40.0 * scale[0], 86.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -8.0 * scale[0], -
              6.0 * scale[1], -12.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -36.0 * scale[1], -28.0 *
              scale[0], -33.0 * scale[1], -21.0 * scale[0], 4.0 * scale[1])
    Curveto_r(4.0 * scale[0], 16.0 * scale[1], 2.0 * scale[0],
              32.0 * scale[1], -3.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0],
              14.0 * scale[1], -10.0 * scale[0], 23.0 * scale[1])
    Curveto_r(1.0 * scale[0], 14.0 * scale[1], 4.0 * scale[0],
              13.0 * scale[1], 20.0 * scale[0], -7.0 * scale[1])
    Curveto_r(11.0 * scale[0], -13.0 * scale[1], 20.0 * scale[0], -
              19.0 * scale[1], 20.0 * scale[0], -13.0 * scale[1])
    Curveto_r(0.0 * scale[0], 33.0 * scale[1], -70.0 * scale[0],
              74.0 * scale[1], -112.0 * scale[0], 64.0 * scale[1])
    te.end_fill()
    Moveto(105.0 * scale[0], 1290.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(880.0 * scale[0], 1271.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 18.0 * scale[1], -14.0 * scale[0],
              21.0 * scale[1], -14.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(99.0 * scale[0], 1253.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -21.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(166.0 * scale[0], 1257.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0], -
              15.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 0.0 * scale[0],
              11.0 * scale[1], -7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              8.0 * scale[1], -5.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(135.0 * scale[0], 1250.0 * scale[1], x, y)
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
    Moveto(785.0 * scale[0], 1239.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0], -
              12.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 17.0 * scale[1], 1.0 * scale[0],
              20.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(171.0 * scale[0], 1212.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -14.0 * scale[1], -5.0 * scale[0], -
              20.0 * scale[1], -12.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -17.0 * scale[0], -
              2.0 * scale[1], -24.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -18.0 * scale[1], -61.0 *
              scale[0], -40.0 * scale[1], -50.0 * scale[0], -22.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], 0.0 * scale[0],
              19.0 * scale[1], -5.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 22.0 * scale[1], -10.0 * scale[0],
              22.0 * scale[1], -6.0 * scale[0], 1.0 * scale[1])
    Curveto_r(2.0 * scale[0], -12.0 * scale[1], -1.0 * scale[0], -
              24.0 * scale[1], -6.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -2.0 * scale[1], -3.0 * scale[0], -
              12.0 * scale[1], 7.0 * scale[0], -21.0 * scale[1])
    Curveto_r(19.0 * scale[0], -20.0 * scale[1], 61.0 *
              scale[0], -19.0 * scale[1], 58.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 7.0 * scale[1], 4.0 * scale[0],
              10.0 * scale[1], 12.0 * scale[0], 7.0 * scale[1])
    Curveto_r(17.0 * scale[0], -7.0 * scale[1], 39.0 * scale[0],
              39.0 * scale[1], 32.0 * scale[0], 65.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 10.0 * scale[1], -5.0 * scale[0],
              7.0 * scale[1], -6.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(327.0 * scale[0], 1214.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -13.0 * scale[1], 2.0 * scale[0], -
              15.0 * scale[1], -18.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-28.0 * scale[0], 9.0 * scale[1], -24.0 * scale[0],
              3.0 * scale[1], 9.0 * scale[0], -14.0 * scale[1])
    Curveto_r(20.0 * scale[0], -11.0 * scale[1], 22.0 *
              scale[0], -9.0 * scale[1], 22.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -4.0 * scale[0],
              25.0 * scale[1], -10.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              7.0 * scale[1], -3.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(602.0 * scale[0], 1210.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(865.0 * scale[0], 1198.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -44.0 * scale[1], -47.0 *
              scale[0], -46.0 * scale[1], -56.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 17.0 * scale[1], -7.0 * scale[0],
              24.0 * scale[1], -8.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -6.0 * scale[0], -
              10.0 * scale[1], -13.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -10.0 * scale[0],
              4.0 * scale[1], -6.0 * scale[0], 0.0 * scale[1])
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], 2.0 * scale[0], -
              21.0 * scale[1], -2.0 * scale[0], -36.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -16.0 * scale[1], -5.0 * scale[0], -
              29.0 * scale[1], -2.0 * scale[0], -28.0 * scale[1])
    Curveto_r(4.0 * scale[0], 1.0 * scale[1], 17.0 * scale[0], -
              3.0 * scale[1], 29.0 * scale[0], -10.0 * scale[1])
    Curveto_r(35.0 * scale[0], -20.0 * scale[1], 80.0 * scale[0],
              8.0 * scale[1], 89.0 * scale[0], 53.0 * scale[1])
    Curveto_r(3.0 * scale[0], 20.0 * scale[1], 4.0 * scale[0],
              39.0 * scale[1], 0.0 * scale[0], 42.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -6.0 * scale[0], -13.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], -5.0 * scale[0], -
              26.0 * scale[1], -10.0 * scale[0], -34.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -11.0 * scale[1], -8.0 *
              scale[0], -6.0 * scale[1], -4.0 * scale[0], 18.0 * scale[1])
    Curveto_r(4.0 * scale[0], 17.0 * scale[1], 5.0 * scale[0],
              32.0 * scale[1], 2.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              15.0 * scale[1], -13.0 * scale[0], -32.0 * scale[1])
    te.end_fill()
    Moveto_r(-44.0 * scale[0], -48.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0], -
              3.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -10.0 * scale[1], -37.0 * scale[0],
              16.0 * scale[1], -36.0 * scale[0], 35.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], 3.0 * scale[0],
              9.0 * scale[1], 9.0 * scale[0], -6.0 * scale[1])
    Curveto_r(5.0 * scale[0], -13.0 * scale[1], 15.0 * scale[0], -
              23.0 * scale[1], 21.0 * scale[0], -23.0 * scale[1])
    te.end_fill()
    Moveto(52.0 * scale[0], 1200.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(620.0 * scale[0], 1205.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 7.0 * scale[0], -
              15.0 * scale[1], 18.0 * scale[0], -13.0 * scale[1])
    Curveto_r(21.0 * scale[0], 4.0 * scale[1], 19.0 * scale[0],
              22.0 * scale[1], -2.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 2.0 * scale[1], -16.0 * scale[0], -
              3.0 * scale[1], -16.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(446.0 * scale[0], 1118.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -11.0 * scale[1], 34.0 *
              scale[0], -10.0 * scale[1], 34.0 * scale[0], 1.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -9.0 * scale[0],
              9.0 * scale[1], -19.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -17.0 *
              scale[0], -5.0 * scale[1], -15.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(98.0 * scale[0], 1113.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(521.0 * scale[0], 886.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -2.0 * scale[1], 20.0 * scale[0], -
              6.0 * scale[1], 39.0 * scale[0], -10.0 * scale[1])
    Curveto_r(25.0 * scale[0], -4.0 * scale[1], 31.0 *
              scale[0], -3.0 * scale[1], 20.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 9.0 * scale[1], -69.0 * scale[0],
              15.0 * scale[1], -59.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(620.0 * scale[0], 871.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 6.0 * scale[0], -
              11.0 * scale[1], 13.0 * scale[0], -11.0 * scale[1])
    Curveto_r(17.0 * scale[0], -1.0 * scale[1], 52.0 * scale[0], -
              31.0 * scale[1], 60.0 * scale[0], -54.0 * scale[1])
    Curveto_r(10.0 * scale[0], -24.0 * scale[1], 18.0 *
              scale[0], -16.0 * scale[1], 11.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 21.0 * scale[1], -84.0 * scale[0],
              72.0 * scale[1], -84.0 * scale[0], 54.0 * scale[1])
    te.end_fill()
    Moveto(455.0 * scale[0], 859.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -5.0 * scale[1], -33.0 * scale[0], -
              13.0 * scale[1], -49.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -6.0 * scale[1], -27.0 * scale[0], -
              13.0 * scale[1], -24.0 * scale[0], -15.0 * scale[1])
    Curveto_r(6.0 * scale[0], -7.0 * scale[1], 97.0 * scale[0],
              25.0 * scale[1], 104.0 * scale[0], 36.0 * scale[1])
    Curveto_r(6.0 * scale[0], 11.0 * scale[1], -5.0 * scale[0],
              11.0 * scale[1], -31.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(191.0 * scale[0], 811.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(25.0 * scale[0], -16.0 * scale[1], 96.0 * scale[0], -
              25.0 * scale[1], 103.0 * scale[0], -12.0 * scale[1])
    Curveto_r(5.0 * scale[0], 7.0 * scale[1], -6.0 * scale[0],
              11.0 * scale[1], -31.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 0.0 * scale[1], -49.0 * scale[0],
              3.0 * scale[1], -63.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 4.0 * scale[1], -22.0 * scale[0],
              3.0 * scale[1], -9.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(348.0 * scale[0], 813.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(147.0 * scale[0], 789.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(340.0 * scale[0], 780.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(185.0 * scale[0], 770.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], -3.0 * scale[0], -
              14.0 * scale[1], -12.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-23.0 * scale[0], -15.0 * scale[1], 92.0 *
              scale[0], -6.0 * scale[1], 128.0 * scale[0], 10.0 * scale[1])
    Curveto_r(21.0 * scale[0], 9.0 * scale[1], 20.0 * scale[0],
              10.0 * scale[1], -11.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -2.0 * scale[1], -52.0 *
              scale[0], -1.0 * scale[1], -72.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 5.0 * scale[1], -36.0 * scale[0],
              5.0 * scale[1], -33.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(419.0 * scale[0], 733.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -13.0 * scale[1], -11.0 *
              scale[0], -17.0 * scale[1], -1.0 * scale[0], -21.0 * scale[1])
    Curveto_r(9.0 * scale[0], -3.0 * scale[1], 10.0 * scale[0], -
              7.0 * scale[1], 2.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -10.0 * scale[1], -8.0 *
              scale[0], -15.0 * scale[1], 2.0 * scale[0], -21.0 * scale[1])
    Curveto_r(7.0 * scale[0], -4.0 * scale[1], 10.0 *
              scale[0], -3.0 * scale[1], 5.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 5.0 * scale[1], 1.0 * scale[0],
              17.0 * scale[1], 10.0 * scale[0], 27.0 * scale[1])
    Curveto_r(10.0 * scale[0], 11.0 * scale[1], 13.0 * scale[0],
              19.0 * scale[1], 8.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-22.0 * scale[0], -5.0 * scale[1], -27.0 * scale[0],
              1.0 * scale[1], -15.0 * scale[0], 15.0 * scale[1])
    Curveto_r(7.0 * scale[0], 8.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              7.0 * scale[1], -18.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(260.0 * scale[0], 725.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-33.0 * scale[0], -11.0 * scale[1], -33.0 *
              scale[0], -12.0 * scale[1], -10.0 * scale[0], -18.0 * scale[1])
    Curveto_r(16.0 * scale[0], -4.0 * scale[1], 30.0 *
              scale[0], -1.0 * scale[1], 39.0 * scale[0], 8.0 * scale[1])
    Curveto_r(21.0 * scale[0], 21.0 * scale[1], 11.0 * scale[0],
              24.0 * scale[1], -29.0 * scale[0], 10.0 * scale[1])
    te.end_fill()
    Moveto(232.0 * scale[0], 675.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -15.0 * scale[1], -8.0 * scale[0], -
              26.0 * scale[1], -1.0 * scale[0], -30.0 * scale[1])
    Curveto_r(5.0 * scale[0], -4.0 * scale[1], 6.0 * scale[0], -
              12.0 * scale[1], 3.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], -1.0 *
              scale[0], -6.0 * scale[1], 7.0 * scale[0], 2.0 * scale[1])
    Curveto_r(11.0 * scale[0], 10.0 * scale[1], 11.0 * scale[0],
              15.0 * scale[1], 2.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 3.0 * scale[1], -8.0 * scale[0],
              11.0 * scale[1], 3.0 * scale[0], 29.0 * scale[1])
    Curveto_r(9.0 * scale[0], 13.0 * scale[1], 12.0 * scale[0],
              24.0 * scale[1], 7.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              11.0 * scale[1], -21.0 * scale[0], -25.0 * scale[1])
    te.end_fill()
    Moveto(485.0 * scale[0], 651.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              12.0 * scale[1], 3.0 * scale[0], -15.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 9.0 * scale[0],
              1.0 * scale[1], 9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], -3.0 * scale[0],
              19.0 * scale[1], -12.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(343.0 * scale[0], 618.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], -8.0 * scale[0], -
              17.0 * scale[1], -8.0 * scale[0], -22.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -6.0 * scale[0], -
              11.0 * scale[1], -14.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -3.0 * scale[1], -11.0 * scale[0],
              0.0 * scale[1], -7.0 * scale[0], 7.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              11.0 * scale[1], -3.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              4.0 * scale[1], -12.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -20.0 * scale[1], -4.0 * scale[0], -
              25.0 * scale[1], -13.0 * scale[0], -39.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -8.0 * scale[1], -5.0 *
              scale[0], -12.0 * scale[1], 0.0 * scale[0], -9.0 * scale[1])
    Curveto_r(5.0 * scale[0], 4.0 * scale[1], 9.0 * scale[0], -
              7.0 * scale[1], 9.0 * scale[0], -22.0 * scale[1])
    Curveto_r(0.0 * scale[0], -15.0 * scale[1], -3.0 * scale[0], -
              26.0 * scale[1], -7.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 2.0 * scale[1], -8.0 * scale[0], -
              3.0 * scale[1], -8.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 5.0 * scale[0], -
              16.0 * scale[1], 11.0 * scale[0], -16.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0], -
              5.0 * scale[1], 4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -1.0 *
              scale[0], -9.0 * scale[1], 7.0 * scale[0], -8.0 * scale[1])
    Curveto_r(7.0 * scale[0], 2.0 * scale[1], 12.0 * scale[0], -
              2.0 * scale[1], 11.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -6.0 * scale[1], 5.0 * scale[0], -
              10.0 * scale[1], 15.0 * scale[0], -8.0 * scale[1])
    Curveto_r(9.0 * scale[0], 2.0 * scale[1], 21.0 * scale[0],
              4.0 * scale[1], 25.0 * scale[0], 4.0 * scale[1])
    Curveto_r(5.0 * scale[0], 1.0 * scale[1], 6.0 * scale[0],
              5.0 * scale[1], 3.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], 1.0 * scale[0],
              11.0 * scale[1], 9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 14.0 * scale[0],
              0.0 * scale[1], 12.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 11.0 * scale[0], -15.0 * scale[1])
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 12.0 *
              scale[0], -1.0 * scale[1], 11.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 20.0 * scale[1], 2.0 * scale[0],
              30.0 * scale[1], 16.0 * scale[0], 30.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0], -
              6.0 * scale[1], 11.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -1.0 * scale[0], -
              16.0 * scale[1], 3.0 * scale[0], -19.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 14.0 * scale[0],
              9.0 * scale[1], 20.0 * scale[0], 26.0 * scale[1])
    Curveto_r(6.0 * scale[0], 17.0 * scale[1], 15.0 * scale[0],
              28.0 * scale[1], 21.0 * scale[0], 24.0 * scale[1])
    Curveto_r(7.0 * scale[0], -5.0 * scale[1], 8.0 * scale[0],
              2.0 * scale[1], 3.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 15.0 * scale[1], -7.0 * scale[0],
              38.0 * scale[1], -8.0 * scale[0], 50.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], -4.0 * scale[0],
              19.0 * scale[1], -8.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -17.0 * scale[0],
              4.0 * scale[1], -27.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 15.0 * scale[1], -16.0 * scale[0],
              22.0 * scale[1], -7.0 * scale[0], 25.0 * scale[1])
    Curveto_r(8.0 * scale[0], 4.0 * scale[1], 7.0 * scale[0],
              6.0 * scale[1], -2.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 1.0 * scale[1], -25.0 * scale[0], -
              9.0 * scale[1], -38.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -17.0 * scale[1], -26.0 *
              scale[0], -19.0 * scale[1], -36.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 10.0 * scale[1], -8.0 * scale[0],
              11.0 * scale[1], 8.0 * scale[0], 6.0 * scale[1])
    Curveto_r(17.0 * scale[0], -6.0 * scale[1], 18.0 *
              scale[0], -5.0 * scale[1], 5.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 10.0 * scale[1], -13.0 *
              scale[0], 11.0 * scale[1], 3.0 * scale[0], 6.0 * scale[1])
    Curveto_r(9.0 * scale[0], -3.0 * scale[1], 17.0 *
              scale[0], -1.0 * scale[1], 17.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -27.0 * scale[0],
              12.0 * scale[1], -37.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto_r(47.0 * scale[0], -83.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -9.0 * scale[0], -
              15.0 * scale[1], -20.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 0.0 * scale[1], -26.0 * scale[0],
              11.0 * scale[1], -13.0 * scale[0], 23.0 * scale[1])
    Curveto_r(12.0 * scale[0], 13.0 * scale[1], 33.0 * scale[0],
              7.0 * scale[1], 33.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(712.0 * scale[0], 595.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 4.0 * scale[0], -
              31.0 * scale[1], 8.0 * scale[0], -45.0 * scale[1])
    Curveto_r(6.0 * scale[0], -20.0 * scale[1], 8.0 * scale[0], -
              21.0 * scale[1], 8.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], -4.0 * scale[0],
              31.0 * scale[1], -8.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 20.0 * scale[1], -8.0 * scale[0],
              21.0 * scale[1], -8.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(260.0 * scale[0], 580.0 * scale[1], x, y)
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
    Moveto(240.0 * scale[0], 488.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-23.0 * scale[0], -33.0 * scale[1])
    Lineto_r(28.0 * scale[0], 28.0 * scale[1])
    Curveto_r(15.0 * scale[0], 16.0 * scale[1], 25.0 * scale[0],
              31.0 * scale[1], 22.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -15.0 * scale[0], -
              10.0 * scale[1], -27.0 * scale[0], -28.0 * scale[1])
    te.end_fill()
    Moveto(670.0 * scale[0], 475.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 6.0 * scale[0], -
              12.0 * scale[1], 15.0 * scale[0], -9.0 * scale[1])
    Curveto_r(8.0 * scale[0], 4.0 * scale[1], 15.0 * scale[0],
              10.0 * scale[1], 15.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -7.0 * scale[0],
              9.0 * scale[1], -15.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              7.0 * scale[1], -15.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(691.0 * scale[0], 324.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(166.0 * scale[0], 257.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0], -
              15.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 0.0 * scale[0],
              11.0 * scale[1], -7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              8.0 * scale[1], -5.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(676.0 * scale[0], 198.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -34.0 * scale[1], -12.0 * scale[0], -
              69.0 * scale[1], -20.0 * scale[0], -77.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -15.0 * scale[1], -17.0 *
              scale[0], -28.0 * scale[1], -32.0 * scale[0], -98.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -16.0 * scale[1], 8.0 * scale[0],
              1.0 * scale[1], 26.0 * scale[0], 37.0 * scale[1])
    Curveto_r(22.0 * scale[0], 45.0 * scale[1], 33.0 * scale[0],
              86.0 * scale[1], 37.0 * scale[0], 133.0 * scale[1])
    Curveto_r(7.0 * scale[0], 84.0 * scale[1], -2.0 * scale[0],
              89.0 * scale[1], -11.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(140.0 * scale[0], 221.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              11.0 * scale[1], 15.0 * scale[0], -15.0 * scale[1])
    Curveto_r(9.0 * scale[0], -3.0 * scale[1], 15.0 * scale[0],
              0.0 * scale[1], 15.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -7.0 * scale[0],
              15.0 * scale[1], -15.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              4.0 * scale[1], -15.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(200.0 * scale[0], 190.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 3.0 * scale[0], -
              21.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(9.0 * scale[0], 9.0 * scale[1], 9.0 * scale[0],
              15.0 * scale[1], 0.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 9.0 * scale[1], -12.0 * scale[0],
              7.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#dd9ca5')
    te.end_fill()
    Moveto(409.0 * scale[0], 1289.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -16.0 * scale[1], -26.0 *
              scale[0], -27.0 * scale[1], -16.0 * scale[0], -24.0 * scale[1])
    Curveto_r(14.0 * scale[0], 6.0 * scale[1], 16.0 * scale[0],
              3.0 * scale[1], 10.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -17.0 * scale[1], -5.0 *
              scale[0], -17.0 * scale[1], 11.0 * scale[0], -5.0 * scale[1])
    Curveto_r(13.0 * scale[0], 11.0 * scale[1], 14.0 * scale[0],
              16.0 * scale[1], 4.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 8.0 * scale[1], -4.0 * scale[0],
              13.0 * scale[1], 15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              6.0 * scale[1], 7.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 5.0 * scale[0],
              12.0 * scale[1], 11.0 * scale[0], 9.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 26.0 * scale[0], -
              8.0 * scale[1], 45.0 * scale[0], -9.0 * scale[1])
    Curveto_r(29.0 * scale[0], -1.0 * scale[1], 32.0 * scale[0],
              1.0 * scale[1], 19.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 12.0 * scale[1], -17.0 * scale[0],
              12.0 * scale[1], -29.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -8.0 * scale[1], -16.0 *
              scale[0], -9.0 * scale[1], -16.0 * scale[0], -1.0 * scale[1])
    Curveto_r(0.0 * scale[0], 20.0 * scale[1], -26.0 * scale[0],
              12.0 * scale[1], -61.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(104.0 * scale[0], 1296.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -15.0 * scale[1], 4.0 * scale[0], -
              17.0 * scale[1], -7.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 9.0 * scale[1], -17.0 * scale[0],
              8.0 * scale[1], -26.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -10.0 * scale[1], -7.0 *
              scale[0], -14.0 * scale[1], 4.0 * scale[0], -15.0 * scale[1])
    Curveto_r(8.0 * scale[0], -1.0 * scale[1], 22.0 * scale[0], -
              3.0 * scale[1], 30.0 * scale[0], -4.0 * scale[1])
    Curveto_r(8.0 * scale[0], -1.0 * scale[1], 12.0 *
              scale[0], -5.0 * scale[1], 9.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -4.0 * scale[1], 0.0 * scale[0], -
              10.0 * scale[1], 5.0 * scale[0], -13.0 * scale[1])
    Curveto_r(19.0 * scale[0], -12.0 * scale[1], 18.0 * scale[0],
              21.0 * scale[1], -2.0 * scale[0], 44.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 19.0 * scale[1], -19.0 * scale[0],
              20.0 * scale[1], -13.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(135.0 * scale[0], 1300.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -1.0 * scale[0], -
              18.0 * scale[1], 6.0 * scale[0], -26.0 * scale[1])
    Curveto_r(9.0 * scale[0], -11.0 * scale[1], 9.0 * scale[0], -
              20.0 * scale[1], 1.0 * scale[0], -40.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -20.0 * scale[1], -9.0 *
              scale[0], -26.0 * scale[1], 2.0 * scale[0], -30.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 14.0 * scale[0], -
              11.0 * scale[1], 12.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -7.0 * scale[1], -1.0 *
              scale[0], -8.0 * scale[1], 2.0 * scale[0], -4.0 * scale[1])
    Curveto_r(2.0 * scale[0], 4.0 * scale[1], 11.0 * scale[0],
              2.0 * scale[1], 20.0 * scale[0], -5.0 * scale[1])
    Curveto_r(15.0 * scale[0], -12.0 * scale[1], 16.0 *
              scale[0], -11.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 10.0 * scale[1], -11.0 * scale[0],
              26.0 * scale[1], -8.0 * scale[0], 37.0 * scale[1])
    Curveto_r(2.0 * scale[0], 10.0 * scale[1], 0.0 * scale[0],
              25.0 * scale[1], -4.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], -5.0 * scale[0],
              18.0 * scale[1], 1.0 * scale[0], 22.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 7.0 * scale[0],
              11.0 * scale[1], -1.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 17.0 * scale[1], -25.0 * scale[0],
              18.0 * scale[1], -34.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(837.0 * scale[0], 1293.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -16.0 * scale[1], 5.0 * scale[0], -
              16.0 * scale[1], -10.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 11.0 * scale[1], -18.0 * scale[0],
              10.0 * scale[1], -28.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -14.0 * scale[1], -16.0 * scale[0], -
              23.0 * scale[1], -22.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -7.0 * scale[0],
              1.0 * scale[1], -3.0 * scale[0], -6.0 * scale[1])
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 12.0 * scale[0], -
              9.0 * scale[1], 17.0 * scale[0], -6.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 6.0 * scale[0], -
              1.0 * scale[1], 3.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -11.0 * scale[0], -
              13.0 * scale[1], -17.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -12.0 * scale[0], -
              9.0 * scale[1], -13.0 * scale[0], -33.0 * scale[1])
    Curveto_r(0.0 * scale[0], -29.0 * scale[1], 2.0 * scale[0], -
              34.0 * scale[1], 10.0 * scale[0], -21.0 * scale[1])
    Curveto_r(9.0 * scale[0], 15.0 * scale[1], 11.0 * scale[0],
              14.0 * scale[1], 20.0 * scale[0], -4.0 * scale[1])
    Curveto_r(6.0 * scale[0], -12.0 * scale[1], 18.0 * scale[0], -
              23.0 * scale[1], 26.0 * scale[0], -25.0 * scale[1])
    Curveto_r(12.0 * scale[0], -4.0 * scale[1], 12.0 *
              scale[0], -3.0 * scale[1], 2.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 11.0 * scale[1], -46.0 * scale[0],
              66.0 * scale[1], -32.0 * scale[0], 57.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 10.0 *
              scale[0], -1.0 * scale[1], 10.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], 3.0 * scale[0],
              9.0 * scale[1], 7.0 * scale[0], 6.0 * scale[1])
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], 12.0 *
              scale[0], -2.0 * scale[1], 20.0 * scale[0], 4.0 * scale[1])
    Curveto_r(11.0 * scale[0], 10.0 * scale[1], 11.0 * scale[0],
              15.0 * scale[1], 1.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 13.0 * scale[1], -10.0 * scale[0],
              15.0 * scale[1], 3.0 * scale[0], 10.0 * scale[1])
    Curveto_r(9.0 * scale[0], -4.0 * scale[1], 21.0 *
              scale[0], -2.0 * scale[1], 26.0 * scale[0], 3.0 * scale[1])
    Curveto_r(6.0 * scale[0], 6.0 * scale[1], 10.0 * scale[0],
              4.0 * scale[1], 10.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -3.0 * scale[0], -
              13.0 * scale[1], -7.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 2.0 * scale[1], -7.0 * scale[0], -
              2.0 * scale[1], -7.0 * scale[0], -9.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 6.0 * scale[0], -
              12.0 * scale[1], 14.0 * scale[0], -9.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 13.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -16.0 * scale[1])
    Curveto_r(0.0 * scale[0], -15.0 * scale[1], -5.0 * scale[0], -
              19.0 * scale[1], -17.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 4.0 * scale[1], -14.0 * scale[0],
              2.0 * scale[1], -8.0 * scale[0], -3.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 13.0 * scale[0], -
              12.0 * scale[1], 17.0 * scale[0], -17.0 * scale[1])
    Curveto_r(4.0 * scale[0], -4.0 * scale[1], 11.0 * scale[0],
              7.0 * scale[1], 17.0 * scale[0], 25.0 * scale[1])
    Curveto_r(7.0 * scale[0], 26.0 * scale[1], 9.0 * scale[0],
              28.0 * scale[1], 10.0 * scale[0], 12.0 * scale[1])
    Curveto_r(1.0 * scale[0], -34.0 * scale[1], 21.0 *
              scale[0], -28.0 * scale[1], 21.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 20.0 * scale[1], -6.0 * scale[0],
              30.0 * scale[1], -20.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 3.0 * scale[1], -20.0 * scale[0],
              13.0 * scale[1], -20.0 * scale[0], 22.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], 5.0 * scale[0],
              14.0 * scale[1], 13.0 * scale[0], 10.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 3.0 * scale[0],
              1.0 * scale[1], -7.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-28.0 * scale[0], 22.0 * scale[1], -57.0 * scale[0],
              21.0 * scale[1], -49.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto_r(-26.0 * scale[0], -26.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -9.0 * scale[1], -11.0 *
              scale[0], -8.0 * scale[1], -5.0 * scale[0], 6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 10.0 * scale[1], 9.0 * scale[0],
              15.0 * scale[1], 12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 0.0 * scale[0], -
              11.0 * scale[1], -7.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto_r(19.0 * scale[0], -31.0 * scale[1], 0, 0)
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
    Moveto(555.0 * scale[0], 1270.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(21.0 * scale[0], -40.0 * scale[1], 19.0 * scale[0], -
              47.0 * scale[1], -5.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 20.0 * scale[1], -19.0 * scale[0],
              21.0 * scale[1], -20.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 5.0 * scale[0], -
              20.0 * scale[1], 10.0 * scale[0], -23.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0], -
              17.0 * scale[1], 4.0 * scale[0], -31.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -17.0 * scale[1], -1.0 * scale[0], -
              29.0 * scale[1], 11.0 * scale[0], -38.0 * scale[1])
    Curveto_r(16.0 * scale[0], -11.0 * scale[1], 15.0 * scale[0], -
              14.0 * scale[1], -8.0 * scale[0], -29.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -8.0 * scale[1], -35.0 * scale[0], -
              14.0 * scale[1], -48.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 2.0 * scale[1], -18.0 * scale[0],
              2.0 * scale[1], -11.0 * scale[0], -2.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 9.0 * scale[0], -
              10.0 * scale[1], 6.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -19.0 * scale[1], 40.0 * scale[0],
              3.0 * scale[1], 66.0 * scale[0], 28.0 * scale[1])
    Curveto_r(21.0 * scale[0], 20.0 * scale[1], 22.0 * scale[0],
              26.0 * scale[1], 11.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 7.0 * scale[1], -12.0 * scale[0],
              13.0 * scale[1], -3.0 * scale[0], 32.0 * scale[1])
    Curveto_r(12.0 * scale[0], 23.0 * scale[1], 12.0 * scale[0],
              23.0 * scale[1], 6.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -13.0 * scale[1], -1.0 *
              scale[0], -23.0 * scale[1], 5.0 * scale[0], -23.0 * scale[1])
    Curveto_r(18.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              53.0 * scale[1], -9.0 * scale[0], 88.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 40.0 * scale[1], -36.0 * scale[0],
              42.0 * scale[1], -15.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(65.0 * scale[0], 1250.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              10.0 * scale[1], -11.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -15.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -12.0 * scale[1])
    Curveto_r(15.0 * scale[0], -15.0 * scale[1], 16.0 *
              scale[0], -48.0 * scale[1], 2.0 * scale[0], -48.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              4.0 * scale[1], -10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], 37.0 *
              scale[0], -2.0 * scale[1], 51.0 * scale[0], 16.0 * scale[1])
    Curveto_r(9.0 * scale[0], 10.0 * scale[1], 9.0 * scale[0],
              17.0 * scale[1], 1.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              17.0 * scale[1], -1.0 * scale[0], 30.0 * scale[1])
    Curveto_r(8.0 * scale[0], 15.0 * scale[1], 6.0 * scale[0],
              18.0 * scale[1], -11.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -18.0 * scale[0], -
              4.0 * scale[1], -15.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto_r(12.0 * scale[0], -62.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -6.0 *
              scale[0], -5.0 * scale[1], -6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 11.0 * scale[1], 2.0 * scale[0],
              17.0 * scale[1], 5.0 * scale[0], 13.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 4.0 * scale[0], -
              12.0 * scale[1], 1.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(317.0 * scale[0], 1235.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -8.0 * scale[1], -17.0 * scale[0], -
              11.0 * scale[1], -21.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0],
              1.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -4.0 * scale[0], -
              9.0 * scale[1], -10.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -7.0 * scale[0],
              0.0 * scale[1], -4.0 * scale[0], -8.0 * scale[1])
    Curveto_r(2.0 * scale[0], -7.0 * scale[1], 20.0 * scale[0], -
              21.0 * scale[1], 39.0 * scale[0], -30.0 * scale[1])
    Lineto_r(35.0 * scale[0], -17.0 * scale[1])
    Lineto_r(-1.0 * scale[0], 28.0 * scale[1])
    Curveto_r(0.0 * scale[0], 19.0 * scale[1], -2.0 * scale[0],
              22.0 * scale[1], -7.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -15.0 * scale[1], -10.0 *
              scale[0], -15.0 * scale[1], -32.0 * scale[0], -2.0 * scale[1])
    Lineto_r(-25.0 * scale[0], 15.0 * scale[1])
    Lineto_r(24.0 * scale[0], -7.0 * scale[1])
    Curveto_r(19.0 * scale[0], -5.0 * scale[1], 23.0 *
              scale[0], -3.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], -2.0 * scale[0],
              18.0 * scale[1], 3.0 * scale[0], 21.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], 11.0 * scale[0], -
              1.0 * scale[1], 13.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], 6.0 *
              scale[0], -6.0 * scale[1], 6.0 * scale[0], 5.0 * scale[1])
    Curveto_r(1.0 * scale[0], 21.0 * scale[1], -13.0 * scale[0],
              22.0 * scale[1], -32.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(370.0 * scale[0], 1241.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              11.0 * scale[1], 14.0 * scale[0], -14.0 * scale[1])
    Curveto_r(10.0 * scale[0], -4.0 * scale[1], 13.0 *
              scale[0], -1.0 * scale[1], 9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 15.0 * scale[1], -23.0 * scale[0],
              19.0 * scale[1], -23.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(604.0 * scale[0], 1205.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -25.0 * scale[1], 0.0 * scale[0], -
              45.0 * scale[1], 2.0 * scale[0], -45.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 34.0 * scale[0],
              14.0 * scale[1], 34.0 * scale[0], 22.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -4.0 * scale[0],
              6.0 * scale[1], -10.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -4.0 * scale[1], -10.0 * scale[0],
              5.0 * scale[1], -10.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 15.0 * scale[1], 4.0 * scale[0],
              24.0 * scale[1], 10.0 * scale[0], 20.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 10.0 *
              scale[0], -2.0 * scale[1], 10.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -22.0 * scale[0],
              22.0 * scale[1], -33.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 0.0 * scale[1], -2.0 * scale[0], -
              20.0 * scale[1], -3.0 * scale[0], -45.0 * scale[1])
    te.end_fill()
    Moveto(191.0 * scale[0], 1224.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(644.0 * scale[0], 1216.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -9.0 * scale[1], -7.0 * scale[0], -
              15.0 * scale[1], 3.0 * scale[0], -24.0 * scale[1])
    Curveto_r(11.0 * scale[0], -11.0 * scale[1], 14.0 *
              scale[0], -10.0 * scale[1], 19.0 * scale[0], 2.0 * scale[1])
    Curveto_r(3.0 * scale[0], 9.0 * scale[1], 11.0 * scale[0],
              13.0 * scale[1], 17.0 * scale[0], 9.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 7.0 *
              scale[0], -1.0 * scale[1], 3.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], -11.0 * scale[0],
              9.0 * scale[1], -16.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -3.0 * scale[1], -10.0 *
              scale[0], -1.0 * scale[1], -12.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 5.0 * scale[1], -8.0 * scale[0],
              4.0 * scale[1], -14.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(99.0 * scale[0], 1170.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-21.0 * scale[0], -17.0 * scale[1], -21.0 *
              scale[0], -19.0 * scale[1], -4.0 * scale[0], -13.0 * scale[1])
    Curveto_r(23.0 * scale[0], 8.0 * scale[1], 51.0 * scale[0],
              33.0 * scale[1], 37.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0], -
              9.0 * scale[1], -33.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(374.0 * scale[0], 1174.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -9.0 * scale[1], 6.0 * scale[0], -
              18.0 * scale[1], 6.0 * scale[0], -20.0 * scale[1])
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 4.0 * scale[0], -
              4.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              9.0 * scale[1], 4.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 11.0 * scale[1], -10.0 * scale[0],
              20.0 * scale[1], -15.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              7.0 * scale[1], -4.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(815.0 * scale[0], 1170.0 * scale[1], x, y)
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
    Moveto(890.0 * scale[0], 1170.0 * scale[1], x, y)
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
    Moveto(160.0 * scale[0], 1145.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -8.0 * scale[1], -17.0 * scale[0], -
              12.0 * scale[1], -23.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -7.0 * scale[0],
              1.0 * scale[1], -3.0 * scale[0], -6.0 * scale[1])
    Curveto_r(6.0 * scale[0], -9.0 * scale[1], 13.0 *
              scale[0], -8.0 * scale[1], 27.0 * scale[0], 5.0 * scale[1])
    Curveto_r(10.0 * scale[0], 9.0 * scale[1], 19.0 * scale[0],
              19.0 * scale[1], 19.0 * scale[0], 21.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -8.0 * scale[0],
              2.0 * scale[1], -20.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(855.0 * scale[0], 1150.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -3.0 * scale[0], -
              10.0 * scale[1], 2.0 * scale[0], -10.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 2.0 * scale[0], -
              4.0 * scale[1], -6.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              11.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 11.0 *
              scale[0], -2.0 * scale[1], 11.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 4.0 * scale[0],
              9.0 * scale[1], 9.0 * scale[0], 6.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 14.0 * scale[0],
              1.0 * scale[1], 21.0 * scale[0], 9.0 * scale[1])
    Curveto_r(9.0 * scale[0], 10.0 * scale[1], 9.0 * scale[0],
              15.0 * scale[1], 1.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              5.0 * scale[1], -11.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -5.0 * scale[0], -
              7.0 * scale[1], -10.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -8.0 * scale[0],
              11.0 * scale[1], -5.0 * scale[0], 16.0 * scale[1])
    Curveto_r(4.0 * scale[0], 5.0 * scale[1], 4.0 * scale[0],
              9.0 * scale[1], 1.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              4.0 * scale[1], -11.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(410.0 * scale[0], 1140.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(780.0 * scale[0], 1141.0 * scale[1], x, y)
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
    Moveto(65.0 * scale[0], 1130.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 11.0 * scale[0], -
              8.0 * scale[1], 16.0 * scale[0], -5.0 * scale[1])
    Curveto_r(14.0 * scale[0], 9.0 * scale[1], 11.0 * scale[0],
              15.0 * scale[1], -7.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              5.0 * scale[1], -9.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(425.0 * scale[0], 1121.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 16.0 * scale[0], -16.0 * scale[1])
    Curveto_r(28.0 * scale[0], -9.0 * scale[1], 33.0 *
              scale[0], -2.0 * scale[1], 9.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 6.0 * scale[1], -21.0 * scale[0],
              8.0 * scale[1], -25.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(583.0 * scale[0], 830.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -21.0 * scale[1], 10.0 *
              scale[0], -18.0 * scale[1], 13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(1.0 * scale[0], 8.0 * scale[1], -2.0 * scale[0],
              15.0 * scale[1], -6.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              9.0 * scale[1], -7.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(499.0 * scale[0], 793.0 * scale[1], x, y)
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
    Moveto(438.0 * scale[0], 723.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 9.0 * scale[0], -
              10.0 * scale[1], 6.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], -2.0 *
              scale[0], -8.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 11.0 * scale[1], 14.0 * scale[0],
              26.0 * scale[1], -5.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -13.0 *
              scale[0], -3.0 * scale[1], -5.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(705.0 * scale[0], 683.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -10.0 * scale[1], -8.0 * scale[0], -
              32.0 * scale[1], -11.0 * scale[0], -50.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -26.0 * scale[1], -1.0 * scale[0], -
              31.0 * scale[1], 11.0 * scale[0], -27.0 * scale[1])
    Curveto_r(11.0 * scale[0], 4.0 * scale[1], 15.0 * scale[0],
              19.0 * scale[1], 13.0 * scale[0], 50.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 49.0 * scale[1], -3.0 * scale[0],
              52.0 * scale[1], -13.0 * scale[0], 27.0 * scale[1])
    te.end_fill()
    Moveto(460.0 * scale[0], 670.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -23.0 * scale[1], 12.0 * scale[0], -
              24.0 * scale[1], -3.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 11.0 * scale[1], -17.0 * scale[0],
              11.0 * scale[1], -17.0 * scale[0], -1.0 * scale[1])
    Curveto_r(0.0 * scale[0], -24.0 * scale[1], 12.0 * scale[0], -
              29.0 * scale[1], 36.0 * scale[0], -13.0 * scale[1])
    Curveto_r(17.0 * scale[0], 11.0 * scale[1], 24.0 * scale[0],
              12.0 * scale[1], 28.0 * scale[0], 2.0 * scale[1])
    Curveto_r(3.0 * scale[0], -6.0 * scale[1], 4.0 *
              scale[0], -3.0 * scale[1], 3.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 11.0 * scale[1], -9.0 * scale[0],
              19.0 * scale[1], -16.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -1.0 * scale[1], -20.0 * scale[0],
              3.0 * scale[1], -29.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 12.0 * scale[1], -14.0 * scale[0],
              10.0 * scale[1], -2.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(633.0 * scale[0], 638.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -13.0 * scale[1], -23.0 *
              scale[0], -36.0 * scale[1], -27.0 * scale[0], -53.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -22.0 * scale[1], -4.0 *
              scale[0], -26.0 * scale[1], 4.0 * scale[0], -15.0 * scale[1])
    Curveto_r(5.0 * scale[0], 8.0 * scale[1], 10.0 * scale[0],
              23.0 * scale[1], 10.0 * scale[0], 32.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], 5.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 11.0 * scale[1])
    Curveto_r(12.0 * scale[0], -5.0 * scale[1], 15.0 *
              scale[0], -2.0 * scale[1], 11.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 9.0 * scale[1], -1.0 * scale[0],
              21.0 * scale[1], 5.0 * scale[0], 27.0 * scale[1])
    Curveto_r(6.0 * scale[0], 6.0 * scale[1], 9.0 * scale[0],
              11.0 * scale[1], 6.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              10.0 * scale[1], -26.0 * scale[0], -22.0 * scale[1])
    te.end_fill()
    Moveto(555.0 * scale[0], 620.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 0.0 * scale[0], -
              10.0 * scale[1], -8.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 0.0 * scale[1], -30.0 * scale[0], -
              27.0 * scale[1], -18.0 * scale[0], -35.0 * scale[1])
    Curveto_r(5.0 * scale[0], -2.0 * scale[1], 16.0 * scale[0],
              6.0 * scale[1], 25.0 * scale[0], 20.0 * scale[1])
    Curveto_r(19.0 * scale[0], 29.0 * scale[1], 20.0 * scale[0],
              35.0 * scale[1], 5.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              4.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(330.0 * scale[0], 600.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-14.0 * scale[0], -11.0 * scale[1], -21.0 *
              scale[0], -20.0 * scale[1], -17.0 * scale[0], -20.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0],
              9.0 * scale[1], 34.0 * scale[0], 20.0 * scale[1])
    Curveto_r(14.0 * scale[0], 11.0 * scale[1], 22.0 * scale[0],
              20.0 * scale[1], 17.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0], -
              9.0 * scale[1], -34.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(433.0 * scale[0], 596.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(14.0 * scale[0], -13.0 * scale[1], 30.0 * scale[0], -
              41.0 * scale[1], 36.0 * scale[0], -62.0 * scale[1])
    Curveto_r(9.0 * scale[0], -34.0 * scale[1], 8.0 * scale[0], -
              41.0 * scale[1], -11.0 * scale[0], -61.0 * scale[1])
    Curveto_r(-23.0 * scale[0], -25.0 * scale[1], -18.0 *
              scale[0], -29.0 * scale[1], 13.0 * scale[0], -12.0 * scale[1])
    Curveto_r(17.0 * scale[0], 9.0 * scale[1], 19.0 * scale[0],
              17.0 * scale[1], 14.0 * scale[0], 57.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 27.0 * scale[1], -15.0 * scale[0],
              54.0 * scale[1], -26.0 * scale[0], 64.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -19.0 * scale[0],
              21.0 * scale[1], -19.0 * scale[0], 27.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -7.0 * scale[0],
              11.0 * scale[1], -16.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -11.0 *
              scale[0], -5.0 * scale[1], 9.0 * scale[0], -24.0 * scale[1])
    te.end_fill()
    Moveto(251.0 * scale[0], 601.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -8.0 * scale[1], -12.0 *
              scale[0], -12.0 * scale[1], -2.0 * scale[0], -24.0 * scale[1])
    Curveto_r(6.0 * scale[0], -8.0 * scale[1], 14.0 * scale[0], -
              25.0 * scale[1], 16.0 * scale[0], -38.0 * scale[1])
    Curveto_r(3.0 * scale[0], -13.0 * scale[1], 12.0 * scale[0], -
              30.0 * scale[1], 21.0 * scale[0], -38.0 * scale[1])
    Curveto_r(15.0 * scale[0], -15.0 * scale[1], 15.0 *
              scale[0], -14.0 * scale[1], 6.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 15.0 * scale[1], -8.0 * scale[0],
              24.0 * scale[1], 1.0 * scale[0], 34.0 * scale[1])
    Curveto_r(9.0 * scale[0], 10.0 * scale[1], 9.0 * scale[0],
              11.0 * scale[1], 0.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -9.0 * scale[1], -16.0 *
              scale[0], -1.0 * scale[1], -2.0 * scale[0], 27.0 * scale[1])
    Curveto_r(9.0 * scale[0], 18.0 * scale[1], 9.0 * scale[0],
              20.0 * scale[1], -2.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -19.0 * scale[1], -31.0 *
              scale[0], -16.0 * scale[1], -24.0 * scale[0], 7.0 * scale[1])
    Curveto_r(7.0 * scale[0], 23.0 * scale[1], 6.0 * scale[0],
              23.0 * scale[1], -14.0 * scale[0], 11.0 * scale[1])
    te.end_fill()
    Moveto(570.0 * scale[0], 566.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              17.0 * scale[1], 9.0 * scale[0], -20.0 * scale[1])
    Curveto_r(5.0 * scale[0], -4.0 * scale[1], 7.0 * scale[0],
              3.0 * scale[1], 4.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 23.0 * scale[1], -13.0 * scale[0],
              26.0 * scale[1], -13.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(355.0 * scale[0], 539.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0], -
              12.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 17.0 * scale[1], 1.0 * scale[0],
              20.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(220.0 * scale[0], 475.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -9.0 * scale[1], -11.0 * scale[0], -
              17.0 * scale[1], -9.0 * scale[0], -20.0 * scale[1])
    Curveto_r(3.0 * scale[0], -2.0 * scale[1], 10.0 * scale[0],
              5.0 * scale[1], 17.0 * scale[0], 15.0 * scale[1])
    Curveto_r(14.0 * scale[0], 24.0 * scale[1], 10.0 * scale[0],
              26.0 * scale[1], -8.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(404.0 * scale[0], 465.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-17.0 * scale[0], -13.0 * scale[1], -17.0 *
              scale[0], -14.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0],
              5.0 * scale[1], 23.0 * scale[0], 11.0 * scale[1])
    Curveto_r(11.0 * scale[0], 17.0 * scale[1], 0.0 * scale[0],
              20.0 * scale[1], -21.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(296.0 * scale[0], 456.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], 13.0 * scale[0], -
              17.0 * scale[1], 22.0 * scale[0], -21.0 * scale[1])
    Curveto_r(13.0 * scale[0], -5.0 * scale[1], 13.0 *
              scale[0], -2.0 * scale[1], -3.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 24.0 * scale[1], -26.0 * scale[0],
              25.0 * scale[1], -19.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(678.0 * scale[0], 464.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -2.0 * scale[0], -
              30.0 * scale[1], 4.0 * scale[0], -55.0 * scale[1])
    Curveto_r(6.0 * scale[0], -24.0 * scale[1], 11.0 * scale[0], -
              84.0 * scale[1], 10.0 * scale[0], -134.0 * scale[1])
    Lineto_r(0.0 * scale[0], -90.0 * scale[1])
    Lineto_r(10.0 * scale[0], 60.0 * scale[1])
    Curveto_r(12.0 * scale[0], 80.0 * scale[1], -6.0 * scale[0],
              249.0 * scale[1], -24.0 * scale[0], 219.0 * scale[1])
    te.end_fill()
    Moveto(355.0 * scale[0], 450.0 * scale[1], x, y)
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
    Moveto(157.0 * scale[0], 371.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -17.0 * scale[1], -3.0 *
              scale[0], -21.0 * scale[1], 5.0 * scale[0], -13.0 * scale[1])
    Curveto_r(5.0 * scale[0], 5.0 * scale[1], 8.0 * scale[0],
              16.0 * scale[1], 6.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], -7.0 * scale[0],
              3.0 * scale[1], -11.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(137.0 * scale[0], 333.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -3.0 * scale[1], -7.0 * scale[0], -
              13.0 * scale[1], -7.0 * scale[0], -22.0 * scale[1])
    Curveto_r(1.0 * scale[0], -13.0 * scale[1], 3.0 * scale[0], -
              13.0 * scale[1], 11.0 * scale[0], 2.0 * scale[1])
    Curveto_r(11.0 * scale[0], 19.0 * scale[1], 8.0 * scale[0],
              33.0 * scale[1], -4.0 * scale[0], 20.0 * scale[1])
    te.end_fill()
    Moveto(162.0 * scale[0], 255.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -8.0 * scale[0], -
              25.0 * scale[1], -3.0 * scale[0], -25.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 23.0 * scale[0],
              41.0 * scale[1], 17.0 * scale[0], 47.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 2.0 * scale[1], -8.0 * scale[0], -
              8.0 * scale[1], -14.0 * scale[0], -22.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#8b71b1')
    te.end_fill()
    Moveto(217.0 * scale[0], 1012.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-157.0 * scale[0], -3.0 * scale[1])
    Lineto_r(22.0 * scale[0], -23.0 * scale[1])
    Curveto_r(13.0 * scale[0], -13.0 * scale[1], 26.0 * scale[0], -
              21.0 * scale[1], 31.0 * scale[0], -19.0 * scale[1])
    Curveto_r(7.0 * scale[0], 4.0 * scale[1], 11.0 * scale[0], -
              12.0 * scale[1], 8.0 * scale[0], -36.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -7.0 * scale[1], 1.0 * scale[0], -
              11.0 * scale[1], 6.0 * scale[0], -8.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 9.0 * scale[0], -
              3.0 * scale[1], 9.0 * scale[0], -13.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], -4.0 * scale[0], -
              16.0 * scale[1], -8.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 3.0 * scale[1], -8.0 * scale[0], -
              2.0 * scale[1], -8.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], -5.0 * scale[0], -
              16.0 * scale[1], -11.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              5.0 * scale[1], -3.0 * scale[0], -12.0 * scale[1])
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 3.0 * scale[0], -
              8.0 * scale[1], -2.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -16.0 * scale[0],
              2.0 * scale[1], -24.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -7.0 * scale[1], -12.0 *
              scale[0], -9.0 * scale[1], 2.0 * scale[0], -9.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0], -
              3.0 * scale[1], 16.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              15.0 * scale[1], 5.0 * scale[0], -23.0 * scale[1])
    Curveto_r(11.0 * scale[0], -30.0 * scale[1], 13.0 *
              scale[0], -79.0 * scale[1], 3.0 * scale[0], -77.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 1.0 * scale[1], -10.0 * scale[0], -
              3.0 * scale[1], -9.0 * scale[0], -10.0 * scale[1])
    Curveto_r(2.0 * scale[0], -8.0 * scale[1], -11.0 * scale[0], -
              11.0 * scale[1], -41.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-28.0 * scale[0], 2.0 * scale[1], -46.0 *
              scale[0], -1.0 * scale[1], -49.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -23.0 * scale[1], -8.0 * scale[0], -
              257.0 * scale[1], 0.0 * scale[0], -257.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0],
              4.0 * scale[1], 21.0 * scale[0], 9.0 * scale[1])
    Curveto_r(11.0 * scale[0], 7.0 * scale[1], 11.0 * scale[0],
              9.0 * scale[1], -1.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 4.0 * scale[1], -15.0 * scale[0],
              26.0 * scale[1], -16.0 * scale[0], 81.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 42.0 * scale[1], 2.0 * scale[0],
              76.0 * scale[1], 7.0 * scale[0], 76.0 * scale[1])
    Curveto_r(15.0 * scale[0], 0.0 * scale[1], 96.0 * scale[0], -
              41.0 * scale[1], 128.0 * scale[0], -66.0 * scale[1])
    Lineto_r(32.0 * scale[0], -23.0 * scale[1])
    Lineto_r(8.0 * scale[0], 27.0 * scale[1])
    Curveto_r(4.0 * scale[0], 15.0 * scale[1], 6.0 * scale[0],
              32.0 * scale[1], 5.0 * scale[0], 39.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 7.0 * scale[1], 6.0 * scale[0],
              10.0 * scale[1], 17.0 * scale[0], 8.0 * scale[1])
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 18.0 * scale[0],
              3.0 * scale[1], 19.0 * scale[0], 16.0 * scale[1])
    Curveto_r(1.0 * scale[0], 12.0 * scale[1], -2.0 * scale[0],
              17.0 * scale[1], -10.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -3.0 * scale[1], -1.0 * scale[0],
              10.0 * scale[1], 11.0 * scale[0], 29.0 * scale[1])
    Curveto_r(25.0 * scale[0], 41.0 * scale[1], 21.0 * scale[0],
              45.0 * scale[1], -44.0 * scale[0], 44.0 * scale[1])
    Curveto_r(-46.0 * scale[0], -1.0 * scale[1], -54.0 * scale[0],
              16.0 * scale[1], -17.0 * scale[0], 33.0 * scale[1])
    Curveto_r(13.0 * scale[0], 6.0 * scale[1], 21.0 * scale[0],
              16.0 * scale[1], 18.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], -10.0 * scale[0],
              8.0 * scale[1], -15.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -15.0 * scale[0],
              3.0 * scale[1], -22.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 10.0 * scale[1], -22.0 * scale[0],
              22.0 * scale[1], -32.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-40.0 * scale[0], 15.0 * scale[1], -3.0 * scale[0],
              19.0 * scale[1], 71.0 * scale[0], 8.0 * scale[1])
    Curveto_r(87.0 * scale[0], -14.0 * scale[1], 163.0 *
              scale[0], -9.0 * scale[1], 208.0 * scale[0], 12.0 * scale[1])
    Curveto_r(17.0 * scale[0], 8.0 * scale[1], 41.0 * scale[0],
              19.0 * scale[1], 55.0 * scale[0], 25.0 * scale[1])
    Curveto_r(14.0 * scale[0], 7.0 * scale[1], 18.0 * scale[0],
              11.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-68.0 * scale[0], -5.0 * scale[1], -115.0 * scale[0],
              15.0 * scale[1], -104.0 * scale[0], 45.0 * scale[1])
    Curveto_r(6.0 * scale[0], 14.0 * scale[1], 8.0 * scale[0],
              14.0 * scale[1], 33.0 * scale[0], -2.0 * scale[1])
    Curveto_r(14.0 * scale[0], -9.0 * scale[1], 33.0 * scale[0], -
              17.0 * scale[1], 41.0 * scale[0], -16.0 * scale[1])
    Curveto_r(8.0 * scale[0], 1.0 * scale[1], 26.0 * scale[0],
              2.0 * scale[1], 40.0 * scale[0], 3.0 * scale[1])
    Curveto_r(23.0 * scale[0], 1.0 * scale[1], 25.0 * scale[0],
              6.0 * scale[1], 28.0 * scale[0], 50.0 * scale[1])
    Curveto_r(2.0 * scale[0], 30.0 * scale[1], -2.0 * scale[0],
              52.0 * scale[1], -9.0 * scale[0], 57.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 9.0 * scale[1], -68.0 * scale[0],
              10.0 * scale[1], -272.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto_r(263.0 * scale[0], -82.0 * scale[1], 0, 0)
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
    Moveto_r(-190.0 * scale[0], -50.0 * scale[1], 0, 0)
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
    Moveto(10.0 * scale[0], 1001.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 26.0 *
              scale[0], -9.0 * scale[1], 36.0 * scale[0], 2.0 * scale[1])
    Curveto_r(4.0 * scale[0], 4.0 * scale[1], -2.0 * scale[0],
              7.0 * scale[1], -14.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -4.0 * scale[1], -22.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(563.0 * scale[0], 1003.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(11.0 * scale[0], -3.0 * scale[1], 16.0 * scale[0], -
              10.0 * scale[1], 13.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -9.0 * scale[1], 3.0 * scale[0], -
              18.0 * scale[1], 19.0 * scale[0], -24.0 * scale[1])
    Curveto_r(32.0 * scale[0], -12.0 * scale[1], 32.0 *
              scale[0], -23.0 * scale[1], 0.0 * scale[0], -44.0 * scale[1])
    Curveto_r(-28.0 * scale[0], -19.0 * scale[1], -25.0 *
              scale[0], -36.0 * scale[1], 7.0 * scale[0], -36.0 * scale[1])
    Curveto_r(29.0 * scale[0], 0.0 * scale[1], 96.0 * scale[0], -
              39.0 * scale[1], 101.0 * scale[0], -60.0 * scale[1])
    Curveto_r(2.0 * scale[0], -9.0 * scale[1], 3.0 * scale[0], -
              33.0 * scale[1], 2.0 * scale[0], -53.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -20.0 * scale[1], 1.0 * scale[0], -
              34.0 * scale[1], 6.0 * scale[0], -31.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 9.0 * scale[0],
              0.0 * scale[1], 9.0 * scale[0], -6.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 5.0 * scale[0], -
              8.0 * scale[1], 10.0 * scale[0], -5.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 10.0 * scale[0],
              0.0 * scale[1], 10.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 21.0 * scale[0], -
              13.0 * scale[1], 87.0 * scale[0], -11.0 * scale[1])
    Curveto_r(60.0 * scale[0], 1.0 * scale[1], 80.0 * scale[0], -
              1.0 * scale[1], 63.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -5.0 * scale[1], -38.0 * scale[0], -
              10.0 * scale[1], -55.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -1.0 * scale[1], -47.0 *
              scale[0], -8.0 * scale[1], -67.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-27.0 * scale[0], -10.0 * scale[1], -38.0 *
              scale[0], -10.0 * scale[1], -42.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 15.0 * scale[1], -5.0 * scale[0], -
              26.0 * scale[1], 1.0 * scale[0], -107.0 * scale[1])
    Curveto_r(4.0 * scale[0], -50.0 * scale[1], 8.0 * scale[0], -
              65.0 * scale[1], 17.0 * scale[0], -58.0 * scale[1])
    Curveto_r(13.0 * scale[0], 11.0 * scale[1], 124.0 * scale[0], -
              16.0 * scale[1], 148.0 * scale[0], -36.0 * scale[1])
    Curveto_r(26.0 * scale[0], -22.0 * scale[1], 45.0 * scale[0],
              16.0 * scale[1], 52.0 * scale[0], 109.0 * scale[1])
    Curveto_r(7.0 * scale[0], 75.0 * scale[1], 5.0 * scale[0],
              87.0 * scale[1], -11.0 * scale[0], 103.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 13.0 * scale[1], -14.0 * scale[0],
              20.0 * scale[1], -5.0 * scale[0], 23.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 12.0 * scale[0],
              42.0 * scale[1], 12.0 * scale[0], 148.0 * scale[1])
    Lineto_r(0.0 * scale[0], 145.0 * scale[1])
    Lineto_r(-172.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-95.0 * scale[0], 0.0 * scale[1], -184.0 * scale[0],
              1.0 * scale[1], -198.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 3.0 * scale[1], -17.0 * scale[0],
              2.0 * scale[1], -7.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(770.0 * scale[0], 481.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(30.0 * scale[0], -3.0 * scale[1], 72.0 * scale[0], -
              16.0 * scale[1], 93.0 * scale[0], -29.0 * scale[1])
    Curveto_r(21.0 * scale[0], -12.0 * scale[1], 35.0 * scale[0], -
              17.0 * scale[1], 32.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 24.0 * scale[1], -86.0 * scale[0],
              50.0 * scale[1], -132.0 * scale[0], 49.0 * scale[1])
    Lineto_r(-48.0 * scale[0], -2.0 * scale[1])
    Lineto_r(55.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(942.0 * scale[0], 380.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(942.0 * scale[0], 318.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -39.0 * scale[1], -20.0 * scale[0], -
              80.0 * scale[1], -31.0 * scale[0], -73.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -19.0 * scale[0], -
              4.0 * scale[1], -29.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -11.0 * scale[1], -28.0 *
              scale[0], -19.0 * scale[1], -38.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 2.0 * scale[1], -30.0 *
              scale[0], -1.0 * scale[1], -44.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -5.0 * scale[1], -43.0 *
              scale[0], -9.0 * scale[1], -65.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-39.0 * scale[0], -1.0 * scale[1], -40.0 *
              scale[0], -2.0 * scale[1], -51.0 * scale[0], -46.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -25.0 * scale[1], -21.0 * scale[0], -
              64.0 * scale[1], -33.0 * scale[0], -87.0 * scale[1])
    Curveto_r(-28.0 * scale[0], -56.0 * scale[1], -27.0 *
              scale[0], -63.0 * scale[1], 12.0 * scale[0], -63.0 * scale[1])
    Curveto_r(78.0 * scale[0], 0.0 * scale[1], 107.0 * scale[0],
              11.0 * scale[1], 122.0 * scale[0], 46.0 * scale[1])
    Curveto_r(18.0 * scale[0], 44.0 * scale[1], 88.0 * scale[0],
              119.0 * scale[1], 125.0 * scale[0], 134.0 * scale[1])
    Curveto_r(35.0 * scale[0], 15.0 * scale[1], 43.0 * scale[0],
              36.0 * scale[1], 37.0 * scale[0], 111.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 29.0 * scale[1], -4.0 * scale[0],
              42.0 * scale[1], -5.0 * scale[0], 27.0 * scale[1])
    te.end_fill()
    Moveto(0.0 * scale[0], 279.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 36.0 * scale[0], -
              29.0 * scale[1], 70.0 * scale[0], -29.0 * scale[1])
    Curveto_r(27.0 * scale[0], 0.0 * scale[1], 30.0 * scale[0], -
              3.0 * scale[1], 25.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -18.0 * scale[1], -2.0 * scale[0], -
              23.0 * scale[1], 14.0 * scale[0], -23.0 * scale[1])
    Curveto_r(15.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0],
              4.0 * scale[1], 10.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 7.0 * scale[1], -8.0 * scale[0],
              17.0 * scale[1], -5.0 * scale[0], 22.0 * scale[1])
    Curveto_r(6.0 * scale[0], 8.0 * scale[1], -18.0 * scale[0],
              28.0 * scale[1], -34.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 1.0 * scale[1], -12.0 * scale[0],
              3.0 * scale[1], -20.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-37.0 * scale[0], 12.0 * scale[1], -60.0 * scale[0],
              14.0 * scale[1], -60.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(30.0 * scale[0], 220.0 * scale[1], x, y)
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
    te.color('#4d2125')
    te.end_fill()
    Moveto(0.0 * scale[0], 1363.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 8.0 * scale[0], -7.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], 14.0 * scale[0],
              14.0 * scale[1], 22.0 * scale[0], 17.0 * scale[1])
    Curveto_r(10.0 * scale[0], 4.0 * scale[1], 8.0 * scale[0],
              6.0 * scale[1], -7.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 1.0 * scale[1], -23.0 * scale[0], -
              5.0 * scale[1], -23.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(902.0 * scale[0], 1370.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(14.0 * scale[0], -4.0 * scale[1], 31.0 * scale[0], -
              11.0 * scale[1], 37.0 * scale[0], -15.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 11.0 * scale[0],
              1.0 * scale[1], 11.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], -10.0 * scale[0],
              16.0 * scale[1], -37.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-35.0 * scale[0], -1.0 * scale[1], -36.0 *
              scale[0], -1.0 * scale[1], -11.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(0.0 * scale[0], 1295.0 * scale[1], x, y)
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
    Moveto(55.0 * scale[0], 1290.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-26.0 * scale[0], -28.0 * scale[1], -15.0 *
              scale[0], -31.0 * scale[1], 12.0 * scale[0], -3.0 * scale[1])
    Curveto_r(12.0 * scale[0], 13.0 * scale[1], 19.0 * scale[0],
              23.0 * scale[1], 14.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0], -
              9.0 * scale[1], -26.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(880.0 * scale[0], 1306.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 7.0 * scale[0], -
              7.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 12.0 *
              scale[0], -2.0 * scale[1], 9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], -25.0 * scale[0],
              14.0 * scale[1], -25.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(917.0 * scale[0], 1234.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -27.0 * scale[1], 7.0 * scale[0], -
              51.0 * scale[1], 9.0 * scale[0], -53.0 * scale[1])
    Curveto_r(8.0 * scale[0], -9.0 * scale[1], 3.0 * scale[0],
              75.0 * scale[1], -5.0 * scale[0], 88.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 8.0 * scale[1], -7.0 * scale[0], -
              5.0 * scale[1], -4.0 * scale[0], -35.0 * scale[1])
    te.end_fill()
    Moveto(105.0 * scale[0], 1220.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -26.0 * scale[1], 4.0 * scale[0], -
              48.0 * scale[1], 16.0 * scale[0], -29.0 * scale[1])
    Curveto_r(12.0 * scale[0], 19.0 * scale[1], 11.0 * scale[0],
              49.0 * scale[1], 0.0 * scale[0], 49.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              9.0 * scale[1], -16.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(830.0 * scale[0], 1204.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 4.0 * scale[0], -
              23.0 * scale[1], 10.0 * scale[0], -19.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 10.0 * scale[0], 26.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], -4.0 * scale[0],
              19.0 * scale[1], -10.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              12.0 * scale[1], -10.0 * scale[0], -26.0 * scale[1])
    te.end_fill()
    Moveto(21.0 * scale[0], 1208.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -10.0 * scale[1], -5.0 * scale[0], -
              18.0 * scale[1], -11.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              7.0 * scale[1], -10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 15.0 * scale[0], -4.0 * scale[1])
    Curveto_r(13.0 * scale[0], 11.0 * scale[1], 15.0 * scale[0],
              8.0 * scale[1], 15.0 * scale[0], -14.0 * scale[1])
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 4.0 * scale[0], -
              26.0 * scale[1], 9.0 * scale[0], -26.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 5.0 * scale[0],
              15.0 * scale[1], 0.0 * scale[0], 38.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 52.0 * scale[1], -17.0 * scale[0],
              59.0 * scale[1], -18.0 * scale[0], 40.0 * scale[1])
    te.end_fill()
    Moveto(0.0 * scale[0], 1050.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(0.0 * scale[0], -30.0 * scale[1])
    Lineto_r(288.0 * scale[0], -1.0 * scale[1])
    Curveto_r(158.0 * scale[0], -1.0 * scale[1], 371.0 *
              scale[0], -4.0 * scale[1], 475.0 * scale[0], -8.0 * scale[1])
    Lineto_r(187.0 * scale[0], -6.0 * scale[1])
    Lineto_r(-1.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 17.0 * scale[1], -3.0 * scale[0],
              23.0 * scale[1], -6.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -9.0 * scale[1], -16.0 * scale[0], -
              19.0 * scale[1], -31.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-42.0 * scale[0], -9.0 * scale[1], -854.0 * scale[0],
              5.0 * scale[1], -881.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 5.0 * scale[1], -21.0 * scale[0],
              14.0 * scale[1], -17.0 * scale[0], 23.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], 1.0 * scale[0],
              15.0 * scale[1], -4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              13.0 * scale[1], -10.0 * scale[0], -30.0 * scale[1])
    te.end_fill()
    Moveto(81.0 * scale[0], 954.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(13.0 * scale[0], -17.0 * scale[1], 26.0 * scale[0], -
              30.0 * scale[1], 28.0 * scale[0], -27.0 * scale[1])
    Curveto_r(3.0 * scale[0], 2.0 * scale[1], -8.0 * scale[0],
              16.0 * scale[1], -24.0 * scale[0], 31.0 * scale[1])
    Lineto_r(-28.0 * scale[0], 27.0 * scale[1])
    Lineto_r(24.0 * scale[0], -31.0 * scale[1])
    te.end_fill()
    Moveto(6.0 * scale[0], 935.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -9.0 * scale[1], -6.0 * scale[0], -
              22.0 * scale[1], -5.0 * scale[0], -28.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], 5.0 * scale[0], -
              1.0 * scale[1], 10.0 * scale[0], 12.0 * scale[1])
    Curveto_r(5.0 * scale[0], 13.0 * scale[1], 8.0 * scale[0],
              26.0 * scale[1], 5.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 2.0 * scale[1], -6.0 * scale[0], -
              3.0 * scale[1], -10.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(584.0 * scale[0], 860.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(15.0 * scale[0], -5.0 * scale[1], 36.0 * scale[0], -
              16.0 * scale[1], 45.0 * scale[0], -24.0 * scale[1])
    Curveto_r(10.0 * scale[0], -9.0 * scale[1], 20.0 * scale[0], -
              13.0 * scale[1], 24.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 6.0 * scale[1], 37.0 * scale[0], -
              48.0 * scale[1], 37.0 * scale[0], -64.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -20.0 * scale[0], -
              22.0 * scale[1], -45.0 * scale[0], -38.0 * scale[1])
    Curveto_r(-25.0 * scale[0], -15.0 * scale[1], -45.0 *
              scale[0], -31.0 * scale[1], -45.0 * scale[0], -35.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 18.0 * scale[0], -
              16.0 * scale[1], 40.0 * scale[0], -27.0 * scale[1])
    Curveto_r(31.0 * scale[0], -15.0 * scale[1], 42.0 *
              scale[0], -17.0 * scale[1], 50.0 * scale[0], -7.0 * scale[1])
    Curveto_r(10.0 * scale[0], 13.0 * scale[1], 13.0 * scale[0],
              97.0 * scale[1], 4.0 * scale[0], 146.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 31.0 * scale[1], -68.0 * scale[0],
              69.0 * scale[1], -110.0 * scale[0], 68.0 * scale[1])
    Lineto_r(-29.0 * scale[0], -1.0 * scale[1])
    Lineto_r(29.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(67.0 * scale[0], 830.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(14.0 * scale[0], -17.0 * scale[1], 29.0 * scale[0], -
              27.0 * scale[1], 32.0 * scale[0], -24.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              10.0 * scale[1], -12.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 6.0 * scale[1], -17.0 * scale[0],
              17.0 * scale[1], -17.0 * scale[0], 24.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -7.0 * scale[0],
              15.0 * scale[1], -15.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              8.0 * scale[1], 12.0 * scale[0], -30.0 * scale[1])
    te.end_fill()
    Moveto(21.0 * scale[0], 827.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -8.0 * scale[1], -13.0 * scale[0], -
              29.0 * scale[1], -16.0 * scale[0], -48.0 * scale[1])
    Lineto_r(-5.0 * scale[0], -34.0 * scale[1])
    Lineto_r(11.0 * scale[0], 35.0 * scale[1])
    Curveto_r(6.0 * scale[0], 19.0 * scale[1], 15.0 * scale[0],
              41.0 * scale[1], 21.0 * scale[0], 48.0 * scale[1])
    Curveto_r(6.0 * scale[0], 6.0 * scale[1], 8.0 * scale[0],
              12.0 * scale[1], 5.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              6.0 * scale[1], -16.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(136.0 * scale[0], 812.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(56.0 * scale[0], -48.0 * scale[1], 118.0 * scale[0], -
              55.0 * scale[1], 211.0 * scale[0], -21.0 * scale[1])
    Curveto_r(32.0 * scale[0], 11.0 * scale[1], 64.0 * scale[0],
              23.0 * scale[1], 72.0 * scale[0], 25.0 * scale[1])
    Curveto_r(8.0 * scale[0], 2.0 * scale[1], 12.0 * scale[0],
              6.0 * scale[1], 10.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 3.0 * scale[1], -29.0 * scale[0], -
              3.0 * scale[1], -59.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-103.0 * scale[0], -29.0 * scale[1], -106.0 *
              scale[0], -29.0 * scale[1], -219.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-33.0 * scale[0], 10.0 * scale[1], -34.0 * scale[0],
              10.0 * scale[1], -15.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(280.0 * scale[0], 750.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-14.0 * scale[0], -4.0 * scale[1], -52.0 *
              scale[0], -9.0 * scale[1], -85.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-46.0 * scale[0], -2.0 * scale[1], -54.0 *
              scale[0], -4.0 * scale[1], -35.0 * scale[0], -10.0 * scale[1])
    Curveto_r(41.0 * scale[0], -13.0 * scale[1], 85.0 *
              scale[0], -11.0 * scale[1], 118.0 * scale[0], 6.0 * scale[1])
    Curveto_r(18.0 * scale[0], 8.0 * scale[1], 32.0 * scale[0],
              17.0 * scale[1], 32.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 2.0 * scale[1], -1.0 * scale[0],
              4.0 * scale[1], -2.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -1.0 * scale[1], -14.0 *
              scale[0], -5.0 * scale[1], -28.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(523.0 * scale[0], 752.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-17.0 * scale[0], -11.0 * scale[1], 11.0 *
              scale[0], -45.0 * scale[1], 34.0 * scale[0], -40.0 * scale[1])
    Curveto_r(25.0 * scale[0], 5.0 * scale[1], 24.0 * scale[0],
              42.0 * scale[1], -2.0 * scale[0], 46.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 1.0 * scale[1], -25.0 *
              scale[0], -1.0 * scale[1], -32.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto_r(21.0 * scale[0], -14.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -8.0 * scale[1], -2.0 *
              scale[0], -9.0 * scale[1], 9.0 * scale[0], -5.0 * scale[1])
    Curveto_r(10.0 * scale[0], 3.0 * scale[1], 17.0 * scale[0],
              2.0 * scale[1], 17.0 * scale[0], -3.0 * scale[1])
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], -27.0 * scale[0], -
              13.0 * scale[1], -34.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -3.0 * scale[0],
              11.0 * scale[1], 1.0 * scale[0], 15.0 * scale[1])
    Curveto_r(10.0 * scale[0], 10.0 * scale[1], 15.0 * scale[0],
              7.0 * scale[1], 7.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(262.0 * scale[0], 684.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-20.0 * scale[0], -19.0 * scale[1], -28.0 *
              scale[0], -31.0 * scale[1], -17.0 * scale[0], -26.0 * scale[1])
    Curveto_r(22.0 * scale[0], 11.0 * scale[1], 73.0 * scale[0],
              62.0 * scale[1], 62.0 * scale[0], 62.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -24.0 * scale[0], -
              16.0 * scale[1], -45.0 * scale[0], -36.0 * scale[1])
    te.end_fill()
    Moveto(420.0 * scale[0], 710.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(235.0 * scale[0], 619.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0], -
              13.0 * scale[1], -2.0 * scale[0], -16.0 * scale[1])
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 27.0 * scale[0],
              6.0 * scale[1], 27.0 * scale[0], 18.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], -17.0 * scale[0],
              12.0 * scale[1], -25.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(310.0 * scale[0], 610.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(249.0 * scale[0], 513.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -21.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(227.0 * scale[0], 458.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-26.0 * scale[0], -30.0 * scale[1], -47.0 *
              scale[0], -62.0 * scale[1], -47.0 * scale[0], -71.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], -9.0 * scale[0], -
              32.0 * scale[1], -21.0 * scale[0], -52.0 * scale[1])
    Curveto_r(-24.0 * scale[0], -39.0 * scale[1], -41.0 * scale[0], -
              105.0 * scale[1], -29.0 * scale[0], -105.0 * scale[1])
    Curveto_r(15.0 * scale[0], 0.0 * scale[1], 47.0 * scale[0],
              63.0 * scale[1], 61.0 * scale[0], 118.0 * scale[1])
    Curveto_r(7.0 * scale[0], 29.0 * scale[1], 20.0 * scale[0],
              60.0 * scale[1], 29.0 * scale[0], 70.0 * scale[1])
    Curveto_r(9.0 * scale[0], 9.0 * scale[1], 17.0 * scale[0],
              22.0 * scale[1], 18.0 * scale[0], 27.0 * scale[1])
    Curveto_r(1.0 * scale[0], 13.0 * scale[1], 32.0 * scale[0],
              19.0 * scale[1], 32.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 9.0 * scale[0], -
              15.0 * scale[1], 21.0 * scale[0], -21.0 * scale[1])
    Curveto_r(19.0 * scale[0], -11.0 * scale[1], 20.0 *
              scale[0], -10.0 * scale[1], 8.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 13.0 * scale[1], -15.0 * scale[0],
              34.0 * scale[1], -18.0 * scale[0], 47.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 24.0 * scale[1], -9.0 * scale[0],
              23.0 * scale[1], -54.0 * scale[0], -30.0 * scale[1])
    te.end_fill()
    Moveto(350.0 * scale[0], 430.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -8.0 * scale[1], -7.0 *
              scale[0], -9.0 * scale[1], 15.0 * scale[0], -4.0 * scale[1])
    Curveto_r(37.0 * scale[0], 8.0 * scale[1], 45.0 * scale[0],
              14.0 * scale[1], 19.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 0.0 * scale[1], -26.0 * scale[0], -
              5.0 * scale[1], -34.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(187.0 * scale[0], 276.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -7.0 * scale[1], -9.0 * scale[0], -
              34.0 * scale[1], -12.0 * scale[0], -60.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -39.0 * scale[1], -5.0 *
              scale[0], -45.0 * scale[1], 8.0 * scale[0], -40.0 * scale[1])
    Curveto_r(10.0 * scale[0], 3.0 * scale[1], 16.0 * scale[0],
              22.0 * scale[1], 19.0 * scale[0], 56.0 * scale[1])
    Curveto_r(3.0 * scale[0], 49.0 * scale[1], -5.0 * scale[0],
              72.0 * scale[1], -15.0 * scale[0], 44.0 * scale[1])
    te.end_fill()
    Moveto(440.0 * scale[0], 237.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -12.0 * scale[1], -24.0 * scale[0], -
              41.0 * scale[1], -34.0 * scale[0], -64.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -24.0 * scale[1], -24.0 *
              scale[0], -43.0 * scale[1], -30.0 * scale[0], -43.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -18.0 * scale[0], -
              15.0 * scale[1], -27.0 * scale[0], -32.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -17.0 * scale[1], -24.0 * scale[0], -
              36.0 * scale[1], -34.0 * scale[0], -42.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -6.0 * scale[1], -27.0 * scale[0], -
              20.0 * scale[1], -37.0 * scale[0], -31.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -20.0 * scale[1], -17.0 *
              scale[0], -20.0 * scale[1], -18.0 * scale[0], 2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], -6.0 * scale[0],
              22.0 * scale[1], -12.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -1.0 * scale[1], -15.0 * scale[0],
              22.0 * scale[1], -19.0 * scale[0], 78.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 44.0 * scale[1], -7.0 * scale[0],
              73.0 * scale[1], -8.0 * scale[0], 65.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -22.0 * scale[1], -1.0 * scale[0], -
              130.0 * scale[1], 5.0 * scale[0], -163.0 * scale[1])
    Curveto_r(6.0 * scale[0], -27.0 * scale[1], 7.0 * scale[0], -
              27.0 * scale[1], 82.0 * scale[0], -27.0 * scale[1])
    Curveto_r(47.0 * scale[0], 0.0 * scale[1], 72.0 * scale[0],
              4.0 * scale[1], 64.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 7.0 * scale[1], -9.0 * scale[0],
              16.0 * scale[1], 12.0 * scale[0], 47.0 * scale[1])
    Curveto_r(48.0 * scale[0], 73.0 * scale[1], 101.0 * scale[0],
              244.0 * scale[1], 56.0 * scale[0], 181.0 * scale[1])
    te.end_fill()
    Moveto(136.0 * scale[0], 194.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -9.0 * scale[1], -4.0 * scale[0], -
              19.0 * scale[1], -1.0 * scale[0], -22.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              3.0 * scale[1], 11.0 * scale[0], 12.0 * scale[1])
    Curveto_r(4.0 * scale[0], 9.0 * scale[1], 4.0 * scale[0],
              19.0 * scale[1], 1.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 3.0 * scale[1], -7.0 * scale[0], -
              3.0 * scale[1], -11.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(655.0 * scale[0], 160.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -12.0 * scale[1], -5.0 * scale[0], -
              24.0 * scale[1], -2.0 * scale[0], -27.0 * scale[1])
    Curveto_r(3.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0],
              5.0 * scale[1], 12.0 * scale[0], 17.0 * scale[1])
    Curveto_r(4.0 * scale[0], 12.0 * scale[1], 5.0 * scale[0],
              24.0 * scale[1], 2.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 2.0 * scale[1], -8.0 * scale[0], -
              5.0 * scale[1], -12.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(626.0 * scale[0], 80.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -19.0 * scale[1], -14.0 * scale[0], -
              45.0 * scale[1], -22.0 * scale[0], -58.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -12.0 * scale[1], -10.0 *
              scale[0], -22.0 * scale[1], -5.0 * scale[0], -22.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 44.0 * scale[0],
              85.0 * scale[1], 39.0 * scale[0], 102.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 7.0 * scale[1], -8.0 * scale[0], -
              3.0 * scale[1], -12.0 * scale[0], -22.0 * scale[1])
    te.end_fill()
    Moveto(935.0 * scale[0], 10.0 * scale[1], x, y)
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
    te.color('#86391a')
    te.end_fill()
    Moveto(28.0 * scale[0], 1373.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-21.0 * scale[0], -5.0 * scale[1], -37.0 * scale[0], -
              55.0 * scale[1], -20.0 * scale[0], -61.0 * scale[1])
    Curveto_r(7.0 * scale[0], -2.0 * scale[1], 9.0 * scale[0], -
              10.0 * scale[1], 4.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -26.0 * scale[1], -15.0 * scale[0], -
              102.0 * scale[1], -3.0 * scale[0], -102.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              7.0 * scale[1], 11.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 4.0 * scale[0],
              15.0 * scale[1], 10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              7.0 * scale[1], 4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 8.0 * scale[1], -1.0 * scale[0],
              15.0 * scale[1], 4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0],
              11.0 * scale[1], 2.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 26.0 * scale[1], -7.0 * scale[0],
              29.0 * scale[1], 5.0 * scale[0], 19.0 * scale[1])
    Curveto_r(8.0 * scale[0], -7.0 * scale[1], 12.0 * scale[0], -
              17.0 * scale[1], 8.0 * scale[0], -24.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], -2.0 *
              scale[0], -7.0 * scale[1], 3.0 * scale[0], -3.0 * scale[1])
    Curveto_r(5.0 * scale[0], 5.0 * scale[1], 9.0 * scale[0],
              14.0 * scale[1], 9.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], 55.0 * scale[0],
              28.0 * scale[1], 80.0 * scale[0], 20.0 * scale[1])
    Curveto_r(11.0 * scale[0], -3.0 * scale[1], 22.0 *
              scale[0], -6.0 * scale[1], 25.0 * scale[0], -5.0 * scale[1])
    Curveto_r(5.0 * scale[0], 1.0 * scale[1], 24.0 * scale[0], -
              39.0 * scale[1], 22.0 * scale[0], -49.0 * scale[1])
    Curveto_r(0.0 * scale[0], -3.0 * scale[1], 14.0 *
              scale[0], -3.0 * scale[1], 31.0 * scale[0], 0.0 * scale[1])
    Lineto_r(32.0 * scale[0], 5.0 * scale[1])
    Lineto_r(-30.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 4.0 * scale[1], -30.0 * scale[0],
              11.0 * scale[1], -29.0 * scale[0], 23.0 * scale[1])
    Curveto_r(1.0 * scale[0], 9.0 * scale[1], -1.0 * scale[0],
              17.0 * scale[1], -5.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 3.0 * scale[1], -46.0 * scale[0],
              10.0 * scale[1], -49.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 5.0 * scale[1], -7.0 * scale[0],
              8.0 * scale[1], -11.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -9.0 * scale[1], -81.0 *
              scale[0], -13.0 * scale[1], -81.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              10.0 * scale[1], 35.0 * scale[0], 14.0 * scale[1])
    Curveto_r(12.0 * scale[0], 1.0 * scale[1], 30.0 * scale[0],
              7.0 * scale[1], 42.0 * scale[0], 13.0 * scale[1])
    Curveto_r(11.0 * scale[0], 6.0 * scale[1], 24.0 * scale[0],
              8.0 * scale[1], 28.0 * scale[0], 4.0 * scale[1])
    Curveto_r(5.0 * scale[0], -4.0 * scale[1], 5.0 *
              scale[0], -1.0 * scale[1], 1.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 12.0 * scale[1], -90.0 * scale[0],
              15.0 * scale[1], -128.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto_r(4.0 * scale[0], -45.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -7.0 * scale[1], -12.0 *
              scale[0], -8.0 * scale[1], -12.0 * scale[0], -2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], 12.0 * scale[0],
              26.0 * scale[1], 19.0 * scale[0], 19.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], -1.0 * scale[0], -
              11.0 * scale[1], -7.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(350.0 * scale[0], 1365.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(33.0 * scale[0], -19.0 * scale[1], 49.0 *
              scale[0], -19.0 * scale[1], 24.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 8.0 * scale[1], -26.0 * scale[0],
              14.0 * scale[1], -34.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              6.0 * scale[1], 10.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(548.0 * scale[0], 1373.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(775.0 * scale[0], 1353.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(52.0 * scale[0], -17.0 * scale[1], 73.0 * scale[0], -
              28.0 * scale[1], 60.0 * scale[0], -31.0 * scale[1])
    Curveto_r(-27.0 * scale[0], -6.0 * scale[1], -78.0 * scale[0], -
              49.0 * scale[1], -66.0 * scale[0], -56.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 16.0 * scale[0],
              4.0 * scale[1], 24.0 * scale[0], 17.0 * scale[1])
    Curveto_r(10.0 * scale[0], 16.0 * scale[1], 26.0 * scale[0],
              23.0 * scale[1], 53.0 * scale[0], 25.0 * scale[1])
    Curveto_r(22.0 * scale[0], 2.0 * scale[1], 48.0 * scale[0],
              5.0 * scale[1], 59.0 * scale[0], 7.0 * scale[1])
    Curveto_r(11.0 * scale[0], 3.0 * scale[1], 14.0 * scale[0],
              2.0 * scale[1], 7.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -3.0 * scale[1], -9.0 * scale[0], -
              11.0 * scale[1], -6.0 * scale[0], -16.0 * scale[1])
    Curveto_r(5.0 * scale[0], -7.0 * scale[1], 2.0 * scale[0], -
              8.0 * scale[1], -7.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 4.0 * scale[1], -4.0 * scale[0], -
              2.0 * scale[1], 9.0 * scale[0], -14.0 * scale[1])
    Curveto_r(24.0 * scale[0], -23.0 * scale[1], 32.0 * scale[0], -
              101.0 * scale[1], 11.0 * scale[0], -101.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              7.0 * scale[1], -5.0 * scale[0], -15.0 * scale[1])
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], 1.0 * scale[0], -
              15.0 * scale[1], -5.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              6.0 * scale[1], -3.0 * scale[0], -12.0 * scale[1])
    Curveto_r(4.0 * scale[0], -7.0 * scale[1], 4.0 * scale[0], -
              10.0 * scale[1], -1.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 11.0 * scale[1], -35.0 * scale[0], -
              11.0 * scale[1], -35.0 * scale[0], -34.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], -5.0 * scale[0], -
              16.0 * scale[1], -10.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -8.0 * scale[0],
              10.0 * scale[1], -5.0 * scale[0], 15.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], -13.0 * scale[0],
              10.0 * scale[1], -34.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 2.0 * scale[1], -38.0 * scale[0],
              1.0 * scale[1], -35.0 * scale[0], -1.0 * scale[1])
    Curveto_r(2.0 * scale[0], -2.0 * scale[1], -2.0 * scale[0], -
              11.0 * scale[1], -9.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -14.0 * scale[1], -10.0 *
              scale[0], -14.0 * scale[1], 3.0 * scale[0], -4.0 * scale[1])
    Curveto_r(25.0 * scale[0], 19.0 * scale[1], 58.0 * scale[0],
              11.0 * scale[1], 70.0 * scale[0], -15.0 * scale[1])
    Curveto_r(11.0 * scale[0], -24.0 * scale[1], 10.0 * scale[0], -
              25.0 * scale[1], -27.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 4.0 * scale[1], -45.0 * scale[0],
              2.0 * scale[1], -53.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -8.0 * scale[1], -12.0 *
              scale[0], -10.0 * scale[1], 5.0 * scale[0], -11.0 * scale[1])
    Lineto_r(20.0 * scale[0], 0.0 * scale[1])
    Lineto_r(-20.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -6.0 * scale[1], 8.0 *
              scale[0], -8.0 * scale[1], 67.0 * scale[0], -6.0 * scale[1])
    Curveto_r(48.0 * scale[0], 2.0 * scale[1], 91.0 * scale[0],
              7.0 * scale[1], 95.0 * scale[0], 11.0 * scale[1])
    Curveto_r(5.0 * scale[0], 4.0 * scale[1], 9.0 * scale[0],
              77.0 * scale[1], 11.0 * scale[0], 161.0 * scale[1])
    Curveto_r(3.0 * scale[0], 185.0 * scale[1], 10.0 * scale[0],
              178.0 * scale[1], -148.0 * scale[0], 182.0 * scale[1])
    Lineto_r(-105.0 * scale[0], 3.0 * scale[1])
    Lineto_r(80.0 * scale[0], -27.0 * scale[1])
    te.end_fill()
    Moveto_r(113.0 * scale[0], 0.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -2.0 * scale[1], -26.0 *
              scale[0], -2.0 * scale[1], -35.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              5.0 * scale[1], 17.0 * scale[0], 5.0 * scale[1])
    Curveto_r(19.0 * scale[0], 0.0 * scale[1], 27.0 * scale[0], -
              2.0 * scale[1], 18.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(19.0 * scale[0], -268.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-23.0 * scale[0], -22.0 * scale[1], -33.0 *
              scale[0], -18.0 * scale[1], -12.0 * scale[0], 5.0 * scale[1])
    Curveto_r(10.0 * scale[0], 11.0 * scale[1], 20.0 * scale[0],
              18.0 * scale[1], 23.0 * scale[0], 16.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], -3.0 * scale[0], -
              12.0 * scale[1], -11.0 * scale[0], -21.0 * scale[1])
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
    Moveto(668.0 * scale[0], 1323.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(320.0 * scale[0], 1255.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -8.0 * scale[1], -8.0 * scale[0], -
              15.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              7.0 * scale[1], 22.0 * scale[0], 15.0 * scale[1])
    Curveto_r(7.0 * scale[0], 8.0 * scale[1], 8.0 * scale[0],
              15.0 * scale[1], 2.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              7.0 * scale[1], -22.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(363.0 * scale[0], 1253.0 * scale[1], x, y)
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
    Moveto(206.0 * scale[0], 1208.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -4.0 * scale[1], 0.0 * scale[0], -
              9.0 * scale[1], -6.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -10.0 * scale[0], -
              14.0 * scale[1], -10.0 * scale[0], -23.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], -9.0 * scale[0], -
              24.0 * scale[1], -19.0 * scale[0], -32.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -7.0 * scale[1], -17.0 * scale[0], -
              18.0 * scale[1], -14.0 * scale[0], -24.0 * scale[1])
    Curveto_r(4.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              7.0 * scale[1], -10.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 3.0 * scale[1], -23.0 * scale[0], -
              1.0 * scale[1], -32.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -9.0 * scale[1], -15.0 * scale[0], -
              11.0 * scale[1], -15.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -14.0 * scale[0],
              20.0 * scale[1], -31.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 13.0 * scale[1], -29.0 * scale[0],
              19.0 * scale[1], -25.0 * scale[0], 12.0 * scale[1])
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 2.0 * scale[0], -
              11.0 * scale[1], -5.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0],
              11.0 * scale[1], -7.0 * scale[0], 30.0 * scale[1])
    Curveto_r(4.0 * scale[0], 27.0 * scale[1], 3.0 * scale[0],
              29.0 * scale[1], -12.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-22.0 * scale[0], -20.0 * scale[1], -24.0 *
              scale[0], -99.0 * scale[1], -2.0 * scale[0], -90.0 * scale[1])
    Curveto_r(12.0 * scale[0], 5.0 * scale[1], 13.0 * scale[0],
              3.0 * scale[1], 2.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -26.0 * scale[1], 3.0 * scale[0], -
              39.0 * scale[1], 78.0 * scale[0], -42.0 * scale[1])
    Lineto_r(67.0 * scale[0], -3.0 * scale[1])
    Lineto_r(-45.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 12.0 * scale[1], -49.0 * scale[0],
              21.0 * scale[1], -53.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -1.0 * scale[1], -6.0 * scale[0],
              2.0 * scale[1], -3.0 * scale[0], 6.0 * scale[1])
    Curveto_r(6.0 * scale[0], 10.0 * scale[1], 84.0 * scale[0], -
              10.0 * scale[1], 129.0 * scale[0], -34.0 * scale[1])
    Curveto_r(16.0 * scale[0], -7.0 * scale[1], 36.0 * scale[0], -
              14.0 * scale[1], 45.0 * scale[0], -13.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0],
              16.0 * scale[1], -53.0 * scale[0], 35.0 * scale[1])
    Lineto_r(-70.0 * scale[0], 34.0 * scale[1])
    Lineto_r(60.0 * scale[0], -4.0 * scale[1])
    Curveto_r(51.0 * scale[0], -3.0 * scale[1], 55.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-39.0 * scale[0], 14.0 * scale[1], -40.0 * scale[0],
              15.0 * scale[1], -22.0 * scale[0], 32.0 * scale[1])
    Curveto_r(9.0 * scale[0], 9.0 * scale[1], 28.0 * scale[0],
              14.0 * scale[1], 48.0 * scale[0], 12.0 * scale[1])
    Curveto_r(19.0 * scale[0], -2.0 * scale[1], 24.0 *
              scale[0], -1.0 * scale[1], 12.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-51.0 * scale[0], 10.0 * scale[1], -54.0 * scale[0],
              58.0 * scale[1], -3.0 * scale[0], 51.0 * scale[1])
    Curveto_r(17.0 * scale[0], -3.0 * scale[1], 26.0 * scale[0],
              0.0 * scale[1], 24.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 6.0 * scale[1], -17.0 * scale[0],
              11.0 * scale[1], -33.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -27.0 *
              scale[0], -3.0 * scale[1], -25.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(739.0 * scale[0], 1211.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(8.0 * scale[0], -5.0 * scale[1], 12.0 * scale[0], -
              18.0 * scale[1], 9.0 * scale[0], -28.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -11.0 * scale[1], 1.0 * scale[0], -
              28.0 * scale[1], 8.0 * scale[0], -38.0 * scale[1])
    Curveto_r(8.0 * scale[0], -10.0 * scale[1], 14.0 * scale[0], -
              14.0 * scale[1], 14.0 * scale[0], -8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -4.0 * scale[0],
              14.0 * scale[1], -8.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -7.0 * scale[0],
              19.0 * scale[1], -4.0 * scale[0], 36.0 * scale[1])
    Curveto_r(3.0 * scale[0], 24.0 * scale[1], 1.0 * scale[0],
              30.0 * scale[1], -14.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 0.0 * scale[1], -16.0 *
              scale[0], -2.0 * scale[1], -5.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(355.0 * scale[0], 1201.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              12.0 * scale[1], 3.0 * scale[0], -15.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 9.0 * scale[0],
              1.0 * scale[1], 9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], -3.0 * scale[0],
              19.0 * scale[1], -12.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(591.0 * scale[0], 1184.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(293.0 * scale[0], 1133.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 25.0 *
              scale[0], -2.0 * scale[1], 35.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -27.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(376.0 * scale[0], 1132.0 * scale[1], x, y)
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
    Moveto(248.0 * scale[0], 1083.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(353.0 * scale[0], 1033.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(648.0 * scale[0], 1023.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 30.0 *
              scale[0], -2.0 * scale[1], 40.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 0.0 * scale[1], -30.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(494.0 * scale[0], 865.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -8.0 * scale[1], -12.0 * scale[0], -
              15.0 * scale[1], -20.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0], -
              5.0 * scale[1], -14.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -6.0 * scale[0], -
              9.0 * scale[1], -14.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -17.0 * scale[0], -
              1.0 * scale[1], -20.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -10.0 * scale[1], -15.0 * scale[0], -
              14.0 * scale[1], -31.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 4.0 * scale[1], -23.0 * scale[0],
              2.0 * scale[1], -16.0 * scale[0], -6.0 * scale[1])
    Curveto_r(14.0 * scale[0], -17.0 * scale[1], -1.0 * scale[0], -
              37.0 * scale[1], -19.0 * scale[0], -26.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 16.0 * scale[1], -35.0 * scale[0],
              11.0 * scale[1], -14.0 * scale[0], -6.0 * scale[1])
    Curveto_r(10.0 * scale[0], -8.0 * scale[1], 14.0 * scale[0], -
              13.0 * scale[1], 7.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 8.0 * scale[1], -44.0 * scale[0], -
              4.0 * scale[1], -37.0 * scale[0], -15.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 0.0 * scale[0], -
              9.0 * scale[1], -6.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              6.0 * scale[1], -7.0 * scale[0], -14.0 * scale[1])
    Curveto_r(4.0 * scale[0], -9.0 * scale[1], -8.0 * scale[0], -
              27.0 * scale[1], -29.0 * scale[0], -45.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -17.0 * scale[1], -30.0 *
              scale[0], -31.0 * scale[1], -24.0 * scale[0], -31.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0], -
              3.0 * scale[1], 9.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -22.0 * scale[1], 2.0 * scale[0], -
              33.0 * scale[1], 13.0 * scale[0], -27.0 * scale[1])
    Curveto_r(7.0 * scale[0], 5.0 * scale[1], 9.0 * scale[0],
              2.0 * scale[1], 6.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -9.0 * scale[1], 0.0 * scale[0], -
              15.0 * scale[1], 8.0 * scale[0], -15.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0],
              5.0 * scale[1], 14.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 6.0 * scale[0],
              7.0 * scale[1], 14.0 * scale[0], 4.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 20.0 * scale[0],
              1.0 * scale[1], 26.0 * scale[0], 9.0 * scale[1])
    Curveto_r(7.0 * scale[0], 8.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 31.0 * scale[0], 14.0 * scale[1])
    Curveto_r(24.0 * scale[0], 0.0 * scale[1], 33.0 * scale[0],
              17.0 * scale[1], 14.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 7.0 * scale[1], -12.0 * scale[0],
              15.0 * scale[1], -6.0 * scale[0], 38.0 * scale[1])
    Curveto_r(9.0 * scale[0], 28.0 * scale[1], 16.0 * scale[0],
              18.0 * scale[1], 11.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -12.0 * scale[1], 1.0 * scale[0], -
              13.0 * scale[1], 14.0 * scale[0], -2.0 * scale[1])
    Curveto_r(8.0 * scale[0], 7.0 * scale[1], 12.0 * scale[0],
              19.0 * scale[1], 10.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], 1.0 * scale[0],
              24.0 * scale[1], 10.0 * scale[0], 37.0 * scale[1])
    Curveto_r(9.0 * scale[0], 12.0 * scale[1], 16.0 * scale[0],
              19.0 * scale[1], 16.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 15.0 * scale[0],
              6.0 * scale[1], 32.0 * scale[0], 23.0 * scale[1])
    Curveto_r(18.0 * scale[0], 16.0 * scale[1], 40.0 * scale[0],
              29.0 * scale[1], 49.0 * scale[0], 29.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0],
              7.0 * scale[1], 23.0 * scale[0], 16.0 * scale[1])
    Curveto_r(4.0 * scale[0], 9.0 * scale[1], 13.0 * scale[0],
              14.0 * scale[1], 21.0 * scale[0], 10.0 * scale[1])
    Curveto_r(12.0 * scale[0], -4.0 * scale[1], 13.0 *
              scale[0], -2.0 * scale[1], 6.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], -7.0 * scale[0],
              21.0 * scale[1], -4.0 * scale[0], 25.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0],
              6.0 * scale[1], -31.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 0.0 * scale[1], -39.0 * scale[0], -
              5.0 * scale[1], -42.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(248.0 * scale[0], 763.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(420.0 * scale[0], 670.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(477.0 * scale[0], 639.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -27.0 *
              scale[0], -7.0 * scale[1], -40.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 5.0 * scale[1], -20.0 * scale[0],
              4.0 * scale[1], -4.0 * scale[0], -5.0 * scale[1])
    Curveto_r(9.0 * scale[0], -6.0 * scale[1], 17.0 * scale[0], -
              17.0 * scale[1], 17.0 * scale[0], -24.0 * scale[1])
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 29.0 * scale[0], -
              30.0 * scale[1], 38.0 * scale[0], -21.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 3.0 * scale[0],
              5.0 * scale[1], -1.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -2.0 * scale[0],
              14.0 * scale[1], 3.0 * scale[0], 30.0 * scale[1])
    Curveto_r(5.0 * scale[0], 17.0 * scale[1], 8.0 * scale[0],
              30.0 * scale[1], 7.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              5.0 * scale[1], -20.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(668.0 * scale[0], 636.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-18.0 * scale[0], -13.0 * scale[1], -14.0 *
              scale[0], -26.0 * scale[1], 8.0 * scale[0], -26.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              9.0 * scale[1], 11.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 11.0 * scale[1], -1.0 * scale[0],
              20.0 * scale[1], -2.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              7.0 * scale[1], -17.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(501.0 * scale[0], 607.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -8.0 * scale[1], -8.0 * scale[0], -
              17.0 * scale[1], -4.0 * scale[0], -20.0 * scale[1])
    Curveto_r(11.0 * scale[0], -12.0 * scale[1], 21.0 *
              scale[0], -7.0 * scale[1], 26.0 * scale[0], 13.0 * scale[1])
    Curveto_r(6.0 * scale[0], 23.0 * scale[1], -5.0 * scale[0],
              26.0 * scale[1], -22.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(617.0 * scale[0], 577.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -42.0 * scale[1], -2.0 *
              scale[0], -45.0 * scale[1], 11.0 * scale[0], -8.0 * scale[1])
    Curveto_r(6.0 * scale[0], 17.0 * scale[1], 7.0 * scale[0],
              33.0 * scale[1], 3.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 2.0 * scale[1], -11.0 * scale[0], -
              10.0 * scale[1], -14.0 * scale[0], -28.0 * scale[1])
    te.end_fill()
    Moveto(557.0 * scale[0], 593.0 * scale[1], x, y)
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
    Moveto(699.0 * scale[0], 594.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -5.0 * scale[1], 0.0 * scale[0], -
              22.0 * scale[1], 1.0 * scale[0], -37.0 * scale[1])
    Curveto_r(1.0 * scale[0], -15.0 * scale[1], -4.0 * scale[0], -
              35.0 * scale[1], -11.0 * scale[0], -43.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -20.0 * scale[1], -3.0 *
              scale[0], -30.0 * scale[1], 16.0 * scale[0], -11.0 * scale[1])
    Curveto_r(10.0 * scale[0], 11.0 * scale[1], 14.0 * scale[0],
              27.0 * scale[1], 10.0 * scale[0], 53.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 35.0 * scale[1], -14.0 * scale[0],
              58.0 * scale[1], -16.0 * scale[0], 38.0 * scale[1])
    te.end_fill()
    Moveto(491.0 * scale[0], 554.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(235.0 * scale[0], 450.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -3.0 * scale[0], -
              10.0 * scale[1], 0.0 * scale[0], -10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 0.0 * scale[1], -3.0 * scale[0], -
              9.0 * scale[1], -13.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -11.0 * scale[1], -24.0 *
              scale[0], -43.0 * scale[1], -31.0 * scale[0], -71.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -43.0 * scale[1], -11.0 *
              scale[0], -53.0 * scale[1], 0.0 * scale[0], -60.0 * scale[1])
    Curveto_r(8.0 * scale[0], -5.0 * scale[1], 13.0 * scale[0], -
              21.0 * scale[1], 11.0 * scale[0], -39.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -20.0 * scale[1], 2.0 * scale[0], -
              36.0 * scale[1], 12.0 * scale[0], -43.0 * scale[1])
    Curveto_r(11.0 * scale[0], -9.0 * scale[1], 16.0 * scale[0], -
              33.0 * scale[1], 18.0 * scale[0], -87.0 * scale[1])
    Curveto_r(2.0 * scale[0], -54.0 * scale[1], 7.0 * scale[0], -
              74.0 * scale[1], 16.0 * scale[0], -72.0 * scale[1])
    Curveto_r(6.0 * scale[0], 1.0 * scale[1], 12.0 * scale[0], -
              4.0 * scale[1], 12.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 4.0 * scale[0], -
              8.0 * scale[1], 10.0 * scale[0], 2.0 * scale[1])
    Curveto_r(9.0 * scale[0], 13.0 * scale[1], 10.0 * scale[0],
              13.0 * scale[1], 10.0 * scale[0], 0.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 3.0 * scale[0], -
              11.0 * scale[1], 8.0 * scale[0], -5.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], 15.0 * scale[0],
              15.0 * scale[1], 25.0 * scale[0], 20.0 * scale[1])
    Curveto_r(10.0 * scale[0], 6.0 * scale[1], 26.0 * scale[0],
              24.0 * scale[1], 35.0 * scale[0], 40.0 * scale[1])
    Curveto_r(9.0 * scale[0], 17.0 * scale[1], 22.0 * scale[0],
              33.0 * scale[1], 27.0 * scale[0], 37.0 * scale[1])
    Curveto_r(6.0 * scale[0], 5.0 * scale[1], 6.0 * scale[0],
              8.0 * scale[1], -2.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0], -
              17.0 * scale[1], -30.0 * scale[0], -37.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -40.0 * scale[1], -43.0 *
              scale[0], -55.0 * scale[1], -43.0 * scale[0], -28.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], 4.0 * scale[0],
              13.0 * scale[1], 10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              0.0 * scale[1], 5.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 16.0 * scale[1], 32.0 * scale[0],
              107.0 * scale[1], 45.0 * scale[0], 107.0 * scale[1])
    Curveto_r(16.0 * scale[0], 0.0 * scale[1], 58.0 * scale[0],
              64.0 * scale[1], 64.0 * scale[0], 100.0 * scale[1])
    Lineto_r(7.0 * scale[0], 35.0 * scale[1])
    Lineto_r(-14.0 * scale[0], -30.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -17.0 * scale[1], -21.0 * scale[0], -
              36.0 * scale[1], -29.0 * scale[0], -42.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -11.0 * scale[1], -16.0 *
              scale[0], -7.0 * scale[1], -26.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 35.0 * scale[1], -10.0 * scale[0],
              38.0 * scale[1], 24.0 * scale[0], 67.0 * scale[1])
    Curveto_r(20.0 * scale[0], 16.0 * scale[1], 42.0 * scale[0],
              42.0 * scale[1], 49.0 * scale[0], 57.0 * scale[1])
    Curveto_r(8.0 * scale[0], 15.0 * scale[1], 26.0 * scale[0],
              30.0 * scale[1], 41.0 * scale[0], 33.0 * scale[1])
    Curveto_r(14.0 * scale[0], 4.0 * scale[1], 24.0 * scale[0],
              9.0 * scale[1], 22.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 2.0 * scale[1], -24.0 * scale[0], -
              2.0 * scale[1], -47.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-23.0 * scale[0], -8.0 * scale[1], -39.0 *
              scale[0], -10.0 * scale[1], -36.0 * scale[0], -5.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 1.0 * scale[0],
              10.0 * scale[1], -4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              5.0 * scale[1], -11.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -10.0 * scale[0], -
              9.0 * scale[1], -25.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 3.0 * scale[1], -22.0 * scale[0],
              2.0 * scale[1], -20.0 * scale[0], -2.0 * scale[1])
    Curveto_r(9.0 * scale[0], -15.0 * scale[1], -70.0 *
              scale[0], -1.0 * scale[1], -81.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 18.0 * scale[1], -30.0 * scale[0],
              21.0 * scale[1], -39.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(668.0 * scale[0], 357.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -71.0 * scale[1], 3.0 * scale[0], -
              80.0 * scale[1], -22.0 * scale[0], -117.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -22.0 * scale[1], -26.0 *
              scale[0], -46.0 * scale[1], -26.0 * scale[0], -55.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -4.0 * scale[0], -
              15.0 * scale[1], -10.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0],
              3.0 * scale[1], -9.0 * scale[0], 8.0 * scale[1])
    Curveto_r(1.0 * scale[0], 4.0 * scale[1], 1.0 * scale[0],
              16.0 * scale[1], 0.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 19.0 * scale[1], -3.0 * scale[0],
              19.0 * scale[1], -13.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -25.0 * scale[1], -33.0 *
              scale[0], -30.0 * scale[1], -41.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -6.0 * scale[0],
              2.0 * scale[1], -6.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -16.0 * scale[1], -7.0 * scale[0], -
              21.0 * scale[1], -22.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 1.0 * scale[1], -21.0 * scale[0],
              5.0 * scale[1], -16.0 * scale[0], 64.0 * scale[1])
    Curveto_r(4.0 * scale[0], 38.0 * scale[1], 2.0 * scale[0],
              63.0 * scale[1], -3.0 * scale[0], 63.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              15.0 * scale[1], -10.0 * scale[0], -32.0 * scale[1])
    Curveto_r(0.0 * scale[0], -18.0 * scale[1], -5.0 * scale[0], -
              40.0 * scale[1], -10.0 * scale[0], -48.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -11.0 * scale[1], -10.0 * scale[0],
              7.0 * scale[1], -9.0 * scale[0], 58.0 * scale[1])
    Curveto_r(1.0 * scale[0], 40.0 * scale[1], -1.0 * scale[0],
              75.0 * scale[1], -5.0 * scale[0], 79.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -6.0 * scale[0], -
              5.0 * scale[1], -6.0 * scale[0], -19.0 * scale[1])
    Curveto_r(0.0 * scale[0], -33.0 * scale[1], -19.0 * scale[0], -
              88.0 * scale[1], -31.0 * scale[0], -88.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              6.0 * scale[1], -9.0 * scale[0], -12.0 * scale[1])
    Curveto_r(1.0 * scale[0], -7.0 * scale[1], 10.0 * scale[0], -
              2.0 * scale[1], 20.0 * scale[0], 11.0 * scale[1])
    Curveto_r(15.0 * scale[0], 17.0 * scale[1], 20.0 * scale[0],
              19.0 * scale[1], 20.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], -26.0 * scale[1], -49.0 * scale[0], -
              148.0 * scale[1], -76.0 * scale[0], -190.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -31.0 * scale[1], -23.0 *
              scale[0], -40.0 * scale[1], -12.0 * scale[0], -47.0 * scale[1])
    Curveto_r(20.0 * scale[0], -13.0 * scale[1], 215.0 *
              scale[0], -11.0 * scale[1], 224.0 * scale[0], 2.0 * scale[1])
    Curveto_r(4.0 * scale[0], 8.0 * scale[1], 9.0 * scale[0],
              7.0 * scale[1], 16.0 * scale[0], -2.0 * scale[1])
    Curveto_r(8.0 * scale[0], -11.0 * scale[1], 9.0 *
              scale[0], -10.0 * scale[1], 5.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 25.0 * scale[1], 13.0 * scale[0],
              91.0 * scale[1], 34.0 * scale[0], 106.0 * scale[1])
    Curveto_r(11.0 * scale[0], 7.0 * scale[1], 19.0 * scale[0],
              19.0 * scale[1], 19.0 * scale[0], 25.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -4.0 * scale[0],
              6.0 * scale[1], -10.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -13.0 * scale[1], -10.0 *
              scale[0], -13.0 * scale[1], -10.0 * scale[0], 2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], 7.0 * scale[0],
              24.0 * scale[1], 16.0 * scale[0], 33.0 * scale[1])
    Curveto_r(12.0 * scale[0], 11.0 * scale[1], 15.0 * scale[0],
              26.0 * scale[1], 11.0 * scale[0], 51.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 19.0 * scale[1], -1.0 * scale[0],
              34.0 * scale[1], 4.0 * scale[0], 34.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 5.0 * scale[0],
              115.0 * scale[1], -9.0 * scale[0], 150.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 18.0 * scale[1], -8.0 * scale[0],
              4.0 * scale[1], -4.0 * scale[0], -53.0 * scale[1])
    te.end_fill()
    Moveto(406.0 * scale[0], 195.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -26.0 * scale[1], -7.0 *
              scale[0], -32.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(6.0 * scale[0], 10.0 * scale[1], 9.0 * scale[0],
              21.0 * scale[1], 6.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 3.0 * scale[1], -7.0 * scale[0], -
              2.0 * scale[1], -11.0 * scale[0], -11.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#c14225')
    te.end_fill()
    Moveto(377.0 * scale[0], 694.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -19.0 * scale[1], 0.0 * scale[0], -
              33.0 * scale[1], 11.0 * scale[0], -42.0 * scale[1])
    Curveto_r(10.0 * scale[0], -7.0 * scale[1], 12.0 *
              scale[0], -11.0 * scale[1], 6.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -11.0 * scale[0], -
              1.0 * scale[1], -11.0 * scale[0], -9.0 * scale[1])
    Curveto_r(0.0 * scale[0], -18.0 * scale[1], 6.0 * scale[0], -
              18.0 * scale[1], 32.0 * scale[0], -2.0 * scale[1])
    Curveto_r(24.0 * scale[0], 14.0 * scale[1], 32.0 * scale[0],
              39.0 * scale[1], 10.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -4.0 * scale[1], -15.0 *
              scale[0], -1.0 * scale[1], -15.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              8.0 * scale[1], -12.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -5.0 * scale[1], -9.0 *
              scale[0], -2.0 * scale[1], -6.0 * scale[0], 8.0 * scale[1])
    Curveto_r(4.0 * scale[0], 8.0 * scale[1], 3.0 * scale[0],
              20.0 * scale[1], -2.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 9.0 * scale[1], -9.0 * scale[0],
              3.0 * scale[1], -13.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(639.0 * scale[0], 609.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -5.0 * scale[1], -11.0 *
              scale[0], -9.0 * scale[1], -7.0 * scale[0], -9.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 3.0 * scale[0], -
              13.0 * scale[1], -3.0 * scale[0], -28.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -33.0 * scale[1], -48.0 *
              scale[0], -41.0 * scale[1], -56.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 12.0 * scale[1], -12.0 * scale[0],
              17.0 * scale[1], -25.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-26.0 * scale[0], -5.0 * scale[1], -61.0 * scale[0],
              13.0 * scale[1], -52.0 * scale[0], 27.0 * scale[1])
    Curveto_r(4.0 * scale[0], 7.0 * scale[1], 3.0 * scale[0],
              8.0 * scale[1], -4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -4.0 * scale[1], -10.0 * scale[0], -
              31.0 * scale[1], -8.0 * scale[0], -71.0 * scale[1])
    Curveto_r(3.0 * scale[0], -52.0 * scale[1], 1.0 * scale[0], -
              67.0 * scale[1], -12.0 * scale[0], -76.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -8.0 * scale[1], -12.0 *
              scale[0], -9.0 * scale[1], 8.0 * scale[0], -4.0 * scale[1])
    Curveto_r(22.0 * scale[0], 5.0 * scale[1], 23.0 * scale[0],
              4.0 * scale[1], 7.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -7.0 * scale[1], -26.0 *
              scale[0], -9.0 * scale[1], -35.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 3.0 * scale[1], -13.0 * scale[0],
              3.0 * scale[1], -10.0 * scale[0], -1.0 * scale[1])
    Curveto_r(11.0 * scale[0], -11.0 * scale[1], -18.0 * scale[0], -
              58.0 * scale[1], -56.0 * scale[0], -90.0 * scale[1])
    Curveto_r(-34.0 * scale[0], -29.0 * scale[1], -35.0 *
              scale[0], -32.0 * scale[1], -24.0 * scale[0], -67.0 * scale[1])
    Curveto_r(10.0 * scale[0], -31.0 * scale[1], 14.0 * scale[0], -
              35.0 * scale[1], 26.0 * scale[0], -24.0 * scale[1])
    Curveto_r(8.0 * scale[0], 6.0 * scale[1], 21.0 * scale[0],
              25.0 * scale[1], 29.0 * scale[0], 42.0 * scale[1])
    Lineto_r(14.0 * scale[0], 30.0 * scale[1])
    Lineto_r(-6.0 * scale[0], -35.0 * scale[1])
    Lineto_r(-6.0 * scale[0], -35.0 * scale[1])
    Lineto_r(22.0 * scale[0], 42.0 * scale[1])
    Curveto_r(13.0 * scale[0], 24.0 * scale[1], 25.0 * scale[0],
              41.0 * scale[1], 27.0 * scale[0], 38.0 * scale[1])
    Curveto_r(3.0 * scale[0], -2.0 * scale[1], 4.0 * scale[0], -
              37.0 * scale[1], 3.0 * scale[0], -77.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -51.0 * scale[1], 2.0 * scale[0], -
              69.0 * scale[1], 9.0 * scale[0], -58.0 * scale[1])
    Curveto_r(5.0 * scale[0], 8.0 * scale[1], 10.0 * scale[0],
              30.0 * scale[1], 10.0 * scale[0], 48.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], 4.0 * scale[0],
              32.0 * scale[1], 10.0 * scale[0], 32.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0], -
              25.0 * scale[1], 3.0 * scale[0], -63.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -59.0 * scale[1], -4.0 * scale[0], -
              63.0 * scale[1], 16.0 * scale[0], -64.0 * scale[1])
    Curveto_r(15.0 * scale[0], -1.0 * scale[1], 21.0 * scale[0],
              4.0 * scale[1], 22.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], 3.0 * scale[0],
              16.0 * scale[1], 6.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -20.0 * scale[1], 29.0 *
              scale[0], -15.0 * scale[1], 41.0 * scale[0], 9.0 * scale[1])
    Curveto_r(10.0 * scale[0], 22.0 * scale[1], 11.0 * scale[0],
              22.0 * scale[1], 13.0 * scale[0], 3.0 * scale[1])
    Curveto_r(1.0 * scale[0], -11.0 * scale[1], 1.0 * scale[0], -
              23.0 * scale[1], 0.0 * scale[0], -27.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 3.0 * scale[0], -
              8.0 * scale[1], 9.0 * scale[0], -8.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              7.0 * scale[1], 10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], 11.0 * scale[0],
              32.0 * scale[1], 24.0 * scale[0], 53.0 * scale[1])
    Curveto_r(18.0 * scale[0], 28.0 * scale[1], 25.0 * scale[0],
              54.0 * scale[1], 28.0 * scale[0], 109.0 * scale[1])
    Curveto_r(2.0 * scale[0], 40.0 * scale[1], 0.0 * scale[0],
              67.0 * scale[1], -4.0 * scale[0], 60.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -22.0 * scale[1], 4.0 * scale[0],
              77.0 * scale[1], 19.0 * scale[0], 101.0 * scale[1])
    Curveto_r(20.0 * scale[0], 33.0 * scale[1], 13.0 * scale[0],
              93.0 * scale[1], -13.0 * scale[0], 103.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 4.0 * scale[1], -27.0 * scale[0],
              3.0 * scale[1], -35.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto_r(-142.0 * scale[0], -61.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -6.0 *
              scale[0], -5.0 * scale[1], -6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 11.0 * scale[1], 2.0 * scale[0],
              17.0 * scale[1], 5.0 * scale[0], 13.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 4.0 * scale[0], -
              12.0 * scale[1], 1.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(457.0 * scale[0], 493.0 * scale[1], x, y)
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
    Moveto(368.0 * scale[0], 207.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-14.0 * scale[0], -12.0 * scale[1], -28.0 *
              scale[0], -31.0 * scale[1], -30.0 * scale[0], -42.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -11.0 * scale[1], -9.0 * scale[0], -
              26.0 * scale[1], -15.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -18.0 * scale[1], -16.0 *
              scale[0], -32.0 * scale[1], 2.0 * scale[0], -32.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              9.0 * scale[1], 15.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], 8.0 * scale[0],
              24.0 * scale[1], 19.0 * scale[0], 29.0 * scale[1])
    Curveto_r(10.0 * scale[0], 6.0 * scale[1], 21.0 * scale[0],
              18.0 * scale[1], 25.0 * scale[0], 26.0 * scale[1])
    Curveto_r(3.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              13.0 * scale[1], -4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -10.0 * scale[1], -12.0 *
              scale[0], 7.0 * scale[1], 7.0 * scale[0], 27.0 * scale[1])
    Curveto_r(22.0 * scale[0], 24.0 * scale[1], 14.0 * scale[0],
              22.0 * scale[1], -19.0 * scale[0], -5.0 * scale[1])
    te.penup()
