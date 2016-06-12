# Convert TextExpander snippets to Keyboard Maestro macros

Simple batch convert of all your Snippets to Macros.

### Usage

Download the script and read the comments and make any changed before running the script with

`$ python TE.py`

### Notes

This script will copy the snippets as they are, but doesn't convert any of the fancy features (fillPopups etc) from TextExpander automatically.

So if TextExpander you have a snippet where it prompts you with a dropdown lise so:

`@include breakpoint(%fillpopup:name=size:$small:$medium:default=$large:$xlarge%) {%|}`

Then that will be what Keyboard Maestro will paste (or type depending on your settings).

The fillpop won't work, so be sure to go through manually if you have fancy snippets.

## Insert cursor here

Included a find and replace for plaintext snippets allowing the "place cursor here" to work in Keyboard Maestro. The string in TextExpander to place cursor is `%|` and in Keyboard Maestro it is `%|%`

Although the find and replace would work with the other snippet types it woudln't work if you opt to have the snippet typed rather than pasted.

If you don't then replace

 `'Text': text,`

 with

 `'Text': text.replace("%|", "%|%", 1),`

You may want to do a find and replace for `%clipboard` replace with `%PastClipboard%1%` if you use "insert clipboard".

You can also drag your Settings.textexpandersettings file into Sublime and do a find and replace on the whole folder to replace TextExpander variables with the equivalent for Keyboard Maestro.


