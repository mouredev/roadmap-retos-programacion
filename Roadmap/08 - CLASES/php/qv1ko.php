<?php

    class C1 {

        private $c1String;

        public function __construct($value = "example") {
            $this->c1String = $value;
        }

        public function getC1String() {
            return $this->c1String;
        }

        public function setC1String($c1String) {
            $this->c1String = $c1String;
        }

        public function __toString() {
            return "Class 1 value: " . $this->c1String;
        }

    }

    class C2 {

        private $c2String;

        public function __construct($value = "example") {
            $this->c2String = $value;
        }

        public function getC2String() {
            return $this->c2String;
        }

        public function setC2String($c2String) {
            $this->c2String = $c2String;
        }

        public function __toString() {
            return "Class 2 value: " . $this->c2String;
        }

    }

    function main() {

        $example1 = new C1();
        echo $example1 . "\n";
        $example1->setC1String("Example 1");
        echo $example1->getC1String() . "\n";

        $example2 = new C2();
        echo $example2 . "\n";
        $example2->setC2String("Example 2");
        echo $example2->getC2String() . "\n";

    }

    main();

?>
