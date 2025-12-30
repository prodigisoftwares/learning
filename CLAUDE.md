This project makes use of Django, Tailwind, Vanilla Javascript for reactive elements, HTMX for ajax functionality.

We use test.sh to run unit tests.

This is a containerized development environment.

Django apps should always be created in BASE_DIR/apps

I run the migrations. So, just prompt me to do that when you create a model(s).

Always use django testcase in this project's unit tests.

When writing unit tests, do not test Django's or other 3rd party code's functionality. We only test our own code.

Instead of using the name of CHANGELOG.md to track changelogs, use a timestamp with date and hour minutes along with the issue number instead to the name of the file in the changelogs directory.

There should be no inline styles of CSS. Tailwind classes are preferred but if standard css is absolutely necessary, then it should reside in custom.css so it can be compiled with tailwind into styles.css.

With Django, class based views are preferred unless only one request type is needed.

We don't use cdn links for 3rd party assets, only static assets.

The root of the project is at: /home/harlin/Sandbox/certtests
The django project is at: /home/harlin/Sandbox/certtests/certtests
test.sh is at: /home/harlin/Sandbox/certtests/certtests
The venv is at: /home/harlin/Sandbox/certtests/.venv
Pre-commit config is in root folder.

All solutions should be elegant.

Ensure that you do not introduce linting errors as you write code.

There should be only changelog file per issue.

WE NEVER SHIP BROKEN CODE. EVER.
