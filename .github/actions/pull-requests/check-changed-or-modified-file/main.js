const core = require('@actions/core')
const path = require('node:path')
const utils = require('../../utils.js')

// Required data
const author = core.getInput('author')
const challenge = core.getInput('challenge')
const changedOrModifiedFile = core.getInput('changed-or-modified-file')
const programmingLanguage = core.getInput('programming-language')

const changedOrModifiedFileProps = path.parse(changedOrModifiedFile)
const challengeProps = utils.challenges.getChallengeProps(challenge)
const languageProps = utils.programmingLanguages.getLanguageProps(programmingLanguage)

// By the required actions we know that the challenge and language exists
if (challengeProps && languageProps) {
	const { folderName: challengeFolder } = challengeProps
	const { folderName: languageFolder, fileExtension: languageFileExtension } = languageProps
	const expectedDirectory = path.join('Roadmap', challengeFolder, languageFolder ?? '')

	// Check if directory is valid
	const isValidDirectory = changedOrModifiedFileProps.dir === expectedDirectory
	if (!isValidDirectory) {
		core.setFailed(
			"Directory of the changed or modified file of the pull request doesn't match with the challenge and programming language of the pull request title. " +
				'Please check the directory of the changed or modified file of the pull request. ' +
				`It should be: ${expectedDirectory}` +
				'If you think this is an error, please contact an administrator.'
		)
	}

	// Check if file name is valid
	const isValidFileName = changedOrModifiedFileProps.name === author
	if (!isValidFileName) {
		core.setFailed(
			"File name of the changed or modified file of the pull request doesn't match with the author name. " +
				'Please check the file name of the changed or modified file of the pull request. ' +
				`It should be: ${author}` +
				'If you think this is an error, please contact an administrator.'
		)
	}

	// Check if file extension is valid
	const isValidFileExtension = changedOrModifiedFileProps.ext === languageFileExtension
	if (!isValidFileExtension) {
		core.setFailed(
			"File extension name of the changed or modified file of the pull request doesn't match with the programming language of the pull request title. " +
				'Please check the file extension name of the changed or modified file of the pull request. ' +
				`It should be: ${languageFileExtension}` +
				'If you think this is an error, please contact an administrator.'
		)
	}
}
