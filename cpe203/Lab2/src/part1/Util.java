package part1;

import java.util.List;

public class Util {
    public static double perimeter(Circle circle) {
        return 2 * Math.PI * circle.getRadius();
    }

    public static double perimeter(Rectangle rectangle) {
        return Math.abs(2 * (rectangle.getBottomRight().getX() - rectangle.getTopLeft().getX() +
                (rectangle.getBottomRight().getY() - rectangle.getTopLeft().getY())));
    }

    public static double perimeter(Polygon polygon) {
        double sum = 0;
        List<Point> points = polygon.getPoints();
        for (int i = 0; i<(points.size()) ; i++) {
            double a = 0;
            double b = 0;
            if (i == points.size()-1) {
                a = Math.abs(points.get(0).getX() - points.get(i).getX());
                b = Math.abs(points.get(0).getY() - points.get(i).getY());
            } else {
                a = Math.abs(points.get(i + 1).getX() - points.get(i).getX());
                b = Math.abs(points.get(i + 1).getY() - points.get(i).getY());
            }
            sum += Math.sqrt(a * a + b * b);
        }
        return sum;
    }
}
