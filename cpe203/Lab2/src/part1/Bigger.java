package part1;

public class Bigger {
    public static double whichIsBigger(Circle cir, Rectangle rect, Polygon poly) {
        double cirPerim = Util.perimeter(cir);
        double rectPerim = Util.perimeter(rect);
        double polyPerim = Util.perimeter(poly);
        if (cirPerim >= rectPerim) {
            if (cirPerim >= polyPerim)
                return cirPerim;
        } else {
            if (rectPerim >= polyPerim)
                return rectPerim;
        }
        return polyPerim;
    }
}
