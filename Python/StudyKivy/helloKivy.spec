# -*- mode: python -*-
from wolframclient.evaluation import WolframLanguageSession 
from wolframclient.language import wl,wlexpr
block_cipher = None


a = Analysis(['helloKivy.py'],
             pathex=['E:\\Python\\Projects\\StudyKivy'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='HelloKivy',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,Tree('E:\\Python\\Projects\\StudyKivy'),
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='HelloKivy')
