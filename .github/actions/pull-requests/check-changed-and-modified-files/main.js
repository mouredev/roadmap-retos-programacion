const core = require('@actions/core')

// Required data
const changedAndModifiedFiles = core.getInput('changed-and-modified-files').split(' ')
core.debug(`Changed and modified files: ${changedAndModifiedFiles}`)

// Check if changed and modified files are valid
const isValidFiles = changedAndModifiedFiles.length === 1

if (isValidFiles) {
	// On valid files, set the output
	core.setOutput('changed-or-modified-file', changedAndModifiedFiles[0])
} else {
	// On invalid files, set the action as failed
	core.setFailed(
		'Pull request must change or modified exactly one file. ' +
			'Please, check the pull request and try again. ' +
			'If you think this is an error, please contact an administrator.'
	)
}
