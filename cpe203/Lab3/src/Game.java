import java.util.*;

public class Game {
    private int[] winningNums = new int[5];
    private Random random = new Random();

    public Game(){
        winningLotNumber();
    }

    public void winningLotNumber() {
        ArrayList<Integer> nums = new ArrayList<>();
        nums.add(0);
        for (int i=0; i<5; i++) {
            int randNum = 0;
            while (nums.contains(randNum)) {
                randNum = random.ints(1, 42).findFirst().getAsInt();
            }
            winningNums[i] = randNum;
        }
    }

    public int getMatches(int[] aList, int[] bList) {
        int sum = 0;
        for (int x : aList) {
            for (int y : bList) {
                if (x == y) {
                    sum++;
                }
            }
        }
        return sum;
    }

    public float getResult(int[] guesses) {
        int matches = getMatches(winningNums, guesses);
        float winnings = -1;
        if (matches == 2) {
            winnings = 1;
        } else if (matches == 3) {
            winnings = 10.86f;
        } else if (matches == 4) {
            winnings = 197.53f;
        } else if (matches == 5) {
            winnings = 212534.83f;
        }
        return winnings;
    }
}
