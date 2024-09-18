public class simonguzman {
    public static void main(String[] args) {
        libraryManagementSystemLiskovViolation();
    }

    /****************************** ejemplo sin lsp (Incorrecto) ******************************/
    public static void libraryManagementSystemLiskovViolation(){
        Book physicalBook = new Book("1984", "George Orwell", 3);
        EBook ebook = new EBook("Digital Fortress", "Dan Brown", "www.download.com");

        LoanManager loanManager = new LoanManager();

        loanManager.borrowBook(physicalBook);
        
        loanManager.borrowBook(ebook);
    }

    static class Book{
        private String title;
        private String author;
        private int copies;

        public Book(){

        }

        public Book(String title, String author, int copies){
            this.title = title;
            this.author = author;
            this.copies = copies;
        }

        public String getTitle() {
            return title;
        }

        public int getCopies() {
            return copies;
        }

        public void setCopies(int copies) {
            this.copies = copies;
        }

        public void borrow(){
            if (copies > 0){
                copies--;
                System.out.println("Libro prestado: " + title);
            } else {
                System.out.println("No hay copias disponibles de: " + title);
            }
        }        
    }

    static class EBook extends Book {
        private String downloadLink;

        public EBook(String title, String author,String downloadLink) {
            super(title, author, 1);
            this.downloadLink = downloadLink;
        }

        @Override
        public void borrow(){
            System.out.println("No se puede prestar el eBook, pero puedes descargarlo aquí: " + downloadLink);
        }
    }

    static class LoanManager{
        public void borrowBook(Book book){
            book.borrow();
        }
    }
}
