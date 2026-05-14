import fs from "fs"
import { stat } from "fs/promises"
import zlib from "zlib"
import { pipeline } from "stream/promises"

const filePathToCompress = "archivo.txt"
const pathToCompressedFileSaved = "archivo.txt.gz"

async function compressFile(inputPath, outboundPath) {
  const reading = fs.createReadStream(inputPath)

  const compresion = zlib.createGzip()

  const writing = fs.createWriteStream(outboundPath)

  try {
    await pipeline(reading, compresion, writing)
    console.log('✅ File successfully compressed')
  } catch (e) {
    console.error('❌ Compression failed:', e)
  }
}

async function checkSize(inputPath) {
  const size = await stat(inputPath)
  return size.size
}

async function program(inputPath, outboundPath) {
  const initialSize = await checkSize(inputPath)

  console.info("Initial file size: " + initialSize)

  await compressFile(inputPath, outboundPath)

  const finalSize = await checkSize(outboundPath)

  console.info("Final file size: " + finalSize)
}

program(filePathToCompress, pathToCompressedFileSaved)