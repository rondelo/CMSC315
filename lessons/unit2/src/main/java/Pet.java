public class Pet {

    private String name;
    private int hungerLevel;

    public Pet(String name) {
        this.name = name;
        this.hungerLevel = 5; // default value
    }

    public void feed() {
        hungerLevel -= 2;
        if (hungerLevel < 0) {
            hungerLevel = 0;
        }
    }

    public int getHungerLevel() {
        return hungerLevel;
    }

    public String getName() {
        return name;
    }

    public static void main(String[] args) {

        Pet myPet = new Pet("Buddy");

        System.out.println("Pet name: " + myPet.getName());
        System.out.println("Initial hunger level: " + myPet.getHungerLevel());

        myPet.feed();

        System.out.println("After feeding:");
        System.out.println("Hunger level: " + myPet.getHungerLevel());
    }
}