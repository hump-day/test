

### ISort: automatic import sorting

This second tool will sort your imports according to the [PEP8](https://www.python.org/dev/peps/pep-0008/#imports). That's it! One less thing for you to do!

It is run by calling `isort .` in the project root. Notice the dot at the end, it tells ISort to use the current directory.

### Pre-commit: run linting before committing

This third tool doesn't check your code, but rather makes sure that you actually *do* check it.

It makes use of a feature called [Git hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) which allow you to run a piece of code before running `git commit`.
The good thing about it is that it will cancel your commit if the lint doesn't pass. You won't have to wait for Github Actions to report and have a second fix commit.

It is *installed* by running `pre-commit install` and can be run manually by calling only `pre-commit`.

[Lint before you push!](https://soundcloud.com/lemonsaurusrex/lint-before-you-push)

#### Hooks List:

- `check-toml`: Lints and corrects your TOML files.
- `check-yaml`: Lints and corrects your YAML files.
- `end-of-file-fixer`: Makes sure you always have an empty line at the end of your file.
- `trailing-whitespaces`: Removes whitespaces at the end of each line.
- `python-check-blanket-noqa`: Forbids you from using noqas on large pieces of code.
- `isort`: Runs ISort.
- `flake8`: Runs flake8.

## How do I use it?

### Creating your Team Repository

One person in the team, preferably the leader, will have to create the repository and add other members as collaborators.

1. In the top right corner of your screen, where **Clone** usually is, you have a **Use this template** button to click.

![](https://docs.github.com/assets/images/help/repository/use-this-template-button.png)

2. Give the repository a name and a description.

![](https://docs.github.com/assets/images/help/repository/create-repository-name.png)

3. Click **Create repository from template**.

4. Click **Settings** in your newly created repository.

![](https://docs.github.com/assets/images/help/repository/repo-actions-settings.png)

5. Select **Manage access**.

<!-- Yes, this is inline html. The source image is too vertical to be displayed with 100% width. -->
<img src="https://docs.github.com/assets/images/help/repository/manage-access-tab.png" style="width: 30%"></img>

6. Click **Invite a collaborator**.

![](https://docs.github.com/assets/images/help/repository/invite-a-collaborator-button.png)

7. Insert the names of each of your teammates, and invite them. Once they have accepted the invitation in their email, they will have write access to the repository.

You are now ready to go! Now sit down, relax, and wait for the kickstart!
Don't forget to swap "Python Discord" in the `LICENSE` file for the name of each of your team members or the name of your team after the start of the jam.

### Using the Default Pip Setup

Our default setup includes a bare requirement file to be used with a [virtual environment](https://docs.python.org/3/library/venv.html).

We recommend this if you never have used any other dependency manager, although if you have, feel free to switch to it. More on that below.

#### Creating the environment
Create a virtual environment in the folder `.venv`.
```shell
$ python -m venv .venv
```

#### Enter the environment
It will change based on your operating system and shell.
```shell
# Linux, Bash
$ source .venv/bin/activate
# Linux, Fish
$ source .venv/bin/activate.fish
# Linux, Csh
$ source .venv/bin/activate.csh
# Linux, PowerShell Core
$ .venv/bin/Activate.ps1
# Windows, cmd.exe
> .venv\Scripts\activate.bat
# Windows, PowerShell
> .venv\Scripts\Activate.ps1
```

#### Installing the Dependencies
Once the environment is created and activated, use this command to install the development dependencies.
```shell
$ pip install -r dev-requirements.txt
```

#### Exiting the environment
Interestingly enough, it is the same for every platform
```shell
$ deactivate
```

Once the environment is activated, all the commands listed previously should work. We highly recommend that you run `pre-commit install` as soon as possible.

## How do I adapt it to my project?

If you wish to use Pipenv or Poetry, you will have to move the dependencies in `dev-requirements.txt` to the development dependencies of your tool.

We've included a porting of `dev-requirements.txt` to both [poetry](./samples/pyproject.toml) and [pipenv](./samples/Pipfile) in the [samples folder](./samples).
If you use the poetry setup, make sure to change the project name, description, and authors at the top of the file.

When installing new dependencies, don't forget to [pin them](https://pip.pypa.io/en/stable/user_guide/#pinned-version-numbers) by adding a version tag at the end.
For example, if I wish to install `Click`, a quick look at [PyPI](https://pypi.org/project/click/) tells me that 8.0.1 is the latest version.
I will then add `click ~= 8.0`, without the last number, to my dependency manager.

A code jam project is left unmaintained after the end of the event. If the dependencies aren't pinned, the project will break after the first major change in an API.

## Final words

Don't forget to replace this README with an actual description of your project! Images are also welcome!

We hope this template will be helpful. Good luck in the jam!
