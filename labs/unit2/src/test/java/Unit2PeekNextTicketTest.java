import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

public class Unit2PeekNextTicketTest {

    @Test
    @DisplayName("peekNextTicket on empty queue returns message and does not modify state")
    public void testPeekEmptyQueue() {
        Unit2Project app = new Unit2Project();

        String result = app.peekNextTicket();

        assertEquals("No tickets available.",
                result,
                "Should return message when queue is empty.");

        assertEquals(0,
                app.getPendingTicketCount(),
                "Queue should remain empty.");
    }

    @Test
    @DisplayName("peekNextTicket returns correct ticket and does not modify state when queue has one element")
    public void testPeekSingleTicket() {
        Unit2Project app = new Unit2Project();

        app.addTicket("Reset password");

        String result = app.peekNextTicket();

        assertEquals("Reset password",
                result,
                "Peek should return the only ticket in the queue.");

        assertEquals(1,
                app.getPendingTicketCount(),
                "Queue size should remain 1 after peek.");
    }

    @Test
    @DisplayName("peekNextTicket returns the first ticket and does not remove tickets when queue has multiple elements")
    public void testPeekMultipleTickets() {
        // Create a new ticket management system.
        Unit2Project app = new Unit2Project();

        // Add three tickets to the queue in FIFO order.
        app.addTicket("Reset password");
        app.addTicket("Install printer");
        app.addTicket("Update software");

        // Peek at the next ticket without removing it.
        String result = app.peekNextTicket();

        // Verify that the first ticket added is returned.
        assertEquals("Reset password",
                result,
                "Peek should return the first ticket in the queue.");

        // Verify that peeking does not remove any tickets.
        assertEquals(3,
                app.getPendingTicketCount(),
                "Queue size should remain 3 after peek.");
    }
}
