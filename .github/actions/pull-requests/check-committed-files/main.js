import { debug, getInput, setFailed } from '@actions/core'
import path from 'node:path'

// Inputs
const author = getInput('author')
const committedFiles = getInput('committed-files').split('\\n')
debug(`'author' (input): ${author}`)
debug(`'committed-files' (input): ${committedFiles}`)

// Check each commited file
for (const committedFile of committedFiles) {
	const parsedFile = path.parse(committedFile)
	debug(`Committed file properties: ${parsedFile}`)

	// Check file name
	const isValidFileName = parsedFile.name.toLowerCase() === author.toLowerCase()
	debug(`Is valid file name? ${isValidFileName}`)

	if (!isValidFileName) {
		setFailed(
			`The file name: '${parsedFile.name + parsedFile.ext}', inside '${
				parsedFile.dir
			}' directory doesn't match with the author name of the pull request. ` +
				'Please rename the file name. ' +
				`It should be: '${author}', case insensitive. ` +
				'If you think this is an error, please contact an administrator.'
		)
	}
}
