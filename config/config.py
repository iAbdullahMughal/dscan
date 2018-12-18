__author__ = 'Muhammad Abdullah Mughal'
__email__ = 'iamabdullahmughal@gmail.com'
__website__ = 'https://www.iabdullahmughal.com'
__twitter__ = '@iabdullahmughal'

import os
import sys


class GitConfig:
    PROJECT_NAME = 'Sharingan'
    PROJECT_DESCRIPTION = 'A project to visualize vba macro into graph to show function and code flow.'
    PROJECT_HOME_PAGE = 'https://github.com/iAbdullahMughal/Sharingan'
    PROJECT_WIKI = 'https://github.com/iAbdullahMughal/Sharingan/wiki'
    PROJECT_ISSUES = 'https://github.com/iAbdullahMughal/Sharingan/issues'


class ProjectConfig:
    LINE_SEPARATOR = "\n"
    R_SEPARATOR = "\r"
    LIST_AUTORUN = [
        'AutoExec', 'AutoOpen', 'DocumentOpen', 'AutoExit', 'AutoClose',
        'Document_Close', 'DocumentBeforeClose', 'DocumentChange', 'AutoNew',
        'Document_New', 'NewDocument', 'Document_Open', 'Document_BeforeClose',
        'Auto_Open', 'Workbook_Open', 'Workbook_Activate', 'Workbook_Deactivate', 'Auto_Close',
        'Workbook_Close', u'\w+_Painted', u'\w+_Change', u'\w+_DocumentBeforePrint',
        u'\w+_DocumentOpen', u'\w+_DocumentBeforeClose', u'\w+_DocumentBeforeSave',
        u'\w+_GotFocus', u'\w+_LostFocus', u'\w+_MouseHover', u'\w+_Resize',
        'App_WorkbookOpen', 'App_NewWorkbook', 'App_WorkbookBeforeClose', 'Workbook_BeforeClose',
        'FileSave', 'CloseWithoutSaving', 'FileOpen', 'FileClose', 'FileExit',
        'Workbook_SheetSelectionChange', 'Workbook_BeforeSave', 'FileTemplates',
        'ViewVBCode', 'ToolsMacro', 'FormatStyle', 'OpenMyMacro', 'HelpAbout',
        u'\w+_Layout', u'\w+_Painting',
        u'\w+_BeforeNavigate2', u'\w+_BeforeScriptExecute', u'\w+_DocumentComplete', u'\w+_DownloadBegin',
        u'\w+_DownloadComplete', u'\w+_FileDownload', u'\w+_NavigateComplete2', u'\w+_NavigateError',
        u'\w+_ProgressChange', u'\w+_PropertyChange', u'\w+_PropertyChange', u'\w+_StatusTextChange',
        u'\w+_TitleChange', u'\w+_MouseMove', u'\w+_MouseEnter', u'\w+_MouseLeave'
    ]

    LIST_MALICIOUS_CASE_SENSITIVE = [
        "Environ", "Open", 'Write', 'Put', 'Output', 'Print #', 'Binary', 'FileCopy',
        'CopyFile', 'Kill', 'CreateTextFile', 'ADODB.Stream', 'WriteText',
        'SaveToFile', 'Shell', 'vbNormal', 'vbNormalFocus', 'vbHide',
        'vbMinimizedFocus', 'vbMaximizedFocus', 'vbNormalNoFocus',
        'vbMinimizedNoFocus', 'WScript.Shell', u'\w+\.Run', 'ShellExecute', 'MacScript',
        'popen', r'exec[lv][ep]?', 'noexit',
        'ExecutionPolicy', 'noprofile', 'command', 'EncodedCommand',
        'invoke-command', 'scriptblock', 'Invoke-Expression',
        'AuthorizationManager', 'Start-Process', 'Application\.Visible',
        'ShowWindow', 'SW_HIDE', 'MkDir', 'ActiveWorkbook.SaveAs',
        'Application.AltStartupPath', 'CreateObject', 'New-Object',
        'Shell\.Application', 'Windows', 'FindWindow', 'libc\.dylib', 'dylib',
        'CreateThread', 'VirtualAlloc', 'VirtualAllocEx', 'RtlMoveMemory',
        'EnumSystemLanguageGroupsW?', u'EnumDateFormats(?:W|(?:Ex){1,2})?',
        'URLDownloadToFileA', 'Msxml2\.XMLHTTP', 'Microsoft\.XMLHTTP', 'User-Agent',
        'Net\.WebClient', 'DownloadFile', 'DownloadString', 'MSXML2\.ServerXMLHTTP',
        'SendKeys', 'AppActivate', 'CallByName',
        'RegOpenKeyExAs', 'RegOpenKeyEx', 'RegCloseKey',
        'RegQueryValueExA', 'RegQueryValueEx', 'RegRead',
        'GetVolumeInformationA', 'GetVolumeInformation', '1824245000',
        r'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\ProductId',
        'popupkiller', 'SbieDll\.dll', 'SandboxieControlWndClass',
        'currentuser', 'Schmidti', 'AccessVBOM', 'VBAWarnings',
        'ProtectedView', 'DisableAttachementsInPV', 'DisableInternetFilesInPV',
        'DisableUnsafeLocationsInPV', 'blockcontentexecutionfrominternet',
        'VBProject', 'VBComponents', 'CodeModule', 'AddFromString', 'Call', 'GetObject',
        'ExecQuery', 'GetStringValue', 'GetDWORDValue', u'ActiveDocument\.\w+', 'DOMDocument',
        'IXMLDOMElement', 'ComputerName', 'Domain', 'RegRead', 'RegWrite', '#If Mac',
        'appdata', u'WordBasic\.\w+', 'WriteLine', 'Exec',
        'Cells', u'Application\.\w+', 'Sleep', 'Process', u'NormalTemplate\.\w+',
        u'\w+\.Application', 'CommandBars', u'System\.\w+', "setRequestHeader", "Send", "setOption",
        "RecentFiles", "Mozilla", "UserName", "DeleteFile", "Delete", "\.Execute", "\.Content",
        "MsgBox", "\.Quit", 'Run', 'Now', 'Comments',
        'CopyFolder', 'http', 'winmgmts', 'bin\.base64', '\.Create'
    ]

    LIST_MALICIOUS_CASE_SENSITIVE += [u"\.caption", u"\.text", u"\.value", u"\.ControlTipText", u"\.tag",
                                      u"\.CustomDocumentProperties"]

    LIST_OBFUSCATION_KEYWORDS = ['Asc', 'Mid', 'Left', 'Right', 'Tan', 'StrReverse', 'Xor',
                                 'Chr', 'ChrB', 'ChrW', 'CStr', 'StrConv', 'Replace', 'Int'
                                 ]

    LIST_MALICIOUS_CASE_SENSITIVE += LIST_OBFUSCATION_KEYWORDS

    LIST_MALICIOUS_CASE_INSENSITIVE = [
        r'SYSTEM\\ControlSet001\\Services\\Disk\\Enum', 'VIRTUAL', 'VMWARE', 'VBOX',
        u'"[\-w_\\/]+\.(?:EXE|PIF|GADGET|MSI|MSP|MSC|VBS|VBE|VB|JSE|JS|WSF|WSC|WSH|WS|BAT|CMD|DLL|SCR|HTA|CPL|CLASS|JAR'
        u'|PS1XML|PS1|PS2XML|PS2|PSC1|PSC2|SCF|LNK|INF|REG)"',
        'FileSystemObject', 'GetSpecialFolder', 'PowerShell', u'SELECT \* FROM \w+', 'deletefolder',
        'Environ\(\"ALLUSERSPROFILE\"\)'
    ]


class LocationConfig:
    BASE_DIR = os.path.abspath(os.path.dirname(sys.modules['__main__'].__file__))
    JSON_LOCATION = BASE_DIR + '/'
