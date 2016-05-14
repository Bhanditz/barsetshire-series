<<<<<<< HEAD
# barsetshire-series

This is a data visualization that shows how various topics such as gender, religion, and class appear across Anythony Trollope's
[Barsetshire series](https://en.wikipedia.org/wiki/Chronicles_of_Barsetshire); a series consisting of six novels written between 1855
and 1867.  

The vis tracks how each topic appears in each chapter---lighter bars mean that topic wasn't particulalry present in that chapter,
while darker bars suggest a stronger presence.  Topics are tracked via word frequencies---each topic has a corpus of words 
related to it, and I ran a python script to determine the frequencies of those words in each chapter of the series.

The vis should be live in early April; for now I'm still collecting data and finalizing the design.
=======
## Basic Text Mining / Barsetshire Towers

#### What's in here?

- fulltext versions of all six of Trollope's Barsetshire novels
- folders of each novel broken up by chapter + json files of chapter names
- tools folder with scripts and ideas that may be of use

#### NLTK

This takes advantage of the Python library NLTK. If it is not installed, you'll need use pip to install NLTK (assuming Python 2.7.9 or higher, no need to install pip).

Make sure you have NLTK ([Install instructions](http://www.nltk.org/install.html))

##### NLTK Resources

- [Natural Language Processing with Python online book](http://www.nltk.org/book/)
- [Natural Language Toolkit](http://www.nltk.org/)
>>>>>>> barsetshire-data/master
