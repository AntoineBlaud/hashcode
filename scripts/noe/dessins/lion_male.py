import turtle as te
from helper import *


def lion_male(x, y, scale):

    te.penup()
    te.color('#eaeb67')
    te.end_fill()
    Moveto(408.0 * scale[0], 1040.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -6.0 * scale[1], -18.0 * scale[0], -
              18.0 * scale[1], -18.0 * scale[0], -26.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -7.0 * scale[0], -
              17.0 * scale[1], -15.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -4.0 * scale[1], -15.0 * scale[0], -
              13.0 * scale[1], -15.0 * scale[0], -21.0 * scale[1])
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], 3.0 * scale[0], -
              13.0 * scale[1], 16.0 * scale[0], -2.0 * scale[1])
    Curveto_r(13.0 * scale[0], 11.0 * scale[1], 14.0 * scale[0],
              9.0 * scale[1], 9.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -29.0 * scale[1], 10.0 * scale[0], -
              38.0 * scale[1], 32.0 * scale[0], -16.0 * scale[1])
    Curveto_r(22.0 * scale[0], 22.0 * scale[1], 181.0 * scale[0],
              7.0 * scale[1], 258.0 * scale[0], -25.0 * scale[1])
    Curveto_r(21.0 * scale[0], -9.0 * scale[1], 40.0 * scale[0], -
              14.0 * scale[1], 43.0 * scale[0], -11.0 * scale[1])
    Curveto_r(8.0 * scale[0], 8.0 * scale[1], 29.0 * scale[0], -
              39.0 * scale[1], 23.0 * scale[0], -50.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -19.0 * scale[1], -9.0 *
              scale[0], -34.0 * scale[1], 5.0 * scale[0], -46.0 * scale[1])
    Curveto_r(8.0 * scale[0], -7.0 * scale[1], 17.0 * scale[0], -
              9.0 * scale[1], 21.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], 14.0 * scale[0],
              2.0 * scale[1], 24.0 * scale[0], -4.0 * scale[1])
    Curveto_r(20.0 * scale[0], -10.0 * scale[1], 26.0 *
              scale[0], -55.0 * scale[1], 9.0 * scale[0], -61.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -2.0 * scale[1], -4.0 * scale[0], -
              14.0 * scale[1], 4.0 * scale[0], -30.0 * scale[1])
    Curveto_r(9.0 * scale[0], -17.0 * scale[1], 11.0 * scale[0], -
              38.0 * scale[1], 7.0 * scale[0], -60.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -31.0 * scale[1], 18.0 * scale[0], -
              113.0 * scale[1], 38.0 * scale[0], -128.0 * scale[1])
    Curveto_r(16.0 * scale[0], -11.0 * scale[1], 20.0 * scale[0], -
              162.0 * scale[1], 8.0 * scale[0], -253.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -35.0 * scale[1], -4.0 *
              scale[0], -57.0 * scale[1], 3.0 * scale[0], -57.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              6.0 * scale[1], 4.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], -1.0 * scale[0],
              17.0 * scale[1], 5.0 * scale[0], 21.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 11.0 * scale[0],
              0.0 * scale[1], 11.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], 6.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], 11.0 * scale[1])
    Curveto_r(14.0 * scale[0], 29.0 * scale[1], 37.0 * scale[0],
              39.0 * scale[1], 37.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], -7.0 * scale[0], -
              16.0 * scale[1], -15.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              7.0 * scale[1], -15.0 * scale[0], -15.0 * scale[1])
    Curveto_r(0.0 * scale[0], -22.0 * scale[1], 38.0 *
              scale[0], -18.0 * scale[1], 50.0 * scale[0], 5.0 * scale[1])
    Curveto_r(6.0 * scale[0], 12.0 * scale[1], 8.0 * scale[0],
              30.0 * scale[1], 5.0 * scale[0], 40.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 26.0 * scale[1], 4.0 * scale[0],
              47.0 * scale[1], 16.0 * scale[0], 29.0 * scale[1])
    Curveto_r(5.0 * scale[0], -8.0 * scale[1], 9.0 * scale[0],
              63.0 * scale[1], 9.0 * scale[0], 168.0 * scale[1])
    Curveto_r(0.0 * scale[0], 162.0 * scale[1], -2.0 * scale[0],
              182.0 * scale[1], -16.0 * scale[0], 176.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -5.0 * scale[1], -15.0 * scale[0],
              1.0 * scale[1], -13.0 * scale[0], 33.0 * scale[1])
    Curveto_r(4.0 * scale[0], 62.0 * scale[1], -10.0 * scale[0],
              118.0 * scale[1], -37.0 * scale[0], 149.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 24.0 * scale[1], -32.0 * scale[0],
              29.0 * scale[1], -77.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-49.0 * scale[0], 1.0 * scale[1], -53.0 * scale[0],
              3.0 * scale[1], -49.0 * scale[0], 23.0 * scale[1])
    Curveto_r(2.0 * scale[0], 12.0 * scale[1], -3.0 * scale[0],
              30.0 * scale[1], -12.0 * scale[0], 39.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -20.0 * scale[0],
              29.0 * scale[1], -23.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 15.0 * scale[1], -16.0 * scale[0],
              38.0 * scale[1], -30.0 * scale[0], 51.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 21.0 * scale[1], -34.0 * scale[0],
              23.0 * scale[1], -161.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-85.0 * scale[0], 1.0 * scale[1], -144.0 *
              scale[0], -2.0 * scale[1], -154.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(500.0 * scale[0], 860.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 6.0 * scale[0], -
              10.0 * scale[1], 14.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 18.0 * scale[0],
              5.0 * scale[1], 21.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], -3.0 * scale[0],
              10.0 * scale[1], -14.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -21.0 * scale[0], -
              4.0 * scale[1], -21.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(445.0 * scale[0], 850.0 * scale[1], x, y)
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
    Moveto(542.0 * scale[0], 835.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-14.0 * scale[0], -31.0 * scale[1], -15.0 * scale[0], -
              104.0 * scale[1], -3.0 * scale[0], -124.0 * scale[1])
    Curveto_r(5.0 * scale[0], -8.0 * scale[1], 17.0 * scale[0], -
              16.0 * scale[1], 26.0 * scale[0], -17.0 * scale[1])
    Curveto_r(14.0 * scale[0], -2.0 * scale[1], 14.0 * scale[0],
              1.0 * scale[1], -4.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-28.0 * scale[0], 30.0 * scale[1], -30.0 * scale[0],
              102.0 * scale[1], -3.0 * scale[0], 110.0 * scale[1])
    Curveto_r(10.0 * scale[0], 4.0 * scale[1], 19.0 * scale[0],
              13.0 * scale[1], 19.0 * scale[0], 21.0 * scale[1])
    Curveto_r(0.0 * scale[0], 24.0 * scale[1], -23.0 * scale[0],
              17.0 * scale[1], -35.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(710.0 * scale[0], 690.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(20.0 * scale[0], -13.0 * scale[1], 33.0 *
              scale[0], -13.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -14.0 * scale[0],
              10.0 * scale[1], -23.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 0.0 * scale[1], -15.0 *
              scale[0], -2.0 * scale[1], -2.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(971.0 * scale[0], 684.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(592.0 * scale[0], 606.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -35.0 * scale[1], 18.0 * scale[0], -
              45.0 * scale[1], 18.0 * scale[0], -13.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -5.0 * scale[0],
              29.0 * scale[1], -10.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], -10.0 * scale[0], -
              3.0 * scale[1], -8.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(972.0 * scale[0], 270.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#d8d1ac')
    te.end_fill()
    Moveto(253.0 * scale[0], 1433.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(131.0 * scale[0], -2.0 * scale[1], 343.0 *
              scale[0], -2.0 * scale[1], 470.0 * scale[0], 0.0 * scale[1])
    Curveto_r(128.0 * scale[0], 1.0 * scale[1], 21.0 * scale[0],
              2.0 * scale[1], -238.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-259.0 * scale[0], 0.0 * scale[1], -363.0 *
              scale[0], -1.0 * scale[1], -232.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(380.0 * scale[0], 1362.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -42.0 * scale[1], 17.0 * scale[0], -
              54.0 * scale[1], 52.0 * scale[0], -36.0 * scale[1])
    Curveto_r(31.0 * scale[0], 16.0 * scale[1], 30.0 * scale[0],
              27.0 * scale[1], -5.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 12.0 * scale[1], -21.0 * scale[0],
              11.0 * scale[1], -4.0 * scale[0], -8.0 * scale[1])
    Curveto_r(19.0 * scale[0], -22.0 * scale[1], 14.0 * scale[0], -
              33.0 * scale[1], -16.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -18.0 * scale[0],
              5.0 * scale[1], -15.0 * scale[0], 30.0 * scale[1])
    Curveto_r(3.0 * scale[0], 17.0 * scale[1], 1.0 * scale[0],
              30.0 * scale[1], -4.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              13.0 * scale[1], -8.0 * scale[0], -28.0 * scale[1])
    te.end_fill()
    Moveto(557.0 * scale[0], 1383.0 * scale[1], x, y)
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
    Moveto(515.0 * scale[0], 1351.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              15.0 * scale[1], 15.0 * scale[0], -21.0 * scale[1])
    Curveto_r(13.0 * scale[0], -7.0 * scale[1], 20.0 *
              scale[0], -7.0 * scale[1], 20.0 * scale[0], 0.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -5.0 * scale[0],
              10.0 * scale[1], -11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0],
              5.0 * scale[1], -4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              10.0 * scale[1], -4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(580.0 * scale[0], 1347.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], -4.0 * scale[0], -
              17.0 * scale[1], -10.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              4.0 * scale[1], -10.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 4.0 * scale[0], -
              10.0 * scale[1], 9.0 * scale[0], -10.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 25.0 * scale[0],
              39.0 * scale[1], 17.0 * scale[0], 47.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              1.0 * scale[1], -6.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(75.0 * scale[0], 1330.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], -11.0 *
              scale[0], -8.0 * scale[1], -16.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 4.0 * scale[1], -9.0 * scale[0], -
              4.0 * scale[1], -9.0 * scale[0], -16.0 * scale[1])
    Curveto_r(0.0 * scale[0], -20.0 * scale[1], 1.0 * scale[0], -
              21.0 * scale[1], 13.0 * scale[0], -7.0 * scale[1])
    Curveto_r(6.0 * scale[0], 9.0 * scale[1], 30.0 * scale[0],
              18.0 * scale[1], 52.0 * scale[0], 20.0 * scale[1])
    Curveto_r(32.0 * scale[0], 2.0 * scale[1], 40.0 * scale[0],
              0.0 * scale[1], 40.0 * scale[0], -14.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 4.0 * scale[0], -
              20.0 * scale[1], 9.0 * scale[0], -25.0 * scale[1])
    Curveto_r(4.0 * scale[0], -4.0 * scale[1], 6.0 * scale[0],
              6.0 * scale[1], 4.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 27.0 * scale[1], -7.0 * scale[0],
              30.0 * scale[1], -45.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 2.0 * scale[1], -44.0 *
              scale[0], -2.0 * scale[1], -48.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(815.0 * scale[0], 1330.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 2.0 * scale[0], -
              10.0 * scale[1], -2.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              10.0 * scale[1], -10.0 * scale[0], -22.0 * scale[1])
    Lineto_r(-1.0 * scale[0], -23.0 * scale[1])
    Lineto_r(10.0 * scale[0], 23.0 * scale[1])
    Curveto_r(6.0 * scale[0], 12.0 * scale[1], 20.0 * scale[0],
              22.0 * scale[1], 32.0 * scale[0], 22.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 28.0 * scale[0],
              5.0 * scale[1], 36.0 * scale[0], 10.0 * scale[1])
    Curveto_r(11.0 * scale[0], 7.0 * scale[1], 3.0 * scale[0],
              10.0 * scale[1], -28.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-26.0 * scale[0], 0.0 * scale[1], -41.0 * scale[0], -
              4.0 * scale[1], -37.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(900.0 * scale[0], 1333.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0], -
              15.0 * scale[1], 10.0 * scale[0], -23.0 * scale[1])
    Curveto_r(7.0 * scale[0], -12.0 * scale[1], 9.0 *
              scale[0], -10.0 * scale[1], 7.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 19.0 * scale[1], -17.0 * scale[0],
              33.0 * scale[1], -17.0 * scale[0], 15.0 * scale[1])
    te.end_fill()
    Moveto(443.0 * scale[0], 1313.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-26.0 * scale[0], -10.0 * scale[1], -12.0 *
              scale[0], -22.0 * scale[1], 13.0 * scale[0], -12.0 * scale[1])
    Curveto_r(15.0 * scale[0], 5.0 * scale[1], 35.0 * scale[0],
              7.0 * scale[1], 45.0 * scale[0], 4.0 * scale[1])
    Curveto_r(11.0 * scale[0], -4.0 * scale[1], 19.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], -54.0 * scale[0],
              14.0 * scale[1], -77.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(530.0 * scale[0], 1305.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 12.0 * scale[0], -
              19.0 * scale[1], 26.0 * scale[0], -32.0 * scale[1])
    Curveto_r(24.0 * scale[0], -22.0 * scale[1], 26.0 * scale[0], -
              29.0 * scale[1], 21.0 * scale[0], -76.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -35.0 * scale[1], -3.0 *
              scale[0], -47.0 * scale[1], 3.0 * scale[0], -37.0 * scale[1])
    Curveto_r(21.0 * scale[0], 32.0 * scale[1], 11.0 * scale[0],
              89.0 * scale[1], -20.0 * scale[0], 122.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 17.0 * scale[1], -30.0 * scale[0],
              27.0 * scale[1], -30.0 * scale[0], 23.0 * scale[1])
    te.end_fill()
    Moveto(400.0 * scale[0], 1285.0 * scale[1], x, y)
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
    Moveto(150.0 * scale[0], 1261.0 * scale[1], x, y)
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
    Moveto(906.0 * scale[0], 1250.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -14.0 * scale[1], 10.0 * scale[0], -
              29.0 * scale[1], 14.0 * scale[0], -34.0 * scale[1])
    Curveto_r(13.0 * scale[0], -13.0 * scale[1], 6.0 * scale[0],
              16.0 * scale[1], -8.0 * scale[0], 39.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 19.0 * scale[1], -13.0 * scale[0],
              18.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(376.0 * scale[0], 1234.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -27.0 * scale[1], 12.0 * scale[0], -
              94.0 * scale[1], 26.0 * scale[0], -94.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 4.0 * scale[0],
              9.0 * scale[1], -2.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 11.0 * scale[1], -12.0 * scale[0],
              38.0 * scale[1], -12.0 * scale[0], 60.0 * scale[1])
    Curveto_r(0.0 * scale[0], 46.0 * scale[1], -3.0 * scale[0],
              49.0 * scale[1], -12.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(60.0 * scale[0], 1240.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -8.0 * scale[1], -12.0 *
              scale[0], -10.0 * scale[1], 3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0],
              5.0 * scale[1], 17.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], -1.0 * scale[0],
              12.0 * scale[1], -20.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(805.0 * scale[0], 1240.0 * scale[1], x, y)
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
    Moveto(43.0 * scale[0], 1189.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -13.0 * scale[1], 7.0 * scale[0], -
              27.0 * scale[1], 7.0 * scale[0], -31.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 14.0 * scale[0], -
              8.0 * scale[1], 31.0 * scale[0], -8.0 * scale[1])
    Curveto_r(16.0 * scale[0], 0.0 * scale[1], 28.0 * scale[0],
              4.0 * scale[1], 25.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], -15.0 * scale[0],
              7.0 * scale[1], -26.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -4.0 * scale[1], -20.0 * scale[0],
              0.0 * scale[1], -20.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], -5.0 * scale[0],
              24.0 * scale[1], -12.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -9.0 * scale[0],
              0.0 * scale[1], -5.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(151.0 * scale[0], 1193.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -8.0 * scale[1], -11.0 * scale[0], -
              16.0 * scale[1], -8.0 * scale[0], -19.0 * scale[1])
    Curveto_r(2.0 * scale[0], -2.0 * scale[1], 10.0 * scale[0],
              2.0 * scale[1], 17.0 * scale[0], 11.0 * scale[1])
    Curveto_r(17.0 * scale[0], 20.0 * scale[1], 9.0 * scale[0],
              27.0 * scale[1], -9.0 * scale[0], 8.0 * scale[1])
    te.end_fill()
    Moveto(790.0 * scale[0], 1195.0 * scale[1], x, y)
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
    Moveto(806.0 * scale[0], 1158.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], 17.0 * scale[0], -
              8.0 * scale[1], 31.0 * scale[0], -8.0 * scale[1])
    Curveto_r(15.0 * scale[0], 0.0 * scale[1], 23.0 * scale[0],
              3.0 * scale[1], 19.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 10.0 * scale[1], -56.0 * scale[0],
              10.0 * scale[1], -50.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(515.0 * scale[0], 1119.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -10.0 * scale[1], -26.0 *
              scale[0], -19.0 * scale[1], -22.0 * scale[0], -19.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 67.0 * scale[0],
              29.0 * scale[1], 67.0 * scale[0], 35.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], -15.0 * scale[0],
              4.0 * scale[1], -45.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(440.0 * scale[0], 1110.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(8.0 * scale[0], -5.0 * scale[1], 22.0 * scale[0], -
              10.0 * scale[1], 30.0 * scale[0], -10.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              1.0 * scale[1], 0.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -22.0 * scale[0],
              10.0 * scale[1], -30.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -13.0 *
              scale[0], -1.0 * scale[1], 0.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(816.0 * scale[0], 995.0 * scale[1], x, y)
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
    Moveto(70.0 * scale[0], 986.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(915.0 * scale[0], 970.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], -11.0 *
              scale[0], -7.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 5.0 * scale[1], -8.0 * scale[0],
              2.0 * scale[1], -3.0 * scale[0], -5.0 * scale[1])
    Curveto_r(5.0 * scale[0], -9.0 * scale[1], 10.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -2.0 * scale[1])
    Curveto_r(17.0 * scale[0], 17.0 * scale[1], 27.0 * scale[0],
              13.0 * scale[1], 27.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -15.0 * scale[1], -5.0 * scale[0], -
              19.0 * scale[1], -15.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -15.0 * scale[0],
              0.0 * scale[1], -15.0 * scale[0], -6.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -4.0 * scale[0], -
              7.0 * scale[1], -14.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -17.0 * scale[0],
              7.0 * scale[1], -27.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -11.0 * scale[1], -10.0 *
              scale[0], -14.0 * scale[1], -2.0 * scale[0], -9.0 * scale[1])
    Curveto_r(7.0 * scale[0], 4.0 * scale[1], 22.0 * scale[0],
              2.0 * scale[1], 34.0 * scale[0], -5.0 * scale[1])
    Curveto_r(12.0 * scale[0], -6.0 * scale[1], 19.0 *
              scale[0], -7.0 * scale[1], 15.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], 15.0 * scale[0], 15.0 * scale[1])
    Curveto_r(15.0 * scale[0], 4.0 * scale[1], 20.0 * scale[0],
              12.0 * scale[1], 17.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 25.0 * scale[1], -22.0 * scale[0],
              36.0 * scale[1], -33.0 * scale[0], 19.0 * scale[1])
    te.end_fill()
    Moveto(76.0 * scale[0], 935.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-17.0 * scale[0], -13.0 * scale[1], -18.0 *
              scale[0], -15.0 * scale[1], -3.0 * scale[0], -15.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0],
              5.0 * scale[1], 17.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 5.0 * scale[0],
              7.0 * scale[1], 10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 10.0 *
              scale[0], -1.0 * scale[1], 10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 15.0 * scale[1], -11.0 * scale[0],
              13.0 * scale[1], -34.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(328.0 * scale[0], 923.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(582.0 * scale[0], 853.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -2.0 * scale[1], -10.0 *
              scale[0], -8.0 * scale[1], -7.0 * scale[0], -13.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], -4.0 * scale[0], -
              11.0 * scale[1], -15.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-28.0 * scale[0], -9.0 * scale[1], -29.0 * scale[0], -
              84.0 * scale[1], -1.0 * scale[0], -109.0 * scale[1])
    Curveto_r(25.0 * scale[0], -23.0 * scale[1], 76.0 * scale[0], -
              24.0 * scale[1], 100.0 * scale[0], -2.0 * scale[1])
    Curveto_r(16.0 * scale[0], 15.0 * scale[1], 19.0 * scale[0],
              15.0 * scale[1], 24.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], -8.0 * scale[1], 15.0 * scale[0], -
              15.0 * scale[1], 26.0 * scale[0], -15.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 23.0 * scale[0], -
              4.0 * scale[1], 26.0 * scale[0], -10.0 * scale[1])
    Curveto_r(13.0 * scale[0], -20.0 * scale[1], 25.0 *
              scale[0], -9.0 * scale[1], 25.0 * scale[0], 23.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], -4.0 * scale[0],
              28.0 * scale[1], -8.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -15.0 * scale[1], -54.0 *
              scale[0], -17.0 * scale[1], -63.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 7.0 * scale[1], -12.0 * scale[0],
              8.0 * scale[1], -20.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-27.0 * scale[0], -17.0 * scale[1], -64.0 *
              scale[0], -11.0 * scale[1], -86.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-28.0 * scale[0], 31.0 * scale[1], -29.0 * scale[0],
              52.0 * scale[1], -3.0 * scale[0], 75.0 * scale[1])
    Curveto_r(16.0 * scale[0], 13.0 * scale[1], 29.0 * scale[0],
              40.0 * scale[1], 18.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              3.0 * scale[1], -16.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(720.0 * scale[0], 828.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], 9.0 * scale[0], -
              26.0 * scale[1], 20.0 * scale[0], -43.0 * scale[1])
    Curveto_r(22.0 * scale[0], -34.0 * scale[1], 25.0 *
              scale[0], -30.0 * scale[1], 8.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 15.0 * scale[1], -11.0 * scale[0],
              31.0 * scale[1], -10.0 * scale[0], 36.0 * scale[1])
    Curveto_r(1.0 * scale[0], 4.0 * scale[1], -2.0 * scale[0],
              7.0 * scale[1], -8.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              6.0 * scale[1], -10.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(630.0 * scale[0], 647.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-21.0 * scale[0], -10.0 * scale[1], -24.0 *
              scale[0], -19.0 * scale[1], -22.0 * scale[0], -47.0 * scale[1])
    Curveto_r(5.0 * scale[0], -54.0 * scale[1], 27.0 * scale[0], -
              80.0 * scale[1], 63.0 * scale[0], -76.0 * scale[1])
    Curveto_r(48.0 * scale[0], 5.0 * scale[1], 65.0 * scale[0],
              28.0 * scale[1], 53.0 * scale[0], 73.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 27.0 * scale[1], -14.0 * scale[0],
              38.0 * scale[1], -27.0 * scale[0], 37.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -1.0 * scale[1], -15.0 * scale[0],
              2.0 * scale[1], -12.0 * scale[0], 6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], -2.0 * scale[0],
              11.0 * scale[1], -11.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 7.0 * scale[1], -14.0 * scale[0],
              8.0 * scale[1], -44.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto_r(54.0 * scale[0], -48.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(13.0 * scale[0], -26.0 * scale[1], 13.0 *
              scale[0], -30.0 * scale[1], 1.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -17.0 * scale[0],
              1.0 * scale[1], -20.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -5.0 * scale[1], -11.0 *
              scale[0], -6.0 * scale[1], -17.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -5.0 * scale[0],
              10.0 * scale[1], 3.0 * scale[0], 15.0 * scale[1])
    Curveto_r(10.0 * scale[0], 6.0 * scale[1], 11.0 * scale[0],
              9.0 * scale[1], 2.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0],
              9.0 * scale[1], -13.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 30.0 * scale[1], 27.0 * scale[0],
              24.0 * scale[1], 44.0 * scale[0], -11.0 * scale[1])
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
    Moveto(851.0 * scale[0], 474.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(825.0 * scale[0], 189.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0], -
              12.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 17.0 * scale[1], 1.0 * scale[0],
              20.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(958.0 * scale[0], 28.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -10.0 * scale[1], -14.0 *
              scale[0], -18.0 * scale[1], -9.0 * scale[0], -18.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 36.0 * scale[0],
              29.0 * scale[1], 30.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 1.0 * scale[1], -12.0 * scale[0], -
              6.0 * scale[1], -21.0 * scale[0], -16.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#ebf0dd')
    te.end_fill()
    Moveto(0.0 * scale[0], 1429.0 * scale[1], x, y)
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
    Moveto(950.0 * scale[0], 1436.0 * scale[1], x, y)
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
    Moveto(103.0 * scale[0], 1293.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-20.0 * scale[0], -7.0 * scale[1], -15.0 *
              scale[0], -19.0 * scale[1], 7.0 * scale[0], -19.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0],
              6.0 * scale[1], 20.0 * scale[0], 13.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -6.0 * scale[0],
              15.0 * scale[1], -27.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(845.0 * scale[0], 1291.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -18.0 * scale[1], 17.0 *
              scale[0], -23.0 * scale[1], 33.0 * scale[0], -7.0 * scale[1])
    Curveto_r(15.0 * scale[0], 15.0 * scale[1], 15.0 * scale[0],
              16.0 * scale[1], -5.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -24.0 *
              scale[0], -4.0 * scale[1], -28.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(441.0 * scale[0], 1263.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-30.0 * scale[0], -38.0 * scale[1], -36.0 *
              scale[0], -68.0 * scale[1], -17.0 * scale[0], -95.0 * scale[1])
    Curveto_r(21.0 * scale[0], -29.0 * scale[1], 20.0 * scale[0], -
              42.0 * scale[1], -1.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 5.0 * scale[1], -15.0 * scale[0],
              4.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(10.0 * scale[0], -10.0 * scale[1], 17.0 *
              scale[0], -9.0 * scale[1], 33.0 * scale[0], 6.0 * scale[1])
    Curveto_r(15.0 * scale[0], 14.0 * scale[1], 23.0 * scale[0],
              15.0 * scale[1], 34.0 * scale[0], 6.0 * scale[1])
    Curveto_r(21.0 * scale[0], -17.0 * scale[1], 61.0 * scale[0],
              16.0 * scale[1], 44.0 * scale[0], 37.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 10.0 * scale[1], -9.0 * scale[0],
              18.0 * scale[1], -1.0 * scale[0], 31.0 * scale[1])
    Curveto_r(9.0 * scale[0], 14.0 * scale[1], 6.0 * scale[0],
              24.0 * scale[1], -14.0 * scale[0], 49.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 39.0 * scale[1], -45.0 * scale[0],
              40.0 * scale[1], -72.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(802.0 * scale[0], 1260.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(86.0 * scale[0], 1243.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -5.0 * scale[1], 12.0 * scale[0], -
              12.0 * scale[1], 16.0 * scale[0], -18.0 * scale[1])
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 8.0 *
              scale[0], -2.0 * scale[1], 8.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], -7.0 * scale[0],
              17.0 * scale[1], -17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -12.0 *
              scale[0], -3.0 * scale[1], -7.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(830.0 * scale[0], 1246.0 * scale[1], x, y)
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
    Moveto(910.0 * scale[0], 1212.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -7.0 * scale[0], -
              18.0 * scale[1], -16.0 * scale[0], -26.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -9.0 * scale[1], -11.0 * scale[0], -
              16.0 * scale[1], -5.0 * scale[0], -16.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 35.0 * scale[0],
              39.0 * scale[1], 27.0 * scale[0], 48.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -6.0 * scale[0],
              0.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(58.0 * scale[0], 1203.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(800.0 * scale[0], 1201.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 11.0 * scale[0], -
              6.0 * scale[1], 25.0 * scale[0], -3.0 * scale[1])
    Curveto_r(14.0 * scale[0], 2.0 * scale[1], 25.0 * scale[0],
              6.0 * scale[1], 25.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 2.0 * scale[1], -11.0 * scale[0],
              4.0 * scale[1], -25.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -25.0 *
              scale[0], -4.0 * scale[1], -25.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(830.0 * scale[0], 1005.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(27.0 * scale[0], -14.0 * scale[1], 36.0 *
              scale[0], -13.0 * scale[1], 25.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -16.0 * scale[0],
              11.0 * scale[1], -28.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -1.0 * scale[1], -21.0 *
              scale[0], -1.0 * scale[1], 3.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(42.0 * scale[0], 985.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -35.0 * scale[1], -15.0 *
              scale[0], -50.0 * scale[1], 4.0 * scale[0], -69.0 * scale[1])
    Curveto_r(12.0 * scale[0], -12.0 * scale[1], 20.0 *
              scale[0], -13.0 * scale[1], 35.0 * scale[0], -6.0 * scale[1])
    Curveto_r(23.0 * scale[0], 13.0 * scale[1], 20.0 * scale[0],
              37.0 * scale[1], -7.0 * scale[0], 74.0 * scale[1])
    Lineto_r(-20.0 * scale[0], 28.0 * scale[1])
    Lineto_r(-12.0 * scale[0], -27.0 * scale[1])
    te.end_fill()
    Moveto_r(48.0 * scale[0], -55.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -8.0 * scale[0], -
              10.0 * scale[1], -17.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0],
              2.0 * scale[1], -3.0 * scale[0], 10.0 * scale[1])
    Curveto_r(19.0 * scale[0], 12.0 * scale[1], 20.0 * scale[0],
              12.0 * scale[1], 20.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(797.0 * scale[0], 992.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -2.0 * scale[1], -17.0 * scale[0], -
              11.0 * scale[1], -15.0 * scale[0], -25.0 * scale[1])
    Curveto_r(5.0 * scale[0], -32.0 * scale[1], 28.0 *
              scale[0], -33.0 * scale[1], 29.0 * scale[0], 0.0 * scale[1])
    Curveto_r(1.0 * scale[0], 23.0 * scale[1], 2.0 * scale[0],
              24.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(5.0 * scale[0], -28.0 * scale[1], 23.0 * scale[0], -
              31.0 * scale[1], 23.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 21.0 * scale[1], -16.0 * scale[0],
              29.0 * scale[1], -43.0 * scale[0], 23.0 * scale[1])
    te.end_fill()
    Moveto(915.0 * scale[0], 960.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -12.0 *
              scale[0], -7.0 * scale[1], -20.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 7.0 * scale[1], -19.0 *
              scale[0], -11.0 * scale[1], 0.0 * scale[0], -27.0 * scale[1])
    Curveto_r(10.0 * scale[0], -8.0 * scale[1], 15.0 *
              scale[0], -9.0 * scale[1], 15.0 * scale[0], -2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 7.0 * scale[0],
              9.0 * scale[1], 15.0 * scale[0], 6.0 * scale[1])
    Curveto_r(10.0 * scale[0], -4.0 * scale[1], 15.0 * scale[0],
              0.0 * scale[1], 15.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 22.0 * scale[1], -14.0 * scale[0],
              28.0 * scale[1], -25.0 * scale[0], 11.0 * scale[1])
    te.end_fill()
    Moveto(870.0 * scale[0], 910.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 10.0 * scale[0], -
              10.0 * scale[1], 23.0 * scale[0], -10.0 * scale[1])
    Curveto_r(18.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0],
              2.0 * scale[1], 7.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 13.0 * scale[1], -30.0 * scale[0],
              13.0 * scale[1], -30.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(582.0 * scale[0], 825.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-28.0 * scale[0], -29.0 * scale[1], -28.0 *
              scale[0], -45.0 * scale[1], 1.0 * scale[0], -77.0 * scale[1])
    Curveto_r(22.0 * scale[0], -25.0 * scale[1], 59.0 * scale[0], -
              31.0 * scale[1], 86.0 * scale[0], -14.0 * scale[1])
    Curveto_r(7.0 * scale[0], 5.0 * scale[1], 16.0 * scale[0],
              4.0 * scale[1], 20.0 * scale[0], -2.0 * scale[1])
    Curveto_r(9.0 * scale[0], -14.0 * scale[1], 60.0 *
              scale[0], -10.0 * scale[1], 66.0 * scale[0], 6.0 * scale[1])
    Curveto_r(5.0 * scale[0], 14.0 * scale[1], -35.0 * scale[0],
              92.0 * scale[1], -48.0 * scale[0], 92.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              12.0 * scale[1], -18.0 * scale[0], -27.0 * scale[1])
    Lineto_r(-10.0 * scale[0], -28.0 * scale[1])
    Lineto_r(-21.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-32.0 * scale[0], 43.0 * scale[1], -50.0 * scale[0],
              49.0 * scale[1], -76.0 * scale[0], 22.0 * scale[1])
    te.end_fill()
    Moveto(640.0 * scale[0], 610.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 6.0 * scale[0], -
              20.0 * scale[1], 13.0 * scale[0], -20.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0], -
              3.0 * scale[1], -2.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -5.0 * scale[1], -9.0 * scale[0], -
              11.0 * scale[1], -3.0 * scale[0], -15.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 13.0 *
              scale[0], -2.0 * scale[1], 17.0 * scale[0], 3.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 12.0 * scale[0],
              8.0 * scale[1], 20.0 * scale[0], 5.0 * scale[1])
    Curveto_r(12.0 * scale[0], -5.0 * scale[1], 12.0 *
              scale[0], -1.0 * scale[1], -1.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 35.0 * scale[1], -44.0 * scale[0],
              41.0 * scale[1], -44.0 * scale[0], 11.0 * scale[1])
    te.end_fill()
    Moveto(965.0 * scale[0], 21.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -5.0 * scale[1], -23.0 * scale[0], -
              11.0 * scale[1], -40.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-24.0 * scale[0], -3.0 * scale[1], -21.0 *
              scale[0], -4.0 * scale[1], 13.0 * scale[0], -6.0 * scale[1])
    Curveto_r(31.0 * scale[0], -1.0 * scale[1], 42.0 * scale[0],
              3.0 * scale[1], 42.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], -3.0 * scale[0],
              18.0 * scale[1], -15.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(0.0 * scale[0], 10.0 * scale[1], x, y)
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
    Moveto(58.0 * scale[0], 3.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 32.0 *
              scale[0], -2.0 * scale[1], 45.0 * scale[0], 0.0 * scale[1])
    Curveto_r(12.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              4.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 0.0 * scale[1], -35.0 *
              scale[0], -2.0 * scale[1], -22.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(318.0 * scale[0], 3.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(105.0 * scale[0], -2.0 * scale[1], 279.0 *
              scale[0], -2.0 * scale[1], 385.0 * scale[0], 0.0 * scale[1])
    Curveto_r(105.0 * scale[0], 1.0 * scale[1], 19.0 * scale[0],
              2.0 * scale[1], -193.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-212.0 * scale[0], 0.0 * scale[1], -298.0 *
              scale[0], -1.0 * scale[1], -192.0 * scale[0], -2.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#b38842')
    te.end_fill()
    Moveto(375.0 * scale[0], 1409.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], 13.0 * scale[0], -
              5.0 * scale[1], 22.0 * scale[0], -2.0 * scale[1])
    Curveto_r(9.0 * scale[0], 4.0 * scale[1], 14.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 9.0 * scale[0], -
              16.0 * scale[1], 28.0 * scale[0], -22.0 * scale[1])
    Curveto_r(18.0 * scale[0], -7.0 * scale[1], 36.0 * scale[0], -
              20.0 * scale[1], 39.0 * scale[0], -29.0 * scale[1])
    Curveto_r(6.0 * scale[0], -13.0 * scale[1], 4.0 * scale[0], -
              14.0 * scale[1], -9.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 11.0 * scale[1], -16.0 * scale[0],
              11.0 * scale[1], -13.0 * scale[0], -1.0 * scale[1])
    Curveto_r(2.0 * scale[0], -8.0 * scale[1], 11.0 * scale[0], -
              17.0 * scale[1], 21.0 * scale[0], -21.0 * scale[1])
    Curveto_r(21.0 * scale[0], -9.0 * scale[1], 49.0 * scale[0],
              0.0 * scale[1], 41.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], -10.0 * scale[0],
              7.0 * scale[1], -15.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -4.0 * scale[1], -9.0 *
              scale[0], -3.0 * scale[1], -9.0 * scale[0], 0.0 * scale[1])
    Curveto_r(0.0 * scale[0], 3.0 * scale[1], 14.0 * scale[0],
              11.0 * scale[1], 31.0 * scale[0], 17.0 * scale[1])
    Curveto_r(23.0 * scale[0], 8.0 * scale[1], 27.0 * scale[0],
              13.0 * scale[1], 17.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 7.0 * scale[1], -8.0 * scale[0],
              9.0 * scale[1], 7.0 * scale[0], 9.0 * scale[1])
    Curveto_r(15.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0],
              3.0 * scale[1], 7.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 17.0 * scale[1], -69.0 * scale[0],
              18.0 * scale[1], -83.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -8.0 * scale[1], -16.0 * scale[0], -
              14.0 * scale[1], -22.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], 9.0 * scale[0], 14.0 * scale[1])
    Curveto_r(17.0 * scale[0], 13.0 * scale[1], 14.0 * scale[0],
              15.0 * scale[1], -33.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-29.0 * scale[0], 0.0 * scale[1], -51.0 *
              scale[0], -4.0 * scale[1], -48.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(240.0 * scale[0], 1400.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 9.0 * scale[0], -
              10.0 * scale[1], 21.0 * scale[0], -10.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0],
              5.0 * scale[1], 14.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -13.0 * scale[0],
              10.0 * scale[1], -21.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0], -
              4.0 * scale[1], -14.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(300.0 * scale[0], 1400.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(20.0 * scale[0], -13.0 * scale[1], 1.0 * scale[0], -
              19.0 * scale[1], -73.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-59.0 * scale[0], -3.0 * scale[1], -78.0 * scale[0], -
              19.0 * scale[1], -30.0 * scale[0], -26.0 * scale[1])
    Curveto_r(34.0 * scale[0], -4.0 * scale[1], 41.0 * scale[0], -
              11.0 * scale[1], 24.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0], -
              10.0 * scale[1], 35.0 * scale[0], -15.0 * scale[1])
    Curveto_r(65.0 * scale[0], -9.0 * scale[1], 86.0 *
              scale[0], -8.0 * scale[1], 79.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], 4.0 * scale[0],
              10.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(21.0 * scale[0], 0.0 * scale[1], 24.0 * scale[0],
              4.0 * scale[1], 19.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 33.0 * scale[1], -28.0 * scale[0],
              51.0 * scale[1], -62.0 * scale[0], 52.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -22.0 * scale[0], -
              2.0 * scale[1], -10.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto_r(-2.0 * scale[0], -67.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -2.0 * scale[1], -28.0 *
              scale[0], -2.0 * scale[1], -40.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 2.0 * scale[1], -5.0 * scale[0],
              4.0 * scale[1], 17.0 * scale[0], 4.0 * scale[1])
    Curveto_r(22.0 * scale[0], 1.0 * scale[1], 32.0 * scale[0], -
              1.0 * scale[1], 23.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(640.0 * scale[0], 1388.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(32.0 * scale[0], -15.0 * scale[1], 68.0 * scale[0], -
              22.0 * scale[1], 125.0 * scale[0], -24.0 * scale[1])
    Curveto_r(73.0 * scale[0], -3.0 * scale[1], 77.0 *
              scale[0], -2.0 * scale[1], 45.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 7.0 * scale[1], -41.0 * scale[0],
              16.0 * scale[1], -49.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -48.0 * scale[0],
              11.0 * scale[1], -90.0 * scale[0], 13.0 * scale[1])
    Lineto_r(-76.0 * scale[0], 3.0 * scale[1])
    Lineto_r(45.0 * scale[0], -22.0 * scale[1])
    te.end_fill()
    Moveto(600.0 * scale[0], 1339.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -22.0 * scale[1], -4.0 * scale[0], -
              38.0 * scale[1], -9.0 * scale[0], -34.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -13.0 * scale[0],
              0.0 * scale[1], -17.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -8.0 * scale[1], -3.0 *
              scale[0], -9.0 * scale[1], 4.0 * scale[0], -5.0 * scale[1])
    Curveto_r(7.0 * scale[0], 4.0 * scale[1], 12.0 * scale[0],
              1.0 * scale[1], 12.0 * scale[0], -8.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 4.0 * scale[0], -
              16.0 * scale[1], 9.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 6.0 * scale[0], -
              12.0 * scale[1], -1.0 * scale[0], -30.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -17.0 * scale[1], -8.0 * scale[0], -
              40.0 * scale[1], -5.0 * scale[0], -51.0 * scale[1])
    Curveto_r(7.0 * scale[0], -25.0 * scale[1], -2.0 * scale[0], -
              51.0 * scale[1], -14.0 * scale[0], -43.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -6.0 * scale[0], -
              1.0 * scale[1], -3.0 * scale[0], -9.0 * scale[1])
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], 19.0 * scale[0], -
              14.0 * scale[1], 36.0 * scale[0], -15.0 * scale[1])
    Curveto_r(53.0 * scale[0], -1.0 * scale[1], 43.0 * scale[0], -
              12.0 * scale[1], -13.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 0.0 * scale[1], -59.0 *
              scale[0], -1.0 * scale[1], -66.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              6.0 * scale[1], -6.0 * scale[0], -14.0 * scale[1])
    Curveto_r(6.0 * scale[0], -14.0 * scale[1], 13.0 * scale[0], -
              14.0 * scale[1], 210.0 * scale[0], 3.0 * scale[1])
    Curveto_r(87.0 * scale[0], 8.0 * scale[1], 87.0 * scale[0],
              20.0 * scale[1], 0.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-52.0 * scale[0], -2.0 * scale[1], -68.0 * scale[0],
              0.0 * scale[1], -57.0 * scale[0], 7.0 * scale[1])
    Curveto_r(8.0 * scale[0], 6.0 * scale[1], 27.0 * scale[0],
              11.0 * scale[1], 42.0 * scale[0], 11.0 * scale[1])
    Curveto_r(68.0 * scale[0], 0.0 * scale[1], 80.0 * scale[0],
              38.0 * scale[1], 21.0 * scale[0], 69.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 11.0 * scale[1], -31.0 * scale[0],
              20.0 * scale[1], -21.0 * scale[0], 21.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0], -
              4.0 * scale[1], 23.0 * scale[0], -10.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 11.0 * scale[0], -
              10.0 * scale[1], 17.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 5.0 * scale[0],
              7.0 * scale[1], -3.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 15.0 * scale[1], -12.0 * scale[0],
              16.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(13.0 * scale[0], -5.0 * scale[1], 17.0 *
              scale[0], -3.0 * scale[1], 14.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 7.0 * scale[1], -15.0 * scale[0],
              13.0 * scale[1], -30.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -24.0 * scale[0],
              4.0 * scale[1], -21.0 * scale[0], 8.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], 17.0 * scale[0],
              8.0 * scale[1], 32.0 * scale[0], 8.0 * scale[1])
    Curveto_r(26.0 * scale[0], 1.0 * scale[1], 26.0 * scale[0],
              1.0 * scale[1], 8.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 14.0 * scale[1], -19.0 * scale[0],
              15.0 * scale[1], 0.0 * scale[0], 22.0 * scale[1])
    Curveto_r(16.0 * scale[0], 6.0 * scale[1], 15.0 * scale[0],
              8.0 * scale[1], -11.0 * scale[0], 14.0 * scale[1])
    Lineto_r(-30.0 * scale[0], 7.0 * scale[1])
    Lineto_r(33.0 * scale[0], 1.0 * scale[1])
    Curveto_r(37.0 * scale[0], 1.0 * scale[1], 43.0 * scale[0],
              18.0 * scale[1], 10.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-54.0 * scale[0], 11.0 * scale[1], -127.0 * scale[0],
              16.0 * scale[1], -130.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -3.0 *
              scale[0], -3.0 * scale[1], -2.0 * scale[0], 4.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], -16.0 * scale[0],
              23.0 * scale[1], -32.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              18.0 * scale[1], -4.0 * scale[0], -41.0 * scale[1])
    te.end_fill()
    Moveto(355.0 * scale[0], 1311.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], -7.0 * scale[0], -
              12.0 * scale[1], -22.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-26.0 * scale[0], -4.0 * scale[1], -26.0 *
              scale[0], -4.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(22.0 * scale[0], -1.0 * scale[1], 32.0 * scale[0],
              3.0 * scale[1], 32.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -5.0 * scale[0],
              15.0 * scale[1], -11.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              4.0 * scale[1], -4.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(192.0 * scale[0], 1274.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -16.0 * scale[1], 14.0 * scale[0], -
              19.0 * scale[1], 78.0 * scale[0], -22.0 * scale[1])
    Curveto_r(41.0 * scale[0], -2.0 * scale[1], 86.0 * scale[0],
              0.0 * scale[1], 100.0 * scale[0], 4.0 * scale[1])
    Lineto_r(25.0 * scale[0], 6.0 * scale[1])
    Lineto_r(-23.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 5.0 * scale[1], -59.0 * scale[0],
              12.0 * scale[1], -103.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-76.0 * scale[0], 7.0 * scale[1], -81.0 * scale[0],
              6.0 * scale[1], -77.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(215.0 * scale[0], 1227.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -9.0 * scale[1], -25.0 * scale[0], -
              16.0 * scale[1], -17.0 * scale[0], -21.0 * scale[1])
    Curveto_r(7.0 * scale[0], -4.0 * scale[1], 12.0 *
              scale[0], -2.0 * scale[1], 12.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 5.0 * scale[0],
              6.0 * scale[1], 13.0 * scale[0], -4.0 * scale[1])
    Curveto_r(8.0 * scale[0], -11.0 * scale[1], 33.0 * scale[0], -
              19.0 * scale[1], 73.0 * scale[0], -23.0 * scale[1])
    Lineto_r(61.0 * scale[0], -7.0 * scale[1])
    Lineto_r(1.0 * scale[0], 29.0 * scale[1])
    Curveto_r(1.0 * scale[0], 29.0 * scale[1], -1.0 * scale[0],
              29.0 * scale[1], -56.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-31.0 * scale[0], 2.0 * scale[1], -70.0 * scale[0], -
              3.0 * scale[1], -87.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(41.0 * scale[0], 1164.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(202.0 * scale[0], 1175.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(10.0 * scale[0], -11.0 * scale[1], 117.0 * scale[0], -
              35.0 * scale[1], 153.0 * scale[0], -35.0 * scale[1])
    Curveto_r(44.0 * scale[0], 1.0 * scale[1], 12.0 * scale[0],
              16.0 * scale[1], -50.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-27.0 * scale[0], 4.0 * scale[1], -63.0 * scale[0],
              9.0 * scale[1], -80.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 3.0 * scale[1], -27.0 * scale[0],
              2.0 * scale[1], -23.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(200.0 * scale[0], 1150.0 * scale[1], x, y)
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
    Moveto(300.0 * scale[0], 1121.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(25.0 * scale[0], -10.0 * scale[1], 48.0 * scale[0], -
              17.0 * scale[1], 51.0 * scale[0], -15.0 * scale[1])
    Curveto_r(4.0 * scale[0], 2.0 * scale[1], 12.0 * scale[0], -
              3.0 * scale[1], 19.0 * scale[0], -11.0 * scale[1])
    Curveto_r(7.0 * scale[0], -9.0 * scale[1], 28.0 * scale[0], -
              15.0 * scale[1], 49.0 * scale[0], -14.0 * scale[1])
    Curveto_r(20.0 * scale[0], 1.0 * scale[1], 28.0 * scale[0],
              3.0 * scale[1], 18.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 3.0 * scale[1], -16.0 * scale[0],
              11.0 * scale[1], -13.0 * scale[0], 19.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], 2.0 * scale[0],
              13.0 * scale[1], -3.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -20.0 *
              scale[0], -1.0 * scale[1], -33.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 4.0 * scale[1], -48.0 * scale[0],
              11.0 * scale[1], -78.0 * scale[0], 14.0 * scale[1])
    Lineto_r(-55.0 * scale[0], 7.0 * scale[1])
    Lineto_r(45.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(180.0 * scale[0], 1125.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], 115.0 * scale[0], -
              56.0 * scale[1], 143.0 * scale[0], -53.0 * scale[1])
    Curveto_r(29.0 * scale[0], 3.0 * scale[1], 29.0 * scale[0],
              4.0 * scale[1], 12.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 11.0 * scale[1], -17.0 * scale[0],
              11.0 * scale[1], -11.0 * scale[0], 1.0 * scale[1])
    Curveto_r(6.0 * scale[0], -10.0 * scale[1], 3.0 * scale[0], -
              9.0 * scale[1], -15.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 8.0 * scale[1], -40.0 * scale[0],
              18.0 * scale[1], -59.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 3.0 * scale[1], -43.0 * scale[0],
              9.0 * scale[1], -52.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 3.0 * scale[1], -18.0 * scale[0],
              3.0 * scale[1], -18.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(718.0 * scale[0], 1073.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(339.0 * scale[0], 1056.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -3.0 * scale[1], -67.0 * scale[0], -
              5.0 * scale[1], -144.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-77.0 * scale[0], -1.0 * scale[1], -146.0 *
              scale[0], -4.0 * scale[1], -153.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -7.0 * scale[1], -13.0 *
              scale[0], -19.0 * scale[1], 11.0 * scale[0], -15.0 * scale[1])
    Curveto_r(16.0 * scale[0], 3.0 * scale[1], 27.0 * scale[0], -
              4.0 * scale[1], 42.0 * scale[0], -26.0 * scale[1])
    Curveto_r(11.0 * scale[0], -17.0 * scale[1], 23.0 * scale[0], -
              31.0 * scale[1], 26.0 * scale[0], -31.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], -2.0 * scale[0], -
              53.0 * scale[1], -14.0 * scale[0], -67.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -14.0 * scale[1], -71.0 *
              scale[0], -18.0 * scale[1], -63.0 * scale[0], -5.0 * scale[1])
    Curveto_r(2.0 * scale[0], 4.0 * scale[1], -4.0 * scale[0],
              8.0 * scale[1], -15.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -19.0 * scale[0], -
              6.0 * scale[1], -18.0 * scale[0], -16.0 * scale[1])
    Curveto_r(1.0 * scale[0], -8.0 * scale[1], -1.0 * scale[0], -
              23.0 * scale[1], -6.0 * scale[0], -32.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -32.0 * scale[1], 2.0 * scale[0], -
              48.0 * scale[1], 44.0 * scale[0], -48.0 * scale[1])
    Curveto_r(29.0 * scale[0], 0.0 * scale[1], 44.0 * scale[0],
              6.0 * scale[1], 54.0 * scale[0], 21.0 * scale[1])
    Curveto_r(8.0 * scale[0], 11.0 * scale[1], 21.0 * scale[0],
              22.0 * scale[1], 28.0 * scale[0], 23.0 * scale[1])
    Curveto_r(8.0 * scale[0], 1.0 * scale[1], 32.0 * scale[0],
              10.0 * scale[1], 53.0 * scale[0], 19.0 * scale[1])
    Curveto_r(21.0 * scale[0], 10.0 * scale[1], 56.0 * scale[0],
              20.0 * scale[1], 78.0 * scale[0], 23.0 * scale[1])
    Curveto_r(23.0 * scale[0], 4.0 * scale[1], 38.0 * scale[0],
              12.0 * scale[1], 38.0 * scale[0], 21.0 * scale[1])
    Curveto_r(0.0 * scale[0], 38.0 * scale[1], 58.0 * scale[0],
              116.0 * scale[1], 100.0 * scale[0], 135.0 * scale[1])
    Curveto_r(9.0 * scale[0], 4.0 * scale[1], 0.0 * scale[0],
              7.0 * scale[1], -21.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 1.0 * scale[1], -38.0 *
              scale[0], -1.0 * scale[1], -40.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto_r(-39.0 * scale[0], -101.0 * scale[1], 0, 0)
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
    Moveto(628.0 * scale[0], 1053.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(711.0 * scale[0], 1046.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 34.0 * scale[0], -
              6.0 * scale[1], 68.0 * scale[0], -7.0 * scale[1])
    Curveto_r(39.0 * scale[0], -1.0 * scale[1], 58.0 * scale[0], -
              5.0 * scale[1], 49.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -6.0 * scale[1], -1.0 *
              scale[0], -9.0 * scale[1], 22.0 * scale[0], -9.0 * scale[1])
    Curveto_r(45.0 * scale[0], 0.0 * scale[1], 71.0 * scale[0], -
              15.0 * scale[1], 41.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -3.0 * scale[1], -19.0 *
              scale[0], -1.0 * scale[1], -15.0 * scale[0], 4.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], 3.0 * scale[0],
              9.0 * scale[1], 0.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              13.0 * scale[1], -20.0 * scale[0], -30.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -34.0 * scale[1], -15.0 *
              scale[0], -37.0 * scale[1], 9.0 * scale[0], -14.0 * scale[1])
    Curveto_r(12.0 * scale[0], 13.0 * scale[1], 18.0 * scale[0],
              14.0 * scale[1], 31.0 * scale[0], 4.0 * scale[1])
    Curveto_r(12.0 * scale[0], -11.0 * scale[1], 13.0 *
              scale[0], -10.0 * scale[1], 9.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 10.0 * scale[1], 2.0 * scale[0],
              14.0 * scale[1], 22.0 * scale[0], 13.0 * scale[1])
    Curveto_r(16.0 * scale[0], 0.0 * scale[1], 31.0 * scale[0],
              6.0 * scale[1], 35.0 * scale[0], 15.0 * scale[1])
    Curveto_r(4.0 * scale[0], 8.0 * scale[1], 6.0 * scale[0], -
              28.0 * scale[1], 6.0 * scale[0], -80.0 * scale[1])
    Curveto_r(0.0 * scale[0], -52.0 * scale[1], -3.0 * scale[0], -
              85.0 * scale[1], -5.0 * scale[0], -72.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 13.0 * scale[1], -9.0 * scale[0],
              19.0 * scale[1], -15.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -5.0 * scale[1], -8.0 *
              scale[0], -2.0 * scale[1], -2.0 * scale[0], 7.0 * scale[1])
    Curveto_r(14.0 * scale[0], 23.0 * scale[1], 13.0 * scale[0],
              39.0 * scale[1], -3.0 * scale[0], 39.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              6.0 * scale[1], -10.0 * scale[0], -12.0 * scale[1])
    Curveto_r(6.0 * scale[0], -16.0 * scale[1], -54.0 * scale[0], -
              18.0 * scale[1], -65.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 6.0 * scale[1], -8.0 * scale[0],
              6.0 * scale[1], -8.0 * scale[0], -2.0 * scale[1])
    Curveto_r(0.0 * scale[0], -15.0 * scale[1], 12.0 * scale[0], -
              23.0 * scale[1], 43.0 * scale[0], -25.0 * scale[1])
    Curveto_r(14.0 * scale[0], -1.0 * scale[1], 23.0 * scale[0], -
              6.0 * scale[1], 21.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              11.0 * scale[1], 10.0 * scale[0], -14.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 18.0 * scale[0], -
              20.0 * scale[1], 22.0 * scale[0], -37.0 * scale[1])
    Lineto_r(7.0 * scale[0], -32.0 * scale[1])
    Lineto_r(9.0 * scale[0], 30.0 * scale[1])
    Curveto_r(5.0 * scale[0], 17.0 * scale[1], 8.0 * scale[0],
              78.0 * scale[1], 7.0 * scale[0], 137.0 * scale[1])
    Lineto_r(-2.0 * scale[0], 106.0 * scale[1])
    Lineto_r(-136.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-74.0 * scale[0], 1.0 * scale[1], -133.0 *
              scale[0], -1.0 * scale[1], -130.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(751.0 * scale[0], 1013.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -10.0 * scale[1], 14.0 * scale[0], -
              20.0 * scale[1], 16.0 * scale[0], -22.0 * scale[1])
    Curveto_r(1.0 * scale[0], -1.0 * scale[1], 12.0 * scale[0],
              4.0 * scale[1], 25.0 * scale[0], 13.0 * scale[1])
    Curveto_r(12.0 * scale[0], 9.0 * scale[1], 18.0 * scale[0],
              16.0 * scale[1], 12.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              5.0 * scale[1], -22.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -9.0 * scale[1], -13.0 *
              scale[0], -7.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              17.0 * scale[1], -16.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              8.0 * scale[1], 3.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(477.0 * scale[0], 932.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-20.0 * scale[0], -2.0 * scale[1], -35.0 *
              scale[0], -7.0 * scale[1], -32.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 19.0 * scale[0], -
              7.0 * scale[1], 34.0 * scale[0], -4.0 * scale[1])
    Curveto_r(24.0 * scale[0], 5.0 * scale[1], 29.0 * scale[0],
              3.0 * scale[1], 28.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -11.0 * scale[1], 6.0 * scale[0], -
              19.0 * scale[1], 18.0 * scale[0], -21.0 * scale[1])
    Lineto_r(20.0 * scale[0], -3.0 * scale[1])
    Lineto_r(-20.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 5.0 * scale[1], -17.0 * scale[0],
              10.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(4.0 * scale[0], 1.0 * scale[1], 12.0 * scale[0],
              3.0 * scale[1], 17.0 * scale[0], 4.0 * scale[1])
    Curveto_r(6.0 * scale[0], 1.0 * scale[1], 22.0 * scale[0],
              3.0 * scale[1], 36.0 * scale[0], 4.0 * scale[1])
    Curveto_r(34.0 * scale[0], 1.0 * scale[1], 23.0 * scale[0],
              17.0 * scale[1], -13.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 0.0 * scale[1], -30.0 * scale[0],
              2.0 * scale[1], -33.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -22.0 * scale[0],
              4.0 * scale[1], -43.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(790.0 * scale[0], 931.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], 28.0 * scale[0], -
              33.0 * scale[1], 50.0 * scale[0], -46.0 * scale[1])
    Curveto_r(12.0 * scale[0], -6.0 * scale[1], 13.0 *
              scale[0], -5.0 * scale[1], 3.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 18.0 * scale[1], -16.0 * scale[0],
              29.0 * scale[1], 4.0 * scale[0], 29.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0],
              3.0 * scale[1], 10.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 9.0 * scale[1], -67.0 * scale[0],
              13.0 * scale[1], -67.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(378.0 * scale[0], 923.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(328.0 * scale[0], 913.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(608.0 * scale[0], 913.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(646.0 * scale[0], 905.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -11.0 * scale[1], 2.0 * scale[0], -
              15.0 * scale[1], 26.0 * scale[0], -15.0 * scale[1])
    Curveto_r(30.0 * scale[0], 0.0 * scale[1], 31.0 * scale[0],
              1.0 * scale[1], 12.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 18.0 * scale[1], -31.0 * scale[0],
              18.0 * scale[1], -38.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(555.0 * scale[0], 881.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              12.0 * scale[1], 3.0 * scale[0], -15.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 9.0 * scale[0],
              1.0 * scale[1], 9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], -3.0 * scale[0],
              19.0 * scale[1], -12.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(376.0 * scale[0], 863.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -32.0 * scale[1], 21.0 *
              scale[0], -75.0 * scale[1], 52.0 * scale[0], -70.0 * scale[1])
    Curveto_r(16.0 * scale[0], 3.0 * scale[1], 22.0 * scale[0], -
              1.0 * scale[1], 22.0 * scale[0], -14.0 * scale[1])
    Curveto_r(0.0 * scale[0], -24.0 * scale[1], 16.0 * scale[0], -
              33.0 * scale[1], 24.0 * scale[0], -13.0 * scale[1])
    Curveto_r(3.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              12.0 * scale[1], -5.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -3.0 * scale[1], -10.0 * scale[0],
              1.0 * scale[1], -9.0 * scale[0], 12.0 * scale[1])
    Curveto_r(4.0 * scale[0], 35.0 * scale[1], 0.0 * scale[0],
              43.0 * scale[1], -15.0 * scale[0], 37.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -3.0 * scale[1], -22.0 * scale[0],
              2.0 * scale[1], -30.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 11.0 * scale[1], -15.0 * scale[0],
              15.0 * scale[1], -16.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -4.0 * scale[0],
              1.0 * scale[1], -8.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 25.0 * scale[1], -7.0 * scale[0],
              25.0 * scale[1], -15.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(443.0 * scale[0], 867.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              11.0 * scale[1], 1.0 * scale[0], -14.0 * scale[1])
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], 6.0 *
              scale[0], -1.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], 4.0 * scale[0],
              10.0 * scale[1], 8.0 * scale[0], 7.0 * scale[1])
    Curveto_r(4.0 * scale[0], -2.0 * scale[1], 14.0 *
              scale[0], -1.0 * scale[1], 22.0 * scale[0], 4.0 * scale[1])
    Curveto_r(11.0 * scale[0], 7.0 * scale[1], 9.0 * scale[0],
              9.0 * scale[1], -8.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -1.0 * scale[1], -26.0 *
              scale[0], -5.0 * scale[1], -29.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(494.0 * scale[0], 808.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-14.0 * scale[0], -17.0 * scale[1], -15.0 *
              scale[0], -19.0 * scale[1], -2.0 * scale[0], -10.0 * scale[1])
    Curveto_r(15.0 * scale[0], 12.0 * scale[1], 17.0 * scale[0],
              9.0 * scale[1], 21.0 * scale[0], -35.0 * scale[1])
    Lineto_r(3.0 * scale[0], -48.0 * scale[1])
    Lineto_r(2.0 * scale[0], 58.0 * scale[1])
    Curveto_r(1.0 * scale[0], 31.0 * scale[1], 0.0 * scale[0],
              57.0 * scale[1], -1.0 * scale[0], 57.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              10.0 * scale[1], -23.0 * scale[0], -22.0 * scale[1])
    te.end_fill()
    Moveto(797.0 * scale[0], 765.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -11.0 * scale[1], -10.0 * scale[0], -
              27.0 * scale[1], -13.0 * scale[0], -35.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], 1.0 *
              scale[0], -5.0 * scale[1], 11.0 * scale[0], 8.0 * scale[1])
    Curveto_r(9.0 * scale[0], 12.0 * scale[1], 15.0 * scale[0],
              28.0 * scale[1], 13.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 7.0 * scale[1], -7.0 * scale[0],
              4.0 * scale[1], -11.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(645.0 * scale[0], 699.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-38.0 * scale[0], -24.0 * scale[1], -100.0 *
              scale[0], -25.0 * scale[1], -114.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              12.0 * scale[1], -11.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -38.0 * scale[1], 76.0 * scale[0], -
              47.0 * scale[1], 128.0 * scale[0], -15.0 * scale[1])
    Curveto_r(17.0 * scale[0], 11.0 * scale[1], 32.0 * scale[0],
              22.0 * scale[1], 32.0 * scale[0], 25.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], 0.0 * scale[0],
              7.0 * scale[1], -35.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(703.0 * scale[0], 673.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 17.0 * scale[0], -
              9.0 * scale[1], 17.0 * scale[0], -14.0 * scale[1])
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], 27.0 *
              scale[0], -12.0 * scale[1], 35.0 * scale[0], 1.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], 0.0 * scale[0],
              7.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -3.0 * scale[1], -18.0 *
              scale[0], -1.0 * scale[1], -22.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -14.0 * scale[0],
              10.0 * scale[1], -23.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -1.0 * scale[1], -15.0 *
              scale[0], -2.0 * scale[1], 1.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(560.0 * scale[0], 611.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -25.0 * scale[1], -13.0 *
              scale[0], -34.0 * scale[1], 1.0 * scale[0], -25.0 * scale[1])
    Curveto_r(7.0 * scale[0], 4.0 * scale[1], 10.0 * scale[0], -
              14.0 * scale[1], 7.0 * scale[0], -60.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -36.0 * scale[1], 1.0 * scale[0], -
              66.0 * scale[1], 5.0 * scale[0], -66.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 5.0 * scale[0], -
              4.0 * scale[1], 2.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              10.0 * scale[1], 9.0 * scale[0], -10.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0], -
              4.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], 66.0 *
              scale[0], -13.0 * scale[1], 91.0 * scale[0], 1.0 * scale[1])
    Curveto_r(11.0 * scale[0], 5.0 * scale[1], 17.0 * scale[0],
              14.0 * scale[1], 14.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 5.0 * scale[1], 2.0 * scale[0],
              14.0 * scale[1], 10.0 * scale[0], 21.0 * scale[1])
    Curveto_r(8.0 * scale[0], 7.0 * scale[1], 15.0 * scale[0],
              19.0 * scale[1], 15.0 * scale[0], 26.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], -9.0 * scale[0],
              9.0 * scale[1], -36.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-31.0 * scale[0], -18.0 * scale[1], -40.0 *
              scale[0], -19.0 * scale[1], -70.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-35.0 * scale[0], 13.0 * scale[1], -42.0 * scale[0],
              27.0 * scale[1], -46.0 * scale[0], 106.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 23.0 * scale[1], -3.0 * scale[0],
              42.0 * scale[1], -5.0 * scale[0], 42.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              9.0 * scale[1], -13.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(13.0 * scale[0], 373.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -21.0 * scale[1], -4.0 * scale[0], -
              68.0 * scale[1], -8.0 * scale[0], -105.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -67.0 * scale[1], -7.0 * scale[0], -
              68.0 * scale[1], 15.0 * scale[0], -68.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 34.0 * scale[0], -
              10.0 * scale[1], 47.0 * scale[0], -22.0 * scale[1])
    Curveto_r(20.0 * scale[0], -18.0 * scale[1], 23.0 *
              scale[0], -19.0 * scale[1], 23.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], 5.0 * scale[0],
              17.0 * scale[1], 10.0 * scale[0], 17.0 * scale[1])
    Curveto_r(18.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              84.0 * scale[1], -10.0 * scale[0], 115.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 17.0 * scale[1], -20.0 * scale[0],
              40.0 * scale[1], -20.0 * scale[0], 53.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], -4.0 * scale[0],
              22.0 * scale[1], -10.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0],
              7.0 * scale[1], -10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              15.0 * scale[1], -18.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -18.0 * scale[0], -
              8.0 * scale[1], -19.0 * scale[0], -37.0 * scale[1])
    te.end_fill()
    Moveto(0.0 * scale[0], 136.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 16.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(56.0 * scale[0], 93.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(750.0 * scale[0], 76.0 * scale[1], x, y)
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
    Moveto(710.0 * scale[0], 45.0 * scale[1], x, y)
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
    Moveto(0.0 * scale[0], 39.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 49.0 * scale[0], -
              23.0 * scale[1], 57.0 * scale[0], -15.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -4.0 * scale[0],
              6.0 * scale[1], -16.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0],
              4.0 * scale[1], -17.0 * scale[0], 8.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], -1.0 * scale[0],
              9.0 * scale[1], -9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              4.0 * scale[1], -15.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(893.0 * scale[0], 23.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 25.0 *
              scale[0], -2.0 * scale[1], 35.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -27.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(728.0 * scale[0], 13.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(17.0 * scale[0], -2.0 * scale[1], 47.0 *
              scale[0], -2.0 * scale[1], 65.0 * scale[0], 0.0 * scale[1])
    Curveto_r(17.0 * scale[0], 2.0 * scale[1], 3.0 * scale[0],
              4.0 * scale[1], -33.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-36.0 * scale[0], 0.0 * scale[1], -50.0 *
              scale[0], -2.0 * scale[1], -32.0 * scale[0], -4.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#759eaa')
    te.end_fill()
    Moveto(390.0 * scale[0], 1355.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -26.0 * scale[1], 7.0 * scale[0], -
              29.0 * scale[1], 35.0 * scale[0], -19.0 * scale[1])
    Curveto_r(14.0 * scale[0], 6.0 * scale[1], 14.0 * scale[0],
              8.0 * scale[1], -1.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 26.0 * scale[1], -34.0 * scale[0],
              24.0 * scale[1], -34.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(533.0 * scale[0], 1355.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -28.0 * scale[1], 47.0 * scale[0], -
              33.0 * scale[1], 47.0 * scale[0], -6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -7.0 * scale[0],
              18.0 * scale[1], -24.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -24.0 * scale[0], -
              5.0 * scale[1], -23.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(100.0 * scale[0], 1321.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-32.0 * scale[0], -5.0 * scale[1], -35.0 *
              scale[0], -9.0 * scale[1], -38.0 * scale[0], -42.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -35.0 * scale[1], -2.0 * scale[0], -
              36.0 * scale[1], 23.0 * scale[0], -31.0 * scale[1])
    Curveto_r(22.0 * scale[0], 4.0 * scale[1], 26.0 * scale[0],
              1.0 * scale[1], 23.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -11.0 * scale[1], -13.0 * scale[0], -
              23.0 * scale[1], -26.0 * scale[0], -29.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -5.0 * scale[1], -22.0 * scale[0], -
              18.0 * scale[1], -22.0 * scale[0], -28.0 * scale[1])
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 5.0 * scale[0], -
              18.0 * scale[1], 28.0 * scale[0], -12.0 * scale[1])
    Curveto_r(44.0 * scale[0], 11.0 * scale[1], 72.0 * scale[0],
              33.0 * scale[1], 72.0 * scale[0], 60.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], -5.0 * scale[0],
              27.0 * scale[1], -10.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -7.0 * scale[0],
              11.0 * scale[1], 1.0 * scale[0], 21.0 * scale[1])
    Curveto_r(9.0 * scale[0], 11.0 * scale[1], 8.0 * scale[0],
              14.0 * scale[1], -5.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -9.0 * scale[0], -
              10.0 * scale[1], -21.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-33.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0],
              25.0 * scale[1], 20.0 * scale[0], 28.0 * scale[1])
    Curveto_r(18.0 * scale[0], 2.0 * scale[1], 31.0 * scale[0],
              8.0 * scale[1], 28.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 14.0 * scale[1], -14.0 * scale[0],
              16.0 * scale[1], -57.0 * scale[0], 8.0 * scale[1])
    te.end_fill()
    Moveto(848.0 * scale[0], 1323.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-30.0 * scale[0], -5.0 * scale[1], -30.0 *
              scale[0], -5.0 * scale[1], -33.0 * scale[0], -45.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -23.0 * scale[1], 2.0 * scale[0], -
              28.0 * scale[1], 21.0 * scale[0], -28.0 * scale[1])
    Curveto_r(31.0 * scale[0], 0.0 * scale[1], 28.0 * scale[0], -
              39.0 * scale[1], -3.0 * scale[0], -51.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -5.0 * scale[1], -23.0 * scale[0], -
              15.0 * scale[1], -23.0 * scale[0], -24.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 8.0 * scale[0], -
              13.0 * scale[1], 33.0 * scale[0], -8.0 * scale[1])
    Curveto_r(82.0 * scale[0], 15.0 * scale[1], 91.0 * scale[0],
              83.0 * scale[1], 14.0 * scale[0], 107.0 * scale[1])
    Curveto_r(-27.0 * scale[0], 9.0 * scale[1], -10.0 * scale[0],
              26.0 * scale[1], 24.0 * scale[0], 26.0 * scale[1])
    Curveto_r(20.0 * scale[0], 0.0 * scale[1], 29.0 * scale[0],
              4.0 * scale[1], 27.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 14.0 * scale[1], -20.0 * scale[0],
              16.0 * scale[1], -60.0 * scale[0], 10.0 * scale[1])
    te.end_fill()
    Moveto(445.0 * scale[0], 1296.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-17.0 * scale[0], -7.0 * scale[1], -35.0 * scale[0], -
              19.0 * scale[1], -41.0 * scale[0], -27.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -15.0 * scale[1], -24.0 * scale[0], -
              110.0 * scale[1], -13.0 * scale[0], -103.0 * scale[1])
    Curveto_r(4.0 * scale[0], 2.0 * scale[1], 9.0 * scale[0], -
              3.0 * scale[1], 12.0 * scale[0], -10.0 * scale[1])
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], 16.0 * scale[0], -
              20.0 * scale[1], 29.0 * scale[0], -26.0 * scale[1])
    Curveto_r(19.0 * scale[0], -9.0 * scale[1], 21.0 *
              scale[0], -9.0 * scale[1], 8.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 13.0 * scale[1], -18.0 * scale[0],
              20.0 * scale[1], -27.0 * scale[0], 63.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 26.0 * scale[1], 37.0 * scale[0],
              89.0 * scale[1], 62.0 * scale[0], 93.0 * scale[1])
    Curveto_r(30.0 * scale[0], 3.0 * scale[1], 67.0 * scale[0], -
              54.0 * scale[1], 52.0 * scale[0], -79.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -14.0 * scale[1], -9.0 *
              scale[0], -21.0 * scale[1], 1.0 * scale[0], -31.0 * scale[1])
    Curveto_r(16.0 * scale[0], -16.0 * scale[1], -13.0 * scale[0], -
              48.0 * scale[1], -45.0 * scale[0], -48.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -23.0 * scale[0], -
              4.0 * scale[1], -23.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -17.0 * scale[1], 41.0 * scale[0], -
              11.0 * scale[1], 76.0 * scale[0], 11.0 * scale[1])
    Curveto_r(23.0 * scale[0], 14.0 * scale[1], 35.0 * scale[0],
              30.0 * scale[1], 39.0 * scale[0], 52.0 * scale[1])
    Curveto_r(8.0 * scale[0], 44.0 * scale[1], 1.0 * scale[0],
              95.0 * scale[1], -15.0 * scale[0], 110.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              9.0 * scale[1], -6.0 * scale[0], 0.0 * scale[1])
    Curveto_r(4.0 * scale[0], -8.0 * scale[1], 1.0 * scale[0], -
              13.0 * scale[1], -8.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0],
              4.0 * scale[1], -18.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 17.0 * scale[1], -52.0 * scale[0],
              21.0 * scale[1], -83.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(885.0 * scale[0], 1280.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 11.0 * scale[0], -
              8.0 * scale[1], 16.0 * scale[0], -5.0 * scale[1])
    Curveto_r(14.0 * scale[0], 9.0 * scale[1], 11.0 * scale[0],
              15.0 * scale[1], -7.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              5.0 * scale[1], -9.0 * scale[0], -10.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#cdbd5a')
    te.end_fill()
    Moveto(450.0 * scale[0], 1400.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(380.0 * scale[0], 1396.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 7.0 * scale[0], -
              7.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 12.0 *
              scale[0], -2.0 * scale[1], 9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], -25.0 * scale[0],
              14.0 * scale[1], -25.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(380.0 * scale[0], 1315.0 * scale[1], x, y)
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
    Moveto(576.0 * scale[0], 1313.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(400.0 * scale[0], 1052.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-31.0 * scale[0], -14.0 * scale[1], -68.0 *
              scale[0], -55.0 * scale[1], -85.0 * scale[0], -93.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -37.0 * scale[1], -13.0 *
              scale[0], -69.0 * scale[1], 5.0 * scale[0], -40.0 * scale[1])
    Curveto_r(5.0 * scale[0], 8.0 * scale[1], 17.0 * scale[0],
              12.0 * scale[1], 30.0 * scale[0], 8.0 * scale[1])
    Curveto_r(16.0 * scale[0], -4.0 * scale[1], 23.0 * scale[0],
              0.0 * scale[1], 31.0 * scale[0], 19.0 * scale[1])
    Curveto_r(12.0 * scale[0], 34.0 * scale[1], 11.0 * scale[0],
              39.0 * scale[1], -6.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -10.0 * scale[1], -15.0 *
              scale[0], -10.0 * scale[1], -15.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 7.0 * scale[0],
              17.0 * scale[1], 15.0 * scale[0], 21.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 15.0 * scale[0],
              12.0 * scale[1], 15.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 25.0 * scale[1], 21.0 * scale[0],
              31.0 * scale[1], 130.0 * scale[0], 37.0 * scale[1])
    Lineto_r(105.0 * scale[0], 5.0 * scale[1])
    Lineto_r(-105.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-58.0 * scale[0], 1.0 * scale[1], -112.0 *
              scale[0], -1.0 * scale[1], -120.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(685.0 * scale[0], 1043.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(31.0 * scale[0], -8.0 * scale[1], 62.0 * scale[0], -
              41.0 * scale[1], 68.0 * scale[0], -72.0 * scale[1])
    Curveto_r(3.0 * scale[0], -16.0 * scale[1], 13.0 * scale[0], -
              36.0 * scale[1], 23.0 * scale[0], -45.0 * scale[1])
    Curveto_r(9.0 * scale[0], -9.0 * scale[1], 14.0 * scale[0], -
              27.0 * scale[1], 12.0 * scale[0], -39.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -20.0 * scale[1], 0.0 * scale[0], -
              22.0 * scale[1], 49.0 * scale[0], -23.0 * scale[1])
    Curveto_r(45.0 * scale[0], 0.0 * scale[1], 56.0 * scale[0], -
              5.0 * scale[1], 77.0 * scale[0], -29.0 * scale[1])
    Curveto_r(27.0 * scale[0], -31.0 * scale[1], 41.0 * scale[0], -
              87.0 * scale[1], 37.0 * scale[0], -149.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -27.0 * scale[1], 1.0 * scale[0], -
              37.0 * scale[1], 10.0 * scale[0], -34.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 14.0 * scale[0],
              31.0 * scale[1], 15.0 * scale[0], 89.0 * scale[1])
    Curveto_r(2.0 * scale[0], 51.0 * scale[1], 0.0 * scale[0],
              74.0 * scale[1], -5.0 * scale[0], 59.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -25.0 * scale[1], -8.0 *
              scale[0], -25.0 * scale[1], -15.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 17.0 * scale[1], -14.0 * scale[0],
              34.0 * scale[1], -22.0 * scale[0], 37.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 3.0 * scale[1], -13.0 * scale[0],
              9.0 * scale[1], -10.0 * scale[0], 14.0 * scale[1])
    Curveto_r(2.0 * scale[0], 4.0 * scale[1], -7.0 * scale[0],
              9.0 * scale[1], -21.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-28.0 * scale[0], 2.0 * scale[1], -43.0 * scale[0],
              9.0 * scale[1], -43.0 * scale[0], 21.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 33.0 * scale[0], 3.0 * scale[1])
    Curveto_r(17.0 * scale[0], -3.0 * scale[1], 30.0 *
              scale[0], -2.0 * scale[1], 27.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -18.0 * scale[0],
              7.0 * scale[1], -35.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 2.0 * scale[1], -33.0 * scale[0],
              8.0 * scale[1], -37.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 5.0 * scale[1], -10.0 * scale[0],
              6.0 * scale[1], -14.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -3.0 * scale[1], -2.0 * scale[0], -
              13.0 * scale[1], 4.0 * scale[0], -20.0 * scale[1])
    Curveto_r(9.0 * scale[0], -10.0 * scale[1], 8.0 * scale[0], -
              14.0 * scale[1], -3.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0],
              4.0 * scale[1], -15.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], -9.0 * scale[0],
              17.0 * scale[1], -20.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 11.0 * scale[1], -20.0 * scale[0],
              27.0 * scale[1], -20.0 * scale[0], 35.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -6.0 * scale[0],
              15.0 * scale[1], -12.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0],
              4.0 * scale[1], 2.0 * scale[0], 10.0 * scale[1])
    Curveto_r(10.0 * scale[0], 6.0 * scale[1], 11.0 * scale[0],
              10.0 * scale[1], 3.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 6.0 * scale[0],
              10.0 * scale[1], 13.0 * scale[0], 10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 1.0 * scale[1], 26.0 * scale[0],
              7.0 * scale[1], 42.0 * scale[0], 14.0 * scale[1])
    Lineto_r(30.0 * scale[0], 13.0 * scale[1])
    Lineto_r(-50.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-27.0 * scale[0], 1.0 * scale[1], -68.0 * scale[0],
              3.0 * scale[1], -90.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 3.0 * scale[1], -31.0 * scale[0],
              2.0 * scale[1], -20.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto_r(75.0 * scale[0], -23.0 * scale[1], 0, 0)
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
    Moveto(880.0 * scale[0], 1010.0 * scale[1], x, y)
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
    Moveto(875.0 * scale[0], 959.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0], -
              12.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 17.0 * scale[1], 1.0 * scale[0],
              20.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(415.0 * scale[0], 940.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(846.0 * scale[0], 941.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              11.0 * scale[1], 9.0 * scale[0], -14.0 * scale[1])
    Curveto_r(9.0 * scale[0], -4.0 * scale[1], 12.0 *
              scale[0], -1.0 * scale[1], 8.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 16.0 * scale[1], -10.0 * scale[0],
              17.0 * scale[1], -17.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(618.0 * scale[0], 928.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -5.0 * scale[1], 16.0 * scale[0], -
              8.0 * scale[1], 23.0 * scale[0], -6.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 3.0 * scale[0],
              7.0 * scale[1], -10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 4.0 * scale[1], -21.0 * scale[0],
              3.0 * scale[1], -13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(89.0 * scale[0], 913.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -21.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(478.0 * scale[0], 913.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(590.0 * scale[0], 908.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 14.0 * scale[0], -
              8.0 * scale[1], 30.0 * scale[0], -8.0 * scale[1])
    Curveto_r(17.0 * scale[0], 0.0 * scale[1], 30.0 * scale[0],
              2.0 * scale[1], 30.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 2.0 * scale[1], -13.0 * scale[0],
              6.0 * scale[1], -30.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 3.0 * scale[1], -30.0 * scale[0],
              1.0 * scale[1], -30.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(670.0 * scale[0], 916.0 * scale[1], x, y)
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
    Moveto(513.0 * scale[0], 897.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], 3.0 * scale[0], -
              8.0 * scale[1], 15.0 * scale[0], -5.0 * scale[1])
    Curveto_r(13.0 * scale[0], 4.0 * scale[1], 20.0 * scale[0],
              2.0 * scale[1], 16.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -16.0 *
              scale[0], -7.0 * scale[1], -27.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 3.0 * scale[1], -28.0 * scale[0], -
              3.0 * scale[1], -43.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -16.0 * scale[1], -29.0 *
              scale[0], -22.0 * scale[1], -43.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 4.0 * scale[1], -20.0 * scale[0],
              2.0 * scale[1], -15.0 * scale[0], -12.0 * scale[1])
    Curveto_r(4.0 * scale[0], -10.0 * scale[1], 14.0 * scale[0], -
              15.0 * scale[1], 25.0 * scale[0], -12.0 * scale[1])
    Curveto_r(19.0 * scale[0], 5.0 * scale[1], 23.0 * scale[0], -
              2.0 * scale[1], 19.0 * scale[0], -38.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -16.0 * scale[1], 5.0 * scale[0], -
              13.0 * scale[1], 29.0 * scale[0], 15.0 * scale[1])
    Lineto_r(30.0 * scale[0], 35.0 * scale[1])
    Lineto_r(1.0 * scale[0], -58.0 * scale[1])
    Curveto_r(0.0 * scale[0], -79.0 * scale[1], 11.0 * scale[0], -
              97.0 * scale[1], 58.0 * scale[0], -97.0 * scale[1])
    Curveto_r(20.0 * scale[0], 0.0 * scale[1], 44.0 * scale[0],
              5.0 * scale[1], 52.0 * scale[0], 10.0 * scale[1])
    Curveto_r(10.0 * scale[0], 6.0 * scale[1], 0.0 * scale[0],
              8.0 * scale[1], -33.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-38.0 * scale[0], -2.0 * scale[1], -50.0 * scale[0],
              1.0 * scale[1], -58.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 27.0 * scale[1], -11.0 * scale[0],
              96.0 * scale[1], 6.0 * scale[0], 129.0 * scale[1])
    Curveto_r(9.0 * scale[0], 17.0 * scale[1], 12.0 * scale[0],
              30.0 * scale[1], 8.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], 1.0 * scale[0],
              7.0 * scale[1], 11.0 * scale[0], 15.0 * scale[1])
    Curveto_r(15.0 * scale[0], 11.0 * scale[1], 16.0 * scale[0],
              15.0 * scale[1], 5.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 7.0 * scale[1], -49.0 * scale[0],
              4.0 * scale[1], -56.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto_r(22.0 * scale[0], -37.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -13.0 * scale[0], -
              10.0 * scale[1], -21.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0],
              5.0 * scale[1], -14.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 9.0 * scale[0],
              10.0 * scale[1], 21.0 * scale[0], 10.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0], -
              4.0 * scale[1], 14.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(424.0 * scale[0], 889.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], -2.0 * scale[0], -
              15.0 * scale[1], 3.0 * scale[0], -20.0 * scale[1])
    Curveto_r(5.0 * scale[0], -5.0 * scale[1], 9.0 * scale[0], -
              1.0 * scale[1], 9.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 23.0 * scale[1], -2.0 * scale[0],
              24.0 * scale[1], -12.0 * scale[0], 9.0 * scale[1])
    te.end_fill()
    Moveto(729.0 * scale[0], 877.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -8.0 * scale[1], 7.0 * scale[0], -
              18.0 * scale[1], 3.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -5.0 * scale[1], -1.0 *
              scale[0], -5.0 * scale[1], 6.0 * scale[0], -1.0 * scale[1])
    Curveto_r(10.0 * scale[0], 6.0 * scale[1], 10.0 * scale[0],
              11.0 * scale[1], 1.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 8.0 * scale[1], -14.0 * scale[0],
              14.0 * scale[1], -16.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], 0.0 * scale[0], -
              6.0 * scale[1], 6.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(659.0 * scale[0], 713.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(16.0 * scale[0], 13.0 * scale[1], 21.0 * scale[0],
              21.0 * scale[1], 13.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              8.0 * scale[1], -17.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(762.0 * scale[0], 710.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(680.0 * scale[0], 696.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 8.0 * scale[0], -
              16.0 * scale[1], 18.0 * scale[0], -16.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 23.0 * scale[0], -
              5.0 * scale[1], 30.0 * scale[0], -12.0 * scale[1])
    Curveto_r(9.0 * scale[0], -9.0 * scale[1], 15.0 *
              scale[0], -9.0 * scale[1], 24.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 9.0 * scale[1], 8.0 * scale[0],
              12.0 * scale[1], -8.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -30.0 * scale[0],
              7.0 * scale[1], -42.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 14.0 * scale[1], -22.0 * scale[0],
              14.0 * scale[1], -22.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(806.0 * scale[0], 687.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0], -
              15.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 0.0 * scale[0],
              11.0 * scale[1], -7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              8.0 * scale[1], -5.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(579.0 * scale[0], 624.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -18.0 * scale[1], 2.0 * scale[0], -
              80.0 * scale[1], 7.0 * scale[0], -105.0 * scale[1])
    Curveto_r(7.0 * scale[0], -37.0 * scale[1], 60.0 * scale[0], -
              55.0 * scale[1], 102.0 * scale[0], -33.0 * scale[1])
    Curveto_r(36.0 * scale[0], 18.0 * scale[1], 52.0 * scale[0],
              42.0 * scale[1], 51.0 * scale[0], 76.0 * scale[1])
    Curveto_r(0.0 * scale[0], 23.0 * scale[1], 0.0 * scale[0],
              23.0 * scale[1], -9.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -27.0 * scale[1], -26.0 *
              scale[0], -37.0 * scale[1], -62.0 * scale[0], -41.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -2.0 * scale[1], -33.0 * scale[0],
              4.0 * scale[1], -50.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 17.0 * scale[1], -23.0 * scale[0],
              40.0 * scale[1], -25.0 * scale[0], 52.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 23.0 * scale[1], -12.0 * scale[0],
              37.0 * scale[1], -14.0 * scale[0], 22.0 * scale[1])
    te.end_fill()
    Moveto(863.0 * scale[0], 380.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -30.0 * scale[1], 2.0 * scale[0], -
              43.0 * scale[1], 4.0 * scale[0], -27.0 * scale[1])
    Curveto_r(2.0 * scale[0], 15.0 * scale[1], 2.0 * scale[0],
              39.0 * scale[1], 0.0 * scale[0], 55.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 15.0 * scale[1], -4.0 * scale[0],
              2.0 * scale[1], -4.0 * scale[0], -28.0 * scale[1])
    te.end_fill()
    Moveto(956.0 * scale[0], 311.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0], -
              20.0 * scale[1], -1.0 * scale[0], -31.0 * scale[1])
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 1.0 * scale[0], -
              28.0 * scale[1], -5.0 * scale[0], -40.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -23.0 * scale[1], -50.0 *
              scale[0], -27.0 * scale[1], -50.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 7.0 * scale[0],
              15.0 * scale[1], 15.0 * scale[0], 15.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              7.0 * scale[1], 15.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 22.0 * scale[1], -23.0 * scale[0],
              12.0 * scale[1], -37.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -13.0 * scale[1], -13.0 * scale[0], -
              18.0 * scale[1], -13.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -5.0 * scale[0],
              10.0 * scale[1], -11.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -4.0 * scale[1], -8.0 * scale[0], -
              13.0 * scale[1], -5.0 * scale[0], -21.0 * scale[1])
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], 1.0 * scale[0], -
              14.0 * scale[1], -3.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 6.0 * scale[1], -9.0 * scale[0],
              1.0 * scale[1], -16.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -15.0 * scale[1], -10.0 *
              scale[0], -19.0 * scale[1], -1.0 * scale[0], -14.0 * scale[1])
    Curveto_r(7.0 * scale[0], 5.0 * scale[1], 10.0 * scale[0],
              3.0 * scale[1], 7.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -10.0 * scale[0], -
              13.0 * scale[1], -16.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 2.0 * scale[1], -8.0 * scale[0], -
              4.0 * scale[1], 0.0 * scale[0], -22.0 * scale[1])
    Curveto_r(6.0 * scale[0], -14.0 * scale[1], 15.0 * scale[0], -
              25.0 * scale[1], 19.0 * scale[0], -25.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 6.0 * scale[0], -
              6.0 * scale[1], 3.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -7.0 * scale[1], 2.0 * scale[0], -
              31.0 * scale[1], 10.0 * scale[0], -54.0 * scale[1])
    Curveto_r(8.0 * scale[0], -23.0 * scale[1], 13.0 * scale[0], -
              43.0 * scale[1], 11.0 * scale[0], -45.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -2.0 * scale[1], 11.0 *
              scale[0], -5.0 * scale[1], 30.0 * scale[0], -6.0 * scale[1])
    Curveto_r(39.0 * scale[0], -3.0 * scale[1], 79.0 * scale[0],
              14.0 * scale[1], 70.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 5.0 * scale[1], -1.0 * scale[0],
              9.0 * scale[1], 5.0 * scale[0], 9.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              36.0 * scale[1], 8.0 * scale[0], 126.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 124.0 * scale[1], -9.0 * scale[0],
              157.0 * scale[1], -22.0 * scale[0], 135.0 * scale[1])
    te.end_fill()
    Moveto_r(-28.0 * scale[0], -288.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -2.0 * scale[1], -26.0 *
              scale[0], -2.0 * scale[1], -35.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              5.0 * scale[1], 17.0 * scale[0], 5.0 * scale[1])
    Curveto_r(19.0 * scale[0], 0.0 * scale[1], 27.0 * scale[0], -
              2.0 * scale[1], 18.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(4.0 * scale[0], 173.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -35.0 * scale[1], 14.0 * scale[0], -
              55.0 * scale[1], 28.0 * scale[0], -47.0 * scale[1])
    Curveto_r(7.0 * scale[0], 4.0 * scale[1], 8.0 * scale[0],
              2.0 * scale[1], 4.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -9.0 * scale[1], -11.0 *
              scale[0], -9.0 * scale[1], -23.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 11.0 * scale[1], -14.0 * scale[0],
              6.0 * scale[1], -11.0 * scale[0], -32.0 * scale[1])
    Curveto_r(2.0 * scale[0], -33.0 * scale[1], 7.0 * scale[0], -
              43.0 * scale[1], 18.0 * scale[0], -41.0 * scale[1])
    Curveto_r(11.0 * scale[0], 2.0 * scale[1], 11.0 * scale[0], -
              1.0 * scale[1], -3.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -12.0 * scale[1], -16.0 *
              scale[0], -14.0 * scale[1], -1.0 * scale[0], -20.0 * scale[1])
    Curveto_r(31.0 * scale[0], -12.0 * scale[1], 82.0 *
              scale[0], -6.0 * scale[1], 88.0 * scale[0], 10.0 * scale[1])
    Curveto_r(11.0 * scale[0], 27.0 * scale[1], 7.0 * scale[0],
              35.0 * scale[1], -16.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-28.0 * scale[0], -3.0 * scale[1], -58.0 * scale[0],
              10.0 * scale[1], -58.0 * scale[0], 24.0 * scale[1])
    Curveto_r(0.0 * scale[0], 18.0 * scale[1], 31.0 * scale[0],
              46.0 * scale[1], 46.0 * scale[0], 40.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 11.0 * scale[0], -
              10.0 * scale[1], 7.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -1.0 *
              scale[0], -7.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 11.0 * scale[0],
              26.0 * scale[1], 11.0 * scale[0], 49.0 * scale[1])
    Curveto_r(0.0 * scale[0], 27.0 * scale[1], -3.0 * scale[0],
              36.0 * scale[1], -7.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -17.0 * scale[1], -8.0 *
              scale[0], -17.0 * scale[1], -25.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 12.0 * scale[1], -29.0 * scale[0],
              21.0 * scale[1], -41.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 0.0 * scale[1], -22.0 * scale[0], -
              5.0 * scale[1], -21.0 * scale[0], -27.0 * scale[1])
    te.end_fill()
    Moveto_r(49.0 * scale[0], -150.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              5.0 * scale[1], 12.0 * scale[0], 5.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#1e140a')
    te.end_fill()
    Moveto(10.0 * scale[0], 1415.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -9.0 * scale[1], -10.0 * scale[0], -
              18.0 * scale[1], -6.0 * scale[0], -22.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 6.0 *
              scale[0], -1.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 10.0 * scale[0],
              16.0 * scale[1], 23.0 * scale[0], 21.0 * scale[1])
    Curveto_r(15.0 * scale[0], 6.0 * scale[1], 17.0 * scale[0],
              9.0 * scale[1], 6.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 1.0 * scale[1], -22.0 * scale[0], -
              6.0 * scale[1], -29.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(890.0 * scale[0], 1423.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(51.0 * scale[0], -5.0 * scale[1], 67.0 * scale[0], -
              15.0 * scale[1], 73.0 * scale[0], -46.0 * scale[1])
    Curveto_r(3.0 * scale[0], -16.0 * scale[1], 5.0 *
              scale[0], -13.0 * scale[1], 6.0 * scale[0], 9.0 * scale[1])
    Curveto_r(1.0 * scale[0], 38.0 * scale[1], -12.0 * scale[0],
              45.0 * scale[1], -77.0 * scale[0], 42.0 * scale[1])
    Lineto_r(-47.0 * scale[0], -1.0 * scale[1])
    Lineto_r(45.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(68.0 * scale[0], 1223.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(958.0 * scale[0], 1085.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -14.0 * scale[1], -1.0 *
              scale[0], -28.0 * scale[1], 3.0 * scale[0], -31.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 9.0 * scale[0],
              9.0 * scale[1], 9.0 * scale[0], 25.0 * scale[1])
    Curveto_r(0.0 * scale[0], 38.0 * scale[1], -6.0 * scale[0],
              40.0 * scale[1], -12.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(0.0 * scale[0], 1077.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 8.0 * scale[0], -
              17.0 * scale[1], 18.0 * scale[0], -17.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              4.0 * scale[1], 7.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 4.0 * scale[1], -13.0 * scale[0],
              11.0 * scale[1], -17.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 5.0 * scale[1], -8.0 * scale[0],
              2.0 * scale[1], -8.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(331.0 * scale[0], 905.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-24.0 * scale[0], -7.0 * scale[1], -53.0 * scale[0], -
              22.0 * scale[1], -65.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -11.0 * scale[1], -45.0 *
              scale[0], -24.0 * scale[1], -76.0 * scale[0], -29.0 * scale[1])
    Curveto_r(-47.0 * scale[0], -7.0 * scale[1], -55.0 * scale[0], -
              12.0 * scale[1], -58.0 * scale[0], -31.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -13.0 * scale[1], 2.0 * scale[0], -
              29.0 * scale[1], 8.0 * scale[0], -37.0 * scale[1])
    Curveto_r(16.0 * scale[0], -19.0 * scale[1], 4.0 * scale[0], -
              35.0 * scale[1], -26.0 * scale[0], -35.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 0.0 * scale[1], -24.0 * scale[0], -
              3.0 * scale[1], -19.0 * scale[0], -22.0 * scale[1])
    Curveto_r(6.0 * scale[0], -18.0 * scale[1], 4.0 * scale[0], -
              20.0 * scale[1], -11.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 7.0 * scale[1], -18.0 * scale[0],
              6.0 * scale[1], -2.0 * scale[0], -10.0 * scale[1])
    Curveto_r(13.0 * scale[0], -13.0 * scale[1], 14.0 *
              scale[0], -21.0 * scale[1], 6.0 * scale[0], -38.0 * scale[1])
    Curveto_r(-24.0 * scale[0], -47.0 * scale[1], -27.0 *
              scale[0], -54.0 * scale[1], -22.0 * scale[0], -73.0 * scale[1])
    Curveto_r(4.0 * scale[0], -13.0 * scale[1], 0.0 * scale[0], -
              23.0 * scale[1], -11.0 * scale[0], -27.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -5.0 * scale[1], -15.0 *
              scale[0], -7.0 * scale[1], -1.0 * scale[0], -22.0 * scale[1])
    Curveto_r(12.0 * scale[0], -12.0 * scale[1], 15.0 * scale[0], -
              27.0 * scale[1], 10.0 * scale[0], -59.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -25.0 * scale[1], -1.0 *
              scale[0], -46.0 * scale[1], 5.0 * scale[0], -49.0 * scale[1])
    Curveto_r(5.0 * scale[0], -4.0 * scale[1], 13.0 * scale[0], -
              28.0 * scale[1], 17.0 * scale[0], -54.0 * scale[1])
    Curveto_r(3.0 * scale[0], -26.0 * scale[1], 13.0 * scale[0], -
              54.0 * scale[1], 21.0 * scale[0], -63.0 * scale[1])
    Curveto_r(11.0 * scale[0], -14.0 * scale[1], 12.0 * scale[0], -
              35.0 * scale[1], 5.0 * scale[0], -115.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -55.0 * scale[1], -5.0 * scale[0], -
              101.0 * scale[1], 0.0 * scale[0], -102.0 * scale[1])
    Curveto_r(4.0 * scale[0], -2.0 * scale[1], 6.0 * scale[0], -
              8.0 * scale[1], 3.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -3.0 * scale[0], -
              21.0 * scale[1], 1.0 * scale[0], -35.0 * scale[1])
    Lineto_r(6.0 * scale[0], -25.0 * scale[1])
    Lineto_r(279.0 * scale[0], 0.0 * scale[1])
    Curveto_r(153.0 * scale[0], 0.0 * scale[1], 279.0 * scale[0],
              3.0 * scale[1], 279.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], 21.0 * scale[0],
              30.0 * scale[1], 46.0 * scale[0], 57.0 * scale[1])
    Curveto_r(113.0 * scale[0], 121.0 * scale[1], 148.0 * scale[0],
              223.0 * scale[1], 124.0 * scale[0], 357.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 68.0 * scale[1], -32.0 * scale[0],
              122.0 * scale[1], -51.0 * scale[0], 133.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 4.0 * scale[1], -9.0 * scale[0],
              2.0 * scale[1], -9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 4.0 * scale[0], -
              11.0 * scale[1], 10.0 * scale[0], -13.0 * scale[1])
    Curveto_r(15.0 * scale[0], -5.0 * scale[1], 33.0 * scale[0], -
              156.0 * scale[1], 27.0 * scale[0], -232.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -45.0 * scale[1], -12.0 * scale[0], -
              75.0 * scale[1], -24.0 * scale[0], -88.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -11.0 * scale[1], -18.0 *
              scale[0], -25.0 * scale[1], -18.0 * scale[0], -31.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -22.0 * scale[1], -18.0 * scale[0], -
              52.0 * scale[1], -42.0 * scale[0], -74.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -12.0 * scale[1], -23.0 *
              scale[0], -25.0 * scale[1], -23.0 * scale[0], -28.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], -35.0 * scale[0], -
              42.0 * scale[1], -55.0 * scale[0], -49.0 * scale[1])
    Curveto_r(-24.0 * scale[0], -10.0 * scale[1], -127.0 *
              scale[0], -11.0 * scale[1], -170.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 3.0 * scale[1], -38.0 * scale[0],
              6.0 * scale[1], -47.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 1.0 * scale[1], -15.0 * scale[0],
              6.0 * scale[1], -12.0 * scale[0], 16.0 * scale[1])
    Curveto_r(4.0 * scale[0], 8.0 * scale[1], 1.0 * scale[0],
              15.0 * scale[1], -5.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0], -
              7.0 * scale[1], -17.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -26.0 * scale[1], -37.0 *
              scale[0], -18.0 * scale[1], -30.0 * scale[0], 8.0 * scale[1])
    Curveto_r(4.0 * scale[0], 16.0 * scale[1], -1.0 * scale[0],
              28.0 * scale[1], -14.0 * scale[0], 40.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 19.0 * scale[1], -18.0 * scale[0],
              64.0 * scale[1], 10.0 * scale[0], 107.0 * scale[1])
    Curveto_r(8.0 * scale[0], 14.0 * scale[1], 20.0 * scale[0],
              34.0 * scale[1], 26.0 * scale[0], 44.0 * scale[1])
    Curveto_r(6.0 * scale[0], 11.0 * scale[1], 23.0 * scale[0],
              24.0 * scale[1], 38.0 * scale[0], 29.0 * scale[1])
    Curveto_r(29.0 * scale[0], 10.0 * scale[1], 95.0 * scale[0],
              74.0 * scale[1], 96.0 * scale[0], 93.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 14.0 * scale[0],
              9.0 * scale[1], 47.0 * scale[0], 3.0 * scale[1])
    Curveto_r(30.0 * scale[0], -6.0 * scale[1], 51.0 *
              scale[0], -5.0 * scale[1], 57.0 * scale[0], 1.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], -3.0 * scale[0],
              10.0 * scale[1], -30.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-46.0 * scale[0], 0.0 * scale[1], -56.0 * scale[0],
              12.0 * scale[1], -85.0 * scale[0], 102.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 48.0 * scale[1], -16.0 * scale[0],
              63.0 * scale[1], -6.0 * scale[0], 79.0 * scale[1])
    Curveto_r(6.0 * scale[0], 10.0 * scale[1], 14.0 * scale[0],
              19.0 * scale[1], 17.0 * scale[0], 19.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              7.0 * scale[1], 26.0 * scale[0], 15.0 * scale[1])
    Curveto_r(16.0 * scale[0], 13.0 * scale[1], 14.0 * scale[0],
              13.0 * scale[1], -19.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -9.0 * scale[1], -42.0 * scale[0], -
              13.0 * scale[1], -47.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 9.0 * scale[1], -47.0 * scale[0],
              85.0 * scale[1], -55.0 * scale[0], 128.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 27.0 * scale[1], -12.0 * scale[0],
              37.0 * scale[1], -26.0 * scale[0], 37.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 0.0 * scale[1], -69.0 * scale[0],
              38.0 * scale[1], -69.0 * scale[0], 58.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], 9.0 * scale[0],
              25.0 * scale[1], 20.0 * scale[0], 39.0 * scale[1])
    Curveto_r(35.0 * scale[0], 45.0 * scale[1], 29.0 * scale[0],
              49.0 * scale[1], -39.0 * scale[0], 28.0 * scale[1])
    te.end_fill()
    Moveto_r(-121.0 * scale[0], -95.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-20.0 * scale[0], -13.0 * scale[1], -33.0 *
              scale[0], -13.0 * scale[1], -25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 14.0 * scale[0],
              10.0 * scale[1], 23.0 * scale[0], 10.0 * scale[1])
    Curveto_r(15.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0], -
              2.0 * scale[1], 2.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto_r(10.0 * scale[0], -732.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(10.0 * scale[0], -21.0 * scale[1], 15.0 * scale[0], -
              40.0 * scale[1], 11.0 * scale[0], -43.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -6.0 * scale[1], -64.0 * scale[0],
              9.0 * scale[1], -88.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 10.0 * scale[1], -15.0 * scale[0],
              11.0 * scale[1], -1.0 * scale[0], 6.0 * scale[1])
    Curveto_r(14.0 * scale[0], -4.0 * scale[1], 17.0 * scale[0],
              1.0 * scale[1], 16.0 * scale[0], 32.0 * scale[1])
    Curveto_r(0.0 * scale[0], 20.0 * scale[1], 0.0 * scale[0],
              41.0 * scale[1], 1.0 * scale[0], 46.0 * scale[1])
    Curveto_r(2.0 * scale[0], 16.0 * scale[1], 42.0 * scale[0], -
              28.0 * scale[1], 61.0 * scale[0], -66.0 * scale[1])
    te.end_fill()
    Moveto(410.0 * scale[0], 891.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -13.0 * scale[1], -7.0 *
              scale[0], -22.0 * scale[1], 0.0 * scale[0], -26.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 10.0 * scale[0],
              3.0 * scale[1], 10.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], 6.0 * scale[0],
              21.0 * scale[1], 20.0 * scale[0], 21.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0], -
              7.0 * scale[1], 20.0 * scale[0], -17.0 * scale[1])
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 11.0 * scale[0], -6.0 * scale[1])
    Curveto_r(6.0 * scale[0], 6.0 * scale[1], 8.0 * scale[0],
              16.0 * scale[1], 5.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 18.0 * scale[1], -54.0 * scale[0],
              13.0 * scale[1], -66.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(570.0 * scale[0], 880.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -3.0 * scale[1], 16.0 * scale[0], -
              14.0 * scale[1], 35.0 * scale[0], -23.0 * scale[1])
    Curveto_r(18.0 * scale[0], -9.0 * scale[1], 42.0 * scale[0], -
              28.0 * scale[1], 51.0 * scale[0], -42.0 * scale[1])
    Lineto_r(17.0 * scale[0], -26.0 * scale[1])
    Lineto_r(18.0 * scale[0], 31.0 * scale[1])
    Curveto_r(10.0 * scale[0], 16.0 * scale[1], 23.0 * scale[0],
              30.0 * scale[1], 29.0 * scale[0], 30.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              7.0 * scale[1], 10.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -8.0 * scale[0],
              16.0 * scale[1], -46.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-26.0 * scale[0], -2.0 * scale[1], -41.0 *
              scale[0], -2.0 * scale[1], -35.0 * scale[0], 2.0 * scale[1])
    Curveto_r(7.0 * scale[0], 4.0 * scale[1], -9.0 * scale[0],
              8.0 * scale[1], -34.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 0.0 * scale[1], -45.0 *
              scale[0], -3.0 * scale[1], -45.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(760.0 * scale[0], 773.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -18.0 * scale[1], 18.0 * scale[0], -
              35.0 * scale[1], 24.0 * scale[0], -24.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], 4.0 * scale[0],
              16.0 * scale[1], 1.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 12.0 * scale[1], -25.0 * scale[0],
              13.0 * scale[1], -25.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(770.0 * scale[0], 709.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 7.0 * scale[0], -
              22.0 * scale[1], 15.0 * scale[0], -29.0 * scale[1])
    Curveto_r(19.0 * scale[0], -16.0 * scale[1], 19.0 * scale[0],
              0.0 * scale[1], 0.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 16.0 * scale[1], -14.0 * scale[0],
              16.0 * scale[1], -15.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(370.0 * scale[0], 160.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 11.0 * scale[0], -
              26.0 * scale[1], 23.0 * scale[0], -14.0 * scale[1])
    Curveto_r(8.0 * scale[0], 8.0 * scale[1], -3.0 * scale[0],
              34.0 * scale[1], -14.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              9.0 * scale[1], -9.0 * scale[0], -20.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#6a471d')
    te.end_fill()
    Moveto(118.0 * scale[0], 1423.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-27.0 * scale[0], -2.0 * scale[1], -48.0 *
              scale[0], -8.0 * scale[1], -48.0 * scale[0], -13.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], -9.0 * scale[0], -
              6.0 * scale[1], -21.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 4.0 * scale[1], -25.0 * scale[0],
              0.0 * scale[1], -30.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -21.0 * scale[1], -11.0 *
              scale[0], -57.0 * scale[1], 4.0 * scale[0], -62.0 * scale[1])
    Curveto_r(10.0 * scale[0], -4.0 * scale[1], 10.0 *
              scale[0], -6.0 * scale[1], 0.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -1.0 * scale[1], -18.0 * scale[0], -
              111.0 * scale[1], 2.0 * scale[0], -111.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0], -
              6.0 * scale[1], 8.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -15.0 * scale[1], -5.0 *
              scale[0], -16.0 * scale[1], 9.0 * scale[0], -3.0 * scale[1])
    Curveto_r(15.0 * scale[0], 14.0 * scale[1], 15.0 * scale[0],
              16.0 * scale[1], -3.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 12.0 * scale[1], -17.0 * scale[0],
              18.0 * scale[1], -7.0 * scale[0], 28.0 * scale[1])
    Curveto_r(16.0 * scale[0], 16.0 * scale[1], 17.0 * scale[0],
              92.0 * scale[1], 1.0 * scale[0], 92.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0],
              9.0 * scale[1], -6.0 * scale[0], 20.0 * scale[1])
    Curveto_r(3.0 * scale[0], 12.0 * scale[1], 13.0 * scale[0],
              20.0 * scale[1], 22.0 * scale[0], 19.0 * scale[1])
    Curveto_r(9.0 * scale[0], -1.0 * scale[1], 30.0 * scale[0],
              0.0 * scale[1], 46.0 * scale[0], 1.0 * scale[1])
    Curveto_r(29.0 * scale[0], 2.0 * scale[1], 30.0 * scale[0],
              2.0 * scale[1], 5.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 6.0 * scale[1], 7.0 * scale[0],
              10.0 * scale[1], 75.0 * scale[0], 15.0 * scale[1])
    Curveto_r(55.0 * scale[0], 4.0 * scale[1], 109.0 * scale[0],
              8.0 * scale[1], 120.0 * scale[0], 10.0 * scale[1])
    Curveto_r(28.0 * scale[0], 4.0 * scale[1], -119.0 * scale[0],
              3.0 * scale[1], -177.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(337.0 * scale[0], 1423.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -3.0 * scale[1], 2.0 * scale[0], -
              13.0 * scale[1], 14.0 * scale[0], -21.0 * scale[1])
    Curveto_r(26.0 * scale[0], -18.0 * scale[1], 32.0 *
              scale[0], -12.0 * scale[1], 9.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 10.0 * scale[1], -20.0 * scale[0],
              15.0 * scale[1], -23.0 * scale[0], 11.0 * scale[1])
    te.end_fill()
    Moveto(546.0 * scale[0], 1413.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(10.0 * scale[0], -7.0 * scale[1], 23.0 * scale[0], -
              13.0 * scale[1], 28.0 * scale[0], -12.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 5.0 * scale[0],
              3.0 * scale[1], -2.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 2.0 * scale[1], -10.0 * scale[0],
              9.0 * scale[1], -7.0 * scale[0], 13.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], -4.0 * scale[0],
              8.0 * scale[1], -15.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -1.0 * scale[1], -20.0 *
              scale[0], -2.0 * scale[1], -4.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(653.0 * scale[0], 1423.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(728.0 * scale[0], 1419.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -6.0 * scale[1], -17.0 *
              scale[0], -7.0 * scale[1], 12.0 * scale[0], -8.0 * scale[1])
    Curveto_r(98.0 * scale[0], -4.0 * scale[1], 186.0 * scale[0], -
              14.0 * scale[1], 194.0 * scale[0], -22.0 * scale[1])
    Curveto_r(11.0 * scale[0], -10.0 * scale[1], 3.0 * scale[0], -
              11.0 * scale[1], -54.0 * scale[0], -11.0 * scale[1])
    Lineto_r(-35.0 * scale[0], 1.0 * scale[1])
    Lineto_r(30.0 * scale[0], -9.0 * scale[1])
    Curveto_r(17.0 * scale[0], -4.0 * scale[1], 26.0 *
              scale[0], -8.0 * scale[1], 20.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -1.0 * scale[1], 1.0 * scale[0], -
              9.0 * scale[1], 15.0 * scale[0], -19.0 * scale[1])
    Curveto_r(26.0 * scale[0], -18.0 * scale[1], 32.0 * scale[0], -
              42.0 * scale[1], 15.0 * scale[0], -54.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -5.0 * scale[1], -5.0 *
              scale[0], -8.0 * scale[1], 4.0 * scale[0], -8.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0], -
              3.0 * scale[1], 2.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -10.0 * scale[1], -9.0 * scale[0], -
              16.0 * scale[1], -1.0 * scale[0], -21.0 * scale[1])
    Curveto_r(18.0 * scale[0], -11.0 * scale[1], 11.0 * scale[0], -
              38.0 * scale[1], -17.0 * scale[0], -67.0 * scale[1])
    Curveto_r(-22.0 * scale[0], -23.0 * scale[1], -24.0 *
              scale[0], -28.0 * scale[1], -10.0 * scale[0], -28.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 21.0 * scale[0],
              10.0 * scale[1], 26.0 * scale[0], 22.0 * scale[1])
    Curveto_r(6.0 * scale[0], 16.0 * scale[1], 10.0 * scale[0],
              18.0 * scale[1], 16.0 * scale[0], 8.0 * scale[1])
    Curveto_r(5.0 * scale[0], -9.0 * scale[1], 4.0 * scale[0], -
              15.0 * scale[1], -4.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -3.0 * scale[1], -9.0 *
              scale[0], -7.0 * scale[1], 1.0 * scale[0], -20.0 * scale[1])
    Curveto_r(10.0 * scale[0], -12.0 * scale[1], 10.0 *
              scale[0], -16.0 * scale[1], 0.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -3.0 * scale[1], -9.0 * scale[0], -
              10.0 * scale[1], -6.0 * scale[0], -15.0 * scale[1])
    Curveto_r(5.0 * scale[0], -8.0 * scale[1], -4.0 * scale[0], -
              9.0 * scale[1], -27.0 * scale[0], -5.0 * scale[1])
    Lineto_r(-34.0 * scale[0], 7.0 * scale[1])
    Lineto_r(25.0 * scale[0], -16.0 * scale[1])
    Curveto_r(24.0 * scale[0], -14.0 * scale[1], 21.0 * scale[0], -
              15.0 * scale[1], -44.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-41.0 * scale[0], 3.0 * scale[1], -63.0 * scale[0],
              1.0 * scale[1], -55.0 * scale[0], -4.0 * scale[1])
    Curveto_r(8.0 * scale[0], -5.0 * scale[1], -66.0 * scale[0], -
              8.0 * scale[1], -179.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-107.0 * scale[0], 0.0 * scale[1], -196.0 *
              scale[0], -1.0 * scale[1], -198.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -9.0 * scale[1], 426.0 *
              scale[0], -17.0 * scale[1], 451.0 * scale[0], -7.0 * scale[1])
    Curveto_r(14.0 * scale[0], 5.0 * scale[1], 37.0 * scale[0],
              10.0 * scale[1], 50.0 * scale[0], 10.0 * scale[1])
    Curveto_r(20.0 * scale[0], 0.0 * scale[1], 25.0 * scale[0],
              6.0 * scale[1], 30.0 * scale[0], 43.0 * scale[1])
    Curveto_r(3.0 * scale[0], 23.0 * scale[1], 5.0 * scale[0],
              85.0 * scale[1], 3.0 * scale[0], 137.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 81.0 * scale[1], -5.0 * scale[0],
              95.0 * scale[1], -20.0 * scale[0], 95.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0],
              4.0 * scale[1], -25.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 5.0 * scale[1], 3.0 * scale[0],
              7.0 * scale[1], 18.0 * scale[0], 4.0 * scale[1])
    Curveto_r(22.0 * scale[0], -4.0 * scale[1], 25.0 *
              scale[0], -2.0 * scale[1], 21.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 12.0 * scale[1], -11.0 * scale[0],
              26.0 * scale[1], -21.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 10.0 * scale[1], -176.0 * scale[0],
              20.0 * scale[1], -203.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(974.0 * scale[0], 1230.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -80.0 * scale[1], 2.0 * scale[0], -
              112.0 * scale[1], 3.0 * scale[0], -72.0 * scale[1])
    Curveto_r(2.0 * scale[0], 39.0 * scale[1], 2.0 * scale[0],
              105.0 * scale[1], 0.0 * scale[0], 145.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 39.0 * scale[1], -3.0 * scale[0],
              7.0 * scale[1], -3.0 * scale[0], -73.0 * scale[1])
    te.end_fill()
    Moveto(168.0 * scale[0], 1320.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -16.0 * scale[1], 7.0 * scale[0], -
              28.0 * scale[1], 11.0 * scale[0], -25.0 * scale[1])
    Curveto_r(11.0 * scale[0], 6.0 * scale[1], 6.0 * scale[0],
              48.0 * scale[1], -6.0 * scale[0], 52.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 2.0 * scale[1], -8.0 * scale[0], -
              9.0 * scale[1], -5.0 * scale[0], -27.0 * scale[1])
    te.end_fill()
    Moveto(420.0 * scale[0], 1320.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -5.0 * scale[1], -12.0 * scale[0], -
              11.0 * scale[1], -10.0 * scale[0], -14.0 * scale[1])
    Curveto_r(3.0 * scale[0], -2.0 * scale[1], 14.0 * scale[0],
              2.0 * scale[1], 24.0 * scale[0], 10.0 * scale[1])
    Curveto_r(22.0 * scale[0], 15.0 * scale[1], 10.0 * scale[0],
              19.0 * scale[1], -14.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(792.0 * scale[0], 1305.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(775.0 * scale[0], 1250.0 * scale[1], x, y)
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
    Moveto(248.0 * scale[0], 1243.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 30.0 *
              scale[0], -2.0 * scale[1], 40.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 0.0 * scale[1], -30.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(180.0 * scale[0], 1230.0 * scale[1], x, y)
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
    Moveto(805.0 * scale[0], 1220.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 10.0 * scale[0], -
              10.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              5.0 * scale[1], 9.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -7.0 * scale[0],
              10.0 * scale[1], -16.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              4.0 * scale[1], -9.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(13.0 * scale[0], 1133.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(2.0 * scale[0], -58.0 * scale[1])
    Lineto_r(35.0 * scale[0], -4.0 * scale[1])
    Lineto_r(35.0 * scale[0], -4.0 * scale[1])
    Lineto_r(-30.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-43.0 * scale[0], -11.0 * scale[1], 107.0 *
              scale[0], -11.0 * scale[1], 165.0 * scale[0], -1.0 * scale[1])
    Lineto_r(45.0 * scale[0], 8.0 * scale[1])
    Lineto_r(-51.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-28.0 * scale[0], 0.0 * scale[1], -77.0 * scale[0],
              10.0 * scale[1], -110.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-32.0 * scale[0], 12.0 * scale[1], -64.0 * scale[0],
              21.0 * scale[1], -71.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0],
              3.0 * scale[1], -8.0 * scale[0], 7.0 * scale[1])
    Curveto_r(5.0 * scale[0], 8.0 * scale[1], 31.0 * scale[0],
              5.0 * scale[1], 90.0 * scale[0], -9.0 * scale[1])
    Curveto_r(22.0 * scale[0], -5.0 * scale[1], 41.0 *
              scale[0], -8.0 * scale[1], 43.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 2.0 * scale[1], -7.0 * scale[0],
              7.0 * scale[1], -22.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 7.0 * scale[1], -34.0 * scale[0],
              20.0 * scale[1], -8.0 * scale[0], 27.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 4.0 * scale[0],
              4.0 * scale[1], -13.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -1.0 * scale[1], -33.0 *
              scale[0], -5.0 * scale[1], -36.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -20.0 * scale[0],
              6.0 * scale[1], -37.0 * scale[0], 23.0 * scale[1])
    Lineto_r(-32.0 * scale[0], 31.0 * scale[1])
    Lineto_r(3.0 * scale[0], -58.0 * scale[1])
    te.end_fill()
    Moveto_r(125.0 * scale[0], -70.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -2.0 * scale[1], -26.0 *
              scale[0], -2.0 * scale[1], -35.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              5.0 * scale[1], 17.0 * scale[0], 5.0 * scale[1])
    Curveto_r(19.0 * scale[0], 0.0 * scale[1], 27.0 * scale[0], -
              2.0 * scale[1], 18.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(273.0 * scale[0], 1173.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(146.0 * scale[0], 1155.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -8.0 * scale[1], 13.0 * scale[0], -
              15.0 * scale[1], 21.0 * scale[0], -15.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              2.0 * scale[1], -1.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 8.0 * scale[1], -17.0 * scale[0],
              15.0 * scale[1], -20.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -3.0 * scale[0], -
              7.0 * scale[1], 0.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(813.0 * scale[0], 1144.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(23.0 * scale[0], -17.0 * scale[1], 46.0 * scale[0], -
              22.0 * scale[1], 56.0 * scale[0], -11.0 * scale[1])
    Curveto_r(8.0 * scale[0], 10.0 * scale[1], 3.0 * scale[0],
              13.0 * scale[1], -24.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -33.0 *
              scale[0], -1.0 * scale[1], -32.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(895.0 * scale[0], 1130.0 * scale[1], x, y)
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
    Moveto(283.0 * scale[0], 1063.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 25.0 *
              scale[0], -2.0 * scale[1], 35.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -27.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(2.0 * scale[0], 1020.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], 2.0 * scale[0], -
              27.0 * scale[1], 5.0 * scale[0], -17.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              25.0 * scale[1], 0.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(25.0 * scale[0], 990.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -16.0 * scale[1], -15.0 * scale[0], -
              39.0 * scale[1], -14.0 * scale[0], -52.0 * scale[1])
    Curveto_r(1.0 * scale[0], -19.0 * scale[1], 2.0 *
              scale[0], -18.0 * scale[1], 8.0 * scale[0], 7.0 * scale[1])
    Curveto_r(4.0 * scale[0], 17.0 * scale[1], 13.0 * scale[0],
              40.0 * scale[1], 20.0 * scale[0], 53.0 * scale[1])
    Curveto_r(6.0 * scale[0], 12.0 * scale[1], 9.0 * scale[0],
              22.0 * scale[1], 7.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              13.0 * scale[1], -21.0 * scale[0], -30.0 * scale[1])
    te.end_fill()
    Moveto(70.0 * scale[0], 1013.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 10.0 * scale[0], -
              18.0 * scale[1], 23.0 * scale[0], -29.0 * scale[1])
    Lineto_r(22.0 * scale[0], -19.0 * scale[1])
    Lineto_r(-20.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 14.0 * scale[1], -21.0 * scale[0],
              27.0 * scale[1], -22.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 2.0 * scale[1], -3.0 * scale[0],
              0.0 * scale[1], -3.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(952.0 * scale[0], 950.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(111.0 * scale[0], 944.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(415.0 * scale[0], 929.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -17.0 * scale[1], 1.0 *
              scale[0], -21.0 * scale[1], 15.0 * scale[0], -4.0 * scale[1])
    Curveto_r(8.0 * scale[0], 9.0 * scale[1], 8.0 * scale[0],
              15.0 * scale[1], 2.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0], -
              5.0 * scale[1], -17.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(58.0 * scale[0], 893.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(255.0 * scale[0], 886.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -7.0 * scale[1], -33.0 * scale[0], -
              18.0 * scale[1], -50.0 * scale[0], -24.0 * scale[1])
    Lineto_r(-30.0 * scale[0], -12.0 * scale[1])
    Lineto_r(35.0 * scale[0], 6.0 * scale[1])
    Curveto_r(19.0 * scale[0], 4.0 * scale[1], 37.0 * scale[0],
              10.0 * scale[1], 40.0 * scale[0], 14.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], 14.0 * scale[0],
              12.0 * scale[1], 25.0 * scale[0], 18.0 * scale[1])
    Curveto_r(11.0 * scale[0], 6.0 * scale[1], 15.0 * scale[0],
              12.0 * scale[1], 10.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -19.0 * scale[0], -
              6.0 * scale[1], -30.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(590.0 * scale[0], 896.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 30.0 * scale[0], -
              14.0 * scale[1], 35.0 * scale[0], -6.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], -3.0 * scale[0],
              10.0 * scale[1], -14.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -21.0 *
              scale[0], -2.0 * scale[1], -21.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(4.0 * scale[0], 762.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -67.0 * scale[1], 9.0 * scale[0], -
              329.0 * scale[1], 1.0 * scale[0], -343.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -8.0 * scale[1], -2.0 *
              scale[0], -8.0 * scale[1], 12.0 * scale[0], -1.0 * scale[1])
    Curveto_r(23.0 * scale[0], 12.0 * scale[1], 34.0 * scale[0],
              6.0 * scale[1], 51.0 * scale[0], -28.0 * scale[1])
    Lineto_r(12.0 * scale[0], -25.0 * scale[1])
    Lineto_r(-6.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 14.0 * scale[1], -12.0 * scale[0],
              30.0 * scale[1], -19.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 7.0 * scale[1], -11.0 * scale[0],
              20.0 * scale[1], -6.0 * scale[0], 46.0 * scale[1])
    Curveto_r(5.0 * scale[0], 20.0 * scale[1], 5.0 * scale[0],
              42.0 * scale[1], 0.0 * scale[0], 49.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 22.0 * scale[1], -10.0 * scale[0],
              73.0 * scale[1], 7.0 * scale[0], 97.0 * scale[1])
    Curveto_r(10.0 * scale[0], 14.0 * scale[1], 14.0 * scale[0],
              38.0 * scale[1], 12.0 * scale[0], 65.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 29.0 * scale[1], 1.0 * scale[0],
              41.0 * scale[1], 10.0 * scale[0], 40.0 * scale[1])
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 12.0 * scale[0],
              3.0 * scale[1], 12.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 7.0 * scale[0],
              16.0 * scale[1], 17.0 * scale[0], 18.0 * scale[1])
    Curveto_r(19.0 * scale[0], 4.0 * scale[1], 25.0 * scale[0],
              55.0 * scale[1], 6.0 * scale[0], 55.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              11.0 * scale[1], -13.0 * scale[0], -24.0 * scale[1])
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], -4.0 * scale[0], -
              21.0 * scale[1], -10.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -13.0 * scale[0], -
              1.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -9.0 * scale[1], -13.0 * scale[0], -
              14.0 * scale[1], -21.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 4.0 * scale[1], -14.0 * scale[0],
              0.0 * scale[1], -9.0 * scale[0], -20.0 * scale[1])
    Curveto_r(4.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              25.0 * scale[1], -3.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 0.0 * scale[1], -36.0 * scale[0],
              83.0 * scale[1], -22.0 * scale[0], 88.0 * scale[1])
    Curveto_r(13.0 * scale[0], 4.0 * scale[1], 4.0 * scale[0],
              22.0 * scale[1], -11.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              17.0 * scale[1], -4.0 * scale[0], -48.0 * scale[1])
    te.end_fill()
    Moveto_r(33.0 * scale[0], -124.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -6.0 *
              scale[0], -5.0 * scale[1], -6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 11.0 * scale[1], 2.0 * scale[0],
              17.0 * scale[1], 5.0 * scale[0], 13.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 4.0 * scale[0], -
              12.0 * scale[1], 1.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(492.0 * scale[0], 788.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -7.0 * scale[1], -8.0 * scale[0], -
              29.0 * scale[1], -7.0 * scale[0], -47.0 * scale[1])
    Curveto_r(3.0 * scale[0], -30.0 * scale[1], 1.0 * scale[0], -
              32.0 * scale[1], -8.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], -17.0 * scale[0],
              26.0 * scale[1], -25.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 13.0 * scale[1], -14.0 * scale[0],
              13.0 * scale[1], -9.0 * scale[0], 0.0 * scale[1])
    Curveto_r(4.0 * scale[0], -8.0 * scale[1], 10.0 * scale[0], -
              23.0 * scale[1], 13.0 * scale[0], -32.0 * scale[1])
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 15.0 * scale[0], -
              20.0 * scale[1], 25.0 * scale[0], -23.0 * scale[1])
    Curveto_r(10.0 * scale[0], -4.0 * scale[1], 19.0 * scale[0], -
              13.0 * scale[1], 19.0 * scale[0], -20.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              25.0 * scale[1], 10.0 * scale[0], -39.0 * scale[1])
    Curveto_r(7.0 * scale[0], -19.0 * scale[1], 14.0 * scale[0], -
              24.0 * scale[1], 27.0 * scale[0], -19.0 * scale[1])
    Curveto_r(9.0 * scale[0], 4.0 * scale[1], 12.0 * scale[0],
              8.0 * scale[1], 6.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0],
              11.0 * scale[1], -6.0 * scale[0], 19.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], -1.0 * scale[0],
              14.0 * scale[1], -10.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0],
              15.0 * scale[1], -22.0 * scale[0], 54.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 30.0 * scale[1], -4.0 * scale[0],
              59.0 * scale[1], 0.0 * scale[0], 65.0 * scale[1])
    Curveto_r(9.0 * scale[0], 15.0 * scale[1], 0.0 * scale[0],
              14.0 * scale[1], -13.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(428.0 * scale[0], 783.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(791.0 * scale[0], 764.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(636.0 * scale[0], 674.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-24.0 * scale[0], -24.0 * scale[1], -19.0 *
              scale[0], -30.0 * scale[1], 7.0 * scale[0], -8.0 * scale[1])
    Curveto_r(12.0 * scale[0], 10.0 * scale[1], 24.0 * scale[0],
              20.0 * scale[1], 26.0 * scale[0], 21.0 * scale[1])
    Curveto_r(2.0 * scale[0], 2.0 * scale[1], -1.0 * scale[0],
              3.0 * scale[1], -7.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -18.0 * scale[0], -
              7.0 * scale[1], -26.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(764.0 * scale[0], 673.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 2.0 * scale[0], -
              14.0 * scale[1], -3.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -3.0 * scale[1], -7.0 * scale[0], -
              13.0 * scale[1], -4.0 * scale[0], -21.0 * scale[1])
    Curveto_r(5.0 * scale[0], -14.0 * scale[1], 3.0 * scale[0], -
              15.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 12.0 * scale[1], -22.0 * scale[0],
              12.0 * scale[1], -7.0 * scale[0], -11.0 * scale[1])
    Curveto_r(10.0 * scale[0], -13.0 * scale[1], 14.0 * scale[0], -
              32.0 * scale[1], 11.0 * scale[0], -45.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -12.0 * scale[1], -1.0 *
              scale[0], -31.0 * scale[1], 5.0 * scale[0], -43.0 * scale[1])
    Curveto_r(9.0 * scale[0], -15.0 * scale[1], 7.0 * scale[0], -
              32.0 * scale[1], -7.0 * scale[0], -73.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -43.0 * scale[1], -23.0 *
              scale[0], -53.0 * scale[1], -49.0 * scale[0], -60.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -4.0 * scale[1], -38.0 * scale[0], -
              19.0 * scale[1], -47.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -20.0 * scale[1], -22.0 *
              scale[0], -24.0 * scale[1], -41.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 5.0 * scale[1], -25.0 * scale[0],
              3.0 * scale[1], -25.0 * scale[0], -23.0 * scale[1])
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], -5.0 * scale[0], -
              34.0 * scale[1], -11.0 * scale[0], -40.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -7.0 * scale[1], -8.0 * scale[0], -
              25.0 * scale[1], -2.0 * scale[0], -54.0 * scale[1])
    Curveto_r(8.0 * scale[0], -39.0 * scale[1], 12.0 * scale[0], -
              44.0 * scale[1], 34.0 * scale[0], -41.0 * scale[1])
    Curveto_r(13.0 * scale[0], 1.0 * scale[1], 30.0 * scale[0],
              10.0 * scale[1], 37.0 * scale[0], 19.0 * scale[1])
    Curveto_r(11.0 * scale[0], 16.0 * scale[1], 12.0 * scale[0],
              16.0 * scale[1], 12.0 * scale[0], 0.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 3.0 * scale[0], -
              17.0 * scale[1], 8.0 * scale[0], -17.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 62.0 * scale[0],
              48.0 * scale[1], 62.0 * scale[0], 58.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 6.0 * scale[0],
              12.0 * scale[1], 13.0 * scale[0], 15.0 * scale[1])
    Curveto_r(16.0 * scale[0], 6.0 * scale[1], 66.0 * scale[0],
              108.0 * scale[1], 65.0 * scale[0], 133.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], 3.0 * scale[0],
              36.0 * scale[1], 7.0 * scale[0], 57.0 * scale[1])
    Curveto_r(5.0 * scale[0], 25.0 * scale[1], 4.0 * scale[0],
              37.0 * scale[1], -4.0 * scale[0], 37.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              5.0 * scale[1], -11.0 * scale[0], -12.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -3.0 * scale[0], -
              8.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 4.0 * scale[1], 1.0 * scale[0],
              18.0 * scale[1], 11.0 * scale[0], 33.0 * scale[1])
    Curveto_r(11.0 * scale[0], 17.0 * scale[1], 13.0 * scale[0],
              29.0 * scale[1], 7.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -14.0 * scale[0],
              19.0 * scale[1], -18.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 21.0 * scale[1], -9.0 * scale[0],
              25.0 * scale[1], -16.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -9.0 * scale[1], -7.0 *
              scale[0], -3.0 * scale[1], -3.0 * scale[0], 17.0 * scale[1])
    Curveto_r(4.0 * scale[0], 16.0 * scale[1], 11.0 * scale[0],
              32.0 * scale[1], 16.0 * scale[0], 35.0 * scale[1])
    Curveto_r(5.0 * scale[0], 4.0 * scale[1], 2.0 * scale[0],
              15.0 * scale[1], -7.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 10.0 * scale[1], -13.0 * scale[0],
              14.0 * scale[1], -10.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto_r(18.0 * scale[0], -128.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -16.0 * scale[1], 1.0 * scale[0], -
              25.0 * scale[1], -7.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0],
              9.0 * scale[1], -7.0 * scale[0], 25.0 * scale[1])
    Curveto_r(2.0 * scale[0], 14.0 * scale[1], 6.0 * scale[0],
              25.0 * scale[1], 7.0 * scale[0], 25.0 * scale[1])
    Curveto_r(1.0 * scale[0], 0.0 * scale[1], 5.0 * scale[0], -
              11.0 * scale[1], 7.0 * scale[0], -25.0 * scale[1])
    te.end_fill()
    Moveto(690.0 * scale[0], 660.0 * scale[1], x, y)
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
    Moveto(560.0 * scale[0], 646.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 7.0 * scale[0], -
              7.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 12.0 *
              scale[0], -2.0 * scale[1], 9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], -25.0 * scale[0],
              14.0 * scale[1], -25.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(539.0 * scale[0], 603.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -21.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(526.0 * scale[0], 555.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(13.0 * scale[0], -54.0 * scale[1], 24.0 * scale[0], -
              73.0 * scale[1], 18.0 * scale[0], -30.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 22.0 * scale[1], -11.0 * scale[0],
              45.0 * scale[1], -16.0 * scale[0], 50.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 6.0 * scale[1], -7.0 * scale[0], -
              1.0 * scale[1], -2.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(706.0 * scale[0], 433.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(618.0 * scale[0], 413.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 32.0 *
              scale[0], -2.0 * scale[1], 45.0 * scale[0], 0.0 * scale[1])
    Curveto_r(12.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              4.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 0.0 * scale[1], -35.0 *
              scale[0], -2.0 * scale[1], -22.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(112.0 * scale[0], 260.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(770.0 * scale[0], 126.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-31.0 * scale[0], -37.0 * scale[1], -32.0 *
              scale[0], -39.0 * scale[1], -5.0 * scale[0], -16.0 * scale[1])
    Curveto_r(51.0 * scale[0], 43.0 * scale[1], 55.0 * scale[0],
              49.0 * scale[1], 48.0 * scale[0], 53.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 2.0 * scale[1], -24.0 * scale[0], -
              15.0 * scale[1], -43.0 * scale[0], -37.0 * scale[1])
    te.end_fill()
    Moveto(818.0 * scale[0], 122.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -11.0 * scale[1], 0.0 * scale[0], -
              19.0 * scale[1], 7.0 * scale[0], -19.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              8.0 * scale[1], 7.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 23.0 * scale[1], -8.0 * scale[0],
              23.0 * scale[1], -14.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(95.0 * scale[0], 109.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0], -
              12.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 17.0 * scale[1], 1.0 * scale[0],
              20.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(821.0 * scale[0], 68.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -29.0 * scale[1], -11.0 * scale[0], -
              34.0 * scale[1], -81.0 * scale[0], -41.0 * scale[1])
    Curveto_r(-27.0 * scale[0], -3.0 * scale[1], -23.0 *
              scale[0], -4.0 * scale[1], 15.0 * scale[0], -5.0 * scale[1])
    Curveto_r(54.0 * scale[0], -2.0 * scale[1], 95.0 * scale[0],
              17.0 * scale[1], 95.0 * scale[0], 44.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -4.0 * scale[0],
              13.0 * scale[1], -9.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -4.0 * scale[1], -12.0 * scale[0],
              0.0 * scale[1], -14.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 7.0 * scale[1], -6.0 * scale[0],
              1.0 * scale[1], -6.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(190.0 * scale[0], 70.0 * scale[1], x, y)
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
    Moveto(198.0 * scale[0], 13.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 30.0 *
              scale[0], -2.0 * scale[1], 40.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 0.0 * scale[1], -30.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(538.0 * scale[0], 13.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(23.0 * scale[0], -2.0 * scale[1], 61.0 *
              scale[0], -2.0 * scale[1], 85.0 * scale[0], 0.0 * scale[1])
    Curveto_r(23.0 * scale[0], 2.0 * scale[1], 4.0 * scale[0],
              4.0 * scale[1], -43.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-47.0 * scale[0], 0.0 * scale[1], -66.0 *
              scale[0], -2.0 * scale[1], -42.0 * scale[0], -4.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#443012')
    te.end_fill()
    Moveto(35.0 * scale[0], 1421.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -5.0 * scale[1], -22.0 *
              scale[0], -7.0 * scale[1], -25.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 2.0 * scale[1], -6.0 * scale[0], -
              40.0 * scale[1], -6.0 * scale[0], -93.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -53.0 * scale[1], 1.0 * scale[0], -
              75.0 * scale[1], 3.0 * scale[0], -47.0 * scale[1])
    Curveto_r(2.0 * scale[0], 27.0 * scale[1], 10.0 * scale[0],
              53.0 * scale[1], 16.0 * scale[0], 57.0 * scale[1])
    Curveto_r(9.0 * scale[0], 6.0 * scale[1], 9.0 * scale[0],
              8.0 * scale[1], 0.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0],
              28.0 * scale[1], -7.0 * scale[0], 54.0 * scale[1])
    Curveto_r(3.0 * scale[0], 9.0 * scale[1], 17.0 * scale[0],
              16.0 * scale[1], 30.0 * scale[0], 16.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 24.0 * scale[0],
              5.0 * scale[1], 24.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], -7.0 * scale[0],
              12.0 * scale[1], -35.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(98.0 * scale[0], 1423.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 32.0 *
              scale[0], -2.0 * scale[1], 45.0 * scale[0], 0.0 * scale[1])
    Curveto_r(12.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              4.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 0.0 * scale[1], -35.0 *
              scale[0], -2.0 * scale[1], -22.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(318.0 * scale[0], 1423.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(703.0 * scale[0], 1423.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 25.0 *
              scale[0], -2.0 * scale[1], 35.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -27.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(783.0 * scale[0], 1423.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(15.0 * scale[0], -2.0 * scale[1], 37.0 *
              scale[0], -2.0 * scale[1], 50.0 * scale[0], 0.0 * scale[1])
    Curveto_r(12.0 * scale[0], 2.0 * scale[1], 0.0 * scale[0],
              4.0 * scale[1], -28.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-27.0 * scale[0], 0.0 * scale[1], -38.0 *
              scale[0], -2.0 * scale[1], -22.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(920.0 * scale[0], 1409.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(32.0 * scale[0], -13.0 * scale[1], 30.0 *
              scale[0], -8.0 * scale[1], 37.0 * scale[0], -80.0 * scale[1])
    Curveto_r(3.0 * scale[0], -35.0 * scale[1], 8.0 * scale[0], -
              66.0 * scale[1], 11.0 * scale[0], -69.0 * scale[1])
    Curveto_r(10.0 * scale[0], -11.0 * scale[1], -8.0 * scale[0],
              133.0 * scale[1], -19.0 * scale[0], 146.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 8.0 * scale[1], -21.0 * scale[0],
              14.0 * scale[1], -33.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -1.0 * scale[1], 4.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(44.0 * scale[0], 1336.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -4.0 * scale[0], -
              23.0 * scale[1], -1.0 * scale[0], -33.0 * scale[1])
    Curveto_r(3.0 * scale[0], -12.0 * scale[1], 5.0 *
              scale[0], -9.0 * scale[1], 6.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], 7.0 * scale[0],
              29.0 * scale[1], 14.0 * scale[0], 31.0 * scale[1])
    Curveto_r(9.0 * scale[0], 4.0 * scale[1], 9.0 * scale[0],
              6.0 * scale[1], -1.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 1.0 * scale[1], -15.0 * scale[0], -
              5.0 * scale[1], -18.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(98.0 * scale[0], 1343.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 32.0 *
              scale[0], -2.0 * scale[1], 45.0 * scale[0], 0.0 * scale[1])
    Curveto_r(12.0 * scale[0], 2.0 * scale[1], 2.0 * scale[0],
              4.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 0.0 * scale[1], -35.0 *
              scale[0], -2.0 * scale[1], -22.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(843.0 * scale[0], 1343.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(910.0 * scale[0], 1276.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 7.0 * scale[0], -
              9.0 * scale[1], 15.0 * scale[0], -16.0 * scale[1])
    Curveto_r(13.0 * scale[0], -11.0 * scale[1], 14.0 *
              scale[0], -10.0 * scale[1], 9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 14.0 * scale[1], -24.0 * scale[0],
              23.0 * scale[1], -24.0 * scale[0], 12.0 * scale[1])
    te.end_fill()
    Moveto(962.0 * scale[0], 1225.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(928.0 * scale[0], 1217.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -19.0 * scale[1], -2.0 *
              scale[0], -25.0 * scale[1], 4.0 * scale[0], -19.0 * scale[1])
    Curveto_r(6.0 * scale[0], 6.0 * scale[1], 8.0 * scale[0],
              18.0 * scale[1], 6.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 14.0 * scale[1], -5.0 * scale[0],
              12.0 * scale[1], -10.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(57.0 * scale[0], 1219.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(5.0 * scale[0], 1210.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 3.0 * scale[0], -
              18.0 * scale[1], 13.0 * scale[0], -28.0 * scale[1])
    Curveto_r(19.0 * scale[0], -19.0 * scale[1], 19.0 *
              scale[0], -18.0 * scale[1], 18.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 28.0 * scale[1], -19.0 * scale[0],
              39.0 * scale[1], -31.0 * scale[0], 19.0 * scale[1])
    te.end_fill()
    Moveto(962.0 * scale[0], 1165.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(0.0 * scale[0], 1143.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -24.0 * scale[1], 3.0 * scale[0], -
              33.0 * scale[1], 9.0 * scale[0], -25.0 * scale[1])
    Curveto_r(7.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              62.0 * scale[1], -5.0 * scale[0], 62.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              17.0 * scale[1], -4.0 * scale[0], -37.0 * scale[1])
    te.end_fill()
    Moveto(55.0 * scale[0], 1141.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -11.0 * scale[1], 9.0 * scale[0], -
              23.0 * scale[1], 19.0 * scale[0], -14.0 * scale[1])
    Curveto_r(9.0 * scale[0], 9.0 * scale[1], 7.0 * scale[0],
              23.0 * scale[1], -3.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(838.0 * scale[0], 1143.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(468.0 * scale[0], 1133.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(954.0 * scale[0], 1100.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -24.0 * scale[1], -12.0 * scale[0], -
              30.0 * scale[1], -33.0 * scale[0], -31.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -35.0 *
              scale[0], -4.0 * scale[1], -46.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -6.0 * scale[1], -7.0 *
              scale[0], -9.0 * scale[1], 31.0 * scale[0], -9.0 * scale[1])
    Curveto_r(35.0 * scale[0], -1.0 * scale[1], 51.0 * scale[0],
              3.0 * scale[1], 51.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], 3.0 * scale[0],
              25.0 * scale[1], 7.0 * scale[0], 40.0 * scale[1])
    Curveto_r(3.0 * scale[0], 15.0 * scale[1], 4.0 * scale[0],
              27.0 * scale[1], 1.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              13.0 * scale[1], -11.0 * scale[0], -30.0 * scale[1])
    te.end_fill()
    Moveto(971.0 * scale[0], 1074.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(15.0 * scale[0], 1060.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-14.0 * scale[0], -7.0 * scale[1], -8.0 *
              scale[0], -8.0 * scale[1], 20.0 * scale[0], -3.0 * scale[1])
    Curveto_r(22.0 * scale[0], 3.0 * scale[1], 42.0 * scale[0],
              7.0 * scale[1], 44.0 * scale[0], 9.0 * scale[1])
    Curveto_r(9.0 * scale[0], 8.0 * scale[1], -45.0 * scale[0],
              2.0 * scale[1], -64.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(103.0 * scale[0], 1063.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 25.0 *
              scale[0], -2.0 * scale[1], 35.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -27.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(373.0 * scale[0], 1063.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 25.0 *
              scale[0], -2.0 * scale[1], 35.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -27.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(258.0 * scale[0], 876.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -8.0 * scale[1], -23.0 * scale[0], -
              16.0 * scale[1], -34.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -4.0 * scale[1], -17.0 *
              scale[0], -5.0 * scale[1], 2.0 * scale[0], -6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 29.0 * scale[0],
              8.0 * scale[1], 39.0 * scale[0], 19.0 * scale[1])
    Curveto_r(20.0 * scale[0], 23.0 * scale[1], 14.0 * scale[0],
              28.0 * scale[1], -7.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(650.0 * scale[0], 880.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(357.0 * scale[0], 863.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -12.0 * scale[1], -7.0 *
              scale[0], -40.0 * scale[1], 11.0 * scale[0], -54.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 10.0 * scale[1], -11.0 * scale[0],
              27.0 * scale[1], -8.0 * scale[0], 38.0 * scale[1])
    Curveto_r(5.0 * scale[0], 21.0 * scale[1], 4.0 * scale[0],
              24.0 * scale[1], -6.0 * scale[0], 13.0 * scale[1])
    te.end_fill()
    Moveto(407.0 * scale[0], 859.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(163.0 * scale[0], 843.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(185.0 * scale[0], 810.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -13.0 * scale[1], 5.0 *
              scale[0], -13.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(13.0 * scale[0], 8.0 * scale[1], 13.0 * scale[0],
              10.0 * scale[1], -2.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0], -
              4.0 * scale[1], -23.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(760.0 * scale[0], 786.0 * scale[1], x, y)
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
    Moveto(130.0 * scale[0], 772.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -10.0 * scale[0], -
              17.0 * scale[1], -22.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-22.0 * scale[0], -8.0 * scale[1], -22.0 *
              scale[0], -9.0 * scale[1], 4.0 * scale[0], -9.0 * scale[1])
    Curveto_r(31.0 * scale[0], -1.0 * scale[1], 46.0 * scale[0],
              15.0 * scale[1], 29.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 8.0 * scale[1], -11.0 * scale[0],
              8.0 * scale[1], -11.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(3.0 * scale[0], 585.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -93.0 * scale[1], 3.0 * scale[0], -
              145.0 * scale[1], 6.0 * scale[0], -115.0 * scale[1])
    Curveto_r(3.0 * scale[0], 30.0 * scale[1], 3.0 * scale[0],
              107.0 * scale[1], 0.0 * scale[0], 170.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 107.0 * scale[1], -5.0 * scale[0],
              103.0 * scale[1], -6.0 * scale[0], -55.0 * scale[1])
    te.end_fill()
    Moveto(451.0 * scale[0], 718.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(18.0 * scale[0], -65.0 * scale[1], 51.0 * scale[0], -
              119.0 * scale[1], 64.0 * scale[0], -106.0 * scale[1])
    Curveto_r(6.0 * scale[0], 6.0 * scale[1], -19.0 * scale[0],
              88.0 * scale[1], -27.0 * scale[0], 88.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0],
              6.0 * scale[1], -4.0 * scale[0], 13.0 * scale[1])
    Curveto_r(1.0 * scale[0], 6.0 * scale[1], 1.0 * scale[0],
              9.0 * scale[1], -1.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -13.0 * scale[1], -23.0 *
              scale[0], -9.0 * scale[1], -23.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -4.0 * scale[0],
              17.0 * scale[1], -9.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -6.0 * scale[0], -
              7.0 * scale[1], 0.0 * scale[0], -27.0 * scale[1])
    te.end_fill()
    Moveto(775.0 * scale[0], 739.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0], -
              12.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 17.0 * scale[1], 1.0 * scale[0],
              20.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(66.0 * scale[0], 723.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -3.0 * scale[0], -
              23.0 * scale[1], 0.0 * scale[0], -44.0 * scale[1])
    Curveto_r(4.0 * scale[0], -26.0 * scale[1], 1.0 * scale[0], -
              44.0 * scale[1], -10.0 * scale[0], -60.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -31.0 * scale[1], -22.0 *
              scale[0], -71.0 * scale[1], 0.0 * scale[0], -62.0 * scale[1])
    Curveto_r(10.0 * scale[0], 3.0 * scale[1], 14.0 * scale[0],
              13.0 * scale[1], 10.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 10.0 * scale[1], -1.0 * scale[0],
              28.0 * scale[1], 5.0 * scale[0], 38.0 * scale[1])
    Curveto_r(5.0 * scale[0], 11.0 * scale[1], 13.0 * scale[0],
              27.0 * scale[1], 18.0 * scale[0], 38.0 * scale[1])
    Curveto_r(7.0 * scale[0], 13.0 * scale[1], 5.0 * scale[0],
              23.0 * scale[1], -7.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 16.0 * scale[1], -16.0 * scale[0],
              17.0 * scale[1], 1.0 * scale[0], 10.0 * scale[1])
    Curveto_r(9.0 * scale[0], -3.0 * scale[1], 17.0 *
              scale[0], -2.0 * scale[1], 17.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], -26.0 * scale[0],
              23.0 * scale[1], -34.0 * scale[0], 15.0 * scale[1])
    te.end_fill()
    Moveto(766.0 * scale[0], 675.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -9.0 * scale[1], -2.0 * scale[0], -
              14.0 * scale[1], 3.0 * scale[0], -11.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 12.0 * scale[0], -
              1.0 * scale[1], 15.0 * scale[0], -10.0 * scale[1])
    Curveto_r(4.0 * scale[0], -11.0 * scale[1], 2.0 * scale[0], -
              15.0 * scale[1], -7.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 4.0 * scale[1], -13.0 *
              scale[0], -2.0 * scale[1], -9.0 * scale[0], -19.0 * scale[1])
    Curveto_r(2.0 * scale[0], -13.0 * scale[1], 9.0 * scale[0], -
              24.0 * scale[1], 14.0 * scale[0], -24.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0],
              6.0 * scale[1], 5.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 6.0 * scale[1], 3.0 * scale[0],
              17.0 * scale[1], 12.0 * scale[0], 24.0 * scale[1])
    Curveto_r(12.0 * scale[0], 10.0 * scale[1], 13.0 * scale[0],
              12.0 * scale[1], 2.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0],
              3.0 * scale[1], 0.0 * scale[0], 18.0 * scale[1])
    Curveto_r(7.0 * scale[0], 9.0 * scale[1], 9.0 * scale[0],
              14.0 * scale[1], 5.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -4.0 * scale[1], -15.0 *
              scale[0], -3.0 * scale[1], -21.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 8.0 * scale[1], -14.0 * scale[0],
              6.0 * scale[1], -19.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(596.0 * scale[0], 655.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -8.0 * scale[1], -15.0 * scale[0], -
              15.0 * scale[1], -10.0 * scale[0], -15.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0],
              7.0 * scale[1], 30.0 * scale[0], 15.0 * scale[1])
    Curveto_r(10.0 * scale[0], 8.0 * scale[1], 15.0 * scale[0],
              14.0 * scale[1], 9.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -19.0 * scale[0], -
              6.0 * scale[1], -29.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(540.0 * scale[0], 630.0 * scale[1], x, y)
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
    Moveto(730.0 * scale[0], 615.0 * scale[1], x, y)
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
    Moveto(516.0 * scale[0], 582.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -10.0 * scale[1], 13.0 * scale[0], -
              86.0 * scale[1], 20.0 * scale[0], -80.0 * scale[1])
    Curveto_r(2.0 * scale[0], 2.0 * scale[1], -1.0 * scale[0],
              19.0 * scale[1], -6.0 * scale[0], 38.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 18.0 * scale[1], -7.0 * scale[0],
              37.0 * scale[1], -4.0 * scale[0], 41.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], 3.0 * scale[0],
              9.0 * scale[1], 0.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              4.0 * scale[1], -10.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(780.0 * scale[0], 582.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              9.0 * scale[1], 15.0 * scale[0], -9.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              4.0 * scale[1], 9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -9.0 * scale[0],
              8.0 * scale[1], -15.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              4.0 * scale[1], -9.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(790.0 * scale[0], 550.0 * scale[1], x, y)
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
    Moveto(48.0 * scale[0], 524.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -10.0 * scale[1], 6.0 * scale[0], -
              32.0 * scale[1], 1.0 * scale[0], -53.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -27.0 * scale[1], -5.0 *
              scale[0], -38.0 * scale[1], 7.0 * scale[0], -44.0 * scale[1])
    Curveto_r(7.0 * scale[0], -4.0 * scale[1], 14.0 * scale[0], -
              16.0 * scale[1], 15.0 * scale[0], -25.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 2.0 * scale[0], -
              12.0 * scale[1], 6.0 * scale[0], -4.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 0.0 * scale[0],
              19.0 * scale[1], -7.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 8.0 * scale[1], -9.0 * scale[0],
              29.0 * scale[1], -6.0 * scale[0], 49.0 * scale[1])
    Curveto_r(6.0 * scale[0], 38.0 * scale[1], -1.0 * scale[0],
              66.0 * scale[1], -16.0 * scale[0], 66.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -5.0 * scale[0], -
              6.0 * scale[1], 0.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(740.0 * scale[0], 526.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -47.0 * scale[1], -24.0 * scale[0], -
              98.0 * scale[1], -49.0 * scale[0], -107.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -5.0 * scale[1], -34.0 * scale[0], -
              13.0 * scale[1], -43.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -6.0 * scale[1], -35.0 *
              scale[0], -6.0 * scale[1], -63.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-31.0 * scale[0], 6.0 * scale[1], -45.0 * scale[0],
              5.0 * scale[1], -45.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -19.0 * scale[1], -67.0 * scale[0], -
              83.0 * scale[1], -96.0 * scale[0], -93.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -5.0 * scale[1], -32.0 * scale[0], -
              18.0 * scale[1], -38.0 * scale[0], -29.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -10.0 * scale[1], -18.0 * scale[0], -
              30.0 * scale[1], -26.0 * scale[0], -44.0 * scale[1])
    Curveto_r(-28.0 * scale[0], -43.0 * scale[1], -32.0 * scale[0], -
              88.0 * scale[1], -10.0 * scale[0], -107.0 * scale[1])
    Curveto_r(13.0 * scale[0], -12.0 * scale[1], 18.0 * scale[0], -
              24.0 * scale[1], 14.0 * scale[0], -40.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -26.0 * scale[1], 20.0 *
              scale[0], -34.0 * scale[1], 30.0 * scale[0], -8.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 15.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0], -
              7.0 * scale[1], 5.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -10.0 * scale[1], 1.0 * scale[0], -
              15.0 * scale[1], 12.0 * scale[0], -16.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 28.0 * scale[0], -
              3.0 * scale[1], 42.0 * scale[0], -5.0 * scale[1])
    Curveto_r(45.0 * scale[0], -9.0 * scale[1], 155.0 *
              scale[0], -9.0 * scale[1], 167.0 * scale[0], 0.0 * scale[1])
    Curveto_r(7.0 * scale[0], 4.0 * scale[1], 20.0 * scale[0],
              6.0 * scale[1], 28.0 * scale[0], 2.0 * scale[1])
    Curveto_r(9.0 * scale[0], -3.0 * scale[1], 14.0 *
              scale[0], -2.0 * scale[1], 10.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], 10.0 * scale[0], 24.0 * scale[1])
    Curveto_r(8.0 * scale[0], 9.0 * scale[1], 15.0 * scale[0],
              18.0 * scale[1], 15.0 * scale[0], 22.0 * scale[1])
    Curveto_r(0.0 * scale[0], 3.0 * scale[1], 10.0 * scale[0],
              16.0 * scale[1], 23.0 * scale[0], 28.0 * scale[1])
    Curveto_r(24.0 * scale[0], 22.0 * scale[1], 40.0 * scale[0],
              52.0 * scale[1], 42.0 * scale[0], 74.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 9.0 * scale[0],
              21.0 * scale[1], 20.0 * scale[0], 33.0 * scale[1])
    Curveto_r(18.0 * scale[0], 20.0 * scale[1], 20.0 * scale[0],
              36.0 * scale[1], 19.0 * scale[0], 146.0 * scale[1])
    Curveto_r(0.0 * scale[0], 68.0 * scale[1], -3.0 * scale[0],
              127.0 * scale[1], -7.0 * scale[0], 131.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 4.0 * scale[1], -13.0 * scale[0],
              1.0 * scale[1], -20.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -9.0 * scale[1], -9.0 * scale[0], -
              14.0 * scale[1], 1.0 * scale[0], -20.0 * scale[1])
    Curveto_r(10.0 * scale[0], -6.0 * scale[1], 11.0 * scale[0], -
              19.0 * scale[1], 6.0 * scale[0], -47.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -21.0 * scale[1], -7.0 * scale[0], -
              45.0 * scale[1], -6.0 * scale[0], -51.0 * scale[1])
    Curveto_r(4.0 * scale[0], -18.0 * scale[1], -50.0 * scale[0], -
              124.0 * scale[1], -65.0 * scale[0], -130.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -3.0 * scale[1], -13.0 * scale[0], -
              9.0 * scale[1], -13.0 * scale[0], -15.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], -51.0 * scale[0], -
              57.0 * scale[1], -62.0 * scale[0], -58.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0],
              8.0 * scale[1], -8.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 16.0 * scale[1], -1.0 * scale[0],
              16.0 * scale[1], -12.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -9.0 * scale[1], -24.0 * scale[0], -
              18.0 * scale[1], -37.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-22.0 * scale[0], -3.0 * scale[1], -26.0 * scale[0],
              2.0 * scale[1], -34.0 * scale[0], 41.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 29.0 * scale[1], -5.0 * scale[0],
              47.0 * scale[1], 2.0 * scale[0], 54.0 * scale[1])
    Curveto_r(6.0 * scale[0], 6.0 * scale[1], 11.0 * scale[0],
              24.0 * scale[1], 11.0 * scale[0], 40.0 * scale[1])
    Curveto_r(0.0 * scale[0], 26.0 * scale[1], 3.0 * scale[0],
              28.0 * scale[1], 25.0 * scale[0], 23.0 * scale[1])
    Curveto_r(19.0 * scale[0], -5.0 * scale[1], 28.0 *
              scale[0], -1.0 * scale[1], 41.0 * scale[0], 19.0 * scale[1])
    Curveto_r(9.0 * scale[0], 14.0 * scale[1], 30.0 * scale[0],
              29.0 * scale[1], 47.0 * scale[0], 33.0 * scale[1])
    Curveto_r(26.0 * scale[0], 7.0 * scale[1], 34.0 * scale[0],
              17.0 * scale[1], 49.0 * scale[0], 61.0 * scale[1])
    Curveto_r(13.0 * scale[0], 37.0 * scale[1], 15.0 * scale[0],
              57.0 * scale[1], 8.0 * scale[0], 69.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 16.0 * scale[1], -9.0 * scale[0],
              15.0 * scale[1], -10.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto_r(-347.0 * scale[0], -360.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -15.0 * scale[1], -1.0 * scale[0], -
              26.0 * scale[1], -15.0 * scale[0], -26.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0],
              9.0 * scale[1], -8.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 23.0 * scale[1], 15.0 * scale[0],
              27.0 * scale[1], 23.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(541.0 * scale[0], 474.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(578.0 * scale[0], 413.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(81.0 * scale[0], 364.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(106.0 * scale[0], 297.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0], -
              15.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 0.0 * scale[0],
              11.0 * scale[1], -7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              8.0 * scale[1], -5.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(771.0 * scale[0], 137.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-29.0 * scale[0], -35.0 * scale[1], -30.0 *
              scale[0], -38.0 * scale[1], -7.0 * scale[0], -17.0 * scale[1])
    Curveto_r(24.0 * scale[0], 22.0 * scale[1], 52.0 * scale[0],
              60.0 * scale[1], 44.0 * scale[0], 60.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -18.0 * scale[0], -
              19.0 * scale[1], -37.0 * scale[0], -43.0 * scale[1])
    te.end_fill()
    Moveto(101.0 * scale[0], 134.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(159.0 * scale[0], 144.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              26.0 * scale[1], -1.0 * scale[0], -46.0 * scale[1])
    Curveto_r(1.0 * scale[0], -31.0 * scale[1], -2.0 * scale[0], -
              36.0 * scale[1], -16.0 * scale[0], -32.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 5.0 * scale[1], -14.0 * scale[0],
              4.0 * scale[1], 1.0 * scale[0], -6.0 * scale[1])
    Curveto_r(24.0 * scale[0], -16.0 * scale[1], 78.0 * scale[0], -
              31.0 * scale[1], 88.0 * scale[0], -25.0 * scale[1])
    Curveto_r(10.0 * scale[0], 7.0 * scale[1], -25.0 * scale[0],
              76.0 * scale[1], -50.0 * scale[0], 99.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 11.0 * scale[1], -22.0 * scale[0],
              15.0 * scale[1], -22.0 * scale[0], 10.0 * scale[1])
    te.end_fill()
    Moveto_r(51.0 * scale[0], -74.0 * scale[1], 0, 0)
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
    Moveto(812.0 * scale[0], 135.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -11.0 * scale[1], 5.0 * scale[0], -
              31.0 * scale[1], 13.0 * scale[0], -45.0 * scale[1])
    Curveto_r(9.0 * scale[0], -16.0 * scale[1], 14.0 * scale[0], -
              19.0 * scale[1], 15.0 * scale[0], -9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -4.0 * scale[0],
              19.0 * scale[1], -9.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 5.0 * scale[1], -11.0 * scale[0],
              18.0 * scale[1], -14.0 * scale[0], 29.0 * scale[1])
    Lineto_r(-5.0 * scale[0], 20.0 * scale[1])
    Lineto_r(0.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(719.0 * scale[0], 73.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 17.0 * scale[0],
              15.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], -21.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(827.0 * scale[0], 36.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-17.0 * scale[0], -13.0 * scale[1], -16.0 *
              scale[0], -14.0 * scale[1], 6.0 * scale[0], -12.0 * scale[1])
    Curveto_r(15.0 * scale[0], 0.0 * scale[1], 23.0 * scale[0],
              6.0 * scale[1], 20.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 14.0 * scale[1], -4.0 * scale[0],
              15.0 * scale[1], -26.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(133.0 * scale[0], 13.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 25.0 *
              scale[0], -2.0 * scale[1], 35.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -27.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(313.0 * scale[0], 13.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(37.0 * scale[0], -2.0 * scale[1], 96.0 *
              scale[0], -2.0 * scale[1], 130.0 * scale[0], 0.0 * scale[1])
    Curveto_r(34.0 * scale[0], 2.0 * scale[1], 4.0 * scale[0],
              3.0 * scale[1], -68.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-71.0 * scale[0], 0.0 * scale[1], -99.0 *
              scale[0], -1.0 * scale[1], -62.0 * scale[0], -3.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#93652f')
    te.end_fill()
    Moveto(357.0 * scale[0], 1414.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -13.0 * scale[1], 3.0 * scale[0], -
              15.0 * scale[1], -7.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -11.0 * scale[0],
              4.0 * scale[1], -6.0 * scale[0], -3.0 * scale[1])
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 13.0 * scale[0], -
              9.0 * scale[1], 21.0 * scale[0], -6.0 * scale[1])
    Curveto_r(8.0 * scale[0], 4.0 * scale[1], 12.0 * scale[0],
              10.0 * scale[1], 9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], 5.0 * scale[0],
              9.0 * scale[1], 18.0 * scale[0], 9.0 * scale[1])
    Curveto_r(18.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0], -
              2.0 * scale[1], 8.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              4.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], 33.0 * scale[0],
              9.0 * scale[1], 65.0 * scale[0], 7.0 * scale[1])
    Curveto_r(32.0 * scale[0], -2.0 * scale[1], 57.0 * scale[0],
              0.0 * scale[1], 55.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -45.0 * scale[0],
              7.0 * scale[1], -95.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-80.0 * scale[0], 1.0 * scale[1], -89.0 * scale[0],
              0.0 * scale[1], -83.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(560.0 * scale[0], 1415.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -8.0 * scale[1], -9.0 * scale[0], -
              15.0 * scale[1], -4.0 * scale[0], -15.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 2.0 * scale[0], -
              5.0 * scale[1], -6.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -7.0 * scale[1], -11.0 *
              scale[0], -9.0 * scale[1], -2.0 * scale[0], -7.0 * scale[1])
    Curveto_r(8.0 * scale[0], 2.0 * scale[1], 13.0 * scale[0],
              7.0 * scale[1], 12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 5.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], 11.0 * scale[0], 17.0 * scale[1])
    Curveto_r(8.0 * scale[0], 4.0 * scale[1], 11.0 * scale[0],
              11.0 * scale[1], 8.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 3.0 * scale[1], -12.0 * scale[0], -
              1.0 * scale[1], -19.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(590.0 * scale[0], 1365.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -66.0 * scale[1], -11.0 * scale[0], -
              88.0 * scale[1], -29.0 * scale[0], -58.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], -11.0 * scale[0],
              13.0 * scale[1], -11.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 5.0 * scale[0], -
              15.0 * scale[1], 11.0 * scale[0], -19.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 17.0 * scale[0], -
              20.0 * scale[1], 24.0 * scale[0], -36.0 * scale[1])
    Curveto_r(11.0 * scale[0], -28.0 * scale[1], 13.0 *
              scale[0], -28.0 * scale[1], 18.0 * scale[0], -9.0 * scale[1])
    Curveto_r(3.0 * scale[0], 12.0 * scale[1], 1.0 * scale[0],
              21.0 * scale[1], -3.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -2.0 * scale[0],
              109.0 * scale[1], 6.0 * scale[0], 119.0 * scale[1])
    Curveto_r(2.0 * scale[0], 2.0 * scale[1], 11.0 * scale[0], -
              4.0 * scale[1], 20.0 * scale[0], -13.0 * scale[1])
    Curveto_r(9.0 * scale[0], -10.0 * scale[1], 23.0 * scale[0], -
              15.0 * scale[1], 30.0 * scale[0], -12.0 * scale[1])
    Curveto_r(7.0 * scale[0], 3.0 * scale[1], 16.0 * scale[0],
              1.0 * scale[1], 19.0 * scale[0], -4.0 * scale[1])
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 24.0 * scale[0], -
              10.0 * scale[1], 46.0 * scale[0], -10.0 * scale[1])
    Curveto_r(22.0 * scale[0], 0.0 * scale[1], 49.0 * scale[0], -
              5.0 * scale[1], 59.0 * scale[0], -10.0 * scale[1])
    Curveto_r(13.0 * scale[0], -7.0 * scale[1], 21.0 *
              scale[0], -7.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], 24.0 * scale[0],
              10.0 * scale[1], 45.0 * scale[0], 10.0 * scale[1])
    Curveto_r(46.0 * scale[0], 0.0 * scale[1], 62.0 * scale[0],
              17.0 * scale[1], 23.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 4.0 * scale[1], -23.0 *
              scale[0], 5.0 * scale[1], 7.0 * scale[0], 5.0 * scale[1])
    Curveto_r(58.0 * scale[0], 0.0 * scale[1], 65.0 * scale[0],
              1.0 * scale[1], 55.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 5.0 * scale[1], -57.0 * scale[0],
              12.0 * scale[1], -115.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-58.0 * scale[0], 3.0 * scale[1], -98.0 * scale[0],
              3.0 * scale[1], -90.0 * scale[0], 0.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 24.0 * scale[0], -
              9.0 * scale[1], 35.0 * scale[0], -14.0 * scale[1])
    Curveto_r(11.0 * scale[0], -5.0 * scale[1], 34.0 * scale[0], -
              13.0 * scale[1], 50.0 * scale[0], -19.0 * scale[1])
    Curveto_r(25.0 * scale[0], -9.0 * scale[1], 16.0 * scale[0], -
              10.0 * scale[1], -50.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-54.0 * scale[0], 3.0 * scale[1], -95.0 * scale[0],
              10.0 * scale[1], -125.0 * scale[0], 25.0 * scale[1])
    Lineto_r(-45.0 * scale[0], 20.0 * scale[1])
    Lineto_r(59.0 * scale[0], 1.0 * scale[1])
    Curveto_r(73.0 * scale[0], 1.0 * scale[1], 70.0 * scale[0],
              7.0 * scale[1], -6.0 * scale[0], 14.0 * scale[1])
    Lineto_r(-58.0 * scale[0], 5.0 * scale[1])
    Lineto_r(0.0 * scale[0], -63.0 * scale[1])
    te.end_fill()
    Moveto(125.0 * scale[0], 1410.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-27.0 * scale[0], -4.0 * scale[1], -39.0 *
              scale[0], -8.0 * scale[1], -26.0 * scale[0], -8.0 * scale[1])
    Curveto_r(38.0 * scale[0], -3.0 * scale[1], 17.0 * scale[0], -
              13.0 * scale[1], -27.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-31.0 * scale[0], 0.0 * scale[1], -41.0 * scale[0], -
              5.0 * scale[1], -45.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -17.0 * scale[1], 1.0 * scale[0], -
              19.0 * scale[1], 69.0 * scale[0], -19.0 * scale[1])
    Curveto_r(54.0 * scale[0], 0.0 * scale[1], 73.0 * scale[0],
              3.0 * scale[1], 72.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 8.0 * scale[1], 17.0 * scale[0],
              13.0 * scale[1], 62.0 * scale[0], 15.0 * scale[1])
    Curveto_r(36.0 * scale[0], 2.0 * scale[1], 69.0 * scale[0],
              7.0 * scale[1], 74.0 * scale[0], 13.0 * scale[1])
    Curveto_r(6.0 * scale[0], 6.0 * scale[1], 5.0 * scale[0],
              9.0 * scale[1], -5.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 1.0 * scale[1], -3.0 * scale[0],
              5.0 * scale[1], 11.0 * scale[0], 9.0 * scale[1])
    Curveto_r(31.0 * scale[0], 10.0 * scale[1], -112.0 * scale[0],
              10.0 * scale[1], -185.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto_r(150.0 * scale[0], -10.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], -3.0 * scale[0], -
              10.0 * scale[1], -14.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -21.0 * scale[0],
              5.0 * scale[1], -21.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 6.0 * scale[0],
              10.0 * scale[1], 14.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 18.0 * scale[0], -
              4.0 * scale[1], 21.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(372.0 * scale[0], 1365.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              22.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 9.0 * scale[1], 2.0 * scale[0],
              23.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0], -
              1.0 * scale[1], -5.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(440.0 * scale[0], 1372.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 9.0 * scale[0], -
              13.0 * scale[1], 20.0 * scale[0], -19.0 * scale[1])
    Curveto_r(16.0 * scale[0], -11.0 * scale[1], 18.0 *
              scale[0], -10.0 * scale[1], 14.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 15.0 * scale[1], -34.0 * scale[0],
              30.0 * scale[1], -34.0 * scale[0], 18.0 * scale[1])
    te.end_fill()
    Moveto(184.0 * scale[0], 1331.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -14.0 * scale[1], -5.0 * scale[0], -
              37.0 * scale[1], -13.0 * scale[0], -51.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -15.0 * scale[1], -11.0 *
              scale[0], -21.0 * scale[1], -3.0 * scale[0], -17.0 * scale[1])
    Curveto_r(7.0 * scale[0], 5.0 * scale[1], 12.0 * scale[0],
              3.0 * scale[1], 12.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 6.0 * scale[0], -
              16.0 * scale[1], 13.0 * scale[0], -16.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0], -
              9.0 * scale[1], 14.0 * scale[0], -21.0 * scale[1])
    Curveto_r(1.0 * scale[0], -15.0 * scale[1], -1.0 * scale[0], -
              18.0 * scale[1], -11.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 8.0 * scale[1], -12.0 * scale[0],
              5.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(1.0 * scale[0], -15.0 * scale[1], -4.0 * scale[0], -
              22.0 * scale[1], -16.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 2.0 * scale[1], -22.0 * scale[0],
              0.0 * scale[1], -1.0 * scale[0], -21.0 * scale[1])
    Curveto_r(15.0 * scale[0], -16.0 * scale[1], 15.0 * scale[0], -
              17.0 * scale[1], -3.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-55.0 * scale[0], 6.0 * scale[1], -76.0 * scale[0], -
              12.0 * scale[1], -28.0 * scale[0], -24.0 * scale[1])
    Curveto_r(52.0 * scale[0], -13.0 * scale[1], 17.0 * scale[0], -
              14.0 * scale[1], -44.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-34.0 * scale[0], 7.0 * scale[1], -64.0 * scale[0],
              9.0 * scale[1], -67.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -3.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 8.0 * scale[0], -7.0 * scale[1])
    Curveto_r(7.0 * scale[0], -1.0 * scale[1], 39.0 * scale[0], -
              10.0 * scale[1], 71.0 * scale[0], -22.0 * scale[1])
    Curveto_r(37.0 * scale[0], -13.0 * scale[1], 82.0 * scale[0], -
              21.0 * scale[1], 120.0 * scale[0], -20.0 * scale[1])
    Lineto_r(61.0 * scale[0], 0.0 * scale[1])
    Lineto_r(-53.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-34.0 * scale[0], 15.0 * scale[1], -51.0 * scale[0],
              29.0 * scale[1], -46.0 * scale[0], 36.0 * scale[1])
    Curveto_r(4.0 * scale[0], 7.0 * scale[1], 9.0 * scale[0],
              7.0 * scale[1], 13.0 * scale[0], 2.0 * scale[1])
    Curveto_r(3.0 * scale[0], -6.0 * scale[1], 24.0 * scale[0], -
              13.0 * scale[1], 46.0 * scale[0], -17.0 * scale[1])
    Curveto_r(22.0 * scale[0], -4.0 * scale[1], 49.0 * scale[0], -
              13.0 * scale[1], 60.0 * scale[0], -19.0 * scale[1])
    Curveto_r(11.0 * scale[0], -6.0 * scale[1], 23.0 * scale[0], -
              11.0 * scale[1], 27.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              3.0 * scale[1], 14.0 * scale[0], -7.0 * scale[1])
    Curveto_r(4.0 * scale[0], -5.0 * scale[1], 55.0 * scale[0], -
              7.0 * scale[1], 113.0 * scale[0], -7.0 * scale[1])
    Curveto_r(58.0 * scale[0], 1.0 * scale[1], 98.0 * scale[0],
              3.0 * scale[1], 89.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 5.0 * scale[1], -25.0 * scale[0],
              23.0 * scale[1], -8.0 * scale[0], 23.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              5.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -5.0 * scale[0],
              8.0 * scale[1], -15.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -13.0 * scale[1], -81.0 *
              scale[0], -10.0 * scale[1], -120.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 7.0 * scale[1], -18.0 * scale[0],
              6.0 * scale[1], -5.0 * scale[0], -7.0 * scale[1])
    Curveto_r(9.0 * scale[0], -9.0 * scale[1], 22.0 * scale[0], -
              18.0 * scale[1], 30.0 * scale[0], -22.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], -1.0 * scale[0], -
              6.0 * scale[1], -21.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -1.0 * scale[1], -42.0 * scale[0],
              5.0 * scale[1], -49.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 8.0 * scale[1], -15.0 * scale[0],
              13.0 * scale[1], -19.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -2.0 * scale[1], -26.0 * scale[0],
              5.0 * scale[1], -51.0 * scale[0], 15.0 * scale[1])
    Lineto_r(-45.0 * scale[0], 18.0 * scale[1])
    Lineto_r(60.0 * scale[0], -6.0 * scale[1])
    Curveto_r(33.0 * scale[0], -3.0 * scale[1], 62.0 *
              scale[0], -6.0 * scale[1], 65.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 0.0 * scale[1], 6.0 * scale[0],
              2.0 * scale[1], 8.0 * scale[0], 7.0 * scale[1])
    Curveto_r(6.0 * scale[0], 18.0 * scale[1], 1.0 * scale[0],
              27.0 * scale[1], -15.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -16.0 *
              scale[0], -2.0 * scale[1], -3.0 * scale[0], -11.0 * scale[1])
    Curveto_r(11.0 * scale[0], -8.0 * scale[1], 0.0 * scale[0], -
              9.0 * scale[1], -40.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-69.0 * scale[0], 7.0 * scale[1], -142.0 * scale[0],
              28.0 * scale[1], -117.0 * scale[0], 34.0 * scale[1])
    Curveto_r(20.0 * scale[0], 4.0 * scale[1], 20.0 * scale[0],
              7.0 * scale[1], 7.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 14.0 * scale[1], -7.0 * scale[0],
              19.0 * scale[1], 3.0 * scale[0], 19.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0],
              6.0 * scale[1], 14.0 * scale[0], 13.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -10.0 * scale[0],
              13.0 * scale[1], -21.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -1.0 * scale[1], -22.0 * scale[0],
              6.0 * scale[1], -24.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 14.0 * scale[1], 4.0 * scale[0],
              17.0 * scale[1], 40.0 * scale[0], 16.0 * scale[1])
    Curveto_r(24.0 * scale[0], 0.0 * scale[1], 65.0 * scale[0], -
              4.0 * scale[1], 93.0 * scale[0], -8.0 * scale[1])
    Curveto_r(27.0 * scale[0], -5.0 * scale[1], 55.0 *
              scale[0], -6.0 * scale[1], 62.0 * scale[0], -4.0 * scale[1])
    Curveto_r(20.0 * scale[0], 8.0 * scale[1], -16.0 * scale[0],
              53.0 * scale[1], -41.0 * scale[0], 52.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -2.0 * scale[1], -20.0 *
              scale[0], -2.0 * scale[1], 2.0 * scale[0], -6.0 * scale[1])
    Curveto_r(36.0 * scale[0], -7.0 * scale[1], 27.0 * scale[0], -
              33.0 * scale[1], -10.0 * scale[0], -32.0 * scale[1])
    Lineto_r(-33.0 * scale[0], 1.0 * scale[1])
    Lineto_r(30.0 * scale[0], 8.0 * scale[1])
    Curveto_r(29.0 * scale[0], 7.0 * scale[1], 29.0 * scale[0],
              8.0 * scale[1], -10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-42.0 * scale[0], 2.0 * scale[1], -129.0 * scale[0],
              18.0 * scale[1], -107.0 * scale[0], 20.0 * scale[1])
    Curveto_r(21.0 * scale[0], 2.0 * scale[1], 13.0 * scale[0],
              18.0 * scale[1], -12.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 4.0 * scale[1], -24.0 * scale[0],
              2.0 * scale[1], -22.0 * scale[0], -21.0 * scale[1])
    te.end_fill()
    Moveto_r(35.0 * scale[0], -180.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -5.0 * scale[1], 9.0 * scale[0], -
              11.0 * scale[1], 5.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -15.0 * scale[0],
              1.0 * scale[1], -22.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 16.0 * scale[1], -5.0 * scale[0],
              18.0 * scale[1], 17.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(918.0 * scale[0], 1353.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(258.0 * scale[0], 1333.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -2.0 * scale[1], 30.0 *
              scale[0], -2.0 * scale[1], 40.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -23.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 0.0 * scale[1], -30.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(458.0 * scale[0], 1323.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(500.0 * scale[0], 1326.0 * scale[1], x, y)
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
    Moveto(922.0 * scale[0], 1310.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(753.0 * scale[0], 1313.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(24.0 * scale[0], -4.0 * scale[1], 26.0 * scale[0], -
              6.0 * scale[1], 13.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -10.0 * scale[1], -12.0 *
              scale[0], -14.0 * scale[1], 11.0 * scale[0], -31.0 * scale[1])
    Lineto_r(26.0 * scale[0], -19.0 * scale[1])
    Lineto_r(-6.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 13.0 * scale[1], -7.0 * scale[0],
              30.0 * scale[1], -7.0 * scale[0], 37.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -12.0 * scale[0],
              11.0 * scale[1], -32.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-32.0 * scale[0], -2.0 * scale[1], -32.0 *
              scale[0], -2.0 * scale[1], -5.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(335.0 * scale[0], 1251.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-33.0 * scale[0], -5.0 * scale[1], -36.0 *
              scale[0], -7.0 * scale[1], -17.0 * scale[0], -13.0 * scale[1])
    Curveto_r(26.0 * scale[0], -7.0 * scale[1], 62.0 * scale[0],
              0.0 * scale[1], 62.0 * scale[0], 13.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -1.0 * scale[0],
              8.0 * scale[1], -2.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -1.0 * scale[1], -21.0 *
              scale[0], -5.0 * scale[1], -43.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(726.0 * scale[0], 1252.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], 7.0 * scale[0], -
              8.0 * scale[1], 21.0 * scale[0], -8.0 * scale[1])
    Curveto_r(15.0 * scale[0], 1.0 * scale[1], 28.0 * scale[0], -
              5.0 * scale[1], 30.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], -1.0 * scale[0], -
              10.0 * scale[1], -14.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 6.0 * scale[1], -16.0 * scale[0],
              5.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0], -
              17.0 * scale[1], 3.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0],
              5.0 * scale[1], -17.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -14.0 * scale[0],
              10.0 * scale[1], -23.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -1.0 * scale[1], -9.0 *
              scale[0], -5.0 * scale[1], 9.0 * scale[0], -15.0 * scale[1])
    Curveto_r(36.0 * scale[0], -20.0 * scale[1], 44.0 * scale[0], -
              21.0 * scale[1], 46.0 * scale[0], -10.0 * scale[1])
    Curveto_r(1.0 * scale[0], 5.0 * scale[1], 9.0 * scale[0],
              12.0 * scale[1], 19.0 * scale[0], 15.0 * scale[1])
    Curveto_r(15.0 * scale[0], 6.0 * scale[1], 15.0 * scale[0],
              9.0 * scale[1], -6.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 22.0 * scale[1], -55.0 * scale[0],
              29.0 * scale[1], -64.0 * scale[0], 14.0 * scale[1])
    te.end_fill()
    Moveto(356.0 * scale[0], 1195.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -11.0 * scale[1], -1.0 * scale[0], -
              15.0 * scale[1], -19.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -29.0 * scale[0], -
              4.0 * scale[1], -32.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -11.0 * scale[1], 34.0 *
              scale[0], -14.0 * scale[1], 58.0 * scale[0], -4.0 * scale[1])
    Curveto_r(15.0 * scale[0], 5.0 * scale[1], 12.0 * scale[0],
              44.0 * scale[1], -4.0 * scale[0], 44.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0], -
              7.0 * scale[1], -3.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(235.0 * scale[0], 1180.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -13.0 * scale[1], 15.0 *
              scale[0], -13.0 * scale[1], 35.0 * scale[0], 0.0 * scale[1])
    Curveto_r(12.0 * scale[0], 8.0 * scale[1], 11.0 * scale[0],
              10.0 * scale[1], -7.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -25.0 * scale[0], -
              4.0 * scale[1], -28.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(930.0 * scale[0], 1177.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], -10.0 * scale[0], -
              22.0 * scale[1], -22.0 * scale[0], -27.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -5.0 * scale[1], -17.0 *
              scale[0], -9.0 * scale[1], -10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(6.0 * scale[0], -1.0 * scale[1], 12.0 * scale[0], -
              6.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -5.0 * scale[0], -
              7.0 * scale[1], -15.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 10.0 * scale[1], -19.0 * scale[0],
              10.0 * scale[1], -27.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -8.0 * scale[1], -18.0 *
              scale[0], -7.0 * scale[1], -38.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 8.0 * scale[1], -31.0 * scale[0],
              11.0 * scale[1], -35.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -4.0 * scale[1], -4.0 * scale[0],
              4.0 * scale[1], 0.0 * scale[0], 17.0 * scale[1])
    Curveto_r(5.0 * scale[0], 16.0 * scale[1], 4.0 * scale[0],
              21.0 * scale[1], -4.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -4.0 * scale[1], -11.0 * scale[0], -
              13.0 * scale[1], -11.0 * scale[0], -21.0 * scale[1])
    Curveto_r(0.0 * scale[0], -15.0 * scale[1], -22.0 * scale[0], -
              25.0 * scale[1], -58.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 0.0 * scale[1], -34.0 * scale[0], -
              5.0 * scale[1], -42.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -7.0 * scale[1], 5.0 *
              scale[0], -9.0 * scale[1], 57.0 * scale[0], -7.0 * scale[1])
    Curveto_r(41.0 * scale[0], 2.0 * scale[1], 69.0 * scale[0],
              0.0 * scale[1], 64.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -5.0 * scale[1], -54.0 * scale[0], -
              11.0 * scale[1], -110.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-55.0 * scale[0], -3.0 * scale[1], -101.0 * scale[0], -
              10.0 * scale[1], -101.0 * scale[0], -14.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 50.0 * scale[0], -
              8.0 * scale[1], 111.0 * scale[0], -7.0 * scale[1])
    Curveto_r(61.0 * scale[0], 0.0 * scale[1], 105.0 * scale[0],
              4.0 * scale[1], 99.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 4.0 * scale[1], 18.0 * scale[0],
              6.0 * scale[1], 56.0 * scale[0], 3.0 * scale[1])
    Curveto_r(65.0 * scale[0], -4.0 * scale[1], 68.0 *
              scale[0], -3.0 * scale[1], 44.0 * scale[0], 11.0 * scale[1])
    Lineto_r(-25.0 * scale[0], 16.0 * scale[1])
    Lineto_r(34.0 * scale[0], -7.0 * scale[1])
    Curveto_r(23.0 * scale[0], -4.0 * scale[1], 32.0 *
              scale[0], -3.0 * scale[1], 27.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], 0.0 * scale[0],
              12.0 * scale[1], 6.0 * scale[0], 15.0 * scale[1])
    Curveto_r(10.0 * scale[0], 3.0 * scale[1], 10.0 * scale[0],
              7.0 * scale[1], 0.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 13.0 * scale[1], -10.0 * scale[0],
              17.0 * scale[1], 0.0 * scale[0], 21.0 * scale[1])
    Curveto_r(10.0 * scale[0], 4.0 * scale[1], 11.0 * scale[0],
              7.0 * scale[1], 1.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 11.0 * scale[1], -13.0 * scale[0],
              10.0 * scale[1], -13.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(577.0 * scale[0], 1145.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-17.0 * scale[0], -35.0 * scale[1])
    Lineto_r(47.0 * scale[0], 0.0 * scale[1])
    Curveto_r(51.0 * scale[0], 0.0 * scale[1], 54.0 * scale[0],
              11.0 * scale[1], 4.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-35.0 * scale[0], 1.0 * scale[1], -35.0 * scale[0],
              2.0 * scale[1], -20.0 * scale[0], 30.0 * scale[1])
    Curveto_r(6.0 * scale[0], 11.0 * scale[1], 9.0 * scale[0],
              22.0 * scale[1], 7.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 2.0 * scale[1], -12.0 * scale[0], -
              12.0 * scale[1], -21.0 * scale[0], -31.0 * scale[1])
    te.end_fill()
    Moveto(228.0 * scale[0], 1053.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(23.0 * scale[0], -2.0 * scale[1], 59.0 *
              scale[0], -2.0 * scale[1], 80.0 * scale[0], 0.0 * scale[1])
    Curveto_r(20.0 * scale[0], 2.0 * scale[1], 1.0 * scale[0],
              4.0 * scale[1], -43.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-44.0 * scale[0], 0.0 * scale[1], -61.0 *
              scale[0], -2.0 * scale[1], -37.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(668.0 * scale[0], 1053.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(6.0 * scale[0], 1004.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -68.0 * scale[1], -7.0 * scale[0], -
              146.0 * scale[1], 3.0 * scale[0], -140.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 7.0 * scale[0],
              16.0 * scale[1], 3.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 14.0 * scale[1], -2.0 * scale[0],
              19.0 * scale[1], 6.0 * scale[0], 14.0 * scale[1])
    Curveto_r(7.0 * scale[0], -4.0 * scale[1], 12.0 *
              scale[0], -1.0 * scale[1], 12.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], -5.0 * scale[0],
              13.0 * scale[1], -10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -4.0 * scale[1], -10.0 * scale[0],
              5.0 * scale[1], -10.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], 4.0 * scale[0],
              24.0 * scale[1], 12.0 * scale[0], 19.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 8.0 *
              scale[0], -3.0 * scale[1], 5.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 15.0 * scale[1], 3.0 * scale[0],
              43.0 * scale[1], 17.0 * scale[0], 35.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 5.0 * scale[0],
              1.0 * scale[1], -3.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 15.0 * scale[1], -13.0 * scale[0],
              19.0 * scale[1], 0.0 * scale[0], 27.0 * scale[1])
    Curveto_r(11.0 * scale[0], 7.0 * scale[1], 9.0 * scale[0],
              9.0 * scale[1], -7.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 0.0 * scale[1], -22.0 * scale[0], -
              8.0 * scale[1], -28.0 * scale[0], -46.0 * scale[1])
    te.end_fill()
    Moveto(78.0 * scale[0], 1043.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(48.0 * scale[0], 1023.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(865.0 * scale[0], 1011.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              12.0 * scale[1], 3.0 * scale[0], -15.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 9.0 * scale[0],
              1.0 * scale[1], 9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], -3.0 * scale[0],
              19.0 * scale[1], -12.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(83.0 * scale[0], 997.0 * scale[1], x, y)
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
    Moveto(962.0 * scale[0], 998.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -12.0 * scale[1], -8.0 * scale[0], -
              16.0 * scale[1], -19.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 5.0 * scale[1], -17.0 * scale[0],
              5.0 * scale[1], 0.0 * scale[0], -6.0 * scale[1])
    Curveto_r(23.0 * scale[0], -15.0 * scale[1], 22.0 * scale[0], -
              47.0 * scale[1], -3.0 * scale[0], -60.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -6.0 * scale[1], -20.0 * scale[0], -
              16.0 * scale[1], -19.0 * scale[0], -23.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 2.0 *
              scale[0], -9.0 * scale[1], 6.0 * scale[0], 1.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 11.0 * scale[0],
              12.0 * scale[1], 19.0 * scale[0], 12.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0], -
              5.0 * scale[1], 8.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -10.0 * scale[1], -4.0 *
              scale[0], -10.0 * scale[1], 5.0 * scale[0], -2.0 * scale[1])
    Curveto_r(8.0 * scale[0], 7.0 * scale[1], 11.0 * scale[0],
              31.0 * scale[1], 8.0 * scale[0], 65.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 30.0 * scale[1], -4.0 * scale[0],
              46.0 * scale[1], -5.0 * scale[0], 37.0 * scale[1])
    te.end_fill()
    Moveto(861.0 * scale[0], 964.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -9.0 * scale[1], -22.0 * scale[0], -
              14.0 * scale[1], -32.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 3.0 * scale[1], -20.0 *
              scale[0], -1.0 * scale[1], -23.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -10.0 * scale[1], 2.0 * scale[0], -
              11.0 * scale[1], 24.0 * scale[0], -5.0 * scale[1])
    Curveto_r(16.0 * scale[0], 4.0 * scale[1], 30.0 * scale[0],
              7.0 * scale[1], 32.0 * scale[0], 5.0 * scale[1])
    Curveto_r(2.0 * scale[0], -2.0 * scale[1], 9.0 * scale[0],
              5.0 * scale[1], 16.0 * scale[0], 15.0 * scale[1])
    Curveto_r(14.0 * scale[0], 24.0 * scale[1], 3.0 * scale[0],
              26.0 * scale[1], -17.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(108.0 * scale[0], 963.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(286.0 * scale[0], 955.0 * scale[1], x, y)
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
    Moveto(455.0 * scale[0], 939.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -5.0 * scale[1], 18.0 * scale[0], -
              9.0 * scale[1], 32.0 * scale[0], -9.0 * scale[1])
    Curveto_r(32.0 * scale[0], 0.0 * scale[1], 23.0 * scale[0],
              12.0 * scale[1], -12.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 1.0 * scale[1], -23.0 *
              scale[0], -2.0 * scale[1], -20.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(520.0 * scale[0], 938.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 6.0 * scale[0], -
              9.0 * scale[1], 13.0 * scale[0], -9.0 * scale[1])
    Curveto_r(6.0 * scale[0], -1.0 * scale[1], 24.0 * scale[0], -
              3.0 * scale[1], 40.0 * scale[0], -5.0 * scale[1])
    Curveto_r(15.0 * scale[0], -1.0 * scale[1], 27.0 * scale[0],
              1.0 * scale[1], 27.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], -18.0 * scale[0],
              10.0 * scale[1], -40.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 2.0 * scale[1], -40.0 * scale[0],
              0.0 * scale[1], -40.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(102.0 * scale[0], 918.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -7.0 * scale[1], -12.0 * scale[0], -
              16.0 * scale[1], -12.0 * scale[0], -21.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              1.0 * scale[1], 16.0 * scale[0], 8.0 * scale[1])
    Curveto_r(9.0 * scale[0], 9.0 * scale[1], 14.0 * scale[0],
              18.0 * scale[1], 12.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0], -
              1.0 * scale[1], -16.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(425.0 * scale[0], 920.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -11.0 *
              scale[0], -7.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -8.0 * scale[0],
              2.0 * scale[1], -5.0 * scale[0], -3.0 * scale[1])
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 1.0 * scale[0], -
              13.0 * scale[1], -7.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -3.0 * scale[1], -12.0 * scale[0], -
              15.0 * scale[1], -9.0 * scale[0], -31.0 * scale[1])
    Curveto_r(3.0 * scale[0], -14.0 * scale[1], 9.0 * scale[0], -
              23.0 * scale[1], 14.0 * scale[0], -20.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 7.0 * scale[0],
              9.0 * scale[1], 4.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 14.0 * scale[1], 7.0 * scale[0],
              41.0 * scale[1], 28.0 * scale[0], 49.0 * scale[1])
    Curveto_r(13.0 * scale[0], 5.0 * scale[1], 16.0 * scale[0],
              10.0 * scale[1], 9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -13.0 * scale[0],
              2.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(486.0 * scale[0], 893.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(230.0 * scale[0], 890.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-53.0 * scale[0], -17.0 * scale[1], -83.0 *
              scale[0], -31.0 * scale[1], -77.0 * scale[0], -36.0 * scale[1])
    Curveto_r(7.0 * scale[0], -8.0 * scale[1], 76.0 * scale[0],
              14.0 * scale[1], 102.0 * scale[0], 32.0 * scale[1])
    Curveto_r(21.0 * scale[0], 15.0 * scale[1], 13.0 * scale[0],
              17.0 * scale[1], -25.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(958.0 * scale[0], 855.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -14.0 * scale[1], 6.0 * scale[0], -
              25.0 * scale[1], 8.0 * scale[0], -25.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 4.0 * scale[0],
              11.0 * scale[1], 4.0 * scale[0], 25.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -4.0 * scale[0],
              25.0 * scale[1], -9.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0], -
              11.0 * scale[1], -3.0 * scale[0], -25.0 * scale[1])
    te.end_fill()
    Moveto(367.0 * scale[0], 863.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-14.0 * scale[0], -14.0 * scale[1], -6.0 *
              scale[0], -43.0 * scale[1], 16.0 * scale[0], -54.0 * scale[1])
    Curveto_r(22.0 * scale[0], -12.0 * scale[1], 22.0 *
              scale[0], -12.0 * scale[1], 3.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 12.0 * scale[1], -16.0 * scale[0],
              28.0 * scale[1], -13.0 * scale[0], 37.0 * scale[1])
    Curveto_r(7.0 * scale[0], 16.0 * scale[1], 4.0 * scale[0],
              19.0 * scale[1], -6.0 * scale[0], 8.0 * scale[1])
    te.end_fill()
    Moveto(108.0 * scale[0], 835.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-15.0 * scale[0], -17.0 * scale[1], -32.0 *
              scale[0], -25.0 * scale[1], -55.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -32.0 *
              scale[0], -4.0 * scale[1], -29.0 * scale[0], -9.0 * scale[1])
    Curveto_r(4.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              11.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              88.0 * scale[1], 22.0 * scale[0], -88.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              11.0 * scale[1], 3.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 20.0 * scale[1], -4.0 * scale[0],
              25.0 * scale[1], 5.0 * scale[0], 19.0 * scale[1])
    Curveto_r(7.0 * scale[0], -4.0 * scale[1], 18.0 * scale[0],
              1.0 * scale[1], 26.0 * scale[0], 11.0 * scale[1])
    Curveto_r(8.0 * scale[0], 11.0 * scale[1], 15.0 * scale[0],
              15.0 * scale[1], 16.0 * scale[0], 9.0 * scale[1])
    Curveto_r(1.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0],
              4.0 * scale[1], 9.0 * scale[0], 20.0 * scale[1])
    Lineto_r(7.0 * scale[0], 30.0 * scale[1])
    Lineto_r(11.0 * scale[0], -25.0 * scale[1])
    Lineto_r(11.0 * scale[0], -25.0 * scale[1])
    Lineto_r(-1.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 14.0 * scale[1], 2.0 * scale[0],
              35.0 * scale[1], 6.0 * scale[0], 48.0 * scale[1])
    Curveto_r(10.0 * scale[0], 29.0 * scale[1], 1.0 * scale[0],
              28.0 * scale[1], -26.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(489.0 * scale[0], 793.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -9.0 * scale[1], -9.0 * scale[0], -
              14.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 4.0 * scale[1], 14.0 * scale[0], -
              13.0 * scale[1], 18.0 * scale[0], -53.0 * scale[1])
    Curveto_r(5.0 * scale[0], -45.0 * scale[1], 11.0 * scale[0], -
              60.0 * scale[1], 23.0 * scale[0], -60.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0], -
              6.0 * scale[1], 9.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -18.0 * scale[1], 1.0 * scale[0], -
              19.0 * scale[1], 45.0 * scale[0], -3.0 * scale[1])
    Lineto_r(34.0 * scale[0], 13.0 * scale[1])
    Lineto_r(-40.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-46.0 * scale[0], 6.0 * scale[1], -62.0 * scale[0],
              30.0 * scale[1], -66.0 * scale[0], 98.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 23.0 * scale[1], -4.0 * scale[0],
              42.0 * scale[1], -5.0 * scale[0], 42.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              8.0 * scale[1], -15.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(470.0 * scale[0], 750.0 * scale[1], x, y)
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
    Moveto(665.0 * scale[0], 700.0 * scale[1], x, y)
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
    Moveto(643.0 * scale[0], 675.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 8.0 * scale[0], -
              11.0 * scale[1], 18.0 * scale[0], -10.0 * scale[1])
    Curveto_r(29.0 * scale[0], 2.0 * scale[1], 32.0 * scale[0],
              12.0 * scale[1], 6.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 3.0 * scale[1], -24.0 * scale[0],
              0.0 * scale[1], -24.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(695.0 * scale[0], 660.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(31.0 * scale[0], 644.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(733.0 * scale[0], 652.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(-22.0 * scale[0], -7.0 * scale[1])
    Lineto_r(24.0 * scale[0], -11.0 * scale[1])
    Curveto_r(20.0 * scale[0], -10.0 * scale[1], 23.0 *
              scale[0], -9.0 * scale[1], 22.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 11.0 * scale[1], -1.0 * scale[0],
              19.0 * scale[1], -2.0 * scale[0], 18.0 * scale[1])
    Curveto_r(0.0 * scale[0], -1.0 * scale[1], -10.0 * scale[0], -
              4.0 * scale[1], -22.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(542.0 * scale[0], 598.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -15.0 * scale[1], 6.0 * scale[0], -
              128.0 * scale[1], 20.0 * scale[0], -128.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0],
              27.0 * scale[1], 8.0 * scale[0], 61.0 * scale[1])
    Curveto_r(0.0 * scale[0], 43.0 * scale[1], -3.0 * scale[0],
              58.0 * scale[1], -12.0 * scale[0], 53.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -5.0 * scale[1], -9.0 *
              scale[0], -2.0 * scale[1], -5.0 * scale[0], 9.0 * scale[1])
    Curveto_r(8.0 * scale[0], 20.0 * scale[1], 3.0 * scale[0],
              22.0 * scale[1], -11.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(761.0 * scale[0], 594.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(768.0 * scale[0], 545.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -16.0 * scale[1], -1.0 *
              scale[0], -25.0 * scale[1], 7.0 * scale[0], -25.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              9.0 * scale[1], 7.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 14.0 * scale[1], -6.0 * scale[0],
              25.0 * scale[1], -7.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 0.0 * scale[1], -5.0 * scale[0], -
              11.0 * scale[1], -7.0 * scale[0], -25.0 * scale[1])
    te.end_fill()
    Moveto(715.0 * scale[0], 469.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0], -
              12.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 17.0 * scale[1], 1.0 * scale[0],
              20.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(560.0 * scale[0], 450.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 9.0 * scale[0], -
              14.0 * scale[1], 20.0 * scale[0], -20.0 * scale[1])
    Curveto_r(14.0 * scale[0], -7.0 * scale[1], 20.0 *
              scale[0], -7.0 * scale[1], 20.0 * scale[0], 0.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -7.0 * scale[0],
              10.0 * scale[1], -16.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0],
              5.0 * scale[1], -9.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 1.0 * scale[0],
              10.0 * scale[1], -4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              4.0 * scale[1], -11.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(690.0 * scale[0], 430.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 18.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], -15.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(17.0 * scale[0], 418.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -7.0 * scale[1], -17.0 * scale[0], -
              22.0 * scale[1], -16.0 * scale[0], -66.0 * scale[1])
    Curveto_r(1.0 * scale[0], -51.0 * scale[1], 2.0 * scale[0], -
              54.0 * scale[1], 10.0 * scale[0], -27.0 * scale[1])
    Curveto_r(5.0 * scale[0], 17.0 * scale[1], 7.0 * scale[0],
              42.0 * scale[1], 5.0 * scale[0], 58.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 22.0 * scale[1], -2.0 * scale[0],
              27.0 * scale[1], 14.0 * scale[0], 27.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0], -
              7.0 * scale[1], 20.0 * scale[0], -15.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              15.0 * scale[1], 9.0 * scale[0], -15.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 1.0 * scale[0],
              38.0 * scale[1], -13.0 * scale[0], 43.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 3.0 * scale[1], -20.0 * scale[0],
              1.0 * scale[1], -29.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(71.0 * scale[0], 355.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 8.0 * scale[0], -
              33.0 * scale[1], 19.0 * scale[0], -50.0 * scale[1])
    Curveto_r(11.0 * scale[0], -16.0 * scale[1], 20.0 * scale[0], -
              25.0 * scale[1], 20.0 * scale[0], -18.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -4.0 * scale[0],
              15.0 * scale[1], -10.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -14.0 * scale[0],
              20.0 * scale[1], -19.0 * scale[0], 38.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 20.0 * scale[1], -9.0 * scale[0],
              25.0 * scale[1], -10.0 * scale[0], 12.0 * scale[1])
    te.end_fill()
    Moveto(748.0 * scale[0], 91.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-58.0 * scale[0], -57.0 * scale[1], -67.0 *
              scale[0], -71.0 * scale[1], -47.0 * scale[0], -71.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0],
              4.0 * scale[1], 5.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], 1.0 * scale[0],
              14.0 * scale[1], 9.0 * scale[0], 21.0 * scale[1])
    Curveto_r(13.0 * scale[0], 11.0 * scale[1], 14.0 * scale[0],
              10.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -13.0 * scale[1], 1.0 * scale[0], -
              16.0 * scale[1], 32.0 * scale[0], -16.0 * scale[1])
    Curveto_r(61.0 * scale[0], 0.0 * scale[1], 69.0 * scale[0],
              10.0 * scale[1], 58.0 * scale[0], 68.0 * scale[1])
    Lineto_r(-9.0 * scale[0], 50.0 * scale[1])
    Lineto_r(-57.0 * scale[0], -57.0 * scale[1])
    te.end_fill()
    Moveto_r(22.0 * scale[0], -22.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -4.0 * scale[0], -
              9.0 * scale[1], -10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0],
              7.0 * scale[1], -10.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 5.0 * scale[0],
              12.0 * scale[1], 10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 10.0 * scale[0], -
              10.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(828.0 * scale[0], 13.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.penup()
