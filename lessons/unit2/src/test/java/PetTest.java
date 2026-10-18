import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class PetTest {

    @Test
    public void testFeedOnce() {

        Pet p = new Pet("Buddy");

        p.feed();

        assertEquals(3, p.getHungerLevel());
    }

    @Test
    public void testFeedMultipleTimes() {

        Pet p = new Pet("Luna");

        p.feed();
        p.feed();

        assertEquals(1, p.getHungerLevel());
    }

    @Test
    public void testName() {

        Pet p = new Pet("Max");

        assertEquals("Max", p.getName());
    }
}