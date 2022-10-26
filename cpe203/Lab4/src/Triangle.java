import java.awt.Color;
import java.awt.Point;

public class Triangle implements Shape {
    private Point vertexA;
    private Point vertexB;
    private Point vertexC;
    private Color color;

    public Triangle(Point a, Point b, Point c, Color color) {
        this.vertexA = a;
        this.vertexB = b;
        this.vertexC = c;
        this.color = color;
    }

    public Point getVertexA() { return vertexA; }
    public Point getVertexB() { return vertexB; }
    public Point getVertexC() { return vertexC; }
    public Color getColor() { return color; }
    public void setColor(Color color) { this.color = color; }

    public double getArea() {
        return Math.abs(0.5 * (vertexA.x*(vertexB.y- vertexC.y) +
                vertexB.x*(vertexC.y - vertexA.y) +
                vertexC.x*(vertexA.y - vertexB.y)));
    }

    public double getPerimeter() {
        double sideA = Math.sqrt(Math.pow(Math.abs(vertexB.x - vertexA.x), 2) +
                Math.pow(Math.abs(vertexB.y - vertexA.y), 2));
        double sideB = Math.sqrt(Math.pow(Math.abs(vertexC.x - vertexB.x), 2) +
                Math.pow(Math.abs(vertexC.y - vertexB.y), 2));
        double sideC = Math.sqrt(Math.pow(Math.abs(vertexA.x - vertexC.x), 2) +
                Math.pow(Math.abs(vertexA.y - vertexC.y), 2));
        return sideA + sideB + sideC;
    }

    public void translate(Point point) {
        vertexA.x += point.x;
        vertexA.y += point.y;
        vertexB.x += point.x;
        vertexB.y += point.y;
        vertexC.x += point.x;
        vertexC.y += point.y;
    }
}
