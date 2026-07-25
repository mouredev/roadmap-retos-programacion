import simpleGit from "simple-git";
import { Octokit } from "@octokit/rest";
import { hideBin } from "yargs/helpers";
import yargs from "yargs/yargs";
import fs from "fs";
import path from "path";
import dotenv from "dotenv";

dotenv.config();

const TOKEN = process.env.GITHUB_TOKEN;

const git = simpleGit();
const octokit = new Octokit({ auth: TOKEN });

//GIT CLONE COMMAND
yargs(hideBin(process.argv))
  .command(
    "clone [repoUrl] [dir]",
    "Clone a repository",
    (yargs) => {
      yargs
        .positional("repoUrl", {
          describe: "URL of the repository to clone",
          type: "string",
          demandOption: true,
        })
        .positional("dir", {
          describe: "Directory to clone the repository into",
          type: "string",
          default: ".",
        });
    },
    async (argv) => {
      try {
        const destinationDir = path.resolve(argv.dir);
        const files = fs.readdirSync(destinationDir);

        if (destinationDir === process.cwd() && files.length > 0) {
          console.error("Error: Directory is not empty.");
          return;
        }

        console.log(`Cloning repository from ${argv.repoUrl} into ${argv.dir}`);
        await git.clone(argv.repoUrl, destinationDir);
        console.log(`Repository cloned into ${destinationDir}`);
      } catch (error) {
        console.error("Error cloning repository:", error.message);
      }
    }
  )
  // GIT ADD COMMAND
  .command(
    "add [files]",
    "Add files to the Git index (staging area)",
    (yargs) => {
      yargs.positional("files", {
        describe: "Files to add (use '.' to add all files)",
        type: "string",
        demandOption: true,
      });
    },
    async (argv) => {
      try {
        await git.add(argv.files);
        console.log(`Files added: ${argv.files}`);
      } catch (error) {
        console.error("Error adding files:", error.message);
      }
    }
  )
  // GIT COMMIT COMMAND
  .command(
    "commit [message]",
    "Commit changes with a message",
    (yargs) => {
      yargs.positional("message", {
        describe: "Commit message",
        type: "string",
        demandOption: true,
      });
    },
    async (argv) => {
      try {
        await git.commit(argv.message);
        console.log(`Changes committed with message: "${argv.message}"`);
      } catch (error) {
        console.error("Error committing changes:", error.message);
      }
    }
  )
  // GIT PUSH COMMAND
  .command(
    "push",
    "Push changes to a remote repository",
    () => {},
    async () => {
      try {
        await git.push("origin", "main");
        console.log("Changes pushed to a remote repository");
      } catch (error) {
        console.error("Error pushing changes:", error.message);
      }
    }
  )
  //GIT PULL COMMAND
  .command(
    "pull",
    "Pull changes from a remote repository",
    () => {},
    async () => {
      try {
        await git.pull("origin", "main");
        console.log("Changes pulled from a remote repository");
      } catch (error) {
        console.error("Error pulling changes:", error.message);
      }
    }
  )
  //GIT STATUS COMMAND
  .command(
    "status",
    "Show the status of the repository",
    () => {},
    async () => {
      try {
        const status = await git.status();
        console.log("Repository status:");
        console.log(status);
      } catch (error) {
        console.error("Error retrieving repository status:", error.message);
      }
    }
  )
  //GIT LOG COMMAND
  .command(
    "log",
    "Show commit history",
    () => {},
    async () => {
      try {
        const log = await git.log();
        console.log("Commit history:");
        console.log(log);
      } catch (error) {
        console.error("Error retrieving commit history:", error.message);
      }
    }
  )
  //CREATE REPO COMMAND
  .command(
    "create-repo [repoName]",
    "Create a new repository",
    (yargs) => {
      yargs.positional("repoName", {
        describe: "Name of the new repository",
        type: "string",
        demandOption: true,
      });
    },
    async (argv) => {
      try {
        const response = await octokit.repos.createForAuthenticatedUser({
          name: argv.repoName,
          private: false,
        });
        console.log(`Repository ${argv.repoName} created successfully`);
        console.log(`URL: ${response.data.html_url}`);
      } catch (error) {
        console.error("Error creating repository:", error.message);
      }
    }
  )
  //GIT CREATE BRANCH COMMAND
  .command(
    "create-branch [branchName]",
    "Create a new branch",
    (yargs) => {
      yargs.positional("branchName", {
        describe: "Name of the new branch",
        type: "string",
        demandOption: true,
      });
    },
    async (argv) => {
      try {
        await git.checkoutLocalBranch(argv.branchName);
        console.log(`Branch "${argv.branchName}" created successfully`);
      } catch (error) {
        console.error("Error creating branch:", error.message);
      }
    }
  )
  //GIT SWITCH BRANCH  COMMAND
  .command(
    "switch-branch [branchName]",
    "Switch to a branch",
    (yargs) => {
      yargs.positional("branchName", {
        describe: "Name of the branch to switch to",
        type: "string",
        demandOption: true,
      });
    },
    async (argv) => {
      try {
        await git.checkout(argv.branchName);
        console.log(`Switched to branch "${argv.branchName}".`);
      } catch (error) {
        console.error("Error switching branches:", error.message);
      }
    }
  )
  //GIT DELETE BRANCH COMMAND
  .command(
    "delete-branch",
    "Delete a branch",
    (yargs) => {
      yargs.positional("branchName", {
        describe: "Name of the branch to delete",
        type: "string",
        demandOption: true,
      });
    },
    async (argv) => {
      try {
        await git.deleteLocalBranch(argv.branchName);
        console.log(`Branch "${argv.branchName}" deleted successfully`);
      } catch (error) {
        console.error("Error deleting branch:", error.message);
      }
    }
  )
  //GIT SET REMOTE REPOSITORY COMMAND
  .command(
    "set-remote [name] [url]",
    "Set a remote repository",
    (yargs) => {
      yargs
        .positional("name", {
          describe: "Name of the remote (e.g., origin)",
          type: "string",
          demandOption: true,
        })
        .positional("url", {
          describe: "URL of the remote repository",
          type: "string",
          demandOption: true,
        });
    },
    async (argv) => {
      try {
        await git.addRemote(argv.name, argv.url);
        console.log(`Remote "${argv.name}" set to ${argv.url}`);
      } catch (error) {
        console.error("Error setting remote repository:", error.message);
      }
    }
  )
  //SET WORKING DIRECTORY COMMAND
  .command(
    "set-dir [directory]",
    "Set working directory for Git commands",
    (yargs) => {
      yargs.positional("directory", {
        describe: "Path to the directory",
        type: "string",
        demandOption: true,
      });
    },
    async (argv) => {
      try {
        const dir = path.resolve(argv.directory);
        if (!fs.existsSync(dir)) {
          console.error("The specified directory does not exist.");
          return;
        }

        git.cwd(dir);
        console.log(`Working diretory set to: ${dir}`);
      } catch (error) {
        console.error("Error setting working directory");
      }
    }
  )
  //EXIT FROM CLI COMMAND
  .command(
    "exit",
    "Exit the CLI",
    () => {},
    () => {
      console.log("Exiting the CLI, Goodbye!");
      process.exit(0);
    }
  )
  .help().argv;
