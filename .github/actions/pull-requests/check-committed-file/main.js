import { debug, getInput, setFailed } from '@actions/core'
import * as path from 'node:path'
import { getChallengeFolder, getProgrammingLanguageExtension, wrapperChallengesFolder } from '../../utils.js'

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

const challengeFolder = getChallengeFolder(titleProps.challenge)
const committedFileProps = path.parse(committedFile)

// Check if directory is valid
const expectedDirectory = path.join(wrapperChallengesFolder, challengeFolder, titleProps.language)
const isValidDirectory = path.normalize(committedFileProps.dir) === expectedDirectory
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
if (!isValidFileExtension) {
	setFailed(
		"File extension of committed file doesn't match with the programming language name of the pull request title. " +
			'Please check the file extension name of committed file of the pull request. ' +
			`It should be: '${expectedFileExtension}'. ` +
			'If you think this is an error, please contact an administrator.'
	)
}
