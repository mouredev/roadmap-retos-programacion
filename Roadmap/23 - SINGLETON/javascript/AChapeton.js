const counter = () => {
  var instance = null;
  var count = 0;
  function printCount() {
      console.log("Numero de instancias activas: " + count);
  }
  function init() {
      count++;
      return {};
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
      createInstance: createInstance,
      closeInstance: closeInstance,
      printCount: printCount
  };
}
var foo = counter();
foo.printCount();
foo.createInstance();
foo.printCount();
foo.createInstance();
foo.printCount();
foo.createInstance();
foo.printCount();
foo.closeInstance();
foo.printCount();
foo.createInstance();
foo.printCount();
foo.closeInstance();
foo.printCount();
