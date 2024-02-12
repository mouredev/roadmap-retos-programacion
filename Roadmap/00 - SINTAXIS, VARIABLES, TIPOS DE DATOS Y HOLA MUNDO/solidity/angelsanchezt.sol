// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Encuentra más información en: https://docs.soliditylang.org/

// Este es un comentario de una línea en Solidity.

/*
  Este es un comentario de varias líneas en Solidity.
  Puedes añadir más información aquí.
*/

contract MiContrato {
    // Variable
    uint256 public miVariable;

    // Constante
    uint256 public constant MI_CONSTANTE = 42;

    // Variables representando tipos de datos primitivos
    bool public miBool = true;
    int256 public miInt = -123;
    uint256 public miUint = 456;
    address public miAddress = 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4;
    string public miString = "Hola, mundo!";
    bytes32 public miBytes32 = 0x5a78f59fd5c970eddfdbb96bb5ca45671b63b3bb9c8427e4b9503260d297056a;

    // Constructor
    constructor() {
        miVariable = 7;
    }

    // Función para imprimir por terminal
    function imprimirSaludo() public pure returns (string memory) {
        return "Hola, Solidity!";
    }
}
