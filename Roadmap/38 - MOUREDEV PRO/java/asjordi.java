import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import com.fasterxml.jackson.databind.MappingIterator;
import com.fasterxml.jackson.databind.SequenceWriter;
import com.fasterxml.jackson.dataformat.csv.CsvMapper;
import com.fasterxml.jackson.dataformat.csv.CsvSchema;
import net.datafaker.Faker;

import java.io.File;
import java.io.IOException;
import java.security.SecureRandom;
import java.util.*;

public class Main {

    private static File csvFile = new File("persons.csv");

    public static void main(String[] args) {
//        createCsvFile();
        Random r = new SecureRandom();
        var persons = readCsvFile();
        var uniquePersons = new ArrayList<>(persons.stream().distinct().filter(p -> p.status().equals("active")).toList());
        Collections.shuffle(uniquePersons);

        var winnerSubscription = uniquePersons.get(r.nextInt(uniquePersons.size()));
        var winnerDiscount = uniquePersons.get(r.nextInt(uniquePersons.size()));
        var winnerBook = uniquePersons.get(r.nextInt(uniquePersons.size()));

        System.out.println("Winner subscription: " + winnerSubscription.id + " " + winnerSubscription.email());
        System.out.println("Winner discount: " + winnerDiscount.id + " " + winnerDiscount.email());
        System.out.println("Winner book: " + winnerBook.id + " " + winnerBook.email());

    }

    @JsonPropertyOrder({"id", "email", "status"})
    record Person(int id, String email, String status) {
        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof Person person)) return false;
            return id == person.id && Objects.equals(email, person.email) && Objects.equals(status, person.status);
        }

        @Override
        public int hashCode() {
            return Objects.hash(id, email, status);
        }
    }

    public static List<Person> readCsvFile() {
        CsvMapper mapper = new CsvMapper();
        CsvSchema schema = CsvSchema.emptySchema().withHeader();

        try (MappingIterator<Person> iterator = mapper
                .readerFor(Person.class)
                .with(schema)
                .readValues(csvFile)) {

            return iterator.readAll();
        }
        catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static void createCsvFile() {
        List<Person> persons = generatePersons();

        CsvMapper mapper = new CsvMapper();
        CsvSchema schema = mapper
                .schemaFor(Person.class)
                .withHeader();

        try {
            mapper.writer(schema).writeValue(csvFile, persons);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static List<Person> generatePersons() {
        List<Person> list = new LinkedList<>();
        Faker f = new Faker();

        for (int i = 1; i <= 1000; i++) {
            list.add(new Person(i, f.internet().emailAddress(), f.options().option("active", "inactive")));
        }

        return list;
    }

}
