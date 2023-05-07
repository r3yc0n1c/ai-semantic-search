# AI Semantic Search
Implementation and usage of semantic search in E-commerce site using artificial intelligence

# Built with
- pinecone-client
- sentence_transformers
- flask
- pandas

# Usage

- To store data into Pinecone Index -
```sh
$ python3 store.py
```

- To run the app -
```sh
$ python3 search.py

 * Serving Flask app 'search'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 111-657-709
```

- Go to http://127.0.0.1:5000

- Pass the search query like this
http://localhost:5000/search?q=Cycling%20Shorts

# Demo
[![Watch the video](https://i3.ytimg.com/vi/NtCQci6_dbU/maxresdefault.jpg)](https://youtu.be/NtCQci6_dbU)

<p align='center'> Watch the video here - <a href='https://youtu.be/NtCQci6_dbU'>https://youtu.be/NtCQci6_dbU</a></p>

# Feats
- [x] Vector Database
- [x] Vectorization Algorithm
- [x] Similarity Search Algorithm
- [ ] User Interface

# License
<p align="center">
<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.<br/>
Read the <a href="./LICENSE">LICENSE</a> for more details.
</p>
