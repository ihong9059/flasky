from flask import render_template, flash, redirect, url_for
from flask import session
from . import ctr
from flask_login import login_user, logout_user, login_required, \
    current_user
from .forms import NameForm

@ctr.route('/hks', methods=['GET', 'POST'])
@login_required
def testHks():
    form = NameForm()
    if form.validate_on_submit():
        form.name.data = form.name.data + ':new'
        session['name'] = form.name.data
        flash('submitted name:{}'.format(form.name.data))
        form.name.data = ''
        return redirect(url_for('ctr.testHks'))
    form.name.data =  session.get('name')   
    return render_template('ctr/indexCtr.html', form = form,
                           name = session.get('name'))
