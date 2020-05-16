import platform
ttk_theme = "xpnative"
if platform.platform().startswith('Linux'):
    print('Linux detected')
    ttk_theme = "plastik"
