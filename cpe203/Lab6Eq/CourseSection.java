import java.time.LocalTime;
import java.util.Objects;

class CourseSection
{
   private final String prefix;
   private final String number;
   private final int enrollment;
   private final LocalTime startTime;
   private final LocalTime endTime;

   public CourseSection(final String prefix, final String number,
      final int enrollment, final LocalTime startTime, final LocalTime endTime)
   {
      this.prefix = prefix;
      this.number = number;
      this.enrollment = enrollment;
      this.startTime = startTime;
      this.endTime = endTime;
   }

   // additional likely methods not defined since they are not needed for testing
   public boolean equals(Object o) {
      if (this == o) {
         return true;
      }
      if (o == null) {
         return false;
      }
      if (getClass() != o.getClass()) {
         return false;
      }
      CourseSection s = (CourseSection) o;
      return Objects.equals(prefix, s.prefix) && Objects.equals(number, s.number) &&
              Objects.equals(enrollment, s.enrollment) && Objects.equals(startTime, s.startTime)
              && Objects.equals(endTime, s.endTime);
   }

   public int hashCode() {
      int prime = 17;
      int result = 1;
      result = prime * result + ((prefix == null) ? 0 : prefix.hashCode());
      result = prime * result + ((number == null) ? 0 : number.hashCode());
      result = prime * result + enrollment;
      return result;
   }
}
