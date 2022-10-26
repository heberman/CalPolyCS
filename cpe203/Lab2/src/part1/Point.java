package part1;
public class Point {
    private final double x;
    private final double y;
    private final double z;

    public Point(final double x, final double y) {
        this.x = x;
        this.y = y;
        this.z = 0;
    }

    public Point(final double x, final double y, final double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public String toString() {
        return x + ", " + y + ", " + z;
    }

    public double getX() { return x; }
    public double getY() { return y; }
    public double getZ() { return z; }
    public double getRadius() { return Math.sqrt(x * x + y * y); }
    public double getAngle() { return Math.atan(y / x); }

    public Point rotate90() {
        return new Point(y * -1, x);
    }
}
