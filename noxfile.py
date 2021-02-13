import nox

locations = "logview", "tests", "noxfile.py"


@nox.session
def tests(session):
    session.install("pytest-cov")
    session.run("pytest", "--cov-report", "term-missing", "--cov=logview", "tests/")


@nox.session
def lint(session):
    args = session.posargs or locations
    session.install("flake8")
    session.run("flake8", *args)


@nox.session
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)
