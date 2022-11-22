from re import template
from tkinter import Button
from flask import Flask, render_template
app = Flask("__name__")

import routes, db