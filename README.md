# Utilities

### backup.bat
Backs up my files to mounted network drives with robocopy.

### resetIconCache.bat
Resets Windows' icon cache. Useful for fixing broken icons.

### strip_ssa.py
Strips lines containing a keyword from .ssa/.ass subtitle files.

Often, each line in an .ssa file will have a keyword to distinguish different styles of content such as dialogue, lyrics, chapter titles, translations, etc.

.ssa files can be opened with any standard text editor, and you can inspect it to see which lines contain the tag that you want to keep. This also converts the files to UTF-8 to avoid decoding issues.

One of the most popular tools for subtitle editing, [SubtitleEdit](https://www.nikse.dk/subtitleedit), can error when trying to read formatting lines or files with nonstandard encoding.

Stripping out unnecessary lines will reduce the likelihood of encountering an error when using SubtitleEdit to convert the subtitles to a different format.
