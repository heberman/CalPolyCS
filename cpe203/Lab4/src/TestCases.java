import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.util.ArrayList;
import java.util.stream.Collectors;
import java.util.Arrays;
import java.util.List;
import java.util.LinkedList;

import java.awt.Color;
import java.awt.Point;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;
import org.junit.Test;

public class TestCases
{
   public static final double DELTA = 0.00001;

   /* some sample tests but you must write more! see lab write up */

   @Test
   public void testCircleGetArea()
   {
      Circle c = new Circle(5.678, new Point(2, 3), Color.BLACK);

      assertEquals(101.2839543, c.getArea(), DELTA);
   }

   @Test
   public void testCircleGetPerimeter()
   {
      Circle c = new Circle(5.678, new Point(2, 3), Color.BLACK);

      assertEquals(35.6759261, c.getPerimeter(), DELTA);
   }

   @Test
   public void testCircleGetRadius()
   {
      Circle c = new Circle(5.678, new Point(2, 3), Color.BLACK);

      assertEquals(5.678, c.getRadius(), DELTA);
   }

   @Test
   public void testCircleSetRadius()
   {
      Circle c = new Circle(5.678, new Point(2, 3), Color.BLACK);
      c.setRadius(2.0);
      assertEquals(2.0, c.getRadius(), DELTA);
   }

   @Test
   public void testCircleGetCenter()
   {
      Circle c = new Circle(5.678, new Point(2, 3), Color.BLACK);
      assertEquals(new Point(2,3), c.getCenter());
   }

   @Test
   public void testRectangleGetWidth()
   {
      Rectangle r = new Rectangle(3.0, 4.0, new Point(2, 3), Color.BLACK);

      assertEquals(3.0, r.getWidth(), DELTA);
   }

   @Test
   public void testRectangleGetHeight()
   {
      Rectangle r = new Rectangle(3.0, 4.0, new Point(2, 3), Color.BLACK);

      assertEquals(4.0, r.getHeight(), DELTA);
   }

   @Test
   public void testRectangleGetTopLeft()
   {
      Rectangle r = new Rectangle(3.0, 4.0, new Point(2, 3), Color.BLACK);

      assertEquals(new Point(2,3), r.getTopLeft());
   }

   @Test
   public void testRectangleGetArea()
   {
      Rectangle r = new Rectangle(3.0, 4.0, new Point(2, 3), Color.BLACK);

      assertEquals(12.0, r.getArea(), DELTA);
   }

   @Test
   public void testRectangleGetPerimeter()
   {
      Rectangle r = new Rectangle(3.0, 4.0, new Point(2, 3), Color.BLACK);

      assertEquals(14.0, r.getPerimeter(), DELTA);
   }

   @Test
   public void testTriangleGetA()
   {
      Triangle t1 = new Triangle(new Point(4,1), new Point(2, 3), new Point(0,1), Color.BLACK);

      assertEquals(new Point(4,1), t1.getVertexA());
   }

   @Test
   public void testTriangleGetB()
   {
      Triangle t1 = new Triangle(new Point(4,1), new Point(2, 3), new Point(0,1), Color.BLACK);

      assertEquals(new Point(2,3), t1.getVertexB());
   }

   @Test
   public void testTriangleGetC()
   {
      Triangle t1 = new Triangle(new Point(4,1), new Point(2, 3), new Point(0,1), Color.BLACK);

      assertEquals(new Point(0,1), t1.getVertexC());
   }

   @Test
   public void testTriangleGetArea()
   {
      Triangle t1 = new Triangle(new Point(4,1), new Point(2, 3), new Point(0,1), Color.BLACK);

      assertEquals(4.0, t1.getArea(), DELTA);
   }

   @Test
   public void testTriangleGetPerimeter()
   {
      Triangle t1 = new Triangle(new Point(4,1), new Point(2, 3), new Point(0,1), Color.BLACK);

      assertEquals(9.65685, t1.getPerimeter(), DELTA);
   }

   @Test
   public void testConvexPolygonGetVertex()
   {
      Point[] c1List = {new Point(0,1), new Point(2,3), new Point(4,1)};
      ConvexPolygon c1 = new ConvexPolygon(c1List, Color.BLACK);
      assertEquals(new Point(0,1), c1.getVertex(0));
   }

   @Test
   public void testConvexPolygonGetArea()
   {
      Point[] c1List = {new Point(0,1), new Point(2,3), new Point(4,1)};
      ConvexPolygon c1 = new ConvexPolygon(c1List, Color.BLACK);
      assertEquals(4.0, c1.getArea(), DELTA);
   }

   @Test
   public void testConvexPolygonGetPerimeter()
   {
      Point[] c1List = {new Point(0,1), new Point(2,3), new Point(4,1)};
      ConvexPolygon c1 = new ConvexPolygon(c1List, Color.BLACK);
      assertEquals(9.65685, c1.getPerimeter(), DELTA);
   }

   @Test
   public void testWorkSpaceGet()
   {
      WorkSpace ws = new WorkSpace();

      Rectangle r = new Rectangle(1.234, 5.678, new Point(2, 3), Color.BLACK);

      ws.add(r);
      ws.add(new Circle(5.678, new Point(2, 3), Color.BLACK));
      ws.add(new Triangle(new Point(0,0), new Point(2,-4), new Point(3, 0),
              Color.BLACK));

      assertEquals(r, ws.get(0));
   }

   @Test
   public void testWorkSpaceSize()
   {
      WorkSpace ws = new WorkSpace();

      ws.add(new Rectangle(1.234, 5.678, new Point(2, 3), Color.BLACK));
      ws.add(new Circle(5.678, new Point(2, 3), Color.BLACK));
      ws.add(new Triangle(new Point(0,0), new Point(2,-4), new Point(3, 0),
              Color.BLACK));

      assertEquals(3, ws.size());
   }

   @Test
   public void testWorkSpaceAreaOfAllShapes()
   {
      WorkSpace ws = new WorkSpace();

      ws.add(new Rectangle(1.234, 5.678, new Point(2, 3), Color.BLACK));
      ws.add(new Circle(5.678, new Point(2, 3), Color.BLACK));
      ws.add(new Triangle(new Point(0,0), new Point(2,-4), new Point(3, 0), 
                 Color.BLACK));

      assertEquals(114.2906063, ws.getAreaOfAllShapes(), DELTA);
   }

   @Test
   public void testWorkSpaceGetCircles()
   {
      WorkSpace ws = new WorkSpace();
      List<Circle> expected = new LinkedList<>();

      // Have to make sure the same objects go into the WorkSpace as
      // into the expected List since we haven't overriden equals in Circle.
      Circle c1 = new Circle(5.678, new Point(2, 3), Color.BLACK);
      Circle c2 = new Circle(1.11, new Point(-5, -3), Color.RED);

      ws.add(new Rectangle(1.234, 5.678, new Point(2, 3), Color.BLACK));
      ws.add(c1);
      ws.add(new Triangle(new Point(0,0), new Point(2,-4), new Point(3, 0),
                 Color.BLACK));
      ws.add(c2);

      expected.add(c1);
      expected.add(c2);

      // Doesn't matter if the "type" of lists are different (e.g Linked vs
      // Array).  List equals only looks at the objects in the List.
      assertEquals(expected, ws.getCircles());
   }

   @Test
   public void testWorkSpaceGetRectangles()
   {
      WorkSpace ws = new WorkSpace();
      List<Rectangle> expected = new LinkedList<>();

      // Have to make sure the same objects go into the WorkSpace as
      // into the expected List since we haven't overriden equals in Circle.
      Rectangle r1 = new Rectangle(1.0, 2.0, new Point(2, 3), Color.BLACK);
      Rectangle r2 = new Rectangle(2.0, 3.0, new Point(2, 5), Color.RED);

      ws.add(new Circle(1.234, new Point(2, 3), Color.BLACK));
      ws.add(r1);
      ws.add(new Triangle(new Point(0,0), new Point(2,-4), new Point(3, 0),
              Color.BLACK));
      ws.add(r2);

      expected.add(r1);
      expected.add(r2);

      // Doesn't matter if the "type" of lists are different (e.g Linked vs
      // Array).  List equals only looks at the objects in the List.
      assertEquals(expected, ws.getRectangles());
   }

   @Test
   public void testWorkSpaceGetTriangles()
   {
      WorkSpace ws = new WorkSpace();
      List<Triangle> expected = new LinkedList<>();

      // Have to make sure the same objects go into the WorkSpace as
      // into the expected List since we haven't overriden equals in Circle.
      Triangle t1 = new Triangle(new Point(4,1), new Point(2, 3), new Point(0,1), Color.BLACK);
      Triangle t2 = new Triangle(new Point(4,2), new Point(2, 4), new Point(0,2), Color.RED);

      ws.add(new Circle(1.234, new Point(2, 3), Color.BLACK));
      ws.add(t1);
      ws.add(new Rectangle(2.0, 3.0, new Point(2, 5), Color.RED));
      ws.add(t2);

      expected.add(t1);
      expected.add(t2);

      // Doesn't matter if the "type" of lists are different (e.g Linked vs
      // Array).  List equals only looks at the objects in the List.
      assertEquals(expected, ws.getTriangles());
   }

   @Test
   public void testWorkSpaceGetConvexPolygons()
   {
      WorkSpace ws = new WorkSpace();
      List<ConvexPolygon> expected = new LinkedList<>();

      // Have to make sure the same objects go into the WorkSpace as
      // into the expected List since we haven't overriden equals in Circle.
      Point[] c1List = {new Point(0,1), new Point(2,3), new Point(4,1)};
      ConvexPolygon c1 = new ConvexPolygon(c1List, Color.BLACK);
      Point[] c2List = {new Point(1,1), new Point(3,3), new Point(5,1)};
      ConvexPolygon c2 = new ConvexPolygon(c2List, Color.BLACK);
      ws.add(new Circle(1.234, new Point(2, 3), Color.BLACK));
      ws.add(c1);
      ws.add(new Rectangle(2.0, 3.0, new Point(2, 5), Color.RED));
      ws.add(c2);

      expected.add(c1);
      expected.add(c2);

      // Doesn't matter if the "type" of lists are different (e.g Linked vs
      // Array).  List equals only looks at the objects in the List.
      assertEquals(expected, ws.getConvexPolygons());
   }

   @Test
   public void testWorkSpaceGetShapesByColor()
   {
      WorkSpace ws = new WorkSpace();
      List<Shape> expected = new LinkedList<>();

      // Have to make sure the same objects go into the WorkSpace as
      // into the expected List since we haven't overriden equals in Circle.
      Point[] c1List = {new Point(0,1), new Point(2,3), new Point(4,1)};
      ConvexPolygon c1 = new ConvexPolygon(c1List, Color.RED);
      Point[] c2List = {new Point(1,1), new Point(3,3), new Point(5,1)};
      ConvexPolygon c2 = new ConvexPolygon(c2List, Color.BLACK);
      ws.add(new Circle(1.234, new Point(2, 3), Color.BLACK));
      ws.add(c1);
      Rectangle r1 = new Rectangle(2.0, 3.0, new Point(2, 5), Color.RED);
      ws.add(r1);
      ws.add(c2);

      expected.add(c1);
      expected.add(r1);

      // Doesn't matter if the "type" of lists are different (e.g Linked vs
      // Array).  List equals only looks at the objects in the List.
      assertEquals(expected, ws.getShapesByColor(Color.RED));
   }

   @Test
   public void testWorkSpaceGetAreaOfAllShapes()
   {
      WorkSpace ws = new WorkSpace();
      ws.add(new Circle(2.0, new Point(0,0), Color.CYAN));
      ws.add(new Rectangle(2.0, 1.0, new Point(0,0), Color.CYAN));
      ws.add(new Rectangle(1.5, 2.5, new Point(0,0), Color.CYAN));


      // Doesn't matter if the "type" of lists are different (e.g Linked vs
      // Array).  List equals only looks at the objects in the List.
      assertEquals(18.31637, ws.getAreaOfAllShapes(), DELTA);
   }

   @Test
   public void testWorkSpaceGetPerimeterOfAllShapes()
   {
      WorkSpace ws = new WorkSpace();
      ws.add(new Circle(2.0, new Point(0,0), Color.CYAN));
      ws.add(new Rectangle(2.0, 1.0, new Point(0,0), Color.CYAN));
      ws.add(new Rectangle(1.5, 2.5, new Point(0,0), Color.CYAN));


      // Doesn't matter if the "type" of lists are different (e.g Linked vs
      // Array).  List equals only looks at the objects in the List.
      assertEquals(26.56637, ws.getPerimeterOfAllShapes(), DELTA);
   }

   /* HINT - comment out implementation tests for the classes that you have not 
    * yet implemented */
   @Test
   public void testCircleImplSpecifics()
      throws NoSuchMethodException
   {
      final List<String> expectedMethodNames = Arrays.asList(
         "getColor", "setColor", "getArea", "getPerimeter", "translate",
         "getRadius", "setRadius", "getCenter");

      final List<Class> expectedMethodReturns = Arrays.asList(
         Color.class, void.class, double.class, double.class, void.class,
         double.class, void.class, Point.class);

      final List<Class[]> expectedMethodParameters = Arrays.asList(
         new Class[0], new Class[] {Color.class}, new Class[0], new Class[0], new Class[] {Point.class},
         new Class[0], new Class[] {double.class}, new Class[0]);

      verifyImplSpecifics(Circle.class, expectedMethodNames,
         expectedMethodReturns, expectedMethodParameters);
   }

   @Test
   public void testRectangleImplSpecifics()
      throws NoSuchMethodException
   {
      final List<String> expectedMethodNames = Arrays.asList(
         "getColor", "setColor", "getArea", "getPerimeter", "translate",
         "getWidth", "setWidth", "getHeight", "setHeight", "getTopLeft");

      final List<Class> expectedMethodReturns = Arrays.asList(
         Color.class, void.class, double.class, double.class, void.class,
         double.class, void.class, double.class, void.class, Point.class);

      final List<Class[]> expectedMethodParameters = Arrays.asList(
         new Class[0], new Class[] {Color.class}, new Class[0], new Class[0], new Class[] {Point.class},
         new Class[0], new Class[] {double.class}, new Class[0], new Class[] {double.class}, new Class[0]);

      verifyImplSpecifics(Rectangle.class, expectedMethodNames,
         expectedMethodReturns, expectedMethodParameters);
   }

   @Test
   public void testTriangleImplSpecifics()
      throws NoSuchMethodException
   {
      final List<String> expectedMethodNames = Arrays.asList(
         "getColor", "setColor", "getArea", "getPerimeter", "translate",
         "getVertexA", "getVertexB", "getVertexC");

      final List<Class> expectedMethodReturns = Arrays.asList(
         Color.class, void.class, double.class, double.class, void.class,
         Point.class, Point.class, Point.class);

      final List<Class[]> expectedMethodParameters = Arrays.asList(
         new Class[0], new Class[] {Color.class}, new Class[0], new Class[0], new Class[] {Point.class},
         new Class[0], new Class[0], new Class[0]);

      verifyImplSpecifics(Triangle.class, expectedMethodNames,
         expectedMethodReturns, expectedMethodParameters);
   }

   @Test
   public void testConvexPolygonImplSpecifics()
      throws NoSuchMethodException
   {
      final List<String> expectedMethodNames = Arrays.asList(
         "getColor", "setColor", "getArea", "getPerimeter", "translate",
         "getVertex");

      final List<Class> expectedMethodReturns = Arrays.asList(
         Color.class, void.class, double.class, double.class, void.class,
         Point.class);

      final List<Class[]> expectedMethodParameters = Arrays.asList(
         new Class[0], new Class[] {Color.class}, new Class[0], new Class[0], new Class[] {Point.class},
         new Class[] {int.class});

      verifyImplSpecifics(ConvexPolygon.class, expectedMethodNames,
         expectedMethodReturns, expectedMethodParameters);
   }

   private static void verifyImplSpecifics(
      final Class<?> clazz,
      final List<String> expectedMethodNames,
      final List<Class> expectedMethodReturns,
      final List<Class[]> expectedMethodParameters)
      throws NoSuchMethodException
   {
      assertEquals("Unexpected number of public fields",
         0, clazz.getFields().length);

      final List<Method> publicMethods = Arrays.stream(
         clazz.getDeclaredMethods())
            .filter(m -> Modifier.isPublic(m.getModifiers()))
            .collect(Collectors.toList());

      assertEquals("Unexpected number of public methods",
         expectedMethodNames.size(), publicMethods.size());

      assertTrue("Invalid test configuration",
         expectedMethodNames.size() == expectedMethodReturns.size());
      assertTrue("Invalid test configuration",
         expectedMethodNames.size() == expectedMethodParameters.size());

      for (int i = 0; i < expectedMethodNames.size(); i++)
      {
         Method method = clazz.getDeclaredMethod(expectedMethodNames.get(i),
            expectedMethodParameters.get(i));
         assertEquals(expectedMethodReturns.get(i), method.getReturnType());
      }
   }
}
