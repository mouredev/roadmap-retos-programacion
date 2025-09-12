interface fooType {
  createInstance: () => {};
  closeInstance: () => void;
  printCount: () => void;
}

const counter = () => {

  let instance: {} | null = null;
  let count: number = 0;

  function printCount() {
      console.log("Numero de instancias activas: " + count);
  }

  function init() {
      count++;
      return {}
  }

  function createInstance() {
      if (instance == null) {
        instance = init();
      }
      return instance;
  }

  function closeInstance() {
      count--;
      instance = null;
  }

  return {
      createInstance,
      closeInstance,
      printCount
  }
}

let foo: fooType = counter();

foo.printCount()  
foo.createInstance()
foo.printCount() 
foo.createInstance()
foo.printCount() 
foo.createInstance()
foo.printCount() 
foo.closeInstance()
foo.printCount() 
foo.createInstance();
foo.printCount();
foo.closeInstance();
foo.printCount();