# Piazza study resources downloader

Provides you with an ability to download all resources linked in the piazza resources panel.

## How it works

In order to make it work follow the steps:

1. Create an empty directory and go there

2. Dowload the repository `git clone https://github.com/warmspringwinds/piazza_resources_downloader.git`

3. Go to piazza resources page where all the resources can be dowloaded.

4. If you are in Chrome press `ctrl + shift + j` and paste the contents of the `fetch_urls_and_names.js`
into the console. If you are using Firefox got to `Developer > Debugger` and then `Console` in the opened window. It can warn you when you try to paste that you have to first type in the console `allow pasting`.

5. You should see outputs with links and with names. Copy both outputs in respective files:
`resources_links.txt` and `resources_names.txt`.

6. While being in the repository directory run `python get_resources_files.py`.

## Shorter way

### Use existing links

I have already extracted all the links and filenames for `Machine Learning course in Tum`.
So in order to download it just do steps `1, 2, 6` from the aforementioned guide.

But be careful while doing this. The links are changed sometimes and you can get no files in that case.
Better use the first approach or just download the archive.

### `Machine Learning course in Tum` archive

Or you can just download the archived [zip](https://drive.google.com/file/d/0B_6oHpf9oDHRY2c4U19FRnFRSEk/view?usp=sharing)