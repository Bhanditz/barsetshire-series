# Adding Topics

Suppose you want to add a new topic to the Barsetshire Visualization.  You want to see how words related to the topic "Cereal" might come up.  While cereal probably isn't a central theme in Victorian literature, you can certainly try it out.

First you'll need to download the repository.  You'll also have to know how to run python programs to make this work.

Suppose we want to look for the words "bowl," "spoon," and "cheerios" in the series.  We'll need to enter this data into the program `freqmetrics.py` in the folder `barsetshire-data/tools`.

Once you've opened up this folder, you'll see a bit of code.  If you scroll down to the bottom you'll see a list of topics and the words associated with them.  It looks something like this:

```python
allcorps = {
	"Class": ['archdeacon', 'bishop', 'dr', '...'],
	"Writing": ['letter', 'write', 'read', '...']
  }
```

All you have to do is type out your topic and words into this list.  Your list will need to be written like so:

```python
"Cereal": ['bowl','spoon','cheerios'],
```

Notice that there is a comma at the end of this string.  *This is important!* Make sure you have it in the code.

Once you have this ready, you can paste the text just above the first item in the list (in this case it's the `Class` item).  It will look like this:

```python
allcorps = {

    "Cereal": ['bowl', 'spoon', 'cheerios' ],
	"Class": ['archdeacon', 'bishop', 'dr', '...'],
	"Writing": ['letter', 'write', 'read', '...']
  }
```

After you do this, save the `freqmetrics.py` program, and then run the `databuild.py` program.  It may take a little while, but once it's done, the data will be ready to visualize.  In fact, you don't have to do any more work after this!  Just open up the webpage and it'll be ready to go.
