import { debug, getInput, setFailed } from '@actions/core'
import path from 'node:path'
import {
	arraytoString,
	getProgrammingLanguageExtension,
	getProgrammingLanguageFolderName,
	getProgrammingLanguageFolderNames,
} from '../../utils.mjs'

// Inputs
const author = getInput('author')
const committedFiles = getInput('committed-files').split('\\n')
debug(`'author' (input): ${author}`)
debug(`'committed-files' (input): ${committedFiles}`)

// Required data
const authorLowerCase = author.toLowerCase()
const programmingLanguageFolders = getProgrammingLanguageFolderNames()
debug(`Author name (lowercase): ${authorLowerCase}`)
debug(`Programming language folder names: ${programmingLanguageFolders}`)

// Check each commited file
for (const committedFile of committedFiles) {
	const parsedFile = path.parse(committedFile)
	debug(`Committed file properties: ${parsedFile}`)

	// Check file name
	const isValidFileName = parsedFile.name.toLowerCase() === authorLowerCase
	debug(`Is valid file name? ${isValidFileName}`)

	if (!isValidFileName) {
		setFailed(
			`The file name: '${parsedFile.base}', inside '${parsedFile.dir}' directory doesn't match with the author name of the pull request. ` +
				'Please rename the file name. ' +
				`It should be: '${author}', case insensitive. ` +
				'If you think this is an error, please contact an administrator.'
		)
	}

	// Check programming language folder
	const programmingLanguageFolder = parsedFile.dir.split(path.sep).pop() // Get the last folder, in this case the programming language name.
	debug(`Last folder of the commited file: ${programmingLanguageFolder}`)

	if (!programmingLanguageFolder) {
		throw new Error(
			`The programming language folder of '${parsedFile.base}' (committed file) inside '${parsedFile.dir}' is undefined!`
		)
	}

	if (!programmingLanguageFolders.includes(programmingLanguageFolder)) {
		setFailed(
			`The programming language folder '${programmingLanguageFolder}', where '${parsedFile.base}' (committed file) is located doesn't match with an existing one. ` +
				`It should be on of these: ${arraytoString({
					array: programmingLanguageFolders,
					finalSeparator: ', or ',
					separator: ', ',
				})}. ` +
				'If you think this is an error, please contact an administrator.'
		)
	}

	// Check file extension
	const expectedFileExtBasedOnLastFolder = getProgrammingLanguageExtension(programmingLanguageFolder)
	const isValidFileExtension = parsedFile.ext === expectedFileExtBasedOnLastFolder
	debug(`Expected file extension based on the last folder of the commited file: ${expectedFileExtBasedOnLastFolder}`)
	debug(`Is valid file extension? ${isValidFileExtension}`)

	if (!isValidFileExtension) {
		const expectedLastFolderBasedOnCommittedFileExt = getProgrammingLanguageFolderName(parsedFile.ext)
		debug(`Expected last folder based on the extension of the commited file: ${expectedLastFolderBasedOnCommittedFileExt}`)

		setFailed(
			`The file extension of '${parsedFile.base}' file, inside '${parsedFile.dir}' directory doesn't match with the programming language folder. ` +
				'Check the file extension or the programming language folder where it is located. ' +
				`The file extension should be: '${expectedFileExtBasedOnLastFolder}', ` +
				`or the programming language folder where it is located should be: '${expectedLastFolderBasedOnCommittedFileExt}'. ` +
				'If you think this is an error, please contact an administrator.'
		)
	}
}
