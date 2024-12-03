package main

import (
	"archive/zip"
	"io"
	"os"
	"strings"
)

/* -------------------------------------------------------------------------- */
/*                                  FUNCTIONS                                 */
/* -------------------------------------------------------------------------- */

func createZip(filePaths []string, zipFilePath string) error {
	archive, err := os.Create(zipFilePath)
	if err != nil {
		return err
	}
	defer archive.Close()

	var zipWriter *zip.Writer = zip.NewWriter(archive)
	defer zipWriter.Close()

	for _, filePath := range filePaths {
		file, err := os.Open(filePath)
		if err != nil {
			return err
		}
		defer file.Close()

		fileStats, err := file.Stat()
		if err != nil {
			return err
		}

		fileZipped, err := zipWriter.Create(fileStats.Name())
		if err != nil {
			return err
		}

		_, err = io.Copy(fileZipped, file)
		if err != nil {
			return err
		}
	}

	zipWriter.Close()

	return nil
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	var filePaths []string = make([]string, 2, 2)
	filePaths[0] = "./hozlucas28.go"
	filePaths[1] = "./hozlucas28.txt"

	var zipFilePath string = "./hozlucas28.zip"

	for _, filePath := range append(filePaths[1:], zipFilePath) {
		if _, err := os.Stat(filePath); err == nil {
			if err = os.Remove(filePath); err != nil {
				panic(err)
			}
		}
	}

	var fileContent []string = make([]string, 3, 3)
	fileContent[0] = "Lucas Nahuel Hoz"
	fileContent[1] = "23"
	fileContent[2] = "Argentina"

	file, err := os.Create(filePaths[1])
	if err != nil {
		panic(err)
	}

	_, err = file.WriteString(strings.Join(fileContent, "|"))
	if err != nil {
		panic(err)
	}

	createZip(filePaths, zipFilePath)

	file.Close()

	// Uncomment to remove files on program finish
	// for _, filePath := range append(filePaths[1:], zipFilePath) {
	// 	if _, err := os.Stat(filePath); err == nil {
	// 		if err = os.Remove(filePath); err != nil {
	// 			panic(err)
	// 		}
	// 	}
	// }
}
