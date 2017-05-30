import plistlib
import os
import glob

'''
This script will parse through all group_*.xml files within your TextExpander folder.
Anything marked as Plain Text, Shell Script or JavaScript should be converted into
Keyboard Maestro groups with the same title and abbreviation.

All new KM Macro files will be saved to the Desktop.

'''

# Modify this area to customize how the script will run

# Change this path to where ever your TextExander Settings live
HOME = os.path.expanduser('~')
TEXTEXPANDER_PATH = HOME + '/Library/Application Support/TextExpander/Settings.textexpanderlocal'
SAVE_PATH = HOME + '/Desktop/TextExpander_to_KeyboardMaestro'

# Change this if you'd like to change your snippets when importing to Keyboard Maestro
# If your snippet is ttest, you can make it ;;ttest by changing the variable to ';;'
OPTIONAL_NEW_PREFIX = ''

# Change this if you want the snippet to inserted by typing or pasting
# Remember it MUST be 'paste' or 'type' or the script will fail
PASTE_OR_TYPE = 'paste' # 'type'




############

# Edit below at your own risk

############

snippet_types = {
    'plaintext': 0,
    'applescript': 2,
    'shell': 3,
    'javascript': 4,
}

snippet_types_to_values = dict((value, key) for key, value in snippet_types.iteritems())


class KeyboardMaestroMacros(object):
    @classmethod
    def macro_by_name(cls, macro_name, group_name, name, text, abbreviation):
        return getattr(cls, macro_name)(group_name, name, text, abbreviation)

    @staticmethod
    def javascript(group_name, name, text, abbreviation):
        return {
            'Activate': 'Normal',
            'CreationDate': 0.0,
            'IsActive': True,
            'Macros': [
                {'Actions': [
                    {'DisplayKind': KeyboardMaestroMacros._paste_or_type(),
                     'IncludeStdErr': True,
                     'IsActive': True,
                     'IsDisclosed': True,
                     'MacroActionType': 'ExecuteJavaScriptForAutomation',
                     'Path': '',
                     'Text': text,
                     'TimeOutAbortsMacro': True,
                     'TrimResults': True,
                     'TrimResultsNew': True,
                     'UseText': True}, {
                        'IsActive': True,
                        'IsDisclosed': True,
                        'MacroActionType': 'DeletePastClipboard',
                        'PastExpression': '0'}
                    ],
                 'CreationDate': 482018934.65354,
                 'IsActive': True,
                 'ModificationDate': 482018953.856014,
                 'Name': name,
                 'Triggers': [{
                    'Case': 'Exact',
                    'DiacriticalsMatter': True,
                    'MacroTriggerType': 'TypedString',
                    'OnlyAfterWordBreak': False,
                    'SimulateDeletes': True,
                    'TypedString': KeyboardMaestroMacros._abbreviation(abbreviation)}]}
            ],
            'Name': 'Snippet - %s' % group_name,
        }

    @staticmethod
    def applescript(group_name, name, text, abbreviation):
        return {
            'Activate': 'Normal',
            'CreationDate': 0.0,
            'IsActive': True,
            'Macros': [
                {'Actions': [
                    {'DisplayKind': KeyboardMaestroMacros._paste_or_type(),
                     'IncludeStdErr': True,
                     'IsActive': True,
                     'IsDisclosed': True,
                     'MacroActionType': 'ExecuteAppleScript',
                     'Path': '',
                     'Text': text,
                     'TimeOutAbortsMacro': True,
                     'TrimResults': True,
                     'TrimResultsNew': True,
                     'UseText': True}, {
                        'IsActive': True,
                        'IsDisclosed': True,
                        'MacroActionType': 'DeletePastClipboard',
                        'PastExpression': '0'}
                    ],
                 'CreationDate': 482018934.65354,
                 'IsActive': True,
                 'ModificationDate': 482018953.856014,
                 'Name': name,
                 'Triggers': [{
                    'Case': 'Exact',
                    'DiacriticalsMatter': True,
                    'MacroTriggerType': 'TypedString',
                    'OnlyAfterWordBreak': False,
                    'SimulateDeletes': True,
                    'TypedString': KeyboardMaestroMacros._abbreviation(abbreviation)}]}
            ],
            'Name': 'Snippet - %s' % group_name,
        }

    @staticmethod
    def plaintext(group_name, name, text, abbreviation):
        return {
            'Activate': 'Normal',
            'CreationDate': 0.0,
            'IsActive': True,
            'Macros': [{'Actions': [
                {
                    'Action': KeyboardMaestroMacros._paste_or_type('plaintext'),
                    'IsActive': True,
                    'IsDisclosed': True,
                    'MacroActionType': 'InsertText',
                    'Paste': True,
                    'Text': text.replace("%|", "%|%", 1)}, {
                        'IsActive': True,
                        'IsDisclosed': True,
                        'MacroActionType': 'DeletePastClipboard',
                        'PastExpression': '0'
                    }],
                'CreationDate': 0.0,
                'IsActive': True,
                'ModificationDate': 482031702.132113,
                'Name': name,
                'Triggers': [{
                    'Case': 'Exact',
                    'DiacriticalsMatter': True,
                    'MacroTriggerType': 'TypedString',
                    'OnlyAfterWordBreak': False,
                    'SimulateDeletes': True,
                    'TypedString': KeyboardMaestroMacros._abbreviation(abbreviation)}],
            }],
            'Name': 'Snippet - %s' % group_name,
        }

    @staticmethod
    def shell(group_name, name, text, abbreviation):
        return {
            'Activate': 'Normal',
            'CreationDate': 0.0,
            'IsActive': True,
            'Macros': [{
                'Actions': [{
                    'DisplayKind': KeyboardMaestroMacros._paste_or_type(),
                    'IncludeStdErr': True,
                    'IsActive': True,
                    'IsDisclosed': True,
                    'MacroActionType': 'ExecuteShellScript',
                    'Path': '',
                    'Text': text,
                    'TimeOutAbortsMacro': True,
                    'TrimResults': True,
                    'TrimResultsNew': True,
                    'UseText': True},
                 {'IsActive': True,
                  'IsDisclosed': True,
                  'MacroActionType': 'DeletePastClipboard',
                  'PastExpression': '0'}],
                'CreationDate': 482018896.698121,
                'IsActive': True,
                'ModificationDate': 482020783.300151,
                'Name': name,
                'Triggers': [{
                    'Case': 'Exact',
                    'DiacriticalsMatter': True,
                    'MacroTriggerType': 'TypedString',
                    'OnlyAfterWordBreak': False,
                    'SimulateDeletes': True,
                    'TypedString': KeyboardMaestroMacros._abbreviation(abbreviation)}],
                }],
            'Name': 'Snippet - %s' % group_name,
        }

    @staticmethod
    def _abbreviation(name):
        return OPTIONAL_NEW_PREFIX + name

    @staticmethod
    def _paste_or_type(snippet_type=None):
        value = {
            'paste': "Pasting",
            'type': "Typing"
        }
        if snippet_type == 'plaintext':
            return "By%s" % value[PASTE_OR_TYPE]
        else:
            return value[PASTE_OR_TYPE]


def parse_textexpander():
    '''
    Each TextExpander group is its own file starting with the file name 'group_'.

    Example snippet dictionary
    {
        'abbreviation': '.bimg',
        'abbreviationMode': 0,
        'creationDate': datetime.datetime(2013, 5, 19, 19, 42, 16),
        'label': '',
        'modificationDate': datetime.datetime(2015, 1, 10, 20, 19, 59),
        'plainText': 'some text,
        'snippetType': 3,
        'uuidString': '100F8D1F-A2D1-4313-8B55-EFD504AE7894'
    }

    Return a list of dictionaries where the keys are the name of the group
    '''
    to_ret = {}

    # Let's get all the xml group files in the directory
    xml_files = [f for f in glob.glob(TEXTEXPANDER_PATH + "/*.xml")
                 if f.startswith(TEXTEXPANDER_PATH + "/group_")]

    for xml_file in xml_files:
        pl = plistlib.readPlist(xml_file)
        if pl['name'] not in to_ret:
            to_ret[pl['name']] = []
        for snippet in pl['snippetPlists']:
            if snippet['snippetType'] in snippet_types.values():
                to_ret[pl['name']].append(snippet)
    return to_ret


def main():
    text_expanders = parse_textexpander()
    for group, text_expander in text_expanders.iteritems():
        macros_to_create = []
        for snippet in text_expander:
            macros_to_create.append(
                KeyboardMaestroMacros.macro_by_name(snippet_types_to_values[snippet['snippetType']],
                                                    group,
                                                    snippet['label'],
                                                    snippet['plainText'],
                                                    snippet['abbreviation'])
                )

        # Create a new folder on the desktop to put the macros
        if not os.path.exists(SAVE_PATH):
            os.mkdir(SAVE_PATH)
        # Save the macros
        with open(SAVE_PATH + '/%s.kmmacros' % group, 'w') as f:
            f.write(plistlib.writePlistToString(macros_to_create))

if __name__ == '__main__':
    main()
