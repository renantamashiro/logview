import nox


@nox.session
def tests(session):
    session.install("pytest-cov")
    session.run("pytest", "--cov-report", "term-missing", "--cov=logview", "tests/")