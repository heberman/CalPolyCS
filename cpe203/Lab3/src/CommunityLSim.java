import java.util.*;

public final class CommunityLSim {

  ArrayList<Player> players; 
  int numPeeps;
  Random random = new Random();

  //you will need to add more instance variables

  public CommunityLSim( int numP) {
	  	numPeeps = numP;
		//create the players
  		players = new ArrayList<Player>();

		//generate a community of 30
		for (int i = 0; i < numPeeps; i++) {
			if (i < numPeeps/2.0)
				players.add(new Player(PlayerKind.POORLY_PAID, (float)(99+Math.random()))); 
			else
				players.add(new Player(PlayerKind.WELL_PAID, (float)(100.1+Math.random()))); 
		}
	
	}

	public int getSize() {
		return numPeeps;
	}

	public Player getPlayer(int i) {
		return players.get(i);
	}

	public void addPocketChange() {
  		for (Player player : players) {
			if (player.getKind() == PlayerKind.WELL_PAID) {
				player.addMoney(.1f);
			} else {
				player.addMoney(.03f);
			}
  		}
	}

	public ArrayList<Integer> reDoWhoPlays(int range) {
		ArrayList<Integer> players = new ArrayList<>();
		for (int i=0; i<range*0.3; i++) {
			int randNum = randomUniqIndx(0, range/2);
			while (players.contains(randNum)) {
				randNum = randomUniqIndx(0, range/2);
			}
			players.add(randNum);
		}
		for (int i=0; i<range*0.2; i++) {
			int randNum = randomUniqIndx(range/2, range);
			while (players.contains(randNum)) {
				randNum = randomUniqIndx(range/2, range);
			}
			players.add(randNum);
		}
		return players;
	}

	/* generate some random indices for who might play the lottery 
		in a given range of indices */ 
 	private int randomUniqIndx(int startRange, int endRange) {
 		return random.ints(startRange,endRange).findFirst().getAsInt();
	}
    
	public void simulateYears(int numYears) {
  		/*now simulate lottery play for some years */
  		for (int year=0; year < numYears; year++) {
			Game game = new Game();
			ArrayList<Integer> newPlayersIndeces = reDoWhoPlays(numPeeps);
			ArrayList<Player> newPlayers = new ArrayList<>();
			for (int playerIndex : newPlayersIndeces) {
				newPlayers.add(players.get(playerIndex));
			}
			for (Player player : newPlayers) {
				float result = game.getResult(player.getLottoNums());
				player.addMoney(result);
				if (result == -1) {
					int randNum = random.ints(0, 10).findFirst().getAsInt();
					int randPlayer = random.ints(0, numPeeps/2).findFirst().getAsInt();
					if (randNum < 3) {
						players.get(randPlayer).addMoney(1);

					} else {
						players.get(randPlayer + numPeeps/2).addMoney(1);
					}
				}
			}
			addPocketChange();
    		// add code so that each member of the community who plays, plays 
			//right now just everyone updates their list of funds each year
			for (Player p : players) {
				p.updateMoneyEachYear();
			}
			float largest = 0f;
			float smallest = 1000f;
			for (Player p : players) {
				if (p.getMoney() > largest) {
					largest = p.getMoney();
				} else if (p.getMoney() < smallest) {
					smallest = p.getMoney();
				}
			}
			System.out.println("After year " + year + ":");
			System.out.println("The person with the most money has: " + largest);
			System.out.println("The person with the least money has: " + smallest);
    	} //years
  }	

}
