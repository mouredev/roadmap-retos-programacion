public class ExampleFechas {
    public static void main(String[] args) {
        LocalDateTime actual = LocalDateTime.now();
        LocalDateTime birthDate = LocalDateTime.of(1992, 07, 13, 01, 52, 35);
        Period period = Period.between(birthDate.toLocalDate(), actual.toLocalDate());
        System.out.println(period.getYears() + " años");
        System.out.println(period.getMonths() + " meses");
        System.out.println(period.getDays() + " días");

    }

}