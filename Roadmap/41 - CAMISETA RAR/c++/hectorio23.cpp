// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

// FOR UBUNTU:
// sudo apt install zlib1g-dev

// FOR ARCH LINUX
// sudo pacman -S zlib1g-dev

// For compiling the program use:
// g++ hectorio23.cpp -o hectorio23 -lz


#include <iostream>
#include <fstream>
#include <zlib.h> // Librería para manejar gzip
#include <stdexcept>

// Función para comprimir en formato gzip usando zlib
void comprimirGzip(const std::string& archivo) {
    std::ifstream file(archivo, std::ios_base::binary);
    if (!file.is_open()) {
        throw std::runtime_error("No se pudo abrir el archivo.");
    }

    std::string compressedFile = archivo + ".gz";
    gzFile outFile = gzopen(compressedFile.c_str(), "wb");
    if (!outFile) {
        throw std::runtime_error("No se pudo crear el archivo comprimido.");
    }

    char buffer[128];
    while (file.read(buffer, sizeof(buffer)) || file.gcount()) {
        gzwrite(outFile, buffer, file.gcount());
    }

    gzclose(outFile);
    std::cout << "Archivo comprimido exitosamente en formato gzip: " << compressedFile << std::endl;
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cerr << "Uso: " << argv[0] << " <archivo> <formato(gzip)>" << std::endl;
        return 1;
    }

    try {
        comprimirGzip(argv[1]);  // Por ahora, solo manejo gzip
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}


