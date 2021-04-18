import turtle as te
from helper import *


def ship(x, y, scale):

    te.penup()
    te.color('#b25b28')
    te.end_fill()
    Moveto(2086.0 * scale[0], 2495.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -1.0 * scale[0], -
              15.0 * scale[1], 3.0 * scale[0], -15.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              7.0 * scale[1], 15.0 * scale[0], 15.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], 1.0 * scale[0],
              15.0 * scale[1], -3.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              7.0 * scale[1], -15.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(1990.0 * scale[0], 2436.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 7.0 * scale[0], -
              7.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 12.0 *
              scale[0], -2.0 * scale[1], 9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], -25.0 * scale[0],
              14.0 * scale[1], -25.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(1947.0 * scale[0], 2343.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -9.0 * scale[1], -9.0 *
              scale[0], -23.0 * scale[1], 1.0 * scale[0], -23.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              7.0 * scale[1], 9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], -1.0 * scale[0],
              18.0 * scale[1], -10.0 * scale[0], 8.0 * scale[1])
    te.end_fill()
    Moveto(1985.0 * scale[0], 2330.0 * scale[1], x, y)
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
    Moveto(363.0 * scale[0], 2253.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -6.0 * scale[1], -18.0 * scale[0], -
              103.0 * scale[1], -3.0 * scale[0], -103.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              22.0 * scale[1], 10.0 * scale[0], 49.0 * scale[1])
    Curveto_r(0.0 * scale[0], 47.0 * scale[1], 1.0 * scale[0],
              48.0 * scale[1], 28.0 * scale[0], 43.0 * scale[1])
    Curveto_r(15.0 * scale[0], -2.0 * scale[1], 24.0 *
              scale[0], -2.0 * scale[1], 21.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 9.0 * scale[1], -41.0 * scale[0],
              14.0 * scale[1], -56.0 * scale[0], 9.0 * scale[1])
    te.end_fill()
    Moveto(3185.0 * scale[0], 2250.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-18.0 * scale[0], -8.0 * scale[1], -17.0 *
              scale[0], -9.0 * scale[1], 8.0 * scale[0], -9.0 * scale[1])
    Curveto_r(16.0 * scale[0], -1.0 * scale[1], 26.0 * scale[0],
              3.0 * scale[1], 22.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -7.0 * scale[0],
              10.0 * scale[1], -8.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              4.0 * scale[1], -22.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(495.0 * scale[0], 2240.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], 6.0 * scale[0], -
              10.0 * scale[1], 22.0 * scale[0], -10.0 * scale[1])
    Curveto_r(22.0 * scale[0], 0.0 * scale[1], 25.0 * scale[0],
              2.0 * scale[1], 13.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 12.0 * scale[1], -27.0 * scale[0],
              12.0 * scale[1], -35.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(1876.0 * scale[0], 2234.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -25.0 * scale[1], 1.0 *
              scale[0], -29.0 * scale[1], 14.0 * scale[0], -5.0 * scale[1])
    Curveto_r(6.0 * scale[0], 12.0 * scale[1], 7.0 * scale[0],
              21.0 * scale[1], 1.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              7.0 * scale[1], -15.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(3075.0 * scale[0], 2240.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-18.0 * scale[0], -8.0 * scale[1], -17.0 *
              scale[0], -9.0 * scale[1], 8.0 * scale[0], -9.0 * scale[1])
    Curveto_r(16.0 * scale[0], -1.0 * scale[1], 26.0 * scale[0],
              3.0 * scale[1], 22.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -7.0 * scale[0],
              10.0 * scale[1], -8.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              4.0 * scale[1], -22.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(3230.0 * scale[0], 2200.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -27.0 * scale[1], 5.0 * scale[0], -
              50.0 * scale[1], 10.0 * scale[0], -50.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              23.0 * scale[1], 10.0 * scale[0], 50.0 * scale[1])
    Curveto_r(0.0 * scale[0], 28.0 * scale[1], -4.0 * scale[0],
              50.0 * scale[1], -10.0 * scale[0], 50.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              22.0 * scale[1], -10.0 * scale[0], -50.0 * scale[1])
    te.end_fill()
    Moveto(615.0 * scale[0], 2230.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], 7.0 * scale[0], -
              10.0 * scale[1], 27.0 * scale[0], -9.0 * scale[1])
    Curveto_r(27.0 * scale[0], 0.0 * scale[1], 30.0 * scale[0],
              2.0 * scale[1], 13.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-27.0 * scale[0], 12.0 * scale[1], -33.0 * scale[0],
              12.0 * scale[1], -40.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(2945.0 * scale[0], 2230.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -7.0 * scale[1], -12.0 *
              scale[0], -9.0 * scale[1], 18.0 * scale[0], -9.0 * scale[1])
    Curveto_r(23.0 * scale[0], -1.0 * scale[1], 36.0 * scale[0],
              3.0 * scale[1], 32.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 12.0 * scale[1], -23.0 * scale[0],
              12.0 * scale[1], -50.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(750.0 * scale[0], 2220.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -7.0 * scale[1], -6.0 * scale[0], -
              10.0 * scale[1], 20.0 * scale[0], -10.0 * scale[1])
    Curveto_r(26.0 * scale[0], 0.0 * scale[1], 31.0 * scale[0],
              3.0 * scale[1], 20.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -17.0 * scale[0],
              10.0 * scale[1], -20.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              5.0 * scale[1], -20.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(2810.0 * scale[0], 2220.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -7.0 * scale[1], -7.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -10.0 * scale[1])
    Curveto_r(20.0 * scale[0], 0.0 * scale[1], 31.0 * scale[0],
              4.0 * scale[1], 27.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 13.0 * scale[1], -26.0 * scale[0],
              13.0 * scale[1], -45.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(920.0 * scale[0], 2210.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 17.0 * scale[0], -
              10.0 * scale[1], 38.0 * scale[0], -9.0 * scale[1])
    Curveto_r(30.0 * scale[0], 0.0 * scale[1], 33.0 * scale[0],
              2.0 * scale[1], 17.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-28.0 * scale[0], 12.0 * scale[1], -55.0 * scale[0],
              12.0 * scale[1], -55.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(1920.0 * scale[0], 2209.0 * scale[1], x, y)
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
    Moveto(2630.0 * scale[0], 2210.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-21.0 * scale[0], -7.0 * scale[1], -19.0 *
              scale[0], -8.0 * scale[1], 18.0 * scale[0], -9.0 * scale[1])
    Curveto_r(23.0 * scale[0], -1.0 * scale[1], 42.0 * scale[0],
              4.0 * scale[1], 42.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], -24.0 * scale[0],
              12.0 * scale[1], -60.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(1120.0 * scale[0], 2200.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 21.0 * scale[0], -
              9.0 * scale[1], 48.0 * scale[0], -9.0 * scale[1])
    Curveto_r(42.0 * scale[0], 1.0 * scale[1], 44.0 * scale[0],
              2.0 * scale[1], 17.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-44.0 * scale[0], 11.0 * scale[1], -65.0 * scale[0],
              11.0 * scale[1], -65.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(1990.0 * scale[0], 2201.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-25.0 * scale[0], -7.0 * scale[1])
    Lineto_r(28.0 * scale[0], -6.0 * scale[1])
    Curveto_r(19.0 * scale[0], -4.0 * scale[1], 27.0 *
              scale[0], -1.0 * scale[1], 27.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -1.0 * scale[0],
              14.0 * scale[1], -2.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -1.0 * scale[1], -14.0 *
              scale[0], -4.0 * scale[1], -28.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(2415.0 * scale[0], 2200.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-38.0 * scale[0], -7.0 * scale[1], -38.0 *
              scale[0], -7.0 * scale[1], 18.0 * scale[0], -9.0 * scale[1])
    Curveto_r(37.0 * scale[0], 0.0 * scale[1], 56.0 * scale[0],
              3.0 * scale[1], 52.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 11.0 * scale[1], -10.0 * scale[0],
              11.0 * scale[1], -70.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(1385.0 * scale[0], 2190.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -5.0 * scale[1], 18.0 *
              scale[0], -8.0 * scale[1], 85.0 * scale[0], -8.0 * scale[1])
    Curveto_r(91.0 * scale[0], 1.0 * scale[1], 98.0 * scale[0],
              2.0 * scale[1], 50.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-73.0 * scale[0], 11.0 * scale[1], -111.0 * scale[0],
              10.0 * scale[1], -135.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(1807.0 * scale[0], 2193.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -2.0 * scale[1], -15.0 * scale[0], -
              9.0 * scale[1], -12.0 * scale[0], -13.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], -5.0 * scale[0], -
              26.0 * scale[1], -18.0 * scale[0], -47.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -21.0 * scale[1], -26.0 *
              scale[0], -43.0 * scale[1], -30.0 * scale[0], -49.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], 1.0 * scale[0], -
              14.0 * scale[1], 12.0 * scale[0], -17.0 * scale[1])
    Curveto_r(14.0 * scale[0], -3.0 * scale[1], 24.0 * scale[0],
              8.0 * scale[1], 45.0 * scale[0], 49.0 * scale[1])
    Curveto_r(15.0 * scale[0], 30.0 * scale[1], 34.0 * scale[0],
              61.0 * scale[1], 43.0 * scale[0], 69.0 * scale[1])
    Curveto_r(13.0 * scale[0], 13.0 * scale[1], 12.0 * scale[0],
              15.0 * scale[1], -4.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -1.0 * scale[1], -26.0 *
              scale[0], -3.0 * scale[1], -36.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(2100.0 * scale[0], 2190.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-41.0 * scale[0], -6.0 * scale[1], -39.0 *
              scale[0], -7.0 * scale[1], 27.0 * scale[0], -8.0 * scale[1])
    Curveto_r(39.0 * scale[0], -1.0 * scale[1], 75.0 * scale[0],
              3.0 * scale[1], 78.0 * scale[0], 8.0 * scale[1])
    Curveto_r(7.0 * scale[0], 11.0 * scale[1], -34.0 * scale[0],
              11.0 * scale[1], -105.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(1900.0 * scale[0], 2141.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -25.0 * scale[1], -30.0 *
              scale[0], -53.0 * scale[1], -37.0 * scale[0], -62.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -14.0 * scale[1], -11.0 *
              scale[0], -16.0 * scale[1], 10.0 * scale[0], -12.0 * scale[1])
    Curveto_r(15.0 * scale[0], 3.0 * scale[1], 33.0 * scale[0],
              20.0 * scale[1], 46.0 * scale[0], 44.0 * scale[1])
    Curveto_r(12.0 * scale[0], 21.0 * scale[1], 28.0 * scale[0],
              45.0 * scale[1], 36.0 * scale[0], 53.0 * scale[1])
    Curveto_r(12.0 * scale[0], 12.0 * scale[1], 11.0 * scale[0],
              14.0 * scale[1], -9.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 4.0 * scale[1], -27.0 * scale[0], -
              3.0 * scale[1], -46.0 * scale[0], -41.0 * scale[1])
    te.end_fill()
    Moveto(366.0 * scale[0], 2141.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], 7.0 * scale[0], -
              10.0 * scale[1], 26.0 * scale[0], -10.0 * scale[1])
    Curveto_r(18.0 * scale[0], 0.0 * scale[1], 47.0 * scale[0], -
              2.0 * scale[1], 63.0 * scale[0], -5.0 * scale[1])
    Lineto_r(30.0 * scale[0], -6.0 * scale[1])
    Lineto_r(-30.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-49.0 * scale[0], 17.0 * scale[1], -83.0 * scale[0],
              21.0 * scale[1], -89.0 * scale[0], 10.0 * scale[1])
    te.end_fill()
    Moveto(3155.0 * scale[0], 2134.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-39.0 * scale[0], -14.0 * scale[1], -39.0 *
              scale[0], -14.0 * scale[1], -5.0 * scale[0], -8.0 * scale[1])
    Curveto_r(19.0 * scale[0], 4.0 * scale[1], 48.0 * scale[0],
              6.0 * scale[1], 63.0 * scale[0], 6.0 * scale[1])
    Curveto_r(15.0 * scale[0], -1.0 * scale[1], 25.0 * scale[0],
              3.0 * scale[1], 22.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 13.0 * scale[1], -31.0 * scale[0],
              11.0 * scale[1], -80.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(553.0 * scale[0], 2113.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 25.0 *
              scale[0], -2.0 * scale[1], 35.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -27.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(3013.0 * scale[0], 2113.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(698.0 * scale[0], 2103.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(2858.0 * scale[0], 2103.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 30.0 *
              scale[0], -2.0 * scale[1], 40.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 0.0 * scale[1], -30.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(868.0 * scale[0], 2093.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 30.0 *
              scale[0], -2.0 * scale[1], 40.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 0.0 * scale[1], -30.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(2688.0 * scale[0], 2093.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 30.0 *
              scale[0], -2.0 * scale[1], 40.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 0.0 * scale[1], -30.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(1068.0 * scale[0], 2083.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(18.0 * scale[0], -2.0 * scale[1], 45.0 *
              scale[0], -2.0 * scale[1], 60.0 * scale[0], 0.0 * scale[1])
    Curveto_r(15.0 * scale[0], 2.0 * scale[1], 0.0 * scale[0],
              4.0 * scale[1], -33.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-33.0 * scale[0], 0.0 * scale[1], -45.0 *
              scale[0], -2.0 * scale[1], -27.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(2463.0 * scale[0], 2083.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(15.0 * scale[0], -2.0 * scale[1], 39.0 *
              scale[0], -2.0 * scale[1], 55.0 * scale[0], 0.0 * scale[1])
    Curveto_r(15.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              4.0 * scale[1], -28.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 0.0 * scale[1], -43.0 *
              scale[0], -2.0 * scale[1], -27.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(458.0 * scale[0], 2055.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -13.0 * scale[1], -2.0 *
              scale[0], -22.0 * scale[1], 2.0 * scale[0], -20.0 * scale[1])
    Curveto_r(11.0 * scale[0], 7.0 * scale[1], 22.0 * scale[0], -
              43.0 * scale[1], 14.0 * scale[0], -57.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -3.0 *
              scale[0], -8.0 * scale[1], 3.0 * scale[0], -5.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 16.0 * scale[0], -
              7.0 * scale[1], 23.0 * scale[0], -23.0 * scale[1])
    Curveto_r(7.0 * scale[0], -17.0 * scale[1], 13.0 * scale[0], -
              30.0 * scale[1], 14.0 * scale[0], -30.0 * scale[1])
    Curveto_r(64.0 * scale[0], -14.0 * scale[1], 1003.0 * scale[0], -
              56.0 * scale[1], 1072.0 * scale[0], -48.0 * scale[1])
    Curveto_r(33.0 * scale[0], 4.0 * scale[1], 44.0 * scale[0], -
              7.0 * scale[1], 25.0 * scale[0], -28.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -5.0 * scale[1], -20.0 * scale[0], -
              29.0 * scale[1], -34.0 * scale[0], -54.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -25.0 * scale[1], -37.0 *
              scale[0], -67.0 * scale[1], -53.0 * scale[0], -94.0 * scale[1])
    Lineto_r(-27.0 * scale[0], -49.0 * scale[1])
    Lineto_r(-186.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-156.0 * scale[0], 5.0 * scale[1], -514.0 * scale[0],
              23.0 * scale[1], -613.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 1.0 * scale[1], -33.0 * scale[0],
              7.0 * scale[1], -40.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 7.0 * scale[1], -16.0 * scale[0],
              12.0 * scale[1], -21.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], 5.0 * scale[0], -
              12.0 * scale[1], 22.0 * scale[0], -26.0 * scale[1])
    Curveto_r(17.0 * scale[0], -14.0 * scale[1], 29.0 * scale[0], -
              29.0 * scale[1], 26.0 * scale[0], -34.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -4.0 * scale[1], 5.0 * scale[0], -
              16.0 * scale[1], 18.0 * scale[0], -26.0 * scale[1])
    Lineto_r(22.0 * scale[0], -19.0 * scale[1])
    Lineto_r(-20.0 * scale[0], 25.0 * scale[1])
    Lineto_r(-20.0 * scale[0], 25.0 * scale[1])
    Lineto_r(27.0 * scale[0], -24.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 25.0 * scale[0], -
              28.0 * scale[1], 21.0 * scale[0], -34.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], -1.0 *
              scale[0], -7.0 * scale[1], 5.0 * scale[0], -3.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 13.0 * scale[0],
              2.0 * scale[1], 17.0 * scale[0], -4.0 * scale[1])
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 10.0 * scale[0], -
              8.0 * scale[1], 15.0 * scale[0], -5.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 22.0 * scale[0], -
              19.0 * scale[1], 24.0 * scale[0], -40.0 * scale[1])
    Curveto_r(1.0 * scale[0], -5.0 * scale[1], 9.0 * scale[0], -
              9.0 * scale[1], 19.0 * scale[0], -7.0 * scale[1])
    Curveto_r(9.0 * scale[0], 2.0 * scale[1], 17.0 * scale[0], -
              1.0 * scale[1], 17.0 * scale[0], -6.0 * scale[1])
    Curveto_r(0.0 * scale[0], -20.0 * scale[1], 92.0 * scale[0], -
              42.0 * scale[1], 234.0 * scale[0], -57.0 * scale[1])
    Curveto_r(82.0 * scale[0], -9.0 * scale[1], 155.0 * scale[0], -
              14.0 * scale[1], 163.0 * scale[0], -11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 3.0 * scale[1], 17.0 * scale[0],
              16.0 * scale[1], 22.0 * scale[0], 29.0 * scale[1])
    Curveto_r(7.0 * scale[0], 18.0 * scale[1], 28.0 * scale[0],
              30.0 * scale[1], 83.0 * scale[0], 50.0 * scale[1])
    Curveto_r(40.0 * scale[0], 14.0 * scale[1], 85.0 * scale[0],
              29.0 * scale[1], 100.0 * scale[0], 33.0 * scale[1])
    Curveto_r(17.0 * scale[0], 3.0 * scale[1], 35.0 * scale[0],
              20.0 * scale[1], 48.0 * scale[0], 41.0 * scale[1])
    Curveto_r(15.0 * scale[0], 26.0 * scale[1], 26.0 * scale[0],
              34.0 * scale[1], 40.0 * scale[0], 30.0 * scale[1])
    Curveto_r(11.0 * scale[0], -3.0 * scale[1], 20.0 *
              scale[0], -2.0 * scale[1], 20.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], 29.0 * scale[0],
              57.0 * scale[1], 64.0 * scale[0], 117.0 * scale[1])
    Curveto_r(44.0 * scale[0], 77.0 * scale[1], 58.0 * scale[0],
              109.0 * scale[1], 46.0 * scale[0], 106.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -3.0 * scale[1], -20.0 * scale[0],
              2.0 * scale[1], -23.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 9.0 * scale[1], -2.0 * scale[0],
              15.0 * scale[1], 3.0 * scale[0], 13.0 * scale[1])
    Curveto_r(8.0 * scale[0], -2.0 * scale[1], 84.0 * scale[0],
              113.0 * scale[1], 78.0 * scale[0], 118.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 1.0 * scale[1], -174.0 * scale[0],
              7.0 * scale[1], -383.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-363.0 * scale[0], 11.0 * scale[1], -841.0 * scale[0],
              37.0 * scale[1], -856.0 * scale[0], 46.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              6.0 * scale[1], -11.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(1378.0 * scale[0], 2073.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(29.0 * scale[0], -2.0 * scale[1], 74.0 *
              scale[0], -2.0 * scale[1], 100.0 * scale[0], 0.0 * scale[1])
    Curveto_r(26.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              3.0 * scale[1], -53.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-55.0 * scale[0], 0.0 * scale[1], -76.0 *
              scale[0], -1.0 * scale[1], -47.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(2123.0 * scale[0], 2073.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(26.0 * scale[0], -2.0 * scale[1], 67.0 *
              scale[0], -2.0 * scale[1], 90.0 * scale[0], 0.0 * scale[1])
    Curveto_r(23.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              3.0 * scale[1], -48.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-49.0 * scale[0], 0.0 * scale[1], -68.0 *
              scale[0], -1.0 * scale[1], -42.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(3015.0 * scale[0], 2065.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-17.0 * scale[0], -7.0 * scale[1], -615.0 * scale[0], -
              34.0 * scale[1], -892.0 * scale[0], -41.0 * scale[1])
    Lineto_r(-261.0 * scale[0], -7.0 * scale[1])
    Lineto_r(-17.0 * scale[0], -36.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -20.0 * scale[1], -14.0 * scale[0], -
              39.0 * scale[1], -13.0 * scale[0], -43.0 * scale[1])
    Curveto_r(2.0 * scale[0], -4.0 * scale[1], -7.0 * scale[0], -
              15.0 * scale[1], -19.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -9.0 * scale[1], -23.0 * scale[0], -
              23.0 * scale[1], -23.0 * scale[0], -32.0 * scale[1])
    Curveto_r(0.0 * scale[0], -15.0 * scale[1], 33.0 * scale[0], -
              16.0 * scale[1], 353.0 * scale[0], -9.0 * scale[1])
    Curveto_r(193.0 * scale[0], 3.0 * scale[1], 456.0 * scale[0],
              13.0 * scale[1], 582.0 * scale[0], 21.0 * scale[1])
    Curveto_r(127.0 * scale[0], 8.0 * scale[1], 269.0 * scale[0],
              16.0 * scale[1], 317.0 * scale[0], 18.0 * scale[1])
    Lineto_r(86.0 * scale[0], 2.0 * scale[1])
    Lineto_r(7.0 * scale[0], 43.0 * scale[1])
    Curveto_r(3.0 * scale[0], 23.0 * scale[1], 9.0 * scale[0],
              40.0 * scale[1], 13.0 * scale[0], 38.0 * scale[1])
    Curveto_r(4.0 * scale[0], -2.0 * scale[1], 7.0 * scale[0],
              13.0 * scale[1], 7.0 * scale[0], 35.0 * scale[1])
    Lineto_r(0.0 * scale[0], 39.0 * scale[1])
    Lineto_r(-65.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-36.0 * scale[0], 0.0 * scale[1], -69.0 *
              scale[0], -2.0 * scale[1], -75.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(1736.0 * scale[0], 2003.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(1740.0 * scale[0], 1870.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -80.0 * scale[0], -
              151.0 * scale[1], -114.0 * scale[0], -202.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -26.0 * scale[1], -17.0 *
              scale[0], -26.0 * scale[1], 2.0 * scale[0], -21.0 * scale[1])
    Curveto_r(12.0 * scale[0], 3.0 * scale[1], 22.0 * scale[0], -
              2.0 * scale[1], 26.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], -9.0 * scale[1], 2.0 * scale[0], -
              14.0 * scale[1], -3.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 4.0 * scale[1], -23.0 * scale[0], -
              19.0 * scale[1], -41.0 * scale[0], -50.0 * scale[1])
    Curveto_r(-27.0 * scale[0], -49.0 * scale[1], -30.0 *
              scale[0], -60.0 * scale[1], -23.0 * scale[0], -97.0 * scale[1])
    Lineto_r(9.0 * scale[0], -42.0 * scale[1])
    Lineto_r(244.0 * scale[0], 0.0 * scale[1])
    Curveto_r(311.0 * scale[0], 0.0 * scale[1], 660.0 * scale[0],
              8.0 * scale[1], 649.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 7.0 * scale[1], 226.0 * scale[0],
              35.0 * scale[1], 293.0 * scale[0], 35.0 * scale[1])
    Curveto_r(25.0 * scale[0], 0.0 * scale[1], 43.0 * scale[0],
              2.0 * scale[1], 38.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              11.0 * scale[1], 6.0 * scale[0], 18.0 * scale[1])
    Curveto_r(8.0 * scale[0], 7.0 * scale[1], 14.0 * scale[0],
              9.0 * scale[1], 14.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 26.0 * scale[0],
              18.0 * scale[1], 58.0 * scale[0], 50.0 * scale[1])
    Curveto_r(32.0 * scale[0], 32.0 * scale[1], 62.0 * scale[0],
              54.0 * scale[1], 67.0 * scale[0], 50.0 * scale[1])
    Curveto_r(4.0 * scale[0], -5.0 * scale[1], 5.0 *
              scale[0], -3.0 * scale[1], 1.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -2.0 * scale[0],
              14.0 * scale[1], 4.0 * scale[0], 18.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 8.0 * scale[0],
              11.0 * scale[1], 5.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 8.0 * scale[1], 8.0 * scale[0],
              13.0 * scale[1], 27.0 * scale[0], 10.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 5.0 * scale[0],
              6.0 * scale[1], 2.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 12.0 * scale[1], -20.0 * scale[0],
              14.0 * scale[1], -72.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-336.0 * scale[0], -23.0 * scale[1], -1272.0 *
              scale[0], -49.0 * scale[1], -1272.0 * scale[0], -35.0 * scale[1])
    Curveto_r(1.0 * scale[0], 6.0 * scale[1], 56.0 * scale[0],
              109.0 * scale[1], 93.0 * scale[0], 171.0 * scale[1])
    Curveto_r(27.0 * scale[0], 45.0 * scale[1], 27.0 * scale[0],
              47.0 * scale[1], 7.0 * scale[0], 52.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 3.0 * scale[1], -20.0 * scale[0],
              1.0 * scale[1], -20.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(530.0 * scale[0], 1861.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              15.0 * scale[1], 17.0 * scale[0], -22.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 15.0 *
              scale[0], -12.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 23.0 * scale[1], -21.0 * scale[0],
              28.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(556.0 * scale[0], 1812.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 13.0 * scale[0], -
              15.0 * scale[1], 17.0 * scale[0], -24.0 * scale[1])
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 12.0 * scale[0], -
              18.0 * scale[1], 19.0 * scale[0], -18.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              3.0 * scale[1], 2.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -13.0 * scale[0],
              15.0 * scale[1], -17.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -12.0 * scale[0],
              17.0 * scale[1], -19.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              3.0 * scale[1], -2.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(3067.0 * scale[0], 1799.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(600.0 * scale[0], 1746.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 7.0 * scale[0], -
              7.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 12.0 *
              scale[0], -2.0 * scale[1], 9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], -25.0 * scale[0],
              14.0 * scale[1], -25.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(1486.0 * scale[0], 1575.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -14.0 * scale[1], -23.0 * scale[0], -
              25.0 * scale[1], -31.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              5.0 * scale[1], -15.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -4.0 * scale[0], -
              8.0 * scale[1], -8.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -39.0 * scale[0], -
              4.0 * scale[1], -75.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-47.0 * scale[0], -14.0 * scale[1], -72.0 *
              scale[0], -28.0 * scale[1], -83.0 * scale[0], -45.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -13.0 * scale[1], -14.0 * scale[0], -
              27.0 * scale[1], -11.0 * scale[0], -31.0 * scale[1])
    Curveto_r(10.0 * scale[0], -9.0 * scale[1], -35.0 * scale[0], -
              83.0 * scale[1], -46.0 * scale[0], -76.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -7.0 * scale[0],
              1.0 * scale[1], -3.0 * scale[0], -5.0 * scale[1])
    Curveto_r(8.0 * scale[0], -14.0 * scale[1], -28.0 * scale[0], -
              74.0 * scale[1], -40.0 * scale[0], -64.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 4.0 * scale[1], -2.0 * scale[0], -
              1.0 * scale[1], 5.0 * scale[0], -10.0 * scale[1])
    Curveto_r(7.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0], -
              18.0 * scale[1], 5.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0], -
              18.0 * scale[1], -34.0 * scale[0], -39.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -22.0 * scale[1], -28.0 *
              scale[0], -38.0 * scale[1], -32.0 * scale[0], -35.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0], -
              3.0 * scale[1], -1.0 * scale[0], -12.0 * scale[1])
    Curveto_r(4.0 * scale[0], -12.0 * scale[1], 3.0 * scale[0], -
              15.0 * scale[1], -5.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -10.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -10.0 * scale[1])
    Curveto_r(5.0 * scale[0], -13.0 * scale[1], 3.0 * scale[0], -
              15.0 * scale[1], -8.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 8.0 * scale[1], -12.0 * scale[0],
              6.0 * scale[1], 0.0 * scale[0], -8.0 * scale[1])
    Curveto_r(8.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0], -
              17.0 * scale[1], 3.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              8.0 * scale[1], -9.0 * scale[0], -19.0 * scale[1])
    Curveto_r(1.0 * scale[0], -12.0 * scale[1], 7.0 * scale[0], -
              17.0 * scale[1], 19.0 * scale[0], -13.0 * scale[1])
    Curveto_r(10.0 * scale[0], 2.0 * scale[1], 18.0 * scale[0],
              0.0 * scale[1], 18.0 * scale[0], -6.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 9.0 * scale[0], -
              14.0 * scale[1], 20.0 * scale[0], -17.0 * scale[1])
    Curveto_r(11.0 * scale[0], -4.0 * scale[1], 17.0 * scale[0], -
              11.0 * scale[1], 14.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], -2.0 *
              scale[0], -8.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(14.0 * scale[0], 8.0 * scale[1], 74.0 * scale[0], -
              28.0 * scale[1], 64.0 * scale[0], -39.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -5.0 * scale[1], -1.0 *
              scale[0], -5.0 * scale[1], 5.0 * scale[0], -1.0 * scale[1])
    Curveto_r(16.0 * scale[0], 9.0 * scale[1], 56.0 * scale[0], -
              17.0 * scale[1], 45.0 * scale[0], -29.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -5.0 * scale[1], -1.0 *
              scale[0], -5.0 * scale[1], 6.0 * scale[0], -1.0 * scale[1])
    Curveto_r(7.0 * scale[0], 4.0 * scale[1], 24.0 * scale[0],
              1.0 * scale[1], 37.0 * scale[0], -8.0 * scale[1])
    Curveto_r(32.0 * scale[0], -21.0 * scale[1], 42.0 *
              scale[0], -20.0 * scale[1], 48.0 * scale[0], 5.0 * scale[1])
    Curveto_r(4.0 * scale[0], 13.0 * scale[1], 10.0 * scale[0],
              18.0 * scale[1], 18.0 * scale[0], 13.0 * scale[1])
    Curveto_r(7.0 * scale[0], -4.0 * scale[1], 10.0 *
              scale[0], -3.0 * scale[1], 5.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 17.0 * scale[1], 55.0 * scale[0],
              128.0 * scale[1], 68.0 * scale[0], 115.0 * scale[1])
    Curveto_r(4.0 * scale[0], -4.0 * scale[1], 4.0 * scale[0],
              1.0 * scale[1], 0.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 15.0 * scale[1], -4.0 * scale[0],
              17.0 * scale[1], 7.0 * scale[0], 11.0 * scale[1])
    Curveto_r(12.0 * scale[0], -7.0 * scale[1], 12.0 *
              scale[0], -6.0 * scale[1], 1.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 13.0 * scale[1], -10.0 * scale[0],
              17.0 * scale[1], 3.0 * scale[0], 21.0 * scale[1])
    Curveto_r(8.0 * scale[0], 4.0 * scale[1], 12.0 * scale[0],
              13.0 * scale[1], 9.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], -1.0 * scale[0],
              15.0 * scale[1], 5.0 * scale[0], 15.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0],
              13.0 * scale[1], 30.0 * scale[0], 30.0 * scale[1])
    Curveto_r(10.0 * scale[0], 16.0 * scale[1], 21.0 * scale[0],
              27.0 * scale[1], 26.0 * scale[0], 22.0 * scale[1])
    Curveto_r(5.0 * scale[0], -4.0 * scale[1], 5.0 *
              scale[0], -2.0 * scale[1], 1.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 7.0 * scale[1], 0.0 * scale[0],
              26.0 * scale[1], 9.0 * scale[0], 42.0 * scale[1])
    Curveto_r(11.0 * scale[0], 23.0 * scale[1], 13.0 * scale[0],
              40.0 * scale[1], 7.0 * scale[0], 68.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 44.0 * scale[1], -5.0 * scale[0],
              66.0 * scale[1], 11.0 * scale[0], 56.0 * scale[1])
    Curveto_r(9.0 * scale[0], -5.0 * scale[1], 9.0 *
              scale[0], -3.0 * scale[1], 0.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 8.0 * scale[1], -15.0 * scale[0],
              35.0 * scale[1], -19.0 * scale[0], 59.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 25.0 * scale[1], -10.0 * scale[0],
              38.0 * scale[1], -12.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -23.0 * scale[0], -
              44.0 * scale[1], -45.0 * scale[0], -80.0 * scale[1])
    Curveto_r(-22.0 * scale[0], -36.0 * scale[1], -45.0 *
              scale[0], -74.0 * scale[1], -52.0 * scale[0], -85.0 * scale[1])
    Curveto_r(-61.0 * scale[0], -110.0 * scale[1], -79.0 * scale[0], -
              135.0 * scale[1], -95.0 * scale[0], -135.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 0.0 * scale[1], -23.0 * scale[0],
              6.0 * scale[1], -29.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 19.0 * scale[1], 11.0 * scale[0],
              72.0 * scale[1], 171.0 * scale[0], 334.0 * scale[1])
    Curveto_r(23.0 * scale[0], 37.0 * scale[1], 18.0 * scale[0],
              44.0 * scale[1], -6.0 * scale[0], 7.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#c56c38')
    te.end_fill()
    Moveto(2109.0 * scale[0], 2643.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -11.0 * scale[1], -10.0 *
              scale[0], -14.0 * scale[1], -1.0 * scale[0], -9.0 * scale[1])
    Curveto_r(15.0 * scale[0], 9.0 * scale[1], 15.0 * scale[0],
              1.0 * scale[1], 1.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -11.0 * scale[1], -14.0 * scale[0], -
              17.0 * scale[1], -19.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -12.0 * scale[0],
              0.0 * scale[1], -16.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -8.0 * scale[1], -3.0 *
              scale[0], -9.0 * scale[1], 6.0 * scale[0], -4.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 11.0 * scale[0],
              3.0 * scale[1], 8.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -11.0 * scale[0], -
              13.0 * scale[1], -17.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 1.0 * scale[1], -10.0 *
              scale[0], -2.0 * scale[1], -6.0 * scale[0], -7.0 * scale[1])
    Curveto_r(7.0 * scale[0], -13.0 * scale[1], -33.0 * scale[0], -
              93.0 * scale[1], -44.0 * scale[0], -87.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 3.0 * scale[1], -7.0 * scale[0], -
              8.0 * scale[1], -6.0 * scale[0], -24.0 * scale[1])
    Curveto_r(1.0 * scale[0], -16.0 * scale[1], -1.0 * scale[0], -
              27.0 * scale[1], -5.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 2.0 * scale[1], -19.0 * scale[0], -
              17.0 * scale[1], -33.0 * scale[0], -44.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -36.0 * scale[1], -24.0 *
              scale[0], -50.0 * scale[1], -15.0 * scale[0], -59.0 * scale[1])
    Curveto_r(14.0 * scale[0], -14.0 * scale[1], 32.0 *
              scale[0], -16.0 * scale[1], 24.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 12.0 * scale[1], 19.0 * scale[0],
              33.0 * scale[1], 29.0 * scale[0], 23.0 * scale[1])
    Curveto_r(5.0 * scale[0], -4.0 * scale[1], 5.0 *
              scale[0], -1.0 * scale[1], 1.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 17.0 * scale[1], 12.0 * scale[0],
              55.0 * scale[1], 26.0 * scale[0], 47.0 * scale[1])
    Curveto_r(7.0 * scale[0], -4.0 * scale[1], 8.0 *
              scale[0], -3.0 * scale[1], 4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 16.0 * scale[1], 22.0 * scale[0],
              74.0 * scale[1], 36.0 * scale[0], 66.0 * scale[1])
    Curveto_r(7.0 * scale[0], -4.0 * scale[1], 8.0 *
              scale[0], -3.0 * scale[1], 4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 14.0 * scale[1], 22.0 * scale[0],
              75.0 * scale[1], 34.0 * scale[0], 67.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 12.0 * scale[0],
              0.0 * scale[1], 16.0 * scale[0], 6.0 * scale[1])
    Curveto_r(4.0 * scale[0], 8.0 * scale[1], 3.0 * scale[0],
              9.0 * scale[1], -4.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -9.0 * scale[1], -15.0 *
              scale[0], -1.0 * scale[1], -1.0 * scale[0], 25.0 * scale[1])
    Curveto_r(5.0 * scale[0], 11.0 * scale[1], 14.0 * scale[0],
              17.0 * scale[1], 19.0 * scale[0], 14.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 3.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 12.0 * scale[1], -3.0 * scale[0],
              15.0 * scale[1], 6.0 * scale[0], 9.0 * scale[1])
    Curveto_r(10.0 * scale[0], -6.0 * scale[1], 11.0 *
              scale[0], -3.0 * scale[1], 2.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 11.0 * scale[1], -19.0 * scale[0],
              21.0 * scale[1], -29.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], 2.0 * scale[1], 3.0 * scale[0], 9.0 * scale[1])
    Curveto_r(15.0 * scale[0], 7.0 * scale[1], 16.0 * scale[0],
              9.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 1.0 * scale[1], -23.0 * scale[0], -
              7.0 * scale[1], -30.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(1960.0 * scale[0], 2390.0 * scale[1], x, y)
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
    Moveto(1890.0 * scale[0], 2269.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -4.0 * scale[0], -
              8.0 * scale[1], -9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -12.0 * scale[0],
              1.0 * scale[1], -15.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -10.0 * scale[1], 13.0 *
              scale[0], -9.0 * scale[1], 31.0 * scale[0], 2.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 15.0 * scale[0],
              2.0 * scale[1], 19.0 * scale[0], -4.0 * scale[1])
    Curveto_r(4.0 * scale[0], -7.0 * scale[1], 3.0 * scale[0], -
              9.0 * scale[1], -3.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -15.0 * scale[0], -
              5.0 * scale[1], -22.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -23.0 * scale[1], -14.0 *
              scale[0], -24.0 * scale[1], -28.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 12.0 * scale[1], -15.0 * scale[0],
              11.0 * scale[1], -9.0 * scale[0], -9.0 * scale[1])
    Curveto_r(4.0 * scale[0], -12.0 * scale[1], 3.0 * scale[0], -
              22.0 * scale[1], -2.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -26.0 * scale[0], -
              33.0 * scale[1], -47.0 * scale[0], -72.0 * scale[1])
    Curveto_r(-53.0 * scale[0], -100.0 * scale[1], -65.0 * scale[0], -
              122.0 * scale[1], -133.0 * scale[0], -235.0 * scale[1])
    Curveto_r(-61.0 * scale[0], -102.0 * scale[1], -91.0 * scale[0], -
              154.0 * scale[1], -137.0 * scale[0], -238.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -27.0 * scale[1], -62.0 * scale[0], -
              108.0 * scale[1], -105.0 * scale[0], -180.0 * scale[1])
    Curveto_r(-111.0 * scale[0], -187.0 * scale[1], -124.0 *
              scale[0], -214.0 * scale[1], -109.0 * scale[0], -231.0 * scale[1])
    Curveto_r(6.0 * scale[0], -8.0 * scale[1], 19.0 * scale[0], -
              14.0 * scale[1], 29.0 * scale[0], -14.0 * scale[1])
    Curveto_r(16.0 * scale[0], 0.0 * scale[1], 34.0 * scale[0],
              25.0 * scale[1], 95.0 * scale[0], 135.0 * scale[1])
    Curveto_r(7.0 * scale[0], 11.0 * scale[1], 30.0 * scale[0],
              50.0 * scale[1], 53.0 * scale[0], 88.0 * scale[1])
    Curveto_r(23.0 * scale[0], 37.0 * scale[1], 42.0 * scale[0],
              70.0 * scale[1], 42.0 * scale[0], 73.0 * scale[1])
    Curveto_r(0.0 * scale[0], 3.0 * scale[1], 38.0 * scale[0],
              69.0 * scale[1], 84.0 * scale[0], 147.0 * scale[1])
    Curveto_r(82.0 * scale[0], 140.0 * scale[1], 95.0 * scale[0],
              162.0 * scale[1], 184.0 * scale[0], 322.0 * scale[1])
    Curveto_r(24.0 * scale[0], 44.0 * scale[1], 50.0 * scale[0],
              87.0 * scale[1], 56.0 * scale[0], 95.0 * scale[1])
    Curveto_r(7.0 * scale[0], 8.0 * scale[1], 23.0 * scale[0],
              36.0 * scale[1], 37.0 * scale[0], 63.0 * scale[1])
    Curveto_r(18.0 * scale[0], 35.0 * scale[1], 30.0 * scale[0],
              47.0 * scale[1], 46.0 * scale[0], 47.0 * scale[1])
    Curveto_r(22.0 * scale[0], 0.0 * scale[1], 32.0 * scale[0], -
              15.0 * scale[1], 14.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -4.0 * scale[1], -63.0 * scale[0], -
              89.0 * scale[1], -58.0 * scale[0], -94.0 * scale[1])
    Curveto_r(7.0 * scale[0], -8.0 * scale[1], 663.0 * scale[0],
              14.0 * scale[1], 942.0 * scale[0], 31.0 * scale[1])
    Curveto_r(151.0 * scale[0], 9.0 * scale[1], 277.0 * scale[0],
              22.0 * scale[1], 318.0 * scale[0], 32.0 * scale[1])
    Lineto_r(67.0 * scale[0], 17.0 * scale[1])
    Lineto_r(0.0 * scale[0], 46.0 * scale[1])
    Lineto_r(0.0 * scale[0], 46.0 * scale[1])
    Lineto_r(-132.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-185.0 * scale[0], -17.0 * scale[1], -449.0 *
              scale[0], -33.0 * scale[1], -743.0 * scale[0], -44.0 * scale[1])
    Curveto_r(-279.0 * scale[0], -11.0 * scale[1], -368.0 *
              scale[0], -11.0 * scale[1], -270.0 * scale[0], 0.0 * scale[1])
    Lineto_r(60.0 * scale[0], 7.0 * scale[1])
    Lineto_r(-62.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-35.0 * scale[0], 1.0 * scale[1], -63.0 *
              scale[0], -2.0 * scale[1], -63.0 * scale[0], -8.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -19.0 *
              scale[0], -3.0 * scale[1], -44.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 8.0 * scale[1], -48.0 * scale[0],
              11.0 * scale[1], -52.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -3.0 * scale[1], -4.0 * scale[0],
              1.0 * scale[1], -2.0 * scale[0], 9.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], 11.0 * scale[0],
              14.0 * scale[1], 18.0 * scale[0], 12.0 * scale[1])
    Curveto_r(11.0 * scale[0], -3.0 * scale[1], 11.0 * scale[0],
              0.0 * scale[1], 0.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 13.0 * scale[1], -10.0 *
              scale[0], 15.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(20.0 * scale[0], -8.0 * scale[1], 21.0 * scale[0],
              0.0 * scale[1], 0.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 18.0 * scale[1], -54.0 * scale[0],
              22.0 * scale[1], -54.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(413.0 * scale[0], 2253.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(3163.0 * scale[0], 2253.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(370.0 * scale[0], 2198.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -35.0 * scale[1], 4.0 * scale[0], -
              48.0 * scale[1], 15.0 * scale[0], -49.0 * scale[1])
    Curveto_r(8.0 * scale[0], -1.0 * scale[1], 18.0 * scale[0], -
              2.0 * scale[1], 23.0 * scale[0], -3.0 * scale[1])
    Curveto_r(4.0 * scale[0], -2.0 * scale[1], 25.0 * scale[0], -
              7.0 * scale[1], 47.0 * scale[0], -13.0 * scale[1])
    Curveto_r(72.0 * scale[0], -20.0 * scale[1], 507.0 * scale[0], -
              44.0 * scale[1], 1046.0 * scale[0], -59.0 * scale[1])
    Lineto_r(236.0 * scale[0], -6.0 * scale[1])
    Lineto_r(32.0 * scale[0], 51.0 * scale[1])
    Curveto_r(17.0 * scale[0], 28.0 * scale[1], 31.0 * scale[0],
              53.0 * scale[1], 31.0 * scale[0], 55.0 * scale[1])
    Curveto_r(0.0 * scale[0], 1.0 * scale[1], -136.0 * scale[0],
              6.0 * scale[1], -302.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-316.0 * scale[0], 7.0 * scale[1], -742.0 * scale[0],
              28.0 * scale[1], -985.0 * scale[0], 50.0 * scale[1])
    Lineto_r(-143.0 * scale[0], 13.0 * scale[1])
    Lineto_r(0.0 * scale[0], -48.0 * scale[1])
    te.end_fill()
    Moveto(528.0 * scale[0], 2243.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(3053.0 * scale[0], 2243.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(653.0 * scale[0], 2233.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 25.0 *
              scale[0], -2.0 * scale[1], 35.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -27.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(2923.0 * scale[0], 2233.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(798.0 * scale[0], 2223.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 30.0 *
              scale[0], -2.0 * scale[1], 40.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 0.0 * scale[1], -30.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(2768.0 * scale[0], 2223.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 30.0 *
              scale[0], -2.0 * scale[1], 40.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 0.0 * scale[1], -30.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(978.0 * scale[0], 2213.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 30.0 *
              scale[0], -2.0 * scale[1], 40.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 0.0 * scale[1], -30.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(2598.0 * scale[0], 2213.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 30.0 *
              scale[0], -2.0 * scale[1], 40.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 0.0 * scale[1], -30.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(1188.0 * scale[0], 2203.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(18.0 * scale[0], -2.0 * scale[1], 45.0 *
              scale[0], -2.0 * scale[1], 60.0 * scale[0], 0.0 * scale[1])
    Curveto_r(15.0 * scale[0], 2.0 * scale[1], 0.0 * scale[0],
              4.0 * scale[1], -33.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-33.0 * scale[0], 0.0 * scale[1], -45.0 *
              scale[0], -2.0 * scale[1], -27.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(1640.0 * scale[0], 2200.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-165.0 * scale[0], -6.0 * scale[1])
    Lineto_r(168.0 * scale[0], -2.0 * scale[1])
    Curveto_r(106.0 * scale[0], -1.0 * scale[1], 167.0 * scale[0],
              2.0 * scale[1], 167.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -1.0 * scale[0],
              9.0 * scale[1], -2.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -1.0 * scale[1], -77.0 * scale[0], -
              5.0 * scale[1], -168.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(2368.0 * scale[0], 2203.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(18.0 * scale[0], -2.0 * scale[1], 45.0 *
              scale[0], -2.0 * scale[1], 60.0 * scale[0], 0.0 * scale[1])
    Curveto_r(15.0 * scale[0], 2.0 * scale[1], 0.0 * scale[0],
              4.0 * scale[1], -33.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-33.0 * scale[0], 0.0 * scale[1], -45.0 *
              scale[0], -2.0 * scale[1], -27.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(3171.0 * scale[0], 2114.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(504.0 * scale[0], 1908.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -7.0 * scale[1], -3.0 *
              scale[0], -8.0 * scale[1], 6.0 * scale[0], -3.0 * scale[1])
    Curveto_r(10.0 * scale[0], 6.0 * scale[1], 12.0 * scale[0],
              4.0 * scale[1], 7.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -11.0 * scale[1], -3.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 9.0 * scale[0],
              2.0 * scale[1], 5.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -9.0 * scale[1], -3.0 * scale[0], -
              15.0 * scale[1], 2.0 * scale[0], -12.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], 22.0 * scale[0], -
              17.0 * scale[1], 40.0 * scale[0], -45.0 * scale[1])
    Curveto_r(35.0 * scale[0], -57.0 * scale[1], 38.0 * scale[0], -
              67.0 * scale[1], 14.0 * scale[0], -48.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 13.0 * scale[1], -17.0 * scale[0],
              12.0 * scale[1], -4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(8.0 * scale[0], -9.0 * scale[1], 16.0 * scale[0], -
              15.0 * scale[1], 19.0 * scale[0], -12.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 32.0 * scale[0], -
              15.0 * scale[1], 32.0 * scale[0], -27.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -8.0 * scale[0], -
              4.0 * scale[1], -17.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 13.0 * scale[1], -17.0 * scale[0],
              12.0 * scale[1], -4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(8.0 * scale[0], -9.0 * scale[1], 16.0 * scale[0], -
              15.0 * scale[1], 19.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 14.0 * scale[0], -
              3.0 * scale[1], 24.0 * scale[0], -12.0 * scale[1])
    Curveto_r(11.0 * scale[0], -10.0 * scale[1], 31.0 * scale[0], -
              18.0 * scale[1], 46.0 * scale[0], -19.0 * scale[1])
    Curveto_r(98.0 * scale[0], -7.0 * scale[1], 457.0 * scale[0], -
              25.0 * scale[1], 613.0 * scale[0], -30.0 * scale[1])
    Lineto_r(186.0 * scale[0], -7.0 * scale[1])
    Lineto_r(27.0 * scale[0], 49.0 * scale[1])
    Curveto_r(16.0 * scale[0], 27.0 * scale[1], 40.0 * scale[0],
              69.0 * scale[1], 53.0 * scale[0], 94.0 * scale[1])
    Curveto_r(14.0 * scale[0], 25.0 * scale[1], 29.0 * scale[0],
              49.0 * scale[1], 34.0 * scale[0], 54.0 * scale[1])
    Curveto_r(19.0 * scale[0], 21.0 * scale[1], 8.0 * scale[0],
              32.0 * scale[1], -25.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -2.0 * scale[1], -178.0 * scale[0],
              1.0 * scale[1], -353.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-282.0 * scale[0], 10.0 * scale[1], -410.0 * scale[0],
              17.0 * scale[1], -655.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-45.0 * scale[0], 3.0 * scale[1], -69.0 * scale[0],
              1.0 * scale[1], -74.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(2780.0 * scale[0], 1899.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-140.0 * scale[0], -10.0 * scale[1], -423.0 *
              scale[0], -21.0 * scale[1], -627.0 * scale[0], -25.0 * scale[1])
    Lineto_r(-373.0 * scale[0], -7.0 * scale[1])
    Lineto_r(-39.0 * scale[0], -66.0 * scale[1])
    Curveto_r(-36.0 * scale[0], -61.0 * scale[1], -81.0 * scale[0], -
              146.0 * scale[1], -81.0 * scale[0], -153.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], 819.0 * scale[0],
              11.0 * scale[1], 1005.0 * scale[0], 21.0 * scale[1])
    Curveto_r(291.0 * scale[0], 16.0 * scale[1], 335.0 * scale[0],
              20.0 * scale[1], 348.0 * scale[0], 28.0 * scale[1])
    Curveto_r(7.0 * scale[0], 4.0 * scale[1], 15.0 * scale[0],
              8.0 * scale[1], 19.0 * scale[0], 8.0 * scale[1])
    Curveto_r(3.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              4.0 * scale[1], 15.0 * scale[0], 9.0 * scale[1])
    Curveto_r(5.0 * scale[0], 5.0 * scale[1], 2.0 * scale[0],
              6.0 * scale[1], -6.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -5.0 * scale[1], -12.0 *
              scale[0], -3.0 * scale[1], -9.0 * scale[0], 6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], 10.0 * scale[0],
              13.0 * scale[1], 15.0 * scale[0], 12.0 * scale[1])
    Curveto_r(5.0 * scale[0], -1.0 * scale[1], 10.0 * scale[0],
              7.0 * scale[1], 11.0 * scale[0], 18.0 * scale[1])
    Curveto_r(1.0 * scale[0], 10.0 * scale[1], 3.0 * scale[0],
              28.0 * scale[1], 4.0 * scale[0], 38.0 * scale[1])
    Curveto_r(1.0 * scale[0], 11.0 * scale[1], 5.0 * scale[0],
              18.0 * scale[1], 9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(4.0 * scale[0], -2.0 * scale[1], 15.0 * scale[0],
              16.0 * scale[1], 24.0 * scale[0], 41.0 * scale[1])
    Curveto_r(10.0 * scale[0], 24.0 * scale[1], 21.0 * scale[0],
              42.0 * scale[1], 25.0 * scale[0], 40.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 6.0 * scale[0],
              4.0 * scale[1], 3.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 17.0 * scale[1], -12.0 * scale[0],
              20.0 * scale[1], -47.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-22.0 * scale[0], -1.0 * scale[1], -156.0 * scale[0], -
              10.0 * scale[1], -296.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(3096.0 * scale[0], 1825.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -26.0 * scale[1], -7.0 *
              scale[0], -32.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(6.0 * scale[0], 10.0 * scale[1], 9.0 * scale[0],
              21.0 * scale[1], 6.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 3.0 * scale[1], -7.0 * scale[0], -
              2.0 * scale[1], -11.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(3070.0 * scale[0], 1770.0 * scale[1], x, y)
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
    Moveto(650.0 * scale[0], 1675.0 * scale[1], x, y)
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
    Moveto(2979.0 * scale[0], 1633.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(16.0 * scale[0], 13.0 * scale[1], 21.0 * scale[0],
              21.0 * scale[1], 13.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              8.0 * scale[1], -17.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(755.0 * scale[0], 1570.0 * scale[1], x, y)
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
    Moveto(2909.0 * scale[0], 1553.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-24.0 * scale[0], -28.0 * scale[1])
    Lineto_r(28.0 * scale[0], 24.0 * scale[1])
    Curveto_r(25.0 * scale[0], 23.0 * scale[1], 32.0 * scale[0],
              31.0 * scale[1], 24.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0], -
              12.0 * scale[1], -28.0 * scale[0], -27.0 * scale[1])
    te.end_fill()
    Moveto(852.0 * scale[0], 1494.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(10.0 * scale[0], -10.0 * scale[1], 20.0 * scale[0], -
              16.0 * scale[1], 22.0 * scale[0], -13.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              11.0 * scale[1], -17.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 13.0 * scale[1], -21.0 * scale[0],
              12.0 * scale[1], -5.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(2839.0 * scale[0], 1493.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(16.0 * scale[0], 13.0 * scale[1], 21.0 * scale[0],
              21.0 * scale[1], 13.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              8.0 * scale[1], -17.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(938.0 * scale[0], 1473.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(1008.0 * scale[0], 1463.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(2688.0 * scale[0], 1463.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(1098.0 * scale[0], 1453.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(2608.0 * scale[0], 1453.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(1198.0 * scale[0], 1443.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(2508.0 * scale[0], 1443.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(2373.0 * scale[0], 1433.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(2198.0 * scale[0], 1423.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 30.0 *
              scale[0], -2.0 * scale[1], 40.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 0.0 * scale[1], -30.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(1577.0 * scale[0], 1321.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -17.0 * scale[1], -3.0 *
              scale[0], -21.0 * scale[1], 5.0 * scale[0], -13.0 * scale[1])
    Curveto_r(5.0 * scale[0], 5.0 * scale[1], 8.0 * scale[0],
              16.0 * scale[1], 6.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], -7.0 * scale[0],
              3.0 * scale[1], -11.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(1476.0 * scale[0], 1183.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(1360.0 * scale[0], 950.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 0.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#9d4510')
    te.end_fill()
    Moveto(2116.0 * scale[0], 2642.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 6.0 * scale[0], -
              7.0 * scale[1], 19.0 * scale[0], -4.0 * scale[1])
    Curveto_r(27.0 * scale[0], 5.0 * scale[1], 31.0 * scale[0], -
              6.0 * scale[1], 14.0 * scale[0], -41.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -21.0 * scale[1], -10.0 *
              scale[0], -22.0 * scale[1], 6.0 * scale[0], -2.0 * scale[1])
    Curveto_r(8.0 * scale[0], 11.0 * scale[1], 14.0 * scale[0],
              26.0 * scale[1], 13.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 17.0 * scale[1], -43.0 * scale[0],
              26.0 * scale[1], -52.0 * scale[0], 12.0 * scale[1])
    te.end_fill()
    Moveto(2046.0 * scale[0], 2523.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(2033.0 * scale[0], 2398.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-15.0 * scale[0], -18.0 * scale[1], -35.0 *
              scale[0], -58.0 * scale[1], -29.0 * scale[0], -58.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              16.0 * scale[1], 25.0 * scale[0], 35.0 * scale[1])
    Curveto_r(20.0 * scale[0], 35.0 * scale[1], 22.0 * scale[0],
              46.0 * scale[1], 4.0 * scale[0], 23.0 * scale[1])
    te.end_fill()
    Moveto(1966.0 * scale[0], 2383.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(1845.0 * scale[0], 2297.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-27.0 * scale[0], -27.0 * scale[1], -35.0 *
              scale[0], -43.0 * scale[1], -35.0 * scale[0], -70.0 * scale[1])
    Curveto_r(0.0 * scale[0], -30.0 * scale[1], 3.0 * scale[0], -
              34.0 * scale[1], 23.0 * scale[0], -30.0 * scale[1])
    Curveto_r(15.0 * scale[0], 3.0 * scale[1], 22.0 * scale[0],
              12.0 * scale[1], 23.0 * scale[0], 29.0 * scale[1])
    Curveto_r(2.0 * scale[0], 34.0 * scale[1], 22.0 * scale[0],
              54.0 * scale[1], 54.0 * scale[0], 54.0 * scale[1])
    Curveto_r(32.0 * scale[0], 0.0 * scale[1], 60.0 * scale[0], -
              27.0 * scale[1], 60.0 * scale[0], -58.0 * scale[1])
    Curveto_r(0.0 * scale[0], -15.0 * scale[1], 6.0 * scale[0], -
              22.0 * scale[1], 20.0 * scale[0], -22.0 * scale[1])
    Curveto_r(29.0 * scale[0], 0.0 * scale[1], 34.0 * scale[0],
              21.0 * scale[1], 16.0 * scale[0], 65.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 20.0 * scale[1], -14.0 * scale[0],
              40.0 * scale[1], -12.0 * scale[0], 44.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], -3.0 * scale[0],
              7.0 * scale[1], -12.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 1.0 * scale[1], -36.0 * scale[0],
              5.0 * scale[1], -59.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-39.0 * scale[0], 6.0 * scale[1], -45.0 * scale[0],
              4.0 * scale[1], -78.0 * scale[0], -29.0 * scale[1])
    te.end_fill()
    Moveto(3218.0 * scale[0], 2253.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(438.0 * scale[0], 2243.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 32.0 *
              scale[0], -2.0 * scale[1], 45.0 * scale[0], 0.0 * scale[1])
    Curveto_r(12.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              4.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 0.0 * scale[1], -35.0 *
              scale[0], -2.0 * scale[1], -22.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(3118.0 * scale[0], 2243.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 30.0 *
              scale[0], -2.0 * scale[1], 40.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 0.0 * scale[1], -30.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(558.0 * scale[0], 2233.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 32.0 *
              scale[0], -2.0 * scale[1], 45.0 * scale[0], 0.0 * scale[1])
    Curveto_r(12.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              4.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 0.0 * scale[1], -35.0 *
              scale[0], -2.0 * scale[1], -22.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(3008.0 * scale[0], 2233.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 30.0 *
              scale[0], -2.0 * scale[1], 40.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 0.0 * scale[1], -30.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(693.0 * scale[0], 2223.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(15.0 * scale[0], -2.0 * scale[1], 37.0 *
              scale[0], -2.0 * scale[1], 50.0 * scale[0], 0.0 * scale[1])
    Curveto_r(12.0 * scale[0], 2.0 * scale[1], 0.0 * scale[0],
              4.0 * scale[1], -28.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-27.0 * scale[0], 0.0 * scale[1], -38.0 *
              scale[0], -2.0 * scale[1], -22.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(2868.0 * scale[0], 2223.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 32.0 *
              scale[0], -2.0 * scale[1], 45.0 * scale[0], 0.0 * scale[1])
    Curveto_r(12.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              4.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 0.0 * scale[1], -35.0 *
              scale[0], -2.0 * scale[1], -22.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(828.0 * scale[0], 2213.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(17.0 * scale[0], -2.0 * scale[1], 47.0 *
              scale[0], -2.0 * scale[1], 65.0 * scale[0], 0.0 * scale[1])
    Curveto_r(17.0 * scale[0], 2.0 * scale[1], 3.0 * scale[0],
              4.0 * scale[1], -33.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-36.0 * scale[0], 0.0 * scale[1], -50.0 *
              scale[0], -2.0 * scale[1], -32.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(2718.0 * scale[0], 2213.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(18.0 * scale[0], -2.0 * scale[1], 45.0 *
              scale[0], -2.0 * scale[1], 60.0 * scale[0], 0.0 * scale[1])
    Curveto_r(15.0 * scale[0], 2.0 * scale[1], 0.0 * scale[0],
              4.0 * scale[1], -33.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-33.0 * scale[0], 0.0 * scale[1], -45.0 *
              scale[0], -2.0 * scale[1], -27.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(1017.0 * scale[0], 2203.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(18.0 * scale[0], -2.0 * scale[1], 50.0 *
              scale[0], -2.0 * scale[1], 70.0 * scale[0], 0.0 * scale[1])
    Curveto_r(21.0 * scale[0], 2.0 * scale[1], 7.0 * scale[0],
              4.0 * scale[1], -32.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-38.0 * scale[0], 0.0 * scale[1], -55.0 *
              scale[0], -2.0 * scale[1], -38.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(2507.0 * scale[0], 2203.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(18.0 * scale[0], -2.0 * scale[1], 50.0 *
              scale[0], -2.0 * scale[1], 70.0 * scale[0], 0.0 * scale[1])
    Curveto_r(21.0 * scale[0], 2.0 * scale[1], 7.0 * scale[0],
              4.0 * scale[1], -32.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-38.0 * scale[0], 0.0 * scale[1], -55.0 *
              scale[0], -2.0 * scale[1], -38.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(1258.0 * scale[0], 2193.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(29.0 * scale[0], -2.0 * scale[1], 74.0 *
              scale[0], -2.0 * scale[1], 100.0 * scale[0], 0.0 * scale[1])
    Curveto_r(26.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              3.0 * scale[1], -53.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-55.0 * scale[0], 0.0 * scale[1], -76.0 *
              scale[0], -1.0 * scale[1], -47.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(2253.0 * scale[0], 2193.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(26.0 * scale[0], -2.0 * scale[1], 67.0 *
              scale[0], -2.0 * scale[1], 90.0 * scale[0], 0.0 * scale[1])
    Curveto_r(23.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              3.0 * scale[1], -48.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-49.0 * scale[0], 0.0 * scale[1], -68.0 *
              scale[0], -1.0 * scale[1], -42.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(1623.0 * scale[0], 2183.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(31.0 * scale[0], -2.0 * scale[1], 83.0 *
              scale[0], -2.0 * scale[1], 115.0 * scale[0], 0.0 * scale[1])
    Curveto_r(31.0 * scale[0], 2.0 * scale[1], 5.0 * scale[0],
              3.0 * scale[1], -58.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-63.0 * scale[0], 0.0 * scale[1], -89.0 *
              scale[0], -1.0 * scale[1], -57.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(1938.0 * scale[0], 2183.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(2038.0 * scale[0], 2183.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(430.0 * scale[0], 2123.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -15.0 * scale[1], 52.0 * scale[0], -
              168.0 * scale[1], 66.0 * scale[0], -193.0 * scale[1])
    Curveto_r(22.0 * scale[0], -41.0 * scale[1], 16.0 * scale[0], -
              10.0 * scale[1], -11.0 * scale[0], 55.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 60.0 * scale[1], -32.0 * scale[0],
              101.0 * scale[1], -17.0 * scale[0], 91.0 * scale[1])
    Curveto_r(16.0 * scale[0], -10.0 * scale[1], 482.0 * scale[0], -
              35.0 * scale[1], 857.0 * scale[0], -47.0 * scale[1])
    Curveto_r(209.0 * scale[0], -7.0 * scale[1], 381.0 * scale[0], -
              13.0 * scale[1], 383.0 * scale[0], -14.0 * scale[1])
    Curveto_r(1.0 * scale[0], -1.0 * scale[1], -16.0 * scale[0], -
              32.0 * scale[1], -38.0 * scale[0], -70.0 * scale[1])
    Curveto_r(-41.0 * scale[0], -66.0 * scale[1], -45.0 *
              scale[0], -83.0 * scale[1], -17.0 * scale[0], -72.0 * scale[1])
    Curveto_r(12.0 * scale[0], 4.0 * scale[1], 117.0 * scale[0],
              177.0 * scale[1], 117.0 * scale[0], 192.0 * scale[1])
    Curveto_r(0.0 * scale[0], 3.0 * scale[1], -78.0 * scale[0],
              5.0 * scale[1], -172.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-299.0 * scale[0], 0.0 * scale[1], -1135.0 * scale[0],
              41.0 * scale[1], -1160.0 * scale[0], 56.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -8.0 * scale[0],
              1.0 * scale[1], -8.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(3090.0 * scale[0], 2118.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-245.0 * scale[0], -21.0 * scale[1], -836.0 *
              scale[0], -48.0 * scale[1], -1082.0 * scale[0], -48.0 * scale[1])
    Lineto_r(-146.0 * scale[0], 0.0 * scale[1])
    Lineto_r(-54.0 * scale[0], -92.0 * scale[1])
    Curveto_r(-29.0 * scale[0], -51.0 * scale[1], -54.0 * scale[0], -
              96.0 * scale[1], -56.0 * scale[0], -100.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -17.0 * scale[1], 34.0 *
              scale[0], -7.0 * scale[1], 43.0 * scale[0], 10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 10.0 * scale[1], 23.0 * scale[0],
              44.0 * scale[1], 39.0 * scale[0], 74.0 * scale[1])
    Lineto_r(29.0 * scale[0], 55.0 * scale[1])
    Lineto_r(271.0 * scale[0], 7.0 * scale[1])
    Curveto_r(244.0 * scale[0], 6.0 * scale[1], 648.0 * scale[0],
              25.0 * scale[1], 922.0 * scale[0], 42.0 * scale[1])
    Lineto_r(102.0 * scale[0], 7.0 * scale[1])
    Lineto_r(-8.0 * scale[0], -39.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -21.0 * scale[1], -11.0 * scale[0], -
              57.0 * scale[1], -15.0 * scale[0], -79.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -22.0 * scale[1], -5.0 * scale[0], -
              37.0 * scale[1], -1.0 * scale[0], -34.0 * scale[1])
    Curveto_r(9.0 * scale[0], 9.0 * scale[1], 38.0 * scale[0],
              156.0 * scale[1], 34.0 * scale[0], 181.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 22.0 * scale[1], -5.0 * scale[0],
              23.0 * scale[1], -78.0 * scale[0], 16.0 * scale[1])
    te.end_fill()
    Moveto(3106.0 * scale[0], 1865.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -26.0 * scale[1], -7.0 *
              scale[0], -32.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(6.0 * scale[0], 10.0 * scale[1], 9.0 * scale[0],
              21.0 * scale[1], 6.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 3.0 * scale[1], -7.0 * scale[0], -
              2.0 * scale[1], -11.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(3085.0 * scale[0], 1819.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0], -
              12.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 17.0 * scale[1], 1.0 * scale[0],
              20.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(610.0 * scale[0], 1736.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(680.0 * scale[0], 1655.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(46.0 * scale[0], -52.0 * scale[1], 136.0 * scale[0], -
              130.0 * scale[1], 180.0 * scale[0], -157.0 * scale[1])
    Curveto_r(16.0 * scale[0], -10.0 * scale[1], 83.0 * scale[0], -
              22.0 * scale[1], 185.0 * scale[0], -32.0 * scale[1])
    Curveto_r(88.0 * scale[0], -10.0 * scale[1], 172.0 * scale[0], -
              19.0 * scale[1], 187.0 * scale[0], -22.0 * scale[1])
    Lineto_r(26.0 * scale[0], -5.0 * scale[1])
    Lineto_r(-89.0 * scale[0], -155.0 * scale[1])
    Curveto_r(-49.0 * scale[0], -85.0 * scale[1], -89.0 * scale[0], -
              160.0 * scale[1], -89.0 * scale[0], -167.0 * scale[1])
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 267.0 * scale[0], -
              170.0 * scale[1], 283.0 * scale[0], -164.0 * scale[1])
    Curveto_r(7.0 * scale[0], 3.0 * scale[1], 58.0 * scale[0],
              86.0 * scale[1], 115.0 * scale[0], 186.0 * scale[1])
    Curveto_r(100.0 * scale[0], 175.0 * scale[1], 103.0 * scale[0],
              182.0 * scale[1], 97.0 * scale[0], 226.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 25.0 * scale[1], -11.0 * scale[0],
              45.0 * scale[1], -15.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              18.0 * scale[1], 1.0 * scale[0], -40.0 * scale[1])
    Curveto_r(8.0 * scale[0], -35.0 * scale[1], 5.0 * scale[0], -
              47.0 * scale[1], -21.0 * scale[0], -98.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -31.0 * scale[1], -35.0 *
              scale[0], -64.0 * scale[1], -40.0 * scale[0], -72.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -8.0 * scale[1], -27.0 * scale[0], -
              44.0 * scale[1], -47.0 * scale[0], -80.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -36.0 * scale[1], -46.0 *
              scale[0], -78.0 * scale[1], -56.0 * scale[0], -95.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -16.0 * scale[1], -20.0 * scale[0], -
              38.0 * scale[1], -23.0 * scale[0], -47.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -10.0 * scale[1], -10.0 * scale[0], -
              18.0 * scale[1], -14.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -251.0 * scale[0],
              137.0 * scale[1], -264.0 * scale[0], 150.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 9.0 * scale[1], 9.0 * scale[0],
              44.0 * scale[1], 108.0 * scale[0], 214.0 * scale[1])
    Curveto_r(32.0 * scale[0], 55.0 * scale[1], 59.0 * scale[0],
              110.0 * scale[1], 61.0 * scale[0], 123.0 * scale[1])
    Curveto_r(4.0 * scale[0], 38.0 * scale[1], 24.0 * scale[0],
              52.0 * scale[1], 117.0 * scale[0], 80.0 * scale[1])
    Curveto_r(82.0 * scale[0], 24.0 * scale[1], 92.0 * scale[0],
              30.0 * scale[1], 119.0 * scale[0], 69.0 * scale[1])
    Curveto_r(33.0 * scale[0], 49.0 * scale[1], 35.0 * scale[0],
              54.0 * scale[1], 14.0 * scale[0], 54.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -25.0 * scale[0], -
              15.0 * scale[1], -36.0 * scale[0], -34.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -20.0 * scale[1], -31.0 *
              scale[0], -37.0 * scale[1], -47.0 * scale[0], -40.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -4.0 * scale[1], -60.0 * scale[0], -
              19.0 * scale[1], -100.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-55.0 * scale[0], -20.0 * scale[1], -76.0 *
              scale[0], -32.0 * scale[1], -83.0 * scale[0], -50.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -13.0 * scale[1], -15.0 * scale[0], -
              26.0 * scale[1], -22.0 * scale[0], -29.0 * scale[1])
    Curveto_r(-22.0 * scale[0], -8.0 * scale[1], -317.0 * scale[0],
              26.0 * scale[1], -353.0 * scale[0], 41.0 * scale[1])
    Curveto_r(-35.0 * scale[0], 14.0 * scale[1], -62.0 * scale[0],
              36.0 * scale[1], -169.0 * scale[0], 135.0 * scale[1])
    Curveto_r(-61.0 * scale[0], 57.0 * scale[1], -64.0 * scale[0],
              59.0 * scale[1], -25.0 * scale[0], 15.0 * scale[1])
    te.end_fill()
    Moveto(3000.0 * scale[0], 1680.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -18.0 * scale[1], -149.0 * scale[0], -
              167.0 * scale[1], -178.0 * scale[0], -178.0 * scale[1])
    Curveto_r(-35.0 * scale[0], -14.0 * scale[1], -236.0 *
              scale[0], -39.0 * scale[1], -427.0 * scale[0], -53.0 * scale[1])
    Curveto_r(-82.0 * scale[0], -6.0 * scale[1], -296.0 * scale[0], -
              12.0 * scale[1], -475.0 * scale[0], -12.0 * scale[1])
    Lineto_r(-324.0 * scale[0], -2.0 * scale[1])
    Lineto_r(-9.0 * scale[0], 42.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 39.0 * scale[1], -5.0 * scale[0],
              49.0 * scale[1], 27.0 * scale[0], 103.0 * scale[1])
    Curveto_r(41.0 * scale[0], 70.0 * scale[1], 41.0 * scale[0],
              70.0 * scale[1], 21.0 * scale[0], 70.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -30.0 * scale[0], -
              28.0 * scale[1], -50.0 * scale[0], -62.0 * scale[1])
    Curveto_r(-33.0 * scale[0], -56.0 * scale[1], -36.0 * scale[0], -
              66.0 * scale[1], -29.0 * scale[0], -107.0 * scale[1])
    Curveto_r(4.0 * scale[0], -26.0 * scale[1], 7.0 * scale[0], -
              50.0 * scale[1], 5.0 * scale[0], -54.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -12.0 * scale[1], 715.0 *
              scale[0], -1.0 * scale[1], 864.0 * scale[0], 12.0 * scale[1])
    Curveto_r(219.0 * scale[0], 20.0 * scale[1], 380.0 * scale[0],
              43.0 * scale[1], 412.0 * scale[0], 58.0 * scale[1])
    Curveto_r(49.0 * scale[0], 23.0 * scale[1], 202.0 * scale[0],
              193.0 * scale[1], 174.0 * scale[0], 193.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              5.0 * scale[1], -11.0 * scale[0], -10.0 * scale[1])
    te.penup()
