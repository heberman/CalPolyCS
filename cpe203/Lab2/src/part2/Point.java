package part2;
public class Point {
    private final double x;
    private final double y;

    public Point(final double x, final double y) {
        this.x = x;
        this.y = y;
    }

    public double getX() { return x; }
    public double getY() { return y; }
    public double getRadius() { return Math.sqrt(x * x + y * y); }
    public double getAngle() { return Math.atan(y / x); }

    public Point rotate90() {
        return new Point(y * -1, x);
    }
}
