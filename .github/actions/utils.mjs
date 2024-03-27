import fs from 'node:fs'
import path from 'node:path'

export const wrapperChallengesFolder = 'Roadmap'
export const excludeExtensions = ['.md', '.json']
export const roadmapPath = path.resolve(wrapperChallengesFolder)

// Helpers
/**
 * Converts an array of strings to a string with specified separators.
 * @param {Object} options - The options object.
 * @param {string[]} options.array - The array of strings to convert.
 * @param {string} options.finalSeparator - The separator to use before the last element.
 * @param {string} options.separator - The separator to use between elements.
 * @returns {string} The converted string.
 */
export function arraytoString({ array, finalSeparator, separator }) {
	const lastElementI = array.length - 1

	const stringifiedArray = array.reduce((prev, current, index) => {
		const currentFmt = `'${current}'`

		if (index === 0) return currentFmt
		if (index === lastElementI) return prev + finalSeparator + currentFmt
		return prev + separator + currentFmt
	}, array[0])

	return stringifiedArray
}

// Challenges data
export function getChallengeFolders() {
	const roadmapContent = fs.readdirSync(roadmapPath, { withFileTypes: true })
	const challengeFolders = roadmapContent.filter((dirent) => dirent.isDirectory())
	return challengeFolders.map((folder) => folder.name)
}

/**
 * Retrieves the folder name of the given challenge.
 * @param {string} challenge - The challenge number.
 * @returns {string | 'null'} - The folder name of the challenge, or 'null' if not found.
 */
export function getChallengeFolder(challenge) {
	const challengeFolders = getChallengeFolders()
	const challengeFolder = challengeFolders.find((folder) => folder.slice(0, 2) === challenge)
	return challengeFolder ?? 'null'
}

export function getChallengeNumbers() {
	const challengeFolders = getChallengeFolders()
	const challengeNumbers = challengeFolders.map((folder) => folder.slice(0, 2))
	return challengeNumbers
}

// Programming languages data
/**
 * Retrieves the file extension associated with a given programming language.
 *
 * @param {string} languageName - The name of the programming language.
 * @returns {string} - The file extension associated with the programming language, or 'null' if not found.
 */
export function getProgrammingLanguageExtension(languageName) {
	const challengeFolders = getChallengeFolders()
	const languagePaths = challengeFolders.map((folder) => path.resolve(roadmapPath, folder, languageName))
	const files = languagePaths.map((path) => (fs.existsSync(path) ? fs.readdirSync(path)[0] : ''))
	const filesFiltered = files.filter((file) => file !== '' && !excludeExtensions.includes(path.extname(file)))
	return filesFiltered.length > 0 ? path.extname(filesFiltered[0]) : 'null'
}

export function getProgrammingLanguageExtensions() {
	const roadmapContentDeep = fs.readdirSync(roadmapPath, { recursive: true, withFileTypes: true })
	const files = roadmapContentDeep.filter((file) => file.isFile())
	const fileExtensions = files.map((file) => path.extname(file.name))
	const fileExtensionsFiltered = fileExtensions.filter((extension) => !excludeExtensions.includes(extension))
	return [...new Set(fileExtensionsFiltered).values()]
}

/**
 * Retrieves the folder name of the programming language based on the file extension.
 * @param {string} extension - The file extension to search for.
 * @returns {string} - The folder name of the programming language, or 'null' if not found.
 */
export function getProgrammingLanguageFolderName(extension) {
	const challengesFolders = getChallengeFolders()
	const foldersToSeek = challengesFolders.map((folder) => path.resolve(roadmapPath, folder))
	const foldersContent = foldersToSeek.map((folder) => fs.readdirSync(folder, { recursive: true })).flat()
	const folderName = foldersContent.find((folder) => path.extname(folder.toString()) === extension)
	return folderName?.toString().split(path.sep)[0] ?? 'null'
}

export function getProgrammingLanguageFolderNames() {
	const challengesFolders = getChallengeFolders()
	const foldersToSeek = challengesFolders.map((folder) => path.resolve(roadmapPath, folder))
	const foldersContent = foldersToSeek.map((folder) => fs.readdirSync(folder, { withFileTypes: true })).flat()
	const folderNames = foldersContent.filter((folder) => folder.isDirectory()).map((folder) => folder.name)
	return [...new Set(folderNames).values()]
}
