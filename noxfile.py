import nox


# if you get errors about _sqlite3, you forgot to add sqlite-devel
# with your system package manager before compiling python with pyenv
@nox.session(python=["3.8", "3.12"])
def tests(session):
    session.run("poetry", "install", external=True)
    session.run("pytest", "--cov")
