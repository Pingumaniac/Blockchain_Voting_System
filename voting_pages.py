# Perhaps not needed

from flask import Flask, Blueprint, g, render_template, request, redirect, url_for, session, jsonify, flash, escape
from flask_bootstrap import Bootstrap
import pymysql
from simayiAPI.sqlAPI import DB

voting_pages = Blueprint("voting_pages", __name__, static_folder="static", template_folder="templates")

