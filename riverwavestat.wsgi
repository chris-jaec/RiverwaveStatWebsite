activate_this = '/var/www/html/riverwavestat/riverwavestat/bin/activate_this.py'
exec(open(activate_this).read(), dict(__file__=activate_this))
import sys
sys.path.insert(0, '/var/www/html/riverwavestat')
from riverwavestat import app as application