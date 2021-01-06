import nox


@nox.session
def tests(session):
    session.install("pytest-cov")
    session.run("pytest", "--cov=logview", "tests/")