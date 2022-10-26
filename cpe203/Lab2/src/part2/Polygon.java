package part2;

import java.util.List;

public class Polygon {
    private final List<Point> points;

    public Polygon(List<Point> points) {
        this.points = points;
    }

    public List<Point> getPoints() { return points; }

    public double perimeter() {
        double sum = 0;
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
