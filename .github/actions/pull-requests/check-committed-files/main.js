import { debug, getInput, setFailed } from '@actions/core'

// Inputs
const committedFiles = getInput('committed-files').split('\\n')
debug(`'committed-files' (input): ${committedFiles}`)

// Check if changed and modified files are valid
const isValidCommittedFiles = committedFiles.length === 1
debug(`Is valid committed files? ${isValidCommittedFiles}`)

if (isValidCommittedFiles) {
} else {
	// On invalid files, set the action as failed
	setFailed(
		'Pull request must commit just one file. ' +
			'Please, check the pull request. ' +
			'If you think this is an error, please contact an administrator.'
	)
}
