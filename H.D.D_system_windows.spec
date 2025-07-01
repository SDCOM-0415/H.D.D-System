# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['Main.PY'],
    pathex=[],
    binaries=[],
    datas=[
        ('*.png', '.'),
        ('*.mp3', '.'),
        ('*.wav', '.'),
        ('*.ttf', '.'),
        ('Icon.ico', '.'),
        ('*.py', '.')
    ],
    hiddenimports=['sip', 'PyQt5.sip'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher
)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='H.D.D-System-Windows',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='Icon.ico',
    onefile=True,
    runtime_tmpdir=None,
    include_python_dll=True,
    python_dll_name='python39.dll'
)