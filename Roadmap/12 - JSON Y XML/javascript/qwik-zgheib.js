/* -- exercise */
import fs from "fs";

const content = {
  name: "Qwik Zgheib",
  age: 22,
  birthdate: "2002-11-09",
  programmingLanguages: ["JavaScript", "Typescript", "Python"],
};

const exerciseMain = {
  createfile: (filename, content, type = "json") => {
    try {
      const jsonContent = JSON.stringify(content);
      if (type === "json") fs.writeFileSync(`${filename}.json`, jsonContent);
      if (type === "xml") {
        const xmlContent = `<data>
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
  readFile: (filename) => {
    try {
      const jsonContent = fs.readFileSync(`${filename}.json`, "utf-8");
      const xmlContent = fs.readFileSync(`${filename}.xml`, "utf-8");
      console.log(`Reading ${filename}.json\n`, jsonContent);
      console.log(`\nReading ${filename}.xml\n`, xmlContent);
    } catch (error) {
      console.error(error);
    }
  },
  deleteFile: (filename) => {
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
