package part1;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        List<Point> points = new ArrayList<>();
        try {
            File file = new File(args[0]);
            Scanner reader = new Scanner(file);
            while (reader.hasNextLine()) {
                String data = reader.nextLine();
                String[] strings = data.split(", ");
                double[] numbers = new double[strings.length];
                for(int i = 0;i < strings.length;i++)
                    numbers[i] = Double.parseDouble(strings[i]);
                points.add(new Point(numbers[0], numbers[1], numbers[2]));

            }
            reader.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found.");
            e.printStackTrace();
        }
        try {
            File file = new File("drawMe.txt");
            FileWriter fileWriter = new FileWriter(file);
            for (Point p : points) {
                fileWriter.write(p.toString() + "\n");
            }
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}
