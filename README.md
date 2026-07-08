# Google Maps POI Scraper

A tool to extract POI data from google maps using the Google Places API (New) written in Python using the google-maps-places library

### Instructions for working in the virtual environment

##### Steps:

1. Clone the repository (git clone [repo_link])
2. Open your terminal in the repository directory and run `python -m venv [vitual environment name]`
3. Run the following command to activate the virtual environment; `./.venv/Scripts/activate`
4. If the name of your virtual environment shows up in paranthesis next to the terminal path, you've successfully activated your virtual environment
5. You must run the virual environment activation command with each new window or terminal if it isn't activated already
6. All source files and folders for your project should be located outside the virtual environment folder but within the repo
   ##### For example
   ```
   my-project/
   ├── .venv/
   ├── .gitignore
   ├── README.md
   ├── src/
   │   ├── main.py
   │   └── utils.py
   └── tests/
    └── test_main.py
   ```

_Note:_

- Packages installed globally are not accessible by default within the virtual environment. To access them you must include the `--system-site-packages` flag when creating a virtual environment. For existing environments;
  - Locate and open the pyvenv.cfg file in a text editor.
  - Find the line include-system-site-packages = false.
  - Change false to true.
  - Save and close the file.

## Dependencies

- Python version 3.14
- google-maps-places
