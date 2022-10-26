package part1;

public class Rectangle {
    private final Point topLeft;
    private final Point bottomRight;

    public Rectangle(final Point topLeft, final Point bottomRight) {
        this.topLeft = topLeft;
        this.bottomRight = bottomRight;
    }

    public Point getTopLeft() { return topLeft; }
    public Point getBottomRight() { return bottomRight; }
}
