MENTORS_AND_SCHOOL = "SELECT mentors.first_name, mentors.last_name, schools.name, schools.country \
                     FROM mentors LEFT JOIN schools ON mentors.city = schools.city \
                     ORDER BY mentors.id;"

ALL_SCHOOL_PAGE = "SELECT mentors.id, mentors.first_name, mentors.last_name, schools.name, schools.country \
                    FROM mentors RIGHT JOIN schools ON mentors.city = schools.city \
                    ORDER BY mentors.id"

MENTORS_BY_COUNTRY = "SELECT schools.country, COUNT(mentors.id) \
                     FROM mentors RIGHT JOIN schools ON mentors.city = schools.city \
                     GROUP BY schools.country;"
