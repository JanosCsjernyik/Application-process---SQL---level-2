MENTORS_AND_SCHOOL = "SELECT mentors.first_name, mentors.last_name, schools.name, schools.country \
                     FROM mentors LEFT JOIN schools ON mentors.city = schools.city \
                     ORDER BY mentors.id;"

ALL_SCHOOL_PAGE = "SELECT mentors.id, mentors.first_name, mentors.last_name, schools.name, schools.country \
                   FROM mentors RIGHT JOIN schools ON mentors.city = schools.city \
                   ORDER BY mentors.id"

MENTORS_BY_COUNTRY = "SELECT schools.country, COUNT(mentors.id) \
                     FROM mentors RIGHT JOIN schools ON mentors.city = schools.city \
                     GROUP BY schools.country;"

CONTACTS = "SELECT schools.name, mentors.first_name, mentors.last_name \
            FROM mentors INNER JOIN schools ON mentors.id = schools.contact_person;"

APPLICANTS = "SELECT applicants.first_name_applicant, applicants.application_code, applicants_mentors.creation_date \
             FROM applicants INNER JOIN applicants_mentors ON applicants.id = applicants_mentors.applicant_id \
             ORDER BY applicants_mentors.creation_date DESC LIMIT 5"

APPLICANTS_AND_MENTORS = "SELECT applicants.first_name_applicant, applicants.application_code, mentors.first_name, mentors.last_name \
                         FROM applicants \
                         LEFT JOIN applicants_mentors ON(applicants.id = applicants_mentors.applicant_id) \
                         LEFT JOIN mentors ON(applicants_mentors.mentor_id = mentors.id) \
                         ORDER BY applicants.id;"