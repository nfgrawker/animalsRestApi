# animalsRestApi
This project is intended to show proficiency in Django/DRF.
# To Run this server
   - Clone repository
   - open a terminal and make sure working directory is in animalsRestApi
   - Have python 3.7 or higher and pip added to path.
   - Run `pip install -r /path/to/requirements.txt`
   - Run `python manage.py makemigrations animals`
   - Run `python manage.py migrate`
   - Run `python manage.py runserver`
   
   The server should now be running on https://localhost:8000 and this will be reffered to as the base url later in the docs.

1. **It has 4 models.**
   1. Animals, Specific animals, can be wild or owned by people.`"first_name":String, "last_name":String, "location:Location PK"`
   2. Species, these are a general category with some info on natuarl wild charactaristics. `"name":String, "region":Region PK, "wiki_url":String`
   3. Location, this will be where specific animals were last seen or pemeanently houses at. `"name":String, "zip_code":String`
   4. Region, a specific region where species are generally located. Takes `"name":String, "location":String, "coordinates":String`

2. **For APIs**
   1. `http://{baseapi}/animal-list?model=<model>`
      1. This takes a GET
         1. Returns all current objects of requested model
      2. This takes a POST.
         1. Creates all current objects of requested model if able.
         2. Must send in an json object like `{"entries":[{ModelData},{ModelData},{ModelData}]}`
         3. Be aware only one type of model can be sent in at one time.
   2. `http://{baseapi}/animals/<pk>/`
      1. This takes a Get, Must have correct PK.
         1. Returns one object associated with the PK
      2. This takes a put, delete, post.
         1. Will do the correct action with associated PK and return the object or status code. If it is a post then pass in 0 for the pk.

3. **Things to Add**
   1. Refactor views into a more readable/sustainable format, consider using mixins.
   2. Consider adding dataclasses for incoming requests.data so we have editor support and documentation of what we expect.(might coinside with API docs.)
   3. Switch to postgres with location support, gis django model library as well.
   4. Add tests.
   5. Make fully mypy complaint and run black/flake8 on each file.
   6. Switch to using swagger/openapi for auto docs, might be cleaner and more extensive.

