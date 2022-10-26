import java.awt.Color;
import java.awt.Point;
import java.lang.Math;

public class Circle implements Shape {
    private double radius;
    private Point center;
    private Color color;

    public Circle (double rad, Point cen, Color color) {
        this.radius = rad;
        this.center = cen;
        this.color = color;
    }

    public Color getColor() { return color; }

    public void setColor(Color color) { this.color = color; }

    public double getRadius() { return radius; }

    public void setRadius(double rad) { this.radius = rad; }

    public Point getCenter() { return center; }

    public double getArea() { return Math.PI * radius * radius; }

    public double getPerimeter() { return 2 * Math.PI * radius; }

    public void translate(Point point) {
        center.x += point.x;
        center.y += point.y;
    }
}
