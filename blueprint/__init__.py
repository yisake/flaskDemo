from flask import Blueprint
admin=Blueprint('admin' ,__name__)

@admin.route('/')
def index():
    return 'index'

@admin.route('/logout')
def logout():
    return 'log out'