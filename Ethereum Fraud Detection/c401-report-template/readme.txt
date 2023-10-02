------------------------------------
SCMS M.Tech. Project Report Template
------------------------------------

Use the standardized LaTeX template in this directory/tarball for writing your SCMS M.Tech. internship project report.
The template is defined by two files, namely,

 sipr.tex
 sbk.cls

These are included with each of the example report provided in this directory/tarball.

Note
 -- Please do not modify or tamper with these files.
 -- Mandatory parts of the main LaTeX source file (report.tex in the example report) have been clearly marked.

--------------
Example Report
--------------

 example-report/ (courtesy Suraj Meghwani CMS1002)

See the LaTeX source files and compiled .pdf files for these examples.
Study the structure of the report.tex file.

-----------------------
Processing instructions
-----------------------

If there are no LaTeX errors in your source, the following
sequence of shell commands produces the file report.pdf:

$ cd example-report/
$ pdflatex report
$ bibtex report
$ pdflatex report
$ pdflatex report

Occasionally, pdflatex may need to be invoked once again.

In your own report, you may have to correct syntactic and other errors at each of these steps.
Once your LaTeX sources are bug-free, easy compilation to pdf can be done via the makefile
provided in each directory. It can be invoked as

$ make

from the linux command line from inside example-report/.

----------
LaTeX Help
----------

The internet is replete with help and tutorials on LaTeX. Many GUIs are also available for LaTeX.
An online GUI is available at https://overleaf.com/.
For any additional help you may require, please talk to your friends, foes, faculty advisor, and
other local LaTeX experts.

----------
Spellcheck
----------

In the least, run
$ aspell -c <file.tex>
on EACH of the LaTeX source files to find potentially misspelt words -- Correct them if and as appropriate.
Note: Not every word that aspell -c reports may be misspelt. aspell has limitations.

----------
Plagiarism
----------

Plagiarism in any form is unacceptable by University policy.

------------------
Printing & Binding
------------------

If a hard copy is required, print your report double-sided. Save paper.
Your binding method should hold pages securely.
Use any reasonable binding method, including spiral binding, can be used to create bound copies of your printed report.
Hard binding with or without embossing is not required.
We discourage the use of the so-called "patti files".
