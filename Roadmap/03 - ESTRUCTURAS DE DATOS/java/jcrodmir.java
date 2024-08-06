import java.util.*;

public class EstructuraDatos {


    public static void main(String[] args) {
        /*Array*/
        int[] array= new int[4];
        array[0]=3;
        array[1]=2;
        array[2]=1;
        array[3]=4;
        System.out.println("Array\n");
        for (int i = 0; i <  array.length  ; i++) {
            System.out.println("value: " + i);
        }
        System.out.println("Update Array 4 to 5");
        array[3]=5;
        for (int i = 0; i <  array.length  ; i++) {
            System.out.println("value: " + i);
        }
        System.out.println("Sort Array");
        Arrays.sort(array);
        for (int i = 0; i <  array.length  ; i++) {
            System.out.println("value: " + i);
        }

        /*LISTAS*/
        //Order, Access by index , Can repeat elements.
        System.out.println("\nARRAYLIST\n");
        List<Integer> list= new ArrayList<>();
        System.out.println("Add 4 elements");
        list.add(8);
        list.add(10);
        list.add(6);
        list.add(5);
        list.forEach(value -> System.out.println("value: " + value));
        list.remove(3);
        System.out.println("Remove last element 5: ");
        list.forEach(value -> System.out.println("value: " + value));
        list.set(0,7);
        System.out.println("Update first element 8 to 7: ");
        list.forEach(value -> System.out.println("value: " + value));
        System.out.println("Sort the elements: ");
        list.sort(Comparator.naturalOrder());
        list.forEach(value -> System.out.println("value: " + value));

        /*ArrayList
        //When: When you need quick access to elements by index.
        //Advantage:The same when
        //Disadvantage:Insertions and deletions in the middle of the list are expensive  because they
        //require scrolling elements.*/
        System.out.println("\nARRAYLIST\n");
        ArrayList<Integer> arrayList= new ArrayList<>();
        System.out.println("Add 4 elements");
        arrayList.add(8);
        arrayList.add(10);
        arrayList.add(6);
        arrayList.add(5);
        arrayList.forEach(value -> System.out.println("value: " + value));
        arrayList.remove(3);
        System.out.println("Remove last element 5: ");
        arrayList.forEach(value -> System.out.println("value: " + value));
        arrayList.set(0,7);
        System.out.println("Update first element 8 to 7: ");
        arrayList.forEach(value -> System.out.println("value: " + value));
        System.out.println("Sort the elements: ");
        arrayList.sort(Comparator.naturalOrder());
        arrayList.forEach(value -> System.out.println("value: " + value));

        /*LinkedList
        //When: When you need a lot of inserts and deletes at the beginning or in the middle of the list.
        //Advantage:The same when
        //Disadvantage:Slow access to items by index due to having to traverse the list from the beginning.*/
        System.out.println("\nLINKEDLIST\n");
        LinkedList<Integer> linkedList= new LinkedList<>();
        System.out.println("Add 4 elements");
        linkedList.add(8);
        linkedList.add(10);
        linkedList.add(6);
        linkedList.add(5);
        linkedList.forEach(value -> System.out.println("value: " + value));
        linkedList.remove(3);
        System.out.println("Remove last element 5: ");
        linkedList.forEach(value -> System.out.println("value: " + value));
        linkedList.set(0,7);
        System.out.println("Update first element 8 to 7: ");
        linkedList.forEach(value -> System.out.println("value: " + value));
        System.out.println("Sort the elements: ");
        linkedList.sort(Comparator.naturalOrder());
        linkedList.forEach(value -> System.out.println("value: " + value));
        //Vector
        //When to use: similar to ArrayList but when you need a synchronized version for access from multiple threads.
        //Advantages: Synchronized, so it is safe for concurrent access.
        System.out.println("\nVECTOR\n");
        Vector<Integer> vector= new Vector<>();
        System.out.println("Add 4 elements");
        vector.add(8);
        vector.add(10);
        vector.add(6);
        vector.add(5);
        vector.forEach(value -> System.out.println("value: " + value));
        vector.remove(3);
        System.out.println("Remove last element 5: ");
        vector.forEach(value -> System.out.println("value: " + value));
        vector.set(0,7);
        System.out.println("Update first element 8 to 7: ");
        vector.forEach(value -> System.out.println("value: " + value));
        System.out.println("Sort the elements: ");
        vector.sort(Comparator.naturalOrder());
        vector.forEach(value -> System.out.println("value: " + value));
        //Stack
        //When to use: When you need a LIFO stack.
        //Advantages: Provides stack-specific methods such as push and pop.
        //Disadvantages: It is deprecated and ArrayDeque is recommended as a replacement
        System.out.println("\nSTACK\n");
        Stack<Integer> stack= new Stack<>();
        System.out.println("Add 4 elements");
        stack.add(8);
        stack.add(10);
        stack.add(6);
        stack.add(5);
        stack.forEach(value -> System.out.println("value: " + value));
        stack.remove(3);
        System.out.println("Remove last element 5: ");
        stack.forEach(value -> System.out.println("value: " + value));
        stack.set(0,7);
        System.out.println("Update first element 8 to 7: ");
        stack.forEach(value -> System.out.println("value: " + value));
        System.out.println("Sort the elements: ");
        stack.sort(Comparator.naturalOrder());
        stack.forEach(value -> System.out.println("value: " + value));

        /*CONJUNTOS*/
        //Unique values, without Order, belongs a group.
        //HashSet
        //When to use: When you need an unordered set and have no duplicates.
        //Advantages: Fast insert, delete and search operations.
        //Disadvantages: Does not guarantee any order of the elements.
        System.out.println("\nHashSet\n");
        HashSet<Integer> hashSet = new HashSet<>();
        hashSet.add(5);
        hashSet.add(3);
        hashSet.add(4);//Ignoring
        hashSet.add(4);
        hashSet.add(1);
        hashSet.forEach(value -> System.out.println("Value: " + value));
        System.out.println("Remove the value 5");
        hashSet.remove(5);
        System.out.println("Update  is not available");
        hashSet.forEach(value -> System.out.println("Value: " + value));
        //LinkedHashSet
        //When to use: when you need a set that maintains insertion order.
        //Advantages: Maintains insertion order.
        //Disadvantages: Slightly slower than HashSet due to order maintenance.
        System.out.println("\nLinkedHashSet\n");
        LinkedHashSet<Integer> linkedHashSet = new LinkedHashSet<>();
        linkedHashSet.add(5);
        linkedHashSet.add(3);
        linkedHashSet.add(4);//Ignoring
        linkedHashSet.add(4);
        linkedHashSet.add(1);
        linkedHashSet.forEach(value -> System.out.println("Value: " + value));
        System.out.println("Remove the value 5");
        linkedHashSet.remove(5);
        System.out.println("Update  is not available");
        linkedHashSet.forEach(value -> System.out.println("Value: " + value));
        //TreeSet
        //When to use: When you need a sorted set.
        //Advantages: Keeps the elements in ascending order.
        //Disadvantages: Slower operations compared to HashSet due to the need to maintain order.
        System.out.println("\nTreeSet\n");
        TreeSet<Integer> treeSet = new TreeSet<>();
        treeSet.add(5);
        treeSet.add(3);
        treeSet.add(4);//Ignoring
        treeSet.add(4);
        treeSet.add(1);
        treeSet.forEach(value -> System.out.println("Value: " + value));
        System.out.println("Remove the value 5");
        treeSet.remove(5);
        System.out.println("Update  is not available");
        treeSet.forEach(value -> System.out.println("Value: " + value));

        /*MAP*/
        //HashMap
        //When to use: when you need an unordered map with unique keys.
        //Advantages: Fast insert, delete and search operations.
        //Disadvantages: Does not guarantee any order of the keys.
        System.out.println("\nHashMap\n");
        HashMap<Integer,Integer> hashMap = new HashMap<>();
        hashMap.put(2,4);
        hashMap.put(3,6);
        hashMap.put(4,8);
        hashMap.put(5,10);
        System.out.println(hashMap);
        System.out.println("remove last  key-value");
        hashMap.remove(5);//clear lo borra entero
        System.out.println(hashMap);
        hashMap.put(2,8);
        System.out.println("update   key 2 to value 8");
        System.out.println(hashMap);
        //LinkedHashMap
        //When to use: When you need a map that maintains insertion or access order.
        //Advantages: Maintains insertion or access order.
        //Disadvantages: Slightly slower than HashMap due to order maintenance.
        System.out.println("\nLinkedHashMap\n");
        LinkedHashMap<Integer,Integer> linkedHashMap = new LinkedHashMap<>();
        linkedHashMap.put(2,4);
        linkedHashMap.put(3,6);
        linkedHashMap.put(4,8);
        linkedHashMap.put(5,10);
        System.out.println(linkedHashMap);
        System.out.println("remove last  key-value");
        linkedHashMap.remove(5);//clear lo borra entero
        System.out.println(linkedHashMap);
        linkedHashMap.put(2,8);
        System.out.println("update   key 2 to value 8");
        System.out.println(linkedHashMap);
        //TreeMap
        //When to use: When you need a map ordered by keys.
        //Advantages: Keeps keys in ascending order.
        //Disadvantages: Slower operations compared to HashMap due to the need to maintain order.
        System.out.println("\nTreeMap\n");
        TreeMap<Integer,Integer> treeMap = new TreeMap<>();
        treeMap.put(2,4);
        treeMap.put(3,6);
        treeMap.put(4,8);
        treeMap.put(5,10);
        System.out.println(treeMap);
        System.out.println("remove last  key-value");
        treeMap.remove(5);//clear lo borra entero
        System.out.println(treeMap);
        treeMap.put(2,8);
        System.out.println("update   key 2 to value 8");
        System.out.println(treeMap);
        //Hashtable
        //When to use: Similar to HashMap but when you need a synchronized version for multi-threaded access.
        //Advantages: Synchronized, so it is safe for concurrent access.
        //Disadvantages: Synchronization operations can add overhead.
        System.out.println("\nHashtable\n");
        Hashtable<Integer,Integer> hashtable = new Hashtable<>();
        hashtable.put(2,4);
        hashtable.put(3,6);
        hashtable.put(4,8);
        hashtable.put(5,10);
        System.out.println(hashtable);
        System.out.println("remove last  key-value");
        hashtable.remove(5);//clear lo borra entero
        System.out.println(hashtable);
        hashtable.put(2,8);
        System.out.println("update   key 2 to value 8");
        System.out.println(hashtable);

        /*QUEUES DEQUES*/
        //PriorityQueue
        //When to use: when you need a queue with priority.
        //Advantages: Items are automatically ordered according to their priority.
        //Disadvantages: Does not allow null elements and is not synchronized.
        System.out.println("PriorityQueue");
        PriorityQueue<Integer> priorityQueue= new PriorityQueue<>();
        priorityQueue.add(2);
        priorityQueue.add(3);
        priorityQueue.add(1);
        System.out.println(priorityQueue);
        System.out.println("Queue with order, all poll");
        System.out.println(priorityQueue.poll()+"-"+priorityQueue.poll()+"-"+priorityQueue.poll());
        //ArrayDeque
        //When to use: When you need a deque or a stack.
        //Advantages: Provides efficient operations to add and remove elements from both ends.
        //Disadvantages: Does not allow null elements.
        System.out.println("ArrayDeque");
        ArrayDeque<Integer> arrayDeque= new ArrayDeque<>();
        arrayDeque.add(2);
        arrayDeque.add(3);
        arrayDeque.add(1);
        System.out.println("peekFirst show the first of the Queue");
        System.out.println(arrayDeque.peekFirst());
        System.out.println(arrayDeque);
        System.out.println("Queue with order, all poll");
        System.out.println(arrayDeque.poll()+"-"+arrayDeque.poll()+"-"+arrayDeque.poll());
        //LinkedList(like Deque)
        //When to use: When you need a deque and also want the features of a linked list.
        //Advantages: Versatility to use as a list, queue or deque.
        //Disadvantages: Slower operations compared to ArrayDeque for some operations.
        System.out.println("LinkedList");
        LinkedList<Integer> linkedListQueue= new LinkedList<>();
        linkedListQueue.add(2);
        linkedListQueue.add(3);
        linkedListQueue.add(1);
        System.out.println(linkedListQueue);
        System.out.println("Update 1 to a 5");
        linkedListQueue.set(2,5);
        System.out.println("delete number 2  add a null");
        linkedListQueue.remove(0);
        System.out.println(linkedListQueue);
        System.out.println("Queue like a list, all poll");
        System.out.println(linkedListQueue.poll()+"-"+linkedListQueue.poll()+"-"+linkedListQueue.poll());

        //EXTRA Contacts
        System.out.println("----------------------------CONTACTS-----------------------------------------------");
        int exit=1;
        ArrayList<String[]> contacts = new ArrayList<>();
        while(exit !=0){
            Scanner chooseNumber= new Scanner(System.in);
            System.out.println("Add contact: 1");
            System.out.println("Update contact: 2");
            System.out.println("Delete contact: 3");
            System.out.println("Sort contact: 4");
            System.out.println("Exit: 5");
            System.out.print("Your Choice: ");
            int number= chooseNumber.nextInt();
            switch (number){
                case 1:
                    System.out.println("Add contact");
                    Scanner chooseName= new Scanner(System.in);
                    System.out.print("Add name: ");
                    String name= chooseName.next();
                    Scanner choosePhone= new Scanner(System.in);
                    System.out.print("Add number: ");
                    String phone= choosePhone.next();
                    if(checkContact(name,phone) ){
                        contacts.add(new String[]{name, phone});
                        System.out.println("New Contact " + name + " added");
                    }
                    break;
                case 2:
                    System.out.println("Update contact");
                    showContacts(contacts);
                    System.out.println("Number to update");
                    int updateNumber= pickNumber();
                    System.out.println("1 update name ");
                    System.out.println("2 update phone ");
                    if(updateNumber >= 0) {
                        updateControl(contacts, updateNumber);
                    }
                    else{
                        System.out.println("Invalid Option");
                    }

                    break;
                case 3:
                    System.out.println("Delete contact");
                    showContacts(contacts);
                    System.out.println("Number to delete");
                    deleteControl(contacts);

                    break;
                case 4:
                    System.out.println("Sort contact");
                    contacts.sort(Comparator.comparing(value -> value[0]));
                    contacts.forEach(value -> System.out.println("Contact: " +value[0] + " Phone: " +value[1]));
                    break;
                case 5:
                    System.out.println("See you");
                    exit =0;
                    break;
                default:
                    System.out.println("Wrong Option");
                    break;
            }

        }
    }
    public static void showContacts(ArrayList<String[]> contacts){
        contacts.forEach(value ->
                System.out.println(contacts.indexOf(value) +".Contact: " +value[0] + " Phone: " +value[1]));

    }
    public static void updateControl(ArrayList<String[]> contacts, int updateNumber){

        int updateOption= pickNumber();
        Scanner newUpdate= new Scanner(System.in);
        String[] oldContact=contacts.get(updateNumber);
        switch (updateOption){
            case 1:

                System.out.print("Add name: ");
                String newName= newUpdate.next();
                if(checkName(newName)){
                    contacts.set(updateNumber,new String[]{newName, oldContact[1]});
                }
                System.out.println("Update name successfully");
                break;
            case 2:
                System.out.print("Add phone: ");
                String newPhone= newUpdate.next();
                if(checkName(newPhone)){
                    contacts.set(updateNumber,new String[]{oldContact[0], newPhone});
                }
                System.out.println("Update phone successfully");
                break;
            case -1:
                break;
            default:
                System.out.println("Invalid option");

        }
    }

    public static void deleteControl(ArrayList<String[]> contacts){
        try {
            contacts.remove(pickNumber());
            System.out.println("Contact deleted");
        }catch (IndexOutOfBoundsException e){

        }

    }

    public static int pickNumber(){
        try {
            Scanner chooseNumber= new Scanner(System.in);
            return chooseNumber.nextInt();
        }catch (InputMismatchException e){
            System.out.println("Invalid Option");
            return -1;
        }
    }
    public static boolean checkName(String name){
        boolean answer= name != null;
        return answer;
    }
    public static boolean checkPhone(String phone){
        boolean answer= phone != null && phone.length()<=11 && !phone.isEmpty();

        try {
            Long.parseLong(phone);
        }catch (NumberFormatException e){
            answer = false;
            System.out.println("It´s not numeric" );
        }
        return answer;
    }
    public static  boolean checkContact(String name,String phone){
        return checkPhone(phone) && checkName(name);
    }

}