package part2;

import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.util.ArrayList;
import java.util.function.Predicate;
import java.util.stream.Collectors;
import java.util.Arrays;
import java.util.List;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;
import org.junit.Test;
import part1.Util;

public class PartTwoTestCases
{
   public static final double DELTA = 0.00001;

   @Test
   public void testCircleImplSpecifics()
      throws NoSuchMethodException
   {
      final List<String> expectedMethodNames = Arrays.asList(
         "getCenter", "getRadius", "perimeter");

      final List<Class> expectedMethodReturns = Arrays.asList(
         Point.class, double.class, double.class);

      final List<Class[]> expectedMethodParameters = Arrays.asList(
         new Class[0], new Class[0], new Class[0]);

      verifyImplSpecifics(Circle.class, expectedMethodNames,
         expectedMethodReturns, expectedMethodParameters);
   }

   @Test
   public void testRectangleImplSpecifics()
      throws NoSuchMethodException
   {
      final List<String> expectedMethodNames = Arrays.asList(
         "getTopLeft", "getBottomRight", "perimeter");

      final List<Class> expectedMethodReturns = Arrays.asList(
         Point.class, Point.class, double.class);

      final List<Class[]> expectedMethodParameters = Arrays.asList(
         new Class[0], new Class[0], new Class[0]);

      verifyImplSpecifics(Rectangle.class, expectedMethodNames,
         expectedMethodReturns, expectedMethodParameters);
   }

   @Test
   public void testPolygonImplSpecifics()
      throws NoSuchMethodException
   {
      final List<String> expectedMethodNames = Arrays.asList(
         "getPoints", "perimeter");

      final List<Class> expectedMethodReturns = Arrays.asList(
         List.class, double.class);

      final List<Class[]> expectedMethodParameters = Arrays.asList(
         new Class[0], new Class[0]);

      verifyImplSpecifics(Polygon.class, expectedMethodNames,
         expectedMethodReturns, expectedMethodParameters);
   }

    @Test
    public void testPerimeterC1() {
       Circle c = new Circle(new Point(1.0, 1.0), 1.0);
       assertEquals(6.28319, c.perimeter(), DELTA);
    }

    @Test
    public void testPerimeterC2() {
        Circle c = new Circle(new Point(1.0, 1.0), 2.0);
        assertEquals(12.56637, c.perimeter(), DELTA);
    }

    @Test
    public void testPerimeterR1() {
       Rectangle r = new Rectangle(new Point(1.0, 1.0), new Point(3.0, 2.0));
       assertEquals(6.0, r.perimeter(), DELTA);
    }

    @Test
    public void testPerimeterR2() {
       Rectangle r = new Rectangle(new Point(3.0, 2.0), new Point(1.0, 1.0));
       assertEquals(6.0, r.perimeter(), DELTA);
   }

    @Test
    public void testPerimeterP1() {
        List<Point> input =
                new ArrayList<Point>(Arrays.asList(new Point(0.0,0.0), new Point(2.0,0.0), new Point(0.0,2.0)));
        assertEquals(6.82843, new Polygon(input).perimeter(), DELTA);
    }

    @Test
    public void testPerimeterP2() {
        List<Point> input =
                new ArrayList<Point>(Arrays.asList(new Point(0.0,0.0), new Point(0.0,2.0), new Point(4.0,5.0), new Point(4.0,3.0), new Point(8.0,0.0)));
        assertEquals(22.0, new Polygon(input).perimeter(), DELTA);
    }

    @Test
    public void testBigger() {
        Circle c = new Circle(new Point(1.0,1.0), 2.0);
        Rectangle r = new Rectangle(new Point(-1.0, 2.0), new Point(1.0, -1.6));
        List<Point> points = new ArrayList<>();
        points.add(new Point(0.0,0.0));
        points.add(new Point(3.0,1.0));
        points.add(new Point(1.0,4.0));
        points.add(new Point(-1.0,4.0));
        Polygon p = new Polygon(points);
        assertEquals(12.89093, Bigger.whichIsBigger(c, r, p), DELTA);
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
