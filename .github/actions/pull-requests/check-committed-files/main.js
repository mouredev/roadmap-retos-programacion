const core = require('@actions/core')

// Inputs
const committedFiles = core.getInput('committed-files').split('\\n')
core.debug(`'committed-files' (input): ${committedFiles}`)

// Check if changed and modified files are valid
const isValidCommittedFiles = committedFiles.length === 1
core.debug(`Is valid committed files? ${isValidCommittedFiles}`)

if (isValidCommittedFiles) {
	// On valid files, set the output
	const committedFile = committedFiles[0]
	core.debug(`'committed-file' (output): ${committedFile}`)

	core.setOutput('committed-file', committedFile)
} else {
	// On invalid files, set the action as failed
	core.setFailed(
		'Pull request must commit just one file. ' +
			'Please, check the pull request. ' +
			'If you think this is an error, please contact an administrator.'
	)
}
