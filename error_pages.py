from flask import Flask, Blueprint, g, render_template, request, redirect, url_for, session, jsonify, flash, escape
from flask_bootstrap import Bootstrap
import pymysql
from simayiAPI.sqlAPI import DB

error_pages = Blueprint("error_pages", __name__, static_folder="static", template_folder="templates")

@error_pages.route('/error/400', methods = ['GET'])
def page400():
    if request.method == 'GET':
        return render_template('/error/400.html', userName = g.userName), 400

@error_pages.route('/error/408', methods = ['GET'])
def page408():
    if request.method == 'GET':
        return render_template('/errror/408.html', userName = g.userName), 408

"""
HTTP status code 410 is given when the page for the corresponding URL has been deleted from the server(?),
but the data for this page is stored in the cache of the client's computer.
"""
@error_pages.route('/error/410', methods = ['GET'])
def page410():
    if request.method == 'GET':
        return render_template('/error/410.html', userName = g.userName), 410

@error_pages.route('/error/429', methods = ['GET'])
def page429():
    if request.method == 'GET':
        return render_template('/error/429.html', userName = g.userName), 429

@error_pages.route('/error/431', methods = ['GET'])
def page431():
    if request.method == 'GET':
        return render_template('/error/431.html', userName = g.userName), 431

@error_pages.route('/error/451', methods = ['GET'])
def page451():
    if request.method == 'GET':
        return render_template('/error/451.html', userName = g.userName), 451

@error_pages.route('/error/500', methods = ['GET'])
def page500():
    if request.method == 'GET':
        return render_template('/error/500.html', userName = g.userName), 500

@error_pages.route('/error/503', methods = ['GET'])
def page503():
    if request.method == 'GET':
        return render_template('/error/503.html', userName = g.userName), 503