import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

# Main window class for the application
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        # Create the browser widget and set the initial page
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))

        # Set the browser as the central widget
        self.setCentralWidget(self.browser)
        
        # Create a toolbar for navigation
        navtb = QToolBar()
        self.addToolBar(navtb)

        # Add a 'Back' button to the toolbar
        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.browser.back)
        navtb.addAction(back_btn)

        # Add a 'Next' button to the toolbar
        next_btn = QAction("Next", self)
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)

        # Add a 'Reload' button to the toolbar
        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        # Create a URL bar for inputting addresses
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)

        # Show the main window
        self.show()

        # Update the URL bar when the browser URL changes
        self.browser.urlChanged.connect(self.update_urlbar)

        # Update the window title when the page finishes loading
        self.browser.loadFinished.connect(self.update_title)

    # Update the window title to the current page title
    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("%s - Your Browser Name" % title)

    # Navigate to the URL entered in the URL bar
    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("https")
        self.browser.setUrl(q)

    # Update the URL bar to the current URL
    def update_urlbar(self, q):
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

# Create the application instance
app = QApplication(sys.argv)
# Create the main window
window = MainWindow()
# Start the event loop
app.exec_()
