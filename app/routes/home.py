from flask import Blueprint

bp = Blueprint("home", __name__)


@bp.route("/")
def index():
    # return simple text for now
    return "Welcome to BrainSnap!"
