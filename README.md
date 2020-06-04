# Student Management System

## This is a simple API for:
* creating a unified interface for keeping track of fcs students
* accounts for students to login and see their own pages
* admins can login and see everyone
* it will be able to use Github OAuth

## Schema

* User
  * email
  * password
  * groups: student, admin, or volunteer

* Profile
  * first_name
  * last_name
  * preferred_name
  * discord_name
  * github_username
  * codepen_username
  * fcc_profile_url
  * phone
  * timezone

* Volunteer
  * hours_available
  
* Attendance
  * date
  * student_id
  
* Project (labs)
  * name
  * details
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

* coming soon...

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

## Roadmap

### Version 2

* Students will be able to have public profiles with this information:
  * First Name
  * Last Name
  * Preferred Name
  * GitHub Username
  * Codepen Username
  * Certificates/Badges
