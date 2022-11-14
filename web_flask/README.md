# 0x04. AirBnB clone - Web framework

## About
Building application server with `Flask` framework

## Tasks
0. Script that starts a Flask web application:
	* Listens on `0.0.0.0`, port `5000`
	* Routes:
		* `/`: display **"Hello HBNB!"**
	* [0-hello_route.py](0-hello_route.py)
	* [__init__.py](__init__.py)
1. Script that starts a Flask web application:
	* Listens on `0.0.0.0`, port `5000`
	* Routes:
		* `/`: display **"Hello HBNB!"**
		* `/hbnb`: display **"HBNB"**
	* [1-hbnb_route.py](1-hbnb_route.py)
2. Script that starts a Flask web application:
	* Listens on `0.0.0.0`, port `5000`
	* Routes:
		* `/`: display **Hello HBNB!**
		* `/hbnb`: display **"HBNB"**
		* `/c/<text>`: display **"C "** followed by the value of the `text` variable (replace underscore _ symbols with a space )
	* [2-c_route.py](2-c_route.py)
3. Script that starts a Flask web application:

	* Listens on `0.0.0.0`, port `5000`
	* Routes:
		* `/`: display **"Hello HBNB!"**
		* `/hbnb`: display *HBNB*
		* `/c/<text>`: display **"C "**, followed by the value of the `text` variable (replace underscore _ symbols with a space )
		* `/python/(<text>)`: display **"Python "**, followed by the value of the `text` variable (replace underscore _ symbols with a space )
	* The default value of text is **"is cool"**
	* [3-python_route.py](3-python_route.py)
4. Script that starts a Flask web application:
	* Listens on `0.0.0.0`, port `5000`
	* Routes:
		* `/`: display **"Hello HBNB!"**
		* `/hbnb`: display *HBNB*
		* `/c/<text>`: display **"C "**, followed by the value of the `text` variable (replace underscore _ symbols with a space )
		* `/python/(<text>)`: display **"Python "**, followed by the value of the `text` variable (replace underscore _ symbols with a space )
		* `/number/<n>`: display **"n is a number"** only if `n` is an integer
	* [4-number_route.py](4-number_route.py)
5. Script that starts a Flask web application:
	* Listens on `0.0.0.0`, port `5000`
	* Routes:
		* `/`: display **"Hello HBNB!"**
		* `/hbnb`: display *HBNB*
		* `/c/<text>`: display **"C "**, followed by the value of the text variable (replace underscore _ symbols with a space )
		* `/python/(<text>)`: display **"Python "**, followed by the value of the text variable (replace underscore _ symbols with a space )
		* `/number/<n>`: display **"n is a number"** only if `n` is an integer
		* `/number_template/<n>`: display a `HTML` page only if `n` is an integer: `H1` tag: **"Number: n"** inside the tag `BODY`
	* [5-number_template.py](5-number_template.py)
	* [templates/5-number.html](templates/5-number.html)
4. Script that starts a Flask web application:
	* Listens on `0.0.0.0`, port `5000`
	* Routes:
		* `/`: display **"Hello HBNB!"**
		* `/hbnb`: display *HBNB*
		* `/c/<text>`: display **"C "**, followed by the value of the text variable (replace underscore _ symbols with a space )
		* `/python/(<text>)`: display **"Python "**, followed by the value of the text variable (replace underscore _ symbols with a space )
		* `/number/<n>`: display **"n is a number"** only if `n` is an integer
		* `/number_template/<n>`: display a `HTML` page only if `n` is an integer: `H1` tag: **"Number: n"** inside the tag `BODY`
		* `/number_odd_or_even/<n>`: display a HTML page only if `n` is an integer: `H1` tag: **“Number: n is even|odd”** inside the tag `BODY`
	* [6-number_odd_or_even.py](6-number_odd_or_even.py)
	* [templates/6-number_odd_or_even.html](templates/6-number_odd_or_even.html)
7. HBNB data storage improvements:
	* `FileStorage`:
		* Add a public method `def close(self):` to reload JSON file to object
		* [models/engine/file_storage.py](../models/engine/file_storage.py)
	* `DBStorage`:
		* Add a public method `def close(self)`: to close database `session`
		* [models/engine/db_storage.py](../models/engine/db_storage.py)
8. Script that starts a Flask web application:
	* Listens on `0.0.0.0`, port `5000`
	* Fetches data from storage engine `FileStorage` or `DBStorage`
	* Removes SQLAlchemy session after each request
	* Routes:
		* `/states_list`: display a `HTML` page: (inside the tag `BODY`)
			* `H1` tag: **“States”**
			* `UL` tag: with the list of all `State` objects present in `DBStorage` sorted by name (A->Z)
				* `LI` tag: description of one `State: <state.id>: <B><state.name></B>`
	* [web_flask/7-states_list.py](web_flask/7-states_list.py)
	* [web_flask/templates/7-states_list.html](web_flask/templates/7-states_list.html)
9. Script that starts a Flask web application:
	* Listens on `0.0.0.0`, port `5000`
	* Removes SQLAlchemy session after each request
	* Routes:
		* `/cities_by_states`: display a `HTML` page: (inside the tag `BODY`)
			* `H1` tag: **“States”**
			* `UL` tag: with the list of all `State` objects present in `DBStorage` sorted by name (A->Z)
				* `LI` tag: description of one `State: <state.id>: <B><state.name></B>` + `UL` tag: with the list of `City` objects linked to the `State` sorted by name (A->Z)
					* `LI` tag: description of one `City: <city.id>: <B><city.name></B>`
	* [web_flask/8-cities_by_states.py](web_flask/8-cities_by_states.py)
	* [web_flask/templates/8-cities_by_states.html](web_flask/templates/8-cities_by_states.html) 
10. Script that starts a Flask web application:
	* Listens on `0.0.0.0`, port `5000`
	* Fetches data from storage engine `FileStorage` or `DBStorage`
	* Removes SQLAlchemy session after each request
	* Routes:
		* `/states`: display a `HTML` page: (inside the tag `BODY`)
			* `H1` tag: **“States”**
			* `UL` tag: with the list of all `State` objects present in `DBStorage` sorted by name (A->Z)
				* `LI` tag: description of one `State: <state.id>: <B><state.name></B>`
		* `/states/<id>`: display a HTML page: (inside the tag BODY)
			* If a `State` object is found with this `id`:
				* `H1` tag: **“State:”**
				* `H3` tag: **“Cities:”**
				* `UL` tag: with the list of `City` objects linked to the `State` sorted by name (A->Z)
					* `LI` tag: description of one `City: <city.id>: <B><city.name></B>`
			* `Otherwise`:
				* H1 tag: “Not found!”
	* [web_flask/9-states.py](web_flask/9-states.py)
	* [web_flask/templates/9-states.html](web_flask/templates/9-states.html)
11. Script that starts a Flask web application:
	* Listens on `0.0.0.0`, port `5000`
	* Fetches data from storage engine `FileStorage` or `DBStorage`
	* Removes SQLAlchemy session after each request
	* Routes:
		* `/hbnb_filters`: display a HTML page like [6-index.html`](../web_static/6-index.html)
			* `State`, `City` and `Amenity` objects must be loaded from `DBStorage` and sorted by name (A->Z) 
	* [web_flask/10-hbnb_filters.py](web_flask/10-hbnb_filters.py)
	* [web_flask/templates/10-hbnb_filters.html](web_flask/templates/10-hbnb_filters.html)
	* [web_flask/static/](web_flask/static/)
12. Script that starts a Flask web application:
	* Listens on `0.0.0.0`, port `5000`
	* Fetches data from storage engine `FileStorage` or `DBStorage`
	* Removes SQLAlchemy session after each request
	* Routes:
		* `/hbnb`:  display a HTML page like [8-index.html](../web_static/8-index.html)
			* `State`, `City` and `Amenity` objects must be loaded from `DBStorage` and sorted by name (A->Z)
	* [web_flask/100-hbnb.py](web_flask/100-hbnb.py)
	* [web_flask/templates/100-hbnb.html](web_flask/templates/100-hbnb.html)
	* [web_flask/static/](web_flask/static/)
