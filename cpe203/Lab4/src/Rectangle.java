import java.awt.Color;
import java.awt.Point;


public class Rectangle implements Shape{
    private double width;
    private double height;
    private Point topLeft;
    private Color color;

    public Rectangle(double w, double h, Point tl, Color c) {
        this.width = w;
        this.height = h;
        this.topLeft = tl;
        this.color = c;
    }

    public double getWidth() { return width; }
    public void setWidth(double width) { this.width = width; }
    public double getHeight() { return height; }
    public void setHeight(double height) { this.height = height; }
    public Point getTopLeft() { return topLeft; }
    public Color getColor() { return color; }
    public void setColor(Color color) { this.color = color; }
    public double getArea() { return width * height; }
    public double getPerimeter() { return 2 * (width + height); }
    public void translate(Point point) {
        topLeft.x += point.x;
        topLeft.y += point.y;;
    }
}
