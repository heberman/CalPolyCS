public class Point {
    private double x;
    private double y;
    private int z;

    public Point(final double x, final double y) {
        this.x = x;
        this.y = y;
        this.z = 0;
    }

    public Point(final double x, final double y, final int z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public String toString() {
        return x + ", " + y + ", " + z;
    }

    public double getX() { return x; }
    public double getY() { return y; }
    public int getZ() { return z; }
    public void setX(double x) { this.x = x; }
    public void setY(double y) { this.y = y; }
    public void setZ(int z) { this.z = z; }
    public double getRadius() { return Math.sqrt(x * x + y * y); }
    public double getAngle() { return Math.atan(y / x); }

    public Point scale() { return new Point(x * 0.5, y * 0.5, z); }

    public Point translate() { return new Point(x - 150, y - 37, z); }

    public Point rotate90() {
        return new Point(y * -1, x);
    }
}
