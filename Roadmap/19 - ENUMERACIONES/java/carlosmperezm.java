public class chartypes {

  public static void main(String[] args) {
    exercise(1);
    extra();

  }

  private static void exercise(int dayNumber) {
    enum Day {
      MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY;
    }
    System.out.println(Day.values()[dayNumber - 1]);
  }

  enum OrderStatus {
    PENDING, SENT, DELIVERED, CANCELLED;
  }

  public static class Order {
    OrderStatus status = OrderStatus.PENDING;

    public void sendOrder() {
      if (status == OrderStatus.PENDING)
        status = OrderStatus.SENT;
      else
        System.out.println("The order can't be sent");
    }

    public void deliverOrder() {
      if (status == OrderStatus.SENT)
        status = OrderStatus.DELIVERED;
      else
        System.out.println("The order can't be delivered");
    }

    public void cancelOrder() {
      status = OrderStatus.CANCELLED;
    }

    public void ShowStatus(OrderStatus status) {
      switch (status) {
        case PENDING:
          System.out.println("The order is pending");
          break;
        case SENT:
          System.out.println("The order is sent");
          break;
        case DELIVERED:
          System.out.println("The order is delivered");
          break;
        case CANCELLED:
          System.out.println("The order is cancelled");
          break;
      }

    }

  }

  private static void extra() {
    Order order1 = new Order();
    order1.ShowStatus(order1.status);
    order1.sendOrder();
    order1.ShowStatus(order1.status);
    order1.deliverOrder();
    order1.ShowStatus(order1.status);
    order1.cancelOrder();
    order1.ShowStatus(order1.status);
    System.out.println("__________________________");
    System.out.println("Order 2");

    Order order2 = new Order();
    order2.ShowStatus(order2.status);
    // order2.sendOrder();
    order2.ShowStatus(order2.status);
    order2.deliverOrder();
    order2.ShowStatus(order2.status);
    order2.cancelOrder();
    order2.ShowStatus(order2.status);

  }

}
