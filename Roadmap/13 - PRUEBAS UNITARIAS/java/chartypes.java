import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class chartypes {

    public static void main(String[] args) {
        Tests.addSumCorrectly();
    }

    // Exercise
    public static int add(int x, int y) {
        return x + y;
    }
}

class Tests {
    @Test
    static void addSumCorrectly() {
        assertEquals(4, chartypes.add(2, 2));
        assertEquals(5, chartypes.add(3, 2));
        assertEquals(0, chartypes.add(0, 0));
        assertEquals(100, chartypes.add(99, 1));
        assertEquals(1, chartypes.add(0, 1));
    }
}