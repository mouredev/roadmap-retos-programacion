import arc from 'archiver'
import fs from 'node:fs'
import fsP from 'node:fs/promises'
import path from 'node:path'

/* -------------------------------------------------------------------------- */
/*                                    TYPES                                   */
/* -------------------------------------------------------------------------- */

type FilePath = `${string}/${string}.${string}`
type ZipFilePath = `${string}/${string}.zip`

/* -------------------------------------------------------------------------- */
/*                                  FUNCTIONS                                 */
/* -------------------------------------------------------------------------- */

async function createZipFile(
    filePaths: FilePath[],
    zipFilePath: ZipFilePath
): Promise<void> {
    const ws: fs.WriteStream = fs.createWriteStream(zipFilePath)
    const archive = arc.create('zip', {
        zlib: {level: 9},
    })

    archive.pipe(ws)

    for (const filePath of filePaths) {
        const fileContent: string = await fsP.readFile(filePath, {
            encoding: 'utf-8',
        })
        archive.append(fileContent, {name: path.basename(filePath)})
    }

    await archive.finalize()
    ws.close()
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

;(async () => {
    const filePaths: FilePath[] = ['./hozlucas28.ts', './hozlucas28.txt']
    const compressPath: ZipFilePath = './hozlucas28.zip'

    for (const filePath of [...filePaths.slice(1), compressPath]) {
        if (fs.existsSync(filePath)) await fsP.rm(filePath)
    }

    const fileContent: string[] = ['Lucas Nahuel Hoz', '22', 'Argentina']
    await fsP.writeFile(filePaths[1], fileContent.join('|'), {
        encoding: 'utf-8',
    })

    await createZipFile(filePaths, compressPath)

    // Uncomment to remove files on program finish
    // for (const filePath of [...filePaths.slice(1), compressPath]) {
    //     await fsP.rm(filePath)
    // }
})()
