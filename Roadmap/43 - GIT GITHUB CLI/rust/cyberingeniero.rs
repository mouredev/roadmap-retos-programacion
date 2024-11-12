/*
_____________________________________
https://github.com/cyberingeniero
octubre 2024 - Rust
_____________________________________
43 GIT GITHUB CLI
_____________________________________
* Desarrolla un CLI (Command Line Interface) que permita
* interactuar con Git y GitHub de manera real desde terminal.
*
* El programa debe permitir las siguientes opciones:
* 1. Establecer el directorio de trabajo
* 2. Crear un nuevo repositorio
* 3. Crear una nueva rama
* 4. Cambiar de rama
* 5. Mostrar ficheros pendientes de hacer commit
* 6. Hacer commit (junto con un add de todos los ficheros)
* 7. Mostrar el historial de commits
* 8. Eliminar rama
* 9. Establecer repositorio remoto
* 10. Hacer pull
* 11. Hacer push
* 12. Salir
*/

// [dependencies]
// clap = "4.0"
// git2 = "0.19"
// colored = "2.0"

// src/modules/git_commands.rs

// use colored::*;
// use git2::{BranchType, FetchOptions, PushOptions, RemoteCallbacks, Repository, Sort};
// use std::io::{self};
// use std::path::Path;
// use std::{env, fs};

// pub fn set_directory() {
//     println!(
//         "{}",
//         "Please enter the path to set the working directory:"
//             .blue()
//             .bold()
//     );

//     let mut input = String::new();
//     std::io::stdin()
//         .read_line(&mut input)
//         .expect("Failed to read input");

//     let path = input.trim();
//     if env::set_current_dir(Path::new(path)).is_ok() {
//         println!("{}", format!("Changed directory to: {}", path).green());
//     } else {
//         println!(
//             "{}",
//             "Failed to change directory. Please check the path.".red()
//         );
//     }
// }

// pub fn create_new_repo() {
//     let repo = Repository::init(".");
//     match repo {
//         Ok(_) => println!(
//             "{}",
//             "Initialized new repository in the current directory."
//                 .green()
//                 .bold()
//         ),
//         Err(e) => println!(
//             "{}",
//             format!("Failed to initialize repository: {}", e).red()
//         ),
//     }
// }

// pub fn create_new_branch() {
//     let repo = Repository::open(".").expect("Not a git repository");

//     println!("{}", "Enter the name of the new branch:".blue().bold());
//     let mut branch_name = String::new();
//     std::io::stdin()
//         .read_line(&mut branch_name)
//         .expect("Failed to read input");

//     let branch_name = branch_name.trim();
//     let head = repo.head().unwrap();
//     let target = head.target().unwrap();
//     let commit = repo.find_commit(target).unwrap();
//     let _branch_result = repo.branch(branch_name, &commit, false);

//     match _branch_result {
//         Ok(_) => println!(
//             "{}",
//             format!("Branch '{}' created successfully.", branch_name).green()
//         ),
//         Err(e) => println!("{}", format!("Failed to create branch: {}", e).red()),
//     }
// }

// pub fn switch_branch() {
//     let repo = Repository::open(".").expect("Not a git repository");

//     println!(
//         "{}",
//         "Enter the name of the branch to switch to:".blue().bold()
//     );
//     let mut branch_name = String::new();
//     std::io::stdin()
//         .read_line(&mut branch_name)
//         .expect("Failed to read input");
//     let branch_name = branch_name.trim();

//     match repo.set_head(&format!("refs/heads/{}", branch_name)) {
//         Ok(_) => println!(
//             "{}",
//             format!("Switched to branch '{}'.", branch_name).green()
//         ),
//         Err(e) => println!("{}", format!("Failed to switch branches: {}", e).red()),
//     }
// }

// pub fn git_status() {
//     let repo = Repository::open(".").expect("Not a git repository");
//     let mut status_options = git2::StatusOptions::new();
//     status_options.include_untracked(true);

//     let statuses = repo.statuses(Some(&mut status_options)).unwrap();
//     if statuses.is_empty() {
//         println!("{}", "No files to commit.".yellow());
//     } else {
//         for entry in statuses.iter() {
//             let status = entry.status();
//             let path = entry.path().unwrap();
//             if status.contains(git2::Status::INDEX_NEW) || status.contains(git2::Status::WT_NEW) {
//                 println!("{}", format!("New file: {}", path).cyan());
//             } else if status.contains(git2::Status::INDEX_MODIFIED)
//                 || status.contains(git2::Status::WT_MODIFIED)
//             {
//                 println!("{}", format!("Modified file: {}", path).magenta());
//             }
//         }
//     }
// }

// pub fn commit_changes() {
//     let repo = match Repository::open(".") {
//         Ok(repo) => repo,
//         Err(e) => {
//             println!("Failed to open the repository: {}", e);
//             return;
//         }
//     };

//     let mut index = match repo.index() {
//         Ok(index) => index,
//         Err(e) => {
//             println!("Failed to get index: {}", e);
//             return;
//         }
//     };

//     // Agregar todos los archivos al índice
//     if let Err(e) = index.add_all(["*"].iter(), git2::IndexAddOption::DEFAULT, None) {
//         println!("Failed to add files to index: {}", e);
//         return;
//     }

//     if let Err(e) = index.write() {
//         println!("Failed to write index: {}", e);
//         return;
//     }

//     let oid = match index.write_tree() {
//         Ok(oid) => oid,
//         Err(e) => {
//             println!("Failed to write tree: {}", e);
//             return;
//         }
//     };

//     let signature = match repo.signature() {
//         Ok(sig) => sig,
//         Err(e) => {
//             println!("Failed to get signature: {}", e);
//             return;
//         }
//     };

//     // Verificar si el repositorio tiene commits previos o es un primer commit (unborn branch)
//     let parent_commit = match repo.head() {
//         Ok(head) => match head.peel_to_commit() {
//             Ok(commit) => Some(commit),
//             Err(e) => {
//                 println!("Failed to get parent commit: {}", e);
//                 return;
//             }
//         },
//         Err(_e) => {
//             // No hay HEAD, por lo que estamos en el primer commit
//             None
//         }
//     };

//     let tree = match repo.find_tree(oid) {
//         Ok(tree) => tree,
//         Err(e) => {
//             println!("Failed to find tree: {}", e);
//             return;
//         }
//     };

//     println!("Enter a commit message:");
//     let mut message = String::new();
//     if let Err(e) = io::stdin().read_line(&mut message) {
//         println!("Failed to read input: {}", e);
//         return;
//     }

//     let message = message.trim();
//     if message.is_empty() {
//         println!("Commit message cannot be empty.");
//         return;
//     }

//     // Crear el commit: si no hay `parent_commit`, es el primer commit.
//     let commit_result = if let Some(parent) = parent_commit {
//         repo.commit(
//             Some("HEAD"),
//             &signature,
//             &signature,
//             message,
//             &tree,
//             &[&parent],
//         )
//     } else {
//         // Primer commit, no hay padres
//         repo.commit(Some("HEAD"), &signature, &signature, message, &tree, &[])
//     };

//     match commit_result {
//         Ok(_) => println!("Commit successful with message: {}", message),
//         Err(e) => println!("Failed to create commit: {}", e),
//     }
// }

// pub fn git_log() {
//     let repo = Repository::open(".").expect("Not a git repository");

//     let mut revwalk = repo.revwalk().unwrap();
//     revwalk.push_head().unwrap();
//     revwalk.set_sorting(Sort::TIME).unwrap();

//     for id in revwalk {
//         let commit = repo.find_commit(id.unwrap()).unwrap();
//         println!(
//             "{}: {}\n{}: {}\n{}: {}\n",
//             "Commit".bold().blue(),
//             commit.id(),
//             "Author".bold().yellow(),
//             commit.author(),
//             "Message".bold().green(),
//             commit.message().unwrap_or("No message")
//         );
//     }
// }

// pub fn delete_branch() {
//     let repo = Repository::open(".").expect("Not a git repository");

//     println!(
//         "{}",
//         "Enter the name of the branch to delete:".blue().bold()
//     );
//     let mut branch_name = String::new();
//     std::io::stdin()
//         .read_line(&mut branch_name)
//         .expect("Failed to read input");
//     let branch_name = branch_name.trim();

//     let find_result = repo.find_branch(branch_name, BranchType::Local);

//     match find_result {
//         Ok(mut branch) => {
//             branch.delete().expect("Failed to delete branch");
//             println!(
//                 "{}",
//                 format!("Branch '{}' deleted successfully.", branch_name).green()
//             );
//         }
//         Err(_) => println!("{}", format!("Branch '{}' not found.", branch_name).red()),
//     }
// }

// pub fn set_remote() {
//     let repo = Repository::open(".").expect("Not a git repository");

//     println!(
//         "{}",
//         "Enter the remote name (e.g., 'origin'):".blue().bold()
//     );
//     let mut remote_name = String::new();
//     std::io::stdin()
//         .read_line(&mut remote_name)
//         .expect("Failed to read input");
//     let remote_name = remote_name.trim();

//     println!(
//         "{}",
//         "Enter the remote URL (e.g., 'https://github.com/user/repo.git'):"
//             .blue()
//             .bold()
//     );
//     let mut remote_url = String::new();
//     std::io::stdin()
//         .read_line(&mut remote_url)
//         .expect("Failed to read input");
//     let remote_url = remote_url.trim();

//     let remote_result = repo.remote(remote_name, remote_url);

//     match remote_result {
//         Ok(_) => println!(
//             "{}",
//             format!("Remote '{}' set to URL '{}'.", remote_name, remote_url).green()
//         ),
//         Err(e) => println!("{}", format!("Failed to set remote: {}", e).red()),
//     }
// }

// pub fn git_pull() {
//     let repo = Repository::open(".").expect("Not a git repository");
//     let mut remote = repo
//         .find_remote("origin")
//         .expect("No 'origin' remote found");

//     let mut callbacks = RemoteCallbacks::new();
//     callbacks.credentials(|_url, _username_from_url, _allowed_types| {
//         git2::Cred::ssh_key(
//             "git",
//             None,
//             std::path::Path::new(&format!("{}/.ssh/id_rsa", std::env::var("HOME").unwrap())),
//             None,
//         )
//     });

//     let mut fetch_options = FetchOptions::new();
//     fetch_options.remote_callbacks(callbacks);

//     remote
//         .fetch(
//             &["refs/heads/main:refs/heads/main"],
//             Some(&mut fetch_options),
//             None,
//         )
//         .unwrap();
//     println!("{}", "Pull successful".green());
// }

// pub fn git_push() {
//     let repo = Repository::open(".").expect("Not a git repository");
//     let mut remote = repo
//         .find_remote("origin")
//         .expect("No 'origin' remote found");

//     let mut callbacks = RemoteCallbacks::new();
//     callbacks.credentials(|_url, _username_from_url, _allowed_types| {
//         git2::Cred::ssh_key(
//             "git",
//             None,
//             std::path::Path::new(&format!("{}/.ssh/id_rsa", std::env::var("HOME").unwrap())),
//             None,
//         )
//     });

//     let mut push_options = PushOptions::new();
//     push_options.remote_callbacks(callbacks);

//     remote
//         .push(&["refs/heads/main"], Some(&mut push_options))
//         .unwrap();
//     println!("{}", "Push successful".green());
// }

// pub fn show_repo_path() {
//     match Repository::discover(".") {
//         Ok(repo) => {
//             let repo_path = repo.path();
//             println!("Repository path: {}", repo_path.display());
//         }
//         Err(e) => {
//             println!("Not a git repository: {}", e);
//         }
//     }
// }

// pub fn delete_repo() {
//     let repo_path = ".git";

//     if Path::new(repo_path).exists() {
//         match fs::remove_dir_all(repo_path) {
//             Ok(_) => println!("Repository deleted successfully."),
//             Err(e) => println!("Failed to delete repository: {}", e),
//         }
//     } else {
//         println!("No git repository found in this directory.");
//     }
// }

// src/main.rs
use clap::{Arg, Command};

mod modules {
    pub mod git_commands;
}

use modules::git_commands;

fn main() {
    let matches = Command::new("GitHub CLI")
        .version("1.0")
        .about("Interacts with Git and GitHub")
        .arg(Arg::new("option").required(true).index(1))
        .get_matches();

    let option = matches.get_one::<String>("option").unwrap();

    match option.as_str() {
        "set-dir" => git_commands::set_directory(),
        "new-repo" => git_commands::create_new_repo(),
        "new-branch" => git_commands::create_new_branch(),
        "switch-branch" => git_commands::switch_branch(),
        "status" => git_commands::git_status(),
        "commit" => git_commands::commit_changes(),
        "log" => git_commands::git_log(),
        "delete-branch" => git_commands::delete_branch(),
        "set-remote" => git_commands::set_remote(),
        "pull" => git_commands::git_pull(),
        "push" => git_commands::git_push(),
        "exit" => println!("Exiting..."),
        "show-repo-path" => git_commands::show_repo_path(),
        "delete-repo" => git_commands::delete_repo(),
        _ => println!("Invalid option!"),
    }
}
