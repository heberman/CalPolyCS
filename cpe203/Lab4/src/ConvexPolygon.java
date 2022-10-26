import java.awt.*;

public class ConvexPolygon implements Shape {
    private Point[] points;
    private Color color;

    public ConvexPolygon(Point[] points, Color color) {
        this.points = points;
        this.color = color;
    }

    public Color getColor() { return color; }
    public void setColor(Color color) { this.color = color; }
    public double getArea() {
        double sum = 0;
        for (int i =0; i<points.length; i++) {
            if (i != points.length - 1)
                sum += points[i].x * points[i+1].y - points[i].y * points[i+1].x;
            else
                sum += points[i].x * points[0].y - points[i].y * points[0].x;
        }
        return Math.abs(sum/2);
    }
    public double getPerimeter() {
        double sum = 0;
        for (int i =0; i<points.length; i++) {
            if (i != points.length - 1)
                sum += Math.sqrt(Math.pow(Math.abs(points[i+1].x - points[i].x), 2) +
                        Math.pow(Math.abs(points[i+1].y - points[i].y), 2));
            else
                sum += Math.sqrt(Math.pow(Math.abs(points[0].x - points[i].x), 2) +
                        Math.pow(Math.abs(points[0].y - points[i].y), 2));
        }
        return sum;
    }
    public void translate(Point point) {
        for (Point vertex : points) {
            vertex.x += point.x;
            vertex.y += point.y;
        }
    }
    public Point getVertex(int index) {
        return points[index];
    }

}
