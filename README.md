# Student Management System

## This is a simple API for:
* creating a unified interface for keeping track of fcs students
* accounts for students to login and see their own pages
* admins can login and see everyone via the Django admin interface
* it will be able to use Github OAuth

## Table of Contents

* [Requirements](#requirements)
* [Schema](#schema)
* [API](#api)
* [Roadmap](#roadmap)

## Requirements

* Students and Organizers/Admin accounts login using GitHub OAUTH
* Private Student Profile: Visible to only the user and organizers/admins
  * FreeCodeCamp.org progress page url: freecodecamp.org/codecafecentral
  * Email
  * Discord Name
  * Phone
  * Attendenance (not editable by students)
  * List of labs:
    * Link to the lab starter
    * input field for a link to their completed version

* Admin Dashboard
  * Student Progress/Outcomes
    * Grouped by enrollment period (semester)
      * Show all students in a table to track progress/outcomes
      * Be able to edit any part of the table
      * Similar to: https://docs.google.com/spreadsheets/d/1M2rAQSHNFqZlhAV0i1fKfVLBpx4CqRMUzowoGWS_KKQ/edit#gid=0
  * Volunteer management
    * Be able to view volunteers listed in a table
  * Waitlist
    * Table of all those on the waitlist

## Schema

* User
  * email
  * password
  * groups: student, admin, or volunteer (can only belong to one)

* StudentProfile
  * first_name
  * last_name
  * preferred_name
  * discord_name
  * github_username
  * codepen_username
  * fcc_profile_url
  * current_level
  * phone
  * timezone

* Volunteer
  * first_name
  * last_name
  * email
  * hours_available
  
* VolunteerHours
  * volunteer_id
  * day: CharField with choices -> mon, tue, wed, thu, fri, sat, sun
  * begin_hour: models.PositiveSmallIntegerField(validators=[MaxValueValidator(24)])
  * end_hour: models.PositiveSmallIntegerField(validators=[MaxValueValidator(24)])
  
* Lecture
  * date
  * title
  * description
  * slides_url
  
* Attendance
  * lecture_id
  * student_id
  
* Project (labs)
  * title
  * description
  * url

* StudentSubmission
  * student_id
  * project_id
  * url
  
* StudentCertificate 
  * student_id
  * certificate_id
  
* Certificate
  * name
  * description

* Waitlist
  * first_name
  * last_name
  * email
  * notes

## API

**Prefix:** /api/v1

**/students**

* get (temporary, only for testing)
* post

**/students/:id**

* get
* patch
* delete

**/students/:id/certificates**

* get

**/certificates**

* get

## Roadmap

### Version 2

* Students will be able to have public profiles with this information:
  * First Name
  * Last Name
  * Preferred Name
  * GitHub Username
  * Codepen Username
  * Certificates/Badges
  
* Area where volunteers can view their own information and update their hours
