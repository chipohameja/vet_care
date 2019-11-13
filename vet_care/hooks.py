# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "vet_care"
app_title = "Vet Care"
app_publisher = "9T9IT"
app_description = "ERPNext App for Vet Care"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@9t9it.com"
app_license = "MIT"

fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [
                    "Patient Appointment-vc_owner"
                ]
            ]
        ]
    }
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/vet_care/css/vet_care.css"
# app_include_js = "/assets/vet_care/js/vet_care.js"

# include js, css files in header of web template
# web_include_css = "/assets/vet_care/css/vet_care.css"
# web_include_js = "/assets/vet_care/js/vet_care.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "vet_care.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "vet_care.install.before_install"
# after_install = "vet_care.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "vet_care.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Patient Appointment": {
        "validate": "vet_care.doc_events.patient_appointment.validate"
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"vet_care.tasks.all"
# 	],
# 	"daily": [
# 		"vet_care.tasks.daily"
# 	],
# 	"hourly": [
# 		"vet_care.tasks.hourly"
# 	],
# 	"weekly": [
# 		"vet_care.tasks.weekly"
# 	]
# 	"monthly": [
# 		"vet_care.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "vet_care.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "vet_care.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "vet_care.task.get_dashboard_data"
# }
