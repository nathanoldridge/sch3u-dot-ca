SCH3U.ca, the website

application.py is a Flask app written in Python that
creates the interactive quiz website sch3u.ca



Troubleshooting 502 Bad Gateway

To deploy on Elastic Beanstalk, you must zip these files together
WITHOUT they are contained in.

The zip can not contain a folder, say "sch3u", which THEN contains
these files. "application.py" must be in the root of the ZIP.

If you do not follow this instruction, you are likely to get a
502 Bad Gateway response from the server once you have launched.

Troubleshooting 404 File Not Found

Flask apps require most content to be inside of specifically-named folders.
If style.css is in the ROOT folder, at the same level as application.py,
then the server will not be able to 'find' it despite how the URL is written
in the link. It, for example, MUST stay inside of /static

