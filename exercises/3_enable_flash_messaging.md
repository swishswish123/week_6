# Enable flash messaging

Flask provides a way to pass messages from one request to the next (and only the next) using [message flashing](https://flask.palletsprojects.com/en/1.1.x/quickstart/#message-flashing).

This can be useful for highlighting errors to the user.

## Enable message flashing in the base template

Since we may want to do this for any page in our application let's enable this in the `base.html` template.

Add the following to the base jinja template above the main content:

```jinja2
{# Displays flashed messages on a page #}
{% with messages = get_flashed_messages() %}
    {% if messages %}
        <ul>
        {% for message in messages %}
            <li>{{ message }}</li>
        {% endfor %}
        </ul>
    {% endif %}
{% endwith %}
```

Change the auth.signup route to flash a message and then redirect to the main.index to see this in action:

```python
from flask import Blueprint, render_template, flash, redirect, url_for

from my_app.auth.forms import SignupForm

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        name = form.first_name.data
        flash(f"Hello, {name}. You are signed up.")
        return redirect(url_for('main.index'))
    return render_template('signup.html', title='Sign Up', form=form)
```

## Add message flashing to a specific page

Currently the signup form returns if it doesn’t pass the validation, however we don’t give any feedback to the user.

We can access the validation errors of our form object using form.errors. 

Add the following to signup.html.

```jinja2
{# Display the form validation errors #}
    {% for field, errors in form.errors.items() %}
        <div class="alert alert-error">
            {{ form[field].label }}: {{ ', '.join(errors) }}
        </div>
    {% endfor %}
```

##Challenge

Improve the formatting by adding the error messages next to the input box on the form rather than a list at the top of the page.

Hint: Consider writing a Jinja2 template macro `_formhelpers.html` to generate forms and add styling. Read the [documentation here](https://flask.palletsprojects.com/en/1.1.x/patterns/wtforms/#forms-in-templates) which contains the necessary code.