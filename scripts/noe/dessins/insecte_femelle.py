import turtle as te
from helper import *


def insecte_femelle(x, y, scale):

    te.penup()
    te.color('#d39b8a')
    te.end_fill()
    Moveto(445.0 * scale[0], 1330.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -9.0 * scale[0], -
              8.0 * scale[1], -13.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 11.0 * scale[1], -72.0 * scale[0], -
              58.0 * scale[1], -56.0 * scale[0], -72.0 * scale[1])
    Curveto_r(4.0 * scale[0], -4.0 * scale[1], 9.0 * scale[0], -
              1.0 * scale[1], 11.0 * scale[0], 6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 9.0 * scale[0],
              10.0 * scale[1], 14.0 * scale[0], 7.0 * scale[1])
    Curveto_r(5.0 * scale[0], -4.0 * scale[1], 6.0 * scale[0],
              2.0 * scale[1], 2.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 11.0 * scale[1], -2.0 * scale[0],
              15.0 * scale[1], 4.0 * scale[0], 11.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 14.0 * scale[0],
              0.0 * scale[1], 17.0 * scale[0], 9.0 * scale[1])
    Curveto_r(4.0 * scale[0], 9.0 * scale[1], 13.0 * scale[0],
              14.0 * scale[1], 22.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 12.0 *
              scale[0], -2.0 * scale[1], 9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], 7.0 * scale[0],
              10.0 * scale[1], 24.0 * scale[0], 10.0 * scale[1])
    Curveto_r(17.0 * scale[0], 0.0 * scale[1], 31.0 * scale[0], -
              4.0 * scale[1], 31.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0], -
              9.0 * scale[1], 11.0 * scale[0], -7.0 * scale[1])
    Curveto_r(12.0 * scale[0], 2.0 * scale[1], 19.0 * scale[0], -
              19.0 * scale[1], 22.0 * scale[0], -70.0 * scale[1])
    Curveto_r(3.0 * scale[0], -36.0 * scale[1], 17.0 * scale[0], -
              57.0 * scale[1], 18.0 * scale[0], -27.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], 3.0 * scale[0],
              13.0 * scale[1], 6.0 * scale[0], 7.0 * scale[1])
    Curveto_r(8.0 * scale[0], -21.0 * scale[1], 19.0 * scale[0], -
              15.0 * scale[1], 21.0 * scale[0], 13.0 * scale[1])
    Curveto_r(2.0 * scale[0], 28.0 * scale[1], -25.0 * scale[0],
              87.0 * scale[1], -37.0 * scale[0], 80.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -3.0 * scale[1], -15.0 * scale[0],
              4.0 * scale[1], -24.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 20.0 * scale[1], -71.0 * scale[0],
              26.0 * scale[1], -82.0 * scale[0], 9.0 * scale[1])
    te.end_fill()
    Moveto(79.0 * scale[0], 1283.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-18.0 * scale[0], -18.0 * scale[1], -20.0 *
              scale[0], -26.0 * scale[1], -10.0 * scale[0], -36.0 * scale[1])
    Curveto_r(10.0 * scale[0], -9.0 * scale[1], 11.0 *
              scale[0], -8.0 * scale[1], 5.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 13.0 * scale[1], -2.0 * scale[0],
              16.0 * scale[1], 9.0 * scale[0], 11.0 * scale[1])
    Curveto_r(10.0 * scale[0], -3.0 * scale[1], 13.0 * scale[0], -
              12.0 * scale[1], 9.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -15.0 * scale[1], -4.0 *
              scale[0], -15.0 * scale[1], 13.0 * scale[0], -2.0 * scale[1])
    Curveto_r(16.0 * scale[0], 14.0 * scale[1], 17.0 * scale[0],
              13.0 * scale[1], 11.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -31.0 * scale[1], -15.0 * scale[0], -
              114.0 * scale[1], -8.0 * scale[0], -114.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 38.0 * scale[0],
              20.0 * scale[1], 27.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0],
              19.0 * scale[1], -11.0 * scale[0], 43.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 23.0 * scale[1], 1.0 * scale[0],
              31.0 * scale[1], 3.0 * scale[0], 18.0 * scale[1])
    Curveto_r(4.0 * scale[0], -19.0 * scale[1], 7.0 * scale[0], -
              21.0 * scale[1], 14.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 10.0 * scale[1], 9.0 * scale[0],
              3.0 * scale[1], 9.0 * scale[0], -23.0 * scale[1])
    Curveto_r(0.0 * scale[0], -20.0 * scale[1], 5.0 * scale[0], -
              40.0 * scale[1], 11.0 * scale[0], -44.0 * scale[1])
    Curveto_r(8.0 * scale[0], -5.0 * scale[1], 9.0 * scale[0],
              12.0 * scale[1], 3.0 * scale[0], 57.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 35.0 * scale[1], -7.0 * scale[0],
              78.0 * scale[1], -8.0 * scale[0], 94.0 * scale[1])
    Curveto_r(0.0 * scale[0], 26.0 * scale[1], -4.0 * scale[0],
              30.0 * scale[1], -27.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 1.0 * scale[1], -37.0 * scale[0], -
              8.0 * scale[1], -50.0 * scale[0], -23.0 * scale[1])
    te.end_fill()
    Moveto_r(40.0 * scale[0], 14.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -1.0 * scale[1], -13.0 * scale[0], -
              9.0 * scale[1], -24.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -14.0 * scale[1], -19.0 *
              scale[0], -14.0 * scale[1], -6.0 * scale[0], 3.0 * scale[1])
    Curveto_r(7.0 * scale[0], 9.0 * scale[1], 18.0 * scale[0],
              17.0 * scale[1], 24.0 * scale[0], 17.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0], -
              1.0 * scale[1], 6.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(810.0 * scale[0], 1285.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-21.0 * scale[0], -22.0 * scale[1], -22.0 *
              scale[0], -27.0 * scale[1], -9.0 * scale[0], -40.0 * scale[1])
    Curveto_r(10.0 * scale[0], -10.0 * scale[1], 18.0 *
              scale[0], -11.0 * scale[1], 29.0 * scale[0], -4.0 * scale[1])
    Curveto_r(13.0 * scale[0], 9.0 * scale[1], 12.0 * scale[0],
              10.0 * scale[1], -2.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -6.0 * scale[1], -25.0 * scale[0],
              8.0 * scale[1], -9.0 * scale[0], 18.0 * scale[1])
    Curveto_r(11.0 * scale[0], 7.0 * scale[1], 33.0 * scale[0], -
              18.0 * scale[1], 24.0 * scale[0], -27.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -9.0 * scale[1], -12.0 * scale[0], -
              92.0 * scale[1], -4.0 * scale[0], -106.0 * scale[1])
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 12.0 * scale[0], -
              7.0 * scale[1], 21.0 * scale[0], -1.0 * scale[1])
    Curveto_r(10.0 * scale[0], 7.0 * scale[1], 11.0 * scale[0],
              10.0 * scale[1], 3.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0],
              15.0 * scale[1], -12.0 * scale[0], 43.0 * scale[1])
    Curveto_r(1.0 * scale[0], 28.0 * scale[1], 3.0 * scale[0],
              34.0 * scale[1], 7.0 * scale[0], 17.0 * scale[1])
    Curveto_r(4.0 * scale[0], -23.0 * scale[1], 5.0 * scale[0], -
              24.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    Curveto_r(6.0 * scale[0], 15.0 * scale[1], 8.0 * scale[0],
              10.0 * scale[1], 8.0 * scale[0], -22.0 * scale[1])
    Curveto_r(1.0 * scale[0], -23.0 * scale[1], 6.0 * scale[0], -
              45.0 * scale[1], 12.0 * scale[0], -49.0 * scale[1])
    Curveto_r(8.0 * scale[0], -5.0 * scale[1], 9.0 * scale[0],
              11.0 * scale[1], 3.0 * scale[0], 57.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 35.0 * scale[1], -8.0 * scale[0],
              78.0 * scale[1], -7.0 * scale[0], 95.0 * scale[1])
    Curveto_r(0.0 * scale[0], 25.0 * scale[1], -4.0 * scale[0],
              30.0 * scale[1], -19.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -2.0 * scale[1], -18.0 *
              scale[0], -9.0 * scale[1], -18.0 * scale[0], -14.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -5.0 * scale[0], -
              6.0 * scale[1], -10.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -8.0 * scale[0],
              11.0 * scale[1], -5.0 * scale[0], 16.0 * scale[1])
    Curveto_r(11.0 * scale[0], 17.0 * scale[1], -1.0 * scale[0],
              9.0 * scale[1], -25.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto_r(20.0 * scale[0], 1.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], -8.0 * scale[0], -
              10.0 * scale[1], -17.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -13.0 * scale[1], -17.0 *
              scale[0], -12.0 * scale[1], -4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(13.0 * scale[0], 16.0 * scale[1], 21.0 * scale[0],
              21.0 * scale[1], 21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(342.0 * scale[0], 1250.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(600.0 * scale[0], 1258.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], 5.0 * scale[0], -
              20.0 * scale[1], 11.0 * scale[0], -28.0 * scale[1])
    Curveto_r(9.0 * scale[0], -12.0 * scale[1], 10.0 *
              scale[0], -10.0 * scale[1], 6.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 19.0 * scale[1], -3.0 * scale[0],
              21.0 * scale[1], 9.0 * scale[0], 11.0 * scale[1])
    Curveto_r(7.0 * scale[0], -6.0 * scale[1], 12.0 * scale[0], -
              14.0 * scale[1], 10.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -3.0 * scale[1], 2.0 * scale[0], -
              11.0 * scale[1], 9.0 * scale[0], -18.0 * scale[1])
    Curveto_r(10.0 * scale[0], -9.0 * scale[1], 17.0 *
              scale[0], -9.0 * scale[1], 30.0 * scale[0], 1.0 * scale[1])
    Curveto_r(13.0 * scale[0], 9.0 * scale[1], 15.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -12.0 * scale[0],
              2.0 * scale[1], -12.0 * scale[0], -3.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -4.0 * scale[0], -
              11.0 * scale[1], -10.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0],
              6.0 * scale[1], -4.0 * scale[0], 13.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], -6.0 * scale[0],
              18.0 * scale[1], -21.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-32.0 * scale[0], 15.0 * scale[1], -35.0 * scale[0],
              15.0 * scale[1], -35.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(303.0 * scale[0], 1249.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -5.0 * scale[1], -23.0 * scale[0], -
              14.0 * scale[1], -23.0 * scale[0], -22.0 * scale[1])
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], 68.0 * scale[0], -
              52.0 * scale[1], 76.0 * scale[0], -44.0 * scale[1])
    Curveto_r(9.0 * scale[0], 9.0 * scale[1], -9.0 * scale[0],
              37.0 * scale[1], -28.0 * scale[0], 43.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 5.0 * scale[1], -18.0 * scale[0],
              8.0 * scale[1], -7.0 * scale[0], 15.0 * scale[1])
    Curveto_r(20.0 * scale[0], 12.0 * scale[1], 7.0 * scale[0],
              18.0 * scale[1], -18.0 * scale[0], 8.0 * scale[1])
    te.end_fill()
    Moveto_r(38.0 * scale[0], -46.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(13.0 * scale[0], -17.0 * scale[1], 13.0 *
              scale[0], -17.0 * scale[1], -6.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 8.0 * scale[1], -22.0 * scale[0],
              16.0 * scale[1], -24.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 2.0 * scale[1], 0.0 * scale[0],
              3.0 * scale[1], 6.0 * scale[0], 3.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0], -
              8.0 * scale[1], 24.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(370.0 * scale[0], 1213.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -49.0 * scale[1], 56.0 * scale[0], -
              94.0 * scale[1], 117.0 * scale[0], -92.0 * scale[1])
    Curveto_r(33.0 * scale[0], 2.0 * scale[1], 34.0 * scale[0],
              3.0 * scale[1], 8.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 2.0 * scale[1], -37.0 * scale[0],
              7.0 * scale[1], -45.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -19.0 * scale[0],
              7.0 * scale[1], -25.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 1.0 * scale[1], -20.0 * scale[0],
              19.0 * scale[1], -32.0 * scale[0], 41.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 22.0 * scale[1], -23.0 * scale[0],
              35.0 * scale[1], -23.0 * scale[0], 28.0 * scale[1])
    te.end_fill()
    Moveto(600.0 * scale[0], 1194.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              16.0 * scale[1], 24.0 * scale[0], -8.0 * scale[1])
    Curveto_r(22.0 * scale[0], 8.0 * scale[1], 20.0 * scale[0],
              19.0 * scale[1], -4.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 1.0 * scale[1], -20.0 * scale[0], -
              4.0 * scale[1], -20.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(547.0 * scale[0], 1162.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-20.0 * scale[0], -22.0 * scale[1], -22.0 *
              scale[0], -33.0 * scale[1], -4.0 * scale[0], -26.0 * scale[1])
    Curveto_r(15.0 * scale[0], 6.0 * scale[1], 40.0 * scale[0],
              44.0 * scale[1], 29.0 * scale[0], 44.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0], -
              8.0 * scale[1], -25.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(870.0 * scale[0], 812.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -39.0 * scale[1], 2.0 * scale[0], -
              42.0 * scale[1], 15.0 * scale[0], -28.0 * scale[1])
    Curveto_r(19.0 * scale[0], 18.0 * scale[1], 19.0 * scale[0],
              27.0 * scale[1], 0.0 * scale[0], 52.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 18.0 * scale[1], -14.0 * scale[0],
              16.0 * scale[1], -15.0 * scale[0], -24.0 * scale[1])
    te.end_fill()
    Moveto(742.0 * scale[0], 823.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -2.0 * scale[1], -10.0 *
              scale[0], -9.0 * scale[1], -6.0 * scale[0], -14.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 0.0 * scale[0], -
              9.0 * scale[1], -6.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              6.0 * scale[1], 0.0 * scale[0], -20.0 * scale[1])
    Curveto_r(6.0 * scale[0], -11.0 * scale[1], 10.0 * scale[0], -
              28.0 * scale[1], 8.0 * scale[0], -37.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -9.0 * scale[1], 2.0 * scale[0], -
              18.0 * scale[1], 8.0 * scale[0], -20.0 * scale[1])
    Curveto_r(12.0 * scale[0], -4.0 * scale[1], 12.0 * scale[0],
              22.0 * scale[1], 0.0 * scale[0], 50.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 18.0 * scale[1], -2.0 * scale[0],
              32.0 * scale[1], 15.0 * scale[0], 32.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              19.0 * scale[1], 2.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 1.0 * scale[1], -14.0 * scale[0],
              0.0 * scale[1], -21.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(950.0 * scale[0], 774.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 5.0 * scale[0], -
              12.0 * scale[1], 10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 8.0 * scale[0],
              11.0 * scale[1], 5.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 14.0 * scale[1], -15.0 * scale[0],
              11.0 * scale[1], -15.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(710.0 * scale[0], 771.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 18.0 * scale[1], -14.0 * scale[0],
              21.0 * scale[1], -14.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(773.0 * scale[0], 704.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -6.0 * scale[1], -8.0 * scale[0], -
              15.0 * scale[1], -5.0 * scale[0], -20.0 * scale[1])
    Curveto_r(10.0 * scale[0], -13.0 * scale[1], 42.0 *
              scale[0], -17.0 * scale[1], 42.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], 5.0 * scale[0], 23.0 * scale[1])
    Curveto_r(7.0 * scale[0], 17.0 * scale[1], -27.0 * scale[0],
              19.0 * scale[1], -42.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(145.0 * scale[0], 661.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -11.0 * scale[1], 13.0 * scale[0], -
              26.0 * scale[1], 22.0 * scale[0], -17.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], 17.0 * scale[0], -
              1.0 * scale[1], 30.0 * scale[0], -9.0 * scale[1])
    Curveto_r(13.0 * scale[0], -9.0 * scale[1], 23.0 * scale[0], -
              12.0 * scale[1], 23.0 * scale[0], -8.0 * scale[1])
    Curveto_r(1.0 * scale[0], 5.0 * scale[1], 8.0 * scale[0], -
              5.0 * scale[1], 16.0 * scale[0], -20.0 * scale[1])
    Curveto_r(9.0 * scale[0], -16.0 * scale[1], 18.0 * scale[0], -
              27.0 * scale[1], 21.0 * scale[0], -24.0 * scale[1])
    Curveto_r(9.0 * scale[0], 10.0 * scale[1], -19.0 * scale[0],
              48.0 * scale[1], -50.0 * scale[0], 67.0 * scale[1])
    Curveto_r(-35.0 * scale[0], 22.0 * scale[1], -53.0 * scale[0],
              25.0 * scale[1], -62.0 * scale[0], 11.0 * scale[1])
    te.end_fill()
    Moveto(0.0 * scale[0], 598.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 2.0 * scale[0], -
              18.0 * scale[1], 5.0 * scale[0], -18.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              8.0 * scale[1], 14.0 * scale[0], 18.0 * scale[1])
    Curveto_r(8.0 * scale[0], 14.0 * scale[1], 6.0 * scale[0],
              19.0 * scale[1], -5.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0], -
              9.0 * scale[1], -14.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(40.0 * scale[0], 579.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-17.0 * scale[0], -30.0 * scale[1], -6.0 *
              scale[0], -34.0 * scale[1], 14.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 14.0 * scale[1], 12.0 * scale[0],
              25.0 * scale[1], 7.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              9.0 * scale[1], -21.0 * scale[0], -21.0 * scale[1])
    te.end_fill()
    Moveto(88.0 * scale[0], 573.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(118.0 * scale[0], 542.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(20.0 * scale[0], -22.0 * scale[1], 25.0 *
              scale[0], -21.0 * scale[1], 16.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -12.0 * scale[0],
              16.0 * scale[1], -20.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -10.0 *
              scale[0], -4.0 * scale[1], 4.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(0.0 * scale[0], 490.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 3.0 * scale[0], -
              21.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(9.0 * scale[0], 9.0 * scale[1], 9.0 * scale[0],
              15.0 * scale[1], 0.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 9.0 * scale[1], -12.0 * scale[0],
              7.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(124.0 * scale[0], 489.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -9.0 * scale[1], -2.0 * scale[0], -
              10.0 * scale[1], 12.0 * scale[0], -6.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 18.0 * scale[0],
              6.0 * scale[1], -1.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -15.0 * scale[1], -19.0 *
              scale[0], -16.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(14.0 * scale[0], 2.0 * scale[1], 25.0 * scale[0],
              10.0 * scale[1], 25.0 * scale[0], 18.0 * scale[1])
    Curveto_r(0.0 * scale[0], 19.0 * scale[1], -31.0 * scale[0],
              25.0 * scale[1], -41.0 * scale[0], 9.0 * scale[1])
    te.end_fill()
    Moveto(370.0 * scale[0], 19.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0], -
              7.0 * scale[1], 10.0 * scale[0], -4.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 10.0 * scale[0],
              8.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 2.0 * scale[1], -4.0 * scale[0],
              4.0 * scale[1], -10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              5.0 * scale[1], -10.0 * scale[0], -11.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#99afbb')
    te.end_fill()
    Moveto(46.0 * scale[0], 992.0 * scale[1], x, y)
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
    Moveto(253.0 * scale[0], 934.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-17.0 * scale[0], -8.0 * scale[1], -37.0 * scale[0], -
              29.0 * scale[1], -43.0 * scale[0], -45.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -16.0 * scale[1], -16.0 * scale[0], -
              29.0 * scale[1], -21.0 * scale[0], -29.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              7.0 * scale[1], -9.0 * scale[0], -16.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], -7.0 * scale[0], -
              22.0 * scale[1], -16.0 * scale[0], -29.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -10.0 * scale[1], -13.0 *
              scale[0], -13.0 * scale[1], 16.0 * scale[0], -19.0 * scale[1])
    Curveto_r(19.0 * scale[0], -3.0 * scale[1], 38.0 *
              scale[0], -2.0 * scale[1], 44.0 * scale[0], 4.0 * scale[1])
    Curveto_r(6.0 * scale[0], 6.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 27.0 * scale[0], -6.0 * scale[1])
    Curveto_r(13.0 * scale[0], -12.0 * scale[1], 19.0 *
              scale[0], -12.0 * scale[1], 25.0 * scale[0], -3.0 * scale[1])
    Curveto_r(4.0 * scale[0], 7.0 * scale[1], 3.0 * scale[0],
              10.0 * scale[1], -4.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -9.0 * scale[1], -23.0 * scale[0],
              7.0 * scale[1], -11.0 * scale[0], 24.0 * scale[1])
    Curveto_r(7.0 * scale[0], 12.0 * scale[1], 9.0 * scale[0],
              12.0 * scale[1], 9.0 * scale[0], 1.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 6.0 * scale[0], -
              11.0 * scale[1], 16.0 * scale[0], -7.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 13.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 0.0 * scale[0], -
              11.0 * scale[1], 8.0 * scale[0], -14.0 * scale[1])
    Curveto_r(10.0 * scale[0], -4.0 * scale[1], 12.0 * scale[0],
              0.0 * scale[1], 8.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 20.0 * scale[1], -4.0 * scale[0],
              21.0 * scale[1], 11.0 * scale[0], 8.0 * scale[1])
    Curveto_r(15.0 * scale[0], -12.0 * scale[1], 17.0 *
              scale[0], -12.0 * scale[1], 12.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], 7.0 * scale[0],
              22.0 * scale[1], 25.0 * scale[0], 34.0 * scale[1])
    Curveto_r(16.0 * scale[0], 11.0 * scale[1], 30.0 * scale[0],
              23.0 * scale[1], 30.0 * scale[0], 27.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], 7.0 * scale[0],
              5.0 * scale[1], 15.0 * scale[0], 2.0 * scale[1])
    Curveto_r(24.0 * scale[0], -10.0 * scale[1], 16.0 * scale[0],
              9.0 * scale[1], -14.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-39.0 * scale[0], 30.0 * scale[1], -98.0 * scale[0],
              38.0 * scale[1], -138.0 * scale[0], 17.0 * scale[1])
    te.end_fill()
    Moveto(484.0 * scale[0], 670.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -140.0 * scale[1], 2.0 * scale[0], -
              198.0 * scale[1], 3.0 * scale[0], -128.0 * scale[1])
    Curveto_r(2.0 * scale[0], 71.0 * scale[1], 2.0 * scale[0],
              185.0 * scale[1], 0.0 * scale[0], 255.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 71.0 * scale[1], -3.0 * scale[0],
              13.0 * scale[1], -3.0 * scale[0], -127.0 * scale[1])
    te.end_fill()
    Moveto(501.0 * scale[0], 730.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -184.0 * scale[1], 7.0 * scale[0], -
              229.0 * scale[1], 20.0 * scale[0], -209.0 * scale[1])
    Curveto_r(7.0 * scale[0], 11.0 * scale[1], 9.0 * scale[0],
              10.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], 6.0 * scale[0], -
              17.0 * scale[1], 18.0 * scale[0], -14.0 * scale[1])
    Curveto_r(9.0 * scale[0], 2.0 * scale[1], 30.0 * scale[0], -
              3.0 * scale[1], 45.0 * scale[0], -10.0 * scale[1])
    Curveto_r(23.0 * scale[0], -11.0 * scale[1], 39.0 *
              scale[0], -12.0 * scale[1], 78.0 * scale[0], -4.0 * scale[1])
    Curveto_r(62.0 * scale[0], 14.0 * scale[1], 59.0 * scale[0],
              14.0 * scale[1], 59.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 11.0 * scale[0], -
              21.0 * scale[1], 25.0 * scale[0], -27.0 * scale[1])
    Curveto_r(14.0 * scale[0], -6.0 * scale[1], 25.0 * scale[0], -
              16.0 * scale[1], 25.0 * scale[0], -22.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 5.0 * scale[0], -
              4.0 * scale[1], 10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(5.0 * scale[0], 8.0 * scale[1], 10.0 * scale[0],
              10.0 * scale[1], 10.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 9.0 * scale[0], -
              9.0 * scale[1], 20.0 * scale[0], -6.0 * scale[1])
    Curveto_r(25.0 * scale[0], 7.0 * scale[1], 25.0 * scale[0],
              11.0 * scale[1], -2.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 10.0 * scale[1], -17.0 * scale[0],
              18.0 * scale[1], -10.0 * scale[0], 19.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0], -
              5.0 * scale[1], 12.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 5.0 * scale[0], -
              8.0 * scale[1], 15.0 * scale[0], 1.0 * scale[1])
    Curveto_r(12.0 * scale[0], 10.0 * scale[1], 15.0 * scale[0],
              10.0 * scale[1], 15.0 * scale[0], 0.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 3.0 * scale[0], -
              10.0 * scale[1], 6.0 * scale[0], -7.0 * scale[1])
    Curveto_r(4.0 * scale[0], 4.0 * scale[1], 1.0 * scale[0],
              13.0 * scale[1], -6.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 8.0 * scale[1], -9.0 * scale[0],
              15.0 * scale[1], -4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 18.0 * scale[0],
              7.0 * scale[1], 28.0 * scale[0], 15.0 * scale[1])
    Curveto_r(16.0 * scale[0], 12.0 * scale[1], 17.0 * scale[0],
              17.0 * scale[1], 6.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 8.0 * scale[1], -25.0 * scale[0],
              15.0 * scale[1], -41.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-50.0 * scale[0], 0.0 * scale[1], -107.0 * scale[0],
              30.0 * scale[1], -138.0 * scale[0], 72.0 * scale[1])
    Lineto_r(-30.0 * scale[0], 41.0 * scale[1])
    Lineto_r(-8.0 * scale[0], -54.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -30.0 * scale[1], -6.0 * scale[0], -
              58.0 * scale[1], -4.0 * scale[0], -63.0 * scale[1])
    Curveto_r(1.0 * scale[0], -5.0 * scale[1], -4.0 * scale[0], -
              4.0 * scale[1], -12.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -17.0 * scale[0],
              9.0 * scale[1], -27.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -7.0 * scale[1], -7.0 *
              scale[0], -1.0 * scale[1], 3.0 * scale[0], 15.0 * scale[1])
    Curveto_r(18.0 * scale[0], 28.0 * scale[1], 22.0 * scale[0],
              84.0 * scale[1], 9.0 * scale[0], 105.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 7.0 * scale[1], -19.0 * scale[0],
              14.0 * scale[1], -32.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 3.0 * scale[1], -25.0 * scale[0], -
              3.0 * scale[1], -32.0 * scale[0], -31.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -19.0 * scale[1], -18.0 * scale[0], -
              45.0 * scale[1], -28.0 * scale[0], -58.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -22.0 * scale[1], -18.0 *
              scale[0], -22.0 * scale[1], -23.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 10.0 * scale[1], 1.0 * scale[0],
              24.0 * scale[1], 9.0 * scale[0], 30.0 * scale[1])
    Curveto_r(22.0 * scale[0], 19.0 * scale[1], 27.0 * scale[0],
              90.0 * scale[1], 10.0 * scale[0], 132.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 24.0 * scale[1], -13.0 * scale[0],
              45.0 * scale[1], -8.0 * scale[0], 60.0 * scale[1])
    Curveto_r(7.0 * scale[0], 17.0 * scale[1], 4.0 * scale[0],
              28.0 * scale[1], -10.0 * scale[0], 41.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 18.0 * scale[1], -19.0 * scale[0],
              15.0 * scale[1], -17.0 * scale[0], -143.0 * scale[1])
    te.end_fill()
    Moveto(87.0 * scale[0], 873.0 * scale[1], x, y)
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
    Moveto(105.0 * scale[0], 859.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -15.0 * scale[1], -2.0 *
              scale[0], -25.0 * scale[1], 9.0 * scale[0], -31.0 * scale[1])
    Curveto_r(9.0 * scale[0], -5.0 * scale[1], 14.0 * scale[0], -
              13.0 * scale[1], 11.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -15.0 * scale[1], 12.0 *
              scale[0], -10.0 * scale[1], 25.0 * scale[0], 6.0 * scale[1])
    Curveto_r(10.0 * scale[0], 12.0 * scale[1], 9.0 * scale[0],
              20.0 * scale[1], -4.0 * scale[0], 40.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 31.0 * scale[1], -33.0 * scale[0],
              32.0 * scale[1], -41.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(17.0 * scale[0], 859.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -5.0 * scale[1], -17.0 * scale[0], -
              17.0 * scale[1], -17.0 * scale[0], -24.0 * scale[1])
    Curveto_r(0.0 * scale[0], -23.0 * scale[1], 16.0 * scale[0], -
              17.0 * scale[1], 28.0 * scale[0], 10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 14.0 * scale[1], 11.0 * scale[0],
              25.0 * scale[1], 9.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              5.0 * scale[1], -20.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(55.0 * scale[0], 850.0 * scale[1], x, y)
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
    Moveto(365.0 * scale[0], 821.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              12.0 * scale[1], 3.0 * scale[0], -15.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 9.0 * scale[0],
              1.0 * scale[1], 9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], -3.0 * scale[0],
              19.0 * scale[1], -12.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(116.0 * scale[0], 775.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-26.0 * scale[0], -24.0 * scale[1])
    Lineto_r(58.0 * scale[0], -20.0 * scale[1])
    Curveto_r(31.0 * scale[0], -11.0 * scale[1], 69.0 * scale[0], -
              27.0 * scale[1], 85.0 * scale[0], -35.0 * scale[1])
    Curveto_r(15.0 * scale[0], -8.0 * scale[1], 27.0 * scale[0], -
              11.0 * scale[1], 27.0 * scale[0], -6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 11.0 * scale[0],
              12.0 * scale[1], 25.0 * scale[0], 16.0 * scale[1])
    Curveto_r(28.0 * scale[0], 7.0 * scale[1], 31.0 * scale[0],
              16.0 * scale[1], 12.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 8.0 * scale[1], -19.0 * scale[0],
              6.0 * scale[1], -35.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-27.0 * scale[0], -25.0 * scale[1], -42.0 *
              scale[0], -25.0 * scale[1], -42.0 * scale[0], -1.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], -17.0 * scale[0],
              29.0 * scale[1], -39.0 * scale[0], 44.0 * scale[1])
    Lineto_r(-39.0 * scale[0], 26.0 * scale[1])
    Lineto_r(-26.0 * scale[0], -24.0 * scale[1])
    te.end_fill()
    Moveto(433.0 * scale[0], 782.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -15.0 * scale[1], -22.0 *
              scale[0], -27.0 * scale[1], -23.0 * scale[0], -87.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -114.0 * scale[1], 6.0 * scale[0], -
              160.0 * scale[1], 23.0 * scale[0], -159.0 * scale[1])
    Curveto_r(8.0 * scale[0], 1.0 * scale[1], 14.0 * scale[0], -
              5.0 * scale[1], 12.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -9.0 * scale[1], -10.0 * scale[0], -
              15.0 * scale[1], -18.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 1.0 * scale[1], -14.0 *
              scale[0], -1.0 * scale[1], 1.0 * scale[0], -21.0 * scale[1])
    Curveto_r(28.0 * scale[0], -37.0 * scale[1], 33.0 * scale[0], -
              10.0 * scale[1], 30.0 * scale[0], 159.0 * scale[1])
    Lineto_r(-3.0 * scale[0], 155.0 * scale[1])
    Lineto_r(-22.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(372.0 * scale[0], 705.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -7.0 * scale[0], -
              25.0 * scale[1], -2.0 * scale[0], -25.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 25.0 * scale[0],
              39.0 * scale[1], 18.0 * scale[0], 46.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 2.0 * scale[1], -10.0 * scale[0], -
              7.0 * scale[1], -16.0 * scale[0], -21.0 * scale[1])
    te.end_fill()
    Moveto(931.0 * scale[0], 614.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(936.0 * scale[0], 563.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -9.0 * scale[1], -1.0 * scale[0], -
              20.0 * scale[1], 6.0 * scale[0], -25.0 * scale[1])
    Curveto_r(8.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              7.0 * scale[1], -12.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 3.0 * scale[1], -23.0 * scale[0],
              4.0 * scale[1], -20.0 * scale[0], 2.0 * scale[1])
    Curveto_r(8.0 * scale[0], -9.0 * scale[1], 55.0 * scale[0], -
              31.0 * scale[1], 48.0 * scale[0], -24.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -2.0 * scale[0],
              21.0 * scale[1], 2.0 * scale[0], 37.0 * scale[1])
    Curveto_r(6.0 * scale[0], 22.0 * scale[1], 5.0 * scale[0],
              29.0 * scale[1], -5.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0], -
              8.0 * scale[1], -19.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(888.0 * scale[0], 513.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(875.0 * scale[0], 490.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(945.0 * scale[0], 441.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              12.0 * scale[1], 5.0 * scale[0], -16.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 10.0 * scale[0],
              1.0 * scale[1], 10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 18.0 * scale[1], -6.0 * scale[0],
              21.0 * scale[1], -15.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(890.0 * scale[0], 408.0 * scale[1], x, y)
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
    Moveto(477.0 * scale[0], 381.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -17.0 * scale[1], -3.0 *
              scale[0], -21.0 * scale[1], 5.0 * scale[0], -13.0 * scale[1])
    Curveto_r(5.0 * scale[0], 5.0 * scale[1], 8.0 * scale[0],
              16.0 * scale[1], 6.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], -7.0 * scale[0],
              3.0 * scale[1], -11.0 * scale[0], -10.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#eddee3')
    te.end_fill()
    Moveto(94.0 * scale[0], 1287.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-23.0 * scale[0], -20.0 * scale[1], -25.0 *
              scale[0], -27.0 * scale[1], -16.0 * scale[0], -43.0 * scale[1])
    Curveto_r(11.0 * scale[0], -17.0 * scale[1], 12.0 *
              scale[0], -17.0 * scale[1], 9.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 19.0 * scale[1], 6.0 * scale[0],
              29.0 * scale[1], 33.0 * scale[0], 42.0 * scale[1])
    Curveto_r(19.0 * scale[0], 10.0 * scale[1], 27.0 * scale[0],
              18.0 * scale[1], 18.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -29.0 * scale[0], -
              10.0 * scale[1], -44.0 * scale[0], -23.0 * scale[1])
    te.end_fill()
    Moveto(163.0 * scale[0], 1260.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -30.0 * scale[1], 2.0 * scale[0], -
              43.0 * scale[1], 4.0 * scale[0], -27.0 * scale[1])
    Curveto_r(2.0 * scale[0], 15.0 * scale[1], 2.0 * scale[0],
              39.0 * scale[1], 0.0 * scale[0], 55.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 15.0 * scale[1], -4.0 * scale[0],
              2.0 * scale[1], -4.0 * scale[0], -28.0 * scale[1])
    te.end_fill()
    Moveto(451.0 * scale[0], 1301.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -5.0 * scale[1], -21.0 * scale[0], -
              26.0 * scale[1], -31.0 * scale[0], -48.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -35.0 * scale[1], -16.0 *
              scale[0], -43.0 * scale[1], -3.0 * scale[0], -66.0 * scale[1])
    Curveto_r(8.0 * scale[0], -15.0 * scale[1], 11.0 * scale[0], -
              31.0 * scale[1], 8.0 * scale[0], -36.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 9.0 *
              scale[0], -4.0 * scale[1], 25.0 * scale[0], 2.0 * scale[1])
    Curveto_r(24.0 * scale[0], 9.0 * scale[1], 33.0 * scale[0],
              9.0 * scale[1], 39.0 * scale[0], -1.0 * scale[1])
    Curveto_r(13.0 * scale[0], -22.0 * scale[1], 45.0 * scale[0],
              22.0 * scale[1], 32.0 * scale[0], 46.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 13.0 * scale[1], -7.0 * scale[0],
              22.0 * scale[1], 1.0 * scale[0], 30.0 * scale[1])
    Curveto_r(16.0 * scale[0], 16.0 * scale[1], -27.0 * scale[0],
              73.0 * scale[1], -49.0 * scale[0], 65.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -4.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -9.0 * scale[0], 5.0 * scale[1])
    Curveto_r(8.0 * scale[0], 14.0 * scale[1], 6.0 * scale[0],
              15.0 * scale[1], -13.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(819.0 * scale[0], 1283.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -19.0 * scale[1], -17.0 *
              scale[0], -22.0 * scale[1], -4.0 * scale[0], -11.0 * scale[1])
    Curveto_r(11.0 * scale[0], 9.0 * scale[1], 32.0 * scale[0],
              21.0 * scale[1], 45.0 * scale[0], 27.0 * scale[1])
    Curveto_r(22.0 * scale[0], 9.0 * scale[1], 23.0 * scale[0],
              10.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 1.0 * scale[1], -31.0 * scale[0], -
              11.0 * scale[1], -45.0 * scale[0], -26.0 * scale[1])
    te.end_fill()
    Moveto(893.0 * scale[0], 1245.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -38.0 * scale[1], 2.0 * scale[0], -
              53.0 * scale[1], 4.0 * scale[0], -32.0 * scale[1])
    Curveto_r(2.0 * scale[0], 20.0 * scale[1], 2.0 * scale[0],
              52.0 * scale[1], 0.0 * scale[0], 70.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 17.0 * scale[1], -4.0 * scale[0],
              1.0 * scale[1], -4.0 * scale[0], -38.0 * scale[1])
    te.end_fill()
    Moveto(371.0 * scale[0], 1234.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(817.0 * scale[0], 1239.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(102.0 * scale[0], 1210.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 2.0 * scale[0], -
              27.0 * scale[1], 5.0 * scale[0], -17.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              25.0 * scale[1], 0.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(128.0 * scale[0], 1123.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(858.0 * scale[0], 1123.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(474.0 * scale[0], 700.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -184.0 * scale[1], 2.0 * scale[0], -
              260.0 * scale[1], 3.0 * scale[0], -167.0 * scale[1])
    Curveto_r(2.0 * scale[0], 92.0 * scale[1], 2.0 * scale[0],
              242.0 * scale[1], 0.0 * scale[0], 335.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 92.0 * scale[1], -3.0 * scale[0],
              16.0 * scale[1], -3.0 * scale[0], -168.0 * scale[1])
    te.end_fill()
    Moveto(42.0 * scale[0], 978.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-22.0 * scale[0], -28.0 * scale[1], -18.0 *
              scale[0], -84.0 * scale[1], 7.0 * scale[0], -91.0 * scale[1])
    Curveto_r(49.0 * scale[0], -13.0 * scale[1], 68.0 * scale[0],
              43.0 * scale[1], 28.0 * scale[0], 82.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 17.0 * scale[1], -26.0 * scale[0],
              19.0 * scale[1], -35.0 * scale[0], 9.0 * scale[1])
    te.end_fill()
    Moveto(36.0 * scale[0], 819.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -44.0 * scale[1], -5.0 *
              scale[0], -71.0 * scale[1], 32.0 * scale[0], -67.0 * scale[1])
    Curveto_r(38.0 * scale[0], 4.0 * scale[1], 42.0 * scale[0],
              45.0 * scale[1], 8.0 * scale[0], 77.0 * scale[1])
    Lineto_r(-26.0 * scale[0], 24.0 * scale[1])
    Lineto_r(-14.0 * scale[0], -34.0 * scale[1])
    te.end_fill()
    Moveto(720.0 * scale[0], 780.0 * scale[1], x, y)
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
    Moveto(877.0 * scale[0], 649.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-23.0 * scale[0], -13.0 * scale[1], -21.0 *
              scale[0], -44.0 * scale[1], 5.0 * scale[0], -79.0 * scale[1])
    Curveto_r(20.0 * scale[0], -27.0 * scale[1], 22.0 * scale[0], -
              28.0 * scale[1], 34.0 * scale[0], -12.0 * scale[1])
    Curveto_r(34.0 * scale[0], 44.0 * scale[1], 4.0 * scale[0],
              114.0 * scale[1], -39.0 * scale[0], 91.0 * scale[1])
    te.end_fill()
    Moveto(867.0 * scale[0], 503.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-14.0 * scale[0], -13.0 * scale[1], -6.0 *
              scale[0], -45.0 * scale[1], 17.0 * scale[0], -70.0 * scale[1])
    Lineto_r(24.0 * scale[0], -26.0 * scale[1])
    Lineto_r(16.0 * scale[0], 32.0 * scale[1])
    Curveto_r(13.0 * scale[0], 24.0 * scale[1], 14.0 * scale[0],
              36.0 * scale[1], 6.0 * scale[0], 51.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 19.0 * scale[1], -49.0 * scale[0],
              27.0 * scale[1], -63.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto_r(33.0 * scale[0], -7.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], -7.0 * scale[0], -
              7.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -2.0 * scale[1], -9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(6.0 * scale[0], 10.0 * scale[1], 25.0 * scale[0],
              14.0 * scale[1], 25.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(10.0 * scale[0], 465.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              15.0 * scale[1], 10.0 * scale[0], -15.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              7.0 * scale[1], 4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              15.0 * scale[1], -10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              7.0 * scale[1], -4.0 * scale[0], -15.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#1e1706')
    te.end_fill()
    Moveto(3.0 * scale[0], 1385.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -9.0 * scale[1], -3.0 * scale[0], -
              19.0 * scale[1], 1.0 * scale[0], -22.0 * scale[1])
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], 6.0 * scale[0],
              1.0 * scale[1], 6.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], 11.0 * scale[0],
              17.0 * scale[1], 28.0 * scale[0], 20.0 * scale[1])
    Lineto_r(27.0 * scale[0], 4.0 * scale[1])
    Lineto_r(-28.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 0.0 * scale[1], -30.0 * scale[0], -
              5.0 * scale[1], -34.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(894.0 * scale[0], 1389.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(22.0 * scale[0], -5.0 * scale[1], 45.0 * scale[0], -
              14.0 * scale[1], 51.0 * scale[0], -19.0 * scale[1])
    Curveto_r(7.0 * scale[0], -5.0 * scale[1], 13.0 * scale[0], -
              40.0 * scale[1], 14.0 * scale[0], -77.0 * scale[1])
    Curveto_r(3.0 * scale[0], -95.0 * scale[1], 11.0 *
              scale[0], -92.0 * scale[1], 11.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 49.0 * scale[1], -5.0 * scale[0],
              85.0 * scale[1], -12.0 * scale[0], 92.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 7.0 * scale[1], -32.0 * scale[0],
              12.0 * scale[1], -57.0 * scale[0], 11.0 * scale[1])
    Lineto_r(-46.0 * scale[0], -1.0 * scale[1])
    Lineto_r(39.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(962.0 * scale[0], 1148.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -37.0 * scale[1], -7.0 * scale[0], -
              79.0 * scale[1], -12.0 * scale[0], -94.0 * scale[1])
    Lineto_r(-11.0 * scale[0], -27.0 * scale[1])
    Lineto_r(-224.0 * scale[0], 6.0 * scale[1])
    Lineto_r(-225.0 * scale[0], 6.0 * scale[1])
    Lineto_r(1.0 * scale[0], -52.0 * scale[1])
    Curveto_r(1.0 * scale[0], -40.0 * scale[1], 3.0 * scale[0], -
              45.0 * scale[1], 8.0 * scale[0], -23.0 * scale[1])
    Curveto_r(8.0 * scale[0], 38.0 * scale[1], 31.0 * scale[0],
              47.0 * scale[1], 31.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], -30.0 * scale[1], 30.0 * scale[0], -
              96.0 * scale[1], 43.0 * scale[0], -96.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              10.0 * scale[1], 3.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 12.0 * scale[1], -6.0 * scale[0],
              25.0 * scale[1], -6.0 * scale[0], 30.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], -7.0 * scale[0],
              7.0 * scale[1], -15.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0],
              7.0 * scale[1], -15.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 5.0 * scale[0],
              15.0 * scale[1], 10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              5.0 * scale[1], 10.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 4.0 * scale[0], -
              8.0 * scale[1], 9.0 * scale[0], -5.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 7.0 * scale[0],
              16.0 * scale[1], 4.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 16.0 * scale[1], -2.0 * scale[0],
              18.0 * scale[1], 5.0 * scale[0], 8.0 * scale[1])
    Curveto_r(8.0 * scale[0], -11.0 * scale[1], 11.0 *
              scale[0], -9.0 * scale[1], 17.0 * scale[0], 8.0 * scale[1])
    Curveto_r(5.0 * scale[0], 17.0 * scale[1], 12.0 * scale[0],
              20.0 * scale[1], 28.0 * scale[0], 15.0 * scale[1])
    Curveto_r(12.0 * scale[0], -4.0 * scale[1], 28.0 * scale[0], -
              15.0 * scale[1], 35.0 * scale[0], -25.0 * scale[1])
    Curveto_r(15.0 * scale[0], -21.0 * scale[1], 42.0 *
              scale[0], -26.0 * scale[1], 42.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 3.0 * scale[0],
              9.0 * scale[1], 6.0 * scale[0], 5.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 0.0 * scale[0], -
              21.0 * scale[1], -7.0 * scale[0], -40.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -28.0 * scale[1], -9.0 *
              scale[0], -46.0 * scale[1], 1.0 * scale[0], -96.0 * scale[1])
    Lineto_r(14.0 * scale[0], -61.0 * scale[1])
    Lineto_r(13.0 * scale[0], 53.0 * scale[1])
    Curveto_r(14.0 * scale[0], 52.0 * scale[1], 45.0 * scale[0],
              89.0 * scale[1], 69.0 * scale[0], 80.0 * scale[1])
    Curveto_r(7.0 * scale[0], -2.0 * scale[1], 15.0 * scale[0],
              0.0 * scale[1], 19.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 18.0 * scale[1], 28.0 * scale[0],
              12.0 * scale[1], 20.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -10.0 * scale[1], -9.0 * scale[0], -
              24.0 * scale[1], -12.0 * scale[0], -32.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -11.0 * scale[1], -2.0 *
              scale[0], -11.0 * scale[1], 16.0 * scale[0], -1.0 * scale[1])
    Curveto_r(21.0 * scale[0], 11.0 * scale[1], 22.0 * scale[0],
              10.0 * scale[1], 16.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -22.0 * scale[1], -7.0 *
              scale[0], -22.0 * scale[1], 20.0 * scale[0], 5.0 * scale[1])
    Curveto_r(45.0 * scale[0], 44.0 * scale[1], 56.0 * scale[0],
              37.0 * scale[1], 52.0 * scale[0], -35.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -35.0 * scale[1], -3.0 *
              scale[0], -50.0 * scale[1], 0.0 * scale[0], -35.0 * scale[1])
    Curveto_r(3.0 * scale[0], 20.0 * scale[1], 9.0 * scale[0],
              27.0 * scale[1], 19.0 * scale[0], 23.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 17.0 * scale[0],
              0.0 * scale[1], 20.0 * scale[0], 7.0 * scale[1])
    Curveto_r(2.0 * scale[0], 7.0 * scale[1], 3.0 * scale[0],
              94.0 * scale[1], 1.0 * scale[0], 192.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 99.0 * scale[1], -4.0 * scale[0],
              150.0 * scale[1], -5.0 * scale[0], 113.0 * scale[1])
    te.end_fill()
    Moveto_r(-22.0 * scale[0], -138.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -6.0 * scale[0], -
              10.0 * scale[1], -12.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 0.0 * scale[1], -10.0 *
              scale[0], -2.0 * scale[1], 0.0 * scale[0], -6.0 * scale[1])
    Curveto_r(14.0 * scale[0], -5.0 * scale[1], 17.0 * scale[0], -
              33.0 * scale[1], 3.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 7.0 * scale[1], -12.0 * scale[0],
              13.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0],
              5.0 * scale[1], -14.0 * scale[0], 10.0 * scale[1])
    Curveto_r(1.0 * scale[0], 6.0 * scale[1], 8.0 * scale[0],
              9.0 * scale[1], 15.0 * scale[0], 9.0 * scale[1])
    Curveto_r(6.0 * scale[0], -1.0 * scale[1], 12.0 * scale[0],
              2.0 * scale[1], 12.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 7.0 * scale[0],
              9.0 * scale[1], 15.0 * scale[0], 9.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0], -
              4.0 * scale[1], 15.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(672.0 * scale[0], 890.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(620.0 * scale[0], 866.0 * scale[1], x, y)
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
    Moveto(813.0 * scale[0], 830.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -25.0 * scale[1], 2.0 * scale[0], -
              35.0 * scale[1], 4.0 * scale[0], -22.0 * scale[1])
    Curveto_r(2.0 * scale[0], 12.0 * scale[1], 2.0 * scale[0],
              32.0 * scale[1], 0.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 12.0 * scale[1], -4.0 * scale[0],
              2.0 * scale[1], -4.0 * scale[0], -23.0 * scale[1])
    te.end_fill()
    Moveto(676.0 * scale[0], 823.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -53.0 * scale[1], 3.0 * scale[0], -
              53.0 * scale[1], 15.0 * scale[0], -53.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              13.0 * scale[1], 4.0 * scale[0], 38.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 51.0 * scale[1], -22.0 * scale[0],
              61.0 * scale[1], -19.0 * scale[0], 15.0 * scale[1])
    te.end_fill()
    Moveto(543.0 * scale[0], 825.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -9.0 * scale[1], -3.0 * scale[0], -
              18.0 * scale[1], -1.0 * scale[0], -21.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 8.0 * scale[0],
              4.0 * scale[1], 11.0 * scale[0], 16.0 * scale[1])
    Curveto_r(6.0 * scale[0], 23.0 * scale[1], -1.0 * scale[0],
              27.0 * scale[1], -10.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(391.0 * scale[0], 794.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(280.0 * scale[0], 784.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 9.0 * scale[0], -
              23.0 * scale[1], 21.0 * scale[0], -38.0 * scale[1])
    Curveto_r(11.0 * scale[0], -15.0 * scale[1], 22.0 * scale[0], -
              34.0 * scale[1], 23.0 * scale[0], -43.0 * scale[1])
    Curveto_r(2.0 * scale[0], -9.0 * scale[1], 8.0 * scale[0], -
              19.0 * scale[1], 14.0 * scale[0], -21.0 * scale[1])
    Curveto_r(16.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0],
              26.0 * scale[1], -18.0 * scale[0], 53.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 11.0 * scale[1], -22.0 * scale[0],
              29.0 * scale[1], -28.0 * scale[0], 40.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 11.0 * scale[1], -12.0 * scale[0],
              15.0 * scale[1], -12.0 * scale[0], 9.0 * scale[1])
    te.end_fill()
    Moveto(820.0 * scale[0], 768.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 10.0 * scale[0], -
              36.0 * scale[1], 22.0 * scale[0], -59.0 * scale[1])
    Curveto_r(21.0 * scale[0], -41.0 * scale[1], 21.0 *
              scale[0], -42.0 * scale[1], 3.0 * scale[0], -75.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -24.0 * scale[1], -22.0 *
              scale[0], -31.0 * scale[1], -30.0 * scale[0], -24.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 5.0 * scale[1], -20.0 * scale[0],
              7.0 * scale[1], -31.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -3.0 * scale[1], -30.0 * scale[0],
              6.0 * scale[1], -53.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 20.0 * scale[1], -30.0 * scale[0],
              36.0 * scale[1], -24.0 * scale[0], 36.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0],
              11.0 * scale[1], 5.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 19.0 * scale[1], -1.0 * scale[0],
              25.0 * scale[1], 7.0 * scale[0], 20.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 11.0 *
              scale[0], -3.0 * scale[1], 11.0 * scale[0], 2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 20.0 * scale[1], -13.0 * scale[0],
              19.0 * scale[1], -35.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -20.0 * scale[1], -21.0 *
              scale[0], -25.0 * scale[1], -9.0 * scale[0], -47.0 * scale[1])
    Curveto_r(33.0 * scale[0], -61.0 * scale[1], 73.0 * scale[0], -
              90.0 * scale[1], 141.0 * scale[0], -100.0 * scale[1])
    Curveto_r(39.0 * scale[0], -6.0 * scale[1], 41.0 *
              scale[0], -5.0 * scale[1], 32.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 27.0 * scale[1], -2.0 * scale[0],
              57.0 * scale[1], 27.0 * scale[0], 64.0 * scale[1])
    Curveto_r(31.0 * scale[0], 8.0 * scale[1], 54.0 * scale[0], -
              11.0 * scale[1], 54.0 * scale[0], -43.0 * scale[1])
    Curveto_r(0.0 * scale[0], -15.0 * scale[1], 5.0 * scale[0], -
              23.0 * scale[1], 13.0 * scale[0], -21.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 13.0 * scale[0],
              30.0 * scale[1], 15.0 * scale[0], 79.0 * scale[1])
    Curveto_r(2.0 * scale[0], 65.0 * scale[1], 0.0 * scale[0],
              75.0 * scale[1], -18.0 * scale[0], 86.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 13.0 * scale[1], -19.0 * scale[0],
              12.0 * scale[1], -3.0 * scale[0], -21.0 * scale[1])
    Curveto_r(22.0 * scale[0], -48.0 * scale[1], 13.0 * scale[0], -
              67.0 * scale[1], -29.0 * scale[0], -60.0 * scale[1])
    Curveto_r(-40.0 * scale[0], 8.0 * scale[1], -52.0 * scale[0],
              18.0 * scale[1], -77.0 * scale[0], 69.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 22.0 * scale[1], -20.0 * scale[0],
              32.0 * scale[1], -21.0 * scale[0], 23.0 * scale[1])
    te.end_fill()
    Moveto(397.0 * scale[0], 728.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -23.0 * scale[1], -12.0 * scale[0], -
              47.0 * scale[1], -20.0 * scale[0], -53.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -8.0 * scale[1], -11.0 *
              scale[0], -15.0 * scale[1], 4.0 * scale[0], -40.0 * scale[1])
    Curveto_r(11.0 * scale[0], -17.0 * scale[1], 16.0 * scale[0], -
              39.0 * scale[1], 13.0 * scale[0], -52.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -13.0 * scale[1], -2.0 *
              scale[0], -23.0 * scale[1], 3.0 * scale[0], -23.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              47.0 * scale[1], 9.0 * scale[0], 105.0 * scale[1])
    Curveto_r(1.0 * scale[0], 58.0 * scale[1], 0.0 * scale[0],
              105.0 * scale[1], -1.0 * scale[0], 105.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 0.0 * scale[1], -5.0 * scale[0], -
              19.0 * scale[1], -8.0 * scale[0], -42.0 * scale[1])
    te.end_fill()
    Moveto(24.0 * scale[0], 742.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 33.0 * scale[0], -
              15.0 * scale[1], 67.0 * scale[0], -22.0 * scale[1])
    Curveto_r(33.0 * scale[0], -7.0 * scale[1], 67.0 * scale[0], -
              19.0 * scale[1], 75.0 * scale[0], -27.0 * scale[1])
    Curveto_r(8.0 * scale[0], -8.0 * scale[1], 18.0 * scale[0], -
              12.0 * scale[1], 24.0 * scale[0], -8.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 18.0 * scale[0], -
              3.0 * scale[1], 29.0 * scale[0], -14.0 * scale[1])
    Curveto_r(11.0 * scale[0], -11.0 * scale[1], 22.0 * scale[0], -
              17.0 * scale[1], 24.0 * scale[0], -15.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 4.0 * scale[0], -
              3.0 * scale[1], 3.0 * scale[0], -13.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 5.0 * scale[0], -
              17.0 * scale[1], 13.0 * scale[0], -15.0 * scale[1])
    Curveto_r(8.0 * scale[0], 2.0 * scale[1], 11.0 * scale[0], -
              3.0 * scale[1], 8.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -11.0 * scale[1], 1.0 * scale[0], -
              18.0 * scale[1], 18.0 * scale[0], -22.0 * scale[1])
    Curveto_r(29.0 * scale[0], -7.0 * scale[1], 30.0 * scale[0], -
              10.0 * scale[1], 10.0 * scale[0], -30.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -19.0 * scale[1], -20.0 *
              scale[0], -45.0 * scale[1], -2.0 * scale[0], -38.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 18.0 * scale[0], -
              6.0 * scale[1], 25.0 * scale[0], -21.0 * scale[1])
    Curveto_r(7.0 * scale[0], -15.0 * scale[1], 8.0 * scale[0], -
              25.0 * scale[1], 2.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              7.0 * scale[1], -10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], -8.0 * scale[0], -
              14.0 * scale[1], -27.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 3.0 * scale[1], -28.0 * scale[0],
              7.0 * scale[1], -28.0 * scale[0], 38.0 * scale[1])
    Curveto_r(0.0 * scale[0], 27.0 * scale[1], -4.0 * scale[0],
              34.0 * scale[1], -17.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -1.0 * scale[1], -19.0 * scale[0],
              6.0 * scale[1], -23.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 28.0 * scale[1], -53.0 * scale[0],
              68.0 * scale[1], -93.0 * scale[0], 85.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 8.0 * scale[1], -35.0 * scale[0],
              21.0 * scale[1], -38.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], -14.0 * scale[0],
              15.0 * scale[1], -23.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -23.0 * scale[0],
              6.0 * scale[1], -30.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 10.0 * scale[1], -13.0 * scale[0],
              10.0 * scale[1], -7.0 * scale[0], 0.0 * scale[1])
    Curveto_r(4.0 * scale[0], -8.0 * scale[1], 1.0 * scale[0], -
              13.0 * scale[1], -8.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-33.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0], -
              17.0 * scale[1], 33.0 * scale[0], -29.0 * scale[1])
    Curveto_r(47.0 * scale[0], -12.0 * scale[1], 90.0 * scale[0], -
              41.0 * scale[1], 61.0 * scale[0], -41.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 0.0 * scale[1], 41.0 * scale[0], -
              56.0 * scale[1], 67.0 * scale[0], -64.0 * scale[1])
    Curveto_r(24.0 * scale[0], -8.0 * scale[1], 33.0 * scale[0], -
              33.0 * scale[1], 33.0 * scale[0], -96.0 * scale[1])
    Curveto_r(0.0 * scale[0], -39.0 * scale[1], -4.0 * scale[0], -
              48.0 * scale[1], -27.0 * scale[0], -62.0 * scale[1])
    Lineto_r(-28.0 * scale[0], -17.0 * scale[1])
    Lineto_r(66.0 * scale[0], -1.0 * scale[1])
    Curveto_r(36.0 * scale[0], 0.0 * scale[1], 107.0 * scale[0], -
              3.0 * scale[1], 157.0 * scale[0], -6.0 * scale[1])
    Lineto_r(92.0 * scale[0], -7.0 * scale[1])
    Lineto_r(0.0 * scale[0], 32.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], -4.0 * scale[0],
              31.0 * scale[1], -10.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0],
              6.0 * scale[1], -10.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -4.0 * scale[0],
              18.0 * scale[1], -10.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -7.0 * scale[0],
              0.0 * scale[1], -4.0 * scale[0], -9.0 * scale[1])
    Curveto_r(7.0 * scale[0], -17.0 * scale[1], -24.0 * scale[0], -
              68.0 * scale[1], -39.0 * scale[0], -63.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 1.0 * scale[1], -10.0 * scale[0],
              35.0 * scale[1], -11.0 * scale[0], 74.0 * scale[1])
    Curveto_r(0.0 * scale[0], 39.0 * scale[1], -4.0 * scale[0],
              69.0 * scale[1], -8.0 * scale[0], 66.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -2.0 * scale[1], -8.0 * scale[0],
              2.0 * scale[1], -8.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], -67.0 * scale[0],
              105.0 * scale[1], -95.0 * scale[0], 131.0 * scale[1])
    Curveto_r(-33.0 * scale[0], 30.0 * scale[1], -124.0 * scale[0],
              72.0 * scale[1], -173.0 * scale[0], 80.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 3.0 * scale[1], -48.0 * scale[0],
              8.0 * scale[1], -60.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 3.0 * scale[1], -21.0 * scale[0],
              1.0 * scale[1], -18.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(550.0 * scale[0], 681.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -22.0 * scale[1], -15.0 * scale[0], -
              43.0 * scale[1], -20.0 * scale[0], -46.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -3.0 * scale[1], -10.0 * scale[0], -
              11.0 * scale[1], -10.0 * scale[0], -17.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], 5.0 * scale[0], -
              6.0 * scale[1], 15.0 * scale[0], 2.0 * scale[1])
    Curveto_r(16.0 * scale[0], 13.0 * scale[1], 40.0 * scale[0],
              88.0 * scale[1], 31.0 * scale[0], 97.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0], -
              13.0 * scale[1], -16.0 * scale[0], -36.0 * scale[1])
    te.end_fill()
    Moveto(641.0 * scale[0], 695.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -16.0 * scale[1], 8.0 * scale[0], -
              50.0 * scale[1], 5.0 * scale[0], -75.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -31.0 * scale[1], -3.0 *
              scale[0], -39.0 * scale[1], 3.0 * scale[0], -25.0 * scale[1])
    Curveto_r(15.0 * scale[0], 31.0 * scale[1], 12.0 * scale[0],
              89.0 * scale[1], -4.0 * scale[0], 111.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 18.0 * scale[1], -14.0 * scale[0],
              17.0 * scale[1], -4.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(52.0 * scale[0], 531.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -6.0 * scale[1], -10.0 *
              scale[0], -10.0 * scale[1], 2.0 * scale[0], -20.0 * scale[1])
    Curveto_r(12.0 * scale[0], -10.0 * scale[1], 15.0 *
              scale[0], -9.0 * scale[1], 13.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 12.0 * scale[1], -1.0 * scale[0],
              21.0 * scale[1], -2.0 * scale[0], 21.0 * scale[1])
    Curveto_r(0.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0], -
              4.0 * scale[1], -13.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(410.0 * scale[0], 520.0 * scale[1], x, y)
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
    Moveto(81.0 * scale[0], 450.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -71.0 * scale[1], 1.0 * scale[0], -
              74.0 * scale[1], -16.0 * scale[0], -60.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -15.0 * scale[0],
              9.0 * scale[1], -15.0 * scale[0], 1.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              11.0 * scale[1], -22.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 1.0 * scale[1], -23.0 * scale[0],
              1.0 * scale[1], -4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(11.0 * scale[0], 8.0 * scale[1], 14.0 * scale[0],
              15.0 * scale[1], 8.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0],
              8.0 * scale[1], -13.0 * scale[0], 18.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -2.0 * scale[0],
              14.0 * scale[1], -9.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -11.0 * scale[1], -9.0 * scale[0], -
              31.0 * scale[1], -9.0 * scale[0], -45.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -24.0 * scale[1], 1.0 * scale[0], -
              25.0 * scale[1], 54.0 * scale[0], -22.0 * scale[1])
    Curveto_r(48.0 * scale[0], 3.0 * scale[1], 55.0 * scale[0],
              7.0 * scale[1], 57.0 * scale[0], 25.0 * scale[1])
    Curveto_r(2.0 * scale[0], 41.0 * scale[1], -3.0 * scale[0],
              70.0 * scale[1], -18.0 * scale[0], 91.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 20.0 * scale[1], -15.0 * scale[0],
              18.0 * scale[1], -13.0 * scale[0], -24.0 * scale[1])
    te.end_fill()
    Moveto(35.0 * scale[0], 460.0 * scale[1], x, y)
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
    Moveto(40.0 * scale[0], 430.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], 18.0 * scale[0], -
              22.0 * scale[1], 24.0 * scale[0], -11.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], -1.0 * scale[0],
              11.0 * scale[1], -9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -15.0 * scale[0],
              1.0 * scale[1], -15.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(947.0 * scale[0], 361.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -6.0 * scale[1], -17.0 *
              scale[0], -9.0 * scale[1], -5.0 * scale[0], -19.0 * scale[1])
    Curveto_r(11.0 * scale[0], -9.0 * scale[1], 15.0 * scale[0], -
              45.0 * scale[1], 15.0 * scale[0], -159.0 * scale[1])
    Curveto_r(1.0 * scale[0], -81.0 * scale[1], -3.0 * scale[0], -
              155.0 * scale[1], -8.0 * scale[0], -165.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -12.0 * scale[1], -6.0 *
              scale[0], -18.0 * scale[1], 1.0 * scale[0], -18.0 * scale[1])
    Curveto_r(19.0 * scale[0], 0.0 * scale[1], 21.0 * scale[0],
              22.0 * scale[1], 18.0 * scale[0], 196.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 161.0 * scale[1], -4.0 * scale[0],
              171.0 * scale[1], -21.0 * scale[0], 165.0 * scale[1])
    te.end_fill()
    Moveto(523.0 * scale[0], 353.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(20.0 * scale[0], -2.0 * scale[1], 54.0 *
              scale[0], -2.0 * scale[1], 75.0 * scale[0], 0.0 * scale[1])
    Curveto_r(20.0 * scale[0], 2.0 * scale[1], 3.0 * scale[0],
              4.0 * scale[1], -38.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-41.0 * scale[0], 0.0 * scale[1], -58.0 *
              scale[0], -2.0 * scale[1], -37.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(828.0 * scale[0], 353.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(0.0 * scale[0], 16.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 8.0 * scale[0], -
              16.0 * scale[1], 28.0 * scale[0], -15.0 * scale[1])
    Curveto_r(15.0 * scale[0], 0.0 * scale[1], 21.0 * scale[0],
              3.0 * scale[1], 12.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -21.0 * scale[0],
              10.0 * scale[1], -27.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 7.0 * scale[1], -13.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], -7.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#8c6b9d')
    te.end_fill()
    Moveto(492.0 * scale[0], 1306.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(10.0 * scale[0], -7.0 * scale[1], 14.0 * scale[0], -
              17.0 * scale[1], 10.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -5.0 * scale[1], -2.0 *
              scale[0], -5.0 * scale[1], 5.0 * scale[0], -1.0 * scale[1])
    Curveto_r(13.0 * scale[0], 7.0 * scale[1], 30.0 * scale[0], -
              55.0 * scale[1], 19.0 * scale[0], -73.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              12.0 * scale[1], 4.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 5.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], 4.0 * scale[0], -
              6.0 * scale[1], 16.0 * scale[0], -3.0 * scale[1])
    Curveto_r(17.0 * scale[0], 5.0 * scale[1], 18.0 * scale[0],
              8.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 6.0 * scale[1], -14.0 * scale[0],
              23.0 * scale[1], -13.0 * scale[0], 55.0 * scale[1])
    Curveto_r(1.0 * scale[0], 38.0 * scale[1], -2.0 * scale[0],
              48.0 * scale[1], -17.0 * scale[0], 52.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 2.0 * scale[1], -18.0 * scale[0],
              8.0 * scale[1], -18.0 * scale[0], 13.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -8.0 * scale[0],
              9.0 * scale[1], -17.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -1.0 * scale[1], -17.0 *
              scale[0], -1.0 * scale[1], -1.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(152.0 * scale[0], 1270.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(399.0 * scale[0], 1273.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              11.0 * scale[1], 0.0 * scale[0], -15.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -3.0 * scale[0], -
              8.0 * scale[1], -9.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              12.0 * scale[1], -10.0 * scale[0], -26.0 * scale[1])
    Curveto_r(0.0 * scale[0], -23.0 * scale[1], 2.0 * scale[0], -
              25.0 * scale[1], 15.0 * scale[0], -14.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 13.0 * scale[0],
              15.0 * scale[1], 10.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], 0.0 * scale[0],
              11.0 * scale[1], 6.0 * scale[0], 19.0 * scale[1])
    Curveto_r(9.0 * scale[0], 10.0 * scale[1], 8.0 * scale[0],
              13.0 * scale[1], -2.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -5.0 * scale[0],
              4.0 * scale[1], 6.0 * scale[0], 9.0 * scale[1])
    Curveto_r(17.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              9.0 * scale[1], 3.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 1.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -19.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(820.0 * scale[0], 1266.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(121.0 * scale[0], 1210.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -26.0 * scale[1], 11.0 * scale[0], -
              60.0 * scale[1], 20.0 * scale[0], -54.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 9.0 * scale[0],
              15.0 * scale[1], 9.0 * scale[0], 27.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], -2.0 * scale[0],
              19.0 * scale[1], -9.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -11.0 * scale[1], -10.0 *
              scale[0], -9.0 * scale[1], -14.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 13.0 * scale[1], -5.0 * scale[0],
              17.0 * scale[1], -6.0 * scale[0], 9.0 * scale[1])
    te.end_fill()
    Moveto(851.0 * scale[0], 1198.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -33.0 * scale[1], 8.0 * scale[0], -
              60.0 * scale[1], 20.0 * scale[0], -52.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 9.0 * scale[0],
              20.0 * scale[1], 8.0 * scale[0], 37.0 * scale[1])
    Curveto_r(0.0 * scale[0], 26.0 * scale[1], -2.0 * scale[0],
              28.0 * scale[1], -8.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -19.0 * scale[1], -9.0 *
              scale[0], -18.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Lineto_r(-5.0 * scale[0], 25.0 * scale[1])
    Lineto_r(-2.0 * scale[0], -27.0 * scale[1])
    te.end_fill()
    Moveto(23.0 * scale[0], 1022.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-24.0 * scale[0], -4.0 * scale[1], -29.0 * scale[0], -
              18.0 * scale[1], -14.0 * scale[0], -41.0 * scale[1])
    Curveto_r(7.0 * scale[0], -10.0 * scale[1], 12.0 *
              scale[0], -8.0 * scale[1], 24.0 * scale[0], 9.0 * scale[1])
    Curveto_r(9.0 * scale[0], 13.0 * scale[1], 17.0 * scale[0],
              17.0 * scale[1], 22.0 * scale[0], 11.0 * scale[1])
    Curveto_r(3.0 * scale[0], -6.0 * scale[1], 10.0 * scale[0], -
              9.0 * scale[1], 15.0 * scale[0], -6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 7.0 * scale[1], 42.0 * scale[0], -
              43.0 * scale[1], 35.0 * scale[0], -55.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], -1.0 * scale[0], -
              10.0 * scale[1], 5.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              8.0 * scale[1], 8.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -10.0 * scale[1], -8.0 * scale[0], -
              18.0 * scale[1], -14.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 0.0 * scale[1], -45.0 * scale[0], -
              33.0 * scale[1], -34.0 * scale[0], -40.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 5.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 3.0 * scale[0], -
              15.0 * scale[1], 13.0 * scale[0], -22.0 * scale[1])
    Curveto_r(12.0 * scale[0], -8.0 * scale[1], 18.0 * scale[0], -
              22.0 * scale[1], 15.0 * scale[0], -38.0 * scale[1])
    Lineto_r(-4.0 * scale[0], -24.0 * scale[1])
    Lineto_r(21.0 * scale[0], 22.0 * scale[1])
    Lineto_r(21.0 * scale[0], 22.0 * scale[1])
    Lineto_r(39.0 * scale[0], -26.0 * scale[1])
    Curveto_r(40.0 * scale[0], -26.0 * scale[1], 52.0 * scale[0], -
              57.0 * scale[1], 28.0 * scale[0], -68.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -3.0 * scale[1], -2.0 *
              scale[0], -3.0 * scale[1], 12.0 * scale[0], 0.0 * scale[1])
    Curveto_r(13.0 * scale[0], 4.0 * scale[1], 30.0 * scale[0],
              13.0 * scale[1], 38.0 * scale[0], 21.0 * scale[1])
    Curveto_r(10.0 * scale[0], 9.0 * scale[1], 18.0 * scale[0],
              11.0 * scale[1], 26.0 * scale[0], 3.0 * scale[1])
    Curveto_r(7.0 * scale[0], -5.0 * scale[1], 16.0 * scale[0], -
              7.0 * scale[1], 20.0 * scale[0], -3.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], -10.0 * scale[0],
              24.0 * scale[1], -31.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 26.0 * scale[1], -40.0 * scale[0],
              35.0 * scale[1], -48.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -6.0 * scale[1], -27.0 *
              scale[0], -7.0 * scale[1], -45.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-29.0 * scale[0], 5.0 * scale[1], -31.0 * scale[0],
              8.0 * scale[1], -16.0 * scale[0], 18.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 16.0 * scale[0],
              20.0 * scale[1], 16.0 * scale[0], 29.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], 4.0 * scale[0],
              16.0 * scale[1], 9.0 * scale[0], 16.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0],
              13.0 * scale[1], 21.0 * scale[0], 29.0 * scale[1])
    Curveto_r(26.0 * scale[0], 63.0 * scale[1], 124.0 * scale[0],
              77.0 * scale[1], 183.0 * scale[0], 26.0 * scale[1])
    Curveto_r(30.0 * scale[0], -26.0 * scale[1], 35.0 * scale[0], -
              40.0 * scale[1], 12.0 * scale[0], -31.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -15.0 * scale[0],
              2.0 * scale[1], -15.0 * scale[0], -2.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], -14.0 * scale[0], -
              16.0 * scale[1], -30.0 * scale[0], -27.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -12.0 * scale[1], -28.0 *
              scale[0], -26.0 * scale[1], -25.0 * scale[0], -34.0 * scale[1])
    Curveto_r(5.0 * scale[0], -12.0 * scale[1], 3.0 * scale[0], -
              12.0 * scale[1], -12.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 13.0 * scale[1], -16.0 * scale[0],
              12.0 * scale[1], -11.0 * scale[0], -8.0 * scale[1])
    Curveto_r(4.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              20.0 * scale[1], -8.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -11.0 * scale[0],
              9.0 * scale[1], -8.0 * scale[0], 14.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -10.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -4.0 * scale[1], -16.0 *
              scale[0], -1.0 * scale[1], -16.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], -2.0 * scale[0],
              11.0 * scale[1], -10.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -11.0 * scale[1], -2.0 * scale[0], -
              17.0 * scale[1], 21.0 * scale[0], -27.0 * scale[1])
    Curveto_r(16.0 * scale[0], -7.0 * scale[1], 28.0 * scale[0], -
              18.0 * scale[1], 27.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -7.0 * scale[1], 3.0 * scale[0], -
              12.0 * scale[1], 10.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 1.0 * scale[1], 11.0 * scale[0], -
              2.0 * scale[1], 7.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              13.0 * scale[1], 9.0 * scale[0], -16.0 * scale[1])
    Curveto_r(9.0 * scale[0], -3.0 * scale[1], 14.0 * scale[0], -
              10.0 * scale[1], 11.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], 2.0 * scale[0], -
              11.0 * scale[1], 10.0 * scale[0], -14.0 * scale[1])
    Curveto_r(9.0 * scale[0], -3.0 * scale[1], 18.0 * scale[0],
              1.0 * scale[1], 21.0 * scale[0], 9.0 * scale[1])
    Curveto_r(4.0 * scale[0], 8.0 * scale[1], 9.0 * scale[0],
              13.0 * scale[1], 13.0 * scale[0], 11.0 * scale[1])
    Curveto_r(3.0 * scale[0], -2.0 * scale[1], 5.0 * scale[0],
              19.0 * scale[1], 3.0 * scale[0], 47.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 49.0 * scale[1], -2.0 * scale[0],
              50.0 * scale[1], 10.0 * scale[0], 24.0 * scale[1])
    Curveto_r(12.0 * scale[0], -26.0 * scale[1], 14.0 * scale[0], -
              27.0 * scale[1], 36.0 * scale[0], -12.0 * scale[1])
    Curveto_r(21.0 * scale[0], 15.0 * scale[1], 22.0 * scale[0],
              23.0 * scale[1], 22.0 * scale[0], 130.0 * scale[1])
    Lineto_r(0.0 * scale[0], 114.0 * scale[1])
    Lineto_r(-207.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-115.0 * scale[0], -1.0 * scale[1], -218.0 *
              scale[0], -3.0 * scale[1], -230.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(73.0 * scale[0], -158.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -9.0 * scale[1], -9.0 * scale[0], -
              15.0 * scale[1], -11.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -3.0 * scale[0],
              13.0 * scale[1], 1.0 * scale[0], 22.0 * scale[1])
    Curveto_r(4.0 * scale[0], 9.0 * scale[1], 9.0 * scale[0],
              15.0 * scale[1], 11.0 * scale[0], 12.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 3.0 * scale[0], -
              13.0 * scale[1], -1.0 * scale[0], -22.0 * scale[1])
    te.end_fill()
    Moveto_r(50.0 * scale[0], -9.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(18.0 * scale[0], -27.0 * scale[1], 13.0 * scale[0], -
              39.0 * scale[1], -19.0 * scale[0], -57.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -10.0 * scale[1], -21.0 *
              scale[0], -9.0 * scale[1], -9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(14.0 * scale[0], 17.0 * scale[1], 1.0 * scale[0],
              34.0 * scale[1], -17.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -13.0 * scale[0],
              0.0 * scale[1], -17.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 7.0 * scale[1], -3.0 * scale[0],
              9.0 * scale[1], 3.0 * scale[0], 6.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 14.0 * scale[0],
              4.0 * scale[1], 17.0 * scale[0], 18.0 * scale[1])
    Curveto_r(8.0 * scale[0], 32.0 * scale[1], 21.0 * scale[0],
              32.0 * scale[1], 42.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto_r(234.0 * scale[0], -41.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -5.0 * scale[0], -
              12.0 * scale[1], -10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -8.0 * scale[0],
              11.0 * scale[1], -5.0 * scale[0], 16.0 * scale[1])
    Curveto_r(9.0 * scale[0], 14.0 * scale[1], 15.0 * scale[0],
              11.0 * scale[1], 15.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(1.0 * scale[0], 908.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-1.0 * scale[0], -58.0 * scale[1])
    Lineto_r(25.0 * scale[0], 12.0 * scale[1])
    Curveto_r(28.0 * scale[0], 12.0 * scale[1], 35.0 * scale[0],
              31.0 * scale[1], 8.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -5.0 * scale[1], -15.0 *
              scale[0], -2.0 * scale[1], -10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              17.0 * scale[1], -3.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0],
              12.0 * scale[1], -13.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 15.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -6.0 * scale[0], -30.0 * scale[1])
    te.end_fill()
    Moveto(25.0 * scale[0], 840.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -11.0 * scale[1], -11.0 * scale[0], -
              20.0 * scale[1], -16.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              10.0 * scale[1], -9.0 * scale[0], -21.0 * scale[1])
    Curveto_r(0.0 * scale[0], -18.0 * scale[1], 4.0 * scale[0], -
              16.0 * scale[1], 25.0 * scale[0], 15.0 * scale[1])
    Curveto_r(28.0 * scale[0], 41.0 * scale[1], 29.0 * scale[0],
              46.0 * scale[1], 16.0 * scale[0], 46.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              9.0 * scale[1], -16.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(463.0 * scale[0], 745.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -27.0 * scale[1], 2.0 * scale[0], -
              38.0 * scale[1], 4.0 * scale[0], -22.0 * scale[1])
    Curveto_r(2.0 * scale[0], 15.0 * scale[1], 2.0 * scale[0],
              37.0 * scale[1], 0.0 * scale[0], 50.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 12.0 * scale[1], -4.0 * scale[0],
              0.0 * scale[1], -4.0 * scale[0], -28.0 * scale[1])
    te.end_fill()
    Moveto(10.0 * scale[0], 762.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              9.0 * scale[1], 15.0 * scale[0], -9.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              4.0 * scale[1], 9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -9.0 * scale[0],
              8.0 * scale[1], -15.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              4.0 * scale[1], -9.0 * scale[0], -8.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#a97436')
    te.end_fill()
    Moveto(360.0 * scale[0], 1387.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 14.0 * scale[0], -
              13.0 * scale[1], 30.0 * scale[0], -18.0 * scale[1])
    Curveto_r(17.0 * scale[0], -6.0 * scale[1], 30.0 * scale[0], -
              16.0 * scale[1], 30.0 * scale[0], -22.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -4.0 * scale[0], -
              7.0 * scale[1], -12.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 7.0 * scale[1], -20.0 * scale[0],
              12.0 * scale[1], -30.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 0.0 * scale[1], -29.0 * scale[0],
              6.0 * scale[1], -41.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 10.0 * scale[1], -42.0 * scale[0],
              13.0 * scale[1], -102.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-57.0 * scale[0], -4.0 * scale[1], -73.0 *
              scale[0], -8.0 * scale[1], -55.0 * scale[0], -13.0 * scale[1])
    Curveto_r(21.0 * scale[0], -6.0 * scale[1], 19.0 * scale[0], -
              7.0 * scale[1], -15.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-22.0 * scale[0], -1.0 * scale[1], -49.0 *
              scale[0], -5.0 * scale[1], -59.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -7.0 * scale[1], -18.0 *
              scale[0], -8.0 * scale[1], 5.0 * scale[0], -15.0 * scale[1])
    Curveto_r(36.0 * scale[0], -12.0 * scale[1], 41.0 * scale[0], -
              13.0 * scale[1], 79.0 * scale[0], -15.0 * scale[1])
    Curveto_r(29.0 * scale[0], -2.0 * scale[1], 32.0 * scale[0], -
              4.0 * scale[1], 15.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -5.0 * scale[1], -14.0 *
              scale[0], -9.0 * scale[1], -7.0 * scale[0], -9.0 * scale[1])
    Curveto_r(7.0 * scale[0], -1.0 * scale[1], 11.0 * scale[0], -
              5.0 * scale[1], 8.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], 17.0 *
              scale[0], -6.0 * scale[1], 45.0 * scale[0], -4.0 * scale[1])
    Curveto_r(35.0 * scale[0], 3.0 * scale[1], 49.0 * scale[0],
              0.0 * scale[1], 44.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              9.0 * scale[1], 30.0 * scale[0], -4.0 * scale[1])
    Curveto_r(30.0 * scale[0], 5.0 * scale[1], 36.0 * scale[0],
              4.0 * scale[1], 30.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -9.0 * scale[1], -4.0 *
              scale[0], -11.0 * scale[1], 3.0 * scale[0], -6.0 * scale[1])
    Curveto_r(19.0 * scale[0], 12.0 * scale[1], 14.0 * scale[0],
              26.0 * scale[1], -10.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 1.0 * scale[1], -9.0 * scale[0],
              4.0 * scale[1], 15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(21.0 * scale[0], 5.0 * scale[1], 45.0 * scale[0],
              16.0 * scale[1], 54.0 * scale[0], 24.0 * scale[1])
    Curveto_r(8.0 * scale[0], 8.0 * scale[1], 19.0 * scale[0],
              12.0 * scale[1], 25.0 * scale[0], 9.0 * scale[1])
    Curveto_r(7.0 * scale[0], -4.0 * scale[1], 8.0 *
              scale[0], -2.0 * scale[1], 4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 16.0 * scale[1], 46.0 * scale[0],
              16.0 * scale[1], 62.0 * scale[0], 0.0 * scale[1])
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 12.0 * scale[0], -
              8.0 * scale[1], 12.0 * scale[0], -3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 7.0 * scale[0],
              0.0 * scale[1], 16.0 * scale[0], -11.0 * scale[1])
    Curveto_r(8.0 * scale[0], -10.0 * scale[1], 13.0 *
              scale[0], -13.0 * scale[1], 9.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 8.0 * scale[1], -1.0 * scale[0],
              11.0 * scale[1], 9.0 * scale[0], 7.0 * scale[1])
    Curveto_r(9.0 * scale[0], -3.0 * scale[1], 15.0 * scale[0], -
              9.0 * scale[1], 14.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -24.0 * scale[1], 6.0 * scale[0], -
              32.0 * scale[1], 33.0 * scale[0], -32.0 * scale[1])
    Curveto_r(21.0 * scale[0], 0.0 * scale[1], 28.0 * scale[0], -
              4.0 * scale[1], 23.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -10.0 * scale[1], -4.0 *
              scale[0], -10.0 * scale[1], 7.0 * scale[0], 0.0 * scale[1])
    Curveto_r(19.0 * scale[0], 18.0 * scale[1], 34.0 * scale[0],
              15.0 * scale[1], 18.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -15.0 * scale[1], -12.0 *
              scale[0], -15.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(12.0 * scale[0], 6.0 * scale[1], 22.0 * scale[0],
              8.0 * scale[1], 21.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -22.0 * scale[1], 2.0 * scale[0], -
              34.0 * scale[1], 14.0 * scale[0], -27.0 * scale[1])
    Curveto_r(9.0 * scale[0], 6.0 * scale[1], 9.0 * scale[0],
              4.0 * scale[1], -1.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -13.0 * scale[1], -10.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -22.0 * scale[1])
    Curveto_r(9.0 * scale[0], -3.0 * scale[1], 19.0 * scale[0], -
              4.0 * scale[1], 23.0 * scale[0], -1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 2.0 * scale[1], 8.0 * scale[0], -
              2.0 * scale[1], 8.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], -5.0 * scale[0], -
              11.0 * scale[1], -17.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 5.0 * scale[1], -30.0 * scale[0],
              7.0 * scale[1], -46.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -2.0 * scale[1], -33.0 *
              scale[0], -4.0 * scale[1], -37.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -1.0 * scale[1], -6.0 * scale[0], -
              5.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              8.0 * scale[1], -12.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0],
              8.0 * scale[1], -24.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 10.0 * scale[1], -7.0 * scale[0],
              6.0 * scale[1], -7.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -26.0 * scale[1], -36.0 * scale[0], -
              62.0 * scale[1], -52.0 * scale[0], -52.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 2.0 * scale[1], -10.0 * scale[0],
              0.0 * scale[1], -13.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -24.0 *
              scale[0], -5.0 * scale[1], -48.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 5.0 * scale[1], -80.0 * scale[0],
              11.0 * scale[1], -125.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-46.0 * scale[0], 3.0 * scale[1], -96.0 * scale[0],
              10.0 * scale[1], -113.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 5.0 * scale[1], -30.0 * scale[0],
              5.0 * scale[1], -30.0 * scale[0], -1.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 12.0 * scale[0], -
              11.0 * scale[1], 28.0 * scale[0], -15.0 * scale[1])
    Curveto_r(67.0 * scale[0], -15.0 * scale[1], 104.0 * scale[0], -
              26.0 * scale[1], 100.0 * scale[0], -29.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -2.0 * scale[1], -32.0 * scale[0],
              3.0 * scale[1], -67.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-35.0 * scale[0], 8.0 * scale[1], -66.0 * scale[0],
              13.0 * scale[1], -68.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], 8.0 * scale[0], -
              8.0 * scale[1], 23.0 * scale[0], -11.0 * scale[1])
    Curveto_r(45.0 * scale[0], -10.0 * scale[1], 115.0 * scale[0], -
              37.0 * scale[1], 110.0 * scale[0], -42.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -20.0 * scale[0],
              0.0 * scale[1], -39.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-40.0 * scale[0], 13.0 * scale[1], -145.0 * scale[0],
              26.0 * scale[1], -135.0 * scale[0], 16.0 * scale[1])
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], 12.0 * scale[0], -
              8.0 * scale[1], 20.0 * scale[0], -9.0 * scale[1])
    Curveto_r(7.0 * scale[0], -1.0 * scale[1], 32.0 * scale[0], -
              12.0 * scale[1], 55.0 * scale[0], -24.0 * scale[1])
    Curveto_r(40.0 * scale[0], -21.0 * scale[1], 109.0 * scale[0], -
              27.0 * scale[1], 119.0 * scale[0], -10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], 9.0 * scale[0],
              6.0 * scale[1], 13.0 * scale[0], 3.0 * scale[1])
    Curveto_r(5.0 * scale[0], -2.0 * scale[1], 100.0 * scale[0], -
              7.0 * scale[1], 212.0 * scale[0], -10.0 * scale[1])
    Curveto_r(183.0 * scale[0], -5.0 * scale[1], 201.0 *
              scale[0], -4.0 * scale[1], 179.0 * scale[0], 9.0 * scale[1])
    Lineto_r(-25.0 * scale[0], 15.0 * scale[1])
    Lineto_r(23.0 * scale[0], 1.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 36.0 * scale[0],
              7.0 * scale[1], 51.0 * scale[0], 15.0 * scale[1])
    Curveto_r(16.0 * scale[0], 8.0 * scale[1], 32.0 * scale[0],
              11.0 * scale[1], 36.0 * scale[0], 7.0 * scale[1])
    Curveto_r(5.0 * scale[0], -4.0 * scale[1], 5.0 *
              scale[0], -1.0 * scale[1], 1.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 14.0 * scale[1], -36.0 * scale[0],
              17.0 * scale[1], -36.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -46.0 * scale[0], -
              9.0 * scale[1], -102.0 * scale[0], -8.0 * scale[1])
    Lineto_r(-103.0 * scale[0], 0.0 * scale[1])
    Lineto_r(92.0 * scale[0], 6.0 * scale[1])
    Curveto_r(72.0 * scale[0], 5.0 * scale[1], 96.0 * scale[0],
              10.0 * scale[1], 110.0 * scale[0], 25.0 * scale[1])
    Curveto_r(10.0 * scale[0], 10.0 * scale[1], 13.0 * scale[0],
              16.0 * scale[1], 7.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -4.0 * scale[1], -20.0 * scale[0],
              3.0 * scale[1], -30.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 18.0 * scale[1], -16.0 * scale[0],
              19.0 * scale[1], -1.0 * scale[0], 13.0 * scale[1])
    Curveto_r(10.0 * scale[0], -3.0 * scale[1], 17.0 *
              scale[0], -1.0 * scale[1], 17.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 5.0 * scale[0],
              10.0 * scale[1], 12.0 * scale[0], 9.0 * scale[1])
    Curveto_r(7.0 * scale[0], -2.0 * scale[1], 12.0 * scale[0],
              4.0 * scale[1], 13.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], -15.0 * scale[0],
              20.0 * scale[1], -35.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 7.0 * scale[1], -27.0 * scale[0],
              12.0 * scale[1], -17.0 * scale[0], 13.0 * scale[1])
    Curveto_r(28.0 * scale[0], 2.0 * scale[1], 20.0 * scale[0],
              29.0 * scale[1], -10.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 4.0 * scale[1], -24.0 *
              scale[0], 4.0 * scale[1], 7.0 * scale[0], 6.0 * scale[1])
    Curveto_r(33.0 * scale[0], 3.0 * scale[1], 33.0 * scale[0],
              4.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 7.0 * scale[1], -23.0 * scale[0],
              8.0 * scale[1], -4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(12.0 * scale[0], 1.0 * scale[1], 28.0 * scale[0],
              9.0 * scale[1], 35.0 * scale[0], 18.0 * scale[1])
    Curveto_r(12.0 * scale[0], 15.0 * scale[1], 12.0 * scale[0],
              16.0 * scale[1], -3.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -3.0 * scale[1], -20.0 *
              scale[0], -2.0 * scale[1], -23.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], 14.0 * scale[0],
              10.0 * scale[1], 42.0 * scale[0], 11.0 * scale[1])
    Curveto_r(43.0 * scale[0], 1.0 * scale[1], 45.0 * scale[0],
              2.0 * scale[1], 19.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 5.0 * scale[1], -34.0 * scale[0],
              6.0 * scale[1], -39.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -3.0 * scale[1], -7.0 *
              scale[0], -1.0 * scale[1], -4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(8.0 * scale[0], 13.0 * scale[1], -64.0 * scale[0],
              31.0 * scale[1], -150.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-94.0 * scale[0], 6.0 * scale[1], -85.0 *
              scale[0], -6.0 * scale[1], 27.0 * scale[0], -39.0 * scale[1])
    Lineto_r(45.0 * scale[0], -13.0 * scale[1])
    Lineto_r(-40.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 2.0 * scale[1], -63.0 * scale[0],
              14.0 * scale[1], -90.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-36.0 * scale[0], 17.0 * scale[1], -75.0 * scale[0],
              25.0 * scale[1], -138.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-48.0 * scale[0], 3.0 * scale[1], -87.0 * scale[0],
              1.0 * scale[1], -87.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto_r(-53.0 * scale[0], -83.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 17.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(390.0 * scale[0], -10.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 17.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(-260.0 * scale[0], -198.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(8.0 * scale[0], -8.0 * scale[1], -24.0 *
              scale[0], -6.0 * scale[1], -62.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-26.0 * scale[0], 7.0 * scale[1], -24.0 * scale[0],
              7.0 * scale[1], 13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(23.0 * scale[0], -2.0 * scale[1], 46.0 * scale[0], -
              6.0 * scale[1], 49.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto_r(90.0 * scale[0], -2.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -9.0 * scale[1], -76.0 * scale[0], -
              10.0 * scale[1], -71.0 * scale[0], -2.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], 21.0 * scale[0],
              8.0 * scale[1], 41.0 * scale[0], 8.0 * scale[1])
    Curveto_r(20.0 * scale[0], 0.0 * scale[1], 34.0 * scale[0], -
              3.0 * scale[1], 30.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto_r(58.0 * scale[0], -4.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -6.0 * scale[1], -1.0 * scale[0], -
              7.0 * scale[1], -9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 7.0 * scale[1], -21.0 * scale[0],
              14.0 * scale[1], -7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0], -
              4.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto_r(112.0 * scale[0], -36.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 17.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(172.0 * scale[0], 1275.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
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
    Moveto(187.0 * scale[0], 1249.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -12.0 * scale[1], 0.0 * scale[0], -
              22.0 * scale[1], 8.0 * scale[0], -25.0 * scale[1])
    Curveto_r(22.0 * scale[0], -9.0 * scale[1], 80.0 * scale[0],
              2.0 * scale[1], 78.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 6.0 * scale[1], 3.0 * scale[0],
              11.0 * scale[1], 10.0 * scale[0], 12.0 * scale[1])
    Curveto_r(19.0 * scale[0], 2.0 * scale[1], -35.0 * scale[0],
              17.0 * scale[1], -64.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 1.0 * scale[1], -28.0 * scale[0], -
              5.0 * scale[1], -32.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(320.0 * scale[0], 1240.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -9.0 * scale[1], -13.0 *
              scale[0], -10.0 * scale[1], 0.0 * scale[0], -10.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0], -
              1.0 * scale[1], 0.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -7.0 * scale[1], -11.0 *
              scale[0], -10.0 * scale[1], -2.0 * scale[0], -10.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 28.0 * scale[0],
              27.0 * scale[1], 20.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 2.0 * scale[1], -10.0 * scale[0],
              0.0 * scale[1], -18.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(601.0 * scale[0], 1224.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(356.0 * scale[0], 1213.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(645.0 * scale[0], 1220.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(243.0 * scale[0], 1212.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-18.0 * scale[0], -2.0 * scale[1], -33.0 *
              scale[0], -7.0 * scale[1], -33.0 * scale[0], -12.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -8.0 * scale[0], -
              7.0 * scale[1], -17.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 5.0 * scale[1], -17.0 * scale[0],
              4.0 * scale[1], -3.0 * scale[0], -11.0 * scale[1])
    Curveto_r(14.0 * scale[0], -14.0 * scale[1], 45.0 * scale[0], -
              22.0 * scale[1], 166.0 * scale[0], -41.0 * scale[1])
    Curveto_r(23.0 * scale[0], -4.0 * scale[1], 31.0 *
              scale[0], -1.0 * scale[1], 31.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], -10.0 * scale[0],
              15.0 * scale[1], -28.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-37.0 * scale[0], 0.0 * scale[1], -59.0 * scale[0],
              9.0 * scale[1], -59.0 * scale[0], 25.0 * scale[1])
    Curveto_r(0.0 * scale[0], 16.0 * scale[1], -17.0 * scale[0],
              21.0 * scale[1], -57.0 * scale[0], 17.0 * scale[1])
    te.end_fill()
    Moveto(403.0 * scale[0], 1155.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              12.0 * scale[1], 9.0 * scale[0], -9.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 6.0 * scale[0],
              10.0 * scale[1], 3.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 13.0 * scale[1], -12.0 * scale[0],
              11.0 * scale[1], -12.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(120.0 * scale[0], 1148.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 7.0 * scale[0], -
              8.0 * scale[1], 15.0 * scale[0], -8.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              4.0 * scale[1], 15.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -7.0 * scale[0],
              9.0 * scale[1], -15.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              4.0 * scale[1], -15.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(198.0 * scale[0], 1043.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(877.0 * scale[0], 864.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], 2.0 * scale[0], -
              18.0 * scale[1], 11.0 * scale[0], -34.0 * scale[1])
    Curveto_r(15.0 * scale[0], -25.0 * scale[1], 15.0 * scale[0], -
              29.0 * scale[1], -1.0 * scale[0], -44.0 * scale[1])
    Curveto_r(-25.0 * scale[0], -25.0 * scale[1], 9.0 * scale[0], -
              96.0 * scale[1], 45.0 * scale[0], -96.0 * scale[1])
    Curveto_r(16.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0],
              5.0 * scale[1], 14.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 12.0 * scale[1], -6.0 * scale[0],
              25.0 * scale[1], -6.0 * scale[0], 30.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], -4.0 * scale[0],
              7.0 * scale[1], -10.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              8.0 * scale[1], -4.0 * scale[0], -17.0 * scale[1])
    Curveto_r(2.0 * scale[0], -10.0 * scale[1], -1.0 *
              scale[0], -7.0 * scale[1], -8.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 14.0 * scale[1], -17.0 * scale[0],
              28.0 * scale[1], -23.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 5.0 * scale[1], -5.0 * scale[0],
              8.0 * scale[1], 3.0 * scale[0], 8.0 * scale[1])
    Curveto_r(17.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0],
              76.0 * scale[1], -2.0 * scale[0], 83.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -16.0 * scale[0],
              3.0 * scale[1], -19.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(740.0 * scale[0], 840.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -17.0 * scale[1], -8.0 * scale[0], -
              20.0 * scale[1], 12.0 * scale[0], -17.0 * scale[1])
    Curveto_r(14.0 * scale[0], 1.0 * scale[1], 22.0 * scale[0], -
              3.0 * scale[1], 21.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -7.0 * scale[1], 4.0 * scale[0], -
              10.0 * scale[1], 12.0 * scale[0], -7.0 * scale[1])
    Curveto_r(16.0 * scale[0], 7.0 * scale[1], 18.0 * scale[0],
              14.0 * scale[1], 9.0 * scale[0], 38.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 22.0 * scale[1], -41.0 * scale[0],
              20.0 * scale[1], -54.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(830.0 * scale[0], 817.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 26.0 * scale[0], -
              87.0 * scale[1], 33.0 * scale[0], -87.0 * scale[1])
    Curveto_r(1.0 * scale[0], 0.0 * scale[1], 3.0 * scale[0],
              26.0 * scale[1], 4.0 * scale[0], 58.0 * scale[1])
    Curveto_r(1.0 * scale[0], 50.0 * scale[1], 0.0 * scale[0],
              53.0 * scale[1], -8.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -38.0 * scale[1], -22.0 *
              scale[0], -45.0 * scale[1], -13.0 * scale[0], -9.0 * scale[1])
    Curveto_r(3.0 * scale[0], 13.0 * scale[1], 1.0 * scale[0],
              27.0 * scale[1], -5.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 5.0 * scale[1], -11.0 * scale[0], -
              2.0 * scale[1], -11.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(931.0 * scale[0], 813.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -17.0 * scale[1], 18.0 * scale[0], -
              47.0 * scale[1], 18.0 * scale[0], -35.0 * scale[1])
    Curveto_r(1.0 * scale[0], 7.0 * scale[1], 6.0 * scale[0],
              10.0 * scale[1], 12.0 * scale[0], 6.0 * scale[1])
    Curveto_r(8.0 * scale[0], -4.0 * scale[1], 8.0 * scale[0],
              0.0 * scale[1], 0.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 20.0 * scale[1], -32.0 * scale[0],
              29.0 * scale[1], -30.0 * scale[0], 14.0 * scale[1])
    te.end_fill()
    Moveto(584.0 * scale[0], 804.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-15.0 * scale[0], -6.0 * scale[1], -6.0 * scale[0], -
              51.0 * scale[1], 12.0 * scale[0], -58.0 * scale[1])
    Curveto_r(10.0 * scale[0], -4.0 * scale[1], 14.0 * scale[0],
              4.0 * scale[1], 14.0 * scale[0], 29.0 * scale[1])
    Curveto_r(0.0 * scale[0], 34.0 * scale[1], -4.0 * scale[0],
              38.0 * scale[1], -26.0 * scale[0], 29.0 * scale[1])
    te.end_fill()
    Moveto(733.0 * scale[0], 799.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -6.0 * scale[1], 15.0 * scale[0], -
              14.0 * scale[1], 12.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              11.0 * scale[1], 5.0 * scale[0], -15.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0], -
              21.0 * scale[1], 4.0 * scale[0], -39.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -26.0 * scale[1], 1.0 * scale[0], -
              40.0 * scale[1], 21.0 * scale[0], -64.0 * scale[1])
    Curveto_r(26.0 * scale[0], -31.0 * scale[1], 62.0 *
              scale[0], -34.0 * scale[1], 51.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], -1.0 * scale[0],
              11.0 * scale[1], 4.0 * scale[0], 8.0 * scale[1])
    Curveto_r(15.0 * scale[0], -9.0 * scale[1], 12.0 * scale[0],
              37.0 * scale[1], -4.0 * scale[0], 58.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 9.0 * scale[1], -18.0 * scale[0],
              17.0 * scale[1], -24.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0],
              7.0 * scale[1], -5.0 * scale[0], 16.0 * scale[1])
    Curveto_r(6.0 * scale[0], 17.0 * scale[1], -29.0 * scale[0],
              47.0 * scale[1], -62.0 * scale[0], 51.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 3.0 * scale[1], -19.0 * scale[0],
              2.0 * scale[1], -2.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto_r(82.0 * scale[0], -97.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -7.0 * scale[1], -5.0 * scale[0], -
              18.0 * scale[1], -5.0 * scale[0], -23.0 * scale[1])
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], -32.0 *
              scale[0], -8.0 * scale[1], -42.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 13.0 * scale[1], 12.0 * scale[0],
              32.0 * scale[1], 34.0 * scale[0], 32.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0], -
              5.0 * scale[1], 13.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(104.0 * scale[0], 686.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], 3.0 * scale[0], -
              23.0 * scale[1], 13.0 * scale[0], -33.0 * scale[1])
    Curveto_r(21.0 * scale[0], -20.0 * scale[1], 84.0 * scale[0], -
              46.0 * scale[1], 92.0 * scale[0], -37.0 * scale[1])
    Curveto_r(9.0 * scale[0], 9.0 * scale[1], -30.0 * scale[0],
              33.0 * scale[1], -44.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -3.0 * scale[1], -16.0 *
              scale[0], -1.0 * scale[1], -20.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], 1.0 * scale[0],
              14.0 * scale[1], 9.0 * scale[0], 17.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 13.0 * scale[0],
              10.0 * scale[1], 10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], -10.0 * scale[0],
              7.0 * scale[1], -15.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -4.0 * scale[1], -9.0 *
              scale[0], -1.0 * scale[1], -9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 16.0 * scale[1], -30.0 * scale[0],
              13.0 * scale[1], -36.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(3.0 * scale[0], 628.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -7.0 * scale[1], 10.0 * scale[0], -
              12.0 * scale[1], 17.0 * scale[0], -10.0 * scale[1])
    Curveto_r(9.0 * scale[0], 2.0 * scale[1], 8.0 * scale[0], -
              5.0 * scale[1], -4.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -29.0 * scale[1], -21.0 *
              scale[0], -40.0 * scale[1], -6.0 * scale[0], -31.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 10.0 * scale[0], -
              1.0 * scale[1], 10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(0.0 * scale[0], -23.0 * scale[1], 28.0 *
              scale[0], -20.0 * scale[1], 35.0 * scale[0], 4.0 * scale[1])
    Curveto_r(4.0 * scale[0], 11.0 * scale[1], 10.0 * scale[0],
              18.0 * scale[1], 14.0 * scale[0], 16.0 * scale[1])
    Curveto_r(4.0 * scale[0], -3.0 * scale[1], 13.0 *
              scale[0], -1.0 * scale[1], 21.0 * scale[0], 5.0 * scale[1])
    Curveto_r(12.0 * scale[0], 7.0 * scale[1], 12.0 * scale[0],
              9.0 * scale[1], 1.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0],
              6.0 * scale[1], -7.0 * scale[0], 15.0 * scale[1])
    Curveto_r(4.0 * scale[0], 10.0 * scale[1], -1.0 * scale[0],
              15.0 * scale[1], -14.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0],
              5.0 * scale[1], -20.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -12.0 * scale[0],
              10.0 * scale[1], -26.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -24.0 * scale[0], -
              5.0 * scale[1], -21.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto_r(51.0 * scale[0], -53.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -14.0 * scale[1], -19.0 * scale[0], -
              24.0 * scale[1], -21.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 7.0 * scale[1], 16.0 * scale[0],
              46.0 * scale[1], 28.0 * scale[0], 46.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 2.0 * scale[0], -
              11.0 * scale[1], -7.0 * scale[0], -25.0 * scale[1])
    te.end_fill()
    Moveto(330.0 * scale[0], 628.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 5.0 * scale[0], -
              20.0 * scale[1], 10.0 * scale[0], -23.0 * scale[1])
    Curveto_r(13.0 * scale[0], -8.0 * scale[1], 13.0 * scale[0],
              5.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 13.0 * scale[1], -10.0 * scale[0],
              13.0 * scale[1], -10.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(240.0 * scale[0], 580.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 7.0 * scale[0], -
              13.0 * scale[1], 15.0 * scale[0], -20.0 * scale[1])
    Curveto_r(12.0 * scale[0], -10.0 * scale[1], 15.0 *
              scale[0], -9.0 * scale[1], 15.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], -7.0 * scale[0],
              20.0 * scale[1], -15.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              4.0 * scale[1], -15.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(95.0 * scale[0], 539.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 1.0 *
              scale[0], -6.0 * scale[1], 9.0 * scale[0], -3.0 * scale[1])
    Curveto_r(12.0 * scale[0], 5.0 * scale[1], 13.0 * scale[0], -
              3.0 * scale[1], 9.0 * scale[0], -47.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -42.0 * scale[1], -2.0 *
              scale[0], -51.0 * scale[1], 9.0 * scale[0], -46.0 * scale[1])
    Curveto_r(11.0 * scale[0], 4.0 * scale[1], 14.0 * scale[0], -
              3.0 * scale[1], 13.0 * scale[0], -29.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -36.0 * scale[1], 10.0 * scale[0], -
              40.0 * scale[1], 38.0 * scale[0], -10.0 * scale[1])
    Curveto_r(10.0 * scale[0], 11.0 * scale[1], 17.0 * scale[0],
              35.0 * scale[1], 17.0 * scale[0], 58.0 * scale[1])
    Curveto_r(0.0 * scale[0], 35.0 * scale[1], -4.0 * scale[0],
              41.0 * scale[1], -30.0 * scale[0], 51.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 6.0 * scale[1], -29.0 * scale[0],
              16.0 * scale[1], -26.0 * scale[0], 22.0 * scale[1])
    Curveto_r(5.0 * scale[0], 13.0 * scale[1], -31.0 * scale[0],
              17.0 * scale[1], -39.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto_r(70.0 * scale[0], -59.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -11.0 * scale[0], -
              16.0 * scale[1], -25.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-24.0 * scale[0], -4.0 * scale[1], -25.0 *
              scale[0], -3.0 * scale[1], -5.0 * scale[0], 12.0 * scale[1])
    Curveto_r(19.0 * scale[0], 15.0 * scale[1], 19.0 * scale[0],
              16.0 * scale[1], 1.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -4.0 * scale[1], -17.0 *
              scale[0], -3.0 * scale[1], -12.0 * scale[0], 6.0 * scale[1])
    Curveto_r(10.0 * scale[0], 16.0 * scale[1], 41.0 * scale[0],
              10.0 * scale[1], 41.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(13.0 * scale[0], 497.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -13.0 * scale[1], 19.0 * scale[0], -
              22.0 * scale[1], 34.0 * scale[0], -22.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 23.0 * scale[0],
              1.0 * scale[1], 23.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], -32.0 * scale[0],
              34.0 * scale[1], -48.0 * scale[0], 37.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 3.0 * scale[1], -18.0 * scale[0],
              0.0 * scale[1], -9.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(0.0 * scale[0], 461.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 18.0 * scale[1], -14.0 * scale[0],
              21.0 * scale[1], -14.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(205.0 * scale[0], 341.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(30.0 * scale[0], -8.0 * scale[1])
    Lineto_r(-30.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -4.0 * scale[1], -35.0 *
              scale[0], -9.0 * scale[1], -41.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -2.0 * scale[1], -17.0 * scale[0],
              2.0 * scale[1], -23.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 16.0 * scale[1], -3.0 * scale[0], -
              22.0 * scale[1], 15.0 * scale[0], -43.0 * scale[1])
    Curveto_r(7.0 * scale[0], -8.0 * scale[1], 15.0 * scale[0], -
              36.0 * scale[1], 19.0 * scale[0], -62.0 * scale[1])
    Curveto_r(4.0 * scale[0], -27.0 * scale[1], 12.0 * scale[0], -
              48.0 * scale[1], 19.0 * scale[0], -48.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 5.0 * scale[0], -
              4.0 * scale[1], -3.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -5.0 * scale[1], -10.0 * scale[0], -
              14.0 * scale[1], -7.0 * scale[0], -20.0 * scale[1])
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 2.0 * scale[0], -
              27.0 * scale[1], -5.0 * scale[0], -46.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -32.0 * scale[1], -21.0 *
              scale[0], -40.0 * scale[1], -42.0 * scale[0], -36.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 1.0 * scale[1], -6.0 * scale[0], -
              3.0 * scale[1], -3.0 * scale[0], -8.0 * scale[1])
    Curveto_r(17.0 * scale[0], -27.0 * scale[1], 236.0 * scale[0], -
              65.0 * scale[1], 236.0 * scale[0], -41.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], -64.0 * scale[0],
              35.0 * scale[1], -125.0 * scale[0], 50.0 * scale[1])
    Lineto_r(-40.0 * scale[0], 10.0 * scale[1])
    Lineto_r(41.0 * scale[0], -5.0 * scale[1])
    Curveto_r(37.0 * scale[0], -4.0 * scale[1], 40.0 *
              scale[0], -3.0 * scale[1], 40.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 18.0 * scale[1], 4.0 * scale[0],
              22.0 * scale[1], 29.0 * scale[0], 22.0 * scale[1])
    Curveto_r(35.0 * scale[0], 0.0 * scale[1], 58.0 * scale[0],
              12.0 * scale[1], 49.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], -8.0 * scale[0],
              7.0 * scale[1], -12.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -6.0 * scale[1], -9.0 * scale[0],
              60.0 * scale[1], 1.0 * scale[0], 70.0 * scale[1])
    Curveto_r(4.0 * scale[0], 4.0 * scale[1], 7.0 * scale[0],
              19.0 * scale[1], 7.0 * scale[0], 33.0 * scale[1])
    Curveto_r(1.0 * scale[0], 88.0 * scale[1], 153.0 * scale[0],
              117.0 * scale[1], 218.0 * scale[0], 42.0 * scale[1])
    Curveto_r(12.0 * scale[0], -13.0 * scale[1], 40.0 * scale[0], -
              22.0 * scale[1], 87.0 * scale[0], -29.0 * scale[1])
    Curveto_r(39.0 * scale[0], -6.0 * scale[1], 78.0 * scale[0], -
              13.0 * scale[1], 87.0 * scale[0], -17.0 * scale[1])
    Curveto_r(13.0 * scale[0], -5.0 * scale[1], 17.0 *
              scale[0], -2.0 * scale[1], 15.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 14.0 * scale[1], -13.0 * scale[0],
              24.0 * scale[1], -42.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 7.0 * scale[1], -51.0 * scale[0],
              19.0 * scale[1], -64.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -28.0 * scale[0],
              10.0 * scale[1], -33.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -3.0 * scale[1], -8.0 * scale[0],
              0.0 * scale[1], -8.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 7.0 * scale[0],
              9.0 * scale[1], 18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(27.0 * scale[0], -10.0 * scale[1], 125.0 * scale[0], -
              35.0 * scale[1], 139.0 * scale[0], -35.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              5.0 * scale[1], 13.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -4.0 * scale[0],
              7.0 * scale[1], -10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -10.0 *
              scale[0], -3.0 * scale[1], -10.0 * scale[0], 2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], -20.0 * scale[0],
              16.0 * scale[1], -45.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-45.0 * scale[0], 19.0 * scale[1], -90.0 * scale[0],
              20.0 * scale[1], -112.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -5.0 * scale[1], -21.0 *
              scale[0], -6.0 * scale[1], -30.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 4.0 * scale[1], -106.0 * scale[0],
              9.0 * scale[1], -213.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-107.0 * scale[0], 1.0 * scale[1], -181.0 *
              scale[0], -1.0 * scale[1], -165.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(75.0 * scale[0], -47.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], -21.0 * scale[0], -
              4.0 * scale[1], -47.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-37.0 * scale[0], 1.0 * scale[1], -42.0 * scale[0],
              3.0 * scale[1], -23.0 * scale[0], 8.0 * scale[1])
    Curveto_r(24.0 * scale[0], 7.0 * scale[1], 70.0 * scale[0],
              3.0 * scale[1], 70.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(83.0 * scale[0], 9.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              5.0 * scale[1], 12.0 * scale[0], 5.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(257.0 * scale[0], -19.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], -7.0 * scale[0], -
              4.0 * scale[1], -15.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0],
              4.0 * scale[1], -15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 7.0 * scale[0],
              7.0 * scale[1], 15.0 * scale[0], 4.0 * scale[1])
    Curveto_r(8.0 * scale[0], -4.0 * scale[1], 15.0 * scale[0], -
              8.0 * scale[1], 15.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto_r(63.0 * scale[0], -11.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -21.0 *
              scale[0], -2.0 * scale[1], -30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 3.0 * scale[1], -4.0 * scale[0],
              5.0 * scale[1], 12.0 * scale[0], 5.0 * scale[1])
    Curveto_r(17.0 * scale[0], 0.0 * scale[1], 24.0 * scale[0], -
              2.0 * scale[1], 18.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(57.0 * scale[0], -13.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(18.0 * scale[0], -12.0 * scale[1], 2.0 * scale[0], -
              12.0 * scale[1], -25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              9.0 * scale[1], -5.0 * scale[0], 9.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 22.0 * scale[0], -
              4.0 * scale[1], 30.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(115.0 * scale[0], 300.0 * scale[1], x, y)
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
    Moveto(590.0 * scale[0], 239.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 7.0 * scale[0], -
              12.0 * scale[1], 16.0 * scale[0], -17.0 * scale[1])
    Curveto_r(11.0 * scale[0], -6.0 * scale[1], 13.0 * scale[0], -
              11.0 * scale[1], 5.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-27.0 * scale[0], -17.0 * scale[1], -6.0 *
              scale[0], -26.0 * scale[1], 62.0 * scale[0], -26.0 * scale[1])
    Curveto_r(46.0 * scale[0], 0.0 * scale[1], 80.0 * scale[0],
              5.0 * scale[1], 92.0 * scale[0], 14.0 * scale[1])
    Curveto_r(17.0 * scale[0], 12.0 * scale[1], 14.0 * scale[0],
              15.0 * scale[1], -31.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-58.0 * scale[0], 18.0 * scale[1], -144.0 * scale[0],
              28.0 * scale[1], -144.0 * scale[0], 16.0 * scale[1])
    te.end_fill()
    Moveto(588.0 * scale[0], 152.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -15.0 * scale[1], 1.0 * scale[0], -
              17.0 * scale[1], 31.0 * scale[0], -15.0 * scale[1])
    Curveto_r(29.0 * scale[0], 2.0 * scale[1], 31.0 * scale[0],
              1.0 * scale[1], 11.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-22.0 * scale[0], -6.0 * scale[1], -25.0 * scale[0], -
              13.0 * scale[1], -27.0 * scale[0], -59.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -48.0 * scale[1], 0.0 * scale[0], -
              52.0 * scale[1], 25.0 * scale[0], -61.0 * scale[1])
    Curveto_r(16.0 * scale[0], -5.0 * scale[1], 56.0 *
              scale[0], -6.0 * scale[1], 92.0 * scale[0], -2.0 * scale[1])
    Curveto_r(36.0 * scale[0], 4.0 * scale[1], 56.0 * scale[0],
              8.0 * scale[1], 46.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-43.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              15.0 * scale[1], 67.0 * scale[0], 20.0 * scale[1])
    Curveto_r(5.0 * scale[0], 1.0 * scale[1], 6.0 * scale[0],
              5.0 * scale[1], 2.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], -12.0 * scale[0],
              7.0 * scale[1], -20.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -3.0 * scale[1], -15.0 * scale[0],
              0.0 * scale[1], -15.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -3.0 * scale[0],
              10.0 * scale[1], -7.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-27.0 * scale[0], -4.0 * scale[1], -42.0 * scale[0],
              3.0 * scale[1], -37.0 * scale[0], 16.0 * scale[1])
    Curveto_r(6.0 * scale[0], 15.0 * scale[1], -14.0 * scale[0],
              20.0 * scale[1], -59.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -1.0 * scale[1], -16.0 * scale[0],
              2.0 * scale[1], -12.0 * scale[0], 7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], -3.0 * scale[0],
              12.0 * scale[1], -12.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 3.0 * scale[1], 5.0 * scale[0],
              4.0 * scale[1], 33.0 * scale[0], 1.0 * scale[1])
    Curveto_r(58.0 * scale[0], -4.0 * scale[1], 64.0 *
              scale[0], -2.0 * scale[1], 57.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 17.0 * scale[1], -15.0 * scale[0],
              19.0 * scale[1], -88.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-71.0 * scale[0], 0.0 * scale[1], -83.0 * scale[0], -
              3.0 * scale[1], -87.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto_r(115.0 * scale[0], -69.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -21.0 *
              scale[0], -2.0 * scale[1], -30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 3.0 * scale[1], -4.0 * scale[0],
              5.0 * scale[1], 12.0 * scale[0], 5.0 * scale[1])
    Curveto_r(17.0 * scale[0], 0.0 * scale[1], 24.0 * scale[0], -
              2.0 * scale[1], 18.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(466.0 * scale[0], 31.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -3.0 * scale[1], -31.0 * scale[0], -
              12.0 * scale[1], -33.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -10.0 * scale[1], 17.0 * scale[0], -
              12.0 * scale[1], 82.0 * scale[0], -11.0 * scale[1])
    Curveto_r(47.0 * scale[0], 1.0 * scale[1], 80.0 * scale[0],
              5.0 * scale[1], 73.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -16.0 * scale[0],
              5.0 * scale[1], -20.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -3.0 * scale[1], -18.0 * scale[0],
              2.0 * scale[1], -30.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 17.0 * scale[1], -27.0 * scale[0],
              17.0 * scale[1], -72.0 * scale[0], 7.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#834e19')
    te.end_fill()
    Moveto(135.0 * scale[0], 1388.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-49.0 * scale[0], -5.0 * scale[1], -91.0 * scale[0], -
              12.0 * scale[1], -93.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -5.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -18.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0], -
              9.0 * scale[1], -14.0 * scale[0], -20.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 6.0 * scale[0], -
              20.0 * scale[1], 13.0 * scale[0], -20.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0], -
              2.0 * scale[1], 0.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -11.0 * scale[1], -12.0 *
              scale[0], -190.0 * scale[1], 7.0 * scale[0], -202.0 * scale[1])
    Curveto_r(13.0 * scale[0], -8.0 * scale[1], 12.0 * scale[0], -
              10.0 * scale[1], -2.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 0.0 * scale[1], -23.0 * scale[0], -
              19.0 * scale[1], -2.0 * scale[0], -27.0 * scale[1])
    Curveto_r(13.0 * scale[0], -5.0 * scale[1], 13.0 *
              scale[0], -7.0 * scale[1], 2.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -7.0 * scale[1], -10.0 *
              scale[0], -9.0 * scale[1], 2.0 * scale[0], -9.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 26.0 * scale[0], -
              3.0 * scale[1], 39.0 * scale[0], -7.0 * scale[1])
    Curveto_r(18.0 * scale[0], -5.0 * scale[1], 22.0 *
              scale[0], -3.0 * scale[1], 16.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], -4.0 * scale[0],
              11.0 * scale[1], 11.0 * scale[0], 5.0 * scale[1])
    Curveto_r(10.0 * scale[0], -4.0 * scale[1], 52.0 * scale[0], -
              9.0 * scale[1], 93.0 * scale[0], -10.0 * scale[1])
    Lineto_r(75.0 * scale[0], -2.0 * scale[1])
    Lineto_r(-40.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 12.0 * scale[1], -45.0 * scale[0],
              22.0 * scale[1], -53.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 2.0 * scale[1], -19.0 * scale[0],
              8.0 * scale[1], -25.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 9.0 * scale[1], -8.0 * scale[0],
              10.0 * scale[1], 0.0 * scale[0], 6.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 33.0 * scale[0], -
              9.0 * scale[1], 59.0 * scale[0], -12.0 * scale[1])
    Curveto_r(27.0 * scale[0], -2.0 * scale[1], 63.0 * scale[0], -
              10.0 * scale[1], 82.0 * scale[0], -16.0 * scale[1])
    Curveto_r(19.0 * scale[0], -6.0 * scale[1], 36.0 *
              scale[0], -9.0 * scale[1], 39.0 * scale[0], -6.0 * scale[1])
    Curveto_r(5.0 * scale[0], 5.0 * scale[1], -65.0 * scale[0],
              32.0 * scale[1], -110.0 * scale[0], 42.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 3.0 * scale[1], -26.0 * scale[0],
              8.0 * scale[1], -23.0 * scale[0], 11.0 * scale[1])
    Curveto_r(2.0 * scale[0], 3.0 * scale[1], 33.0 * scale[0], -
              2.0 * scale[1], 68.0 * scale[0], -10.0 * scale[1])
    Curveto_r(35.0 * scale[0], -8.0 * scale[1], 65.0 * scale[0], -
              13.0 * scale[1], 67.0 * scale[0], -11.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -33.0 * scale[0],
              14.0 * scale[1], -100.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 4.0 * scale[1], -28.0 * scale[0],
              10.0 * scale[1], -28.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 14.0 * scale[0],
              6.0 * scale[1], 33.0 * scale[0], 1.0 * scale[1])
    Curveto_r(85.0 * scale[0], -23.0 * scale[1], 195.0 *
              scale[0], -19.0 * scale[1], 156.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -9.0 * scale[0],
              3.0 * scale[1], -5.0 * scale[0], -5.0 * scale[1])
    Curveto_r(6.0 * scale[0], -9.0 * scale[1], -1.0 * scale[0], -
              11.0 * scale[1], -26.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-125.0 * scale[0], 21.0 * scale[1], -153.0 * scale[0],
              28.0 * scale[1], -170.0 * scale[0], 43.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 16.0 * scale[1], -19.0 * scale[0],
              16.0 * scale[1], -9.0 * scale[0], -8.0 * scale[1])
    Curveto_r(5.0 * scale[0], -14.0 * scale[1], 6.0 * scale[0], -
              32.0 * scale[1], 1.0 * scale[0], -39.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -8.0 * scale[1], -7.0 * scale[0], -
              17.0 * scale[1], -5.0 * scale[0], -20.0 * scale[1])
    Curveto_r(7.0 * scale[0], -11.0 * scale[1], -60.0 *
              scale[0], -4.0 * scale[1], -84.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 11.0 * scale[1], -21.0 * scale[0],
              15.0 * scale[1], -10.0 * scale[0], 23.0 * scale[1])
    Curveto_r(11.0 * scale[0], 7.0 * scale[1], 11.0 * scale[0],
              11.0 * scale[1], 2.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 2.0 * scale[1], -13.0 * scale[0],
              9.0 * scale[1], -13.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 5.0 * scale[0],
              7.0 * scale[1], 10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 10.0 * scale[0],
              0.0 * scale[1], 10.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -8.0 * scale[0],
              18.0 * scale[1], -18.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 13.0 * scale[1], -29.0 * scale[0],
              74.0 * scale[1], -11.0 * scale[0], 74.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 18.0 * scale[1], 14.0 * scale[0],
              27.0 * scale[1], 44.0 * scale[0], 19.0 * scale[1])
    Curveto_r(15.0 * scale[0], -4.0 * scale[1], 20.0 *
              scale[0], -3.0 * scale[1], 15.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 7.0 * scale[1], -15.0 * scale[0],
              12.0 * scale[1], -24.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-32.0 * scale[0], 1.0 * scale[1], 21.0 * scale[0],
              17.0 * scale[1], 63.0 * scale[0], 19.0 * scale[1])
    Curveto_r(35.0 * scale[0], 2.0 * scale[1], 37.0 * scale[0],
              3.0 * scale[1], 15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 6.0 * scale[1], -10.0 * scale[0],
              8.0 * scale[1], 35.0 * scale[0], 9.0 * scale[1])
    Curveto_r(33.0 * scale[0], 1.0 * scale[1], 67.0 * scale[0],
              6.0 * scale[1], 75.0 * scale[0], 11.0 * scale[1])
    Curveto_r(17.0 * scale[0], 11.0 * scale[1], -1.0 * scale[0],
              10.0 * scale[1], -155.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto_r(19.0 * scale[0], -314.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(19.0 * scale[0], -19.0 * scale[1], 21.0 *
              scale[0], -31.0 * scale[1], 3.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 6.0 * scale[1], -18.0 * scale[0],
              7.0 * scale[1], -22.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -4.0 * scale[1], -5.0 *
              scale[0], -2.0 * scale[1], -2.0 * scale[0], 5.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], 1.0 * scale[0],
              14.0 * scale[1], -5.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 4.0 * scale[1], -9.0 * scale[0],
              6.0 * scale[1], -1.0 * scale[0], 6.0 * scale[1])
    Curveto_r(6.0 * scale[0], 1.0 * scale[1], 19.0 * scale[0], -
              6.0 * scale[1], 27.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto_r(-84.0 * scale[0], -14.0 * scale[1], 0, 0)
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
    Moveto(344.0 * scale[0], 1383.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -10.0 * scale[1], 13.0 * scale[0], -
              20.0 * scale[1], 27.0 * scale[0], -21.0 * scale[1])
    Curveto_r(13.0 * scale[0], -2.0 * scale[1], 30.0 * scale[0], -
              9.0 * scale[1], 37.0 * scale[0], -14.0 * scale[1])
    Curveto_r(8.0 * scale[0], -7.0 * scale[1], 12.0 *
              scale[0], -7.0 * scale[1], 12.0 * scale[0], 0.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -13.0 * scale[0],
              15.0 * scale[1], -30.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 5.0 * scale[1], -30.0 * scale[0],
              15.0 * scale[1], -30.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -4.0 * scale[0],
              11.0 * scale[1], -9.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              8.0 * scale[1], -7.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(450.0 * scale[0], 1391.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(58.0 * scale[0], -4.0 * scale[1], 101.0 * scale[0], -
              14.0 * scale[1], 135.0 * scale[0], -30.0 * scale[1])
    Curveto_r(27.0 * scale[0], -13.0 * scale[1], 68.0 * scale[0], -
              25.0 * scale[1], 90.0 * scale[0], -27.0 * scale[1])
    Lineto_r(40.0 * scale[0], -3.0 * scale[1])
    Lineto_r(-45.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-112.0 * scale[0], 33.0 * scale[1], -121.0 * scale[0],
              45.0 * scale[1], -27.0 * scale[0], 39.0 * scale[1])
    Curveto_r(73.0 * scale[0], -5.0 * scale[1], 159.0 * scale[0], -
              22.0 * scale[1], 153.0 * scale[0], -31.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -11.0 * scale[1], 55.0 *
              scale[0], -12.0 * scale[1], 75.0 * scale[0], -2.0 * scale[1])
    Curveto_r(11.0 * scale[0], 6.0 * scale[1], 20.0 * scale[0],
              6.0 * scale[1], 24.0 * scale[0], 1.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], -4.0 * scale[0], -
              11.0 * scale[1], -15.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -2.0 * scale[1], -17.0 *
              scale[0], -7.0 * scale[1], -12.0 * scale[0], -16.0 * scale[1])
    Curveto_r(13.0 * scale[0], -19.0 * scale[1], 72.0 *
              scale[0], -4.0 * scale[1], 72.0 * scale[0], 19.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], -8.0 * scale[0],
              23.0 * scale[1], -18.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 13.0 * scale[1], -161.0 * scale[0],
              22.0 * scale[1], -377.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-109.0 * scale[0], 1.0 * scale[1], -146.0 * scale[0],
              0.0 * scale[1], -95.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(436.0 * scale[0], 1342.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -4.0 * scale[1], 11.0 *
              scale[0], -6.0 * scale[1], 30.0 * scale[0], -4.0 * scale[1])
    Curveto_r(19.0 * scale[0], 2.0 * scale[1], 34.0 * scale[0],
              6.0 * scale[1], 34.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -59.0 * scale[0],
              4.0 * scale[1], -64.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(140.0 * scale[0], 1320.0 * scale[1], x, y)
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
    Moveto(547.0 * scale[0], 1319.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(775.0 * scale[0], 1320.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 13.0 * scale[0], -
              6.0 * scale[1], 23.0 * scale[0], -3.0 * scale[1])
    Curveto_r(15.0 * scale[0], 6.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -9.0 * scale[1], -23.0 * scale[0], -
              17.0 * scale[1], -35.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -1.0 * scale[1], -18.0 *
              scale[0], -2.0 * scale[1], 4.0 * scale[0], -9.0 * scale[1])
    Lineto_r(25.0 * scale[0], -7.0 * scale[1])
    Lineto_r(-30.0 * scale[0], -5.0 * scale[1])
    Lineto_r(-30.0 * scale[0], -5.0 * scale[1])
    Lineto_r(30.0 * scale[0], 1.0 * scale[1])
    Curveto_r(18.0 * scale[0], 1.0 * scale[1], 29.0 * scale[0],
              6.0 * scale[1], 28.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 6.0 * scale[1], 3.0 * scale[0],
              12.0 * scale[1], 10.0 * scale[0], 12.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0],
              9.0 * scale[1], 30.0 * scale[0], 20.0 * scale[1])
    Curveto_r(16.0 * scale[0], 20.0 * scale[1], 16.0 * scale[0],
              20.0 * scale[1], -24.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 0.0 * scale[1], -38.0 * scale[0], -
              4.0 * scale[1], -34.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(189.0 * scale[0], 1318.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -2.0 * scale[1], -2.0 * scale[0], -
              14.0 * scale[1], -4.0 * scale[0], -28.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -14.0 * scale[1], -6.0 * scale[0], -
              34.0 * scale[1], -10.0 * scale[0], -45.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -14.0 * scale[1], 0.0 * scale[0], -
              27.0 * scale[1], 14.0 * scale[0], -39.0 * scale[1])
    Curveto_r(12.0 * scale[0], -11.0 * scale[1], 21.0 *
              scale[0], -14.0 * scale[1], 21.0 * scale[0], -8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], 8.0 * scale[0],
              13.0 * scale[1], 18.0 * scale[0], 13.0 * scale[1])
    Curveto_r(9.0 * scale[0], 1.0 * scale[1], 4.0 * scale[0],
              4.0 * scale[1], -13.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 5.0 * scale[1], -29.0 * scale[0],
              11.0 * scale[1], -27.0 * scale[0], 26.0 * scale[1])
    Curveto_r(5.0 * scale[0], 28.0 * scale[1], 6.0 * scale[0],
              28.0 * scale[1], 58.0 * scale[0], 20.0 * scale[1])
    Curveto_r(34.0 * scale[0], -5.0 * scale[1], 43.0 * scale[0], -
              9.0 * scale[1], 33.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-23.0 * scale[0], -14.0 * scale[1], 4.0 *
              scale[0], -9.0 * scale[1], 31.0 * scale[0], 6.0 * scale[1])
    Curveto_r(38.0 * scale[0], 22.0 * scale[1], 48.0 * scale[0],
              19.0 * scale[1], 42.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -16.0 * scale[1], -2.0 *
              scale[0], -25.0 * scale[1], 2.0 * scale[0], -21.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], 9.0 * scale[0],
              12.0 * scale[1], 10.0 * scale[0], 20.0 * scale[1])
    Curveto_r(1.0 * scale[0], 7.0 * scale[1], 8.0 * scale[0],
              24.0 * scale[1], 15.0 * scale[0], 36.0 * scale[1])
    Curveto_r(15.0 * scale[0], 29.0 * scale[1], 14.0 * scale[0],
              30.0 * scale[1], -24.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-24.0 * scale[0], -5.0 * scale[1], -25.0 *
              scale[0], -7.0 * scale[1], -7.0 * scale[0], -8.0 * scale[1])
    Curveto_r(38.0 * scale[0], -2.0 * scale[1], 24.0 * scale[0], -
              16.0 * scale[1], -18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-23.0 * scale[0], -1.0 * scale[1], -37.0 * scale[0],
              2.0 * scale[1], -34.0 * scale[0], 7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              8.0 * scale[1], -45.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-28.0 * scale[0], -2.0 * scale[1], -48.0 * scale[0],
              0.0 * scale[1], -45.0 * scale[0], 4.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], -1.0 * scale[0],
              9.0 * scale[1], -8.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0],
              4.0 * scale[1], 7.0 * scale[0], 9.0 * scale[1])
    Curveto_r(17.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              9.0 * scale[1], 3.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 1.0 * scale[1], -18.0 * scale[0],
              0.0 * scale[1], -19.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(288.0 * scale[0], 1303.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(916.0 * scale[0], 1302.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 10.0 * scale[0], -
              20.0 * scale[1], 8.0 * scale[0], -35.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -17.0 * scale[1], 2.0 * scale[0], -
              27.0 * scale[1], 8.0 * scale[0], -25.0 * scale[1])
    Curveto_r(6.0 * scale[0], 2.0 * scale[1], 12.0 * scale[0],
              18.0 * scale[1], 13.0 * scale[0], 36.0 * scale[1])
    Curveto_r(2.0 * scale[0], 27.0 * scale[1], -1.0 * scale[0],
              32.0 * scale[1], -19.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -16.0 *
              scale[0], -3.0 * scale[1], -10.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(678.0 * scale[0], 1293.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(605.0 * scale[0], 1271.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(17.0 * scale[0], -4.0 * scale[1], 39.0 * scale[0], -
              13.0 * scale[1], 51.0 * scale[0], -19.0 * scale[1])
    Curveto_r(16.0 * scale[0], -9.0 * scale[1], 21.0 *
              scale[0], -8.0 * scale[1], 21.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -7.0 * scale[0],
              11.0 * scale[1], -15.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -3.0 * scale[1], -13.0 *
              scale[0], -1.0 * scale[1], -9.0 * scale[0], 5.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], -10.0 * scale[0],
              10.0 * scale[1], -36.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-38.0 * scale[0], 1.0 * scale[1], -39.0 * scale[0],
              0.0 * scale[1], -12.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(780.0 * scale[0], 1240.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -8.0 * scale[0], -
              10.0 * scale[1], -17.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 0.0 * scale[1], -15.0 *
              scale[0], -2.0 * scale[1], 2.0 * scale[0], -9.0 * scale[1])
    Curveto_r(33.0 * scale[0], -14.0 * scale[1], 43.0 *
              scale[0], -11.0 * scale[1], 38.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 20.0 * scale[1], -23.0 * scale[0],
              28.0 * scale[1], -23.0 * scale[0], 10.0 * scale[1])
    te.end_fill()
    Moveto(901.0 * scale[0], 1224.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(592.0 * scale[0], 1200.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 2.0 * scale[0], -
              27.0 * scale[1], 5.0 * scale[0], -17.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              25.0 * scale[1], 0.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(924.0 * scale[0], 1219.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -21.0 * scale[1], -13.0 *
              scale[0], -83.0 * scale[1], -1.0 * scale[0], -92.0 * scale[1])
    Curveto_r(8.0 * scale[0], -6.0 * scale[1], 6.0 * scale[0], -
              7.0 * scale[1], -5.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 4.0 * scale[1], -18.0 * scale[0],
              0.0 * scale[1], -19.0 * scale[0], -12.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], -3.0 * scale[0], -
              12.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 10.0 * scale[1], -11.0 * scale[0],
              9.0 * scale[1], -34.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -9.0 * scale[1], -29.0 * scale[0], -
              13.0 * scale[1], -29.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 3.0 * scale[1], -13.0 * scale[0], -
              1.0 * scale[1], -30.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -8.0 * scale[1], -39.0 * scale[0], -
              15.0 * scale[1], -52.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-22.0 * scale[0], -1.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], 5.0 * scale[0], -16.0 * scale[1])
    Curveto_r(39.0 * scale[0], -21.0 * scale[1], 172.0 *
              scale[0], -16.0 * scale[1], 173.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 4.0 * scale[0],
              26.0 * scale[1], 9.0 * scale[0], 40.0 * scale[1])
    Curveto_r(10.0 * scale[0], 31.0 * scale[1], 13.0 * scale[0],
              120.0 * scale[1], 3.0 * scale[0], 126.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 2.0 * scale[1], -10.0 * scale[0], -
              1.0 * scale[1], -14.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto_r(-44.0 * scale[0], -139.0 * scale[1], 0, 0)
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
    Moveto(620.0 * scale[0], 1209.0 * scale[1], x, y)
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
    Moveto(361.0 * scale[0], 1198.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -20.0 * scale[1], -14.0 *
              scale[0], -23.0 * scale[1], -42.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 7.0 * scale[1], -19.0 * scale[0],
              7.0 * scale[1], -19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], 41.0 * scale[0], -
              24.0 * scale[1], 63.0 * scale[0], -19.0 * scale[1])
    Curveto_r(10.0 * scale[0], 2.0 * scale[1], 12.0 * scale[0],
              9.0 * scale[1], 6.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 17.0 * scale[1], -8.0 * scale[0],
              17.0 * scale[1], -8.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(660.0 * scale[0], 1199.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -8.0 * scale[1], -10.0 *
              scale[0], -9.0 * scale[1], 7.0 * scale[0], -4.0 * scale[1])
    Curveto_r(12.0 * scale[0], 3.0 * scale[1], 31.0 * scale[0],
              2.0 * scale[1], 41.0 * scale[0], -4.0 * scale[1])
    Curveto_r(13.0 * scale[0], -7.0 * scale[1], 19.0 *
              scale[0], -7.0 * scale[1], 19.0 * scale[0], 2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 15.0 * scale[1], -48.0 * scale[0],
              19.0 * scale[1], -67.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(790.0 * scale[0], 1167.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -8.0 * scale[0], -
              6.0 * scale[1], -17.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], 1.0 * scale[0], -13.0 * scale[1])
    Curveto_r(10.0 * scale[0], -11.0 * scale[1], 24.0 * scale[0], -
              18.0 * scale[1], 30.0 * scale[0], -14.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 3.0 * scale[0], -
              3.0 * scale[1], -7.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -15.0 * scale[1], -38.0 * scale[0], -
              20.0 * scale[1], -110.0 * scale[0], -25.0 * scale[1])
    Lineto_r(-92.0 * scale[0], -6.0 * scale[1])
    Lineto_r(103.0 * scale[0], 0.0 * scale[1])
    Curveto_r(61.0 * scale[0], -1.0 * scale[1], 102.0 * scale[0],
              3.0 * scale[1], 102.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 9.0 * scale[0],
              8.0 * scale[1], 20.0 * scale[0], 5.0 * scale[1])
    Curveto_r(17.0 * scale[0], -4.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 11.0 * scale[1], -9.0 * scale[0],
              28.0 * scale[1], -6.0 * scale[0], 38.0 * scale[1])
    Curveto_r(3.0 * scale[0], 14.0 * scale[1], 0.0 * scale[0],
              18.0 * scale[1], -14.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -1.0 * scale[1], -19.0 *
              scale[0], -5.0 * scale[1], -19.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(526.0 * scale[0], 1153.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(550.0 * scale[0], 1142.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-23.0 * scale[0], -22.0 * scale[1], -23.0 *
              scale[0], -24.0 * scale[1], -3.0 * scale[0], -13.0 * scale[1])
    Curveto_r(12.0 * scale[0], 6.0 * scale[1], 25.0 * scale[0],
              16.0 * scale[1], 28.0 * scale[0], 22.0 * scale[1])
    Curveto_r(13.0 * scale[0], 20.0 * scale[1], 0.0 * scale[0],
              15.0 * scale[1], -25.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(468.0 * scale[0], 1133.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(375.0 * scale[0], 1101.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(38.0 * scale[0], -11.0 * scale[1], 70.0 *
              scale[0], -13.0 * scale[1], 62.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -26.0 * scale[0],
              8.0 * scale[1], -49.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-37.0 * scale[0], 2.0 * scale[1], -39.0 * scale[0],
              2.0 * scale[1], -13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(456.0 * scale[0], 1092.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -8.0 * scale[1], 62.0 *
              scale[0], -7.0 * scale[1], 71.0 * scale[0], 2.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0],
              6.0 * scale[1], -30.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 0.0 * scale[1], -38.0 *
              scale[0], -3.0 * scale[1], -41.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(560.0 * scale[0], 1096.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 7.0 * scale[0], -
              7.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 12.0 *
              scale[0], -2.0 * scale[1], 9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], -25.0 * scale[0],
              14.0 * scale[1], -25.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(678.0 * scale[0], 1053.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(393.0 * scale[0], 1043.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(15.0 * scale[0], -2.0 * scale[1], 39.0 *
              scale[0], -2.0 * scale[1], 55.0 * scale[0], 0.0 * scale[1])
    Curveto_r(15.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              4.0 * scale[1], -28.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 0.0 * scale[1], -43.0 *
              scale[0], -2.0 * scale[1], -27.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(750.0 * scale[0], 870.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 9.0 * scale[0], -
              10.0 * scale[1], 19.0 * scale[0], -10.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 21.0 * scale[0], -
              5.0 * scale[1], 23.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], -7.0 * scale[1], 7.0 * scale[0], -
              5.0 * scale[1], 11.0 * scale[0], 6.0 * scale[1])
    Curveto_r(4.0 * scale[0], 9.0 * scale[1], 3.0 * scale[0],
              15.0 * scale[1], -2.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -1.0 * scale[1], -16.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 13.0 * scale[1], -35.0 * scale[0],
              13.0 * scale[1], -35.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(863.0 * scale[0], 854.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -13.0 * scale[1], -7.0 * scale[0], -
              13.0 * scale[1], -14.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 10.0 * scale[1], -9.0 * scale[0],
              10.0 * scale[1], -8.0 * scale[0], -2.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              23.0 * scale[1], 7.0 * scale[0], -32.0 * scale[1])
    Curveto_r(6.0 * scale[0], -14.0 * scale[1], 10.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], 17.0 * scale[1])
    Curveto_r(11.0 * scale[0], 35.0 * scale[1], 9.0 * scale[0],
              49.0 * scale[1], -3.0 * scale[0], 19.0 * scale[1])
    te.end_fill()
    Moveto(902.0 * scale[0], 856.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -8.0 * scale[1], 15.0 * scale[0], -
              12.0 * scale[1], 17.0 * scale[0], -11.0 * scale[1])
    Curveto_r(5.0 * scale[0], 6.0 * scale[1], -10.0 * scale[0],
              25.0 * scale[1], -20.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              6.0 * scale[1], 3.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(775.0 * scale[0], 800.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 * scale[0], -
              13.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(10.0 * scale[0], -4.0 * scale[1], 15.0 * scale[0], -
              14.0 * scale[1], 12.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -12.0 * scale[1], 0.0 * scale[0], -
              19.0 * scale[1], 8.0 * scale[0], -19.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              7.0 * scale[1], 2.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 35.0 * scale[1], -21.0 * scale[0],
              43.0 * scale[1], -32.0 * scale[0], 25.0 * scale[1])
    te.end_fill()
    Moveto(836.0 * scale[0], 767.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0], -
              15.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 0.0 * scale[0],
              11.0 * scale[1], -7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              8.0 * scale[1], -5.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(898.0 * scale[0], 773.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 12.0 * scale[0], -
              11.0 * scale[1], 12.0 * scale[0], -19.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(14.0 * scale[0], 9.0 * scale[1], 0.0 * scale[0],
              35.0 * scale[1], -19.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 0.0 * scale[1], -11.0 *
              scale[0], -2.0 * scale[1], -3.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(3.0 * scale[0], 703.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -17.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 7.0 * scale[0], -13.0 * scale[1])
    Curveto_r(7.0 * scale[0], 11.0 * scale[1], 11.0 * scale[0],
              11.0 * scale[1], 23.0 * scale[0], 1.0 * scale[1])
    Curveto_r(11.0 * scale[0], -9.0 * scale[1], 17.0 *
              scale[0], -9.0 * scale[1], 22.0 * scale[0], -1.0 * scale[1])
    Curveto_r(7.0 * scale[0], 11.0 * scale[1], -21.0 * scale[0],
              39.0 * scale[1], -40.0 * scale[0], 40.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              12.0 * scale[1], -12.0 * scale[0], -27.0 * scale[1])
    te.end_fill()
    Moveto(885.0 * scale[0], 710.0 * scale[1], x, y)
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
    Moveto(68.0 * scale[0], 698.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -27.0 * scale[1], 100.0 * scale[0], -
              103.0 * scale[1], 119.0 * scale[0], -84.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -7.0 * scale[0],
              8.0 * scale[1], -22.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 4.0 * scale[1], -37.0 * scale[0],
              16.0 * scale[1], -48.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 16.0 * scale[1], -18.0 * scale[0],
              23.0 * scale[1], -8.0 * scale[0], 38.0 * scale[1])
    Curveto_r(10.0 * scale[0], 17.0 * scale[1], 8.0 * scale[0],
              19.0 * scale[1], -13.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -26.0 * scale[0], -
              6.0 * scale[1], -28.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(750.0 * scale[0], 680.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -4.0 * scale[0], -
              8.0 * scale[1], -10.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 9.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], 5.0 * scale[0], -21.0 * scale[1])
    Curveto_r(8.0 * scale[0], -9.0 * scale[1], 19.0 * scale[0], -
              13.0 * scale[1], 24.0 * scale[0], -10.0 * scale[1])
    Curveto_r(5.0 * scale[0], 4.0 * scale[1], 11.0 * scale[0],
              0.0 * scale[1], 14.0 * scale[0], -6.0 * scale[1])
    Curveto_r(2.0 * scale[0], -7.0 * scale[1], 7.0 * scale[0], -
              11.0 * scale[1], 10.0 * scale[0], -8.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -6.0 * scale[0],
              18.0 * scale[1], -19.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 15.0 * scale[1], -24.0 * scale[0],
              23.0 * scale[1], -24.0 * scale[0], 17.0 * scale[1])
    te.end_fill()
    Moveto(50.0 * scale[0], 630.0 * scale[1], x, y)
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
    Moveto(230.0 * scale[0], 578.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 7.0 * scale[0], -
              19.0 * scale[1], 16.0 * scale[0], -22.0 * scale[1])
    Curveto_r(15.0 * scale[0], -6.0 * scale[1], 15.0 *
              scale[0], -4.0 * scale[1], 3.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 10.0 * scale[1], -15.0 * scale[0],
              20.0 * scale[1], -16.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 2.0 * scale[1], -3.0 * scale[0], -
              3.0 * scale[1], -3.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(56.0 * scale[0], 564.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -9.0 * scale[1], -4.0 * scale[0], -
              19.0 * scale[1], -1.0 * scale[0], -22.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 5.0 * scale[0],
              0.0 * scale[1], 5.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], 5.0 * scale[0],
              9.0 * scale[1], 10.0 * scale[0], 6.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 10.0 *
              scale[0], -2.0 * scale[1], 10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 18.0 * scale[1], -18.0 * scale[0],
              21.0 * scale[1], -24.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(5.0 * scale[0], 560.0 * scale[1], x, y)
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
    Moveto(94.0 * scale[0], 553.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -13.0 * scale[1], 0.0 * scale[0], -
              23.0 * scale[1], -5.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -11.0 *
              scale[0], -24.0 * scale[1], 6.0 * scale[0], -46.0 * scale[1])
    Curveto_r(14.0 * scale[0], -18.0 * scale[1], 14.0 *
              scale[0], -18.0 * scale[1], 15.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], -4.0 * scale[0],
              20.0 * scale[1], -10.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -8.0 * scale[1], -13.0 * scale[0],
              8.0 * scale[1], -1.0 * scale[0], 21.0 * scale[1])
    Curveto_r(5.0 * scale[0], 5.0 * scale[1], 5.0 * scale[0],
              17.0 * scale[1], 0.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 18.0 * scale[1], -9.0 * scale[0],
              18.0 * scale[1], -5.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(140.0 * scale[0], 532.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 11.0 * scale[0], -
              14.0 * scale[1], 25.0 * scale[0], -20.0 * scale[1])
    Curveto_r(21.0 * scale[0], -10.0 * scale[1], 25.0 * scale[0], -
              19.0 * scale[1], 25.0 * scale[0], -51.0 * scale[1])
    Curveto_r(0.0 * scale[0], -23.0 * scale[1], -7.0 * scale[0], -
              46.0 * scale[1], -16.0 * scale[0], -56.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -9.0 * scale[1], -14.0 * scale[0], -
              18.0 * scale[1], -11.0 * scale[0], -21.0 * scale[1])
    Curveto_r(13.0 * scale[0], -14.0 * scale[1], 37.0 * scale[0],
              31.0 * scale[1], 37.0 * scale[0], 71.0 * scale[1])
    Curveto_r(0.0 * scale[0], 37.0 * scale[1], -5.0 * scale[0],
              47.0 * scale[1], -30.0 * scale[0], 65.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 12.0 * scale[1], -30.0 * scale[0],
              17.0 * scale[1], -30.0 * scale[0], 12.0 * scale[1])
    te.end_fill()
    Moveto(4.0 * scale[0], 523.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(10.0 * scale[0], -11.0 * scale[1], 37.0 *
              scale[0], -12.0 * scale[1], 30.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], -12.0 * scale[0],
              9.0 * scale[1], -21.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -13.0 *
              scale[0], -3.0 * scale[1], -9.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(121.0 * scale[0], 441.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              11.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 9.0 * scale[0], -
              11.0 * scale[1], 6.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              11.0 * scale[1], 5.0 * scale[0], -15.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 8.0 * scale[0], -
              11.0 * scale[1], 5.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -5.0 * scale[1], -1.0 *
              scale[0], -9.0 * scale[1], 4.0 * scale[0], -9.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0],
              17.0 * scale[1], 2.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 4.0 * scale[1], -8.0 * scale[0],
              17.0 * scale[1], -6.0 * scale[0], 31.0 * scale[1])
    Curveto_r(1.0 * scale[0], 14.0 * scale[1], 2.0 * scale[0],
              25.0 * scale[1], 1.0 * scale[0], 25.0 * scale[1])
    Curveto_r(0.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              4.0 * scale[1], -15.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(48.0 * scale[0], 352.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -2.0 * scale[1], -18.0 * scale[0], -
              12.0 * scale[1], -18.0 * scale[0], -23.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], -4.0 * scale[0], -
              19.0 * scale[1], -9.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -19.0 * scale[0], -
              139.0 * scale[1], -6.0 * scale[0], -144.0 * scale[1])
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 6.0 * scale[0], -
              7.0 * scale[1], 0.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -12.0 * scale[1], -11.0 *
              scale[0], -63.0 * scale[1], 5.0 * scale[0], -74.0 * scale[1])
    Curveto_r(9.0 * scale[0], -5.0 * scale[1], 10.0 *
              scale[0], -9.0 * scale[1], 3.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 0.0 * scale[1], -3.0 * scale[0], -
              39.0 * scale[1], 18.0 * scale[0], -51.0 * scale[1])
    Curveto_r(29.0 * scale[0], -15.0 * scale[1], 179.0 * scale[0], -
              24.0 * scale[1], 179.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -18.0 * scale[0],
              16.0 * scale[1], -40.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 6.0 * scale[1], -42.0 * scale[0],
              15.0 * scale[1], -45.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 5.0 * scale[1], -3.0 * scale[0],
              9.0 * scale[1], 2.0 * scale[0], 8.0 * scale[1])
    Curveto_r(21.0 * scale[0], -4.0 * scale[1], 30.0 * scale[0],
              4.0 * scale[1], 42.0 * scale[0], 36.0 * scale[1])
    Curveto_r(7.0 * scale[0], 19.0 * scale[1], 9.0 * scale[0],
              40.0 * scale[1], 5.0 * scale[0], 46.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], 0.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 20.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 9.0 * scale[0],
              9.0 * scale[1], 3.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0],
              21.0 * scale[1], -19.0 * scale[0], 48.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 26.0 * scale[1], -12.0 * scale[0],
              54.0 * scale[1], -19.0 * scale[0], 62.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 21.0 * scale[1], -31.0 * scale[0],
              59.0 * scale[1], -16.0 * scale[0], 44.0 * scale[1])
    Curveto_r(8.0 * scale[0], -8.0 * scale[1], 24.0 * scale[0], -
              9.0 * scale[1], 47.0 * scale[0], -4.0 * scale[1])
    Curveto_r(45.0 * scale[0], 10.0 * scale[1], 54.0 * scale[0],
              20.0 * scale[1], 19.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 0.0 * scale[1], -25.0 * scale[0],
              4.0 * scale[1], -21.0 * scale[0], 11.0 * scale[1])
    Curveto_r(6.0 * scale[0], 9.0 * scale[1], -87.0 * scale[0],
              10.0 * scale[1], -137.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto_r(82.0 * scale[0], -52.0 * scale[1], 0, 0)
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
    Moveto(575.0 * scale[0], 340.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 12.0 * scale[0], -
              10.0 * scale[1], 20.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0],
              5.0 * scale[1], 20.0 * scale[0], 10.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              10.0 * scale[1], -20.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 0.0 * scale[1], -24.0 * scale[0], -
              4.0 * scale[1], -20.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(730.0 * scale[0], 332.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(19.0 * scale[0], -9.0 * scale[1], 37.0 * scale[0], -
              20.0 * scale[1], 38.0 * scale[0], -25.0 * scale[1])
    Curveto_r(2.0 * scale[0], -4.0 * scale[1], 8.0 * scale[0], -
              5.0 * scale[1], 13.0 * scale[0], -1.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 9.0 * scale[0],
              0.0 * scale[1], 9.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -6.0 * scale[0], -
              11.0 * scale[1], -13.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -112.0 * scale[0],
              25.0 * scale[1], -139.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 4.0 * scale[1], -18.0 * scale[0],
              3.0 * scale[1], -18.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              9.0 * scale[1], 8.0 * scale[0], -6.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 19.0 * scale[0], -
              1.0 * scale[1], 33.0 * scale[0], -7.0 * scale[1])
    Curveto_r(13.0 * scale[0], -7.0 * scale[1], 42.0 * scale[0], -
              19.0 * scale[1], 64.0 * scale[0], -26.0 * scale[1])
    Curveto_r(29.0 * scale[0], -9.0 * scale[1], 41.0 * scale[0], -
              19.0 * scale[1], 42.0 * scale[0], -33.0 * scale[1])
    Curveto_r(2.0 * scale[0], -15.0 * scale[1], -2.0 * scale[0], -
              18.0 * scale[1], -15.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 7.0 * scale[1], -118.0 * scale[0],
              25.0 * scale[1], -140.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              4.0 * scale[1], -7.0 * scale[0], -10.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 23.0 * scale[0], -
              10.0 * scale[1], 44.0 * scale[0], -10.0 * scale[1])
    Curveto_r(21.0 * scale[0], 0.0 * scale[1], 59.0 * scale[0], -
              7.0 * scale[1], 86.0 * scale[0], -16.0 * scale[1])
    Lineto_r(48.0 * scale[0], -17.0 * scale[1])
    Lineto_r(-23.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -10.0 * scale[1], -18.0 *
              scale[0], -19.0 * scale[1], -12.0 * scale[0], -21.0 * scale[1])
    Curveto_r(5.0 * scale[0], -2.0 * scale[1], 12.0 * scale[0], -
              13.0 * scale[1], 14.0 * scale[0], -24.0 * scale[1])
    Curveto_r(3.0 * scale[0], -18.0 * scale[1], -2.0 * scale[0], -
              20.0 * scale[1], -52.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 1.0 * scale[1], -47.0 * scale[0],
              0.0 * scale[1], -37.0 * scale[0], -3.0 * scale[1])
    Curveto_r(9.0 * scale[0], -3.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 12.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -5.0 * scale[1], 2.0 * scale[0], -
              8.0 * scale[1], 12.0 * scale[0], -7.0 * scale[1])
    Curveto_r(45.0 * scale[0], 3.0 * scale[1], 65.0 * scale[0], -
              2.0 * scale[1], 59.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -13.0 * scale[1], 10.0 * scale[0], -
              20.0 * scale[1], 37.0 * scale[0], -16.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0], -
              4.0 * scale[1], 7.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 7.0 * scale[0], -
              9.0 * scale[1], 15.0 * scale[0], -6.0 * scale[1])
    Curveto_r(8.0 * scale[0], 4.0 * scale[1], 17.0 * scale[0],
              2.0 * scale[1], 20.0 * scale[0], -3.0 * scale[1])
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 3.0 * scale[0], -
              10.0 * scale[1], -2.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-72.0 * scale[0], -5.0 * scale[1], -110.0 *
              scale[0], -17.0 * scale[1], -67.0 * scale[0], -21.0 * scale[1])
    Curveto_r(10.0 * scale[0], -1.0 * scale[1], -6.0 * scale[0], -
              4.0 * scale[1], -36.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-45.0 * scale[0], -6.0 * scale[1], -37.0 *
              scale[0], -7.0 * scale[1], 45.0 * scale[0], -7.0 * scale[1])
    Curveto_r(82.0 * scale[0], 1.0 * scale[1], 183.0 * scale[0],
              11.0 * scale[1], 152.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -1.0 * scale[0],
              8.0 * scale[1], 7.0 * scale[0], 17.0 * scale[1])
    Curveto_r(16.0 * scale[0], 16.0 * scale[1], 12.0 * scale[0],
              39.0 * scale[1], -5.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -4.0 * scale[1], -9.0 *
              scale[0], -2.0 * scale[1], -9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 5.0 * scale[0],
              11.0 * scale[1], 11.0 * scale[0], 13.0 * scale[1])
    Curveto_r(15.0 * scale[0], 5.0 * scale[1], 20.0 * scale[0],
              70.0 * scale[1], 10.0 * scale[0], 123.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 25.0 * scale[1], -6.0 * scale[0],
              47.0 * scale[1], -3.0 * scale[0], 50.0 * scale[1])
    Curveto_r(9.0 * scale[0], 9.0 * scale[1], 9.0 * scale[0],
              45.0 * scale[1], 1.0 * scale[0], 51.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 2.0 * scale[1], -6.0 * scale[0],
              11.0 * scale[1], -2.0 * scale[0], 19.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], 1.0 * scale[0],
              15.0 * scale[1], -5.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              5.0 * scale[1], -14.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -7.0 * scale[1], -21.0 *
              scale[0], -5.0 * scale[1], -53.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-28.0 * scale[0], 8.0 * scale[1], -77.0 * scale[0],
              15.0 * scale[1], -110.0 * scale[0], 14.0 * scale[1])
    Lineto_r(-60.0 * scale[0], 0.0 * scale[1])
    Lineto_r(35.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto_r(177.0 * scale[0], -88.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 17.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(-7.0 * scale[0], -29.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], -7.0 * scale[0], -
              5.0 * scale[1], -15.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -3.0 * scale[1], -15.0 * scale[0],
              0.0 * scale[1], -15.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], 6.0 * scale[0],
              12.0 * scale[1], 15.0 * scale[0], 9.0 * scale[1])
    Curveto_r(8.0 * scale[0], -4.0 * scale[1], 15.0 * scale[0], -
              7.0 * scale[1], 15.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto_r(28.0 * scale[0], -80.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -14.0 * scale[1], -6.0 * scale[0], -
              25.0 * scale[1], -10.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0],
              11.0 * scale[1], -6.0 * scale[0], 25.0 * scale[1])
    Curveto_r(1.0 * scale[0], 14.0 * scale[1], 6.0 * scale[0],
              25.0 * scale[1], 10.0 * scale[0], 25.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0], -
              11.0 * scale[1], 6.0 * scale[0], -25.0 * scale[1])
    te.end_fill()
    Moveto_r(-25.0 * scale[0], -62.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              5.0 * scale[1], 12.0 * scale[0], 5.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(4.0 * scale[0], -49.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 17.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(427.0 * scale[0], 315.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-44.0 * scale[0], -15.0 * scale[1], -66.0 *
              scale[0], -40.0 * scale[1], -67.0 * scale[0], -73.0 * scale[1])
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], -5.0 * scale[0], -
              31.0 * scale[1], -11.0 * scale[0], -41.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -14.0 * scale[1], -8.0 *
              scale[0], -25.0 * scale[1], 4.0 * scale[0], -49.0 * scale[1])
    Curveto_r(18.0 * scale[0], -37.0 * scale[1], 10.0 * scale[0], -
              47.0 * scale[1], -38.0 * scale[0], -47.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 0.0 * scale[1], -30.0 * scale[0], -
              4.0 * scale[1], -29.0 * scale[0], -22.0 * scale[1])
    Curveto_r(0.0 * scale[0], -21.0 * scale[1], -3.0 * scale[0], -
              22.0 * scale[1], -40.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 4.0 * scale[1], -22.0 * scale[0],
              0.0 * scale[1], 29.0 * scale[0], -15.0 * scale[1])
    Curveto_r(39.0 * scale[0], -12.0 * scale[1], 80.0 * scale[0], -
              22.0 * scale[1], 93.0 * scale[0], -22.0 * scale[1])
    Curveto_r(18.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0], -
              3.0 * scale[1], 12.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -11.0 * scale[1], -5.0 * scale[0], -
              14.0 * scale[1], 19.0 * scale[0], -13.0 * scale[1])
    Curveto_r(16.0 * scale[0], 1.0 * scale[1], 32.0 * scale[0],
              6.0 * scale[1], 35.0 * scale[0], 13.0 * scale[1])
    Curveto_r(9.0 * scale[0], 23.0 * scale[1], 77.0 * scale[0],
              26.0 * scale[1], 112.0 * scale[0], 5.0 * scale[1])
    Curveto_r(27.0 * scale[0], -17.0 * scale[1], 33.0 *
              scale[0], -18.0 * scale[1], 44.0 * scale[0], -6.0 * scale[1])
    Curveto_r(6.0 * scale[0], 9.0 * scale[1], 12.0 * scale[0],
              37.0 * scale[1], 13.0 * scale[0], 63.0 * scale[1])
    Curveto_r(2.0 * scale[0], 42.0 * scale[1], 5.0 * scale[0],
              49.0 * scale[1], 27.0 * scale[0], 55.0 * scale[1])
    Curveto_r(20.0 * scale[0], 6.0 * scale[1], 18.0 * scale[0],
              7.0 * scale[1], -11.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-30.0 * scale[0], -2.0 * scale[1], -35.0 * scale[0],
              0.0 * scale[1], -31.0 * scale[0], 15.0 * scale[1])
    Curveto_r(4.0 * scale[0], 15.0 * scale[1], 17.0 * scale[0],
              18.0 * scale[1], 76.0 * scale[0], 20.0 * scale[1])
    Lineto_r(71.0 * scale[0], 2.0 * scale[1])
    Lineto_r(-67.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-64.0 * scale[0], 4.0 * scale[1], -82.0 * scale[0],
              13.0 * scale[1], -57.0 * scale[0], 29.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 6.0 * scale[0],
              10.0 * scale[1], -5.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 5.0 * scale[1], -16.0 * scale[0],
              17.0 * scale[1], -16.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 57.0 * scale[1], -89.0 * scale[0],
              93.0 * scale[1], -163.0 * scale[0], 67.0 * scale[1])
    te.end_fill()
    Moveto(210.0 * scale[0], 299.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -5.0 * scale[1], -14.0 *
              scale[0], -7.0 * scale[1], 23.0 * scale[0], -8.0 * scale[1])
    Curveto_r(26.0 * scale[0], -1.0 * scale[1], 47.0 * scale[0],
              1.0 * scale[1], 47.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -46.0 * scale[0],
              12.0 * scale[1], -70.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(338.0 * scale[0], 303.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(590.0 * scale[0], 290.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 7.0 * scale[0], -
              10.0 * scale[1], 15.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              2.0 * scale[1], 15.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 2.0 * scale[1], -7.0 * scale[0],
              6.0 * scale[1], -15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -15.0 * scale[0],
              1.0 * scale[1], -15.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(653.0 * scale[0], 273.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(715.0 * scale[0], 260.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(27.0 * scale[0], -12.0 * scale[1], 43.0 *
              scale[0], -12.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -22.0 * scale[0],
              9.0 * scale[1], -30.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 0.0 * scale[1], -8.0 *
              scale[0], -3.0 * scale[1], 5.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(673.0 * scale[0], 83.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(600.0 * scale[0], 10.0 * scale[1], x, y)
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
    Moveto(298.0 * scale[0], 3.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#6e9c87')
    te.end_fill()
    Moveto(482.0 * scale[0], 970.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 2.0 * scale[0], -
              27.0 * scale[1], 5.0 * scale[0], -17.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              25.0 * scale[1], 0.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(506.0 * scale[0], 955.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -11.0 * scale[1], -10.0 * scale[0], -
              83.0 * scale[1], -11.0 * scale[0], -160.0 * scale[1])
    Lineto_r(-2.0 * scale[0], -140.0 * scale[1])
    Lineto_r(6.0 * scale[0], 120.0 * scale[1])
    Curveto_r(3.0 * scale[0], 66.0 * scale[1], 9.0 * scale[0],
              112.0 * scale[1], 13.0 * scale[0], 103.0 * scale[1])
    Curveto_r(4.0 * scale[0], -10.0 * scale[1], 12.0 * scale[0], -
              18.0 * scale[1], 18.0 * scale[0], -18.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0],
              5.0 * scale[1], 5.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], -2.0 * scale[0],
              17.0 * scale[1], 4.0 * scale[0], 24.0 * scale[1])
    Curveto_r(9.0 * scale[0], 11.0 * scale[1], 8.0 * scale[0],
              17.0 * scale[1], -3.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 8.0 * scale[1], -16.0 * scale[0],
              23.0 * scale[1], -18.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 18.0 * scale[1], -4.0 * scale[0],
              18.0 * scale[1], -12.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(531.0 * scale[0], 843.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -6.0 * scale[1], -4.0 * scale[0], -
              20.0 * scale[1], -7.0 * scale[0], -30.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -17.0 * scale[1], -5.0 *
              scale[0], -17.0 * scale[1], 6.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 10.0 * scale[1], 9.0 * scale[0],
              23.0 * scale[1], 6.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -5.0 * scale[0],
              9.0 * scale[1], -5.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(563.0 * scale[0], 775.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              15.0 * scale[1], 9.0 * scale[0], -15.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0],
              7.0 * scale[1], 8.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -4.0 * scale[0],
              15.0 * scale[1], -8.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              7.0 * scale[1], -9.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(270.0 * scale[0], 700.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -5.0 * scale[1], -12.0 * scale[0], -
              11.0 * scale[1], -10.0 * scale[0], -14.0 * scale[1])
    Curveto_r(3.0 * scale[0], -2.0 * scale[1], 14.0 * scale[0],
              2.0 * scale[1], 24.0 * scale[0], 10.0 * scale[1])
    Curveto_r(22.0 * scale[0], 15.0 * scale[1], 10.0 * scale[0],
              19.0 * scale[1], -14.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(347.0 * scale[0], 699.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(285.0 * scale[0], 680.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], 3.0 * scale[0], -
              10.0 * scale[1], 14.0 * scale[0], -10.0 * scale[1])
    Curveto_r(25.0 * scale[0], 0.0 * scale[1], 27.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 4.0 * scale[1], -17.0 * scale[0],
              2.0 * scale[1], -20.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(541.0 * scale[0], 674.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(662.0 * scale[0], 665.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(295.0 * scale[0], 648.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(11.0 * scale[0], -6.0 * scale[1], 24.0 * scale[0], -
              16.0 * scale[1], 28.0 * scale[0], -22.0 * scale[1])
    Curveto_r(5.0 * scale[0], -7.0 * scale[1], 6.0 *
              scale[0], -4.0 * scale[1], 3.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 10.0 * scale[1], -6.0 * scale[0],
              21.0 * scale[1], -6.0 * scale[0], 23.0 * scale[1])
    Curveto_r(0.0 * scale[0], 2.0 * scale[1], -10.0 * scale[0],
              4.0 * scale[1], -22.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-22.0 * scale[0], -1.0 * scale[1], -22.0 *
              scale[0], -1.0 * scale[1], -3.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(525.0 * scale[0], 640.0 * scale[1], x, y)
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
    Moveto(535.0 * scale[0], 620.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -11.0 * scale[1], -16.0 *
              scale[0], -22.0 * scale[1], -14.0 * scale[0], -24.0 * scale[1])
    Curveto_r(2.0 * scale[0], -2.0 * scale[1], 12.0 * scale[0],
              7.0 * scale[1], 22.0 * scale[0], 20.0 * scale[1])
    Curveto_r(22.0 * scale[0], 29.0 * scale[1], 17.0 * scale[0],
              32.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(710.0 * scale[0], 626.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(493.0 * scale[0], 585.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -9.0 * scale[1], -2.0 * scale[0], -
              39.0 * scale[1], 2.0 * scale[0], -68.0 * scale[1])
    Curveto_r(4.0 * scale[0], -29.0 * scale[1], 6.0 * scale[0], -
              73.0 * scale[1], 6.0 * scale[0], -99.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -27.0 * scale[1], 0.0 * scale[0], -
              48.0 * scale[1], 1.0 * scale[0], -48.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 18.0 * scale[0],
              4.0 * scale[1], 35.0 * scale[0], 9.0 * scale[1])
    Curveto_r(20.0 * scale[0], 6.0 * scale[1], 35.0 * scale[0],
              6.0 * scale[1], 38.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], -14.0 * scale[1], 53.0 *
              scale[0], -11.0 * scale[1], 91.0 * scale[0], 7.0 * scale[1])
    Curveto_r(30.0 * scale[0], 14.0 * scale[1], 36.0 * scale[0],
              14.0 * scale[1], 64.0 * scale[0], 0.0 * scale[1])
    Curveto_r(35.0 * scale[0], -17.0 * scale[1], 220.0 *
              scale[0], -21.0 * scale[1], 220.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -4.0 * scale[0],
              9.0 * scale[1], -10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0],
              5.0 * scale[1], -10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 9.0 * scale[0],
              10.0 * scale[1], 20.0 * scale[0], 10.0 * scale[1])
    Curveto_r(18.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0],
              7.0 * scale[1], 20.0 * scale[0], 82.0 * scale[1])
    Curveto_r(0.0 * scale[0], 76.0 * scale[1], -7.0 * scale[0],
              104.0 * scale[1], -12.0 * scale[0], 46.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -17.0 * scale[1], -7.0 * scale[0], -
              24.0 * scale[1], -16.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 4.0 * scale[1], -11.0 * scale[0],
              6.0 * scale[1], 0.0 * scale[0], 13.0 * scale[1])
    Curveto_r(11.0 * scale[0], 7.0 * scale[1], 11.0 * scale[0],
              9.0 * scale[1], -1.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0],
              6.0 * scale[1], -7.0 * scale[0], 15.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], 0.0 * scale[0],
              15.0 * scale[1], -5.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              9.0 * scale[1], -6.0 * scale[0], -20.0 * scale[1])
    Curveto_r(7.0 * scale[0], -28.0 * scale[1], -9.0 * scale[0], -
              25.0 * scale[1], -29.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 14.0 * scale[1], -19.0 * scale[0],
              23.0 * scale[1], -22.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], 1.0 * scale[0], -
              12.0 * scale[1], 8.0 * scale[0], -21.0 * scale[1])
    Curveto_r(7.0 * scale[0], -9.0 * scale[1], 11.0 * scale[0], -
              17.0 * scale[1], 9.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -1.0 * scale[1], -15.0 * scale[0], -
              10.0 * scale[1], -29.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -9.0 * scale[1], -18.0 * scale[0], -
              17.0 * scale[1], -11.0 * scale[0], -17.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 23.0 * scale[0],
              8.0 * scale[1], 33.0 * scale[0], 17.0 * scale[1])
    Curveto_r(15.0 * scale[0], 14.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 27.0 * scale[0], 4.0 * scale[1])
    Curveto_r(5.0 * scale[0], -7.0 * scale[1], 12.0 * scale[0], -
              13.0 * scale[1], 17.0 * scale[0], -13.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0], -
              4.0 * scale[1], 6.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -5.0 * scale[1], 3.0 *
              scale[0], -9.0 * scale[1], 9.0 * scale[0], -9.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0], -
              10.0 * scale[1], 7.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -13.0 * scale[1], -1.0 *
              scale[0], -22.0 * scale[1], 3.0 * scale[0], -19.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 9.0 * scale[0], -
              2.0 * scale[1], 9.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], -6.0 * scale[0], -
              13.0 * scale[1], -13.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -18.0 * scale[0], -
              6.0 * scale[1], -25.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -30.0 * scale[1], -32.0 *
              scale[0], -33.0 * scale[1], -39.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 11.0 * scale[1], -9.0 * scale[0],
              20.0 * scale[1], -14.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0],
              5.0 * scale[1], -9.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 5.0 * scale[0],
              7.0 * scale[1], 12.0 * scale[0], 3.0 * scale[1])
    Curveto_r(7.0 * scale[0], -4.0 * scale[1], 8.0 *
              scale[0], -3.0 * scale[1], 4.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], -12.0 * scale[0],
              9.0 * scale[1], -17.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -3.0 * scale[1], -9.0 * scale[0],
              2.0 * scale[1], -7.0 * scale[0], 12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 13.0 * scale[1], -3.0 * scale[0],
              19.0 * scale[1], -14.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -1.0 * scale[1], -18.0 * scale[0],
              2.0 * scale[1], -18.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -6.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -1.0 * scale[1], -3.0 * scale[0], -
              9.0 * scale[1], 10.0 * scale[0], -19.0 * scale[1])
    Curveto_r(27.0 * scale[0], -23.0 * scale[1], 27.0 *
              scale[0], -27.0 * scale[1], 2.0 * scale[0], -34.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -3.0 * scale[1], -20.0 * scale[0],
              0.0 * scale[1], -20.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -5.0 * scale[0],
              5.0 * scale[1], -10.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -8.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -10.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -11.0 * scale[0],
              16.0 * scale[1], -25.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -25.0 * scale[0],
              18.0 * scale[1], -25.0 * scale[0], 27.0 * scale[1])
    Curveto_r(0.0 * scale[0], 18.0 * scale[1], 3.0 * scale[0],
              18.0 * scale[1], -59.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-39.0 * scale[0], -8.0 * scale[1], -55.0 *
              scale[0], -7.0 * scale[1], -78.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 7.0 * scale[1], -36.0 * scale[0],
              12.0 * scale[1], -45.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -3.0 * scale[1], -18.0 * scale[0],
              2.0 * scale[1], -18.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 15.0 * scale[1], -2.0 * scale[0],
              16.0 * scale[1], -10.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -12.0 * scale[1], -10.0 *
              scale[0], -11.0 * scale[1], -10.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], -3.0 * scale[0],
              29.0 * scale[1], -7.0 * scale[0], 39.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 12.0 * scale[1], -3.0 * scale[0],
              15.0 * scale[1], 5.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -5.0 * scale[1], 10.0 *
              scale[0], -2.0 * scale[1], 6.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 20.0 * scale[1], -13.0 * scale[0],
              20.0 * scale[1], -21.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(620.0 * scale[0], 580.0 * scale[1], x, y)
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
    Moveto(647.0 * scale[0], 585.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -8.0 * scale[1], -3.0 * scale[0], -
              16.0 * scale[1], 1.0 * scale[0], -19.0 * scale[1])
    Curveto_r(4.0 * scale[0], -3.0 * scale[1], 9.0 * scale[0],
              4.0 * scale[1], 9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(2.0 * scale[0], 23.0 * scale[1], -3.0 * scale[0],
              25.0 * scale[1], -10.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(808.0 * scale[0], 573.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(433.0 * scale[0], 523.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 0.0 * scale[0], -
              14.0 * scale[1], -8.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -5.0 * scale[1], -14.0 *
              scale[0], -8.0 * scale[1], 1.0 * scale[0], -31.0 * scale[1])
    Curveto_r(16.0 * scale[0], -24.0 * scale[1], 35.0 *
              scale[0], -26.0 * scale[1], 33.0 * scale[0], -2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -2.0 * scale[0],
              8.0 * scale[1], -6.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -10.0 * scale[1], -8.0 *
              scale[0], -9.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 14.0 * scale[1], -10.0 * scale[0],
              19.0 * scale[1], 3.0 * scale[0], 29.0 * scale[1])
    Curveto_r(12.0 * scale[0], 9.0 * scale[1], 12.0 * scale[0],
              13.0 * scale[1], 2.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -11.0 * scale[0],
              4.0 * scale[1], -7.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(685.0 * scale[0], 380.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 10.0 * scale[0], -
              10.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              5.0 * scale[1], 9.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -7.0 * scale[0],
              10.0 * scale[1], -16.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              4.0 * scale[1], -9.0 * scale[0], -10.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#596442')
    te.end_fill()
    Moveto(450.0 * scale[0], 1150.0 * scale[1], x, y)
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
    Moveto(348.0 * scale[0], 1043.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(558.0 * scale[0], 1043.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(743.0 * scale[0], 1033.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(26.0 * scale[0], -2.0 * scale[1], 68.0 *
              scale[0], -2.0 * scale[1], 95.0 * scale[0], 0.0 * scale[1])
    Curveto_r(26.0 * scale[0], 2.0 * scale[1], 4.0 * scale[0],
              3.0 * scale[1], -48.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-52.0 * scale[0], 0.0 * scale[1], -74.0 *
              scale[0], -1.0 * scale[1], -47.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(68.0 * scale[0], 1023.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 32.0 *
              scale[0], -2.0 * scale[1], 45.0 * scale[0], 0.0 * scale[1])
    Curveto_r(12.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              4.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 0.0 * scale[1], -35.0 *
              scale[0], -2.0 * scale[1], -22.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(188.0 * scale[0], 1023.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(29.0 * scale[0], -2.0 * scale[1], 74.0 *
              scale[0], -2.0 * scale[1], 100.0 * scale[0], 0.0 * scale[1])
    Curveto_r(26.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              3.0 * scale[1], -53.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-55.0 * scale[0], 0.0 * scale[1], -76.0 *
              scale[0], -1.0 * scale[1], -47.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(464.0 * scale[0], 910.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -69.0 * scale[1], 1.0 * scale[0], -
              97.0 * scale[1], 3.0 * scale[0], -62.0 * scale[1])
    Curveto_r(2.0 * scale[0], 34.0 * scale[1], 2.0 * scale[0],
              90.0 * scale[1], 0.0 * scale[0], 125.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 34.0 * scale[1], -3.0 * scale[0],
              6.0 * scale[1], -3.0 * scale[0], -63.0 * scale[1])
    te.end_fill()
    Moveto(36.0 * scale[0], 993.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(906.0 * scale[0], 986.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(20.0 * scale[0], -27.0 * scale[1], 37.0 * scale[0], -
              35.0 * scale[1], 28.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 7.0 * scale[1], -14.0 * scale[0],
              18.0 * scale[1], -25.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 13.0 * scale[1], -21.0 * scale[0],
              13.0 * scale[1], -3.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(70.0 * scale[0], 986.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 5.0 * scale[0], -
              18.0 * scale[1], 10.0 * scale[0], -21.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 10.0 * scale[0],
              1.0 * scale[1], 10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -4.0 * scale[0],
              18.0 * scale[1], -10.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0], -
              1.0 * scale[1], -10.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(512.0 * scale[0], 988.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -7.0 * scale[1], -12.0 * scale[0], -
              19.0 * scale[1], -12.0 * scale[0], -27.0 * scale[1])
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 1.0 * scale[0], -
              14.0 * scale[1], 10.0 * scale[0], -1.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 10.0 * scale[0],
              11.0 * scale[1], 10.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], 4.0 * scale[0], -
              23.0 * scale[1], 10.0 * scale[0], -23.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 6.0 * scale[0],
              9.0 * scale[1], 1.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 12.0 * scale[1], -6.0 * scale[0],
              28.0 * scale[1], -4.0 * scale[0], 35.0 * scale[1])
    Curveto_r(6.0 * scale[0], 15.0 * scale[1], 0.0 * scale[0],
              15.0 * scale[1], -15.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(640.0 * scale[0], 988.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 5.0 * scale[0], -
              20.0 * scale[1], 10.0 * scale[0], -23.0 * scale[1])
    Curveto_r(13.0 * scale[0], -8.0 * scale[1], 13.0 * scale[0],
              5.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 13.0 * scale[1], -10.0 * scale[0],
              13.0 * scale[1], -10.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(5.0 * scale[0], 970.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -14.0 * scale[1], 5.0 * scale[0], -
              34.0 * scale[1], 6.0 * scale[0], -45.0 * scale[1])
    Curveto_r(1.0 * scale[0], -16.0 * scale[1], 2.0 *
              scale[0], -15.0 * scale[1], 8.0 * scale[0], 5.0 * scale[1])
    Curveto_r(4.0 * scale[0], 14.0 * scale[1], 4.0 * scale[0],
              27.0 * scale[1], 1.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0],
              12.0 * scale[1], -14.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], -4.0 * scale[0],
              4.0 * scale[1], -1.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(580.0 * scale[0], 955.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -16.0 * scale[1], -2.0 * scale[0], -
              34.0 * scale[1], -1.0 * scale[0], -39.0 * scale[1])
    Curveto_r(1.0 * scale[0], -6.0 * scale[1], 5.0 * scale[0], -
              21.0 * scale[1], 7.0 * scale[0], -36.0 * scale[1])
    Curveto_r(5.0 * scale[0], -21.0 * scale[1], 2.0 * scale[0], -
              26.0 * scale[1], -18.0 * scale[0], -27.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0],
              1.0 * scale[1], -10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 12.0 * scale[0],
              10.0 * scale[1], 12.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -3.0 * scale[0],
              7.0 * scale[1], -7.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], -13.0 *
              scale[0], -1.0 * scale[1], -21.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 10.0 * scale[1], -15.0 * scale[0],
              9.0 * scale[1], -9.0 * scale[0], -6.0 * scale[1])
    Curveto_r(4.0 * scale[0], -10.0 * scale[1], 7.0 * scale[0], -
              25.0 * scale[1], 7.0 * scale[0], -33.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 9.0 * scale[0], -9.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 12.0 * scale[0],
              1.0 * scale[1], 16.0 * scale[0], -5.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 2.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              13.0 * scale[1], -14.0 * scale[0], -30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -16.0 * scale[1], -1.0 *
              scale[0], -30.0 * scale[1], 3.0 * scale[0], -30.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 6.0 * scale[0], -
              8.0 * scale[1], 3.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -15.0 * scale[1], -4.0 *
              scale[0], -16.0 * scale[1], 5.0 * scale[0], -3.0 * scale[1])
    Curveto_r(9.0 * scale[0], 12.0 * scale[1], 11.0 * scale[0],
              13.0 * scale[1], 11.0 * scale[0], 1.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 3.0 * scale[0], -
              11.0 * scale[1], 7.0 * scale[0], -8.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], 12.0 * scale[0],
              2.0 * scale[1], 19.0 * scale[0], -4.0 * scale[1])
    Curveto_r(8.0 * scale[0], -6.0 * scale[1], 21.0 * scale[0], -
              9.0 * scale[1], 29.0 * scale[0], -5.0 * scale[1])
    Curveto_r(10.0 * scale[0], 3.0 * scale[1], 23.0 * scale[0], -
              8.0 * scale[1], 40.0 * scale[0], -32.0 * scale[1])
    Curveto_r(14.0 * scale[0], -20.0 * scale[1], 25.0 * scale[0], -
              33.0 * scale[1], 25.0 * scale[0], -29.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], -7.0 * scale[0],
              19.0 * scale[1], -16.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 20.0 * scale[1], -14.0 * scale[0],
              23.0 * scale[1], -2.0 * scale[0], 19.0 * scale[1])
    Curveto_r(20.0 * scale[0], -8.0 * scale[1], 47.0 * scale[0],
              61.0 * scale[1], 37.0 * scale[0], 95.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 22.0 * scale[1], -7.0 * scale[0],
              20.0 * scale[1], -8.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -20.0 * scale[1], -5.0 * scale[0], -
              39.0 * scale[1], -10.0 * scale[0], -42.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -22.0 * scale[0],
              36.0 * scale[1], -19.0 * scale[0], 64.0 * scale[1])
    Curveto_r(1.0 * scale[0], 8.0 * scale[1], 0.0 * scale[0],
              34.0 * scale[1], 0.0 * scale[0], 58.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 51.0 * scale[1], -22.0 * scale[0],
              48.0 * scale[1], -22.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -36.0 * scale[1], -8.0 * scale[0], -
              42.0 * scale[1], -28.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 16.0 * scale[1], -15.0 * scale[0],
              28.0 * scale[1], 2.0 * scale[0], 28.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0],
              14.0 * scale[1], 19.0 * scale[0], 33.0 * scale[1])
    Curveto_r(4.0 * scale[0], 25.0 * scale[1], 0.0 * scale[0],
              36.0 * scale[1], -17.0 * scale[0], 49.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              16.0 * scale[1], -25.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -21.0 * scale[1], -4.0 *
              scale[0], -21.0 * scale[1], -12.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 25.0 * scale[1], -7.0 * scale[0],
              24.0 * scale[1], -9.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(30.0 * scale[0], -180.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -33.0 * scale[1], -1.0 * scale[0], -
              34.0 * scale[1], -25.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-29.0 * scale[0], 13.0 * scale[1], -32.0 * scale[0],
              33.0 * scale[1], -7.0 * scale[0], 47.0 * scale[1])
    Curveto_r(27.0 * scale[0], 16.0 * scale[1], 32.0 * scale[0],
              13.0 * scale[1], 32.0 * scale[0], -24.0 * scale[1])
    te.end_fill()
    Moveto(545.0 * scale[0], 961.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              12.0 * scale[1], 5.0 * scale[0], -16.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 10.0 * scale[0],
              1.0 * scale[1], 10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 18.0 * scale[1], -6.0 * scale[0],
              21.0 * scale[1], -15.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(106.0 * scale[0], 915.0 * scale[1], x, y)
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
    Moveto(491.0 * scale[0], 904.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(785.0 * scale[0], 890.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -13.0 * scale[1], 4.0 * scale[0], -
              32.0 * scale[1], 16.0 * scale[0], -25.0 * scale[1])
    Curveto_r(12.0 * scale[0], 8.0 * scale[1], 12.0 * scale[0],
              35.0 * scale[1], 0.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(680.0 * scale[0], 873.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], 5.0 * scale[0], -
              25.0 * scale[1], 10.0 * scale[0], -28.0 * scale[1])
    Curveto_r(13.0 * scale[0], -8.0 * scale[1], 13.0 * scale[0],
              15.0 * scale[1], 0.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 12.0 * scale[1], -10.0 * scale[0],
              11.0 * scale[1], -10.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(880.0 * scale[0], 880.0 * scale[1], x, y)
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
    Moveto(45.0 * scale[0], 870.0 * scale[1], x, y)
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
    Moveto(736.0 * scale[0], 855.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -26.0 * scale[1], -7.0 *
              scale[0], -32.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(6.0 * scale[0], 10.0 * scale[1], 9.0 * scale[0],
              21.0 * scale[1], 6.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 3.0 * scale[1], -7.0 * scale[0], -
              2.0 * scale[1], -11.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(827.0 * scale[0], 856.0 * scale[1], x, y)
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
    Moveto(70.0 * scale[0], 846.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(11.0 * scale[0], 784.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(391.0 * scale[0], 744.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(313.0 * scale[0], 737.0 * scale[1], x, y)
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
    Moveto(858.0 * scale[0], 724.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(11.0 * scale[0], -22.0 * scale[1], 42.0 * scale[0], -
              51.0 * scale[1], 42.0 * scale[0], -40.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], -12.0 * scale[0],
              19.0 * scale[1], -26.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 21.0 * scale[1], -24.0 * scale[0],
              22.0 * scale[1], -16.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(575.0 * scale[0], 720.0 * scale[1], x, y)
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
    Moveto(277.0 * scale[0], 692.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-22.0 * scale[0], -15.0 * scale[1], -25.0 *
              scale[0], -21.0 * scale[1], -14.0 * scale[0], -25.0 * scale[1])
    Curveto_r(9.0 * scale[0], -3.0 * scale[1], 18.0 * scale[0],
              1.0 * scale[1], 21.0 * scale[0], 8.0 * scale[1])
    Curveto_r(3.0 * scale[0], 9.0 * scale[1], 12.0 * scale[0],
              12.0 * scale[1], 22.0 * scale[0], 8.0 * scale[1])
    Curveto_r(16.0 * scale[0], -6.0 * scale[1], 16.0 * scale[0], -
              7.0 * scale[1], -2.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -7.0 * scale[1], -17.0 *
              scale[0], -8.0 * scale[1], -1.0 * scale[0], -8.0 * scale[1])
    Curveto_r(9.0 * scale[0], -1.0 * scale[1], 17.0 * scale[0], -
              6.0 * scale[1], 17.0 * scale[0], -12.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -7.0 * scale[0], -
              9.0 * scale[1], -15.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], 2.0 * scale[0], -
              17.0 * scale[1], 23.0 * scale[0], -44.0 * scale[1])
    Curveto_r(20.0 * scale[0], -27.0 * scale[1], 44.0 * scale[0], -
              49.0 * scale[1], 52.0 * scale[0], -50.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0], -
              1.0 * scale[1], 0.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -5.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -5.0 * scale[0], -10.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0], -
              26.0 * scale[1], 18.0 * scale[0], -122.0 * scale[1])
    Curveto_r(2.0 * scale[0], -34.0 * scale[1], 10.0 * scale[0], -
              35.0 * scale[1], 29.0 * scale[0], -5.0 * scale[1])
    Curveto_r(9.0 * scale[0], 13.0 * scale[1], 12.0 * scale[0],
              30.0 * scale[1], 8.0 * scale[0], 42.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 11.0 * scale[1], -5.0 * scale[0],
              25.0 * scale[1], -2.0 * scale[0], 30.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              7.0 * scale[1], -2.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -4.0 * scale[1], -14.0 *
              scale[0], -2.0 * scale[1], -21.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 9.0 * scale[1], -7.0 * scale[0],
              15.0 * scale[1], 9.0 * scale[0], 30.0 * scale[1])
    Curveto_r(12.0 * scale[0], 10.0 * scale[1], 15.0 * scale[0],
              16.0 * scale[1], 9.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-23.0 * scale[0], -11.0 * scale[1], -36.0 * scale[0],
              6.0 * scale[1], -16.0 * scale[0], 20.0 * scale[1])
    Curveto_r(10.0 * scale[0], 7.0 * scale[1], 15.0 * scale[0],
              17.0 * scale[1], 10.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 4.0 * scale[1], -7.0 * scale[0],
              2.0 * scale[1], -7.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -4.0 * scale[0], -
              9.0 * scale[1], -10.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0],
              19.0 * scale[1], -10.0 * scale[0], 35.0 * scale[1])
    Curveto_r(0.0 * scale[0], 19.0 * scale[1], -13.0 * scale[0],
              43.0 * scale[1], -42.0 * scale[0], 74.0 * scale[1])
    Lineto_r(-43.0 * scale[0], 47.0 * scale[1])
    Lineto_r(-28.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto_r(67.0 * scale[0], -68.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -24.0 * scale[1], 7.0 * scale[0], -
              28.0 * scale[1], -9.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 14.0 * scale[1], -20.0 * scale[0],
              30.0 * scale[1], -6.0 * scale[0], 30.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0], -
              7.0 * scale[1], 15.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(618.0 * scale[0], 703.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(950.0 * scale[0], 702.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -8.0 * scale[0], -
              13.0 * scale[1], -17.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -4.0 * scale[1], -16.0 *
              scale[0], -5.0 * scale[1], -1.0 * scale[0], -6.0 * scale[1])
    Curveto_r(18.0 * scale[0], -1.0 * scale[1], 34.0 * scale[0],
              16.0 * scale[1], 24.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0],
              1.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(464.0 * scale[0], 605.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -55.0 * scale[1], 1.0 * scale[0], -
              76.0 * scale[1], 3.0 * scale[0], -47.0 * scale[1])
    Curveto_r(2.0 * scale[0], 29.0 * scale[1], 2.0 * scale[0],
              74.0 * scale[1], 0.0 * scale[0], 100.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 26.0 * scale[1], -3.0 * scale[0],
              2.0 * scale[1], -3.0 * scale[0], -53.0 * scale[1])
    te.end_fill()
    Moveto(841.0 * scale[0], 684.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(641.0 * scale[0], 664.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(492.0 * scale[0], 620.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 2.0 * scale[0], -
              27.0 * scale[1], 5.0 * scale[0], -17.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              25.0 * scale[1], 0.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(190.0 * scale[0], 600.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0], -
              10.0 * scale[1], 10.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              9.0 * scale[1], 10.0 * scale[0], -20.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 5.0 * scale[0], -
              20.0 * scale[1], 10.0 * scale[0], -20.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              3.0 * scale[1], -2.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 25.0 * scale[1], -28.0 * scale[0],
              34.0 * scale[1], -28.0 * scale[0], 15.0 * scale[1])
    te.end_fill()
    Moveto(930.0 * scale[0], 579.0 * scale[1], x, y)
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
    Moveto(491.0 * scale[0], 431.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -45.0 * scale[1], -6.0 * scale[0], -
              67.0 * scale[1], -16.0 * scale[0], -75.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -9.0 * scale[1], -11.0 *
              scale[0], -11.0 * scale[1], 11.0 * scale[0], -13.0 * scale[1])
    Curveto_r(19.0 * scale[0], -1.0 * scale[1], 23.0 * scale[0],
              1.0 * scale[1], 13.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 7.0 * scale[1], 221.0 * scale[0],
              16.0 * scale[1], 255.0 * scale[0], 10.0 * scale[1])
    Curveto_r(5.0 * scale[0], -1.0 * scale[1], 4.0 * scale[0],
              4.0 * scale[1], -3.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 23.0 * scale[1], -56.0 * scale[0],
              28.0 * scale[1], -87.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-33.0 * scale[0], -17.0 * scale[1], -80.0 *
              scale[0], -20.0 * scale[1], -89.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -18.0 * scale[0],
              6.0 * scale[1], -38.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -5.0 * scale[1], -34.0 *
              scale[0], -9.0 * scale[1], -36.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -1.0 * scale[0],
              19.0 * scale[1], 2.0 * scale[0], 43.0 * scale[1])
    Curveto_r(3.0 * scale[0], 23.0 * scale[1], 1.0 * scale[0],
              51.0 * scale[1], -3.0 * scale[0], 62.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 14.0 * scale[1], -9.0 * scale[0],
              0.0 * scale[1], -9.0 * scale[0], -44.0 * scale[1])
    te.end_fill()
    Moveto_r(219.0 * scale[0], -51.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -4.0 * scale[0], -
              10.0 * scale[1], -9.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0],
              5.0 * scale[1], -16.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], 1.0 * scale[0],
              10.0 * scale[1], 9.0 * scale[0], 10.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0], -
              4.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(933.0 * scale[0], 453.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -34.0 * scale[1], -10.0 *
              scale[0], -36.0 * scale[1], 3.0 * scale[0], -19.0 * scale[1])
    Curveto_r(12.0 * scale[0], 17.0 * scale[1], 20.0 * scale[0],
              56.0 * scale[1], 11.0 * scale[0], 56.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              17.0 * scale[1], -14.0 * scale[0], -37.0 * scale[1])
    te.end_fill()
    Moveto(50.0 * scale[0], 449.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 5.0 * scale[0], -
              17.0 * scale[1], 10.0 * scale[0], -14.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 8.0 * scale[0],
              10.0 * scale[1], 5.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], 1.0 * scale[0],
              11.0 * scale[1], 7.0 * scale[0], 13.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 6.0 * scale[0],
              6.0 * scale[1], -4.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 1.0 * scale[1], -18.0 * scale[0], -
              6.0 * scale[1], -18.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(446.0 * scale[0], 452.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], -2.0 * scale[0], -
              13.0 * scale[1], 4.0 * scale[0], -17.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 8.0 * scale[0], -
              11.0 * scale[1], 5.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -5.0 * scale[1], -1.0 *
              scale[0], -9.0 * scale[1], 4.0 * scale[0], -9.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0],
              20.0 * scale[1], 2.0 * scale[0], 39.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 8.0 * scale[1], -11.0 * scale[0],
              9.0 * scale[1], -15.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(850.0 * scale[0], 453.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -15.0 * scale[1], 18.0 * scale[0], -
              35.0 * scale[1], 27.0 * scale[0], -32.0 * scale[1])
    Curveto_r(5.0 * scale[0], 2.0 * scale[1], 1.0 * scale[0],
              12.0 * scale[1], -9.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -18.0 * scale[0],
              14.0 * scale[1], -18.0 * scale[0], 10.0 * scale[1])
    te.end_fill()
    Moveto(38.0 * scale[0], 418.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(11.0 * scale[0], -14.0 * scale[1], 10.0 * scale[0], -
              18.0 * scale[1], -5.0 * scale[0], -27.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -10.0 * scale[1], -17.0 *
              scale[0], -10.0 * scale[1], 0.0 * scale[0], -11.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0],
              4.0 * scale[1], 17.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 6.0 * scale[0],
              7.0 * scale[1], 14.0 * scale[0], 4.0 * scale[1])
    Curveto_r(18.0 * scale[0], -7.0 * scale[1], 30.0 * scale[0],
              12.0 * scale[1], 15.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 4.0 * scale[1], -9.0 * scale[0],
              3.0 * scale[1], -5.0 * scale[0], -4.0 * scale[1])
    Curveto_r(11.0 * scale[0], -18.0 * scale[1], -5.0 *
              scale[0], -14.0 * scale[1], -28.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 14.0 * scale[1], -19.0 * scale[0],
              15.0 * scale[1], -8.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(880.0 * scale[0], 403.0 * scale[1], x, y)
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
    Moveto(930.0 * scale[0], 400.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0], -
              10.0 * scale[1], 10.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              5.0 * scale[1], 10.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -15.0 * scale[0], -
              10.0 * scale[1], -45.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 3.0 * scale[1], -47.0 * scale[0],
              2.0 * scale[1], -50.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -8.0 * scale[1], 72.0 * scale[0], -
              12.0 * scale[1], 97.0 * scale[0], -4.0 * scale[1])
    Curveto_r(25.0 * scale[0], 8.0 * scale[1], 24.0 * scale[0],
              44.0 * scale[1], -2.0 * scale[0], 44.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0], -
              4.0 * scale[1], -20.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(788.0 * scale[0], 363.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 30.0 *
              scale[0], -2.0 * scale[1], 40.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 0.0 * scale[1], -30.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(78.0 * scale[0], 353.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(218.0 * scale[0], 353.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(18.0 * scale[0], -2.0 * scale[1], 45.0 *
              scale[0], -2.0 * scale[1], 60.0 * scale[0], 0.0 * scale[1])
    Curveto_r(15.0 * scale[0], 2.0 * scale[1], 0.0 * scale[0],
              4.0 * scale[1], -33.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-33.0 * scale[0], 0.0 * scale[1], -45.0 *
              scale[0], -2.0 * scale[1], -27.0 * scale[0], -4.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#503314')
    te.end_fill()
    Moveto(38.0 * scale[0], 1392.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-36.0 * scale[0], -4.0 * scale[1], -39.0 * scale[0], -
              25.0 * scale[1], -37.0 * scale[0], -212.0 * scale[1])
    Curveto_r(1.0 * scale[0], -122.0 * scale[1], 4.0 * scale[0], -
              157.0 * scale[1], 15.0 * scale[0], -157.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              3.0 * scale[1], 9.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 3.0 * scale[1], 21.0 * scale[0],
              6.0 * scale[1], 51.0 * scale[0], 6.0 * scale[1])
    Curveto_r(29.0 * scale[0], -1.0 * scale[1], 54.0 *
              scale[0], -3.0 * scale[1], 54.0 * scale[0], -6.0 * scale[1])
    Curveto_r(0.0 * scale[0], -3.0 * scale[1], 37.0 *
              scale[0], -3.0 * scale[1], 82.0 * scale[0], 0.0 * scale[1])
    Lineto_r(83.0 * scale[0], 4.0 * scale[1])
    Lineto_r(-90.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-49.0 * scale[0], 4.0 * scale[1], -99.0 * scale[0],
              10.0 * scale[1], -109.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -17.0 * scale[0],
              5.0 * scale[1], -12.0 * scale[0], -3.0 * scale[1])
    Curveto_r(4.0 * scale[0], -7.0 * scale[1], 1.0 * scale[0], -
              12.0 * scale[1], -8.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0],
              6.0 * scale[1], -10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(4.0 * scale[0], 8.0 * scale[1], 1.0 * scale[0],
              15.0 * scale[1], -6.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              4.0 * scale[1], -5.0 * scale[0], -10.0 * scale[1])
    Curveto_r(3.0 * scale[0], -6.0 * scale[1], -4.0 * scale[0], -
              10.0 * scale[1], -17.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -19.0 * scale[0],
              3.0 * scale[1], -10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(11.0 * scale[0], 7.0 * scale[1], 11.0 * scale[0],
              9.0 * scale[1], -2.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 8.0 * scale[1], -20.0 * scale[0],
              27.0 * scale[1], 2.0 * scale[0], 27.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              2.0 * scale[1], 2.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 12.0 * scale[1], -25.0 * scale[0],
              191.0 * scale[1], -7.0 * scale[0], 202.0 * scale[1])
    Curveto_r(9.0 * scale[0], 6.0 * scale[1], 9.0 * scale[0],
              8.0 * scale[1], 0.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0],
              9.0 * scale[1], -13.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], 6.0 * scale[0],
              20.0 * scale[1], 14.0 * scale[0], 20.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 44.0 * scale[0],
              14.0 * scale[1], 93.0 * scale[0], 19.0 * scale[1])
    Lineto_r(90.0 * scale[0], 9.0 * scale[1])
    Lineto_r(-80.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-44.0 * scale[0], -1.0 * scale[1], -92.0 *
              scale[0], -3.0 * scale[1], -107.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(238.0 * scale[0], 1393.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(315.0 * scale[0], 1390.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(28.0 * scale[0], -12.0 * scale[1], 37.0 *
              scale[0], -12.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -16.0 * scale[0],
              10.0 * scale[1], -28.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 0.0 * scale[1], -21.0 *
              scale[0], -1.0 * scale[1], -2.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(680.0 * scale[0], 1397.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 54.0 * scale[0], -
              8.0 * scale[1], 115.0 * scale[0], -12.0 * scale[1])
    Curveto_r(60.0 * scale[0], -3.0 * scale[1], 117.0 * scale[0], -
              11.0 * scale[1], 127.0 * scale[0], -16.0 * scale[1])
    Curveto_r(26.0 * scale[0], -14.0 * scale[1], 23.0 * scale[0], -
              47.0 * scale[1], -4.0 * scale[0], -52.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -4.0 * scale[1], -20.0 *
              scale[0], -4.0 * scale[1], 3.0 * scale[0], -6.0 * scale[1])
    Curveto_r(24.0 * scale[0], -1.0 * scale[1], 26.0 * scale[0], -
              5.0 * scale[1], 24.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -18.0 * scale[1], -7.0 * scale[0], -
              34.0 * scale[1], -13.0 * scale[0], -36.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -10.0 * scale[0],
              8.0 * scale[1], -7.0 * scale[0], 27.0 * scale[1])
    Curveto_r(2.0 * scale[0], 17.0 * scale[1], -1.0 * scale[0],
              31.0 * scale[1], -6.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              13.0 * scale[1], -9.0 * scale[0], -29.0 * scale[1])
    Curveto_r(0.0 * scale[0], -15.0 * scale[1], -3.0 * scale[0], -
              50.0 * scale[1], -7.0 * scale[0], -76.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -37.0 * scale[1], -3.0 *
              scale[0], -46.0 * scale[1], 6.0 * scale[0], -41.0 * scale[1])
    Curveto_r(7.0 * scale[0], 5.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 17.0 * scale[1], 11.0 * scale[0],
              56.0 * scale[1], 22.0 * scale[0], 49.0 * scale[1])
    Curveto_r(10.0 * scale[0], -6.0 * scale[1], 7.0 * scale[0], -
              94.0 * scale[1], -3.0 * scale[0], -126.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -14.0 * scale[1], -9.0 * scale[0], -
              32.0 * scale[1], -9.0 * scale[0], -40.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -8.0 * scale[1], -7.0 * scale[0], -
              14.0 * scale[1], -13.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 1.0 * scale[1], -13.0 * scale[0], -
              2.0 * scale[1], -13.0 * scale[0], -8.0 * scale[1])
    Curveto_r(0.0 * scale[0], -22.0 * scale[1], 41.0 *
              scale[0], -9.0 * scale[1], 51.0 * scale[0], 16.0 * scale[1])
    Curveto_r(9.0 * scale[0], 25.0 * scale[1], 13.0 * scale[0],
              242.0 * scale[1], 6.0 * scale[0], 289.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 33.0 * scale[1], -54.0 * scale[0],
              48.0 * scale[1], -172.0 * scale[0], 53.0 * scale[1])
    Curveto_r(-60.0 * scale[0], 2.0 * scale[1], -108.0 * scale[0],
              2.0 * scale[1], -105.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(868.0 * scale[0], 1343.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(840.0 * scale[0], 1320.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -8.0 * scale[1], -11.0 *
              scale[0], -10.0 * scale[1], 8.0 * scale[0], -10.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 22.0 * scale[0],
              5.0 * scale[1], 22.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], -11.0 * scale[0],
              13.0 * scale[1], -30.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(66.0 * scale[0], 1305.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -8.0 * scale[1], 1.0 * scale[0], -
              15.0 * scale[1], -5.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              61.0 * scale[1], 11.0 * scale[0], -74.0 * scale[1])
    Curveto_r(10.0 * scale[0], -6.0 * scale[1], 18.0 * scale[0], -
              17.0 * scale[1], 18.0 * scale[0], -24.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -4.0 * scale[0], -
              10.0 * scale[1], -10.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0],
              2.0 * scale[1], -10.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 6.0 * scale[0], -
              12.0 * scale[1], 13.0 * scale[0], -15.0 * scale[1])
    Curveto_r(9.0 * scale[0], -5.0 * scale[1], 9.0 * scale[0], -
              7.0 * scale[1], -1.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -6.0 * scale[1], -7.0 *
              scale[0], -24.0 * scale[1], 9.0 * scale[0], -24.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              23.0 * scale[1], 9.0 * scale[0], 51.0 * scale[1])
    Curveto_r(0.0 * scale[0], 29.0 * scale[1], -4.0 * scale[0],
              48.0 * scale[1], -9.0 * scale[0], 44.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -3.0 * scale[1], -15.0 * scale[0],
              4.0 * scale[1], -21.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 26.0 * scale[1], 14.0 * scale[0],
              67.0 * scale[1], 50.0 * scale[0], 73.0 * scale[1])
    Curveto_r(15.0 * scale[0], 2.0 * scale[1], 9.0 * scale[0],
              5.0 * scale[1], -17.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-34.0 * scale[0], 1.0 * scale[1], -41.0 * scale[0], -
              2.0 * scale[1], -37.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(813.0 * scale[0], 1206.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -14.0 * scale[1], 13.0 * scale[0], -
              23.0 * scale[1], 15.0 * scale[0], -21.0 * scale[1])
    Curveto_r(7.0 * scale[0], 6.0 * scale[1], -9.0 * scale[0],
              45.0 * scale[1], -18.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -3.0 * scale[0], -
              11.0 * scale[1], 3.0 * scale[0], -24.0 * scale[1])
    te.end_fill()
    Moveto(170.0 * scale[0], 1210.0 * scale[1], x, y)
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
    Moveto(172.0 * scale[0], 1160.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 2.0 * scale[0], -
              27.0 * scale[1], 5.0 * scale[0], -17.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              25.0 * scale[1], 0.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(822.0 * scale[0], 1150.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(907.0 * scale[0], 1129.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(837.0 * scale[0], 1109.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(8.0 * scale[0], -8.0 * scale[1], 16.0 *
              scale[0], -8.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(16.0 * scale[0], 9.0 * scale[1], 14.0 * scale[0],
              10.0 * scale[1], -11.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 0.0 * scale[1], -27.0 * scale[0], -
              3.0 * scale[1], -19.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(130.0 * scale[0], 1080.0 * scale[1], x, y)
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
    Moveto(343.0 * scale[0], 1033.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(26.0 * scale[0], -2.0 * scale[1], 67.0 *
              scale[0], -2.0 * scale[1], 90.0 * scale[0], 0.0 * scale[1])
    Curveto_r(23.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              3.0 * scale[1], -48.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-49.0 * scale[0], 0.0 * scale[1], -68.0 *
              scale[0], -1.0 * scale[1], -42.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(648.0 * scale[0], 1033.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 30.0 *
              scale[0], -2.0 * scale[1], 40.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 0.0 * scale[1], -30.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(595.0 * scale[0], 997.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -14.0 * scale[1], -5.0 * scale[0], -
              34.0 * scale[1], -2.0 * scale[0], -44.0 * scale[1])
    Curveto_r(4.0 * scale[0], -15.0 * scale[1], 5.0 *
              scale[0], -14.0 * scale[1], 6.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], 6.0 * scale[0],
              25.0 * scale[1], 11.0 * scale[0], 28.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 9.0 * scale[0],
              2.0 * scale[1], 8.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -5.0 * scale[1], 4.0 * scale[0], -
              16.0 * scale[1], 14.0 * scale[0], -23.0 * scale[1])
    Curveto_r(20.0 * scale[0], -16.0 * scale[1], 14.0 * scale[0], -
              78.0 * scale[1], -8.0 * scale[0], -78.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -18.0 *
              scale[0], -15.0 * scale[1], 4.0 * scale[0], -31.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 15.0 * scale[1], -11.0 * scale[0],
              17.0 * scale[1], 3.0 * scale[0], 17.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0],
              8.0 * scale[1], 16.0 * scale[0], 19.0 * scale[1])
    Curveto_r(0.0 * scale[0], 28.0 * scale[1], 17.0 * scale[0],
              35.0 * scale[1], 30.0 * scale[0], 14.0 * scale[1])
    Curveto_r(10.0 * scale[0], -16.0 * scale[1], 11.0 *
              scale[0], -16.0 * scale[1], 7.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 13.0 * scale[1], -1.0 * scale[0],
              26.0 * scale[1], 4.0 * scale[0], 29.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 7.0 * scale[0],
              10.0 * scale[1], 4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 5.0 * scale[1], -1.0 * scale[0],
              9.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              8.0 * scale[1], 11.0 * scale[0], 18.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -2.0 * scale[0],
              15.0 * scale[1], -10.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -12.0 * scale[1], -13.0 *
              scale[0], -13.0 * scale[1], -29.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 11.0 * scale[1], -19.0 * scale[0],
              10.0 * scale[1], -14.0 * scale[0], -4.0 * scale[1])
    Curveto_r(5.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], -6.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 5.0 * scale[1], -11.0 * scale[0],
              17.0 * scale[1], -8.0 * scale[0], 27.0 * scale[1])
    Curveto_r(3.0 * scale[0], 11.0 * scale[1], 1.0 * scale[0],
              19.0 * scale[1], -3.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0],
              3.0 * scale[1], -24.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 4.0 * scale[1], -17.0 * scale[0], -
              2.0 * scale[1], -21.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(571.0 * scale[0], 984.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(15.0 * scale[0], 970.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(565.0 * scale[0], 951.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              12.0 * scale[1], 5.0 * scale[0], -16.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 10.0 * scale[0],
              1.0 * scale[1], 10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 18.0 * scale[1], -6.0 * scale[0],
              21.0 * scale[1], -15.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(815.0 * scale[0], 929.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -12.0 *
              scale[0], -8.0 * scale[1], -19.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 7.0 * scale[1], -53.0 * scale[0], -
              24.0 * scale[1], -61.0 * scale[0], -53.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -16.0 * scale[1], -3.0 *
              scale[0], -20.0 * scale[1], 3.0 * scale[0], -12.0 * scale[1])
    Curveto_r(7.0 * scale[0], 11.0 * scale[1], 57.0 * scale[0],
              42.0 * scale[1], 67.0 * scale[0], 42.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 6.0 * scale[0], -
              12.0 * scale[1], 10.0 * scale[0], -27.0 * scale[1])
    Curveto_r(5.0 * scale[0], -21.0 * scale[1], 8.0 * scale[0], -
              24.0 * scale[1], 15.0 * scale[0], -13.0 * scale[1])
    Curveto_r(7.0 * scale[0], 12.0 * scale[1], 10.0 * scale[0],
              11.0 * scale[1], 16.0 * scale[0], -3.0 * scale[1])
    Curveto_r(6.0 * scale[0], -17.0 * scale[1], 7.0 * scale[0], -
              17.0 * scale[1], 20.0 * scale[0], 0.0 * scale[1])
    Curveto_r(19.0 * scale[0], 25.0 * scale[1], 17.0 * scale[0],
              41.0 * scale[1], -2.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -18.0 * scale[1], -15.0 *
              scale[0], -18.0 * scale[1], -9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(6.0 * scale[0], 22.0 * scale[1], 5.0 * scale[0],
              23.0 * scale[1], -16.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-23.0 * scale[0], -13.0 * scale[1], -23.0 *
              scale[0], -15.0 * scale[1], -3.0 * scale[0], 35.0 * scale[1])
    Curveto_r(7.0 * scale[0], 17.0 * scale[1], -11.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(897.0 * scale[0], 903.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -11.0 * scale[1], -8.0 *
              scale[0], -22.0 * scale[1], 13.0 * scale[0], -33.0 * scale[1])
    Curveto_r(18.0 * scale[0], -9.0 * scale[1], 20.0 *
              scale[0], -8.0 * scale[1], 20.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 24.0 * scale[1], -18.0 * scale[0],
              34.0 * scale[1], -33.0 * scale[0], 18.0 * scale[1])
    te.end_fill()
    Moveto(576.0 * scale[0], 882.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -4.0 * scale[1], -1.0 * scale[0], -
              14.0 * scale[1], 5.0 * scale[0], -22.0 * scale[1])
    Curveto_r(7.0 * scale[0], -12.0 * scale[1], 9.0 *
              scale[0], -10.0 * scale[1], 9.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 23.0 * scale[1], -5.0 * scale[0],
              28.0 * scale[1], -14.0 * scale[0], 14.0 * scale[1])
    te.end_fill()
    Moveto(802.0 * scale[0], 825.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -22.0 * scale[1], 3.0 * scale[0], -
              49.0 * scale[1], 7.0 * scale[0], -59.0 * scale[1])
    Curveto_r(7.0 * scale[0], -19.0 * scale[1], 8.0 * scale[0], -
              19.0 * scale[1], 13.0 * scale[0], 2.0 * scale[1])
    Curveto_r(4.0 * scale[0], 12.0 * scale[1], 2.0 * scale[0],
              22.0 * scale[1], -2.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0],
              17.0 * scale[1], -13.0 * scale[0], 38.0 * scale[1])
    Lineto_r(-4.0 * scale[0], 37.0 * scale[1])
    Lineto_r(-1.0 * scale[0], -40.0 * scale[1])
    te.end_fill()
    Moveto(690.0 * scale[0], 825.0 * scale[1], x, y)
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
    Moveto(911.0 * scale[0], 824.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(948.0 * scale[0], 819.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -10.0 * scale[1], 17.0 * scale[0], -
              19.0 * scale[1], 17.0 * scale[0], -19.0 * scale[1])
    Curveto_r(0.0 * scale[0], 0.0 * scale[1], 1.0 * scale[0],
              8.0 * scale[1], 1.0 * scale[0], 18.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], -8.0 * scale[0],
              19.0 * scale[1], -17.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 2.0 * scale[1], -17.0 * scale[0],
              0.0 * scale[1], -1.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(530.0 * scale[0], 803.0 * scale[1], x, y)
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
    Moveto(920.0 * scale[0], 770.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(13.0 * scale[0], -24.0 * scale[1], 17.0 *
              scale[0], -25.0 * scale[1], 17.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -6.0 * scale[0],
              16.0 * scale[1], -14.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 4.0 * scale[1], -11.0 * scale[0],
              1.0 * scale[1], -3.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(390.0 * scale[0], 769.0 * scale[1], x, y)
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
    Moveto(680.0 * scale[0], 759.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 4.0 * scale[0], -
              8.0 * scale[1], 9.0 * scale[0], -5.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 13.0 * scale[0], -
              12.0 * scale[1], 19.0 * scale[0], -34.0 * scale[1])
    Curveto_r(7.0 * scale[0], -28.0 * scale[1], 7.0 * scale[0], -
              40.0 * scale[1], -1.0 * scale[0], -40.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], 5.0 * scale[0], -
              16.0 * scale[1], 23.0 * scale[0], -35.0 * scale[1])
    Curveto_r(26.0 * scale[0], -27.0 * scale[1], 41.0 * scale[0], -
              35.0 * scale[1], 57.0 * scale[0], -30.0 * scale[1])
    Curveto_r(12.0 * scale[0], 3.0 * scale[1], 25.0 * scale[0],
              0.0 * scale[1], 29.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], -13.0 * scale[1], 44.0 * scale[0],
              38.0 * scale[1], 44.0 * scale[0], 61.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], -8.0 * scale[0],
              6.0 * scale[1], -23.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-26.0 * scale[0], -31.0 * scale[1], -69.0 *
              scale[0], -46.0 * scale[1], -60.0 * scale[0], -21.0 * scale[1])
    Curveto_r(4.0 * scale[0], 10.0 * scale[1], 2.0 * scale[0],
              13.0 * scale[1], -5.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -9.0 * scale[1], -49.0 * scale[0],
              23.0 * scale[1], -36.0 * scale[0], 32.0 * scale[1])
    Curveto_r(5.0 * scale[0], 4.0 * scale[1], 9.0 * scale[0],
              13.0 * scale[1], 8.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 6.0 * scale[1], -2.0 * scale[0],
              17.0 * scale[1], -3.0 * scale[0], 22.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -7.0 * scale[0],
              9.0 * scale[1], -13.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -13.0 * scale[0],
              4.0 * scale[1], -13.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 15.0 * scale[1], -13.0 * scale[0],
              30.0 * scale[1], -27.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              5.0 * scale[1], -8.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(861.0 * scale[0], 765.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 6.0 * scale[0], -
              21.0 * scale[1], 14.0 * scale[0], -35.0 * scale[1])
    Curveto_r(8.0 * scale[0], -14.0 * scale[1], 14.0 * scale[0], -
              20.0 * scale[1], 14.0 * scale[0], -15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -6.0 * scale[0],
              21.0 * scale[1], -14.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 14.0 * scale[1], -14.0 * scale[0],
              21.0 * scale[1], -14.0 * scale[0], 15.0 * scale[1])
    te.end_fill()
    Moveto(14.0 * scale[0], 749.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], -1.0 * scale[0], -
              15.0 * scale[1], 7.0 * scale[0], -20.0 * scale[1])
    Curveto_r(40.0 * scale[0], -24.0 * scale[1], 44.0 * scale[0], -
              28.0 * scale[1], 33.0 * scale[0], -39.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -7.0 * scale[1], -16.0 *
              scale[0], -4.0 * scale[1], -31.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 20.0 * scale[1], -21.0 * scale[0],
              20.0 * scale[1], -19.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], -15.0 * scale[1], 7.0 * scale[0], -
              24.0 * scale[1], 16.0 * scale[0], -23.0 * scale[1])
    Curveto_r(38.0 * scale[0], 3.0 * scale[1], 56.0 * scale[0], -
              3.0 * scale[1], 69.0 * scale[0], -22.0 * scale[1])
    Curveto_r(12.0 * scale[0], -20.0 * scale[1], 11.0 * scale[0], -
              21.0 * scale[1], -8.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 3.0 * scale[1], -19.0 * scale[0],
              1.0 * scale[1], -15.0 * scale[0], -4.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 12.0 * scale[0], -
              9.0 * scale[1], 19.0 * scale[0], -9.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0], -
              6.0 * scale[1], 9.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -11.0 * scale[1], -2.0 *
              scale[0], -13.0 * scale[1], 10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(14.0 * scale[0], 5.0 * scale[1], 14.0 * scale[0],
              9.0 * scale[1], 4.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 14.0 * scale[1], -10.0 *
              scale[0], 15.0 * scale[1], 6.0 * scale[0], 8.0 * scale[1])
    Curveto_r(12.0 * scale[0], -4.0 * scale[1], 6.0 * scale[0],
              6.0 * scale[1], -15.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-38.0 * scale[0], 36.0 * scale[1], -40.0 * scale[0],
              57.0 * scale[1], -6.0 * scale[0], 59.0 * scale[1])
    Curveto_r(12.0 * scale[0], 1.0 * scale[1], 2.0 * scale[0],
              7.0 * scale[1], -23.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 7.0 * scale[1], -44.0 * scale[0],
              18.0 * scale[1], -42.0 * scale[0], 24.0 * scale[1])
    Curveto_r(3.0 * scale[0], 15.0 * scale[1], -5.0 * scale[0],
              15.0 * scale[1], -14.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(840.0 * scale[0], 741.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 18.0 * scale[1], -14.0 * scale[0],
              21.0 * scale[1], -14.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(560.0 * scale[0], 728.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 6.0 * scale[0], -
              8.0 * scale[1], 14.0 * scale[0], -5.0 * scale[1])
    Curveto_r(7.0 * scale[0], 3.0 * scale[1], 19.0 * scale[0],
              1.0 * scale[1], 25.0 * scale[0], -4.0 * scale[1])
    Curveto_r(8.0 * scale[0], -6.0 * scale[1], 8.0 *
              scale[0], -5.0 * scale[1], 1.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 15.0 * scale[1], -40.0 * scale[0],
              19.0 * scale[1], -40.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(624.0 * scale[0], 719.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], -3.0 *
              scale[0], -9.0 * scale[1], 4.0 * scale[0], -5.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 15.0 * scale[0], -
              1.0 * scale[1], 20.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -15.0 * scale[1], 10.0 *
              scale[0], -14.0 * scale[1], 16.0 * scale[0], 2.0 * scale[1])
    Curveto_r(4.0 * scale[0], 10.0 * scale[1], 4.0 * scale[0],
              15.0 * scale[1], 0.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -4.0 * scale[1], -13.0 *
              scale[0], -2.0 * scale[1], -20.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 7.0 * scale[1], -14.0 * scale[0],
              6.0 * scale[1], -20.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(140.0 * scale[0], 700.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 7.0 * scale[0], -
              10.0 * scale[1], 15.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              2.0 * scale[1], 15.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 2.0 * scale[1], -7.0 * scale[0],
              6.0 * scale[1], -15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -15.0 * scale[0],
              1.0 * scale[1], -15.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(860.0 * scale[0], 706.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(900.0 * scale[0], 690.0 * scale[1], x, y)
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
    Moveto(185.0 * scale[0], 680.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -9.0 * scale[1], 1.0 * scale[0], -
              14.0 * scale[1], 18.0 * scale[0], -11.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0], -
              3.0 * scale[1], 7.0 * scale[0], -8.0 * scale[1])
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 29.0 * scale[0], -
              21.0 * scale[1], 36.0 * scale[0], -9.0 * scale[1])
    Curveto_r(4.0 * scale[0], 7.0 * scale[1], 3.0 * scale[0],
              8.0 * scale[1], -4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -4.0 * scale[1], -12.0 *
              scale[0], -3.0 * scale[1], -12.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 16.0 * scale[1], -38.0 * scale[0],
              33.0 * scale[1], -45.0 * scale[0], 21.0 * scale[1])
    te.end_fill()
    Moveto(940.0 * scale[0], 680.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(362.0 * scale[0], 650.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -16.0 * scale[1], 23.0 * scale[0], -
              30.0 * scale[1], 25.0 * scale[0], -30.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0],
              14.0 * scale[1], -14.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 17.0 * scale[1], -21.0 * scale[0],
              30.0 * scale[1], -25.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], 1.0 * scale[0], -
              13.0 * scale[1], 14.0 * scale[0], -30.0 * scale[1])
    te.end_fill()
    Moveto(7.0 * scale[0], 643.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -2.0 * scale[1], 19.0 *
              scale[0], -2.0 * scale[1], 26.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(305.0 * scale[0], 620.0 * scale[1], x, y)
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
    Moveto(246.0 * scale[0], 618.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], 9.0 * scale[0], -
              8.0 * scale[1], 15.0 * scale[0], -8.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              4.0 * scale[1], 9.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -7.0 * scale[0],
              9.0 * scale[1], -15.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -9.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(175.0 * scale[0], 591.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(17.0 * scale[0], -16.0 * scale[1], 32.0 * scale[0], -
              23.0 * scale[1], 34.0 * scale[0], -17.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 9.0 * scale[0],
              15.0 * scale[1], 15.0 * scale[0], 19.0 * scale[1])
    Curveto_r(6.0 * scale[0], 5.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -11.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -3.0 * scale[1], -23.0 *
              scale[0], -2.0 * scale[1], -23.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -10.0 * scale[0],
              12.0 * scale[1], -22.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 6.0 * scale[1], -19.0 * scale[0],
              3.0 * scale[1], 7.0 * scale[0], -22.0 * scale[1])
    te.end_fill()
    Moveto(274.0 * scale[0], 606.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -8.0 * scale[1], -8.0 * scale[0], -
              19.0 * scale[1], -3.0 * scale[0], -29.0 * scale[1])
    Curveto_r(10.0 * scale[0], -17.0 * scale[1], -4.0 * scale[0], -
              32.0 * scale[1], -20.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 4.0 * scale[1], -16.0 * scale[0],
              3.0 * scale[1], -24.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -7.0 * scale[1], -10.0 *
              scale[0], -35.0 * scale[1], 12.0 * scale[0], -32.0 * scale[1])
    Curveto_r(12.0 * scale[0], 2.0 * scale[1], 16.0 * scale[0], -
              5.0 * scale[1], 16.0 * scale[0], -32.0 * scale[1])
    Curveto_r(0.0 * scale[0], -31.0 * scale[1], 3.0 * scale[0], -
              35.0 * scale[1], 28.0 * scale[0], -38.0 * scale[1])
    Curveto_r(19.0 * scale[0], -2.0 * scale[1], 27.0 * scale[0],
              1.0 * scale[1], 27.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], 4.0 * scale[0],
              16.0 * scale[1], 10.0 * scale[0], 16.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 5.0 * scale[0],
              10.0 * scale[1], -2.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 15.0 * scale[1], -17.0 * scale[0],
              24.0 * scale[1], -25.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -7.0 * scale[1], -17.0 * scale[0],
              19.0 * scale[1], 2.0 * scale[0], 38.0 * scale[1])
    Curveto_r(19.0 * scale[0], 18.0 * scale[1], 19.0 * scale[0],
              26.0 * scale[1], 0.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0],
              6.0 * scale[1], -9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(7.0 * scale[0], 18.0 * scale[1], 3.0 * scale[0],
              19.0 * scale[1], -12.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(330.0 * scale[0], 586.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(60.0 * scale[0], 550.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -13.0 * scale[0], -
              10.0 * scale[1], -30.0 * scale[0], -12.0 * scale[1])
    Lineto_r(-30.0 * scale[0], -3.0 * scale[1])
    Lineto_r(25.0 * scale[0], -12.0 * scale[1])
    Curveto_r(14.0 * scale[0], -6.0 * scale[1], 23.0 *
              scale[0], -8.0 * scale[1], 20.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], 1.0 * scale[0],
              10.0 * scale[1], 9.0 * scale[0], 13.0 * scale[1])
    Curveto_r(9.0 * scale[0], 4.0 * scale[1], 13.0 * scale[0], -
              2.0 * scale[1], 11.0 * scale[0], -16.0 * scale[1])
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], 1.0 * scale[0], -
              26.0 * scale[1], 3.0 * scale[0], -30.0 * scale[1])
    Curveto_r(5.0 * scale[0], -11.0 * scale[1], 52.0 * scale[0],
              33.0 * scale[1], 52.0 * scale[0], 47.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 6.0 * scale[1], -10.0 * scale[0],
              0.0 * scale[1], -22.0 * scale[0], -14.0 * scale[1])
    Lineto_r(-21.0 * scale[0], -25.0 * scale[1])
    Lineto_r(6.0 * scale[0], 26.0 * scale[1])
    Curveto_r(5.0 * scale[0], 19.0 * scale[1], 2.0 * scale[0],
              29.0 * scale[1], -8.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -15.0 * scale[0],
              1.0 * scale[1], -15.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(168.0 * scale[0], 522.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(27.0 * scale[0], -22.0 * scale[1], 32.0 * scale[0], -
              34.0 * scale[1], 32.0 * scale[0], -67.0 * scale[1])
    Curveto_r(0.0 * scale[0], -46.0 * scale[1], -6.0 * scale[0], -
              57.0 * scale[1], -39.0 * scale[0], -75.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -11.0 * scale[1], -26.0 *
              scale[0], -10.0 * scale[1], -36.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 15.0 * scale[1], -13.0 * scale[0],
              14.0 * scale[1], -17.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -22.0 * scale[1], -2.0 * scale[0], -
              24.0 * scale[1], 26.0 * scale[0], -17.0 * scale[1])
    Curveto_r(60.0 * scale[0], 13.0 * scale[1], 76.0 * scale[0],
              30.0 * scale[1], 76.0 * scale[0], 80.0 * scale[1])
    Curveto_r(0.0 * scale[0], 69.0 * scale[1], -9.0 * scale[0],
              88.0 * scale[1], -44.0 * scale[0], 99.0 * scale[1])
    Lineto_r(-31.0 * scale[0], 11.0 * scale[1])
    Lineto_r(33.0 * scale[0], -28.0 * scale[1])
    te.end_fill()
    Moveto(375.0 * scale[0], 540.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(11.0 * scale[0], -5.0 * scale[1], 14.0 *
              scale[0], -9.0 * scale[1], 8.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -1.0 * scale[1], -13.0 * scale[0], -
              6.0 * scale[1], -13.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 8.0 * scale[0], -
              5.0 * scale[1], 20.0 * scale[0], 2.0 * scale[1])
    Curveto_r(20.0 * scale[0], 13.0 * scale[1], 9.0 * scale[0],
              28.0 * scale[1], -20.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 0.0 * scale[1], -8.0 *
              scale[0], -3.0 * scale[1], 5.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(383.0 * scale[0], 485.0 * scale[1], x, y)
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
    Moveto(33.0 * scale[0], 445.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              12.0 * scale[1], 9.0 * scale[0], -9.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 6.0 * scale[0],
              10.0 * scale[1], 3.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 13.0 * scale[1], -12.0 * scale[0],
              11.0 * scale[1], -12.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(64.0 * scale[0], 435.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -18.0 * scale[1], 3.0 * scale[0], -
              22.0 * scale[1], 12.0 * scale[0], -14.0 * scale[1])
    Curveto_r(7.0 * scale[0], 6.0 * scale[1], 10.0 * scale[0],
              17.0 * scale[1], 7.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 22.0 * scale[1], -19.0 * scale[0],
              16.0 * scale[1], -19.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(387.0 * scale[0], 395.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -19.0 * scale[1], 12.0 * scale[0], -
              30.0 * scale[1], 26.0 * scale[0], -16.0 * scale[1])
    Curveto_r(9.0 * scale[0], 9.0 * scale[1], 8.0 * scale[0],
              11.0 * scale[1], -6.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -5.0 * scale[1], -16.0 *
              scale[0], -2.0 * scale[1], -11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 9.0 * scale[1], 4.0 * scale[0],
              16.0 * scale[1], 1.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              7.0 * scale[1], -10.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(15.0 * scale[0], 390.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(685.0 * scale[0], 359.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-53.0 * scale[0], -5.0 * scale[1], -48.0 *
              scale[0], -6.0 * scale[1], 39.0 * scale[0], -7.0 * scale[1])
    Curveto_r(98.0 * scale[0], -2.0 * scale[1], 124.0 * scale[0],
              3.0 * scale[1], 56.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 2.0 * scale[1], -62.0 * scale[0],
              1.0 * scale[1], -95.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(852.0 * scale[0], 354.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-22.0 * scale[0], -11.0 * scale[1], -21.0 *
              scale[0], -12.0 * scale[1], 20.0 * scale[0], -22.0 * scale[1])
    Curveto_r(27.0 * scale[0], -7.0 * scale[1], 44.0 *
              scale[0], -8.0 * scale[1], 46.0 * scale[0], -2.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 8.0 * scale[0],
              10.0 * scale[1], 14.0 * scale[0], 10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0], -
              6.0 * scale[1], 5.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -3.0 * scale[0], -
              17.0 * scale[1], 1.0 * scale[0], -20.0 * scale[1])
    Curveto_r(8.0 * scale[0], -9.0 * scale[1], 10.0 * scale[0], -
              46.0 * scale[1], 2.0 * scale[0], -51.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -3.0 * scale[1], -4.0 * scale[0], -
              25.0 * scale[1], 1.0 * scale[0], -49.0 * scale[1])
    Curveto_r(10.0 * scale[0], -55.0 * scale[1], 5.0 * scale[0], -
              119.0 * scale[1], -11.0 * scale[0], -124.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -3.0 * scale[1], -5.0 *
              scale[0], -8.0 * scale[1], 6.0 * scale[0], -16.0 * scale[1])
    Curveto_r(15.0 * scale[0], -12.0 * scale[1], 15.0 * scale[0], -
              13.0 * scale[1], -1.0 * scale[0], -29.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -9.0 * scale[1], -13.0 * scale[0], -
              18.0 * scale[1], -8.0 * scale[0], -18.0 * scale[1])
    Curveto_r(4.0 * scale[0], -1.0 * scale[1], -5.0 * scale[0], -
              5.0 * scale[1], -22.0 * scale[0], -9.0 * scale[1])
    Lineto_r(-30.0 * scale[0], -8.0 * scale[1])
    Lineto_r(32.0 * scale[0], -1.0 * scale[1])
    Curveto_r(22.0 * scale[0], -1.0 * scale[1], 35.0 * scale[0],
              5.0 * scale[1], 42.0 * scale[0], 17.0 * scale[1])
    Curveto_r(5.0 * scale[0], 10.0 * scale[1], 9.0 * scale[0],
              84.0 * scale[1], 8.0 * scale[0], 165.0 * scale[1])
    Curveto_r(0.0 * scale[0], 120.0 * scale[1], -3.0 * scale[0],
              150.0 * scale[1], -16.0 * scale[0], 161.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 19.0 * scale[1], -62.0 * scale[0],
              24.0 * scale[1], -89.0 * scale[0], 10.0 * scale[1])
    te.end_fill()
    Moveto(7.0 * scale[0], 354.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -4.0 * scale[1], -6.0 * scale[0], -
              46.0 * scale[1], -5.0 * scale[0], -93.0 * scale[1])
    Curveto_r(2.0 * scale[0], -80.0 * scale[1], 2.0 * scale[0], -
              81.0 * scale[1], 5.0 * scale[0], -21.0 * scale[1])
    Curveto_r(2.0 * scale[0], 35.0 * scale[1], 9.0 * scale[0],
              68.0 * scale[1], 15.0 * scale[0], 71.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 9.0 * scale[0],
              14.0 * scale[1], 2.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 12.0 * scale[1], -13.0 * scale[0],
              18.0 * scale[1], -17.0 * scale[0], 14.0 * scale[1])
    te.end_fill()
    Moveto(313.0 * scale[0], 353.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(888.0 * scale[0], 243.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(870.0 * scale[0], 215.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 6.0 * scale[0], -
              12.0 * scale[1], 15.0 * scale[0], -9.0 * scale[1])
    Curveto_r(8.0 * scale[0], 4.0 * scale[1], 15.0 * scale[0],
              7.0 * scale[1], 15.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 2.0 * scale[1], -7.0 * scale[0],
              5.0 * scale[1], -15.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 3.0 * scale[1], -15.0 * scale[0],
              0.0 * scale[1], -15.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(0.0 * scale[0], 160.0 * scale[1], x, y)
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
    Moveto(910.0 * scale[0], 125.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              15.0 * scale[1], 10.0 * scale[0], -15.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              7.0 * scale[1], 4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              15.0 * scale[1], -10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              7.0 * scale[1], -4.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(0.0 * scale[0], 67.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -43.0 * scale[1], 17.0 * scale[0], -
              58.0 * scale[1], 72.0 * scale[0], -63.0 * scale[1])
    Curveto_r(40.0 * scale[0], -3.0 * scale[1], 35.0 * scale[0],
              0.0 * scale[1], -20.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 5.0 * scale[1], -46.0 * scale[0],
              45.0 * scale[1], -32.0 * scale[0], 54.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], 2.0 * scale[0],
              11.0 * scale[1], -6.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 11.0 * scale[1], -14.0 * scale[0],
              7.0 * scale[1], -14.0 * scale[0], -21.0 * scale[1])
    te.end_fill()
    Moveto(878.0 * scale[0], 73.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(888.0 * scale[0], 23.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.penup()
