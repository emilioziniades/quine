I have been reading [Godel, Escher, Bach](https://en.wikipedia.org/wiki/G%C3%B6del,_Escher,_Bach). The book includes discussion of quines: structures that are self replicating. It is possible to create programs that are quines: they print their own source code. I thought I would try it out in python.

`quine.py` prints it's own source code.

```
python3 quine.py
```

To check this, you could do the following

```
$ python3 quine.py > quine2.py
$ git diff quine.py quine2.py
```

There is absolutely no difference between the original file, and the source code produced by the running of that file.

If you are still skeptical, you could go further.

```
$ python3 quine.py | python3 | python3 | python3 | python3 > quine2.py
$ git diff quine.py quine2.py
```

The code is perfectly self replicating, and could run in a loop forever.

`test.py` does both of the above. You can run the following

```
$ python3 -m unittest test.py
```
