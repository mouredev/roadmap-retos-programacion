import { debug, getInput, setFailed } from '@actions/core'
import * as path from 'node:path'
import { getChallengeFolder, getProgrammingLanguageExtension, wrapperChallengesFolder } from '../../utils.mjs'

// Inputs
const author = getInput('author')
const committedFile = getInput('committed-file')
const title = getInput('title')
debug(`'author' (input): ${author}`)
debug(`'committed-file' (input): ${committedFile}`)
debug(`'title' (input): ${title}`)

// Required data
const titleProps = {
	challenge: title.slice(1, 3),
	language: title.slice(6).toLowerCase(),
}
debug(`Title properties: ${JSON.stringify(titleProps)}`)

const challengeFolder = getChallengeFolder(titleProps.challenge)
const committedFileProps = path.parse(committedFile)
committedFileProps.dir = path.normalize(committedFileProps.dir)
debug(`Folder name of the programming language: ${challengeFolder}`)
debug(`Committed file properties: ${JSON.stringify(committedFileProps)}`)

// Check if directory is valid
const expectedDirectory = path.join(wrapperChallengesFolder, challengeFolder, titleProps.language)
const isValidDirectory = committedFileProps.dir === expectedDirectory
debug(`Expected directory: ${expectedDirectory}`)
debug(`Is valid directory? ${isValidDirectory}`)

if (!isValidDirectory) {
	setFailed(
		"Directory of committed file doesn't match with the challenge and programming language of the pull request title. " +
			'Please check the directory of committed file of the pull request. ' +
			`It should be: '${expectedDirectory}'. ` +
			'If you think this is an error, please contact an administrator.'
	)
}

// Check if file name is valid
const isValidFileName = committedFileProps.name === author
debug(`Is valid file name? ${isValidFileName}`)

if (!isValidFileName) {
	setFailed(
		"File name of committed file doesn't match with the author name. " +
			'Please check the file name of committed file of the pull request. ' +
			`It should be: '${author}'. ` +
			'If you think this is an error, please contact an administrator.'
	)
}

// Check if file extension is valid
const expectedFileExtension = getProgrammingLanguageExtension(titleProps.language)
const isValidFileExtension = committedFileProps.ext === expectedFileExtension
debug(`Expected file extension: ${expectedFileExtension}`)
debug(`Is valid file extension? ${isValidFileExtension}`)

if (!isValidFileExtension) {
	setFailed(
		"File extension of committed file doesn't match with the programming language name of the pull request title. " +
			'Please check the file extension name of committed file of the pull request. ' +
			`It should be: '${expectedFileExtension}'. ` +
			'If you think this is an error, please contact an administrator.'
	)
}
