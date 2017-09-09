from flask import Flask, render_template, redirect, url_for, request
import database_handlre
import queries

app = Flask(__name__)


@app.route('/')
def route_index():
    return render_template('list.html')


@app.route('/mentors')
def route_mentors():
    query = database_handlre.query_select(queries.MENTORS_AND_SCHOOL)
    return render_template('mentors.html', query=query)


@app.route('/all-school')
def route_all_school():
    query = database_handlre.query_select(queries.ALL_SCHOOL_PAGE)
    return render_template('all-school.html', query=query)


@app.route('/mentors-by-country')
def route_mentors_by_country():
    query = database_handlre.query_select(queries.MENTORS_BY_COUNTRY)
    return render_template('mentors-by-country.html', query=query)


@app.route('/contacts')
def route_contacts():
    query = database_handlre.query_select(queries.CONTACTS)
    return render_template('contacts.html', query=query)


@app.route('/applicants')
def route_applicants():
    query = database_handlre.query_select(queries.APPLICANTS)
    return render_template('applicants.html', query=query)


@app.route('/applicants-and-mentors')
def route_applicants_and_mentors():
    query = database_handlre.query_select(queries.APPLICANTS_AND_MENTORS)
    print(query)
    return render_template('applicants-and-mentors.html', query=query)


if __name__ == '__main__':
    app.run(debug=True)
