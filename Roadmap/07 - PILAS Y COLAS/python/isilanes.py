from typing import Any


class Stack:
    """
    Implementation of a stack of elements (LIFO).
    """

    def __init__(self):
        self.contents = []

    def add(self, element: Any) -> None:
        """
        Add element 'element' to the stack.

        Args:
            element (Any):
                Object to add to the upper position of the stack.

        Returns:
            Nothing.
        """
        self.contents.append(element)

    def remove(self) -> Any:
        """
        Remove (and return) the upper element of the stack.

        Args:
            None.

        Returns:
            Last element in the stack, or None if stack is empty.
        """
        return self.contents.pop() if self.contents else None

    def drop(self) -> None:
        """
        Remove all elements in the stack, resulting in an empty stack.
        The dropped elements are not returned.

        Args:
            None.

        Returns:
            Nothing.
        """
        self.contents = []


class Queue:
    """
    Implementation of a queue of elements (FIFO).
    """

    def __init__(self):
        self.contents = []

    def add(self, element: Any) -> None:
        """
        Add element 'element' to the queue.

        Args:
            element (Any):
                Object to add to the last position of the queue.

       Returns:
           Nothing.
        """
        self.contents.append(element)

    def remove(self) -> Any:
        """
        Remove (and return) the upper element of the stack.

        Args:
            None.

        Returns:
            Last element in the stack, or None if the queue is empty.
        """
        return self.contents.pop(0) if self.contents else None


def main() -> None:
    s = Stack()
    s.add(1)
    s.add(2)
    s.add(3)
    print(f"Stack after adding 3 elements: {s.contents}")
    extracted = s.remove()
    print(f"Stack after removing 1 element ({extracted}): {s.contents}")

    q = Queue()
    q.add(1)
    q.add(2)
    q.add(3)
    print(f"Queue after adding 3 elements: {q.contents}")
    extracted = q.remove()
    print(f"Queue after removing 1 element ({extracted}): {q.contents}")


def browser(verbose: bool = False) -> None:
    """
    Simulate a browser history using stacks.

    Each step we are asked for a new URL. Our response options are:
    - quit: exit the browser.
    - atrás: go back to the previous URL in the browse history. If we are
             at the first URL in the history, give a warning and do nothing.
    - adelante: go to the next URL in the browse history. If we are at the
                latest URL, give a warning and do nothing.
    - <url>: go to that URL.

    Note that going to a new URL will erase any existing future URL. For example:
    If we visit URLs A, B, C and D, the past URLs are (A, B, C), and the current one
    is D. If we go back (atrás) twice, the current URL will be B. The previous URL will be
    just A. Now going forward (adelante) would take us to C, then D. However, if we are
    sitting at B, and now we visit X, the "future" URLs (C, D) will be dropped. The current
    URL will be X, and the "past" ones will be (A, B).

    Args:
        verbose (bool):
            If True, print the state of the past/present/future URL stacks at every step.
            By default, do not print it.

    Returns:
        Nothing.
    """
    past_stack = Stack()
    future_stack = Stack()
    current_url = None

    while True:
        if verbose:
            print(f"{past_stack.contents} <- {current_url} -> {future_stack.contents}")

        url = input("Introduce una URL que visitar, o adelante/atrás para visitar la página correspondiente (quit para salir): ")
        if url == "quit":
            print("Saliendo...")
            break

        if url == "adelante":
            url = future_stack.remove()
            if url is None:
                print(f"Ya estás en la última URL: {current_url}")
                continue
            if current_url is not None:  # the undefined initial 'URL'
                past_stack.add(current_url)
            current_url = url
            print(f"Avanzamos a la URL '{url}'")
            continue

        if url == "atrás":
            url = past_stack.remove()
            if url is None:
                print(f"Ya estás en la primera URL: {current_url}")
                continue
            if current_url is not None:  # this should never happen
                future_stack.add(current_url)
            current_url = url
            print(f"Retrocedemos a la URL '{url}'")
            continue

        if current_url is not None:  # the undefined initial 'URL'
            past_stack.add(current_url)
        current_url = url
        future_stack.drop()
        print(f"Como pediste, visitamos la URL '{url}'")


def shared_printer(verbose: bool = False) -> None:
    """
    Simulate a shared printer, using a Queue. The user is prompted for documents. Any string is
    interpreted as a 'document', except the string 'quit', which quits, and 'imprimir', which
    'prints' one document from the queue, effectively removing it from the queue.

    Args:
        verbose (bool):
            If True, print the status of the queue at every step.
            By default, do not print it.

    Return:
        Nothing.
    """
    printer = Queue()

    while True:
        if verbose:
            print(f"Cola: {printer.contents}")

        msg = (
            "Introduce un documento a imprimir"
            ", o 'imprimir' para procesar un documento de la cola"
            ", o 'quit' para salir: "
        )
        doc = input(msg)
        if doc == "quit":
            print("Saliendo...")
            break

        if doc == "imprimir":
            doc = printer.remove()
            if doc is None:
                print("La cola de impresión está vacía.")
                continue
            print(f"Imprimiendo el documento: {doc}")
            continue

        printer.add(doc)
        print(f"Añadido el documento {doc} a la cola de impresión.")


def extra() -> None:
    browser(verbose=True)
    shared_printer(verbose=True)


if __name__ == "__main__":
    main()
    extra()
