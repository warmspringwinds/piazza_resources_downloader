# Piazza study resources downloader

Provides you with an ability to download all resources linked in the piazza resources panel.

## How it works

In order to make it work follow the steps:

1. Create an empty directory and go there

2. Dowload the repository `git clone https://github.com/warmspringwinds/piazza_resources_downloader.git`

3. Go to piazza resources page where all the resources can be dowloaded.

4. If you are in Chrome press `ctrl + shift + j` and paste the contents of the `fetch_urls_and_names.js`
into the console.

5. You should see outputs with links and with names. Copy both outputs in respective files:
`resources_links.txt` and `resources_names.txt`.

6. While being in the repository directory run `python get_resources_files.py`.