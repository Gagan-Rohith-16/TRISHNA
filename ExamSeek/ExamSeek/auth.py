from flask import flash, redirect, url_for, session
from flask_login import current_user, login_user, logout_user
from functools import wraps

def redirect_if_authenticated(f):
    """Decorator to redirect users to home page if they're already authenticated"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect(url_for('home'))
        return f(*args, **kwargs)
    return decorated_function

def ensure_csrf(form_name):
    """Decorator to ensure CSRF protection for a form"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # Check if the CSRF token is valid
            form = globals()[form_name]()
            if form.validate_on_submit():
                return f(*args, **kwargs)
            else:
                flash('Form validation failed. Please try again.', 'danger')
                return redirect(url_for('home'))
        return decorated_function
    return decorator
