"""
This module includes all consts used in this project
"""

# Action
ACTION_DOWN = 0
ACTION_UP = 1
ACTION_MOVE = 2

# KeyCode
KEYCODE_UNKNOWN = 0
KEYCODE_SOFT_LEFT = 1
KEYCODE_SOFT_RIGHT = 2
KEYCODE_HOME = 3
KEYCODE_BACK = 4
KEYCODE_CALL = 5
KEYCODE_ENDCALL = 6
KEYCODE_0 = 7
KEYCODE_1 = 8
KEYCODE_2 = 9
KEYCODE_3 = 10
KEYCODE_4 = 11
KEYCODE_5 = 12
KEYCODE_6 = 13
KEYCODE_7 = 14
KEYCODE_8 = 15
KEYCODE_9 = 16
KEYCODE_STAR = 17
KEYCODE_POUND = 18
KEYCODE_DPAD_UP = 19
KEYCODE_DPAD_DOWN = 20
KEYCODE_DPAD_LEFT = 21
KEYCODE_DPAD_RIGHT = 22
KEYCODE_DPAD_CENTER = 23
KEYCODE_VOLUME_UP = 24
KEYCODE_VOLUME_DOWN = 25
KEYCODE_POWER = 26
KEYCODE_CAMERA = 27
KEYCODE_CLEAR = 28
KEYCODE_A = 29
KEYCODE_B = 30
KEYCODE_C = 31
KEYCODE_D = 32
KEYCODE_E = 33
KEYCODE_F = 34
KEYCODE_G = 35
KEYCODE_H = 36
KEYCODE_I = 37
KEYCODE_J = 38
KEYCODE_K = 39
KEYCODE_L = 40
KEYCODE_M = 41
KEYCODE_N = 42
KEYCODE_O = 43
KEYCODE_P = 44
KEYCODE_Q = 45
KEYCODE_R = 46
KEYCODE_S = 47
KEYCODE_T = 48
KEYCODE_U = 49
KEYCODE_V = 50
KEYCODE_W = 51
KEYCODE_X = 52
KEYCODE_Y = 53
KEYCODE_Z = 54
KEYCODE_COMMA = 55
KEYCODE_PERIOD = 56
KEYCODE_ALT_LEFT = 57
KEYCODE_ALT_RIGHT = 58
KEYCODE_SHIFT_LEFT = 59
KEYCODE_SHIFT_RIGHT = 60
KEYCODE_TAB = 61
KEYCODE_SPACE = 62
KEYCODE_SYM = 63
KEYCODE_EXPLORER = 64
KEYCODE_ENVELOPE = 65
KEYCODE_ENTER = 66
KEYCODE_DEL = 67
KEYCODE_GRAVE = 68
KEYCODE_MINUS = 69
KEYCODE_EQUALS = 70
KEYCODE_LEFT_BRACKET = 71
KEYCODE_RIGHT_BRACKET = 72
KEYCODE_BACKSLASH = 73
KEYCODE_SEMICOLON = 74
KEYCODE_APOSTROPHE = 75
KEYCODE_SLASH = 76
KEYCODE_AT = 77
KEYCODE_NUM = 78
KEYCODE_HEADSETHOOK = 79
KEYCODE_PLUS = 81
KEYCODE_MENU = 82
KEYCODE_NOTIFICATION = 83
KEYCODE_SEARCH = 84
KEYCODE_MEDIA_PLAY_PAUSE = 85
KEYCODE_MEDIA_STOP = 86
KEYCODE_MEDIA_NEXT = 87
KEYCODE_MEDIA_PREVIOUS = 88
KEYCODE_MEDIA_REWIND = 89
KEYCODE_MEDIA_FAST_FORWARD = 90
KEYCODE_MUTE = 91
KEYCODE_PAGE_UP = 92
KEYCODE_PAGE_DOWN = 93
KEYCODE_BUTTON_A = 96
KEYCODE_BUTTON_B = 97
KEYCODE_BUTTON_C = 98
KEYCODE_BUTTON_X = 99
KEYCODE_BUTTON_Y = 100
KEYCODE_BUTTON_Z = 101
KEYCODE_BUTTON_L1 = 102
KEYCODE_BUTTON_R1 = 103
KEYCODE_BUTTON_L2 = 104
KEYCODE_BUTTON_R2 = 105
KEYCODE_BUTTON_THUMBL = 106
KEYCODE_BUTTON_THUMBR = 107
KEYCODE_BUTTON_START = 108
KEYCODE_BUTTON_SELECT = 109
KEYCODE_BUTTON_MODE = 110
KEYCODE_ESCAPE = 111
KEYCODE_FORWARD_DEL = 112
KEYCODE_CTRL_LEFT = 113
KEYCODE_CTRL_RIGHT = 114
KEYCODE_CAPS_LOCK = 115
KEYCODE_SCROLL_LOCK = 116
KEYCODE_META_LEFT = 117
KEYCODE_META_RIGHT = 118
KEYCODE_FUNCTION = 119
KEYCODE_SYSRQ = 120
KEYCODE_BREAK = 121
KEYCODE_MOVE_HOME = 122
KEYCODE_MOVE_END = 123
KEYCODE_INSERT = 124
KEYCODE_FORWARD = 125
KEYCODE_MEDIA_PLAY = 126
KEYCODE_MEDIA_PAUSE = 127
KEYCODE_MEDIA_CLOSE = 128
KEYCODE_MEDIA_EJECT = 129
KEYCODE_MEDIA_RECORD = 130
KEYCODE_F1 = 131
KEYCODE_F2 = 132
KEYCODE_F3 = 133
KEYCODE_F4 = 134
KEYCODE_F5 = 135
KEYCODE_F6 = 136
KEYCODE_F7 = 137
KEYCODE_F8 = 138
KEYCODE_F9 = 139
KEYCODE_F10 = 140
KEYCODE_F11 = 141
KEYCODE_F12 = 142
KEYCODE_NUM_LOCK = 143
KEYCODE_NUMPAD_0 = 144
KEYCODE_NUMPAD_1 = 145
KEYCODE_NUMPAD_2 = 146
KEYCODE_NUMPAD_3 = 147
KEYCODE_NUMPAD_4 = 148
KEYCODE_NUMPAD_5 = 149
KEYCODE_NUMPAD_6 = 150
KEYCODE_NUMPAD_7 = 151
KEYCODE_NUMPAD_8 = 152
KEYCODE_NUMPAD_9 = 153
KEYCODE_NUMPAD_DIVIDE = 154
KEYCODE_NUMPAD_MULTIPLY = 155
KEYCODE_NUMPAD_SUBTRACT = 156
KEYCODE_NUMPAD_ADD = 157
KEYCODE_NUMPAD_DOT = 158
KEYCODE_NUMPAD_COMMA = 159
KEYCODE_NUMPAD_ENTER = 160
KEYCODE_NUMPAD_EQUALS = 161
KEYCODE_NUMPAD_LEFT_PAREN = 162
KEYCODE_NUMPAD_RIGHT_PAREN = 163
KEYCODE_VOLUME_MUTE = 164
KEYCODE_INFO = 165
KEYCODE_CHANNEL_UP = 166
KEYCODE_CHANNEL_DOWN = 167
KEYCODE_ZOOM_IN = 168
KEYCODE_ZOOM_OUT = 169
KEYCODE_TV = 170
KEYCODE_WINDOW = 171
KEYCODE_GUIDE = 172
KEYCODE_DVR = 173
KEYCODE_BOOKMARK = 174
KEYCODE_CAPTIONS = 175
KEYCODE_SETTINGS = 176
KEYCODE_TV_POWER = 177
KEYCODE_TV_INPUT = 178
KEYCODE_STB_POWER = 179
KEYCODE_STB_INPUT = 180
KEYCODE_AVR_POWER = 181
KEYCODE_AVR_INPUT = 182
KEYCODE_PROG_RED = 183
KEYCODE_PROG_GREEN = 184
KEYCODE_PROG_YELLOW = 185
KEYCODE_PROG_BLUE = 186
KEYCODE_APP_SWITCH = 187
KEYCODE_BUTTON_1 = 188
KEYCODE_BUTTON_2 = 189
KEYCODE_BUTTON_3 = 190
KEYCODE_BUTTON_4 = 191
KEYCODE_BUTTON_5 = 192
KEYCODE_BUTTON_6 = 193
KEYCODE_BUTTON_7 = 194
KEYCODE_BUTTON_8 = 195
KEYCODE_BUTTON_9 = 196
KEYCODE_BUTTON_10 = 197
KEYCODE_BUTTON_11 = 198
KEYCODE_BUTTON_12 = 199
KEYCODE_BUTTON_13 = 200
KEYCODE_BUTTON_14 = 201
KEYCODE_BUTTON_15 = 202
KEYCODE_BUTTON_16 = 203
KEYCODE_LANGUAGE_SWITCH = 204
KEYCODE_MANNER_MODE = 205
KEYCODE_3D_MODE = 206
KEYCODE_CONTACTS = 207
KEYCODE_CALENDAR = 208
KEYCODE_MUSIC = 209
KEYCODE_CALCULATOR = 210
KEYCODE_ZENKAKU_HANKAKU = 211
KEYCODE_EISU = 212
KEYCODE_MUHENKAN = 213
KEYCODE_HENKAN = 214
KEYCODE_KATAKANA_HIRAGANA = 215
KEYCODE_YEN = 216
KEYCODE_RO = 217
KEYCODE_KANA = 218
KEYCODE_ASSIST = 219
KEYCODE_BRIGHTNESS_DOWN = 220
KEYCODE_BRIGHTNESS_UP = 221
KEYCODE_MEDIA_AUDIO_TRACK = 222
KEYCODE_SLEEP = 223
KEYCODE_WAKEUP = 224
KEYCODE_PAIRING = 225
KEYCODE_MEDIA_TOP_MENU = 226
KEYCODE_11 = 227
KEYCODE_12 = 228
KEYCODE_LAST_CHANNEL = 229
KEYCODE_TV_DATA_SERVICE = 230
KEYCODE_VOICE_ASSIST = 231
KEYCODE_TV_RADIO_SERVICE = 232
KEYCODE_TV_TELETEXT = 233
KEYCODE_TV_NUMBER_ENTRY = 234
KEYCODE_TV_TERRESTRIAL_ANALOG = 235
KEYCODE_TV_TERRESTRIAL_DIGITAL = 236
KEYCODE_TV_SATELLITE = 237
KEYCODE_TV_SATELLITE_BS = 238
KEYCODE_TV_SATELLITE_CS = 239
KEYCODE_TV_SATELLITE_SERVICE = 240
KEYCODE_TV_NETWORK = 241
KEYCODE_TV_ANTENNA_CABLE = 242
KEYCODE_TV_INPUT_HDMI_1 = 243
KEYCODE_TV_INPUT_HDMI_2 = 244
KEYCODE_TV_INPUT_HDMI_3 = 245
KEYCODE_TV_INPUT_HDMI_4 = 246
KEYCODE_TV_INPUT_COMPOSITE_1 = 247
KEYCODE_TV_INPUT_COMPOSITE_2 = 248
KEYCODE_TV_INPUT_COMPONENT_1 = 249
KEYCODE_TV_INPUT_COMPONENT_2 = 250
KEYCODE_TV_INPUT_VGA_1 = 251
KEYCODE_TV_AUDIO_DESCRIPTION = 252
KEYCODE_TV_AUDIO_DESCRIPTION_MIX_UP = 253
KEYCODE_TV_AUDIO_DESCRIPTION_MIX_DOWN = 254
KEYCODE_TV_ZOOM_MODE = 255
KEYCODE_TV_CONTENTS_MENU = 256
KEYCODE_TV_MEDIA_CONTEXT_MENU = 257
KEYCODE_TV_TIMER_PROGRAMMING = 258
KEYCODE_HELP = 259
KEYCODE_NAVIGATE_PREVIOUS = 260
KEYCODE_NAVIGATE_NEXT = 261
KEYCODE_NAVIGATE_IN = 262
KEYCODE_NAVIGATE_OUT = 263
KEYCODE_STEM_PRIMARY = 264
KEYCODE_STEM_1 = 265
KEYCODE_STEM_2 = 266
KEYCODE_STEM_3 = 267
KEYCODE_DPAD_UP_LEFT = 268
KEYCODE_DPAD_DOWN_LEFT = 269
KEYCODE_DPAD_UP_RIGHT = 270
KEYCODE_DPAD_DOWN_RIGHT = 271
KEYCODE_MEDIA_SKIP_FORWARD = 272
KEYCODE_MEDIA_SKIP_BACKWARD = 273
KEYCODE_MEDIA_STEP_FORWARD = 274
KEYCODE_MEDIA_STEP_BACKWARD = 275
KEYCODE_SOFT_SLEEP = 276
KEYCODE_CUT = 277
KEYCODE_COPY = 278
KEYCODE_PASTE = 279
KEYCODE_SYSTEM_NAVIGATION_UP = 280
KEYCODE_SYSTEM_NAVIGATION_DOWN = 281
KEYCODE_SYSTEM_NAVIGATION_LEFT = 282
KEYCODE_SYSTEM_NAVIGATION_RIGHT = 283
KEYCODE_KEYCODE_ALL_APPS = 284
KEYCODE_KEYCODE_REFRESH = 285
KEYCODE_KEYCODE_THUMBS_UP = 286
KEYCODE_KEYCODE_THUMBS_DOWN = 287

# Event
EVENT_INIT = "init"
EVENT_FRAME = "frame"
EVENT_CHANGE = "change"
EVENT_DISCONNECT = "disconnect"

# Type
TYPE_INJECT_KEYCODE = 0
TYPE_INJECT_TEXT = 1
TYPE_INJECT_TOUCH_EVENT = 2
TYPE_INJECT_SCROLL_EVENT = 3
TYPE_BACK_OR_SCREEN_ON = 4
TYPE_EXPAND_NOTIFICATION_PANEL = 5
TYPE_EXPAND_SETTINGS_PANEL = 6
TYPE_COLLAPSE_PANELS = 7
TYPE_GET_CLIPBOARD = 8
TYPE_SET_CLIPBOARD = 9
TYPE_SET_SCREEN_POWER_MODE = 10
TYPE_ROTATE_DEVICE = 11

# Lock screen orientation
LOCK_SCREEN_ORIENTATION_UNLOCKED = -1
LOCK_SCREEN_ORIENTATION_INITIAL = -2
LOCK_SCREEN_ORIENTATION_0 = 0
LOCK_SCREEN_ORIENTATION_1 = 1
LOCK_SCREEN_ORIENTATION_2 = 2
LOCK_SCREEN_ORIENTATION_3 = 3

# Screen power mode
POWER_MODE_OFF = 0
POWER_MODE_NORMAL = 2
