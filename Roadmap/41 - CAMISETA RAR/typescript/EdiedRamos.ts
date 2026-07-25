// Author: EdiedRamos
// Github: https://github.com/EdiedRamos

import { createGzip, type Gzip } from "node:zlib";
import { pipeline } from "node:stream";
import { createReadStream, createWriteStream } from "node:fs";
import { join } from "node:path";

// ===========
// = CLASSES =
// ===========
class Compression {
  private gzip: Gzip;

  constructor() {
    this.gzip = createGzip();
  }

  public compress(sourcePath: string, destinationPath: string): Promise<void> {
    return new Promise((resolve, reject) => {
      const source = createReadStream(sourcePath);
      const destination = createWriteStream(destinationPath);

      pipeline(source, this.gzip, destination, (err) => {
        if (err) {
          reject(err);
        } else {
          resolve();
        }
      });
    });
  }
}

// ========
// = MAIN =
// ========

(() => {
  const compression = new Compression();
  compression.compress("YOUR_SOURCE_PATH", "YOUR_DESTINATION_PATH");
})();
