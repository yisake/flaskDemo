from flask import Blueprint
admin=Blueprint('admin' ,__name__)

@admin.route('/')
def index():
    return 'admin index'

@admin.route('/logout')
def logout():
    return 'admin log out'