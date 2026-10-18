public class DiscountCalculator {

    public static double applyDiscount(double price, double discountRate) {
        double discount = price * discountRate;
        return price - discount;
    }

    public static void printReceipt(String item, double price, double finalPrice) {
        System.out.println("Item: " + item);
        System.out.println("Original Price: $" + price);
        System.out.println("Final Price: $" + finalPrice);
    }

    public static void main(String[] args) {

        String itemName = "Headphones";
        double price = 80.00;
        double discountRate = 0.25;

        double finalPrice = applyDiscount(price, discountRate);

        printReceipt(itemName, price, finalPrice);
    }
}