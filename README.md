# Convert TextExpander snippets to Keyboard Maestro macros

A simple batch convert script to convert all of your [TextExpander](https://textexpander.com/) snippets into [Keyboard Maestro](https://www.keyboardmaestro.com/main/) macros.

## Usage

Download the script and read the comments; make any changes before running the script with

```
$ python TE.py
```

## Notes

### Fancy snippets

This script will copy the snippets as they are, but doesn't convert any of the fancy features (fillPopups etc) from TextExpander automatically.

So, if you have a TextExpander snippet where it prompts you with a dropdown like so:

```
@include breakpoint(%fillpopup:name=size:$small:$medium:default=$large:$xlarge%) {%|}
```

Then that will be what Keyboard Maestro will exactly paste (or type depending on your settings).

So, be sure to go through the converted macros manually if you had fancy snippets.

### Insert cursor here token

Included is a find-and-replace for plaintext snippets allowing the “place cursor here” token to work in Keyboard Maestro. The string in TextExpander to place the cursor somewhere is `%|` and in Keyboard Maestro it is `%|%`.

Although the find-and-replace works well with pasted, plain text snippets, it doesn't work with the other snippet types (AppleScript, JavaScript, etc), so it's not enabled for those snippet types.

If you don't want this find-and-replace behavior, then (on line 144) then replace `'Text': text.replace("%|", "%|%", 1),` with `'Text': text,`.

### Other tokens

You may want to manually do a find-and-replace for `%clipboard`, replacing it with `%PastClipboard%1%` if you use “insert clipboard” token in your TextExpander snippets.

You can also drag your Settings.textexpandersettings folder into your code editor of choice and do a find-and-replace on the whole folder to replace TextExpander tokens with the Keyboard Maestro equivalent.

### XML not well-formed error

If you get a `xml.parsers.expat.ExpatError: not well-formed (invalid token):` error when running the script, try opening up Settings.textexpandersettings and looking for the group .xml file with `<string>Suggested Snippets</string>` in it; delete that entire file. That group is the snippet suggestion group from TextExpander, and doesn't always play nice with the convert script.
