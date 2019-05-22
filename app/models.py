from . import db


class GitRepository(db.Model):
    """Represents a single Git repository and its metadata. Each commit
    stored separately.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    remote_git_url = db.Column(db.String(2048))
    commit  = db.relationship("GitCommit", backref="repository",
                              lazy="dynamic")


class GitCommit(db.Model):
    """A single Git commit and its metadata."""
    id = db.Column(db.Integer, primary_key=True)
    repository  = db.Integer, db.ForeignKey("gitRepository.id")
