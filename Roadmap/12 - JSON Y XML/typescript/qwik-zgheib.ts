/* -- exercise */
import fs from "fs";

interface Content {
  name: string;
  age: number;
  birthdate: string;
  programmingLanguages: string[];
}

const content: Content = {
  name: "Qwik Zgheib",
  age: 22,
  birthdate: "2002-11-09",
  programmingLanguages: ["JavaScript", "Typescript", "Python"],
};

type FileType = "json" | "xml";

const exerciseMain = {
  createfile: (filename: string, content: Content, type: FileType = "json"): void => {
    try {
      const jsonContent: string = JSON.stringify(content);
      if (type === "json") fs.writeFileSync(`${filename}.json`, jsonContent);
      if (type === "xml") {
        const xmlContent: string = `<data>
          <name>${content.name}</name>
          <age>${content.age}</age>
          <birthdate>${content.birthdate}</birthdate>
          <programmingLanguages>
            ${content.programmingLanguages.map((lang) => `<language>${lang}</language>`).join("")}
          </programmingLanguages>
        </data>`;
        fs.writeFileSync(`${filename}.xml`, xmlContent);
      }
    } catch (error) {
      console.error(error);
    }
  },
  readFile: (filename: string): void => {
    try {
      const jsonContent: string = fs.readFileSync(`${filename}.json`, "utf-8");
      const xmlContent: string = fs.readFileSync(`${filename}.xml`, "utf-8");
      console.log(`Reading ${filename}.json\n`, jsonContent);
      console.log(`\nReading ${filename}.xml\n`, xmlContent);
    } catch (error) {
      console.error(error);
    }
  },
  deleteFile: (filename: string): void => {
    try {
      console.log("Deleting files...");
      fs.unlinkSync(`${filename}.json`);
      fs.unlinkSync(`${filename}.xml`);
    } catch (error) {
      console.error(error);
    }
  },
};

exerciseMain.createfile("data", content, "json");
exerciseMain.createfile("data", content, "xml");

exerciseMain.readFile("data");
exerciseMain.deleteFile("data");
