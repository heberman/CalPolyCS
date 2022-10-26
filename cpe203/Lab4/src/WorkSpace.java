import java.awt.*;
import java.util.ArrayList;
import java.util.List;

public class WorkSpace {
    private List<Shape> shapes;

    public WorkSpace() {
        shapes = new ArrayList<>();
    }
    public void add(Shape shape) {
        shapes.add(shape);
    }

    public Shape get(int index) {
        return shapes.get(index);
    }

    public int size() {
        return shapes.size();
    }

    public List<Circle> getCircles() {
        List<Circle> circles = new ArrayList<>();
        for (Shape shape : shapes) {
            if (shape instanceof Circle) {
                circles.add((Circle)shape);
            }
        }
        return circles;
    }

    public List<Rectangle> getRectangles() {
        List<Rectangle> rectangles = new ArrayList<>();
        for (Shape shape : shapes) {
            if (shape instanceof Rectangle) {
                rectangles.add((Rectangle) shape);
            }
        }
        return rectangles;
    }

    public List<Triangle> getTriangles() {
        List<Triangle> triangles = new ArrayList<>();
        for (Shape shape : shapes) {
            if (shape instanceof Triangle) {
                triangles.add((Triangle)shape);
            }
        }
        return triangles;
    }

    public List<ConvexPolygon> getConvexPolygons() {
        List<ConvexPolygon> convexPolygons = new ArrayList<>();
        for (Shape shape : shapes) {
            if (shape instanceof ConvexPolygon) {
                convexPolygons.add((ConvexPolygon) shape);
            }
        }
        return convexPolygons;
    }

    public List<Shape> getShapesByColor(Color color) {
        List<Shape> colorShapes = new ArrayList<>();
        for (Shape shape : shapes) {
            if (shape.getColor() == color) {
                colorShapes.add(shape);
            }
        }
        return colorShapes;
    }

    public double getAreaOfAllShapes() {
        double sum = 0;
        for (Shape shape : shapes) {
            sum += shape.getArea();
        }
        return sum;
    }

    public double getPerimeterOfAllShapes() {
        double sum = 0;
        for (Shape shape : shapes) {
            sum += shape.getPerimeter();
        }
        return sum;
    }
}
