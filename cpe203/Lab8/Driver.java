import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Driver {
    private static List<Point> readFile(String filename) {
        List<Point> points = new ArrayList<>();
        try {
            File file = new File(filename);
            Scanner reader = new Scanner(file);
            while (reader.hasNextLine()) {
                String data = reader.nextLine();
                String[] strings = data.split(", ");
                double[] numbers = new double[strings.length];
                for(int i = 0;i < strings.length;i++)
                    numbers[i] = Double.parseDouble(strings[i]);
                points.add(new Point(numbers[0], numbers[1], (int)numbers[2]));

            }
            reader.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found.");
            e.printStackTrace();
        }
        return points;
    }

    private static void writeFile(List<Point> points) {
        try {
            File file = new File("drawMe.txt");
            FileWriter fileWriter = new FileWriter(file);
            for (Point p : points) {
                fileWriter.write(p.toString() + "\n");
            }
            fileWriter.close();
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        //read all points into points list
        List<Point> points = readFile(args[0]);

        //removes all points that have a z > 2
        List<Point> pts1 = points.stream().filter(p -> p.getZ() <= 2).collect(Collectors.toList());
        //scale down all the points by 0.5
        List<Point> pts2 = pts1.stream().map(Point::scale).collect(Collectors.toList());
        //translate all points by {-150, -37}
        List<Point> pts3 = pts2.stream().map(Point::translate).collect(Collectors.toList());

        //write new points onto file
        writeFile(pts3);
    }
}
