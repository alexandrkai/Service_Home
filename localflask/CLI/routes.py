import click
from flask import Blueprint

blueprint_cli = Blueprint('commands', __name__)


@blueprint_cli.cli.command("say_my_name")
@click.option('-name', default="Noname")
def say_my_name(name):
    print("say_my_name %s " % name)


# для вызова метода надо в командной строке написать
# flask commands create_db
@blueprint_cli.cli.command("create_db")
@click.option('-name', default="Noname")
def create_db(name):
    print("creating db %s " % name)
    # conn.drop_all()
    # conn.create_all()
    # conn.session.commit()


@blueprint_cli.cli.command("create-user")
@click.argument("name")
def create_user(name):
    print(name)
