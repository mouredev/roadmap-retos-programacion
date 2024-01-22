import { debug, getInput, setFailed } from '@actions/core'
import { arraytoString, getChallengeNumbers, getProgrammingLanguageFolderNames } from '../../utils.js'

// Inputs
const title = getInput('title')
debug(`'title' (input): ${title}`)

// Required data
const challenges = getChallengeNumbers()
const languageNames = getProgrammingLanguageFolderNames()
debug(`Available challenge numbers: ${challenges}`)
debug(`Available names of programming languages: ${languageNames}`)

const challengesJoined = challenges.join('|')
const languageNamesJoined = languageNames.join('|').replaceAll('+', '\\+')

// Regular expressions
const challengeRegex = new RegExp(`#(${challengesJoined})`)
const languageNameRegex = new RegExp(`(${languageNamesJoined})+$`, 'i')
debug(`Challenge number regular expression: ${challengeRegex}`)
debug(`Programming language name regular expression: ${languageNameRegex}`)

// Check if challenge number is valid
const isValidChallenge = challengeRegex.test(title)
debug(`Is valid challenge number? ${isValidChallenge}`)

if (!isValidChallenge) {
	const availableChallenges = arraytoString({
		array: challenges,
		finalSeparator: ', or ',
		separator: ', ',
	})

	setFailed(
		"Challenge number of the pull request title doesn't match with existing ones. " +
			'Please check the challenge number of the pull request title. ' +
			`It should be one of these: ${availableChallenges}. ` +
			'If you think this is an error, please contact an administrator.'
	)
}

// Check if programming language name is valid
const isValidLanguageName = languageNameRegex.test(title)
debug(`Is valid programming language name? ${isValidLanguageName}`)

if (!isValidLanguageName) {
	const availableLanguageNames = arraytoString({
		array: languageNames.map((languageName) => languageName[0].toUpperCase() + languageName.slice(1)),
		finalSeparator: ', or ',
		separator: ', ',
	})

	setFailed(
		"Programming language name of the pull request title doesn't match with existing ones. " +
			'Please check the programming language name of the pull request title. ' +
			`It should be one of these: ${availableLanguageNames}. ` +
			'If you think this is an error, please contact an administrator.'
	)
}

if (isValidChallenge && isValidLanguageName) {
	const titleFormatRegex = new RegExp(`#(${challengesJoined}) - (${languageNamesJoined})`, 'i')
	debug(`Title format regular expression: ${titleFormatRegex}`)

	const matches = title.match(titleFormatRegex)
	const isValidTitleFormat = matches && matches.length > 0
	debug(`Is valid title format? ${isValidTitleFormat}`)

	if (!isValidTitleFormat) {
		// On invalid title, set the action as failed
		setFailed(
			'Invalid pull request title format. ' +
				"It should be: '#<CHALLENGE NUMBER> - <LANGUAGE NAME>'. " +
				"For example: '#01 - Javascript'."
		)
	}
}
