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


if __name__ == '__main__':
    app.run(debug=True)
