const core = require('@actions/core')
const utils = require('../../utils.js')
const process = require('node:process')

// Required data
const title = core.getInput('title')
const challengeNumbers = utils.challenges.getNumbers()
const programmingLanguageNames = utils.programmingLanguages.getNames()

// Regular expressions
const challengeNumberRegex = new RegExp(`#(${challengeNumbers.join('|')})`)
const programmingLanguageNameRegex = new RegExp(`(${programmingLanguageNames.join('|')})+$`)
const titleRegex = new RegExp(`#(${challengeNumbers.join('|')}) - (${programmingLanguageNames.join('|')})`)

// Check if challenge number is valid
const isValidChallengeNumber = challengeNumberRegex.test(title)
if (!isValidChallengeNumber) {
	const availableChallengeNumbers = challengeNumbers.reduce((prev, current, index, array) => {
		if (index === 0) return current.toString()
		if (index === array.length - 1) return prev + ', or ' + current
		return prev + ', ' + current
	})

	core.setFailed(
		"Challenge number of the pull request title doesn't match with existing ones. " +
			'Please check the challenge number of the pull request title. ' +
			`It should be one of these: ${availableChallengeNumbers}` +
			'If you think this is an error, please contact an administrator.'
	)
}

// Check if programming language name is valid
const isValidProgrammingLanguageName = programmingLanguageNameRegex.test(title)
if (!isValidProgrammingLanguageName) {
	const availableProgrammingLanguageNames = programmingLanguageNames.reduce((prev, current, index, array) => {
		if (index === 0) return current
		if (index === array.length - 1) return prev + ', or ' + current
		return prev + ', ' + current
	})

	core.setFailed(
		"Programming language name of the pull request title doesn't match with existing ones. " +
			'Please check the programming language name of the pull request title. ' +
			`It should be one of these: ${availableProgrammingLanguageNames}` +
			'If you think this is an error, please contact an administrator.'
	)
}

if (isValidChallengeNumber && isValidProgrammingLanguageName) {
	const matches = title.match(titleRegex)
	const isValidTitle = matches && matches.length > 0

	if (isValidTitle) {
		// On valid title, set the outputs
		core.setOutput('challenge', matches[1])
		core.setOutput('programming-language', matches[2])
	} else {
		// On invalid title, set the action as failed
		core.setFailed(
			'Invalid pull request title format. ' +
				'It should be: #<CHALLENGE NUMBER> - <LANGUAGE NAME>. ' +
				'For example: #01 - JavaScript'
		)
	}
}
