About
=====

DotSublime is aimed to quick deploy sublime text 3(ST3) settings when newly installed ST3.

Installation
============

1. Download and install ST3 in your way. (ubuntu for example)

```sh
sudo add-apt-repository ppa:webupd8team/sublime-text-3
sudo apt-get update
sudo apt-get install sublime-text-installer
```

2. Fetch my default configure and custom yourself.

```sh
cd ~/.config
git clone https://github.com/quchunguang/dotsublime.git sublime-text-3
cd sublime-text-3 # and change what you like
```

3. Install package control. (strongly recommend)

Run ST3, press ctrl+` to show console. then paste following code and return to run.

```python
import urllib.request,os,hashlib; h = '7183a2d3e96f11eeadd761d777e62404' + 'e330c659d4bb41d3bdf022e94cab3cd0'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
```

4. Install some useful packages via package control for ST3.

Run ST3, press ctrl+shift+p to show command window. input 'ip' (which means install package) and return.
Following are my favorites,

* AutoPEP8
* Clickable URLs
* Generate Password
* GenerateUUID
* Pandown
* SideBarEnhancements
* GoSublime
* HTML-JS-CSS Prettify

