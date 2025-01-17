import turtle as te
from helper import *


def plage(x, y, scale):

    te.penup()
    te.color('#fcda96')
    te.end_fill()
    Moveto(110.0 * scale[0], 1616.0 * scale[1], x, y)
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
    Moveto(165.0 * scale[0], 1610.0 * scale[1], x, y)
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
    Moveto(55.0 * scale[0], 1599.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-17.0 * scale[0], -6.0 * scale[1], -17.0 *
              scale[0], -8.0 * scale[1], -2.0 * scale[0], -8.0 * scale[1])
    Curveto_r(9.0 * scale[0], -1.0 * scale[1], 17.0 * scale[0], -
              6.0 * scale[1], 17.0 * scale[0], -12.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -12.0 * scale[0], -
              10.0 * scale[1], -35.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-34.0 * scale[0], 6.0 * scale[1], -35.0 * scale[0],
              5.0 * scale[1], -35.0 * scale[0], -28.0 * scale[1])
    Curveto_r(0.0 * scale[0], -25.0 * scale[1], 4.0 * scale[0], -
              33.0 * scale[1], 14.0 * scale[0], -29.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 30.0 * scale[0], -
              9.0 * scale[1], 50.0 * scale[0], -27.0 * scale[1])
    Lineto_r(37.0 * scale[0], -32.0 * scale[1])
    Lineto_r(46.0 * scale[0], 23.0 * scale[1])
    Lineto_r(45.0 * scale[0], 23.0 * scale[1])
    Lineto_r(34.0 * scale[0], -38.0 * scale[1])
    Curveto_r(32.0 * scale[0], -34.0 * scale[1], 38.0 * scale[0], -
              36.0 * scale[1], 73.0 * scale[0], -30.0 * scale[1])
    Curveto_r(29.0 * scale[0], 5.0 * scale[1], 49.0 * scale[0],
              1.0 * scale[1], 80.0 * scale[0], -14.0 * scale[1])
    Curveto_r(22.0 * scale[0], -12.0 * scale[1], 58.0 * scale[0], -
              21.0 * scale[1], 79.0 * scale[0], -21.0 * scale[1])
    Curveto_r(22.0 * scale[0], 0.0 * scale[1], 61.0 * scale[0], -
              9.0 * scale[1], 87.0 * scale[0], -21.0 * scale[1])
    Curveto_r(48.0 * scale[0], -21.0 * scale[1], 169.0 * scale[0], -
              28.0 * scale[1], 235.0 * scale[0], -14.0 * scale[1])
    Curveto_r(24.0 * scale[0], 5.0 * scale[1], 33.0 * scale[0],
              1.0 * scale[1], 57.0 * scale[0], -29.0 * scale[1])
    Curveto_r(33.0 * scale[0], -42.0 * scale[1], 48.0 * scale[0], -
              44.0 * scale[1], 82.0 * scale[0], -12.0 * scale[1])
    Curveto_r(15.0 * scale[0], 14.0 * scale[1], 48.0 * scale[0],
              31.0 * scale[1], 74.0 * scale[0], 38.0 * scale[1])
    Curveto_r(43.0 * scale[0], 11.0 * scale[1], 52.0 * scale[0],
              10.0 * scale[1], 79.0 * scale[0], -5.0 * scale[1])
    Curveto_r(37.0 * scale[0], -21.0 * scale[1], 57.0 *
              scale[0], -21.0 * scale[1], 86.0 * scale[0], -1.0 * scale[1])
    Curveto_r(30.0 * scale[0], 21.0 * scale[1], 74.0 * scale[0],
              34.0 * scale[1], 149.0 * scale[0], 44.0 * scale[1])
    Curveto_r(56.0 * scale[0], 7.0 * scale[1], 129.0 * scale[0],
              38.0 * scale[1], 229.0 * scale[0], 96.0 * scale[1])
    Curveto_r(31.0 * scale[0], 18.0 * scale[1], 32.0 * scale[0],
              18.0 * scale[1], 62.0 * scale[0], -8.0 * scale[1])
    Curveto_r(20.0 * scale[0], -17.0 * scale[1], 49.0 * scale[0], -
              29.0 * scale[1], 81.0 * scale[0], -33.0 * scale[1])
    Curveto_r(28.0 * scale[0], -4.0 * scale[1], 62.0 * scale[0], -
              16.0 * scale[1], 75.0 * scale[0], -26.0 * scale[1])
    Curveto_r(27.0 * scale[0], -22.0 * scale[1], 161.0 * scale[0], -
              49.0 * scale[1], 238.0 * scale[0], -49.0 * scale[1])
    Curveto_r(41.0 * scale[0], 0.0 * scale[1], 50.0 * scale[0], -
              4.0 * scale[1], 65.0 * scale[0], -27.0 * scale[1])
    Curveto_r(9.0 * scale[0], -16.0 * scale[1], 18.0 * scale[0], -
              29.0 * scale[1], 19.0 * scale[0], -31.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 34.0 * scale[0], -
              10.0 * scale[1], 62.0 * scale[0], -11.0 * scale[1])
    Curveto_r(18.0 * scale[0], -1.0 * scale[1], 27.0 * scale[0], -
              11.0 * scale[1], 39.0 * scale[0], -41.0 * scale[1])
    Curveto_r(17.0 * scale[0], -42.0 * scale[1], 31.0 * scale[0], -
              48.0 * scale[1], 78.0 * scale[0], -30.0 * scale[1])
    Curveto_r(21.0 * scale[0], 8.0 * scale[1], 38.0 * scale[0],
              3.0 * scale[1], 103.0 * scale[0], -29.0 * scale[1])
    Curveto_r(42.0 * scale[0], -22.0 * scale[1], 106.0 * scale[0], -
              48.0 * scale[1], 141.0 * scale[0], -59.0 * scale[1])
    Lineto_r(63.0 * scale[0], -19.0 * scale[1])
    Lineto_r(57.0 * scale[0], 29.0 * scale[1])
    Curveto_r(38.0 * scale[0], 20.0 * scale[1], 72.0 * scale[0],
              29.0 * scale[1], 101.0 * scale[0], 29.0 * scale[1])
    Curveto_r(73.0 * scale[0], 0.0 * scale[1], 140.0 * scale[0],
              20.0 * scale[1], 161.0 * scale[0], 49.0 * scale[1])
    Curveto_r(10.0 * scale[0], 14.0 * scale[1], 28.0 * scale[0],
              35.0 * scale[1], 40.0 * scale[0], 47.0 * scale[1])
    Lineto_r(22.0 * scale[0], 22.0 * scale[1])
    Lineto_r(-26.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 6.0 * scale[1], -35.0 * scale[0],
              0.0 * scale[1], -68.0 * scale[0], -26.0 * scale[1])
    Curveto_r(-38.0 * scale[0], -30.0 * scale[1], -43.0 *
              scale[0], -31.0 * scale[1], -54.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 15.0 * scale[1], -14.0 * scale[0],
              16.0 * scale[1], -25.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -11.0 * scale[1], -16.0 *
              scale[0], -12.0 * scale[1], -25.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 8.0 * scale[1], -14.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -16.0 * scale[1], -11.0 * scale[0], -
              19.0 * scale[1], -26.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 4.0 * scale[1], -21.0 * scale[0],
              2.0 * scale[1], -21.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -4.0 * scale[0], -
              11.0 * scale[1], -10.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0],
              6.0 * scale[1], -10.0 * scale[0], 13.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -9.0 * scale[0],
              13.0 * scale[1], -22.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -1.0 * scale[1], -22.0 *
              scale[0], -8.0 * scale[1], -20.0 * scale[0], -19.0 * scale[1])
    Curveto_r(4.0 * scale[0], -21.0 * scale[1], -14.0 *
              scale[0], -21.0 * scale[1], -22.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 22.0 * scale[1], -8.0 * scale[0],
              24.0 * scale[1], 6.0 * scale[0], 22.0 * scale[1])
    Curveto_r(7.0 * scale[0], -2.0 * scale[1], 13.0 * scale[0],
              4.0 * scale[1], 13.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -10.0 * scale[0],
              16.0 * scale[1], -22.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 2.0 * scale[1], -23.0 * scale[0], -
              2.0 * scale[1], -23.0 * scale[0], -12.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], -4.0 * scale[0], -
              16.0 * scale[1], -10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              7.0 * scale[1], -10.0 * scale[0], -15.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -6.0 * scale[0], -
              15.0 * scale[1], -14.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -29.0 * scale[0],
              17.0 * scale[1], -16.0 * scale[0], 25.0 * scale[1])
    Curveto_r(17.0 * scale[0], 10.0 * scale[1], 11.0 * scale[0],
              25.0 * scale[1], -7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -5.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -8.0 * scale[0], 8.0 * scale[1])
    Curveto_r(6.0 * scale[0], 11.0 * scale[1], 5.0 * scale[0],
              12.0 * scale[1], -6.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -19.0 * scale[1], -46.0 *
              scale[0], -16.0 * scale[1], -52.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 13.0 * scale[1], -13.0 * scale[0],
              20.0 * scale[1], -29.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 0.0 * scale[1], -20.0 *
              scale[0], -2.0 * scale[1], -8.0 * scale[0], -10.0 * scale[1])
    Curveto_r(25.0 * scale[0], -16.0 * scale[1], -2.0 * scale[0], -
              28.0 * scale[1], -30.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 8.0 * scale[1], -19.0 * scale[0],
              14.0 * scale[1], -11.0 * scale[0], 14.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              4.0 * scale[1], -5.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-28.0 * scale[0], 21.0 * scale[1], -34.0 * scale[0],
              18.0 * scale[1], -21.0 * scale[0], -10.0 * scale[1])
    Curveto_r(7.0 * scale[0], -14.0 * scale[1], 15.0 * scale[0], -
              25.0 * scale[1], 20.0 * scale[0], -25.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0], -
              7.0 * scale[1], 7.0 * scale[0], -15.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -4.0 * scale[0], -
              15.0 * scale[1], -9.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0], -
              3.0 * scale[1], -27.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -5.0 * scale[1], -16.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], 15.0 * scale[1])
    Curveto_r(4.0 * scale[0], 12.0 * scale[1], 3.0 * scale[0],
              22.0 * scale[1], 0.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 1.0 * scale[1], -20.0 * scale[0],
              2.0 * scale[1], -36.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 1.0 * scale[1], -31.0 * scale[0],
              8.0 * scale[1], -37.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 17.0 * scale[1], -15.0 * scale[0],
              22.0 * scale[1], -29.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -4.0 * scale[1], -20.0 * scale[0],
              0.0 * scale[1], -20.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 16.0 * scale[1], -3.0 * scale[0],
              18.0 * scale[1], -14.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -9.0 * scale[1], -16.0 *
              scale[0], -8.0 * scale[1], -26.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 8.0 * scale[1], -19.0 * scale[0],
              15.0 * scale[1], -26.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0],
              5.0 * scale[1], -14.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -4.0 * scale[0],
              8.0 * scale[1], -14.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -10.0 * scale[1], -20.0 *
              scale[0], -10.0 * scale[1], -38.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 7.0 * scale[1], -31.0 * scale[0],
              12.0 * scale[1], -40.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -1.0 * scale[1], -18.0 * scale[0],
              4.0 * scale[1], -18.0 * scale[0], 17.0 * scale[1])
    Curveto_r(0.0 * scale[0], 24.0 * scale[1], -17.0 * scale[0],
              32.0 * scale[1], -52.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -3.0 * scale[1], -33.0 * scale[0],
              2.0 * scale[1], -47.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 11.0 * scale[1], -27.0 * scale[0],
              18.0 * scale[1], -36.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -4.0 * scale[1], -15.0 * scale[0],
              0.0 * scale[1], -15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], 8.0 * scale[0],
              16.0 * scale[1], 18.0 * scale[0], 17.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              3.0 * scale[1], -6.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 6.0 * scale[1], -27.0 * scale[0],
              5.0 * scale[1], -38.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -20.0 * scale[1], -26.0 *
              scale[0], -19.0 * scale[1], -52.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-26.0 * scale[0], 24.0 * scale[1], -28.0 * scale[0],
              40.0 * scale[1], -7.0 * scale[0], 40.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0], -
              7.0 * scale[1], 15.0 * scale[0], -15.0 * scale[1])
    Curveto_r(0.0 * scale[0], -17.0 * scale[1], 16.0 * scale[0], -
              20.0 * scale[1], 25.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], -6.0 * scale[0],
              21.0 * scale[1], -20.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 30.0 * scale[1], -37.0 * scale[0],
              32.0 * scale[1], -29.0 * scale[0], 11.0 * scale[1])
    Curveto_r(5.0 * scale[0], -13.0 * scale[1], 2.0 * scale[0], -
              14.0 * scale[1], -19.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 7.0 * scale[1], -36.0 * scale[0],
              7.0 * scale[1], -57.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-22.0 * scale[0], -7.0 * scale[1], -35.0 *
              scale[0], -7.0 * scale[1], -42.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 8.0 * scale[1], -18.0 * scale[0],
              6.0 * scale[1], -34.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -8.0 * scale[1], -28.0 *
              scale[0], -12.0 * scale[1], -34.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -17.0 * scale[0],
              2.0 * scale[1], -25.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -7.0 * scale[1], -15.0 *
              scale[0], -8.0 * scale[1], -20.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 7.0 * scale[1], -11.0 * scale[0],
              5.0 * scale[1], -21.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -17.0 * scale[1], -34.0 *
              scale[0], -20.0 * scale[1], -34.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -4.0 * scale[0],
              7.0 * scale[1], -10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -7.0 * scale[1], -2.0 * scale[0],
              23.0 * scale[1], 13.0 * scale[0], 43.0 * scale[1])
    Curveto_r(7.0 * scale[0], 9.0 * scale[1], 6.0 * scale[0],
              11.0 * scale[1], -4.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-24.0 * scale[0], -9.0 * scale[1], -42.0 * scale[0], -
              45.0 * scale[1], -29.0 * scale[0], -59.0 * scale[1])
    Curveto_r(7.0 * scale[0], -10.0 * scale[1], 6.0 * scale[0], -
              17.0 * scale[1], -4.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -10.0 * scale[1], -17.0 *
              scale[0], -8.0 * scale[1], -26.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 12.0 * scale[1], -17.0 * scale[0],
              21.0 * scale[1], -25.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0], -
              17.0 * scale[1], -2.0 * scale[0], -23.0 * scale[1])
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 9.0 * scale[0], -
              8.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -4.0 * scale[1], -15.0 *
              scale[0], -2.0 * scale[1], -24.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 11.0 * scale[1], -17.0 * scale[0],
              11.0 * scale[1], -23.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -7.0 * scale[1], -20.0 * scale[0], -
              11.0 * scale[1], -33.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 2.0 * scale[1], -33.0 * scale[0], -
              3.0 * scale[1], -43.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -13.0 * scale[1], -19.0 *
              scale[0], -12.0 * scale[1], -30.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 11.0 * scale[1], -19.0 * scale[0],
              15.0 * scale[1], -27.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -5.0 * scale[1], -20.0 *
              scale[0], -9.0 * scale[1], -28.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -1.0 * scale[1], -25.0 *
              scale[0], -2.0 * scale[1], -37.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -1.0 * scale[1], -23.0 *
              scale[0], -8.0 * scale[1], -23.0 * scale[0], -21.0 * scale[1])
    Curveto_r(0.0 * scale[0], -28.0 * scale[1], -21.0 * scale[0], -
              37.0 * scale[1], -36.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 12.0 * scale[1], -13.0 * scale[0],
              13.0 * scale[1], -16.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -17.0 * scale[1], -41.0 *
              scale[0], -21.0 * scale[1], -50.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 9.0 * scale[1], -12.0 * scale[0],
              9.0 * scale[1], -27.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-23.0 * scale[0], -14.0 * scale[1], -35.0 *
              scale[0], -5.0 * scale[1], -20.0 * scale[0], 14.0 * scale[1])
    Curveto_r(9.0 * scale[0], 10.0 * scale[1], 7.0 * scale[0],
              13.0 * scale[1], -9.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 0.0 * scale[1], -19.0 * scale[0], -
              5.0 * scale[1], -15.0 * scale[0], -20.0 * scale[1])
    Curveto_r(3.0 * scale[0], -11.0 * scale[1], 0.0 * scale[0], -
              20.0 * scale[1], -5.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0],
              9.0 * scale[1], -22.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 14.0 * scale[1], -21.0 * scale[0],
              20.0 * scale[1], -45.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -34.0 *
              scale[0], -3.0 * scale[1], -33.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], -9.0 * scale[1], -5.0 * scale[0], -
              13.0 * scale[1], -27.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0],
              6.0 * scale[1], -9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(5.0 * scale[0], 11.0 * scale[1], -1.0 * scale[0],
              15.0 * scale[1], -25.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 0.0 * scale[1], -31.0 * scale[0], -
              5.0 * scale[1], -31.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -8.0 * scale[1], -6.0 *
              scale[0], -7.0 * scale[1], -14.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 16.0 * scale[1], -14.0 * scale[0],
              16.0 * scale[1], -29.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -14.0 * scale[1], -21.0 *
              scale[0], -15.0 * scale[1], -42.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 7.0 * scale[1], -31.0 * scale[0],
              10.0 * scale[1], -36.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -12.0 * scale[0],
              3.0 * scale[1], -16.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 25.0 * scale[1], -25.0 * scale[0],
              34.0 * scale[1], -40.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -7.0 * scale[1], -17.0 *
              scale[0], -7.0 * scale[1], -26.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 8.0 * scale[1], -17.0 * scale[0],
              5.0 * scale[1], -26.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -17.0 * scale[1], -19.0 *
              scale[0], -22.0 * scale[1], -39.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-65.0 * scale[0], 10.0 * scale[1], -72.0 * scale[0],
              14.0 * scale[1], -73.0 * scale[0], 36.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], -3.0 * scale[0],
              16.0 * scale[1], -6.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -19.0 * scale[1], -31.0 *
              scale[0], -16.0 * scale[1], -36.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 16.0 * scale[1], -5.0 * scale[0],
              16.0 * scale[1], -6.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -11.0 * scale[1], -9.0 * scale[0], -
              18.0 * scale[1], -22.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0],
              5.0 * scale[1], -17.0 * scale[0], 25.0 * scale[1])
    Curveto_r(4.0 * scale[0], 16.0 * scale[1], 1.0 * scale[0],
              25.0 * scale[1], -8.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -19.0 * scale[0],
              3.0 * scale[1], -27.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 3.0 * scale[1], -16.0 * scale[0], -
              3.0 * scale[1], -20.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -19.0 * scale[1], -8.0 * scale[0], -
              20.0 * scale[1], -29.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 6.0 * scale[1], -26.0 * scale[0],
              17.0 * scale[1], -30.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 7.0 * scale[1], -8.0 * scale[0],
              4.0 * scale[1], -8.0 * scale[0], -6.0 * scale[1])
    Curveto_r(0.0 * scale[0], -19.0 * scale[1], -26.0 * scale[0], -
              25.0 * scale[1], -32.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 5.0 * scale[1], -23.0 * scale[0],
              12.0 * scale[1], -48.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-34.0 * scale[0], 3.0 * scale[1], -46.0 * scale[0],
              8.0 * scale[1], -50.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 16.0 * scale[1], -10.0 * scale[0],
              18.0 * scale[1], -25.0 * scale[0], 12.0 * scale[1])
    te.end_fill()
    Moveto_r(745.0 * scale[0], -139.0 * scale[1], 0, 0)
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
    Moveto_r(90.0 * scale[0], -10.0 * scale[1], 0, 0)
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
    Moveto_r(1610.0 * scale[0], -200.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -11.0 * scale[0], -
              10.0 * scale[1], -25.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -25.0 * scale[0],
              5.0 * scale[1], -25.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 11.0 * scale[0],
              10.0 * scale[1], 25.0 * scale[0], 10.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 25.0 * scale[0], -
              4.0 * scale[1], 25.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(367.0 * scale[0], 1559.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(3816.0 * scale[0], 1557.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-17.0 * scale[0], -12.0 * scale[1], -17.0 *
              scale[0], -14.0 * scale[1], -2.0 * scale[0], -20.0 * scale[1])
    Curveto_r(9.0 * scale[0], -4.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 16.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], 27.0 * scale[0],
              13.0 * scale[1], 35.0 * scale[0], 1.0 * scale[1])
    Curveto_r(7.0 * scale[0], -13.0 * scale[1], -52.0 * scale[0], -
              41.0 * scale[1], -71.0 * scale[0], -34.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 3.0 * scale[1], -12.0 * scale[0],
              12.0 * scale[1], -8.0 * scale[0], 26.0 * scale[1])
    Curveto_r(5.0 * scale[0], 15.0 * scale[1], 3.0 * scale[0],
              19.0 * scale[1], -10.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -3.0 * scale[1], -18.0 *
              scale[0], -2.0 * scale[1], -21.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], -55.0 * scale[0], -
              10.0 * scale[1], -55.0 * scale[0], -21.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 18.0 *
              scale[0], -10.0 * scale[1], 24.0 * scale[0], 1.0 * scale[1])
    Curveto_r(9.0 * scale[0], 14.0 * scale[1], 46.0 * scale[0],
              1.0 * scale[1], 46.0 * scale[0], -15.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], -7.0 * scale[0], -
              13.0 * scale[1], -25.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 4.0 * scale[1], -25.0 * scale[0],
              2.0 * scale[1], -25.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -7.0 * scale[0], -
              11.0 * scale[1], -15.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0],
              9.0 * scale[1], -15.0 * scale[0], 25.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], -4.0 * scale[0],
              23.0 * scale[1], -14.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -3.0 * scale[1], -14.0 * scale[0], -
              17.0 * scale[1], -13.0 * scale[0], -32.0 * scale[1])
    Curveto_r(2.0 * scale[0], -23.0 * scale[1], -2.0 * scale[0], -
              27.0 * scale[1], -28.0 * scale[0], -30.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -2.0 * scale[1], -34.0 *
              scale[0], -8.0 * scale[1], -40.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -12.0 * scale[1], -21.0 *
              scale[0], -11.0 * scale[1], -37.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 17.0 * scale[1], -68.0 * scale[0],
              31.0 * scale[1], -68.0 * scale[0], 18.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 6.0 * scale[0], -
              11.0 * scale[1], 13.0 * scale[0], -14.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 6.0 * scale[0], -
              9.0 * scale[1], -8.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -11.0 * scale[1], -24.0 *
              scale[0], -12.0 * scale[1], -33.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 6.0 * scale[1], -29.0 * scale[0],
              8.0 * scale[1], -55.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-23.0 * scale[0], -4.0 * scale[1], -48.0 *
              scale[0], -8.0 * scale[1], -55.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -1.0 * scale[1], -10.0 *
              scale[0], -9.0 * scale[1], -6.0 * scale[0], -20.0 * scale[1])
    Curveto_r(8.0 * scale[0], -25.0 * scale[1], -21.0 * scale[0], -
              34.0 * scale[1], -50.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 15.0 * scale[1], -24.0 * scale[0],
              15.0 * scale[1], -19.0 * scale[0], -3.0 * scale[1])
    Curveto_r(5.0 * scale[0], -20.0 * scale[1], -15.0 * scale[0], -
              28.0 * scale[1], -31.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 4.0 * scale[1], -18.0 * scale[0],
              9.0 * scale[1], -32.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 2.0 * scale[1], -24.0 *
              scale[0], -1.0 * scale[1], -18.0 * scale[0], -9.0 * scale[1])
    Curveto_r(4.0 * scale[0], -7.0 * scale[1], 3.0 * scale[0], -
              9.0 * scale[1], -4.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -13.0 * scale[0],
              2.0 * scale[1], -17.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -15.0 * scale[1], -37.0 *
              scale[0], -1.0 * scale[1], -31.0 * scale[0], 15.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], -1.0 * scale[0],
              14.0 * scale[1], -10.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0], -
              6.0 * scale[1], -10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(11.0 * scale[0], -29.0 * scale[1], -11.0 * scale[0], -
              54.0 * scale[1], -43.0 * scale[0], -48.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 5.0 * scale[1], -30.0 * scale[0],
              2.0 * scale[1], -35.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -17.0 * scale[1], 8.0 * scale[0], -
              34.0 * scale[1], 30.0 * scale[0], -34.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 21.0 * scale[0],
              11.0 * scale[1], 34.0 * scale[0], 25.0 * scale[1])
    Curveto_r(29.0 * scale[0], 31.0 * scale[1], 51.0 * scale[0],
              32.0 * scale[1], 76.0 * scale[0], 4.0 * scale[1])
    Curveto_r(17.0 * scale[0], -20.0 * scale[1], 26.0 * scale[0], -
              21.0 * scale[1], 109.0 * scale[0], -16.0 * scale[1])
    Curveto_r(59.0 * scale[0], 3.0 * scale[1], 118.0 * scale[0],
              15.0 * scale[1], 173.0 * scale[0], 33.0 * scale[1])
    Curveto_r(73.0 * scale[0], 24.0 * scale[1], 87.0 * scale[0],
              32.0 * scale[1], 108.0 * scale[0], 65.0 * scale[1])
    Curveto_r(24.0 * scale[0], 38.0 * scale[1], 25.0 * scale[0],
              39.0 * scale[1], 72.0 * scale[0], 32.0 * scale[1])
    Curveto_r(26.0 * scale[0], -3.0 * scale[1], 63.0 * scale[0], -
              14.0 * scale[1], 82.0 * scale[0], -23.0 * scale[1])
    Curveto_r(32.0 * scale[0], -16.0 * scale[1], 39.0 *
              scale[0], -17.0 * scale[1], 69.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 8.0 * scale[1], 50.0 * scale[0],
              14.0 * scale[1], 71.0 * scale[0], 14.0 * scale[1])
    Curveto_r(21.0 * scale[0], 0.0 * scale[1], 57.0 * scale[0],
              7.0 * scale[1], 80.0 * scale[0], 15.0 * scale[1])
    Curveto_r(37.0 * scale[0], 13.0 * scale[1], 46.0 * scale[0],
              13.0 * scale[1], 71.0 * scale[0], 1.0 * scale[1])
    Curveto_r(27.0 * scale[0], -13.0 * scale[1], 30.0 *
              scale[0], -13.0 * scale[1], 44.0 * scale[0], 7.0 * scale[1])
    Lineto_r(15.0 * scale[0], 21.0 * scale[1])
    Lineto_r(0.0 * scale[0], -23.0 * scale[1])
    Curveto_r(0.0 * scale[0], -45.0 * scale[1], 63.0 * scale[0], -
              67.0 * scale[1], 104.0 * scale[0], -36.0 * scale[1])
    Curveto_r(27.0 * scale[0], 21.0 * scale[1], 40.0 * scale[0],
              19.0 * scale[1], 73.0 * scale[0], -9.0 * scale[1])
    Lineto_r(28.0 * scale[0], -24.0 * scale[1])
    Lineto_r(36.0 * scale[0], 19.0 * scale[1])
    Curveto_r(36.0 * scale[0], 18.0 * scale[1], 39.0 * scale[0],
              18.0 * scale[1], 91.0 * scale[0], 0.0 * scale[1])
    Curveto_r(29.0 * scale[0], -10.0 * scale[1], 61.0 * scale[0], -
              22.0 * scale[1], 71.0 * scale[0], -26.0 * scale[1])
    Curveto_r(15.0 * scale[0], -6.0 * scale[1], 17.0 * scale[0],
              0.0 * scale[1], 17.0 * scale[0], 71.0 * scale[1])
    Curveto_r(0.0 * scale[0], 47.0 * scale[1], -4.0 * scale[0],
              74.0 * scale[1], -9.0 * scale[0], 66.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -18.0 * scale[1], -67.0 *
              scale[0], -12.0 * scale[1], -63.0 * scale[0], 7.0 * scale[1])
    Curveto_r(2.0 * scale[0], 10.0 * scale[1], -4.0 * scale[0],
              12.0 * scale[1], -25.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-55.0 * scale[0], -12.0 * scale[1], -89.0 *
              scale[0], -13.0 * scale[1], -136.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-35.0 * scale[0], 7.0 * scale[1], -52.0 * scale[0],
              7.0 * scale[1], -62.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -9.0 * scale[1], -15.0 *
              scale[0], -10.0 * scale[1], -15.0 * scale[0], -1.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -4.0 * scale[0],
              10.0 * scale[1], -9.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -1.0 * scale[1], -16.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -11.0 * scale[0],
              8.0 * scale[1], -19.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -3.0 * scale[1], -24.0 *
              scale[0], -1.0 * scale[1], -37.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 6.0 * scale[1], -32.0 * scale[0],
              5.0 * scale[1], -43.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -7.0 * scale[1], -17.0 *
              scale[0], -7.0 * scale[1], -12.0 * scale[0], 0.0 * scale[1])
    Curveto_r(10.0 * scale[0], 16.0 * scale[1], -61.0 * scale[0],
              27.0 * scale[1], -78.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -9.0 * scale[1], -16.0 *
              scale[0], -9.0 * scale[1], -22.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 9.0 * scale[1], -10.0 * scale[0],
              8.0 * scale[1], -19.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -21.0 * scale[1], -57.0 *
              scale[0], -17.0 * scale[1], -63.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 21.0 * scale[1], -31.0 * scale[0],
              23.0 * scale[1], -56.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto_r(204.0 * scale[0], -22.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -4.0 * scale[0], -
              15.0 * scale[1], -10.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0],
              7.0 * scale[1], -10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 5.0 * scale[0],
              15.0 * scale[1], 10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              7.0 * scale[1], 10.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto_r(-478.0 * scale[0], -80.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -5.0 * scale[0], -
              11.0 * scale[1], -11.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -2.0 * scale[1], -11.0 * scale[0],
              4.0 * scale[1], -11.0 * scale[0], 13.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], 5.0 * scale[0],
              15.0 * scale[1], 11.0 * scale[0], 13.0 * scale[1])
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 11.0 * scale[0], -
              8.0 * scale[1], 11.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(430.0 * scale[0], 1549.0 * scale[1], x, y)
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
    Moveto(3520.0 * scale[0], 1530.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 9.0 * scale[0], -
              10.0 * scale[1], 20.0 * scale[0], -10.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0],
              5.0 * scale[1], 20.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -9.0 * scale[0],
              10.0 * scale[1], -20.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0], -
              4.0 * scale[1], -20.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(3345.0 * scale[0], 1470.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(2030.0 * scale[0], 1460.0 * scale[1], x, y)
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
    Moveto(3243.0 * scale[0], 1459.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -5.0 * scale[1], -21.0 * scale[0], -
              11.0 * scale[1], -34.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-27.0 * scale[0], -2.0 * scale[1], -49.0 * scale[0], -
              15.0 * scale[1], -49.0 * scale[0], -30.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 7.0 * scale[0], -
              5.0 * scale[1], 15.0 * scale[0], 2.0 * scale[1])
    Curveto_r(8.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              10.0 * scale[1], 28.0 * scale[0], 7.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 27.0 * scale[0],
              6.0 * scale[1], 42.0 * scale[0], 19.0 * scale[1])
    Curveto_r(15.0 * scale[0], 13.0 * scale[1], 24.0 * scale[0],
              24.0 * scale[1], 19.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              5.0 * scale[1], -21.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(3053.0 * scale[0], 1428.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 20.0 * scale[0], -
              8.0 * scale[1], 29.0 * scale[0], -8.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0], -
              6.0 * scale[1], 21.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], -7.0 * scale[1], 6.0 *
              scale[0], -3.0 * scale[1], 6.0 * scale[0], 9.0 * scale[1])
    Curveto_r(1.0 * scale[0], 18.0 * scale[1], -4.0 * scale[0],
              21.0 * scale[1], -34.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -1.0 * scale[1], -30.0 *
              scale[0], -4.0 * scale[1], -22.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(3120.0 * scale[0], 1430.0 * scale[1], x, y)
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
    Moveto(3298.0 * scale[0], 1428.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -9.0 * scale[1], 15.0 *
              scale[0], -9.0 * scale[1], 24.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 9.0 * scale[1], 7.0 * scale[0],
              12.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -21.0 * scale[0], -
              3.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(2070.0 * scale[0], 1420.0 * scale[1], x, y)
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
    Moveto(2933.0 * scale[0], 1418.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -7.0 * scale[1], -7.0 * scale[0], -
              22.0 * scale[1], -3.0 * scale[0], -33.0 * scale[1])
    Curveto_r(7.0 * scale[0], -18.0 * scale[1], 8.0 * scale[0], -
              17.0 * scale[1], 15.0 * scale[0], 8.0 * scale[1])
    Curveto_r(8.0 * scale[0], 32.0 * scale[1], 3.0 * scale[0],
              43.0 * scale[1], -12.0 * scale[0], 25.0 * scale[1])
    te.end_fill()
    Moveto(2955.0 * scale[0], 1390.0 * scale[1], x, y)
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
    Moveto(2170.0 * scale[0], 1386.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], 7.0 * scale[0], -
              7.0 * scale[1], 16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 12.0 *
              scale[0], -2.0 * scale[1], 9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 10.0 * scale[1], -25.0 * scale[0],
              14.0 * scale[1], -25.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(2846.0 * scale[0], 1365.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -15.0 * scale[0], -
              15.0 * scale[1], -26.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -20.0 *
              scale[0], -4.0 * scale[1], -20.0 * scale[0], -9.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 12.0 * scale[0], -
              6.0 * scale[1], 31.0 * scale[0], -1.0 * scale[1])
    Curveto_r(18.0 * scale[0], 5.0 * scale[1], 36.0 * scale[0],
              7.0 * scale[1], 40.0 * scale[0], 4.0 * scale[1])
    Curveto_r(14.0 * scale[0], -8.0 * scale[1], 10.0 * scale[0],
              6.0 * scale[1], -5.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 12.0 * scale[1], -15.0 * scale[0],
              12.0 * scale[1], -20.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(2990.0 * scale[0], 1369.0 * scale[1], x, y)
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
    Moveto(2950.0 * scale[0], 1319.0 * scale[1], x, y)
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
    Moveto(2691.0 * scale[0], 1284.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(0.0 * scale[0], 630.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(0.0 * scale[0], -630.0 * scale[1])
    Lineto_r(2250.0 * scale[0], 0.0 * scale[1])
    Lineto_r(2250.0 * scale[0], 0.0 * scale[1])
    Lineto_r(0.0 * scale[0], 605.0 * scale[1])
    Lineto_r(0.0 * scale[0], 606.0 * scale[1])
    Lineto_r(-22.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-31.0 * scale[0], -29.0 * scale[1], -145.0 *
              scale[0], -82.0 * scale[1], -188.0 * scale[0], -87.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -3.0 * scale[1], -36.0 *
              scale[0], -8.0 * scale[1], -38.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -5.0 * scale[1], -15.0 *
              scale[0], -6.0 * scale[1], -30.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 4.0 * scale[1], -24.0 * scale[0],
              2.0 * scale[1], -12.0 * scale[0], -6.0 * scale[1])
    Curveto_r(12.0 * scale[0], -9.0 * scale[1], 11.0 * scale[0], -
              11.0 * scale[1], -8.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0],
              4.0 * scale[1], -17.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], -1.0 * scale[0],
              10.0 * scale[1], -9.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -7.0 * scale[0], -
              10.0 * scale[1], -15.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -4.0 * scale[0],
              10.0 * scale[1], -10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              7.0 * scale[1], -10.0 * scale[0], -15.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -5.0 * scale[0], -
              15.0 * scale[1], -11.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0],
              6.0 * scale[1], -6.0 * scale[0], 14.0 * scale[1])
    Curveto_r(4.0 * scale[0], 10.0 * scale[1], -14.0 * scale[0],
              16.0 * scale[1], -66.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-40.0 * scale[0], 7.0 * scale[1], -103.0 * scale[0],
              21.0 * scale[1], -142.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-38.0 * scale[0], 10.0 * scale[1], -83.0 * scale[0],
              20.0 * scale[1], -100.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 1.0 * scale[1], -34.0 * scale[0],
              5.0 * scale[1], -40.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 16.0 * scale[1], -144.0 * scale[0],
              33.0 * scale[1], -233.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-70.0 * scale[0], 0.0 * scale[1], -133.0 * scale[0], -
              8.0 * scale[1], -227.0 * scale[0], -28.0 * scale[1])
    Curveto_r(-71.0 * scale[0], -16.0 * scale[1], -133.0 *
              scale[0], -30.0 * scale[1], -136.0 * scale[0], -32.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -2.0 * scale[1], -35.0 *
              scale[0], -6.0 * scale[1], -70.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-70.0 * scale[0], -7.0 * scale[1], -142.0 * scale[0], -
              19.0 * scale[1], -234.0 * scale[0], -40.0 * scale[1])
    Curveto_r(-118.0 * scale[0], -28.0 * scale[1], -228.0 *
              scale[0], -45.0 * scale[1], -292.0 * scale[0], -45.0 * scale[1])
    Curveto_r(-64.0 * scale[0], 0.0 * scale[1], -251.0 * scale[0],
              33.0 * scale[1], -282.0 * scale[0], 50.0 * scale[1])
    Curveto_r(-42.0 * scale[0], 22.0 * scale[1], -221.0 * scale[0],
              61.0 * scale[1], -295.0 * scale[0], 64.0 * scale[1])
    Curveto_r(-75.0 * scale[0], 3.0 * scale[1], -225.0 * scale[0], -
              19.0 * scale[1], -272.0 * scale[0], -39.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -8.0 * scale[1], -35.0 * scale[0], -
              10.0 * scale[1], -97.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-23.0 * scale[0], -1.0 * scale[1], -36.0 *
              scale[0], -6.0 * scale[1], -32.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              10.0 * scale[1], -10.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0],
              4.0 * scale[1], -11.0 * scale[0], 8.0 * scale[1])
    Curveto_r(2.0 * scale[0], 4.0 * scale[1], -12.0 * scale[0],
              6.0 * scale[1], -32.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-62.0 * scale[0], -5.0 * scale[1], -81.0 * scale[0], -
              12.0 * scale[1], -78.0 * scale[0], -25.0 * scale[1])
    Curveto_r(1.0 * scale[0], -6.0 * scale[1], 1.0 * scale[0], -
              9.0 * scale[1], -1.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -10.0 * scale[0],
              4.0 * scale[1], -15.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -4.0 * scale[1], -8.0 *
              scale[0], -2.0 * scale[1], -4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(5.0 * scale[0], 8.0 * scale[1], -1.0 * scale[0],
              12.0 * scale[1], -14.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 * scale[0], -
              4.0 * scale[1], -14.0 * scale[0], -12.0 * scale[1])
    Curveto_r(6.0 * scale[0], -10.0 * scale[1], 4.0 * scale[0], -
              10.0 * scale[1], -8.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 9.0 * scale[1], -32.0 * scale[0],
              11.0 * scale[1], -65.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-127.0 * scale[0], -16.0 * scale[1], -400.0 *
              scale[0], -3.0 * scale[1], -543.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 6.0 * scale[1], -66.0 * scale[0],
              13.0 * scale[1], -80.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 3.0 * scale[1], -43.0 * scale[0],
              11.0 * scale[1], -65.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-59.0 * scale[0], 20.0 * scale[1], -112.0 * scale[0],
              36.0 * scale[1], -132.0 * scale[0], 42.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 2.0 * scale[1], -61.0 * scale[0],
              16.0 * scale[1], -113.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-133.0 * scale[0], 35.0 * scale[1], -244.0 * scale[0],
              54.0 * scale[1], -322.0 * scale[0], 54.0 * scale[1])
    Lineto_r(-68.0 * scale[0], 0.0 * scale[1])
    Lineto_r(0.0 * scale[0], -630.0 * scale[1])
    te.end_fill()
    Moveto_r(3420.0 * scale[0], 540.0 * scale[1], 0, 0)
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
    Moveto_r(50.0 * scale[0], 0.0 * scale[1], 0, 0)
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
    Moveto_r(-2910.0 * scale[0], -83.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 15.0 * scale[0],
              1.0 * scale[1], 34.0 * scale[0], 12.0 * scale[1])
    Curveto_r(47.0 * scale[0], 29.0 * scale[1], 52.0 * scale[0],
              26.0 * scale[1], 22.0 * scale[0], -13.0 * scale[1])
    Lineto_r(-26.0 * scale[0], -35.0 * scale[1])
    Lineto_r(30.0 * scale[0], -21.0 * scale[1])
    Curveto_r(41.0 * scale[0], -29.0 * scale[1], 38.0 * scale[0], -
              43.0 * scale[1], -6.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 8.0 * scale[1], -38.0 * scale[0],
              15.0 * scale[1], -39.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              16.0 * scale[1], -15.0 * scale[0], -35.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -48.0 * scale[1], -34.0 *
              scale[0], -45.0 * scale[1], -27.0 * scale[0], 5.0 * scale[1])
    Lineto_r(5.0 * scale[0], 40.0 * scale[1])
    Lineto_r(-39.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-49.0 * scale[0], 0.0 * scale[1], -51.0 * scale[0],
              17.0 * scale[1], -3.0 * scale[0], 26.0 * scale[1])
    Curveto_r(38.0 * scale[0], 7.0 * scale[1], 37.0 * scale[0],
              3.0 * scale[1], 18.0 * scale[0], 79.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 15.0 * scale[1], 1.0 * scale[0],
              13.0 * scale[1], 20.0 * scale[0], -10.0 * scale[1])
    Curveto_r(14.0 * scale[0], -16.0 * scale[1], 26.0 * scale[0], -
              34.0 * scale[1], 26.0 * scale[0], -38.0 * scale[1])
    te.end_fill()
    Moveto_r(2824.0 * scale[0], 38.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -8.0 * scale[1], -11.0 * scale[0], -
              15.0 * scale[1], -16.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], 2.0 * scale[0], 15.0 * scale[1])
    Curveto_r(7.0 * scale[0], 8.0 * scale[1], 14.0 * scale[0],
              15.0 * scale[1], 16.0 * scale[0], 15.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 1.0 * scale[0], -
              7.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto_r(-1523.0 * scale[0], -17.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -4.0 * scale[1], -20.0 * scale[0], -
              12.0 * scale[1], -17.0 * scale[0], -17.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], -3.0 * scale[0], -
              11.0 * scale[1], -14.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -3.0 * scale[1], -20.0 *
              scale[0], -1.0 * scale[1], -20.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 15.0 * scale[1], 52.0 * scale[0],
              50.0 * scale[1], 63.0 * scale[0], 43.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 1.0 * scale[0], -
              10.0 * scale[1], -12.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto_r(1889.0 * scale[0], 2.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -5.0 * scale[1], -22.0 *
              scale[0], -9.0 * scale[1], -30.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0],
              3.0 * scale[1], 5.0 * scale[0], 9.0 * scale[1])
    Curveto_r(27.0 * scale[0], 12.0 * scale[1], 43.0 * scale[0],
              12.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto_r(83.0 * scale[0], -3.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -7.0 * scale[1], -3.0 * scale[0], -
              13.0 * scale[1], -14.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -1.0 * scale[1], -16.0 * scale[0],
              1.0 * scale[1], -6.0 * scale[0], 12.0 * scale[1])
    Curveto_r(15.0 * scale[0], 18.0 * scale[1], 14.0 * scale[0],
              18.0 * scale[1], 20.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto_r(-2066.0 * scale[0], -3.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 17.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(2157.0 * scale[0], -6.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], -9.0 * scale[0], -
              8.0 * scale[1], -15.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0],
              4.0 * scale[1], -9.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 7.0 * scale[0],
              9.0 * scale[1], 15.0 * scale[0], 9.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0], -
              4.0 * scale[1], 9.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto_r(76.0 * scale[0], -8.0 * scale[1], 0, 0)
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
    Moveto_r(-2333.0 * scale[0], -22.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -6.0 *
              scale[0], -5.0 * scale[1], -6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 11.0 * scale[1], 2.0 * scale[0],
              17.0 * scale[1], 5.0 * scale[0], 13.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 4.0 * scale[0], -
              12.0 * scale[1], 1.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto_r(2404.0 * scale[0], 12.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(18.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0], -
              16.0 * scale[1], -10.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -1.0 * scale[1], -22.0 * scale[0],
              5.0 * scale[1], -25.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 11.0 * scale[1], -2.0 * scale[0],
              14.0 * scale[1], 10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 20.0 * scale[0], -
              6.0 * scale[1], 25.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto_r(-184.0 * scale[0], -22.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -6.0 *
              scale[0], -5.0 * scale[1], -6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 11.0 * scale[1], 2.0 * scale[0],
              17.0 * scale[1], 5.0 * scale[0], 13.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 4.0 * scale[0], -
              12.0 * scale[1], 1.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto_r(-1867.0 * scale[0], 2.0 * scale[1], 0, 0)
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
    Moveto_r(-1000.0 * scale[0], -15.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], -19.0 *
              scale[0], -12.0 * scale[1], -23.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 9.0 * scale[1], -1.0 * scale[0],
              12.0 * scale[1], 9.0 * scale[0], 8.0 * scale[1])
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 14.0 * scale[0], -
              7.0 * scale[1], 14.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto_r(140.0 * scale[0], -3.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -3.0 * scale[1], -7.0 * scale[0], -
              13.0 * scale[1], -16.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -15.0 * scale[1], -18.0 *
              scale[0], -16.0 * scale[1], -30.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 19.0 * scale[1], -18.0 * scale[0],
              31.0 * scale[1], 1.0 * scale[0], 15.0 * scale[1])
    Curveto_r(12.0 * scale[0], -10.0 * scale[1], 19.0 *
              scale[0], -10.0 * scale[1], 27.0 * scale[0], -2.0 * scale[1])
    Curveto_r(9.0 * scale[0], 9.0 * scale[1], 9.0 * scale[0],
              12.0 * scale[1], 0.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0],
              4.0 * scale[1], -12.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 7.0 * scale[0],
              7.0 * scale[1], 15.0 * scale[0], 4.0 * scale[1])
    Curveto_r(8.0 * scale[0], -4.0 * scale[1], 15.0 * scale[0], -
              9.0 * scale[1], 15.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto_r(94.0 * scale[0], 3.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(11.0 * scale[0], -8.0 * scale[1], 15.0 * scale[0], -
              15.0 * scale[1], 9.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -43.0 * scale[0],
              12.0 * scale[1], -43.0 * scale[0], 21.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], 12.0 * scale[0],
              11.0 * scale[1], 34.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto_r(2771.0 * scale[0], 5.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -6.0 * scale[1], 0.0 * scale[0], -
              16.0 * scale[1], -7.0 * scale[0], -24.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -11.0 * scale[1], -17.0 *
              scale[0], -11.0 * scale[1], -33.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 12.0 * scale[1], -17.0 * scale[0],
              14.0 * scale[1], -2.0 * scale[0], 14.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0],
              5.0 * scale[1], 17.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], 17.0 * scale[0],
              13.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto_r(110.0 * scale[0], 0.0 * scale[1], 0, 0)
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
    Moveto_r(-3275.0 * scale[0], -10.0 * scale[1], 0, 0)
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
    Moveto_r(440.0 * scale[0], 6.0 * scale[1], 0, 0)
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
    Moveto_r(-250.0 * scale[0], -40.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-14.0 * scale[0], -14.0 * scale[1], -32.0 * scale[0],
              3.0 * scale[1], -17.0 * scale[0], 18.0 * scale[1])
    Curveto_r(9.0 * scale[0], 10.0 * scale[1], 14.0 * scale[0],
              11.0 * scale[1], 19.0 * scale[0], 2.0 * scale[1])
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 3.0 * scale[0], -
              15.0 * scale[1], -2.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto_r(377.0 * scale[0], 18.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 17.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(2473.0 * scale[0], -3.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 3.0 * scale[0], -
              18.0 * scale[1], 6.0 * scale[0], -28.0 * scale[1])
    Curveto_r(5.0 * scale[0], -15.0 * scale[1], 3.0 * scale[0], -
              15.0 * scale[1], -7.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 11.0 * scale[1], -17.0 * scale[0],
              23.0 * scale[1], -23.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 5.0 * scale[1], -4.0 * scale[0],
              8.0 * scale[1], 7.0 * scale[0], 8.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0], -
              4.0 * scale[1], 17.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto_r(375.0 * scale[0], -1.0 * scale[1], 0, 0)
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
    Moveto_r(80.0 * scale[0], 0.0 * scale[1], 0, 0)
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
    Moveto_r(-3516.0 * scale[0], -21.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -10.0 * scale[1], -23.0 *
              scale[0], -4.0 * scale[1], -14.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 11.0 * scale[0],
              8.0 * scale[1], 17.0 * scale[0], 5.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 5.0 * scale[0], -
              9.0 * scale[1], -3.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto_r(419.0 * scale[0], 9.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -6.0 * scale[1], -10.0 * scale[0], -
              14.0 * scale[1], -16.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -10.0 * scale[0],
              2.0 * scale[1], -6.0 * scale[0], 12.0 * scale[1])
    Curveto_r(7.0 * scale[0], 18.0 * scale[1], 28.0 * scale[0],
              22.0 * scale[1], 22.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto_r(532.0 * scale[0], -3.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -9.0 * scale[1], -15.0 * scale[0], -
              13.0 * scale[1], -17.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 7.0 * scale[1], 7.0 * scale[0],
              26.0 * scale[1], 19.0 * scale[0], 26.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 6.0 * scale[0], -
              6.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto_r(2300.0 * scale[0], 5.0 * scale[1], 0, 0)
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
    Moveto_r(-3120.0 * scale[0], -14.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -7.0 * scale[1], -13.0 *
              scale[0], -7.0 * scale[1], -20.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 6.0 * scale[1], -3.0 * scale[0],
              10.0 * scale[1], 10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0], -
              4.0 * scale[1], 10.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto_r(377.0 * scale[0], -8.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -6.0 *
              scale[0], -5.0 * scale[1], -6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 11.0 * scale[1], 2.0 * scale[0],
              17.0 * scale[1], 5.0 * scale[0], 13.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 4.0 * scale[0], -
              12.0 * scale[1], 1.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto_r(103.0 * scale[0], 18.0 * scale[1], 0, 0)
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
    Moveto_r(122.0 * scale[0], -5.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(8.0 * scale[0], 11.0 * scale[1], 9.0 * scale[0],
              11.0 * scale[1], 6.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -16.0 * scale[1], -22.0 *
              scale[0], -18.0 * scale[1], -24.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 8.0 * scale[1], -1.0 * scale[0],
              7.0 * scale[1], 3.0 * scale[0], 0.0 * scale[1])
    Curveto_r(4.0 * scale[0], -8.0 * scale[1], 8.0 * scale[0], -
              7.0 * scale[1], 15.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto_r(74.0 * scale[0], -18.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -7.0 * scale[1], -26.0 * scale[0],
              7.0 * scale[1], -26.0 * scale[0], 19.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 6.0 * scale[0],
              6.0 * scale[1], 15.0 * scale[0], -2.0 * scale[1])
    Curveto_r(9.0 * scale[0], -7.0 * scale[1], 13.0 * scale[0], -
              15.0 * scale[1], 11.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto_r(74.0 * scale[0], 17.0 * scale[1], 0, 0)
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
    Moveto_r(30.0 * scale[0], 0.0 * scale[1], 0, 0)
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
    Moveto_r(1950.0 * scale[0], 0.0 * scale[1], 0, 0)
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
    Moveto_r(-2530.0 * scale[0], -4.0 * scale[1], 0, 0)
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
    Moveto_r(40.0 * scale[0], -6.0 * scale[1], 0, 0)
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
    Moveto_r(102.0 * scale[0], -7.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -4.0 * scale[1], -8.0 *
              scale[0], -9.0 * scale[1], 5.0 * scale[0], -19.0 * scale[1])
    Curveto_r(17.0 * scale[0], -13.0 * scale[1], 17.0 * scale[0], -
              13.0 * scale[1], -2.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 0.0 * scale[1], -45.0 * scale[0],
              17.0 * scale[1], -45.0 * scale[0], 31.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], 42.0 * scale[0],
              17.0 * scale[1], 50.0 * scale[0], 11.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], -1.0 * scale[0], -
              7.0 * scale[1], -8.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto_r(2863.0 * scale[0], 7.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 16.0 * scale[0], -
              10.0 * scale[1], 28.0 * scale[0], -10.0 * scale[1])
    Curveto_r(15.0 * scale[0], 0.0 * scale[1], 18.0 * scale[0], -
              3.0 * scale[1], 10.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -9.0 * scale[1], -19.0 *
              scale[0], -6.0 * scale[1], -39.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 11.0 * scale[1], -22.0 * scale[0],
              21.0 * scale[1], -16.0 * scale[0], 21.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0], -
              4.0 * scale[1], 17.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto_r(-2764.0 * scale[0], -10.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0], -
              4.0 * scale[1], 9.0 * scale[0], -9.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -11.0 * scale[0], -
              8.0 * scale[1], -25.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -25.0 * scale[0],
              7.0 * scale[1], -25.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 6.0 * scale[0],
              11.0 * scale[1], 16.0 * scale[0], 7.0 * scale[1])
    Curveto_r(9.0 * scale[0], -3.0 * scale[1], 20.0 * scale[0], -
              6.0 * scale[1], 25.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto_r(94.0 * scale[0], 0.0 * scale[1], 0, 0)
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
    Moveto_r(-457.0 * scale[0], -18.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(8.0 * scale[0], -7.0 * scale[1], 11.0 * scale[0], -
              16.0 * scale[1], 8.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -3.0 * scale[1], -11.0 * scale[0],
              0.0 * scale[1], -15.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              10.0 * scale[1], -15.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -13.0 *
              scale[0], -9.0 * scale[1], -21.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 5.0 * scale[1], -12.0 * scale[0],
              9.0 * scale[1], -2.0 * scale[0], 19.0 * scale[1])
    Curveto_r(14.0 * scale[0], 15.0 * scale[1], 26.0 * scale[0],
              15.0 * scale[1], 45.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto_r(65.0 * scale[0], 4.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -11.0 * scale[1], 14.0 * scale[0], -
              12.0 * scale[1], 42.0 * scale[0], -6.0 * scale[1])
    Curveto_r(33.0 * scale[0], 8.0 * scale[1], 35.0 * scale[0],
              7.0 * scale[1], 22.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -10.0 * scale[1], -12.0 * scale[0], -
              23.0 * scale[1], -10.0 * scale[0], -29.0 * scale[1])
    Curveto_r(3.0 * scale[0], -7.0 * scale[1], 0.0 * scale[0], -
              13.0 * scale[1], -6.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0], -
              8.0 * scale[1], -11.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -16.0 * scale[1], -2.0 *
              scale[0], -16.0 * scale[1], -12.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 15.0 * scale[1], -8.0 * scale[0],
              21.0 * scale[1], 0.0 * scale[0], 24.0 * scale[1])
    Curveto_r(7.0 * scale[0], 2.0 * scale[1], 12.0 * scale[0],
              11.0 * scale[1], 12.0 * scale[0], 19.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], -3.0 * scale[0],
              13.0 * scale[1], -14.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -9.0 * scale[1], -15.0 *
              scale[0], -9.0 * scale[1], -19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 10.0 * scale[1], -8.0 * scale[0],
              10.0 * scale[1], -16.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -9.0 * scale[1], -7.0 * scale[0], -
              18.0 * scale[1], -1.0 * scale[0], -24.0 * scale[1])
    Curveto_r(6.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              16.0 * scale[1], -7.0 * scale[0], -28.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -17.0 * scale[1], -15.0 *
              scale[0], -18.0 * scale[1], 0.0 * scale[0], -18.0 * scale[1])
    Curveto_r(18.0 * scale[0], 0.0 * scale[1], 23.0 * scale[0], -
              15.0 * scale[1], 8.0 * scale[0], -24.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -14.0 * scale[0],
              1.0 * scale[1], -21.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 8.0 * scale[1], -20.0 * scale[0],
              15.0 * scale[1], -29.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0],
              3.0 * scale[1], 7.0 * scale[0], 9.0 * scale[1])
    Curveto_r(14.0 * scale[0], 6.0 * scale[1], 22.0 * scale[0],
              18.0 * scale[1], 22.0 * scale[0], 32.0 * scale[1])
    Curveto_r(0.0 * scale[0], 54.0 * scale[1], 21.0 * scale[0],
              87.0 * scale[1], 33.0 * scale[0], 54.0 * scale[1])
    te.end_fill()
    Moveto_r(131.0 * scale[0], 5.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -9.0 * scale[1], -35.0 * scale[0], -
              24.0 * scale[1], -43.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 5.0 * scale[1], 18.0 * scale[0],
              24.0 * scale[1], 31.0 * scale[0], 24.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0], -
              4.0 * scale[1], 12.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto_r(669.0 * scale[0], -14.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -8.0 * scale[1], -8.0 *
              scale[0], -8.0 * scale[1], -10.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 6.0 * scale[1], -14.0 * scale[0],
              9.0 * scale[1], -26.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -4.0 * scale[1], -21.0 *
              scale[0], -4.0 * scale[1], -2.0 * scale[0], 4.0 * scale[1])
    Curveto_r(24.0 * scale[0], 11.0 * scale[1], 47.0 * scale[0],
              4.0 * scale[1], 38.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto_r(2226.0 * scale[0], 9.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(19.0 * scale[0], -23.0 * scale[1], -4.0 * scale[0], -
              28.0 * scale[1], -29.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 19.0 * scale[1], -22.0 * scale[0],
              20.0 * scale[1], -3.0 * scale[0], 20.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 26.0 * scale[0], -
              6.0 * scale[1], 32.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto_r(-2779.0 * scale[0], -6.0 * scale[1], 0, 0)
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
    Moveto_r(2688.0 * scale[0], -4.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -8.0 * scale[1], -15.0 * scale[0], -
              12.0 * scale[1], -17.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 6.0 * scale[1], 10.0 * scale[0],
              25.0 * scale[1], 20.0 * scale[0], 25.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 4.0 * scale[0], -
              6.0 * scale[1], -3.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto_r(303.0 * scale[0], -9.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -9.0 * scale[1], -11.0 *
              scale[0], -8.0 * scale[1], -5.0 * scale[0], 6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 10.0 * scale[1], 9.0 * scale[0],
              15.0 * scale[1], 12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 0.0 * scale[0], -
              11.0 * scale[1], -7.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto_r(-451.0 * scale[0], -3.0 * scale[1], 0, 0)
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
    Moveto_r(110.0 * scale[0], 1.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -4.0 * scale[0], -
              15.0 * scale[1], -10.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0],
              7.0 * scale[1], -10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 5.0 * scale[0],
              15.0 * scale[1], 10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              7.0 * scale[1], 10.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto_r(-2750.0 * scale[0], -5.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -8.0 * scale[0], -
              10.0 * scale[1], -17.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0],
              2.0 * scale[1], -3.0 * scale[0], 10.0 * scale[1])
    Curveto_r(19.0 * scale[0], 12.0 * scale[1], 20.0 * scale[0],
              12.0 * scale[1], 20.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto_r(30.0 * scale[0], -7.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], 2.0 * scale[0], -
              15.0 * scale[1], 8.0 * scale[0], -5.0 * scale[1])
    Curveto_r(6.0 * scale[0], 8.0 * scale[1], 9.0 * scale[0],
              1.0 * scale[1], 9.0 * scale[0], -20.0 * scale[1])
    Curveto_r(0.0 * scale[0], -18.0 * scale[1], -2.0 * scale[0], -
              27.0 * scale[1], -5.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 6.0 * scale[1], -8.0 * scale[0],
              10.0 * scale[1], -13.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -9.0 *
              scale[0], -2.0 * scale[1], -10.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], -2.0 * scale[0],
              18.0 * scale[1], -5.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 12.0 * scale[1], 1.0 * scale[0],
              22.0 * scale[1], 6.0 * scale[0], 22.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              8.0 * scale[1], 10.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto_r(2810.0 * scale[0], -5.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -18.0 * scale[1], -2.0 * scale[0], -
              20.0 * scale[1], -9.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 8.0 * scale[1], -7.0 * scale[0],
              18.0 * scale[1], -5.0 * scale[0], 22.0 * scale[1])
    Curveto_r(9.0 * scale[0], 14.0 * scale[1], 14.0 * scale[0],
              9.0 * scale[1], 14.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto_r(100.0 * scale[0], 7.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -15.0 * scale[1], -30.0 *
              scale[0], -12.0 * scale[1], -30.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 10.0 * scale[0],
              9.0 * scale[1], 21.0 * scale[0], 9.0 * scale[1])
    Curveto_r(18.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0], -
              2.0 * scale[1], 9.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto_r(45.0 * scale[0], 6.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 2.0 * scale[0], -
              12.0 * scale[1], -3.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -9.0 * scale[0],
              1.0 * scale[1], -9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], 3.0 * scale[0],
              19.0 * scale[1], 12.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto_r(-3025.0 * scale[0], -11.0 * scale[1], 0, 0)
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
    Moveto_r(313.0 * scale[0], -5.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -8.0 * scale[1], 2.0 * scale[0], -
              17.0 * scale[1], -3.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -4.0 * scale[1], -10.0 *
              scale[0], -4.0 * scale[1], -10.0 * scale[0], -1.0 * scale[1])
    Curveto_r(0.0 * scale[0], 2.0 * scale[1], -3.0 * scale[0],
              11.0 * scale[1], -6.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -2.0 * scale[0],
              16.0 * scale[1], 4.0 * scale[0], 16.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0], -
              7.0 * scale[1], 15.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto_r(86.0 * scale[0], -6.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -12.0 * scale[1], 1.0 * scale[0], -
              12.0 * scale[1], -14.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 14.0 * scale[1], -18.0 * scale[0],
              13.0 * scale[1], -12.0 * scale[0], -15.0 * scale[1])
    Curveto_r(5.0 * scale[0], -29.0 * scale[1], 4.0 * scale[0], -
              31.0 * scale[1], -23.0 * scale[0], -30.0 * scale[1])
    Curveto_r(-39.0 * scale[0], 1.0 * scale[1], -47.0 * scale[0],
              11.0 * scale[1], -15.0 * scale[0], 19.0 * scale[1])
    Curveto_r(17.0 * scale[0], 4.0 * scale[1], 25.0 * scale[0],
              12.0 * scale[1], 21.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 14.0 * scale[1], 11.0 * scale[0],
              25.0 * scale[1], 28.0 * scale[0], 21.0 * scale[1])
    Curveto_r(6.0 * scale[0], -1.0 * scale[1], 12.0 * scale[0], -
              9.0 * scale[1], 15.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto_r(2652.0 * scale[0], -10.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -13.0 * scale[1], -10.0 * scale[0], -
              19.0 * scale[1], -10.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 15.0 * scale[1], 10.0 * scale[0],
              45.0 * scale[1], 15.0 * scale[0], 40.0 * scale[1])
    Curveto_r(3.0 * scale[0], -2.0 * scale[1], 0.0 * scale[0], -
              15.0 * scale[1], -5.0 * scale[0], -28.0 * scale[1])
    te.end_fill()
    Moveto_r(-3251.0 * scale[0], 13.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -7.0 * scale[0], -
              9.0 * scale[1], -15.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0],
              4.0 * scale[1], -15.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], 7.0 * scale[0],
              8.0 * scale[1], 15.0 * scale[0], 8.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0], -
              4.0 * scale[1], 15.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto_r(387.0 * scale[0], -9.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -10.0 * scale[1], -23.0 *
              scale[0], -12.0 * scale[1], -36.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-29.0 * scale[0], 9.0 * scale[1], -20.0 * scale[0],
              20.0 * scale[1], 19.0 * scale[0], 21.0 * scale[1])
    Curveto_r(28.0 * scale[0], 1.0 * scale[1], 30.0 * scale[0], -
              1.0 * scale[1], 17.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto_r(83.0 * scale[0], 13.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], -9.0 * scale[0], -
              6.0 * scale[1], -20.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -3.0 * scale[1], -20.0 *
              scale[0], -1.0 * scale[1], -20.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 9.0 * scale[0],
              9.0 * scale[1], 20.0 * scale[0], 9.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0], -
              2.0 * scale[1], 20.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto_r(2360.0 * scale[0], -6.0 * scale[1], 0, 0)
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
    Moveto_r(-2207.0 * scale[0], -25.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -13.0 * scale[1], -13.0 * scale[0], -
              30.0 * scale[1], -22.0 * scale[0], -37.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -12.0 * scale[1], -15.0 *
              scale[0], -11.0 * scale[1], -2.0 * scale[0], 5.0 * scale[1])
    Curveto_r(8.0 * scale[0], 9.0 * scale[1], 11.0 * scale[0],
              20.0 * scale[1], 8.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              12.0 * scale[1], 4.0 * scale[0], 20.0 * scale[1])
    Curveto_r(16.0 * scale[0], 18.0 * scale[1], 17.0 * scale[0],
              17.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto_r(-593.0 * scale[0], 5.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -7.0 * scale[0], -
              10.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              4.0 * scale[1], -9.0 * scale[0], -10.0 * scale[1])
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              10.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0],
              28.0 * scale[1], 7.0 * scale[0], 33.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 18.0 * scale[0],
              5.0 * scale[1], 20.0 * scale[0], 6.0 * scale[1])
    Curveto_r(1.0 * scale[0], 0.0 * scale[1], 2.0 * scale[0], -
              3.0 * scale[1], 2.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto_r(300.0 * scale[0], -25.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -6.0 * scale[0], -
              15.0 * scale[1], -12.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -3.0 * scale[1], -10.0 *
              scale[0], -11.0 * scale[1], -2.0 * scale[0], -34.0 * scale[1])
    Curveto_r(11.0 * scale[0], -29.0 * scale[1], 10.0 * scale[0], -
              30.0 * scale[1], -13.0 * scale[0], -30.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -21.0 * scale[0],
              2.0 * scale[1], -12.0 * scale[0], 13.0 * scale[1])
    Curveto_r(10.0 * scale[0], 13.0 * scale[1], 6.0 * scale[0],
              18.0 * scale[1], -13.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -1.0 * scale[1], -12.0 * scale[0],
              5.0 * scale[1], -19.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 23.0 * scale[1], 4.0 * scale[0],
              42.0 * scale[1], 27.0 * scale[0], 23.0 * scale[1])
    Curveto_r(10.0 * scale[0], -8.0 * scale[1], 15.0 *
              scale[0], -9.0 * scale[1], 11.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], -2.0 * scale[0],
              15.0 * scale[1], 4.0 * scale[0], 18.0 * scale[1])
    Curveto_r(5.0 * scale[0], 4.0 * scale[1], 8.0 * scale[0],
              14.0 * scale[1], 4.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 13.0 * scale[1], -3.0 * scale[0],
              14.0 * scale[1], 10.0 * scale[0], 3.0 * scale[1])
    Curveto_r(8.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              18.0 * scale[1], 15.0 * scale[0], -25.0 * scale[1])
    te.end_fill()
    Moveto_r(130.0 * scale[0], 23.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -4.0 * scale[0], -
              6.0 * scale[1], -10.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0], -
              4.0 * scale[1], -10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(0.0 * scale[0], -22.0 * scale[1], 0.0 * scale[0], -
              22.0 * scale[1], -15.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 26.0 * scale[1], -19.0 * scale[0],
              29.0 * scale[1], 10.0 * scale[0], 30.0 * scale[1])
    Curveto_r(14.0 * scale[0], 1.0 * scale[1], 25.0 * scale[0], -
              2.0 * scale[1], 25.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto_r(260.0 * scale[0], 3.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -4.0 * scale[0], -
              13.0 * scale[1], -10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -10.0 * scale[0],
              1.0 * scale[1], -10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], 5.0 * scale[0],
              16.0 * scale[1], 10.0 * scale[0], 16.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              4.0 * scale[1], 10.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto_r(2175.0 * scale[0], -1.0 * scale[1], 0, 0)
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
    Moveto_r(85.0 * scale[0], 6.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], -9.0 * scale[0], -
              6.0 * scale[1], -20.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -3.0 * scale[1], -18.0 *
              scale[0], -1.0 * scale[1], -14.0 * scale[0], 4.0 * scale[1])
    Curveto_r(5.0 * scale[0], 9.0 * scale[1], 34.0 * scale[0],
              13.0 * scale[1], 34.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto_r(-2870.0 * scale[0], -16.0 * scale[1], 0, 0)
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
    Moveto_r(130.0 * scale[0], 0.0 * scale[1], 0, 0)
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
    Moveto_r(565.0 * scale[0], 0.0 * scale[1], 0, 0)
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
    Moveto_r(-825.0 * scale[0], -21.0 * scale[1], 0, 0)
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
    Moveto_r(700.0 * scale[0], 11.0 * scale[1], 0, 0)
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
    Moveto_r(70.0 * scale[0], 0.0 * scale[1], 0, 0)
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
    Moveto_r(-570.0 * scale[0], -15.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -4.0 * scale[0], -
              15.0 * scale[1], -9.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -22.0 * scale[0],
              16.0 * scale[1], -14.0 * scale[0], 24.0 * scale[1])
    Curveto_r(11.0 * scale[0], 11.0 * scale[1], 23.0 * scale[0],
              6.0 * scale[1], 23.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto_r(722.0 * scale[0], -7.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -7.0 * scale[1], -12.0 *
              scale[0], -8.0 * scale[1], -12.0 * scale[0], -2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], 12.0 * scale[0],
              26.0 * scale[1], 19.0 * scale[0], 19.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], -1.0 * scale[0], -
              11.0 * scale[1], -7.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto_r(-693.0 * scale[0], -5.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -10.0 * scale[1], -18.0 * scale[0], -
              21.0 * scale[1], -23.0 * scale[0], -24.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -14.0 * scale[1], 6.0 * scale[0], -
              30.0 * scale[1], 35.0 * scale[0], -24.0 * scale[1])
    Curveto_r(19.0 * scale[0], 4.0 * scale[1], 29.0 * scale[0],
              3.0 * scale[1], 29.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -7.0 * scale[0], -
              10.0 * scale[1], -15.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 6.0 * scale[1], -20.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -20.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 14.0 *
              scale[0], -2.0 * scale[1], 16.0 * scale[0], 4.0 * scale[1])
    Curveto_r(6.0 * scale[0], 19.0 * scale[1], 22.0 * scale[0],
              14.0 * scale[1], 22.0 * scale[0], -8.0 * scale[1])
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], -5.0 * scale[0], -
              19.0 * scale[1], -30.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 4.0 * scale[1], -30.0 * scale[0],
              2.0 * scale[1], -30.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 6.0 * scale[0], -
              17.0 * scale[1], 13.0 * scale[0], -20.0 * scale[1])
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 8.0 * scale[0], -
              8.0 * scale[1], 4.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -5.0 * scale[1], -12.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 8.0 * scale[1], -15.0 * scale[0],
              15.0 * scale[1], -21.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -23.0 * scale[0],
              24.0 * scale[1], -5.0 * scale[0], 31.0 * scale[1])
    Curveto_r(12.0 * scale[0], 5.0 * scale[1], 9.0 * scale[0],
              12.0 * scale[1], -16.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 16.0 * scale[1], -27.0 * scale[0],
              32.0 * scale[1], -23.0 * scale[0], 36.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 10.0 * scale[0],
              0.0 * scale[1], 14.0 * scale[0], -7.0 * scale[1])
    Curveto_r(7.0 * scale[0], -10.0 * scale[1], 13.0 *
              scale[0], -7.0 * scale[1], 27.0 * scale[0], 13.0 * scale[1])
    Curveto_r(11.0 * scale[0], 14.0 * scale[1], 23.0 * scale[0],
              26.0 * scale[1], 28.0 * scale[0], 26.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 2.0 * scale[0], -
              8.0 * scale[1], -5.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto_r(188.0 * scale[0], 6.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -6.0 * scale[1], 9.0 * scale[0], -
              18.0 * scale[1], 6.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -11.0 * scale[1], -8.0 *
              scale[0], -11.0 * scale[1], -20.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 9.0 * scale[1], -24.0 * scale[0],
              12.0 * scale[1], -37.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -6.0 * scale[1], -21.0 *
              scale[0], -6.0 * scale[1], -2.0 * scale[0], 9.0 * scale[1])
    Curveto_r(23.0 * scale[0], 19.0 * scale[1], 38.0 * scale[0],
              20.0 * scale[1], 53.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto_r(83.0 * scale[0], 7.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], -19.0 * scale[0], -
              15.0 * scale[1], -25.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], 1.0 * scale[0],
              10.0 * scale[1], 9.0 * scale[0], 10.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0], -
              2.0 * scale[1], 16.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto_r(44.0 * scale[0], -12.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -8.0 * scale[1], 16.0 * scale[0], -
              22.0 * scale[1], 16.0 * scale[0], -31.0 * scale[1])
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 6.0 * scale[0], -
              13.0 * scale[1], 15.0 * scale[0], -9.0 * scale[1])
    Curveto_r(17.0 * scale[0], 6.0 * scale[1], 18.0 * scale[0],
              4.0 * scale[1], 9.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -23.0 * scale[1], -22.0 *
              scale[0], -20.0 * scale[1], -29.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 12.0 * scale[1], -17.0 * scale[0],
              32.0 * scale[1], -28.0 * scale[0], 45.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 25.0 * scale[1], -7.0 * scale[0],
              31.0 * scale[1], 17.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto_r(-694.0 * scale[0], 2.0 * scale[1], 0, 0)
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
    Moveto_r(3113.0 * scale[0], -34.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -9.0 * scale[1], 6.0 * scale[0], -
              11.0 * scale[1], -7.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 3.0 * scale[1], -16.0 * scale[0],
              16.0 * scale[1], -15.0 * scale[0], 28.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], 10.0 * scale[0], -
              21.0 * scale[1], 16.0 * scale[0], -28.0 * scale[1])
    te.end_fill()
    Moveto_r(-3248.0 * scale[0], 18.0 * scale[1], 0, 0)
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
    Moveto_r(392.0 * scale[0], -52.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -33.0 * scale[1], -1.0 * scale[0], -
              32.0 * scale[1], -21.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 8.0 * scale[1], -13.0 * scale[0],
              20.0 * scale[1], -10.0 * scale[0], 26.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], 10.0 * scale[0],
              5.0 * scale[1], 15.0 * scale[0], -3.0 * scale[1])
    Curveto_r(7.0 * scale[0], -11.0 * scale[1], 9.0 * scale[0], -
              11.0 * scale[1], 9.0 * scale[0], -1.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], -11.0 * scale[0],
              18.0 * scale[1], -25.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -25.0 * scale[0],
              15.0 * scale[1], -25.0 * scale[0], 19.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 13.0 * scale[0],
              0.0 * scale[1], 29.0 * scale[0], -9.0 * scale[1])
    Curveto_r(23.0 * scale[0], -13.0 * scale[1], 29.0 * scale[0], -
              23.0 * scale[1], 28.0 * scale[0], -44.0 * scale[1])
    te.end_fill()
    Moveto_r(593.0 * scale[0], 49.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 8.0 * scale[0],
              0.0 * scale[1], -3.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -9.0 * scale[1], -22.0 *
              scale[0], -9.0 * scale[1], -33.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 10.0 * scale[1], -14.0 * scale[0],
              10.0 * scale[1], -14.0 * scale[0], 0.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -3.0 * scale[0], -
              11.0 * scale[1], -6.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 12.0 * scale[1], 7.0 * scale[0],
              27.0 * scale[1], 24.0 * scale[0], 18.0 * scale[1])
    Curveto_r(9.0 * scale[0], -4.0 * scale[1], 24.0 * scale[0], -
              6.0 * scale[1], 32.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto_r(50.0 * scale[0], 3.0 * scale[1], 0, 0)
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
    Moveto_r(2235.0 * scale[0], 0.0 * scale[1], 0, 0)
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
    Moveto_r(-3348.0 * scale[0], -22.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -6.0 *
              scale[0], -5.0 * scale[1], -6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 11.0 * scale[1], 2.0 * scale[0],
              17.0 * scale[1], 5.0 * scale[0], 13.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 4.0 * scale[0], -
              12.0 * scale[1], 1.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto_r(993.0 * scale[0], 18.0 * scale[1], 0, 0)
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
    Moveto_r(277.0 * scale[0], -18.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -6.0 *
              scale[0], -5.0 * scale[1], -6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 11.0 * scale[1], 2.0 * scale[0],
              17.0 * scale[1], 5.0 * scale[0], 13.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 4.0 * scale[0], -
              12.0 * scale[1], 1.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto_r(2128.0 * scale[0], 12.0 * scale[1], 0, 0)
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
    Moveto_r(-3115.0 * scale[0], -22.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], -23.0 *
              scale[0], -5.0 * scale[1], -28.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              10.0 * scale[1], 12.0 * scale[0], 6.0 * scale[1])
    Curveto_r(9.0 * scale[0], -3.0 * scale[1], 16.0 * scale[0], -
              11.0 * scale[1], 16.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto_r(54.0 * scale[0], 10.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -7.0 * scale[1], -2.0 *
              scale[0], -9.0 * scale[1], 8.0 * scale[0], -6.0 * scale[1])
    Curveto_r(12.0 * scale[0], 5.0 * scale[1], 14.0 * scale[0],
              0.0 * scale[1], 10.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -26.0 * scale[1], -5.0 * scale[0], -
              26.0 * scale[1], -15.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 12.0 * scale[1], -15.0 * scale[0],
              22.0 * scale[1], -21.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0],
              5.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(20.0 * scale[0], 13.0 * scale[1], 23.0 * scale[0],
              12.0 * scale[1], 14.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto_r(59.0 * scale[0], -3.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -9.0 * scale[1], -8.0 * scale[0], -
              14.0 * scale[1], -10.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], 2.0 * scale[0], 15.0 * scale[1])
    Curveto_r(9.0 * scale[0], 16.0 * scale[1], 15.0 * scale[0],
              13.0 * scale[1], 8.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto_r(-193.0 * scale[0], -5.0 * scale[1], 0, 0)
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
    Moveto_r(976.0 * scale[0], -17.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -11.0 * scale[1], -19.0 *
              scale[0], -7.0 * scale[1], -22.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 15.0 * scale[1], 0.0 * scale[0],
              16.0 * scale[1], 12.0 * scale[0], 6.0 * scale[1])
    Curveto_r(8.0 * scale[0], -6.0 * scale[1], 12.0 * scale[0], -
              14.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto_r(2039.0 * scale[0], 18.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              12.0 * scale[1], -5.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -10.0 * scale[0],
              1.0 * scale[1], -10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 18.0 * scale[1], 6.0 * scale[0],
              21.0 * scale[1], 15.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto_r(55.0 * scale[0], -1.0 * scale[1], 0, 0)
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
    Moveto_r(190.0 * scale[0], -6.0 * scale[1], 0, 0)
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
    Moveto_r(-2715.0 * scale[0], -5.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(11.0 * scale[0], -17.0 * scale[1], -1.0 * scale[0], -
              21.0 * scale[1], -15.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 9.0 * scale[1], -8.0 * scale[0],
              15.0 * scale[1], -2.0 * scale[0], 15.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0], -
              5.0 * scale[1], 17.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto_r(59.0 * scale[0], -13.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -18.0 * scale[1], 12.0 * scale[0], -
              24.0 * scale[1], 26.0 * scale[0], -21.0 * scale[1])
    Curveto_r(11.0 * scale[0], 2.0 * scale[1], 20.0 * scale[0],
              0.0 * scale[1], 20.0 * scale[0], -6.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -5.0 * scale[0], -
              9.0 * scale[1], -10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              14.0 * scale[1], 4.0 * scale[0], -35.0 * scale[1])
    Curveto_r(17.0 * scale[0], -40.0 * scale[1], 11.0 * scale[0], -
              43.0 * scale[1], -24.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 14.0 * scale[1], -19.0 * scale[0],
              19.0 * scale[1], -7.0 * scale[0], 15.0 * scale[1])
    Curveto_r(20.0 * scale[0], -6.0 * scale[1], 22.0 * scale[0],
              4.0 * scale[1], 5.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 17.0 * scale[1], -58.0 * scale[0],
              14.0 * scale[1], -58.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -4.0 * scale[0], -
              6.0 * scale[1], -10.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 10.0 * scale[1], -12.0 * scale[0],
              21.0 * scale[1], 13.0 * scale[0], 33.0 * scale[1])
    Curveto_r(12.0 * scale[0], 6.0 * scale[1], 16.0 * scale[0],
              11.0 * scale[1], 9.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 1.0 * scale[1], -10.0 * scale[0],
              4.0 * scale[1], 0.0 * scale[0], 16.0 * scale[1])
    Curveto_r(18.0 * scale[0], 20.0 * scale[1], 25.0 * scale[0],
              18.0 * scale[1], 32.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto_r(33.0 * scale[0], 18.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 17.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(153.0 * scale[0], -4.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(13.0 * scale[0], -9.0 * scale[1], 13.0 * scale[0], -
              12.0 * scale[1], -2.0 * scale[0], -24.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -7.0 * scale[1], -18.0 * scale[0], -
              18.0 * scale[1], -18.0 * scale[0], -25.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -4.0 * scale[0], -
              11.0 * scale[1], -10.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0],
              17.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 8.0 * scale[0],
              15.0 * scale[1], 5.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 21.0 * scale[1], 2.0 * scale[0],
              24.0 * scale[1], 25.0 * scale[0], 9.0 * scale[1])
    te.end_fill()
    Moveto_r(-1030.0 * scale[0], -10.0 * scale[1], 0, 0)
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
    Moveto_r(925.0 * scale[0], -8.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -11.0 * scale[0],
              0.0 * scale[1], -18.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 10.0 * scale[1], -8.0 * scale[0],
              11.0 * scale[1], 6.0 * scale[0], 5.0 * scale[1])
    Curveto_r(10.0 * scale[0], -3.0 * scale[1], 15.0 * scale[0], -
              9.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto_r(145.0 * scale[0], 8.0 * scale[1], 0, 0)
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
    Moveto_r(1986.0 * scale[0], -12.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -7.0 * scale[1], 3.0 * scale[0], -
              8.0 * scale[1], -4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 4.0 * scale[1], -12.0 * scale[0],
              0.0 * scale[1], -12.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -13.0 * scale[1], -3.0 * scale[0], -
              15.0 * scale[1], -11.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 12.0 * scale[1], -4.0 * scale[0],
              33.0 * scale[1], 11.0 * scale[0], 33.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0], -
              5.0 * scale[1], 16.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto_r(-2289.0 * scale[0], -20.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -18.0 * scale[1], 0.0 * scale[0], -
              20.0 * scale[1], -7.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 13.0 * scale[1], -10.0 * scale[0],
              12.0 * scale[1], -10.0 * scale[0], -2.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 6.0 * scale[0], -
              18.0 * scale[1], 14.0 * scale[0], -18.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0], -
              4.0 * scale[1], 20.0 * scale[0], -9.0 * scale[1])
    Curveto_r(10.0 * scale[0], -16.0 * scale[1], -22.0 *
              scale[0], -6.0 * scale[1], -44.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-26.0 * scale[0], 23.0 * scale[1], -25.0 * scale[0],
              33.0 * scale[1], 3.0 * scale[0], 38.0 * scale[1])
    Curveto_r(12.0 * scale[0], 2.0 * scale[1], 22.0 * scale[0],
              5.0 * scale[1], 22.0 * scale[0], 6.0 * scale[1])
    Curveto_r(1.0 * scale[0], 0.0 * scale[1], 2.0 * scale[0], -
              9.0 * scale[1], 2.0 * scale[0], -21.0 * scale[1])
    te.end_fill()
    Moveto_r(350.0 * scale[0], 0.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -6.0 *
              scale[0], -5.0 * scale[1], -6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 11.0 * scale[1], 2.0 * scale[0],
              17.0 * scale[1], 5.0 * scale[0], 13.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 4.0 * scale[0], -
              12.0 * scale[1], 1.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto_r(2153.0 * scale[0], 12.0 * scale[1], 0, 0)
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
    Moveto_r(123.0 * scale[0], -4.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -10.0 * scale[1], 1.0 * scale[0], -
              13.0 * scale[1], -9.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 6.0 * scale[1], -19.0 * scale[0],
              23.0 * scale[1], -5.0 * scale[0], 23.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0], -
              7.0 * scale[1], 14.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto_r(-3093.0 * scale[0], -6.0 * scale[1], 0, 0)
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
    Moveto_r(267.0 * scale[0], -15.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -16.0 * scale[1], 2.0 * scale[0], -
              34.0 * scale[1], 12.0 * scale[0], -46.0 * scale[1])
    Curveto_r(14.0 * scale[0], -18.0 * scale[1], 20.0 *
              scale[0], -19.0 * scale[1], 46.0 * scale[0], -9.0 * scale[1])
    Curveto_r(26.0 * scale[0], 10.0 * scale[1], 28.0 * scale[0],
              9.0 * scale[1], 15.0 * scale[0], -3.0 * scale[1])
    Curveto_r(-17.0 * scale[0], -17.0 * scale[1], -81.0 *
              scale[0], -40.0 * scale[1], -88.0 * scale[0], -32.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], 2.0 * scale[0],
              11.0 * scale[1], 11.0 * scale[0], 18.0 * scale[1])
    Curveto_r(16.0 * scale[0], 11.0 * scale[1], 16.0 * scale[0],
              13.0 * scale[1], -3.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 10.0 * scale[1], -20.0 * scale[0],
              15.0 * scale[1], -20.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -3.0 * scale[1], -3.0 *
              scale[0], -3.0 * scale[1], -7.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], 2.0 * scale[0],
              14.0 * scale[1], 13.0 * scale[0], 22.0 * scale[1])
    Curveto_r(15.0 * scale[0], 11.0 * scale[1], 16.0 * scale[0],
              14.0 * scale[1], 4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0],
              1.0 * scale[1], 0.0 * scale[0], 10.0 * scale[1])
    Curveto_r(22.0 * scale[0], 14.0 * scale[1], 23.0 * scale[0],
              13.0 * scale[1], 17.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto_r(140.0 * scale[0], 5.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -21.0 * scale[1], -17.0 * scale[0], -
              40.0 * scale[1], -17.0 * scale[0], -22.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], 11.0 * scale[0],
              42.0 * scale[1], 16.0 * scale[0], 42.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 3.0 * scale[0], -
              9.0 * scale[1], 1.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto_r(253.0 * scale[0], -2.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0], -
              6.0 * scale[1], 10.0 * scale[0], -3.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 10.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], -22.0 * scale[0], -
              25.0 * scale[1], -30.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 8.0 * scale[1], -17.0 * scale[0],
              10.0 * scale[1], -34.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -5.0 * scale[1], -25.0 *
              scale[0], -3.0 * scale[1], -20.0 * scale[0], 9.0 * scale[1])
    Curveto_r(6.0 * scale[0], 17.0 * scale[1], 64.0 * scale[0],
              21.0 * scale[1], 64.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto_r(-608.0 * scale[0], -20.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -7.0 * scale[1], -12.0 *
              scale[0], -8.0 * scale[1], -12.0 * scale[0], -2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], 12.0 * scale[0],
              26.0 * scale[1], 19.0 * scale[0], 19.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], -1.0 * scale[0], -
              11.0 * scale[1], -7.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto_r(38.0 * scale[0], 12.0 * scale[1], 0, 0)
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
    Moveto_r(110.0 * scale[0], -25.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -5.0 * scale[0], -
              3.0 * scale[1], -10.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 8.0 * scale[1], -10.0 * scale[0],
              20.0 * scale[1], -10.0 * scale[0], 25.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 5.0 * scale[0],
              3.0 * scale[1], 10.0 * scale[0], -5.0 * scale[1])
    Curveto_r(5.0 * scale[0], -8.0 * scale[1], 10.0 * scale[0], -
              19.0 * scale[1], 10.0 * scale[0], -25.0 * scale[1])
    te.end_fill()
    Moveto_r(-280.0 * scale[0], 15.0 * scale[1], 0, 0)
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
    Moveto_r(-146.0 * scale[0], -16.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], 2.0 * scale[0], -
              12.0 * scale[1], -4.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0],
              10.0 * scale[1], -10.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], 7.0 * scale[0],
              11.0 * scale[1], 14.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto_r(73.0 * scale[0], -4.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -11.0 * scale[1], -2.0 * scale[0], -
              18.0 * scale[1], -8.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 7.0 * scale[1], -12.0 * scale[0],
              35.0 * scale[1], -1.0 * scale[0], 35.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0], -
              9.0 * scale[1], 9.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto_r(153.0 * scale[0], 10.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -7.0 * scale[0], -
              10.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0],
              5.0 * scale[1], -9.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 10.0 * scale[0],
              10.0 * scale[1], 16.0 * scale[0], 10.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0], -
              4.0 * scale[1], 9.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto_r(163.0 * scale[0], -4.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(17.0 * scale[0], -13.0 * scale[1], 16.0 * scale[0], -
              14.0 * scale[1], -2.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -3.0 * scale[1], -19.0 * scale[0],
              0.0 * scale[1], -18.0 * scale[0], 7.0 * scale[1])
    Curveto_r(1.0 * scale[0], 6.0 * scale[1], -6.0 * scale[0],
              10.0 * scale[1], -15.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -2.0 * scale[1], -18.0 * scale[0],
              2.0 * scale[1], -18.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], 32.0 * scale[0],
              12.0 * scale[1], 53.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto_r(212.0 * scale[0], 4.0 * scale[1], 0, 0)
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
    Moveto_r(370.0 * scale[0], 1.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(17.0 * scale[0], -7.0 * scale[1], 14.0 * scale[0], -
              9.0 * scale[1], -16.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-24.0 * scale[0], -3.0 * scale[1], -36.0 *
              scale[0], -1.0 * scale[1], -36.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], 21.0 * scale[0],
              16.0 * scale[1], 52.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto_r(-795.0 * scale[0], -11.0 * scale[1], 0, 0)
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
    Moveto_r(100.0 * scale[0], -15.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -15.0 * scale[1], -21.0 *
              scale[0], -12.0 * scale[1], -30.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 20.0 * scale[1], -10.0 * scale[0],
              21.0 * scale[1], 9.0 * scale[0], 10.0 * scale[1])
    Curveto_r(12.0 * scale[0], -6.0 * scale[1], 21.0 * scale[0], -
              13.0 * scale[1], 21.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto_r(250.0 * scale[0], 15.0 * scale[1], 0, 0)
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
    Moveto_r(497.0 * scale[0], -15.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -8.0 * scale[1], -11.0 * scale[0], -
              15.0 * scale[1], -17.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0],
              27.0 * scale[1], 3.0 * scale[0], 33.0 * scale[1])
    Curveto_r(16.0 * scale[0], 6.0 * scale[1], 21.0 * scale[0],
              1.0 * scale[1], 14.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto_r(-159.0 * scale[0], -5.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -19.0 * scale[1], -28.0 *
              scale[0], -27.0 * scale[1], -28.0 * scale[0], -14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 30.0 * scale[0],
              33.0 * scale[1], 38.0 * scale[0], 34.0 * scale[1])
    Curveto_r(1.0 * scale[0], 0.0 * scale[1], -3.0 * scale[0], -
              9.0 * scale[1], -10.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto_r(302.0 * scale[0], 5.0 * scale[1], 0, 0)
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
    Moveto_r(2200.0 * scale[0], 5.0 * scale[1], 0, 0)
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
    Moveto_r(-3420.0 * scale[0], -10.0 * scale[1], 0, 0)
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
    Moveto_r(748.0 * scale[0], -5.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -2.0 * scale[1], -2.0 * scale[0], -
              13.0 * scale[1], -8.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -21.0 * scale[1], -13.0 *
              scale[0], -21.0 * scale[1], -28.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 14.0 * scale[1], -14.0 * scale[0],
              18.0 * scale[1], -3.0 * scale[0], 22.0 * scale[1])
    Curveto_r(11.0 * scale[0], 5.0 * scale[1], 11.0 * scale[0],
              7.0 * scale[1], 0.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 6.0 * scale[1], -6.0 * scale[0],
              7.0 * scale[1], 11.0 * scale[0], 2.0 * scale[1])
    Curveto_r(14.0 * scale[0], -3.0 * scale[1], 26.0 *
              scale[0], -8.0 * scale[1], 28.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto_r(78.0 * scale[0], 2.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -4.0 * scale[1], -2.0 * scale[0], -
              10.0 * scale[1], -12.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -3.0 * scale[1], -22.0 * scale[0], -
              11.0 * scale[1], -26.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], 15.0 * scale[1])
    Curveto_r(2.0 * scale[0], 23.0 * scale[1], 26.0 * scale[0],
              32.0 * scale[1], 43.0 * scale[0], 15.0 * scale[1])
    te.end_fill()
    Moveto_r(2554.0 * scale[0], -11.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -7.0 * scale[1], -13.0 *
              scale[0], -7.0 * scale[1], -20.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 6.0 * scale[1], -3.0 * scale[0],
              10.0 * scale[1], 10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0], -
              4.0 * scale[1], 10.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto_r(-3224.0 * scale[0], -8.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -8.0 * scale[1], 2.0 * scale[0], -
              9.0 * scale[1], -9.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 4.0 * scale[1], -17.0 * scale[0],
              1.0 * scale[1], -17.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -3.0 * scale[0], -
              9.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 7.0 * scale[1], 4.0 * scale[0],
              27.0 * scale[1], 16.0 * scale[0], 27.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0], -
              5.0 * scale[1], 16.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto_r(44.0 * scale[0], 2.0 * scale[1], 0, 0)
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
    Moveto_r(304.0 * scale[0], -17.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-12.0 * scale[0], -12.0 * scale[1], -17.0 *
              scale[0], -13.0 * scale[1], -30.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 12.0 * scale[1], -14.0 * scale[0],
              14.0 * scale[1], 3.0 * scale[0], 20.0 * scale[1])
    Curveto_r(29.0 * scale[0], 10.0 * scale[1], 45.0 * scale[0],
              0.0 * scale[1], 27.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto_r(481.0 * scale[0], -3.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              11.0 * scale[1], 7.0 * scale[0], -13.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 6.0 * scale[0], -
              6.0 * scale[1], -4.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -1.0 * scale[1], -18.0 *
              scale[0], -6.0 * scale[1], -18.0 * scale[0], -13.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -3.0 * scale[0], -
              9.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -1.0 * scale[0],
              16.0 * scale[1], 6.0 * scale[0], 27.0 * scale[1])
    Curveto_r(7.0 * scale[0], 14.0 * scale[1], 7.0 * scale[0],
              21.0 * scale[1], 0.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0],
              5.0 * scale[1], -10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 5.0 * scale[0],
              8.0 * scale[1], 15.0 * scale[0], -1.0 * scale[1])
    Curveto_r(8.0 * scale[0], -7.0 * scale[1], 13.0 * scale[0], -
              16.0 * scale[1], 10.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto_r(35.0 * scale[0], 20.0 * scale[1], 0, 0)
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
    Moveto_r(-588.0 * scale[0], -17.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(8.0 * scale[0], -7.0 * scale[1], 18.0 * scale[0], -
              10.0 * scale[1], 21.0 * scale[0], -6.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], 7.0 * scale[0], -
              8.0 * scale[1], 7.0 * scale[0], -25.0 * scale[1])
    Curveto_r(0.0 * scale[0], -22.0 * scale[1], -5.0 * scale[0], -
              32.0 * scale[1], -16.0 * scale[0], -32.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0],
              8.0 * scale[1], -13.0 * scale[0], 18.0 * scale[1])
    Curveto_r(1.0 * scale[0], 9.0 * scale[1], 1.0 * scale[0],
              24.0 * scale[1], 0.0 * scale[0], 32.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 13.0 * scale[1], -2.0 * scale[0],
              13.0 * scale[1], -11.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -12.0 * scale[1], -12.0 *
              scale[0], -12.0 * scale[1], -18.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 7.0 * scale[1], -16.0 * scale[0],
              10.0 * scale[1], -24.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -3.0 * scale[1], -18.0 * scale[0],
              0.0 * scale[1], -20.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 17.0 * scale[1], 53.0 * scale[0],
              18.0 * scale[1], 74.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto_r(219.0 * scale[0], 5.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -7.0 * scale[1], 1.0 * scale[0], -
              17.0 * scale[1], 0.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -4.0 * scale[1], 5.0 * scale[0], -
              18.0 * scale[1], 13.0 * scale[0], -31.0 * scale[1])
    Curveto_r(11.0 * scale[0], -17.0 * scale[1], 22.0 * scale[0], -
              21.0 * scale[1], 40.0 * scale[0], -18.0 * scale[1])
    Curveto_r(14.0 * scale[0], 3.0 * scale[1], 26.0 * scale[0],
              1.0 * scale[1], 26.0 * scale[0], -3.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -18.0 * scale[0], -
              10.0 * scale[1], -40.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-30.0 * scale[0], -2.0 * scale[1], -40.0 * scale[0],
              1.0 * scale[1], -40.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], -6.0 * scale[0],
              13.0 * scale[1], -15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -4.0 * scale[1], -15.0 * scale[0],
              0.0 * scale[1], -15.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], -4.0 * scale[0],
              13.0 * scale[1], -10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -10.0 *
              scale[0], -1.0 * scale[1], -10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 6.0 * scale[0],
              11.0 * scale[1], 14.0 * scale[0], 11.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 18.0 * scale[0],
              4.0 * scale[1], 21.0 * scale[0], 10.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], 0.0 * scale[0],
              7.0 * scale[1], -9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -3.0 * scale[1], -21.0 *
              scale[0], -2.0 * scale[1], -27.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 5.0 * scale[1], -7.0 * scale[0],
              10.0 * scale[1], 7.0 * scale[0], 15.0 * scale[1])
    Curveto_r(29.0 * scale[0], 11.0 * scale[1], 44.0 * scale[0],
              10.0 * scale[1], 45.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto_r(119.0 * scale[0], 2.0 * scale[1], 0, 0)
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
    Moveto_r(90.0 * scale[0], 0.0 * scale[1], 0, 0)
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
    Moveto_r(400.0 * scale[0], 0.0 * scale[1], 0, 0)
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
    Moveto_r(-976.0 * scale[0], -15.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], 1.0 * scale[0], -
              15.0 * scale[1], -4.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0],
              5.0 * scale[1], -10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -5.0 * scale[0],
              7.0 * scale[1], -12.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -4.0 * scale[1], -8.0 *
              scale[0], -3.0 * scale[1], -4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(10.0 * scale[0], 16.0 * scale[1], 23.0 * scale[0],
              15.0 * scale[1], 30.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto_r(406.0 * scale[0], 1.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 11.0 * scale[0], -
              17.0 * scale[1], 25.0 * scale[0], -20.0 * scale[1])
    Curveto_r(14.0 * scale[0], -4.0 * scale[1], 25.0 * scale[0], -
              11.0 * scale[1], 25.0 * scale[0], -17.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -7.0 * scale[0], -
              8.0 * scale[1], -17.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 4.0 * scale[1], -26.0 * scale[0],
              10.0 * scale[1], -35.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 6.0 * scale[1], -25.0 * scale[0],
              43.0 * scale[1], -8.0 * scale[0], 43.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              6.0 * scale[1], 10.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto_r(2797.0 * scale[0], 8.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 17.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(-3122.0 * scale[0], -24.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 23.0 * scale[0],
              6.0 * scale[1], 19.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -7.0 * scale[1], 2.0 * scale[0], -
              16.0 * scale[1], 10.0 * scale[0], -19.0 * scale[1])
    Curveto_r(9.0 * scale[0], -4.0 * scale[1], 16.0 * scale[0], -
              12.0 * scale[1], 16.0 * scale[0], -18.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -7.0 * scale[0], -
              5.0 * scale[1], -19.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 21.0 * scale[1], -53.0 * scale[0],
              27.0 * scale[1], -64.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0],
              0.0 * scale[1], -3.0 * scale[0], 14.0 * scale[1])
    Curveto_r(6.0 * scale[0], 35.0 * scale[1], 8.0 * scale[0],
              37.0 * scale[1], 13.0 * scale[0], 18.0 * scale[1])
    Curveto_r(3.0 * scale[0], -13.0 * scale[1], 9.0 * scale[0], -
              15.0 * scale[1], 28.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto_r(455.0 * scale[0], 9.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 4.0 * scale[0], -
              8.0 * scale[1], 9.0 * scale[0], -5.0 * scale[1])
    Curveto_r(5.0 * scale[0], 4.0 * scale[1], 7.0 * scale[0], -
              3.0 * scale[1], 4.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -16.0 * scale[1], -8.0 * scale[0], -
              17.0 * scale[1], -14.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 7.0 * scale[1], -9.0 * scale[0],
              9.0 * scale[1], -9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0], -
              5.0 * scale[1], -11.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 6.0 * scale[1], -8.0 * scale[0],
              16.0 * scale[1], -5.0 * scale[0], 22.0 * scale[1])
    Curveto_r(9.0 * scale[0], 14.0 * scale[1], 26.0 * scale[0],
              14.0 * scale[1], 26.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto_r(116.0 * scale[0], -14.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -11.0 * scale[1], 7.0 * scale[0], -
              35.0 * scale[1], -7.0 * scale[0], -35.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0],
              7.0 * scale[1], -2.0 * scale[0], 16.0 * scale[1])
    Curveto_r(4.0 * scale[0], 10.0 * scale[1], -1.0 * scale[0],
              17.0 * scale[1], -16.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 3.0 * scale[1], -21.0 * scale[0],
              9.0 * scale[1], -21.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], 30.0 * scale[0],
              0.0 * scale[1], 46.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto_r(-836.0 * scale[0], 0.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -4.0 * scale[0], -
              15.0 * scale[1], -8.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0],
              7.0 * scale[1], -9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 4.0 * scale[0],
              15.0 * scale[1], 9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0], -
              7.0 * scale[1], 8.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto_r(70.0 * scale[0], -10.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -4.0 * scale[0], -
              15.0 * scale[1], -10.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0],
              7.0 * scale[1], -10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 5.0 * scale[0],
              15.0 * scale[1], 10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              7.0 * scale[1], 10.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto_r(370.0 * scale[0], -6.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], -5.0 * scale[0], -
              19.0 * scale[1], -12.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 6.0 * scale[1], -19.0 * scale[0],
              38.0 * scale[1], -2.0 * scale[0], 38.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 14.0 * scale[0], -
              9.0 * scale[1], 14.0 * scale[0], -21.0 * scale[1])
    te.end_fill()
    Moveto_r(733.0 * scale[0], 1.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -12.0 * scale[1], -8.0 * scale[0], -
              19.0 * scale[1], -11.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 6.0 * scale[1], 5.0 * scale[0],
              36.0 * scale[1], 12.0 * scale[0], 36.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 2.0 * scale[0], -
              9.0 * scale[1], -1.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto_r(-1013.0 * scale[0], -2.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], -4.0 * scale[0], -
              10.0 * scale[1], -10.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -10.0 * scale[0], -
              17.0 * scale[1], -10.0 * scale[0], -31.0 * scale[1])
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], -4.0 * scale[0], -
              22.0 * scale[1], -10.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0],
              2.0 * scale[1], -10.0 * scale[0], -3.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -7.0 * scale[0], -
              12.0 * scale[1], -14.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -4.0 * scale[1], -13.0 *
              scale[0], -1.0 * scale[1], -9.0 * scale[0], 11.0 * scale[1])
    Curveto_r(4.0 * scale[0], 9.0 * scale[1], 11.0 * scale[0],
              21.0 * scale[1], 17.0 * scale[0], 25.0 * scale[1])
    Curveto_r(7.0 * scale[0], 5.0 * scale[1], 6.0 * scale[0],
              12.0 * scale[1], -6.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 11.0 * scale[1], -15.0 * scale[0],
              13.0 * scale[1], 0.0 * scale[0], 24.0 * scale[1])
    Curveto_r(18.0 * scale[0], 13.0 * scale[1], 52.0 * scale[0],
              15.0 * scale[1], 52.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto_r(45.0 * scale[0], 2.0 * scale[1], 0, 0)
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
    Moveto_r(275.0 * scale[0], -5.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -4.0 * scale[0], -
              15.0 * scale[1], -10.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0],
              7.0 * scale[1], -10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 5.0 * scale[0],
              15.0 * scale[1], 10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              7.0 * scale[1], 10.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto_r(331.0 * scale[0], 2.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -4.0 * scale[1], -1.0 * scale[0], -
              14.0 * scale[1], -1.0 * scale[0], -23.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -4.0 * scale[0], -
              12.0 * scale[1], -10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 8.0 * scale[1], -13.0 * scale[0],
              48.0 * scale[1], 1.0 * scale[0], 43.0 * scale[1])
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 10.0 * scale[0], -
              7.0 * scale[1], 10.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto_r(114.0 * scale[0], 3.0 * scale[1], 0, 0)
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
    Moveto_r(-242.0 * scale[0], -20.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -11.0 * scale[1], -12.0 * scale[0], -
              20.0 * scale[1], -20.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -11.0 * scale[0],
              4.0 * scale[1], -3.0 * scale[0], 20.0 * scale[1])
    Curveto_r(6.0 * scale[0], 11.0 * scale[1], 15.0 * scale[0],
              20.0 * scale[1], 19.0 * scale[0], 20.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0], -
              9.0 * scale[1], 4.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto_r(-769.0 * scale[0], -6.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], 2.0 * scale[0], -
              12.0 * scale[1], -4.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0],
              10.0 * scale[1], -10.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], 7.0 * scale[0],
              11.0 * scale[1], 14.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto_r(336.0 * scale[0], 1.0 * scale[1], 0, 0)
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
    Moveto_r(500.0 * scale[0], -1.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -5.0 * scale[0], -
              12.0 * scale[1], -10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -8.0 * scale[0],
              11.0 * scale[1], -5.0 * scale[0], 16.0 * scale[1])
    Curveto_r(9.0 * scale[0], 14.0 * scale[1], 15.0 * scale[0],
              11.0 * scale[1], 15.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto_r(-880.0 * scale[0], -25.0 * scale[1], 0, 0)
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
    Moveto_r(630.0 * scale[0], 11.0 * scale[1], 0, 0)
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
    Moveto_r(385.0 * scale[0], 0.0 * scale[1], 0, 0)
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
    Moveto_r(2465.0 * scale[0], -12.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], -3.0 * scale[0], -
              19.0 * scale[1], -11.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 6.0 * scale[1], -8.0 * scale[0],
              16.0 * scale[1], -5.0 * scale[0], 22.0 * scale[1])
    Curveto_r(11.0 * scale[0], 17.0 * scale[1], 16.0 * scale[0],
              13.0 * scale[1], 16.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto_r(-3346.0 * scale[0], -32.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(14.0 * scale[0], -25.0 * scale[1], 26.0 * scale[0], -
              48.0 * scale[1], 26.0 * scale[0], -53.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -60.0 * scale[0],
              83.0 * scale[1], -60.0 * scale[0], 92.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], 10.0 * scale[0],
              1.0 * scale[1], 34.0 * scale[0], -39.0 * scale[1])
    te.end_fill()
    Moveto_r(266.0 * scale[0], 24.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -5.0 * scale[1], -17.0 *
              scale[0], -7.0 * scale[1], -19.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              9.0 * scale[1], 9.0 * scale[0], 14.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 17.0 * scale[0],
              7.0 * scale[1], 19.0 * scale[0], 4.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], -1.0 * scale[0], -
              9.0 * scale[1], -9.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto_r(40.0 * scale[0], 16.0 * scale[1], 0, 0)
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
    Moveto_r(700.0 * scale[0], -11.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -8.0 * scale[1], 8.0 * scale[0], -
              15.0 * scale[1], 2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0],
              7.0 * scale[1], -22.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 8.0 * scale[1], -8.0 * scale[0],
              15.0 * scale[1], -2.0 * scale[0], 15.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0], -
              7.0 * scale[1], 22.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto_r(-808.0 * scale[0], -17.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -7.0 * scale[1], -12.0 *
              scale[0], -8.0 * scale[1], -12.0 * scale[0], -2.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], 12.0 * scale[0],
              26.0 * scale[1], 19.0 * scale[0], 19.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], -1.0 * scale[0], -
              11.0 * scale[1], -7.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto_r(378.0 * scale[0], 12.0 * scale[1], 0, 0)
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
    Moveto_r(229.0 * scale[0], -33.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(1.0 * scale[0], -5.0 * scale[1], -3.0 * scale[0], -
              5.0 * scale[1], -9.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0],
              16.0 * scale[1], -9.0 * scale[0], 28.0 * scale[1])
    Curveto_r(0.0 * scale[0], 21.0 * scale[1], 1.0 * scale[0],
              21.0 * scale[1], 9.0 * scale[0], 2.0 * scale[1])
    Curveto_r(5.0 * scale[0], -11.0 * scale[1], 9.0 * scale[0], -
              24.0 * scale[1], 9.0 * scale[0], -28.0 * scale[1])
    te.end_fill()
    Moveto_r(121.0 * scale[0], 10.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -4.0 * scale[0], -
              5.0 * scale[1], -10.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0],
              14.0 * scale[1], -10.0 * scale[0], 23.0 * scale[1])
    Curveto_r(0.0 * scale[0], 15.0 * scale[1], 2.0 * scale[0],
              15.0 * scale[1], 10.0 * scale[0], 2.0 * scale[1])
    Curveto_r(5.0 * scale[0], -8.0 * scale[1], 10.0 * scale[0], -
              19.0 * scale[1], 10.0 * scale[0], -23.0 * scale[1])
    te.end_fill()
    Moveto_r(-704.0 * scale[0], -3.0 * scale[1], 0, 0)
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
    Moveto_r(144.0 * scale[0], 16.0 * scale[1], 0, 0)
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
    Moveto_r(80.0 * scale[0], 6.0 * scale[1], 0, 0)
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
    Moveto_r(640.0 * scale[0], -11.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -9.0 * scale[1], 8.0 * scale[0], -
              15.0 * scale[1], 2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0],
              7.0 * scale[1], -16.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 8.0 * scale[1], -4.0 * scale[0],
              15.0 * scale[1], -2.0 * scale[0], 15.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0], -
              7.0 * scale[1], 16.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto_r(270.0 * scale[0], 11.0 * scale[1], 0, 0)
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
    Moveto_r(2043.0 * scale[0], -9.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -7.0 * scale[1], -3.0 * scale[0], -
              13.0 * scale[1], -14.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0],
              3.0 * scale[1], -7.0 * scale[0], 13.0 * scale[1])
    Curveto_r(6.0 * scale[0], 7.0 * scale[1], 12.0 * scale[0],
              13.0 * scale[1], 13.0 * scale[0], 13.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 5.0 * scale[0], -
              6.0 * scale[1], 8.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto_r(-2749.0 * scale[0], -32.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -13.0 * scale[1], 0.0 * scale[0], -
              27.0 * scale[1], 6.0 * scale[0], -30.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 10.0 * scale[0], -
              12.0 * scale[1], 10.0 * scale[0], -18.0 * scale[1])
    Curveto_r(0.0 * scale[0], -7.0 * scale[1], -7.0 * scale[0], -
              3.0 * scale[1], -15.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 11.0 * scale[1], -22.0 * scale[0],
              21.0 * scale[1], -31.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 4.0 * scale[1], -29.0 * scale[0],
              14.0 * scale[1], -6.0 * scale[0], 14.0 * scale[1])
    Curveto_r(16.0 * scale[0], 0.0 * scale[1], 22.0 * scale[0],
              6.0 * scale[1], 22.0 * scale[0], 21.0 * scale[1])
    Curveto_r(0.0 * scale[0], 11.0 * scale[1], 4.0 * scale[0],
              18.0 * scale[1], 9.0 * scale[0], 14.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 8.0 * scale[0], -
              16.0 * scale[1], 5.0 * scale[0], -30.0 * scale[1])
    te.end_fill()
    Moveto_r(116.0 * scale[0], 25.0 * scale[1], 0, 0)
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
    Moveto_r(-815.0 * scale[0], -10.0 * scale[1], 0, 0)
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
    Moveto_r(99.0 * scale[0], -5.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], 1.0 * scale[0], -
              15.0 * scale[1], -4.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0],
              7.0 * scale[1], -10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 2.0 * scale[0],
              15.0 * scale[1], 4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 6.0 * scale[0], -
              7.0 * scale[1], 10.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto_r(836.0 * scale[0], 0.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -1.0 * scale[1], -11.0 * scale[0], -
              5.0 * scale[1], -25.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -4.0 * scale[1], -23.0 *
              scale[0], -2.0 * scale[1], -14.0 * scale[0], 8.0 * scale[1])
    Curveto_r(8.0 * scale[0], 10.0 * scale[1], 39.0 * scale[0],
              10.0 * scale[1], 39.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto_r(2297.0 * scale[0], 9.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 17.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(-2990.0 * scale[0], -10.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 17.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(97.0 * scale[0], -9.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(17.0 * scale[0], -13.0 * scale[1], 15.0 * scale[0], -
              14.0 * scale[1], -15.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 1.0 * scale[1], -28.0 * scale[0],
              3.0 * scale[1], -20.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 4.0 * scale[1], 11.0 * scale[0],
              6.0 * scale[1], 0.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 7.0 * scale[1], -11.0 *
              scale[0], 9.0 * scale[1], 1.0 * scale[0], 9.0 * scale[1])
    Curveto_r(8.0 * scale[0], -1.0 * scale[1], 23.0 * scale[0], -
              7.0 * scale[1], 34.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto_r(426.0 * scale[0], 5.0 * scale[1], 0, 0)
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
    Moveto_r(-261.0 * scale[0], -21.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-22.0 * scale[0], -14.0 * scale[1], -33.0 *
              scale[0], -10.0 * scale[1], -19.0 * scale[0], 6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 8.0 * scale[1], 17.0 * scale[0],
              12.0 * scale[1], 22.0 * scale[0], 9.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 5.0 * scale[0], -
              10.0 * scale[1], -3.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto_r(3011.0 * scale[0], 11.0 * scale[1], 0, 0)
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
    Moveto_r(-3376.0 * scale[0], -27.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -15.0 * scale[1], 4.0 * scale[0], -
              15.0 * scale[1], -18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 8.0 * scale[1], -21.0 * scale[0],
              21.0 * scale[1], -1.0 * scale[0], 21.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0], -
              6.0 * scale[1], 19.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto_r(286.0 * scale[0], 13.0 * scale[1], 0, 0)
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
    Moveto_r(35.0 * scale[0], -6.0 * scale[1], 0, 0)
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
    Moveto_r(-545.0 * scale[0], -20.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], -2.0 * scale[0], -
              20.0 * scale[1], -4.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0],
              9.0 * scale[1], -9.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 11.0 * scale[1], -1.0 * scale[0],
              20.0 * scale[1], 4.0 * scale[0], 20.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0], -
              9.0 * scale[1], 9.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto_r(40.0 * scale[0], 16.0 * scale[1], 0, 0)
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
    Moveto_r(688.0 * scale[0], -9.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(8.0 * scale[0], -10.0 * scale[1], 7.0 * scale[0], -
              13.0 * scale[1], -7.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -1.0 * scale[1], -18.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 13.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], 11.0 * scale[0],
              18.0 * scale[1], 25.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto_r(149.0 * scale[0], 7.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 17.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(548.0 * scale[0], -4.0 * scale[1], 0, 0)
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
    Moveto_r(-1075.0 * scale[0], -10.0 * scale[1], 0, 0)
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
    Moveto_r(240.0 * scale[0], 0.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-20.0 * scale[0], -13.0 * scale[1], -33.0 *
              scale[0], -13.0 * scale[1], -25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(3.0 * scale[0], 6.0 * scale[1], 14.0 * scale[0],
              10.0 * scale[1], 23.0 * scale[0], 10.0 * scale[1])
    Curveto_r(15.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0], -
              2.0 * scale[1], 2.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto_r(497.0 * scale[0], -26.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -9.0 * scale[1], -27.0 * scale[0],
              6.0 * scale[1], -27.0 * scale[0], 22.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], 2.0 * scale[0],
              13.0 * scale[1], 16.0 * scale[0], -1.0 * scale[1])
    Curveto_r(9.0 * scale[0], -9.0 * scale[1], 14.0 * scale[0], -
              18.0 * scale[1], 11.0 * scale[0], -21.0 * scale[1])
    te.end_fill()
    Moveto_r(48.0 * scale[0], 26.0 * scale[1], 0, 0)
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
    Moveto_r(65.0 * scale[0], 6.0 * scale[1], 0, 0)
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
    Moveto_r(1895.0 * scale[0], -14.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -11.0 * scale[0],
              0.0 * scale[1], -18.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 10.0 * scale[1], -8.0 * scale[0],
              11.0 * scale[1], 6.0 * scale[0], 5.0 * scale[1])
    Curveto_r(10.0 * scale[0], -3.0 * scale[1], 15.0 * scale[0], -
              9.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto_r(235.0 * scale[0], 8.0 * scale[1], 0, 0)
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
    Moveto_r(-3486.0 * scale[0], -15.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -9.0 * scale[1], 0.0 * scale[0], -
              15.0 * scale[1], -9.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0],
              6.0 * scale[1], -9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(4.0 * scale[0], 8.0 * scale[1], 7.0 * scale[0],
              15.0 * scale[1], 9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 5.0 * scale[0], -
              7.0 * scale[1], 9.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto_r(536.0 * scale[0], 11.0 * scale[1], 0, 0)
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
    Moveto_r(494.0 * scale[0], -5.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              11.0 * scale[1], -9.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -4.0 * scale[1], -12.0 *
              scale[0], -1.0 * scale[1], -8.0 * scale[0], 9.0 * scale[1])
    Curveto_r(6.0 * scale[0], 16.0 * scale[1], 10.0 * scale[0],
              17.0 * scale[1], 17.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto_r(118.0 * scale[0], -3.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -8.0 * scale[1], -18.0 *
              scale[0], -8.0 * scale[1], -34.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 9.0 * scale[1], -20.0 * scale[0],
              10.0 * scale[1], 11.0 * scale[0], 11.0 * scale[1])
    Curveto_r(25.0 * scale[0], 0.0 * scale[1], 31.0 * scale[0], -
              2.0 * scale[1], 23.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto_r(1635.0 * scale[0], -4.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 17.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(61.0 * scale[0], -19.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -9.0 * scale[0],
              2.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 14.0 * scale[1], -5.0 * scale[0],
              15.0 * scale[1], 5.0 * scale[0], 6.0 * scale[1])
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 10.0 * scale[0], -
              15.0 * scale[1], 7.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto_r(-1975.0 * scale[0], -2.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -2.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              5.0 * scale[1], 12.0 * scale[0], 5.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(111.0 * scale[0], -8.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -8.0 * scale[1], -7.0 * scale[0], -
              15.0 * scale[1], -9.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -5.0 * scale[0],
              7.0 * scale[1], -9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], 0.0 * scale[0],
              15.0 * scale[1], 9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0], -
              6.0 * scale[1], 9.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto_r(2701.0 * scale[0], 5.0 * scale[1], 0, 0)
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
    Moveto_r(-2308.0 * scale[0], -22.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -6.0 *
              scale[0], -5.0 * scale[1], -6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 11.0 * scale[1], 2.0 * scale[0],
              17.0 * scale[1], 5.0 * scale[0], 13.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 4.0 * scale[0], -
              12.0 * scale[1], 1.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto_r(1113.0 * scale[0], 1.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], -4.0 * scale[0], -
              18.0 * scale[1], -10.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -7.0 * scale[0],
              12.0 * scale[1], -3.0 * scale[0], 20.0 * scale[1])
    Curveto_r(7.0 * scale[0], 21.0 * scale[1], 13.0 * scale[0],
              19.0 * scale[1], 13.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto_r(-2600.0 * scale[0], 7.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], -7.0 * scale[0], -
              7.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -2.0 * scale[1], -9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(6.0 * scale[0], 10.0 * scale[1], 25.0 * scale[0],
              14.0 * scale[1], 25.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto_r(397.0 * scale[0], -21.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -18.0 * scale[1], -28.0 *
              scale[0], -20.0 * scale[1], -24.0 * scale[0], -2.0 * scale[1])
    Curveto_r(2.0 * scale[0], 13.0 * scale[1], 19.0 * scale[0],
              28.0 * scale[1], 25.0 * scale[0], 22.0 * scale[1])
    Curveto_r(3.0 * scale[0], -2.0 * scale[1], 2.0 * scale[0], -
              11.0 * scale[1], -1.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto_r(59.0 * scale[0], 10.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -5.0 * scale[1], 10.0 * scale[0], -
              13.0 * scale[1], 7.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -14.0 * scale[1], -22.0 *
              scale[0], -8.0 * scale[1], -33.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 22.0 * scale[1], 3.0 * scale[0],
              25.0 * scale[1], 26.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto_r(900.0 * scale[0], 2.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -4.0 * scale[1], 0.0 * scale[0], -
              7.0 * scale[1], -9.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -18.0 * scale[0],
              4.0 * scale[1], -21.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 10.0 * scale[1], 20.0 * scale[0],
              9.0 * scale[1], 30.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto_r(-1109.0 * scale[0], -32.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -4.0 * scale[0], -
              12.0 * scale[1], -9.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -6.0 * scale[0],
              10.0 * scale[1], -3.0 * scale[0], 15.0 * scale[1])
    Curveto_r(9.0 * scale[0], 13.0 * scale[1], 12.0 * scale[0],
              11.0 * scale[1], 12.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto_r(1171.0 * scale[0], -21.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -3.0 * scale[1], -12.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 22.0 * scale[1], -12.0 *
              scale[0], 22.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(10.0 * scale[0], -10.0 * scale[1], 15.0 * scale[0], -
              20.0 * scale[1], 12.0 * scale[0], -24.0 * scale[1])
    te.end_fill()
    Moveto_r(352.0 * scale[0], 32.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], -7.0 * scale[0], -
              7.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -2.0 * scale[1], -9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(6.0 * scale[0], 10.0 * scale[1], 25.0 * scale[0],
              14.0 * scale[1], 25.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto_r(927.0 * scale[0], -28.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -7.0 * scale[1], -5.0 *
              scale[0], -2.0 * scale[1], -5.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], 2.0 * scale[0],
              19.0 * scale[1], 5.0 * scale[0], 13.0 * scale[1])
    Curveto_r(2.0 * scale[0], -7.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 0.0 * scale[0], -25.0 * scale[1])
    te.end_fill()
    Moveto_r(-312.0 * scale[0], 4.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -11.0 * scale[0],
              0.0 * scale[1], -18.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 10.0 * scale[1], -8.0 * scale[0],
              11.0 * scale[1], 6.0 * scale[0], 5.0 * scale[1])
    Curveto_r(10.0 * scale[0], -3.0 * scale[1], 15.0 * scale[0], -
              9.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto_r(1015.0 * scale[0], 14.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -2.0 * scale[1], -7.0 * scale[0], -
              9.0 * scale[1], -15.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -11.0 * scale[1], -14.0 *
              scale[0], -10.0 * scale[1], -9.0 * scale[0], 4.0 * scale[1])
    Curveto_r(5.0 * scale[0], 14.0 * scale[1], 24.0 * scale[0],
              23.0 * scale[1], 24.0 * scale[0], 12.0 * scale[1])
    te.end_fill()
    Moveto_r(240.0 * scale[0], -6.0 * scale[1], 0, 0)
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
    Moveto_r(-2093.0 * scale[0], -22.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -6.0 *
              scale[0], -5.0 * scale[1], -6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 11.0 * scale[1], 2.0 * scale[0],
              17.0 * scale[1], 5.0 * scale[0], 13.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 4.0 * scale[0], -
              12.0 * scale[1], 1.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto_r(1603.0 * scale[0], 16.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -19.0 * scale[0], -
              13.0 * scale[1], -24.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], 1.0 * scale[0],
              9.0 * scale[1], 9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0], -
              2.0 * scale[1], 15.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto_r(465.0 * scale[0], -23.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              12.0 * scale[1], -5.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -10.0 * scale[0],
              1.0 * scale[1], -10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 18.0 * scale[1], 6.0 * scale[0],
              21.0 * scale[1], 15.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto_r(-890.0 * scale[0], -20.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], -11.0 * scale[0], -
              11.0 * scale[1], -16.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0],
              6.0 * scale[1], 3.0 * scale[0], 14.0 * scale[1])
    Curveto_r(14.0 * scale[0], 16.0 * scale[1], 24.0 * scale[0],
              13.0 * scale[1], 13.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto_r(-2627.0 * scale[0], -36.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -9.0 * scale[0],
              2.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 14.0 * scale[1], -5.0 * scale[0],
              15.0 * scale[1], 5.0 * scale[0], 6.0 * scale[1])
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 10.0 * scale[0], -
              15.0 * scale[1], 7.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto_r(3539.0 * scale[0], 19.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 17.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(-1682.0 * scale[0], -14.0 * scale[1], 0, 0)
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
    Moveto_r(605.0 * scale[0], -10.0 * scale[1], 0, 0)
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
    Moveto_r(1135.0 * scale[0], -10.0 * scale[1], 0, 0)
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
    Moveto_r(-3695.0 * scale[0], -20.0 * scale[1], 0, 0)
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
    Moveto_r(2540.0 * scale[0], 6.0 * scale[1], 0, 0)
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
    Moveto_r(314.0 * scale[0], -12.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -24.0 * scale[1], 2.0 * scale[0], -
              26.0 * scale[1], -12.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 11.0 * scale[1], -8.0 * scale[0],
              20.0 * scale[1], -3.0 * scale[0], 20.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0], -
              7.0 * scale[1], 15.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto_r(-923.0 * scale[0], -37.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -9.0 * scale[1], -11.0 *
              scale[0], -8.0 * scale[1], -5.0 * scale[0], 6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 10.0 * scale[1], 9.0 * scale[0],
              15.0 * scale[1], 12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 0.0 * scale[0], -
              11.0 * scale[1], -7.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto_r(986.0 * scale[0], -53.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -5.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 17.0 * scale[0], -
              2.0 * scale[1], 13.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto_r(663.0 * scale[0], -34.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              10.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0],
              5.0 * scale[1], -11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -1.0 * scale[0],
              10.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0], -
              4.0 * scale[1], 11.0 * scale[0], -10.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#5ed6f3')
    te.end_fill()
    Moveto(0.0 * scale[0], 3775.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(0.0 * scale[0], -725.0 * scale[1])
    Lineto_r(2250.0 * scale[0], 0.0 * scale[1])
    Lineto_r(2250.0 * scale[0], 0.0 * scale[1])
    Lineto_r(0.0 * scale[0], 725.0 * scale[1])
    Lineto_r(0.0 * scale[0], 725.0 * scale[1])
    Lineto_r(-2250.0 * scale[0], 0.0 * scale[1])
    Lineto_r(-2250.0 * scale[0], 0.0 * scale[1])
    Lineto_r(0.0 * scale[0], -725.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#74ecdb')
    te.end_fill()
    Moveto(0.0 * scale[0], 2431.0 * scale[1], x, y)
    te.begin_fill()
    Lineto_r(0.0 * scale[0], -619.0 * scale[1])
    Lineto_r(63.0 * scale[0], -4.0 * scale[1])
    Curveto_r(34.0 * scale[0], -3.0 * scale[1], 136.0 *
              scale[0], -6.0 * scale[1], 227.0 * scale[0], -7.0 * scale[1])
    Curveto_r(91.0 * scale[0], -1.0 * scale[1], 329.0 * scale[0], -
              6.0 * scale[1], 530.0 * scale[0], -12.0 * scale[1])
    Curveto_r(452.0 * scale[0], -12.0 * scale[1], 454.0 *
              scale[0], -12.0 * scale[1], 480.0 * scale[0], -4.0 * scale[1])
    Curveto_r(29.0 * scale[0], 9.0 * scale[1], 250.0 * scale[0],
              22.0 * scale[1], 250.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 19.0 * scale[0], -
              9.0 * scale[1], 42.0 * scale[0], -13.0 * scale[1])
    Curveto_r(64.0 * scale[0], -10.0 * scale[1], 174.0 * scale[0], -
              50.0 * scale[1], 339.0 * scale[0], -121.0 * scale[1])
    Curveto_r(82.0 * scale[0], -36.0 * scale[1], 152.0 * scale[0], -
              65.0 * scale[1], 155.0 * scale[0], -65.0 * scale[1])
    Curveto_r(3.0 * scale[0], 0.0 * scale[1], 2.0 * scale[0],
              6.0 * scale[1], -2.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], 12.0 * scale[0], -4.0 * scale[1])
    Curveto_r(31.0 * scale[0], -26.0 * scale[1], 44.0 * scale[0], -
              28.0 * scale[1], 271.0 * scale[0], -34.0 * scale[1])
    Curveto_r(120.0 * scale[0], -3.0 * scale[1], 268.0 *
              scale[0], -8.0 * scale[1], 328.0 * scale[0], -10.0 * scale[1])
    Curveto_r(213.0 * scale[0], -11.0 * scale[1], 305.0 *
              scale[0], -8.0 * scale[1], 325.0 * scale[0], 10.0 * scale[1])
    Curveto_r(9.0 * scale[0], 8.0 * scale[1], 32.0 * scale[0],
              20.0 * scale[1], 51.0 * scale[0], 25.0 * scale[1])
    Curveto_r(31.0 * scale[0], 9.0 * scale[1], 32.0 * scale[0],
              8.0 * scale[1], 15.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -8.0 * scale[1], -25.0 * scale[0], -
              15.0 * scale[1], -32.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0], -
              7.0 * scale[1], -24.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -20.0 * scale[1], -11.0 *
              scale[0], -19.0 * scale[1], 47.0 * scale[0], 6.0 * scale[1])
    Curveto_r(152.0 * scale[0], 66.0 * scale[1], 177.0 * scale[0],
              71.0 * scale[1], 393.0 * scale[0], 80.0 * scale[1])
    Curveto_r(113.0 * scale[0], 4.0 * scale[1], 212.0 * scale[0],
              8.0 * scale[1], 220.0 * scale[0], 9.0 * scale[1])
    Curveto_r(24.0 * scale[0], 3.0 * scale[1], 173.0 * scale[0],
              41.0 * scale[1], 195.0 * scale[0], 50.0 * scale[1])
    Curveto_r(58.0 * scale[0], 24.0 * scale[1], 248.0 * scale[0],
              43.0 * scale[1], 428.0 * scale[0], 42.0 * scale[1])
    Lineto_r(187.0 * scale[0], -1.0 * scale[1])
    Lineto_r(0.0 * scale[0], 650.0 * scale[1])
    Lineto_r(0.0 * scale[0], 649.0 * scale[1])
    Lineto_r(-2250.0 * scale[0], 0.0 * scale[1])
    Lineto_r(-2250.0 * scale[0], 0.0 * scale[1])
    Lineto_r(0.0 * scale[0], -619.0 * scale[1])
    te.end_fill()
    Moveto(0.0 * scale[0], 1752.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -32.0 * scale[1], 16.0 * scale[0], -
              40.0 * scale[1], 110.0 * scale[0], -57.0 * scale[1])
    Curveto_r(52.0 * scale[0], -9.0 * scale[1], 118.0 * scale[0], -
              20.0 * scale[1], 145.0 * scale[0], -25.0 * scale[1])
    Curveto_r(28.0 * scale[0], -5.0 * scale[1], 133.0 * scale[0], -
              11.0 * scale[1], 235.0 * scale[0], -14.0 * scale[1])
    Curveto_r(176.0 * scale[0], -5.0 * scale[1], 181.0 *
              scale[0], -5.0 * scale[1], 110.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-41.0 * scale[0], 7.0 * scale[1], -140.0 * scale[0],
              16.0 * scale[1], -220.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-179.0 * scale[0], 8.0 * scale[1], -249.0 * scale[0],
              20.0 * scale[1], -322.0 * scale[0], 57.0 * scale[1])
    Curveto_r(-49.0 * scale[0], 24.0 * scale[1], -58.0 * scale[0],
              26.0 * scale[1], -58.0 * scale[0], 12.0 * scale[1])
    te.end_fill()
    Moveto(2910.0 * scale[0], 1526.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-45.0 * scale[0], -12.0 * scale[1], -93.0 *
              scale[0], -35.0 * scale[1], -75.0 * scale[0], -36.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 147.0 * scale[0],
              38.0 * scale[1], 153.0 * scale[0], 45.0 * scale[1])
    Curveto_r(9.0 * scale[0], 9.0 * scale[1], -30.0 * scale[0],
              4.0 * scale[1], -78.0 * scale[0], -9.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#f6c67b')
    te.end_fill()
    Moveto(7.0 * scale[0], 1513.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -3.0 * scale[1], -7.0 * scale[0], -
              62.0 * scale[1], -7.0 * scale[0], -130.0 * scale[1])
    Lineto_r(0.0 * scale[0], -123.0 * scale[1])
    Lineto_r(68.0 * scale[0], 0.0 * scale[1])
    Curveto_r(78.0 * scale[0], 0.0 * scale[1], 189.0 * scale[0], -
              19.0 * scale[1], 322.0 * scale[0], -54.0 * scale[1])
    Curveto_r(52.0 * scale[0], -14.0 * scale[1], 103.0 * scale[0], -
              28.0 * scale[1], 113.0 * scale[0], -30.0 * scale[1])
    Curveto_r(20.0 * scale[0], -6.0 * scale[1], 73.0 * scale[0], -
              22.0 * scale[1], 132.0 * scale[0], -42.0 * scale[1])
    Curveto_r(22.0 * scale[0], -7.0 * scale[1], 51.0 * scale[0], -
              15.0 * scale[1], 65.0 * scale[0], -18.0 * scale[1])
    Curveto_r(14.0 * scale[0], -3.0 * scale[1], 50.0 * scale[0], -
              10.0 * scale[1], 80.0 * scale[0], -16.0 * scale[1])
    Curveto_r(143.0 * scale[0], -28.0 * scale[1], 416.0 *
              scale[0], -41.0 * scale[1], 543.0 * scale[0], -25.0 * scale[1])
    Curveto_r(33.0 * scale[0], 4.0 * scale[1], 54.0 * scale[0],
              2.0 * scale[1], 65.0 * scale[0], -7.0 * scale[1])
    Curveto_r(12.0 * scale[0], -10.0 * scale[1], 14.0 *
              scale[0], -10.0 * scale[1], 8.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 8.0 * scale[1], 0.0 * scale[0],
              12.0 * scale[1], 14.0 * scale[0], 12.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0], -
              4.0 * scale[1], 14.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -3.0 *
              scale[0], -8.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 12.0 * scale[0],
              3.0 * scale[1], 15.0 * scale[0], -1.0 * scale[1])
    Curveto_r(2.0 * scale[0], -5.0 * scale[1], 2.0 *
              scale[0], -2.0 * scale[1], 1.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 13.0 * scale[1], 16.0 * scale[0],
              20.0 * scale[1], 78.0 * scale[0], 25.0 * scale[1])
    Curveto_r(20.0 * scale[0], 2.0 * scale[1], 34.0 * scale[0],
              0.0 * scale[1], 32.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], 2.0 * scale[0], -
              8.0 * scale[1], 11.0 * scale[0], -8.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              5.0 * scale[1], 10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 6.0 * scale[1], 9.0 * scale[0],
              11.0 * scale[1], 32.0 * scale[0], 12.0 * scale[1])
    Curveto_r(62.0 * scale[0], 3.0 * scale[1], 77.0 * scale[0],
              5.0 * scale[1], 97.0 * scale[0], 13.0 * scale[1])
    Curveto_r(47.0 * scale[0], 20.0 * scale[1], 197.0 * scale[0],
              42.0 * scale[1], 272.0 * scale[0], 39.0 * scale[1])
    Curveto_r(74.0 * scale[0], -3.0 * scale[1], 253.0 * scale[0], -
              42.0 * scale[1], 295.0 * scale[0], -64.0 * scale[1])
    Curveto_r(31.0 * scale[0], -17.0 * scale[1], 218.0 * scale[0], -
              50.0 * scale[1], 282.0 * scale[0], -50.0 * scale[1])
    Curveto_r(64.0 * scale[0], 0.0 * scale[1], 174.0 * scale[0],
              17.0 * scale[1], 292.0 * scale[0], 45.0 * scale[1])
    Curveto_r(92.0 * scale[0], 21.0 * scale[1], 164.0 * scale[0],
              33.0 * scale[1], 234.0 * scale[0], 40.0 * scale[1])
    Curveto_r(35.0 * scale[0], 3.0 * scale[1], 67.0 * scale[0],
              7.0 * scale[1], 70.0 * scale[0], 9.0 * scale[1])
    Curveto_r(3.0 * scale[0], 2.0 * scale[1], 65.0 * scale[0],
              16.0 * scale[1], 136.0 * scale[0], 32.0 * scale[1])
    Curveto_r(94.0 * scale[0], 20.0 * scale[1], 157.0 * scale[0],
              28.0 * scale[1], 227.0 * scale[0], 28.0 * scale[1])
    Curveto_r(89.0 * scale[0], -1.0 * scale[1], 210.0 * scale[0], -
              18.0 * scale[1], 233.0 * scale[0], -34.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 24.0 * scale[0], -
              7.0 * scale[1], 40.0 * scale[0], -8.0 * scale[1])
    Curveto_r(17.0 * scale[0], -1.0 * scale[1], 62.0 * scale[0], -
              11.0 * scale[1], 100.0 * scale[0], -21.0 * scale[1])
    Curveto_r(39.0 * scale[0], -10.0 * scale[1], 102.0 * scale[0], -
              24.0 * scale[1], 142.0 * scale[0], -31.0 * scale[1])
    Curveto_r(52.0 * scale[0], -10.0 * scale[1], 70.0 * scale[0], -
              16.0 * scale[1], 66.0 * scale[0], -26.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], 0.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -14.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              7.0 * scale[1], 11.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], 5.0 * scale[0],
              15.0 * scale[1], 10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              4.0 * scale[1], 10.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              10.0 * scale[1], 15.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              5.0 * scale[1], 15.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 7.0 * scale[0],
              10.0 * scale[1], 16.0 * scale[0], 10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0], -
              4.0 * scale[1], 9.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              10.0 * scale[1], 17.0 * scale[0], -10.0 * scale[1])
    Curveto_r(19.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0],
              2.0 * scale[1], 8.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 8.0 * scale[1], -9.0 * scale[0],
              10.0 * scale[1], 12.0 * scale[0], 6.0 * scale[1])
    Curveto_r(15.0 * scale[0], -2.0 * scale[1], 29.0 *
              scale[0], -1.0 * scale[1], 30.0 * scale[0], 4.0 * scale[1])
    Curveto_r(2.0 * scale[0], 4.0 * scale[1], 19.0 * scale[0],
              9.0 * scale[1], 38.0 * scale[0], 12.0 * scale[1])
    Curveto_r(43.0 * scale[0], 5.0 * scale[1], 157.0 * scale[0],
              58.0 * scale[1], 188.0 * scale[0], 87.0 * scale[1])
    Curveto_r(19.0 * scale[0], 18.0 * scale[1], 22.0 * scale[0],
              31.0 * scale[1], 22.0 * scale[0], 99.0 * scale[1])
    Curveto_r(0.0 * scale[0], 87.0 * scale[1], 1.0 * scale[0],
              86.0 * scale[1], -99.0 * scale[0], 117.0 * scale[1])
    Curveto_r(-39.0 * scale[0], 12.0 * scale[1], -48.0 * scale[0],
              11.0 * scale[1], -80.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-36.0 * scale[0], -18.0 * scale[1], -36.0 *
              scale[0], -18.0 * scale[1], -64.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-33.0 * scale[0], 28.0 * scale[1], -46.0 * scale[0],
              30.0 * scale[1], -73.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-41.0 * scale[0], -31.0 * scale[1], -104.0 *
              scale[0], -9.0 * scale[1], -104.0 * scale[0], 36.0 * scale[1])
    Lineto_r(0.0 * scale[0], 23.0 * scale[1])
    Lineto_r(-15.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -20.0 * scale[1], -17.0 *
              scale[0], -20.0 * scale[1], -44.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 12.0 * scale[1], -34.0 * scale[0],
              12.0 * scale[1], -71.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-23.0 * scale[0], -8.0 * scale[1], -59.0 * scale[0], -
              15.0 * scale[1], -80.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 0.0 * scale[1], -53.0 * scale[0], -
              6.0 * scale[1], -71.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-30.0 * scale[0], -13.0 * scale[1], -37.0 *
              scale[0], -12.0 * scale[1], -69.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 9.0 * scale[1], -56.0 * scale[0],
              20.0 * scale[1], -82.0 * scale[0], 23.0 * scale[1])
    Curveto_r(-47.0 * scale[0], 7.0 * scale[1], -48.0 * scale[0],
              6.0 * scale[1], -72.0 * scale[0], -32.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -33.0 * scale[1], -35.0 * scale[0], -
              41.0 * scale[1], -108.0 * scale[0], -65.0 * scale[1])
    Curveto_r(-55.0 * scale[0], -18.0 * scale[1], -114.0 *
              scale[0], -30.0 * scale[1], -173.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-83.0 * scale[0], -5.0 * scale[1], -92.0 *
              scale[0], -4.0 * scale[1], -109.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 28.0 * scale[1], -44.0 * scale[0],
              27.0 * scale[1], -78.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-27.0 * scale[0], -26.0 * scale[1], -29.0 *
              scale[0], -26.0 * scale[1], -62.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-56.0 * scale[0], 26.0 * scale[1], -108.0 * scale[0],
              4.0 * scale[1], -165.0 * scale[0], -73.0 * scale[1])
    Curveto_r(-21.0 * scale[0], -29.0 * scale[1], -88.0 * scale[0], -
              49.0 * scale[1], -161.0 * scale[0], -49.0 * scale[1])
    Curveto_r(-29.0 * scale[0], 0.0 * scale[1], -63.0 * scale[0], -
              9.0 * scale[1], -101.0 * scale[0], -29.0 * scale[1])
    Lineto_r(-57.0 * scale[0], -29.0 * scale[1])
    Lineto_r(-63.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-35.0 * scale[0], 11.0 * scale[1], -99.0 * scale[0],
              37.0 * scale[1], -141.0 * scale[0], 59.0 * scale[1])
    Curveto_r(-65.0 * scale[0], 32.0 * scale[1], -82.0 * scale[0],
              37.0 * scale[1], -103.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-47.0 * scale[0], -18.0 * scale[1], -61.0 *
              scale[0], -12.0 * scale[1], -78.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 30.0 * scale[1], -21.0 * scale[0],
              40.0 * scale[1], -39.0 * scale[0], 41.0 * scale[1])
    Curveto_r(-28.0 * scale[0], 1.0 * scale[1], -59.0 * scale[0],
              6.0 * scale[1], -62.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 2.0 * scale[1], -10.0 * scale[0],
              15.0 * scale[1], -19.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 23.0 * scale[1], -24.0 * scale[0],
              27.0 * scale[1], -65.0 * scale[0], 27.0 * scale[1])
    Curveto_r(-77.0 * scale[0], 0.0 * scale[1], -211.0 * scale[0],
              27.0 * scale[1], -238.0 * scale[0], 49.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 10.0 * scale[1], -47.0 * scale[0],
              22.0 * scale[1], -75.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-32.0 * scale[0], 4.0 * scale[1], -61.0 * scale[0],
              16.0 * scale[1], -81.0 * scale[0], 33.0 * scale[1])
    Curveto_r(-30.0 * scale[0], 26.0 * scale[1], -31.0 * scale[0],
              26.0 * scale[1], -62.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-100.0 * scale[0], -58.0 * scale[1], -173.0 *
              scale[0], -89.0 * scale[1], -229.0 * scale[0], -96.0 * scale[1])
    Curveto_r(-75.0 * scale[0], -10.0 * scale[1], -119.0 *
              scale[0], -23.0 * scale[1], -149.0 * scale[0], -44.0 * scale[1])
    Curveto_r(-29.0 * scale[0], -20.0 * scale[1], -49.0 *
              scale[0], -20.0 * scale[1], -86.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-27.0 * scale[0], 15.0 * scale[1], -36.0 * scale[0],
              16.0 * scale[1], -79.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-26.0 * scale[0], -7.0 * scale[1], -59.0 * scale[0], -
              24.0 * scale[1], -74.0 * scale[0], -38.0 * scale[1])
    Curveto_r(-34.0 * scale[0], -32.0 * scale[1], -49.0 *
              scale[0], -30.0 * scale[1], -82.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 30.0 * scale[1], -33.0 * scale[0],
              34.0 * scale[1], -57.0 * scale[0], 29.0 * scale[1])
    Curveto_r(-66.0 * scale[0], -14.0 * scale[1], -187.0 *
              scale[0], -7.0 * scale[1], -235.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-26.0 * scale[0], 12.0 * scale[1], -65.0 * scale[0],
              21.0 * scale[1], -87.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 0.0 * scale[1], -57.0 * scale[0],
              9.0 * scale[1], -79.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-31.0 * scale[0], 15.0 * scale[1], -51.0 * scale[0],
              19.0 * scale[1], -80.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-35.0 * scale[0], -6.0 * scale[1], -41.0 *
              scale[0], -4.0 * scale[1], -73.0 * scale[0], 30.0 * scale[1])
    Lineto_r(-34.0 * scale[0], 38.0 * scale[1])
    Lineto_r(-45.0 * scale[0], -23.0 * scale[1])
    Lineto_r(-46.0 * scale[0], -23.0 * scale[1])
    Lineto_r(-36.0 * scale[0], 31.0 * scale[1])
    Curveto_r(-37.0 * scale[0], 33.0 * scale[1], -47.0 * scale[0],
              37.0 * scale[1], -58.0 * scale[0], 25.0 * scale[1])
    te.end_fill()
    Moveto(3405.0 * scale[0], 1170.0 * scale[1], x, y)
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
    Moveto(3455.0 * scale[0], 1170.0 * scale[1], x, y)
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
    Moveto(514.0 * scale[0], 1135.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(19.0 * scale[0], -76.0 * scale[1], 20.0 * scale[0], -
              72.0 * scale[1], -18.0 * scale[0], -79.0 * scale[1])
    Curveto_r(-48.0 * scale[0], -9.0 * scale[1], -46.0 *
              scale[0], -26.0 * scale[1], 3.0 * scale[0], -26.0 * scale[1])
    Lineto_r(39.0 * scale[0], 0.0 * scale[1])
    Lineto_r(-5.0 * scale[0], -40.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -50.0 * scale[1], 11.0 *
              scale[0], -53.0 * scale[1], 27.0 * scale[0], -5.0 * scale[1])
    Curveto_r(6.0 * scale[0], 19.0 * scale[1], 13.0 * scale[0],
              35.0 * scale[1], 15.0 * scale[0], 35.0 * scale[1])
    Curveto_r(1.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0], -
              7.0 * scale[1], 39.0 * scale[0], -15.0 * scale[1])
    Curveto_r(44.0 * scale[0], -18.0 * scale[1], 47.0 *
              scale[0], -4.0 * scale[1], 6.0 * scale[0], 25.0 * scale[1])
    Lineto_r(-30.0 * scale[0], 21.0 * scale[1])
    Lineto_r(26.0 * scale[0], 35.0 * scale[1])
    Curveto_r(30.0 * scale[0], 39.0 * scale[1], 25.0 * scale[0],
              42.0 * scale[1], -22.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -11.0 * scale[1], -34.0 *
              scale[0], -17.0 * scale[1], -34.0 * scale[0], -12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], -12.0 * scale[0],
              22.0 * scale[1], -26.0 * scale[0], 38.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 23.0 * scale[1], -24.0 * scale[0],
              25.0 * scale[1], -20.0 * scale[0], 10.0 * scale[1])
    te.end_fill()
    Moveto(3370.0 * scale[0], 1125.0 * scale[1], x, y)
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
    Moveto(1836.0 * scale[0], 1109.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-31.0 * scale[0], -24.0 * scale[1], -34.0 *
              scale[0], -39.0 * scale[1], -6.0 * scale[0], -32.0 * scale[1])
    Curveto_r(11.0 * scale[0], 3.0 * scale[1], 17.0 * scale[0],
              9.0 * scale[1], 14.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], 5.0 * scale[0],
              13.0 * scale[1], 17.0 * scale[0], 17.0 * scale[1])
    Curveto_r(13.0 * scale[0], 5.0 * scale[1], 18.0 * scale[0],
              11.0 * scale[1], 12.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 4.0 * scale[1], -22.0 * scale[0], -
              3.0 * scale[1], -37.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(3725.0 * scale[0], 1110.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -6.0 * scale[1], -15.0 *
              scale[0], -9.0 * scale[1], -5.0 * scale[0], -9.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 22.0 * scale[0],
              4.0 * scale[1], 30.0 * scale[0], 9.0 * scale[1])
    Curveto_r(18.0 * scale[0], 12.0 * scale[1], 2.0 * scale[0],
              12.0 * scale[1], -25.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(3813.0 * scale[0], 1105.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -11.0 * scale[1], -9.0 *
              scale[0], -13.0 * scale[1], 6.0 * scale[0], -12.0 * scale[1])
    Curveto_r(11.0 * scale[0], 1.0 * scale[1], 17.0 * scale[0],
              7.0 * scale[1], 14.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 16.0 * scale[1], -5.0 * scale[0],
              16.0 * scale[1], -20.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(1748.0 * scale[0], 1103.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(3900.0 * scale[0], 1098.0 * scale[1], x, y)
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
    Moveto(3985.0 * scale[0], 1090.0 * scale[1], x, y)
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
    Moveto(1661.0 * scale[0], 1074.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(4036.0 * scale[0], 1077.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -9.0 * scale[1], 14.0 * scale[0], -
              15.0 * scale[1], 25.0 * scale[0], -14.0 * scale[1])
    Curveto_r(19.0 * scale[0], 1.0 * scale[1], 28.0 * scale[0],
              17.0 * scale[1], 10.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0],
              3.0 * scale[1], -25.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 5.0 * scale[1], -15.0 * scale[0],
              2.0 * scale[1], -10.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(3881.0 * scale[0], 1064.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(2005.0 * scale[0], 1060.0 * scale[1], x, y)
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
    Moveto(997.0 * scale[0], 1045.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], 9.0 * scale[0], -
              12.0 * scale[1], 14.0 * scale[0], -9.0 * scale[1])
    Curveto_r(12.0 * scale[0], 7.0 * scale[1], 11.0 * scale[0],
              11.0 * scale[1], -5.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 4.0 * scale[1], -13.0 * scale[0],
              1.0 * scale[1], -9.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(1130.0 * scale[0], 1050.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 5.0 * scale[0], -
              10.0 * scale[1], 12.0 * scale[0], -10.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0], -
              3.0 * scale[1], 0.0 * scale[0], -12.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -8.0 * scale[1], -15.0 *
              scale[0], -8.0 * scale[1], -27.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 16.0 * scale[1], -20.0 * scale[0],
              4.0 * scale[1], -1.0 * scale[0], -15.0 * scale[1])
    Curveto_r(12.0 * scale[0], -12.0 * scale[1], 16.0 *
              scale[0], -11.0 * scale[1], 30.0 * scale[0], 4.0 * scale[1])
    Curveto_r(20.0 * scale[0], 22.0 * scale[1], 20.0 * scale[0],
              27.0 * scale[1], 1.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -15.0 * scale[0],
              1.0 * scale[1], -15.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(1220.0 * scale[0], 1051.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 24.0 * scale[0], -
              21.0 * scale[1], 43.0 * scale[0], -21.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 2.0 * scale[0],
              7.0 * scale[1], -9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 17.0 * scale[1], -34.0 * scale[0],
              19.0 * scale[1], -34.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(4000.0 * scale[0], 1050.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], -8.0 * scale[0], -
              10.0 * scale[1], -17.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 0.0 * scale[1], -15.0 *
              scale[0], -2.0 * scale[1], 2.0 * scale[0], -14.0 * scale[1])
    Curveto_r(16.0 * scale[0], -11.0 * scale[1], 21.0 *
              scale[0], -11.0 * scale[1], 33.0 * scale[0], 0.0 * scale[1])
    Curveto_r(7.0 * scale[0], 8.0 * scale[1], 10.0 * scale[0],
              18.0 * scale[1], 7.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 13.0 * scale[1], -25.0 * scale[0],
              13.0 * scale[1], -25.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(4120.0 * scale[0], 1050.0 * scale[1], x, y)
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
    Moveto(845.0 * scale[0], 1040.0 * scale[1], x, y)
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
    Moveto(1280.0 * scale[0], 1039.0 * scale[1], x, y)
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
    Moveto(1033.0 * scale[0], 1024.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -9.0 * scale[1], -10.0 * scale[0], -
              15.0 * scale[1], -2.0 * scale[0], -20.0 * scale[1])
    Curveto_r(14.0 * scale[0], -8.0 * scale[1], 30.0 * scale[0],
              8.0 * scale[1], 21.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 9.0 * scale[1], -10.0 * scale[0],
              8.0 * scale[1], -19.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(1408.0 * scale[0], 1023.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(3876.0 * scale[0], 1022.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 16.0 * scale[0], -
              16.0 * scale[1], 23.0 * scale[0], -27.0 * scale[1])
    Curveto_r(10.0 * scale[0], -17.0 * scale[1], 12.0 *
              scale[0], -17.0 * scale[1], 7.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 10.0 * scale[1], -6.0 * scale[0],
              23.0 * scale[1], -6.0 * scale[0], 28.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -8.0 * scale[0],
              9.0 * scale[1], -17.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -7.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(4255.0 * scale[0], 1020.0 * scale[1], x, y)
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
    Moveto(4340.0 * scale[0], 1020.0 * scale[1], x, y)
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
    Moveto(825.0 * scale[0], 1009.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -14.0 * scale[1], -2.0 * scale[0], -
              20.0 * scale[1], 14.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 6.0 * scale[1], 9.0 * scale[0],
              11.0 * scale[1], 3.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -14.0 * scale[0],
              1.0 * scale[1], -17.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(1236.0 * scale[0], 1004.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -10.0 * scale[1], -1.0 *
              scale[0], -14.0 * scale[1], 6.0 * scale[0], -12.0 * scale[1])
    Curveto_r(15.0 * scale[0], 5.0 * scale[1], 23.0 * scale[0],
              28.0 * scale[1], 10.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              7.0 * scale[1], -16.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(1775.0 * scale[0], 1009.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -17.0 * scale[1], 1.0 *
              scale[0], -21.0 * scale[1], 15.0 * scale[0], -4.0 * scale[1])
    Curveto_r(8.0 * scale[0], 9.0 * scale[1], 8.0 * scale[0],
              15.0 * scale[1], 2.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0], -
              5.0 * scale[1], -17.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(4060.0 * scale[0], 1016.0 * scale[1], x, y)
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
    Moveto(950.0 * scale[0], 996.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 13.0 *
              scale[0], -7.0 * scale[1], 20.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 6.0 * scale[1], 3.0 * scale[0],
              10.0 * scale[1], -10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0], -
              4.0 * scale[1], -10.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(1341.0 * scale[0], 994.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(1430.0 * scale[0], 999.0 * scale[1], x, y)
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
    Moveto(1554.0 * scale[0], 999.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -15.0 * scale[1], 20.0 *
              scale[0], -13.0 * scale[1], 24.0 * scale[0], 3.0 * scale[1])
    Curveto_r(3.0 * scale[0], 10.0 * scale[1], 2.0 * scale[0],
              10.0 * scale[1], -6.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -9.0 * scale[1], -11.0 * scale[0], -
              10.0 * scale[1], -15.0 * scale[0], -2.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 7.0 * scale[1], -5.0 * scale[0],
              8.0 * scale[1], -3.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(1620.0 * scale[0], 1002.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -12.0 * scale[1], 19.0 * scale[0], -
              26.0 * scale[1], 26.0 * scale[0], -19.0 * scale[1])
    Curveto_r(2.0 * scale[0], 2.0 * scale[1], -2.0 * scale[0],
              10.0 * scale[1], -11.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 8.0 * scale[1], -15.0 * scale[0],
              8.0 * scale[1], -15.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(1705.0 * scale[0], 1000.0 * scale[1], x, y)
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
    Moveto(1735.0 * scale[0], 1000.0 * scale[1], x, y)
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
    Moveto(3685.0 * scale[0], 1000.0 * scale[1], x, y)
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
    Moveto(1150.0 * scale[0], 989.0 * scale[1], x, y)
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
    Moveto(1195.0 * scale[0], 990.0 * scale[1], x, y)
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
    Moveto(1293.0 * scale[0], 992.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -2.0 * scale[1], -23.0 *
              scale[0], -7.0 * scale[1], -23.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 24.0 * scale[0], -
              31.0 * scale[1], 45.0 * scale[0], -31.0 * scale[1])
    Curveto_r(19.0 * scale[0], 1.0 * scale[1], 19.0 * scale[0],
              1.0 * scale[1], 2.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 10.0 * scale[1], -15.0 * scale[0],
              15.0 * scale[1], -5.0 * scale[0], 19.0 * scale[1])
    Curveto_r(20.0 * scale[0], 7.0 * scale[1], 6.0 * scale[0],
              13.0 * scale[1], -19.0 * scale[0], 9.0 * scale[1])
    te.end_fill()
    Moveto(4174.0 * scale[0], 979.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(20.0 * scale[0], -16.0 * scale[1], 30.0 * scale[0], -
              19.0 * scale[1], 39.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 8.0 * scale[1], 5.0 * scale[0],
              11.0 * scale[1], -10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -25.0 * scale[0],
              5.0 * scale[1], -28.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -11.0 * scale[0],
              10.0 * scale[1], -17.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], 1.0 * scale[0], -
              10.0 * scale[1], 16.0 * scale[0], -21.0 * scale[1])
    te.end_fill()
    Moveto(1370.0 * scale[0], 979.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 11.0 * scale[0], -
              15.0 * scale[1], 25.0 * scale[0], -15.0 * scale[1])
    Curveto_r(14.0 * scale[0], -1.0 * scale[1], 25.0 * scale[0],
              2.0 * scale[1], 25.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -4.0 * scale[0],
              9.0 * scale[1], -9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0],
              3.0 * scale[1], -25.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 4.0 * scale[1], -16.0 * scale[0],
              1.0 * scale[1], -16.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(1485.0 * scale[0], 980.0 * scale[1], x, y)
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
    Moveto(1003.0 * scale[0], 965.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -10.0 * scale[1], -9.0 *
              scale[0], -14.0 * scale[1], 2.0 * scale[0], -19.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 17.0 * scale[0],
              0.0 * scale[1], 21.0 * scale[0], 6.0 * scale[1])
    Curveto_r(4.0 * scale[0], 7.0 * scale[1], 9.0 * scale[0],
              6.0 * scale[1], 15.0 * scale[0], -3.0 * scale[1])
    Curveto_r(4.0 * scale[0], -7.0 * scale[1], 11.0 * scale[0], -
              10.0 * scale[1], 15.0 * scale[0], -7.0 * scale[1])
    Curveto_r(7.0 * scale[0], 8.0 * scale[1], -15.0 * scale[0],
              32.0 * scale[1], -31.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0], -
              5.0 * scale[1], -22.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(1086.0 * scale[0], 958.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -13.0 * scale[1], -6.0 * scale[0], -
              33.0 * scale[1], -6.0 * scale[0], -46.0 * scale[1])
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], -8.0 * scale[0], -
              26.0 * scale[1], -22.0 * scale[0], -32.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -6.0 * scale[1], -18.0 *
              scale[0], -9.0 * scale[1], -7.0 * scale[0], -9.0 * scale[1])
    Curveto_r(9.0 * scale[0], -1.0 * scale[1], 22.0 * scale[0], -
              8.0 * scale[1], 29.0 * scale[0], -16.0 * scale[1])
    Curveto_r(7.0 * scale[0], -8.0 * scale[1], 16.0 * scale[0], -
              12.0 * scale[1], 21.0 * scale[0], -9.0 * scale[1])
    Curveto_r(15.0 * scale[0], 9.0 * scale[1], 10.0 * scale[0],
              24.0 * scale[1], -8.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-15.0 * scale[0], 0.0 * scale[1], -15.0 * scale[0],
              1.0 * scale[1], 0.0 * scale[0], 18.0 * scale[1])
    Curveto_r(11.0 * scale[0], 12.0 * scale[1], 13.0 * scale[0],
              22.0 * scale[1], 7.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              15.0 * scale[1], 1.0 * scale[0], 24.0 * scale[1])
    Curveto_r(8.0 * scale[0], 12.0 * scale[1], 12.0 * scale[0],
              12.0 * scale[1], 16.0 * scale[0], 2.0 * scale[1])
    Curveto_r(4.0 * scale[0], -10.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(11.0 * scale[0], 9.0 * scale[1], 14.0 * scale[0],
              8.0 * scale[1], 14.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -5.0 * scale[0], -
              17.0 * scale[1], -12.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -3.0 * scale[1], -8.0 *
              scale[0], -9.0 * scale[1], 0.0 * scale[0], -24.0 * scale[1])
    Curveto_r(10.0 * scale[0], -17.0 * scale[1], 11.0 *
              scale[0], -17.0 * scale[1], 12.0 * scale[0], -1.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], 5.0 * scale[0],
              17.0 * scale[1], 11.0 * scale[0], 17.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              6.0 * scale[1], 6.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              19.0 * scale[1], 10.0 * scale[0], 29.0 * scale[1])
    Curveto_r(13.0 * scale[0], 15.0 * scale[1], 11.0 * scale[0],
              16.0 * scale[1], -22.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-28.0 * scale[0], -6.0 * scale[1], -38.0 *
              scale[0], -5.0 * scale[1], -42.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 21.0 * scale[1], -20.0 * scale[0],
              17.0 * scale[1], -27.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(1210.0 * scale[0], 970.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-20.0 * scale[0], -12.0 * scale[1], -9.0 *
              scale[0], -21.0 * scale[1], 18.0 * scale[0], -13.0 * scale[1])
    Curveto_r(12.0 * scale[0], 3.0 * scale[1], 19.0 * scale[0],
              9.0 * scale[1], 16.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 11.0 * scale[1], -15.0 * scale[0],
              11.0 * scale[1], -34.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(1875.0 * scale[0], 968.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -8.0 * scale[1], -19.0 *
              scale[0], -8.0 * scale[1], 2.0 * scale[0], -4.0 * scale[1])
    Curveto_r(12.0 * scale[0], 2.0 * scale[1], 24.0 * scale[0], -
              1.0 * scale[1], 26.0 * scale[0], -7.0 * scale[1])
    Curveto_r(2.0 * scale[0], -8.0 * scale[1], 5.0 * scale[0], -
              8.0 * scale[1], 10.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 15.0 * scale[1], -14.0 * scale[0],
              22.0 * scale[1], -38.0 * scale[0], 11.0 * scale[1])
    te.end_fill()
    Moveto(4110.0 * scale[0], 960.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -11.0 * scale[1], 27.0 * scale[0], -
              17.0 * scale[1], 32.0 * scale[0], -14.0 * scale[1])
    Curveto_r(14.0 * scale[0], 9.0 * scale[1], -12.0 * scale[0],
              34.0 * scale[1], -35.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -1.0 * scale[1], 3.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(1340.0 * scale[0], 960.0 * scale[1], x, y)
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
    Moveto(4035.0 * scale[0], 959.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-11.0 * scale[0], -16.0 * scale[1], -1.0 *
              scale[0], -19.0 * scale[1], 13.0 * scale[0], -3.0 * scale[1])
    Curveto_r(7.0 * scale[0], 8.0 * scale[1], 8.0 * scale[0],
              14.0 * scale[1], 3.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              5.0 * scale[1], -16.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(4346.0 * scale[0], 953.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(3880.0 * scale[0], 951.0 * scale[1], x, y)
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
    Moveto(3990.0 * scale[0], 945.0 * scale[1], x, y)
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
    Moveto(1240.0 * scale[0], 940.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -8.0 * scale[1], -12.0 *
              scale[0], -10.0 * scale[1], 3.0 * scale[0], -10.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0],
              5.0 * scale[1], 17.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], -1.0 * scale[0],
              12.0 * scale[1], -20.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(1274.0 * scale[0], 928.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -13.0 * scale[1], 5.0 * scale[0], -
              27.0 * scale[1], 5.0 * scale[0], -31.0 * scale[1])
    Curveto_r(1.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0], -
              6.0 * scale[1], 10.0 * scale[0], -3.0 * scale[1])
    Curveto_r(5.0 * scale[0], 4.0 * scale[1], 11.0 * scale[0],
              0.0 * scale[1], 13.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], -7.0 * scale[1], 5.0 * scale[0],
              2.0 * scale[1], 5.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 21.0 * scale[1], -3.0 * scale[0],
              28.0 * scale[1], -9.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -10.0 * scale[1], -8.0 *
              scale[0], -8.0 * scale[1], -8.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], -4.0 * scale[0],
              17.0 * scale[1], -10.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -8.0 * scale[0], -
              10.0 * scale[1], -6.0 * scale[0], -22.0 * scale[1])
    te.end_fill()
    Moveto(4086.0 * scale[0], 942.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-2.0 * scale[0], -4.0 * scale[1], -1.0 * scale[0], -
              14.0 * scale[1], 5.0 * scale[0], -22.0 * scale[1])
    Curveto_r(7.0 * scale[0], -12.0 * scale[1], 9.0 *
              scale[0], -10.0 * scale[1], 9.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 23.0 * scale[1], -5.0 * scale[0],
              28.0 * scale[1], -14.0 * scale[0], 14.0 * scale[1])
    te.end_fill()
    Moveto(4170.0 * scale[0], 941.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -18.0 * scale[1], 18.0 * scale[0], -
              21.0 * scale[1], 30.0 * scale[0], -6.0 * scale[1])
    Curveto_r(10.0 * scale[0], 13.0 * scale[1], 9.0 * scale[0],
              15.0 * scale[1], -9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -21.0 *
              scale[0], -4.0 * scale[1], -21.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(4233.0 * scale[0], 935.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              12.0 * scale[1], 9.0 * scale[0], -9.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 6.0 * scale[0],
              10.0 * scale[1], 3.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 13.0 * scale[1], -12.0 * scale[0],
              11.0 * scale[1], -12.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(1200.0 * scale[0], 930.0 * scale[1], x, y)
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
    Moveto(1514.0 * scale[0], 924.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -9.0 * scale[1], 6.0 * scale[0], -
              18.0 * scale[1], 6.0 * scale[0], -20.0 * scale[1])
    Curveto_r(0.0 * scale[0], -3.0 * scale[1], 4.0 * scale[0], -
              3.0 * scale[1], 10.0 * scale[0], 1.0 * scale[1])
    Curveto_r(11.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              35.0 * scale[1], -12.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              7.0 * scale[1], -4.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(1583.0 * scale[0], 934.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -3.0 * scale[1], -9.0 * scale[0], -
              12.0 * scale[1], -7.0 * scale[0], -19.0 * scale[1])
    Curveto_r(4.0 * scale[0], -9.0 * scale[1], -4.0 * scale[0], -
              17.0 * scale[1], -21.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-32.0 * scale[0], -8.0 * scale[1], -24.0 *
              scale[0], -18.0 * scale[1], 15.0 * scale[0], -19.0 * scale[1])
    Curveto_r(27.0 * scale[0], -1.0 * scale[1], 28.0 * scale[0],
              1.0 * scale[1], 23.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 28.0 * scale[1], -5.0 * scale[0],
              29.0 * scale[1], 12.0 * scale[0], 15.0 * scale[1])
    Curveto_r(15.0 * scale[0], -13.0 * scale[1], 17.0 *
              scale[0], -13.0 * scale[1], 14.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 17.0 * scale[1], -18.0 * scale[0],
              22.0 * scale[1], -36.0 * scale[0], 15.0 * scale[1])
    te.end_fill()
    Moveto(4266.0 * scale[0], 925.0 * scale[1], x, y)
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
    Moveto(990.0 * scale[0], 922.0 * scale[1], x, y)
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
    Moveto(1354.0 * scale[0], 918.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -15.0 * scale[1], 39.0 *
              scale[0], -20.0 * scale[1], 53.0 * scale[0], -5.0 * scale[1])
    Curveto_r(13.0 * scale[0], 12.0 * scale[1], 11.0 * scale[0],
              14.0 * scale[1], -17.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -1.0 * scale[1], -34.0 *
              scale[0], -4.0 * scale[1], -36.0 * scale[0], -8.0 * scale[1])
    te.end_fill()
    Moveto(1450.0 * scale[0], 921.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 9.0 * scale[0], -
              7.0 * scale[1], 20.0 * scale[0], -4.0 * scale[1])
    Curveto_r(11.0 * scale[0], 3.0 * scale[1], 20.0 * scale[0],
              7.0 * scale[1], 20.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 2.0 * scale[1], -9.0 * scale[0],
              4.0 * scale[1], -20.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -20.0 *
              scale[0], -4.0 * scale[1], -20.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(3820.0 * scale[0], 926.0 * scale[1], x, y)
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
    Moveto(1631.0 * scale[0], 907.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -8.0 * scale[1], -8.0 * scale[0], -
              17.0 * scale[1], -4.0 * scale[0], -20.0 * scale[1])
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], 0.0 * scale[0], -
              15.0 * scale[1], -8.0 * scale[0], -24.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -16.0 * scale[1], -12.0 *
              scale[0], -17.0 * scale[1], 2.0 * scale[0], -5.0 * scale[1])
    Curveto_r(9.0 * scale[0], 7.0 * scale[1], 19.0 * scale[0],
              24.0 * scale[1], 22.0 * scale[0], 37.0 * scale[1])
    Curveto_r(5.0 * scale[0], 29.0 * scale[1], 4.0 * scale[0],
              30.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    te.end_fill()
    Moveto(1028.0 * scale[0], 903.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -5.0 * scale[1], -25.0 *
              scale[0], -33.0 * scale[1], -7.0 * scale[0], -33.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              5.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], 1.0 * scale[0],
              10.0 * scale[1], 9.0 * scale[0], 10.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0],
              5.0 * scale[1], 16.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -1.0 * scale[0],
              9.0 * scale[1], -2.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -1.0 * scale[1], -11.0 *
              scale[0], -3.0 * scale[1], -20.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(1325.0 * scale[0], 897.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -8.0 * scale[1], 1.0 * scale[0], -
              18.0 * scale[1], -4.0 * scale[0], -22.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -3.0 * scale[1], -8.0 * scale[0], -
              12.0 * scale[1], -4.0 * scale[0], -18.0 * scale[1])
    Curveto_r(4.0 * scale[0], -7.0 * scale[1], -1.0 * scale[0], -
              6.0 * scale[1], -11.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 19.0 * scale[1], -46.0 * scale[0],
              0.0 * scale[1], -27.0 * scale[0], -23.0 * scale[1])
    Curveto_r(7.0 * scale[0], -9.0 * scale[1], 16.0 * scale[0], -
              15.0 * scale[1], 19.0 * scale[0], -14.0 * scale[1])
    Curveto_r(19.0 * scale[0], 2.0 * scale[1], 23.0 * scale[0], -
              3.0 * scale[1], 13.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -11.0 * scale[1], -7.0 * scale[0], -
              13.0 * scale[1], 12.0 * scale[0], -13.0 * scale[1])
    Curveto_r(23.0 * scale[0], 0.0 * scale[1], 24.0 * scale[0],
              1.0 * scale[1], 13.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 23.0 * scale[1], -8.0 * scale[0],
              31.0 * scale[1], 2.0 * scale[0], 34.0 * scale[1])
    Curveto_r(17.0 * scale[0], 6.0 * scale[1], 15.0 * scale[0],
              28.0 * scale[1], -3.0 * scale[0], 43.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 11.0 * scale[1], -14.0 * scale[0],
              10.0 * scale[1], -10.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(1430.0 * scale[0], 900.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0], -
              14.0 * scale[1], 15.0 * scale[0], -24.0 * scale[1])
    Curveto_r(15.0 * scale[0], -19.0 * scale[1], 15.0 *
              scale[0], -19.0 * scale[1], 15.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              19.0 * scale[1], 10.0 * scale[0], 16.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 10.0 *
              scale[0], -2.0 * scale[1], 10.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -11.0 * scale[0],
              9.0 * scale[1], -25.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -25.0 *
              scale[0], -3.0 * scale[1], -25.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(1720.0 * scale[0], 894.0 * scale[1], x, y)
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
    Moveto(3900.0 * scale[0], 900.0 * scale[1], x, y)
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
    Moveto(3966.0 * scale[0], 901.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -5.0 * scale[1], 3.0 * scale[0], -
              7.0 * scale[1], 14.0 * scale[0], -4.0 * scale[1])
    Curveto_r(23.0 * scale[0], 6.0 * scale[1], 26.0 * scale[0],
              13.0 * scale[1], 6.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0], -
              4.0 * scale[1], -20.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(1115.0 * scale[0], 890.0 * scale[1], x, y)
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
    Moveto(1245.0 * scale[0], 890.0 * scale[1], x, y)
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
    Moveto(1810.0 * scale[0], 890.0 * scale[1], x, y)
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
    Moveto(980.0 * scale[0], 876.0 * scale[1], x, y)
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
    Moveto(1680.0 * scale[0], 880.0 * scale[1], x, y)
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
    Moveto(1755.0 * scale[0], 880.0 * scale[1], x, y)
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
    Moveto(1177.0 * scale[0], 874.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -8.0 * scale[1], 1.0 * scale[0], -
              24.0 * scale[1], 14.0 * scale[0], -24.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              7.0 * scale[1], 9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 15.0 * scale[1], -12.0 * scale[0],
              20.0 * scale[1], -23.0 * scale[0], 9.0 * scale[1])
    te.end_fill()
    Moveto(1917.0 * scale[0], 873.0 * scale[1], x, y)
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
    Moveto(1206.0 * scale[0], 844.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-14.0 * scale[0], -20.0 * scale[1], -20.0 *
              scale[0], -23.0 * scale[1], -27.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 7.0 * scale[1], -11.0 * scale[0],
              10.0 * scale[1], -14.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -4.0 * scale[1], 7.0 * scale[0], -
              20.0 * scale[1], 23.0 * scale[0], -36.0 * scale[1])
    Curveto_r(25.0 * scale[0], -24.0 * scale[1], 28.0 * scale[0], -
              31.0 * scale[1], 16.0 * scale[0], -36.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -7.0 * scale[1], -14.0 *
              scale[0], -31.0 * scale[1], 5.0 * scale[0], -31.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0], -
              7.0 * scale[1], 21.0 * scale[0], -15.0 * scale[1])
    Curveto_r(5.0 * scale[0], -8.0 * scale[1], 13.0 * scale[0], -
              11.0 * scale[1], 17.0 * scale[0], -6.0 * scale[1])
    Curveto_r(4.0 * scale[0], 5.0 * scale[1], 2.0 * scale[0],
              11.0 * scale[1], -4.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 3.0 * scale[1], -13.0 * scale[0],
              12.0 * scale[1], -13.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], 7.0 * scale[0],
              14.0 * scale[1], 30.0 * scale[0], 10.0 * scale[1])
    Curveto_r(25.0 * scale[0], -6.0 * scale[1], 30.0 *
              scale[0], -3.0 * scale[1], 30.0 * scale[0], 13.0 * scale[1])
    Curveto_r(0.0 * scale[0], 22.0 * scale[1], -16.0 * scale[0],
              27.0 * scale[1], -22.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-2.0 * scale[0], -6.0 * scale[1], -10.0 *
              scale[0], -8.0 * scale[1], -16.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 10.0 * scale[1], -15.0 * scale[0],
              26.0 * scale[1], 3.0 * scale[0], 20.0 * scale[1])
    Curveto_r(8.0 * scale[0], -4.0 * scale[1], 15.0 *
              scale[0], -1.0 * scale[1], 15.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -10.0 * scale[0],
              9.0 * scale[1], -29.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-29.0 * scale[0], -6.0 * scale[1], -53.0 * scale[0],
              10.0 * scale[1], -35.0 * scale[0], 24.0 * scale[1])
    Curveto_r(17.0 * scale[0], 12.0 * scale[1], 36.0 * scale[0],
              41.0 * scale[1], 28.0 * scale[0], 41.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -17.0 * scale[0], -
              12.0 * scale[1], -28.0 * scale[0], -26.0 * scale[1])
    te.end_fill()
    Moveto(1364.0 * scale[0], 854.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -15.0 * scale[1], -19.0 *
              scale[0], -15.0 * scale[1], 2.0 * scale[0], -9.0 * scale[1])
    Curveto_r(13.0 * scale[0], 3.0 * scale[1], 28.0 * scale[0],
              0.0 * scale[1], 37.0 * scale[0], -9.0 * scale[1])
    Curveto_r(12.0 * scale[0], -13.0 * scale[1], 16.0 *
              scale[0], -13.0 * scale[1], 20.0 * scale[0], -2.0 * scale[1])
    Curveto_r(6.0 * scale[0], 15.0 * scale[1], -11.0 * scale[0],
              36.0 * scale[1], -28.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0], -
              7.0 * scale[1], -31.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(1475.0 * scale[0], 860.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 11.0 * scale[0], -
              8.0 * scale[1], 16.0 * scale[0], -5.0 * scale[1])
    Curveto_r(14.0 * scale[0], 9.0 * scale[1], 11.0 * scale[0],
              15.0 * scale[1], -7.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              5.0 * scale[1], -9.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(1527.0 * scale[0], 848.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(11.0 * scale[0], -13.0 * scale[1], 24.0 * scale[0], -
              33.0 * scale[1], 28.0 * scale[0], -45.0 * scale[1])
    Curveto_r(7.0 * scale[0], -27.0 * scale[1], 20.0 * scale[0], -
              30.0 * scale[1], 29.0 * scale[0], -7.0 * scale[1])
    Curveto_r(9.0 * scale[0], 22.0 * scale[1], 8.0 * scale[0],
              24.0 * scale[1], -9.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -4.0 * scale[1], -15.0 * scale[0],
              0.0 * scale[1], -15.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 18.0 * scale[1], -26.0 * scale[0],
              47.0 * scale[1], -42.0 * scale[0], 47.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 0.0 * scale[1], -2.0 * scale[0], -
              10.0 * scale[1], 9.0 * scale[0], -22.0 * scale[1])
    te.end_fill()
    Moveto(830.0 * scale[0], 849.0 * scale[1], x, y)
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
    Moveto(3941.0 * scale[0], 844.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -12.0 * scale[1], 6.0 * scale[0], -
              25.0 * scale[1], 15.0 * scale[0], -28.0 * scale[1])
    Curveto_r(13.0 * scale[0], -5.0 * scale[1], 14.0 *
              scale[0], -3.0 * scale[1], 7.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 7.0 * scale[1], -13.0 * scale[0],
              20.0 * scale[1], -16.0 * scale[0], 28.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 10.0 * scale[1], -6.0 * scale[0],
              8.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(700.0 * scale[0], 840.0 * scale[1], x, y)
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
    Moveto(1050.0 * scale[0], 841.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 11.0 * scale[0], -
              13.0 * scale[1], 25.0 * scale[0], -19.0 * scale[1])
    Curveto_r(14.0 * scale[0], -6.0 * scale[1], 25.0 * scale[0], -
              17.0 * scale[1], 25.0 * scale[0], -24.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], -2.0 *
              scale[0], -10.0 * scale[1], -9.0 * scale[0], 1.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 8.0 * scale[1], -11.0 * scale[0],
              9.0 * scale[1], -15.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 * scale[0], -
              18.0 * scale[1], 10.0 * scale[0], -26.0 * scale[1])
    Curveto_r(20.0 * scale[0], -20.0 * scale[1], 19.0 *
              scale[0], -21.0 * scale[1], 21.0 * scale[0], 12.0 * scale[1])
    Curveto_r(1.0 * scale[0], 21.0 * scale[1], -5.0 * scale[0],
              31.0 * scale[1], -28.0 * scale[0], 44.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 9.0 * scale[1], -29.0 * scale[0],
              14.0 * scale[1], -29.0 * scale[0], 9.0 * scale[1])
    te.end_fill()
    Moveto(1645.0 * scale[0], 839.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -4.0 * scale[0], -
              13.0 * scale[1], -1.0 * scale[0], -16.0 * scale[1])
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], 6.0 *
              scale[0], -1.0 * scale[1], 6.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], 3.0 * scale[0],
              10.0 * scale[1], 14.0 * scale[0], 0.0 * scale[1])
    Curveto_r(11.0 * scale[0], -9.0 * scale[1], 19.0 *
              scale[0], -9.0 * scale[1], 33.0 * scale[0], 0.0 * scale[1])
    Curveto_r(11.0 * scale[0], 7.0 * scale[1], 12.0 * scale[0],
              10.0 * scale[1], 3.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -2.0 * scale[1], -23.0 * scale[0],
              0.0 * scale[1], -32.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 6.0 * scale[1], -19.0 * scale[0],
              5.0 * scale[1], -23.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(1735.0 * scale[0], 840.0 * scale[1], x, y)
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
    Moveto(3970.0 * scale[0], 840.0 * scale[1], x, y)
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
    Moveto(631.0 * scale[0], 824.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(1610.0 * scale[0], 829.0 * scale[1], x, y)
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
    Moveto(1901.0 * scale[0], 824.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(4020.0 * scale[0], 830.0 * scale[1], x, y)
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
    Moveto(892.0 * scale[0], 818.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(5.0 * scale[0], -15.0 * scale[1], 28.0 * scale[0], -
              23.0 * scale[1], 28.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -7.0 * scale[0],
              13.0 * scale[1], -16.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 4.0 * scale[1], -14.0 * scale[0],
              1.0 * scale[1], -12.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(960.0 * scale[0], 820.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -5.0 * scale[1], -10.0 * scale[0], -
              10.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 21.0 * scale[0], -22.0 * scale[1])
    Curveto_r(10.0 * scale[0], -22.0 * scale[1], 10.0 *
              scale[0], -22.0 * scale[1], 15.0 * scale[0], 4.0 * scale[1])
    Curveto_r(4.0 * scale[0], 20.0 * scale[1], 2.0 * scale[0],
              25.0 * scale[1], -10.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -3.0 * scale[1], -13.0 *
              scale[0], -1.0 * scale[1], -8.0 * scale[0], 6.0 * scale[1])
    Curveto_r(9.0 * scale[0], 14.0 * scale[1], 6.0 * scale[0],
              15.0 * scale[1], -14.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(1025.0 * scale[0], 819.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0], -
              12.0 * scale[1], -2.0 * scale[0], -15.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 17.0 * scale[1], 1.0 * scale[0],
              20.0 * scale[1], -8.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(820.0 * scale[0], 810.0 * scale[1], x, y)
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
    Moveto(1794.0 * scale[0], 803.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -10.0 * scale[1], 6.0 * scale[0], -
              17.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(15.0 * scale[0], 3.0 * scale[1], 16.0 * scale[0],
              11.0 * scale[1], 2.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 10.0 * scale[1], -14.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(3840.0 * scale[0], 804.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 5.0 * scale[0], -
              12.0 * scale[1], 10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 8.0 * scale[0],
              11.0 * scale[1], 5.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 14.0 * scale[1], -15.0 * scale[0],
              11.0 * scale[1], -15.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(3895.0 * scale[0], 810.0 * scale[1], x, y)
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
    Moveto(4080.0 * scale[0], 811.0 * scale[1], x, y)
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
    Moveto(1370.0 * scale[0], 795.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -9.0 * scale[1], 15.0 * scale[0], -
              13.0 * scale[1], 17.0 * scale[0], -11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], -7.0 * scale[0],
              26.0 * scale[1], -19.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0], -
              6.0 * scale[1], 2.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(1412.0 * scale[0], 795.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -12.0 * scale[1], -10.0 *
              scale[0], -15.0 * scale[1], 0.0 * scale[0], -16.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 3.0 * scale[0], -
              5.0 * scale[1], -9.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-25.0 * scale[0], -12.0 * scale[1], -29.0 *
              scale[0], -23.0 * scale[1], -13.0 * scale[0], -33.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 10.0 *
              scale[0], -2.0 * scale[1], 10.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 19.0 * scale[1], 45.0 * scale[0],
              22.0 * scale[1], 58.0 * scale[0], 5.0 * scale[1])
    Curveto_r(17.0 * scale[0], -23.0 * scale[1], 15.0 * scale[0], -
              33.0 * scale[1], -5.0 * scale[0], -27.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 4.0 * scale[1], -9.0 *
              scale[0], -1.0 * scale[1], 7.0 * scale[0], -15.0 * scale[1])
    Curveto_r(35.0 * scale[0], -29.0 * scale[1], 41.0 *
              scale[0], -26.0 * scale[1], 24.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 21.0 * scale[1], -10.0 * scale[0],
              35.0 * scale[1], -4.0 * scale[0], 35.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              4.0 * scale[1], 10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -9.0 * scale[0],
              8.0 * scale[1], -20.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-14.0 * scale[0], -3.0 * scale[1], -22.0 * scale[0],
              3.0 * scale[1], -26.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 27.0 * scale[1], -14.0 * scale[0],
              29.0 * scale[1], -32.0 * scale[0], 9.0 * scale[1])
    te.end_fill()
    Moveto(1458.0 * scale[0], 803.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(1605.0 * scale[0], 791.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -11.0 * scale[1], 1.0 * scale[0], -
              22.0 * scale[1], -5.0 * scale[0], -26.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -8.0 * scale[1], -13.0 *
              scale[0], -25.0 * scale[1], 0.0 * scale[0], -25.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              5.0 * scale[1], 10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], 8.0 * scale[0],
              18.0 * scale[1], 18.0 * scale[0], 25.0 * scale[1])
    Curveto_r(15.0 * scale[0], 12.0 * scale[1], 15.0 * scale[0],
              15.0 * scale[1], 2.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 15.0 * scale[1], -32.0 * scale[0],
              12.0 * scale[1], -25.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(585.0 * scale[0], 790.0 * scale[1], x, y)
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
    Moveto(1507.0 * scale[0], 789.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(1650.0 * scale[0], 790.0 * scale[1], x, y)
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
    Moveto(3624.0 * scale[0], 779.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], -1.0 * scale[0], -
              16.0 * scale[1], 5.0 * scale[0], -22.0 * scale[1])
    Curveto_r(8.0 * scale[0], -8.0 * scale[1], 11.0 *
              scale[0], -6.0 * scale[1], 11.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], 4.0 * scale[0],
              14.0 * scale[1], 12.0 * scale[0], 10.0 * scale[1])
    Curveto_r(7.0 * scale[0], -4.0 * scale[1], 8.0 *
              scale[0], -3.0 * scale[1], 4.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 15.0 * scale[1], -23.0 * scale[0],
              15.0 * scale[1], -32.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(1343.0 * scale[0], 773.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-28.0 * scale[0], -5.0 * scale[1], -29.0 *
              scale[0], -15.0 * scale[1], -3.0 * scale[0], -38.0 * scale[1])
    Curveto_r(22.0 * scale[0], -20.0 * scale[1], 54.0 * scale[0], -
              30.0 * scale[1], 44.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 5.0 * scale[1], -12.0 * scale[0],
              9.0 * scale[1], -20.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0],
              8.0 * scale[1], -14.0 * scale[0], 18.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], 2.0 * scale[0],
              15.0 * scale[1], 10.0 * scale[0], 2.0 * scale[1])
    Curveto_r(7.0 * scale[0], -12.0 * scale[1], 9.0 *
              scale[0], -10.0 * scale[1], 7.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], -1.0 * scale[0],
              21.0 * scale[1], -2.0 * scale[0], 21.0 * scale[1])
    Curveto_r(0.0 * scale[0], -1.0 * scale[1], -10.0 * scale[0], -
              4.0 * scale[1], -22.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(1711.0 * scale[0], 764.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(3855.0 * scale[0], 770.0 * scale[1], x, y)
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
    Moveto(3970.0 * scale[0], 771.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 7.0 * scale[0], -
              11.0 * scale[1], 14.0 * scale[0], -14.0 * scale[1])
    Curveto_r(10.0 * scale[0], -4.0 * scale[1], 13.0 *
              scale[0], -1.0 * scale[1], 9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 15.0 * scale[1], -23.0 * scale[0],
              19.0 * scale[1], -23.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(885.0 * scale[0], 760.0 * scale[1], x, y)
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
    Moveto(1150.0 * scale[0], 760.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-13.0 * scale[0], -9.0 * scale[1], -13.0 *
              scale[0], -10.0 * scale[1], 0.0 * scale[0], -10.0 * scale[1])
    Curveto_r(12.0 * scale[0], -1.0 * scale[1], 11.0 * scale[0], -
              4.0 * scale[1], -4.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -8.0 * scale[1], -16.0 * scale[0], -
              18.0 * scale[1], -13.0 * scale[0], -22.0 * scale[1])
    Curveto_r(4.0 * scale[0], -3.0 * scale[1], 7.0 *
              scale[0], -3.0 * scale[1], 7.0 * scale[0], 0.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], 9.0 * scale[0], -
              1.0 * scale[1], 20.0 * scale[0], -11.0 * scale[1])
    Curveto_r(19.0 * scale[0], -16.0 * scale[1], 19.0 *
              scale[0], -18.0 * scale[1], 3.0 * scale[0], -29.0 * scale[1])
    Curveto_r(-9.0 * scale[0], -7.0 * scale[1], -14.0 * scale[0], -
              15.0 * scale[1], -11.0 * scale[0], -18.0 * scale[1])
    Curveto_r(7.0 * scale[0], -8.0 * scale[1], 71.0 * scale[0],
              15.0 * scale[1], 88.0 * scale[0], 32.0 * scale[1])
    Curveto_r(13.0 * scale[0], 12.0 * scale[1], 11.0 * scale[0],
              13.0 * scale[1], -15.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-26.0 * scale[0], -10.0 * scale[1], -32.0 *
              scale[0], -9.0 * scale[1], -46.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 12.0 * scale[1], -14.0 * scale[0],
              30.0 * scale[1], -12.0 * scale[0], 46.0 * scale[1])
    Curveto_r(6.0 * scale[0], 28.0 * scale[1], 5.0 * scale[0],
              29.0 * scale[1], -17.0 * scale[0], 15.0 * scale[1])
    te.end_fill()
    Moveto(1296.0 * scale[0], 754.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -21.0 * scale[1], -8.0 *
              scale[0], -39.0 * scale[1], 1.0 * scale[0], -30.0 * scale[1])
    Curveto_r(8.0 * scale[0], 7.0 * scale[1], 15.0 * scale[0],
              46.0 * scale[1], 9.0 * scale[0], 46.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              7.0 * scale[1], -10.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(1496.0 * scale[0], 743.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -12.0 * scale[1], -1.0 *
              scale[0], -14.0 * scale[1], 20.0 * scale[0], -9.0 * scale[1])
    Curveto_r(17.0 * scale[0], 5.0 * scale[1], 30.0 * scale[0],
              3.0 * scale[1], 34.0 * scale[0], -5.0 * scale[1])
    Curveto_r(8.0 * scale[0], -13.0 * scale[1], 30.0 *
              scale[0], -4.0 * scale[1], 30.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -4.0 * scale[0],
              7.0 * scale[1], -10.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -10.0 *
              scale[0], -2.0 * scale[1], -10.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 16.0 * scale[1], -58.0 * scale[0],
              12.0 * scale[1], -64.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(947.0 * scale[0], 743.0 * scale[1], x, y)
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
    Moveto(975.0 * scale[0], 740.0 * scale[1], x, y)
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
    Moveto(1080.0 * scale[0], 745.0 * scale[1], x, y)
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
    Moveto(805.0 * scale[0], 730.0 * scale[1], x, y)
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
    Moveto(660.0 * scale[0], 721.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 18.0 * scale[1], -14.0 * scale[0],
              21.0 * scale[1], -14.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(730.0 * scale[0], 716.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              17.0 * scale[1], 9.0 * scale[0], -21.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 9.0 * scale[0],
              4.0 * scale[1], 8.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 23.0 * scale[1], -17.0 * scale[0],
              28.0 * scale[1], -17.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(875.0 * scale[0], 720.0 * scale[1], x, y)
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
    Moveto(1010.0 * scale[0], 720.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -8.0 * scale[1])
    Curveto_r(9.0 * scale[0], 2.0 * scale[1], 16.0 * scale[0], -
              2.0 * scale[1], 15.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -7.0 * scale[1], 6.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(18.0 * scale[0], 5.0 * scale[1], 19.0 * scale[0],
              6.0 * scale[1], 2.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 16.0 * scale[1], -53.0 * scale[0],
              18.0 * scale[1], -53.0 * scale[0], 4.0 * scale[1])
    te.end_fill()
    Moveto(1260.0 * scale[0], 720.0 * scale[1], x, y)
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
    Moveto(1593.0 * scale[0], 717.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 12.0 * scale[0], -
              11.0 * scale[1], 36.0 * scale[0], -8.0 * scale[1])
    Curveto_r(30.0 * scale[0], 3.0 * scale[1], 33.0 * scale[0],
              5.0 * scale[1], 16.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-31.0 * scale[0], 12.0 * scale[1], -52.0 * scale[0],
              10.0 * scale[1], -52.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(835.0 * scale[0], 710.0 * scale[1], x, y)
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
    Moveto(920.0 * scale[0], 700.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -11.0 * scale[1], 15.0 * scale[0], -
              18.0 * scale[1], 21.0 * scale[0], -15.0 * scale[1])
    Curveto_r(13.0 * scale[0], 9.0 * scale[1], 11.0 * scale[0],
              13.0 * scale[1], -12.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 11.0 * scale[1], -20.0 * scale[0],
              10.0 * scale[1], -9.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(1185.0 * scale[0], 710.0 * scale[1], x, y)
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
    Moveto(1683.0 * scale[0], 713.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-16.0 * scale[0], -6.0 * scale[1], -17.0 *
              scale[0], -33.0 * scale[1], -3.0 * scale[0], -33.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 26.0 * scale[0],
              28.0 * scale[1], 19.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 2.0 * scale[1], -10.0 * scale[0],
              1.0 * scale[1], -16.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(1528.0 * scale[0], 696.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -14.0 * scale[1], -23.0 *
              scale[0], -26.0 * scale[1], -10.0 * scale[0], -26.0 * scale[1])
    Curveto_r(4.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              9.0 * scale[1], 20.0 * scale[0], 20.0 * scale[1])
    Curveto_r(14.0 * scale[0], 23.0 * scale[1], 13.0 * scale[0],
              24.0 * scale[1], -10.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(1826.0 * scale[0], 695.0 * scale[1], x, y)
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
    Moveto(4025.0 * scale[0], 700.0 * scale[1], x, y)
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
    Moveto(605.0 * scale[0], 690.0 * scale[1], x, y)
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
    Moveto(1329.0 * scale[0], 692.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(11.0 * scale[0], -8.0 * scale[1], 11.0 * scale[0], -
              10.0 * scale[1], 0.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-11.0 * scale[0], -4.0 * scale[1], -11.0 *
              scale[0], -8.0 * scale[1], 3.0 * scale[0], -22.0 * scale[1])
    Curveto_r(15.0 * scale[0], -16.0 * scale[1], 17.0 *
              scale[0], -16.0 * scale[1], 28.0 * scale[0], 5.0 * scale[1])
    Curveto_r(13.0 * scale[0], 25.0 * scale[1], 13.0 * scale[0],
              25.0 * scale[1], -20.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 5.0 * scale[1], -21.0 * scale[0],
              4.0 * scale[1], -11.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(1403.0 * scale[0], 672.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              21.0 * scale[1], 5.0 * scale[0], -15.0 * scale[1])
    Curveto_r(4.0 * scale[0], 5.0 * scale[1], 16.0 * scale[0],
              13.0 * scale[1], 26.0 * scale[0], 16.0 * scale[1])
    Curveto_r(21.0 * scale[0], 8.0 * scale[1], 15.0 * scale[0],
              20.0 * scale[1], -12.0 * scale[0], 22.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 1.0 * scale[1], -17.0 * scale[0], -
              7.0 * scale[1], -19.0 * scale[0], -23.0 * scale[1])
    te.end_fill()
    Moveto(3980.0 * scale[0], 676.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 13.0 *
              scale[0], -7.0 * scale[1], 20.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 6.0 * scale[1], 3.0 * scale[0],
              10.0 * scale[1], -10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 0.0 * scale[1], -16.0 * scale[0], -
              4.0 * scale[1], -10.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(745.0 * scale[0], 669.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -6.0 * scale[1], -4.0 * scale[0], -
              13.0 * scale[1], -1.0 * scale[0], -16.0 * scale[1])
    Curveto_r(3.0 * scale[0], -4.0 * scale[1], 6.0 *
              scale[0], -1.0 * scale[1], 6.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 7.0 * scale[0],
              9.0 * scale[1], 17.0 * scale[0], 5.0 * scale[1])
    Curveto_r(11.0 * scale[0], -4.0 * scale[1], 14.0 *
              scale[0], -3.0 * scale[1], 9.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 15.0 * scale[1], -23.0 * scale[0],
              15.0 * scale[1], -31.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(805.0 * scale[0], 670.0 * scale[1], x, y)
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
    Moveto(1097.0 * scale[0], 671.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-17.0 * scale[0], -6.0 * scale[1], -17.0 *
              scale[0], -8.0 * scale[1], -3.0 * scale[0], -20.0 * scale[1])
    Curveto_r(13.0 * scale[0], -11.0 * scale[1], 18.0 *
              scale[0], -10.0 * scale[1], 30.0 * scale[0], 2.0 * scale[1])
    Curveto_r(18.0 * scale[0], 18.0 * scale[1], 2.0 * scale[0],
              28.0 * scale[1], -27.0 * scale[0], 18.0 * scale[1])
    te.end_fill()
    Moveto(1580.0 * scale[0], 671.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 5.0 * scale[0], -
              11.0 * scale[1], 10.0 * scale[0], -11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0], -
              7.0 * scale[1], 0.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-7.0 * scale[0], -11.0 * scale[1], -9.0 * scale[0], -
              23.0 * scale[1], -6.0 * scale[0], -27.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 6.0 * scale[0],
              0.0 * scale[1], 6.0 * scale[0], 6.0 * scale[1])
    Curveto_r(0.0 * scale[0], 7.0 * scale[1], 8.0 * scale[0],
              12.0 * scale[1], 18.0 * scale[0], 13.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              3.0 * scale[1], 4.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 2.0 * scale[1], -10.0 * scale[0],
              8.0 * scale[1], -7.0 * scale[0], 13.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], -2.0 * scale[0],
              13.0 * scale[1], -10.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -15.0 * scale[0],
              9.0 * scale[1], -15.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(1625.0 * scale[0], 670.0 * scale[1], x, y)
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
    Moveto(978.0 * scale[0], 652.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(2.0 * scale[0], -7.0 * scale[1], 12.0 * scale[0], -
              10.0 * scale[1], 20.0 * scale[0], -7.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 19.0 * scale[0],
              0.0 * scale[1], 24.0 * scale[0], -7.0 * scale[1])
    Curveto_r(6.0 * scale[0], -10.0 * scale[1], 10.0 *
              scale[0], -10.0 * scale[1], 18.0 * scale[0], 2.0 * scale[1])
    Curveto_r(9.0 * scale[0], 13.0 * scale[1], 10.0 * scale[0],
              13.0 * scale[1], 11.0 * scale[0], 0.0 * scale[1])
    Curveto_r(1.0 * scale[0], -8.0 * scale[1], 1.0 * scale[0], -
              23.0 * scale[1], 0.0 * scale[0], -32.0 * scale[1])
    Curveto_r(-1.0 * scale[0], -10.0 * scale[1], 4.0 * scale[0], -
              18.0 * scale[1], 13.0 * scale[0], -18.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 16.0 * scale[0],
              10.0 * scale[1], 16.0 * scale[0], 32.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], -3.0 * scale[0],
              28.0 * scale[1], -7.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], -13.0 *
              scale[0], -1.0 * scale[1], -21.0 * scale[0], 6.0 * scale[1])
    Curveto_r(-21.0 * scale[0], 17.0 * scale[1], -81.0 * scale[0],
              16.0 * scale[1], -74.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(1226.0 * scale[0], 661.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-14.0 * scale[0], -5.0 * scale[1], -16.0 *
              scale[0], -10.0 * scale[1], -7.0 * scale[0], -15.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 19.0 * scale[0], -
              5.0 * scale[1], 27.0 * scale[0], -2.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 12.0 * scale[0],
              1.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], -13.0 * scale[0], -
              10.0 * scale[1], -21.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -14.0 * scale[0], -
              5.0 * scale[1], -14.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 5.0 * scale[0], -
              7.0 * scale[1], 10.0 * scale[0], -4.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 10.0 * scale[0], -
              1.0 * scale[1], 10.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 5.0 * scale[0], -
              15.0 * scale[1], 15.0 * scale[0], -11.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 15.0 * scale[0],
              0.0 * scale[1], 15.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 10.0 * scale[0], -
              14.0 * scale[1], 40.0 * scale[0], -12.0 * scale[1])
    Curveto_r(22.0 * scale[0], 2.0 * scale[1], 40.0 * scale[0],
              7.0 * scale[1], 40.0 * scale[0], 12.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], -12.0 * scale[0],
              6.0 * scale[1], -26.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-18.0 * scale[0], -3.0 * scale[1], -29.0 * scale[0],
              1.0 * scale[1], -40.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 13.0 * scale[1], -14.0 * scale[0],
              27.0 * scale[1], -13.0 * scale[0], 31.0 * scale[1])
    Curveto_r(6.0 * scale[0], 33.0 * scale[1], -7.0 * scale[0],
              40.0 * scale[1], -45.0 * scale[0], 25.0 * scale[1])
    te.end_fill()
    Moveto(1370.0 * scale[0], 660.0 * scale[1], x, y)
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
    Moveto(1460.0 * scale[0], 660.0 * scale[1], x, y)
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
    Moveto(1865.0 * scale[0], 660.0 * scale[1], x, y)
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
    Moveto(874.0 * scale[0], 648.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -7.0 * scale[1], -3.0 *
              scale[0], -8.0 * scale[1], 4.0 * scale[0], -4.0 * scale[1])
    Curveto_r(7.0 * scale[0], 4.0 * scale[1], 12.0 * scale[0],
              2.0 * scale[1], 12.0 * scale[0], -3.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              11.0 * scale[1], 10.0 * scale[0], -11.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0],
              7.0 * scale[1], 4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 18.0 * scale[1], -20.0 * scale[0],
              19.0 * scale[1], -30.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(1290.0 * scale[0], 641.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 8.0 * scale[0], -
              21.0 * scale[1], 18.0 * scale[0], -24.0 * scale[1])
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 25.0 * scale[0], -
              8.0 * scale[1], 35.0 * scale[0], -12.0 * scale[1])
    Curveto_r(10.0 * scale[0], -4.0 * scale[1], 17.0 *
              scale[0], -3.0 * scale[1], 17.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -11.0 * scale[0],
              13.0 * scale[1], -25.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 3.0 * scale[1], -25.0 * scale[0],
              12.0 * scale[1], -25.0 * scale[0], 20.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -4.0 * scale[0],
              14.0 * scale[1], -10.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -10.0 * scale[0], -
              8.0 * scale[1], -10.0 * scale[0], -19.0 * scale[1])
    te.end_fill()
    Moveto(4088.0 * scale[0], 653.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(950.0 * scale[0], 650.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -18.0 * scale[1], -9.0 * scale[0], -
              53.0 * scale[1], -3.0 * scale[0], -44.0 * scale[1])
    Curveto_r(11.0 * scale[0], 15.0 * scale[1], 40.0 * scale[0],
              9.0 * scale[1], 64.0 * scale[0], -12.0 * scale[1])
    Curveto_r(12.0 * scale[0], -10.0 * scale[1], 19.0 *
              scale[0], -12.0 * scale[1], 19.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -7.0 * scale[0],
              14.0 * scale[1], -16.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -13.0 * scale[0],
              12.0 * scale[1], -10.0 * scale[0], 19.0 * scale[1])
    Curveto_r(4.0 * scale[0], 10.0 * scale[1], -1.0 * scale[0],
              11.0 * scale[1], -19.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -7.0 * scale[1], -25.0 *
              scale[0], -5.0 * scale[1], -28.0 * scale[0], 8.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 9.0 * scale[1], -6.0 * scale[0],
              15.0 * scale[1], -7.0 * scale[0], 12.0 * scale[1])
    te.end_fill()
    Moveto(1414.0 * scale[0], 639.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], -1.0 * scale[0], -
              16.0 * scale[1], 5.0 * scale[0], -22.0 * scale[1])
    Curveto_r(6.0 * scale[0], -6.0 * scale[1], 11.0 * scale[0], -
              7.0 * scale[1], 11.0 * scale[0], -1.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 4.0 * scale[0],
              3.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(6.0 * scale[0], -10.0 * scale[1], 10.0 *
              scale[0], -9.0 * scale[1], 14.0 * scale[0], 7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 12.0 * scale[1], 1.0 * scale[0],
              19.0 * scale[1], -4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], -3.0 * scale[1], -9.0 * scale[0],
              0.0 * scale[1], -9.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], -17.0 * scale[0],
              14.0 * scale[1], -26.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(1510.0 * scale[0], 641.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 10.0 * scale[0], -
              11.0 * scale[1], 21.0 * scale[0], -14.0 * scale[1])
    Curveto_r(15.0 * scale[0], -4.0 * scale[1], 20.0 * scale[0], -
              11.0 * scale[1], 16.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -9.0 * scale[1], -2.0 * scale[0], -
              16.0 * scale[1], 2.0 * scale[0], -16.0 * scale[1])
    Curveto_r(14.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0],
              24.0 * scale[1], 7.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 16.0 * scale[1], -46.0 * scale[0],
              26.0 * scale[1], -46.0 * scale[0], 16.0 * scale[1])
    te.end_fill()
    Moveto(703.0 * scale[0], 625.0 * scale[1], x, y)
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
    Moveto(770.0 * scale[0], 615.0 * scale[1], x, y)
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
    Moveto(1134.0 * scale[0], 613.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -25.0 * scale[1], 26.0 * scale[0], -
              28.0 * scale[1], 26.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 12.0 * scale[1], -6.0 * scale[0],
              21.0 * scale[1], -14.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              8.0 * scale[1], -12.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(1883.0 * scale[0], 615.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -9.0 * scale[1], -3.0 * scale[0], -
              18.0 * scale[1], -1.0 * scale[0], -21.0 * scale[1])
    Curveto_r(3.0 * scale[0], -3.0 * scale[1], 8.0 * scale[0],
              4.0 * scale[1], 11.0 * scale[0], 16.0 * scale[1])
    Curveto_r(6.0 * scale[0], 23.0 * scale[1], -1.0 * scale[0],
              27.0 * scale[1], -10.0 * scale[0], 5.0 * scale[1])
    te.end_fill()
    Moveto(828.0 * scale[0], 606.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-15.0 * scale[0], -11.0 * scale[1], -15.0 *
              scale[0], -13.0 * scale[1], 0.0 * scale[0], -24.0 * scale[1])
    Curveto_r(12.0 * scale[0], -7.0 * scale[1], 13.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -4.0 * scale[1], -13.0 * scale[0], -
              16.0 * scale[1], -17.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -12.0 * scale[1], -2.0 *
              scale[0], -15.0 * scale[1], 9.0 * scale[0], -11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 3.0 * scale[1], 14.0 * scale[0],
              9.0 * scale[1], 14.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 5.0 * scale[0],
              6.0 * scale[1], 10.0 * scale[0], 3.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 10.0 * scale[0],
              5.0 * scale[1], 10.0 * scale[0], 19.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], 5.0 * scale[0],
              28.0 * scale[1], 10.0 * scale[0], 31.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 10.0 * scale[0],
              9.0 * scale[1], 10.0 * scale[0], 13.0 * scale[1])
    Curveto_r(0.0 * scale[0], 13.0 * scale[1], -34.0 * scale[0],
              11.0 * scale[1], -52.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(905.0 * scale[0], 610.0 * scale[1], x, y)
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
    Moveto(1180.0 * scale[0], 605.0 * scale[1], x, y)
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
    Moveto(1510.0 * scale[0], 601.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 5.0 * scale[0], -
              23.0 * scale[1], 10.0 * scale[0], -26.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 10.0 * scale[0],
              1.0 * scale[1], 10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], 0.0 * scale[0],
              19.0 * scale[1], 1.0 * scale[0], 23.0 * scale[1])
    Curveto_r(0.0 * scale[0], 4.0 * scale[1], -4.0 * scale[0],
              9.0 * scale[1], -10.0 * scale[0], 11.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 2.0 * scale[1], -11.0 * scale[0], -
              5.0 * scale[1], -11.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(1630.0 * scale[0], 610.0 * scale[1], x, y)
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
    Moveto(1380.0 * scale[0], 590.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -16.0 * scale[1], -8.0 *
              scale[0], -20.0 * scale[1], 3.0 * scale[0], -20.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0],
              9.0 * scale[1], 20.0 * scale[0], 20.0 * scale[1])
    Curveto_r(3.0 * scale[0], 11.0 * scale[1], 1.0 * scale[0],
              20.0 * scale[1], -4.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              9.0 * scale[1], -19.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(620.0 * scale[0], 591.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], -3.0 * scale[1], 7.0 * scale[0],
              1.0 * scale[1], 4.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 18.0 * scale[1], -14.0 * scale[0],
              21.0 * scale[1], -14.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(956.0 * scale[0], 585.0 * scale[1], x, y)
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
    Moveto(1455.0 * scale[0], 591.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -1.0 * scale[0], -
              12.0 * scale[1], 5.0 * scale[0], -16.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 10.0 * scale[0],
              1.0 * scale[1], 10.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 18.0 * scale[1], -6.0 * scale[0],
              21.0 * scale[1], -15.0 * scale[0], 7.0 * scale[1])
    te.end_fill()
    Moveto(570.0 * scale[0], 571.0 * scale[1], x, y)
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
    Moveto(1200.0 * scale[0], 570.0 * scale[1], x, y)
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
    Moveto(1590.0 * scale[0], 570.0 * scale[1], x, y)
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
    Moveto(4054.0 * scale[0], 569.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], -1.0 * scale[0], -
              16.0 * scale[1], 5.0 * scale[0], -22.0 * scale[1])
    Curveto_r(8.0 * scale[0], -8.0 * scale[1], 11.0 * scale[0], -
              5.0 * scale[1], 11.0 * scale[0], 11.0 * scale[1])
    Curveto_r(0.0 * scale[0], 24.0 * scale[1], -5.0 * scale[0],
              28.0 * scale[1], -16.0 * scale[0], 11.0 * scale[1])
    te.end_fill()
    Moveto(690.0 * scale[0], 565.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 60.0 * scale[0], -
              100.0 * scale[1], 60.0 * scale[0], -92.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -12.0 * scale[0],
              28.0 * scale[1], -26.0 * scale[0], 53.0 * scale[1])
    Curveto_r(-24.0 * scale[0], 40.0 * scale[1], -34.0 * scale[0],
              52.0 * scale[1], -34.0 * scale[0], 39.0 * scale[1])
    te.end_fill()
    Moveto(980.0 * scale[0], 560.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -5.0 * scale[1], -12.0 * scale[0], -
              11.0 * scale[1], -9.0 * scale[0], -14.0 * scale[1])
    Curveto_r(2.0 * scale[0], -3.0 * scale[1], 11.0 *
              scale[0], -1.0 * scale[1], 19.0 * scale[0], 4.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 12.0 * scale[0],
              11.0 * scale[1], 9.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 3.0 * scale[1], -11.0 * scale[0],
              1.0 * scale[1], -19.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(1010.0 * scale[0], 559.0 * scale[1], x, y)
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
    Moveto(1710.0 * scale[0], 555.0 * scale[1], x, y)
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
    Moveto(917.0 * scale[0], 553.0 * scale[1], x, y)
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
    Moveto(1285.0 * scale[0], 550.0 * scale[1], x, y)
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
    Moveto(1511.0 * scale[0], 543.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-1.0 * scale[0], -12.0 * scale[1], 4.0 * scale[0], -
              25.0 * scale[1], 9.0 * scale[0], -28.0 * scale[1])
    Curveto_r(12.0 * scale[0], -7.0 * scale[1], 12.0 * scale[0],
              2.0 * scale[1], 0.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 19.0 * scale[1], -9.0 * scale[0],
              19.0 * scale[1], -9.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(1630.0 * scale[0], 548.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -9.0 * scale[1], 5.0 * scale[0], -
              20.0 * scale[1], 10.0 * scale[0], -23.0 * scale[1])
    Curveto_r(13.0 * scale[0], -8.0 * scale[1], 13.0 * scale[0],
              5.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 13.0 * scale[1], -10.0 * scale[0],
              13.0 * scale[1], -10.0 * scale[0], -2.0 * scale[1])
    te.end_fill()
    Moveto(936.0 * scale[0], 534.0 * scale[1], x, y)
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
    Moveto(1070.0 * scale[0], 540.0 * scale[1], x, y)
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
    Moveto(1150.0 * scale[0], 539.0 * scale[1], x, y)
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
    Moveto(1796.0 * scale[0], 535.0 * scale[1], x, y)
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
    Moveto(2060.0 * scale[0], 539.0 * scale[1], x, y)
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
    Moveto(4102.0 * scale[0], 537.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -10.0 * scale[1], -6.0 *
              scale[0], -13.0 * scale[1], 7.0 * scale[0], -13.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0],
              6.0 * scale[1], 14.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 7.0 * scale[1], -6.0 * scale[0],
              13.0 * scale[1], -8.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              6.0 * scale[1], -13.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(1360.0 * scale[0], 521.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -15.0 * scale[1], -6.0 * scale[0], -
              21.0 * scale[1], -22.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-23.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -10.0 * scale[1], 6.0 * scale[0], -14.0 * scale[1])
    Curveto_r(9.0 * scale[0], -1.0 * scale[1], 23.0 * scale[0], -
              11.0 * scale[1], 31.0 * scale[0], -22.0 * scale[1])
    Curveto_r(8.0 * scale[0], -10.0 * scale[1], 15.0 * scale[0], -
              14.0 * scale[1], 15.0 * scale[0], -7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              15.0 * scale[1], -10.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -8.0 * scale[0],
              17.0 * scale[1], -6.0 * scale[0], 30.0 * scale[1])
    Curveto_r(3.0 * scale[0], 14.0 * scale[1], 0.0 * scale[0],
              27.0 * scale[1], -5.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 4.0 * scale[1], -9.0 * scale[0], -
              3.0 * scale[1], -9.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(1475.0 * scale[0], 530.0 * scale[1], x, y)
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
    Moveto(660.0 * scale[0], 520.0 * scale[1], x, y)
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
    Moveto(760.0 * scale[0], 515.0 * scale[1], x, y)
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
    Moveto(1571.0 * scale[0], 516.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -10.0 * scale[1], -6.0 *
              scale[0], -12.0 * scale[1], 14.0 * scale[0], -8.0 * scale[1])
    Curveto_r(29.0 * scale[0], 5.0 * scale[1], 31.0 * scale[0],
              8.0 * scale[1], 11.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 3.0 * scale[1], -19.0 * scale[0],
              0.0 * scale[1], -25.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(3888.0 * scale[0], 523.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(898.0 * scale[0], 513.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(979.0 * scale[0], 511.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(11.0 * scale[0], -7.0 * scale[1], 11.0 *
              scale[0], -9.0 * scale[1], 0.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -3.0 * scale[1], 1.0 * scale[0], -
              5.0 * scale[1], 20.0 * scale[0], -6.0 * scale[1])
    Curveto_r(30.0 * scale[0], -1.0 * scale[1], 32.0 * scale[0],
              0.0 * scale[1], 15.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 8.0 * scale[1], -26.0 * scale[0],
              14.0 * scale[1], -34.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 0.0 * scale[1], -13.0 *
              scale[0], -2.0 * scale[1], -1.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(1425.0 * scale[0], 510.0 * scale[1], x, y)
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
    Moveto(1160.0 * scale[0], 495.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-14.0 * scale[0], -16.0 * scale[1], -3.0 *
              scale[0], -20.0 * scale[1], 19.0 * scale[0], -6.0 * scale[1])
    Curveto_r(8.0 * scale[0], 5.0 * scale[1], 9.0 * scale[0],
              11.0 * scale[1], 3.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 3.0 * scale[1], -15.0 * scale[0], -
              1.0 * scale[1], -22.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(4175.0 * scale[0], 500.0 * scale[1], x, y)
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
    Moveto(780.0 * scale[0], 479.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -4.0 * scale[1], 7.0 * scale[0], -
              10.0 * scale[1], 16.0 * scale[0], -13.0 * scale[1])
    Curveto_r(22.0 * scale[0], -8.0 * scale[1], 24.0 *
              scale[0], -8.0 * scale[1], 18.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 14.0 * scale[1], -34.0 * scale[0],
              19.0 * scale[1], -34.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(1080.0 * scale[0], 479.0 * scale[1], x, y)
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
    Moveto(1120.0 * scale[0], 480.0 * scale[1], x, y)
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
    Moveto(577.0 * scale[0], 460.0 * scale[1], x, y)
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
    Moveto(610.0 * scale[0], 469.0 * scale[1], x, y)
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
    Moveto(1293.0 * scale[0], 466.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 8.0 * scale[0], -
              14.0 * scale[1], 18.0 * scale[0], -13.0 * scale[1])
    Curveto_r(14.0 * scale[0], 1.0 * scale[1], 15.0 * scale[0],
              4.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 17.0 * scale[1], -25.0 * scale[0],
              16.0 * scale[1], -25.0 * scale[0], -1.0 * scale[1])
    te.end_fill()
    Moveto(1448.0 * scale[0], 473.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(2000.0 * scale[0], 470.0 * scale[1], x, y)
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
    Moveto(925.0 * scale[0], 460.0 * scale[1], x, y)
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
    Moveto(1155.0 * scale[0], 460.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-8.0 * scale[0], -13.0 * scale[1], 5.0 *
              scale[0], -13.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(13.0 * scale[0], 8.0 * scale[1], 13.0 * scale[0],
              10.0 * scale[1], -2.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -20.0 * scale[0], -
              4.0 * scale[1], -23.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(1650.0 * scale[0], 456.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -16.0 * scale[1], 18.0 * scale[0], -
              31.0 * scale[1], 27.0 * scale[0], -22.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              12.0 * scale[1], -11.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 14.0 * scale[1], -16.0 * scale[0],
              14.0 * scale[1], -16.0 * scale[0], 1.0 * scale[1])
    te.end_fill()
    Moveto(1705.0 * scale[0], 460.0 * scale[1], x, y)
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
    Moveto(1770.0 * scale[0], 459.0 * scale[1], x, y)
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
    Moveto(3667.0 * scale[0], 459.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(3905.0 * scale[0], 460.0 * scale[1], x, y)
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
    Moveto(416.0 * scale[0], 445.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -9.0 * scale[1], 0.0 * scale[0], -
              15.0 * scale[1], 9.0 * scale[0], -15.0 * scale[1])
    Curveto_r(9.0 * scale[0], 0.0 * scale[1], 12.0 * scale[0],
              6.0 * scale[1], 9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 8.0 * scale[1], -7.0 * scale[0],
              15.0 * scale[1], -9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -5.0 * scale[0], -
              7.0 * scale[1], -9.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(950.0 * scale[0], 449.0 * scale[1], x, y)
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
    Moveto(1447.0 * scale[0], 446.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -10.0 * scale[1], -1.0 *
              scale[0], -13.0 * scale[1], 8.0 * scale[0], -9.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 12.0 * scale[0],
              9.0 * scale[1], 9.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 12.0 * scale[1], -11.0 * scale[0],
              11.0 * scale[1], -17.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(1548.0 * scale[0], 447.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(16.0 * scale[0], -7.0 * scale[1], 26.0 *
              scale[0], -7.0 * scale[1], 34.0 * scale[0], 1.0 * scale[1])
    Curveto_r(8.0 * scale[0], 8.0 * scale[1], 2.0 * scale[0],
              10.0 * scale[1], -23.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-31.0 * scale[0], -1.0 * scale[1], -32.0 *
              scale[0], -2.0 * scale[1], -11.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(3198.0 * scale[0], 443.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(3266.0 * scale[0], 437.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0], -
              15.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 0.0 * scale[0],
              11.0 * scale[1], -7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              8.0 * scale[1], -5.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(1278.0 * scale[0], 423.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(1396.0 * scale[0], 415.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(4.0 * scale[0], -8.0 * scale[1], 7.0 * scale[0], -
              15.0 * scale[1], 9.0 * scale[0], -15.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 5.0 * scale[0],
              7.0 * scale[1], 9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(3.0 * scale[0], 9.0 * scale[1], 0.0 * scale[0],
              15.0 * scale[1], -9.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              6.0 * scale[1], -9.0 * scale[0], -15.0 * scale[1])
    te.end_fill()
    Moveto(4100.0 * scale[0], 420.0 * scale[1], x, y)
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
    Moveto(1801.0 * scale[0], 404.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(2907.0 * scale[0], 405.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-4.0 * scale[0], -8.0 * scale[1], -2.0 * scale[0], -
              17.0 * scale[1], 3.0 * scale[0], -20.0 * scale[1])
    Curveto_r(6.0 * scale[0], -4.0 * scale[1], 10.0 * scale[0],
              3.0 * scale[1], 10.0 * scale[0], 14.0 * scale[1])
    Curveto_r(0.0 * scale[0], 25.0 * scale[1], -6.0 * scale[0],
              27.0 * scale[1], -13.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(295.0 * scale[0], 400.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(705.0 * scale[0], 402.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-14.0 * scale[0], -10.0 * scale[1], -17.0 *
              scale[0], -32.0 * scale[1], -5.0 * scale[0], -32.0 * scale[1])
    Curveto_r(11.0 * scale[0], 0.0 * scale[1], 26.0 * scale[0],
              28.0 * scale[1], 18.0 * scale[0], 35.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 2.0 * scale[1], -8.0 * scale[0],
              1.0 * scale[1], -13.0 * scale[0], -3.0 * scale[1])
    te.end_fill()
    Moveto(750.0 * scale[0], 390.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(11.0 * scale[0], -20.0 * scale[1], 25.0 * scale[0], -
              26.0 * scale[1], 33.0 * scale[0], -12.0 * scale[1])
    Curveto_r(6.0 * scale[0], 8.0 * scale[1], -13.0 * scale[0],
              26.0 * scale[1], -31.0 * scale[0], 30.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 2.0 * scale[1], -10.0 *
              scale[0], -3.0 * scale[1], -2.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto(1646.0 * scale[0], 399.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 12.0 * scale[0], -
              9.0 * scale[1], 21.0 * scale[0], -9.0 * scale[1])
    Curveto_r(19.0 * scale[0], 0.0 * scale[1], 9.0 * scale[0],
              13.0 * scale[1], -12.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 1.0 * scale[1], -13.0 *
              scale[0], -2.0 * scale[1], -9.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(555.0 * scale[0], 371.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -2.0 * scale[0], -
              12.0 * scale[1], 3.0 * scale[0], -15.0 * scale[1])
    Curveto_r(5.0 * scale[0], -3.0 * scale[1], 9.0 * scale[0],
              1.0 * scale[1], 9.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], -3.0 * scale[0],
              19.0 * scale[1], -12.0 * scale[0], 6.0 * scale[1])
    te.end_fill()
    Moveto(1720.0 * scale[0], 362.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -13.0 * scale[1], 14.0 * scale[0], -
              21.0 * scale[1], 18.0 * scale[0], -18.0 * scale[1])
    Curveto_r(3.0 * scale[0], 4.0 * scale[1], -2.0 * scale[0],
              14.0 * scale[1], -12.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 16.0 * scale[1], -18.0 * scale[0],
              16.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(2065.0 * scale[0], 370.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 *
              scale[0], -7.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 7.0 * scale[1], 21.0 * scale[0],
              14.0 * scale[1], 7.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 0.0 * scale[1], -13.0 * scale[0], -
              4.0 * scale[1], -16.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(3012.0 * scale[0], 360.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -14.0 * scale[1], 2.0 * scale[0], -
              19.0 * scale[1], 5.0 * scale[0], -12.0 * scale[1])
    Curveto_r(2.0 * scale[0], 6.0 * scale[1], 2.0 * scale[0],
              18.0 * scale[1], 0.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              1.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(2687.0 * scale[0], 359.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -7.0 * scale[1], 15.0 * scale[0], -
              10.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              9.0 * scale[1], -12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 6.0 * scale[1], -15.0 * scale[0],
              5.0 * scale[1], -6.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(3696.0 * scale[0], 354.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-5.0 * scale[0], -14.0 * scale[1], -4.0 *
              scale[0], -15.0 * scale[1], 9.0 * scale[0], -4.0 * scale[1])
    Curveto_r(17.0 * scale[0], 14.0 * scale[1], 19.0 * scale[0],
              20.0 * scale[1], 6.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -12.0 * scale[0], -
              7.0 * scale[1], -15.0 * scale[0], -16.0 * scale[1])
    te.end_fill()
    Moveto(3945.0 * scale[0], 360.0 * scale[1], x, y)
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
    Moveto(1861.0 * scale[0], 344.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 3.0 * scale[0], -
              14.0 * scale[1], 6.0 * scale[0], -6.0 * scale[1])
    Curveto_r(3.0 * scale[0], 7.0 * scale[1], 2.0 * scale[0],
              16.0 * scale[1], -1.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 4.0 * scale[1], -6.0 * scale[0], -
              2.0 * scale[1], -5.0 * scale[0], -13.0 * scale[1])
    te.end_fill()
    Moveto(3446.0 * scale[0], 348.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 10.0 * scale[0], -
              6.0 * scale[1], 15.0 * scale[0], -3.0 * scale[1])
    Curveto_r(13.0 * scale[0], 9.0 * scale[1], 11.0 * scale[0],
              12.0 * scale[1], -6.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 0.0 * scale[1], -12.0 *
              scale[0], -4.0 * scale[1], -9.0 * scale[0], -9.0 * scale[1])
    te.end_fill()
    Moveto(3920.0 * scale[0], 324.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 5.0 * scale[0], -
              12.0 * scale[1], 10.0 * scale[0], -9.0 * scale[1])
    Curveto_r(6.0 * scale[0], 4.0 * scale[1], 8.0 * scale[0],
              11.0 * scale[1], 5.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 14.0 * scale[1], -15.0 * scale[0],
              11.0 * scale[1], -15.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto(3032.0 * scale[0], 314.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-7.0 * scale[0], -8.0 * scale[1], -8.0 * scale[0], -
              14.0 * scale[1], -3.0 * scale[0], -14.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 25.0 * scale[0],
              19.0 * scale[1], 20.0 * scale[0], 25.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 1.0 * scale[1], -10.0 * scale[0], -
              3.0 * scale[1], -17.0 * scale[0], -11.0 * scale[1])
    te.end_fill()
    Moveto(406.0 * scale[0], 287.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -10.0 * scale[1], 9.0 * scale[0], -
              15.0 * scale[1], 12.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], 3.0 * scale[1], 0.0 * scale[0],
              11.0 * scale[1], -7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 9.0 * scale[1], -11.0 * scale[0],
              8.0 * scale[1], -5.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(3938.0 * scale[0], 293.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(2255.0 * scale[0], 280.0 * scale[1], x, y)
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
    Moveto(2865.0 * scale[0], 270.0 * scale[1], x, y)
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
    Moveto(4000.0 * scale[0], 260.0 * scale[1], x, y)
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
    Moveto(305.0 * scale[0], 240.0 * scale[1], x, y)
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
    Moveto(2840.0 * scale[0], 239.0 * scale[1], x, y)
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
    Moveto(3162.0 * scale[0], 230.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -10.0 * scale[1], 14.0 * scale[0], -
              18.0 * scale[1], 15.0 * scale[0], -16.0 * scale[1])
    Curveto_r(6.0 * scale[0], 6.0 * scale[1], -9.0 * scale[0],
              36.0 * scale[1], -18.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -4.0 * scale[0], -
              9.0 * scale[1], 3.0 * scale[0], -20.0 * scale[1])
    te.end_fill()
    Moveto(2246.0 * scale[0], 203.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -14.0 * scale[1], -5.0 *
              scale[0], -15.0 * scale[1], 5.0 * scale[0], -6.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 10.0 * scale[0],
              15.0 * scale[1], 7.0 * scale[0], 18.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 3.0 * scale[1], -9.0 * scale[0], -
              2.0 * scale[1], -12.0 * scale[0], -12.0 * scale[1])
    te.end_fill()
    Moveto(3218.0 * scale[0], 143.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(3885.0 * scale[0], 110.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(3.0 * scale[0], -5.0 * scale[1], 8.0 * scale[0], -
              10.0 * scale[1], 11.0 * scale[0], -10.0 * scale[1])
    Curveto_r(2.0 * scale[0], 0.0 * scale[1], 4.0 * scale[0],
              5.0 * scale[1], 4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], -5.0 * scale[0],
              10.0 * scale[1], -11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 0.0 * scale[1], -7.0 * scale[0], -
              4.0 * scale[1], -4.0 * scale[0], -10.0 * scale[1])
    te.penup()
    te.penup()
    te.color('#b6fae2')
    te.end_fill()
    Moveto(0.0 * scale[0], 1791.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -22.0 * scale[1], 46.0 * scale[0], -
              55.0 * scale[1], 62.0 * scale[0], -45.0 * scale[1])
    Curveto_r(7.0 * scale[0], 5.0 * scale[1], 8.0 * scale[0],
              3.0 * scale[1], 3.0 * scale[0], -6.0 * scale[1])
    Curveto_r(-6.0 * scale[0], -10.0 * scale[1], -4.0 *
              scale[0], -12.0 * scale[1], 8.0 * scale[0], -7.0 * scale[1])
    Curveto_r(10.0 * scale[0], 3.0 * scale[1], 17.0 * scale[0],
              2.0 * scale[1], 17.0 * scale[0], -2.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 10.0 * scale[0], -
              7.0 * scale[1], 23.0 * scale[0], -4.0 * scale[1])
    Curveto_r(18.0 * scale[0], 4.0 * scale[1], 19.0 * scale[0],
              3.0 * scale[1], 7.0 * scale[0], -7.0 * scale[1])
    Curveto_r(-12.0 * scale[0], -10.0 * scale[1], -11.0 *
              scale[0], -11.0 * scale[1], 9.0 * scale[0], -6.0 * scale[1])
    Curveto_r(22.0 * scale[0], 5.0 * scale[1], 62.0 * scale[0],
              2.0 * scale[1], 406.0 * scale[0], -25.0 * scale[1])
    Curveto_r(204.0 * scale[0], -16.0 * scale[1], 365.0 *
              scale[0], -15.0 * scale[1], 450.0 * scale[0], 4.0 * scale[1])
    Curveto_r(50.0 * scale[0], 11.0 * scale[1], 90.0 * scale[0],
              13.0 * scale[1], 140.0 * scale[0], 8.0 * scale[1])
    Curveto_r(90.0 * scale[0], -10.0 * scale[1], 237.0 *
              scale[0], -3.0 * scale[1], 292.0 * scale[0], 14.0 * scale[1])
    Curveto_r(23.0 * scale[0], 7.0 * scale[1], 41.0 * scale[0],
              10.0 * scale[1], 38.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -14.0 * scale[1], -89.0 * scale[0], -
              30.0 * scale[1], -197.0 * scale[0], -40.0 * scale[1])
    Curveto_r(-74.0 * scale[0], -6.0 * scale[1], -121.0 * scale[0], -
              16.0 * scale[1], -149.0 * scale[0], -30.0 * scale[1])
    Curveto_r(-47.0 * scale[0], -24.0 * scale[1], -159.0 *
              scale[0], -28.0 * scale[1], -301.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-46.0 * scale[0], 5.0 * scale[1], -177.0 * scale[0],
              12.0 * scale[1], -291.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-203.0 * scale[0], 4.0 * scale[1], -207.0 * scale[0],
              3.0 * scale[1], -190.0 * scale[0], -15.0 * scale[1])
    Curveto_r(10.0 * scale[0], -11.0 * scale[1], 19.0 *
              scale[0], -15.0 * scale[1], 21.0 * scale[0], -9.0 * scale[1])
    Curveto_r(5.0 * scale[0], 15.0 * scale[1], 29.0 * scale[0],
              14.0 * scale[1], 35.0 * scale[0], -1.0 * scale[1])
    Curveto_r(4.0 * scale[0], -10.0 * scale[1], 6.0 *
              scale[0], -10.0 * scale[1], 6.0 * scale[0], 0.0 * scale[1])
    Curveto_r(1.0 * scale[0], 6.0 * scale[1], 6.0 * scale[0],
              12.0 * scale[1], 12.0 * scale[0], 12.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 8.0 * scale[0], -
              7.0 * scale[1], 5.0 * scale[0], -16.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -12.0 * scale[1], -2.0 *
              scale[0], -15.0 * scale[1], 9.0 * scale[0], -10.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 22.0 * scale[0],
              9.0 * scale[1], 30.0 * scale[0], 12.0 * scale[1])
    Curveto_r(8.0 * scale[0], 3.0 * scale[1], 15.0 * scale[0],
              1.0 * scale[1], 15.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], -6.0 * scale[1], -5.0 * scale[0], -
              11.0 * scale[1], -12.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-9.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              3.0 * scale[1], -1.0 * scale[0], -11.0 * scale[1])
    Curveto_r(9.0 * scale[0], -9.0 * scale[1], 19.0 * scale[0], -
              9.0 * scale[1], 40.0 * scale[0], -1.0 * scale[1])
    Curveto_r(29.0 * scale[0], 11.0 * scale[1], 48.0 * scale[0],
              10.0 * scale[1], 96.0 * scale[0], -3.0 * scale[1])
    Curveto_r(28.0 * scale[0], -7.0 * scale[1], 37.0 * scale[0], -
              25.0 * scale[1], 13.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-25.0 * scale[0], 0.0 * scale[1], -26.0 * scale[0], -
              28.0 * scale[1], -1.0 * scale[0], -32.0 * scale[1])
    Curveto_r(25.0 * scale[0], -5.0 * scale[1], 45.0 * scale[0],
              7.0 * scale[1], 45.0 * scale[0], 28.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], 27.0 * scale[0],
              37.0 * scale[1], 34.0 * scale[0], 25.0 * scale[1])
    Curveto_r(4.0 * scale[0], -6.0 * scale[1], 13.0 * scale[0], -
              8.0 * scale[1], 21.0 * scale[0], -4.0 * scale[1])
    Curveto_r(10.0 * scale[0], 3.0 * scale[1], 15.0 * scale[0], -
              2.0 * scale[1], 15.0 * scale[0], -17.0 * scale[1])
    Curveto_r(0.0 * scale[0], -31.0 * scale[1], 24.0 * scale[0], -
              20.0 * scale[1], 28.0 * scale[0], 13.0 * scale[1])
    Curveto_r(4.0 * scale[0], 36.0 * scale[1], 28.0 * scale[0],
              34.0 * scale[1], 41.0 * scale[0], -3.0 * scale[1])
    Curveto_r(10.0 * scale[0], -30.0 * scale[1], 43.0 * scale[0], -
              42.0 * scale[1], 56.0 * scale[0], -20.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], 12.0 * scale[0],
              7.0 * scale[1], 20.0 * scale[0], 3.0 * scale[1])
    Curveto_r(11.0 * scale[0], -3.0 * scale[1], 13.0 *
              scale[0], -1.0 * scale[1], 9.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 11.0 * scale[1], 2.0 * scale[0],
              14.0 * scale[1], 28.0 * scale[0], 13.0 * scale[1])
    Curveto_r(28.0 * scale[0], -1.0 * scale[1], 34.0 * scale[0], -
              6.0 * scale[1], 38.0 * scale[0], -31.0 * scale[1])
    Curveto_r(3.0 * scale[0], -18.0 * scale[1], 8.0 * scale[0], -
              25.0 * scale[1], 13.0 * scale[0], -18.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], 4.0 * scale[0],
              18.0 * scale[1], 1.0 * scale[0], 26.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 20.0 * scale[1], 16.0 * scale[0],
              33.0 * scale[1], 27.0 * scale[0], 16.0 * scale[1])
    Curveto_r(6.0 * scale[0], -11.0 * scale[1], 11.0 * scale[0], -
              11.0 * scale[1], 21.0 * scale[0], -1.0 * scale[1])
    Curveto_r(15.0 * scale[0], 15.0 * scale[1], 32.0 * scale[0],
              15.0 * scale[1], 81.0 * scale[0], 1.0 * scale[1])
    Curveto_r(20.0 * scale[0], -5.0 * scale[1], 37.0 * scale[0], -
              16.0 * scale[1], 37.0 * scale[0], -23.0 * scale[1])
    Curveto_r(0.0 * scale[0], -22.0 * scale[1], 31.0 * scale[0], -
              28.0 * scale[1], 46.0 * scale[0], -9.0 * scale[1])
    Curveto_r(20.0 * scale[0], 27.0 * scale[1], 24.0 * scale[0],
              52.0 * scale[1], 8.0 * scale[0], 46.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -3.0 * scale[1], -14.0 * scale[0], -
              14.0 * scale[1], -14.0 * scale[0], -24.0 * scale[1])
    Curveto_r(0.0 * scale[0], -24.0 * scale[1], -16.0 * scale[0], -
              25.0 * scale[1], -29.0 * scale[0], -1.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 10.0 * scale[1], -22.0 * scale[0],
              19.0 * scale[1], -37.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-34.0 * scale[0], 3.0 * scale[1], -41.0 * scale[0],
              9.0 * scale[1], -25.0 * scale[0], 25.0 * scale[1])
    Curveto_r(9.0 * scale[0], 9.0 * scale[1], 14.0 * scale[0],
              9.0 * scale[1], 21.0 * scale[0], -3.0 * scale[1])
    Curveto_r(9.0 * scale[0], -13.0 * scale[1], 11.0 *
              scale[0], -13.0 * scale[1], 20.0 * scale[0], 0.0 * scale[1])
    Curveto_r(7.0 * scale[0], 11.0 * scale[1], 12.0 * scale[0],
              12.0 * scale[1], 20.0 * scale[0], 4.0 * scale[1])
    Curveto_r(13.0 * scale[0], -13.0 * scale[1], 50.0 *
              scale[0], -7.0 * scale[1], 50.0 * scale[0], 7.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], 7.0 * scale[0],
              9.0 * scale[1], 15.0 * scale[0], 9.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0], -
              4.0 * scale[1], 15.0 * scale[0], -10.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 6.0 * scale[0], -
              10.0 * scale[1], 14.0 * scale[0], -10.0 * scale[1])
    Curveto_r(24.0 * scale[0], 0.0 * scale[1], 30.0 * scale[0], -
              22.0 * scale[1], 11.0 * scale[0], -37.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -10.0 * scale[1], -15.0 *
              scale[0], -13.0 * scale[1], -4.0 * scale[0], -13.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 19.0 * scale[0],
              4.0 * scale[1], 24.0 * scale[0], 9.0 * scale[1])
    Curveto_r(6.0 * scale[0], 5.0 * scale[1], 21.0 * scale[0],
              12.0 * scale[1], 35.0 * scale[0], 16.0 * scale[1])
    Curveto_r(22.0 * scale[0], 7.0 * scale[1], 23.0 * scale[0],
              6.0 * scale[1], 11.0 * scale[0], -9.0 * scale[1])
    Curveto_r(-8.0 * scale[0], -9.0 * scale[1], -9.0 * scale[0], -
              16.0 * scale[1], -3.0 * scale[0], -16.0 * scale[1])
    Curveto_r(18.0 * scale[0], 0.0 * scale[1], 24.0 * scale[0],
              20.0 * scale[1], 12.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 10.0 * scale[1], -16.0 * scale[0],
              11.0 * scale[1], -26.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-15.0 * scale[0], -13.0 * scale[1], -34.0 *
              scale[0], -4.0 * scale[1], -34.0 * scale[0], 16.0 * scale[1])
    Curveto_r(0.0 * scale[0], 19.0 * scale[1], 20.0 * scale[0],
              29.0 * scale[1], 32.0 * scale[0], 17.0 * scale[1])
    Curveto_r(8.0 * scale[0], -8.0 * scale[1], 17.0 * scale[0], -
              8.0 * scale[1], 30.0 * scale[0], -1.0 * scale[1])
    Curveto_r(14.0 * scale[0], 8.0 * scale[1], 26.0 * scale[0],
              6.0 * scale[1], 44.0 * scale[0], -6.0 * scale[1])
    Curveto_r(19.0 * scale[0], -12.0 * scale[1], 29.0 *
              scale[0], -13.0 * scale[1], 45.0 * scale[0], -5.0 * scale[1])
    Curveto_r(11.0 * scale[0], 7.0 * scale[1], 27.0 * scale[0],
              9.0 * scale[1], 35.0 * scale[0], 6.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 14.0 * scale[0],
              1.0 * scale[1], 14.0 * scale[0], 8.0 * scale[1])
    Curveto_r(0.0 * scale[0], 15.0 * scale[1], 24.0 * scale[0],
              28.0 * scale[1], 34.0 * scale[0], 19.0 * scale[1])
    Curveto_r(12.0 * scale[0], -12.0 * scale[1], 56.0 *
              scale[0], -8.0 * scale[1], 61.0 * scale[0], 5.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], 12.0 * scale[0],
              11.0 * scale[1], 20.0 * scale[0], 8.0 * scale[1])
    Curveto_r(8.0 * scale[0], -3.0 * scale[1], 15.0 *
              scale[0], -1.0 * scale[1], 15.0 * scale[0], 4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 6.0 * scale[1], 5.0 * scale[0],
              10.0 * scale[1], 10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0], -
              7.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], 4.0 * scale[0], -
              13.0 * scale[1], 8.0 * scale[0], -10.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 8.0 * scale[0],
              19.0 * scale[1], 7.0 * scale[0], 36.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 16.0 * scale[1], 0.0 * scale[0],
              30.0 * scale[1], 2.0 * scale[0], 30.0 * scale[1])
    Curveto_r(10.0 * scale[0], 0.0 * scale[1], 32.0 * scale[0], -
              28.0 * scale[1], 26.0 * scale[0], -33.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -3.0 * scale[1], 4.0 * scale[0], -
              5.0 * scale[1], 16.0 * scale[0], -4.0 * scale[1])
    Curveto_r(23.0 * scale[0], 1.0 * scale[1], 28.0 * scale[0],
              13.0 * scale[1], 9.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 2.0 * scale[1], -8.0 * scale[0],
              10.0 * scale[1], -4.0 * scale[0], 16.0 * scale[1])
    Curveto_r(5.0 * scale[0], 8.0 * scale[1], 16.0 * scale[0],
              10.0 * scale[1], 28.0 * scale[0], 6.0 * scale[1])
    Curveto_r(35.0 * scale[0], -11.0 * scale[1], 97.0 * scale[0], -
              14.0 * scale[1], 102.0 * scale[0], -5.0 * scale[1])
    Curveto_r(6.0 * scale[0], 10.0 * scale[1], -130.0 * scale[0],
              57.0 * scale[1], -193.0 * scale[0], 67.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 4.0 * scale[1], -41.0 * scale[0],
              9.0 * scale[1], -41.0 * scale[0], 13.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -95.0 * scale[0],
              4.0 * scale[1], -215.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-55.0 * scale[0], -6.0 * scale[1], -103.0 * scale[0], -
              11.0 * scale[1], -106.0 * scale[0], -11.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 1.0 * scale[1], -201.0 * scale[0],
              6.0 * scale[1], -440.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-239.0 * scale[0], 6.0 * scale[1], -514.0 * scale[0],
              13.0 * scale[1], -611.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-169.0 * scale[0], 4.0 * scale[1], -178.0 * scale[0],
              4.0 * scale[1], -178.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(4140.0 * scale[0], 1750.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-52.0 * scale[0], -4.0 * scale[1], -123.0 * scale[0], -
              13.0 * scale[1], -157.0 * scale[0], -20.0 * scale[1])
    Lineto_r(-62.0 * scale[0], -12.0 * scale[1])
    Lineto_r(16.0 * scale[0], -24.0 * scale[1])
    Curveto_r(19.0 * scale[0], -30.0 * scale[1], 53.0 *
              scale[0], -32.0 * scale[1], 53.0 * scale[0], -4.0 * scale[1])
    Curveto_r(0.0 * scale[0], 24.0 * scale[1], 25.0 * scale[0],
              26.0 * scale[1], 46.0 * scale[0], 5.0 * scale[1])
    Curveto_r(14.0 * scale[0], -13.0 * scale[1], 11.0 * scale[0], -
              19.0 * scale[1], -7.0 * scale[0], -17.0 * scale[1])
    Curveto_r(-4.0 * scale[0], 1.0 * scale[1], -15.0 * scale[0], -
              8.0 * scale[1], -24.0 * scale[0], -18.0 * scale[1])
    Curveto_r(-10.0 * scale[0], -11.0 * scale[1], -13.0 *
              scale[0], -20.0 * scale[1], -7.0 * scale[0], -20.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 13.0 * scale[0],
              6.0 * scale[1], 16.0 * scale[0], 13.0 * scale[1])
    Curveto_r(3.0 * scale[0], 8.0 * scale[1], 11.0 * scale[0],
              5.0 * scale[1], 25.0 * scale[0], -11.0 * scale[1])
    Curveto_r(20.0 * scale[0], -23.0 * scale[1], 20.0 *
              scale[0], -23.0 * scale[1], 77.0 * scale[0], 6.0 * scale[1])
    Curveto_r(12.0 * scale[0], 6.0 * scale[1], 27.0 * scale[0],
              7.0 * scale[1], 34.0 * scale[0], 2.0 * scale[1])
    Curveto_r(8.0 * scale[0], -5.0 * scale[1], 17.0 * scale[0], -
              7.0 * scale[1], 21.0 * scale[0], -4.0 * scale[1])
    Curveto_r(4.0 * scale[0], 2.0 * scale[1], 10.0 * scale[0], -
              4.0 * scale[1], 13.0 * scale[0], -13.0 * scale[1])
    Curveto_r(6.0 * scale[0], -15.0 * scale[1], 8.0 * scale[0], -
              14.0 * scale[1], 20.0 * scale[0], 2.0 * scale[1])
    Curveto_r(9.0 * scale[0], 13.0 * scale[1], 15.0 * scale[0],
              15.0 * scale[1], 20.0 * scale[0], 7.0 * scale[1])
    Curveto_r(13.0 * scale[0], -21.0 * scale[1], 28.0 *
              scale[0], -14.0 * scale[1], 16.0 * scale[0], 7.0 * scale[1])
    Curveto_r(-12.0 * scale[0], 24.0 * scale[1], -13.0 * scale[0],
              41.0 * scale[1], -1.0 * scale[0], 22.0 * scale[1])
    Curveto_r(8.0 * scale[0], -12.0 * scale[1], 12.0 * scale[0], -
              12.0 * scale[1], 24.0 * scale[0], -2.0 * scale[1])
    Curveto_r(13.0 * scale[0], 10.0 * scale[1], 17.0 * scale[0],
              9.0 * scale[1], 24.0 * scale[0], -4.0 * scale[1])
    Curveto_r(6.0 * scale[0], -9.0 * scale[1], 23.0 * scale[0], -
              17.0 * scale[1], 42.0 * scale[0], -17.0 * scale[1])
    Curveto_r(26.0 * scale[0], -1.0 * scale[1], 32.0 * scale[0], -
              5.0 * scale[1], 28.0 * scale[0], -20.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -12.0 * scale[1], 0.0 * scale[0], -
              18.0 * scale[1], 13.0 * scale[0], -18.0 * scale[1])
    Curveto_r(13.0 * scale[0], 0.0 * scale[1], 17.0 * scale[0],
              5.0 * scale[1], 13.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 23.0 * scale[1], 15.0 * scale[0],
              28.0 * scale[1], 23.0 * scale[0], 5.0 * scale[1])
    Curveto_r(4.0 * scale[0], -8.0 * scale[1], 12.0 * scale[0], -
              15.0 * scale[1], 19.0 * scale[0], -15.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0], -
              3.0 * scale[1], 18.0 * scale[0], -7.0 * scale[1])
    Curveto_r(2.0 * scale[0], -5.0 * scale[1], 2.0 *
              scale[0], -2.0 * scale[1], 1.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 7.0 * scale[1], 8.0 * scale[0],
              12.0 * scale[1], 29.0 * scale[0], 13.0 * scale[1])
    Lineto_r(32.0 * scale[0], 1.0 * scale[1])
    Lineto_r(-34.0 * scale[0], 12.0 * scale[1])
    Curveto_r(-36.0 * scale[0], 13.0 * scale[1], -49.0 * scale[0],
              30.0 * scale[1], -32.0 * scale[0], 40.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 21.0 * scale[0],
              2.0 * scale[1], 35.0 * scale[0], -4.0 * scale[1])
    Curveto_r(25.0 * scale[0], -9.0 * scale[1], 26.0 *
              scale[0], -8.0 * scale[1], 26.0 * scale[0], 30.0 * scale[1])
    Lineto_r(0.0 * scale[0], 40.0 * scale[1])
    Lineto_r(-67.0 * scale[0], 0.0 * scale[1])
    Curveto_r(-38.0 * scale[0], 0.0 * scale[1], -97.0 * scale[0],
              2.0 * scale[1], -133.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-36.0 * scale[0], 2.0 * scale[1], -108.0 * scale[0],
              1.0 * scale[1], -160.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto_r(80.0 * scale[0], -64.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], -11.0 * scale[0], -
              14.0 * scale[1], -35.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-37.0 * scale[0], 1.0 * scale[1], -47.0 * scale[0],
              12.0 * scale[1], -17.0 * scale[0], 20.0 * scale[1])
    Curveto_r(34.0 * scale[0], 9.0 * scale[1], 52.0 * scale[0],
              7.0 * scale[1], 52.0 * scale[0], -7.0 * scale[1])
    te.end_fill()
    Moveto_r(204.0 * scale[0], -19.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -27.0 * scale[1], -3.0 * scale[0], -
              37.0 * scale[1], -15.0 * scale[0], -14.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 9.0 * scale[1], -19.0 * scale[0],
              17.0 * scale[1], -29.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-22.0 * scale[0], 0.0 * scale[1], -27.0 * scale[0],
              16.0 * scale[1], -7.0 * scale[0], 23.0 * scale[1])
    Curveto_r(22.0 * scale[0], 7.0 * scale[1], 45.0 * scale[0], -
              4.0 * scale[1], 51.0 * scale[0], -26.0 * scale[1])
    te.end_fill()
    Moveto_r(-324.0 * scale[0], 8.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -8.0 * scale[1], -9.0 * scale[0], -
              15.0 * scale[1], -20.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-17.0 * scale[0], 0.0 * scale[1], -19.0 * scale[0],
              2.0 * scale[1], -8.0 * scale[0], 15.0 * scale[1])
    Curveto_r(17.0 * scale[0], 19.0 * scale[1], 28.0 * scale[0],
              19.0 * scale[1], 28.0 * scale[0], 0.0 * scale[1])
    te.end_fill()
    Moveto(0.0 * scale[0], 1709.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 4.0 * scale[0], -
              18.0 * scale[1], 10.0 * scale[0], -14.0 * scale[1])
    Curveto_r(5.0 * scale[0], 3.0 * scale[1], 7.0 * scale[0],
              12.0 * scale[1], 3.0 * scale[0], 20.0 * scale[1])
    Curveto_r(-7.0 * scale[0], 21.0 * scale[1], -13.0 * scale[0],
              19.0 * scale[1], -13.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(1813.0 * scale[0], 1702.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(11.0 * scale[0], -11.0 * scale[1], 16.0 * scale[0], -
              25.0 * scale[1], 13.0 * scale[0], -30.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], 1.0 * scale[0], -
              18.0 * scale[1], 9.0 * scale[0], -28.0 * scale[1])
    Curveto_r(13.0 * scale[0], -17.0 * scale[1], 14.0 *
              scale[0], -18.0 * scale[1], 15.0 * scale[0], -1.0 * scale[1])
    Curveto_r(0.0 * scale[0], 9.0 * scale[1], 4.0 * scale[0],
              17.0 * scale[1], 10.0 * scale[0], 17.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 7.0 * scale[0], -
              7.0 * scale[1], 4.0 * scale[0], -15.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -9.0 * scale[1], 1.0 * scale[0], -
              17.0 * scale[1], 10.0 * scale[0], -20.0 * scale[1])
    Curveto_r(9.0 * scale[0], -3.0 * scale[1], 24.0 * scale[0], -
              8.0 * scale[1], 34.0 * scale[0], -11.0 * scale[1])
    Curveto_r(9.0 * scale[0], -4.0 * scale[1], 26.0 * scale[0], -
              7.0 * scale[1], 37.0 * scale[0], -8.0 * scale[1])
    Curveto_r(13.0 * scale[0], -1.0 * scale[1], 21.0 * scale[0], -
              10.0 * scale[1], 25.0 * scale[0], -27.0 * scale[1])
    Curveto_r(4.0 * scale[0], -22.0 * scale[1], 10.0 * scale[0], -
              26.0 * scale[1], 33.0 * scale[0], -23.0 * scale[1])
    Curveto_r(17.0 * scale[0], 2.0 * scale[1], 30.0 * scale[0], -
              3.0 * scale[1], 34.0 * scale[0], -12.0 * scale[1])
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], 9.0 * scale[0], -
              14.0 * scale[1], 14.0 * scale[0], -14.0 * scale[1])
    Curveto_r(5.0 * scale[0], 0.0 * scale[1], 18.0 * scale[0], -
              9.0 * scale[1], 29.0 * scale[0], -20.0 * scale[1])
    Curveto_r(11.0 * scale[0], -11.0 * scale[1], 29.0 * scale[0], -
              20.0 * scale[1], 40.0 * scale[0], -20.0 * scale[1])
    Curveto_r(12.0 * scale[0], 0.0 * scale[1], 20.0 * scale[0], -
              7.0 * scale[1], 20.0 * scale[0], -16.0 * scale[1])
    Curveto_r(0.0 * scale[0], -11.0 * scale[1], 6.0 * scale[0], -
              15.0 * scale[1], 20.0 * scale[0], -11.0 * scale[1])
    Curveto_r(10.0 * scale[0], 3.0 * scale[1], 20.0 * scale[0],
              2.0 * scale[1], 22.0 * scale[0], -2.0 * scale[1])
    Curveto_r(6.0 * scale[0], -11.0 * scale[1], 73.0 * scale[0], -
              39.0 * scale[1], 111.0 * scale[0], -46.0 * scale[1])
    Curveto_r(21.0 * scale[0], -3.0 * scale[1], 40.0 * scale[0], -
              11.0 * scale[1], 43.0 * scale[0], -18.0 * scale[1])
    Curveto_r(5.0 * scale[0], -14.0 * scale[1], 104.0 * scale[0], -
              18.0 * scale[1], 101.0 * scale[0], -4.0 * scale[1])
    Curveto_r(-1.0 * scale[0], 5.0 * scale[1], 4.0 * scale[0],
              12.0 * scale[1], 11.0 * scale[0], 14.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 12.0 * scale[0], -
              2.0 * scale[1], 12.0 * scale[0], -11.0 * scale[1])
    Curveto_r(0.0 * scale[0], -10.0 * scale[1], 6.0 * scale[0], -
              13.0 * scale[1], 17.0 * scale[0], -9.0 * scale[1])
    Curveto_r(12.0 * scale[0], 5.0 * scale[1], 14.0 * scale[0],
              3.0 * scale[1], 9.0 * scale[0], -8.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -8.0 * scale[1], -1.0 *
              scale[0], -6.0 * scale[1], 6.0 * scale[0], 3.0 * scale[1])
    Curveto_r(18.0 * scale[0], 21.0 * scale[1], 42.0 * scale[0],
              8.0 * scale[1], 34.0 * scale[0], -19.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -14.0 * scale[1], -2.0 *
              scale[0], -20.0 * scale[1], 9.0 * scale[0], -20.0 * scale[1])
    Curveto_r(8.0 * scale[0], 0.0 * scale[1], 15.0 * scale[0],
              9.0 * scale[1], 15.0 * scale[0], 19.0 * scale[1])
    Curveto_r(0.0 * scale[0], 10.0 * scale[1], 5.0 * scale[0],
              18.0 * scale[1], 10.0 * scale[0], 18.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              7.0 * scale[1], 10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 22.0 * scale[1], 18.0 * scale[0],
              18.0 * scale[1], 25.0 * scale[0], -6.0 * scale[1])
    Curveto_r(5.0 * scale[0], -16.0 * scale[1], 12.0 * scale[0], -
              19.0 * scale[1], 30.0 * scale[0], -15.0 * scale[1])
    Curveto_r(13.0 * scale[0], 3.0 * scale[1], 27.0 * scale[0],
              2.0 * scale[1], 30.0 * scale[0], -4.0 * scale[1])
    Curveto_r(9.0 * scale[0], -14.0 * scale[1], 35.0 *
              scale[0], -12.0 * scale[1], 35.0 * scale[0], 3.0 * scale[1])
    Curveto_r(0.0 * scale[0], 19.0 * scale[1], 58.0 * scale[0],
              41.0 * scale[1], 73.0 * scale[0], 28.0 * scale[1])
    Curveto_r(14.0 * scale[0], -11.0 * scale[1], 53.0 *
              scale[0], -5.0 * scale[1], 74.0 * scale[0], 11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 5.0 * scale[1], 17.0 * scale[0],
              7.0 * scale[1], 22.0 * scale[0], 4.0 * scale[1])
    Curveto_r(5.0 * scale[0], -4.0 * scale[1], 12.0 *
              scale[0], -2.0 * scale[1], 15.0 * scale[0], 3.0 * scale[1])
    Curveto_r(3.0 * scale[0], 5.0 * scale[1], 21.0 * scale[0],
              9.0 * scale[1], 40.0 * scale[0], 9.0 * scale[1])
    Curveto_r(21.0 * scale[0], 0.0 * scale[1], 43.0 * scale[0],
              8.0 * scale[1], 56.0 * scale[0], 20.0 * scale[1])
    Curveto_r(12.0 * scale[0], 11.0 * scale[1], 41.0 * scale[0],
              24.0 * scale[1], 64.0 * scale[0], 27.0 * scale[1])
    Curveto_r(22.0 * scale[0], 4.0 * scale[1], 46.0 * scale[0],
              12.0 * scale[1], 53.0 * scale[0], 17.0 * scale[1])
    Curveto_r(6.0 * scale[0], 5.0 * scale[1], 30.0 * scale[0],
              11.0 * scale[1], 52.0 * scale[0], 13.0 * scale[1])
    Curveto_r(23.0 * scale[0], 2.0 * scale[1], 48.0 * scale[0],
              11.0 * scale[1], 57.0 * scale[0], 19.0 * scale[1])
    Curveto_r(22.0 * scale[0], 22.0 * scale[1], 93.0 * scale[0],
              18.0 * scale[1], 79.0 * scale[0], -5.0 * scale[1])
    Curveto_r(-3.0 * scale[0], -4.0 * scale[1], 8.0 * scale[0], -
              7.0 * scale[1], 25.0 * scale[0], -6.0 * scale[1])
    Curveto_r(16.0 * scale[0], 1.0 * scale[1], 30.0 * scale[0],
              5.0 * scale[1], 30.0 * scale[0], 9.0 * scale[1])
    Curveto_r(0.0 * scale[0], 14.0 * scale[1], 63.0 * scale[0],
              38.0 * scale[1], 75.0 * scale[0], 28.0 * scale[1])
    Curveto_r(6.0 * scale[0], -5.0 * scale[1], 15.0 * scale[0], -
              7.0 * scale[1], 18.0 * scale[0], -3.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              12.0 * scale[1], -11.0 * scale[0], 19.0 * scale[1])
    Curveto_r(-13.0 * scale[0], 10.0 * scale[1], -14.0 * scale[0],
              15.0 * scale[1], -5.0 * scale[0], 25.0 * scale[1])
    Curveto_r(9.0 * scale[0], 9.0 * scale[1], 15.0 * scale[0],
              9.0 * scale[1], 26.0 * scale[0], 0.0 * scale[1])
    Curveto_r(12.0 * scale[0], -9.0 * scale[1], 16.0 *
              scale[0], -8.0 * scale[1], 20.0 * scale[0], 2.0 * scale[1])
    Curveto_r(6.0 * scale[0], 16.0 * scale[1], 67.0 * scale[0],
              11.0 * scale[1], 67.0 * scale[0], -5.0 * scale[1])
    Curveto_r(0.0 * scale[0], -5.0 * scale[1], 15.0 * scale[0], -
              8.0 * scale[1], 33.0 * scale[0], -6.0 * scale[1])
    Curveto_r(23.0 * scale[0], 2.0 * scale[1], 32.0 * scale[0],
              8.0 * scale[1], 31.0 * scale[0], 21.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 20.0 * scale[1], 1.0 * scale[0],
              21.0 * scale[1], 26.0 * scale[0], 7.0 * scale[1])
    Curveto_r(11.0 * scale[0], -6.0 * scale[1], 17.0 * scale[0], -
              17.0 * scale[1], 14.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -8.0 * scale[1], -1.0 * scale[0], -
              15.0 * scale[1], 5.0 * scale[0], -15.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 11.0 * scale[0],
              5.0 * scale[1], 11.0 * scale[0], 10.0 * scale[1])
    Curveto_r(0.0 * scale[0], 17.0 * scale[1], 3.0 * scale[0],
              25.0 * scale[1], 17.0 * scale[0], 38.0 * scale[1])
    Curveto_r(33.0 * scale[0], 34.0 * scale[1], 16.0 * scale[0],
              37.0 * scale[1], -164.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-193.0 * scale[0], -3.0 * scale[1], -245.0 *
              scale[0], -12.0 * scale[1], -371.0 * scale[0], -63.0 * scale[1])
    Curveto_r(-43.0 * scale[0], -17.0 * scale[1], -84.0 *
              scale[0], -34.0 * scale[1], -92.0 * scale[0], -37.0 * scale[1])
    Curveto_r(-13.0 * scale[0], -5.0 * scale[1], -13.0 *
              scale[0], -3.0 * scale[1], -1.0 * scale[0], 11.0 * scale[1])
    Curveto_r(7.0 * scale[0], 9.0 * scale[1], 19.0 * scale[0],
              17.0 * scale[1], 25.0 * scale[0], 17.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 21.0 * scale[0],
              7.0 * scale[1], 32.0 * scale[0], 15.0 * scale[1])
    Curveto_r(17.0 * scale[0], 13.0 * scale[1], 16.0 * scale[0],
              14.0 * scale[1], -15.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-19.0 * scale[0], -5.0 * scale[1], -42.0 * scale[0], -
              17.0 * scale[1], -51.0 * scale[0], -25.0 * scale[1])
    Curveto_r(-20.0 * scale[0], -18.0 * scale[1], -112.0 *
              scale[0], -21.0 * scale[1], -325.0 * scale[0], -10.0 * scale[1])
    Curveto_r(-60.0 * scale[0], 2.0 * scale[1], -208.0 * scale[0],
              7.0 * scale[1], -328.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-227.0 * scale[0], 6.0 * scale[1], -240.0 * scale[0],
              8.0 * scale[1], -271.0 * scale[0], 34.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 9.0 * scale[1], -16.0 * scale[0],
              10.0 * scale[1], -12.0 * scale[0], 4.0 * scale[1])
    Curveto_r(4.0 * scale[0], -7.0 * scale[1], 5.0 * scale[0], -
              13.0 * scale[1], 2.0 * scale[0], -13.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -62.0 * scale[0],
              25.0 * scale[1], -133.0 * scale[0], 56.0 * scale[1])
    Curveto_r(-172.0 * scale[0], 75.0 * scale[1], -161.0 * scale[0],
              71.0 * scale[1], -140.0 * scale[0], 46.0 * scale[1])
    te.end_fill()
    Moveto_r(405.0 * scale[0], -180.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(22.0 * scale[0], -11.0 * scale[1], 53.0 * scale[0], -
              17.0 * scale[1], 77.0 * scale[0], -15.0 * scale[1])
    Curveto_r(22.0 * scale[0], 2.0 * scale[1], 81.0 * scale[0], -
              4.0 * scale[1], 130.0 * scale[0], -12.0 * scale[1])
    Curveto_r(116.0 * scale[0], -19.0 * scale[1], 306.0 *
              scale[0], -28.0 * scale[1], 339.0 * scale[0], -15.0 * scale[1])
    Curveto_r(43.0 * scale[0], 16.0 * scale[1], 29.0 * scale[0],
              0.0 * scale[1], -18.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-72.0 * scale[0], -32.0 * scale[1], -130.0 *
              scale[0], -39.0 * scale[1], -196.0 * scale[0], -23.0 * scale[1])
    Curveto_r(-41.0 * scale[0], 9.0 * scale[1], -79.0 * scale[0],
              11.0 * scale[1], -124.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-75.0 * scale[0], -9.0 * scale[1], -117.0 * scale[0],
              2.0 * scale[1], -171.0 * scale[0], 43.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 15.0 * scale[1], -50.0 * scale[0],
              33.0 * scale[1], -67.0 * scale[0], 41.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 8.0 * scale[1], -27.0 * scale[0],
              14.0 * scale[1], -20.0 * scale[0], 15.0 * scale[1])
    Curveto_r(7.0 * scale[0], 0.0 * scale[1], 29.0 * scale[0], -
              8.0 * scale[1], 50.0 * scale[0], -18.0 * scale[1])
    te.end_fill()
    Moveto_r(770.0 * scale[0], 13.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-6.0 * scale[0], -7.0 * scale[1], -139.0 * scale[0], -
              45.0 * scale[1], -153.0 * scale[0], -45.0 * scale[1])
    Curveto_r(-18.0 * scale[0], 1.0 * scale[1], 30.0 * scale[0],
              24.0 * scale[1], 75.0 * scale[0], 36.0 * scale[1])
    Curveto_r(48.0 * scale[0], 13.0 * scale[1], 87.0 * scale[0],
              18.0 * scale[1], 78.0 * scale[0], 9.0 * scale[1])
    te.end_fill()
    Moveto_r(-321.0 * scale[0], -151.0 * scale[1], 0, 0)
    te.begin_fill()
    Curveto_r(-9.0 * scale[0], -9.0 * scale[1], -28.0 * scale[0],
              6.0 * scale[1], -21.0 * scale[0], 18.0 * scale[1])
    Curveto_r(4.0 * scale[0], 6.0 * scale[1], 10.0 * scale[0],
              6.0 * scale[1], 17.0 * scale[0], -1.0 * scale[1])
    Curveto_r(6.0 * scale[0], -6.0 * scale[1], 8.0 * scale[0], -
              13.0 * scale[1], 4.0 * scale[0], -17.0 * scale[1])
    te.end_fill()
    Moveto(3885.0 * scale[0], 1710.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -5.0 * scale[1], -18.0 * scale[0], -
              10.0 * scale[1], -33.0 * scale[0], -10.0 * scale[1])
    Lineto_r(-27.0 * scale[0], 0.0 * scale[1])
    Lineto_r(25.0 * scale[0], -13.0 * scale[1])
    Curveto_r(14.0 * scale[0], -8.0 * scale[1], 32.0 * scale[0], -
              11.0 * scale[1], 39.0 * scale[0], -8.0 * scale[1])
    Curveto_r(11.0 * scale[0], 3.0 * scale[1], 12.0 * scale[0],
              6.0 * scale[1], 3.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-10.0 * scale[0], 3.0 * scale[1], -10.0 * scale[0],
              7.0 * scale[1], -1.0 * scale[0], 18.0 * scale[1])
    Curveto_r(6.0 * scale[0], 8.0 * scale[1], 9.0 * scale[0],
              14.0 * scale[1], 6.0 * scale[0], 14.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -9.0 * scale[0], -
              4.0 * scale[1], -12.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(40.0 * scale[0], 1690.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(12.0 * scale[0], -23.0 * scale[1], 26.0 *
              scale[0], -26.0 * scale[1], 33.0 * scale[0], -7.0 * scale[1])
    Curveto_r(3.0 * scale[0], 9.0 * scale[1], 7.0 * scale[0],
              9.0 * scale[1], 19.0 * scale[0], -1.0 * scale[1])
    Curveto_r(12.0 * scale[0], -9.0 * scale[1], 18.0 * scale[0], -
              10.0 * scale[1], 23.0 * scale[0], -2.0 * scale[1])
    Curveto_r(9.0 * scale[0], 15.0 * scale[1], 7.0 * scale[0],
              16.0 * scale[1], -43.0 * scale[0], 24.0 * scale[1])
    Curveto_r(-41.0 * scale[0], 6.0 * scale[1], -42.0 * scale[0],
              5.0 * scale[1], -32.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(158.0 * scale[0], 1703.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(223.0 * scale[0], 1693.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 25.0 *
              scale[0], -2.0 * scale[1], 35.0 * scale[0], 0.0 * scale[1])
    Curveto_r(9.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-19.0 * scale[0], 0.0 * scale[1], -27.0 *
              scale[0], -2.0 * scale[1], -17.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(150.0 * scale[0], 1680.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(8.0 * scale[0], -5.0 * scale[1], 26.0 * scale[0], -
              10.0 * scale[1], 40.0 * scale[0], -10.0 * scale[1])
    Curveto_r(20.0 * scale[0], 0.0 * scale[1], 22.0 * scale[0],
              2.0 * scale[1], 10.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 5.0 * scale[1], -26.0 * scale[0],
              10.0 * scale[1], -40.0 * scale[0], 10.0 * scale[1])
    Curveto_r(-20.0 * scale[0], 0.0 * scale[1], -22.0 * scale[0], -
              2.0 * scale[1], -10.0 * scale[0], -10.0 * scale[1])
    te.end_fill()
    Moveto(373.0 * scale[0], 1683.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(20.0 * scale[0], -2.0 * scale[1], 54.0 *
              scale[0], -2.0 * scale[1], 75.0 * scale[0], 0.0 * scale[1])
    Curveto_r(20.0 * scale[0], 2.0 * scale[1], 3.0 * scale[0],
              4.0 * scale[1], -38.0 * scale[0], 4.0 * scale[1])
    Curveto_r(-41.0 * scale[0], 0.0 * scale[1], -58.0 *
              scale[0], -2.0 * scale[1], -37.0 * scale[0], -4.0 * scale[1])
    te.end_fill()
    Moveto(3757.0 * scale[0], 1675.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-27.0 * scale[0], -7.0 * scale[1], -52.0 * scale[0], -
              17.0 * scale[1], -55.0 * scale[0], -21.0 * scale[1])
    Curveto_r(-4.0 * scale[0], -4.0 * scale[1], 1.0 * scale[0], -
              4.0 * scale[1], 11.0 * scale[0], -1.0 * scale[1])
    Curveto_r(12.0 * scale[0], 5.0 * scale[1], 25.0 * scale[0],
              0.0 * scale[1], 35.0 * scale[0], -12.0 * scale[1])
    Curveto_r(10.0 * scale[0], -10.0 * scale[1], 35.0 * scale[0], -
              22.0 * scale[1], 57.0 * scale[0], -26.0 * scale[1])
    Curveto_r(22.0 * scale[0], -4.0 * scale[1], 36.0 *
              scale[0], -3.0 * scale[1], 32.0 * scale[0], 2.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 4.0 * scale[1], -13.0 * scale[0],
              9.0 * scale[1], -18.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-5.0 * scale[0], 1.0 * scale[1], -11.0 * scale[0],
              2.0 * scale[1], -14.0 * scale[0], 3.0 * scale[1])
    Curveto_r(-3.0 * scale[0], 0.0 * scale[1], -1.0 * scale[0],
              10.0 * scale[1], 5.0 * scale[0], 21.0 * scale[1])
    Curveto_r(9.0 * scale[0], 17.0 * scale[1], 8.0 * scale[0],
              19.0 * scale[1], -7.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-16.0 * scale[0], -6.0 * scale[1], -16.0 *
              scale[0], -5.0 * scale[1], -4.0 * scale[0], 10.0 * scale[1])
    Curveto_r(7.0 * scale[0], 9.0 * scale[1], 12.0 * scale[0],
              17.0 * scale[1], 10.0 * scale[0], 16.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -26.0 * scale[0], -
              7.0 * scale[1], -52.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(553.0 * scale[0], 1673.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(9.0 * scale[0], -2.0 * scale[1], 23.0 *
              scale[0], -2.0 * scale[1], 30.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], -1.0 * scale[0],
              5.0 * scale[1], -18.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-16.0 * scale[0], 0.0 * scale[1], -22.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(255.0 * scale[0], 1656.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(20.0 * scale[0], -14.0 * scale[1], 35.0 *
              scale[0], -12.0 * scale[1], 35.0 * scale[0], 5.0 * scale[1])
    Curveto_r(0.0 * scale[0], 5.0 * scale[1], -12.0 * scale[0],
              9.0 * scale[1], -27.0 * scale[0], 9.0 * scale[1])
    Curveto_r(-26.0 * scale[0], 0.0 * scale[1], -26.0 *
              scale[0], -1.0 * scale[1], -8.0 * scale[0], -14.0 * scale[1])
    te.end_fill()
    Moveto(618.0 * scale[0], 1663.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(6.0 * scale[0], -2.0 * scale[1], 18.0 *
              scale[0], -2.0 * scale[1], 25.0 * scale[0], 0.0 * scale[1])
    Curveto_r(6.0 * scale[0], 3.0 * scale[1], 1.0 * scale[0],
              5.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-14.0 * scale[0], 0.0 * scale[1], -19.0 *
              scale[0], -2.0 * scale[1], -12.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(3920.0 * scale[0], 1650.0 * scale[1], x, y)
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
    Moveto(3685.0 * scale[0], 1619.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -7.0 * scale[1], -19.0 *
              scale[0], -8.0 * scale[1], 2.0 * scale[0], -8.0 * scale[1])
    Curveto_r(12.0 * scale[0], -1.0 * scale[1], 24.0 * scale[0], -
              7.0 * scale[1], 26.0 * scale[0], -13.0 * scale[1])
    Curveto_r(3.0 * scale[0], -8.0 * scale[1], 6.0 *
              scale[0], -7.0 * scale[1], 6.0 * scale[0], 4.0 * scale[1])
    Curveto_r(1.0 * scale[0], 22.0 * scale[1], -9.0 * scale[0],
              27.0 * scale[1], -34.0 * scale[0], 17.0 * scale[1])
    te.end_fill()
    Moveto(3738.0 * scale[0], 1603.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(7.0 * scale[0], -3.0 * scale[1], 16.0 *
              scale[0], -2.0 * scale[1], 19.0 * scale[0], 1.0 * scale[1])
    Curveto_r(4.0 * scale[0], 3.0 * scale[1], -2.0 * scale[0],
              6.0 * scale[1], -13.0 * scale[0], 5.0 * scale[1])
    Curveto_r(-11.0 * scale[0], 0.0 * scale[1], -14.0 *
              scale[0], -3.0 * scale[1], -6.0 * scale[0], -6.0 * scale[1])
    te.end_fill()
    Moveto(4335.0 * scale[0], 1590.0 * scale[1], x, y)
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
    Moveto(515.0 * scale[0], 1560.0 * scale[1], x, y)
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
    Moveto(985.0 * scale[0], 1559.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-10.0 * scale[0], -15.0 * scale[1], 3.0 * scale[0], -
              25.0 * scale[1], 16.0 * scale[0], -12.0 * scale[1])
    Curveto_r(7.0 * scale[0], 7.0 * scale[1], 7.0 * scale[0],
              13.0 * scale[1], 1.0 * scale[0], 17.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 3.0 * scale[1], -14.0 * scale[0],
              1.0 * scale[1], -17.0 * scale[0], -5.0 * scale[1])
    te.end_fill()
    Moveto(1026.0 * scale[0], 1562.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -6.0 * scale[1], 1.0 * scale[0], -
              13.0 * scale[1], 10.0 * scale[0], -16.0 * scale[1])
    Curveto_r(23.0 * scale[0], -9.0 * scale[1], 28.0 *
              scale[0], -2.0 * scale[1], 10.0 * scale[0], 13.0 * scale[1])
    Curveto_r(-8.0 * scale[0], 7.0 * scale[1], -17.0 * scale[0],
              8.0 * scale[1], -20.0 * scale[0], 3.0 * scale[1])
    te.end_fill()
    Moveto(3455.0 * scale[0], 1562.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-19.0 * scale[0], -13.0 * scale[1], -14.0 *
              scale[0], -42.0 * scale[1], 7.0 * scale[0], -42.0 * scale[1])
    Curveto_r(17.0 * scale[0], 0.0 * scale[1], 18.0 * scale[0],
              3.0 * scale[1], 8.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-6.0 * scale[0], 8.0 * scale[1], -9.0 * scale[0],
              19.0 * scale[1], -5.0 * scale[0], 25.0 * scale[1])
    Curveto_r(7.0 * scale[0], 12.0 * scale[1], 4.0 * scale[0],
              13.0 * scale[1], -10.0 * scale[0], 2.0 * scale[1])
    te.end_fill()
    Moveto(746.0 * scale[0], 1535.0 * scale[1], x, y)
    te.begin_fill()
    Curveto_r(-3.0 * scale[0], -8.0 * scale[1], -1.0 * scale[0], -
              15.0 * scale[1], 4.0 * scale[0], -15.0 * scale[1])
    Curveto_r(6.0 * scale[0], 0.0 * scale[1], 10.0 * scale[0],
              7.0 * scale[1], 10.0 * scale[0], 15.0 * scale[1])
    Curveto_r(0.0 * scale[0], 8.0 * scale[1], -2.0 * scale[0],
              15.0 * scale[1], -4.0 * scale[0], 15.0 * scale[1])
    Curveto_r(-2.0 * scale[0], 0.0 * scale[1], -6.0 * scale[0], -
              7.0 * scale[1], -10.0 * scale[0], -15.0 * scale[1])
    te.penup()
