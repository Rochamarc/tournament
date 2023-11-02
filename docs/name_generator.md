# Table of Contents

* [configure](#configure)
* [file\_handler](#file_handler)
  * [open\_basic\_files](#file_handler.open_basic_files)
  * [open\_language\_files](#file_handler.open_language_files)
* [base\_controller](#base_controller)
  * [BaseController](#base_controller.BaseController)
    * [get\_select\_query](#base_controller.BaseController.get_select_query)
    * [get\_insert\_query](#base_controller.BaseController.get_insert_query)
* [names\_controller](#names_controller)
  * [NamesController](#names_controller.NamesController)
    * [insert\_first\_names](#names_controller.NamesController.insert_first_names)
    * [insert\_last\_names](#names_controller.NamesController.insert_last_names)
    * [select\_first\_names](#names_controller.NamesController.select_first_names)
    * [select\_last\_names](#names_controller.NamesController.select_last_names)
    * [select\_full\_name\_by\_nationality](#names_controller.NamesController.select_full_name_by_nationality)

<a id="configure"></a>

# configure

<a id="file_handler"></a>

# file\_handler

<a id="file_handler.open_basic_files"></a>

#### open\_basic\_files

```python
def open_basic_files(dir_name: str, file_name: str) -> list[str]
```

Open files that only has on item by row
in NameGenerator/files/{dir_name}/{file_name}.csv

Parameters
----------
dir_name : str
    String with the directory name inside files
file_name : str
    Name of the file without the extension

Returns
-------
    A list of lists with names

<a id="file_handler.open_language_files"></a>

#### open\_language\_files

```python
def open_language_files(dir_name: str, file_name: str) -> dict
```

Open files that has two items by row
in NameGenerator/files/{dir_name}/{file_name}.csv

Parameters
----------
dir_name : str
    String with the directory name inside files
file_name : str
    Name of the file without the extension

Returns
-------
    A list of lists with names

<a id="base_controller"></a>

# base\_controller

<a id="base_controller.BaseController"></a>

## BaseController Objects

```python
class BaseController()
```

Base class that contains every property and functions used in other controllers

<a id="base_controller.BaseController.get_select_query"></a>

#### get\_select\_query

```python
@classmethod
def get_select_query(cls, file_name: str) -> str
```

Get one query on queries/select

Parameters
----------
file_name : str
    Name of the file inside the path without the file extension

Returns
-------
    A string with the query in the file

Raises
------
    FileNotFoundError
        If the file doesnt exists

<a id="base_controller.BaseController.get_insert_query"></a>

#### get\_insert\_query

```python
@classmethod
def get_insert_query(cls, file_name: str) -> str
```

Get one query on queries/insert

Parameters
----------
file_name : str
    Name of the file inside the path without the file extension

Returns
-------
    A string with the query in the file

Raises
------
    FileNotFoundError
        If the file doesnt exists

<a id="names_controller"></a>

# names\_controller

<a id="names_controller.NamesController"></a>

## NamesController Objects

```python
class NamesController(BaseController)
```

Class that handle tournament_name database

Methods
-------
insert_first_names(first_names: list, nationality: str)
    Insert first names in database
insert_last_names(last_names: list, nationality: str)
    Insert last names in database
select_first_names(nationality: str)
    Select a list of first names in database
select_last_names(nationality: str)
    Select a list of last names in database
select_full_name_by_nationality(nationality: str)
    Select a random full name by nationality

<a id="names_controller.NamesController.insert_first_names"></a>

#### insert\_first\_names

```python
@classmethod
def insert_first_names(cls, first_names: list, nationality: str) -> None
```

Insert names into the tournament_name.first_names

Parameters
----------
first_names : list
    A list of first names
nationality : str
    A string with the nationality of the names

Returns
-------
    None

<a id="names_controller.NamesController.insert_last_names"></a>

#### insert\_last\_names

```python
@classmethod
def insert_last_names(cls, last_names: list, nationality: str) -> None
```

Insert names into the tournament_name.last_names

Parameters
----------
last_names : list
    A list of last names
nationality : str
    A string with the nationality of the names

Returns
-------
    None

<a id="names_controller.NamesController.select_first_names"></a>

#### select\_first\_names

```python
@classmethod
def select_first_names(cls, nationality: str) -> list
```

Select first names from tournament_name.first_names

Parameters
----------
nationality : str
    Str used to select the nationality of first names

Returns
-------
    A list of lists with first names

<a id="names_controller.NamesController.select_last_names"></a>

#### select\_last\_names

```python
@classmethod
def select_last_names(cls, nationality: str) -> list
```

Select last names from tournament_name.last_names

Parameters
----------
nationality : str
    Str used to select the nationality of last names

Returns
-------
    A list of lists with last names

<a id="names_controller.NamesController.select_full_name_by_nationality"></a>

#### select\_full\_name\_by\_nationality

```python
@classmethod
def select_full_name_by_nationality(cls, nationality: str) -> list[set]
```

Select a random name from tournament_name.first_names & tournament_name.last_names

Parameters
----------
nationality : str
    Str used to select the nationality of the name

Returns
-------
    A two dimentional list with first name and last name

