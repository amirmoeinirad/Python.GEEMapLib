
# Amir Moeini Rad
# October 2025


# Main Concept: Connecting to Google Earth Engine (GEE) data repository


# ----------------------------------------------------- #
# Packages                                              #
# ----------------------------------------------------- #


# > pip install geemap
# The Earth Engine API. It lets you communicate directly with Google Earth Engine’s huge cloud datasets.
import ee
# A Python library that acts as a bridge between Google Earth Engine and Python.
# It works on top of 'ee' and provides visualization capabilities.
import geemap
# Make sure that 'geemap' and 'earthengine-api' versions are compatible.
# -->> The version that works for me: earthengine-api=1.0.0 & gemap=0.3.0 <<--

# > pip install httplib2
# A Python HTTP client library that handles various HTTP features like caching, authentication, and redirects.
from httplib2 import Http, ProxyInfo

# > pip install pysocks
# A SOCKS proxy client that allows Python's socket module to direct traffic through a SOCKS proxy server.
import socks


# ----------------------------------------------------- #
# Google Service Account                                #
# ----------------------------------------------------- #


# A file containing your Google Service Account credentials.
# You must download your own from the Google Cloud Console > Service Accounts section.
key_file = "your-file.json"

# Your Google Service Account email
# It's available in your Google Cloud Console > Service Accounts section.
service_account = "your-sevrice-account-email"

# Your complete Service Account credentials
credentials = ee.ServiceAccountCredentials(service_account, key_file)


# ----------------------------------------------------- #
# Proxy Settings                                        #
# ----------------------------------------------------- #


# You must set the following options if you are using a proxy on your network.
PROXY_HOST = "127.0.0.1"              # The hostname or IP
PROXY_PORT = 50347                    # The port number
PROXY_TYPE = socks.PROXY_TYPE_HTTP   # Most corporate proxies are HTTP or SOCKS5

proxy_info = ProxyInfo(
    proxy_type=PROXY_TYPE,
    proxy_host=PROXY_HOST,
    proxy_port=PROXY_PORT
    # Add proxy_user='user' and proxy_pass='password' if required
)

# The httplib2 transport object will use the proxy
http_transport = Http(proxy_info=proxy_info)


# ----------------------------------------------------- #
# Main App                                              #
# ----------------------------------------------------- #


print("\nEE Library Version: " + ee.__version__)
print("GEEMap Library Version: " + geemap.__version__)


# This line asks you for your Google Earth Engine account information.
# However, since it is likely to throw errors, we used the Google Service Account.
# ee.Authenticate()


# initialize the GEE API
# This line connects the Python environment to your Google Earth Engine account.
ee.Initialize(credentials, project='your-project-ID', http_transport=http_transport)
print("\nConnected successfully to Google Earth Engine (GEE) using the Google Service Account.")


# Initialize the map
# Create an interactive map centered on Tehran
Map = geemap.Map(center=[35.6892, 51.3890], zoom=8)
print("\nMap initialized successfully.")


print("\nDone")
