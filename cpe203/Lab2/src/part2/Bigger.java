package part2;

public class Bigger {
    public static double whichIsBigger(Circle cir, Rectangle rect, Polygon poly) {
        double cirPerim = cir.perimeter();
        double rectPerim = rect.perimeter();
        double polyPerim = poly.perimeter();
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
