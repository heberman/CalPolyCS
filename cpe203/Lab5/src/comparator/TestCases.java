//Authors: Henry B, Bharath S

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;

import java.util.Comparator;
import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

import org.junit.Test;
import org.junit.Before;

public class TestCases
{
   private static final Song[] songs = new Song[] {
         new Song("Decemberists", "The Mariner's Revenge Song", 2005),
         new Song("Rogue Wave", "Love's Lost Guarantee", 2005),
         new Song("Avett Brothers", "Talk on Indolence", 2006),
         new Song("Gerry Rafferty", "Baker Street", 1998),
         new Song("City and Colour", "Sleeping Sickness", 2007),
         new Song("Foo Fighters", "Baker Street", 1997),
         new Song("Queen", "Bohemian Rhapsody", 1975),
         new Song("Gerry Rafferty", "Baker Street", 1978)
      };

   @Test
   public void testArtistComparator()
   {
      ArtistComparator ac = new ArtistComparator();
      assertTrue(ac.compare(songs[0], songs[1]) < 0);
      assertTrue(ac.compare(songs[1], songs[0]) > 0);
      assertTrue(ac.compare(songs[1], songs[2]) > 0);
   }

   @Test
   public void testLambdaTitleComparator()
   {
      Comparator<Song> comp = (s1, s2) -> s1.getTitle().compareTo(s2.getTitle());
      assertTrue(comp.compare(songs[0], songs[1]) > 0);
      assertTrue(comp.compare(songs[1], songs[2]) < 0);
   }

   @Test
   public void testYearExtractorComparator()
   {
      Comparator<Song> comp = Comparator.comparing(Song::getYear,
              Comparator.reverseOrder());
      assertTrue(comp.compare(songs[1], songs[2]) > 0);
      assertTrue(comp.compare(songs[0], songs[1]) == 0);

   }

   @Test
   public void testComposedComparator()
   {
      Comparator<Song> c1_year = Comparator.comparing(Song::getYear,
              Comparator.reverseOrder());
      ArtistComparator c2_artist = new ArtistComparator();
      Comparator<Song> c3_title = Comparator.comparing(Song::getTitle);
      ComposedComparator cc1 = new ComposedComparator(c1_year, c2_artist);
      ComposedComparator cc2 = new ComposedComparator(c3_title, c2_artist);
      assertTrue(cc1.compare(songs[0], songs[1]) < 0);
      assertTrue(cc2.compare(songs[3], songs[5]) > 0);
   }

   @Test
   public void testThenComparing()
   {
      Comparator<Song> c_title = Comparator.comparing(Song::getTitle);
      Comparator<Song> c_artist = Comparator.comparing(Song::getArtist);
      Comparator<Song> c1 = c_title.thenComparing(c_artist);
      assertTrue(c1.compare(songs[3], songs[5]) > 0);
   }

   @Test
   public void runSort()
   {
      List<Song> songList = new ArrayList<>(Arrays.asList(songs));
      List<Song> expectedList = Arrays.asList(
         new Song("Avett Brothers", "Talk on Indolence", 2006),
         new Song("City and Colour", "Sleeping Sickness", 2007),
         new Song("Decemberists", "The Mariner's Revenge Song", 2005),
         new Song("Foo Fighters", "Baker Street", 1997),
         new Song("Gerry Rafferty", "Baker Street", 1998),
         new Song("Gerry Rafferty", "Baker Street", 1978),
         new Song("Queen", "Bohemian Rhapsody", 1975),
         new Song("Rogue Wave", "Love's Lost Guarantee", 2005)
         );
      ArtistComparator ac = new ArtistComparator();
      songList.sort(ac);

      assertEquals(songList, expectedList);
   }
}
