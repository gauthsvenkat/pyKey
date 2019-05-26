from distutils.core import setup
setup(
  name = 'pyWinKey',         
  packages = ['pyWinKey'],  
  version = '0.1',      
  license='MIT',        
  description = 'A python wrapper for the windows SendInput function to synthesize keystrokes',
  author = 'Gautham',
  author_email = 'gauthsvenkat@gmail.com',
  url = 'https://github.com/andohuman',
  download_url = 'https://github.com/andohuman/pyWinKey/archive/v_01.tar.gz',
  keywords = ['keyboard', 'simulate', 'keypress', 'scancodes'],
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)