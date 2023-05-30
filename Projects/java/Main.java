
import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Archive> archive = new ArrayList<>();

        while (true) {
            System.out.println("Identifier?: (empty will stop)");
            String ID = scanner.nextLine();
            if (ID.isEmpty()) {
                break;
            }

            System.out.println("Name? (empty will stop");
            String name = scanner.nextLine();
            if (name.isEmpty()) {
                break;
            } Archive item = new Archive(ID, name);

            if(archive.contains(item)) {
                continue;
            }

            if (!(archive.contains(item))) {
                archive.add(item);
            }
        }

        System.out.println("==Items==");
        for(Archive i : archive) {
            System.out.println(i);
        }
    }
}
