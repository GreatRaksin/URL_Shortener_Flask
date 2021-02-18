from flask import Flask, render_template, request, flash, redirect, url_for
from app import app


@app.route('/')
def hello_world():
    return render_template('base.html', title='Main Page')